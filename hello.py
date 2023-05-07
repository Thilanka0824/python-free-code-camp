# Ask user for name and print hello + name
name = input("What's your name? ").strip().title()

# remove whitespace from str
name = name.strip()

# capitalize first letter of name
name = name.capitalize()

# use title() method
name = name.title()

# say hello to user
print(f"hello, {name}")