
from datetime import datetime
from pathlib import Path
import json

DATA = Path(__file__).parent / "data"

def grade_from_percent(percent):
    if percent >= 90: return "A+"
    if percent >= 80: return "A"
    if percent >= 70: return "B"
    if percent >= 60: return "C"
    return "D"

def save_score(topic, score, total):
    DATA.mkdir(exist_ok=True)
    with open(DATA/'scores.txt','a',encoding='utf-8') as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M} | {topic} | {score}/{total}\n")

def cgpa_classification(cgpa):
    if cgpa >= 9: return "Outstanding"
    if cgpa >= 8: return "Distinction"
    if cgpa >= 7: return "First Class"
    if cgpa >= 6: return "Second Class"
    return "Pass"
