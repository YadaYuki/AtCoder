import math

def get_theta(H,M):
    M_angle = 6 * M
    H_angle = 30 * H + 0.5 * M
    return (M_angle - H_angle) * math.pi / 180 

def calculate_vector_distance(a,b,theta):
    return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(theta))

if __name__ == "__main__":
    A,B,H,M = map(int,input().split())
    print(calculate_vector_distance(A,B,get_theta(H,M)))
