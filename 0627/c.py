def get_sum_arr(arr):
    sum_arr = [0]
    N = len(arr)
    for i in range(1,N+1):
        sum_arr.append(sum_arr[i-1] + arr[i-1])
    return sum_arr

def get_max_b(left_time,j,B_sum_arr):
    # [0,1,2,3,4,5]
    while B_sum_arr[j] > left_time and j > 0:
        j -= 1
    return j
def get_max_book_num(A,B,K):
    A_sum_arr,B_sum_arr = get_sum_arr(A),get_sum_arr(B)
    count,i,j = 0,0,len(B_sum_arr)-1
    for i in range(0,len(A_sum_arr)):
        if K < A_sum_arr[i]:
            break
        else:
            left_time = K - A_sum_arr[i]
            j = get_max_b(left_time,j,B_sum_arr)
        count = max(count,(i+j))
    return count
if __name__ == "__main__":
    N,M,K = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    print(get_max_book_num(A,B,K))
    
