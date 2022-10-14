import sys


# create read_file function to read the numbers in the file
# add numbers in a list as integers
# return the list


def read_file(filename):
    try:
        numbers_file = open(filename, 'r')
    except (FileNotFoundError, IndexError):
        print('File not found')
        sys.exit(0)
    numbers = []
    lines = numbers_file.readlines()
    for line in lines:
        list = line.split()
        for item in list:
            numbers.append(int(item))
    return numbers


# create function to filter odd and even numbers
# odd numbers are True, even numbers are False
# create a temporary list and store the even and odd numbers in it
# filter numbers and return the temp list


def filter_odd_or_even(numbers, odd):
    temp_list = []
    if odd:
        for item in numbers:
            if item % 2 != 0:
                temp_list.append(item)
        return temp_list
    if not odd:
        for item in numbers:
            if item % 2 == 0:
                temp_list.append(item)
        return temp_list

# create reversed bubble sort -> comparing two numbers
# swap the values at the end


def reversed_bubble_sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


# create and call the main functions
# even and odd numbers should be read from the files
# combine two lists
# call the functions
# print the updated list


def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    number_list_1 = read_file(file1)
    number_list_2 = read_file(file2)
    number_list_1 = filter_odd_or_even(number_list_1, True)
    number_list_2 = filter_odd_or_even(number_list_2, False)
    sorted_numbers = number_list_1 + number_list_2
    reversed_bubble_sort(sorted_numbers)
    print(list(sorted_numbers))


if __name__ == "__main__":
    main()
