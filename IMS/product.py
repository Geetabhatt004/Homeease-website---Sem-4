from tkinter import*
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1100x550+220+130")
        self.root.title("Supply Chain System | developed by group 5")
        self.root.config(bg="white")
        self.root.focus_force()
#=======================================================
        
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_pid=StringVar()
        self.var_product_id=StringVar()
        self.var_category=StringVar()
        self.var_supplier=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()
        self.name_list=[]
        self.sup_list=[]
        self.fectch_cat_sup()
        
        
  #==searchframe==
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)
        
     #==titlle==
        title=Label(product_frame,text=" Manage product Details",font=("groudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        #===column1====
        lbl_category=Label(product_frame,text="Category",font=("groudy old style",18),bg="white").place(x=30,y=50)
       
        
        lbl_supplier=Label(product_frame,text="Supplier",font=("groudy old style",18),bg="white").place(x=30,y=110)
        
        lbl_product_name=Label(product_frame,text=" Name",font=("groudy old style",18),bg="white").place(x=30,y=160)
        
        lbl_price=Label(product_frame,text="Price",font=("groudy old style",18),bg="white").place(x=30,y=210)
        
        lbl_quantity=Label(product_frame,text="Quantity",font=("groudy old style",18),bg="white").place(x=30,y=260)
        
        lbl_status=Label(product_frame,text="Status",font=("groudy old style",18),bg="white").place(x=30,y=310)
        
        
         #==column2
        cmb_name=ttk.Combobox(product_frame,textvariable=self.name_list,values=("select"),state="readonly",justify=CENTER,font=("groudy old style",12,"bold"))
        cmb_name.place(x=150,y=56,width=200)
        cmb_name.current(0)
       
        
        cmb_supplier=ttk.Combobox(product_frame,textvariable=self.var_supplier,values=self.sup_list,state="readonly",justify=CENTER,font=("groudy old style",12,"bold"))
        cmb_supplier.place(x=150,y=110,width=200)
        cmb_supplier.current(0)
        
        txt_name=Entry(product_frame,textvariable=self.var_name,font=("groudy old style",15,),bg="lightyellow").place(x=150,y=165,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("groudy old style",15,),bg="lightyellow").place(x=150,y=210,width=200)
        txt_quantity=Entry(product_frame,textvariable=self.var_quantity,font=("groudy old style",15,),bg="lightyellow").place(x=150,y=260,width=200)
        
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state="readonly",justify=CENTER,font=("groudy old style",12,"bold"))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)
        #buttons----
        
        btn_add=Button(product_frame,text="Save",command=self.add,font=("groudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=20,y=400,width=100,height=40)
        
        btn_update=Button(product_frame,text="Update",command=self.update,font=("groudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=130,y=400,width=100,height=40)
        
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("groudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=240,y=400,width=100,height=40)
        
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("groudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=350,y=400,width=100,height=40)
        
        
           #==searchframe==
        SearchFrame=LabelFrame(self.root,text="Search Supplier",font=("groudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=20,width=620,height=80)
      
        
        #==options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchBy,values=("select","name","contact","email"),state="readonly",justify=CENTER,font=("groudy old style",12,"bold"))
        cmb_search.place(x=20,y=10,width=180)
        cmb_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("groudy old style",15,"bold"),bg="lightyellow").place(x=210,y=8)
        
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("groudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=440,y=7,width=150,height=30)
        
        
        #===product details===== 
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=590,height=390)
        
        
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)
        
        
        self.productTable=ttk.Treeview(p_frame,columns=("product_id","category","supplier","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        
        self.productTable.heading("product_id",text="Product_ID")
        self.productTable.heading("category",text="Category")
        self.productTable.heading("supplier",text="Supplier")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("quantity",text="Quantity")
        self.productTable.heading("status",text="Status")
      
        self.productTable["show"]="headings"
        
        self.productTable.column("product_id",width=90)
        self.productTable.column("category",width=150)
        self.productTable.column("name",width=200)
        self.productTable.column("price",width=150)
        self.productTable.column("quantity",width=200)
        self.productTable.column("status",width=150)
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        
        
 #===================================================
         
    def fectch_cat_sup(self):  
        self.name_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from directory")
            name=cur.fetchall()
           
            if len(name)>0:
                del self.name_list[:]
                self.name_list.append("Select")
           
                for i in name:
                       self.name_list.append(i[0])
              
            cur.execute("Select name from distributor")
            dis=cur.fetchall()
            if len(dis)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
           
                for i in dis:
                       self.sup_list.append(i[0])
            print(dis)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
            
    def add(self):   
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
        
            if self.var_category.get()=="Select" or self.var_supplier.get()=="Select"or self.var_name.get()=="Select" or self.var_category.get()=="Empty" or self.var_supplier.get()=="Select":
                messagebox.showerror("Error","ALL fiedls should  be required",parent=self.root)
            else:
                cur.execute("Select * from product where name=? ",(self.var_name.get(),))
               
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Product is  already present, try different id",parent=self.root)
                else:
                    cur.execute("Insert into product(category,supplier,name,price,quantity,status)values(?,?,?,?,?,?)",(
                                        
                                        self.var_category.get(),
                                        self.var_supplier.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_quantity.get(),
                                        self.var_status.get()               
                                              
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Item Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
       
       
            

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select* from product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
  
    
        
    def get_data(self,ev):  
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_pid.get(row[0])
        self.var_category.get(row[2])
        self.var_supplier.set(row[1])
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_quantity.set(row[5]),
        self.var_status.set(row[6])       
        self.var_pid.get(row[0])
        self.var_category.get(row[2])
        self.var_supplier.set(row[1])
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_quantity.set(row[5]),
        self.var_status.set(row[6])       
        
        
   
        
    def update(self):   
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
    
            if self.var_pid.set()=="":
                messagebox.showerror("Error","Please select Product list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ",parent=self.root)
                else:
                    cur.execute("Update product set category=?,supplier=?,name=?,price=?,quantity=? ,status=? where pid=?",(
                                         self.var_category.get(),
                                        self.var_supplier.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_quantity.get(),
                                        self.var_status.get(),
                                        self.var_pid.get() 
                                                      
                    ))
                    con.commit()
                    messagebox.showinfo("Success","product Updated Successfully",parent=self.root)
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
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                         self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)         
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
       
        
        
        
if __name__ =="__main":      
        
    root=Tk()
    obj=productClass(root)
    root.mainloop()