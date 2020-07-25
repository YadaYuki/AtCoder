import sys
def gen_abs_arr(N):
    arr = [0]
    for i in range(1,N):
        arr.append(int((i+1)/2))
    return arr
if __name__=="__main__":
    X,N = [int(i) for i in input().split(" ")]
    p = [int(i) for i in input().split(" ")]
    if not (X in p):
        print(X)
        sys.exit()
    diff_arr = [item-X for item in p]
    diff_abs_arr = [abs(item) for item in diff_arr]
    diff_abs_arr.sort()

    abs_arr = gen_abs_arr(N)
    min_val = None
    
    for i in range(1,N):
        if (diff_abs_arr[i] != abs_arr[i]): # 差の絶対値が同じ数値の組み合わせは2つある。その2つが存在しない場合
            min_val = diff_abs_arr[i]
            if min_val in diff_arr: # 差の絶対値が同じ数値の組み合わせの中でも小さいほうが答えである。
                min_val = min_val * (-1)
            break
            
    if not min_val:
        if N % 2 == 0:
            min_val = diff_abs_arr[-1]
            if min_val in diff_arr: # 差の絶対値が同じ数値の組み合わせの中でも小さいほうが答えである。
                min_val = min_val * (-1)
        else :
            min_val = (diff_abs_arr[-1] + 1) * (-1)
    print(min_val+X)


    