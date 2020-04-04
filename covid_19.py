import requests
from bs4 import BeautifulSoup
from tkinter import *

import time
import logiced



root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title("Coronavirus updates")
root.configure(background='#adc2db')

#adc2db


result = requests.get("https://www.worldometers.info/coronavirus/")
#background_image = Tk.PhotoImage(Image.open(download.jfif))
src = result.content
#print(src)
soup   = BeautifulSoup(src,'lxml')
run = True








		
def main():

	
#	background_label = Label(root, image=background_image)
#	background_label.place(x=0, y=0, relwidth=1, relheight=1)

	logiced.logic(soup) 
	mylabel1 = Label(root,text=logiced.doto[0] , bg='#adc2db')
	mylabel2 = Label(root,text=logiced.doto[1] , bg='#adc2db')
	mylabel3 = Label(root,text=logiced.doto[2] , bg='#adc2db')
	mylabel1.pack()
	mylabel2.pack()
	mylabel3.pack()
	mylabel3 = Label(root,text="" , bg='#adc2db')
	mylabel1.pack()
	#myButton = Button(root,text="Refresh" , padx=50,command=boom,fg="#3c356e",bg="white")
	#myButton.pack()





main()
root.mainloop()


