# a dictionary that stores questions and answers 
# have a varibale that tracks the score of the player 
#loop through the dictionary using the key value pairs
#display each question to he user and allow them to anwers 
# tell them if they are right or wrong 
# show the final result quiz is completed 


quiz = {
   "question1": {
       "question": "what is the capital of france?",
       "Answer": "Paris"
   },
   "question2":{
       "question": "what is the capital of germany",
       "Answer" : "Berlin"
   },
    "question3":{
       "question": "what is the capital of italy",
       "Answer" : "rome"
   },
    "question4":{
       "question": "what is the capital of Spain",
       "Answer" : "Madrid"
   },
    "question5":{
       "question": "what is the capital of portugal",
       "Answer" : "lisbon"
   },
    "question6":{
       "question": "what is the capital of switzerland",
       "Answer" : "bern"
   },
    "question7":{
       "question": "what is the capital of Austria",
       "Answer" : "vienna"
   },

}

score = 0 

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer?")


    if answer.lower()== value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))

    else:
        print("Wrong")
        print("The answer is " + value["answer"])
        print("Your score is: " + str(score))