fp = open("poem.txt", "r", encoding="utf-8")
data = fp.readlines()
fp.close()

lines = len(data)
for i in range(0, lines, 4):
	print("詞牌名：", data[i].split(":")[1])
	print("作者：", data[i+1].split(":")[1])
	print("內容：", data[i+2].split(":")[1])
