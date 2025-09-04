import tkinter as tk

def spawn_popups():
    for _ in range(2):
        create_popup()

def create_popup():
    popup = tk.Toplevel()
    popup.title("window")
    popup.geometry("200x100")
    label = tk.Label(popup, text="Loser")
    label.pack(pady=10)
    
    # Override the close button behavior
    popup.protocol("WM_DELETE_WINDOW", lambda: on_close(popup))

def on_close(popup):
    popup.destroy()
    spawn_popups()

# Main window
root = tk.Tk()
root.title("window")
root.geometry("200x100")
root.protocol("WM_DELETE_WINDOW", create_popup)

btn = tk.Label(root, text ="Loser")
btn.pack(pady=10)

root.mainloop()