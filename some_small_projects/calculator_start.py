#calculator
import tkinter
# crate icone
calculator = tkinter.Tk(className='Calculator')
calculator.config(background='grey')
calculator.geometry('350x450')

input_label = tkinter.Entry(calculator)
input_label.grid(row = 0, column = 0)



# starting mainloop and window output
calculator.mainloop()