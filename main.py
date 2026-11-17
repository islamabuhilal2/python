import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def open_login_window():
    authenticated = False

    login_win = tk.Tk()
    login_win.title("Hospital - Login")
    login_win.resizable(False, False)
    center_window(login_win, 900, 600)

    # Header
    tk.Label(
        login_win,
        text="Hospital System Login",
        font=("Helvetica", 24, "bold")
    ).pack(pady=(25, 25))

    # Username field
    tk.Label(login_win, text="Username:", font=("Helvetica", 11)).pack(anchor="w", padx=250)
    username_entry = tk.Entry(login_win, font=("Helvetica", 11), width=28)
    username_entry.pack(pady=(20, 20))
    username_entry.focus()

    # Password field
    tk.Label(login_win, text="Password:", font=("Helvetica", 11)).pack(anchor="w", padx=250)
    password_entry = tk.Entry(login_win, font=("Helvetica", 11), width=28, show="*")
    password_entry.pack(pady=(20, 20))

    def verify_login(event=None):
        nonlocal authenticated
        username = username_entry.get().strip()
        password = password_entry.get()

        # Replace with your database or user check
        if username == "admin" and password == "1234":
            authenticated = True
            login_win.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            password_entry.delete(0, tk.END)

    # Login button & Enter key support
    tk.Button(
        login_win,
        text="Login",
        font=("Helvetica", 11, "bold"),
        width=15,
        bg="#0078D7",
        fg="white",
        command=verify_login
    ).pack()

    login_win.bind("<Return>", verify_login)
    login_win.mainloop()

    return authenticated


def open_main_window():
    root = tk.Tk()
    root.title("Hospital")
    center_window(root, 900, 600)

    tk.Label(root, text="Hi to the hospital system", font=("Helvetica", 18)).pack(expand=True)
    root.mainloop()


# 1. Initialize the Splash Screen window
splash = tk.Tk()
splash.overrideredirect(True)  # Removes the title bar and window borders

# 2. Dimensions for the splash screen
splash_width = 1000
splash_height = 600

try:
    # 3. Get the exact folder where this Python script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "bg.jpg")

    # 4. Open, resize, and display the image
    img = Image.open(image_path)
    img = img.resize((splash_width, splash_height))
    splash_img = ImageTk.PhotoImage(img)

    splash_label = tk.Label(splash, image=splash_img, borderwidth=0)
    splash_label.pack()

except FileNotFoundError:
    print(f"Error: Could not find image at {image_path}")
    fallback_label = tk.Label(
        splash,
        text=f"Image Not Found:\n{image_path}",
        bg="black",
        fg="white",
        font=("Helvetica", 10)
    )
    fallback_label.pack(expand=True, fill="both")

# 5. Center the splash screen on the monitor
center_window(splash, splash_width, splash_height)

# 6. Close the splash screen after 4000 milliseconds (4 seconds)
splash.after(4000, splash.destroy)
splash.mainloop()

# 7. Launch login screen, then open main window only if login succeeds
if open_login_window():
    open_main_window()