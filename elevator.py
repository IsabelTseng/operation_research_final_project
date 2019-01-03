from parameters import MAX_PASSANGER, ELEVATOR_PASS_TIME, ELEVATOR_SPEED_UP_TIME, ELEVATOR_SLOW_DOWN_TIME, ELEVATOR_DOOR_OPEN_TIME, ELEVATOR_DOOR_CLOSE_TIME

sign = lambda x: [1, -1][x < 0]

class Elevator():
    def __init__(self, algorithm):
        self.current_time = 0
        self.floor = 1
        self.target_floor = 1
        self.state = 'idle'
        self.direction = 0
        self.passengers = []
        self.requests = []
        self.sort = algorithm
        self.output_data = []

    def serve(self, input_data):
        while len(output_data) < len(input_data):
            if self.state == 'idle':
                # If no one in elevator
                if len(passengers) == 0:
                    # If no one is waiting for elevator, remain idle
                    if len(requests) == 0:
                        self.direction = 0
                        self.change_state('idle')
                    # If someone is waiting for elevator
                    else:
                        if requests[0]['exit_floor'] != self.floor:
                            self.target_floor = requests[0]['exit_floor']
                            self.direction = sign(self.target_floor - self.floor)
                            self.change_state('move')
                        else:
                            self.change_state('door_open')
                # If somebody in elevator
                else:
                    # If someone is leaving elevator
                    if sum([p['exit_floor'] == self.floor for p in self.passengers]) > 0:
                        self.change_state('door_open')
                    # If no one is leaving elevator
                    else:
                        # If no one is waiting for elevator
                        if len(requests) == 0:
                            self.target_floor = passengers[0]['exit_floor']
                            self.direction = sign(self.target_floor - self.floor)
                            self.change_state('move')
            elif self.state == 'door_open':
                self.flush_passenger()
                self.accept_passenger()
                self.change_state('idle')
            elif self.state == 'move':
                if self.floor == self.target_floor:
                    self.change_state('idle')
                else:
                    self.change_state('move')
            self.queue_request()
            self.sort(self.requests)
            self.sort(self.passengers)

    def accept_passenger(self):
        for request in self.requests:
            if len(self.passengers) < MAX_PASSANGER and request['enter_floor'] == self.floor and request['direction'] == self.direction:
                self.passengers.append(request)
                self.requests.remove(request)

    def flush_passenger(self):
        for passenger in self.passengers:
            if passenger['exit_floor'] == self.floor:
                self.output.append({
                    'id': passenger['id'],
                    'wating_time': self.current_time - passenger['timestamp'],
                    'bias': passenger['time_quantum'] - passenger['waiting_time']
                })
                self.passengers.remove(passenger)

    def queue_request(self):
        for request in input_data:
            if request['timestamp'] <= self.current_time:
                self.requests.append(request)

    def change_state(self, new_state):
        if self.state == 'idle':
            if new_state == 'idle':
                self.current_time += 1
            elif new_state == 'door_open':
                self.current_time += ELEVATOR_DOOR_OPEN_TIME
            elif new_state == 'move':
                self.current_time += ELEVATOR_SPEED_UP_TIME
                self.floor += self.direction
        elif self.state == 'door_open':
            if new_state == 'idle':
                self.current_time += ELEVATOR_DOOR_CLOSE_TIME
            elif new_state == 'door_open':
                pass
            elif new_state == 'move':
                print('Cannot transit from "door_open" to "move"')
                new_state = 'door_open'
        elif self.state == 'move':
            if new_state == 'idle':
                self.current_time += ELEVATOR_SLOW_DOWN_TIME
            elif new_state == 'door_open':
                print('Cannot transit from "move" to "door_open"')
                new_state = 'move'
            elif new_state == 'move':
                self.floor += self.direction
                self.current_time += ELEVATOR_PASS_TIME
        self.state = new_state