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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(f"{timer}") #stops the timer
    timer_label.config(text="Timer", fg=GREEN) #resets the timer label
    #resetting the checkmarks
    check_label.config(text="")
    #changing the timer 
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work = WORK_MIN * 60
    short_brk = SHORT_BREAK_MIN * 60
    long_brk = LONG_BREAK_MIN * 60
    reps +=1
    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work)

    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(long_brk)
        reps = 0

    elif reps % 2 == 0 and reps != 8:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_brk)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
            count_sec = f"0{count_sec}"
    
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:  #checking when the timer hits zero(0)
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_label.config(text=marks)         
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=100, bg=YELLOW)


timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=3, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=3, row=2)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=2, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=4, row=3)

check_label = Label(fg=GREEN, bg=YELLOW,font=(FONT_NAME, 15, "bold"))
check_label.grid(column=3, row=4)

window.mainloop()