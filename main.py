from utils.input_generator import get_input
from utils.elevator import Elevator
from algorithms.look import look
from algorithms.scan_edf import scan_edf
import utils.analytics as aly
import time

elevator1 = Elevator(look)
elevator2 = Elevator(scan_edf)

look_wait_time_list = []
edf_wait_time_list = []
look_wait_time_mean_list = []
edf_wait_time_mean_list = []

ROUND = 500

for i in range(ROUND):
    input_data = get_input()
    elevator1.serve(input_data)
    elevator2.serve(input_data)

    look_wait_time = [x['waiting_time'] for x in elevator1.output_data]
    look_wait_time_list += look_wait_time
    look_wait_time_mean = int(aly.get_average(look_wait_time))
    look_wait_time_mean_list.append(look_wait_time_mean)
    #print(f'Average waiting time with LOOK: { look_wait_time_mean }')

    edf_wait_time = [x['waiting_time'] for x in elevator2.output_data]
    edf_wait_time_list += edf_wait_time
    edf_wait_time_mean = int(aly.get_average(edf_wait_time))
    edf_wait_time_mean_list.append(edf_wait_time_mean)
    #print(f'Average waiting time with SCAN-EDF: { edf_wait_time_mean }')

    """
    x_max = max([max(look_wait_time), max(edf_wait_time)])
    aly.get_histogram(
        data = look_wait_time,
        title = f'Waiting time distribution with LOOK, average = { look_wait_time_mean }',
        xlabel = 'waiting time',
        ylabel = 'count',
        filename = f'look{ i + 1 }',
        x_min = 0,
        x_max = x_max,
        bins = x_max // 60
    )

    aly.get_histogram(
        data = edf_wait_time,
        title = f'Waiting time distribution with SCAN-EDF, average = { edf_wait_time_mean }',
        xlabel = 'waiting time',
        ylabel = 'count',
        filename = f'scan_edf{ i + 1 }',
        x_min = 0,
        x_max = x_max,
        bins = x_max // 60
    )
    """

#print('--------------')
print(f'Mean of average waiting time with LOOK: { aly.get_average(look_wait_time_mean_list) }')
print(f'Standard deviation of average waiting time with LOOK: { aly.get_std(look_wait_time_mean_list) }')
print(f'Mean of average waiting time with SCAN-EDF: { int(aly.get_average(edf_wait_time_mean_list)) }')
print(f'Standard deviation of average waiting time with SCAN-EDF: { aly.get_std(edf_wait_time_mean_list) }')

aly.get_histogram(
    data = look_wait_time_list,
    title = f'Waiting time distribution with { ROUND } round of LOOK, average = { int(aly.get_average(look_wait_time_mean_list)) }',
    xlabel = 'waiting time',
    ylabel = 'count',
    filename = f'look_average',
    x_min = 0,
    x_max = max(look_wait_time_list),
    bins = max(look_wait_time_list) // 60
)

aly.get_histogram(
    data = edf_wait_time_list,
    title = f'Waiting time distribution with { ROUND } round of SCAN-EDF, average = { int(aly.get_average(edf_wait_time_mean_list)) }',
    xlabel = 'waiting time',
    ylabel = 'count',
    filename = f'scan_edf_average',
    x_min = 0,
    x_max = max(edf_wait_time_list),
    bins = max(look_wait_time_list) // 60
)
