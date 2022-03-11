data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # % 是用來求餘數
			print(len(data))

print('檔案讀取完了, 總共有', len(line), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)

print('每一筆留言的平均長度為', sum_len/len(d))

new = []
for d in data:
	if len(d) < 100: # 篩選長度小於100的留言
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
