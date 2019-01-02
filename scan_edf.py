import random
Input = []
for i in range(1,20):
    person = {}
    person['id'] = i
    person['enter_floor'] = random.randint(1,12)      
    person['exit_floor'] = random.randint(1,12)
    person['time_quantum'] = random.randint(30,60)
    person['intime'] = random.randint(1,61)
    Input.append(person)

def scan_edf(Input):
    new_Input=[]
    current_min=9999
    current_floor=1
    current_time=0
    current_task=1
    direction=0
    waiting_time=0
    diff=0
    bias=0
    Output=[]

    for person in Input:
        newperson=person.copy()
        newperson['time_limit']=newperson['intime']+newperson['time_quantum']
        if (newperson['enter_floor']-newperson['exit_floor']<0):
            newperson['direction']=0
        else :
            newperson['direction']=1
        new_Input.append(newperson)

    while(len(new_Input)!=0):
        for person in new_Input:
            if (person['time_limit']<current_min):  #尋找最小的time limit
                current_min=person['time_limit']
                current_task=person['id']
                diff=abs(person['enter_floor']-current_floor)                
            elif (person['time_limit']==current_min): #一樣的time limit就scan，看哪層離電梯比較近
                if (diff>abs(person['enter_floor']-current_floor)):
                    current_task=person['id']
                    diff=abs(person['enter_floor']-current_floor)

        for person in new_Input:
            if(person['id']==current_task):
                current_time=person['intime']+diff*2+(abs(person['exit_floor']-person['enter_floor']))*2+2*8  
                waiting_time=current_time-person['intime']
                bias=person['time_limit']-current_time
                direction=person['direction']
                current_min=9999
                new_Input.remove(person)
                in_person={}
                in_person['id']=current_task
                in_person['waiting_time']=waiting_time
                in_person['bias']=bias
                Output.append(in_person)
    return Output.copy()

print(*Input,sep='\n')
Output=scan_edf(Input)
print(*Output,sep='\n')

    




