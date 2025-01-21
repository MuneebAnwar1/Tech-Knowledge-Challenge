# Displaying the quiz with blanks and options for each blank
print("In the world of technology, the first programmable computer was invented by [_______] in the early 1940s. \nLater, the development of the [_______] revolutionized how we interact with computers.\nOne of the most popular operating systems today is [_______], developed by Microsoft. \nThe invention of the [_______] enabled wireless communication, making mobile phones and the internet more accessible. \nIn 2008, the first version of [_______], the most widely used mobile operating system, was released.")

# Displaying the options for filling the blanks
print('''Options for Each Blank:
1. konrad zuse
2. microprocessor
3. windows
4. bluetooth
5. android
''')

# Prompting the user to input answers for each blank
n1 = input("blank 1: ").lower()  # Answer for the first blank
n2 = input("blank 2: ").lower()  # Answer for the second blank
n3 = input("blank 3: ").lower()  # Answer for the third blank
n4 = input("blank 4: ").lower()  # Answer for the fourth blank
n5 = input("blank 5: ").lower()  # Answer for the fifth blank

# Initialize score to track the number of correct answers
score = 0

# Start a loop to check the answers continuously
while True:
    # Check if the answer for blank 1 is correct
    if n1 == "konrad zuse":
        print("1 is correct answer")  # Inform the user that answer 1 is correct
        score += 1  # Increase the score
    # Check if the answer for blank 2 is correct
    if n2 == "microprocessor":
        print("2 is correct answer")  # Inform the user that answer 2 is correct
        score += 1  # Increase the score
    # Check if the answer for blank 3 is correct
    if n3 == "windows":
        print("3 is correct answer")  # Inform the user that answer 3 is correct
        score += 1  # Increase the score
    # Check if the answer for blank 4 is correct
    if n4 == "bluetooth":
        print("4 is correct answer")  # Inform the user that answer 4 is correct
        score += 1  # Increase the score
    # Check if the answer for blank 5 is correct
    if n5 == "android":
        print("5 is correct answer")  # Inform the user that answer 5 is correct
        score += 1  # Increase the score
        break  # Exit the loop if all answers are correct

    else:
        print("Wrong Answer!!!")  # If any answer is incorrect, inform the user

# Display the final score after all answers are correct
print(f"Your Score is {score}")
