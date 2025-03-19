// Copyright (c) 2025, adityayudhap21@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Something Document', {
	refresh:function(frm){
		if (frm.doc.docstatus == 1){
			frm.add_custom_button(__('Set To Open'),function(){
				set_status_to_open(frm)
			})
		}
	}
});

function set_status_to_open(frm){
	frappe.call({
		method:"interview_test_app.interview_test_app.doctype.something_document.something_document_api.set_status_to_open",
		args:{
			name:frm.doc.name
		},
		callback:function(r){
			frm.reload_doc()
		}
	})
}