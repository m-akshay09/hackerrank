if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    set1= set(arr)
    li1= list(set1)
    li1.sort()
    print(li1[-2])