//Prototype javascript file for the store page - Tim

//Determines which button is highlighted
var selectedbtn;

//Change button formatting and determines which table is visible
function chkbtn(btn, tab) {	
	//Get all the category buttons in an array
	var catbuttons = document.getElementsByClassName('catbutton');
	
	//Set which button was selected
	selectedbtn = btn;
	
	//Format the buttons based on if it was selected or not
	for(var i = 0; i < catbuttons.length; i++) {
		if(catbuttons[i].id === selectedbtn.id) {
			catbuttons[i].style.background = '#ffc';
			catbuttons[i].style.color = 'black';
		}
		else {
			catbuttons[i].style.background = '#6d1d1c';
			catbuttons[i].style.color = 'white';
		}
	}
	
	//Get all possible category tables
	var cattables = document.getElementsByClassName('cattable');
	
	//Set which one should be displayed
	var selectedtab = tab;
	
	//Make the selected one visible, make all others not visible
	for(var i = 0; i < cattables.length; i++) {
		if(cattables[i].id === selectedtab.id) {
			cattables[i].style.display = 'table';
		}
		else {
			cattables[i].style.display = 'none';
		}
	}
}

//Determines what happens if the mouse if over the button
function overbtn(btn) {
	btn.style.background = '#ffc';
	btn.style.color = 'black';
}

//Determines what happens when the mouse leaves the button
function outbtn(btn) {
	if(btn !== selectedbtn) {
		btn.style.background = '#6d1d1c';
		btn.style.color = 'white';
	}
}


