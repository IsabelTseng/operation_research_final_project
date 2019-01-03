import input_generator as gen
#import algorithms.scan_edf
import analytics as aly

for i in range(10):
    input = gen.get_input()
    count = [0 for i in range(3600 // 5)]
    for x in input:
        count[(x['timestamp'] // 5) - 1] += 1

    aly.get_histogram(count, title = 'request per 5 seconds', xlabel = 'request', ylabel = 'count', filename = f'{ i + 1 }')