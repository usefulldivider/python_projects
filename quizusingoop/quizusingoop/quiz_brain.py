class Brain:
    def __init__(self, qb):
        self.qlist=qb
        self.qnum=0
        self.score=0

    def ended(self):
        print(f"\nYour final score is {self.score}/{len(self.qlist)}")
        exit()
    def nextques(self):
        while self.qnum!=12:
            ans=input(f"Q {self.qnum+1}:{self.qlist[self.qnum].question}(True/False)?\ntype end to end ").capitalize()
            if ans=="End":
                self.ended()
            if ans!=self.qlist[self.qnum].answer:
                print(f"wrong answer\nThe right answer is {self.qlist[self.qnum].answer}")
            else:
                self.score+=1
                print("correct answer")
            print(f"Score:{self.score}/{self.qnum+1}")
            self.qnum += 1


