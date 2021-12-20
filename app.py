list = [2, 1, 2, 3, 4]


def count_evens(nums):
    for item in nums:
        count = 0
        if(item % 2 == 0):
            count = count + 1
        else:
            continue

        return count


print(count_evens(list))
