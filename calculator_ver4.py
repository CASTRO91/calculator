from tkinter import *


class Calcul:


    def mathematical_action(self, signs: str, sign: str):
        self.signs = signs
        self.sign = sign
        Calcul().alert_button()
        if inputbox_invisible_2.get() in signs and len(inputbox_invisible_1.get()) != 0 and len(
                inputbox.get()) == 0 and inputbox_invisible_3.get() != 'double sign':
            inputbox_invisible_2.delete(0, END)
            inputbox_invisible_2.insert(1, sign)
        elif inputbox_invisible_2.get() in signs and len(inputbox_invisible_1.get()) != 0 and len(
                inputbox.get()) != 0 and inputbox_invisible_3.get() == 'double sign':
            inputbox_invisible_2.delete(0, END)
            inputbox_invisible_2.insert(1, sign)
        elif len(inputbox_invisible_2.get()) == 0 and len(inputbox_invisible_1.get()) == 0:
            inputbox_invisible_1.insert(1, inputbox.get())
            inputbox.delete(0, END)
            inputbox_invisible_2.insert(1, sign)
        elif inputbox_invisible_2.get() in sign + signs and len(inputbox_invisible_1.get()) != 0 and len(
                inputbox.get()) != 0:
            Calcul().equal()
            inputbox_invisible_2.insert(1, sign)
            inputbox_invisible_1.insert(1, inputbox.get())
            inputbox_invisible_3.insert(1, 'double sign')

    @staticmethod
    def del_ac():
        inputbox.delete(0, END)
        inputbox_invisible_1.delete(0, END)
        inputbox_invisible_2.delete(0, END)
        inputbox_invisible_3.delete(0, END)

    @staticmethod
    def messages():
        if inputbox_invisible_3.get() == 'double sign':
            inputbox_invisible_3.delete(0, END)
            inputbox.delete(0, END)
        if inputbox_invisible_3.get() == 'zero sign':
            inputbox_invisible_3.delete(0, END)
            inputbox.delete(0, END)

    @staticmethod
    def alert_button():
        if inputbox.get() == 'Cannot divide by zero':
            Calcul().del_ac()
        if inputbox.get() == 'Invalid input':
            Calcul().del_ac()

    @staticmethod
    def one():
        Calcul().messages()
        Calcul().alert_button()
        inputbox.insert(END, '1')

    @staticmethod
    def two():
        Calcul().messages()
        Calcul().alert_button()
        inputbox.insert(END, '2')

    @staticmethod
    def three():
        Calcul().messages()
        Calcul().alert_button()
        inputbox.insert(END, '3')

    @staticmethod
    def four():
        Calcul().messages()
        Calcul().alert_button()
        inputbox.insert(END, '4')

    @staticmethod
    def five():
        Calcul().messages()
        Calcul().alert_button()
        inputbox.insert(END, '5')

    @staticmethod
    def six():
        Calcul().messages()
        Calcul().alert_button()
        inputbox.insert(END, '6')

    @staticmethod
    def seven():
        Calcul().messages()
        Calcul().alert_button()
        inputbox.insert(END, '7')

    @staticmethod
    def eight():
        Calcul().messages()
        Calcul().alert_button()
        inputbox.insert(END, '8')

    @staticmethod
    def nine():
        Calcul().messages()
        Calcul().alert_button()
        inputbox.insert(END, '9')

    @staticmethod
    def zero():
        Calcul().messages()
        Calcul().alert_button()
        inputbox.insert(END, '0')

    @staticmethod
    def point():
        Calcul().alert_button()
        if len(inputbox.get()) == 0:
            inputbox.insert(END, '0.')
        elif '.' not in inputbox.get():
            inputbox.insert(END, '.')

    @staticmethod
    def pm():
        Calcul().alert_button()
        if '.' in inputbox.get():
            rez = float(inputbox.get()) * -1
            inputbox.delete(0, END)
            inputbox.insert(1, str(rez))
        else:
            rez = int(inputbox.get()) * -1
            inputbox.delete(0, END)
            inputbox.insert(1, str(rez))

    @staticmethod
    def plus():
        Calcul().mathematical_action('-/*^', '+')

    @staticmethod
    def minus():
        Calcul().mathematical_action('+/*^', '-')

    @staticmethod
    def multi():
        Calcul().mathematical_action('-/+^', '*')

    @staticmethod
    def divide():
        Calcul().mathematical_action('-+*^', '/')

    @staticmethod
    def sqrt():
        Calcul().alert_button()
        if '-' in inputbox.get():
            Calcul().del_ac()
            inputbox.insert(1, 'Invalid input')
        elif len(inputbox_invisible_2.get()) != 0 and len(inputbox_invisible_1.get()) != 0 and len(inputbox.get()) != 0:
            Calcul().equal()
            if '-' in inputbox.get():
                Calcul().del_ac()
                inputbox.insert(1, 'Invalid input')
            else:
                rez = inputbox.get()
                Calcul().del_ac()
                inputbox.insert(1, str(float(rez) ** 0.5))
        elif len(inputbox_invisible_2.get()) == 0 and len(inputbox_invisible_1.get()) == 0 and len(inputbox.get()) != 0:
            if '-' in inputbox.get():
                Calcul().del_ac()
                inputbox.insert(1, 'Invalid input')
            else:
                rez = inputbox.get()
                Calcul().del_ac()
                inputbox.insert(1, str(float(rez) ** 0.5))

    def equal(self):
        if len(inputbox_invisible_2.get()) != 0 and len(inputbox_invisible_1.get()) != 0 and len(inputbox.get()) == 0:
            rez = inputbox_invisible_1.get()
            Calcul().del_ac()
            inputbox.insert(1, rez)

        if inputbox_invisible_2.get() == '+':
            if '.' not in inputbox.get() and '.' not in inputbox_invisible_1.get():
                self.value_1 = inputbox.get()
                inputbox.delete(0, END)
                rez = int(self.value_1) + int(inputbox_invisible_1.get())
                Calcul().del_ac()
                inputbox.insert(1, str(rez))
            else:
                self.value_1 = inputbox.get()
                inputbox.delete(0, END)
                rez = float(self.value_1) + float(inputbox_invisible_1.get())
                Calcul().del_ac()
                inputbox.insert(1, str(rez))
        elif inputbox_invisible_2.get() == '-':
            if '.' not in inputbox.get() and '.' not in inputbox_invisible_1.get():
                self.value_1 = inputbox.get()
                inputbox.delete(0, END)
                rez = int(inputbox_invisible_1.get()) - int(self.value_1)
                Calcul().del_ac()
                inputbox.insert(1, str(rez))
            else:
                self.value_1 = inputbox.get()
                inputbox.delete(0, END)
                rez = float(inputbox_invisible_1.get()) - float(self.value_1)
                Calcul().del_ac()
                inputbox.insert(1, str(rez))
        elif inputbox_invisible_2.get() == '*':
            if '.' not in inputbox.get() and '.' not in inputbox_invisible_1.get():
                self.value_1 = inputbox.get()
                inputbox.delete(0, END)
                rez = int(inputbox_invisible_1.get()) * int(self.value_1)
                Calcul().del_ac()
                inputbox.insert(1, str(rez))
            else:
                self.value_1 = inputbox.get()
                inputbox.delete(0, END)
                rez = float(inputbox_invisible_1.get()) * float(self.value_1)
                Calcul().del_ac()
                inputbox.insert(1, str(rez))
        elif inputbox_invisible_2.get() == '/':
            self.value_1 = inputbox.get()
            inputbox.delete(0, END)
            try:
                rez = float(inputbox_invisible_1.get()) / float(self.value_1)
                Calcul().del_ac()
                inputbox.insert(1, str(rez))
            except ZeroDivisionError:
                inputbox.insert(1, 'Cannot divide by zero')

    @staticmethod
    def equal_button():
        Calcul().alert_button()
        if inputbox_invisible_2.get() == '-' and len(inputbox_invisible_1.get()) == 0 and len(inputbox.get()) != 0:
            inputbox_invisible_1.insert(1, '0')
        if inputbox_invisible_3.get() != 'zero sign':
            Calcul().equal()
            inputbox_invisible_3.insert(1, 'zero sign')



x = 370
y = 515
window = Tk()
window.title('Calculator')
window.geometry(f'{x}x{y}')
window.resizable(False, False)

inputbox = Entry(borderwidth=5, font='arial 25', justify=RIGHT)

inputbox.grid(row=0, column=0, columnspan=4)

inputbox_invisible_1 = Entry()
inputbox_invisible_1.grid(row=0, column=8, columnspan=1)
inputbox_invisible_2 = Entry()
inputbox_invisible_2.grid(row=1, column=8, columnspan=1)
inputbox_invisible_3 = Entry()
inputbox_invisible_3.grid(row=2, column=8, columnspan=1)

button_AC = Button(window, text='AC', width=3, height=1, font='arial 35', command=Calcul().del_ac)
button_AC.grid(row=1, column=0)

button_SQRT = Button(window, text='√x', width=3, height=1, font='arial 35', command=Calcul().sqrt)
button_SQRT.grid(row=1, column=1)

button_PM = Button(window, text='+/-', width=3, height=1, font='arial 35', command=Calcul().pm)
button_PM.grid(row=1, column=2)

button_DIVIDE = Button(window, text='/', width=3, height=1, font='arial 35', command=Calcul().divide)
button_DIVIDE.grid(row=1, column=3)

button_7 = Button(window, text='7', width=3, height=1, font='arial 35', command=Calcul().seven)
button_7.grid(row=2, column=0)

button_8 = Button(window, text='8', width=3, height=1, font='arial 35', command=Calcul().eight)
button_8.grid(row=2, column=1)

button_9 = Button(window, text='9', width=3, height=1, font='arial 35', command=Calcul().nine)
button_9.grid(row=2, column=2)

button_MULTI = Button(window, text='X', width=3, height=1, font='arial 35', command=Calcul().multi)
button_MULTI.grid(row=2, column=3)

button_4 = Button(window, text='4', width=3, height=1, font='arial 35', command=Calcul().four)
button_4.grid(row=3, column=0)

button_5 = Button(window, text='5', width=3, height=1, font='arial 35', command=Calcul().five)
button_5.grid(row=3, column=1)

button_6 = Button(window, text='6', width=3, height=1, font='arial 35', command=Calcul().six)
button_6.grid(row=3, column=2)

button_MINUS = Button(window, text='-', width=3, height=1, font='arial 35', command=Calcul().minus)
button_MINUS.grid(row=3, column=3)

button_1 = Button(window, text='1', width=3, height=1, font='arial 35', command=Calcul().one)
button_1.grid(row=4, column=0)

button_2 = Button(window, text='2', width=3, height=1, font='arial 35', command=Calcul().two)
button_2.grid(row=4, column=1)

button_3 = Button(window, text='3', width=3, height=1, font='arial 35', command=Calcul().three)
button_3.grid(row=4, column=2)

button_PLUS = Button(window, text='+', width=3, height=1, font='arial 35', command=Calcul().plus)
button_PLUS.grid(row=4, column=3)

button_0 = Button(window, text='0', width=6, height=1, font='arial 35', command=Calcul().zero)
button_0.grid(row=5, column=0, columnspan=2)

button_POINT = Button(window, text=',', width=3, height=1, font='arial 35', command=Calcul().point)
button_POINT.grid(row=5, column=2)

button_EQUAL = Button(window, text='=', width=3, height=1, font='arial 35', command=Calcul().equal_button)
button_EQUAL.grid(row=5, column=3)


window.mainloop()
