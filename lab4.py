"""

This program will take a number, then output the deficient numbers, perfect numbbers, and abundant numbers.

"""

upper_bound = int(input("Enter an upper bound for a check: "))

lower_bound = 1




def proper_divisors_sum(n) : 
	divisors_sum = 0
	for i in range(1, n):
		if n % i == 0:
			divisors_sum += i
	return divisors_sum
		
def count_classification(lower_bound, upper_bound) :
	deficient_count = 0
	perfect_count = 0
	abundant_count = 0
	for num in range(1, upper_bound + 1) :
		div_sum = proper_divisors_sum(num)
		if div_sum == num:
			perfect_count += 1
		elif div_sum < num:
			deficient_count += 1
		else:
			abundant_count += 1
	return deficient_count, perfect_count, abundant_count

deficient, perfect, abundant = count_classification(1, upper_bound)

print(f"Between 1 and {upper_bound} there are")

print(f"{deficient} deficient numbers")
print(f"{perfect} perfect numbers")
print(f"{abundant} abundant numbers")
	
