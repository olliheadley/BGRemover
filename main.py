import tkinter as tk
from tkinter import filedialog, StringVar, OptionMenu
from PIL import Image, ImageTk
from rembg import remove
import numpy as np
import io

# Function to open a file dialog and select an image
def open_image():
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        display_image(file_path)

# Function to display the selected image and remove the background
def display_image(file_path):
    input_image = Image.open(file_path)
    input_image = input_image.convert("RGBA")
    input_array = np.array(input_image)
    output_array = remove(input_array)
    output_image = Image.fromarray(output_array)

    # Set the transparent background to the selected color
    color = selected_color.get()
    if color == "White":
        new_image = Image.new("RGBA", output_image.size, "WHITE")
    elif color == "Black":
        new_image = Image.new("RGBA", output_image.size, "BLACK")
    elif color == "Blue":
        new_image = Image.new("RGBA", output_image.size, "BLUE")
    # Add more color options as needed

    final_image = Image.alpha_composite(new_image, output_image)

    # Display the original and background-removed images
    input_photo = ImageTk.PhotoImage(input_image)
    output_photo = ImageTk.PhotoImage(final_image)

    input_label.config(image=input_photo)
    input_label.image = input_photo
    output_label.config(image=output_photo)
    output_label.image = output_photo

# Create the main window
root = tk.Tk()
root.title("Image Background Remover")

# Create and position the widgets
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Dropdown menu for selecting the background color
color_options = ["White", "Black", "Blue"]  # Add more color options as needed
selected_color = StringVar(root)
selected_color.set(color_options[0])  # Set the default color
color_menu = OptionMenu(root, selected_color, *color_options)
color_menu.pack()

input_label = tk.Label(root)
input_label.pack()

output_label = tk.Label(root)
output_label.pack()

# Run the application
root.mainloop()
