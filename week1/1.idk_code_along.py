from datetime import datetime
now = datetime.now()
print(type(now), now)

#datetime.weekday() - starts at 0 for Monday, ends at 6 for Sunday
print(now.weekday())