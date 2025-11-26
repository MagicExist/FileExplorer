from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, ListView, ListItem, Label
from textual.containers import Container,Vertical,Horizontal
from pathlib import Path
#Modules
from modules.basic_operations import list_dirs,Item,ItemType,list_common_dirs

class FileExplorerApp(App):
    def __init__(self):
        super().__init__()
        self.current_path = Path.home()

    CSS_PATH =  "./main.css"

    BINDINGS = [
        ("a", "filter_all", "All Files"),
        ("h", "filter_hidden", "Hidden Files"),
        ("d", "filter_dir", "Filter Dirs"),
        ("f", "filter_file", "Filter FIles")
    ]

    def compose(self) -> ComposeResult:

        yield Header()
    
        yield Horizontal(
            Container(
                Vertical(
                    Container(
                        Label("Common Dirs"),
                        ListView(id="common_dirs_list"),
                        classes="common_dirs_container"
                    ),
                ),
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

    def update_common_dirs(self,dir_list):
         """
        Updates the common directories ListView with new directory items.

        Clears the existing items in the ListView with ID `#common_dirs_list`
        and appends new `ListItem` objects, each containing a `Label` that
        displays the directory name prefixed with a folder emoji 📁.

        Args:
            dir_list (list[Item]): A list of `Item` objects representing
                common directories to display in the sidebar.
         """

         list_view = self.query_one("#common_dirs_list")
         list_view.clear()        

         for dir in dir_list:
             list_view.append(
                 ListItem(
                     Label(f"📁{dir.name}")
                 )
             )


    def update_items(self,item_list) -> None:
        """
        Update the file list view with new items.

        This method clears the contents of the ListView identified by `#files_list`
        and repopulates it using the provided `item_list`. Each item is displayed
        with an emoji according to its type:
        
        - 📄 for files (`ItemType.FILE`)
        - 📁 for directories (`ItemType.DIR`)
        - ❓ for unknown or unsupported item types

        After updating the list, focus is returned to the ListView so the user can
        continue navigating with the keyboard.

        Args:
            item_list (list): A list of items returned by `list_dirs()`. Each item
                must have at least a `.name` attribute and a `.type` attribute that
                corresponds to one of the values in `ItemType`.

        Returns:
            None: This method updates the UI but does not return a value.
        """
        list_view = self.query_one("#files_list")
        list_view.clear()                                                          #Clear the list view items

        for item in item_list:
            if item.type == ItemType.FILE:
                list_view.append(ListItem(Label(f"📄{item.name}")))
            elif item.type == ItemType.DIR:
                list_view.append(ListItem(Label(f"📁{item.name}")))
            else:
                list_view.append(ListItem(Label(f"❓{item.name}")))
        list_view.focus()                                                           #User start focus in the list view items to nav with arrows

    #binding actions
    def action_filter_all(self):
        """
        Show all items in the current directory.

        This action retrieves every item inside the current path, regardless of
        its type (files, directories, or hidden items), and updates the ListView
        to display them. Intended to be triggered by a keybinding.
        
        Returns:
            None: The UI is updated but no value is returned.
        """
        all_list = list_dirs(self.current_path)
        self.update_items(all_list)

    def action_filter_hidden(self):
        """
        Show only hidden items in the current directory.

        This action retrieves only items classified as `ItemType.HIDDEN` inside
        the current path and updates the ListView accordingly. Intended to be
        triggered by a keybinding to quickly toggle visibility of hidden files.
        
        Returns:
            None: The UI is updated but no value is returned.
        """
        hidden_list = list_dirs(self.current_path,ItemType.HIDDEN)
        self.update_items(hidden_list)
    
    def action_filter_dir(self) -> None:
        """
        Filters and displays only directories in the current path.

        Retrieves a list of items from `self.current_path` that are directories
        and updates the UI or internal state to show only these directory items.

        Args:
            self: The instance of the class containing the current path and 
                the `update_items` method.
        Returns:
            None: The UI is updated but no value is returned.
        """

        dir_list = list_dirs(self.current_path,ItemType.DIR)
        self.update_items(dir_list)

    def action_filter_file(self) -> None:
        """
        Filters and displays only files in the current path.

        Retrieves a list of items from `self.current_path` that are files
        and updates the UI or internal state to show only these file items.

        Args:
            self: The instance of the class containing the current path and 
                the `update_items` method.
        Returns:
            None: The UI is updated but no value is returned.
        """

        file_list = list_dirs(self.current_path,ItemType.FILE)
        self.update_items(file_list)

    def on_mount(self) -> None: #This function fires each time that you run the app
        self.title = "File Explorer"
        self.sub_title = "v0.3" #file explorer version

        

    def on_ready(self) -> None:
        #List items from home
        home_items = list_dirs(self.current_path)                                      #get items from "home" dir
        self.update_items(home_items)

        common_dirs = list_common_dirs()   
        self.update_common_dirs(common_dirs)
        

if __name__ == "__main__":
    app = FileExplorerApp()
    app.run()