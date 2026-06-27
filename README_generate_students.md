README for students CSV generator

This repository now contains a small Python script to generate a realistic-looking CSV of 500 students with two subject scores.

Files added:
- scripts/generate_students_csv.py  (generator script)

Usage:
1. Run the script locally (requires Python 3):

   python3 scripts/generate_students_csv.py --out data/students_500.csv --n 500 --seed 42

2. The script will create data/students_500.csv. The generation is deterministic when a seed is provided.

If you want me to also commit the generated CSV directly into the repository, tell me and I will generate the CSV content here and upload it as data/students_500.csv.
