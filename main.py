# Make the AI Judge Feel Nostalgic: A Childhood Memory (Python 3.13, standard library only).
# Writes one childhood-memory sentence to /output/entry.txt. Deterministic:
# the same fixed line on every run, no clock, no randomness, no network,
# no model call.
# Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# One sentence, at most 280 characters, recalling a childhood memory. The
# nostalgia sits in small, exact, honest details rather than announced
# sentiment: a grandmother serving rice from a steaming pot, a tin plate, a
# child eating cross-legged on the cool kitchen floor, evening rain drumming
# on the zinc roof. A concrete place, a concrete time, a concrete sensation,
# and a warm ache that lingers after the sentence ends. The line is fixed
# on purpose: the judge compares exact texts, so a program that invents a
# new line on every run would gamble the entry on chance.
ENTRY = (
    "Grandmother spooned rice straight from the steaming pot onto my tin "
    "plate, and I ate cross-legged on the cool kitchen floor while evening "
    "rain drummed softly on the zinc roof above us."
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
assert 1 <= len(ENTRY) <= 280, "entry must be 1-280 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be a single sentence"
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
