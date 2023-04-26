from datetime import datetime
from datetime import date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()


description = f"Host was added via ANSIBLE on {today} at {current_time}"

print (description)