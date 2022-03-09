import React, { Component } from 'react';
import './../main.css';
import './chatbot/functions'
import { useState } from "react";
const main_message = "Welcome to Psych Doctor.";

main_function = function (e) {
	e.preventDefault(); // prevents the page from being reloaded.
	var submit_button = document.getElementById('accept_response');
	var resp = document.getElementById("user_response");
	var system_response = document.getElementById("system_response");
	submit_button.onclick = function (resp) {
		// run this function, on click , and the input is recorded as resp.
		system_response.innerHTML = "Button clicked.";
	}

}




class Main extends Component{
const { userResp, setUserResp } = useState('');	
	render() {
		return (
			<div>
				<script src = "./chatbot/functions.js"></script>
				<center>
					<h3>{main_message}</h3>
					<form onSubmit={main_function}>
						<p id = "system_response"></p>
						<label for="user_response">Enter your response :</label>
						<input type="text" value="user_response" onChange={(e)=>setUserResp(this.target.value)} name="user_response"></input><br/>
						<button id = "accept_response" type = "submit" >Submit</button>
					</form>
				</center>
			</div>
		)
	}

	
}

export default Main