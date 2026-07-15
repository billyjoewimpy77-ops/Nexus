
# ADGINUS NEXUS - Mycelium v1.0 - Universe Archive
# Founder: William Joseph Lane - Master Builder
# For: Patricia Gail Lane & Cayden Elizabeth Lane - 11/11/11 11th hour
# Mantra: I build worlds!
# Principle: No nesting, no drift. One file can belong to many universes.

from datetime import datetime
from typing import List, Dict
import uuid

FOUNDER = {
    "name": "William Joseph Lane",
    "mantra": "I build worlds!"
}

class MyceliumUniverse:
    def __init__(self, name: str, description: str, tags: List[str] = []):
        self.id = name.lower().replace(" ", "_").replace("/", "_")
        self.name = name
        self.description = description
        self.tags = tags
        self.file_ids = []
        self.created = datetime.now().isoformat()
        self.founder_stamp = FOUNDER["name"]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "tags": self.tags,
            "file_ids": self.file_ids,
            "created": self.created
        }

class MyceliumFile:
    def __init__(self, name: str, content_preview: str = "", universe_ids: List[str] = []):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.content_preview = content_preview
        self.universe_ids = universe_ids
        self.owner = "student"
        self.created = datetime.now().isoformat()

class MyceliumEngine:
    def __init__(self):
        self.universes: Dict[str, MyceliumUniverse] = {}
        self.files: Dict[str, MyceliumFile] = {}
        self.guide = """
        FOLDERS vs UNIVERSES:
        Folders: You bury a file 6 levels deep and forget where it lives. One file, one place.
        Universes: You tag a file to the worlds you're building. One file, many universes.
        """
        self.create_universe("Foundation - ABCs", "Letters, reading, the start of worlds", ["ABCs", "reading", "foundation"])
        self.create_universe("Foundation - 123s", "Numbers, counting, the logic of worlds", ["123s", "math", "foundation"])
        self.create_universe("Foundation - Typing", "Home row, speed, building with hands", ["typing", "foundation"])
        self.create_universe("Talent - Building", "Where student lights up building worlds", ["talent", "building"])

    def create_universe(self, name: str, description: str, tags: List[str] = []):
        uni = MyceliumUniverse(name, description, tags)
        self.universes[uni.id] = uni
        return uni.to_dict()

    def add_file(self, file_name: str, content_preview: str, universe_ids: List[str]):
        f = MyceliumFile(file_name, content_preview, universe_ids)
        self.files[f.id] = f
        for uid in universe_ids:
            if uid in self.universes:
                if f.id not in self.universes[uid].file_ids:
                    self.universes[uid].file_ids.append(f.id)
        return {"file_id": f.id, "name": f.name, "universes": universe_ids}

    def search(self, query: str):
        query = query.lower()
        results = []
        for uni in self.universes.values():
            if query in uni.name.lower() or any(query in t.lower() for t in uni.tags) or query in uni.description.lower():
                results.append(uni.to_dict())
        for f in self.files.values():
            if query in f.name.lower():
                results.append({"type": "file", "id": f.id, "name": f.name, "universes": f.universe_ids})
        return results

    def status(self):
        return {
            "name": "Mycelium",
            "universes": len(self.universes),
            "files": len(self.files),
            "guide": self.guide,
            "founder": FOUNDER
        }

mycelium = MyceliumEngine()

if __name__ == "__main__":
    print(mycelium.status())
    print(mycelium.search("typing")) 
