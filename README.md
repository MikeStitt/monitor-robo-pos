# monitor-robo-pos

A python script to monitor an FRC robot position. 
See https://docs.wpilib.org/en/stable/docs/software/examples-tutorials/wpilib-examples.html
StateSpaceDriveSimulation

## Setup

python3.10 from https://www.python.org/downloads/

```shell
cd monitor-robo-pos
python -m pip install -r .\requirements.txt
```

## Running

Use the "2022 WPILib VS Code", "WPILib Command Palette" button, "Create a new project" option 
to install the example StateSpaceDriveSimulation.
We use the Java version. But we think that the C++ version would also work.

Again, in "2022 WPILib VS Code", use the "Simulate Robot Code" option to 
launch "Robot Simulation"

A pop-up appears:

- [ ] [[Pick extensions to run] [1 Selected]] [OK]
- [ ] Sim DriverStation
- [X] Sim GUI

Select OK in the above pop-up.

The "Robot Simulation" appears.

Plug a wired Xbox Controller into a USB port on the PC.

In the "Robot Simulation", drag the "System Joysticks", "0: Xbox Controller" to the 
"Joysticks", "Joysticks[0]" text.

In "Joysticks[0]", "0: Xbox Controller", [x] Map gamepad is checked.

Now the "Joysticks[0]", "0: Xbox Controller" fields should change as one uses the Xbox controller.

In "Robot State", Select "Teleoperated".

Now the "NetworkTables", "SmartDashboard", "Field", "Robot", list of 3 doubles that
represent X, Y, heading orientation of the simulated robot should have the significant
digits to the left of the decimal point respond to Xbox controller joystick commands.

Also "NetworkTables", "LiveWindow", "Ungrouped", "DifferentialDrive[1]": 
"Left Motor Speed" and "Right Motor Speed" show the changes in motor speeds in
response to Xbox controller joystick commands.

To run this, monitor-robo-pos.py, program, use a Windows PowerShell or Windows
Command Prompt window:

```shell
cd monitor-robo-pos.py
python monitor-robo-pos.py
```

A window real-time matplotlib figure should appear. Use the Xbox controller
to drive the simulated robot. The real-time figure will show 
the position and heading of the simulated robot.

