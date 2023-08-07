import tkinter as tk
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Comparison")
        
        self.timer_count_1 = 0
        self.timer_count_2 = 0
        
        self.label_1 = tk.Label(root, text="Timer 1: 0")
        self.label_1.pack()
        
        self.label_2 = tk.Label(root, text="Timer 2: 0")
        self.label_2.pack()
        
        self.start_timers()
        
    def delayLooper(self):
        for i in range(1, 3000) :
            print(i)

    def update_timer_1(self):
        self.timer_count_1 += 1
        self.delayLooper()
        self.label_1.config(text=f"Timer 1: {self.timer_count_1}")
        self.root.after(1000, self.update_timer_1)
        
    def update_timer_2(self):
        current_time = int(time.time())
        self.delayLooper()
        self.timer_count_2 = current_time - self.start_time
        self.label_2.config(text=f"Timer 2: {self.timer_count_2}")
        self.root.after(300, self.update_timer_2)
        
    def start_timers(self):
        self.start_time = int(time.time())
        self.update_timer_1()
        self.update_timer_2()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    app = TimerApp(root)
    root.mainloop()