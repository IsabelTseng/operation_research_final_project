from utils.config import MAX_PASSANGER, ELEVATOR_PASS_TIME, ELEVATOR_SPEED_UP_TIME, ELEVATOR_SLOW_DOWN_TIME, ELEVATOR_DOOR_OPEN_TIME, ELEVATOR_DOOR_CLOSE_TIME
sign = lambda x: [1, -1][x < 0]

class Elevator():
    def __init__(self, algorithm):
        self.sort = algorithm

    def initialize(self):
        self.current_time = 0
        self.floor = 1
        self.target_floor = 1
        self.state = 'idle'
        self.direction = 0
        self.passengers = []
        self.requests = []
        self.input_data = []
        self.output_data = []

    def serve(self, input_data):
        self.initialize()
        self.input_data = input_data.copy()
        while len(self.output_data) < len(input_data):
            if self.state == 'idle':
                # If no one in elevator
                if len(self.passengers) == 0:
                    # If no one is waiting for elevator, remain idle
                    if len(self.requests) == 0:
                        self.direction = 0
                        self.change_state('idle')
                    # If someone is waiting for elevator
                    else:
                        # If someone is entering elevator
                        if len(self.passengers) < MAX_PASSANGER and sum([p['enter_floor'] == self.floor for p in self.requests]) > 0:
                            self.change_state('door_open')
                        # If no one is entering elevator
                        else:
                            # If the one waiting is not at current floor
                            if self.requests[0]['enter_floor'] != self.floor:
                                self.target_floor = self.requests[0]['enter_floor']
                                self.direction = self.set_direction(self.target_floor - self.floor)
                                self.change_state('move')
                            # If the one waiting is at current floor
                            else:
                                self.direction = self.requests[0]['direction']
                                self.change_state('door_open')
                # If somebody in elevator
                else:
                    # If someone is leaving elevator
                    if sum([p['exit_floor'] == self.floor for p in self.passengers]) > 0:
                        self.change_state('door_open')
                    # If someone is entering elevator
                    elif len(self.passengers) < MAX_PASSANGER and sum([p['enter_floor'] == self.floor for p in self.requests]) > 0:
                        self.change_state('door_open')
                    else:
                        # If no one is waiting for elevator
                        if len(self.requests) == 0:
                            self.target_floor = self.passengers[0]['exit_floor']
                            self.direction = self.set_direction(self.target_floor - self.floor)
                            self.change_state('move')
                        # If someone is also waiting for elevator
                        else:
                            if len(self.passengers) == MAX_PASSANGER:
                                target = self.passengers[0]
                            else:
                                target = self.sort([self.passengers[0], self.requests[0]], {
                                    'target': 'enter_floor',
                                    'current_floor': self.floor,
                                    'direction': self.direction,
                                })[0]
                            self.target_floor = target['exit_floor'] if target['id'] == self.passengers[0]['id'] else target['enter_floor']
                            self.direction = self.set_direction(self.target_floor - self.floor)
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
            self.requests = self.sort(self.requests, {
                'target': 'enter_floor',
                'current_floor': self.floor,
                'direction': self.direction,
            })
            self.passengers = self.sort(self.passengers, {
                'target': 'exit_floor',
                'current_floor': self.floor,
                'direction': self.direction,
            })

    def accept_passenger(self):
        for i in range(len(self.requests) - 1, -1, -1):
            if len(self.passengers) < MAX_PASSANGER and self.requests[i]['enter_floor'] == self.floor:# and self.requests[i]['direction'] == self.direction:
                self.passengers.append(self.requests[i])
                self.requests.pop(i)

    def flush_passenger(self):
        for i in range(len(self.passengers) - 1, -1, -1):
            if self.passengers[i]['exit_floor'] == self.floor:
                self.output_data.append({
                    'id': self.passengers[i]['id'],
                    'waiting_time': self.current_time - self.passengers[i]['timestamp'],
                    'bias': self.passengers[i]['time_quantum'] - (self.current_time - self.passengers[i]['timestamp'])
                })
                self.passengers.pop(i)

    def queue_request(self):
        for i in range(len(self.input_data) - 1, -1, -1):
            if self.input_data[i]['timestamp'] <= self.current_time:
                self.requests.append(self.input_data[i])
                self.input_data.pop(i)

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

    def set_direction(self, diff):
        if diff == 0:
            return -self.direction
        elif diff > 0:
            return 1
        else:
            return -1
