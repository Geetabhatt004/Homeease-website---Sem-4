from tkinter import*
from supplier import supplierClass
from manufacture import manufactureClass
from distributor import distributorClass
from inventory import inventoryClass
from product import productClass
class IMS:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Supply Chain System | developed by group 5")
        self.root.config(bg="white")
        
        
          
        #==title===
        title=Label(self.root,text="Supply Managment System",font=("times new roman",60,"bold"),bg="#010c48",fg="white",anchor="w",padx=100,).place(x=0,y=0,relwidth=1,height=120)
        
        #==button logout==
        Btn_logout=Button(self.root,text="Logout",font=("times new roman",20,"bold"),bg="yellow",fg="black",cursor="hand2").place(x=1100,y=40,height=50,width=150)
      
      
        #===clock==
        self.lbl_clock=Label(self.root,text=" Welcome to Supply Managment System\t\t Date: DD-MM-YY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4D6363",fg="white")
        self.lbl_clock.place(x=0,y=120,relwidth=1,height=50)
        
       
        #===LEFT MENU BTN===
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=170,height=520,width="250")
        
        
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",34),bg="#009688",fg="white",cursor="hand2").pack(side=TOP,fill=X)
      
       
        
        btn_suppliers=Button(LeftMenu,text="Suppliers",command=self.supplier,font=("times new roman",20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_Manufacturs=Button(LeftMenu,text="Manufactures",command=self.manufacture,font=("times new roman",20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_Distributors=Button(LeftMenu,text="Distributors",command=self.distributor,font=("times new roman",20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_Intentory=Button(LeftMenu,text="Intentory",command=self.inventory,font=("times new roman",20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_Orders=Button(LeftMenu,text="Orders",command=self.order,font=("times new roman",20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X) 
        
        btn_Logistics=Button(LeftMenu,text="Logistics",font=("times new roman",20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_Exit=Button(LeftMenu,text="Exit",font=("times new roman",20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        
        
        
        #==content==
        self.lbl_supplier=Label(self.root,text="Total Suppliers\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))
        self.lbl_supplier.place(x=300,y=250,height=150,width=320)
        
        self.lbl_manufactures=Label(self.root,text="Total Manufactures\n[0]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("times new roman",20,"bold"))
        self.lbl_manufactures.place(x=650,y=250,height=150,width=320)
        
        self.lbl_distributors=Label(self.root,text="Total Distributors\n[0]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("times new roman",20,"bold"))
        self.lbl_distributors.place(x=1000,y=250,height=150,width=320)
        
        self.lbl_inventory=Label(self.root,text="Total Inventory\n[0]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("times new roman",20,"bold"))
        self.lbl_inventory.place(x=650,y=450,height=150,width=320)
        
        self.lbl_order=Label(self.root,text="Total Orders\n[0]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("times new roman",20,"bold"))
        self.lbl_order.place(x=300,y=450,height=150,width=320)
        
        self.lbl_logistics=Label(self.root,text="Total Logistics\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))
        self.lbl_logistics.place(x=1000,y=450,height=150,width=320)
        
        #==fotter==
        
        lbl_footer=Label(self.root,text="Supply Chain System\n DEveloped by Group 5\n major project of DBMS|Submitted to - JOYTI MA'AM",font=("times new roman",14),bg="#4D6363",fg="white")
        lbl_footer.pack(side=BOTTOM,fill=X)
#===========================================================


    def supplier(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=supplierClass(self.new_win)
      
    def manufacture(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=manufactureClass(self.new_win)
      
    def distributor(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=distributorClass(self.new_win)
      
    def inventory(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=inventoryClass(self.new_win)
      
    def order(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=productClass(self.new_win)
    
    
if __name__ =="__main__"  :
        
        
     root=Tk()
     obj=IMS(root)
     root.mainloop()
