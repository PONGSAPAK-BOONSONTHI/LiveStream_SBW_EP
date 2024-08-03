from argparse import ArgumentParser
from time import sleep
from datetime import timedelta

parser = ArgumentParser()
parser.add_argument("--minutes", "-m", type=int, required=False, default=10, help="minutes to set timer to")
parser.add_argument("--file", "-f", type=str, required=False, default="countdown.txt", help="file to write timer output to")
args = parser.parse_args()

minutes = args.minutes
output_file_name = args.file
seconds = minutes * 60

print("timer set for {} minutes".format(minutes))
print("sending output to {}".format(output_file_name))

try:
  output = open(output_file_name, "w")
  output.write(str(timedelta(seconds=seconds)))
  output.close()

  while seconds > 0:
    sleep(1)
    seconds -= 1
    output = open(output_file_name, "w")
    output.write(str(timedelta(seconds=seconds)))
    output.close()
except KeyboardInterrupt:
  output = open(output_file_name, "w")
  output.write(str(timedelta(seconds=0)))
  output.close()