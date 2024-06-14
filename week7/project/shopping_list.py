from week7.project.shopping_item import ShoppingItem


class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item_name):
        item = ShoppingItem(item_name)
        self.items.append(item)

    def mark_item_as_purchased(self, item_name):
        for item in self.items:
            if item.name == item_name:
                item.mark_as_purchased()
                return
        raise ValueError(f"Item '{item_name}' not found in list '{self.name}'")

    def __str__(self):
        return f"{self.name}:\n" + "\n".join(str(item) for item in self.items)

