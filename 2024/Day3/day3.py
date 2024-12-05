import re


def read_data(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            yield line

pattern = r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))'

count = True
res = 0
for line in read_data('day3.input'):
    for match in re.finditer(pattern, line):
        full_match = match.group(1)
        if full_match.startswith('mul'):
            if count:
                num1, num2 = match.groups()[1:]
                res += int(num1) * int(num2)
        # print(f"Pair found: {num1} * {num2} = {int(num1) * int(num2)}")
        elif full_match.startswith('don'):
            count = False
        else:
            count = True        
print(res)
