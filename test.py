import tkinter as tk
from PIL import Image, ImageTk
import os

def open_main_window():
    # Destroy the splash screen and launch the main application
    splash.destroy()
    
    root = tk.Tk()
    root.title("Main Application")
    root.geometry("600x400")
    
    # Center the main window
    x = (root.winfo_screenwidth() // 2) - (600 // 2)
    y = (root.winfo_screenheight() // 2) - (400 // 2)
    root.geometry(f"600x400+{x}+{y}")
    
    tk.Label(root, text="Welcome to the Main Application!", font=("Helvetica", 18)).pack(expand=True)
    root.mainloop()

# 1. Initialize the Splash Screen window
splash = tk.Tk()
splash.overrideredirect(True) # Removes the title bar and window borders

# 2. Dimensions for the splash screen
splash_width = 500
splash_height = 300

try:
    # 3. Get the exact folder where this Python script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Join that folder path with your image name
    image_path = os.path.join(script_dir, "A.png")
    
    # 4. Open, resize, and display the image using the absolute path
    img = Image.open(image_path) 
    img = img.resize((splash_width, splash_height))
    splash_img = ImageTk.PhotoImage(img)
    
    # Place the image in a label
    splash_label = tk.Label(splash, image=splash_img, borderwidth=0)
    splash_label.pack()
    
except FileNotFoundError:
    # Fallback if the image still isn't found
    print(f"Error: Could not find image at {image_path}")
    fallback_label = tk.Label(splash, text=f"Image Not Found:\n{image_path}", bg="black", fg="white", font=("Helvetica", 10))
    fallback_label.pack(expand=True, fill="both")

# 5. Center the splash screen on the monitor
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
center_x = int((screen_width / 2) - (splash_width / 2))
center_y = int((screen_height / 2) - (splash_height / 2))
splash.geometry(f"{splash_width}x{splash_height}+{center_x}+{center_y}")

# 6. Schedule the main window to open after 3000 milliseconds (3 seconds)
splash.after(3000, open_main_window)

splash.mainloop()