$(document).ready(function () {
	$('#msgsTable').DataTable({
		data: {},
		columns: [
	        { data: 'time', width: "10%"},
	        { data: 'class', width: "10%" },
	        { data: 'channel', width: "20%" },
	        { data: 'message', width: "35%" },
	        { data: 'data', width: "25%" },
	    ],
		searching: false,
		paging: false,
		ordering: true,
		autoWidth: true,
		info: false
	});
});