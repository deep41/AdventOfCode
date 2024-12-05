counter = 0
accepted_strings = {
  'one' : 1, 
  'two' : 2,
  'three' : 3,
  'four' : 4,
  'five' : 5,
  'six' : 6, 
  'seven' : 7, 
  'eight' : 8,
  'nine' : 9,
  '0' : 0,
  '1' : 1,
  '2' : 2,
  '3' : 3,
  '4' : 4,
  '5' : 5,
  '6' : 6,
  '7' : 7,
  '8' : 8,
  '9' : 9,
}
string_keys = list(accepted_strings.keys())[:9]
num_keys = list(accepted_strings.keys())[9:]


with open('day1/input.file', 'r') as file:
  for line in file:
    first, last = -1, -1
    first_pos = None
    last_pos = None
    for pos in range(len(line)):
      if line[pos] in num_keys:
        if (first == -1):
          first = line[pos]
          first_pos = pos
        last = line[pos]
        last_pos = pos

    smallString1 = line[:first_pos]
    index = 0
    # print(f'--> {smallString1}')
    while len(smallString1) > 2 and index < len(string_keys):
      num_index = smallString1.find(string_keys[index])
      if num_index != -1:
        first = string_keys[index]
        smallString1 = smallString1[:num_index + 1]
        # print(f'--> {smallString1}')

      index += 1

    smallString2 = line[last_pos + 1:]
    index = 0
    # print(f'--> {smallString2}')
    while len(smallString2) > 2 and index < len(string_keys):
      num_index = smallString2.rfind(string_keys[index])
      if num_index != -1:
        last = string_keys[index]
        smallString2 = smallString2[num_index + len(string_keys[index]) - 1:]
        # print(f'--> {smallString2}')
      index += 1
    number = accepted_strings[first] * 10 + accepted_strings[last]
    counter += number

print(counter)