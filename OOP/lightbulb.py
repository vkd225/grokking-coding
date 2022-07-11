# Design a class to handle lights on a dimmer where 5 is the minimum value of the dimmer (off)
# and 15 is the max value of the dimmer (all the way on)

# Implement a lightbulb class and a dimmer class that controls the lightbulbs based on wattage and output.


class LightBulb:
  def __init__(self, input_voltage):
    self.input_voltage = input_voltage

  def show_luminosity(self):
    return self.input_voltage

class Dimmer:
  def __init__(self, watt):
    self.watt = watt

  def output_luminosity(self):
    return self.watt


d = Dimmer(12)
print(d.output_luminosity())

