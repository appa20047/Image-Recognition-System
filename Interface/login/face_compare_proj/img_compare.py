import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from skimage.metrics import structural_similarity as ssim

image1_path = None
image2_path = None
image1_label = None
image2_label = None

def compare_images(image1, image2):
    # Load images
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    
    # Resize images to the same dimensions
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))
    
    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Compute Structural Similarity Index (SSI)
    ssim_value = ssim(gray1, gray2)
    
    return ssim_value

def open_file(image_num):
    global image1_path, image2_path, image1_label, image2_label
    filename = filedialog.askopenfilename(initialdir="/Desktop/", title="Select file", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))
    if filename:
        if image_num == 1:
            image1_path = filename
            load_image(image1_label, filename)
        else:
            image2_path = filename
            load_image(image2_label, filename)

def load_image(label, filename):
    image = Image.open(filename)
    image = ImageTk.PhotoImage(image)
    label.config(image=image)
    label.image = image

def compare_images_gui():
    global image1_label, image2_label
    window = tk.Tk()
    window.title("Image Comparison")
    window.geometry("340x440")
    window.configure(bg='#333333')
    
    frame = tk.Frame(bg="#333333")
    image1_label = tk.Label(frame)
    image1_label.grid(row=0, column=0, padx=5, pady=5)
    
    image2_label = tk.Label(frame)
    image2_label.grid(row=0, column=1, padx=5, pady=5)
    
    browse_button1 = tk.Button(frame, text="Browse Image 1", bg="#00c3ff", fg="#333333", font=("Arial",16), command=lambda: open_file(1))
    browse_button1.grid(row=1, column=0, padx=5, pady=5)
    
    browse_button2 = tk.Button(frame, text="Browse Image 2", bg="#ff009d", fg="#333333", font=("Arial",16), command=lambda: open_file(2))
    browse_button2.grid(row=1, column=1, padx=5, pady=5)
    
    compare_button = tk.Button(frame, text="Compare",bg="#000000", fg="#ff3399" ,command=perform_comparison)
    compare_button.grid(row=2, columnspan=2, padx=5, pady=5)
    
    frame.pack()
    window.mainloop()

def perform_comparison():
    global image1_path, image2_path
    if image1_path and image2_path:
        similarity = compare_images(image1_path, image2_path)
        messagebox.showinfo("Comparison Result", f"Similarity: {similarity}")
        
    else:
        messagebox.showwarning("Warning", "Please select both images.")

if __name__ == "__main__":
    compare_images_gui()
