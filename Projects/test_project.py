class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Blue\n(c) Purple\n(d) Brown\n\n",
    "What color are bananas?\n(a) Blue\n(b) Yellow\n(c) Green\n(d) Orange\n\n",
    "What is the Capital of India?\n(a) Mumbai\n(b) Chattisgarh\n(c) Delhi\n(d) Trivandrum\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        ans = input(question.prompt).lower()
        if ans == question.answer:
            score += 1
        else:
            print("explanation\n")
    print("your score is "+str(score) + "/" + str(len(questions)))

run_test(questions)
