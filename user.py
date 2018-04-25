import argparse

import record as r
import plot as p
import file


def record(args):
    # Record Signal
    if args.advanced:
        signal = r.record_advanced(args.duration, args.iterations, args.channels)
    else:
        signal = r.record(args.channels)
    print('Finished recording')

    # Save Signal to file
    filename = file.save_signal(signal, args.name)
    print('Saved signal to: ' + filename)    


def plot(args):
    signal = file.get_signal(args.name)
    print('Signal loaded from file')
    p.plot_channels(signal)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Record and plot signal from the OpenBCI Ganglion Board')
    subparsers = parser.add_subparsers()

    # Record Subparser
    parser_record = subparsers.add_parser('record', help='Record the Signal and save it to a json-file')
    parser_record.add_argument('-a', '--advanced', action='store_true')
    parser_record.add_argument('-c', '--channels', type=int, default=4)
    parser_record.add_argument('-d', '--duration', type=float, default=1)
    parser_record.add_argument('-i', '--iterations', type=int, default=1)
    parser_record.add_argument('-n', '--name', help='Filename of the json-file')
    parser_record.set_defaults(func=record)

    # Plot Subparser
    parser_print = subparsers.add_parser('plot', help='Plots the Signal of a file')
    parser_print.add_argument('name', help='Filename')
    parser_print.set_defaults(func=plot)
    
   
    args = parser.parse_args()
    args.func(args)