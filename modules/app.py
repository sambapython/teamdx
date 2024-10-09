"""
print("this is app start")
import sales
import sys
import os
print(os.__file__)
sys.path.append("C:\\Users\\h")
print(sys.path)
import os
import math
import purchase
purchase.create_supplier()
sales.add_customer()
sales.add_sales_order()
print(sales.a)
print("this is app end")
"""
"""
import sys
print(sys.path)
import erp
"""
#import erp
#erp.stock.create_product()
from erp import stock, accounts
stock.create_product()
accounts.create_account()

#package.ini 