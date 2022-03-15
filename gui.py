import tkinter
import who_is_your_bff_engine as bff
import Plotting

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


go_button = tkinter.Button(root, height=2, width=12, font='Helvetica 12 bold',
                           command=lambda: Plotting.plot_cloud(),
                           text='Print Wordcloud')
go_button.grid(row=3, column=1)

exit_button = tkinter.Button(root, height=1, width=13, text='EXIT', command=root.quit, font='Helvetica 10 bold')
exit_button.grid(row=5, column=1)

root.mainloop()
