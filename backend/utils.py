import sqlite3
from datetime import datetime

# Database connection function

def get_db_connection():
    conn = sqlite3.connect('backend/database/ascendants_path.db')
    conn.row_factory = sqlite3.Row #get results as dictionaries
    return conn

# Create Character Model Class
class Character:
    def __init__(self, id, name, level_id, experience, strenght, agility, inteligence, endurance, perception):
        self.id = id
        self.name = name
        self.level_id = level_id
        self.experience = experience
        self.strenght = strenght
        self.agility = agility
        self.inteligence = inteligence
        self.endurance = endurance
        self.percepction = perception

def to_dict(self):
    return self.__dict__

# Create Quest Model Class
class Quest:
    def __init__(self, character_id, quest_id, is_complited=0):
        self.character_id = character_id
        self.quest_id = quest_id
        self.is_complited = is_complited

    def to_dict(self):
        return self.__dict__
    
class CharacterQuests:
    def __init__(self, character_id, quest_id, is_complited=0):
        self.character_id = character_id
        self.quest_id = quest_id
        self.is_complited = is_complited

    def to_dict(self):
        return self.__dict__
    
# Create a new character
def create_character(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Characters (name) VALUES (?)", (name,))
    conn.commit()
    character_id = cursor.lastrowid
    conn.close()
    return character_id

# Get a character by id
def get_character(character_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Characters WHERE id = ?", (character_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        character = Character(row['id'], row['name'], row['level_id'], row['experience'], row['strenght'], row['agility'], row['intelligence'], row['endurance'], row['perception'])
        return character
    return None

# Create a new quest
def create_quest(title, description, experience_reward, type, deadline):
    conn = get_db_connection()
    cursor = conn.cursor()
    now =datetime.now()
    cursor.execute("INSERT INTO Quests (title, description, experience_reward, type, deadline, creation_date) VALUES (?,?,?,?,?,?)", (title, description, experience_reward, type, deadline, now))
    conn.commit()
    quest_id = cursor.lastrowid
    conn.close()
    return quest_id

# Get quest, optionally filtered by type
def get_quests(type=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if type:
        cursor.execute("SELECT * FROM Quests WHERE type = ?", (type,))
    else:
        cursor.execute("SELECT * FROM Quests")
    rows = cursor. fetchall()
    conn.close()
    quests = []
    for row in rows:
        quest = Quest(row['id'], row['title'], row['description'], row['experience_reward'], row['type'], row['deadline'], row['creation_date'], row['is_completed'])
        quests.append(quest)
    return quests

def get_all_quests():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Quests")
    rows = cursor.fetchall()
    conn.close()
    quests = []
    for row in rows:
        quest = Quest(row['id'], row['title'], row['description'], row['experience_reward'], row['type'], row['deadline'], row['creation_date'], row['is_completed'])
        quests.append(quest)
    return quests

# Create a relationship between a character and a quest
def create_character_quest(character_id, quest_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO CharacterQuests (character_id, quest_id, VALUES (?, ?)", (character_id, quest_id))
    conn.commit()
    conn.close()

def complete_quest(character_id, quest_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE CharaceterQuests SET is_completed = 1 WHERE charater_id = ? AND quest_id = ?", (character_id, quest_id))
    conn.commit()
    conn.close()


def get_character_quests(character_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SLECT * FROM CharacterQuests WHERE chracter_id = ?", (character_id,))
    rows = cursor.fetchall()
    conn.close()
    character_quests = []
    for row in rows:
        character_quest = CharacterQuests(row['character_id'], row['quest_id'], row['is_complited'])
        character_quests.append(character_quest)
    return character_quests
