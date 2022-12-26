import sqlite3
import copy

def dfs(synset_tree):
    
    for synset_root in synset_tree:

        #上位語を検索
        cur     = conn.execute("select synset1 from synlink where synset2='%s' and link='hypo'" % synset_root[len(synset_root)-1])
        synsets = []
        for result in cur:
            synsets.append(result[0])

        #上位語が一つもないとき
        if len(synsets) == 0:
            return

        #上位語が一つの場合
        elif len(synsets) == 1:
            synset_root.append(synsets[0])
            #dfs(synset_tree)

        #上位語が複数の場合
        elif len(synsets) > 1:
            #現在の道を(上位語の数-1)コ複製する
            for i in range(len(synsets)-1):
                synset_tree.append(copy.deepcopy(synset_root))

            #それぞれ複製した道に複数ある上位語を一つずつ割り当てる
            tree_index = 0
            for hypernym in synsets:
                synset_tree[tree_index].append(hypernym)
                tree_index += 1
                
            #dfs(synset_tree)
			
			
# synsetID から全ての上位語を検索し，synsetID のリストとして返す．
def get_synset_id(cur):
	synset       = []
	synset_roots = []
	
	for row in cur:
		synset.append(row[0])
	
	synset_roots.append([synset[0]])
	return synset_roots
		

# 辞書の作成	
def get_dict():
	global dict
	global path1
	
	# WordNet に登録されている単語のリスト
	file = open(path1, 'r', encoding="utf-8")
	line = file.readline()
	
	while line:
		key_word = line.split(' ')
		line     = file.readline()
		dict.setdefault(key_word[1], key_word[0])
	
	file.close()


# 重要語をリストに登録
def get_key_word():
    global key_word
    global dict
    global path2

    # TF-IDF を使用して求めた重要語のリスト
    file = open(path2, 'r', encoding="utf-8")
    line = file.readline().replace('0','')

    # 登録した重要語の数を数える
    count = 0

    # 重要語がWordNetに登録されていたらリストに登録する
    while line:

        if line in dict.keys():
            key_word.append(line.replace("\n",''))
            count += 1

        if 100 < count:
            break
            
        line = file.readline().replace('0','')

    file.close()


# WordNet に登録されている単語をファイルに記録する
def write_exist_word(cur1, cur2, word):
	global path3

	file   = open(path3, 'a', encoding="utf-8", newline='')
	sub_no = 1
	
	for row1 in cur1:
		#print(row1[0])
		file.write("{}:{}".format(word, row1[0] + "\n"))
	
	'''
	for row2 in cur2:
		print("意味%s：%s" %(sub_no, row2[0]))
		sub_no += 1
	'''
	
	file.close()


if __name__ == '__main__': 
 conn     = sqlite3.connect("wnjpn.db") 
 
 path1    = "data/exist_word.txt"
 path2    = "data2/topic-news/important_word.txt"
 path3    = "data2/topic-news/up_entity.txt"
 dict     = {} 
 key_word = [] 
  
 # WordNetに存在する単語を登録 
 get_dict() 
  
 # 重要語を登録 
 get_key_word() 
 key_size = len(key_word) 
  
 for i in range(key_size): 
   
  # 単語から WordID を取得 
  word    = key_word[i] 
  cur     = conn.execute("select wordid from word where lemma='%s'" % word) 
  word_id = 99999999 #temp 
   
  for row in cur: 
   word_id = row[0] 
   
  if word_id != 99999999: 
   
   # WordID から synsetID を取得してパラメタ(引数)に設定 
   synset_roots = get_synset_id(conn.execute("select synset from sense where wordid='%s'" % word_id)) 
    
   # 上位語を検索 
   dfs(synset_roots) 
    
   # 上位語をファイルに記録する 
   no = 1 
   for root in synset_roots: 
    for synsetID in root: 
     write_exist_word(conn.execute("select name from synset where synset='%s'" % synsetID),\
                      conn.execute("select def from synset_def where (synset='%s' and lang='jpn')" % synsetID),\
                      word)
     no += 1 
    
   #print(synset_roots)
   synset_roots.clear()
 
''' 
実行コマンド
cd reserch\AI\AI_models\knn\wordnet
python wordnet.py 


各ファイルのパス
 path1    = "data/exist_word.txt"
 path2    = "data/dokujo-tsushin/important_word.txt"
 path3    = "data/dokujo-tsushin/up_entity.txt"

 path1    = "data/exist_word.txt"
 path2    = "data/it-life-hack/important_word.txt"
 path3    = "data/it-life-hack/up_entity.txt"

 path1    = "data/exist_word.txt"
 path2    = "data/kaden-channel/important_word.txt"
 path3    = "data/kaden-channel/up_entity.txt"

 path1    = "data/exist_word.txt"
 path2    = "data/livedoor-homme/important_word.txt"
 path3    = "data/livedoor-homme/up_entity.txt"

 path1    = "data/exist_word.txt"
 path2    = "data/movie-enter/important_word.txt"
 path3    = "data/movie-enter/up_entity.txt"

 path1    = "data/exist_word.txt"
 path2    = "data/peachy/important_word.txt"
 path3    = "data/peachy/up_entity.txt"

 path1    = "data/exist_word.txt"
 path2    = "data/smax/important_word.txt"
 path3    = "data/smax/up_entity.txt"

 path1    = "data/exist_word.txt"
 path2    = "data/sports-watch/important_word.txt"
 path3    = "data/sports-watch/up_entity.txt"

 path1    = "data/exist_word.txt"
 path2    = "data/topic-news/important_word.txt"
 path3    = "data/topic-news/up_entity.txt"

 
参考文献 
https://qiita.com/shunji-muto/items/e8a8794eaed5d0518f8f 

'''
