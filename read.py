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

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

# 文字計數
wc = {} # word_count
for d in data:
	words = d.split() # split預設就是空白鍵
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增地餓key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
	
while True:
	word = input('請問你想查什麼字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print(word, '沒有出現過')
print('感謝使用本查詢功能！')
	

