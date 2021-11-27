import tkinter as tk


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
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer',fg=GREEN)
    
    check_mark_label.config(text='')
    global REPS
    REPS = 0

#     start_timer()
# # ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    if not REPS % 8:
        countdown(LONG_BREAK_MIN*60)
        title_label.config(text='Break',fg=RED)
        

    elif not REPS % 2:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text='Break',fg=PINK)
        
    
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text='Work',fg=GREEN)
        

            
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(sec):
    mins, secs = divmod(sec, 60)
    form_text = f'{mins:02d}:{secs:02d}'
    canvas.itemconfig(timer_text, text=form_text)
    if sec > 0:
        global timer
        timer = window.after(1000, countdown, sec - 1)
    else:
        start_timer()
        num_labels = check_mark * (REPS // 2)
        check_mark_label.config(text=num_labels)

# ---------------------------- UI SETUP ------------------------------- #
# window
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100,
              pady=50,
              bg=YELLOW)


# picture
canvas = tk.Canvas(width=200,
                   height=224,
                   bg=YELLOW,
                   highlightthickness=0)

tomato_img = tk.PhotoImage(file='21_30/day_28/tomato.png')
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100,132,
                   text='00:00', fill='white',
                   font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1,
            row=1)


# label
title_label = tk.Label(text='Timer',
                       font=(FONT_NAME, 40, 'bold'),
                       fg=GREEN,
                       bg=YELLOW)
title_label.grid(column=1,
                 row=0)

# buttons
start_button = tk.Button(text='Start',
                         font=(FONT_NAME, 16, 'bold'),
                         highlightthickness=0,
                         command=start_timer)
reset_button = tk.Button(text='Reset',
                         font=(FONT_NAME, 16, 'bold'),
                         highlightthickness=0,
                         command=reset_timer)

start_button.grid(column=0,
                  row=2)
reset_button.grid(column=2,
                  row=2)

# marks
check_mark = '✓'
check_mark_label = tk.Label(text='',
                            font=(FONT_NAME, 24, 'bold'),
                            fg=GREEN,
                            bg=YELLOW)
check_mark_label.grid(column=1,
                      row=3)

window.mainloop()