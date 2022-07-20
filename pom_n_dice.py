import time
import threading
import tkinter as tk
from tkinter import ttk,PhotoImage
import random
from PIL import Image, ImageTk
class PomTimer:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Pomodoro wish you productive day!")
        self.root.call("wm", "iconphoto", self.root._w, PhotoImage(file="upper_icon.png"))
        self.s=ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Baskerville Old Face",17))
        self.s.configure("TButton", font=("Baskerville Old Face", 20))
        self.tabs=ttk.Notebook(self.root)
        self.tabs.pack(fill="both",pady=0,expand=True)
        self.tab1=ttk.Frame(self.tabs, width=600, height=50)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=50)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=50)
        self.tab4 = ttk.Frame(self.tabs, width=600, height=50)
        self.tab5 = ttk.Frame(self.tabs, width=600, height=50)
        self.tabs.add(self.tab1, text="Time to work!")
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=25)
        self.start_button=ttk.Button(self.grid_layout,text="Start",command=self.start_time)
        self.start_button.grid(row=0,column=0)
        self.pause_button = ttk.Button(self.grid_layout, text="Pause timer", command=self.pause)
        self.pause_button.grid(row=0, column=1)
        self.resume_button = ttk.Button(self.grid_layout, text="Resume timer", command=self.resume)
        self.resume_button.grid(row=0, column=2)
        self.dice_button=ttk.Button(self.tab5, text="Let's roll!", command=self.roll_dice)
        self.dice_button.pack(pady=20)
        self.work_time_label=ttk.Label(self.tab1, text="25:00", font=("Baskerville Old Face",75))
        self.work_time_label.pack(pady=40)
        self.short_time_label = ttk.Label(self.tab2, text="05:00", font=("Baskerville Old Face", 75))
        self.short_time_label.pack(pady=40)
        self.long_time_label = ttk.Label(self.tab3, text="10:00", font=("Baskerville Old Face", 75))
        self.long_time_label.pack(pady=40)
        self.input_field=tk.Entry(self.tab4)
        self.input_field.pack(pady=30)
        self.time_button = ttk.Button(self.tab4, text="Let's go", command=self.get_input_time)
        self.time_button.pack(pady=20)
        self.dice_label=ttk.Label(self.tab5,)
        self.dice_label.pack()
        self.sum_label = ttk.Label(self.tab5, text={"25:00"}, font=("Baskerville Old Face", 75))
        self.work_time_label.pack(pady=40)
        self.tabs.add(self.tab2, text="Short break...")
        self.tabs.add(self.tab3, text="Long break uff...")
        self.tabs.add(self.tab4, text="Customizable timer")
        self.tabs.add(self.tab5, text="Roll magic dice ...")
        self.pomodoro_counter_label=ttk.Label(self.grid_layout, text="Full sessions: 0",font=("Baskerville Old Face",25))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=20)
        self.sessions=0
        self.paused=False
        self.resume=False
        self.roll_dice=False
        self.full_seconds=0
        self.sum_of_dice=[]


        self.root.mainloop()

    def start_time_thread(self):
        time = threading.Thread(target=self.start_time)
        time.start()

    def start_time(self):

        self.resume = False
        self.paused=False
        timer_id=self.tabs.index(self.tabs.select())+1

        if timer_id==1:
            self.full_seconds=60*25
            while self.full_seconds > 0 and not self.paused:
                minutes, seconds = divmod(self.full_seconds, 60)
                self.work_time_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                self.full_seconds -=1
            if not self.paused:
                self.sessions +=1
                self.pomodoro_counter_label.configure(text=f"Full sessions: {self.sessions}")

        elif timer_id==2:
            self.full_seconds = 60 * 5
            while self.full_seconds > 0 and not self.paused:
                minutes, seconds = divmod(self.full_seconds, 60)
                self.short_time_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                self.full_seconds -= 1
        elif timer_id==3:
            self.full_seconds = 60 * 10
            while self.full_seconds > 0 and not self.paused:
                minutes, seconds = divmod(self.full_seconds, 60)
                self.long_time_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                self.full_seconds -= 1



    def pause(self):
        self.paused=True
        self.resume=False


    def resume(self):
        self.resume = False
        self.paused = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:

            while self.full_seconds > 0 and not self.paused:
                minutes, seconds = divmod(self.full_seconds, 60)
                self.work_time_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                self.full_seconds -= 1
            if not self.paused:
                self.sessions += 1
                self.pomodoro_counter_label.configure(text=f"Full sessions: {self.sessions}")


        elif timer_id == 2:



            while self.full_seconds > 0 and not self.paused:
                minutes, seconds = divmod(self.full_seconds, 60)

                self.short_time_label.configure(text=f"{minutes:02d}:{seconds:02d}")

                self.root.update()

                time.sleep(1)

                self.full_seconds -= 1

        elif timer_id == 3:



            while self.full_seconds > 0 and not self.paused:
                minutes, seconds = divmod(self.full_seconds, 60)

                self.long_time_label.configure(text=f"{minutes:02d}:{seconds:02d}")

                self.root.update()

                time.sleep(1)

                self.full_seconds -= 1

    def get_input_time(self):
        self.full_seconds=int(self.input_field.get())*60
        self.custom_time = tk.Label(self.tab4, text=f"{self.full_seconds}:00", font=("Baskerville Old Face", 75))
        self.custom_time.pack(pady=20)
        while self.full_seconds > 0 and not self.paused:
            minutes, seconds = divmod(self.full_seconds, 60)

            self.custom_time.configure(text=f"{minutes:02d}:{seconds:02d}")

            self.root.update()

            time.sleep(1)

            self.full_seconds -= 1



    def roll_dice(self):
        dice=random.randint(1,6)
        self.sum_of_dice.append(dice)
        print(dice)
        print(self.sum_of_dice)
        real_sum=sum(self.sum_of_dice)

        print(real_sum)

        if dice ==1:
            dice1=Image.open("dice1.png").resize((150,150))
            dice1=ImageTk.PhotoImage(dice1)

            dice1_label=tk.Label(self.tab5,image=dice1)
            dice1_label.image=dice1
            dice1_label.place(x=150,y=100)
        if dice ==2:
            dice2 = Image.open("dice2.png").resize((150,150))

            dice2 = ImageTk.PhotoImage(dice2)
            dice2_label = tk.Label(self.tab5, image=dice2)
            dice2_label.image = dice2
            dice2_label.place(x=150, y=100)
        if dice == 3:
            dice3 = Image.open("dice3.png").resize((150, 150))

            dice3 = ImageTk.PhotoImage(dice3)
            dice3_label = tk.Label(self.tab5, image=dice3)
            dice3_label.image = dice3
            dice3_label.place(x=150, y=100)
        if dice ==4:
            dice4 = Image.open("dice4.png").resize((150,150))

            dice4 = ImageTk.PhotoImage(dice4)
            dice4_label = tk.Label(self.tab5, image=dice4)
            dice4_label.image = dice4
            dice4_label.place(x=150, y=100)
        if dice ==5:
            dice5 = Image.open("dice5.png").resize((150,150))

            dice5 = ImageTk.PhotoImage(dice5)
            dice5_label = tk.Label(self.tab5, image=dice5)
            dice5_label.image = dice5
            dice5_label.place(x=150, y=100)
        if dice ==6:
            dice6 = Image.open("dice6.png").resize((150,150))

            dice6 = ImageTk.PhotoImage(dice6)
            dice6_label = tk.Label(self.tab5, image=dice6)
            dice6_label.image = dice6
            dice6_label.place(x=150, y=100)




PomTimer()