
# coding: utf-8

# In[113]:


import pyodbc
import csv
global conn 
global cursor
conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
cursor = conn.cursor()


from tkinter import *
def Login():
    global nameL
    global pwordL
    global nameEL
    global pwordEL # More globals :D
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.title('Login') # This makes the window title 'login'
 
    intruction = Label(rootA, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
 
    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
    #global advisor
    
    
    
    loginB = Button(rootA, text='Login', command= CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
 
    #
    rootA.mainloop()
    


    

def CheckLogin():
   
    
    
    cursor=conn.cursor()
    var = cursor.execute('(select TOP 1 usertype from dbo.Login where username = ? and passcode = ?)', str(nameEL.get()), str(pwordEL.get()))
    global list_var
    list_var = var.fetchall()
    #print(list_var)########
    if len(list_var) == 0:
        from tkinter import messagebox
        messagebox.showinfo("Invalid Credentials!", "Please enter the correct Username and Password.")
    else:
        global advisor
        advisor=str(nameEL.get())
        rootA.destroy()  #fdestroy the login window
        page_two() #start the home page
        cursor.close() #close the cursor
        conn.close() #close the connection
def page_two():
    global list_var , root_two,flagfilter
    flagfilter=1
    global design_frame , search_frame , searchBut , seach_entry , hframe,nameEL,advisor,dashtree,add_comment_dict
    root_two = Tk()
    root_two.title('Home Page')
    root_two.resizable()
    root_two.state('zoomed') #before maximizing
    #canvas=Canvas(root_two)
    #canvas.grid(sticky='nwes')
    #name = Label(search_frame , text ="Name :  " + list_var[0][0].capitalize())
    #name.grid(row = 0 , column= 0 , sticky = W)
    
    design_frame = Frame(root_two , bg = 'orange',height=50,  padx = 3) ######  FRAME  #########
    design_frame.grid(column = 0 , row = 0 , sticky = 'nsew',columnspan=2)
    root_two.grid_columnconfigure(0, weight = 1)
    import tkinter
    from PIL import ImageTk,Image
    try:
        from PIL import ImageTk,Image
        img=ImageTk.PhotoImage(Image.open('qsapp logo.png'))
        imglabel=Label(design_frame,background='black',image=img,padx=20,pady=5).grid(row=0,column=4,sticky='ew')
        design_frame.columnconfigure(3,weight=1)
    except:
        pass
    try:
        welc_label =Label(design_frame,background='orange',text='Welcome to the Advisor\'s Dashboard',font='Ariel 22',padx=10,pady=5)
        welc_label.grid(row=0,column=2,sticky='e')
    except:
        pass
        
    
    search_frame = Frame(root_two, bg = 'light blue'  , pady = 30,padx=10) #########  FRAME  #########
    search_frame.grid(column = 0, row = 3 , sticky = 'ew',columnspan=2)
    #root_two.columnconfigure(0, weight = 1)
    
    
    #search = Label(search_frame, bg ='Light Green' , text = "Search Client ----> ",width=20)
    searchBut = Button(search_frame , text = 'Search Client', command = search_client) #, command = search_client )
    add_client_button = Button(search_frame , text = "Add new Client",command=add_client) #add functionality to this button , command = page_three

    global search_entry
    search_entry = Entry(search_frame)
  
    
    
    searchBut.grid(row = 0 , column = 1, sticky = 'ew', padx = 5 , pady = 5) ############### SEARCH FRAME #############
    search_entry.grid(row = 0 , column = 0, sticky = 'ew') ############### SEARCH FRAME #############
    add_client_button.grid(row=0,column=2,padx=5,pady=5,sticky='ew')
    
    hframe = Frame(root_two, bg = 'light blue',  padx = 10 , pady = 10 )  ######   FRAME  #########
    hframe.grid(row = 4, column = 0,sticky='nsew',columnspan=2)
    dashframe = Frame(root_two, bg = 'light blue',  padx = 10 , pady = 10,height=10 )  ######   FRAME  #########
    dashframe.grid(row = 1, column = 0,sticky='nwes',columnspan=2)
    #dashframe.grid_propagate(0)
    fframe = Frame(root_two, bg = 'light blue',   padx = 10 , pady = 10 )  ######   FRAME  #########
    fframe.grid(row = 2, column = 0,sticky='nwes',columnspan=2)
    from tkinter import ttk
    #print('yes')
    #details=Frame(dashframe,pady=10)
    #details.pack(side='top')
    #print('yes')
    filterframe=Frame(dashframe,pady=10)
    filterframe.pack(side='top',fill='x')              ###################adding filters
    Label(filterframe,text="Advisor-  "+advisor.capitalize(),padx=10).pack(side='left',fill='x')
    prob_menu = ['Low', 'Medium', 'High','All'] 
    stat_menu=['Open','Closed','All']
    prod_menu=allproducts()#####prod_menu=cursor.execute('select * from dbo.products).fetchall()
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
    
    crsr=conn.cursor()
    
    advisor_menu=crsr.execute('select  name from dbo.advisor').fetchall()
    for index,i in enumerate(advisor_menu):
        advisor_menu[index]=i[0]
    crsr.close()
    
    conn.close()
    import datetime 
    now = datetime.datetime.now() 
    curr_date = now.day #fetching the current date 
    month_dict = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'} 
    curr_month = month_dict[now.month] 
    cur_year = now.year 
    global menu_adv,menu_stat,menu_,menu_prob,menu_mont,menu_yea,menu_dat
    menu_adv=StringVar(filterframe)
    menu_stat = StringVar(filterframe)
    menu_ = StringVar(filterframe)
    menu_prob = StringVar(filterframe)
    menu_mont = StringVar(filterframe)
    menu_yea = StringVar(filterframe) 
    menu_dat = StringVar(filterframe)
    menu_stat.set('Open')
    menu_prob.set('All')
    menu_.set('All')
    menu_dat.set(curr_date) #set the default value to current date 
    menu_mont.set(curr_month) 
    menu_yea.set(cur_year)
    dates = [x for x in range(1,32)] #choices for dates 1-31 
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'] 
    years = [x for x in range(cur_year - 2 , cur_year + 10)] #setting to past two and future 10 years
     
    if(list_var[0][0]=='admin'):
       
        adv=Button(filterframe,text='Reassign',command=reassign)
        adv.pack(side='right')
        OptionMenu(filterframe,menu_adv,*advisor_menu).pack(side='right')
   
    Label(filterframe,text="Status    ",padx=10).pack(side='left',fill='x')
    OptionMenu(filterframe, menu_stat , *stat_menu).pack(side='left')
    
    Label(filterframe,text="Probability    ",padx=10).pack(side='left',fill='x')
    OptionMenu(filterframe, menu_prob , *prob_menu).pack(side='left')
    
    Label(filterframe,text="Product    ",padx=10).pack(side='left',fill='x')
   
    OptionMenu(filterframe, menu_ , *prod_menu).pack(side='left')
    #daframe=Frame(filterframe).pack(side='bottom')
    Label(filterframe,text="Date    ",padx=10).pack(side='left',fill='x')
    OptionMenu(filterframe, menu_dat , *dates).pack(side='left') ############### 
    OptionMenu(filterframe, menu_mont , *months).pack(side='left')
    OptionMenu(filterframe, menu_yea , *years).pack(side='left')
    global var
    var=IntVar()
    filt=Button(filterframe,text='Apply Filter',command=applyfilter,padx=15)
    filt.pack(side='left')
    filt2=Button(filterframe,text="Remove Filter",command=remove_filter,padx=15)
    filt2.pack(side='left')
    refresh=Button(filterframe,text='Refresh',command=refresh_dashtree)
    refresh.pack(side='left')
    
    treeframe=Frame(dashframe)##################adding trees
    treeframe.pack(side='top',fill='x')
    scrollyframe=Frame(treeframe)
    scrollyframe.pack(side='right',fill='y')
    global dashtree
    dashtree = ttk.Treeview(treeframe)
    dashtree.pack(side = 'top')
    
    xscroll=ttk.Scrollbar(treeframe,orient='horizontal',command=dashtree.xview)
    xscroll.pack(fill='x')
    
    yscroll=ttk.Scrollbar(scrollyframe,orient='vertical',command=dashtree.yview)
    yscroll.pack(side='left',fill='y')
    dashtree.configure(xscrollcommand=xscroll.set)
    dashtree.configure(yscrollcommand=yscroll.set)    
    #print('g')
    dashtree['columns'] = ("1","4", "5", "6", "7","8","9", "10","3","11","12","13","14","15",'16')
    dashtree.column("#0", width=5)
    dashtree.column("5", width=80)
    dashtree.column("7", width=85)
    dashtree.column("6", width=150)
    dashtree.column("3", width=50)
    dashtree.column("8", width=450)
    dashtree.column("4", width=100)
    dashtree.column("1", width=60)
    dashtree.column("9", width=50)
    dashtree.column("10", width=50)
    dashtree.column("3", width=50)
    dashtree.column("11", width=100)
    dashtree.column("12", width=50)
    dashtree.column("15", width=60)
    dashtree.column("13", width=50)
    dashtree.column("14", width=60)
    dashtree.column("16", width=250)






    dashtree.heading("1", text="Client_Code")
   

    dashtree.heading("4", text="Name")
    dashtree.heading("5", text="Phone")
    dashtree.heading("6", text="Email")
    dashtree.heading("7", text="Date")
    dashtree.heading("8", text="Comment")
    dashtree.heading("9", text="Product")
    dashtree.heading("10", text="Probability")
    dashtree.heading("3", text="Price Offered")
    dashtree.heading("11", text="Next Call")
    dashtree.heading("12", text="Status")
    dashtree.heading("14", text="Advisor 1")
    dashtree.heading("16", text="Final Feedback")
    dashtree.heading("13", text="Lead")
    dashtree.heading("15", text="Advisor 2")
    
    try:
        #print("Hi")
        global tree
        #list_clients.grid_remove()
        errLabel.grid_remove()
        add_client_button.grid_remove()
                                                    ###these try and except columns are necessary so as to remove previous search results...
    except Exception as e:                          #####....before printing new results
        #print(e)
        #print('Hiw3')
        pass
    try:
        #print('tree')
        #vsb.pack_remove()
        #tree.pack_remove()
        #hsb.pack_remove()
        #scroll_frame.destroy()
        client_search_frame.destroy()
        clent_details_frame.destroy()
    except Exception as e:
        #print(e)
        pass
        
       # print('ok')
    try:
        root_new.destroy()
    except:
        pass
    try:
       # print("Hi")
        global tree
        #list_clients.grid_remove()
        errLabel.grid_remove()
        add_client_button.grid_remove()
                                                    ###these try and except columns are necessary so as to remove previous search results...
    except Exception as e:                          #####....before printing new results
        print(e)
       # print('Hiw3')
        pass
    try:
        #print('tree')
        #vsb.pack_remove()
        #tree.pack_remove()
        #hsb.pack_remove()
        #scroll_frame.destroy()
        client_search_frame.destroy()
        clent_details_frame.destroy()
    except Exception as e:
        print(e)
        
        print('ok')
    try:
        root_new.destroy()
    except:
        pass
   
    dashtree.bind('<Double-1>', selectItemtree)
    dashtreevalue,dashtreevaluenewclient=dashtree_default()
    indexids=0
    for index, i in enumerate( dashtreevalue):
        try:
            dashtree.insert("", index ,str(indexids) , values =(i[0][0],i[0][10],i[0][12],i[0][11],i[0][1],i[0][2],i[0][3],i[0][4],i[0][7],i[0][5],i[0][6],i[0][9],i[0][13],i[0][14],i[0][8]))
            indexids=indexids+1
            #print('df')
        except Exception as e:
            pass
    for index, i in enumerate(dashtreevaluenewclient):
        try:
            dashtree.insert("",END,str(indexids),values=(i[3],i[0],i[2],i[1],"New","New","New","New","New","New","New","New",i[4],i[5]))
            indexids=indexids+1
        except:
            pass

    
  
    root_two.mainloop()
        
def search_client():
    global errLabel , add_client_button, list_clients,vsb,tree,hsb,scroll_frame,client_search_frame,clent_details_frame,client_name,client_email,client_phone,client_advisor1,client_advisor2,client_lead,client_code
    #print(search_entry.get())
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
    
    crsr=conn.cursor()
    global advisor_reassign,advisor_list
    advisor_list=crsr.execute('select  name from dbo.advisor').fetchall()
    for index,i in enumerate(advisor_list):
        advisor_list[index]=i[0]
    crsr.close()
    global var1,flagdatabase
    cursor = conn.cursor()
    flagdatabase=0
    var1 = cursor.execute('select * from dbo.master_table where client_code = ? ',  str(search_entry.get()) ).fetchall()
    if (len(var1))==0:
        var1 =cursor.execute(" select * from dbo.other where email_id=? or phone=?", str(search_entry.get()), str(search_entry.get()) ).fetchall()
        flagdatabase=1
    
   
     # 
        
        
    try:
       # print("Hi")
        global tree
        #list_clients.grid_remove()
        errLabel.grid_remove()
        add_client_button.grid_remove()
                                                    ###these try and except columns are necessary so as to remove previous search results...
    except Exception as e:                          #####....before printing new results
        print(e)
        #print('Hiw3')
        pass
    try:
        print('tree')
        #vsb.pack_remove()
        #tree.pack_remove()
        #hsb.pack_remove()
        #scroll_frame.destroy()
        client_search_frame.destroy()
        clent_details_frame.destroy()
    except Exception as e:
        print(e)
        
        #print('ok')
    try:
        root_new.destroy()
    except:
        pass
    
        
    
    if len(var1) == 0:
        cursor.close()
        conn.close()
        
        errLabel = Label(search_frame, text = "No such Client found!")
        errLabel.grid(row = 1 , column = 0)
    
        
        #add_client_button.grid(row = 1 , column = 1 , padx = 5)

    else:
         
        global client_name,client_email,client_phone,client_lead,client_phone
       # print('yes')
        from tkinter import ttk
        global results
        results=cursor.execute('select * from dbo.followup where client_code = ? or email_id = ? or phone = ? order by product,date_ DESC', str(search_entry.get()), str(search_entry.get()), str(search_entry.get()) ).fetchall()
        #global tree
        #global hsb,vsb
        #hframe.grid_propagate(0)
        #global scroll_frame
        cursor.close()
        conn.close()
        clent_details_frame=Frame(hframe)
        client_search_frame=Frame(hframe)
        client_name=''
        
        client_email=''
        client_phone=''
        client_advisor1=''
        client_advisor2=''
        client_lead=''
        client_code=''
        
        if flagdatabase==1:
            client_name=var1[0][0]
            client_email=var1[0][1]
            client_phone=var1[0][2]
            client_lead=var1[0][3]
            client_advisor1=var1[0][4]
            client_advisor2=var1[0][5]
        else:
            client_code=var1[0][0]
            client_advisor1=var1[0][2]
            client_advisor2=var1[0][3]###########get lead also from there
            
        #print(client_advisor1,client_advisor2)
        if len(results)==0:
            clent_details_frame=Frame(hframe)
            client_search_frame=Frame(hframe)
            clent_details_frame.pack(side='top',fill='x')
            if client_name!= '':
                Label(clent_details_frame,text='Client Name = {}  '.format(client_name),font=('Quick sand',10,'bold')).pack(side='left')
            if  client_phone!='':
                Label(clent_details_frame,text='Phone =  {} '.format(client_phone)).pack(side='left',padx=10)
            if  client_email!='':
                Label(clent_details_frame,text='Email =  {} '.format(client_email)).pack(side='left',padx=10)
            if  client_code!='':
                Label(clent_details_frame,text='Client Code =   {}'.format(client_code)).pack(side='left',padx=10)
            if  client_lead!='':
                Label(clent_details_frame,text='Lead =   {}'.format(client_lead)).pack(side='left',padx=10)
            if client_advisor1!='' and client_advisor2!='':
                try:
                    client_advisor1=client_advisor1.capitalize()
                except:
                    pass
                try: 
                    client_advisor2=client_advisor2.capitalize()
                except:
                    pass
                if client_advisor1==None:
                    client_advisor1=''
                if client_advisor2==None:
                    client_advisor2=''
                string=str(client_advisor1)+' '+str(client_advisor2)
                #print(string)
                Label(clent_details_frame,text='Advisor/s =   {} '.format(string)).pack(side='left',padx=10)
            Label(clent_details_frame,text="No history for the client").pack(side='left',padx=10)
            Button(clent_details_frame,text="Add comment",command=add_comment_new).pack(side='right')
            if flagdatabase==1:
                Button(clent_details_frame,text="Update client",command=update_client).pack(side='right')
            if list_var[0][0]=='admin':
                
                advisor_reassign=StringVar()
                Button(clent_details_frame,text="Reassign",command=reassign_search).pack(side='right')
                OptionMenu(clent_details_frame,advisor_reassign,*advisor_list).pack(side='right')
            #Button(clent_details_frame,text="Add comment",command=add_comment_new).pack(side='right',padx=50)
            print('sjhd')
        else:
            root_new=Tk()
            root_new.title("Client Details")
            root_new.state("zoomed")
            
            clent_details_frame_=Frame(root_new)
            client_search_frame_=Frame(root_new)
            clent_details_frame_.pack(side='top',fill='x')
            if client_name!='':
                Label(clent_details_frame_,text='Client Name = {}  '.format(client_name),font=('Quick sand',10,'bold')).pack(side='left')
            if client_phone!= '':
                Label(clent_details_frame_,text='Phone =  {} '.format(client_phone)).pack(side='left',padx=10)
            if client_email!='':
                Label(clent_details_frame_,text='Email =  {} '.format(client_email)).pack(side='left',padx=10)
            if client_code!='':
                Label(clent_details_frame_,text='Client Code =   {}'.format(client_code)).pack(side='left',padx=10)
            if client_lead!='':
                Label(clent_details_frame_,text='Lead =   {}'.format(client_lead)).pack(side='left',padx=10)
            if client_advisor1!='' or client_advisor2!='':
                try:
                    client_advisor1=client_advisor1.capitalize()
                except:
                    pass
                try: 
                    client_advisor2=client_advisor2.capitalize()
                except:
                    pass
                if client_advisor1==None:
                    client_advisor1=''
                if client_advisor2==None:
                    client_advisor2=''
                string=str(client_advisor1)+' '+str(client_advisor2)
                #print(string)
                Label(clent_details_frame_,text='Advisor/s =   {} {}'.format(client_advisor1.capitalize(),client_advisor2.capitalize())).pack(side='left',padx=10)
            Button(clent_details_frame_,text='Refresh',command=refresh_tree).pack(side='left',padx=10)
            Button(clent_details_frame_,text="Add comment ",command=add_comment).pack(side='right')
            
            if flagdatabase==1:
                Button(clent_details_frame_,text="Update client",command=update_client).pack(side='right')
            if list_var[0][0]=='admin':
                
                advisor_reassign=StringVar(clent_details_frame_
                                          )
                Button(clent_details_frame_,text="Reassign",command=reassign_search).pack(side='right')
                OptionMenu(clent_details_frame_,advisor_reassign,*advisor_list).pack(side='right')
                
            client_search_frame_.pack(side='top',fill='x',pady=10)
            scroll_frame = Frame(client_search_frame_,bg='red')

            scroll_frame.pack(side='right',fill='y')
            
            tree = ttk.Treeview(client_search_frame_)
            tree.pack(side = 'top')

            tree['columns'] = ("1", "5",  "7","8","9", "10","3","11")
            tree.column("1", width=80)
            tree.column("5", width=450)
            tree.column("7", width=80)
            tree.column("10", width=50)
            tree.column("3", width=50)
            tree.column("8", width=80)
            #tree.column("4", width=450)
            tree.column('#0',width=5)
            tree.column('11',width=350)






            #tree.heading("4", text="Client_Code")
            #tree.heading("2", text="Client ID")
            tree.heading("3", text="Price Offered")

            tree.heading("11", text="Final Feedback")

            tree.heading("1", text="Date")
            tree.heading("5", text="Comment")
            #tree.heading("6", text="Assigned to")
            tree.heading("7", text="Product")
            tree.heading("8", text="Probability")
            tree.heading("9", text="Next Call")
            tree.heading("10", text="Status")

            #creating a scroll bar for the data displayed




            

            hsb = ttk.Scrollbar(client_search_frame_, orient="horizontal", command=tree.xview)
            
            hsb.pack( fill = 'x')

            tree.configure(xscrollcommand=hsb.set)











            vsb = ttk.Scrollbar(scroll_frame, orient="vertical",command=tree.yview)

            
            vsb.pack( side = 'left',  fill = 'y')
            print(results)
            
            
            for index, i in enumerate( results):
                tree.insert("", index ,str(index) , values =(i[1:9]))
                print('df')
               





            tree.configure(yscrollcommand=vsb.set)

 ####          
def selectItemtree(a): #to add comment from dashtree ..this function is binded with double click on dashtreee
    global menu_adv,menu_stat,menu_,menu_prob,menu_mont,menu_yea,menu_dat,add_comment_dict
    global dashtree
    curItem = dashtree.selection() #this takes selected entry from dashtree 
    #print(curItem)
    
    add_comment_dict=dashtree.set(curItem)
   # print(add_comment_dict)
    client_details('addcomment')
    #####addd   close  status and as a separete entry to every entry in sql table and open to every entry but product wise '""""""""""""""""""""'"""
def add_comment():######## tree ke side wala
    #global menu_adv,menu_stat,menu_,menu_prob,menu_mont,menu_yea,menu_dat
    client_details('add')
    
def add_comment_new():#### ui mai no histroy waale clients ke side waala
    client_details('new')
    
    pass#global results
    
def add_client():
    global menu_adv,menu_stat,menu_,menu_prob,menu_mont,menu_yea,menu_dat
    client_details('add new client')
    
    pass#######search client  ke side waala
def reassign():########reassign from dashtree,modify the code accordingly
   # global menu_adv,menu_stat,menu_,menu_prob,menu_mont,menu_yea,menu_dat
    #global dashtree
    #items=dashtree.selection() ###to get selected items on dashtree
    #print(menu_adv.get())
    #print(dashtree.identify_row(items[0]))
    #print(items)
    #print(dashtree.get_children())
    #for i in items: #reassigning them by getting there advisor 
     #   conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
       #                user='sales', password='quant123')
      #  cursor = conn.cursor()
        #client_to_be_assigned=(dashtree.set(i)['1'])
        #sql='update dbo.followup set advisor=\'{}\' where client_code=\'{}\''.format(menu_adv.get(),client_to_be_assigned)
        #cursor.execute(sql)
        #conn.commit()
        #cursor.close()
        #conn.close()
    pass
    try:
        refresh_dashtree()
    except Exception as e:
        print(e)
        
        

def applyfilter():
    dashtree.delete(*dashtree.get_children())
    values_,values_1=returnfilter()
    print(values_,values_1)
    itemid=0
    try:
        for index, i in enumerate(values_):
            try:
                #print(tuple(i[0][0:]))
                dashtree.insert("", END ,str(itemid ), values =(i[0][0],i[0][10],i[0][12],i[0][11],i[0][1],i[0][2],i[0][3],i[0][4],i[0][7],i[0][5],i[0][6],i[0][9],i[0][13],i[0][14],i[0][8]))
                itemid=itemid+1
                #print(itemid)
                                
                #print('df')
            except Exception as e:
                print (e)
                pass
    except Exception as e:
        print(e)
        pass
    try:
        for index, i in enumerate(values_1):
            try:
                
                dashtree.insert("",END,str(itemid),values=(i[3],i[0],i[2],i[1],"New","New","New","New","New","New","New","New",i[4],i[5]))
                itemid=itemid+1
                #print(itemid)
            except Exception as e:
                print(e)
                pass
    except :
        pass
    #print("filter applied")
    global menu_adv,menu_stat,menu_,menu_prob,menu_mont,menu_yea,menu_dat,flagfilter
    
   
   # print(menu_prob.get())
    
   # print(menu_mont.get())
    flagfilter=1
    
def remove_filter():
    dashtree.delete(*dashtree.get_children())
    dashtreevalue,dashtreevaluenewclient=dashtree_default()
    indexid=0
    for index, i in enumerate( dashtreevalue):
        try:
            dashtree.insert("", index ,str(indexid ), values =(i[0][0],i[0][10],i[0][12],i[0][11],i[0][1],i[0][2],i[0][3],i[0][4],i[0][7],i[0][5],i[0][6],i[0][9],i[0][13],i[0][14],i[0][8]))
            indexid=indexid+1
            #print('df')
        except Exception as e:
            #print(e)
            pass
    for index, i in enumerate(dashtreevaluenewclient):
        try:
            dashtree.insert("",END,str(indexid),values=(i[3],i[0],i[2],i[1],"New","New","New","New","New","New","New","New",i[4],i[5]))
            indexid=indexid+1
        except Exception as e:
            #print(e)
            pass
    global flagfilter
    global menu_adv,menu_stat,menu_,menu_prob,menu_mont,menu_yea,menu_dat
    menu_stat.set('Open')
    menu_prob.set('All')
    menu_.set('All')
    menu_.set('All')
    import datetime 
    now = datetime.datetime.now() 
    curr_date = now.day #fetching the current date 
    month_dict = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'} 
    curr_month = month_dict[now.month] 
    cur_year = now.year 
    menu_mont.set(curr_month)
    menu_yea.set(cur_year)
    menu_dat.set(curr_date)
    #print('filter removed')
    flagfilter=0
def update_client():
    
    #global root_four,menu_status,menu_leads,clients,feedback,advisors,name,price,phone,email,comment,menu_years,menu_months,menu_dates,menu_products,menu_prob,menu_year_nc,menu_month_nc,menu_date_nc,menu_time_hour,menu_time_min,menu_time_AMorPM
    
   
    global root_four
    root_four = Tk()
    root_four.title('Client Details Editor')
   
    w,h=root_four.winfo_screenwidth(), root_four.winfo_screenheight()
     
    
    heading_frame_update = Frame(root_four , bg = 'orange', height = 70 , padx = 10) ######  FRAME  #########
    heading_frame_update.grid(column = 0 , row = 0 , sticky = 'ew')
    root_four.grid_columnconfigure(0, weight = 1)
    
    
    entry_frame_update = Frame(root_four  , height = 700,width=w, padx = 10) #########  FRAME  #########
    entry_frame_update.grid(column = 0, row = 1 , sticky = 'nsew')
   
    Label(entry_frame_update,text="Enter Client Details",font=('Quicksand',21,'bold')).grid(row=0,column=3,columnspan=2,pady=5,sticky='ew')
    
    
    
    Label(entry_frame_update,text="Client Code :").grid(row=2,column=3,sticky='ew',pady=4)
   
    Label(entry_frame_update,text="Name :").grid(row=4,column=3,sticky='ew',padx = 20,pady=4)
    Label(entry_frame_update,text="Email ID :").grid(row=5,column=3,sticky='ew',padx = 20,pady=4)
    Label(entry_frame_update,text="Phone No. :").grid(row=6,column=3,sticky='ew',padx = 20,pady=4)
 
    
    
    global clients_update,name_update,email_update,phone_update
    clients_update=Entry(entry_frame_update)
    clients_update.grid(row=2,column = 4,columnspan=1,sticky='ew',padx=4)
    name_update=Entry(entry_frame_update)
    name_update.grid(row=4,column=4,sticky='ew',padx=4)
    email_update=Entry(entry_frame_update)
    email_update.grid(row=5,column=4,sticky='ew',padx=4)
    phone_update=Entry(entry_frame_update)
    phone_update.grid(row=6,column=4,sticky='ew',padx=4)
    
    clients_update.insert(END,string=client_code)
    name_update.insert(END,string=client_name.capitalize())
    email_update.insert(END,string=client_email)
    phone_update.insert(END,string=client_phone)#############
    
    
    Button(entry_frame_update,text="Update Client",command=update_client_details).grid(row=7,column=3,columnspan=2,pady=10)
    root_four.mainloop()
    
def update_client_details():
    global clients_update,name_update,email_update,phone_update
    global root_four
    #conn.close()
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
    cursor = conn.cursor()
    
    if (clients_update.get()).strip()=="":
        #cursor=conn.cursor()
        cursor.execute("update dbo.other set name=?,email_id=?,phone=?",name_update.get(),email_update.get(),phone_update.get())
        #print(cursor.fetchall())
    else:
        cursor.execute(('delete from dbo.other where email_id=? and phone=?'),client_email,client_phone)
        cursor.execute(('insert into dbo.master_table values(?,?,?,?)'),clients_update.get(),'',client_advisor1.capitalize(),client_advisor2.capitalize())
        cursor.execute(('update dbo.followup set email_id=?,name=?,phone=?,lead=?,client_code=? where email_id=? and phone=?'  ),'','','','',clients_update.get(),client_email,client_phone)
    cursor.close()
    conn.commit()
    conn.close()
    root_four.destroy()
    try:
        refresh_dashtree()
    except:
        pass
    try:
        #print("Hi")
        global tree
        #list_clients.grid_remove()
        errLabel.grid_remove()
        add_client_button.grid_remove()
                                                    ###these try and except columns are necessary so as to remove previous search results...
    except Exception as e:                          #####....before printing new results
        #print(e)
        #print('Hiw3')
        pass
    try:
        #print('tree')
        #vsb.pack_remove()
        #tree.pack_remove()
        #hsb.pack_remove()
        #scroll_frame.destroy()
        client_search_frame.destroy()
        clent_details_frame.destroy()
    except Exception as e:
        #print(e)
        pass
        
        #print('ok')
    try:
        root_new.destroy()
    except:
        pass
    
        
    pass
def reassign_search():
    global advisor_reassign
    print(advisor_reassign.get(),client_name,client_email,client_advisor1,client_advisor2,client_code)
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
    cursor = conn.cursor()
    try:
        cursor.execute(('update dbo.master_table set advisor2=? where client_code=?'),advisor_reassign.get(),client_code)
    except  Exception as e:
        print(e,'1')
    try:
        cursor.execute(('update dbo.other set advisor2=? where email_id=? and phone=?'),advisor_reassign.get(),client_email,client_phone)
    except Exception as e:
        print(e,'2')
    try:
        cursor.execute(('update dbo.followup set advisor2=? where client_code=? and email_id=? and phone=? '),advisor_reassign.get(),client_code,client_email,client_phone)
    except Exception as e:
        print(e,'3')
    cursor.close()
    conn.commit()
    conn.close()
    try:
        refresh_dashtree()
    except Exception as e:
        print(e)
    #conn.close()
    pass





import tkinter
from tkinter import *
def client_details(mode):
    global month_dict_2
    global menu_status_,menu_leads_,clients,feedback,advisors,name,price,phone,email,comment,menu_years_,menu_months_,menu_dates_,menu_products_,menu_prob_,menu_year_nc_,menu_month_nc_,menu_date_nc_,menu_time_hour_,menu_time_min_,menu_time_AMorPM_
    
   
    #global heading , search_frame , searchBut , seach_entry , hframe
    global root_three
    root_three = Tk()
    root_three.title('Client Details Editor')
    #root_three.attributes('-fullscreen', True)
    root_three.state('zoomed')
    w,h=root_three.winfo_screenwidth(), root_three.winfo_screenheight()
     #before maximizing
    
    #name = Label(search_frame , text ="Name :  " + list_var[0][0].capitalize())
    #name.grid(row = 0 , column= 0 , sticky = W)
    
    heading_frame = Frame(root_three , bg = 'orange', height = 70 , padx = 10) ######  FRAME  #########
    heading_frame.grid(column = 0 , row = 0 , sticky = 'ew')
    root_three.grid_columnconfigure(0, weight = 1)
    
    
    entry_frame = Frame(root_three  , height = 700,width=w, padx = 10) #########  FRAME  #########
    entry_frame.grid(column = 0, row = 1 , sticky = 'nsew')
    #entry_frame.grid_propagate(0)
    #lists=[client_code,date,comment,advisor,product,probability,next_call,status,price_offered,lead,name,email,phoneno]
    #lists='Client Code,Date,Comment,Advisor,Product,Probability,Next Call,Status,Price_Offered,Lead,Name,Email,honeno'.split(',')
    #root_two.columnconfigure(0, weight = 1)
    
    
    
    #search = Label(search_frame, bg ='Light Green' , text = "Search Client ----> ",width=20)
    #searchBut = Button(search_frame , text = 'Search Client', command = search_client) #, command = search_client )
    
    #search_entry = Entry(search_frame)
  
    
    fframe = Frame(root_three, bg = 'white',  height = 450 ,width=450, padx = 10 , pady = 10 )  ######   FRAME  #########
    fframe.grid(row = 4, column = 0,sticky='nwes')
    #heading_frame.grid_propagate(0)
    #hframe.grid_propagate(0)
    #searchBut.grid(row = 0 , column = 1, sticky = 'ew', padx = 5 , pady = 5) ############### SEARCH FRAME #############
    #search_entry.grid(row = 0 , column = 0, sticky = 'ew') ############### SEARCH FRAME #############
    
    
    import datetime
    today= datetime.datetime.today() 
    cur_year = today.year
    
    
    dates = [str(x).zfill(2) for x in range(1,32)] #choices for dates 1-31
    
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    years = [x for x in range(cur_year - 2 , cur_year + 10)] #setting to past two and future 10 years
    prob_menu = ['Low', 'Medium', 'High']
    status_menu = ['Open', 'Closed']
    leads_menu = ['FB forms', 'Website', 'Incoming call','Incoming email','Twitter','Word of mouth','Other']
    products_menu = allproducts()
    time_hour = [str(x).zfill(2) for x in range(1,13)]
    time_min = [str(x).zfill(2) for x in range(0,61,5)]
    am_or_pm = ['AM', 'PM']
    
    
    menu_months_ = StringVar(entry_frame)
    menu_years_ = StringVar(entry_frame)
    menu_dates_ = StringVar(entry_frame)
    menu_prob_ = StringVar(entry_frame)
    menu_status_ = StringVar(entry_frame)
    menu_leads_ = StringVar(entry_frame)
    menu_products_ = StringVar(entry_frame)
    menu_month_nc_ =  StringVar(entry_frame)
    menu_year_nc_ = StringVar(entry_frame)
    menu_date_nc_ = StringVar(entry_frame)
    menu_time_hour_ = StringVar(entry_frame)
    menu_time_min_ = StringVar(entry_frame)
    menu_time_AMorPM_ = StringVar(entry_frame)
    
    
    
    import datetime
    now = datetime.datetime.now()
    curr_date = now.day  #fetching the current date 
    month_dict = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    month_dict_2={}
    month_dict_={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    for key in month_dict_:
        month_dict_2[month_dict_[key]]=key
        
    curr_month = month_dict[now.month]
    curr_year = now.year

    menu_dates_.set(str(curr_date).zfill(2)) #set the default value to current date
    menu_months_.set(curr_month)
    menu_years_.set(cur_year)
    
    menu_date_nc_.set(str(curr_date).zfill(2))
    menu_month_nc_.set(curr_month)
    menu_year_nc_.set(cur_year)
        
    #Labels
    
    Label(entry_frame,text="Enter Client Details",font=('Quicksand',21,'bold')).grid(row=0,columnspan=3,pady=5,sticky='w')
    
    
    Label(entry_frame,text="Date :").grid(row=1,column=0,sticky='w',pady=4)
    Label(entry_frame,text="Client Code :").grid(row=2,column=0,sticky='w',pady=4)
    Label(entry_frame,text="Final Feedback :").grid(row=7,column=0,sticky='w',pady=4)
    
    Label(entry_frame,text="Product :").grid(row=5,column=0,sticky='w',pady=4)
    Label(entry_frame,text="Probability :").grid(row=6,column=0,sticky='w',pady=4)
    Label(entry_frame,text="Next Call :").grid(row=3,column=0,sticky='w',pady=4)
    
    
    Label(entry_frame,text="Status :").grid(row=1,column=3,sticky='w',padx = 20, pady=4)
    Label(entry_frame,text="Lead :").grid(row=2,column=3,sticky='w',padx = 20,pady=4)
    Label(entry_frame,text="Price Offered :").grid(row=3,column=3,sticky='w',padx = 20,pady=4)
    Label(entry_frame,text="Name :").grid(row=4,column=3,sticky='w',padx = 20,pady=4)
    Label(entry_frame,text="Email ID :").grid(row=5,column=3,sticky='w',padx = 20,pady=4)
    Label(entry_frame,text="Phone No. :").grid(row=6,column=3,sticky='w',padx = 20,pady=4)
    Label(entry_frame,text="Comment").grid(row=8,column=0,sticky='w',pady=4)
   
    
    
   
    clients=Entry(entry_frame)
    clients.grid(row=2,column = 1,columnspan=1,sticky='ew',padx=4)
    feedback=Text(entry_frame,height=5)
    feedback.grid(row=7,column = 1,columnspan=4,sticky='ew',padx=4,pady=4,ipadx = 4 , ipady = 4)
   
    price=Entry(entry_frame)
    price.grid(row=3,column=4,sticky='ew',padx=4)
    name=Entry(entry_frame)
    name.grid(row=4,column=4,sticky='ew',padx=4)
    email=Entry(entry_frame)
    email.grid(row=5,column=4,sticky='ew',padx=4)
    phone=Entry(entry_frame)
    phone.grid(row=6,column=4,sticky='ew',padx=4)
    comment=Text(entry_frame,height=5)
    comment.grid(row=8,column=1,columnspan=4,sticky='ew',padx=4,pady=4,ipadx = 4 , ipady = 4)
    
    #entry_frame.grid_columnconfigure(0,weight=1)
    #entry_frame.grid_columnconfigure(1,weight=1)
    #entry_frame.grid_columnconfigure(2,weight=1)
    #entry_frame.grid_columnconfigure(,weight=3)
    
    #creating the date frame 
    
    date_frame = Frame(entry_frame)
    date_frame.grid(row = 1 , column = 1, sticky = 'ew')
    
    next_call_frame = Frame(entry_frame)
    next_call_frame.grid(row = 3 , column = 1 , sticky = 'ew')
    
    
    OptionMenu(entry_frame, menu_leads_ , *leads_menu) .grid(row=2,column=4,sticky='ew',pady=4)
    OptionMenu(entry_frame, menu_prob_ , *prob_menu) .grid(row=6,column=1,sticky='ew',pady=4)
    OptionMenu(entry_frame, menu_status_ , *status_menu) .grid(row=1,column=4,sticky='ew',pady=4)
    OptionMenu(entry_frame, menu_products_ , *products_menu) .grid(row=5,column=1,sticky='ew',pady=4)
    OptionMenu(date_frame, menu_dates_ , *dates) .grid(row=1,column=1,sticky='ew',pady=4) ###############
    OptionMenu(date_frame, menu_months_ , *months) .grid(row=1,column=2,sticky='ew',pady=4)
    OptionMenu(date_frame, menu_years_ , *years) .grid(row=1,column=3,sticky='ew',pady=4)
    
    OptionMenu(next_call_frame, menu_date_nc_ , *dates) .grid(row=1,column=1,sticky='ew',pady=4) ######  NEXT CALL DropDown #####
    OptionMenu(next_call_frame, menu_month_nc_ , *months) .grid(row=1,column=2,sticky='ew',pady=4)
    OptionMenu(next_call_frame, menu_year_nc_ , *years) .grid(row=1,column=3,sticky='ew',pady=4)
    OptionMenu(next_call_frame , menu_time_hour_, *time_hour).grid(row = 1 , column = 4 , sticky = 'ew' , pady = 4 )
    OptionMenu(next_call_frame , menu_time_min_, *time_min).grid(row = 1 , column = 5 , sticky = 'ew' , pady = 4 )
    OptionMenu(next_call_frame , menu_time_AMorPM_, *am_or_pm).grid(row = 1 , column = 6, sticky = 'ew' , pady = 4 )
    
    
    
    
    
    
    
    menu_prob_.set('Low') #set the default value to current date
    menu_status_.set('Open') #set the default value 
    menu_leads_.set('Website') #set the default value
    menu_products_.set('App') #set the default value 
    
    menu_time_AMorPM_.set('PM')
    menu_time_hour_.set('12')
    menu_time_min_.set('00')
    global results,advisor
    print(type(advisor),type('sfs'))
    global var1,add_comment_dict
    if mode=='addcomment':####from dash tree
        submit=Button(entry_frame,text='Add details',font=('Quicksand',12,'bold'),command=create_client_dashtree)
        submit.grid(row=9,column=0,columnspan=5,rowspan=2,pady=34,sticky='ns')
        Label(entry_frame,text="Advisor :").grid(row=4,column=0,sticky='w',pady=4)
        advisors=Entry(entry_frame)
        advisors.grid(row=4,column = 1,columnspan=1,sticky='ew',padx=4)
        #print('add')
        ######modify them accordingly 
        clients.insert(END,string=str(add_comment_dict['1']))
        advisors.insert(END,string=str(advisor))
        name.insert(END,string=str(add_comment_dict['4']))
        email.insert(END,string=str(add_comment_dict['6']))
        phone.insert(END,string=str(add_comment_dict['5']))
        menu_leads_.set(str(add_comment_dict['13']))
        menu_products_.set(add_comment_dict['9'])
        menu_prob_.set(add_comment_dict['10'])
        
        clients.configure(state='readonly')
        advisors.configure(state='readonly')
        email.configure(state='readonly')
        phone.configure(state='readonly')
        name.configure(state='readonly')
        
        
    if mode=='add':##########for add comment at tree ke side waala
        submit=Button(entry_frame,text='Add details',font=('Quicksand',12,'bold'),command=create_client)
        Label(entry_frame,text="Advisor :").grid(row=4,column=0,sticky='w',pady=4)
        submit.grid(row=9,column=0,columnspan=5,rowspan=2,pady=34,sticky='ns')
        advisors=Entry(entry_frame)
        advisors.grid(row=4,column = 1,columnspan=1,sticky='ew',padx=4)
        print('add')
        
        clients.insert(END,string=client_code)
        advisors.insert(END,string=str(advisor).capitalize())
        name.insert(END,string=str(client_name))
        email.insert(END,string=str(client_email))
        phone.insert(END,string=str(client_phone))
        menu_leads_.set(str(client_lead))
        clients.configure(state='readonly')
        advisors.configure(state='readonly')
        email.configure(state='readonly')
        phone.configure(state='readonly')
        name.configure(state='readonly')
        
        
                

                

                

        #clients.insert(END,string=str(results[0][0]))
        #advisors.insert(END,string=str(advisor))
        #name.insert(END,string=str(results[0][11]))
        #email.insert(END,string=str(results[0][12]))
        #phone.insert(END,string=str(results[0][13]))
        #menu_leads.set(results[0][10])#set the default value
       

    if mode=='new': #no histroy ke side wala
       # print('new')
        submit=Button(entry_frame,text='Add details',font=('Quicksand',12,'bold'),command=create_client_new)
        Label(entry_frame,text="Advisor :").grid(row=4,column=0,sticky='w',pady=4)
        advisors=Entry(entry_frame)
        advisors.grid(row=4,column = 1,columnspan=1,sticky='ew',padx=4)
        submit.grid(row=9,column=0,columnspan=5,rowspan=2,pady=34,sticky='ns')
       
        clients.insert(END,string=str(client_code))
        advisors.insert(END,string=str(advisor))
        name.insert(END,string=str(client_name))
        email.insert(END,string=str(client_email))
        phone.insert(END,string=str(client_phone))
        menu_leads_.set(str(client_lead))
        clients.configure(state='readonly')
        advisors.configure(state='readonly')
        email.configure(state='readonly')
        phone.configure(state='readonly')
        name.configure(state='readonly')
        
    if mode=='add new client':####search ke side wala
        global admin_advisor,advisor_list
        admin_advisor=StringVar(entry_frame)
        admin_advisor.set(advisor.capitalize())
        Label(entry_frame,text="Advisor :").grid(row=4,column=0,sticky='w',pady=4)
        admin_advisor.set(advisor)
        submit=Button(entry_frame,text='Create Client',font=('Quicksand',12,'bold'),command=create_client_newest)
        submit.grid(row=9,column=0,columnspan=5,rowspan=2,pady=34,sticky='ns')
        
        clients.configure(state='readonly')
        #advisors.insert(END,string=(str(advisor)).capitalize())
        #advisors.configure(state='readonly')
        if list_var[0][0]=='admin':
            OptionMenu(entry_frame,admin_advisor,*advisor_list).grid(row=4,column = 1,columnspan=1,sticky='ew',padx=4)
        else:
            advisors=Entry(entry_frame)
            advisors.grid(row=4,column = 1,columnspan=1,sticky='ew',padx=4)
            advisors.insert(END,string=advisor.capitalize())
            advisors.configure(state='readonly')
       ##############write a sql query here
        
        
    
    
    
   

  
    root_three.mainloop()
def create_client():
    global month_dict_2
    global menu_status_, menu_leads_,clients,feedback,advisors,name,price,phone,email,comment,menu_years_,menu_months_,menu_dates_,menu_products_,menu_prob_,menu_year_nc_,menu_month_nc_,menu_date_nc_,menu_time_hour_,menu_time_min_,menu_time_AMorPM_
    #print( menu_status, menu_leads,clients,feedback,advisors,name,price,phone,email,comment,menu_years.get(),menu_months.get(),menu_dates.get(),menu_products,menu_prob,menu_year_nc.get(),menu_month_nc.get(),menu_date_nc.get(),menu_time_hour.get(),menu_time_min.get(),menu_time_AMorPM.get())
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
    cursor = conn.cursor()
    if str(menu_status_.get())=='Open':
        cursor.execute(('insert into dbo.followup values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'),str(clients.get()),str(menu_years_.get())
+str(month_dict_2[str(menu_months_.get())])+str(menu_dates_.get()),(str(advisors.get())).capitalize()+": "+str(comment.get('1.0',END)),str(menu_products_.get()),
str(menu_prob_.get() )   ,str(menu_year_nc_.get())+str(month_dict_2[str(menu_month_nc_.get())])+str(menu_date_nc_.get())+" "+str(menu_time_hour_.get())+":"+str(menu_time_min_.get())+":"+"00"+" "+str(menu_time_AMorPM_.get()),
str(menu_status_.get()), 
str(price.get()),str(feedback.get('1.0',END)),str(menu_leads_.get())   ,str(name.get()),str(email.get()),str(phone.get()),client_advisor1,client_advisor2)
        print('done')
    else:
        cursor.execute(('insert into dbo.followup values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'),str(clients.get()),str(menu_years_.get())
+str(month_dict_2[str(menu_months_.get())])+str(menu_dates_.get()),(str(advisors.get())).capitalize()+": "+str(comment.get('1.0',END)),str(menu_products_.get()),
str(menu_prob_.get() )   ,None,
str(menu_status_.get()), 
str(price.get()),str(feedback.get('1.0',END)),str(menu_leads_.get())   ,str(name.get()),str(email.get()),str(phone.get()),client_advisor1,client_advisor2)
        cursor.execute('update dbo.followup set final_feedback=? ,status_=? where( email_id=? and phone=? and client_code=?) and product=?',str(feedback.get('1.0',END)),str(menu_status_.get()),str(email.get()),str(phone.get()),str(clients.get()),str(menu_products_.get()))
    conn.commit()
    cursor.close()
    conn.close()
    root_three.destroy()
    try:
        refresh_dashtree()
    except Exception as e:
        print(e)
   
    print('yes')  
def create_client_new():
    global month_dict_2
    global menu_status, menu_leads,clients,feedback,advisors,name,price,phone,email,comment,menu_years,menu_months,menu_dates,menu_products,menu_prob,menu_year_nc,menu_month_nc,menu_date_nc,menu_time_hour,menu_time_min,menu_time_AMorPM
    #print( menu_status, menu_leads,clients,feedback,advisors,name,price,phone,email,comment,menu_years.get(),menu_months.get(),menu_dates.get(),menu_products,menu_prob,menu_year_nc.get(),menu_month_nc.get(),menu_date_nc.get(),menu_time_hour.get(),menu_time_min.get(),menu_time_AMorPM.get())
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
    cursor = conn.cursor()
    if str(menu_status_.get())=='Open':
        cursor.execute(('insert into dbo.followup values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'),str(clients.get()),str(menu_years_.get())
+str(month_dict_2[str(menu_months_.get())])+str(menu_dates_.get()),(str(advisors.get())).capitalize()+": "+str(comment.get('1.0',END)),str(menu_products_.get()),
str(menu_prob_.get() )   ,str(menu_year_nc_.get())+str(month_dict_2[str(menu_month_nc_.get())])+str(menu_date_nc_.get())+" "+str(menu_time_hour_.get())+":"+str(menu_time_min_.get())+":"+"00"+" "+str(menu_time_AMorPM_.get()),
str(menu_status_.get()), 
str(price.get()),str(feedback.get('1.0',END)),str(menu_leads_.get())   ,str(name.get()),str(email.get()),str(phone.get()),client_advisor1,client_advisor2)
        print('done')
    else:
        cursor.execute(('insert into dbo.followup values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'),str(clients.get()),str(menu_years_.get())
+str(month_dict_2[str(menu_months_.get())])+str(menu_dates_.get()),(str(advisors.get())).capitalize()+": "+str(comment.get('1.0',END)),str(menu_products_.get()),
str(menu_prob_.get() )   ,None,
str(menu_status_.get()), 
str(price.get()),str(feedback.get('1.0',END)),str(menu_leads_.get())   ,str(name.get()),str(email.get()),str(phone.get()),client_advisor1,client_advisor2)
        cursor.execute('update dbo.followup set final_feedback=? ,status_=? where (email_id=? and phone=? and client_code=?) and product=?',str(feedback.get('1.0',END)),str(menu_status_.get()),str(email.get()),str(phone.get()),str(clients.get()),str(menu_products_.get()))
    conn.commit()
    cursor.close()
    conn.close()
    root_three.destroy()
    try:
        refresh_dashtree()
    except Exception as e:
        print(e)
### 
def create_client_newest():
    print('I am in')
   
    

    global month_dict_2,root_three
    
    global menu_status_, menu_leads_,clients,feedback,advisors,name,price,phone,email,comment,menu_years_,menu_months_,menu_dates_,menu_products_,menu_prob_,menu_year_nc_,menu_month_nc_,menu_date_nc_,menu_time_hour_,menu_time_min_,menu_time_AMorPM_
    #print( menu_status, menu_leads,clients,feedback,advisors,name,price,phone,email,comment,menu_years.get(),menu_months.get(),menu_dates.get(),menu_products,menu_prob,menu_year_nc.get(),menu_month_nc.get(),menu_date_nc.get(),menu_time_hour.get(),menu_time_min.get(),menu_time_AMorPM.get())
    #print(type(str(clients.get())),type(str(menu_years_.get())),'yes',type(str(month_dict_2[str(menu_months_.get())])),type(str(menu_dates_.get())))
    #print(menu_years_.get(),str(month_dict_2[str(menu_months_.get())]))
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
    cursor = conn.cursor()
    if list_var[0][0] =='admin':
        x=admin_advisor.get()
    else:
        x=advisors.get()
    if str(menu_status_.get())=='Open':
        cursor.execute(('insert into dbo.followup values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'),str(clients.get()),str(menu_years_.get())
+str(month_dict_2[str(menu_months_.get())])+str(menu_dates_.get()),advisor.capitalize()+": "+str(comment.get('1.0',END)),str(menu_products_.get()),
str(menu_prob_.get() )   ,str(menu_year_nc_.get())+str(month_dict_2[str(menu_month_nc_.get())])+str(menu_date_nc_.get())+" "+str(menu_time_hour_.get())+":"+str(menu_time_min_.get())+":"+"00"+" "+str(menu_time_AMorPM_.get()),
str(menu_status_.get()), 
str(price.get()),str(feedback.get('1.0',END)),str(menu_leads_.get())   ,str(name.get()),str(email.get()),str(phone.get()),x,'')
       # print('done')
        cursor.execute(('insert into dbo.other values (?,?,?,?,?,?)'),str(name.get()),str(email.get()),str(phone.get()),str(menu_leads_.get()),x,'')
    else:
        cursor.execute(('insert into dbo.followup values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'),str(clients.get()),str(menu_years_.get())
+str(month_dict_2[str(menu_months_.get())])+str(menu_dates_.get()),advisor.capitalize()+": "+str(comment.get('1.0',END)),str(menu_products_.get()),
str(menu_prob_.get() )   ,None,
str(menu_status_.get()), 
str(price.get()),str(feedback.get('1.0',END)),str(menu_leads_.get())   ,str(name.get()),str(email.get()),str(phone.get()),x,'')
        cursor.execute('update dbo.followup set final_feedback=? ,status_=? where (email_id=? and phone=? and client_code=?) and product=?',str(feedback.get('1.0',END)),str(menu_status_.get()),str(email.get()),str(phone.get()),str(clients.get()),str(menu_products_.get()))
        cursor.execute(('insert into dbo.other values (?,?,?,?,?,?)'),str(name.get()),str(email.get()),str(phone.get()),str(menu_leads_.get()),x,'')
    cursor.close()
    
    conn.commit()
    conn.close()
    root_three.destroy()
    try:
        refresh_dashtree()
    except Exception as e:
        print(e)
def create_client_dashtree():
    global month_dict_2,add_comment_dict
    global menu_status_, menu_leads_,clients,feedback,advisors,name,price,phone,email,comment,menu_years_,menu_months_,menu_dates_,menu_products_,menu_prob_,menu_year_nc_,menu_month_nc_,menu_date_nc_,menu_time_hour_,menu_time_min_,menu_time_AMorPM_
    #print( menu_status, menu_leads,clients,feedback,advisors,name,price,phone,email,comment,menu_years.get(),menu_months.get(),menu_dates.get(),menu_products,menu_prob,menu_year_nc.get(),menu_month_nc.get(),menu_date_nc.get(),menu_time_hour.get(),menu_time_min.get(),menu_time_AMorPM.get())
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
    cursor = conn.cursor()
    if str(menu_status_.get())=='Open':
        cursor.execute(('insert into dbo.followup values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'),str(clients.get()),str(menu_years_.get())
+str(month_dict_2[str(menu_months_.get())])+str(menu_dates_.get()),(str(advisors.get())).capitalize()+": "+str(comment.get('1.0',END)),str(menu_products_.get()),
str(menu_prob_.get() )   ,str(menu_year_nc_.get())+str(month_dict_2[str(menu_month_nc_.get())])+str(menu_date_nc_.get())+" "+str(menu_time_hour_.get())+":"+str(menu_time_min_.get())+":"+"00"+" "+str(menu_time_AMorPM_.get()),
str(menu_status_.get()), 
str(price.get()),str(feedback.get('1.0',END)),str(menu_leads_.get())   ,str(name.get()),str(email.get()),str(phone.get()),add_comment_dict['14'],add_comment_dict['15'])
        #print('done')
    else:
        cursor.execute(('insert into dbo.followup values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'),str(clients.get()),str(menu_years_.get())
+str(month_dict_2[str(menu_months_.get())])+str(menu_dates_.get()),(str(advisors.get())).capitalize()+": "+str(comment.get('1.0',END)),str(menu_products_.get()),
str(menu_prob_.get() )   ,None,
str(menu_status_.get()), 
str(price.get()),str(feedback.get('1.0',END)),str(menu_leads_.get())   ,str(name.get()),str(email.get()),str(phone.get()),add_comment_dict['14'],add_comment_dict['15'])  
        cursor.execute('update dbo.followup set final_feedback=? ,status_=? where( email_id=? and phone=? and client_code=?) and product=?',str(feedback.get('1.0',END)),str(menu_status_.get()),str(email.get()),str(phone.get()),str(clients.get()),str(menu_products_.get()))
    conn.commit()
    cursor.close()
    conn.close()
    root_three.destroy()
    try:
        refresh_dashtree()
    except Exception as e:
        print(e)
   
    #print('yes')  
    pass

def refresh_tree():
    pass
# put in try and  except
def refresh_dashtree():
    global dashtree
    dashtree.delete(*dashtree.get_children())
    remove_filter()
    pass


def dashtree_default():
    import pyodbc
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                           user='sales', password='quant123')
    cursor = conn.cursor()
    import datetime
    global advisor
    nows = datetime.datetime.now()+datetime.timedelta(1)
    current_date = nows.day  #fetching the current date 
    month_dictionary = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}



    current_month = month_dictionary[nows.month]
    current_year = nows.year

    sql='select * from(select max(next_call) as next_call,product,email_id,client_code,phone from dbo.followup where ( advisor1=\'{}\' or advisor2=\'{}\') and status_=\'open\'  group by email_id,product,client_code,phone ) as abc where next_call<\'{}\'  order by next_call DESC'.format(advisor,advisor,str(current_year)+str(nows.month).zfill(2)+str(current_date).zfill(2))
    cursor.execute(sql)
    lists=cursor.fetchall()
    #sql='( select def.client_code,def.email_id,def.phone,def.advisor1,def.advisor2 from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select '' as email_id ,'' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select email_id, phone, '' as client_code,advisor1,advisor2 from dbo.other)) as def where abc.client_code != def.client_code and abc.email_id != def.email_id and abc.phone != def.phone and (advisor1=\'{}\' or advisor2=\'{}\')) '.format(advisor,advisor)

    answer=[]
    cursor=conn.cursor()
    sql='select * from((select \'\' as name, \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select name, email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as x where advisor1=? or advisor2=?' 
#sql='( select def.client_code,def.email_id,def.phone,def.advisor1,def.advisor2 from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as def where abc.client_code != def.client_code and abc.email_id != def.email_id and abc.phone != def.phone and (def.advisor1=\'neel\' or def.advisor2=\'neel\'))' 
    cursor.execute(sql,advisor,advisor)
    sql2=' select * from (select  email_id,phone,client_code,max(advisor1) as advisor1,max(advisor2) as advisor2 from dbo.followup     group by client_code,phone,email_id) as abc where advisor1=? or advisor2=?'
    newclients=(cursor.fetchall())
    cursor.execute(sql2,advisor,advisor)
    b1=cursor.fetchall()
    for i in b1:
        for j in newclients:
            if (i[0]==j[1] and i[1]==j[2] and i[2]==j[3]):
                print(j,i)
                newclients.remove(j)

        #sql='( select def.client_code,def.email_id,def.phone,def.advisor1,def.advisor2,def.name from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select \'\' as name, \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select name, email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as def where (abc.client_code != def.client_code or abc.email_id != def.email_id or abc.phone != def.phone) and (def.advisor1=\'{}\' or def.advisor2=\'{}\'))'.format(advisor,advisor) 
        #cursor.execute(sql)
        #newclients=cursor.fetchall()
    cursor.close()
    cursor=conn.cursor()
    


    for i in lists:
        
        cursor.execute('select * from dbo.followup where product=\'{}\' and next_call=\'{}\' and email_id=\'{}\' and  client_code=\'{}\' and  phone=\'{}\''.format(i[1],i[0],i[2],i[3],i[4]))
        answer.append(cursor.fetchall())
        print('yes')
    cursor.close()    
    conn.close()

    return(answer,newclients)

def returnfilter():###############code for getting sql query for filter 
    import datetime
    try:
        conn.close()
    except:
        pass

    def sql_statement(a,b):
        string=' and '
        stringa=a
        stringb=b

        if a=='All':
            stringa=None
        else:
            stringa='probability=\'{}\' '.format(a)
        if b=='All':
            stringb=None
        else:
            stringb='product=\'{}\' '.format(b)

        if a=='All' and b=='All':
            string=''
        else:
            lists=[]
            lists.append(stringa)
            lists.append(stringb)



            listfilter=[i for i in lists if i is not None]
            string='and '.join(listfilter)
        if string!= '':
            string=' and '+string

        return string
    #print("filter applied")
    global menu_adv,menu_stat,menu_,menu_prob,menu_mont,menu_yea,menu_dat,flagfilter
    import pyodbc
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
    cursor = conn.cursor()

    global advisor
    dictionary_for_month={'Jan':1,'Feb':2,"Mar":3,'Apr':4,"May":5,'Jun':6,"Jul":7,"Aug":8,'Sep':9,'Oct':10,"Nov":11,"Dec":12}
    a=dictionary_for_month[menu_mont.get()]
    date=datetime.datetime(int(menu_yea.get()),int(a),int(menu_dat.get()))+datetime.timedelta(1)
    year=date.year
    month=date.month
    date=date.day
    #print(year,month,date)



    x=sql_statement(menu_prob.get(),menu_.get()) #####to get the entry from filters and generating sql statement for remaining filters
    answer=[]
    if menu_stat.get()=='Open': #sepaarately for open and close and all but logic same  so status filter taken care here
        #print(menu_stat.get(),x)
        #######date filter can be used from below statement
        sql='select * from(select max(next_call) as next_call,product,email_id,client_code,phone from dbo.followup where ( advisor1=\'{}\' or advisor2=\'{}\') and status_=\'open\' group by email_id,product,client_code,phone ) as abc where next_call<\'{}\'  order by next_call DESC'.format(advisor,advisor,str(menu_yea.get())+str(a).zfill(2)+str(int(menu_dat.get())+1).zfill(2))
        cursor.execute(sql)
        lists=cursor.fetchall()
        #print(lists, "dekh be list")
        #print('date dekh bhai',str(menu_yea.get())+str(a).zfill(2)+str(int(menu_dat.get())+1).zfill(2))
        #sql='( select def.client_code,def.email_id,def.phone,def.advisor1,def.advisor2 from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select '' as email_id ,'' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select email_id, phone, '' as client_code,advisor1,advisor2 from dbo.other)) as def where abc.client_code != def.client_code and abc.email_id != def.email_id and abc.phone != def.phone and (advisor1=\'{}\' or advisor2=\'{}\')) '.format(advisor,advisor)

        answer=[]
        cursor=conn.cursor()
        sql='select * from((select \'\' as name, \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select name, email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as x where advisor1=? or advisor2=?' 
#sql='( select def.client_code,def.email_id,def.phone,def.advisor1,def.advisor2 from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as def where abc.client_code != def.client_code and abc.email_id != def.email_id and abc.phone != def.phone and (def.advisor1=\'neel\' or def.advisor2=\'neel\'))' 
        cursor.execute(sql,advisor,advisor)
        sql2=' select * from (select  email_id,phone,client_code,max(advisor1) as advisor1,max(advisor2) as advisor2 from dbo.followup     group by client_code,phone,email_id) as abc where advisor1=? or advisor2=?'
        newclients=(cursor.fetchall())
        cursor.execute(sql2,advisor,advisor)
        b1=cursor.fetchall()
        print(b1)
        for i in b1:
            for j in newclients:
                if (i[0]==j[1] and i[1]==j[2] and i[2]==j[3]):
                    print(j,i)
                    newclients.remove(j)
        #print("dekh bhai newclients",newclients)
        #sql='( select def.client_code,def.email_id,def.phone,def.advisor1,def.advisor2,def.name from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select \'\' as name, \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select name, email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as def where (abc.client_code != def.client_code or abc.email_id != def.email_id or abc.phone != def.phone) and (def.advisor1=\'{}\' or def.advisor2=\'{}\'))'.format(advisor,advisor) 
        #cursor.execute(sql)
        #newclients=cursor.fetchall()
        cursor.close()
        
        cursor=conn.cursor()


        try:
            for i in lists:

                cursor.execute('select * from dbo.followup where product=\'{}\' and next_call=\'{}\' and email_id=\'{}\' and  client_code=\'{}\' and  phone=\'{}\'{}'.format(i[1],i[0],i[2],i[3],i[4],x))
                answer.append(cursor.fetchall())
              #  print('yes')
            cursor.close()
            conn.close()
        except Exception as e:
            print(e,"c")
            try:
                conn.close()
            except:
                pass
            pass
        #print(answer,"answer open")
    if menu_stat.get()=='Closed':
        sql='select * from(select max(next_call) as next_call,product,email_id,client_code,phone from dbo.followup where ( advisor1=\'{}\' or advisor2=\'{}\') and status_=\'closed\' group by email_id,product,client_code,phone ) as abc where next_call<\'{}\'  order by next_call DESC'.format(advisor,advisor,str(menu_yea.get())+str(a).zfill(2)+str(int(menu_dat.get())+1).zfill(2))
        #print(sql,menu_stat.get(),x)
        cursor.execute(sql)
        lists=cursor.fetchall()
        #print(lists)
        cursor=conn.cursor()
        sql='select * from((select \'\' as name, \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select name, email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as x where advisor1=? or advisor2=?' 
#sql='( select def.client_code,def.email_id,def.phone,def.advisor1,def.advisor2 from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as def where abc.client_code != def.client_code and abc.email_id != def.email_id and abc.phone != def.phone and (def.advisor1=\'neel\' or def.advisor2=\'neel\'))' 
        cursor.execute(sql,advisor,advisor)
        sql2=' select * from (select  email_id,phone,client_code,max(advisor1) as advisor1,max(advisor2) as advisor2 from dbo.followup     group by client_code,phone,email_id) as abc where advisor1=? or advisor2=?'
        newclients=(cursor.fetchall())
        cursor.execute(sql2,advisor,advisor)
        b1=cursor.fetchall()
        for i in b1:
            for j in newclients:
                if (i[0]==j[1] and i[1]==j[2] and i[2]==j[3]):
                    print(j,i)
                    newclients.remove(j)

        #sql='( select def.client_code,def.email_id,def.phone,def.advisor1,def.advisor2,def.name from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select \'\' as name, \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select name, email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as def where (abc.client_code != def.client_code or abc.email_id != def.email_id or abc.phone != def.phone) and (def.advisor1=\'{}\' or def.advisor2=\'{}\'))'.format(advisor,advisor) 
        #cursor.execute(sql)
        #newclients=cursor.fetchall()
        cursor.close()
        


        cursor=conn.cursor()
        try:
            for i in lists:
            #print('select * from dbo.followup where product=\'{}\' and next_call=\'{}\' and email_id=\'{}\' and client_code=\'{}\' and phone=\'{}\'{}'.format(i[1],i[0],i[2],x))
                cursor.execute('select * from dbo.followup where product=\'{}\' and next_call=\'{}\' and email_id=\'{}\' and client_code=\'{}\' and phone=\'{}\'{}'.format(i[1],i[0],i[2],i[3],i[4],x))
                answer.append(cursor.fetchall())
            cursor.close()    
            conn.close()
        except :
            try:
                conn.close()
            except:
                pass
            pass
        #print(answer,"answer closed")
    if menu_stat.get()=='All':
        sql='select * from(select max(next_call) as next_call,product,email_id,client_code,phone from dbo.followup where ( advisor1=\'{}\' or advisor2=\'{}\')  group by email_id,product,client_code,phone ) as abc where next_call<\'{}\'  order by next_call DESC'.format(advisor,advisor,str(menu_yea.get())+str(a).zfill(2)+str(int(menu_dat.get())+1).zfill(2))
        cursor.execute(sql)
        lists=cursor.fetchall()
        cursor=conn.cursor()
        sql='select * from((select \'\' as name, \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select name, email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as x where advisor1=? or advisor2=?' 
#sql='( select def.client_code,def.email_id,def.phone,def.advisor1,def.advisor2 from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as def where abc.client_code != def.client_code and abc.email_id != def.email_id and abc.phone != def.phone and (def.advisor1=\'neel\' or def.advisor2=\'neel\'))' 
        cursor.execute(sql,advisor,advisor)
        sql2=' select * from (select  email_id,phone,client_code,max(advisor1) as advisor1,max(advisor2) as advisor2 from dbo.followup     group by client_code,phone,email_id) as abc where advisor1=? or advisor2=?'
        newclients=(cursor.fetchall())
        cursor.execute(sql2,advisor,advisor)
        b1=cursor.fetchall()
        for i in b1:
            for j in newclients:
                if (i[0]==j[1] and i[1]==j[2] and i[2]==j[3]):
                    print(j,i)
                    newclients.remove(j)

        #sql='( select def.client_code,def.email_id,def.phone,def.advisor1,def.advisor2,def.name from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select \'\' as name, \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select name, email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as def where (abc.client_code != def.client_code or abc.email_id != def.email_id or abc.phone != def.phone) and (def.advisor1=\'{}\' or def.advisor2=\'{}\'))'.format(advisor,advisor) 
        #cursor.execute(sql)
        #newclients=cursor.fetchall()
        cursor.close()
        cursor=conn.cursor()
        try:
            
            for i in lists:
            #print('select * from dbo.followup where product=\'{}\' and next_call=\'{}\' and email_id=\'{}\' and client_code=\'{}\' and phone=\'{}\'{}'.format(i[1],i[0],i[2],x))
                cursor.execute('select * from dbo.followup where product=\'{}\' and next_call=\'{}\' and email_id=\'{}\' and client_code=\'{}\' and phone=\'{}\'{}'.format(i[1],i[0],i[2],i[3],i[4],x))
                answer.append(cursor.fetchall())
            cursor.close()    
            conn.close()
        except:
            try:
                conn.close()
            except:
                pass
            pass
        #print(answer,"answer all")
    try:
        conn.close()
    except:
        pass
    return(answer,newclients)

flagfilter=1
def allproducts():
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='backend.cxzpw0u1iref.ap-south-1.rds.amazonaws.com,3955', database='sales',
                       user='sales', password='quant123')
    cursor=conn.cursor()
    #_code,def.email_id,def.phone,def.advisor1,def.advisor2 from(select email_id,phone,client_code from dbo.followup     group by client_code,phone,email_id) as abc, ((select \'\' as email_id ,\'\' as phone , client_code,advisor1,advisor2 from dbo.master_table) union (select email_id, phone, \'\' as client_code,advisor1,advisor2 from dbo.other)) as def where abc.client_code != def.client_code and abc.email_id != def.email_id and abc.phone != def.phone and (def.advisor1=\'neel\' or def.advisor2=\'neel\'))' 
    sql='select name from dbo.products'
    cursor.execute(sql)
    lists=[]
    for i in cursor:
        lists.append((i[0].lower()).capitalize())
    cursor.close()
    conn.close
    lists.append('All')
    return (lists)
Login()

