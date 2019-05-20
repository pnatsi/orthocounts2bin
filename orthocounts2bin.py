import argparse
from utils import o2bin


#HERE STARTS THE ARGUMENT DEFINING
usage = "A program to convert Orthogroups.GeneCount.tsv to gene presence/absence aligment"
toolname = "orthocounts2bin"
footer = "Who \n Paschalis Natsidis (p.natsidis@ucl.ac.uk); \n \nWhere \n Telford Lab, UCL;\n\
 ITN IGNITE; \n  \nWhen\n May 2019; \n\n"

parser = argparse.ArgumentParser(description = usage, prog = toolname, epilog = footer, formatter_class=argparse.RawDescriptionHelpFormatter,)
parser.add_argument('-i', metavar = 'filename', dest = 'genecounts', required = True,
                    help = 'file w/ gene counts (from OrthoFinder output)')
parser.add_argument('-o', metavar = 'filename', dest = 'output', required = True,
                    help = 'directory to write the output file(s)')

group1 = parser.add_mutually_exclusive_group()
group1.add_argument('-incl', metavar = 'filename', dest = 'include',
                    help = 'file w/ species. Analyze these species only (optional)')
group1.add_argument('-excl',  metavar = 'filename', dest = 'exclude',
                    help = 'file w/ species. Remove these species from analysis (optional)')

parser.add_argument('-tsv', action = 'store_true', dest = 'tsv',
                    help = 'creates tsv file')
parser.add_argument('-phylip', action = 'store_true', dest = 'phylip',
                    help = 'creates PHYLIP alignment file')
parser.add_argument('-fasta', action = 'store_true', dest = 'fasta',
                    help = 'creates FASTA alignment file')

#parser.print_help()

args = parser.parse_args()

#READ FILENAMES FROM USER INPUT
genecounts_file = args.genecounts
exclude_file = args.exclude
include_file = args.include
output_dir = args.output

#LOAD GENECOUNTS DATA
print("Reading the input file(s)...")
f = open(genecounts_file, "r")
lines = f.readlines()
genecounts_df = [x.strip().split("\t") for x in lines]
#A LIST OF THE SPECIES INCLUDED IN THE INPUT FILE
species = genecounts_df[0][:-1]
#A LIST OF THE ORTHOGROUPS INCLUDED IN THE INPUT FILE
orthogroups = [x[:-1] for x in genecounts_df[1:]] 

#SPECIES EXCLUSION/INCLUSION PROCESS
if exclude_file:
    g = open(exclude_file, "r")
    lines = g.readlines()
    species_to_exclude = [x.strip() for x in lines]
    species_excluded = []
    for entry in species_to_exclude:
        if entry in species:
            species_excluded.append(entry)
    print("These species will be excluded: \n", species_excluded)           
     
if include_file:
    h = open(include_file, "r")
    lines = h.readlines()
    species_to_include = [x.strip() for x in lines]
    species_included = []
    for entry in species_to_include:
        if entry in species:
            species_included.append(entry)
    print("These species will be included: \n", species_included)           

#CONVERT THE COUNTS TABLE TO PRESENCE/ABSENCE TABLE
orthogroups_binary = o2bin(orthogroups)

#CREATE TSV FILE
if args.tsv == True:
    print("Creating .tsv file...")
    tsv_filename = output_dir + "test.tsv"
    output_tsv = open(tsv_filename, "w")
    #CREATE HEADER
    for entry in species:
        output_tsv.write(entry + "\t")
    output_tsv.write("\n")
    #CREATE ROWS WITH 0'S AND 1'S FROM ORTHOGROUPS
    for orthoroup in orthogroups_binary:
        for count in orthoroup[1:]:
            output_tsv.write(str(count) + "\t")
        output_tsv.write("\n")
    print("tsv file made!")


#CREATE PHYLIP FILE
if args.phylip == True:
    print("Creating PHYLIP file...")
    phy_filename = output_dir + "test.phy"
    output_phy = open(phy_filename, "w")
    #CREATE HEADER
    if args.exclude == True:
        species_number = len(species) - len(species_excluded)
    elif args.include == True:
        species_number = len(species_included)
    else:
        species_number = len(species)
    output_phy.write(str(species_number) + " " + str(len(orthogroups_binary)) + "\n")
    #CREATE THE BINARY ALIGNMENT
    if args.exclude == True:
        for i in range(len(species)):
            if species[i] not in species_excluded:
                output_phy.write(species[i] + "\t")
                for group in orthogroups_binary:
                    output_phy.write(str(group[i+1]))
                output_phy.write("\n") 
    elif args.include == True:
        for i in range(len(species)):
            if species[i] in species_included:
                output_phy.write(species[i] + "\t")
                for group in orthogroups_binary:
                    output_phy.write(str(group[i+1]))
                output_phy.write("\n")             
    elif args.exclude == False and args.include == False:
        for i in range(len(species)):
            output_phy.write(species[i] + "\t")
            for group in orthogroups_binary:
                output_phy.write(str(group[i+1]))
            output_phy.write("\n") 
    print("PHYLIP file made!")

#CREATE FASTA FILE
if args.fasta == True:
    print("Creating FASTA file...")
    fasta_filename = output_dir + "test.fasta"
    output_fasta = open(fasta_filename, "w")
    #CREATE THE BINARY ALIGNMENT
    if args.exclude == True:
        for i in range(len(species)):
            if species[i] not in species_excluded:
                output_fasta.write(">" + species[i] + "\n")
                for group in orthogroups_binary:
                    output_fasta.write(str(group[i+1]))
                output_fasta.write("\n")
    elif args.include == True:
        for i in range(len(species)):
            if species[i] in species_included:
                output_fasta.write(">" + species[i] + "\n")
                for group in orthogroups_binary:
                    output_fasta.write(str(group[i+1])) 
                output_fasta.write("\n")
    elif args.exclude == False and args.include == False:
        for i in range(len(species)):
            output_fasta.write(">" + species[i] + "\n")
            for group in orthogroups_binary:
                output_fasta.write(str(group[i+1]))
            output_fasta.write("\n")
    print("FASTA file made!")
