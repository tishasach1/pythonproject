import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("400x300")

        # Quiz data with updated questions
        self.questions = [
            {
                "question": "Which programming language is known as the 'language of the web'?",
                "options": ["Python", "JavaScript", "C++", "Java"],
                "answer": "JavaScript"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Saturn", "Jupiter", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "In which year did the Titanic sink?",
                "options": ["1912", "1905", "1918", "1920"],
                "answer": "1912"
            },
            {
                "question": "What is the smallest unit of life in all living organisms?",
                "options": ["Atom", "Cell", "Organ", "Tissue"],
                "answer": "Cell"
            },
            {
                "question": "Which element is known for being the hardest natural substance?",
                "options": ["Gold", "Diamond", "Iron", "Platinum"],
                "answer": "Diamond"
            }
        ]
        self.current_question = 0
        self.score = 0

        # UI Components
        self.question_label = tk.Label(root, text="", wraplength=380, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar(value="")  # Variable to store selected option
        self.options_buttons = []

        for i in range(4):  # Create buttons for options
            button = tk.Radiobutton(
                root,
                text="",
                variable=self.options_var,
                value="",
                font=("Arial", 12),
                wraplength=380,
                anchor="w",
                padx=10
            )
            button.pack(anchor="w", pady=5)
            self.options_buttons.append(button)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer, font=("Arial", 12))
        self.submit_button.pack(pady=20)

        # Load the first question
        self.load_question()

    def load_question(self):
        """Load the current question and update the options."""
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=f"Q{self.current_question + 1}: {question_data['question']}")
            self.options_var.set("")  # Reset selected option
            for i, option in enumerate(question_data["options"]):
                self.options_buttons[i].config(text=option, value=option)
        else:
            self.show_final_score()

    def submit_answer(self):
        """Check the selected answer and provide feedback."""
        selected_option = self.options_var.get()
        if not selected_option:
            messagebox.showwarning("No Selection", "Please select an answer before submitting!")
            return

        correct_answer = self.questions[self.current_question]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Wrong!", f"Wrong answer. The correct answer was '{correct_answer}'.")

        self.current_question += 1
        self.load_question()

    def show_final_score(self):
        """Display the final score and close the quiz."""
        messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/{len(self.questions)}.")
        self.root.destroy()  # Close the application


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
