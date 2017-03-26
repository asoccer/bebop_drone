# GMU ECE 465 Bebop Drone Repo 
bebop repo of my code

## How it works

Windows hosts the "Server.py" file and from cmd line

   python server.py
   
Ubuntu VM then sends client packets to the host machine (windows)    

Visual Example

![Alt Text](https://github.com/asoccer/bebop_drone/blob/master/images/ss4TSk8.gif)

Todo list

# For Client (Python Pref)
   1. Create a Menu that is able to handle sending information to the Server without the press of "enter"
      * Most likely will require a combination of while and input with an on-screen page that says what does what
   2. Supports the following commands
      * Emergency Power-off mode
      * Take off and hover
      * Land
      * Adjust roll (L/R)
      * Pitch (F/B tilt)
      * Gaz (Vertical Speed)
      * yaw (Angular Speed)
   3. The Client DOES NOT HANDLE EXCEPTIONS. Therefore it's fair game on what is sent *to* the server.
   
# For Server (NodeJs or Python)
   1. Establish connection between drone and client
   2. Build a dictionary of "acceptable" messages that are coming from the client. If it isn't in the allowed commands send "wrong command" back to the client
   3. If the command is correct response with the sent command 
   4. Set methods that can take a command from the client and push the identical message to the drone (PREF JS)



