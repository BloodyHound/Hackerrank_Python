if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lists=sorted(set(arr))
    print (lists[len(lists)-2])
