from items import Items as It
from restaurant import Restaurant as Res
pattern="".center(30,"*")
options="1>Book a seat\n2>Place Order\n3>Search Famous Item\n4>Generate Bill\n5>Find Customer\n6>Find Premium Customer\n7>Add Customer\n8>Print all the items\n9>Exit the programme\n10>Checkout of a Customer"
print(pattern)
print('Welcome to the restaurant :)')
restaurant=Res()
run=True
while(run):
    print(pattern)
    print('What would you like to do ?')
    print(pattern)
    print(options)
    print(pattern)
    choice=int(input())
    if(choice==9):
        run=False
        continue
    elif(choice==1):
        restaurant.bookSeat()
    elif(choice==10):
        restaurant.checkOut()
    elif(choice==8):
        Res.displayAllItems()
    elif(choice==3):
        Res.getFamousItems()
    elif(choice==2):
        Res.placeOrders()
    elif(choice==4):
        Res.printBill()
    elif(choice==7):
        Res.addCustomer()
    elif(choice==6):
        Res.findPremiumCustomer(restaurant.premiumThreshold)

    elif(choice==5):
        print(pattern)
        try:
            phNo=int(input('Enter the phone number of the customer:'))
            Res.findCustomers(phNo)
        except:
            print('Invalid phone number. Please enter valid phone number the next time')
        
    else:
        print(choice)

