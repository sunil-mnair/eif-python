from datetime import *

today = datetime.now()

new_date = today + timedelta(days = 1)
print(new_date) # 2024-07-09  09-Jul-2024

# Tuesday,09-Jul-2024 ("%A,%d-%b")
print(new_date.strftime("%A,%d-%B-%Y"))

birthdate = 'Oct 02, 88'
# %b %d, %y
print(datetime.strptime(birthdate,'%b %d, %y'))

