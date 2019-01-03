import random
Input = []
for i in range(1,100):
    person = {}
    person['id'] = i
    person['enter_floor'] = random.randint(1,12)      
    person['exit_floor'] = random.randint(1,12)
    person['time_quantum'] = random.randint(60,200)
    person['intime'] = random.randint(1,3600)
    Input.append(person)

def scan_edf(Input):
    new_Input=[]
    pesenger=[]
    current_min=9999
    current_floor=1
    current_time=0
    current_task=0
    direction=0
    waiting_time=0
    diff=0
    bias=0
    max_pesenger=15
    Output=[]
    temp_enter=0
    temp_exit=0
    enter_time=0
    exit_time=0

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
                current_task=(person['id'])
                diff=abs(person['enter_floor']-current_floor)
                temp_enter=person['enter_floor']
                temp_exit=person['exit_floor']
                if(current_time<person['intime']):
                    enter_time=person['intime']+diff*2+2
                else:
                    enter_time=current_time+diff*2+2
                exit_time=enter_time+(abs(person['enter_floor']-person['exit_floor']))*2+2+15*2
            elif (person['time_limit']==current_min): #一樣的time limit就scan，看哪層離電梯比較近
                if (diff>abs(person['enter_floor']-current_floor)):
                    current_task=person['id']
                    diff=abs(person['enter_floor']-current_floor)
        


        current_time=exit_time                                                                                                           
        current_floor=temp_exit
        current_min=9999
        for person in new_Input:
            if(person['id']==current_task or (person['intime']<enter_time and  person['enter_floor']==temp_enter and person['exit_floor']==temp_exit) ):
            #if(person['id']==current_task):
                if(len(pesenger)<max_pesenger):
                    pesenger.append(person)
                    new_Input.remove(person)
        for person in pesenger:
                
                #if (current_time<person['intime']):
                 #   current_time=person['intime']+diff*2
                #else:
                 #   current_time=current_time+diff*2
                waiting_time=enter_time-person['intime']
                #current_time=current_time+(abs(person['enter_floor']-person['exit_floor']))*2+8+8
                bias=person['time_quantum']-waiting_time
                in_person={}
                in_person['id']=current_task
                in_person['waiting_time']=waiting_time
                in_person['bias']=bias
                pesenger.remove(person)
                Output.append(in_person)

    return Output.copy()

print(*Input,sep='\n')
Output=scan_edf(Input)
print(*Output,sep='\n')

    




