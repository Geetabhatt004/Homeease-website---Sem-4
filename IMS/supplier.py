from tkinter import*
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1100x550+220+130")
        self.root.title("Supply Chain System | developed by group 5")
        self.root.config(bg="white")
        self.root.focus_force()

        
        
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_supplier_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_password=StringVar()
        self.var_salary=StringVar()
        
        
        
        
        #==searchframe==
        SearchFrame=LabelFrame(self.root,text="Search Supplier",font=("groudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
      
        
        #==options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchBy,values=("select","name","contact","email"),state="readonly",justify=CENTER,font=("groudy old style",12,"bold"))
        cmb_search.place(x=20,y=10,width=180)
        cmb_search.current(0)
       
     
        
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("groudy old style",15,"bold"),bg="lightyellow").place(x=210,y=8)
        
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("groudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=440,y=7,width=150,height=30)
       
       
        
        #==titlle==
        title=Label(self.root,text="Supplier Details",font=("groudy old style",15),bg="#0f4d7d",fg="white").place(x=60,y=100,width=1000)
       
   
       #===content==
       
       
        lbl_supplier_id=Label(self.root,text="Supplier ID",font=("groudy old style",15),bg="WHITE").place(x=60,y=160)
        lbl_supplier_name=Label(self.root,text="Supplier Name",font=("groudy old style",15),bg="WHITE").place(x=360,y=160)
        lbl_supplier_contact=Label(self.root,text="Supplier Contact",font=("groudy old style",15),bg="WHITE").place(x=710,y=160)
        
        
        
        txt_supplier_id=Entry(self.root,textvariable=self.var_supplier_id,font=("groudy old style",15),bg="lightyellow").place(x=170,y=160,width=180)
        txt_supplier_name=Entry(self.root,textvariable=self.var_name,font=("groudy old style",15),bg="lightyellow").place(x=500,y=160,width=190)
        txt_supplier_contact=Entry(self.root,textvariable=self.var_contact,font=("groudy old style",15),bg="lightyellow").place(x=870,y=160,width=190)
     
        
        
        lbl_supplier_email=Label(self.root,text="Email",font=("groudy old style",15),bg="WHITE").place(x=60,y=250)
        lbl_supplier_password=Label(self.root,text="Password",font=("groudy old style",15),bg="WHITE").place(x=360,y=250)
        lbl_supplier_salary=Label(self.root,text="Salary",font=("groudy old style",15),bg="WHITE").place(x=710,y=250)
        
        
        txt_supplier_email=Entry(self.root,textvariable=self.var_email,font=("groudy old style",15),bg="lightyellow").place(x=130,y=250,width=220)
        txt_supplier_password=Entry(self.root,textvariable=self.var_password,font=("groudy old style",15),bg="lightyellow").place(x=470,y=250,width=220)
        txt_supplier_salary=Entry(self.root,textvariable=self.var_salary,font=("groudy old style",15),bg="lightyellow").place(x=800,y=250,width=230)
        
        #==button==
        
        btn_add=Button(self.root,text="Save",command=self.add,font=("groudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=650,y=300,width=100,height=28)
        
        btn_update=Button(self.root,text="Update",command=self.update,font=("groudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=765,y=300,width=100,height=28)
        
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("groudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=880,y=300,width=100,height=28)
        
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("groudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=990,y=300,width=100,height=28)
        
      
        #==supplier details====
        supplier_frame=Frame(self.root,bd=3,relief=RIDGE)
        supplier_frame.place(x=0,y=350,relwidth=1,height=195)
        
        
        scrolly=Scrollbar(supplier_frame,orient=VERTICAL)
        
        scrollx=Scrollbar(supplier_frame,orient=HORIZONTAL)
        
        
        self.supplierTable=ttk.Treeview(supplier_frame,columns=("supplier_id","name","email","contact","password","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        
        self.supplierTable.heading("supplier_id",text="Supplier_ID")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("email",text="Email")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("password",text="Password")
        self.supplierTable.heading("salary",text="Salary")
      
        self.supplierTable["show"]="headings"
        
        self.supplierTable.column("supplier_id",width=90)
        self.supplierTable.column("name",width=150)
        self.supplierTable.column("email",width=200)
        self.supplierTable.column("contact",width=150)
        self.supplierTable.column("password",width=200)
        self.supplierTable.column("salary",width=150)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
       
#========================================================

    def add(self):   
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supplier_id.get()=="":
                messagebox.showerror("Error","Supplier ID must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supplier_id=?",(self.var_supplier_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Supplier id  already assigned, try different id",parent=self.root)
                else:
                    cur.execute("Insert into supplier(supplier_id,name,email,contact,password,salary)values(?,?,?,?,?,?)",(
                                        self.var_supplier_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_contact.get(),
                                        self.var_password.get(),
                                        self.var_salary.get()               
                    ))
                    con.commit()
                    messagebox.showinfo("Success","supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
       
            

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select* from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
  
    
        
    def get_data(self,ev):  
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
       # print(row)
        self.var_supplier_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_contact.set(row[3]),
        self.var_password.set(row[4]),
        self.var_salary.set(row[5])  
        
   
        
    def update(self):   
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
    
            if self.var_supplier_id.get()=="":
                messagebox.showerror("Error","Supplier ID must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supplier_id=?",(self.var_supplier_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,email=?,contact=?,password=?,salary=? where supplier_id=?",(
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_contact.get(),
                                        self.var_password.get(),
                                        self.var_salary.get(),
                                        self.var_supplier_id.get()
                                                      
                    ))
                    con.commit()
                    messagebox.showinfo("Success","supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
       
    
    def delete(self):  
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supplier_id.get()=="":
                messagebox.showerror("Error","Supplier ID must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supplier_id=?",(self.var_supplier_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
                else:
                    
                       op=messagebox.askyesno("Confirm","Do You really want to delete this information?",parent=self.root)
                if op==True: 
                    cur.execute("delete from supplier where  supplier_id=?",(self.var_supplier_id.get(),)) 
                    con.commit()  
                    messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                    self.clear()
                     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    
    
        
       
    def clear(self):
        self.var_supplier_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_password.set("")
        self.var_salary.set("")  
        self.show()                    
    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchBy.get()=="Select":
               messagebox.showerror("Error","Select Search By option",parent=self.root)
               
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
              
              
            else: 
                cur.execute("select* from supplier where "+self.var_searchBy.get()+" LIKE '%"+self.var_searchtxt.get()+"%'") 
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                         self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)         
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
  
    
if __name__ =="__main":      
        
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()

