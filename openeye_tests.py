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
OEDetermineConnectivity(mol)
OEAssignPartialCharges(mol, OECharges_AM1BCCNoSym)

mol.SetTitle("Ammonium")

ostream = oemolostream("ammonium_2.mol2")
OEWriteMolecule(ostream, mol)
ostream = oemolostream("ammonium_2.pdb")
OEWriteMolecule(ostream, mol)
