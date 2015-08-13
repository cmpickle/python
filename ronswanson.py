import requests as req

r = req.get("http://ron-swanson-quotes.herokuapp.com/v2/quotes")
quote = r.json()[0]

print(quote)
