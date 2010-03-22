$(function() {
    /* detect HTML5 & CSS3 support */
    if (!Modernizr.borderradius || !Modernizr.fontface) {
	
	var $dialog = $('<div></div>')
	    .html('Your browser does not support the awesome features of <a href="http://diveintohtml5.org/">HTML5</a> & CSS3. Feel free to continue, but you will likely have a degraded experience.  Consider upgrading to <a href="http://www.google.com/chrome">Chrome</a> or <a href="http://www.mozilla.com/firefox/">Firefox</a>.')
	    .dialog({
		title: 'Unsupported Browser',
		modal: true
	    });
    }
});