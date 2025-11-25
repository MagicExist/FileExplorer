from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Container,Vertical,Horizontal

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
                Static("content",classes="title"),
                classes="content"
            ),
            classes="main-container"
        )

        yield Footer()

    def on_mount(self) -> None: #This function fires each time that you run the app
        self.title = "File Explorer"
        self.sub_title = "v0.1" #file explorer version


if __name__ == "__main__":
    app = FileExplorerApp()
    app.run()