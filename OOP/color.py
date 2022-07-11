class Color:
  def __init__(self):
    self.color_pallete = [[None for x in range(100) for y in range(100)]]
    self.undo_stack = []
    self.redo_stack = []

  def draw_pixel(self, x, y, color):
    if x <=100 and y<=100:
      prev_color = self.color_pallete[x][y]
      self.color_pallete[x][y] = color
      self.undo_stack.append([x, y, prev_color])
      self.redo_stack.clear()

    return

  def undo(self):
    if len(self.undo_stack > 0):
      undo_val = self.undo_stack.pop()
      x = undo_val[0]
      y = undo_val[1]
      prev_color = undo_val[2]

      current_color = self.color_pallete[x][y]
      self.color_pallete[x][y] = prev_color

      self.redo_stack.append([x, y, current_color])
    return


  def redo(self):
    if len(self.redo_stack > 0):
      redo_val = self.redo_stack.pop()
      x = redo_val[0]
      y = redo_val[1]
      next_color = redo_val[2]

      current_color = self.color_pallete[x][y]
      self.color_pallete[x][y] = next_color

      self.undo_stack([x,y, current_color])

    return


abc
def
123


