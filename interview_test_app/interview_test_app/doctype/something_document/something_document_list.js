frappe.listview_settings['Something Document'] = {
    onload: function(listview) {
        listview.page.add_menu_item('Clear Open Documents', () => {
            frappe.call({
				method:"interview_test_app.interview_test_app.doctype.something_document.something_document_api.clear_open_documents",
				callback:function(r){
					listview.refresh(); 
				}
			})
        });
    }
};
