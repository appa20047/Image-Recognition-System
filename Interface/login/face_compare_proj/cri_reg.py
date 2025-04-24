import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3

def browse_image():
    filename = filedialog.askopenfilename()
    if filename:
        image_path.set(filename)

def register_criminal():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    father_name = father_name_entry.get()
    crime = crime_entry.get()
    image_path_value = image_path.get()
    
    if name and age and gender and father_name and crime and image_path_value:
        try:
            with open(image_path_value, 'rb') as f:
                image_blob = f.read()

            conn = sqlite3.connect('criminals.db')
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS criminals 
                              (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                               name TEXT, 
                               age INTEGER, 
                               gender TEXT, 
                               father_name TEXT, 
                               crime TEXT,
                               image BLOB)''')
            cursor.execute('''INSERT INTO criminals (name, age, gender, father_name, crime, image) 
                              VALUES (?, ?, ?, ?, ?, ?)''', (name, age, gender, father_name, crime, image_blob))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Criminal registered successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "Please fill in all fields and select an image.")

def view_criminals():
    try:
        conn = sqlite3.connect('criminals.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM criminals''')
        criminals = cursor.fetchall()
        conn.close()
        for criminal in criminals:
            print(criminal)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Criminal Registration")

# Criminal Name
name_label = tk.Label(root, text="Criminal Name:")
name_label.grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Age
age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=5, pady=5)

# Gender
gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0, sticky="e")
gender_var = tk.StringVar(value="Male")
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=2, column=1, sticky="w", padx=5)
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=2, column=1, sticky="e", padx=5)

# Father's Name
father_name_label = tk.Label(root, text="Father's Name:")
father_name_label.grid(row=3, column=0, sticky="e")
father_name_entry = tk.Entry(root)
father_name_entry.grid(row=3, column=1, padx=5, pady=5)

# Crime Done
crime_label = tk.Label(root, text="Crime Done:")
crime_label.grid(row=4, column=0, sticky="e")
crime_entry = tk.Entry(root)
crime_entry.grid(row=4, column=1, padx=5, pady=5)

# Image Upload
image_label = tk.Label(root, text="Image Path:")
image_label.grid(row=5, column=0, sticky="e")
image_path = tk.StringVar()
image_entry = tk.Entry(root, textvariable=image_path, state='readonly')
image_entry.grid(row=5, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse Image", command=browse_image)
browse_button.grid(row=5, column=2, padx=5, pady=5)

# Register Button
register_button = tk.Button(root, text="Register", command=register_criminal)
register_button.grid(row=6, column=0, columnspan=2, pady=10)

# View Button
view_button = tk.Button(root, text="View Criminals", command=view_criminals)
view_button.grid(row=6, column=2, pady=10)

root.mainloop()
