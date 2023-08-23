import tkinter as tk
from tkinter import messagebox
import time
import os
import shutil


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("타이머 앱")

        self.timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.start_button = tk.Button(root, text="시작", command=self.start_timer)
        self.stop_button = tk.Button(root, text="정지", command=self.stop_timer)
        self.reset_button = tk.Button(root, text="리셋", command=self.reset_timer)

        self.timer_running = False
        self.init_time = None
        self.start_time = None
        self.stop_time = None
        self.elapsed_time = 0

        self.init_hours = 0 
        self.init_minutes = 0
        self.init_seconds = 0

        self.timer_label.pack(pady=20)
        self.start_button.pack(pady=10)
        self.stop_button.pack(pady=10)
        self.reset_button.pack(pady=10)
        self.recorded_time = self.load_recorded_time()
        print(self.recorded_time)
        if self.recorded_time is not None:
            self.init_hours, self.init_minutes, self.init_seconds = map(int, self.recorded_time.split(":"))
            self.timer_label.config(text=f"{self.init_hours:02d}:{self.init_minutes:02d}:{self.init_seconds:02d}")


    def load_recorded_time(self):
        try:
            with open(os.path.join("C:\\time\\timerApp", "recordedTime.txt"), "r") as file:
                recorded_time = file.read()
                return recorded_time
        except FileNotFoundError:
            return None

    def save_recorded_time(self, hour, min, sec):
        save_time = f"{hour}:{min}:{sec}"
        try:
            with open(os.path.join("C:\\time\\timerApp", "recordedTime.txt"), "w") as file:
                file.write(str(save_time))
        except FileNotFoundError:
            os.makedirs("C:\\time\\timerApp") 
            with open(os.path.join("C:\\time\\timerApp", "recordedTime.txt"), "w") as file:
                file.write(str(save_time))

    def delete_timer_directory(self):
        try:
            shutil.rmtree("C:\\time\\timerApp")
        except FileNotFoundError:
            print("file is not found")

    def update_timer(self):
        if self.timer_running:
            current_time = time.time()
            if self.stop_time is None:
                elapsed_time = current_time - self.start_time + float(self.init_hours * 3600 + self.init_minutes * 60 + self.init_seconds)
            else:
                elapsed_time = current_time - self.init_time - (self.start_time - self.stop_time)

            print(elapsed_time)
            hours = int(elapsed_time / 3600)
            minutes = int(elapsed_time / 60)
            seconds = int(elapsed_time % 60)
            self.save_recorded_time(hours, minutes, seconds)
            self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.after(300, self.update_timer)

    def start_timer(self):
        if not self.timer_running:
            if self.init_time is None:
                if self.recorded_time is not None:
                    self.init_time = time.time() + float(self.init_hours * 3600 + self.init_minutes * 60 + self.init_seconds)
                else:
                    self.init_time = time.time()
            self.start_time = time.time()
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.stop_time = time.time()

    def reset_timer(self):
        self.timer_running = False
        self.start_time = None
        self.stop_time = None
        self.elapsed_time = 0
        self.delete_timer_directory()
        self.timer_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()