n = int(input().strip())

for i in range(n):
    results = {}

    while True:
        try:
            s = input().strip()
            if s == '':
                break

            parts = s.split()
            if len(parts) < 4:  # Минимум 4 элемента: номер, задача, время, состояние
                continue

            num = parts[0]
            task = parts[1]
            time = parts[2]
            state = parts[3]

            try:
                num = int(num)
                task = int(task)
                time = int(time)
            except ValueError:
                continue

            if num not in results:
                results[num] = {'solved': 0, 'penalty': 0, 'tasks': {}}

            if task not in results[num]['tasks']:
                results[num]['tasks'][task] = {'solved': False, 'incorrect': 0}

            if state == "C" and not results[num]['tasks'][task]['solved']:
                results[num]['solved'] += 1
                results[num]['penalty'] += time + 20 * results[num]['tasks'][task]['incorrect']
                results[num]['tasks'][task]['solved'] = True

            elif state == "I" and not results[num]['tasks'][task]['solved']:
                results[num]['tasks'][task]['incorrect'] += 1

        except EOFError:
            break

    rating_table = []
    for participant, data in results.items():
        rating_table.append((participant, data['solved'], data['penalty']))

    rating_table.sort(key=lambda x: (-x[1], x[2], x[0]))

    for participant, solved, penalty in rating_table:
        print(participant, solved, penalty)

    if i < n - 1:
        print()
