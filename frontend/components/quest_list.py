import flet as ft
from backend.utils import get_quests, complete_quest, create_quest, get_character, create_character_quest, get_character_quests
from datetime import datetime

class QuestList(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.quests = []
        self.new_quest_title = ft.TextField(label="Quest Title")
        self.new_quest_descprtion = ft.TextField(label="Quest Description")
        self.new_quest_experience = ft.TextField(label="Experience Reward", input_type="number")
        self.new_quest_deadline = ft.TextField(label="Deadline (yyyy-mm-dd)")
        self.character_id = ft.TextField(label="Character id(for test)", input_type="number")
        self.quest_list = ft.Column()
        self.update_list()

    def build(self):
        return ft.Column(
            [
                ft.Text("Quests", style=ft.TextStyle(size=30)),
                self.quest_list,
                ft.Text("Create Quest", style=ft.TextStyle(size=20)),
                self.new_quest_title,
                self.new_quest_descprtion,
                self.new_quest_experience,
                self.new_quest_deadline,
                self.character_id,
                ft.ElevatedButton("Create Quest", on_click=self.create_new_quest),
            ]
        )
    
    def update_list(self):
        self.quests = get_quests()
        self.quest_list.controls.clear()
        for quest in self.quests:
            self.quest_list.controls.append(
                ft.Row(
                    [
                        ft.Text(f"{quest.title}", width=200),
                        ft.Text(f"{quest.description}", width=200),
                        ft.Text(f"Reward:{quest.experience_reward}", width=80),
                        ft.Text(f"Type: {quest.type}", width=80),
                        ft.Text(f"Deadline: {quest.deadline if quest.deadline else '-'}", width=100),
                        ft.ElevatedButton("complete", on_click=lambda e, quest_id=quest.id: self.complete_quest(e,quest_id)),
                    ]
                )
            )

        character_id = self.character_id.value
        if character_id:
             try:
               character_id = int(character_id)
               character_quests = get_character_quests(character_id)
               character = get_character(character_id)
               if character:
                  self.quest_list.controls.insert(0, ft.Text(f"Quests for character {character.name}"))
                  for quest in self.quests:
                     for character_quest in character_quests:
                        if character_quest.quest_id == quest.id:
                           self.quest_list.controls.append(
                            ft.Row(
                                [
                                   ft.Text(f"{quest.title}", width=200),
                                   ft.Text(f"{quest.description}", width=200),
                                   ft.Text(f"Reward: {quest.experience_reward}", width=80),
                                     ft.Text(f"Type: {quest.type}", width=80),
                                    ft.Text(f"Deadline: {quest.deadline if quest.deadline else '-'}", width=100),
                                   ft.Text("Completed!" if character_quest.is_completed else "Not Completed", width=120),
                                 ]
                              )
                            )
               else:
                 self.quest_list.controls.insert(0, ft.Text(f"Character not found"))
             except Exception as e:
                print (e)
                self.quest_list.controls.insert(0, ft.Text(f"Error: Invalid character id"))

        self.update()

    def complete_quest(self, e, quest_id):
       character_id = self.character_id.value
       if character_id:
          create_character_quest(character_id, quest_id)
          complete_quest(character_id, quest_id)
          self.update_list()
    
    def create_new_quest(self, e):
       quest_title = self.new_quest_title.value
       quest_description = self.new_quest_descprtion.value
       quest_experience = self.new_quest_experience.value
       quest_deadline = self.new_quest_deadline.value
       try:
         quest_experience = int(quest_experience)
         if quest_deadline:
           quest_deadline = datetime.strptime(quest_deadline, '%Y-%m-%d').strftime('%Y-%m-%d')
         create_quest(quest_title, quest_description, quest_experience, "normal", quest_deadline)
         self.new_quest_title.value = ""
         self.new_quest_description.value = ""
         self.new_quest_experience.value = ""
         self.new_quest_deadline.value = ""
         self.update_list()
       except Exception as e:
         print (e)
         self.quest_list.controls.insert(0, ft.Text("Error creating quest"))
         self.update()