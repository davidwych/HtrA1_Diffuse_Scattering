#!/bin/bash

AddToBox -c 3num_loop_1_SC_LiNaSO4NH4Cit.pdb -a ./water/water.pdb -na 190300 -o 3num_loop_1_SC_solvated.pdb -P 251356 -RP 3.0 -RW 3.0 -G 0.1 -V 1

AddToBox -c 3num_loop_2_SC_LiNaSO4NH4Cit.pdb -a ./water/water.pdb -na 190300 -o 3num_loop_2_SC_solvated.pdb -P 251356 -RP 3.0 -RW 3.0 -G 0.1 -V 1

AddToBox -c 3num_loop_3_SC_LiNaSO4NH4Cit.pdb -a ./water/water.pdb -na 190300 -o 3num_loop_3_SC_solvated.pdb -P 251356 -RP 3.0 -RW 3.0 -G 0.1 -V 1
