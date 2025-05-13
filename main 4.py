from collections import defaultdict

def parse_input():
    input_data = []
    while True:
        line = input().strip()
        if line == "":
            if input_data:
                n = int(input_data[0])  # Читаем количество тестов
                input_data.pop(0)  # Убираем количество тестов
                blocks = []
                for _ in range(n):
                    # Считываем тарифы
                    fees = list(map(int, input_data[0].split()))
                    input_data.pop(0)  # Убираем строку с тарифами
                    records = []
                    # Читаем записи для каждого теста
                    while input_data and input_data[0] != "":
                        records.append(input_data.pop(0))
                    blocks.append((fees, records))
                return blocks
            else:
                break
        # Игнорируем любые строки, не являющиеся входными данными
        if line and not line.startswith('Пример'):
            input_data.append(line)


def process_block(fees, records):
    trips = defaultdict(list)

    for record in records:
        parts = record.split()

        if len(parts) < 4:
            continue  # Пропускаем некорректные записи

        plate = parts[0]  # номер автомобиля
        date_time = parts[1]  # "01:01:06:01" формат
        action = parts[2]  # "enter" или "exit"
        km_marker = int(parts[3])  # километраж

        # Разделяем дату и время, игнорируем секунды
        try:
            hour, minute = map(int, date_time.split(':')[:2])  # Берем только первые две части
        except ValueError:
            continue  # Пропускаем некорректные записи

        timestamp = (hour, minute)

        trips[plate].append((timestamp, action, km_marker))

    bills = {}
    for plate in trips:
        trips[plate].sort()  # Сортируем по времени
        total_cost = 2  # $2 for the bill processing fee
        i = 0
        while i < len(trips[plate]) - 1:
            if trips[plate][i][1] == "enter" and trips[plate][i + 1][1] == "exit":
                # Вычисляем разницу километража
                hour, minute = trips[plate][i][0]
                km_start = trips[plate][i][2]
                km_end = trips[plate][i + 1][2]

                distance = abs(km_end - km_start)
                cost = distance * fees[hour] / 100 + 1  # Convert cents to dollars, add $1 trip fee
                total_cost += cost
                i += 2  # Переходим к следующей паре
            else:
                i += 1

        if total_cost > 2:  # Ignore if no valid trips were found
            bills[plate] = total_cost

    return sorted(bills.items())

def main():
    blocks = parse_input()
    results = []

    for i, (fees, records) in enumerate(blocks):
        processed = process_block(fees, records)
        if i > 0:
            results.append("")  # Разделение блоков пустой строкой
        for plate, cost in processed:
            results.append(f"{plate} ${cost:.2f}")

    print("\n".join(results))

if __name__ == "__main__":
    main()
