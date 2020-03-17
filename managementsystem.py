from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Management System")

text_input = StringVar()
operator = ""

Tops = Frame(root, width = 1600, height = 50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height = 700, bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height = 700, bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)

# ========== TIME ==============

localtime=time.asctime(time.localtime(time.time()))

#=========== HEADER ============

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Management Systems", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial', 25, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1,column=0)

#=========== CALCULATOR ==========

def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

def Ref():
    x = random.randint(1, 123412)
    randomRef = str(x)
    rand.set(randomRef)

def qExt():
    root.destroy()

def Reset():
    rand= set("")
    Fries=set("")
    Burger=set("")
    Filet=set("")
    SubTotal=set("")
    Total=set("")
    Service_Charge=set("")
    Drinks=set("")
    Tax=set("")
    Cost=set("")
    Chicken_Burger=set("")
    Cheese_Burger=set("")




# ===================================================================

txtDisplay = Entry(f2,font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue", justify='right')

txtDisplay.grid(columnspan=4)

# =========Row 1 Calc============
btn7= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="7", bg="white", command=lambda:btnClick(7)).grid(row=1,column=0)
btn8= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="8", bg="white", command=lambda:btnClick(8)).grid(row=1,column=1)
btn9= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="9", bg= "white", command=lambda:btnClick(9)).grid(row=1,column=2)
Addition= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="+", bg="white", command=lambda:btnClick("+")).grid(row=1,column=3)
# =========Row 2 Calc============
btn4= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="4", bg="white", command=lambda:btnClick(4)).grid(row=2,column=0)
btn5= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="5", bg="white", command=lambda:btnClick(5)).grid(row=2,column=1)
btn6= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="6", bg= "white", command=lambda:btnClick(6)).grid(row=2,column=2)
Subtraction= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="-", bg="white", command=lambda:btnClick("-")).grid(row=2,column=3)
# =========Row 3 Calc============
btn1= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="1", bg="white", command=lambda:btnClick(1)).grid(row=3,column=0)
btn2= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="2", bg="white", command=lambda:btnClick(2)).grid(row=3,column=1)
btn3= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="3", bg= "white", command=lambda:btnClick(3)).grid(row=3,column=2)
Multiplication = Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="*", bg="white", command=lambda:btnClick("*")).grid(row=3,column=3)
 # =========Row 4 Calc============
btn0= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="0", bg="white", command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="C", bg="white", command=btnClearDisplay()).grid(row=4,column=1)
btnEquals= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="=", bg= "white", command=btnEqualsInput()).grid(row=4,column=2)
Division= Button(f2, padx=14, pady=14, bd=8, fg="black", font=('arial', 20, 'bold'),
             text="/", bg= "white", command=lambda:btnClick("/")).grid(row=4,column=2)

# ===================Items=========================

rand= StringVar()
Fries=StringVar()
Burger=StringVar()
Filet=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chicken_Burger=StringVar()
Cheese_Burger=StringVar()

lblReference = Label (f1, font=('arial', 20, 'bold'), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0,column=0)
txtReference= Button(f1, font=('arial', 20, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="powder blue", justify="right")
txtReference.grid(row=0,column=1)

lblFries = Label (f1, font=('arial', 20, 'bold'), text="French Fries", bd=16, anchor="w")
lblFries.grid(row=1,column=0)
txtFries= Button(f1, font=('arial', 20, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="powder blue", justify="right")
txtFries.grid(row=1,column=1)

lblBurger = Label (f1, font=('arial', 20, 'bold'), text="Hamburger", bd=16, anchor="w")
lblBurger.grid(row=2,column=0)
txtBurger= Button(f1, font=('arial', 20, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg="powder blue", justify="right")
txtBurger.grid(row=2,column=1)

lblFilet = Label (f1, font=('arial', 20, 'bold'), text="FIlet", bd=16, anchor="w")
lblFilet.grid(row=3,column=0)
txtFilet= Button(f1, font=('arial', 20, 'bold'), textvariable=Filet, bd=10, insertwidth=4, bg="powder blue", justify="right")
txtFilet.grid(row=3,column=1)

lblChicken = Label (f1, font=('arial', 20, 'bold'), text="Chicken", bd=16, anchor="w")
lblChicken.grid(row=4,column=0)
txtChicken= Button(f1, font=('arial', 20, 'bold'), textvariable=Chicken, bd=10, insertwidth=4, bg="powder blue", justify="right")
txtChicken.grid(row=4,column=1)

lblCheese = Label (f1, font=('arial', 20, 'bold'), text="Cheese", bd=16, anchor="w")
lblCheese.grid(row=5,column=0)
txtCheese= Button(f1, font=('arial', 20, 'bold'), textvariable=Cheese, bd=10, insertwidth=4, bg="powder blue", justify="right")
txtCheese.grid(row=5,column=1)

# ==========================Info 2======================================================




lblDrinks = Label (f1, font=('arial', 20, 'bold'), text="Drinks", bd=16, anchor="w")
lblDrinks.grid(row=0,column=2)
txtDrinks= Button(f1, font=('arial', 20, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="#fffff", justify="right")
txtDrinks.grid(row=0,column=3)

lblCost = Label (f1, font=('arial', 20, 'bold'), text="Cost", bd=16, anchor="w")
lblCost.grid(row=1,column=2)
txtCost= Button(f1, font=('arial', 20, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="#ffffff", justify="right")
txtCost.grid(row=1,column=3)

lblService = Label (f1, font=('arial', 20, 'bold'), text="Service", bd=16, anchor="w")
lblService.grid(row=2,column=2)
txtService= Button(f1, font=('arial', 20, 'bold'), textvariable=Service, bd=10, insertwidth=4, bg="#ffffff", justify="right")
txtService.grid(row=2,column=3)

lvlStateTax = Label (f1, font=('arial', 20, 'bold'), text="State Tax", bd=16, anchor="w")
lvlStateTax.grid(row=3,column=2)
txtStateTax= Button(f1, font=('arial', 20, 'bold'), textvariable=State, bd=10, insertwidth=4, bg="#ffffff", justify="right")
txtStateTax.grid(row=3,column=3)

lblSubTotal = Label (f1, font=('arial', 20, 'bold'), text="Sub Cost", bd=16, anchor="w")
lblSubTotal.grid(row=4,column=2)
txtSubTotal= Button(f1, font=('arial', 20, 'bold'), textvariable=Sub, bd=10, insertwidth=4, bg="#ffffff", justify="right")
txtSubTotal.grid(row=4,column=3)

lblTotalCost = Label (f1, font=('arial', 20, 'bold'), text="Total Cost", bd=16, anchor="w")
lblTotalCost.grid(row=5,column=2)
txtTotalCost= Button(f1, font=('arial', 20, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="#ffffff", justify="right")
txtTotalCost.grid(row=5,column=3)

# ==============Buttons==============================

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'), width=10, text="Total", bg="powder blue", command = Ref).grid(row=7, column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'), width=10, text="Reset", bg="powder blue", command = Reset).grid(row=7, column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'), width=10, text="Exit", bg="powder blue", command = Exit).grid(row=7, column=3)



root.mainloop()