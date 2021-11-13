
scene bg_map_day
with dis
label gakuen_friend_tower:
$ clockanim()


scene bg20_gd_day
with dis

play music gallery_front_day_p_wam

scene bg_par15_rg_tow_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その日、私は塔を訪れていた。"
if place_of_stay == "Castle":
    jump gakuen_friend_tower1a
if place_of_stay == "Hatter":
    jump gakuen_friend_tower1b
if place_of_stay == "Amuse":
    jump gakuen_friend_tower1c

label gakuen_friend_tower1a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディに頼まれ、書類を届けに来たのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は自治会の役員になったわけではないのだが、それでも赤薔薇寮に住む者として、そして自治会員として無理のない範囲で手伝おうとは思っている。"

jump gakuen_friend_tower2
label gakuen_friend_tower1b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドに頼まれ、書類を届けに来たのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は不良生徒の一員になるつもりはないが、全員が素行不良というわけでもない。\n
帽子屋寮に住む者として、寮長の頼みを聞くべきだろう。"

jump gakuen_friend_tower2
label gakuen_friend_tower1c:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに頼まれ、書類を届けに来たのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "担任ということもあってか、用事を言付かることも多い。"

jump gakuen_friend_tower2
label gakuen_friend_tower2:

scene bg25_rr_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなわけで、今回、簡単な書類の配達を引き受けたのだ。\n
届け先は、風紀委員長であるユリウスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ユリウスがいるのは……）"


play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段あまり足を踏み入れることのない他寮というのは、入学してからしばらく経った今でも新鮮だ。\n
記憶を辿りながら、廊下を歩いていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……と。"


show gre_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0258
Gray "「ナイトメア先生ー！！？\n
ナイトメア先生どこですかー！！？」"

play sound se_0417
hide gre_m_03_5
show gre_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0259
Gray "「今日中にチェックしてサインをいただかないと処理できない書類があるんです……！\n
隠れていないで出てきてください！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「…………。\n
……グレイ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "血相を変えたグレイが、ばたばたと早足で廊下をやってくるのが見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "足早に、それでも床に落ちているゴミ一つ見逃さないというような眼光の鋭さ。\n
周囲を確認しながら歩いてきた彼は、私の前で立ち止まる。"


hide gre_m_03_3
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0260
Gray "「ああ、君か。\n
……情けないところを見せてしまったな」"

hide gre_m_01_3
show gre_m_01_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0261
Gray "「塔の日常風景なので、気にしないでくれるとありがたい。\n
ところで、ナイトメア先生を見なかったか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "情けないそれが日常風景というのは、もっとまずいのではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（グレイ……、疲れているのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正常な判断がついていないように思える。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「見ていないわ。\n
私も、今来たところなの」"

hide gre_m_01_15
show gre_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice gra_g0262
Gray "「……そうか。\n
もしも見かけたら……」"

play sound se_0252
hide gre_m_02_10


scene m_cut_tou_friend_u
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice gra_g0263
Gray "「これを割ってくれないか。\n
飛んで駆けつけるから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと差し出されたのは、鶏のものよりも一回りほど小さい卵だった。"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "割ってしまわないように気をつけて受け取るものの、感触としてはつるりとしていて普通の卵よりも頑丈そうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ナイトメアを見つけたら、これを割ればいいのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（場所を知らせるためのアイテムなのかしら？）"


scene m_cut_tou_friend
with dis

show gre_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_g0264
Gray "「ああ、頼む。\n
容赦のひとかけらも与えず、躊躇いなく割ってほしい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「……わ、分かったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（グレイ……、目、据わってない？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「深刻なのね？」"

hide gre_m_03_9
show gre_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice gra_g0265
Gray "「ものすごく……、仕事が溜まっているんだ。\n
それはもう……、ものすごく」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……一体、どれだけの仕事を溜めているのだろうか。\n
他人事ながら、同情してしまいたくなる。"


scene bg25_rr_day
with dis
hide gre_m_03_3
show gre_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0266
Gray "「ところで、君はどうしてここに？\n
塔に、何か用か？」"
if place_of_stay == "Castle":
    jump gakuen_friend_tower3a
if place_of_stay == "Hatter":
    jump gakuen_friend_tower3b
if place_of_stay == "Amuse":
    jump gakuen_friend_tower3c
label gakuen_friend_tower3a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ああ、ビバルディにお使いを頼まれたの。\n
これをね、ユリウスに届けてほしいんですって」"

play sound se_0472
hide gre_m_02_10
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0267
Gray "「ああ、自治会から風紀委員への書類か。\n
お使い、ご苦労様」"

hide gre_m_01_3
show gre_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0268
Gray "「……届けにきてくれたのが君でよかった。\n
君の寮の風紀委員……、エースが来ると妙に絡まれて大変なんだ」"

jump gakuen_friend_tower4
label gakuen_friend_tower3b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ああ、ブラッドにお使いを頼まれたの。\n
これをね、ユリウスに届けてほしいんですって」"

play sound se_0472
hide gre_m_03_11
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0269
Gray "「ああ、ブラッド＝デュプレから風紀委員長への書類か。\n
お使い、ご苦労様」"

hide gre_m_01_3
show gre_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0270
Gray "「……反省文か始末書の類だろうな\n
彼らには、もう少しおとなしくしていてほしいものだ」"

jump gakuen_friend_tower4
label gakuen_friend_tower3c:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ああ、ゴーランドにお使いを頼まれたの。\n
これをね、ユリウスに届けてほしいんですって」"

play sound se_0472
hide gre_m_03_11
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0271
Gray "「ああ、ゴーランド先生から風紀委員長への書類か。\n
お使い、ご苦労様」"

hide gre_m_01_3
show gre_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0272
Gray "「……リサイタルの許可ならしかねると、前から何度も言っているんだが。\n
そのたびに、何人も病人が出て、ここに担ぎ込まれる……」"

jump gakuen_friend_tower4
label gakuen_friend_tower4:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……気苦労が多そうね」"

hide gre_m_03_11
show gre_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice gra_g0273
Gray "「いや、仕事だから……」"

hide gre_m_03_11
show gre_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice gra_g0274
Gray "「それでは、俺は、ナイトメア先生を捕獲……、じゃないな、探しにいってくるとする。\n
委員長の居場所は分かるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「いえ、今から探してみようと思っていたところよ」"

hide gre_m_01_12
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice gra_g0275
Gray "「ああ、それならちょうどよかった。\n
委員長なら、医務室にいる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ありがとう、グレイ。\n
あなたの健闘も祈るわ」"

show gre_m_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gra_g0276
Gray "「……ありがとう。\n
君は優しい子だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイはしみじみと呟いて、それから再び足早にナイトメア探索のため去っていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "探す、というよりもぽろりと漏れた本音からして、捕獲のほうが正解なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……早く、ナイトメアが捕まりますように）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイのためにもそう祈って（ナイトメアにとっては呪いだろうが）、私は再び医務室に向けて歩き始めた。"

hide gre_m_01_3
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0302
pause .15
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice jul_g0317
Julius "「開いている」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「入るわよ？」"

play sound se_0285

scene bg_par16_rs_tow_day
with stripe_l_long

play music drawingroom_day_p_wam
play sound se_0717
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "医務室へと足を踏み入れた。\n
ユリウスは以前と同じく、机の上に腰掛けて、なにやらぱらぱらと書類をめくっている。"


show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0318
Julius "「……おまえか。\n
どうした？ナイトメアに用か？」"
if place_of_stay == "Castle":
    jump gakuen_friend_tower5a
if place_of_stay == "Hatter":
    jump gakuen_friend_tower5b
if place_of_stay == "Amuse":
    jump gakuen_friend_tower5c
label gakuen_friend_tower5a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いいえ、ビバルディから頼まれ物で、あなたに書類を届けにきただけよ。\n
グレイから、あなたがここにいるって聞いて来たの」"

jump gakuen_friend_tower6
label gakuen_friend_tower5b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いいえ、ブラッドから頼まれ物で、あなたに書類を届けにきただけよ。\n
グレイから、あなたがここにいるって聞いて来たの」"

jump gakuen_friend_tower6
label gakuen_friend_tower5c:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いいえ、ゴーランドから頼まれ物で、あなたに書類を届けにきただけよ。\n
グレイから、あなたがここにいるって聞いて来たの」"

jump gakuen_friend_tower6
label gakuen_friend_tower6:
hide yuri_m_02_9
show yuri_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice jul_g0319
Julius "「書類……。\n
ああ、あの件か」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し考える間を挟んで、ユリウスはその書類の内容に思い当たったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「私は運ぶだけだから、内容については分からないわ。\n
受け取ってもらえる？」"

hide yuri_m_02_10
show yuri_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice jul_g0320
Julius "「ああ。\n
私にとっても必要なものだからな」"

hide yuri_m_02_11
if place_of_stay == "Castle":
    jump gakuen_friend_tower7a
if place_of_stay == "Hatter":
    jump gakuen_friend_tower7b
if place_of_stay == "Amuse":
    jump gakuen_friend_tower7c
label gakuen_friend_tower7a:
play sound se_0472
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はユリウスの元へと歩み寄ると、赤薔薇寮より持ってきた封筒を差し出した。\n
自治会の紋章が封に押されている。"

play sound se_0740
show white with Dissolve(.1)
hide white

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスがその紋章の上に指を滑らせると、それに反応したよう紋章の薔薇の花がはらはらと散って封印が解けた。"

jump gakuen_friend_tower8
label gakuen_friend_tower7b:
play sound se_0472
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はユリウスの元へと回り込むと、帽子屋寮より持ってきた封筒を差し出した。\n
ブラッドが好んで使う、帽子をあしらった封印が押されている。"

play sound se_0740

show white with Dissolve(.1)
hide white

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスがその紋章の上に指を滑らせると、それに反応したよう紋章の帽子がすうっと薄くなって消えていった。"

jump gakuen_friend_tower8
label gakuen_friend_tower7c:
play sound se_0472
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はユリウスの元へと回り込むと、遊園地寮より持ってきた封筒を差し出した。\n
落書きのような、可愛らしい猫の封印が押されている。"

jump gakuen_friend_tower8
play sound se_0740

show white with Dissolve(.1)
hide white

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスがその封印の上に指を滑らせると、それに反応したよう紋章の猫がすうっと薄くなって消えていった。"

label gakuen_friend_tower8:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "封筒の中に入っていた書類を取り出し、その内容をぱらぱらっと確認してユリウスが頷く。どうやら目的のもので当たっていたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ運んだだけとはいえ、私としてもよかったと思える。"


show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0321
Julius "「……それで。\n
どうなんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「いや、だから私は中身については知らないって言っているじゃない」"

hide yuri_m_03_9
show yuri_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice jul_g0322
Julius "「書類のことではない。\n
おまえは……」"

play sound se_0078

show white with Dissolve(.1)
if place_of_stay == "Castle":
    jump gakuen_friend_tower9a
if place_of_stay == "Hatter":
    jump gakuen_friend_tower9b
if place_of_stay == "Amuse":
    jump gakuen_friend_tower9c
label gakuen_friend_tower9a:
hide yuri_m_01_13
show yuri_m_01_13 at left ##instant

show nai_m_02_1 at right ##instant
hide white with Dissolve(.5)
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice nig_g0367
Nightmare "「ふふ。\n
委員長は、君が赤薔薇寮で問題なく過ごせているのかを聞いているんだよ」"

jump gakuen_friend_tower10
label gakuen_friend_tower9b:
hide yuri_m_01_13
show yuri_m_01_13 at left##instant]
hide nai_m_02_1
show nai_m_02_1 at right##instant]
##[cg time="500"]
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice nig_g0368
Nightmare "「ふふ。\n
委員長は、君が帽子屋寮で問題なく過ごせているのかを聞いているんだよ」"

jump gakuen_friend_tower10
label gakuen_friend_tower9c:
hide yuri_m_01_13
show yuri_m_01_13 at left ##instant
hide nai_m_02_1
show nai_m_02_1 at right ##instant
hide white with Dissolve(.5)
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice nig_g0369
Nightmare "「ふふ。\n
委員長は、君が遊園地寮で問題なく過ごせているのかを聞いているんだよ」"

jump gakuen_friend_tower10
label gakuen_friend_tower10:
play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ナイトメア……！！\n
いきなり出てこないでよ、心臓に悪いわ」"

play sound se_0216
hide nai_m_02_1
show nai_m_01_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice nig_g0370
Nightmare "「空間魔法は私の特技だからな。\n
特技は活用しなければ」"

hide yuri_m_01_13
show yuri_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jul_g0323
Julius "「何が活用だ。\n
どうせまた、補佐から逃げているんだろう」"

hide nai_m_01_1
show nai_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice nig_g0371
Nightmare "「そ、そんなことはな……」"

play sound se_0053
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice gra_g0277
Gray "「ナイトメア先生ーー！どこにいらっしゃるんです！？\n
決算書は今日までなんですよ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠くから、グレイの悲痛な声が聞こえた。"

play sound se_0697
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_16")
T "「…………」"

hide yuri_m_02_8
show yuri_m_03_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とユリウスは、冷たい視線をナイトメアへと向ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "空間移動なんていう強力な魔法をこんなに無造作に使ってみせるあたり、さすがシンフォニアの学校医だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通ならば媒介としての魔法陣や、杖、呪文詠唱を必要とするはずだが、ナイトメアにそういった媒介を使用した気配はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（呼吸するように軽々と……、いや。\n
……呼吸のほうが難易度高いかもしれないわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ相手は病弱極まりないナイトメアだ。\n
ちょっとした動揺ですら咳き込み、あまつさえ吐血までするらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（優秀な魔法使いなのに、なんて情けない人なの……）"

hide nai_m_02_10
show nai_m_03_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice nig_g0372
Nightmare "「私のことより！聞いていたぞ、委員長！？\n
さりげない親切でポイントアップ、抜け駆けをしようなんておまえもなかなかやるじゃないか」"

hide nai_m_03_10
show nai_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice nig_g0373
Nightmare "「おまえが女子生徒に親切にしようとしているところなんて、私は初めて見たぞ。\n
ふふふふ、いいものを見た」"

hide yuri_m_03_12
show yuri_m_03_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Julius "「…………」"

hide yuri_m_03_13
show yuri_m_02_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice jul_g0324
Julius "「……親切などしていない。\n
ただ、様子を聞こうとしていただけで……」"

hide nai_m_03_11
show nai_m_02_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice nig_g0374
Nightmare "「それ！それが珍しいんだ！\n
おまえにしては珍しすぎる！」"

hide yuri_m_02_11

hide nai_m_02_3

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアが、好き勝手言っている。\n
私は、そっと片手を制服のポケットの中にいれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこには、先ほどグレイから渡された卵が入っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（確か、これを……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「ひとかけらの容赦も与えることなく、そして躊躇うこともなく……。\n
{size=+20}投げつける！！{/size}」"

play sound se_0703
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はその卵を思いっきり振りかぶると、ナイトメアめがけて投げつけた。"

play sound se_0309

show nai_m_03_3 at center
with dis
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0375
Nightmare "{size=+20}「ごぐふ……っ！！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……この使い方でいいのよね？）"

play sound se_0768
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "卵は見事ナイトメアの頬に着弾したようだ。\n
ナイトメアが奇妙な声をあげると同時に、卵が割れる。"

play sound se_0724
hide nai_m_03_3

show white onlayer master with expand
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まばゆい光が医務室内に満ちた。"


scene m_cut_tou_friend2_u ##instantPAY ATTENTION="true"]
hide white

play sound se_0129
pause .1
play sound se_0129
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして次の瞬間、けたたましいほどのひよこの鳴き声が響きわたる。\n
光が収まった後、医務室に中には数十羽にもおよぶ黄色いひよこの大群がいた。"

play sound se_0129
pause .1
play sound se_0129
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わらわらとナイトメアにたかっては、ものすごい音量の鳴き声をあげている。"

play sound se_0129
pause .1
play sound se_0129

scene m_cut_tou_friend2
with dis

show yuri_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0325
Julius "「う、うるさい……！\n
なんなんだ、これは！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「さあ、なんだかは知らないけど……！\n
ナイトメアに会ったらぶつけろってグレイに渡されたのっ」"

hide yuri_m_02_7
show yuri_m_02_7 at left
with dis

show nai_m_03_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice nig_g0376
Nightmare "「グレイ！？グレイだと！？\n
君までがグレイの手先だとは……！」"

play sound se_0129
pause .1
play sound se_0129
hide nai_m_03_7
show nai_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice nig_g0377
Nightmare "「い、痛い……っ、そしてうるさい……！\n
こんなに騒がれては……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは警戒するようにひよこの群れから離れるが、ひよこたちはそんなナイトメアの後について移動する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、小さなくちばしでナイトメアをつんつん突っつく。"

play sound se_0129
pause .1
play sound se_0129
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴよぴよぴよぴよ。\n
その間も彼らは鳴きっぱなしだ。"

hide yuri_m_02_7
show yuri_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0326
Julius "「な、ナイトメア、おまえとりあえずこの部屋から出て行け……！！\n
うるさくてかなわん……！！」"

hide nai_m_02_10
show nai_m_03_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0378
Nightmare "「どうして私が出て行かなければいけないんだっ！？\n
ここは医務室で私の部屋のようなもの……」"

hide yuri_m_03_7
show yuri_m_01_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0327
Julius "「うるさいからに決まっているだろう！\n
ぴよぴよぴよぴようるさいんだ……！！！」"

play sound se_0417
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……足音？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴよぴよとうるさいひよこの鳴き声に混じって、足音が聞こえてくる。"

play sound se_0291
camera at hpunch
camera at vpunch

scene bg_par16_rs_tow_day
with dis
hide yuri_m_01_13

hide nai_m_03_8

##[rchara1 PAY ATTENTION="false"]
show gre_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0278
Gray "「ナイトメア先生……！！\n
ようやく見つけましたよ！！」"

hide gre_m_03_5
show gre_m_03_5 at left
show nai_m_03_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0379
Nightmare "「げげげげげっ！！\n
何故ここが分かったんだ！？」"

hide gre_m_03_5
show gre_m_01_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0279
Gray "「ふふ、そのひよこ探知機のおかげですよ……。\n
彼女に、あなたを見つけたら発動させるように頼んでおいたんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……あれ？\n
投げつけるように、じゃなかったっけ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアにぶつけるよう依頼された気になっていたが、それはどうやら私の気のせいだったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……まあ、なんにしても発動しているのならいいか）"

play sound se_0129
pause .1
play sound se_0129

show yuri_m_01_8 at center
with dis
hide gre_m_01_1

hide nai_m_03_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice jul_g0328
Julius "「おい、トカゲっ。\n
そのうるさいひよこをさっさと黙らせろ！」"


show gre_m_03_1 at center
with dis
hide yuri_m_01_8

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice gra_g0280
Gray "「そうか？\n
この鳴き声も愛らしくていいと思ったんだが……」"

play sound se_0726

show magic_b onlayer master with Dissolve(1.5)
hide gre_m_03_1
show gre_m_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
Gray "「…………」"

hide magic_b
show m_cut_tou_friend2_u onlayer master
with dis
play sound se_0129
pause .1
play sound se_0129
pause .5
play sound se_0740
hide m_cut_tou_friend2_u
show white onlayer master with spread
hide white with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの呪文詠唱に合わせて、ぴよぴよと騒がしかったひよこ達はすぅっと光になって消えていった。"

play sound se_0051
hide gre_m_01_13
show gre_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0281
Gray "「さ、捕まえましたよ、ナイトメア先生。\n
書類チェックと、サインをお願いします」"

hide gre_m_01_1
show gre_m_01_1 at left
show nai_m_03_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0380
Nightmare "「おまえ……、あんな妙なマジックアイテムどこで手に入れてきたんだ。\n
ぴよぴよぴよぴよ……、ああ、頭痛がしてきた」"

hide gre_m_01_1
show gre_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0282
Gray "「通販です。\n
あまりの愛らしさに即決で購入したんですが……、可愛い上に役に立つとは素晴らしい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「……{size=+20}通販？{/size}」"

hide gre_m_02_2
show gre_m_03_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_6")
voice gra_g0283
Gray "「ああ、いいものが見つかりやすい」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（通販、か……。\n
たまに、妙なの売っているわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いいものというよりは、妙なもの、だ。\n
まさか、先刻のが通販グッズだとは……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_3")
T "（……後で、どういう業者か教えてもらおう）"

hide gre_m_03_10
show gre_m_03_4 at center
with dis
hide nai_m_03_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_3")
voice gra_g0284
Gray "「協力、ありがとう。\n
君のおかげで捕まえられた、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアをしっかりと捕獲し、その腕を捕まえてようやくグレイは一息つけたようだ。\n
表情を緩めて私へと視線を流す。"
if place_of_stay == "Castle":
    jump gakuen_friend_tower11a
if place_of_stay == "Hatter":
    jump gakuen_friend_tower11b
if place_of_stay == "Amuse":
    jump gakuen_friend_tower11c
label gakuen_friend_tower11a:
hide gre_m_03_4
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0285
Gray "「巻き込んで悪かったな。\n
君は……、赤薔薇寮に滞在しているんだったか？」"

hide gre_m_01_3
show gre_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0286
Gray "「何か、困っていることはないか？\n
俺に何か手助け出来ることがあれば……」"

jump gakuen_friend_tower12
label gakuen_friend_tower11b:
hide gre_m_01_4
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0287
Gray "「巻き込んで悪かったな。\n
君は……、帽子屋寮に滞在しているんだったか？」"

hide gre_m_01_3
show gre_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0288
Gray "「何か、トラブルに巻き込まれたりはしていないか？\n
俺に何か手助け出来ることがあれば……」"

jump gakuen_friend_tower12
label gakuen_friend_tower11c:
hide gre_m_01_4
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0289
Gray "「巻き込んで悪かったな。\n
ああでも、遊園地寮に滞在している君にはこの手のトラブルは慣れっこか……」"

hide gre_m_01_3
show gre_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0290
Gray "「あそこは楽しくて賑やかな場所だが、騒ぎも多いからな。\n
俺に何か手助け出来ることがあれば……」"

jump gakuen_friend_tower12
label gakuen_friend_tower12:
hide gre_m_01_4
show gre_m_01_4 at left
with dis

show nai_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0381
Nightmare "「そうか、人助けがしたいか、グレイ。\n
それならば、まずこの手を離して私を助けてくれ」"

hide gre_m_01_4
show gre_m_01_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0291
Gray "「却下です。\n
俺は彼女に聞いているんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは親切だ。\n
同寮というわけでもないのに……、いや、同寮でないからこそ、心配してくれているのだろう。"
if place_of_stay == "Castle":
    jump gakuen_friend_tower13a
if place_of_stay == "Hatter":
    jump gakuen_friend_tower13b
if place_of_stay == "Amuse":
    jump gakuen_friend_tower13c
label gakuen_friend_tower13a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「大丈夫よ。\n
赤薔薇寮の使用人達も、皆親切にしてくれているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幼馴染のペーターだけでなく、ビバルディやエースといった赤薔薇寮の幹部も親切だ。\n
……過剰なほどに。"

jump gakuen_friend_tower14
label gakuen_friend_tower13b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「大丈夫よ。\n
帽子屋寮の使用人達も、皆親切にしてくれているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人達だけでなく、ブラッドやエリオット、双子達といった帽子屋寮の幹部も親切だ。\n
……ちょっと怖くなるときもあるが。"

jump gakuen_friend_tower14
label gakuen_friend_tower13c:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「大丈夫よ。\n
遊園地寮の使用人達も、皆親切にしてくれているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人達だけでなく、ゴーランドやピアス、ボリスといった遊園地寮の皆も親切だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……騒々しすぎるという点では否定できないが。"

jump gakuen_friend_tower14
label gakuen_friend_tower14:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らに対して、愛着がわいてきている。\n
もちろんその他の一般の生徒達にも、だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「外から見るより、住みやすい場所なの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の言葉に、グレイが安堵したように微笑む。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_8")
T "（……親切な人だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他寮の生徒にすぎない私のことを、こんなにも気遣ってくれている。"

hide nai_m_02_10
show nai_m_03_10 at center
with dis
hide gre_m_01_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0382
Nightmare "「ああ、そうだ……！\n
せっかく塔に来てくれたんだ、もてなさなければならないよな！？」"

hide nai_m_03_10
show nai_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0383
Nightmare "「塔の主たるもの、客人の一人に茶の一杯も振る舞わないのはどうかと思うぞー！？\n
というわけで、お茶会をしよう、お茶会、珈琲ブレイクだ！」"

hide nai_m_03_1
show nai_m_03_1 at left
with dis

show yuri_m_01_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0329
Julius "「おまえは年がら年中ブレイク中だろう。\n
ああ、そうだ。私達でブレイクしてくるから、おまえは溜めた仕事を片付けたらどうだ？」"

hide nai_m_03_1
show nai_m_03_1 at center
with dis

show gre_m_02_12 at left_center
hide yuri_m_01_13
show yuri_m_01_13 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0292
Gray "「それはいい考えだな、委員長。\n
さ、ナイトメア先生、あなたは執務机へと……」"

hide nai_m_03_1
show nai_m_03_3 at center
with dis
hide gre_m_02_12

hide yuri_m_01_13

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0384
Nightmare "{size=+20}「ちょっと待てええええええ！！\n
それはどんなイジメだ！！？」{/size} "

hide nai_m_03_3
show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0385
Nightmare "「どうして私がおまえたちが楽しく休憩している間に、一人で真面目に働かなければいけないんだ！？」"

hide nai_m_02_10
show nai_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0385_5
Nightmare "「不公平だろう！！？教育という観点からみても、仲間はずれはよくない！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「……先生のくせに、教育が必要なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_16")
T "（指導する立場でしょうに）"

hide nai_m_01_12
show nai_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_16")
voice nig_g0386
Nightmare "「う……！？」"

hide nai_m_02_9


show gre_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_16")
voice gra_g0293
Gray "「日頃不公平なほどに、あなたの尻拭いをさせていただいているので……。\n
たまには俺の気持ちも分かってもらえればと」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「そうね、働きなさいよ。\n
普段サボっているからこういうことになるのよ？」"

hide gre_m_01_5
show gre_m_01_5 at left
with dis

show nai_m_03_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice nig_g0387
Nightmare "「うう、[firstname]！君まで私を見捨てるのか！\n
酷いぞ！！」"

hide gre_m_01_5
show gre_m_01_5 at left_center
hide nai_m_03_6
show nai_m_03_6 at center
with dis

show yuri_m_03_12 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice jul_g0330
Julius "「酷くないだろう、怠け者の節句働き、という言葉があるのを知っているか？\n
日頃怠けていると、皆が祭りを楽しむ日に働くハメになる、という意味の言葉だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_4")
T "「勉強になるわね、ナイトメア」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これぞ、教育的指導だ。"

hide nai_m_03_6
show nai_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0388
Nightmare "「嫌だ！！！\n
私も君とお茶をする！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_3")
T "「でも、仕事が溜まっているんでしょう？」"

hide nai_m_03_2
show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_3")
voice nig_g0389
Nightmare "「そんなことは……っ！」"

hide gre_m_01_5
show gre_m_03_8 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_3")
voice gra_g0294
Gray "「ありますとも。\n
あなたの机の上に詰まれた書類の束が見えないとは言わせませんよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイが釘を刺すように言う。\n
うううっ、と分かりやすくナイトメアの目が泳いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……まるで子供よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そしてユリウスとグレイときたら、その保護者のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "宿題をやりたがらない子供に罰を与えると同時に、その宿題に取り組むモチベーションを上げようとするような……。"

hide yuri_m_03_12
show gre_m_03_8 at left_center
hide gre_m_03_8
show nai_m_01_4 at center
with dis
hide nai_m_02_10
show yuri_m_03_12 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0390
Nightmare "「[firstname]、君、今何か失礼なことを考えていなかったかっ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「考えていないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは子供そのもののくせに、こちらの心を読んでいるのではないかと思うほど鋭い。"

hide gre_m_03_8
show gre_m_02_2 at left
with dis
hide yuri_m_03_12
show yuri_m_03_12 at right
with dis
hide nai_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0295
Gray "「では、メイドに休憩の準備をさせよう。\n
委員長、おまえは珈琲でよかったか？」"

hide yuri_m_03_12
show yuri_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0331
Julius "「ああ。\n
私は珈琲がいい」"


show nai_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0391
Nightmare "「私はココアがいいぞ！」"
if place_of_stay == "Castle":
    jump gakuen_friend_tower15a
if place_of_stay == "Hatter":
    jump gakuen_friend_tower15b
if place_of_stay == "Amuse":
    jump gakuen_friend_tower15c
label gakuen_friend_tower15a:
hide gre_m_02_2
show gre_m_02_11 at left
with dis
hide nai_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0296
Gray "「君は何がいい？\n
紅茶……、だと赤薔薇寮には勝てそうにないな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_1")
T "「ふふ、そうね。\n
それじゃあ、ココアをお願いしようかしら」"

hide gre_m_02_11
show gre_m_03_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_1")
voice gra_g0297
Gray "「そうか、分かった。\n
君はココアだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの言葉に頷く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶に関して、赤薔薇寮に勝てる、もしくは並ぶことが出来るのは、同じく紅茶好きで有名なブラッドが寮長を務めている帽子屋寮ぐらいだろう。"

jump gakuen_friend_tower16
label gakuen_friend_tower15b:
hide gre_m_03_4
show gre_m_02_11 at left
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0298
Gray "「君は何がいい？\n
紅茶……、だと帽子屋寮には勝てそうにないな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_1")
T "「ふふ、そうね。\n
それじゃあ、ココアをお願いしようかしら」"

hide gre_m_02_11
show gre_m_03_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_1")
voice gra_g0297
Gray "「そうか、分かった。\n
君はココアだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの言葉に頷く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶に関して、帽子屋寮に勝てる、もしくは並ぶことが出来るのは、同じく紅茶好きで有名なビバルディが寮長を務めている赤薔薇寮ぐらいだろう。"

jump gakuen_friend_tower16
label gakuen_friend_tower15c:
hide gre_m_03_4
show gre_m_02_9 at left
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0299
Gray "「君は何がいい？\n
普段遊園地寮ではどんなものを飲んでいるんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_1")
T "「遊園地寮だと、冷たいソーダが多いわね。\n
でも今日は気分を変えて……、温かいココアをもらえる？」"

hide gre_m_02_9
show gre_m_03_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_1")
voice gra_g0297
Gray "「そうか、分かった。\n
君はココアだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの言葉に頷く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段は冷たいドリンクばかり飲んでいるのだから、たまにはホットドリンクも悪くない。"

jump gakuen_friend_tower16
label gakuen_friend_tower16:

show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0392
Nightmare "「私もココアがいいぞ！\n
聞いているのか、グレイ！！」"

hide gre_m_03_4
show gre_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイはにこやかに穏やかに、聞こえないフリをする。"

hide yuri_m_01_2
show yuri_m_02_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0332
Julius "「さっさと仕事を終わらせてから来い。\n
……おまえは鬱陶しいんだ」"

hide nai_m_02_10
show nai_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0393
Nightmare "「あれがそんな短時間で終わる量か！！？\n
無理だ！！あれを片付けてから参加だなんて、絶対にむーりーだー！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……そんなすごい量を溜めていたのね、あなた」"

hide gre_m_01_3
show gre_m_03_3 at left
with dis
hide nai_m_02_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice gra_g0300
Gray "「……はあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "憂鬱そうにグレイが溜息をついた。\n
その苦労が偲ばれる。"

hide gre_m_03_3

hide yuri_m_02_11

play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達は、それぞれちらりと視線をナイトメアに向けた後、ぞろぞろと休憩のために移動をしはじめた。"


show nai_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0394
Nightmare "「ま、待ってくれ！\n
本当に置いていくのか！？私だけ仕事しろというのか！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……せめて目の前で休憩するのは避けてあげようという配慮よ、配慮」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中からナイトメアの声が聞こえるが、気にしてはいけない。\n
たまにはこれぐらい厳しくしたほうがいい薬だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちら、と視線をやると、グレイとユリウスも同じことを考えているようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「……ふ」"

hide nai_m_03_3


show gre_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice gra_g0301
Gray "「はは」"

hide gre_m_03_4
show gre_m_03_4 at left
with dis

show yuri_m_02_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice jul_g0333
Julius "「……くく」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことに気づいたら、思わず笑ってしまっていた。\n
私達三人は笑いながら歩く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっとナイトメアは、泣き落としで休憩に混じってくるか、また逃げ出そうとするだろうが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_3")
T "（三人もいるんだから、逃げきれないわよ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真面目で落ち着いた塔、なんていう評価とは違った一面を見てしまった。"

hide gre_m_03_4

hide yuri_m_02_1
##[chara3 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_tow_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_long
jump gakuen_friend_end
