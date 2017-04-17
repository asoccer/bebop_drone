
import sys
import os

import code
import readline
import rlcompleter
#Above from Drone

from getch import getch, pause
op = "\t\tWelcome to Bebop Drone Controller! Commands will be sent via single stroke\n\t\t\t\tConnection to the drone will now begin\n"

#choice = '1 - Emergency take off\n2 - Take off and Hover\n3 - Land\n'
#print op,choice

#key = getch()
#print 'You have selected' + key + '. The key will now be sent to the drone'

print('Searching for Drone...')
#Find drone on network
from Bybop_Discovery import Discovery, DeviceID
discovery = Discovery(DeviceID.ALL)
devices = discovery.get_devices()

#Print the matched devices found on the network
if not devices:
	print 'shit didnt connect'
	sys.exit(1)
print 'The following devices have been found on the network'
for x in devices:
	print x,devices[x]

device = devices.itervalues().next()
#connect to drone
from Bybop_Device import create_and_connect
d2c_port = 54321 # input UDP port
controller_type = 'Type of Controller'
controller_name = 'Application Name'
drone = create_and_connect(device, d2c_port, controller_type, controller_name)

#confirm connection by checking battery level
battery_level = drone.get_battery()
for x in battery:
	print x,battery_level[x]
pause('The Program will now attempt to launch the drone, press enter to begin take off')
#Attempt to take off

drone.take_off()
try:
    flying_state = drone.get_state(copy=False).get_value('ardrone3.PilotingState.FlyingStateChanged')['state']
except:
    flying_state = None
while flying_state != 2: # 2 is hovering
    drone.wait_for('ardrone3.PilotingState.FlyingStateChanged')
    try:
        flying_state = drone.get_state(copy=False).get_value('ardrone3.PilotingState.FlyingStateChanged')['state']
    except:
        flying_state = Nonetake

pause('Next the drone will attempt to land, press enter to begin landing sequence')

drone.land()

pause('Confirm landing. Drone will take off again')

drone.take_off()
try:
    flying_state = drone.get_state(copy=False).get_value('ardrone3.PilotingState.FlyingStateChanged')['state']
except:
    flying_state = None
while flying_state != 2: # 2 is hovering
    drone.wait_for('ardrone3.PilotingState.FlyingStateChanged')
    try:
        flying_state = drone.get_state(copy=False).get_value('ardrone3.PilotingState.FlyingStateChanged')['state']
    except:
        flying_state = Nonetake
pause('Roll will be attemtped')
roll_drone = drone.send_data('ardrone3.Piloting.roll',50)
pause('Wait for drone to complete roll and then send -50 back to it')
roll_drone = drone.send_data('ardrone3.Piloting.roll',-50)
pause('The next command is an emergency landing, prepare your butts for it!')
drone.emergency()
pause('Confirm emergency landing and then terminate the connection')
drone.stop()
pause('Confirm Drone stopped')
