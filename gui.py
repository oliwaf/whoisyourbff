import tkinter
from tkinter import filedialog
import Plotting
import matplotlib.pyplot as plt
import Messenger_playground as Msg
import who_is_your_bff_engine

def printValue():
    pname = who_is_your_bff_engine.get_path()
    tkinter.Label(root, text=f'PATH: {pname}', pady=20,).grid(row=2, column=1)

name = 'Who is Your BFF?'
root = tkinter.Tk()
root.title(name)
root.geometry('230x410+1400+150')
root.resizable(True, True)
root['padx'] = 16
root['pady'] = 16
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=2)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)

select_button = tkinter.Button(root, height=1, width=28, text='See who is your Best Friend',
                                      font='Helvetica 10 bold', command=lambda: Plotting.plot_bar())
select_button.grid(row=0, column=1)


select_friend_button = tkinter.Button(root, height=1, width=18, text='Select your friend',
                                      font='Helvetica 10 bold', command=lambda: printValue())
select_friend_button.grid(row=1, column=1)

wordcloud_button = tkinter.Button(root, height=2, width=12, font='Helvetica 12 bold',
                           command=lambda: [Plotting.plot_worldcloud(),Plotting.plot_line_days(),Plotting.plot_line_hours()],
                           text='Print plots')
wordcloud_button.grid(row=3, column=1)

exit_button = tkinter.Button(root, height=1, width=12, text='EXIT', command=root.quit, font='Helvetica 10 bold')
exit_button.grid(row=5, column=1)


root.mainloop()

