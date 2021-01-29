import json
import time


class Customers:
    def __init__(self):
        customerHandle=open('customers.json')
        customers=json.load(customerHandle)['customer']
        customerHandle.close()
        self.customers=customers
        
    @staticmethod
    def getCustomers():
        customerHandle=open('customers.json')
        customers=json.load(customerHandle)
        customerHandle.close()
        return customers
    def findIfCustomerExists(self,phoneNumber):
        for customer in self.customers:
            if customer['mobile_number']==phoneNumber:
                return customer
        return False
    def addOrder(self,orderArray,mobileNumber,orderTotal):
        for customer in self.customers:
            if customer['mobile_number']==mobileNumber:
                orderFormat={"order_no":len(customer['orderHistory'])+1,"items":[item for item in orderArray],"order_total":orderTotal}
                customer['orderHistory'].append(orderFormat)
        newCustomers={'customer':self.customers}
        with open('customers.json','w',encoding='utf-8') as custFile:
            json.dump(newCustomers,custFile,ensure_ascii=False, indent=4)
        return
    def generateBill(self,customer):
        finalOrder=customer['orderHistory'][len(customer['orderHistory'])-1]
        if finalOrder:
            return finalOrder
        else:
            return False
    #add customer method
    def addCustomer(self,**personData):
        self.customers.append(personData)
        newCustomers={'customer':self.customers}
        with open('customers.json','w') as customFile:
            json.dump(newCustomers,customFile,ensure_ascii=False, indent=4)
        print('Successfully added customer .\n')
        print('******************')
        return
    #find all premuim customers
    def findPremium(self,phoneNumber,threshold):
        customer=self.findIfCustomerExists(phoneNumber)
        if customer:
            sum=0
            for order in customer['orderHistory']:
                sum+=order['order_total']
            if sum>threshold:
                time.sleep(0.5)
                print('Customer is premium\n')
            else:
                time.sleep(0.5)
                print('Customer is not premium')
                
        else:
            print('Customer doesnt exist cannot find whether premimum or not')




    