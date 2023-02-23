# WordNetを用いたラベル推定の実験
「WordNetでフォルダ名を付けてみる実験」で使用したファイル<br><br><br>



<h3>各プログラムの役割</h3>
write_exist_word.py<br>
↓<br>
以下の条件を全て満たす単語をexist_word.txtに登録
<ul>
  <li>wid.txtに登録されている単語</li>
  <li>WordNetに登録されている単語</li><br>
</ul>

wordnet.py<br>
↓<br>
以下の条件を全て満たす単語をup_entity.txtに登録
<ul>
  <li>exist_word.txtに登録されている単語</li>
  <li>important_word.txtに登録されている単語</li><br>
</ul>

replace.py<br>
↓<br>
up_entity.txt内で「重要語が重複している単語」の「一つ目の上位語」を削除<br><br><br>
def_category.py<br>
↓<br>
各上位語の数をカウント<br><br>

reverse.py<br>
↓<br>
ファイルの内容を消去する<br><br><br>

<h3>参考文献</h3>
<ul>
  <li>
    <a href="https://bond-lab.github.io/wnja/jpn/index.html">日本語 WordNet</a>
  </li><br>
  <li>
    <a href="https://aclanthology.org/L08-1077/">Boot-Strapping a WordNet Using Multiple Existing WordNets</a>
  </li><br>
  <li>
    <a href="https://qiita.com/shunji-muto/items/e8a8794eaed5d0518f8f">日本語WordNetで上位語を全てを表示する(python)</a>
  </li><br>
</ul>

