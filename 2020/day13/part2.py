from functools import reduce
import math

def get_inverse(N_i,n_i):
    while N_i > n_i:
        N_i = int(N_i % n_i)
    x_i = 0
    while int((N_i * x_i) % n_i) != 1:
        x_i +=1
    return int(x_i)

def main():
    filename = 'input.txt'
    with open(filename,'r') as infile:
        timestamp = int(infile.readline().strip())
        bus_IDs = [(int(i),(int(i) - index)%(int(i)),index)
                for index,i in enumerate(
                    infile.readline().strip().split(",")) if i != 'x']

    N = reduce(lambda x,y: x*y,[bus[0] for bus in bus_IDs])
    x = 0
    for n_i, b_i, i in bus_IDs:
        N_i = N // n_i
        x_i = get_inverse(N_i, n_i)
        x += b_i * x_i * N_i
    print(int(x%N))

if __name__ == "__main__":
    main()
