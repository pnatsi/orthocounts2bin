# orthocounts2bin
A script that creates a binary gene presence/absence alignment from Orthogroups.GeneCounts.tsv <br>
This aligment can be used to construct phylogenies based on gene content.
<br> 
<br>  
## Arguments
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
 
## Example usage

```
python orthocounts2bin.py -i /Users/pnatsi/orthology/Orthogroups.GeneCounts.tsv -o /Users/pnatsi/orthology/ -tsv -fasta
```
 
**Careful! Only full paths to the input files are currently supported**
 
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
