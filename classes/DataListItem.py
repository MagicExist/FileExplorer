from textual.widgets import ListItem,Label

class DataListItem(ListItem):
    def __init__(self, label: Label, data=None):
        super().__init__(label)
        self.data = data  # store your custom object
