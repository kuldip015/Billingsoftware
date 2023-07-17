from tkinter import *
from tkinter import ttk # for  using the combobox,entry filled etc...
from PIL import Image , ImageTk # what is pillow and pip install pillow
import random
from tkinter import messagebox

class bill_app:
    def __init__(self,root): #constructor
        self.root=root
        self.root.geometry("1530x800+0+0") #widthxheight+x+y
        self.root.title(" Billing Software ") #this is use for the title in gui.
        
        #===========variables==============
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        
        
        #product catrgories list
        self.cate=["Select Option","Clothing","Lifestyle","Mobiles"]
        self.subcatcloth=["Pants","T-shirt","Shirt"]
        self.pant=["Levis","Mufti","Spyker"]
        self.pri_levis=5000
        self.pri_mufti=1000
        self.pri_spyker=3400
        self.tshirt=["Jockey","Calvin Klein","USpolo","Arrow"]
        self.pri_jockey=2000
        self.pri_calkle=4000
        self.pri_polo=1500
        self.pri_arrow=1000
        
        self.shirt=["Peter England","Louis Phillipe","Park Avenue","Denim"]
        self.pri_petereng=2500
        self.pri_louphi=3000
        self.pri_parave=3500
        self.pri_denim=4000
        
        
        
        #subcatlifestyle
        self.subcatlstle=["Bath soap","Face Wash","Hair oil"]
        self.bath_soap=["Detol","LifeBoy","Cinthol","Pearl"]
        self.pri_deol=30
        self.pri_life=20
        self.pri_cinol=40
        self.pri_pearl=30
        
        self.Face_Wash=["Mama's earth","Himalay","Pantjali"]
        self.pri_mamaear=100
        self.pri_himalay=90
        self.pri_pantjali=40
        
        
        self.Hair_oil=["Bajaj","Jashmin","Parachute"]
        self.pri_bajaj=30
        self.pri_jashmin=20
        self.pri_parachute=40
        
        
        
        
        #subcatmobile
        self.subcatMob=["Iphone","Sumsung","Xiome","RealMe","One+"]
        self.iphone=["Iphone X","Iphone_11","Iphone_12","Iphone_13"]
        self.pri_ix=40000
        self.pri_i11=60000
        self.pri_i12=85000
        
        self.samsung=["Smasung M16","Smasung M12","Smasung M21"]
        self.pri_sm16=16000
        self.pri_sm12=12000
        self.pri_sm21=18000
        
        self.xiome=["Redmi-11","Redmi-12","RedmePro"]
        self.pri_r11=11000
        self.pri_r12=12000
        self.pri_rpro=9000
        
        self.realme=["RealMe 12","RealMe 13","RealMe Pro"]
        self.pri_rel12=15000
        self.pri_rel13=16000
        self.pri_relpro=17000
        
        
        self.oneplus=["OnePlus1","OnePlus2","OnePlus3"]
        self.pri_one1=45000
        self.pri_one2=60000
        self.pri_one3=45800
        
        
         #image1  for show the image in gui i have use this pip install Image
        img=Image.open("img2.jpeg") #open image
        img=img.resize((510,130),Image.ANTIALIAS) #ANTIALIAS convert high level image in low level image.
        self.photoimg=ImageTk.PhotoImage(img)   #ImageTK() convert image to photo. self use for class variable.
        
        lbl_img=Label(self.root,image=self.photoimg)  #for dispaly image in gui using label method. use in window powershell pip install Lable
        lbl_img.place(x=0,y=0,width=510,height=130)   #in this we have use same size of  image as we can display in img  object like x,y,width,height.
        
        
        # image2
        img1=Image.open("img3.jpg")
        img1=img1.resize((510,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbl1_img=Label(self.root,image=self.photoimg1)
        lbl1_img.place(x=510,y=0,width=510,height=130)


         # image3
        img2=Image.open("img1.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbl2_img=Label(self.root,image=self.photoimg2)
        lbl2_img.place(x=1020,y=0,width=550,height=130)
        
        #using for title
        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="black",fg="red") #text= which title you have to gave it. then in font we have use diffrent type of font and font size and font charestic and then bg of white and fore ground(text color) color red 
        lbl_title.place(x=0,y=130,width=1530,height=45)
        
        #create a frame (frame work as a contanier)
        main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white") #bd=boder size relief=for boder type,simply use the function in container.
        main_frame.place(x=0,y=175,width=1530,height=620)
        
        #customer labelminiframe
        
        cust_frame=LabelFrame(main_frame,bd=5,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")#in labelframe we can give the text in it. in this we can make frame in main_frame so we have use main_frame not use self.root and then we also text in it also modify the text.
        cust_frame.place(x=10,y=5,width=350,height=140) # in this we have work in main frame so we can use y=5 and x=10 .
        
        
        self.lbl_mol=Label(cust_frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white") # in customer frame use mobile no.
        self.lbl_mol.grid(row=0,column=0,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        #entry filed for mobileno.
        self.entry_mob=ttk.Entry(cust_frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=24) # for enter the mobile number we have use entry filled in it and here ttk.entry for call this method.
        self.entry_mob.grid(row=0,column=1)
          
          
        self.lbl_name=Label(cust_frame,text="Customer Name",font=("times new roman",12,"bold"),bg="white",bd=4) # in customer frame use mobile no.
        self.lbl_name.grid(row=1,column=0,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        #entry filled of custmoer name
        self.entry_name=ttk.Entry(cust_frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24) # for enter the mobile number we have use entry filled in it and here ttk.entry for call this method.
        self.entry_name.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        
        self.lbl_email=Label(cust_frame,text="Email",font=("times new roman",12,"bold"),bg="white",bd=4) # in customer frame use mobile no.
        self.lbl_email.grid(row=2,column=0,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        
        #entry filled of email
        self.entry_email=ttk.Entry(cust_frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24) # for enter the mobile number we have use entry filled in it and here ttk.entry for call this method.
        self.entry_email.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        #product labelframe
        
        prod_frame=LabelFrame(main_frame,bd=5,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")#in labelframe we can give the text in it. in this we can make frame in main_frame so we have use main_frame not use self.root and then we also text in it also modify the text.
        prod_frame.place(x=370,y=5,width=650,height=140) # in this we have work in main frame so we can use y=5 and x=10 .
        
        #category
        self.lbl_cat=Label(prod_frame,text="Select Categories",font=("times new roman",12,"bold"),bg="white",bd=4) # in customer frame use mobile no.
        self.lbl_cat.grid(row=0,column=0,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        self.combo_cat=ttk.Combobox(prod_frame,value=self.cate,font=("times new roman",12,"bold"),width=24,state="readonly")#value=put variable as a list
        self.combo_cat.current(0) #for show the first select option
        self.combo_cat.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_cat.bind("<<ComboboxSelected>>",self.categories)
         
        #subcategory
        self.lbl_subcat=Label(prod_frame,text="Subcategories",font=("times new roman",12,"bold"),bg="white",bd=4) # in customer frame use mobile no.
        self.lbl_subcat.grid(row=1,column=0,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        self.combo_subcat=ttk.Combobox(prod_frame,value=[""],font=("times new roman",12,"bold"),width=24,state="readonly")
        self.combo_subcat.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.combo_subcat.bind("<<ComboboxSelected>>",self.product_add)
    
        #product name
        self.lbl_pname=Label(prod_frame,text="Product Name",font=("times new roman",12,"bold"),bg="white",bd=4) # in customer frame use mobile no.
        self.lbl_pname.grid(row=2,column=0,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        self.combo_pname=ttk.Combobox(prod_frame,textvariable=self.product,font=("times new roman",12,"bold"),width=24,state="readonly")
        self.combo_pname.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.combo_pname.bind("<<ComboboxSelected>>",self.price)
        
        #price
        self.lbl_pri=Label(prod_frame,text="Price",font=("times new roman",12,"bold"),bg="white",bd=4) # in customer frame use mobile no.
        self.lbl_pri.grid(row=0,column=2,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        self.combo_pri=ttk.Combobox(prod_frame,font=("times new roman",12,"bold"),width=24,state="readonly",textvariable=self.prices)
        self.combo_pri.grid(row=0,column=3,sticky=W,padx=5,pady=2)
         
        
        #Qty
        self.lbl_qty=Label(prod_frame,text="Qty",font=("times new roman",12,"bold"),bg="white",bd=4) # in customer frame use mobile no.
        self.lbl_qty.grid(row=1,column=2,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        self.entry_qty=ttk.Entry(prod_frame,textvariable=self.qty,font=("times new roman",12,"bold"),width=24)
        self.entry_qty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        
        #middle frame
        mid_frame=Frame(main_frame,bd=10)
        mid_frame.place(x=10,y=150,width=1000,height=345)
        
        img3=Image.open("img4.jpg")
        img3=img3.resize((1500,340),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lbl3_img=Label(mid_frame,image=self.photoimg3)
        lbl3_img.place(x=0,y=0,width=1500,height=340)
        
        

        
        #search
        search_frame=Frame(main_frame,bd=2)
        search_frame.place(x=1025,y=10,width=500,height=40)
        
        self.lbl_bill=Label(search_frame,text="Bill Number",font=("times new roman",12,"bold"),bg="red",fg="white") # in customer frame use mobile no.
        self.lbl_bill.grid(row=0,column=0,sticky=W) # for sticky label can move around and padx and pady use for padding in customer frame
        
        self.entry_billnum=ttk.Entry(search_frame,textvariable=self.search_bill,font=("times new roman",12,"bold"),width=24)
        self.entry_billnum.grid(row=0,column=1,sticky=W)
        
        self.btn_search=Button(search_frame,height=1,text="Search",font=("times new roman",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btn_search.grid(row=0,column=2,sticky=W)
        
        #Rightframe for bill area
        
        rig_frame=LabelFrame(main_frame,bd=5,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        rig_frame.place(x=1030,y=45,width=480,height=440)
        
        
        scroll_y=Scrollbar(rig_frame,orient=VERTICAL)
        self.textarea=Text(rig_frame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold")) 
        scroll_y.pack(side=RIGHT,fill=Y) 
        scroll_y.config(command=self.textarea.yview) # config the textarea in it.
        self.textarea.pack(fill=BOTH,expand=1) #fill both side and expand both side well
        
        
       #bill counter lableframe
        billcon_frame=LabelFrame(main_frame,bd=5,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")#in labelframe we can give the text in it. in this we can make frame in main_frame so we have use main_frame not use self.root and then we also text in it also modify the text.
        billcon_frame.place(x=0,y=485,width=1520,height=125) # in this we have work in main frame so we can use y=5 and x=10 .
         
        #subtotal
        self.lbl_subtotal=Label(billcon_frame,text="Subtotal",font=("times new roman",12,"bold"),bg="white",bd=4) # in customer frame use mobile no.
        self.lbl_subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        self.entry_subtotal=ttk.Entry(billcon_frame,textvariable=self.sub_total,font=("times new roman",12,"bold"),width=24)
        self.entry_subtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
         #tax
        self.lbl_tax=Label(billcon_frame,text="Tax",font=("times new roman",12,"bold"),bg="white",bd=4) # in customer frame use mobile no.
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        self.entry_tax=ttk.Entry(billcon_frame,textvariable=self.tax_input,font=("times new roman",12,"bold"),width=24)
        self.entry_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        #taxamounttotal
        self.lbl_taxatotal=Label(billcon_frame,text="Total",font=("times new roman",12,"bold"),bg="white",bd=4) # in customer frame use mobile no.
        self.lbl_taxatotal.grid(row=2,column=0,sticky=W,padx=5,pady=2) # for sticky label can move around and padx and pady use for padding in customer frame
        
        self.entry_taxatotal=ttk.Entry(billcon_frame,textvariable=self.total,font=("times new roman",12,"bold"),width=24)
        self.entry_taxatotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        #Button frame
        
        btn_frame=Frame(billcon_frame,bd=2,bg="white")
        btn_frame.place(x=320,y=0)
        
        self.btn_atc=Button(btn_frame,command=self.AddItem,height=2,text="Add To Cart",font=("times new roman",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btn_atc.grid(row=0,column=0)
        
        self.btn_gb=Button(btn_frame,command=self.gen_bill,height=2,text="Generate Bill",font=("times new roman",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btn_gb.grid(row=0,column=1)
        
        self.btn_saveb=Button(btn_frame,command=self.save_bill,height=2,text="Save Bill",font=("times new roman",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btn_saveb.grid(row=0,column=2)
        
        self.btn_pri=Button(btn_frame,height=2,text="Print",font=("times new roman",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btn_pri.grid(row=0,column=3)
        
        self.btn_cle=Button(btn_frame,height=2,text="Clear",font=("times new roman",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btn_cle.grid(row=0,column=4)
        
        self.btn_exit=Button(btn_frame,height=2,text="Exit",font=("times new roman",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btn_exit.grid(row=0,column=5)
        self.welcome()
        self.l=[]
   #**********************Function Declaration**********************************
    def AddItem(self):
         Tax=1
         self.n=self.prices.get()
         self.m=self.qty.get()*self.n 
         self.l.append(self.m)
         if self.product.get=="":
            messagebox.showerror("Error","Please Select the Product Name")     
         else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))
    #************************** generate Bill *************************************
    
    
    
    def gen_bill(self):        
           if self.product.get()=="":
              messagebox.showerror("Error","Please Add to Cart Product") 
           else:   
              text=self.textarea.get(10.0,(10.0+float(len(self.l))))
              self.welcome()
              self.textarea.insert(END,text)
              self.textarea.insert(END,"\n=================================================")
              self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
              self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
              self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
              self.textarea.insert(END,"\n=================================================")
              
   #***************************save bill ***********************************
    def save_bill(self):
              op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
              if op>0:
                     self.bill_data=self.textarea.get(1.0,END)
                     f1=open('bills/'+str(self.bill.get())+".txt",'w')
                     f1.write(self.bill_data)
                     f1.close()
                     
              
     #****************************welcome page************************************   
    def welcome(self): 
         self.textarea.delete(1.0,END) 
         self.textarea.insert(END,"\t\t Welcome Mini Mall")
         self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()} ")
         self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()} ")
         self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()} ")
         self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()} ")
         
         self.textarea.insert(END,"\n=================================================")
         self.textarea.insert(END,f"\nProducts\t\t\tQTY\t\tPrice")
         self.textarea.insert(END,"\n=================================================")
   #conncet the cat to sub cat     
    def categories(self,event=""):
        if self.combo_cat.get()=="Clothing":
            self.combo_subcat.config(values=self.subcatcloth)
            self.combo_subcat.current(0)
            
        if self.combo_cat.get()=="Lifestyle":
            self.combo_subcat.config(values=self.subcatlstle)
            self.combo_subcat.current(0)
            
        if self.combo_cat.get()=="Mobiles":
            self.combo_subcat.config(values=self.subcatMob)
            self.combo_subcat.current(0)
            
            
    
    #all product connect with subcategories
    def product_add(self,event=""):
        #clothings
        if self.combo_subcat.get()=="Pants":
            self.combo_pname.config(values=self.pant)      
            self.combo_pname.current(0)
            
        if self.combo_subcat.get()=="T-shirt":
            self.combo_pname.config(values=self.tshirt)      
            self.combo_pname.current(0)
        
        if self.combo_subcat.get()=="Shirt":
            self.combo_pname.config(values=self.shirt)      
            self.combo_pname.current(0)
        
        #lifestyle    
        if self.combo_subcat.get()=="Bath soap":
            self.combo_pname.config(values=self.bath_soap)      
            self.combo_pname.current(0)
        
        if self.combo_subcat.get()=="Face Wash":
            self.combo_pname.config(values=self.Face_Wash)      
            self.combo_pname.current(0)
        
        if self.combo_subcat.get()=="Hair oil":
            self.combo_pname.config(values=self.Hair_oil)      
            self.combo_pname.current(0)    
        
        #mobile    
        if self.combo_subcat.get()=="Iphone":
            self.combo_pname.config(values=self.iphone)      
            self.combo_pname.current(0)
         
        if self.combo_subcat.get()=="Sumsung":
            self.combo_pname.config(values=self.samsung)      
            self.combo_pname.current(0)
        
        if self.combo_subcat.get()=="Xiome":
            self.combo_pname.config(values=self.xiome)      
            self.combo_pname.current(0)   
        
        if self.combo_subcat.get()=="RealMe":
            self.combo_pname.config(values=self.realme)      
            self.combo_pname.current(0)       
        
        if self.combo_subcat.get()=="One+":
            self.combo_pname.config(values=self.oneplus)      
            self.combo_pname.current(0)    
    
    def price(self,event=""):
        #pant
        if self.combo_pname.get()=="Levis" :
           self.combo_pri.config(value=self.pri_levis) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Mufti" :
           self.combo_pri.config(value=self.pri_mufti) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Spyker" :
           self.combo_pri.config(value=self.pri_spyker) 
           self.combo_pri.current(0)         
           self.qty.set(1)
           
            
        #t-shirt
        if self.combo_pname.get()=="Jockey" :
           self.combo_pri.config(value=self.pri_levis) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Calvin Klein" :
           self.combo_pri.config(value=self.pri_calkle) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="USpolo" :
           self.combo_pri.config(value=self.pri_polo) 
           self.combo_pri.current(0)         
           self.qty.set(1)
        
        if self.combo_pname.get()=="Arrow" :
           self.combo_pri.config(value=self.pri_arrow) 
           self.combo_pri.current(0)         
           self.qty.set(1)
         
         #shirt
        if self.combo_pname.get()=="Peter England" :
           self.combo_pri.config(value=self.pri_petereng) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Louis Phillipe" :
           self.combo_pri.config(value=self.pri_louphi) 
           self.combo_pri.current(0)         
           self.qty.set(1)
           
        if self.combo_pname.get()=="Park Avenue" :
           self.combo_pri.config(value=self.pri_parave) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Denim" :
           self.combo_pri.config(value=self.pri_denim) 
           self.combo_pri.current(0)         
           self.qty.set(1)
                 
       #bath soap
        if self.combo_pname.get()=="Detol" :
           self.combo_pri.config(value=self.pri_deol) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Lifeboy" :
           self.combo_pri.config(value=self.pri_life) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Cinthol" :
           self.combo_pri.config(value=self.pri_cinol) 
           self.combo_pri.current(0)         
           self.qty.set(1)
        
        if self.combo_pname.get()=="Pearl" :
           self.combo_pri.config(value=self.pri_pearl) 
           self.combo_pri.current(0)         
           self.qty.set(1)
         
         #Face wash
        if self.combo_pname.get()=="Mama's earth" :
           self.combo_pri.config(value=self.pri_mamaear) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Himalay" :
           self.combo_pri.config(value=self.pri_himalay) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Pantjali" :
           self.combo_pri.config(value=self.pri_pantjali) 
           self.combo_pri.current(0)         
           self.qty.set(1)
        
        #hair oil
        if self.combo_pname.get()=="Bajaj" :
           self.combo_pri.config(value=self.pri_bajaj) 
           self.combo_pri.current(0)         
           self.qty.set(1)
         
        
        if self.combo_pname.get()=="Jashmin" :
           self.combo_pri.config(value=self.pri_jashmin) 
           self.combo_pri.current(0)         
           self.qty.set(1)
           
        if self.combo_pname.get()=="Parachute" :
           self.combo_pri.config(value=self.pri_parachute) 
           self.combo_pri.current(0)         
           self.qty.set(1)
        
        #i-phone
        if self.combo_pname.get()=="Iphone X" :
           self.combo_pri.config(value=self.pri_ix) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Iphone_11" :
           self.combo_pri.config(value=self.pri_i11) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Iphone_12" :
           self.combo_pri.config(value=self.pri_i12) 
           self.combo_pri.current(0)         
           self.qty.set(1)
        
        #Smasung 
        if self.combo_pname.get()=="Smasung M12" :
           self.combo_pri.config(value=self.pri_sm12) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Smasung M16" :
           self.combo_pri.config(value=self.pri_sm16) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Smasung M21" :
           self.combo_pri.config(value=self.pri_sm21) 
           self.combo_pri.current(0)         
           self.qty.set(1)
        
        #redmi
        if self.combo_pname.get()=="Redmi-11" :
           self.combo_pri.config(value=self.pri_r11) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="Redmi-12" :
           self.combo_pri.config(value=self.pri_r12) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="RedmiPro" :
           self.combo_pri.config(value=self.pri_rpro) 
           self.combo_pri.current(0)         
           self.qty.set(1)
        
        #realme
        if self.combo_pname.get()=="RealMe 12" :
           self.combo_pri.config(value=self.pri_rel12) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="RealMe 13" :
           self.combo_pri.config(value=self.pri_rel13) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="RealMe Pro" :
           self.combo_pri.config(value=self.pri_relpro) 
           self.combo_pri.current(0)         
           self.qty.set(1)
        
        #oneplus
        if self.combo_pname.get()=="OnePlus1" :
           self.combo_pri.config(value=self.pri_one1) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="OnePlus2" :
           self.combo_pri.config(value=self.pri_one2) 
           self.combo_pri.current(0)         
           self.qty.set(1)

        if self.combo_pname.get()=="OnePlus3" :
           self.combo_pri.config(value=self.pri_one3) 
           self.combo_pri.current(0)         
           self.qty.set(1)
        
       
         

        
if __name__ == '__main__' : #what is this
    root=Tk()
    obj=bill_app(root)
    root.mainloop()
    