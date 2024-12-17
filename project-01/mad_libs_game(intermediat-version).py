import random

def mad_libs():
    stories = [
        "Today, I went to the {place} and saw a {adjective} {noun} {verb}ing. It was so funny!",
        "Once upon a time, {name} found a {adjective} {noun} while walking through {place}.",
        "{name} decided to {verb} with a {adjective} {animal} at the {place}. What a day!"
    ]

    # Randomly select a story template
    story_template = random.choice(stories)

    # Collect inputs
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    animal = input("Enter an animal: ")

    # Fill in the story template
    story = story_template.format(
        name=name, place=place, adjective=adjective,
        noun=noun, verb=verb, animal=animal
    )

    print("\nYour Mad Libs story:\n")
    print(story)

# Run the game
mad_libs()

