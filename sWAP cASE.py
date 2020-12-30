def swap_case(s):
    list1=list(s)
    list2=[]
    string=''
    for i in list1:
        if i.isupper():
            x=i.lower()
            list2.append(x)
        elif i.islower():
            x=i.upper()
            list2.append(x)
        else:
            list2.append(i)
    
    for i in list2:
        string=string+i
                
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)