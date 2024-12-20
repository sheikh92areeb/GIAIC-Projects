def mad_libs():
    # Welcome message
    print("Welcome to the Mad Libs game!")
    print("Fill in the blanks to create your story.\n")

    # Asking for user inputs
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    animal = input("Enter an animal: ")

    # Story template
    story = (
        f"Once upon a time, {name} went to {place}. "
        f"It was a {adjective} day, and they decided to bring a {noun} with them. "
        f"While they were there, they saw a {animal} {verb}ing in the distance. "
        f"Surprised, {name} exclaimed, 'What a day to remember!'"
    )

    # Display the completed story
    print("\nYour Mad Libs story:\n")
    print(story)

# Run the Mad Libs function
mad_libs()
