console.log('loading render file.');

const questions = JSON.parse(require('../json_files/questions.json')); // we basically loaded in our questions as a dictionary.
const responses =  JSON.parse(require('../json_files/responses.json')); 


window.onload = function () {
	var submit_button = document.getElementById('accept_response');
	var resp = document.getElementById("user_response");
	var system_response = document.getElementById("system_response");
	submit_button.onclick = function (resp) {
		// run this function, on click , and the input is recorded as resp.
	}




}

