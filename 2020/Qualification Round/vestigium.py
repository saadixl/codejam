def get_list_dup(arr):
	map = {i:arr.count(i) for i in arr}
	mx = max(map.values())
	if mx > 1:
		return 1
	else:
		return 0

def traverse(rows, N, k):
	index = 0
	trace = 0
	row_dup_count = 0
	col_dup_count = 0
	# Since it's N*N ;)
	for row in rows:
		row = row.split(" ")
		row_dup_count += get_list_dup(row)
		col = []
		for i in range(N):
			ith_row = rows[i]
			ith_row = ith_row.split(" ")
			col.append(ith_row[index])
		col_dup_count += get_list_dup(col)
		
		trace += int(row[index])
		index += 1
	print("Case #{}: {} {} {}".format(k, trace, row_dup_count, col_dup_count))

def input_rows(N, k):
	rows = []
	for n in range(0,N):
		row = input()
		rows.append(row)
	traverse(rows, N, k)

# Entry point
T = int(input())	
for x in range(1,T+1):
	N = int(input())
	input_rows(N, x)
