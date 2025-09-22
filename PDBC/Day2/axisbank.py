import mysql.connector

db_connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ramya2003$",
    database="SBIBankDatabase"
)
cursorObj=db_connection.cursor()

def check_bal(user_id):
    cursorObj.execute("select * from accounts where user_id=%s",(user_id,))
    mainbal=cursorObj.fetchone()
    return mainbal
def withdraw(userid):
    amt=int(input("enetr amount to draw------"))
    abc=check_bal(userid)
    acId,userId,accType,main_amt=abc
    print(main_amt,"main_bal")
    if amt>main_amt:
        print(f"you are trying to draw {amt} but you are having onlymain bal {main_amt}")
    elif amt<main_amt:
        cursorObj.execute("update accounts set acc_bal=acc_bal-%s where user_id = %s",(amt,userId))
        db_connection.commit()
        cursorObj.execute("select * from accounts where user_id=%s",(userid,))
        mainbal=cursorObj.fetchone()
        acId,userId,accType,main_amt=mainbal
        print(f"{amt} drawn succesfully------",f"main bal {main_amt}")
def signup():
    name=input("enetr yr name :-- ").strip().lower()
    password=input("eneytr yr pswd hetre :--  ").strip().lower()
    userRole=input("enter role here (customer / admin ):--- ").strip().lower()
    cursorObj.execute("insert into users (user_name,user_password,user_role) values (%s,%s,%s)",(name,password,userRole))
    db_connection.commit()
    cursorObj.execute("select * from users where user_name = %s",(name,))

    data=cursorObj.fetchone()
    print(data,"data")
    user_id,un,up,uRole=data
    print(user_id,"id")
    
    acc_type=input("enter ac/type ( savings / current ):--  ")
    cursorObj.execute("insert into accounts (user_id,acc_type,acc_bal) values (%s,%s,%s) ",(user_id,acc_type,5000))
    db_connection.commit() 

def login():
    name=input('enter name here:---')
    password=input('enter pwd here:---')
    role=input('enter role(customer/admin) here:---')
    cursorObj.execute("select * from users where user_name=%s",(name,))
    data=cursorObj.fetchone()
    user_id,userN,userP,userR=data
    print(userR,"role")
    if userR == "customer":
        print("------Customer menu-------")
        print("------1.withdraw-------")
        print("------2.Deposit-------")
        print("------3.Checkbal-------") 
        choose=input('enter one option here----')
        if choose == "1":
            withdraw(user_id)
        if choose == "3":
            print(check_bal(user_id))  
    if userR == "admin":
        print("-------Admin menu------") 


print("--- SBI bank project-----")
print("1.signup")
print("2.login")
print("3.exit")

choose=input("enetr yr option :--    "  )


if choose == "1":
    signup()
if choose == "2":
    login()