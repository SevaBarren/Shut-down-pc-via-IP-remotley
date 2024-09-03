import argparse
import os

parser = argparse.ArgumentParser(description='Shut down multiple computers via IPv4')
parser.add_argument('-c', '--computers', required=True, nargs='+', help='List of hostnames or IP addresses of the computers to shut down')
parser.add_argument('-t', '--timeout', type=int, default=30, help='Number of seconds to wait before shutting down the computers')
parser.add_argument('-f', '--force', action='store_true', help='Force all applications to close when shutting down the computers')
parser.add_argument('-r', '--reboot', action='store_true', help='Reboot the computers instead of shutting them down')

args = parser.parse_args()

for computer in args.computers:
    command = 'shutdown /s' if not args.reboot else 'shutdown /r'
    if args.force:
        command += ' /f'
    command += f' /m \\\\{computer} /t {args.timeout}'
    os.system(command)
