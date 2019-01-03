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

Output=sorted(Input,key=lambda s: s['intime'])
print(*Output,sep='\n')
