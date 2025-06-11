import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
APPOINTMENTS_FILE = os.path.join(DATA_DIR, 'appointments.json')

def load_users():
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_appointments():
    with open(APPOINTMENTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_appointments(appointments):
    with open(APPOINTMENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(appointments, f, ensure_ascii=False, indent=4)
