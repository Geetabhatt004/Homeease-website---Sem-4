from tkinter import*
from tkinter import ttk,messagebox
import sqlite3

class distributorClass:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1100x550+220+130")
        self.root.title("Supply Chain System | developed by group 5")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_distributor_id=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_location=StringVar()
        
        
        
        
    
        #==options
  
        lbl_search=Label(self.root,text="Sreach Distributor ID",bg="white",font=("groudy old style",10,"bold"))
        lbl_search.place(x=700,y=80)
        
        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("groudy old style",15,"bold"),bg="lightyellow").place(x=850,y=80,width=120)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("groudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)
       
        
        #==titlle==
        title=Label(self.root,text="Distributor  Details",font=("groudy old style",30,"bold"),bg="#0f4d7d",fg="white").place(x=60,y=10,width=1000,height=40)
       #===content==
       
       
        lbl_distributor_id=Label(self.root,text="Distributor ID",font=("groudy old style",15),bg="WHITE").place(x=60,y=70)
        lbl_distributor_name=Label(self.root,text=" Name",font=("groudy old style",15),bg="WHITE").place(x=60,y=110)
        lbl_distributor_contact=Label(self.root,text=" Contact",font=("groudy old style",15),bg="WHITE").place(x=60,y=150)
        lbl_location=Label(self.root,text="Location",font=("goudy old style",15,"bold"),bg="white").place(x=60,y=190)
        
        
        txt_distributor_id=Entry(self.root,textvariable=self.var_distributor_id,font=("groudy old style",15),bg="lightyellow").place(x=200,y=70,width=220)
        txt_distributor_name=Entry(self.root,textvariable=self.var_name,font=("groudy old style",15),bg="lightyellow").place(x=200,y=110,width=220)
        txt_distributor_contact=Entry(self.root,textvariable=self.var_contact,font=("groudy old style",15),bg="lightyellow").place(x=200,y=150,width=220)
        self.txt_location=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_location.place(x=200,y=190,width=220,height=60)
     

        
        #==button==
        
           
        btn_add=Button(self.root,text="Save",command=self.add,font=("groudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=100,y=280,width=150,height=38)
        
        btn_update=Button(self.root,text="Update",command=self.update,font=("groudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=260,y=280,width=150,height=38)
        
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("groudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=280,width=150,height=38)
        
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("groudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=580,y=280,width=150,height=38)
        
        #==supplier details====
        
        disrtibutor_frame=Frame(self.root,bd=3,relief=RIDGE)
        disrtibutor_frame.place(x=0,y=350,width=1100,height=200)
        
        
        scrolly=Scrollbar(disrtibutor_frame,orient=VERTICAL)
        
        scrollx=Scrollbar(disrtibutor_frame,orient=HORIZONTAL)
        
        
        self.disrtibutorTable=ttk.Treeview(disrtibutor_frame,columns=("distributor_id","name","contact","location"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.disrtibutorTable.xview)
        scrolly.config(command=self.disrtibutorTable.yview)
        
        self.disrtibutorTable.heading("distributor_id",text="Distributor_ID")
        self.disrtibutorTable.heading("name",text="Name")
        self.disrtibutorTable.heading("contact",text="Contact")
        self.disrtibutorTable.heading("location",text="Location")
       
      
        self.disrtibutorTable["show"]="headings"
        
        self.disrtibutorTable.column("distributor_id",width=100)
        self.disrtibutorTable.column("name",width=150)
        self.disrtibutorTable.column("contact",width=150)
        self.disrtibutorTable.column("location",width=200)
        self.disrtibutorTable.pack(fill=BOTH,expand=1)
        self.disrtibutorTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#=============================================================
       
    def add(self):   
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_distributor_id.get()=="":
                messagebox.showerror("Error","Distributor ID must be required",parent=self.root)
            else:
                cur.execute("Select * from distributor where distributor_id=?",(self.var_distributor_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This distributor id  already assigned, try different id",parent=self.root)
                else:
                    cur.execute("Insert into distributor(distributor_id,name,contact,location)values(?,?,?,?)",(
                                                self.var_distributor_id.get(),
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_location.get('1.0',END)           
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Distributor Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
       
                   
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select* from distributor")
            rows=cur.fetchall()
            self.disrtibutorTable.delete(*self.disrtibutorTable.get_children())
            for row in rows:
                self.disrtibutorTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
        
            
    def get_data(self,ev):  
        f=self.disrtibutorTable.focus()
        content=(self.disrtibutorTable.item(f))
        row=content['values']
       # print(row)
        self.var_distributor_id.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_location.delete('1.0',END)
        self.txt_location.insert(END,row[3])
        
        
        
             
    def update(self):   
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
    
            if self.var_distributor_id.get()=="":
                messagebox.showerror("Error","Description ID must be required",parent=self.root)
            else:
                cur.execute("Select * from distributor where distributor_id=?",(self.var_distributor_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Distributor ID",parent=self.root)
                else:
                    cur.execute("Update distributor set name=?,contact=?,location=? where distributor_id=?",(
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_location.get('1.0',END),
                                                self.var_distributor_id.get()
                                                      
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Distributor Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
            
            
    def delete(self):  
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_distributor_id.get()=="":
                messagebox.showerror("Error","Distributor ID must be required",parent=self.root)
            else:
                cur.execute("Select * from distributor where distributor_id=?",(self.var_distributor_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Distributor ID",parent=self.root)
                else:
                    
                       op=messagebox.askyesno("Confirm","Do You really want to delete this information?",parent=self.root)
                if op==True: 
                    cur.execute("delete from distributor where distributor_id=?",(self.var_distributor_id.get(),)) 
                    con.commit()  
                    messagebox.showinfo("Delete","Distributor Deleted Successfully",parent=self.root)
                    self.clear()
                     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    
           
   
    def clear(self):
        self.var_distributor_id.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_location.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()                    
    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
               
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Distributor ID should be required ",parent=self.root)
              
              
            else: 
                cur.execute("Select* from distributor where distributor_id=?",(self.var_searchtxt.get(),)) 
                row=cur.fetchone()
                if row!=None:
                    self.disrtibutorTable.delete(*self.disrtibutorTable.get_children())
                    self.disrtibutorTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)         
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    
if __name__ =="__main":      
        
    root=Tk()
    obj=distributorClass(root)
    root.mainloop()    
  