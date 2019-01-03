
def scan_edf(Input,args):
    new_Input = []
    current_min = 9999
    Output=[]
    request=0


    for person in Input:
        newperson = person.copy()
        newperson['time_limit'] = newperson['timestamp'] + newperson['time_quantum']
        new_Input.append(newperson)


    while len(new_Input) > 0:
        for person in new_Input:
            if person['time_limit'] < current_min :  #尋找最小的time limit
                current_min = person['time_limit']
                request = person['id']
                diff = abs(person['enter_floor'] - args['current_floor'])
            elif (person['time_limit'] == current_min): #一樣的time limit就scan，看哪層離電梯比較近
                if (diff > abs(person['enter_floor'] - args['current_floor'])):
                    request = person['id']
                                                                                      
        current_min = 9999
        for person in new_Input:
            if person['id'] == request :
                Output.append(person)
                new_Input.remove(person)


    return Output.copy()


