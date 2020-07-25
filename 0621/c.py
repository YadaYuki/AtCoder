def get_digit_num(num):
    num -= 1
    if num < 26:
        return 1,num
    prev_last,digit_num = 25,2
    while True:
        if (prev_last < num < prev_last + (26 ** digit_num) + 1):
            num -= prev_last + 1
            break
        prev_last = prev_last + (26 ** digit_num)
        digit_num += 1
    return digit_num,num

def get_word(digit_num,num_n_digits):
    alpha_arr = [(chr(ord("a") + i)) for i in range(0,26)]
    idx_arr = [0] * digit_num
    for i in range(digit_num-1,-1,-1):
        idx_arr[i] = num_n_digits % 26
        num_n_digits = int(num_n_digits / 26)
    return "".join([alpha_arr[idx_arr[i]] for i in range(digit_num)])

    
if __name__ == "__main__":
    num = int(input())
    digit_num,num_n_digits = get_digit_num(num)
    print(get_word(digit_num,num_n_digits))