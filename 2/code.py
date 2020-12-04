def check_passwords():
  data = open('data.txt').read()
  array = data.splitlines()

  number_of_good_passwords = 0
  counter = 0
  numbers_list = []
  lower_bound_list = []
  upper_bound_list = []
  char_list = []
  password_list = []

  for i in array:
    array_without_colon = i.replace(':', '')
    split = array_without_colon.split(' ')
    numbers_list.append(split[0])
    char_list.append(split[1])
    password_list.append(split[2])

  for number in numbers_list:
    lower_bound_list.append(int(number.partition("-")[0]))
    upper_bound_list.append(int(number.partition("-")[2]))

  for password in password_list:
    occurrences = 0
    for letter in password:
      if letter == char_list[counter]:
        occurrences += 1
    if upper_bound_list[counter] >= occurrences >= lower_bound_list[counter]:
      number_of_good_passwords += 1
    counter += 1

  print(number_of_good_passwords)


def check_passwords2():
  data = open('data.txt').read()
  array = data.splitlines()

  number_of_good_passwords = 0
  counter = 0
  numbers_list = []
  first_index_list = []
  second_index_list = []
  char_list = []
  password_list = []

  for i in array:
    array_without_colon = i.replace(':', '')
    split = array_without_colon.split(' ')
    numbers_list.append(split[0])
    char_list.append(split[1])
    password_list.append(split[2])

  for number in numbers_list:
    first_index_list.append(int(number.partition("-")[0]) - 1)
    second_index_list.append(int(number.partition("-")[2]) - 1)

  for password in password_list:
    is_correct = False
    if password[first_index_list[counter]] == char_list[counter] or password[second_index_list[counter]] == char_list[counter]:
      is_correct = True
    if password[first_index_list[counter]] == char_list[counter] and password[second_index_list[counter]] == char_list[counter]:
      is_correct = False

    if is_correct:
      number_of_good_passwords += 1
    counter += 1

  print(number_of_good_passwords)


check_passwords()
check_passwords2()
