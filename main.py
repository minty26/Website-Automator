import webbrowser

urls = {
    "work": ["https://www.replit.com", "https://www.github.com", "https://chatgpt.com"],
    "entertainment": ["https://www.disneyplus.com", "https://www.netflix.com", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
}

def open_webpages(urls):
    for url in urls:
        webbrowser.open(url)

def create_library():
    library_name = input("Enter the name for the new library: ")
    library_urls = input("Enter the URLs for the new library (separated by commas): ").split(',')
    urls[library_name] = library_urls
    print(f"New library '{library_name}' created successfully!")

def delete_library():
    library_name = input("Enter the name of the library you want to delete: ")
    if library_name in urls:
        del urls[library_name]
        print(f"Library '{library_name}' deleted successfully!")
    else:
        print(f"Library '{library_name}' not found.")

def display_menu():
    print("\nMenu:")
    print("1. Create a new library")
    print("2. Open a library")
    print("3. Delete a library")
    print("4. Exit")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            create_library()
        elif choice == "2":
            library_name = input("Enter the name of the library you want to open: ")
            if library_name in urls:
                open_webpages(urls[library_name])
            else:
                print(f"Library '{library_name}' not found.")
        elif choice == "3":
            delete_library()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
