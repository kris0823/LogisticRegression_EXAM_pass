import csv
import random
import math

# Reproducible generator for 500 realistic student exam scores
random.seed(2026)

first_names = [
    "James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda",
    "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa", "Matthew"
]

last_names = [
    "Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

num_students = 500
out_path = "exam_scores_500.csv"

rows = []

for idx in range(num_students):
    # Build unique-ish realistic name by combining lists (25 x 20 = 500 unique combos)
    first = first_names[idx % len(first_names)]
    last = last_names[(idx // len(first_names)) % len(last_names)]
    name = f"{first} {last}"

    # Simulate realistic exam scores using a seeded normal distribution and slight correlation
    # Subject A centered ~70, sd ~12
    subj_a = int(round(min(100, max(0, random.gauss(70, 12)))))
    # Subject B correlated with A (rho ~0.6) plus small noise
    noise = random.gauss(0, 8)
    subj_b = int(round(min(100, max(0, 0.6 * subj_a + 0.4 * 70 + noise))))

    rows.append((name, subj_a, subj_b))

# Write CSV
with open(out_path, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "SubjectA", "SubjectB"])
    for r in rows:
        writer.writerow(r)

print(f"Wrote {num_students} rows to {out_path}")
