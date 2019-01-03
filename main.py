from utils.input_generator import get_input
from utils.elevator import Elevator
from algorithms.look import look
from algorithms.scan_edf import scan_edf
import utils.analytics as aly

input_data = get_input()

elevator1 = Elevator(look)
elevator1.serve(input_data)
aly.get_histogram([x['waiting_time'] for x in elevator1.output_data], 'Waiting time distribution with Look', 'waiting time', 'count', 'look', 30)

elevator2 = Elevator(scan_edf)
elevator2.serve(input_data)
aly.get_histogram([x['waiting_time'] for x in elevator2.output_data], 'Waiting time distribution with Scan-edf', 'waiting time', 'count', 'scan_edf', 30)
