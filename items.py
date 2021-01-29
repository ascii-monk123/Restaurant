import json
import time
from searchers.binarySearch import binarySearchItems as bin
class Items:
    def __init__(self) -> None:
        itemHandle=open('items.json')
        items=json.load(itemHandle)['items']
        self.items=items
        itemHandle.close()
    @classmethod
    def displayAllItems(cls):
        items=cls.getItems()
        for item in items["items"]:
            print('**************')
            print('Name : {}'.format(item['name']))
            print('Price : {}'.format(item['price']))
            print('**************')
            time.sleep(0.5)
    @classmethod
    def getItems(cls):
        itemHandle=open('items.json')
        items=json.load(itemHandle)
        itemHandle.close()
        return items
    def searchItems(self,id):
        itemIndex=bin(self.items,0,len(self.items)-1,id)
        if isinstance(itemIndex,int):
            return itemIndex
        else:
            return 'Item Not Present'
    def updateItemStatus(self,orderArray):
        for order in orderArray:
            for item in self.items:
                if item['name']==order['name']:
                    item['times_ordered']+=order['qty']
                    break
        newItems={'items':self.items}
        with open('items.json','w',encoding='utf-8') as itemFile:
            json.dump(newItems,itemFile,ensure_ascii=False, indent=4)
        return

