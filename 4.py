
#13123123123123123
from tkinter import *
class dlg:
    def __init__(self):
        self.frame=Tk()
        self.frame.title('123123')
        self.frame.geometry('600x300')
        self.label1=Label(self.frame,text='my label',width=20)
        # self.label1.place(x=100,y=100)
        self.input1_value=StringVar()
        self.input1=Entry(self.frame,width=20,textvariable=self.input1_value)
        # self.input1.place(x=100,y=200)
        self.btn1=Button(self.frame,text='计算',width=8,command=self.getValue)
        # self.btn1.place(x=250,y=200)
    
    def show(self):
        self.frame.mainloop()
        self.gui_arr()

    def getValue(self):
        print(self.input1_value.get())
        tt=self.input1_value.get()
        self.label1['text']=tt
    def gui_arr(self):
        self.label1.pack(side=TOP)
        self.input1.pack()
        self.btn1.pack()

if __name__ == "__main__":
    mydlg=dlg()
    mydlg.show()