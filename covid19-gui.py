from tkinter import *
import covid as cv

root = Tk()
root.geometry("300x300")
root.title(" COVID-19 ")
states = ['india', 'maharashtra', 'karnataka', 'andhra pradesh', 'tamil nadu', 'kerala', 'delhi', 'uttar pradesh', 'west bengal', 'odisha', 'rajasthan', 'telangana', 'chhattisgarh', 'haryana', 'bihar', 'gujarat', 'madhya pradesh', 'assam', 'punjab', 'jammu and kashmir', 'jharkhand',
          'uttarakhand', 'himachal pradesh', 'goa', 'puducherry', 'tripura', 'manipur', 'total', 'chandigarh', 'arunachal pradesh', 'meghalaya', 'nagaland', 'ladakh', 'sikkim', 'andaman and nicobar islands', 'mizoram', 'dadra and nagar haveli and daman and diu', 'lakshadweep']


def Take_input():
    Output.delete('1.0', END)
    INPUT = inputtxt.get("1.0", "end-1c")
    INPUT = INPUT.lower()
    print(INPUT)
    if INPUT not in states:
        Output.insert(END, 'Please enter a indian state.')
    else:
        Output.insert(END, cv.fetch(INPUT))


l = Label(text="Enter India/State")
inputtxt = Text(root, height=1,
                width=32,
                bg="snow2")

Output = Text(root, height=12,
              width=32,
              bg="linen")
Output.insert(END, cv.fetch('india'))

Display = Button(root, height=2,
                 width=20,
                 text="Fetch",
                 command=lambda: Take_input())
l2 = Label(text="Check docs for list of all available states")

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
l2.pack()

mainloop()
