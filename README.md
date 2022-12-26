# WordNet
「WordNetでフォルダ名を付けてみる実験」で使用したファイル


write_exist_word.py
↓
以下の条件を全て満たす単語をexist_word.txtに登録
<ul>
  <li>wid.txtに登録されている単語</li>
  <li>WordNetに登録されている単語</li>
</ul>


wordnet.py
↓
以下の条件を全て満たす単語をup_entity.txtに登録
   
   ・exist_word.txtに登録されている単語

   ・important_word.txtに登録されている単語


replace.py
↓
up_entity.txt内で「重要語が重複している単語」の「一つ目の上位語」を削除


def_category.py
↓
各上位語の数をカウント


reverse.py
↓
ファイルの内容を消去する


参考文献
<a href="https://qiita.com/shunji-muto/items/e8a8794eaed5d0518f8f">日本語WordNetで上位語を全てを表示する(python)</a>
