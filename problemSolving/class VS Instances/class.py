class Person:
    def __init__(self, initialAge: int):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
	    self.age = initialAge
    
    def amIOld(self):
        if self.age < 13:
            Print("You are young.")
	elif 13 <= self.age <= 19 :
	    print("You are a teenager.")
	else:
	    print("You are old.")
    
    def yearPasses(self):
        self.age += 1


age = int(input())
p = Person(age)
p.amIOld()

for i in range(0, 3):
    p.yearPasses()
    p.amIOld()
