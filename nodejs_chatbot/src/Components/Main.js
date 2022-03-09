import React, { Component } from 'react';
import './../main.css';
const main_message = "Welcome to Psych Doctor.";

class Main extends Component{
	render() {
		return (
			<div>
				<script src = "./chatbot/functions.js"></script>
				<center>
					<h3>{main_message}</h3>
					<form>
						<p id = "system_response"></p>
						<label for="user_response">Enter your response :</label>
						<input type="text" id="user_response" name="user_response"></input><br/>
						<button id = "accept_response">Submit</button>
					</form>
				</center>
			</div>
		)
	}

	
}

export default Main