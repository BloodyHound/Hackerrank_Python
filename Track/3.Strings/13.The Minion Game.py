def minion_game(string):
    Stuart=0
    Kevin=0
    for i in range(len(string)):
        if(string[i] in 'AIUEO'):
            Kevin+=len(string)-i
        else:
            Stuart+=len(string)-i
    if(Stuart>Kevin):
        print("Stuart",str(Stuart))
    elif(Stuart<Kevin):
        print("Kevin",str(Kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
