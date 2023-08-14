username='rohith'
password='python123'
c_name=input("Enter your username : ")
c_pass=str(input("Enter yoyr password : "))
if c_name==username and c_pass==password:
    print("success")
    print('''
    1.Depsite
    2.withdraw
    3.ministatement
    4.exit     
    '''
    )
    amount=60000
    option=int(input("select your option "))
    if option==1:
        dep=int(input("Enter the amount : "))
        amount+=dep
        print("Total amount:",amount)
    elif option==2:
        withdraw=int(input("Enter the amount:"))
        amount-=withdraw
        print("Total amount:",amount)  
    elif option==3:
        print("========ATM========")
        print("Username:",username)
        print("total amount:",amount)
        print("Thanks for visiting")
        print("====================")   
    else:
        print("please enter correct logins")       

              