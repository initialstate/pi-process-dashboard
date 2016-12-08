import psutil
import time
import sys
from ISStreamer.Streamer import Streamer

# --------- User Settings ---------
# Initial State settings
BUCKET_NAME = ":computer: Processes" 
BUCKET_KEY = "pr1208"
ACCESS_KEY = "PLACE YOUR INITIAL STATE ACCESS KEY HERE"
PROCESS_NAME = "PLACE THE NAME OF YOUR PROCESS HERE"
# Set the time to wait until you are sure reboot is complete and network connections are restored (i.e. power outage)
MINUTES_DELAY = 5
# ---------------------------------

def main():
	# Wait for ntpd to run for sync of the clock
	found_ntpd = False
	cnt = 0
	while found_ntpd == False:
		for proc in psutil.process_iter():
			if proc.name() == "ntpd":
				found_ntpd = True 
		cnt += 1
		if cnt == 60: # assume that ntpd has already run if not found in 60 seconds
			found_ntpd=True
		time.sleep(1)

	time.sleep(60*MINUTES_DELAY)
	streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
	streamer.log(PROCESS_NAME,"Exited")
	streamer.flush()

if __name__ == "__main__":
    main()