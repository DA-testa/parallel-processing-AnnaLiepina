# python3
import math

def parallel_processing(n, m, data):
    output = []
    time_counter = 0
    j = 0

    while time_counter < math.ceil(m/n):
        for i in range(n):
            if  j >= m:
                break
            if time_counter == 0:
                output.append((i, 0))
            else:
                output.append((i, time_counter + data[j - 2] - 1))
            j += 1
        time_counter += 1

    return output

def main():
    
    first_line = list(map(int, input().split()))
    
    n = first_line[0]
    m = first_line[1]
    
    data = list(map(int, input().split()))
    
    result = parallel_processing(n, m, data)
    
    
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
