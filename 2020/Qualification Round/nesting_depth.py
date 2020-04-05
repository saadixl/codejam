def wrap_digit(d):
	if d == 0:
		return str(d)
	else:
		prefix = ""
		suffix = ""
		for i in range(d):
			prefix += "("
			suffix += ")"
		return prefix + str(d) + suffix


def input_number(k):
	S = input()
	result = ""
	for i in range(len(S)):
		d = int(S[i])
		wrapped = wrap_digit(d)
		result += wrapped
	# minimizing brackets
	while result.find(")(") != -1:
		result = result.replace(")(", "")
	print("Case #{}: {}".format(k, result))

# Entry point
T = int(input())	
for k in range(1,T+1):
	input_number(k)