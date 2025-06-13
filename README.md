# 🧬 Protein Structure Prediction and Composition Analysis

This project offers a simple yet powerful pipeline to **download**, **parse**, and **analyze protein structures** using their PDB IDs. Built with **Biopython**, it enables inspection of chain organization and amino acid composition from real 3D protein data fetched from RCSB PDB.


## 🔧 Features

- 📥 Downloads `.pdb` files directly from RCSB PDB
- 📖 Parses protein structures using Biopython
- 🔬 Identifies chains and residues in the model
- 📊 Computes amino acid composition (e.g., GLY, ALA, LEU counts)
- 🖥️ Works in both command-line and interactive mode


## 🧠 Use Cases

This tool is ideal for:

- 🧪 Learning protein structure basics  
- 🔍 Preprocessing PDB files before docking or simulation  
- 📚 Teaching bioinformatics or structural biology  
- ✅ Validating the integrity of PDB files


## 💻 How to Run

### 🔹 Option 1: Use the built-in interactive mode

```bash
$ python protein_parser.py
Enter Protein PDB ID (e.g., 1HHO): 8WIX

🔹 Option 2: Command-line mode
$ python protein_parser.py 8WIX

Project Structure
Protein-structure-prediction-/
│
├── sample_data/
│   └── 8WIX.pdb              # Sample structure for testing
│
├── protein_parser.py         # Main Python script
└── README.md                 # Project documentation
Sample Output
✅ Downloaded 8WIX.pdb successfully!

🔬 Structure Summary for 8WIX
🔹 Chains Found: 2
🔹 Total Residues: 284
🔹 Amino Acid Composition:
   - GLY: 35
   - ALA: 20
   - LEU: 40
   - SER: 18
   ...

Requirements
Python 3.7+
Biopython
requests

Install dependencies with:
pip install biopython requests

Future Work
Integrate AlphaFold or Swiss-Model support
Add point mutation analysis
Annotate domains or ligand-binding sites
Visualize structure using NGLView, PyMOL, or 3Dmol.js

## 📄 License
This project is licensed under the [MIT License](LICENSE).
