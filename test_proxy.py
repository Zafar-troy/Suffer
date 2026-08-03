import cloudscraper

s = cloudscraper.create_scraper()

proxies = {
    "http": "http://mjiuxdfd:1a6rzt53lqwt@31.59.20.176:6754",
    "https": "http://mjiuxdfd:1a6rzt53lqwt@31.59.20.176:6754"
}

r = s.get('https://api.sofascore.com/api/v1/sport/football/events/live', proxies=proxies)
print(r.status_code)
print(r.text[:300])