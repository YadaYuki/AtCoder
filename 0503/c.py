if __name__ == "__main__":
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    is_good_arr = [True for i in range(N)]
    for i in range(M):
        A,B = map(lambda i: int(i)-1,input().split())
        if H[A] > H[B]:
            is_good_arr[B] = False
        elif H[B] > H[A]:
            is_good_arr[A] = False
        else:
            is_good_arr[A],is_good_arr[B] = False,False
    print(sum(is_good_arr))