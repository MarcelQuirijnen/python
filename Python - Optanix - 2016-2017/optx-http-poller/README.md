# HTTP Poller MicroService Design

## Overview
The Optanix Platform utilizes low impact self throttling polling to acquire data from managed end devices.
Across the entire application stack we never ask more than one question to a single device at a time.
The data acquisition layer scales by asynchronously asking questions to as many devices as possible in parallel.
This design means that polling time theoretically takes only as long as the slowest device takes to respond to all
its questions to poll an entire network. No other platforms acquires data in our low impact methodology.

This low impact self throttling data acquisition design was first implemented for SNMP based polling and solidified in
the design of the SNMP Poller Service. Historically acquisition of data through HTTP requests has been implemented at
 small scale utilizing PLGN method tests. The PLGN polling method does not scale as it results in a linux process
 being executed for each polled entity of that method. With the proliferation of REST APIs exposed by vendors as a
 replacement for traditional SNMP there is a need to create a bulk asynchronous self throttling poller for acquiring
  data over HTTP.
  
## Run application
#####Go to Venv:<br>
`source venv3/bin/activate` <br><br>
#####Install requirements: <br>
`python3 cmd.py -r`<br> or<br>
`python3 cmd.py --requirements` <br><br>
#####Run application:<br>
`python3 cmd.py`<br> or<br> `python cmd.py -s`<br> or<br> `python3 cmd.py --serve`<br><br>
#####Run in debug mode:<br>
`python3 cmd.py -d`<br> or<br> `python cmd.py --debug`<br><br>
#####Run in special port:<br>
`python3 cmd.py -p [port]`<br> or<br> `python cmd.py --port=[port]`<br><br>
#####Run Unittests:<br>
`python3 cmd.py -t`<br><br>
