var blockingCounter = 0;
function loading(z,a){
	containerState = document.getElementById("button"+z+a).firstChild.className;
	if (containerState == "containerGPIO0"){
		document.getElementById("button"+z+a).innerHTML =
				"<button class='containerGPIO1'><div class='spinner dark'><i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i>	<i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i></div></button>";
	}
	if (containerState == "containerGPIO1"){
		document.getElementById("button"+z+a).innerHTML =
				"<button class='containerGPIO0'><div class='spinner light'><i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i>	<i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i></div></button>";
	}
	if (containerState == "containerTemp0"){
		document.getElementById("button"+z+a).innerHTML =
				"<button class='containerTemp1'><div class='spinner dark'><i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i>	<i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i></div></button>";
	}
	if (containerState == "containerTemp1"){
		document.getElementById("button"+z+a).innerHTML =
				"<button class='containerTemp0'><div class='spinner light'><i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i>	<i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i></div></button>";
	}
	if (containerState == "containerScript0"){
		document.getElementById("button"+z+a).innerHTML =
				"<button class='containerScript1'><div class='spinner dark'><i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i>	<i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i></div></button>";
	}
	if (containerState == "containerScript1"){
		document.getElementById("button"+z+a).innerHTML =
				"<button class='containerScript0'><div class='spinner light'><i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i>	<i></i>  <i></i>  <i></i>  <i></i>  <i></i>  <i></i></div></button>";
	}
}
function toggle(z,a) {
	blockingCounter++;
	loading(z,a);
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4){
			if (this.status == 200) {
				document.getElementById("button"+z+a).innerHTML =
				this.responseText;
			}
			blockingCounter--;
		}
	};
	xhttp.open("GET", "button/"+z+"/"+a+"/", true);
	xhttp.send();
}
function toggleGrid(e) {
	var xhttp = new XMLHttpRequest();
	xhttp.open("POST", "toggle/0/"+e+"/", true);
	xhttp.send();
}
function toggleLevel(e) {
	var xhttp = new XMLHttpRequest();
	xhttp.open("POST", "toggle/1/"+e+"/", true);
	xhttp.send();
}
function grid() {
	var gridDiv = document.getElementById("grid");
	if (gridDiv.style.display === "none") {
		return;
	} else {
		if (blockingCounter == 0){
			var xhttp = new XMLHttpRequest();
			xhttp.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200 && blockingCounter == 0) {
					document.getElementById("grid").innerHTML =
					this.responseText;
					}
				};
			xhttp.open("GET", "grid/", true);
			xhttp.send();
		}
	}
}
function level() {
	var lvlDiv = document.getElementById("level");
	if (lvlDiv.style.display === "none") {
		return;
	} else {
		if (blockingCounter == 0){
			var xhttp = new XMLHttpRequest();
			xhttp.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200 && blockingCounter == 0) {
					document.getElementById("level").innerHTML =
					this.responseText;
					}
				};
			xhttp.open("GET", "level/", true);
			xhttp.send();
		}
	}
}
function btnGrid() {
		var gridDiv = document.getElementById("grid");
		var gridBtn = document.getElementById("gridBTN");
		if (gridDiv.style.display === "none") {
			toggleGrid(1);
			gridDiv.style.display = "block";
			gridBtn.className = "btnON";
		} else {
			toggleGrid(0);
			gridDiv.style.display = "none";
			gridBtn.className = "btnOFF";
		}
	  }
function btnLevel() {
	var lvlDiv = document.getElementById("level");
	var lvlBtn = document.getElementById("lvlBTN");
	if (lvlDiv.style.display === "none") {
		toggleLevel(1);
		lvlDiv.style.display = "block";
		lvlBtn.className = "btnON";
	} else {
		toggleLevel(0);
		lvlDiv.style.display = "none";
		lvlBtn.className = "btnOFF";
	}
  }
window.setInterval(function(){
	grid()
	level()
}, {{ refresh_rate }});