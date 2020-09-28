from tkinter import *
from tkinter import messagebox
import tkinter as tk
import folium 
import webbrowser
import requests
from bs4 import BeautifulSoup as bs

root=tk.Tk()
root.title("Map Application | Manjunathan C")
root.geometry("500x500")
root.config(bg="#3d155f")
ico=PhotoImage(file="icon.png")
root.iconphoto(True,ico)

label1=Label(root,text="Enter the Place ",font=("font awesome",15,"bold italic"),bg="#3d155f",fg="#DF678C")
label1.place(x=155,y=20)

entry=Entry(root,width=28,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="#DF678C",fg="#3d155f")
entry.place(x=40,y=60)

def search():
    try:
        url="https://google.com/search?query="+entry.get()+"+latitude+longitude"
        headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"}
        response=requests.get(url,headers=headers)
        soup=bs(response.text,"html.parser")
        locationFind=soup.find("div",class_="Z0LcW XcVN5d")
        locationSpilit=locationFind.text
        locationSpilit=locationSpilit.split(",")
        latitute=locationSpilit[0]
        latitute=latitute.replace("° N","")
        longitude=locationSpilit[1]
        longitude=longitude.replace("° E","")
        mapFind=folium.Map(location=[latitute,longitude],zoom_start=14)
        mapName=entry.get()+".html"
        a=mapFind.save(mapName)
        webbrowser.open(mapName)
    except:
        messagebox.showerror("Network Error","Please Check Your Internet Connection")
    
buttonSearch=Button(root,text="SEARCH",font=("font awesome",15,"bold italic"),bg="#DF678C",fg="#3d155f",borderwidth=5,command=search)
buttonSearch.place(x=190,y=130)

buttonClear=Button(root,text="CLEAR",font=("font awesome",15,"bold italic"),bg="#DF678C",fg="#3d155f",borderwidth=5,command=lambda: entry.delete(0,END))
buttonClear.place(x=200,y=190)

buttonExit=Button(root,text="EXIT",font=("font awesome",15,"bold italic"),bg="#DF678C",fg="#3d155f",borderwidth=5,command=root.destroy)
buttonExit.place(x=212,y=250)

buttonContact=Button(root,text="CONTACT",font=("font awesome",15,"bold italic"),bg="#DF678C",fg="#3d155f",borderwidth=5,command=lambda:webbrowser.open("https://github.com/cmanjunathan45/"))
buttonContact.place(x=182,y=310)

root.mainloop()