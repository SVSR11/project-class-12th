import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="191005",database="grocery")
co=con.cursor()
co.execute("use grocery")
# FOR LOGIN, SINGUP, SETTING FUNCTION
def again():
    while True:
        print("\n━━━━━━━━━━━━━━━\n1.Login To Account 🤞")
        print("2.Create a New Account 🤝")
        print("3.Setting Menu ⚙\n4.Exit From Program 🚪\n━━━━━━━━━━━━━━━")
        choice=int(input("Enter your choice 👉 "))
        if choice==2:
            signup()
            break
            # For signup()
        elif choice==1:
            login()
            break
            # For login()
        elif choice==3:
            setting()
            break
            # For setting
        elif choice==4:
            print("\n                 Notification            ")
            print(" ------------------------------------------\n Are you Sure You Want to Exit from Grocery ")
            print(" Shopping Complex. \n")
            print("                     (Y) Yes ✔️   (N) No ❌\n --------------------------------------------\n")
            sur=input("Enter Your Choice 👉 ")
            while True:
                if sur in 'Nn':
                    again()
                    break
                elif sur in 'Yy':
                    print("\n            Your Request Accepted ✔️✔️✔️ ")
                    print(" Please Visit Again To Our Grocery Shopping Complex\n\n")
                    exit()
                    break
                else:
                    print("!!!..Invalid Choice Entered..!!!\nPlease Enter Valid Choice from the Following\n")
        else :
            print("!!!..Invalid Choice Entered..!!!")
        return

# LOGIN FUNCTION START FROM HERE
def login():
    global user_id1
    print("\nTo Login In Your Please Enter Your User_ID and Password")
    print("━"*31,"\n")
    user_id1=input("Enter your User_ID 👉 ")
    passwd=input("Enter Your password 👉 ")
    SELECT="select * from grocery1 where user_id="+"'"+user_id1+"'"+" and password="+"'"+passwd+"'"+";"
    global co
    co.execute(SELECT)
    b=co.fetchone()
    if b is None :
        print("\n❌❌ Invalid User_Id and Password ❌❌\n----------------------------------------")
        while True:
            print("Press (0) To Create new account\nPress (1) For Re-login in account\nPress (2) Return To Home Page\n-------------------------------------------")
            ch=int(input("Enter your choice 👉 "))
            if ch==0:
                signup()
                break
            if ch==1:
                login()
                break
            if ch==2:
                again()
                break
    else:
        co=con.cursor()
        c='y'
        while c.lower()=='y':
            print("\nAccount Logged successfully.. ✔️✔️✔️\n")
            print("_"*72,"\n~~~~~~~ WELCOME TO THE SNACKS SECTION OF GROCERY SHOPPING COMPLEX")
            print("━"*40,"\n")
            break
# SIGNUP FUNCTION START FROM HERE
def signup():
    global user_id1
    print("\nTo create Your account Please Enter User id and Password")
    print("━"*32,"\n")
    co=con.cursor()
    Name=input("Enter Your Full Name 👉 ")
    user_id1=input("Create your User_Id 👉 ")
    password=input("Create your Strong Passsword 👉 ")
    print("\nSelect Your Gender\nPress (M) For Male 🧔\nPress (F) For Female 👩\nPress (O) For Other ⚧\n")
    gender=input("Enter your gender 👉 ")
    phone_no=int(input("Enter your phone 👉 "))
    address=input("Enter Your Full Delivery Address 👉 ")
    print("")
    co=con.cursor()
    update="insert into grocery1 values('{}','{}','{}','{}',{},'{}')".format(user_id1,password,Name,gender,phone_no,address)
    co.execute(update)
    co.execute("select *from grocery1 where user_id="+"'"+user_id1+"'"+";")
    a=co.fetchall()
    con.commit()
    from tabulate import tabulate
    headers=["User_id","Password","Name","Gender","Phone_no","Address"]
    print(tabulate(a,headers=headers,tablefmt="psql"))
    print("\nAccount Created successfully.. ✔️✔️✔️\n")
    print("_"*72,"\n~~~~~~~ WELCOME TO THE SNACKS SECTION OF GROCERY SHOPPING COMPLEX ~~~~~~")
    print("━"*40,"\n")
    return
# SETTING FUNCTION START FROM HERE
def table():
    global user_id1
    co.execute("select *from grocery1 where user_id="+"'"+user_id1+"'"+";")
    a=co.fetchall()
    con.commit()
    from tabulate import tabulate
    headers=["User_id","Password","Name","Gender","Phone_no","Address"]
    print(tabulate(a,headers=headers,tablefmt="psql"))
    print("")
    setting()
    return
def userchange():
    global user_id1
    Name=input("Enter your User Name 👉 ")
    user_id1=input("Enter your New User-ID 👉 ")
    print("")
    query="update grocery1 set user_id='{}' where Name='{}';".format(user_id1,Name)
    co.execute(query)
    con.commit()
    print("User_ID Updated Successfully..✔️✔️✔️\n")
    table()
    return
def setting():
    global user_id1
    user_id1=input("Enter your  Account User-ID 👉 ")
    SELECT="select * from grocery1 where user_id="+"'"+user_id1+"'"+" ;"
    global co
    co.execute(SELECT)
    b=co.fetchone()
    if b is None :
        print("\n❌❌ Invalid User_ID Entered ❌❌\n","-"*40,"\n")
        while True:
            print("Press (1) To Change Your User_ID\nPress (0) To Re-Enter Your User_ID\n","-"*37,"\n")
            ch=int(input("Enter your choice 👉 "))
            if ch==1:
                userchange()
                break
            if ch==0:
                setting()
                break
    else:
        co=con.cursor()
        c='y'
        while c.lower()=='y':
            while True:
                print("\n━━━━━━━━━━━━━━━━━━━━━")
                print("Press (1) For Account Related Query 👥\nPress (2) Cart Related Query 🛒\nPress (3) Go To Home Page ")
                print("━"*21)
                se=int(input("Enter your Choice 👉 "))
                if se==1:
                    while True:
                        print("\npress (1) Fetch Account Details \nPress (2) To Change Address\nPress (3) To Change User Name\nPress (4) To Change Phone Number\nPress (5) To Change Password\nPress (6) For Exit\n")
                        lol=int(input("Enter Your Choice 👉 "))
                        if lol==2:
                            co=con.cursor()
                            address=input("Enter Your Address Details 👉 ")
                            co.execute("update grocery1 set address='{}' where user_id='{}';".format(address,user_id1))
                            con.commit()
                            print("\nAddress Updated successfully..✔️✔️✔️\n")
                            table()
                        elif lol==1:
                            table()
                        elif lol==3:
                            co=con.cursor()
                            Name=input("Enter your New Name 👉 ")
                            co.execute("update grocery1 set Name='{}' where user_id='{}';".format(Name,user_id1))
                            con.commit()
                            print("\nName Updated Successfully..✔️✔️✔\n")
                            table()
                        elif lol==4:
                            co=con.cursor()
                            phone_no=input("Enter your New Phone_no. 👉 ")
                            co.execute("update grocery1 set phone_no='{}' where  user_id='{}';".format(phone_no,user_id1))
                            con.commit()
                            print("\nPhone Number Updated Successfully..✔️✔️✔️\n")
                            table()
                        elif lol==5:
                            co=con.cursor()
                            password=int(input("Enter your New Password 👉 "))
                            co.execute("update grocery1 set password='{}' where  user_id='{}';".format(password,user_id1))
                            con.commit()
                            print("\nPassword Updated Successfully..✔️✔️✔️\n\n")
                            table()
                        elif lol==6:
                            print("\n\n")
                            break
                        else:
                            print("\n    !!!..Invalid Choice Entered..!!!")
                            print("Please Select Proper Choice From Following\n")
                elif se==2:
                    while True:
                        print("\n---------------------------------------\nPress (1) See Your Cart 🛒\nPress (2) See Order Details\nPress (3) Return To Home Page")
                        print("---------------------------------------")
                        ct=int(input("Enter Your Choice 👉 "))
                        if ct==1:
                            print("\nTo Check Your Cart Details Please Follow the cretaria")
                            print("-----------------------------------------------------\n")
                            co=con.cursor()
                            from tabulate import tabulate
                            a=input("Enter your date of Purchase in (YYYY-MM-DD) format 👉 ")
                            print("")
#in sql we write '2022-02-13',so to execute the same in Mysql we concatenate " ' " on both sides of t to do the same
                            co.execute("select *from grass2 where user_id="+"'"+user_id1+"'"+" and Purchase_time="+"'"+a+"'"+";")
                            x=co.fetchall()
                            headers=["user_id","Purchase_time","Product","Size","Quantity","Price"]
                            print(tabulate(x,headers=headers,tablefmt="psql"))
                            #again()
                        elif ct==2:
                            a=input("Enter your date of Order in (YYYY-MM-DD) format 👉 ")
                            co.execute("select Invoice_code from invoice where user_id="+"'"+user_id1+"'"+" and Purchase_date="+"'"+a+"'"+"; ")
                            now=co.fetchall()
                            co.execute("select * from grocery1 where user_id="+"'"+user_id1+"'"+"; ")
                            pho=co.fetchall()
                            co.execute("Select Product,Quantity,Price from bill where user_id="+"'"+user_id1+"'"+" and Purchase_date="+"'"+a+"'"+";")
                            it=co.fetchall()
                            print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
                            print("\n Invoice Id         ETA  ")
                            print('#',now[0][0],"        N/A\n_____________________________\n")
                            print("      ⭕━━━━━━━━⭕━━━━━━━━⭕━━━━━━━━━⭕   ")
                            print("    Placed         Confirmed         Process         Ready To Pickup ")
                            import datetime  # Importing Date time module
                            t=datetime.datetime.now()
                            print(" ",a,"\n ", t.strftime("%H:%M:%S"),"\n")
                            print("_”*28,”\n\n Customer Name        Phone_no")
                            print('#',pho[0][2],"         +91-",pho[0][4],"\n") #,pho[0][0]
                            from tabulate import tabulate
                            headers=["Product","Quantity","Price"]
                            print(tabulate(it,headers=headers,tablefmt="orgtbl"))
                            print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
                        elif ct==3:
                            again()
                            break
                        else:
                            print("\n    !!!..Invalid Choice Entered..!!!")
                            print("Please Select Proper Choice From Following\n")
                elif se==3:
                    again()
                    break
                else:
                    print("\n    !!!..Invalid Choice Entered..!!!")
                    print("Please Select Proper Choice From Following\n")
                return
            return # Exit From Setting

# MAIN PROGRAM START FROM HERE HELLO WELCOME
print("━"*41,"\n========= WELCOME TO GROCERY SHOPPING COMPLEX MANAGEMENT SYSTEM =========")
print("━"*41,"\n")
import datetime  # Importing Date time module
global t
t=datetime.datetime.now()
print("\nDate :",t.strftime("%Y-%m-%d"))
print("━"*10,"\n")
again()# LOGIN, SIGNUP, SETTIG FUNCTION CALLING
print("Please Select Snacks Product From Available Option Given Below\n","━"*33,"\n")
while True:
    print("\n--------------------\n(1) For Bistcuits 🍪")
    print("(2) For Drinks 🧴 ")
    print("(3) For Namkeen 📦")
    print("(4) For Exit 🚪\n--------------------")
    ch=int(input("Enter your Choice from given option 👉 "))
    # BISCUITE PROGRAM START FROM HERE
    if ch==1:
        print("\nChoose Your favourite biscuits from Different varieties of biscuits\n ")
        while True:
            print("S_NO    Biscuits_Brand\n----    --------------\n(1)     Britania\n(2)     Parle_Platina\n(3)     Oreo_Products\n(4)     For Exit\n")
            bis=int(input("Enter your favourite biscuit From given Options 👉 "))
            if bis==1:
                while True:
                    from tabulate import tabulate
                    co.execute("select *from Britania")
                    a=co.fetchall()
                    headers=["S_no","Packet_size","Price"]
                    print(tabulate(a,headers=headers,tablefmt="grid"))
                    size=int(input("Choose Your favourite Britania packet 👉 "))
                    if size==1:
                        co=con.cursor()
                        ca=int(input("\nEnter your Quantity 👉 "))
                        su=ca*10
                        ins="insert into grass2 values('{}','{}','Britania','Small_packet','{}','{}')".format(user_id1,t,ca,su)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif size==2:
                        print("\n Item you Select Is Currently Out Of Stock\n   😔😔 SORRY FOR INCONVENIENCE 😔😔\n")
                    elif size==3:
                        co=con.cursor()
                        print("")
                        i=int(input("Enter your Quantity 👉 "))
                        m=i*20
                        ins="insert into grass2 values('{}','{}','Britania','Large_packet','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    else:
                        print(" ❌ Enter the valid Choice From Britania ❌")
            elif bis==2:
                while True:
                    from tabulate import tabulate
                    co.execute("select *from Parle_Platina")
                    a=co.fetchall()
                    headers=["S_no","Packet_size","Price"]
                    print(tabulate(a,headers=headers,tablefmt="grid"))
                    size=int(input("Choose Your favourite Parle_Platina packet 👉 "))
                    if size==1:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*20
                        ins="insert into grass2 values('{}','{}','Parle_Platina','Small_packet','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif size==2:
                        print("\n Item you Select Is Currently Out Of Stock\n   😔😔 SORRY FOR INCONVENIENCE 😔😔\n")
                    elif size==3:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*20
                        ins="insert into grass2 values('{}','{}','Parle_Platina','Large_packet','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    else:
                        print(" ❌ Enter the valid Choice From Parle_Platina ❌")
            elif bis==3:
                while True:
                    from tabulate import tabulate
                    co.execute("select *from Oreo_Product")
                    a=co.fetchall()
                    headers=["S_no","Oreo_Product","Packet_size","Price"]
                    print(tabulate(a,headers=headers,tablefmt="psql"))
                    size=int(input("Choose Your favourite Oreo_Products 👉 "))
                    if size==2:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*8.50
                        ins="insert into grass2 values('{}','{}','Oreo_Biscuits','Medium_packet','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif size==1:
                        print("\n Item you Select Is Currently Out Of Stock\n    😔😔 SORRY FOR INCONVENIENCE 😔😔\n")
                    elif size==3:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*349
                        ins="insert into grass2 values('{}','{}','Oreo_Choco_cookies','Pack Of Six Piece','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif size==4:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*343
                        ins="insert into grass2 values('{}','{}','Oreo_White_cookies','Pack Of Six Piece','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    else:
                        print(" ❌ Enter the valide Oreo_Product ❌")
            elif bis==4:
                print(" 🛍.... Thanks for shopping Us ....🛍 \n")
                break
            else:
                print("❌ Enter the valid Choice ❌")
    # DRINK SECTION ENTRY START FROM HERE
    elif ch==2:
        print("\nChoose Your favourite Drinks from Different varieties of Drink ")
        print("---------------------------------------------------------------")
        while True:
            print("S_NO    Cold_Drink\n----    --------------\n(1)     CocaCola\n(2)     Maaza\n(3)     Mountain_Dew\n(4)     For Exit\n")
            drnk=int(input("Enter your favourite drink From given Option 👉 "))
            # COCA COLA PRGRAM FROM HERE
            if drnk==1:
                while True:
                    from tabulate import tabulate
                    co.execute("select *from CocaCola")
                    a=co.fetchall()
                    headers=["S_no","Bottle_Volume","Price"]
                    print(tabulate(a,headers=headers,tablefmt="grid"))
                    vol=int(input("Choose Your favourite Coca-Cola Bottle_Volume 👉 "))
                    if vol==1:
                        print("\n Item you Select Is Currently Out Of Stock\n    😔😔 SORRY FOR INCONVENIENCE 😔😔\n")
                    elif vol==2:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*46
                        ins="insert into grass2 values('{}','{}','CocaCola','750mL','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print("\n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif vol==3:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*60
                        ins="insert into grass2 values('{}','{}','CocaCola','1L','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif vol==4:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*95
                        ins="insert into grass2 values('{}','{}','CocaCola','2L','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    else:
                        print(" ❌ Enter the valid Choice From CocaCola ❌")
            # MAAZA PROGRAM HERE
            elif drnk==2:
                while True:
                    from tabulate import tabulate
                    co.execute("select *from Maaza")
                    a=co.fetchall()
                    headers=["S_no","Bottle_Volume","Price"]
                    print(tabulate(a,headers=headers,tablefmt="grid"))
                    vol=int(input("Choose Your favourite Maaza Bottle_Volume 👉 "))
                    if vol==1:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*34
                        ins="insert into grass2 values('{}','{}','Maaza','500mL','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif vol==2:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*45
                        ins="insert into grass2 values('{}','{}','Maaza','750mL','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif vol==3:
                        print("\n Item you Select Is Currently Out Of Stock\n    😔😔 SORRY FOR INCONVENIENCE 😔😔\n")
                    elif vol==4:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*90
                        ins="insert into grass2 values('{}','{}','Maaza','2L','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    else:
                        print(" ❌ Enter the valid Choice From Maaza ❌")
            #MOUNTAIN DEW PROGRAM
            elif drnk==3:
                while True:
                    from tabulate import tabulate
                    co.execute("select *from Mountain_Dew ")
                    a=co.fetchall()
                    headers=["S_no","Bottle_Volume","Price"]
                    print(tabulate(a,headers=headers,tablefmt="grid"))
                    vol=int(input("Choose Your favourite Mountain_Dew Bottle_Volume 👉 "))
                    if vol==1:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*32
                        ins="insert into grass2 values('{}','{}','Mountain_Dew','500mL','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                    elif vol==2:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*39
                        ins="insert into grass2 values('{}','{}','Mountain_Dew','750mL','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                    elif vol==3:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*62
                        ins="insert into grass2 values('{}','{}','Mountain_Dew','1L','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                    elif vol==4:
                        print("\n Item you Select Is Currently Out Of Stock\n    😔😔 SORRY FOR INCONVENIENCE 😔😔\n")
                    else:
                        print(" ❌ Enter the valid Choice From Mountain_Dew ❌")
            elif drnk==4:
                print(" 🛍.... Thanks for shopping Us ....🛍 \n")
                break
            else:
                print(" ❌ Enter the valid Choice❌")
    #SALTY SNACKS PRODUCT SECTION START FROM HERE
    elif ch==3:
        print("\nChoose Your favourite Salty snacks from available Stocks ")
        while True:
            print("S_NO    Namkeens\n----    --------------\n(1)     Navrattana\n(2)     Aloo_Bhujiya\n(3)     Lays\n(4)     For Exit\n")
            Nam=int(input("Enter your favourite Salty Snacks From Option 👉 "))
            if Nam==1:
                while True:
                    from tabulate import tabulate
                    co.execute("select *from Navrattana")
                    a=co.fetchall()
                    headers=["S_no","Pack_Size","Price"]
                    print(tabulate(a,headers=headers,tablefmt="grid"))
                    wgt=int(input("Choose Your favourite Navrattana Pack_Size 👉 "))
                    if wgt==1:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*20
                        ins="insert into grass2 values('{}','{}','Navrattana','Small_Pack','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        break
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                    elif wgt==2:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*37
                        ins="insert into grass2 values('{}','{}','Navrattana','Party_Pack','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif wgt==3:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*64
                        ins="insert into grass2 values('{}','{}','Navrattana','Travalling_Pack','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif wgt==4:
                        print("\n Item you Select Is Currently Out Of Stock\n    😔😔 SORRY FOR INCONVENIENCE 😔😔\n")
                    else:
                        print("❌ Enter the valide Choice From Navrattana ❌")
            # ALOO BHIJIYA PROGRAM HERE
            elif Nam==2:
                while True:
                    from tabulate import tabulate
                    co.execute("select *from Aloo_Bhujiya")
                    a=co.fetchall()
                    headers=["S_no","Pack_Size","Price"]
                    print(tabulate(a,headers=headers,tablefmt="psql"))
                    wgt=int(input("Choose Your favourite Bhujiya Pack_Size 👉 "))
                    if wgt==2:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*28
                        ins="insert into grass2 values('{}','{}','Aloo_Bhujiya','Party_Pack','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif wgt==1:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*13
                        ins="insert into grass2 values('{}','{}','Aloo_Bhujiya','Small_Packet','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif wgt==3:
                        print("\n Item you Select Is Currently Out Of Stock\n    😔😔 SORRY FOR INCONVENIENCE 😔😔\n")
                    elif wgt==4:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*95
                        ins="insert into grass2 values('{}','{}','Aloo_Bhujiya','Family_Pack','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    else:
                        print(" ❌ Enter the valid Choice From Aloo_Bhujiya ❌")

            # LAYS PROGRAM FROM HERE
            elif Nam==3:
                while True:
                    from tabulate import tabulate
                    co.execute("select *from Lays")
                    a=co.fetchall()
                    headers=["S_no","Pack_Size","Price"]
                    print(tabulate(a,headers=headers,tablefmt="grid"))
                    wgt=int(input("Choose Your favourite Lays Pack_Size 👉 "))
                    if wgt==1:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*15
                        ins="insert into grass2 values('{}','{}','Lays','Small_pack','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif wgt==2:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*29
                        ins="insert into grass2 values('{}','{}','Lays','Party_pack','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    elif wgt==3:
                        print("\n Item you Select Is Currently Out Of Stock\n    😔😔 SORRY FOR INCONVENIENCE 😔😔\n")
                    elif wgt==4:
                        co=con.cursor()
                        i=int(input("\nEnter your Quantity 👉 "))
                        m=i*76
                        ins="insert into grass2 values('{}','{}','Lays','Family_Pack','{}','{}')".format(user_id1,t,i,m)
                        co.execute(ins)
                        con.commit()
                        print(" \n🛒 Your Product is Added to Cart 🛒 \n")
                        break
                    else:
                        print(" ❌ Enter the valid Choice From Lays ❌")
            elif Nam==4:
                print(" 🛍... Thanks for shopping With Us ....🛍 \n")
                break
            else:
               print(" ❌ Enter the valid Choice ❌")
    elif ch==4:
        break
    else:
        print(" ❌ Enter the valid Choice ❌")

# CART CHECKING PROGRAM START FROM HERE
while True:
    print("\nDo you Want to see your Cart (Y/N) ?\n------------------------------------")
    se=input("Enter your choice 👉 ")
    if se in 'Nn':
        break
    elif se in 'Yy':
        co=con.cursor()
        from tabulate import tabulate
        a=input("Enter your date of Purchase in (YYYY-MM-DD) format 👉 ")
        #in sql we write '2022-02-13',so to execute the same in Mysql we concatenate " ' " on both sides of t to do the same
        co.execute("select *from grass2 where user_id="+"'"+user_id1+"'"+" and Purchase_time="+"'"+a+"'"+";")
        x=co.fetchall()
        headers=["user_id","Purchase_time","Product","Size","Quantity","Price"]
        print(tabulate(x,headers=headers,tablefmt="psql"))
        print("")
        break
    else:
        print("!!!..Please Enter the Valide Choice..!!!")

# RATE FUNCTION DEFINNG FROM HERE
def rate():
    co.execute("use grocery")
    global user_id1
    print("\nRate your experience with Grocery Shopping Complex \n")
    print("  🙁     😐     🙂     😊      😃\n Bad    Okay   Good   Great  Amazing\n")
    rate=int(input("Rate your Experiences 👉 "))
    if rate<=2:
        write_reviews=input("\nWrite your Grievances :")
        print("Your problem will be rectifed as soon as possible ")
        print("   😊😊... Thanks For Rate and Comment...😊😊     \n")
        print("Have A Good Day....Best Wishes From Grocery Shopping Complex ")
        INSERT="insert into visual values('{}',{},'{}')".format(user_id1,rate,write_reviews)
        co.execute(INSERT)
        con.commit()
    else:
        comment= input("\n💬💬 Comment your experience about Grocery Shopping Complex  👉 ")
        INSERT="insert into visual values('{}',{},'{}')".format(user_id1,rate,comment)
        co.execute(INSERT)
        con.commit()
        print("       😊😊... Thanks For Rate and Comment...😊😊      \n")
        print("-- Have A Good Day....Best Wishes From Grocery Shopping Complex --\n")
def bill():
    import datetime
    global a
    print("\n\n\n")
    print("━"*11,"GROCERY SHOPPING COMPLEX","━"*12,"\n")
    import random
    now=random.randint(10000000,999999999)
    print(" Invoice ID #",now)
    co=con.cursor()
    co.execute("insert into invoice values('{}','{}','{}')".format(user_id1,t,now))
    con.commit()
    print("")
    print(" From :\n E-Grocery Shopping Complex\n")
    print(" Date And Time :\n",a.strftime("%Y-%b-%d  %H:%M:%S\n"))
    print(" Ship To :\n",n[0][0],"\n\n","Address :\n",aid[0][0])
    print(" India \n")
    print(" Item Count :                               ",q[0][0])
    print("")
    from tabulate import tabulate
    co.execute("select Product,Size,Quantity,Price from grass2 where user_id="+"'"+user_id1+"'"+" and Purchase_time="+"'"+t+"'"+";")
    it=co.fetchall()
    headers=["Product","Size","Quantity","Price"]
    print(tabulate(it,headers=headers,tablefmt="orgtbl"))
    con.commit()
    print(" \n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    gstper=2.0
    print(" Applied GST Charge :                        2%")
    am=d[0][0]
    gst=am*2.0/100
    amount=am+gst
    print(" Sub Total   :                            ","₹",d[0][0])
    print(" GST Charges  :                           ","₹",gst)
    print(" Grand Total :                            ","₹",amount)
    print(" \n Payment Through :                 ",payment)
    print("  \n                   ..Thanks for shopping with us..         \n         💕 Whoever Is Happy Will Make Others Happy Too   ")
    print('━'*38,'\n\n')
    a= datetime.datetime.now()
    c=a.strftime("%d-%b-%Y  %H:%M:%S")
    b=a.strftime("%d-%b-%Y")
    print("YOUR ORDER SUCCESFULLY ORDERED AT ",c," ✔✔\n\n")
    co=con.cursor()
    co.execute("insert into bill(user_id,Purchase_date,Product,size,Quantity,Price) select  user_id,Purchase_time,Product,Size,Quantity,price from grass2 where user_id="+"'"+user_id1+"'"+" and purchase_time="+"'"+t+"'"+";")
    con.commit()
    print("\nDo You want To Rate Us (Y/N)\n----------------------------")
    ch=input("Enter your choice 👉 ")
    if ch in 'yY':
        rate()
    else:
        print("🙏🙏 Thanks You For Visit Us....Best Wishes From Grocery Shopping Complex 🙏🙏\n\n")
        exit()
#BILLING PROGRAM STARING FROM HERE
while True:
    print("\n=====================================")
    print("Press (1) If Shopping is done ✔✔✔")
    print("Press (2) To Exit From Grocery 🚪🚪🚪")
    print("=====================================\n")
    choice=int(input("Enter your choice from above option 👉 "))
    if choice==1:
        print("\n---------------------------------")
        print("Press (1) For Order and Billing 🧾🧾")
        print("Press (2) For rating and Comment 💬💬")
        print("---------------------------------\n")
        ch=int(input("Enter your choice 👉 "))
        if ch==1:
            co=con.cursor()
            t=input("\nEnter your date of Purchase in (YYYY-MM-DD) format 👉 ")
            co.execute("select Name from grocery1 where user_id="+"'"+user_id1+"'"+";")
            n=co.fetchall()
            co.execute("select address from grocery1 where user_id="+"'"+user_id1+"'"+";")
            aid=co.fetchall()
            co.execute("select sum(price) from grass2 where user_id="+"'"+user_id1+"'"+" and Purchase_time="+"'"+t+"'"+";")
            d=co.fetchall()
            co.execute("select sum(Quantity) from grass2 where user_id="+"'"+user_id1+"'"+" and Purchase_time="+"'"+t+"'"+";")
            q=co.fetchall()
            con.commit()
            import datetime
            a= datetime.datetime.now()
            print()
            print("\n---------------------------------\nNo. Of Item Purchased :",q[0][0])
            print("Total Price Of Item  : ₹",d[0][0],"\n---------------------------------\n")
            print()
            while True:
                print("Do You Want To Continue Your Order (y/n)\n”,”-"*40)
                ch=input("Enter Your Choice 👉 ")
                if ch in 'Yy':
                    while True:
                        global payment
                        print("\n-----------------\n1.Credit Card\n2.Debit Card\n3.Pay On Delivery\n-----------------\n")
                        pay=int(input("Select Your Payment Method 👉 "))
                        if pay==1:
                            co=con.cursor()
                            payment='Credit Card'
                            co.execute("insert into pay values('{}','{}','{}')".format(user_id1,t,payment))
                            con.commit()
                            bill()
                            break
                        elif pay==2:
                            co=con.cursor()
                            payment='Debit Card'
                            co.execute("insert into pay values('{}','{}','{}')".format(user_id1,t,payment))
                            con.commit()
                            bill()
                            break
                        elif pay==3:
                            co=con.cursor()
                            payment='Pay On Delivery'
                            co.execute("insert into pay    values('{}','{}','{}')".format(user_id1,t,payment))
                            con.commit()
                            bill()
                            break
                        else:
                            print("!! Select Proper Method !!")
                    break
                elif ch in 'Nn':
                    print("\nDo You want To Rate Us (Y/N)\n----------------------------")
                    ch=input("Enter your choice 👉 ")
                    if ch in 'yY':
                        rate()
                    else:
                        print("🙏🙏 Thanks You For Visit Us....Best Wishes From Grocery Shopping Complex 🙏🙏\n\n")
                        exit()
                    break
                else:
                    print("!!! Select Apropiate Choice !!!")
            break
        elif ch==2:
            rate()
            break
        else:
            print(" ❌ Invalid Choice ❌")
    if choice==2:
        print("🙏🙏 Thanks You For Visit Us....Best Wishes From Grocery Shopping Complex 🙏🙏\n\n")
        exit()
