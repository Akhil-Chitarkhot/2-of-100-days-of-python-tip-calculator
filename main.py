#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill_amount = input("What is the bill amount? ")
tip_amount = input("What is the tip amount? ")
people_amount = input("How many people are splitting the bill? ")

tip_num = (int(tip_amount)/100) + 1

total_bill = float(bill_amount) * tip_num
split_bill = round(total_bill / int(people_amount), 2)
# split_bill = total_bill / int(people_amount)

print(f"Each person should pay {split_bill}")