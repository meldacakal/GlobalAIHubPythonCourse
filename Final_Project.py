# Final Project - Knowledge Competition
print("*** Welcome to the new episode of 'Who Wants To Be A Billionaire' ***")
name = input("Please enter your name: ")


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "Question 1: Let us start with an easy question. What is the currency of Turkey?: ",
    "Question 2: Who directed Pulp Fiction?: ",
    "Question 3: Who is older Bart or Lisa on The Simpsons?: ",
    "Question 4: Who wrote Crime and Punishment?: ",
    "Question 5: In the Harry Potter, what is the name of Hagrid's dog?: ",
    "Question 6: Complete the missing element: fire, water, air, .... : ",
    "Question 7: What does http stand for?: ",
    "Question 8: How many Lord of the Ring movies are there?: ",
    "Question 9: Where does Spongebob Squarepants live in?:",
    "Question 10: Which mammal has no vocal cords?: ",
]

questions = [
    Question(question_prompts[0], "lira"),
    Question(question_prompts[1], "Quentin Tarantino"),
    Question(question_prompts[2], "Bart"),
    Question(question_prompts[3], "Dostoyevski"),
    Question(question_prompts[4], "Fang"),
    Question(question_prompts[5], "earth"),
    Question(question_prompts[6], "hypertext transfer protocol"),
    Question(question_prompts[7], "3"),
    Question(question_prompts[8], "pineapple"),
    Question(question_prompts[9], "giraffe"),


]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 10

    if score <= 40:
        print("You are a Loser,", name, ".You got",str(score), "out of 100.Try again.")
    else:
        print("We have a WINNER!",name, "got", str(score), "out of 100.Congrats!")


run_quiz(questions)


