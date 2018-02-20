import numpy as np
from decimal import *

getcontext().prec = 20

with open("citrate_fixed_charges.gaff.mol2") as mol2:
    lines = mol2.readlines()
    line_vec = [line for line in lines]
    tot_charge=0
    for i in range(8,27):
        #tot_charge += float(line_vec[i].split()[-1])
        tot_charge += Decimal(line_vec[i].split()[-1])

    #tot_charge = round(tot_charge,8)
    smear = Decimal(-2)-tot_charge
    print(tot_charge, smear)
    add_to_each = round(smear/19, 6)
    #add_to_each = Decimal(add_to_each)
    print(add_to_each)
    new_tot_charge = 0
    print("Calculating new total charge")
    for i in range(8,27):
        old_charge_str = line_vec[i][-1-len(line_vec[i].split()[-1]):-1]
        old_charge = Decimal(old_charge_str)
        print(len(old_charge_str))
        new_charge = old_charge + add_to_each
        print(new_charge)
        new_tot_charge += new_charge
        line_vec[i] = line_vec[i].replace(old_charge_str, str(new_charge))
        print(line_vec[i])
    print("New total charge")
    print(new_tot_charge)
    off_by = Decimal(-2)-new_tot_charge
    print("Off by: {}".format(off_by))
    with open("test.mol2", 'w') as new_file:
        for line in line_vec:
            new_file.write(line)

