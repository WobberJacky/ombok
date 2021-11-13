label gakuen_peter2:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_ros_day
with dis

play music entrance_p_wam

scene bg_par20_re with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その日、いつものように授業を終えてエントランスに向かうと、そこではペーターが待ち受けていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（う、わ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "モンスターにでも遭遇したかのような反応になってしまう。\n
好き嫌いというより、長年の付き合いの結果というか……、条件反射だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは、まだ私に気付いていないのだろう。\n
無表情にも見える顔立ちは、まさしく白皙の美貌なんて言葉が似合う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "透けるように白い肌に銀色の髪、そして唯一色づいた赤の瞳……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（本当に、見た目だけはいいんだから）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女である私が悔しくなるぐらいに、綺麗だ。\n
だからといって、ペーターが女性的というわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生き物として、綺麗だ。\n
綺麗だからこそ、こうして無表情でいると冷たく、無機質に見えてしまうのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……っと、見蕩れている場合じゃなくて。\n
どうして、ペーターがこんなところにいるのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昔から潔癖症の気のあったペーターは、こういった、人が多く集まる場所が苦手だ。雑菌がどうのと、人が集まる場所は避けたがっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（もしかして、私を待っているのかしら）"

menu:
    "声をかけてみる。":
        jump gakuen_peter2_2a
    "スルーする。":
        jump gakuen_peter2_2b
label gakuen_peter2_2a:
$ lovechara_peter_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……ペーター？\n
珍しいわね、こんなところにいるなんて」"


show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
Peter "「……！！！\n
[firstname]！！！」"

hide per_m_02_3
show per_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pet_g0058
Peter "「ああ、[firstname]！\n
あなたを待っていたんです！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱあっと表情を輝かせてペーターが私のもとへと駆けつける。\n
先ほどまでの、冷たい印象すらあった無表情が嘘のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「私を待つ……、って。\n
何か用？」"

jump gakuen_peter2_3
label gakuen_peter2_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……嫌な予感がする）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうしてペーターが待ち構えているということは、おそらく私に何か用事があるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "果たしてそれが私にとっていいことか、と聞かれたら悩まざるをえない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと彼に背を向けると、校舎から出て行こうとする人の流れに逆行して歩きだす。"

hide per_m_01_2
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「……！！！\n
[firstname]！！！」"

hide per_m_02_3
show per_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0059
Peter "「ああ、[firstname]！\n
どうしたんですか、忘れ物ですか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逆にその行動が目立ってしまったのか、見つけられてしまった。\n
こっそり溜息をついてから、今気付いたという顔でペーターへと向き直る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いえ、なんでもないわ。\n
何も忘れてない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ペーターは、こんなところでどうしたの？」"

jump gakuen_peter2_3
label gakuen_peter2_3:
hide per_m_01_3
show per_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0060
Peter "「いえ、ほら、先日美術館のお話をしたでしょうっ？\n
それで、今日あなたがお暇なようでしたらと、お誘いしにきたんですっ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……ああ、そういえば）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの秘宝を探しているという、戯れ半分の言葉。\n
そこから発展して、ペーターが美術館を案内してくれるということになっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれも、半ば冗談、話の流れのようなもの。\n
具体的にいつ行くだとか、そういう話はしていなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「私は、別に予定もないから大丈夫だけど……。\n
ペーターは、自治会の仕事、大丈夫なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこが一番の問題だ。\n
実は意外なことに、あの三人の中で一番まともに仕事をしているのはペーターらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がいると浮かれあがってしまうペーターなのだが、他の二人は私がいようといまいと関係なく仕事をしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな二人と比較したならば、私さえいなければ比較的まともに仕事をするペーターは、大事な働き手。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他二人に、ガミガミと発破をかけているペーターを見かけたこともある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ残念なのは、それがそのまま喧嘩に発展し、結局仕事は一切進まないという点だ。"

hide per_m_02_1
show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0061
Peter "「僕の分の仕事は終わらせてきましたから！」"

hide per_m_02_5
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0061_5
Peter "「会長が仕事を溜めて癇癪を起こそうと、エース君がどこかで野たれ死のうと、僕には関係ありませんよ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "非常にいい笑顔で言い切られてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……いいのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自治会の仕事の全体進行が、部外者ながらに気になるところだ。"

hide per_m_02_13
show per_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0062
Peter "「どうでしょう、駄目ですか？\n
あなたの都合が合わないようでしたら、出直してきますが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の反応をうかがいながら、ペーターの長いウサギ耳が次第にしょんぼりと垂れていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな反応を見せられてしまったら、断れるわけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何より、元々特に予定があったわけでもないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……いいわ、仕事が終わったということなら。\n
案内を頼んでもいいかしら」"


play music flower_day_p_wam
hide per_m_01_8
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0063
Peter "「もちろんです、[firstname]！\n
あなたとデートできるなんて夢のようです！！！」"

hide per_m_02_13
show per_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0064
Peter "「……さ、気が変わらないうちに！！\n
ほら、行きましょう！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「大袈裟なんだから……。\n
それにデートじゃないわよ」"

play sound se_0158
pause .1
play sound se_0774
hide per_m_03_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "訂正する私の言葉は、浮かれたように手を引くペーターにはきっと届いていないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うきうきと弾む足取りで歩む彼に先導されて歩きながら、繋いだままの手へと視線をやる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とても懐かしい感覚がすると思ったら、それは彼の手袋のせいだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……昔からよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通に手を繋ぐのとは違う、さらりとした感触は彼特有のものだ。\n
思えば、ペーターとの接触はいつだってこの薄布一枚隔てていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あなたって……。\n
今でも、潔癖症なの？」"


show per_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0065
Peter "「病気みたいに言わないでくださいよ。\n
僕が潔癖症なのでなく、僕以外の連中が鈍感なだけです」"

hide per_m_03_9
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0066
Peter "「ああ、もちろん！あなたは綺麗ですよ！？\n
僕は、あなたの雑菌にならば耐えられます！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……結局、雑菌はいるんじゃないの」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……生き物として当然だけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばい菌扱いは勘弁願いたい。"

hide per_m_02_3
show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0067
Peter "{size=+20}「あなたの雑菌は綺麗なんです！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……ごめんなさい、ペーター。\n
言っている意味が分からないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "謝る必要があるのかどうか。\n
残念ながら、私には雑菌の美醜が判断できない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呆れる反面、何故か笑い出したいような気にもなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（どうしてかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーター＝ホワイトに手を引かれて、一緒に美術館へと行く。\n
それは、考えてみたらおかしなことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はストーカーみたいだし、常日頃からできるだけ避けようとしていたはずだ。\n
だが、今、手を引かれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この前も、今も。\n
逃げ出そうと暴れることもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（ペーターが落ち着いているから？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間違えた方向に突っ走るのはいつも通りだが、そこまで酷くはない。\n
子供の頃のことを思い出してしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ふふ、昔よくこうして遊びに出かけたわね。\n
ペーターは外で遊ぶの、あんまり好きじゃなかったけど」"

hide per_m_02_5
show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pet_g0068
Peter "「僕は綺麗好きですからね。\n
……あなたは、いつも泥だらけになりながら遊んでいましたよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「あなたはいっつも抵抗していたわよね。\n
ああ、何かおかしいと思ったら逆なのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふふっと笑みが零れた。\n
記憶も溢れ出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "涙目で頭をぶんぶん振って抵抗するペーターの手を握り、力ずくでずるずると引きずって歩いた。\n
懐かしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのときとは反対に、今はペーターが主導。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "互いの立場や年齢など、他にも変わった部分は多いのに、何気ないことばかり比較する。\n
布越しの体温だけが同じ。"

hide per_m_02_8
show per_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0069
Peter "「僕はいつも、あなたが未知の病原菌に感染するんじゃないかと恐れていました……。うう、死なないでくださいね、[firstname]……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「外で泥遊びしたぐらいで、そんな病気になったりしないわよ。\n
あなたのほうこそ、潔癖がすぎると、どんどん抵抗力が落ちていくわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターのようにひたすら菌を避ける生活をしていると、逆に菌に対する抵抗力がなくなってしまいそうなものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうなると、普通の人ならなんでもないような量の菌でも、発症してしまうようなことになると聞く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずっと減菌室で生活するわけにもいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（ペーターのほうこそ、大丈夫なのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "筋金入りの潔癖症たる彼である。\n
こちらのほうが心配してしまう。"

hide per_m_01_8
show per_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0070
Peter "「ああ、優しい人ですね！\n
あなたが僕の心配をしてくれるなんて、嬉しいです！」"

hide per_m_02_12
show per_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0071
Peter "「でも大丈夫ですよ！僕の守りは強固ですから！\n
雑菌一匹たりとも侵入させません！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは何を根拠にした自信なのだろうか。\n
雑菌なんて、空気中にうようよいるものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それともペーターは、そういったものとも接触しないように何か魔法による守りでもかけているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もし、本当にそうなら、それこそビョーキの域。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "美術品に殺菌剤をまいたりしないだろうかと心配しつつ、美術館へと歩みを進めていく。"

hide per_m_03_1
with dis
$ hi_mes()

scene bg_par20_re with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg22_ms_o_day
with stripe_l_medium

scene bg22_ms_i_day
with stripe_l_long

play music gallery_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア高位魔法学校付属の美術館は、ずいぶんと立派な建物だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だいたいどこの学校にも、小さな展示スペースなどがあるものなのだが、シンフォニアの美術館はそんなレベルをはるかに超えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校付属という面を抜きにして、一つの美術館としてみても充分評価に値する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一般の美術館に引けをとらないのはもちろん、マジックアイテムがらみの美術品が多く揃っているあたりシンフォニアらしい特色だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「すごいわね……っ。\n
ここまで立派な美術館だとは、思っていなかったわ」"


show per_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0072
Peter "「シンフォニア高位魔法学校付属美術館は、関係者しか見られない割には充実していまして」"

hide per_m_02_11
show per_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0072_5
Peter "「これだけの設備なのに無名だという意味で有名なんですよ」"

hide per_m_02_7
show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0073
Peter "「各国より珍しい美術品や、マジックアイテムを蒐集しているんです。\n
それこそシンフォニアの秘宝に相応しい、素晴らしい品々ばかり……」"

hide per_m_02_8
show per_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0074
Peter "「……何か興味のあるものはありますか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「んー……、ごめんなさい。\n
私、美術品ってあんまり詳しくないのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「見るのは好きなんだけど、見るだけ、っていうか……。\n
ペーターのお勧めを教えてくれる？」"

hide per_m_03_1
show per_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice pet_g0075
Peter "「僕のお勧めですか？\n
そうですね……、ではアーティファクトなどいかがです？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「アーティファクト？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは私の手を引いて、エントランスから続くホールまで案内してくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ホールの中央からは様々な部屋へと分岐していて、それぞれテーマに沿って美術品が展示されているようだ。"

hide per_m_02_4
show per_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0076
Peter "「アーティファクトというのは、美術品という意味もありますが……」"

hide per_m_01_10
show per_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0076_5
Peter "「どちらかというと過去に作られた、強い力を持つマジックアイテムというような意味合いのものですね」"

hide per_m_01_2
show per_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0077
Peter "「知識がなくとも楽しめるものというなら、珍しい効果を持つアーティファクトは面白いと思いますよ。\n
どうしますか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そうね、見てみたいわ。\n
案内してくれる？」"

hide per_m_02_1
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pet_g0078
Peter "「もちろんですとも！\n
{size=+20}僕に任せて、その身を委ねてください！{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……{size=+20}その表現だと、承服しかねる{/size}」"

hide per_m_02_13
with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは気合たっぷり。\n
慣れた様子で広い美術館の中から目的の場所を見つけだしては、迷いなく私を案内する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さらには、展示品の一つ一つについて、私が興味を持つような形で紹介してくれるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "美術館を訪れる際のガイドとしては、非常に優秀だ。"

show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0079
Peter "「ああ、こちらは『対の母子像』ですね」"

hide per_m_02_8
show per_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0080
Peter "「名前通りセットになっている母と子の像なんですが、何でもこの二つの像はどれだけ引き離しても、再び互いに引き寄せあい、いつの間にか共にあるそうです」"

hide per_m_03_1
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0081
Peter "「僕とあなたのようですよね！\n
ああ、もちろん、僕の場合、離される前に防ぎますけどね！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "優秀なガイド。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただし、説明の途中途中に入る、謎の意気込みをスルーすることが出来るのならば。\n
と、注釈が必要だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（離れない、ねえ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……全寮制の学校に行っちゃったのは、自分なくせに）"

hide per_m_02_13
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
Peter "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやってしばらく見てまわっていると、隣のペーターがはっとしたように立ち止まった。\n
雷にでも打たれたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……？\n
どうしたの？」"

hide per_m_02_3
show per_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice pet_g0082
Peter "「[firstname]、ちょっと来てください……！\n
あなたと、是非試したいアーティファクトがあるんです……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え？\n
試す？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐいぐいと私の手を引いて、ペーターはどこかを目指して歩き出す。\n
その間にある様々な展示物は、すべてスルー。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろいろ面白そうなものを見かけては立ち止まろうと試みるものの、ペーターは止まらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「ね、ねえ……、ちょっと待ってよ？\n
ペーター？」"

hide per_m_01_3
show per_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice pet_g0083
Peter "「どうして忘れていたんでしょう……！\n
あなたがシンフォニアに来たら、真っ先に案内しようと決めていたはずなのに！」"

hide per_m_02_4
show per_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice pet_g0084
Peter "「あなたと会うと、すべてが吹き飛んでしまうんです！なんて罪な人なんでしょう！」"

hide per_m_03_11
show per_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice pet_g0084_5
Peter "「でも大丈夫ですよ、もう思い出しましたから！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "熱に浮かされたような口調で言いながら、ペーターは迷いもなく展示物の間を縫って目的地を目指す。"


play music high_day_p_wam
show m_per2_1and2_5 onlayer master
with dis
hide per_m_03_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やがて、辿り着いた先は小さな小部屋だった。\n
いや、部屋というほどしっかりと壁があるわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薄いパーテーションで区切って、部屋のようにしているだけだ。\n
足を踏み入れたその部屋の中央に、一抱えほどの大きさの丸い盤が浮いていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その中心から光が真っ直ぐに天井へと伸び、時折噴水のようにきらきらと燐粉が散る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……綺麗だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「ねえ、これは何なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice pet_g0085
Peter "「これは占いの道具なんです。\n
とてもとても古い時代のものなのですが……、恋占いで有名なんですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice pet_g0086
Peter "「これで占ってよい結果の出たカップルは、末永く幸せでいられるのだとか。\n
ずっと、あなたとこれを使ってみたかったんです……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段なら、くだらないと笑い飛ばすところだ。\n
そんな占いなんて、思い込みに決まっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろんシンフォニアの授業にも占い学は存在し、私も履修しているから知っている。\n
だからこそ信用出来ないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "優秀な魔法使いが、占星学や数相術など様々な学問の知識をあわせて占っても、当たるも八卦当たらぬも八卦というのが占いというもの。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "アイテム一つで人と人のつながりを判じてしまおうというのは、暴論に思えて仕方がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……だけど、これは信じちゃいそうだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの美術館の小部屋、光の粒子をほろほろとこぼすそのアーティファクトは、本物の風格を漂わせている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（……いや、占う以前に、カップルじゃないんだけど、私達）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "堂々と一緒に占えるような二人なら、占う前からくっついていて当然だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0087
Peter "「さあ、[firstname]、こちらへきてください！僕のほうからあなたの選ぶ花は見えませんし、あなたからは僕の選ぶ花は見えません」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0088
Peter "「そちらにある六つの花の中から、好きなものを一つ選んでくださいね。\n
決まったら、その花に触れてください」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……分かったわ」"

hide m_per2_1and2_5
show m_per2_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とペーターは、その丸い盤を挟むようにして向かい合って立つ。\n
形としては時計に似ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "数字の代わりに、丸い縁の中にそれぞれ描かれている花。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中央のあたりからこんこんと湧き上がる光のせいで、ペーター側のほうを見ることはできない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらくペーターのほうからも、私の手元を見ることは出来ないようになっているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "六つの花が並んでいるが、その中からピンと来たのは二つだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この二つの内から、一つを選ばなければいけないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（どの花がいいかしら……）"
menu:
    "百合を選ぶ。":
        jump gakuen_peter2_4b
    "ひまわりにしよう。":
        jump gakuen_peter2_4a
label gakuen_peter2_4b:
$ lovechara_peter_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（百合にしよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "百合の花の絵の上に、そっと指先を滑らせた。"

play sound se_0640
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

hide m_per2_2
show white onlayer master with spread_short
play sound se_0722
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "途端、光が弾けた。"

play sound se_0612
hide white
show m_per2_3a onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目も眩みそうな白い光の中、するすると茎が伸び、葉をつけ、白い百合が咲き誇る。"

hide m_per2_3a
show m_per2_4a onlayer master with grad_b_extralong

play music quiet_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中央に、女神の姿が現れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（……わ）"

play sound se_0758
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice oda_g0001
Megami "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女神は柔らかく慈しみに満ちた笑みを浮かべ、何事かを囁く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "音としては聞こえているものの、意味のある言葉として理解することはできなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このアーティファクト自体が古そうなので、どこかの地方の古語なのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（でも……、言葉は分からなくても、結果は大体分かる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪い結果を告げる様子ではなかった。"

play sound se_0265
hide m_per2_4a
show white onlayer master with compress_long
hide white
show m_per2_1and2_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やがて結果を告げた女神の姿が消えた。\n
光もおさまり、向かいにいるペーターの姿が見えるようになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0089
Peter "「僕らの相性は、絶好調なようです。\n
ふふ、占いなどしなくとも分かっていたことですが、やはりこうして祝福されると嬉しいものですね……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……あなた、女神の言葉が分かったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0090
Peter "「ええ。\n
僕は、優秀なウサギですから！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（古語も分かるなんて、さすがだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "博識な幼馴染を見直す。"

jump gakuen_peter2_5
label gakuen_peter2_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（ひまわりにしよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひまわりの花の絵の上に、そっと指先を滑らせた。"

play sound se_0640
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

hide m_per2_1and2_5
show white onlayer master with spread_short
play sound se_0722
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "途端、光が弾けた。"

play sound se_0612
hide white
show m_per2_3b onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目も眩みそうな白い光の中、するすると茎が伸び、葉をつけ、ひまわりが咲き誇る。"

hide m_per2_3b
show m_per2_4b onlayer master with grad_b_extralong

play music quiet_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中央に、女神の姿が現れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（……わ）"

play sound se_0758
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice oda_g0002
Megami "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女神は、悲しげな顔で何かを呟いて頭を横に振った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "音としては聞こえているものの、意味のある言葉として理解することはできなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このアーティファクト自体が古そうなので、どこかの地方の古語なのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（でも……、言葉は分からなくても、結果は大体分かる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いい結果を告げる様子ではなかった。"

play sound se_0265
hide m_per2_4b
show white onlayer master with compress_long
hide white
show m_per2_1and2_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やがて結果を告げた女神の姿が消えた。\n
光もおさまり、向かいにいるペーターの姿が見えるようになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0089
Peter "「僕らの相性は、絶好調なようです。\n
ふふ、占いなどしなくとも分かっていたことですが、やはりこうして祝福されると嬉しいものですね……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（ええ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……あなた、女神の言葉が分かったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正直、胡散臭い。\n
あの顔は、どう見ても祝福している表情ではなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0090
Peter "「ええ。\n
僕は、優秀なウサギですから！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（絶対、嘘よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ウサギ耳をしょんぼりとさせながらも、それでも祝福されたと言い張ってやまない幼馴染。\n
笑いがこみあげてきてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこまで言うのなら、いい結果ということでいいのもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（当たるも当たらぬも……、だものね）"

jump gakuen_peter2_5
label gakuen_peter2_5:
hide m_per2_1and2_5

play sound se_0229

play music gallery_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "占い盤のあった小部屋から出て、再び展示品の並ぶ広い区域へと出る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か面白いものがないかと視線をめぐらせてみると、少し離れたところにカウンターがあることに気付いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、美術館のパンフレットを配っているようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（貰っておこうかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「ペーター、私ちょっとパンフレットもらってくるわ」"


show per_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice pet_g0091
Peter "「あ、僕も一緒に……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（もう。\n
なんでも、ついてきたがるんだから）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「すぐそこだから、待っていてくれる？\n
すぐに戻るわ」"

hide per_m_02_9
show per_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice pet_g0092
Peter "「分かりました。\n
早く戻ってきてくださいね、僕、待っていますから！」"

hide per_m_03_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後から掛かる声に頷いて、カウンターへと向かった。"

play sound se_0773
with dis
$ hi_mes()
pause 1


$ time_effect()##PLEASE MANUALLY ADJUST ME
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校付属の美術館では、いちいち専用のパンフレットを作ったりはしないものだが、シンフォニアは別らしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自身の目で確かめたとおり、この美術館の品揃えというのは国立の美術館にも勝るとも劣らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "特にシンフォニア高位魔法学校という特性ゆえにか、魔法がらみの美術品のコレクションは素晴らしいものばかりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっと、許可を得て、外部からこの美術館を訪れたがる人も少なくはないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "内部のものとしても、これだけの美術品なら詳細が知りたいと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "需要に応じているのだろう、カウンターで貰ってきたパンフレットは挿絵つきの親切なものだった。\n
見所なども丁寧に書かれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ついでにとばかり、カウンターの女性とも話をすることが出来た。"


show meido_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0000
Jimu_w "「ああ、新入生の方ですか？\n
こちらの美術館の楽しみ方としては……、そうですね」"

hide meido_a1_2
show meido_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0001
Jimu_w "「月に何度か、美術を趣味にしている教授が、美術館ツアーを開催しています。\n
そちらに申し込んでみたらいかがでしょうか」"

hide meido_a1_3
show meido_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0002
Jimu_w "「より詳細な説明と、学術的にも価値のある美術品を要領よく見てまわることが出来るはずですよ。\n
こちらが申込書になります」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ありがとう、是非参加させてもらうわ。\n
あ、連れがいるのでもう一部貰えますか？」"

play sound se_0472
hide meido_a2_2
show meido_a2_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice hei_g0003
Jimu_w "「はい、どうぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にこやかに笑って彼女は私へと二通の申込書を差し出してくれた。\n
シンフォニアの教授による美術館ツアーなんて、贅沢きわまりない。"

play sound se_0773
hide meido_a2_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "毎月数度と言っていたが、毎回同じコースを辿るのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（次の募集には間に合うかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを思いながら、ペーターの元へと戻る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ペーター……」"



play music notice_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、名前を呼んで駆け寄ろうとして、雰囲気がおかしいことに気付いた。\n
ペーターの周囲には数人の女子生徒がいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どの子も怯えたような、泣き出しそうな顔をしている。\n
そして、その先頭には、クラスメイトの姿があった。"


show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（ボリス？）"

hide bor_m_01_11
show bor_m_01_11 at left
with dis

show per_m_01_14 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一方のペーターは、一切興味ありません、というような冷たい表情でただ周囲を睥睨するばかりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……何があったの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ごめんなさい。\n
彼、私の連れなんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……何があったか教えてくれない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "睨みあうように対峙するペーターと、女の子を庇うように立ったボリスの間へと割り込むようにして聞く。"

hide per_m_01_14
show per_m_01_14 at right
with dis
hide bor_m_01_11
show bor_m_01_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0001
Boris "「え？\n
[firstname]？」"

hide per_m_01_14
show per_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0093
Peter "「ああ、おかえりなさい、[firstname]！\n
……こんな人達のことなんか、気にしなくていいですよ！」"

hide per_m_01_2
show per_m_02_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0094
Peter "「ほら、行きましょう？\n
次のを見に行きませんか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が帰ってきたことに、ペーターは嬉しそうに表情をほころばせる。\n
ほんの数秒前までの冷たい表情が、嘘のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（ああ……。\n
これ、なのね？）"

show white onlayer master ##instant
show bg_par02_ct_ros_day_s onlayer master with Dissolve(.7)
hide white ##instant
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice man_g0059
Seito "「まともっていうか……。\n
普段の副寮長って、超クールよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice tak_g0051
Seito "「すっごく冷たくて、孤高の人っていう感じで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice man_g0060
Seito "「……いわゆる、クールビューティーみたいな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice man_g0061
Seito "「本当なんだってば！\n
普段の副寮長は、愚かな人間とは関わりたくないって感じの、冷血っぽい人なんだから！」"

hide bg_par02_ct_ros_day_s with Dissolve(.7)
show white onlayer master ##instant
hide white with Dissolve(.7)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段のペーターがどういう人物なのか、という話を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "友人達は、ペーター＝ホワイトという人物がいかに周囲に興味がなく、冷たい人間なのかということについてを教えてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、私への対応のほうが特例であるということを。"

hide bor_m_01_2
show bor_m_01_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0002
Boris "「副寮長さん……、この子達がせっかく話しかけてやったっていうのにさ。\n
汚いから寄るな、なんて言うんだぜ？」"

hide bor_m_01_12
show bor_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0003
Boris "「この子達、美術部だからってのもあって、仲良くなれそうだと話かけただけなのに……」"

hide per_m_02_5
show per_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0095
Peter "「頼んでもいないのに、迷惑なだけです。\n
……寄ってこないでもらいたいんですけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰に対して言っても酷い言葉だが、特に女の子に対して言う言葉ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「この子達は、ボリスの連れだったの？」"

hide bor_m_02_8
show bor_m_01_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice bor_g0004
Boris "「や、俺は通りすがっただけ。\n
赤薔薇の副寮長さんがいじめているから、放って置けなくなっちゃったんだよ」"

hide bor_m_01_11
show bor_m_03_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice bor_g0005
Boris "「こっちは……、あんたの連れだったんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスの問いに、私は溜息交じりに頷いた。"

menu:
    "私の連れがごめんなさい。":
        jump gakuen_peter2_6a
    "あの子達をお願いしてもいい？":
        jump gakuen_peter2_6b
label gakuen_peter2_6a:
$ lovechara_peter_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「私の連れが酷いことを言ったわね。\n
この人、潔癖症なの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「あなた達が汚いわけじゃないわ。\n
この人が病気なの」"


show girl_c1_1 at center
with dis
hide per_m_03_9

hide bor_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice mat_g0002
Seito "「え……」"

hide girl_c1_1
show girl_c1_1 at left
with dis

show girl_d2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice sam_g0003
Seito "「えっと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「だから気にしないであげて？」"

hide girl_c1_1
show girl_c1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice mat_g0003
Seito "「……え、ええ。\n
私達も悪気はなかったんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ごめんなさいね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、ボリスの後ろで怯えたように身を竦ませている少女達へと謝った。"


show per_m_01_5 at center
with dis
hide girl_c1_5

hide girl_d2_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0096
Peter "「な……っ！？\n
どうしてあなたが謝るんですか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……あなたが、あの子達に酷いことを言ったからよ」"

hide per_m_01_5
show per_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
Peter "「……っ！」"

jump gakuen_peter2_7
label gakuen_peter2_6b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ボリス、悪いんだけど……。\n
あの子達のフォロー、お願いしてもいい？」"


show bor_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice bor_g0006
Boris "「…………。\n
……ま、他でもないクラスメイトの頼みなら引き受けなきゃね」"

hide bor_m_01_3
show bor_m_02_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice bor_g0007
Boris "「その代わり、次のおっさんの授業の宿題手伝ってよね。\n
俺、レポートとか書くの、苦手なんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……分かった、借り一つね。\n
喜んで手伝わせてもらうわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それから私は改めてボリスの後ろに隠れるようにして、縮こまってしまっている少女達へと向き直った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「私の連れが、ごめんなさいね」"

jump gakuen_peter2_7
label gakuen_peter2_7:

show girl_c2_4 at center
with dis
hide bor_m_02_1

hide per_m_01_8

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice mat_g0004
Seito "「い、いいんです……っ！\n
綺麗だったから、話しかけちゃって……」"

hide girl_c2_4
show girl_c2_4 at left
with dis

show girl_d1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice sam_g0004
Seito "「接触は嫌がられるって、聞いていたのに……。\n
ごめんなさい……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……ええ？\n
そんな……」"

hide girl_c2_4
show girl_c2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice mat_g0005
Seito "「私達が悪かったんです！\n
すいませんでした……！！！」"

hide girl_d1_1
show girl_d1_1 at center
with dis
hide girl_c2_1
show girl_c2_1 at left_center

show bor_m_01_10 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice bor_g0008
Boris "「……よしよし、美術館案内の続きは俺としようぜ？\n
あんな意地悪ウサギより、俺のほうが楽しませてやれると思うよ？」"

play sound se_0745
hide girl_d1_1

hide girl_c2_1

hide bor_m_01_10
pause .5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意図的に調子のいい声を出して、ボリスが少女達を誘導していく。\n
それを見送ってから、私はペーターへと視線を向けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……ペーター」"


show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pet_g0097
Peter "「はい？\n
なんですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私になんと声をかけてもらえるのかと、ペーターは弾むように問いかけてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「あなた……、あの子達に何をしたの？」"

hide per_m_02_8
show per_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice pet_g0098
Peter "「ああ、汚いから汚いと言っただけですよ？\n
僕にそちらの像についての解説を求めていたみたいですが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「どうして教えてあげないのよ」"

hide per_m_03_7
show per_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice pet_g0099
Peter "「……今の話を聞いたところによると、美術部らしいじゃありませんか。\n
一般の生徒に聞くなら、自分で調べるべきだと思いますけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「それは後から知ったことでしょう。\n
……それに断るにしたって、言い方ってものがあるわ」"

hide per_m_02_11
show per_m_01_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pet_g0100
Peter "「どうして僕が、あんな見ず知らずの連中のために解説してやらなければいけないんですか？あなたの命令でしたら、従いますけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……命令なんて、しないけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「でも、優しくしてあげなさいよ。\n
あの子達……、きっと新入生よ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアで話を聞いたように、在校生の間ではペーター＝ホワイトがどんな人間なのであるかというのはすでに知れ渡っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達が彼に声をかけたというのは、それを知らなかった可能性が高い。\n
もしかしたら、寮も違うのではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私と楽しげに話し、解説する姿を見て、おずおずと声をかけたのだとしたら……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……酷いわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしも自分だったらと思うだけで、胸が痛くなるような仕打ちだ。"

hide per_m_01_14
show per_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0101
Peter "「そうでしょうか。\n
興味のないものには、こんなものじゃないですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_3")
T "「私に対するときの半分でいいから、愛想よくしてあげればいいのに……」"

hide per_m_02_4
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_3")
voice pet_g0102
Peter "「そんなの、無理ですよ。\n
あなたは別格で、他の連中とはまったく違います」"

hide per_m_02_3
show per_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_3")
voice pet_g0103
Peter "「半分でも一割でも、同じ扱いにするなんてことは不可能ですよ。\n
僕はあなたにだけ、優しくしたいんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……私、だけ」"

hide per_m_03_6
show per_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pet_g0104
Peter "「ええ。\n
あなただけ、です」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは決して嫌な言葉ではない。\n
むしろ、普通なら言われて嬉しい言葉の部類になるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターが口にすると、本当に私だけだというのが分かる。\n
怖いぐらいに一途な彼が口にするそれは、疑いようのない「本当のこと」だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背筋が寒くなるほど、私だけ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……あんたって本当、アレよね」"

hide per_m_03_11
show per_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice pet_g0105
Peter "「なんです？\n
アレってなんですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「アレはアレよ。\n
……アレ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "輪郭をたどるように答えは見えているのに、その形をはっきりと言うことは出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "妄執の恋か。\n
執着か。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこまで重いものが自分に関わるとは、あまり実感もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……もう、いいわ。\n
ほら、次のを見に行きましょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誤魔化して、ペーターを促した。"

hide per_m_02_10
show per_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0106
Peter "「はいっ！\n
こうして、あなたと一緒に美術館巡りが出来るなんて、僕は幸せです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターはその赤色の双眸にうっとりとした色を浮べて夢見るように言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（綺麗だから話しかけちゃったって、言っていたな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "接触は嫌がられるって聞いていたのに、とも言っていた。\n
彼女達は新入生でも、ペーターについてまったく知らなかったわけではないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知っていても、おそるおそる話しかけてしまう。\n
それだけの魅力がある、綺麗な人。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（たしかに、綺麗だわ。\n
美術品の一つみたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな彼が、私にだけ優しくて、私だけを好き。\n
私だけが特別、なんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "明らかに異常だ。\n
それを受け入れている、私も。"

hide per_m_01_2
with dis
$ hi_mes()

scene bg22_ms_i_day with Dissolve(.8)

scene bg22_ms_o_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
jump gakuen_peter3
