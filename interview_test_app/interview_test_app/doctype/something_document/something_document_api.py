import frappe

@frappe.whitelist()
def clear_open_documents():
    deleted_count = 0
    docs = frappe.get_all("Something Document", filters={"workflow_state":"Open", "docstatus": 0})
    for doc in docs:
        try:
            frappe.delete_doc("Something Document", doc.name, force=1)
            deleted_count += 1
        except Exception as e:
            frappe.log_error(f"Failed to delete {doc.name}: {str(e)}")

    return f"{deleted_count} Open documents deleted."

@frappe.whitelist()
def set_status_to_open(name):
    frappe.db.set_value("Something Document",name,"workflow_state","Open")
    frappe.db.set_value("Something Document",name,"docstatus",0)
    frappe.db.set_value("Something Document",name,"document_status","Open")
    frappe.db.commit()