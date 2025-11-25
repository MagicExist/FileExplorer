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
                ListView(id="files_list"),
                classes="content",
                id="content"
            ),
            classes="main-container"
        )

        yield Footer()

    def update_items(self,item_list) -> None:
        """
            Update the file list view with new items.

            This method clears the current contents of the ListView identified by
            `#files_list` and repopulates it with the items provided in `item_list`.
            Only items whose type is `ItemType.FILE` are displayed. After updating,
            the focus is set back to the ListView so the user can navigate using
            the keyboard.

            Args:
                item_list (list): A list of items returned by `list_dirs()`. Each
                    item must contain at least a `.name` attribute and a `.type`
                    attribute compatible with `ItemType`.

            Returns:
                None: This method performs UI updates but does not return a value.
        """

        list_view = self.query_one("#files_list")
        list_view.clear()

        for item in item_list:
            if item.type == ItemType.FILE:
                list_view.append(ListItem(Label(f"📄{item.name}")))
            elif item.type == ItemType.DIR:
                list_view.append(ListItem(Label(f"📁{item.name}")))
            else:
                list_view.append(ListItem(Label(f"❓{item.name}")))
        list_view.focus()                                                           #User start focus in the list view items to nav with arrows


    def on_mount(self) -> None: #This function fires each time that you run the app
        self.title = "File Explorer"
        self.sub_title = "v0.1" #file explorer version

        

    def on_ready(self) -> None:
        #List items from home
        home_items = list_dirs(Path.home())                                         #get items from "home" dir
        self.update_items(home_items)

if __name__ == "__main__":
    app = FileExplorerApp()
    app.run()