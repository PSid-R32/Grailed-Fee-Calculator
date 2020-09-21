def calculate(price):
  price = (price - (price * (.09 + pp) - .30))
  return(price)

print("Welcome to the Grailed Fee Calculator. \nPayout calculations are conducted in dollars \nPlease follow the prompts below. \n")
d = .029
i = .044
location = (input("Domestic or International \nEnter d (domestic) or i (international) \n"))

if location == 'd':
      pp = .029
else:
   pp = .044

listprice = float(input("\nEnter your listed price: "))
payout = calculate(listprice)
print('After fees, you will receive: %s' % payout, 'USD')