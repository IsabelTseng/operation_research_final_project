def look(Input):
    passenger1 = []
    passenger2 = []

    if direction == 1:
        for person in Input:
            if person['direction'] == 1 :
                if person['enter_floor'] > current_floor : 
                    passenger1.append(person)
                    Input.remove(person)
                else:
                    passenger2.append(person)
                    Input.remove(person)
        passenger1=sorted(passenger1, key = lambda x : x['exit_floor']) 
        passenger2=sorted(passenger2, key = lambda x : x['exit_floor']) 
        Input=sorted(Input, key = lambda x : x['exit_floor'],reverse=True)
        
    else:
        for person in Input:
            if person['direction'] == -1 :
                if person['enter_floor'] < current_floor : 
                    passenger1.append(person)
                    Input.remove(person)
                else :
                    passenger2.append(person)
                    Input.remove(person)
            
        passenger1 = sorted(passenger1, key = lambda x : x['exit_floor'],reverse=True) 
        passenger2 = sorted(passenger2, key = lambda x : x['exit_floor'],reverse=True) 
        Input = sorted(Input, key = lambda x : x['exit_floor'])
    Output = passenger1 + Input + passenger2
    
    return Output.copy()



        
