class Rectangle:
   def __init__(self, width, height):
      self.width = width
      self.height = height
   
   def set_width(self, width):
      self.width = width
   
   def set_height(self, height):
      self.height = height
   
   def get_area(self):
      return self.width * self.height
   
   def get_perimeter(self):
      return 2 * (self.width + self.height)
   
   def get_diagonal(self):
      return (self.width**2 + self.height**2)**0.5
   
   def get_picture(self):
      if self.width > 50 or self.height > 50:
         return "Too big for picture."
      
      picture = ""
      for _ in range(self.height):
         picture = picture + "*"*self.width + "\n"
      return picture
   
   def get_amount_inside(self, other):
      return self.get_area() // other.get_area()
   
   def __repr__(self):
      return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
   def __init__(self, side):
      super().__init__(side, side)
   
   def set_side(self, side):
      self.height = side
      self.width = side
   
   def __repr__(self):
      return f"Square(side={self.width})"
