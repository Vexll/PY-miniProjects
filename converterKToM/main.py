from tkinter import *


def main():
    window = Tk()
    window.title('Km to Mile Converter')
    # window.minsize(width=300, height=100)
    window.config(padx=20, pady=20)

    # Entry
    input_box = Entry(width=15)
    input_box.grid(column=1, row=0)

    # Label
    km_label = Label(text='Km', font=('Arial', 11))
    km_label.grid(column=2, row=0)

    # Label
    equality_text = Label(text='is equal to', font=('Arial', 11))
    equality_text.grid(column=0, row=1)

    # Label
    result = Label(text='0', font=('Arial', 11))
    result.grid(column=1, row=1)

    # Label
    miles = Label(text='Miles', font=('Arial', 11))
    miles.grid(column=2, row=1)

    # converter method
    def converter():
        if not input_box.get().isdigit():
            raise Exception("You must enter a number")

        user_input = int(input_box.get())
        new_result = user_input * 0.621371
        result.config(text=f"{new_result:.2f}")

    # Button
    cal_button = Button(text='calculate', command=converter)
    cal_button.grid(column=1, row=2)

    window.mainloop()


if __name__ == '__main__':
    main()
