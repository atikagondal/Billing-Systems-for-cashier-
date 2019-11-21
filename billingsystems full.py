from tkinter import*
import random
import time;
import datetime

root =Tk()
root.geometry("1350x650+0+0")
root.title("Billing Systems")


Tops =Frame(root, width=1350, height =100, bd=8, relief="raise")
Tops.pack(side=TOP)

f1 =Frame(root, width=900, height =650, bd=8, relief="raise")
f1.pack(side=LEFT)

f1a =Frame(f1, width=900, height =330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a =Frame(f1, width=900, height =320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)

f1aa =Frame(f1a, width=400, height =430, bd=8, relief="raise")
f1aa.pack(side=LEFT)

f1ab =Frame(f1a, width=400, height =430, bd=8, relief="raise")
f1ab.pack(side=RIGHT)


f2aa =Frame(f2a, width=450, height =330, bd=8, relief="raise")
f2aa.pack(side=LEFT)
f2ab =Frame(f2a, width=450, height =330, bd=8, relief="raise")
f2ab.pack(side=LEFT)

f2 =Frame(root, width=440, height =650, bd=8, relief="raise")
f2.pack(side=LEFT)

lblInfo=Label(Tops, font=('arial',60,'bold'),text="        Online Billing Systems         ",bd=10, anchor='w')
lblInfo.grid(row=0,colum=0) 

#__________________________________________________________Calculator________________________________________________________________________________
text_Input=StringVar()
operator=""

def btnClick(numbers):
    global operator
    operator = operator +str(numbers)
    text_Input.set(operator)

    def btnClearDisplay():
        global operator
        operator=""
        text_Input.set("")

        def btnEqualsInput():
         global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator=""


txtDisplay = Entry(f2,font=('arial',60,'bold'), textvariable=text_Input, bd=40, insertwidth=6,justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="7")
btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="8")
btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="9")
btPlus=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),text="+")

#-------------------------------------------------------------------------------------------------------------
btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="6")
btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="5")
btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="4")
btnSub=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="-")
#-----------------------------------------------------------------------------------------------------------------
btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="3")
btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="2")
btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="1")
btnMult=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="*")
#-------------------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="0")
btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="C")
btnEqual=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="=")
                
btnDIV=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="/")

#------------------------------------------------------------------------              

lblRef=label(f1aa,font=('arial',16,'bold') ,text="Epler", bd=16, justify= 'left')
lblRef.grid(row=0,column=0)

txtRef=Entry(f1aa,font=('arial',16,'bold') ,text="Appelsiner", bd=10, insertwidth=2, justify= 'left')
txtRef.grid(row=0,column=1)

lblRef=label(f1aa,font=('arial',16,'bold') ,text="Epler", bd=16, justify= 'left')
lblRef.grid(row=1,column=0)

txtRef=Entry(f1aa,font=('arial',16,'bold') ,text="Appelsiner", bd=10, insertwidth=2, justify= 'left')
txtRef.grid(row=0,column=1)

lblCarpets=label(f1aa,font=('arial',16,'bold') ,text="Epler", bd=16, justify= 'left')
lblCarpets.grid(row=1,column=1)

txtRef=Entry(f1aa,font=('arial',16,'bold') ,text="Appelsiner", bd=10, insertwidth=2, justify= 'left')
txtRef.grid(row=2,column=1)

#--------------------------Orderinformation f1ab-------------------------------------------------------------------------------------------------

lblDateof



root.mainloop()
               
