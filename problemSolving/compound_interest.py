
#principle, Rate, Time
def compound_interest(p, r, t):
    interest = p * ((1 + r / 100) ** t) #formula of interest
    return interest

principle = int(input("Money you borrowed: "))
interest_rate = float(input("Your interest rate: "))
time = float(input("overall duration: "))

total_due = compound_interest(principle, interest_rate, time)

# print(f"You borrowed {principle}")
print("you borrowed" + str(principle))
# print(f"Interest amount is {total_due}")
print("Interest amount is " + str(total_due))