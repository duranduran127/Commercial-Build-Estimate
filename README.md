# Commercial-Build-Estimate
prepared by: Payton duran

# Description 
This app will be a GUI for general contractors who can give a fast and easy estimate of basic material and labor for a commercial contracting job.

# How it works
This is a simple GUI that allows for easy inputs and totals of certain materials a contractor would need for a commercial build-out job. for example, assume there is a local strip mall where a contractor needs to build a new physical therapy store, and while looking at the general store location the owner of the store asks the contractor for a general number or estimate of a build-out. Assuming the two have never worked together the contractor can open the app and give estimated prices for the electrical, framing, permit costs, paint, and more. After the figures are put in the estimate calculator a price will be displayed that is assumed to be after tax and labor costs. It is a quick and simple way to get a fast estimate prior to an official estimate with more accurate figures. This can also be used for on the fly add on. 

# Why I wanted to do it
Building GUI's have always been of interest to me, I like the idea that many lines of code can transform into something that does not look like code at all. the complexity of GUI interfaces are also interesting as they come in many different styles and formats. My father is also a general contractor, and originally my idea was much more complexed in how the code would work. For example, my code would add tax and have individual prices for each item already in the code so that you could place an amount per item that added to a total number rather than placing the total number yourself. However, I asked my dad how the estimates generally work in the real world in a situation like this and with his experience generally contractors will give a total price with labor and taxes assumed to be included to the total. Generally speaking I enjoy the complexity of GUIs and that’s why I chose to do this.

# How I did it
Building the mainframe of the GUI is how I started the project originally. I used tkinter which is a module built into python for GUI interfaces, so first I had to set the size and import the modules below. 

import Tkinter as tk

import random

import time

from Tkinter import 

root = tk.Tk()

root.geometry("1600x800+0+0")

root.title("Commercial Building Estimate")

From here I started building my calculator to use on the side for items that were not included in my function. The calculator has many lines of comes in order for it to work correctly. That includes the display, the buttons and functions. 



txtDisplay = Entry(F2, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                   bg="white", justify='right')
txtDisplay.grid(columnspan=4)

btn7 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="7", bg="white", command=lambda: btnclick(7)).grid(row=2, column=0)




After the calculator was made I went on to create the labels that had the main items of cost such as framing, and electrical, and there is also a total label which is to the left side of the panel. 



lblElectrical = Label(F1, font=('ariel', 16, 'bold'), text="Electrical", bd=16, anchor='w')
lblElectrical.grid(row=3, column=0)
txtElectrical = Entry(F1, font=('ariel', 16, 'bold'), textvariable=Electrical, bd=10, insertwidth=4,
                     bg="white", justify='right')
txtElectrical.grid(row=3, column=1)






After all the labels were build the function buttons were created which are the 'total, reset, and exit' buttons that all function as they should. When first running the program you can click the 'total' button and a random reference will be generated for your customer number, and after all the inputs are entered for the items desired if you press the total button the total price estimate will appear in dollars in the total label section. Once all the labels were created all i did was define the rest of my functions and create a main loop at the end of the program that keeps it open. If you press exit on the program it will close. 

# Modules
tkinter/
pyinstaller/
datetime

