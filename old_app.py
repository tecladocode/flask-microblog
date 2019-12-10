import datetime

entries = []

user_selection = input("Enter 'a' to add an entry, or 'q' to quit: ")

while user_selection != 'q':
    if user_selection == 'a':
        entry_content = input("What did you learn today? ")
        entries.append({"content": entry_content, "date": datetime.datetime.today().strftime("%b %d")})
    user_selection = input("Enter 'a' to add an entry, or 'q' to quit: ")


print(entries)