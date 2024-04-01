from tkinter import*
root=Tk()
from PIL import ImageTk, Image
from tkinter import filedialog
root.geometry("600x600")
root.title("Image Viewer")
root.configure(bg="yellow")

label=Label(root,bg="grey",image="", highlightthickness="3")
label.place(relx=0.5, rely=0.5, anchor=CENTER)

img_path="img1"

def open_image():
    global img_path
    img_path=filedialog.askopenfilename(title="Open Image File", filetypes=[("image files", "*.jpg *.gif *.png *.jpeg")])
    
    print(img_path)
    img=Image.open(img_path)
    img1=ImageTk.PhotoImage(img)
    label["image"]=img1
    img1.close()
    
btn=Button(root, text="Open Image", font=("Arial", 10), bg="yellow", fg="darkblue", relief=SOLID, command=open_image)
btn.place(relx=0.5, rely=0.8, anchor=CENTER)
root.mainloop()