def hittable_targets(room):
   # find the position of Auberon
   # find the position of targets
   # loop through the room and find the position of each target
   # check if the target is hittable
   # the target is hittable if it is in the same row or column and there's no wall prior to the target
   # if the target is hittable in increment count by 1
    
    list_of_targets = []
    list_of_walls = []
    count = 0
    
    for i in range(len(room)):
        for j in range(len(room[0])):
            if room[i][j] == 'A':
                indices_A = [i,j]
            if room[i][j] == 'T':
                indices_T = [i,j]
                list_of_targets.append(indices_T)
            if room[i][j] == 'W':
                indices_W = [i,j]
                list_of_walls.append(indices_W)

    for target in list_of_targets:
        
        if target[0] == indices_A[0]:
            for wall in list_of_walls:
                if (wall[0] == indices_A[0] and
                    min(indices_A[1], target[1]) < wall[1] < max(indices_A[1], target[1])):
                    break
            else:
               
                for next_t in list_of_targets:
                    if (next_t != target and
                        next_t[0] == indices_A[0] and
                        min(indices_A[1], target[1]) < next_t[1] < max(indices_A[1], target[1])):
                        break
                else:
                    count += 1

       
        if target[1] == indices_A[1]:
            for wall in list_of_walls:
                if (wall[1] == indices_A[1] and
                    min(indices_A[0], target[0]) < wall[0] < max(indices_A[0], target[0])):
                    break
            else:
               
                for next_t in list_of_targets:
                    if (next_t != target and
                        next_t[1] == indices_A[1] and
                        min(indices_A[0], target[0]) < next_t[0] < max(indices_A[0], target[0])):
                        break
                else:
                    count += 1

    return count
            


expected = 2
actual = hittable_targets([
    [' ', 'T', 'W', ' ', 'T'],
    ['T', ' ', ' ', ' ', ' '],
    [' ', 'A', ' ', 'T', 'T'],
    [' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', ' ', ' '],
    [' ', 'T', ' ', ' ', ' '],
])
assert actual == expected, f"expected {expected} but got {actual}"

room2 = [
    [' ', 'T', ' ', ' '],
    ['T', 'A', 'T', ' '],
    [' ', 'T', ' ', ' '],
]
assert hittable_targets(room2) == 4

room3 = [
    ['T', ' ', 'T'],
    [' ', 'A', ' '],
    ['T', ' ', 'T'],
    [' ', ' ', ' '],
]
assert hittable_targets(room3) == 0

room4 = [
    ['T', 'A', ' ', 'W', ' ', 'T'],
]
assert hittable_targets(room4) == 1

room5 = [
    ['A'],
]
assert hittable_targets(room5) == 0

print("All tests passed!")
print("If time remains, discuss time & space complexity")
