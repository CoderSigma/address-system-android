from tkinter import *
import sqlite3
from PIL import ImageTk,Image


root = Tk()
root.title("CODER SIGMA")

con = sqlite3.connect('address_book.db')


#tangalin mo lang comment tag dito pag wala pang db 

#c.execute("""CREATE TABLE addresses ( 
#        first_name text,
#        last_name text,
#        address text,
#        city text,
#        state text,
#        zipcode integer
#        )""")
 
#submit
def submit():
    
    
    con = sqlite3.connect("address_book.db")
    c = con.cursor()
    #nag sesend ng update
    
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        }
    )
    con.commit()

    #matic na ano ba ang close ha?
    con.close()
    
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    
def query():
    
    con = sqlite3.connect("address_book.db")
    
    c = con.cursor()
    
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)
    
    print_records= ' '
    for record in records:
        print_records += str(record[6])+str(record[0]) + " " + str(record[1])  + "\n" + str(record[2]) + "\n"+ str(record[3]) + "\n" + str(record[4])+ "\n"+ str(record[5])+ "\n" 
        
    query_label = Label(root, text=print_records)
    query_label.grid(row=15, column=0, columnspan=2)
    
    con.commit()

    con.close()
    
def delete():
   
    con = sqlite3.connect("address_book.db")
    
    c = con.cursor()
    
    c.execute("DELETE from addresses WHERE oid= "+ delete_box.get())
    
    con.commit()

    con.close()
    
def save():
    
    con = sqlite3.connect("address_book.db")
    
    c = con.cursor()
    
    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET 
            first_name = :first,
            last_name = :last,
            city = :city,
            state = :state,
            zipcode = :zipcode
            
            WHERE oid = :oid""",
            {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            
            'oid' : record_id
            
            }
            )
    
    
    con.commit()
    
    con.close()
    
    editor.destroy()
    
    
def update():
    global editor
    editor = Tk()
    editor.title("UPDATE")
    
    con = sqlite3.connect("address_book.db")
    
    c = con.cursor()
    
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid= " + record_id)
    records = c.fetchall()
    
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    
    f_name_editor =Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20)

    l_name_editor =Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_editor =Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor =Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor =Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_editor =Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)


# TEXT SA TABING BOX
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0)

    l_name_label = Label(editor, text="Lates Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Adress")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)
    
    edit_btn = Button(editor, text="Save Record", command=save)
    edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=149)
    
    
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
        
         
    con.commit()

    con.close()
    
    
    #TEXT BOX
f_name =Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name =Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address =Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city =Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state =Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode =Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# TEXT SA TABING BOX

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Lates Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Adress")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=10, column=0)

sub_btn = Button(root, text="Add record to Database", command=submit)
sub_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=149)


delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=149)

edit_btn = Button(root, text="Update Record", command=update)
edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=149)


con.commit()

con.close()

root.mainloop()
