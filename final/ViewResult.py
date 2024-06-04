#View Result
from tkinter import*
from PIL import Image,ImageTk  
from tkinter import ttk,messagebox
import sqlite3
class ViewClass:
    def __init__(self,home):
        self.home=home
        self.home.title("Student Result Management System")
        self.home.geometry("1200x500+80+170")
        self.home.config(bg="#172E36")
        self.home.focus_force()
        footer=Label(self.home,text="©Abhishek KS, 2024",font=("Calibri",13,"bold"),bg="#172E36",fg="white").pack(side=BOTTOM,fill=X)


    #Title of result
        title=Label(self.home,text="View Student Results",font=("Calibri",30,"bold"),bg="#172E36", fg="#D0A85B").place(x=0,y=0,relwidth=1,height=50)

    #Search
        self.var_search=StringVar()
        self.var_id=""

        lbl_select = Label(self.home,text="Enter Roll No.",font=("Calibri",20,"bold"),bg="#172E36", fg="#D0A85B").place(x=450,y=95)
        txt_select = Entry(self.home,textvariable=self.var_search,font=("Calibri",20),bg="White").place(x=650,y=100,width=180,height=35)

        btn_search=Button(self.home,text="Search",font=("Calibri",15,"bold"),bg="#D0A85B",fg="White",cursor="hand2",command=self.search).place(x=880,y=100,width=100,height=35)

        btn_clear=Button(self.home,text="Clear",font=("Calibri",15,"bold"),bg="#D0A85B",fg="White",cursor="hand2",command=self.clear).place(x=1000,y=100,width=100,height=35)

        lbl_roll = Label(self.home,text="Roll No.",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=200,y=310,width=190,height=90)
        lbl_name = Label(self.home,text="Name",font=("Calibri"),bg="white",bd=2,relief=GROOVE).place(x=390,y=310,width=190,height=90)
        lbl_course = Label(self.home,text="Course",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=580,y=310,width=190,height=90)
        lbl_marks = Label(self.home,text="Marks Obtained",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=770,y=310,width=190,height=90)
        lbl_full = Label(self.home,text="Total Marks",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=960,y=310,width=190,height=90)
        lbl_percentage = Label(self.home,text="Percentage",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=1150,y=310,width=190,height=90)

        self.roll = Label(self.home, font=("Calibri", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=200, y=400, width=190, height=90)
        self.name = Label(self.home, font=("Calibri", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=390, y=400, width=190, height=90)
        self.course = Label(self.home, font=("Calibri", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=580, y=400, width=190, height=90)
        self.full = Label(self.home, font=("Calibri", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.full.place(x=770, y=400, width=190, height=90)
        self.marks = Label(self.home, font=("Calibri", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=960, y=400, width=190, height=90)
        self.percentage = Label(self.home, font=("Calibri", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.percentage.place(x=1150, y=400, width=190, height=90)

        #Delete button
        btn_delete=Button(self.home,text="Delete",font=("Calibri",15,"bold"),bg="#D0A85B",fg="white",cursor="hand2",command=self.delete).place(x=700,y=550,width=150,height=35)


    #------------------------------
    def search(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.home)
            else:
                cur.execute("Select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row !=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.percentage.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record Found",parent=self.home) 
               
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")

    def delete(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search student result first",parent=self.home)
            else:
                cur.execute("Select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.home)
                else:
                    p=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.home)
                    if p==True:
                        cur.execute("Delete from result where rid=? ",(self.var_id,))
                        conn.commit()
                        messagebox.showinfo("Delete","Result deleted Successfully",parent=self.home)
                        self.clear() #We are calling clear because we declare show in to that
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    
if __name__=="__main__":
    home=Tk()
    obj=ViewClass(home)
    home.mainloop()