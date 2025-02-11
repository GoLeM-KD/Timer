import time
import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import os

running = False

def reset_timer():
    global running
    running = False
    
    # Reset the time 
    time_label.config(text="00:00:00")

    hours_field.delete(0, tk.END)
    minutes_field.delete(0, tk.END)
    seconds_field.delete(0, tk.END)

    pygame.mixer.music.stop()

def start_timer():
    global running
    running = True

    pygame.mixer.init()
    alarm_path = os.path.join(os.path.dirname(__file__), "alarm.mp3")
    pygame.mixer.music.load(alarm_path)

    try:
        hours = hours_field.get()
        minutes = minutes_field.get()
        seconds = seconds_field.get()

        # Setting values for empty entries
        hours = int(hours) if hours else 0
        minutes = int(minutes) if minutes else 0
        seconds = int(seconds) if seconds else 0

        while running and (hours > 0 or minutes > 0 or seconds > 0):
            time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            root.update()
            time.sleep(1)
            if seconds > 0:
                seconds -= 1
            elif minutes > 0:
                minutes -= 1
                seconds = 59
            elif hours > 0:
                hours -= 1
                minutes = 59
                seconds = 59
        if running:  
            time_label.config(text="00:00:00")
            pygame.mixer.music.play()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for hours, minutes, and seconds.")
    finally:
        running = False  # To Stop after runing the timer
        
root = tk.Tk()
root.title("Kavija's Timer")

user_width = root.winfo_screenwidth()
user_height = root.winfo_screenheight()
left = int(user_width/2 - 400/2)
top = int(user_height/2 - 700/2)
root.geometry(f"400x700+{left}+{top}")
root.resizable(False, False)

# Frame for holding hours,minutes,sex
frame = tk.Frame(root)
frame.pack(pady=20)

# Entry fields for hours,minutes and sex
hours_frame = tk.Frame(frame)
hours_frame.pack(side=tk.LEFT, padx=10)
hours_field = ttk.Entry(hours_frame, width=5)
hours_field.pack()
hours_label = ttk.Label(hours_frame, text="Hours")
hours_label.pack()

minutes_frame = tk.Frame(frame)
minutes_frame.pack(side=tk.LEFT, padx=10)
minutes_field = ttk.Entry(minutes_frame, width=5)
minutes_field.pack()
minutes_label = ttk.Label(minutes_frame, text="Minutes")
minutes_label.pack()

seconds_frame = tk.Frame(frame)
seconds_frame.pack(side=tk.LEFT, padx=10)
seconds_field = ttk.Entry(seconds_frame, width=5)
seconds_field.pack()
seconds_label = ttk.Label(seconds_frame, text="Seconds")
seconds_label.pack()

# Start button
start_button = ttk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=20)

# reset button
reset_button = ttk.Button(root, text="Reset", command=reset_timer)
reset_button.pack(pady=10)

# countdown display
time_label = ttk.Label(root, text="00:00:00", font=("Helvetica", 48))
time_label.pack(pady=20)

root.mainloop()