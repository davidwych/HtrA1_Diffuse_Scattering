with open("3num_loop_3_aligned_new_clean_oe.pdb", 'r') as file:
    lines = file.readlines()
    with open("3num_loop_3_aligned_new_clean_oe2.pdb",'w') as newfile:
        for line in lines:
            if line[0:6] == 'ATOM  ':
                old_resid = line[23:26]
                new_resid = int(old_resid) + 160
                new_resid_str = str(new_resid)
                newline = line[:23] + new_resid_str + line[26:]
                newfile.write(newline)
                #print(line)
                #print(newline)
            else:
                newfile.write(line)
        newfile.write('TER    1599      ASP A 369\nMASTER      560    0    0    3   14    0    0    6 1598    1    0   26\nEND')
