exam_st_date = input("Enter the date with comma separated : ")
date = tuple(exam_st_date.split(','))
print(date[0]+"/"+date[1]+"/"+date[2])
