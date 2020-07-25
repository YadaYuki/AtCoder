if __name__ == "__main__":
    A,B = input().split(" ")
    A = int(A)
    B = float(B)
    B = int(B * 100 + 0.5) # * 100 で生じる誤差を修正
    A *= B
    print(int(A/100))
