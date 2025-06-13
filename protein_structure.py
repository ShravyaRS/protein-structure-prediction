import os
import sys
import requests
from Bio import PDB
from collections import Counter

def download_pdb(protein_id, save_dir="data/input_sequences"):
    """Download a PDB file from RCSB and save it."""
    os.makedirs(save_dir, exist_ok=True)
    url = f"https://files.rcsb.org/download/{protein_id}.pdb"
    response = requests.get(url)

    if response.status_code == 200:
        file_path = os.path.join(save_dir, f"{protein_id}.pdb")
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Downloaded {protein_id}.pdb successfully!")
        return file_path
    else:
        print(f"❌ Error downloading {protein_id} from RCSB.")
        return None

def parse_pdb(protein_id, file_path):
    """Parse the PDB structure and print summary stats."""
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure(protein_id, file_path)
    model = structure[0]

    chains = list(model.get_chains())
    residues = [res for res in model.get_residues() if PDB.is_aa(res)]

    aa_counter = Counter(res.get_resname() for res in residues)

    print(f"\n🔬 Structure Summary for {protein_id}")
    print(f"🔹 Chains Found: {len(chains)}")
    print(f"🔹 Total Residues: {len(residues)}")
    print("🔹 Amino Acid Composition:")
    for aa, count in aa_counter.items():
        print(f"   - {aa}: {count}")

    return structure, residues

def main():
    # Accept command-line argument or input
    if len(sys.argv) > 1:
        protein_id = sys.argv[1].strip().upper()
    else:
        protein_id = input("Enter Protein PDB ID (e.g., 1HHO): ").strip().upper()

    file_path = download_pdb(protein_id)
    if file_path:
        parse_pdb(protein_id, file_path)

if __name__ == "__main__":
    main()
