import sqlite3

def create_database():
    conn = sqlite3.connect('ascendants_path.db')
    cursor = conn.cursor()

    # Create Characters table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Characters (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            level_id INTEGER,
            experience INTEGER DEFAULT 0,
            strength INTEGER DEFAULT 1,
            agility INTEGER DEFAULT 1,
            intelligence INTEGER DEFAULT 1,
            endurance INTEGER DEFAULT 1,
            perception INTEGER DEFAULT 1,
            FOREIGN KEY (level_id) REFERENCES Levels (id)
        )
    ''')

    # Create Levels table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Levels (
            id INTEGER PRIMARY KEY,
            level_number INTEGER NOT NULL,
            required_experience INTEGER NOT NULL
        )
    ''')

    # Create Quests table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Quests (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            experience_reward INTEGER NOT NULL,
            type TEXT NOT NULL CHECK (type IN ('daily', 'normal')) DEFAULT 'normal',
            deadline DATETIME,
            creation_date DATETIME,
            is_completed INTEGER DEFAULT 0
        )
    ''')

     # Create CharacterQuests table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CharacterQuests (
            character_id INTEGER NOT NULL,
            quest_id INTEGER NOT NULL,
            is_completed INTEGER DEFAULT 0,
            PRIMARY KEY (character_id, quest_id),
            FOREIGN KEY (character_id) REFERENCES Characters(id),
            FOREIGN KEY (quest_id) REFERENCES Quests(id)
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database 'ascendants_path.db' created successfully.")