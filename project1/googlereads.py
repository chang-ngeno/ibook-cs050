import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "AS0cveonbrXFGHu9TpC1Vg", "isbns": "9781632168146"})
print(res.json())