import frappe

def execute(filters=None):
    columns = [
        {"label": "Product", "fieldname": "product", "fieldtype": "Link", "options": "Item", "width": 150},
        {"label": "Total Qty", "fieldname": "qty", "fieldtype": "Float", "width": 100},
        {"label": "Total Value", "fieldname": "value", "fieldtype": "Currency", "width": 120},
    ]

    receiving = frappe.db.sql("""
        SELECT product, SUM(qty) as total_qty, SUM(qty * price) as total_value
        FROM `tabProduct Receiving`
        GROUP BY product
    """, as_dict=True)

    delivery = frappe.db.sql("""
        SELECT product, SUM(qty) as total_qty
        FROM `tabDelivering Product`
        GROUP BY product
    """, as_dict=True)

    delivery_map = {d.product: d.total_qty for d in delivery}

    data = []
    for r in receiving:
        product = r.product
        qty_out = delivery_map.get(product, 0)
        net_qty = r.total_qty - qty_out

        data.append({
            "product": product,
            "qty": net_qty,
            "value": r.total_value
        })

    return columns, data
