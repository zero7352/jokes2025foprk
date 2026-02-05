


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

# List of joke categories (Requirement: List)
categories = ["robbers", "tanks", "pencils"]

# Procedure with a parameter (Requirement: Procedure/Function)
def tell_joke(choice):
    # Selection (if/else) inside the procedure
    if choice == categories[0]:
        input("Knock Knock... ")
        input("Calder... ")
        print("Calder police - I've been robbed!")
    elif choice == categories[1]:
        input("Knock Knock... ")
        input("Tank... ")
        print("You are welcome!")
    elif choice == categories[2]:
        input("Knock Knock... ")
        input("Broken pencil... ")
        print("Nevermind, it's pointless!")

# Main Program
start = input("Do you want to hear a joke? (yes/no): ").lower()

# Iteration (Requirement: Loop)
while start == "yes":
    print(f"Options: {categories}")
    question = input("Pick a category: ").lower()
    
    if question in categories:
        tell_joke(question) # Calling the procedure
    else:
        print("That's not an option!")
    
    start = input("Hear another? (yes/no): ").lower()

# Final Scoring
rate = int(input("Rate this 1-10: "))
print(f"{rate * 10}% satisfaction rate!")
