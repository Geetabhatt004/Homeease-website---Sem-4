from tkinter import*
from tkinter import ttk,messagebox
import sqlite3

class inventoryClass:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1100x550+220+130")
        self.root.title("Supply Chain System | developed by group 5")
        self.root.config(bg="white")
        self.root.focus_force()
        self.var_directory_id=StringVar()
        self.var_name=StringVar()
        self.var_directory_id=StringVar()
        
        
         #==titlle==
        lbl_title=Label(self.root,text="Manage  Product  Inventory ",font=("groudy old style",40),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_id=Label(self.root,text="Enter Product ID/Inventory ID ",font=("groudy old style",30),bg="white").place(x=50,y=180)
        txt_id=Entry(self.root,textvariable=self.var_directory_id,font=("groudy old style",20),bg="lightyellow").place(x=50,y=240,width=300)
        
        lbl_name=Label(self.root,text="Enter Product Name ",font=("groudy old style",30),bg="white").place(x=50,y=340)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("groudy old style",20),bg="lightyellow").place(x=50,y=400,width=300)
        
       
        btn_add=Button(self.root,text="ADD",command=self.add,font=("groudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=240,width=150,height=38)
        
        btn_delete=Button(self.root,text="Delete",font=("groudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=240,width=150,height=38)
       
        btn_add=Button(self.root,text="ADD",command=self.add,font=("groudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=400,width=150,height=38)
        
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("groudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=400,width=150,height=38)
        
        
        #==item details====
        directory_frame=Frame(self.root,bd=3,relief=RIDGE)
        directory_frame.place(x=700,y=100,width=380,height=430)
        
        
        scrolly=Scrollbar(directory_frame,orient=VERTICAL)
        
        scrollx=Scrollbar(directory_frame,orient=HORIZONTAL)
        
        
        self.directoryTable=ttk.Treeview(directory_frame,columns=("directory_id","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.directoryTable.xview)
        scrolly.config(command=self.directoryTable.yview)
        
        self.directoryTable.heading("directory_id",text="Directory_ID/Item_ID")
        self.directoryTable.heading("name",text="Name")

        self.directoryTable["show"]="headings"
        
        self.directoryTable.column("directory_id",width=90)
        self.directoryTable.column("name",width=150)
       
        self.directoryTable.pack(fill=BOTH,expand=1)
        self.directoryTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
 #===========================================================       
        
    def add(self):   
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try: 
            if self.var_directory_id.get()=="":
                messagebox.showerror("Error","Inventory ID /Product ID should be required",parent=self.root)
            else:
                cur.execute("Select * from directory where directory_id=?",(self.var_directory_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Item id  already assigned, try different id",parent=self.root)
                else:
                    cur.execute("Insert into directory(directory_id,name)values(?,?)",(
                                        self.var_directory_id.get(),
                                        self.var_name.get()
                                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Item  Added Successfully in this",parent=self.root)
                    self.show()                   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    
            
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select* from directory")
            rows=cur.fetchall()
            self.directoryTable.delete(*self.directoryTable.get_children())
            for row in rows:
                self.directoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)  
            
            
    def get_data(self,ev):  
        f=self.directoryTable.focus()
        content=(self.directoryTable.item(f))
        row=content['values']
       # print(row)
        self.var_directory_id.set(row[0]),
        self.var_name.set(row[1]),
         
    def delete(self):  
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_directory_id.get()=="":
                messagebox.showerror("Error","Inventory ID must be required",parent=self.root)
            else:
                cur.execute("Select * from directory where directory_id=?",(self.var_directory_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    
                       op=messagebox.askyesno("Confirm","Do You really want to delete this Item?",parent=self.root)
                if op==True: 
                    cur.execute("delete from directory where  directory_id=?",(self.var_directory_id.get(),)) 
                    con.commit()  
                    messagebox.showinfo("Delete","Item  Deleted Successfully",parent=self.root)
                    self.show()
                    self.var_directory_id.set("")
                    self.var_name.set("")
                     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                 
       
            
        
        
        
        
        
        
        
        
        
if __name__ =="__main":      
        
    root=Tk()
    obj=inventoryClass(root)
    root.mainloop()