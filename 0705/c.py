def get_binaly_arr(num,digit):
    return list(bin(num)[2:].zfill(digit))

def get_droped_mat(mat,binaly_arr,direction):
    if direction == "H":# 行をdrop!
        return [mat[i] for i in range(len(mat)) if binaly_arr[i] != "0" ]
    elif direction == "W": # 列をdrop!
        return [[arr[i] for i in range(len(arr)) if binaly_arr[i] != "0" ] for arr in mat]
    else :
        print("INVALID DIRECTION!")

def count_black(mat):
    return sum([sum([1 for item in arr if item == "#"]) for arr in mat])
    
if __name__ == "__main__":
    H,W,K = list(map(int,input().split()))
    c = []
    for i in range(0,H):
        c.append(list(input()))

    H_pattern_num = 2 ** H
    W_pattern_num = 2 ** W
    count = 0
    ite_num = 0
    for i in range(0,H_pattern_num):
        for j in range(0,W_pattern_num):
            # バイナリ配列を生成
            H_binaly_arr = get_binaly_arr(i,H)
            W_binaly_arr = get_binaly_arr(j,W)

            mat_temp = c.copy()
            mat_temp = get_droped_mat(c,H_binaly_arr,direction="H")
            mat_temp = get_droped_mat(mat_temp,W_binaly_arr,direction="W")
            if K == count_black(mat_temp):
                count += 1
    print(count)


