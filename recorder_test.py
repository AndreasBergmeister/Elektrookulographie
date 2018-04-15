import csv

from recorder import Recorder

recorder = Recorder(4)
recorder.start_recording()
output = recorder.get_signal()
# output = json.dumps(recorder.get_signal().__d)

all_rows = []
for i, channel in enumerate(output.channels):
    all_rows.append(['Channel ' + str(i+1)] + channel)

all_rows.append(['time'] + output.time)

if output.direction is not None:
    all_rows.append(['direction'].append(output.direction))

with open('records/record1.csv', 'w') as file:
    wr = csv.writer(file)
    wr.writerows(all_rows)
    # for row in all_rows:
    #     wr.writerow(row)  