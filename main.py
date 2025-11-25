from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, ListView, ListItem, Label
from textual.containers import Container,Vertical,Horizontal
from pathlib import Path
#Modules
from modules.basic_operations import list_dirs,Item,ItemType

class FileExplorerApp(App):
    CSS_PATH =  "./main.css"

    def compose(self) -> ComposeResult:

        yield Header()
    
        yield Horizontal(
            Container(
                Static("SideBar",classes="title"),
                classes="sidebar"
            ),
            Container(
                classes="content",
                id="content"
            ),
            classes="main-container"
        )

        yield Footer()

    def on_mount(self) -> None: #This function fires each time that you run the app
        self.title = "File Explorer"
        self.sub_title = "v0.1" #file explorer version

        

    def on_ready(self) -> None:
        #List items from home
        home_items = list_dirs(Path.home())                                         #get items from "home" dir
        list_view = ListView(id="files_list")
        content_area = self.query_one("#content")
        content_area.mount(list_view)                                               #mount the list_view before append items dinamically
        for item in home_items:
            if item.type == ItemType.FILE:
                list_view.append(ListItem(Label(item.name)))
        list_view.focus()                                                           #User start focus in the list view items to nav with arrows

if __name__ == "__main__":
    app = FileExplorerApp()
    app.run()