$('#InventoryGroupBy').on('change', function(evt){
	evt.preventDefault();
	var groupby = this.value;
	console.log(index_url);
	$.ajax({
		url: index_url,
		type: "GET",
		data: {'groupby': groupby},
		success: function(data){
			console.log(data);
			$("#inventorylist").html(data)
			attachGroupDisplayEventHandler();
		}
	});

});

function attachGroupDisplayEventHandler(){
	$('.groupdisplay').on("click", function(evt){
		$(this).toggleClass("fa-toggle-up");	
		$(this).toggleClass("fa-toggle-down");	
		var group = $(this).parent().parent().parent()
		var datarows = $(group).children('.datarow')	
		$(datarows).toggleClass("rowshow");	
		$(datarows).toggleClass("rowhide");	
	});	
};
