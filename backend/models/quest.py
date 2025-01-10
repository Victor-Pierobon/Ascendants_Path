class Quest:
    def __init__(self, id, title, descripton, experience_reward, type, deadline, creation_date, is_completed):
        self.id = id
        self.title = title
        self.description = description
        self.experience_reward = experience_reward
        self.type = type
        self.deadline = deadline
        self.creation_date = creation_date
        self.is_completed = is_completed
    def to_dict(self):
        return self.__dict__
    
