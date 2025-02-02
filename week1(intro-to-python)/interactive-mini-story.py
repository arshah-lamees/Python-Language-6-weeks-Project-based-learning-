# interactive mini-story using input-output operations

# a helper function to reduce the repetitive code e.g., instead of 'input("any input ").strip()' multiple times in your code you just need to call the function
def get_input(prompt):
    return input(prompt).strip() #strip() removes any leading whitespace (spaces, tabs, newlines) from the input string.

def tell_story():
    print("Welcome to your adventure!")
    
    name = get_input("What's your name, brave adventurer? ")
    place = get_input("Name a magical place: ")
    creature = get_input("What's your favorite mythical creature? ")
    treasure = get_input("Name something valuable: ")

    print(f"\nLet's begin the tale of {name}'s Great Adventure!")

    print(f"\nOnce upon a time, in the mystical land of {place}, there lived a brave soul named {name}.")
    print(f"Every day, {name} would wake up and gaze out at the misty mountains, dreaming of adventure.")

    choice = get_input(f"\nOne morning, a {creature} appeared at {name}'s doorstep. Do you (1) Invite it in or (2) Run away? ")

    if choice == "1":
        print(f"\n{name} bravely invited the {creature} inside. It turned out to be friendly!")
        print(f"The {creature} revealed the location of a hidden {treasure}.")
        final_choice = get_input(f"\nDo you want to (1) Seek the {treasure} or (2) Stay home? ")
        if final_choice == "1":
            print(f"\nCongratulations! {name} found the {treasure} and became a legend in {place}!")
        else:
            print(f"\n{name} decided to stay home, but always wondered about the adventure that could have been.")
    else:
        print(f"\n{name} ran away, but the {creature} followed, revealing it needed help.")
        help_choice = get_input("Do you (1) Help the creature or (2) Keep running? ")
        if help_choice == "1":
            print(f"\n{name} decided to help and made a lifelong friend. Together, they had many adventures in {place}!")
        else:
            print(f"\n{name} kept running and eventually found a hidden cave filled with {treasure}. A different kind of adventure!")

    print("\nThe End. Thanks for playing!")
def main():
    tell_story()

main()
