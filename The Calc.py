import tkinter as tk
import operator
root = tk.Tk()
root.title("The Calc")

root.iconbitmap('./Calculator.ico')
root.attributes('-toolwindow', True)
e=tk.Entry(root, borderwidth=9 ,width=45)
e.grid(row=0 ,column=1 ,columnspan=4)
global xx
global k
k=0

global answer

opp=[]
x=0
calc=[]

def n0():
  global xx
  calc.append("0")

  xx="0"
  e.insert("end","0")


def n1():
   global xx
   xx="1"
   calc.append("1")
   e.insert("end","1")

def n2():
 global xx
 xx="2"
 e.insert("end","2")
 calc.append("2")

def n3():
   global xx
   xx="3"
   e.insert("end","3")
   calc.append("3")

def n4():
   global xx
   xx="4"
   calc.append("4")
   e.insert("end","4")

def n5():
   global xx
   xx="5"
   calc.append("5")
   e.insert("end","5")

def n6():
   global xx
   xx="6"
   e.insert("end","6")
   calc.append("6")

def n7():
   global xx
   xx="7"
   e.insert("end","7")
   calc.append("7")

def n8():

   global xx
   xx="8"
   e.insert("end","8")
   calc.append("8")

def n9():
   global xx
   xx="9"
   e.insert("end","9")
   calc.append("9")

def addition():
 global xx
 xx="+"
 e.insert("end","+")


 calc.append(" ")
 opp.append("+")

def substraction():
   global xx
   xx="-"
   calc.append(" ")
   opp.append("-")
   e.insert("end","-")

def division():
   global xx
   xx="/"
   calc.append(" ")
   opp.append("/")
   e.insert("end","/")

def multiplication():
   global xx
   xx="*"
   calc.append(" ")
   opp.append("*")
   e.insert("end","*")

def decimal():
   global xx
   xx="."
   opp.append(".")
   e.insert("end",".")






def equal():
  global k
  numbers= ''.join(calc)
  num=numbers.split()
  l=len(num)

  if l==2:
   num1=int(num[0])
   num2=int(num[1])
   if opp[0]=="+":

        answer=num1+num2
   if opp[0]=="-":

        answer=num1-num2
   if opp[0]=="*":

        answer=num1*num2
   if opp[0]=="/":

        answer=num1/num2


   e.insert("end","="+str(answer))



  if l==3:

   opp.clear()
   calc.clear()
   e.delete(0,'end')

   e.insert(0,"this is only supporting one operation")
   k=1



  opp.clear()
  calc.clear()

  k=1

def out():
 global k
 if k==1:

  opp.clear()
  calc.clear()
  e.delete(0,'end')
  k=0

def clear():
  opp.clear()
  calc.clear()
  e.delete(0,'end')
  k=0

#add append to calc with a spce to divide toletters,then join ,and split

one=tk.Button(root,text="1",width=10,command=lambda:[out(),n1()])
two=tk.Button(root,text="2",width=10,command=lambda:[out(),n2()])
three=tk.Button(root,text="3",width=10,command=lambda:[out(),n3()])
four=tk.Button(root,text="4",width=10,command=lambda:[out(),n4()])
five=tk.Button(root,text="5",width=10,command=lambda:[out(),n5()])
six=tk.Button(root,text="6",width=10,command=lambda:[out(),n6()])
seven=tk.Button(root,text="7",width=10,command=lambda:[out(),n7()])
eight=tk.Button(root,text="8",width=10,command=lambda:[out(),n8()])
nine=tk.Button(root,text="9",width=10,command=lambda:[out(),n9()])
add=tk.Button(root, text="+",width=10,command=lambda:[out(),addition()])
substract=tk.Button(root, text="-",width=10,command=lambda:[out(),substraction()])
multiply=tk.Button(root, text="*",width=10,command=lambda:[out(),multiplication()])
divide=tk.Button(root, text="/",width=10,command=lambda:[out(),division()])
equal=tk.Button(root,text="=",width=10,command= equal  )
zero=tk.Button(root,text="0",width=10,command=lambda:[out(),n0()])
decimal=tk.Button(root,text="clear",width=10,command=lambda:[out(),clear()])



one.grid(row=3, column=1)
two.grid(row=3, column=2)
three.grid(row=3, column=3)

four.grid(row=2, column=1)
five.grid(row=2, column=2)
six.grid(row=2, column=3)

seven.grid(row=1, column=1)
eight.grid(row=1, column=2)
nine.grid(row=1, column=3)

zero.grid(row=4, column=2)

add.grid(row=1, column=4)
substract.grid(row=2,column=4)
multiply.grid(row=3,column=4)
divide.grid(row=4,column=4)
decimal.grid(row=4,column=1)

equal.grid(row=4, column=3)

root.mainloop()
