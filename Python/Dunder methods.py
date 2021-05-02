class Color:
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue
 
 
  def __repr__(self):
    return "Color with RGB = ({red}, {green}, {blue})".format(red=self.red, green=self.green, blue=self.blue)
 
  def add(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_green = min(self.green + other.green, 255)
    new_blue = min(self.blue + other.blue, 255)
 
    return Color(new_red, new_green, new_blue)
 
red = Color(255, 0, 0)
blue = Color(0, 0, 255)
 
magenta = red.add(blue)
print(magenta)
# Prints "Color with RGB = (255, 0, 255)"