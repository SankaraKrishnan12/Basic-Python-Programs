from datetime import datetime
date1 = input("Enter from date in yyyy-mm-dd format : ")
date2 = input("Enter to date in yyyy-mm-dd format : ")
date1 = datetime.strptime(date1, '%Y-%m-%d')
date2 = datetime.strptime(date2, '%Y-%m-%d')
diff = date2 - date1
print(f'The number of days between {date2} and {date1} is {diff.days} days.')
