import flet as ft
from frontend.components.character_form import CharacterForm
from frontend.components.quest_list import QuestList
from frontend.styles import AppStyles

def main(page: ft.Page):
    page.title = "Ascendant's Path"
    page.theme = AppStyles.theme
    page.padding = 50

    def go_character_creation(e):
         print("go_character_creation called")
         page.go("/character_creation")

    def go_quests_page(e):
         print("go_quests_page called")
         page.go("/quests")

    def route_change(route):
        print(f"Route changed to: {page.route}")
        page.views.clear()
        print(f"page.views after clear: {page.views}")
        initial_view = ft.View(
                "/",
                [
                    ft.Text("Welcome to Ascendant's Path", style=ft.TextStyle(size=30)),
                    ft.ElevatedButton("Create a character", on_click=go_character_creation),
                    ft.ElevatedButton("Quests", on_click=go_quests_page),
                ],
            )
        print(f"initial_view: {initial_view}")
        page.views.append(initial_view)
        print(f"page.views after adding initial view: {page.views}")
        if page.route == "/character_creation":
            print("Creating Character Creation View")
            character_creation_view = ft.View(
                    "/character_creation",
                    [
                        CharacterForm(go_quests_page)
                    ],
                )
            page.views.append(character_creation_view)
            print(f"page.views after adding Character Creation View: {page.views}")
        if page.route == "/quests":
           print("Creating Quests View")
           quests_view = ft.View(
                    "/quests",
                    [
                        QuestList()
                    ],
                )
           page.views.append(quests_view)
           print(f"page.views after adding Quests View: {page.views}")
        page.update()
        print(f"page.views after updating: {page.views}")
    
    page.on_route_change = route_change
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)