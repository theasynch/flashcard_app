import tkinter as tk

# Create the main window
main = tk.Tk()
main.title("Flashcard App")

# Set the window size
main.geometry("400x300")

# Create a Label to display the question
question_label = tk.Label(main, text="Question goes here", font=("Garamond", 16))
question_label.pack(pady=20)

# Create a Button to reveal the answer
reveal_button = tk.Button(main, text="Show Answer")
reveal_button.pack()

# Create a Button to go to the next flashcard
next_button = tk.Button(main, text="Next")
next_button.pack(pady=10)

# Start the Tkinter event loop
main.mainloop()
