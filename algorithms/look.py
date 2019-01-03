sign = lambda x: [1, -1][x < 0]

def look(input_data, args):
    passenger1 = []
    passenger2 = []
    passenger3 = []

    new_input = input_data.copy()
    for i in range(len(new_input) - 1, -1, -1):
        if new_input[i]['direction'] == args['direction'] :
            if sign(new_input[i][args['target']] - args['current_floor']) == args['direction']:
                passenger1.append(new_input[i])
                new_input.remove(new_input[i])
            else:
                passenger3.append(new_input[i])
                new_input.remove(new_input[i])

    passenger1 = sorted(passenger1, key = lambda x : x[args['target']], reverse = (args['direction'] == -1))
    passenger3 = sorted(passenger3, key = lambda x : x[args['target']], reverse = (args['direction'] == -1))
    passenger2 = sorted(new_input, key = lambda x : x[args['target']], reverse = (args['direction'] == 1))

    return passenger1 + passenger2 + passenger3