import tkinter.messagebox
from tkinter import *
from  tkinter import ttk
from functools import wraps
class calculator(Tk):
    def __init__(self):
        #setting
        Tk.__init__(self)
        self.title("calclator")
        # self.geometry("{}x{}".format("380", "555"))
        self.geometry("{}x{}".format("720","490"))
        self.resizable(width=False,height=False)
        self.configure(bg="gray")
        #variable
        self.calcuting_var=StringVar()
        #frame
        self.main_frame=Frame(self,width=420,height=500,bg="gray")
        self.main_frame.pack(side="left",fill=Y,expand=True)
        self.frame_1=Frame(self.main_frame,width=400,height=150 ,bg = "gray")
        self.frame_1.grid(row=0,column=0,sticky="nw",padx=2,pady=2)
        self.lable_frame_1=LabelFrame(self.frame_1,text="result",width=400,height=130,bg="white" ,font=("Ariel", 11))
        self.lable_frame_1.grid(row=0,column=0)
        self.frame_2 = Frame(self.main_frame, width=400, height=100 ,bg = "gray")
        self.frame_2.grid(row=1,column=0,sticky="nw",padx=2,pady=2)
        self.frame_3 = Frame(self.main_frame, width=400, height=100 ,bg = "gray")
        self.frame_3.grid(row=2,column=0,sticky="nw",padx=2,pady=2)
        self.frame_4 = Frame(self.main_frame, width=400, height=100 ,bg = "gray")
        self.frame_4.grid(row=3,column=0,sticky="nw",padx=2,pady=2)
        self.frame_5 = Frame(self.main_frame, width=400, height=100 ,bg = "gray")
        self.frame_5.grid(row=4,column=0,sticky="nw",padx=2,pady=2)
        self.frame_6=Frame(self,width=250,height=400,bg="gray")
        self.frame_6.pack(side="left",fill=Y)
        #display_lable
        self.lable_calculating=Label(self.lable_frame_1, width=33,font=("Ariel", 15),bg="white")
        self.lable_calculating.pack(side="top",padx=50,pady=30)
        self.lable_result=Label(self.lable_frame_1, width=33,font=("Ariel", 15),bg="white")
        self.lable_result.place(x=100,y=50)

        #button_row_1
        self.btn_clear=Button(self.frame_2,text="C",command=self.clear_btn,width=9,height=4,font=("Ariel", 11, "bold"))
        self.btn_clear.pack(side="left",pady=2,padx=2)
        self.btn_one = Button(self.frame_2, text="1", command=self.one_btn,width=9,height=4,font=("Ariel", 11, "bold"))
        self.btn_one.pack(side="left",pady=2,padx=2)
        self.btn_two = Button(self.frame_2, text="2", command=self.two_btn,width=9,height=4,font=("Ariel", 11, "bold"))
        self.btn_two.pack(side="left",pady=2,padx=2)
        self.btn_mult = Button(self.frame_2, text="x", command=self.plus_btn,width=9,height=4,font=("Ariel", 11, "bold"))
        self.btn_mult.pack(side="left",pady=2,padx=2)
        self.btn_mode = Button(self.frame_2, text="%", command=self.plus_btn, width=9, height=4,font=("Ariel", 11, "bold"))
        self.btn_mode.pack(side="left", pady=2, padx=2)
        #button_row_2
        self.btn_three = Button(self.frame_3, text="3", command=self.three_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_three.pack(side="left", pady=2, padx=2)
        self.btn_four = Button(self.frame_3, text="4", command=self.four_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_four.pack(side="left", pady=2, padx=2)
        self.btn_five = Button(self.frame_3, text="5", command=self.five_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_five.pack(side="left", pady=2, padx=2)
        self.btn_division = Button(self.frame_3, text="/", command=self.mines_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_division.pack(side="left", pady=2, padx=2)
        self.btn_root = Button(self.frame_3, text="√", command=self.mines_btn, width=9, height=4,font=("Ariel", 11, "bold"))
        self.btn_root.pack(side="left", pady=2, padx=2)
        #button_row_3
        self.btn_six = Button(self.frame_4, text="6", command=self.six_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_six.pack(side="left", pady=2, padx=2)
        self.btn_seven = Button(self.frame_4, text="7", command=self.seven_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_seven.pack(side="left", pady=2, padx=2)
        self.btn_eight = Button(self.frame_4, text="8", command=self.eight_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_eight.pack(side="left", pady=2, padx=2)
        self.btn_plus = Button(self.frame_4, text="+", command=self.mult_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_plus.pack(side="left", pady=2, padx=2)
        self.btn_factorial = Button(self.frame_4, text="x!", command=self.mult_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_factorial.pack(side="left", pady=2, padx=2)
        #button_row_4
        self.btn_nine = Button(self.frame_5, text="9", command=self.nine_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_nine.pack(side="left", pady=2, padx=2)
        self.btn_zero = Button(self.frame_5, text="0", command=self.zero_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_zero.pack(side="left", pady=2, padx=2)
        self.btn_dot= Button(self.frame_5, text=".", command=self.dot_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_dot.pack(side="left", pady=2, padx=2)
        self.btn_mines = Button(self.frame_5, text="_", command=self.dive_btn, width=9, height=4, font=("Ariel", 11, "bold"))
        self.btn_mines.pack(side="left", pady=2, padx=2)
        self.btn_equal = Button(self.frame_5, text="=", command=self.test, width=9, height=4,font=("Ariel", 11, "bold"))
        self.btn_equal.pack(side="left", pady=2, padx=2)
        #history_of_calculting
        self.note_book=self.note_book_maker()
        #button_clear_history
        self.btn_clear_history=Button(self.frame_6,text="clear",width=25,height=8,font=("Arial",10,"bold"))
        self.btn_clear_history.pack(side="top",pady=2)

    #decorator_of_keyboard
    def display_number(func):
        @wraps(func)
        def wrapper(self):
            number=func(self)
            if number == "":
                self.lable_calculating.configure(text="")
                self.calcuting_var.set("")
                self.lable_result.configure(text="")
            else:
                lable=(self.calcuting_var.get())+number
                self.calcuting_var.set(lable)
                self.lable_calculating.configure(text=lable)
        return wrapper


    @display_number
    def clear_btn(self):
        return ""

    @display_number
    def one_btn(self):
        return "1"

    @display_number
    def two_btn(self):
        return "2"

    @display_number
    def plus_btn(self):
        return "+"
    @display_number
    def three_btn(self):
        return "3"

    @display_number
    def four_btn(self):
        return "4"

    @display_number
    def five_btn(self):
        return "5"

    @display_number
    def mines_btn(self):
        return "-"
    @display_number
    def six_btn(self):
        return "6"

    @display_number
    def seven_btn(self):
        return "7"

    @display_number
    def eight_btn(self):
        return "8"

    @display_number
    def mult_btn(self):
        return "x"
    @display_number
    def nine_btn(self):
        return "9"

    @display_number
    def zero_btn(self):
        return "0"

    @display_number
    def dot_btn(self):
        return "."

    @display_number
    def dive_btn(self):
        return "/"
    def error_function(self,ms):
        if ms == "error":
            tkinter.messagebox.showerror("error","some thing is wrong")
        elif ms == "dividesion_error":
            tkinter.messagebox.showerror("divisoinerror","yoc can't use zero for second number")

    def equal_btn (self):
        number=self.calcuting_var.get()
        self.calcuting_var.set("")
        for i in number:
            if i in ["/","x","+","-"]:
                operator=i
        numbers=number.split(operator)
        if operator == "x":
            try:
                result=float(numbers[0])*float(numbers[1])
                self.lable_result.configure(text=str(result))
            except:
                self.error_function("error")
        elif operator == "+":
            try:
                result = float(numbers[0]) +float(numbers[1])
                self.lable_result.configure(text=str(result))
            except:
                self.error_function("error")
        elif operator == "-":
            try:
                result = float(numbers[0]) - float(numbers[1])
                self.lable_result.configure(text=str(result))
            except:
                self.error_function("error")
                self.lable_result.set("")
        else:
            if float(numbers[1])==0:
                self.error_function("dividesion_error")
            try:
                result = float(numbers[0]) /float(numbers[1])
                self.lable_result.configure(text=str(result))
            except:
                self.error_function("error")
    def test(self):
        print(self.winfo_width(),self.winfo_height())
        # self.note_book.insert(END,"3 X 4= 12")
    def note_book_maker(self):
        note_book=ttk.Notebook(self.frame_6,width=200,height=410)
        note_book.pack(fill=BOTH,pady=5,padx=5)
        note_book_frame_1=Frame(note_book)
        note_book.add(note_book_frame_1,text="history")
        list_box=Listbox(note_book_frame_1,width=180,height=400,font=("Arial",12,"bold"))
        list_box.pack(side="top",fill=BOTH,expand=True)
        return list_box
if  __name__ == "__main__":
    app=calculator()
    app.mainloop()