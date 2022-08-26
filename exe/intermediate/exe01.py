def max_min(data):
  min_num = data[0]
  max_num = data[0]
  for num in data:
    if num> min_num:
      min_num = num
    elif num< max_num:
        max_num = num
  return min_num, max_num

list1 = [0, 10, 15, 40, -5, 42, 17, 28, 75]

result = max_min(list1)

print(result)
