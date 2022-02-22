## Import the libraries
import json;

## Load the data
responses = 0
questions = 0
score = 0;
total_questions = 3


with open('./responses.json') as json_file:
	responses = json.load(json_file)
with open('./questions.json') as json_file:
	questions = json.load(json_file)


def returnResp(inputresp):
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
						return f"Your Mental Score is {score}."
			else:
				return resp;


def recordMentalHist():
	## ask all the questions from the json, file.
	print("Ok, for these questions reply with a score from 1-4 (1 meaning a little of the time, 2 meaning some of the time, 3 meaning good part of the time, and 4 meaning most of the time) Do you understand the scoring?")
	resp = input()
	if("no" in resp):
		return
	print("Let me ask you a few questions, to asses your condition.");
	score = 0;
	for i in range(1,(total_questions+1)):
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
	## a recursion method that will keep asking queries regarding the diagnostic.
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