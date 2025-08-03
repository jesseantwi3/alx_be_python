if choice == '1':
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the list.")
elif choice == '2':
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")
elif choice == '3':
    if shopping_list:
        print("Your shopping list:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")

