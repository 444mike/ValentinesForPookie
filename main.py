import tkinter as tk
from datetime import datetime, timedelta

# Set the target date (change this to your special moment)
target_date = datetime(2025, 2, 14, 18, 0, 0)  # Feb 14, 6:00 PM

def update_countdown():
    now = datetime.now()
    time_left = target_date - now
    days, seconds = time_left.days, time_left.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    countdown_text.set(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

    if time_left.total_seconds() > 0:
        root.after(1000, update_countdown)
    else:
        countdown_text.set("It's time! ❤️")

# Create the window
root = tk.Tk()
root.title("💖 Valentine's Countdown 💖")
root.geometry("400x300")

# Message Label
message = tk.Label(root, text="Happy Valentine's Day, [Her Name]! 💕", font=("Arial", 16), fg="red")
message.pack(pady=20)

# Countdown Label
countdown_text = tk.StringVar()
countdown_label = tk.Label(root, textvariable=countdown_text, font=("Arial", 14))
countdown_label.pack()

# Start the countdown
update_countdown()

# Run the GUI
root.mainloop()
