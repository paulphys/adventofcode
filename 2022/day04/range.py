def range_overlap(range1, range2):
  """Whether range1 and range2 overlap."""
  x1, x2 = range1.start, range1.stop
  y1, y2 = range2.start, range2.stop
  return x1 <= y2 and y1 <= x2


a = range(20, 25)
b = range(23, 25)
print(range_overlap(a, b))



