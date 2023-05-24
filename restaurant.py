#!/usr/bin/env python
# coding: utf-8

# In[76]:


class Table():
    def __init__(self, group):
        self.group = group
        self.bill = []
        
    def order(self, item_name:str, price:float, quantity:int):
        new_item = {
            'item': item_name,
            'price': price,
            'quantity': quantity
        }
        
        is_new_item = True
        for bill_item in self.bill:
            if bill_item['item'] == new_item['item']:
                bill_item['quantity'] += new_item['quantity']
                is_new_item = False
        
        if is_new_item == True:
            self.bill.append(new_item)
            
    def remove(self, item_name:str, price:float, quantity:int):
        new_item = {
            'item': item_name,
            'price': price,
            'quantity': quantity
        }
        
        for bill_item in self.bill:
            if bill_item['item'] == new_item['item']:
                bill_item['quantity'] -= new_item['quantity']
                if bill_item['quantity'] <= 0:
                    self.bill.remove(bill_item)
                    
    def get_subtotal(self):
        subtotal = 0
        for bill_item in self.bill:
            subtotal += bill_item['price'] * bill_item['quantity']
            
        return round(subtotal, 2)
    
    def get_total(self, service_charge_percent:float = 0.10):
        subtotal = self.get_subtotal()
        service_charge = round(subtotal * service_charge_percent, 2)
        total = round(subtotal + service_charge, 2)
        
        return {
            'Sub Total': f'£{subtotal}',
            'Service Charge': f'£{service_charge}',
            'Total': f'£{total}'
        }
    
    def split_bill(self):
        subtotal = self.get_subtotal()
        split_total = round(subtotal / self.group)
        
        return split_total


# In[77]:


table01 = Table(5)
table01.order("Risotto", 12.50, 2)
print(table01.bill)
table01.order("Burrito", 20.43, 3)
table01.remove("Burrito", 20.43, 2)
print(table01.bill)
print(table01.get_subtotal())
print(table01.get_total(0.15))
print(table01.split_bill())

