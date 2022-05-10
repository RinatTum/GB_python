def user_data(**kwargs):
    return ' '.join(kwargs.values())


print(user_data(Name=input("Name: "), Surname=input("surname: "), Birthday=input('Birthday'), City=input('City:'),
                Email=input("Mail"), Phone=input("Phone: ")))
