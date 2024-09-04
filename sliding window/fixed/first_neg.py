from typing import List

def get_first_neg_array(arr: List[int], k: int):
    i = 0
    j = 0
    neg_arr: List[int] = []
    result: List[int] = []

    while j < len(arr):
        # Add the current element to the list of negative numbers if it's negative
        if arr[j] < 0:
            neg_arr.append(arr[j])
        
        # If the current window size is less than `k`, simply expand the window
        if (j - i + 1) < k:
            j += 1
        elif (j - i + 1) == k:
            # If the window size is exactly `k`, check for the first negative number
            if neg_arr:
                # The first element in the list of negatives is the first negative in the window
                result.append(neg_arr[0])
            else:
                # If no negative numbers are found in the current window, add 0 or any other placeholder value
                result.append(0)
            
            # Slide the window: If the element going out of the window is negative, remove it from the list
            if arr[i] < 0:
                neg_arr.pop(0)
            
            # Slide the window forward
            i += 1
            j += 1

    print(result)

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3  # Window size
get_first_neg_array(arr=arr, k=k)
