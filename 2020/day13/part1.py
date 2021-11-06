def main():
    with open('input.txt','r') as file:
        timestamp = int(file.readline().strip())
        bus_IDs = [int(i) for i in file.readline().strip().split(",") if i != 'x']
        
    from_timestamp = [(i,(i - (timestamp % i))) for i in bus_IDs]
    from_timestamp_sorted = sorted(from_timestamp,key=lambda i:i[1])
    closest_bus = from_timestamp_sorted[0]
    print(closest_bus[0] * closest_bus[1])

if __name__ == "__main__":
    main()

