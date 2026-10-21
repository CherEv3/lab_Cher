#сталь(V=80 м/мин) алюминий(V=250 м/мин) чугун(V=60 м/мин)
def get_diameter():
    
    while True:
        value = input("Введите диаметр (от 5 до 200): ")
        try:
            diam = float(value)
            if 5 <= diam <= 200:
                return diam
            else:
                print("Ошибка: число вне диапазона от 5 до 200.")
        except ValueError:
            print("Ошибка: введите число.")

def get_zub_count():
   
    while True:
        value = input("Введите количество зубьев (от 1 до 20): ")
        try:
            count = int(value) # Для количества зубьев лучше использовать целое число
            if 1 <= count <= 20:
                return count
            else:
                print("Ошибка: число вне диапазона от 1 до 20.")
        except ValueError:
            print("Ошибка: введите целое число.")

def get_clearance():
    while True:
         value = input("Введите зазор (от 0.01 до 0.5): ")
         try:
            clearance = float(value)
            if 0.01 <= clearance <= 0.5:
                return clearance
            else:
                print("Ошибка: число вне диапазона от 0.01 до 0.5.")
        except ValueError:
    print("Ошибка: введите число.")
def get_glud():
    while True:
        value = input("Введите значение(от 0.1 до 0.5):")
         try:
           glud(value)
                    if 0.01 <= glud <=0.5:
                        return glud
                    else:
                        print("Ошибка: число вне диапазона от 0.01 до 0.5.")
                except ValueError:
        print("Ошибка: введите число.")
            

