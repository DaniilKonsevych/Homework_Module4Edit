def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        if args[0] not in contacts.keys():
            name, phone = args
            contacts[name] = phone
            return "Contact added."
        else:
            return "Contact already exists - can't add."
    except:
        return "Something went wrong. Likely too many our not enough arguments"
    
def change_contact(args, contacts):
    try:
        if args[0] in contacts.keys():
            name, phone = args
            contacts[name] = phone
            return "Contact changed."
        else:
            return "Contact doesn't exist yet - can't change."
    except:
        return "Something went wrong. Likely too many our not enough arguments"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()