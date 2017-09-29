def merge_the_tools(string, k):
    x=[]
    for i in range(0,len(string),k):
        for j in range(i,i+k):
            if(string[j] not in x):
                x.append(string[j])
        print (''.join(x))
        x=[]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
