from functions import * ;

## Start the program.

## Run this file to start the application.
inputresp = "";


print("Welcome to a virtual psychatrist.\nWhat is your name ?");
name = input()
print(f"Welcome {name}, what is your age ?");
age = input()
print("What can i help you with");

keep_asking = True;


inputresp = input()
output = returnResp(inputresp);
print(output)
	
print("Thanks Goodbye.")



