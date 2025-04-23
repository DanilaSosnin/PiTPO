n = int(input().strip())

for i in range(n):
    if i == 0:
        while True:
            line = input().strip()
            if line == '':
                break

    results = {}

    while True:
        try:
            s = input().strip()
            if s == '':
                break

            parts = s.split()
            if len(parts) != 4:
                continue

            num, task, time, state = parts
            num, task, time = int(num), int(task), int(time)

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