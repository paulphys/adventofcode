with open("input.txt") as f:
    key_card, key_door = [int(x.strip()) for x in f]

def loop_size(key):
    subject_number = 7
    n = 1
    i = 0
    while True:
        n = (n * subject_number) % 20201227
        if n == key:
            return i+1
        i += 1

def encryptor(subject_number, loop_size):
    n = 1
    for i in range(loop_size):
        n = (n * subject_number) % 20201227
    return n

loop_size = loop_size(key_card)
enc_key = encryptor(key_door, loop_size)
print(enc_key)
