<%!
	from datagraphvw import Role
%>\
<html>
<body>
<style>
span.graph_typename { color: rgb(0, 0, 120); }
span.graph_varname { font-weight: bold; }
span.graph_access { color: rgb(90, 90, 90); }
span.gdbconsole_output_ok { color: green; }
span.gdbconsole_output_error { color: red; }
table { border-spacing: 0pt; }
td {padding: 2pt; vertical-align:top;}
td.withborder { border-left: 1pt solid; border-left-color: rgba(200, 200, 200, 1)}
table.variabletop {border: 1pt solid rgba(200, 200, 200, 1); background: rgba(255, 255, 255, 1); position: absolute; left:0px; top:0px; }
table.variablechild {border: 1pt solid rgba(200, 200, 200, 1);}
div.removediv {position:absolute; left:2px; top:2px; z-index:1; opacity:0.2}
div.removediv:hover {opacity:1;}
tr.header {background-color: rgba(240, 240, 240, 1); border: 0;}
a {border-bottom:1px dotted;}
* {-webkit-user-select: none; user-select: none; font-family: sans-serif;}
</style>
<script type="text/javascript">
function contextmenu(obj, id) {
	document.getElementById(id).style.background = 'rgba(245, 245, 245, 1)';
	obj.openContextMenu();
	event.stopPropagation();
	document.getElementById(id).style.background = '';
}
</script>
<% assert(top) %>\
%	if varWrapper.getInScope() == True:
<table class="variabletop">
${varWrapper.render(Role.INCLUDE_HEADER)}
</table>
<div class="removediv">
<img onclick="${id}.remove()" src="qrc:icons/images/exit.png" width="16px" height="16px">
</div>
%	endif
</body>
</html>