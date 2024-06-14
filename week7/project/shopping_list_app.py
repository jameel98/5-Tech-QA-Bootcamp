from week7.project.shopping_list import ShoppingList


class ShoppingListApp:
    def __init__(self):
        self.lists = {}

    def create_list(self, list_name):
        if list_name in self.lists:
             raise ValueError(f"List '{list_name}' already exists.")
        self.lists[list_name] = ShoppingList(list_name)

    def add_item_to_list(self, list_name, item_name):
        if list_name not in self.lists:
            raise ValueError(f"List '{list_name}' does not exist.")
        self.lists[list_name].add_item(item_name)

    def mark_item_as_purchased(self, list_name, item_name):
        if list_name not in self.lists:
            raise ValueError(f"List '{list_name}' does not exist.")
        self.lists[list_name].mark_item_as_purchased(item_name)

    def display_lists(self):
        if not self.lists:
            print("No shopping lists available.")
        for shopping_list in self.lists.values():
            print(shopping_list)


    def run(self):
        while True:
            print("\nChoose an option:")
            print("1. Create shopping list")
            print("2. Add item to list")
            print("3. Mark item as purchased")
            print("4. Display all lists")
            print("5. Exit")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == '1':
                list_name = input("Enter the name of the new shopping list: ")
                try:
                    self.create_list(list_name)
                    print(f"Shopping list '{list_name}' created.")
                except ValueError as e:
                    print(e)

            elif choice == '2':
                list_name = input("Enter the name of the shopping list: ")
                item_name = input("Enter the name of the item to add: ")
                try:
                    self.add_item_to_list(list_name, item_name)
                    print(f"Item '{item_name}' added to list '{list_name}'.")
                except ValueError as e:
                    print(e)
                except EOFError:
                    print("EOF error")

            elif choice == '3':
                list_name = input("Enter the name of the shopping list: ")
                item_name = input("Enter the name of the item to mark as purchased: ")
                try:
                    self.mark_item_as_purchased(list_name, item_name)
                    print(f"Item '{item_name}' marked as purchased in list '{list_name}'.")
                except ValueError as e:
                    print(e)

            elif choice == '4':
                self.display_lists()

            elif choice == '5':
                print("Exiting...")
                break

            else:
                print("Invalid choice, please try again.")