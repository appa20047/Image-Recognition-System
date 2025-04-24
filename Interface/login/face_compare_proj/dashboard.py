import tkinter
import subprocess
from subprocess import * 


window = tkinter.Tk()
window.title("Access Form")
window.geometry("340x440")
window.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

def chat_box():
    n= subprocess.run(["python3","chatbox.py"])
    #from subprocess import call
    #call(["python3","chatbox.py"])
    window.destroy


def img_compa():
    m= subprocess.run(["python3","img_compare.py"])
    #from subprocess import call
    #call(["python3","img_compare.py"])
    window.destroy    


def crim_regist():
    p= subprocess.run(["python3","cri_reg.py"])
    #from subprocess import call
    #call(["python3","cri_reg.py"])
    window.destroy        

def crim_show():
    q= subprocess.run(["python3","show.py"])
    #from subprocess import call
    #call(["python3","show.py"])
    window.destroy
    
login_label = tkinter.Label(frame, text="CRIMINAL FACE DETECTION SYSTEM", bg='#333333',fg='#FF3399', font=('Arial', 30) )
login_label.grid(row=1, column=0, columnspan=2, pady=10)



crim_regist = tkinter.Button(frame, text="Criminal Registration" ,bg='#574266', fg='#FFFFFF',width=20,height=5,command=crim_regist)
crim_regist.grid(row=33, column=0 , pady=25)

crim_show = tkinter.Button(frame, text="Criminal Data Show" ,bg='#574266', fg='#FFFFFF',width=20,height=5,command=crim_show)
crim_show.grid(row=30, column=1, columnspan=4, pady=25)

img_compa = tkinter.Button(frame, text="Image Recognition" ,bg='#574266', fg='#FFFFFF',width=20,height=5,command=img_compa)
img_compa.grid(row=30, column=0, pady=25)

chat_box = tkinter.Button(frame, text="Chat-Box" ,bg='#574266', fg='#FFFFFF',width=20,height=5,command=chat_box)
chat_box.grid(row=33, column=1, columnspan=10, pady=50)

frame.pack()





window.mainloop()