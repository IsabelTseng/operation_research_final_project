import random
Input = []
for i in range(1,100):
    person = {}
    person['id'] = i
    person['enter_floor'] = random.randint(1,12)      
    person['exit_floor'] = random.randint(1,12)
    person['time_quantum'] = random.randint(60,200)
    person['timestamp'] = random.randint(1,3600)
    Input.append(person)

def scan_edf(Input):
    new_Input = []
    passenger = []
    current_min = 9999
    current_floor = 1
    current_time = 0
    current_task = 0
    direction = 0
    waiting_time = 0
    bias = 0
    Output=[]
    enter_time = 0
    exit_time = 0
    current_passenger = {}
    MAX_PASSENGER = 15



    for person in Input:
        newperson = person.copy()
        newperson['time_limit'] = newperson['timestamp'] + newperson['time_quantum']
        if newperson['exit_floor'] - newperson['enter_floor'] > 0 :
            newperson['direction'] = 0
        else:
            newperson['direction'] = 1
        new_Input.append(newperson)

#    for time in range(1,3600):
#       for person in Input:
#            if person['timestamp'] == time :

    while(len(new_Input) > 0):
        for person in new_Input:
            if (person['time_limit'] < current_min):  #尋找最小的time limit
                current_min = person['time_limit']
                current_passenger = person.copy()
                diff = abs(person['enter_floor']-current_floor)
                if(current_time < person['timestamp']):
                    enter_time = person['timestamp']+diff*2+2
                else:
                    enter_time = current_time+diff*2+2

            elif (person['time_limit'] == current_min): #一樣的time limit就scan，看哪層離電梯比較近
                if (diff > abs(person['enter_floor'] - current_floor)):
                    current_task = person['id']
                    diff = abs(person['enter_floor'] - current_floor)
                                                                                      
        current_min = 9999
        for person in new_Input:
            if(person['timestamp'] < enter_time and  person['enter_floor'] == current_passenger['enter_floor'] and person['direction'] == current_passenger['direction'] ):
                if(len(passenger) < MAX_PASSENGER):
                    passenger.append(person)
                    new_Input.remove(person)
        if current_passenger['direction'] == 0 :
            passenger = sorted(passenger, key = lambda x : x['exit_floor'])
        else :
            passenger = sorted(passenger, key = lambda x : x['exit_floor'], reverse = True)
         
        for person in passenger:
            if len(passenger) == 1:
                current_time = enter_time+abs(person['exit_floor']-person['enter_floor'])*2+2+15*2
                current_floor = person['exit_floor']
            Output.append(person)
            passenger.remove(person)


    return Output.copy()

print(*Input,sep='\n')
Output=scan_edf(Input)
print(*Output,sep='\n')

    




