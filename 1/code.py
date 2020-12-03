def calculate_sum():
  data = open('data.txt').read()
  array = data.splitlines()
  for i in array:
    for j in array:
      if int(i) + int(j) == 2020:
        solution = int(i) * int(j)
  print(solution)


def calculate_sum2():
  data = open('data.txt').read()
  array = data.splitlines()
  for i in array:
    for j in array:
      for k in array:
        if int(i) + int(j) + int(k) == 2020:
          solution = int(i) * int(j) * int(k)
  print(solution)


calculate_sum()
calculate_sum2()
