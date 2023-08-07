import tkinter as tk
from tkinter import messagebox
import time

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

        self.timer_label.pack(pady=20)
        self.start_button.pack(pady=10)
        self.stop_button.pack(pady=10)
        self.reset_button.pack(pady=10)

    def update_timer(self):
        if self.timer_running:
            current_time = time.time()
            if self.stop_time is None:
                elapsed_time = current_time - self.start_time
            else:
                elapsed_time = current_time - self.init_time - (self.start_time - self.stop_time)

            hours = int(elapsed_time / 3600)
            minutes = int(elapsed_time / 60)
            seconds = int(elapsed_time % 60)
            self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.after(300, self.update_timer)

    def start_timer(self):
        if not self.timer_running:
            if self.init_time is None:
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
        self.elapsed_time = 0
        self.timer_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()