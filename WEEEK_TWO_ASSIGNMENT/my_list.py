# Initial empty list
my_list = []

# Appending the [10, 20, 30, 40] to my_list using +=
my_list += [10, 20, 30, 40]

# Insert 15 at the second position
my_list.insert(1, 15)

# A new_list
new_list = [50, 60, 70]

# Extend my_list with new_list
my_list.extend(new_list)

# Remove last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Sort the list in descending order
# my_list.sort(reverse=True)

# Sorted list without modifying the original
# sorted_list = sorted(my_list)

# Find the index of 30
index_of_30 = my_list.index(30)

print(index_of_30)  