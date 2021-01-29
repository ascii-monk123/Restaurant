from searchers.binarySearch import binarySearch
from items import Items as It
from customers import Customers as Cs
from sorters.quicksort import  quickSort as quick
import time
import os.path
from datetime import datetime
save_path=r"C:\Users\aahan\OneDrive\Desktop\Daa Assignments\Assignment1\bills"
class Restaurant:
    #initialize the seats in the restaurant
    def __init__(self) -> None:
        self.seats=20
        self.famousThreshold=2
        self.premiumThreshold=200
        self.seatArr=[]
    
    def bookSeat(self):
        print('****************\nAvailable seats are {}\n'.format(self.seats))
        noofSeats=int(input('How many seats would you like to book : '))
        try:
            phoneNumber=int(input('Enter the phone number : '))
        except:
            print('Error in ph number')
            return
        for phNo,seats in self.seatArr:
            if phNo==phoneNumber:
                print('Sorry you already have booked {} seats'.format(seats))
                return

        customers=Cs()
        customer=customers.findIfCustomerExists(phoneNumber)
        if customer:
            if(self.seats>0 and self.seats-noofSeats>=0):
                self.seats-=noofSeats
                self.seatArr.append((phoneNumber,noofSeats))
                print('Seat booked successfully')
            else:
                print('Seats full or there arent enough seats')
        else:
            print('Customer doesnt exist make an account first')
    #checkout of a seat
    def checkOut(self):
        print(self.seatArr)
        try:
            phoneNumber=int(input('Enter the phone number : '))
        except:
            print('Error in ph number')
            return
        if(self.seats==20):
            print('How can we have more checkouts than the seats ?? Something is fishy')
            return
        seatIndex=False
        curIndex=0
        for phNo,seats in self.seatArr:
            if phNo==phoneNumber:
                seatIndex=curIndex
                break
            if(curIndex==len(self.seatArr)-1):
                seatIndex=-1
            curIndex+=1
        if seatIndex>=0:
            self.seats+=self.seatArr[seatIndex][1]
            self.seatArr.pop(seatIndex)
            print('Checked Out')
        else:
            print('Sorry you havent reserved a seat')
    #static method to show all items
    @staticmethod
    def displayAllItems():
        It.displayAllItems()
    #static method to get most famous items
    @staticmethod
    def getFamousItems():
        items=It.getItems()['items']
        items=quick(items,'items')
        #now we will print the three most famous items in the list
        for item in items[-3:][::-1]:
            print('************************')
            print('Item name {}'.format(item['name']))
            print('Ordered : {} times'.format(item['times_ordered']))
            time.sleep(0.5)

    #find customer by phone number
    @staticmethod
    def findCustomers(phoneNumber):
        customers=Cs.getCustomers()['customer']
        customers=quick(customers,'customers')
        customerExists=binarySearch(customers,0,len(customers)-1,phoneNumber)
        if customerExists:
            print('Customer Exists')
        else:
            print('Customer doesnt exist')

    #method to place order for a customer
    @staticmethod
    def placeOrders():
        pattern="".center(30,"*")
        print(pattern)
        try:
            phNo=int(input('Enter customers phone number : '))
            customer=Cs()
            customerExists=customer.findIfCustomerExists(phNo)
            if customerExists:
                orderTotal=0
                print(pattern)
                takeOrders=True
                orderArray=[]
                while(takeOrders):
                    try:
                        orderId=int(input('Enter the id number of the item /999 to stop taking orders : '))
                        if orderId==999:
                            takeOrders=False
                            print(pattern)
                            print('Taking orders finished')
                            print(pattern)
                            customer.addOrder(orderArray,phNo,orderTotal)
                            print('Order Added')
                            time.sleep(0.5)
                            itemObj=It()
                            itemObj.updateItemStatus(orderArray)
                            time.sleep(0.5)
                            print('Items have been updated')
                            time.sleep(0.5)
                            continue
                        else:
                            itemObj=It()
                            index=itemObj.searchItems(orderId)
                            if isinstance(index,int):
                                try:
                                    qty=int(input('Enter the quantity you want to buy'))
                                    if qty<1:
                                        time.sleep(0.5)
                                        print('Quantity has to be a +ve integer')
                                        continue
                                    else:
                                        orderTotal+=itemObj.items[index]['price']*qty
                                        orderArray.append({'name':itemObj.items[index]['name'],'price':itemObj.items[index]['price'],'qty':qty})
                                        print(orderTotal)
                                        print(orderArray)
                                        
                                        time.sleep(0.5)


                                except:
                                    time.sleep(0.5)
                                    print('Quantity has to be valid')
                                    continue


                            else:
                                print('Item not present')
                    except:
                        print('Item id can only be a number')
                        continue
            else:
                print('Customer doesnt exist sorry enter valid customer phone Number')
                return
        except:
            print('Phone number has to be numeric')
            return
            
       #method to print a bill of a customer
    @staticmethod
    def printBill():
        pattern="".center(30,"*")
        print(pattern)
        try:
            phNo=int(input('Enter the customers phone number : '))
            customer=Cs()
            customerExists=customer.findIfCustomerExists(phNo)
            if customerExists:
                bill=customer.generateBill(customerExists)
                if bill:
                    now=datetime.now()
                    dt_string = now.strftime("%d/%m/%y %H:%M:%S")
                    completefilename=os.path.join(save_path,customerExists['name']+'.txt')
                    fpoint=open(completefilename,'a')
                    billString=''
                    billString+='\n\n{}\nDate:{}\n{}\n'.format(pattern,dt_string,pattern)
                    billString+="Name : {}\nOrder No : {}\nItems  : ----------------->\n".format(customerExists['name'],bill['order_no'])
                    for item in bill['items']:
                        billString+="Item Name : {}\nQuantity : {}\nPrice : {}\n".format(item['name'],item['qty'],item['price'])
                    billString+="***************************\n"
                    billString+="Order Total = ${}\n".format(bill['order_total'])
                    fpoint.write(billString)
                    fpoint.close()
                    print('Bill generated succesfully')
                else:
                    print('Sorry sir you dont have any orders')
            else:
                print('Customer of the given name doesnt exist')
        except Exception as e:
            print('Invalid phone number',e.message)
            return
        return

    #add a customer
    @staticmethod
    def addCustomer():
        pattern="".center(30,"*")
        print(pattern)
        name=input('Enter your name : ')
        try:
            phNo=int(input('Enter your mobile Number : '))
            if len(str(phNo))==10:
                customers=Cs()
                customers.addCustomer(**{'name':name,'mobile_number':phNo,"orderHistory":[]})
            else:
                print('Valid phone Number should be 10 digits in length\n')
        except Exception as e:
            print('Enter correct number value for the mobile number',e)
            print(pattern)
            return
        return

    #find all premium customers
    @staticmethod
    def findPremiumCustomer(threshold):
        try:
            phoneNumber=int(input('Enter the phone number:'))
            customers=Cs()
            customers.findPremium(phoneNumber,threshold)
        except:
            print('Please enter valid phone number for the customer')


