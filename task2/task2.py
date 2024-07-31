def read_numbers(filename):
  with open(filename, 'r') as file:
    return [list(map(int, line.strip().split())) for line in file]

def point_position(center, radius, points):

  x = points[0] - center[0]
  y = points[1] - center[1]

  if x**2 + y**2 == radius**2:
    return 0

  elif x**2 + y**2 < radius**2: 
    return 1
    
  else:
    return 2

def main(file_1, file_2):

  try:
    circle_coors = read_numbers(file_1)
    points_coors = read_numbers(file_2)

    center_coors = circle_coors[0]
    radius = circle_coors[1][0]

    for nums in points_coors:
      res = point_position(center_coors, radius, nums)
      print(res)
  
  except Exception as e:
    print(f"Ошибка при обработке файла: {e}")

main('circle.txt', 'dot.txt')