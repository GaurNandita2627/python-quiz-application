from questions import questions
import random

# Shuffle questions so every run is slightly different
random.shuffle(questions)
score = 0
total_questions = len(questions)

for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {q['question']}")
    for opt in q["options"]:
        print(opt)

    # Take user input and make sure it is valid
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    while user_answer not in ["A", "B", "C", "D"]:
        user_answer = input("Invalid choice! Enter A/B/C/D only: ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {q['answer']}")

# Calculate results
percentage = (score / total_questions) * 100

print("\n===================================")
print("            QUIZ RESULT")
print("===================================")
print(f"Total Questions : {total_questions}")
print(f"Correct Answers : {score}")
print(f"Percentage      : {percentage:.2f}%")

if percentage >= 50:
    print("Result          : PASS 🎉")
else:
    print("Result          : FAIL ❌")

print("\nThank you for taking the Python Quiz!")
