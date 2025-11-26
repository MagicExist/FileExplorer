from pathlib import Path
from enum import Enum,auto
from dataclasses import dataclass
from platformdirs import user_desktop_dir, user_documents_dir, user_downloads_dir

class ItemType(Enum):
    ALL = auto()
    DIR = auto()
    FILE = auto()
    HIDDEN = auto()

class CommonDirs(Enum):
    DESKTOP = Path(user_desktop_dir())
    DOCUMENTS = Path(user_documents_dir())
    DOWNLOADS = Path(user_downloads_dir())

@dataclass
class Item:
    name: str
    path: Path
    type: ItemType
    hidden: bool

filters = {
    ItemType.ALL: lambda item: True,
    ItemType.DIR: lambda item: item.is_dir(),
    ItemType.FILE: lambda item: item.is_file(),
    ItemType.HIDDEN: lambda item: item.name.startswith('.'),
}



def list_dirs(route='.',type=ItemType.ALL) -> list[Item]:
    """
    Return the items from a specific directory.

    Args:
        route (str): Path to the directory to list.
        type (ItemType): Filter for which kind of items to return.

    Returns:
        list[Item]: A list of Item objects representing files, directories,
            or other types inside the specified directory.
    """
      
    p = Path(route)
    if not p.exists():
        return []
    
    filter = filters[type]
    dir_items = []
    if p.is_dir():
        for item in p.iterdir():
            if filter(item):
                if item.is_dir():
                    kind = ItemType.DIR
                elif item.is_file():
                    kind = ItemType.FILE
                else:
                    kind = ItemType.OTHER
                
                dir_items.append(Item(
                    name=item.name,
                    path=item,
                    type=kind,
                    hidden=item.name.startswith('.')
                ))
        return dir_items
    
def list_common_dirs() -> list[Item]:
    """
    Returns a list of common user directories as `Item` objects.

    Iterates over the `CommonDirs` enum and creates an `Item` instance
    for each directory, including its name, path, type, and hidden status.

    Hidden status is determined by whether the directory name starts with a dot ('.').

    Returns:
        list[Item]: A list of `Item` objects representing common directories
        such as Desktop, Documents, and Downloads.
    """

    items = []
    for dir_enum in CommonDirs:
        path = dir_enum.value
        items.append(
            Item(
                name=path.name,
                path=path,
                type=ItemType.DIR,
                hidden=path.name.startswith('.')
            )
        )
    return items
   