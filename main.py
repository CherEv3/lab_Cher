#сталь(V=80 м/мин) алюминий(V=250 м/мин) чугун(V=60 м/мин)
def diameter():
    while True:
        value=input("Введите диаметр(5 до 200):")
        diameter=float(value)
        if 5<=diameter<=200:
            return diameter
        else:
            print("Ошибка: введено число вне указанных значений")
        
            

