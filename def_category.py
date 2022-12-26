def line_replace(line):
	line = line.replace("\n",'')\
	           .replace(' ','')
	return line


def read_f1(path1, path2):
	f1   = open(path1, 'r', encoding="utf-8")
	f2   = open(path2, 'w', encoding="utf-8", newline='')
	line = line_replace(f1.readline())
	list = []
	pair = []
	prev = ''
	
	while line:
		pos  = line.find(':')
		line = line[pos+1:]
		list.append(line)
		line = line_replace(f1.readline())
	
	f1.close()
	size = len(list)
	
	for i in range(size):
		target = list[i]
		#print("{} : {}".format(list.count(target), target))
		pair.append(str(list.count(target)) + ':' + target)
		
	list.clear()
	pair = sorted(pair, key = lambda x: (x[0]), reverse = True)
	
	for i in range(size):
		this = pair[i]
	
		if this != prev:
			f2.write(this + "\n")
		
		prev = this

	f1.close()
	f2.close()


path1 = "data2/kaden-channel/up_entity.txt"
path2 = "data2/kaden-channel/def_category.txt"
read_f1(path1, path2)

'''

実行コマンド
python def_category.py

実行パス
"data/dokujo-tsushin/up_entity.txt"

"data/it-life-hack/up_entity.txt"

"data/kaden-channel/up_entity.txt"

"data/livedoor-homme/up_entity.txt"

"data/movie-enter/up_entity.txt"

"data/peachy/up_entity.txt"

"data/smax/up_entity.txt"

"data/sports-watch/up_entity.txt"

"data/topic-news/up_entity.txt"

'''

