import random
import tkinter as tk

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

color = random_color()
print("Random Color Code:", color)

# Create a window to dispaly the color
root = tk.Tk()
root.title("Random Color")
root.geometry("300x300")
root.configure(bg=color)

label = tk.Label(root, text="Color Code: " + color, bg=color, fg="white", font=("Arial", 16))
label.pack(expand=True)

root.mainloop()