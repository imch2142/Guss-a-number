from tkinter import *
from PIL import Image ,ImageTk
import random
def game1():
  n=random.randint(1,10)
  m= int(en.get())
  
  if type(m)==int and m>0:
    if m==n:
       label2.config(text="***sucess***",fg="green",font=("Arial", 20))
       
       
      
    else:
       label2.config(text="wrong",fg="red",font=("Arial", 20))
       
  else:
    label2.config(text="the number must be an integer number!!!")

   
    
      
def game():
  global pro1
 
  pro1=Tk()
  pro1.geometry("1800x1300")
  pro1.title("Guess Number")
  
  l1=Label(pro1,text=" *****Welcome In This Game***** ",fg="pink",font=("Arial", 20),bg="#FFF",width="100",height="5")
  l1.pack()
 
  label1=Label(pro1,text=f"guess an integer number between 1 and 10",width=40,height=2,font=("Arial", 30))
  label1.pack(pady=10)
  global label2,en
  label2=Label(pro1,width=40,height=2,font=("Arial", 30))
  label2.pack(pady=10)
  en=Entry(pro1,font=200)
  en.place(x=430,y=400,width=500,height=70)
  global b1
  b1 = Button(pro1,text="OK",width=30,command=game1)
  b1.place(x=580,y=600)
  pro1.mainloop()
  

       
       
      





pro=Tk()
pro.geometry("1800x1300")
pro.title("Guess Number")
background_image = Image.open("t.jpg")  
background_image = background_image.resize((1700, 1200), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(background_image) 
label_background = Label(pro, image=bg_image)
label_background.place(relwidth=1, relheight=1)
lab=Button(pro,text="Play",width=20,bg="#ff69b4",height=5,command=game)
lab.place(x=610,y=600)
pro.mainloop()
