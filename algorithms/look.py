sign = lambda x: [1, -1][x < 0]

def look(input_data, args):
    passenger1 = []
    passenger2 = []
    passenger3 = []

    for i in range(len(input_data) - 1, -1, -1):
        if input_data[i]['direction'] == args['direction']:
            if sign(input_data[i][args['target']] - args['current_floor']) == args['direction']:
                passenger1.append(input_data[i])
                input_data.pop(i)
            else:
                passenger3.append(input_data[i])
                input_data.pop(i)

    passenger1 = sorted(passenger1, key = lambda x : x[args['target']], reverse = (args['direction'] == -1))
    passenger3 = sorted(passenger3, key = lambda x : x[args['target']], reverse = (args['direction'] == -1))
    passenger2 = sorted(input_data, key = lambda x : x[args['target']], reverse = (args['direction'] == 1))

    Output = passenger1 + passenger2 + passenger3

    return Output