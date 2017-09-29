def print_rangoli(size):
    for i in range(1,size+1):
        s='-'.join(chr(96+size-j) for j in range(i))
        print((s+s[::-1][1:]).center(size*4-3,'-'))
    for i in range(size-1,0,-1):
        s='-'.join(chr(96+size-j) for j in range(i))
        print((s+s[::-1][1:]).center(size*4-3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
