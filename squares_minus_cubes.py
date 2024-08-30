# solve x^2 - x^3 = 12

def square(n: float) -> float:
    return n * n

def cube(n: float) -> float:
    return n * n * n

def brute_force_ints(start: int, stop: int, step: int=1, target: int or None=None) -> None:
    for i in range(start, stop+1, step):
        diff = square(i) - cube(i)
        print(f'{i}^2 - {i}^3 = {diff}')
        if diff == target:
            return

if __name__ == '__main__':
    #brute_force_ints(1, 10)
    brute_force_ints(start=0, stop=-100, step=-1, target=12)
