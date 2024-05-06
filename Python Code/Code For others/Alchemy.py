import itertools

count = 0
for i1, dx, dy in itertools.product([1,0],[-1,1],[-1,1]):
    print("index:",i1,"index:", (1 + i1)%2 ,"dx:",dx,"dy:",dy)
    count+=1
print(count)

current_x =

for index, dx, dy in itertools.product([1,0],[-1,1],[-1,1]):
    new_x, new_y = current_x + dx * move_vector[index], current_y + dy * move_vector[(1 + index)%2]
