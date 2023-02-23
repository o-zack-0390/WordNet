# WordNetを用いた「文書群のラベル推定」の実験
「WordNetでフォルダ名を付ける実験」で使用したプログラムを保管<br><br><br>

<h3>背景</h3>
文書フォルダに適切なフォルダ名を機械的に命名する研究において、
<a href="https://www.jstage.jst.go.jp/article/jceeek/2019/0/2019_580/_pdf">先行研究</a>
によりSVMを使用する方法では上手く命名できなかったという実験結果が示された。<br>
そこで、本実験ではWordNetを使用する方法でラベル推定を試みた。<br><br>


<h3>実験データ</h3>
先行研究と同様のデータで実験したいためlivedoorニュースコーパスを使用する<br>
・<a href="https://www.rondhuit.com/download.html">livedoorニュースコーパス</a><br><br>


<h3>実験方法</h3>
カイ二乗検定で重要語を上から100個取得<br>
↓<br>
取得した重要語の中で、WordNetに登録されていない単語は削除<br>
↓<br>
残った重要語から各重要語の上位語を取得<br>
↓<br>
各上位語の出現回数を計算<br>
↓<br>
出現回数が最も多い上位語をカテゴリー名とする<br><br>


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


<h3>実験結果</h3>
[1] <a href="https://user-images.githubusercontent.com/116938721/220819462-68c24e10-c107-44a9-aeb1-4b5d9c021e80.jpg">結果1</a><br>
[2] <a href="https://user-images.githubusercontent.com/116938721/220819506-5b8ae82a-d975-4a15-baa5-092b5fff3d5c.jpg">結果2</a><br>
[3] <a href="https://user-images.githubusercontent.com/116938721/220819524-a1fcac1b-77d2-435f-847b-6d1b3721f441.jpg">結果3</a><br><br>

1行目は本来のフォルダ名であり、2行目以下は機械的に命名したフォルダ名である。<br>
上の行にあるフォルダ名であるほど命名候補となりやすい。<br><br>

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

