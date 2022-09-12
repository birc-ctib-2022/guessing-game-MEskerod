# The following code is just to setup the exercise. You do not need to
# understand but can jump to the game below.


def input_selection(prompt: str, options: list[str]) -> str:
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))


print("Please think of a number from 1 to 20, both included.")
print("Let me know how good my guess is.\n")

# Here, we implement the computer's strategy for guessing
# the number you are thinking of. Don't lie to the
# computer. It won't punish you, but it will frown upon it.

#First algorithm
#for guess in range(1, 21):
#    result = input_selection(
#        "I'm guessing {}\nHow is my guess?".format(guess),
#        ["low", "hit", "high"]
#    )
#    if result == "hit":
#        print("Wuhuu!")
#        break

#    print("I must have been too low, right?", result)

#Second algorithm 
#for guess in range(20,0,-1):
#    result = input_selection(
#        "I'm guessing {}\nHow is my guess?".format(guess),
#        ["low", "hit", "high"]
#    )
#    if result == "hit":
#        print("Wuhuu!")
#        break
#
#    2print("I must have been too high, right?", result)

#Third algorithm 
def find_middle(given_list: list) -> int:
    """Find the middle index of a given list
    If the list contains and even number find_middle should return
    the lowest of the two middle values
    
    >>> find_middle([1,2,3,4,5])
    2
    
    >>> find_middle([1,2,3,4,5,6,7,8]
    3"""

    if len(given_list) % 2 == 0:
        middle_index = (len(given_list)-2)//2
    else: 
        middle_index = (len(given_list)-1)//2
    return middle_index

guesses=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
while True:
    middle = find_middle(guesses)
    guess = guesses[middle]
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low","hit","high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    if result == "high":
        guesses = guesses[:middle]
    if result == "low":
        guesses = guesses[middle+1:]
