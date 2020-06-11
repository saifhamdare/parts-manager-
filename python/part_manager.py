from tkinter import*
from tkinter import messagebox
from db import Database
db=Database('store.db')

def populate_list():
    for row in db.fetch():
        parts_list.insert(END,row)
def add_item():
    if part_text.get()==''or Customer_text.get()== '' or Retailer_text.get()==''or Price_text.get()=='':
        messagebox.showerror('required field','please include all fields')
        return
    db.insert(part_text.get(),Customer_text.get(),Retailer_text.get(),Price_text.get())
    parts_list.delete(0,END)
    parts_list.insert(END,(part_text.get(),Customer_text.get(),Retailer_text.get(),Price_text.get()))
    clear_text()
    populate_list()
def select_item(event):
    try:
        global selected_item
        index=parts_list.curselection()[0]
        selected_item=parts_list.get(index)
    
        part_entry.delete(0,END)
        part_entry.insert(END,selected_item[1])
        Customer_entry.delete(0,END)
        Customer_entry.insert(END,selected_item[2])
        Retailer_entry.delete(0,END)
        Retailer_entry.insert(END,selected_item[3])
        Price_entry.delete(0,END)
        Price_entry.insert(END,selected_item[4])
    except IndexError:
        pass
def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()
def update_item():
    db.update(selected_item[0],part_text.get(),Customer_text.get(),Retailer_text.get(),Price_text.get())
    populate_list()
def clear_text():
    part_entry.delete(0,END)
    Customer_entry.delete(0,END)
    Retailer_entry.delete(0,END)
    Price_entry.delete(0,END)

#create a window object
app=Tk()

#Part
part_text=StringVar()
part_label=Label(app, text='Part Name',font=('bold',14),pady=20)
part_label.grid(row=0,column=0,sticky=W)
part_entry=Entry(app,textvariable=part_text)
part_entry.grid(row=0,column=1)

#Customer
Customer_text=StringVar()
Customer_label=Label(app, text='Customer',font=('bold',14))
Customer_label.grid(row=1,column=0,sticky=W)
Customer_entry=Entry(app,textvariable=Customer_text)
Customer_entry.grid(row=1,column=1)
#Retailer
Retailer_text=StringVar()
Retailer_label=Label(app, text='Retailer',font=('bold',14))
Retailer_label.grid(row=0,column=2,sticky=W)
Retailer_entry=Entry(app,textvariable=Retailer_text)
Retailer_entry.grid(row=0,column=3)
#Price
Price_text=StringVar()
Price_label=Label(app, text='Price',font=('bold',14))
Price_label.grid(row=1,column=2,sticky=W)
Price_entry=Entry(app,textvariable=Price_text)
Price_entry.grid(row=1,column=3)

#PArt List (Listbox)
parts_list=Listbox(app, height=8,width=50, border=3)
parts_list.grid(row=3,column=0,rowspan=6,columnspan=3,pady=20,padx=20)

#scroll bar
scrollbar= Scrollbar(app)
scrollbar.grid(row=3,column=3)
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#bind select
parts_list.bind('<<ListboxSelect>>',select_item)

#Buttons
add_btn=Button(app,text='Add part',width=12,command=add_item,background="green",foreground="#fff")
add_btn.grid(row=2,column=0,pady=20)

remove_btn=Button(app,text='Remove part',width=12,command=remove_item,background="red",foreground="#fff")
remove_btn.grid(row=2,column=1)

update_btn=Button(app,text='Update part',width=12,command=update_item,background="blue",foreground="#fff")
update_btn.grid(row=2,column=2)

clear_btn=Button(app,text='Clear input',width=12,command=clear_text,background="#000",foreground="#fff")
clear_btn.grid(row=2,column=3)

populate_list()

app.title('part manager')
app.geometry('700x350')


#Start program
app,mainloop()