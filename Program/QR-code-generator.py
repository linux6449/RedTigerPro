import qrcode
import os
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('QR Code Generator')
win.geometry('650x650')
win.config(bg='DarkTurquoise')

def generateCode():
    try:
        qr = qrcode.QRCode(version=size.get(), box_size=10, border=5)
        qr.add_data(text.get())
        qr.make(fit=True)
        img = qr.make_image()

        save_dir = loc.get()
        
        qr_folder = os.path.join(save_dir, "QR_Codes")
        if not os.path.exists(qr_folder):
            os.makedirs(qr_folder)
            print(f"Created folder: {qr_folder}")

        file_path = os.path.join(qr_folder, f"{name.get()}.png")
        
        img.save(file_path)
        
        messagebox.showinfo("QR Code Generator", f"QR Code saved successfully!\nLocation: {file_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

headingFrame = Frame(win, bg="azure", bd=5)
headingFrame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code", bg='azure', font=('Times', 20, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

Frame1 = Frame(win, bg="DarkTurquoise")
Frame1.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)

label1 = Label(Frame1, text="Enter the text/URL: ", bg="DarkTurquoise", fg='azure', font=('FiraMono', 13, 'bold'))
label1.place(relx=0.05, rely=0.2, relheight=0.08)

text = Entry(Frame1, font=('Century 12'))
text.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

Frame2 = Frame(win, bg="DarkTurquoise")
Frame2.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)

label2 = Label(Frame2, text="Enter the location to save the QR Code: ", bg="DarkTurquoise", fg='azure', font=('FiraMono', 13, 'bold'))
label2.place(relx=0.05, rely=0.2, relheight=0.08)

loc = Entry(Frame2, font=('Century 12'))
loc.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

Frame3 = Frame(win, bg="DarkTurquoise")
Frame3.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.3)

label3 = Label(Frame3, text="Enter the name of the QR Code: ", bg="DarkTurquoise", fg='azure', font=('FiraMono', 13, 'bold'))
label3.place(relx=0.05, rely=0.2, relheight=0.08)

name = Entry(Frame3, font=('Century 12'))
name.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

Frame4 = Frame(win, bg="DarkTurquoise")
Frame4.place(relx=0.1, rely=0.75, relwidth=0.7, relheight=0.2)

label4 = Label(Frame4, text="Enter the size from 1 to 40 with 1 being 21x21: ", bg="DarkTurquoise", fg='azure', font=('FiraMono', 13, 'bold'))
label4.place(relx=0.05, rely=0.2, relheight=0.08)

size = Entry(Frame4, font=('Century 12'))
size.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.2)

button = Button(win, text='Generate Code', font=('FiraMono', 15, 'normal'), command=generateCode)
button.place(relx=0.35, rely=0.9, relwidth=0.25, relheight=0.05)

win.mainloop()