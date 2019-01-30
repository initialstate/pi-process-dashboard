import psutil
import time
import sys
from ISStreamer.Streamer import Streamer
from subprocess import PIPE, Popen

# --------- User Settings ---------
# Initial State settings
BUCKET_NAME = ":computer: Processes" 
BUCKET_KEY = "pr1208"
ACCESS_KEY = "PLACE YOUR INITIAL STATE ACCESS KEY HERE"
PROCESS_NAME = "PLACE THE NAME OF YOUR PROCESS HERE"
# Set the time between checks
MINUTES_BETWEEN_READS = 15
# ---------------------------------

def main():
	if len(sys.argv) != 2:
		print "Usage: " + sys.argv[0] + " <pid>"
		exit()
	pid = sys.argv[1]

	streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
	if psutil.pid_exists(int(pid)) == False:
		print "Error: That process doesn't exist! Exiting ..."
		exit()
	else:
		streamer.log(PROCESS_NAME,"Running")
		streamer.flush()

	while True:
		if psutil.pid_exists(int(pid)) == False:
			streamer.log(PROCESS_NAME,"Exited")
			streamer.flush()
			exit()
		else:
			streamer.log(PROCESS_NAME,"Running")
			process = Popen(['hostname', '-I'], stdout=PIPE)
			output, _error = process.communicate()
			streamer.log(PROCESS_NAME + " IP Address", output.rstrip())
			streamer.flush()
		time.sleep(60*MINUTES_BETWEEN_READS)

if __name__ == "__main__":
    main()