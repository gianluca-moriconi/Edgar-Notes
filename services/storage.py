import json
import os
from models.note import Note

NOTES_FILE = "notes_db.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_note(title, content):
    note = Note(title, content)
    notes = load_notes()
    notes.append(note.to_dict())
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)

def update_note(note_id, title, content):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = title
            note['content'] = content
            break
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)

def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)
