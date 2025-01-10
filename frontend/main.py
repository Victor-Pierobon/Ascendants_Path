import flet as ft
from frontend.components.character_form import CharacterForm
from frontend.components.quest_list import QuestList

def main(page: ft.Page):
    page.title = "Ascendant's Path"
    page.theme = "dark"
    page.padding = 50


    def go_character_creation(e):
        page.go("/character_creation")

    def go_quests_page(e):
        page.go("/quests")

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Text("Welcome to Ascendant's Path", style=ft.TextStyle(size=30)),
                    ft.ElevatedButton("Create a Character", on_click=go_character_creation),
                    ft.ElevatedButton("Quests", on_click=go_quests_page),
                ],
            )
        )
        if page.route == "/character_creation":
            page.views.append(
                ft.View(
                    "/character_creation",
                    [
                        CharacterForm(go_quests_page),
                    ],
                )
            )
        if page.route == "/quests":
            page.views.append(
                ft.View(
                    "/quests",
                    [
                        QuestList()
                    ],
                )
            )
    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    ft.app(targer=main)