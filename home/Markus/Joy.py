# start the service
joystick = Runtime.start("joystick","Joystick")
print(joystick.getControllers())
python.subscribe("joystick","publishJoystickInput")
joystick.setController(1)


def onJoystickInput(data):
  print(data)
  if (data.id== "H" and data.value == 1.0):
    print("Hello")
