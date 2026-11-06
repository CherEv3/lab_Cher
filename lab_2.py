amoebas = 1
interval_hours = 3
total_time = 24

print("Время (ч)\tКоличество клеток")
print("-" * 30)

for t in range(interval_hours, total_time + 1, interval_hours):
    amoebas *= 2
    # Вот тут самое важное: выводим переменную amoebas, а не текст "+1"
    print(f"{t}\t\t{amoebas}")
