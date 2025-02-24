def menu():
    print("\nDictionary Operations:")
    print("1. Add a key-value pair")
    print("2. Remove a key")
    print("3. Get value of a key")
    print("4. Display all keys")
    print("5. Display all values")
    print("6. Exit")


dictionary = {}

while True:
    menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        key = input("Enter key: ")
        value = input("Enter value: ")
        dictionary[key] = value  
        print("Key-value pair added.")
    
    elif choice == '2':
        key = input("Enter key to remove: ")
        removed_value = dictionary.pop(key, None)  
        if removed_value is not None:
            print(f"Removed key '{key}' with value '{removed_value}'.")
        else:
            print("Key not found.")
    
    elif choice == '3':
        key = input("Enter key to get value: ")
        value = dictionary.get(key, "Key not found") 
        print(f"Value: {value}")
    
    elif choice == '4':
        print("Keys:", list(dictionary.keys()))  
    elif choice == '5':
        print("Values:", list(dictionary.values()))  
    elif choice == '6':
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
