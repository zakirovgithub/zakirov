import random

def printAnswers(mixed_answers, trueAnswer):
    answer = random.choice(mixed_answers)
    print("a) ",answer) 
    mixed_answers.remove(answer)
    if answer == trueAnswer:
        trueAnswer = 'a'
    answer = random.choice(mixed_answers)
    print("b) ",answer)
    mixed_answers.remove(answer)
    if answer == trueAnswer:
        trueAnswer = 'b'
    answer = random.choice(mixed_answers)
    print("c) ",answer)
    if answer == trueAnswer:
        trueAnswer = 'c'
    
    user_answer = input("Your answer: ")
    if user_answer == trueAnswer:
        print("You are correct!")
    elif(user_answer != trueAnswer):
        print("INCORRECT!")
        print("Correct answer: ", trueAnswer)
    else:
        print("Invalid value!")
    
def answerMix(mixed_answers, random_country, trueAnswer, Countries):
    mixed_answers.append(trueAnswer)
    mixed = random.choice(Countries)
    mixed_answers.append(mixed[1])
    mixed = random.choice(Countries)
    mixed_answers.append(mixed[1])
    printAnswers(mixed_answers, trueAnswer)

def Countries(text):
    Countries = []  
    mixed_answers = []
    with open(text, 'r') as file:
        for line in file:
            country, capital = line.strip().split(',')
            Countries.append((country, capital))
    random_country = random.choice(Countries)
    print("Country: ",{random_country[0]})
    trueAnswer = random_country[1]
    answerMix(mixed_answers, random_country, trueAnswer, Countries)
        
print("1. Asia")
print("2. Europe")
print("3. South America")
print("4. North America")
print("5. Africa")
print("6. Australia")
continent = input("Choose continent(Choose number between 1..6): ")

if continent == '1':
    text = 'asia.txt'
    Countries(text)
elif continent == '2':
    text = 'europe.txt'
    Countries(text)
elif continent == '3':
    text = 'southAmerica.txt'
    Countries(text)
elif continent == '4':
    text = 'northAmerica.txt'
    Countries(text)
elif continent == '5':
    text = 'africa.txt'
    Countries(text)
elif continent == '6':
    text = 'australia.txt'
    Countries(text)
else:
    print("Invalid value")