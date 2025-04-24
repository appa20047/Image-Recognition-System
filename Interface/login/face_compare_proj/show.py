import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk
import io

def view_criminals():
    try:
        conn = sqlite3.connect('criminals.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM criminals''')
        criminals = cursor.fetchall()
        conn.close()

        # Create table to display criminals
        root = tk.Tk()
        root.title("View Criminal Records")
        table = ttk.Treeview(root, columns=('Name', 'Age', 'Gender', 'Father\'s Name', 'Crime Done', 'Image'))
        table.heading('#0', text='ID')
        table.heading('#1', text='Name')
        table.heading('#2', text='Age')
        table.heading('#3', text='Gender')
        table.heading('#4', text='Father\'s Name')
        table.heading('#5', text='Crime Done')
        table.heading('#6', text='Image')
        table.pack(fill='both', expand=True)

        for criminal in criminals:
            image_data = criminal[6]
            if image_data:
                image = Image.open(io.BytesIO(image_data))
                image.thumbnail((50, 50))  # Resize the image
                photo = ImageTk.PhotoImage(image)
                table.insert('', 'end', text=criminal[0], values=(criminal[1], criminal[2], criminal[3], criminal[4], criminal[5], photo))
                table.image = photo
            else:
                table.insert('', 'end', text=criminal[0], values=(criminal[1], criminal[2], criminal[3], criminal[4], criminal[5], ''))

        root.mainloop()
    except Exception as e:
        print("Error:", e)

view_criminals()
