# practice

def largestRange(array):
    numbers = {x:0 for x in array}
    left = right = 0

    for number in array:
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1

            while left_count in numbers:
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1 #1

            while right_count in numbers:
                numbers[right_count] = 1
                right_count -= 1
            right_count -= 1 #0

            # right - left = current known range 
            # right_count - left_count = new range generated
            if (right - left) <= (right_count - left_count): # range comparision if left is less then accept the right one
                right = right_count
                left = left_count
    
    return [left, right]


largestRange([1, 4, 3, 2])