import random
from parameters import MAX_PASSANGER, ELEVATOR_PASS_TIME, ELEVATOR_SPEED_UP_TIME, ELEVATOR_SLOW_DOWN_TIME

#Input = []
#for i in range(1,100):
#    person = {}
#    person['id'] = i
#    person['enter_floor'] = random.randint(1,12)
#    person['exit_floor'] = random.randint(1,12)
#    person['time_quantum'] = random.randint(60,200)
#    person['intime'] = random.randint(1,3600)
#    Input.append(person)

def scan_edf(Input):
    new_Input = []
    pesenger = []
    current_floor = 1
    current_time = 0
    current_task = 0
    direction = 0
    waiting_time = 0
    bias = 0
    Output = []
    temp_enter = 0
    temp_exit = 0
    enter_time = 0
    exit_time = 0

    # Calculate time limit and direction
    for person in Input:
        newperson = person.copy()
        newperson['time_limit'] = newperson['intime'] + newperson['time_quantum']
        if newperson['enter_floor'] - newperson['exit_floor'] < 0:
            newperson['direction'] = 'up'
        else:
            newperson['direction'] = 'down'
        new_Input.append(newperson)

    current_request = {
        'id': 0,
        'enter_floor': 0,
        'exit_floor': 0,
        'time_quantum': 0,
        'intime': 0,
        'time_limit': 5000,
        'direction' = 'up'
        }
    # Process all request
    while len(new_Input) > 0:
        # Find first expire request
        for person in new_Input:
            if person['time_limit'] < current_request['time_limit']:  #尋找最小的time limit
                current_request = person.copy()
                diff = abs(person['enter_floor'] - current_floor)
                if current_time < person['intime']:
                    enter_time = person['intime'] + diff * 2 + 2
                else:
                    enter_time = current_time + diff * 2+2
                exit_time = enter_time + (ELEVATOR_SPEED_UP_TIME + ELEVATOR_PASS_TIME * (abs(person['enter_floor'] - person['exit_floor']) - 2) + ELEVATOR_SLOW_DOWN_TIME) + 15
            elif person['time_limit'] == current_min: #一樣的time limit就scan，看哪層離電梯比較近
                if diff > abs(person['enter_floor'] - current_floor):
                    current_task = person['id']
                    diff = abs(person['enter_floor'] - current_floor)

        current_time = exit_time
        current_floor = temp_exit
        current_min = 9999
        for person in new_Input:
            if(person['id']==current_task or (person['intime']<enter_time and  person['enter_floor']==temp_enter and person['exit_floor']==temp_exit) ):
            #if(person['id']==current_task):
                if(len(pesenger)<MAX_PASSANGER):
                    pesenger.append(person)
                    new_Input.remove(person)
        for person in pesenger:
                waiting_time=enter_time-person['intime']
                bias=person['time_quantum']-waiting_time
                in_person={}
                in_person['id']=current_task
                in_person['waiting_time']=waiting_time
                in_person['bias']=bias
                pesenger.remove(person)
                Output.append(in_person)

    return Output.copy()