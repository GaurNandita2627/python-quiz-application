import random

print("===================================")
print("   WELCOME TO PYTHON QUIZ APP")
print("===================================\n")

# Questions covering important Python topics
questions = [
    # Core Fundamentals
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["A. List", "B. Tuple", "C. String", "D. int"],
        "answer": "A"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["A. ^", "B. **", "C. %", "D. //"],
        "answer": "B"
    },
    {
        "question": "What is the output of print(type(True))?",
        "options": ["A. int", "B. bool", "C. str", "D. float"],
        "answer": "B"
    },

    # Control Flow and Functions
    {
        "question": "Which loop is used when the number of iterations is unknown in advance?",
        "options": ["A. for", "B. while", "C. do-while", "D. None of these"],
        "answer": "B"
    },
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["A. func", "B. function", "C. def", "D. define"],
        "answer": "C"
    },

    # Data Structures
    {
        "question": "Which of the following is used to store key-value pairs?",
        "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
        "answer": "B"
    },
    {
        "question": "What is the output of len([1,2,3][1:])?",
        "options": ["A. 1", "B. 2", "C. 3", "D. Error"],
        "answer": "B"
    },

    # Intermediate / Advanced
    {
        "question": "Which of these blocks handle exceptions in Python?",
        "options": ["A. try-except", "B. do-catch", "C. try-catch", "D. handle-error"],
        "answer": "A"
    },
    {
        "question": "Which of the following is correct for creating a class in Python?",
        "options": ["A. class MyClass:", "B. class MyClass()", "C. class MyClass[]:", "D. def class MyClass:"],
        "answer": "A"
    },
    {
        "question": "Which method is used to open a file for writing?",
        "options": ["A. open('file.txt','r')", "B. open('file.txt','w')", "C. open('file.txt','rw')", "D. open('file.txt','a+')"],
        "answer": "B"
    }
]

# Shuffle questions so every run is slightly different
random.shuffle(questions)
score = 0
total_questions = len(questions)

for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {q['question']}")
    for opt in q["options"]:
        print(opt)

    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    # Input validation
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