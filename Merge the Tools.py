def merge_the_tools(string, k):
    split_string=[]
    s=""
    for i in range(0,len(string),k):
        split_string.append(string[i:i+k])
    
    for i in split_string:
        set1=sorted(set(i),key=i.index)
        li1=list(set1)
        for j in li1:
            s+=j
        print(s)
        s=''   
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)