# temp-monitor
Temperature monitor using Python3 and Raspberry Pi Zero

`temp.py` records the temperature from a BMP180 and timestamps it, then pushes it to a CSV file.
`plot.py` plots the data on a (time,temp) axis. Since the Pi-0 is running headless it has no front end and so matplotlib needs to render with 'Agg'.
