from utils.input_generator import get_input
from utils.elevator import Elevator
from algorithms.look import look
from algorithms.scan_edf import scan_edf
import utils.analytics as aly
from itertools import groupby

elevator1 = Elevator(look)
elevator2 = Elevator(scan_edf)

look_wait_time_list = []
edf_wait_time_list = []
look_wait_time_mean_list = []
edf_wait_time_mean_list = []
look_bias_list = []
edf_bias_list = []

ROUND = 100

for i in range(ROUND):
    input_data = get_input()
    elevator1.serve(input_data)
    elevator2.serve(input_data)

    look_wait_time = [x['waiting_time'] for x in elevator1.output_data]
    look_wait_time_list += look_wait_time
    look_wait_time_mean = int(aly.get_average(look_wait_time))
    look_wait_time_mean_list.append(look_wait_time_mean)
    look_bias_list += [x['bias'] for x in elevator1.output_data]

    edf_wait_time = [x['waiting_time'] for x in elevator2.output_data]
    edf_wait_time_list += edf_wait_time
    edf_wait_time_mean = int(aly.get_average(edf_wait_time))
    edf_wait_time_mean_list.append(edf_wait_time_mean)
    edf_bias_list += [x['bias'] for x in elevator2.output_data]

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
max_bias = max([max(edf_bias_list), max(look_bias_list)])
min_bias = min([min(edf_bias_list), min(look_bias_list)])
bin_tags = [f'{ 5 * i } ~ {5 * (i + 1)}' for i in sorted(list(set(range(min_bias // 300, max_bias // 300 + 1))))]

look_bias_list = [x // 300 for x in look_bias_list]
edf_bias_list = [x // 300 for x in edf_bias_list]

look_bias_5min_list = list({ x: look_bias_list.count(x) for x in look_bias_list }.values())
look_bias_5min_list.reverse()
edf_bias_5min_list = list({ x: edf_bias_list.count(x) for x in edf_bias_list }.values())
edf_bias_5min_list.reverse()

size_diff = len(look_bias_5min_list) - len(edf_bias_5min_list)
if size_diff > 0:
    edf_bias_5min_list += [0] * size_diff
else:
    look_bias_5min_list += [0] * size_diff

aly.get_multibarhplot(
    data1 = look_bias_5min_list,
    data2 = edf_bias_5min_list,
    title = 'Bias between requesting waiting time and actual waiting time',
    xlabel = 'count',
    ylabel = 'bias',
    filename = 'bias_distribution',
    bin_tags = bin_tags
)
