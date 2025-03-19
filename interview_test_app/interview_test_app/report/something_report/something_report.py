# Copyright (c) 2025, adityayudhap21@gmail.com and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 150},
        {"label": "Total Count", "fieldname": "total_count", "fieldtype": "Int", "width": 120},
        {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency", "width": 150}
    ]
    data = []

    for status in ["Open", "Closed"]:
        docs = frappe.get_all("Something Document",
                              filters={"workflow_state": status},
                              fields=["amount"])
        total_count = len(docs)
        total_amount = sum([d.amount for d in docs])

        data.append({
            "status": status,
            "total_count": total_count,
            "total_amount": total_amount
        })

    return columns, data
