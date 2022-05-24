from cmath import sqrt
import tkinter as tk
import operator
root = tk.Tk()
root.title("The Calc")

root.iconbitmap('./Calculator.ico')
root.attributes('-toolwindow', True)
e=tk.Entry(root, borderwidth=9 ,width=60)
e.grid(row=0 ,column=1 ,columnspan=5)
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

def square():
   global xx
   xx="square"
   
   opp.append("square")
   e.insert("end"," square ")
def squreroot():
   global xx
   xx="squareroot"
   calc.append(" ")
   opp.append("squareroot")
   e.insert("end"," square root ")
def factors():
   global xx
   xx="factors"
   calc.append(" ")
   opp.append("factors")
   e.insert("end"," factors ")
def HCF():
   global xx
   xx="HCF"
   calc.insert(1," ")
   opp.append("HCF")
   e.insert("end"," HCF ")




def equal():
  global k
  numbers= ''.join(calc)
  num=numbers.split()
  l=len(num)
  if l==1:
   num1=int(num[0])
   if opp[0]=="square":
        print("y")
        answer=num1*num1
   if opp[0]=="squareroot":
        answer=sqrt(num1)
   if opp[0]=="factors":
         input=num1
         numbers = range(1,int(input)+1)
         answer=[]
         for a in numbers:
            b=input/a
            if round(b)==b:
              
              answer.append(round(b))
   e.insert("end","="+str(answer))
     

  if l==2:
   num1=int(num[0])
   num2=int(num[1])
   if opp[0]=="+":

        answer=num1+num2
   elif opp[0]=="-":

        answer=num1-num2
   elif opp[0]=="*":

        answer=num1*num2
   elif opp[0]=="/":
      answer=num1/num2
   elif opp[0]=="HCF":
         
         n1=num1
         n2=num2
         fact1=[]
         input1=int(n1)
         numbers1 = range(1,int(input1)+1)

         for a1 in numbers1:
            b1=input1/a1
            if round(b1)==b1:
               fact1.append(round(b1))

         fact2=[]
         input2=int(n2)
         numbers2 = range(1,int(input2)+1)

         for a2 in numbers2:
            b2=input2/a2
            if round(b2)==b2:
               fact2.append(round(b2))
         len1=len(fact1)
         len2=len(fact2)

         hcf=[]
         if n1>n2:
            leng=len1
            for x in range(int(leng)):
               if fact1[x] in fact2:
                  hcf.append(fact1[x])
         elif n2>n1:
                  leng=len2
                  for x in range(int(leng)):
                     if fact2[x] in fact1:
                        hcf.append(fact2[x])

         answer=hcf[0]
        


   e.insert("end","="+str(answer))


   
   k=1
  if l==3:

   opp.clear()
   calc.clear()
   e.delete(0,'end')

   e.insert(0,"this is only supporting one operation")
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
clear_it=tk.Button(root,text="clear",width=10,command=lambda:[out(),clear()])

square_it=tk.Button(root,text="square",width=10,command=lambda:[out(),square()])
squreroot_it=tk.Button(root,text="Square root",width=10,command=lambda:[out(),squreroot()])
factors_it=tk.Button(root,text="Factors",width=10,command=lambda:[out(),factors()])
HCF_it=tk.Button(root,text="HCF",width=10,command=lambda:[out(),HCF()])

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
clear_it.grid(row=4,column=1)

square_it.grid(row=1,column=5)
squreroot_it.grid(row=2,column=5)
factors_it.grid(row=3,column=5)
HCF_it.grid(row=4,column=5)

equal.grid(row=4, column=3)

root.mainloop()
