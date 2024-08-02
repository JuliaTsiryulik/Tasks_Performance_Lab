import sys

def read_numbers(filename):
  with open(filename, 'r') as file:
    return [int(line.strip()) for line in file]

def calculate_min_moves(nums):
  nums.sort()
  n = len(nums)
  
  #Если четное количество элементов, берем медиану как целое число
  median = nums[n // 2] if n % 2 != 0 else (nums[n // 2 - 1] + nums[n // 2]) // 2
  
  total_moves = sum(abs(num - median) for num in nums)
  
  return total_moves


filename = sys.argv[1]

try:
  nums = read_numbers(filename)
  moves = calculate_min_moves(nums)
  print(moves)
  
except Exception as e:
  print(f"Ошибка при обработке файла: {e}")
  sys.exit(1)

