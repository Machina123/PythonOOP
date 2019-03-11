import datetime

class Note:
    
    AUTO_INCREMENT = 0

    def __init__(self, text, tag):
        Note.AUTO_INCREMENT += 1
        self.id = Note.AUTO_INCREMENT
        self.tag = tag
        self.text = text
        self.creation_date = datetime.datetime.now()

    def match(self, needle):
        if (needle in self.tag) or (needle in self.text):
            return True
        else: 
            return False
    
    def __str__(self):
        return f"ID: {self.id}\nCreation date:{self.creation_date}\nTag: {self.tag}\nText: {self.text}"
    

class Notebook:

    def __init__(self):
        self.notes = []
    
    def new_note(self, note):
        self.notes.append(note)
    
    def modify_text(self, note_id, new_text):
        for note in self.notes:
            if note.id == note_id:
                note.text = new_text
                break
    
    def modify_tag(self, note_id, new_tag):
        for note in self.notes:
            if note.id == note_id:
                note.tag = new_tag
                break
    
    def search(self, needle):
        found_notes = []
        for note in self.notes:
            if note.match(needle):
                found_notes.append(note)
        
        return found_notes
    
    