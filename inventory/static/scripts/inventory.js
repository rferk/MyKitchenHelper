$('#InventoryGroupBy').on('change', function(evt){
	evt.preventDefault();
	var groupby = this.value;
	$.ajax({
		url: index_url,
		type: "GET",
		data: {'groupby': groupby},
		success: function(data){
			$("#inventorylist").html(data)
			attachGroupDisplayEventHandler();
		}
	});

});



function toggleInventoryActionButtons(){
	if ($("#additem").css("display") == "none"){
		$('#additem').css("display", "list-item")
		$('#edititems').css("display", "list-item")	
	} else {
		$('#additem').css("display", "none")
		$('#edititems').css("display", "none")	
	};
};

function toggleAddItemActive(){
	if ($("#adddiv").css("display") == "none"){
		$("#adddiv").css("display", "block")
		$("#contenttitle").html("Add Inventory Item")
	} else {
		$("#adddiv").css("display", "none")
		$("#contenttitle").html("Inventory")
	};
};

// $('#additem').on('click', function(evt){
// 	toggleAddItemActive();
// 	toggleInventoryActionButtons();
// });


function updateAddDiv(data){
	$("#adddiv").html(data);
	attachCancelAddClickEventHandler();
	attachSubmitAddClickEventHandler();
	attachFormSubmitEventHandler();
}


function attachCancelAddClickEventHandler(){
	$('#canceladd').on('click', function(evt){
		toggleAddItemActive();
		toggleInventoryActionButtons();
		$.ajax({
			url: add_url,
			type: "GET",
			success: function(data){
				console.log(data);
				updateAddDiv(data);
			}
		});	
	});	
};

function attachSubmitAddClickEventHandler(){
	$('#submitadd').on('click', function(evt){
		$('#addform').submit();
	});
};

function attachFormSubmitEventHandler(){
	$('#addform').on('submit', function(event){
		event.preventDefault();
		console.log("form submitted");
		// $.ajax({
		// 	url: add_url,
		// 	type: "POST",
			
		// 	success: function(data){
		// 		console.log(data);
		// 		updateAddDiv(data);
		// 		console.log(data);
		// 	}
		// });	

	});
};

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
