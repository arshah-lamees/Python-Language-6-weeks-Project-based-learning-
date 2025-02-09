def run_python_quiz():
    #list of dictionaries which contain questions and their answers
    python_quiz = [
    {
        "question": "What keyword is used to define a function in Python?",
        "answer": "def"
    },
    {
        "question": "Which of these is NOT a valid Python data type: int, float, complex, string, char?",
        "answer": "char"
    },
    {
        "question": "What symbol is used for single-line comments in Python?",
        "answer": "#"
    },
    {
        "question": "What method is used to add an element to the end of a list?",
        "answer": "append"
    },
    {
        "question": "What is the output of print(type([]))?",
        "answer": "<class 'list'>"
    },
    {
        "question": "What keyword is used to exit a loop prematurely?",
        "answer": "break"
    },
    {
        "question": "What function is used to get the length of a sequence?",
        "answer": "len"
    },
    {
        "question": "What is the correct way to open a file named 'example.txt' for reading?",
        "answer": "open('example.txt', 'r')"
    },
    {
        "question": "What is the output of 3 * '7'?",
        "answer": "777"
    },
    {
        "question": "What built-in function can be used to get user input in Python?",
        "answer": "input"
    }
    ]
    score = 0
    total_questions = len(python_quiz)
    print("Welcome to the Python Quiz!")
    print(f"You will be asked {total_questions} questions. Let's begin!\n")
    
    #this loop will iterate through the list of dictionaries, enumerate(python_quiz, 1) create iterator that point to (index, item) pair, q access the item(dictionary) in list through key
    #It prints the question number and the question text.
    #It asks for user input and processes it (strips whitespace and converts to lowercase).
    #It compares the user's answer to the correct answer.
    #It provides feedback and updates the score if the answer is correct.
    #The loop continues until all questions in python_quiz have been processed.
    for i, q in enumerate(python_quiz, 1):
        print(f"Question {i}: {q['question']}")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = q['answer'].lower()
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is {q['answer']}.\n")
    print(f"Quiz completed! Your final score is {score} out of {total_questions}.")
    percentage = (score / total_questions) * 100
    print(f"You got {percentage:.2f}% correct.")
def main():
    run_python_quiz()
main()
