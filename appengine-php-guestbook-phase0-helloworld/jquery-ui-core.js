$(document).ready(function() {

	$(document).click(function() {
		$('#target').effect('highlight');
	});
	
	/*$('#target').draggable({axis:'x'});*/
	/*$('#target').draggable({cursor:'move'});*/
	/*$('#target').draggable({cursor:'crosshair'});*/
	/*$('#target').draggable({revert:true});*/
	$('#target').draggable({grid:[200,200]});

	$("#accordion, #koon").accordion({active: false, collapsible: true});
});