from openeye.oechem import *
from openeye.oeomega import *
from openeye.oeiupac import *
from openeye.oeshape import *
from openeye.oequacpac import *

mol = OEMol()
OESmilesToMol(mol, "[NH4+]")
#OEAddExplicitHydrogens(mol)

omega = OEOmega()
omega.SetMaxConfs(1)
omega.SetStrictStereo(False)
omega.SetStrictAtomTypes(False)
omega(mol)
#OEDetermineConnectivity(mol)
OEAssignCharges(mol, OEAM1BCCCharges())

mol.SetTitle("Ammonium")

ostream = oemolostream("ammonium.mol2")
OEWriteMolecule(ostream, mol)
ostream = oemolostream("ammonium.pdb")
OEWriteMolecule(ostream, mol)
