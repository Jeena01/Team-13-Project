## Import the libraries
import json;

## Load the data
responses = 0
questions = 0
score = 0;			## initially ever user starts with a mental score of zero.
## at the end a higher score means, a user most likely has depression.
total_questions = 3	## How many questions from the json file, we want to ask.

## These 2 files below have the questions stored as a dictionary.
with open('./responses.json') as json_file:
	responses = json.load(json_file)
with open('./questions.json') as json_file:
	questions = json.load(json_file)


"""This function below is our main , function which makes use of the other helper functions to keep the app running. 
It does the following tasks first :
1. Collect user info 
2. Take the user through a questionare to see if he can possibly have depression.
"""
def returnResp(inputresp):
	recordPatientInfo()
	for x in responses:
		if x in inputresp: ## if response key  in string 
			resp =  responses[x];
			if (x == "suffering"):
				score = recordMentalHist()
				print("Do you have any other question regarding your diagnostics ?(yes/no)")
				resp = input()
				if("no" in resp):
					return f"Your Mental Score is {score}."
				else:
					print(f"Your Mental Score is {score}.")
					try:
						answerRestQuestions();
					except KeyError:
						print("Unfortunately i do not have the response for that. Anything Else ?")
						answerRestQuestions();
					finally:
						 print(f"Your Mental Score is {score}.")
			else:
				return resp;


def recordPatientInfo():
	## This method records the patient information, and can be further modified to collect any other information that we may be interested in collecting in the future.
	print("Welcome to a virtual psychatrist.\nWhat is your name ?");
	name = input()
	print(f"Welcome {name}, what is your age ?");
	age = input()
	print("What can i help you with");

	info = [name, age]

	return info
	


def recordMentalHist():
	## ask all the questions from the questions.json, file.
	print("Ok, for these questions reply with a score from 1-4 (1 meaning a little of the time, 2 meaning some of the time, 3 meaning good part of the time, and 4 meaning most of the time) Do you understand the scoring?")
	resp = input()
	if("no" in resp):
		return
	print("Let me ask you a few questions, to asses your condition.");
	score = 0;
	for i in range(1,(total_questions+1)): ## this is where the variables control how many questions are asked.
		ques = str(i);
		print(questions[ques])
		score+= int(input())
	if(score < 25):
		print("You do not have any mental disorder.")
	elif(score < 50):
		print("You have mild depression")
	elif(score<100):
		print("You have a serious case of depression please see a doctor")
	
	return score;

def answerRestQuestions():
	"""
	A recursion method that will try to answer any questions the user might have regarding his/her diagnostics.

	The method will stop when the user enters no.

	Here the base call is user entering 'No'
	"""
	print("What do you want to know regarding your diagnostics.")
	resp = input()
	hasResp = False
	for x in responses:
		if x in resp:
			print(questions[x])
			hasResp = True

	if(not hasResp):
		print("Unfortunately i do not have the response for that.")

	print("Do you have any other questions ?")
	resp = input()
	if("no" in resp):
		return
	else:
		answerRestQuestions();