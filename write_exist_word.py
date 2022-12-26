import sqlite3

if __name__ == '__main__':

    #データベースに接続
	f1   = open("data/wid.txt",        'r', encoding="utf-8")
	f2   = open("data/exist_word.txt", 'w', encoding="utf-8", newline='')
	id   = 1
	conn = sqlite3.connect("wnjpn.db")
	line = f1.readline()
	
	while line:
	
		#単語からそのWordIDを取得
		word    = line[line.find(' ')+1:line.rfind(' ')].replace('0','')
		cur     = conn.execute("select wordid from word where lemma='%s'" % word)
		word_id = 99999999 #temp
		
		for row in cur:
			word_id = row[0]
			
		if word_id != 99999999:
			f2.write("{} {}\n".format(id,word))
			id += 1
		
		line = f1.readline()

'''
実行パス
python write_exist_word.py

wordnetに存在する単語のみ記録する
'''
