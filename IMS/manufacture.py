from tkinter import*
from tkinter import ttk,messagebox
import sqlite3

class manufactureClass:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1100x550+220+130")
        self.root.title("Supply Chain System | developed by group 5")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_manufacture_id=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_description=StringVar()
        
        
        
        
        #==searchframe==
        # SearchFrame=LabelFrame(self.root,text="Search Supplier",font=("groudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        # SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #==options
  
        lbl_search=Label(self.root,text="Sreach Manufacture ID",bg="white",font=("groudy old style",10,"bold"))
        lbl_search.place(x=700,y=80)
        
        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("groudy old style",15,"bold"),bg="lightyellow").place(x=850,y=80,width=120)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("groudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)
       
        
        #==titlle==
        title=Label(self.root,text="Manufatures Details",font=("groudy old style",30,"bold"),bg="#0f4d7d",fg="white").place(x=60,y=10,width=1000,height=40)
       #===content==
       
       
        lbl_manufacture_id=Label(self.root,text="Manufacture ID",font=("groudy old style",15),bg="WHITE").place(x=60,y=70)
        lbl_manufacture_name=Label(self.root,text=" Name",font=("groudy old style",15),bg="WHITE").place(x=60,y=110)
        lbl_manufacture_contact=Label(self.root,text=" Contact",font=("groudy old style",15),bg="WHITE").place(x=60,y=150)
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=60,y=190)
        
        
        txt_manufacture_id=Entry(self.root,textvariable=self.var_manufacture_id,font=("groudy old style",15),bg="lightyellow").place(x=200,y=70,width=190)
        txt_manufacture_name=Entry(self.root,textvariable=self.var_name,font=("groudy old style",15),bg="lightyellow").place(x=200,y=110,width=190)
        txt_manufacture_contact=Entry(self.root,textvariable=self.var_contact,font=("groudy old style",15),bg="lightyellow").place(x=200,y=150,width=190)
        self.txt_description=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_description.place(x=200,y=190,width=440,height=150)
     

        
        #==button==
        
           
        btn_add=Button(self.root,text="Save",command=self.add,font=("groudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=370,width=100,height=35)
        
        btn_update=Button(self.root,text="Update",command=self.update,font=("groudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=370,width=100,height=35)
        
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("groudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=370,width=100,height=35)
        
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("groudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=370,width=100,height=35)
        
        #==supplier details====
        
        manufacture_frame=Frame(self.root,bd=3,relief=RIDGE)
        manufacture_frame.place(x=700,y=140,width=400,height=370)
        
        
        scrolly=Scrollbar(manufacture_frame,orient=VERTICAL)
        
        scrollx=Scrollbar(manufacture_frame,orient=HORIZONTAL)
        
        
        self.manufactureTable=ttk.Treeview(manufacture_frame,columns=("manufacture_id","name","contact","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.manufactureTable.xview)
        scrolly.config(command=self.manufactureTable.yview)
        
        self.manufactureTable.heading("manufacture_id",text="Manufacture_ID")
        self.manufactureTable.heading("name",text="Name")
        self.manufactureTable.heading("contact",text="Contact")
        self.manufactureTable.heading("description",text="Description")
       
      
        self.manufactureTable["show"]="headings"
        
        self.manufactureTable.column("manufacture_id",width=100)
        self.manufactureTable.column("name",width=150)
        self.manufactureTable.column("contact",width=150)
        self.manufactureTable.column("description",width=200)
        self.manufactureTable.pack(fill=BOTH,expand=1)
        self.manufactureTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#=============================================================
       
    def add(self):   
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_manufacture_id.get()=="":
                messagebox.showerror("Error","Manufacture ID must be required",parent=self.root)
            else:
                cur.execute("Select * from manufacture where manufacture_id=?",(self.var_manufacture_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This manufacture id  already assigned, try different id",parent=self.root)
                else:
                    cur.execute("Insert into manufacture(manufacture_id,name,contact,description)values(?,?,?,?)",(
                                                self.var_manufacture_id.get(),
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_description.get('1.0',END)               
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Manufacture Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
       
                   
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select* from manufacture")
            rows=cur.fetchall()
            self.manufactureTable.delete(*self.manufactureTable.get_children())
            for row in rows:
                self.manufactureTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
        
            
    def get_data(self,ev):  
        f=self.manufactureTable.focus()
        content=(self.manufactureTable.item(f))
        row=content['values']
       # print(row)
        self.var_manufacture_id.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[3])
        
        
        
             
    def update(self):   
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
    
            if self.var_manufacture_id.get()=="":
                messagebox.showerror("Error","Manufacture ID must be required",parent=self.root)
            else:
                cur.execute("Select * from manufacture where manufacture_id=?",(self.var_manufacture_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Manufacture ID",parent=self.root)
                else:
                    cur.execute("Update manufacture set name=?,contact=?,description=? where manufacture_id=?",(
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_description.get('1.0',END),
                                                self.var_manufacture_id.get()
                                                      
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Manufacture Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
            
            
    def delete(self):  
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_manufacture_id.get()=="":
                messagebox.showerror("Error","Manufacture ID must be required",parent=self.root)
            else:
                cur.execute("Select * from manufacture where manufacture_id=?",(self.var_manufacture_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Manufacture ID",parent=self.root)
                else:
                    
                       op=messagebox.askyesno("Confirm","Do You really want to delete this information?",parent=self.root)
                if op==True: 
                    cur.execute("delete from manufacture where manufacture_id=?",(self.var_manufacture_id.get(),)) 
                    con.commit()  
                    messagebox.showinfo("Delete","Manufacture Deleted Successfully",parent=self.root)
                    self.clear()
                     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    
           
   
    def clear(self):
        self.var_manufacture_id.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_description.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()                    
    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
               
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Manufacture ID should be required ",parent=self.root)
              
              
            else: 
                cur.execute("Select* from manufacture where manufacture_id=?",(self.var_searchtxt.get(),)) 
                row=cur.fetchone()
                if row!=None:
                    self.manufactureTable.delete(*self.manufactureTable.get_children())
                    self.manufactureTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)         
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    
if __name__ =="__main":      
        
    root=Tk()
    obj=manufactureClass(root)
    root.mainloop()    
  