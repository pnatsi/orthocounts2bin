def o2bin(orthogroups):
    # Converts a list with gene counts to a list with 
    # gene presence/absence information
    orthogroups_binary = []
    
    for group in orthogroups:
        binary_repr = []                # this will store the gene p/a info
        binary_repr.append(group[0])    # first add the name of the orthogroup
        for entry in group[1:]: 
            if int(entry) == 0:     
                binary_repr.append(0)   # keep 0's as they are
            else:
                binary_repr.append(1)   # replace any non-zero with 1
        orthogroups_binary.append(binary_repr)    
    return orthogroups_binary
