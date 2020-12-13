def main():
    filename = 'input.txt'
    with open(filename,'r') as infile:
        timestamp = int(infile.readline().strip())
        bus_IDs = [int(i) for i in infile.readline().strip().split(",") if i != 'x']

    print(f"Timestamp: {timestamp}")
    print(f"Bus IDs: {bus_IDs}")
    from_timestamp = [(i,(i - (timestamp % i))) for i in bus_IDs]
    from_timestamp_sorted = sorted(from_timestamp,key=lambda i:i[1])
    print(f"from_timestamp_sorted : {from_timestamp_sorted}")
    closest_bus = from_timestamp_sorted[0]
    print(f"Closest Bus: {closest_bus}")
    print(closest_bus[0] * closest_bus[1])

if __name__ == "__main__":
    main()
