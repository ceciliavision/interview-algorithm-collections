"""
Greedy approach
- knapsack problems(combinatorial optimization)

Common approach
- sort the array
- dictionary to store completed computation (for future reference back)
- iterate over one variable (set as the key for the dictionary)
- dictionary value is what's eventually going to return (objective)

Leetcode IDs
368 Largest Divisible Subset: store at each number (sorted), what's the longest so far
139. Word Break: fix current subarray, varying subdivision within the subarray
377 Combination Sum IV: knapsack problem
330. Patching Array

Histogram and rectangular area
84. Largest Rectangle in Histogram: global bottleneck; stack to keep track of the bottlenect height so far
85. Maximal Rectangle: run 1D for every row
42. Trapping Rain Water: local bottleneck; 
407. Trapping Rain Water II

"""


def max_duffel_bag_value(cakes, capacity):
	"""
	Two parameters to optimize, fix one and iterate on another (better to sort).
	Keep track of the current optimized value given the fixed paramters

	"""

	sorted_cakes = sorted(cakes, key=lambda x:x[0])
	sorted_w = [w[0] for w in sorted_cakes]
	current_max_profit = dict()
	current_max_profit[0] = 0
	for weight in range(capacity+1):
		weight_i_max = 0
		for cake_item in sorted_cakes:
			cake_w = cake_item[0]
			cake_p = cake_item[1]
			if cake_w <= weight:
				# if adding cake would increas our profit
				this_profit = cake_p + current_max_profit[weight - cake_w]
				weight_i_max = max(weight_i_max, this_profit)
		current_max_profit[weight] = weight_i_max

	return current_max_profit[capacity]

def largestRectangleArea(self, heights: List[int]) -> int:
	"""
	Leetcode #84
	"""

    area_stack = [-1]
    heights.append(0)
    global_max = 0
    for i, rec in enumerate(heights):
        while area_stack and rec < heights[area_stack[-1]]:
            h = heights[area_stack.pop()]
            w = i - area_stack[-1] - 1
            global_max = max(global_max, h * w)
        area_stack.append(i)
    return global_max

cakes = [(7, 160), (3, 90), (2, 15)]
capacity = 20
print('profit for weight capacity %d is: '%(capacity), max_duffel_bag_value(cakes, capacity))

