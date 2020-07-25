if __name__ == "__main__":
    X,N = list(map(int,input().split()))
    p = list(map(int,input().split()))
    if not X in p: # pが空配列・pにXが含まれない
        print(X)
    else:
        i = 1
        while True:
            if not (X - i) in p:
                print(X-i)
                break
            if not (X + i) in p:
                print(X+i)
                break
            i += 1