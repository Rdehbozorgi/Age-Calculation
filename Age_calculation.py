import tkinter as tk
from datetime import datetime


root = tk.Tk()
root.title('birthday')
root.geometry('500x600')

#make datetime from birth user
def date_user(user_brith):
    date_user_brith = datetime.strptime(user_brith, '%Y-%m-%d').date()
    date_now = datetime.now().date()
    year_user = date_now.year - date_user_brith.year
    month_user = date_now.month - date_user_brith.month
    day_user = date_now.day - date_user_brith.day
    #return f'today is {date_now} \n you are {year_user} years and {month_user} month and {day_user} days'
    return date_now, year_user, month_user, day_user

#access brith

def result(date_user):
    date_now, year_user, month_user, day_user = date_user
    if day_user < 0 and month_user > 0:
        #for 31 days
        if month_user in [1,3,5,7,8,10,12]:
            main_day = (31 + day_user)
            main_month = month_user - 1
            return date_now, year_user, main_month, main_day
        #for 30 days
        else:
            main_day = 30 + day_user
            main_month = month_user - 1
            return date_now, year_user, main_month, main_day
    elif month_user < 0 and day_user > 0 :
        main_year = year_user - 1
        main_month = 12 + month_user
        return date_now, main_year, main_month, day_user
    elif month_user < 0 and day_user < 0:
        main_year = year_user - 1
        main_month = (12 + month_user) - 1
        if (12 + month_user) in [1,3,5,7,8,10,12]:
            main_day = (31 + day_user)
        elif (12 + month_user) in [2,4,6,9,11]:
            main_day = 30 + day_user
        return date_now, main_year, main_month, main_day
    elif month_user == 0 and day_user < 0:
        main_year = year_user - 1
        main_month = 11
        if (datetime.now().date().month) in [1,3,5,7,8,10,12]:
            main_day = (31 + day_user)
        elif (datetime.now().date().month) in [2,4,6,9,11]:
            main_day = 30 + day_user
        return date_now, main_year, main_month, main_day
    return date_now, year_user, month_user, day_user



def show_result(result):
    fstring_list = []
    today, year, month, day = result
    for i, j in zip([year, month, day],['year', 'month', 'day']):
        if i != 0:
            fstring_list.append(f'{i} {j}s ')
    main_result = 'and '.join(fstring_list)
    #return main_result
    label.config(text = f'today is {today} \n and {main_result}')
    #return f'today is {today} \n and {main_result}'

#function for common
def final():
    user_brith = user_type.get()
    return show_result(result(date_user(user_brith)))

label = tk.Label(root, text = 'please enter your birth date: ').pack()
user_type = tk.Entry(root)
user_type.pack()
button = tk.Button(root, text = 'Enter', command = final).pack(pady = 50)





#user_brith = '1987-8-31'
'''user = (date_user(user_brith))
print(show_result(result(user)))'''
#print(final)


root.mainloop()

