def birthday(n, p, print_flag=False):
    number = 0
    probability = 1

    while(probability > p):
        number += 1
        probability *= (n - number)/ n
        if print_flag:
            print((number, probability))
    
    return (number, probability)

def check_answer(n, number, print_flag=False):
    probability = 1

    for numerator in range(n - number, n):
        probability *= numerator / n
        if print_flag:
            print((numerator, probability))

    return probability

def part_c(n, p, number, multiplier, print_flag=False):
    probability = check_answer(n, number)
    if print_flag:
        print((n, probability))

    while probability < p:
        n *= multiplier
        probability = check_answer(n, number)
        if print_flag:
            print((n, probability))
        
    return n

if __name__ == '__main__':
    n = 2600
    p = 1 - 0.01
    print_flag = True
    
    #print("Final answer:", birthday(n, p, print_flag))
    #print("Checked answer:", check_answer(n, 153, print_flag))
    print("Part C:", part_c(n, p, 50, 10, print_flag))
