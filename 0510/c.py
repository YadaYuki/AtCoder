def get_items(arr,idx_arr):
    return [arr[i] for i in range(len(arr)) if i in idx_arr]

def to_binaly_arr(val,digit_num):
    return list(bin(val)[2:].zfill(digit_num))

def get_one_idx(binaly_arr):
    return [idx for idx in range(len(binaly_arr)) if binaly_arr[idx] == "1"]

def get_arr_sum(mat):
    if len(mat) == 0:
        return []
    else:
        sum_arr = []
        for j in range(len(mat[0])):
            sum_val = 0
            for i in range(len(mat)):
                sum_val += mat[i][j]
            sum_arr.append(sum_val)
        return sum_arr
def is_all_item_over_X(arr,X):
    return (not (False in [item>=X for item in arr])) and len(arr) > 0

if __name__ == "__main__":
    N,M,X = map(int,input().split())
    C,A = [],[]
    for i in range(N):
        input_val = list(map(int,input().split()))
        C.append(input_val[0])
        A.append(input_val[1:])
    min_price = float("inf")
    for i in range(0,2**N):
        idx_arr = get_one_idx(to_binaly_arr(i,N))
        arr_sum = (get_arr_sum(get_items(A,idx_arr)))
        if is_all_item_over_X(arr_sum,X) == True:
            min_price = min(min_price,sum(get_items(C,idx_arr)))
    if min_price == float("inf"):
        print(-1)
    else:
        print(min_price)