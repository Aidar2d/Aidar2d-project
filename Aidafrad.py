import tkinter
from tkinter import ttk
def degenerator(dlina=14):
    import random
    password = ''
    alpha = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAMNBVCXZ!@#$%^&*()№;%:?*'
    for i in range(dlina):
        password = password + random.choice(alpha)
    entry.delete(0, 'end')
    entry.insert(0, password)
    return password
dlina = 10
window = tkinter.Tk()
window.title('Дегенератор пароля')
window.geometry('550x300')
button_stylee = ttk.Style()
button_stylee.configure('My.TButton',
                        font = ("Papyrus", 13))

entry = ttk.Entry(width=dlina, background="#0e00a3",foreground= "#0e00a3", font=("Papyrus", 19))
entry.pack()
entry.place(width=300, height=30, x = 127, y = 35)
button = ttk.Button(text='PON', command=degenerator, style='My.TButton')
button.place(width=130, height=20)
window["bg"] = "#6606c6"

button.pack()
window.resizable(False, False)

window.mainloop()





