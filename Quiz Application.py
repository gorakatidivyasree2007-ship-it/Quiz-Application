questions = [
    ("What is the capital of India?", "Delhi"),
    ("Which language is this project written in?", "Python"),
    ("How many days are in a week?", "7")
]

score = 0

for question, answer in questions:
    user_answer = input(question + " ").strip()

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"Your score: {score}/{len(questions)}")
