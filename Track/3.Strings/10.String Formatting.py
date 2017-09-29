def print_formatted(number):
    max=len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(max)+str(oct(i)[2:]).rjust(max+1)+str(hex(i)[2:]).upper().rjust(max+1)+str(bin(i)[2:]).rjust(max+1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
