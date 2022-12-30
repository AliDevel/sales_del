import frappe
import json
import csv
from frappe import _

class SalesOrderDelete:
    
    def delete_order(self):
        with open("/home/frappe/frappe-bench/apps/sales_order/sales_order/delete_sales_order/sales.csv", 'r') as file:
            sales_order = csv.reader(file)           
            for id in sales_order:
                frappe.msgprint(id[0])
                sal= frappe.get_doc('Sales Order',id[0])
                sal.cancel()
                frappe.msgprint(sal.status)
                frappe.db.commit()
        
       
                   
       
           
@frappe.whitelist()
def delete():
    SalesOrderDelete().delete_order()