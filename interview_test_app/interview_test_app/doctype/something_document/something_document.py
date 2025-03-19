# Copyright (c) 2025, adityayudhap21@gmail.com and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from frappe import _

class SomethingDocument(Document):
	def on_submit(self):
			previous_doc = frappe.get_all(
				self.doctype,
				filters={
					"docstatus": 1,
					"name": ["!=", self.name]
				},
				fields=["name", "amount"],
				order_by="creation desc",
				limit=1
			)

			previous_amount = previous_doc[0].amount if previous_doc else 0
			total_amount = previous_amount + self.amount
			self.amount = total_amount
			frappe.db.set_value("Something Document",self.name,"amount",total_amount)
	
