# counts2bin
A script to get from Orthogroups.GeneCount.tsv to a gene presence/absence binary alignment.


Arguments
  -i filename     file w/ gene counts (from OrthoFinder output)
  -o filename     directory to write the output file(s)
  -incl filename  file w/ species. Analyze these species only
  -excl filename  file w/ species. Remove these species from analysis
  -tsv            creates tsv file
  -phylip         creates PHYLIP alignment file
  -fasta          creates FASTA alignment file



Who 
 Paschalis Natsidis, PhD candidate (p.natsidis@ucl.ac.uk); 
 
Where 
 Telford Lab, UCL;
 ITN IGNITE; 
  
When
 May 2019; 
