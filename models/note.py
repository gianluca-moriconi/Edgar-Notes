from datetime import datetime
import uuid

class Note:
    def __init__(self, title, content, note_id=None, timestamp=None):
        self.id = note_id or str(uuid.uuid4())
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp
        }
