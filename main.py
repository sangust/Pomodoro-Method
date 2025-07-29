#Bibliotecas 
#A fazer, importar somente o necessario para não importar uma bb inteira
from time import sleep
from datetime import datetime
from tkinter import *


#definição do tempo de estudo
during_time_fix = 30 * 60  
during_time = 30 * 60

resting_during_time_fix = 60 * 5 
resting_during_time = 60 * 5

counter = 0


#Funções
#Definir funções especificamente p o TKinter
def current_time():
    hora_atual = datetime.now().strftime("%H:%M:%S")
    show_real_time.config(text=f'current_time: {hora_atual}')
    gui_pomodoro_method.after(1000, current_time)

def studying_time():
    global during_time
    global counter

    if during_time > 0:
        minute = during_time // 60
        second = during_time % 60
        show_cronogram.config(text=f'--> {minute:02}:{second:02} <--')
        during_time -= 1
        gui_pomodoro_method.after(1000, studying_time)
    
    elif during_time < 1:
        counter += 1
        gui_pomodoro_method.after(1000, lambda: show_cronogram.config(text=f'Now the resting time will Start Over.'))
        gui_pomodoro_method.after(5500, resting_time)
    

def resting_time():
    global during_time
    global during_time_fix
    global resting_during_time 
    global resting_during_time_fix
    if resting_during_time > 0:
        minute = resting_during_time // 60
        second = resting_during_time % 60
        show_cronogram.config(text=f'--> {minute:02}:{second:02} <--')
        resting_during_time -= 1
        gui_pomodoro_method.after(1000, resting_time)
    else:
        show_cronogram.config(text='The resting time has ended, now the studying time is up!')
        during_time = during_time_fix
        resting_during_time = resting_during_time_fix
        gui_pomodoro_method.after(5000, studying_time)


def cronogram():
    start_cronogram.destroy()
    show_cronogram.place(relx=0.5, rely=0.5, anchor='center')
    global counter
    if counter != 4:     
        show_cronogram.config(text=f'The cronogram will start in:')
        gui_pomodoro_method.after(1500, lambda: show_cronogram.config(text='The cronogram will start in: 3'))
        gui_pomodoro_method.after(2500, lambda: show_cronogram.config(text='The cronogram will start in: 2'))
        gui_pomodoro_method.after(3500, lambda: show_cronogram.config(text='The cronogram will start in: 1'))
        gui_pomodoro_method.after(4500, studying_time)
    else:
        global resting_during_time
        resting_during_time *= 4
        show_cronogram.config(text=f'Agora iniciará o tempo de descanso prolongado')
        gui_pomodoro_method.after(1000, resting_time)



#TELA DO CRONOMETRO
gui_pomodoro_method = Tk()
gui_pomodoro_method.title("Pomodoro Method")
gui_pomodoro_method.geometry("320x150")

description = Label(gui_pomodoro_method, text='An cronogram method as Pomodoro Technique', font=("Arial Bold", 11))
description.pack(side=TOP)

start_cronogram = Button(gui_pomodoro_method, text='Start Timer', command=cronogram)
start_cronogram.place(relx=0.5, rely=0.5, anchor='center')

show_cronogram = Label(gui_pomodoro_method, text='')

show_real_time = Label(gui_pomodoro_method, text='')
show_real_time.pack(side=BOTTOM)

current_time()
gui_pomodoro_method.mainloop()

