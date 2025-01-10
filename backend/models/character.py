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