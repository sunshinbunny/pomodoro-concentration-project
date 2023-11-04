from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(text="Timer", fg=GREEN)
    REPS = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global  REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    REPS += 1
    if REPS % 2 != 0:
        count_down(work_sec)
        time_label.config(text="Work", fg=GREEN)
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        time_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        time_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        global marks
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=190 , pady=50, bg=YELLOW)


time_label = Label(text = "Timer", font = (FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
time_label.grid(column = 1, row = 0)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)
start_button.config(padx=10, pady=10)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
reset_button.config(padx=10, pady=10)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column = 1, row = 1)


window.mainloop()