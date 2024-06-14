class ShoppingItem:
    def __init__(self, name):
        self.name = name
        self.purchased = False

    def mark_as_purchased(self):
        self.purchased = True

    def __str__(self):
        #"[X]"
        #"[ ]"
        return f"[{'X' if self.purchased else ' '}] {self.name}"


