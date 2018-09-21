app.getEventLabels();
maxSparklineDatapoints = 300;
$(document).ready(function() {
	var i = 0;
	setInterval( function() {
		app.timelineNumMsgs.push(0);
		if (app.timelineNumMsgs.length > maxSparklineDatapoints) {
			app.timelineNumMsgs.shift();
		}
		app.drawSparkline();
		if (i >= 4) {
			app.timeframeMsgs = 0;
			i = 0;
		}
		i++;
	},1000);
	app.timelineNumMsgs.push(0);
	app.drawSparkline();
});