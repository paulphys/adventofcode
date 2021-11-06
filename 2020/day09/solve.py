def two_num_sum(arr, start, end, find):
    for i in range(start, end + 1):
        complement = find - arr[i]
        if complement != arr[i] and complement in arr[start:end + 1]:
            return True
    return False

def find_bad_index(arr):
    file = open('input.txt', 'r')
    for line in file:
        line = line.strip("\n")
        arr.append(int(line))
    for i in range(25, len(arr)):
        if not two_num_sum(arr, i - 25, i - 1, arr[i]):
            return i

def find_range(what, arr, end):
    for i in range(end + 1):
        curr_sum = arr[i]
        for j in range(i + 1, end + 1):
            curr_sum += arr[j]
            if curr_sum == what:
                return i, j

def part1():
    file = open('input.txt', 'r')
    arr = []
    for line in file:
        line = line.strip("\n")
        arr.append(int(line))
    for i in range(25, len(arr)):
        if not two_num_sum(arr, i - 25, i - 1, arr[i]):
            return arr[i]

def part2():
    arr = []
    idx_bad_num = find_bad_index(arr)
    range_arr = find_range(arr[idx_bad_num], arr, idx_bad_num)
    min_in_range = min(arr[range_arr[0]:range_arr[1]+1])
    max_in_range = max(arr[range_arr[0]:range_arr[1]+1])
    return min_in_range + max_in_range

print(part1())
print(part2())
