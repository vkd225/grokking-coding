# Design a class to handle lights on a dimmer where 5 is the minimum value of the dimmer (off)
# and 15 is the max value of the dimmer (all the way on)

# Implement a lightbulb class and a dimmer class that controls the lightbulbs based on wattage and output.


class LightBulb:
  def __init__(self, input_voltage):
    self.input_voltage = input_voltage

  def show_luminosity(self):
    luminosity = 0
    if self.input_voltage < 5 and self.input_voltage > 15:
      return luminosity

    elif self.input_voltage >= 5 and self.input_voltage <= 15:
      luminosity = self.input_voltage/2
      return luminosity

class Dimmer:
  def __init__(self, watt):
    self.watt = watt

  def output_luminosity(self):
    return self.watt


d = LightBulb(12)
print(d.show_luminosity())




# Dimmer switch's

MIN_LEVEL = 5
MAX_LEVEL = 15


# Dimmer Level | 5 Watt | 10 Watt | 20 Watt
# 5            | 0      | 0       | 0
# 15           | 5      | 10      | 20 (lumens)
# 10           | 2.5    | 5       | 10

# y = mx + c
# 0 = m*0
# 2.5 = m*10
# 5 = m*15



class Bulb:
  def __init__(self, watt):
    # super().__init__(watt)
    self.watt = watt


class DimmerSwitch:
  def __init__(self, dimmer_level):
    self.dimmer_level = dimmer_level

  def calculate_brightness(self, watt):
    """
      Method calculates the brightness of the bulb
      input: dimmer_level
      output: brightness
    """
    print (self.dimmer_level, watt)
    if self.dimmer_level <= 5:
      return 0

    elif self.dimmer_level > 5 and self.dimmer_level < 15:
      return self.dimmer_level/ watt
    else:
      return watt


dimmer_switch=DimmerSwitch(10)
bulb1=Bulb(10)
bulb2=Bulb(5)
bulb3=Bulb(20)

print (dimmer_switch.calculate_brightness(bulb1.watt))
print (dimmer_switch.calculate_brightness(bulb2.watt))
print (dimmer_switch.calculate_brightness(bulb3.watt))




