#!/usr/bin/env python3
"""
generate_students_csv.py

Generates a realistic-looking CSV with 500 students and two subject scores (0-100).
Usage:
    python3 scripts/generate_students_csv.py --out data/students_500.csv --seed 42

This script is deterministic when a seed is provided (default seed=42).
It creates the output directory if needed.
"""
import csv
import os
import random
import argparse

FIRST_NAMES = [
    "James","Mary","John","Patricia","Robert","Jennifer","Michael","Linda",
    "William","Elizabeth","David","Barbara","Richard","Susan","Joseph","Jessica",
    "Thomas","Sarah","Charles","Karen","Christopher","Nancy","Daniel","Lisa",
    "Matthew","Betty","Anthony","Margaret","Mark","Sandra","Donald","Ashley",
    "Steven","Kimberly","Paul","Emily","Andrew","Donna","Joshua","Michelle",
    "Kenneth","Carol","Kevin","Amanda","Brian","Dorothy","George","Melissa",
    "Edward","Deborah"
]

LAST_NAMES = [
    "Smith","Johnson","Williams","Brown","Jones","Miller","Davis","Garcia","Rodriguez","Wilson"
]


def clamp(x, lo=0, hi=100):
    return max(lo, min(hi, int(round(x))))


def generate_students(n=500, seed=42):
    random.seed(seed)
    students = []

    # Create 500 distinct realistic names by pairing first and last names (50 x 10 = 500)
    names = []
    for i in range(len(FIRST_NAMES)):
        for j in range(len(LAST_NAMES)):
            names.append(f"{FIRST_NAMES[i]} {LAST_NAMES[j]}")
    # If more than needed, trim; if less, repeat with middle initial
    if len(names) < n:
        # fallback: add middle initials
        idx = 0
        while len(names) < n:
            fi = FIRST_NAMES[idx % len(FIRST_NAMES)]
            la = LAST_NAMES[idx % len(LAST_NAMES)]
            mi = chr(ord('A') + (idx % 26))
            names.append(f"{fi} {mi}. {la}")
            idx += 1
    names = names[:n]

    # Generate scores: realistic distribution using Gaussian and a mild correlation between subjects
    for i, name in enumerate(names):
        # Base ability sampled from normal around 72 with sd 12
        base = random.gauss(72, 12)
        # Subject A score around base with small noise
        a = clamp(base + random.gauss(0, 8))
        # Subject B correlated with A but with independent noise
        b = clamp(a + random.gauss(-2, 10))
        students.append((name, a, b))
    return students


def write_csv(students, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "SubjectA", "SubjectB"])
        for name, a, b in students:
            writer.writerow([name, a, b])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='data/students_500.csv', help='Output CSV path')
    parser.add_argument('--n', type=int, default=500, help='Number of students')
    parser.add_argument('--seed', type=int, default=42, help='Random seed for reproducibility')
    args = parser.parse_args()

    students = generate_students(n=args.n, seed=args.seed)
    write_csv(students, args.out)
    print(f"Wrote {len(students)} students to {args.out} (seed={args.seed})")
