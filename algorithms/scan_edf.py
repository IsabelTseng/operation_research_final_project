sign = lambda x: [1, -1][x < 0]

def scan_edf(input, args):
    # calculate time limit and floor difference
    new_input = []
    for person in input:
        new_person = person.copy()
        new_person['time_limit'] = new_person['timestamp'] + new_person['time_quantum']
        new_person['floor_diff'] = new_person[args['target']] - args['current_floor']
        new_person['floor_diff'] = new_person['floor_diff'] if sign(new_person['floor_diff']) == args['direction'] else 15
        new_input.append(new_person)

    return sorted(new_input, key = lambda x: (x['time_limit'], x['floor_diff']))