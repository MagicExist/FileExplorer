from pathlib import Path
from enum import Enum,auto
from dataclasses import dataclass

class ItemType(Enum):
    ALL = auto()
    DIR = auto()
    FILE = auto()
    HIDDEN = auto()

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



def list_dirs(route='.',type=ItemType.ALL):
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