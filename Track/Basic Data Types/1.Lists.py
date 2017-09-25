if __name__ == '__main__':
    N = int(input())
    lists=[]
    for i in range(N):
        In=list(input().split())
        if (len(In)==3):
            exec("lists."+In[0]+"("+In[1]+","+In[2]+")")
        elif(len(In)==2):
            exec("lists."+In[0]+"("+In[1]+")")
        elif (In[0]=="print"):
            print(lists)
        else:
            exec("lists."+In[0]+"()")      
