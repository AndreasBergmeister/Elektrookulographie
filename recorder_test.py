import json

from recorder import Recorder

recorder = Recorder(4)
recorder.start_recording()
output = recorder.get_signal()
# output = json.dumps(recorder.get_signal())

print(output)