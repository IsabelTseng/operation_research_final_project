sign = lambda x: [1, -1][x < 0]

def look(input_data, args):
    passenger1 = []
    passenger2 = []
    passenger3 = []

    newInput = Input.copy()
    for i in range(len(newInput)):
        person = newInput[len(Input)-i-1]
        if person['direction'] == args['direction'] :
            if sign(person[args['target']] - args['current_floor']) == args['direction']: 
                passenger1.append(person)
                newInput.remove(person)
            else:
                passenger3.append(person)
                newInput.remove(person)

    passenger1=sorted(passenger1, key = lambda x : x[args['target']], reverse = (args['direction'] == -1)) 
    passenger3=sorted(passenger3, key = lambda x : x[args['target']], reverse = (args['direction'] == -1)) 
    passenger2=sorted(newInput, key = lambda x : x[args['target']],reverse = (args['direction'] == 1))
    
    Output = passenger1 + passenger2 + passenger3 
    
    return Output.copy()