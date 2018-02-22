# HtrA1 Diffuse Scattering Simulations
Setting up simulations of HtrA1 for Diffuse Scattering

# Getting started
These simulations utilize the PDB structure 3NUM, the apo strucure of the HtrA1 active site from Truebestein et al., *Nat Struct. & Mol. Bio.* (**2011**). The original structure is missing two loop regions (resid 285 to 289, and 301 to 314, respectively), which were filled in using [PDBFixer](https://github.com/pandegroup/pdbfixer), which also filled in heavy atoms. This structure was fed in to the [PDB2PQR Server](http://nbcr-222.ucsd.edu/pdb2pqr_2.1.1/), which was used to generate the correct AMBER residue types and assign the correct protonation states (which, given the experimental conditions from the Truebenstein et al. crystallization, were assigned at pH 5.6). Explicit hydrogens were added, and connectivity and bond order information was processed using OpenEye Tools. The "Structure Editing > Model/Refine Loops" feature in Chimera Tools was used to generate loop configurations for the loop regions missing from the original structure. The three loop configurations with the lowest zDOPE scores were selected as the starting structures for the supercell construction.

The `CRYST1` information from the original PDB file was added back in to the top of the newly generated starting structures, and AMBER's `UnitCell` and `PropPDB` were used to generate the Unit Cell and Supercell structures, respectively (in this study, we generated 2x2x2 supercells).

Ions and solute were generated using Open Eye Tools, and prepared using AMBER's `tleap`. The ions were then added to the supercells in numbers determined by their concentrations in the literature. Waters were prepared and added in the same way.

More detailed information on the supercell preparation process can be found in the `HtrA1 Setup Notebook` jupyter notebook.

The `*.X.sh` files are the input files used to submit the scripts for running on a SLURM cluster.
