min_num = int(input("Enter The Minimum Number :"))
max_num = int(input("Enter The Maximum Number :"))
disabled_list = input("Enter The Disabled List :")

test_number = int(input("Enter The Test Number :"))

flag = True

while flag:
    if min_num >= test_number or max_num <= test_number:
        print('invalid output')
        flag = False
    elif str(test_number) in disabled_list:
        test_number = test_number+1
    else:
        print(test_number, 'is Valid')
        flag = False
