principle= int(input("Enter Principle Amount : "))
rate= int(input("Enter Rate Percentage  : "))
time= int(input("Enter Time in Years : "))
si = (principle*rate*time)/100
amount = si+principle
print(f" Simple Interest is {si} and Total Amount is {amount}")
