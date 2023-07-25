import random
import tkinter as tk
from tkinter import messagebox

# Quiz questions and answers
quiz_questions = [
    {
        "question": "What is Python?",
        "choices": [
            "A. A high-level programming language",
            "B. A low-level programming language",
            "C. A markup language",
            "D. A scripting language"
        ],
        "answer": "A"
    },
    {
        "question": "Which statement is used to display output in Python?",
        "choices": [
            "A. print()",
            "B. input()",
            "C. return",
            "D. yield"
        ],
        "answer": "A"
    },
    {
        "question": "What is the output of the following code?\n\n"
                    "x = 5\n"
                    "y = 2\n"
                    "print(x // y)",
        "choices": [
            "A. 2",
            "B. 2.5",
            "C. 2.0",
            "D. 2.2"
        ],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "choices": [
            "A. func",
            "B. def",
            "C. function",
            "D. define"
        ],
        "answer": "B"
    },
]

# Track user's score
score = 0

# Current question index
current_question = 0

# Colors based on the golden ratio
BACKGROUND_COLOR = "#26282F"
TEXT_COLOR = "#E8E9EB"
BUTTON_COLOR = "#FFD700"

def display_welcome_message():
    welcome_message = "Welcome to the Python Quiz Game!\n"
    welcome_message += "Test your knowledge of Python programming with a set of multiple-choice questions.\n"
    welcome_message += "Select the correct answer for each question and see how well you perform.\n\n"
    welcome_message += "Get ready to begin the quiz!"

    messagebox.showinfo("Welcome", welcome_message)

def display_question():
    global current_question

    # Get the current question
    question_data = quiz_questions[current_question]

    # Clear the previous question and choices
    question_label.config(text="")
    for choice in choice_buttons:
        choice.config(text="", state=tk.DISABLED)

    # Display the current question
    question_label.config(text=question_data["question"])

    # Display the choices
    choices = question_data["choices"]
    for i in range(len(choices)):
        choice_buttons[i].config(text=choices[i], state=tk.NORMAL)

def submit_answer(answer):
    global score, current_question

    # Get the current question
    question_data = quiz_questions[current_question]

    # Check if the answer is correct
    if answer == question_data["answer"]:
        score += 1
        messagebox.showinfo("Correct", "Your answer is correct!")
    else:
        correct_answer = question_data["answer"]
        messagebox.showinfo("Incorrect", f"Your answer is incorrect. The correct answer is {correct_answer}.")

    # Move to the next question
    current_question += 1

    # Check if all questions have been answered
    if current_question == len(quiz_questions):
        display_results()
    else:
        display_question()

def display_results():
    # Disable all choice buttons
    for choice in choice_buttons:
        choice.config(state=tk.DISABLED)

    # Display the final score and performance message
    total_questions = len(quiz_questions)
    score_percentage = (score / total_questions) * 100
    message = f"You have completed the quiz!\nYour score: {score}/{total_questions} ({score_percentage:.2f}%)."
    messagebox.showinfo("Quiz Results", message)

    # Ask if the user wants to play again
    play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
    if play_again:
        reset_quiz()
    else:
        window.destroy()

def reset_quiz():
    global score, current_question
    score = 0
    current_question = 0
    display_question()

# Create the main window
window = tk.Tk()
window.title("Python Quiz")
window.configure(bg=BACKGROUND_COLOR)
window.geometry("500x300")

# Create a label for the welcome message
welcome_label = tk.Label(window, text="Welcome to the Python Quiz Game!", fg=TEXT_COLOR, bg=BACKGROUND_COLOR,
                         font=("Arial", 16), wraplength=400)
welcome_label.pack(pady=10)

# Create a label for the question
question_label = tk.Label(window, text="", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("Arial", 14), wraplength=400)
question_label.pack(pady=20)

# Create choice buttons
choice_buttons = []
for i in range(4):
    choice_button = tk.Button(window, text="", font=("Arial", 12), width=40, bg=BUTTON_COLOR, fg=BACKGROUND_COLOR,
                              activebackground=BACKGROUND_COLOR, activeforeground=BUTTON_COLOR,
                              command=lambda i=i: submit_answer(chr(ord('A') + i)))
    choice_button.pack(pady=5)
    choice_buttons.append(choice_button)

# Display the welcome message
display_welcome_message()

# Start the quiz by displaying the first question
display_question()

# Start the GUI event loop
window.mainloop()
