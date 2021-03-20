class Color: 
  def __add__(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_green = min(self.green + other.green, 255)
    new_blue = min(self.blue + other.blue, 255)
 
    return Color(new_red, new_green, new_blue)
	
red = Color(255, 0, 0)
green = Color(0, 255, 0)
blue = Color(0, 0, 255)

# Color with RGB: (255, 0, 255)
magenta = red + blue
 
# Color with RGB: (0, 255, 255)
cyan = green + blue
 
# Color with RGB: (255, 255, 0)
yellow = red + green
 
# Color with RGB: (255, 255, 255)
white = red + green + blue