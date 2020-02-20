total = int(input("Enter the cost value of your trade: "))
#country = "US"
#country = "TR"
country = input("Enter your country (US or TR): ")
if country == "US":
	if total <= 50:
		print("Shipping Cost is  $50")
	elif total <= 100:
		print("Shipping Cost is $25")
	elif total <= 150:
		print("Shipping Costs $5")
	else:
		print("FREE")
if country == "TR": 
	if total <= 50:
		print("Shipping Cost is  $100")
	else:
		print("FREE")