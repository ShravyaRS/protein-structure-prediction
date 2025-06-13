# 🧬 Protein Structure Prediction and Analysis

This project demonstrates how to **fetch, parse, and analyze protein structures** using their PDB IDs. It utilizes **Biopython** to access structural data from the RCSB Protein Data Bank and extract biologically relevant insights.

---

## 🔧 Features

- 📥 Automated download of `.pdb` files from RCSB
- 📖 Parsing protein structure using Biopython
- 🔍 Extraction of chain and residue-level information
- 📊 Clean and interpretable summary output for quick insights

---

## 🧠 Use Cases

This tool is suitable for:

- 🧪 Exploring the structural composition of proteins  
- 🎯 Preparing PDB input files for modeling/docking  
- ✅ Validating PDB IDs prior to simulation or visualization  
- 📚 Teaching bioinformatics or structural biology basics

---

## 💻 How to Use

```bash
$ python protein_parser.py
Enter Protein PDB ID (e.g., 1HHO): 8WIX
✅ Downloaded 8WIX.pdb successfully!
✅ Parsed structure: 8WIX
🔹 Number of Chains: 2
🔹 Number of Residues: 284

Requirements
Python 3.7 or higher
Biopython
requests

Install dependencies:
pip install biopython requests
Future Improvements
Integration with AlphaFold or Swiss-Model for predicted structures
Mutation simulation and impact analysis on key residues
Functional site detection and ligand-binding annotation
3D visualization support using PyMOL or NGLView

