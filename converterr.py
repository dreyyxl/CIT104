# Currency converter program
usd = float(input("Enter amount in USD: "))
rate = float(input("Enter current exchange rate (NGN per USD): "))

ngn = usd * rate
print(f"${usd} = ₦{ngn}")
converts USD to NGN
# updated by Dveloper B