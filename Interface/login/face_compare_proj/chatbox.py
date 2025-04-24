import tkinter as tk

def submit():
    # Function to handle submit button click
    text = text_box.get("1.0", "end-1c")  # Get text from the text box
    print("Submitted Text:", text)

# Create main window
root = tk.Tk()
root.title("ChatBox")
root.geometry("340x440")
root.configure(bg='#333333')

frame = tk.Frame(bg='#333333')

login_label = tk.Label(frame, text="Enter Query" , bg='#333333',fg='#FF3399', font=('Arial', 30) )
login_label.pack()
# Create text box
text_box = tk.Text(frame, width=50, height=20)
text_box.pack()

# Create submit button
submit_button = tk.Button(frame, text="Submit", command=submit)
submit_button.pack()
frame.pack()
# Run the main event loop
root.mainloop()
