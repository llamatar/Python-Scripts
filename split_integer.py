# youtu.be/ZlhgBWFgeNY

def split_integer(number, groups):
    quotient, remainder = divmod(number, groups)
    return [quotient] * (groups-remainder) + [quotient+1] * remainder

tests = [
    split_integer(7, 3) == [2,2,3]
    , split_integer(3, 5) == [0,0,1,1,1]
    , split_integer(10, 4) == [2,2,3,3]
]

if all(tests):
    print('All tests passed')
else:
    failed_tests = [i for i, test in enumerate(tests) if not test]
    print(f'Tests failed: {failed_tests}')


