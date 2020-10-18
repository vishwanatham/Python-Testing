from datetime import datetime

def is_weekday():
    today = datetime.today()
    return (0 <= today.weekday() < 5)


print (is_weekday())