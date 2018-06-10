"""Command-line interaction for the user"""

import argparse

import record
import plot
import blink_detector
import blink_detector_live
import file

def record_call(args):
    # Record signal
    if args.advanced:
        signal = record.record_advanced(args.duration, args.iterations, args.channels)
    else:
        signal = record.record(args.channels)

    # Save signal to file
    filename = file.save_signal(signal, args.name)
    print('Saved signal to: ' + filename)

def plot_call(args):
    signal = file.get_signal(args.name)
    print('signal loaded from file')
    plot.plot(signal)

def detect_call(args):
    signal = file.get_signal(args.name)
    print('signal loaded from file')
    blink_detector.detect(signal)

def detect_live_call(args):
    blink_detector_live.detect_live()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Record and plot signal from the OpenBCI Ganglion Board')
    subparsers = parser.add_subparsers()

    # Record subparser
    parser_record = subparsers.add_parser('record', help='Record the signal from the Ganglion board and save it to a JSON-file')
    parser_record.add_argument('-a', '--advanced', action='store_true')
    parser_record.add_argument('-c', '--channels', type=int, default=4)
    parser_record.add_argument('-d', '--duration', type=float, default=1)
    parser_record.add_argument('-i', '--iterations', type=int, default=1)
    parser_record.add_argument('-n', '--name', help='Filename of the JSON-file')
    parser_record.set_defaults(func=record_call)

    # Plot subparser
    parser_print = subparsers.add_parser('plot', help='Plot the signal of a file')
    parser_print.add_argument('name', help='Filename')
    parser_print.set_defaults(func=plot_call)

    # Blink detector subparser
    parser_print = subparsers.add_parser('blink_detector', help='Detect blinks in the signal of a file')
    parser_print.add_argument('name', help='Filename')
    parser_print.set_defaults(func=detect_call)
    
    # Blink detector live subparser
    parser_print = subparsers.add_parser('blink_detector_live', help='Stream the signal from the Ganglion board and detect blinks')
    parser_print.set_defaults(func=detect_live_call)
   
    args = parser.parse_args()
    args.func(args)