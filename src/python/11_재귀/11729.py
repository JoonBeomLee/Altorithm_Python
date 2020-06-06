hanoi_num = int(input())
count = 0

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, to_pos)
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(from_pos, to_pos)
    hanoi(n - 1, aux_pos, to_pos, from_pos)
    
print(2 ** hanoi_num - 1)
hanoi(hanoi_num, 1, 3, 2)