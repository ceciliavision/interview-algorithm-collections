"""
Collection of permutation-related problems.

Usually for these questions, we can use either a recursive or iterative approach (both provided).

"""

def find_all_permutation_rec(arr):
    """
    Recursive way to find all permutaiton given an array of numbers
    """
    if len(arr) == 1:
        return [arr]

    permutation_list = []
    for i in range(len(arr)):
        num = arr[i]
        rest = arr[:i] + arr[i+1:]
        perm = find_all_permutation_rec(rest)
        for p in perm:
            permutation_list.append([num] + p)

    return permutation_list

def find_all_permutation_iter(arr):
    """
    Iterative way to find all permutaiton given an array of numbers
    """
    permutation_list = [[]]
    for i in range(len(arr)):
        for sub_set in permutation_list:
            for elem in arr:
                if elem not in sub_set:
                    permutation_list = permutation_list + [sub_set+[elem]]

    return [perm for perm in permutation_list if len(perm)==len(arr)]

def get_power_set_rec(arr):
    """
    Recursive way to find the power set of a given array
    """
    power_set = []
    def helper(arr, temp):
        if temp not in power_set:
            power_set.append(temp)
        for pos, ele in enumerate(arr):
            rest = arr[pos+1:]
            helper(rest, temp+[ele])
    helper(arr, [])
    return power_set

def get_power_set_iter(arr):
  power_set=[[]]
  for elem in arr:
    # iterate over the sub sets so far
    for sub_set in power_set:
      # add a new subset consisting of the subset at hand added elem
      power_set = power_set+[list(sub_set)+[elem]]
  return power_set

def nars_num(n):
    all_pos = [pow(i, n) for i in range(10)]

    lb = pow(10, n-1)
    ub = pow(10, n)
    def is_valid(k):
        if k >= lb and k < ub:
            return True
        return False

    def subset(n, k, seen):
        if len(seen) == k:
            return [seen]
        else:
            ll = []
            for pos, i in enumerate(n):
                if i in seen:
                    continue
                rem = n[:pos] + n[pos+1:]
                ll += subset(rem, k, seen+[i])
        return ll
    
    p_list = subset(all_pos, n, [])

    final = []
    for p in p_list:
        if is_valid(sum(p)):
            final.append(p)
    return (final)

arr_test = [1, 2, 3, 4]

print("Permutation using recursive way: ", find_all_permutation_rec(arr_test))
print("Permutation using iterative way: ", find_all_permutation_iter(arr_test))

print("Using recursive way: ", get_power_set_rec(arr_test))
print("Using iterative way: ", get_power_set_iter(arr_test))

