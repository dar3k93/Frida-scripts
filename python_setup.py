import frida
import sys

# get script name from the command line
scriptname = sys.argv[1]

# open script file
fd = open("scriptname", "r")

# get process to be instrumented from command line
procname = sys.argv[2]

# define callback function to receive and output messages
# received from server
def on_message(message, data):
   print(message)
   print(data)

# get connect to frida server through usb and attach to process
session = frida.get_usb_device().attach(procname)

# create script using script file opened above
script = session.create_script(fd.read())

# close file opened above
fd.close()

# setup callback using function defined above
script.on('message', on_message)

# load script into the process
script.load()

# Otherwise early functions, such as onCreate(), can’t be hooked correctly in case you are required to do so.
# device.resume()

# read from stdin to keep script running
sys.stdin.read()
