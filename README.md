# orthocounts2bin
A script to get from Orthogroups.GeneCount.tsv to a gene presence/absence binary alignment. This aligment can be used to construct phylogenies based on gene content.
<br> 
<br> 
<br> 
## Input arguments
Argument    |  Description             
:-------------:|:-----------------------
-i filename | file w/ gene counts (from OrthoFinder output)
-o filename | directory to write the output file(s)
-incl filename | file w/ species. Analyze these species only
-excl filename | file w/ species. Remove these species from analysis
-tsv | creates tsv file
-phylip | creates PHYLIP alignment file
-fasta | creates FASTA alignment file
<br> 
<br>  
 
## Example usage

```
python orthocounts2bin.py -i Orthogroups.GeneCounts.tsv -o ./counts_dir/ -tsv -fasta
```
 
<br>
Who<br> 
 Paschalis Natsidis, PhD candidate (p.natsidis@ucl.ac.uk); <br>
<br>
Where<br>
 Telford Lab, UCL;<br>
 ITN IGNITE; 
<br>
<br>
When<br> 
 May 2019; 
