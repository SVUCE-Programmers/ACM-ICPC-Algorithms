def print_pairs(arr, sum):
  s = set()

  for item in arr:
    temp = sum - item
    if temp >= 0 and temp in s:
      print("Pair with the given sum is", item, "and", temp)
    s.add(item)


if __name__ == "__main__":
  arr = [1, 4, 45, 6, 10, 8]
  n = 16
  print_pairs(arr, n)
