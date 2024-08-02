import sys

def round_array(n, m):

  round_arr = [(i % n) + 1 for i in range((m - 1) * n)]
  round_arr.append(1)

  intervals, path = [], []

  pos = 0

  while True:

    if pos == len(round_arr)-1:
      break

    intervals.append(round_arr[pos:(pos + m)])
    path.append(round_arr[pos])
    pos += m - 1

    if round_arr[pos:(pos + m)] in intervals:
      break

  return ''.join(map(str, path))


n = int(sys.argv[1])
m = int(sys.argv[2])

res = round_array(n, m)
print(res)