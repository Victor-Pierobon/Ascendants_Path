import flet as ft
from backend.utils import create_character, get_character

class CharacterForm(ft.UserControl):
    def __init__(self, go_quests_page):
        super().__init__()
        self.go_quests_page = go_quests_page
        self.character_name = ft.TextField(label="Character Name")
        self.created_character_text = ft.Text()

    def build(self):
        return ft.Column(
            [
                self.character_name,
                ft.ElevatedButton("Create Character", on_click=self.create_character),
                self.created_character_text
            ]
        )
    
    def create_character(self, e):
        character_name =self.character_name.value
        character_id = create_character(character_name)
        if character_id:
            character = get_character(character_id)
            self.created_character_text.value = f"Character {character.name} created successfully!"
            self.update()
            self.go_quests_page(None)
        else:
            self.created_character_text.value = f"Error creating character"
            self.update()