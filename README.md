# Protein Structure Prediction and Composition Analysis

A lightweight pipeline to download, parse, and analyze protein structures using their PDB IDs. Built with Biopython, it enables inspection of chain organization and amino acid composition from 3D protein data fetched from RCSB PDB.

## Features

- Downloads `.pdb` files directly from RCSB PDB
- Parses protein structures using Biopython
- Identifies chains and residues in the model
- Computes amino acid composition (e.g., GLY, ALA, LEU counts)
- Works in both command-line and interactive mode

## Usage

Interactive mode:
```bash
python protein_parser.py
```

Command-line mode:
```bash
python protein_parser.py 8WIX
```

## Project Structure
```
protein-structure-prediction/
├── sample_data/
│   └── 8WIX.pdb              Sample structure for testing
├── protein_parser.py          Main Python script
└── README.md
```

## Sample Output
```
Downloaded 8WIX.pdb successfully!
Structure Summary for 8WIX
  Chains Found: 2
  Total Residues: 284
  Amino Acid Composition:
    GLY: 35
    ALA: 20
    LEU: 40
    SER: 18
    ...
```

## Requirements

- Python 3.7+
- Biopython
- requests
```bash
pip install biopython requests
```

## License

MIT License. See [LICENSE](LICENSE) for details.
