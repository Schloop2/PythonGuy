import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import game


def onImageClick(int):
    game.choice(int)
    game.check

    if game.getDraw == True:
        text.set("Draw!")
    elif game.getResults == True:
        text.set("You Win!")
    else: 
        text.set("You Lose!")


# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Set the window size
root.geometry("400x200")

text = tk.StringVar()
text.set("Choose! Rock, Paper, or Scissors?")

# Label
label = tk.Label(root, 
                 textvariable=text,
                 anchor=tk.N,
                 bg="white",
                 height=1,
                 width =30,
                 bd=3,
                 font=("Arial", 10, "bold"),
                 cursor="hand2",
                 fg="black",
                 padx=15,
                 pady=15,
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                 underline=0,
                 wraplength=250
                )

label.pack(pady=20) # padding

# Load images
imageRock = Image.open("images/rock.jpg") # Rock Image
imagePaper = Image.open("images/paper.jpg") # Paper Image
imageScissors = Image.open("images/scissors.jpg") # Scissors Image


# Resize Images
imageRock = imageRock.resize((100,100))
imagePaper = imagePaper.resize((100,100))
imageScissors = imageScissors.resize((100,100))


# Convert images to PhotoImage format
photo1 = ImageTk.PhotoImage(imageRock)
photo2 = ImageTk.PhotoImage(imagePaper)
photo3 = ImageTk.PhotoImage(imageScissors)


# Create labels to display the images
label1 = tk.Label(root, image=photo1)
label2 = tk.Label(root, image=photo2)
label3 = tk.Label(root, image=photo3)

# Place the labels side by side using pack
label1.pack(side="left", padx=10)
label2.pack(side="left", padx=10)
label3.pack(side="left", padx=10)

# Bind the click event to the labels
label1.bind("<Button-1>", lambda event: onImageClick(0))
label2.bind("<Button-1>", lambda event: onImageClick(1))
label3.bind("<Button-1>", lambda event: onImageClick(2))

# Start the Tkinter event loop
root.mainloop()

# Add a label widget
label = tk.Label(root, text="Rock Paper Scissors")
label.pack(pady=20)


# Start the Tkinter event loop
root.mainloop()