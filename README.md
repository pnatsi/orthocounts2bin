# counts2bin
A script to get from Orthogroups.GeneCount.tsv to a gene presence/absence binary alignment.


Arguments <br>
  `-i filename`     file w/ gene counts (from OrthoFinder output)<br>
  `-o filename`     directory to write the output file(s)<br>
  `-incl filename`  file w/ species. Analyze these species only<br>
  `-excl filename`  file w/ species. Remove these species from analysis<br>
  `-tsv`            creates tsv file<br>
  `-phylip`         creates PHYLIP alignment file<br>
  `-fasta`          creates FASTA alignment file<br>
<br>


Who 
 Paschalis Natsidis, PhD candidate (p.natsidis@ucl.ac.uk); 
 
Where 
 Telford Lab, UCL;
 ITN IGNITE; 
  
When
 May 2019; 
