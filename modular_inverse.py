def find_modular_inverse(base: int, modn: int) -> int:
    for i in range(1,100):
        x = (base * i) % modn
        if x == 1:
            return (i)

if __name__ == '__main__':
    base = int(input('base: '))
    modn = int(input('modn: '))
    print(find_modular_inverse(base, modn))
