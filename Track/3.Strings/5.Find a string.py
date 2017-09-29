def count_substring(string, sub_string):
    import re
    x=re.findall('(?='+sub_string+')',string)
    return len(x)
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
