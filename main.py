from utils.input_generator import get_input
from utils.elevator import Elevator
from algorithms.look import look
from algorithms.scan_edf import scan_edf
import utils.analytics as aly

input_data = get_input()
elevator1 = Elevator(scan_edf)
elevator1.serve(input_data)
print(elevator1.output_data)