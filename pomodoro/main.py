from tkinter import *

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
check_mark = '✔'
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global check_mark, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    mark_label.config(text='')
    check_mark = '✔'
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, check_mark
    if reps == 7:
        reps = 0
        mark_label.config(text='')
        check_mark = '✔'
    else:
        if reps % 2 == 0:
            count_down(WORK_MIN * 60)
            title_label.config(text='Work', fg=GREEN)
        elif reps % 2 == 1 and reps != 7:
            count_down(SHORT_BREAK_MIN * 60)
            title_label.config(text='Break', fg=PINK)
            mark_label.config(text=check_mark)
            check_mark += '✔'
        else:
            count_down(LONG_BREAK_MIN * 60)
            title_label.config(text='Break', fg=RED)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# title label
title_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

# canvas
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 111, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

# start button
start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

# reset button
reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

# check mark label
mark_label = Label(text='', font=(FONT_NAME, 13), fg=GREEN, bg=YELLOW)
mark_label.grid(column=1, row=3)
window.mainloop()
