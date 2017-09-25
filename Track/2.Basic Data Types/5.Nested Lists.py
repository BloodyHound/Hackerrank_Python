if __name__ == '__main__':
    lists=[]
    x=int(input())
    for _ in range(x):
        name = input()
        score = float(input())
        lists.append([name,score])
    s=sorted(set([lists[i][1] for i in range(x)]))
    for name in sorted(x[0] for x in lists if x[1]==s[1]):
        print(name)
