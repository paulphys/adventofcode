from math import prod

hex2bin = str.maketrans({
               "0":"0000","1":"0001","2":"0010","3":"0011",
               "4":"0100","5":"0101","6":"0110","7":"0111",
               "8":"1000", "9":"1001","A":"1010","B":"1011",
               "C":"1100", "D":"1101", "E":"1110","F":"1111"})
transmission = open("input.txt").read().translate(hex2bin)
versions = 0

def decode_cmd(data, i, val):
    length = packets = 0
    if data[i] == '0':
        length = int(data[i+1:i+16], 2)
        commands, i = decode_length(data, i + 16, length)
    else:
        packets = int(data[i+1:i+12], 2)
        commands, i = decode_count(data, i + 12, packets)
    match val:
        case 0: return sum(commands), i
        case 1: return prod(commands), i
        case 2: return min(commands), i
        case 3: return max(commands), i
        case 5: return int(commands[0] > commands[1]), i
        case 6: return int(commands[0] < commands[1]), i
        case 7: return int(commands[0] == commands[1]), i

def decode(data,i=0):
    global versions
    versions += int(data[i:i+3], 2)
    type_id = int(data[i+3:i+6], 2)
    if type_id == 4: return decode_keys(data, i + 6)
    else: return decode_cmd(data, i + 6, type_id)

def decode_keys(data, i):
    value = ''
    while True:
        value += data[i+1:i+5]
        if data[i] == '0':
            return int(value, 2), i + 5
        i += 5

def decode_length(data, i, length):
    end = i + length
    values = []
    while i < end:
        value, i = decode(data, i)
        values.append(value)
    return values, i

def decode_count(data, i, count):
    packets = 0
    values = []
    while packets < count:
        value, i = decode(data, i)
        values.append(value)
        packets += 1
    return values, i

print(f"Part 2: {decode(transmission)[0]}")
print(f"Part 1: {versions}")
