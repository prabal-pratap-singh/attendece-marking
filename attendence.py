import os
directory= r'C:\Prabal\projects\face recognition\source code'
os.chdir(directory)
import cv2
import sys
import face_recognition
from simple_facerec import SimpleFacerec
from datetime import date
from tkinter import *
from tkinter import messagebox
sfr = SimpleFacerec()
sfr.load_encoding_images("images")
window= Tk()
window.title("attendence")
l1=Label(window, text="Name").grid(row=0,column=0)
n=Entry(window)
n.grid(row=0,column=1)
l2=Label(window, text="Registration number").grid(row=1)
r=Entry(window)
r.grid(row=1,column=1) 

def attendence():
    cap = cv2.VideoCapture(0)
#     messagebox.showinfo('Result',n.get())
#     print(n.get())
#     print(r.get())

    times=True
    while times==True:
        ret, frame = cap.read()

        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            if name=='Unknown':

                


                count=0
                while count<=3:
                    i=0
#                     roll_number=input()
                    name_input=n.get()
                    roll_number=r.get()
                    students=open('students.txt','r')
                    for line in students:
                        if roll_number in line:
                            i=1
                    if i==0:
                        students.close()
                        break
                    else:
                        count+=1
                        messagebox.showinfo('Result','your entered registration number is already registered with some other person try again')
                        cap.release()
                        cv2.destroyAllWindows()
                        window.destroy()
                        sys.exit("try again with right registration number")



                students = open("students.txt", 'a+')
                students.write("{}\n".format(name_input))
                students.write("{}\n".format(roll_number))
                students.close()
                directory= r'C:\Prabal\projectts\face recognition\source code\images'
                os.chdir(directory)
                roi_gray=frame[y1:y2, x1:x2]
                cv2.imwrite("{}-{}.jpg".format(name_input,roll_number),roi_gray)
                directory= r'C:\Prabal\projects\face recognition\source code'
                os.chdir(directory)
                sfr.load_encoding_images("images")
            else:
#                 print("your attendence is marked")
                messagebox.showinfo('Result',' Your attendence is marked')
                file_name=date.today()
                file = open("{}.txt".format(file_name), 'a+')
                file.write("{}\n".format(name))
                file.close()
                times = False 
                break
    cap.release()

b1=Button(window,text="Mark Attendence",bg='black',fg='white',command=attendence).grid(row=2)

window.mainloop()