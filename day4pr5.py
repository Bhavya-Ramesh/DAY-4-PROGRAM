def min_jumps_to_end(arr):
    n = len(arr)
    if n == 0 or arr[0] == 0:
        return -1  
    jumps = 1
    max_reach = arr[0]  
    steps_left = arr[0]  
    for i in range(1, n):
        if i == n - 1:
            return jumps  
        max_reach = max(max_reach, i + arr[i])
        steps_left -= 1
        if steps_left == 0:
            jumps += 1
            if i >= max_reach:
                return -1  
            steps_left = max_reach - i
    return -1  
arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
result = min_jumps_to_end(arr)
if result != -1:
    print(f"Minimum number of jumps: {result}")
else:
    print("It's not possible to reach the end.")
