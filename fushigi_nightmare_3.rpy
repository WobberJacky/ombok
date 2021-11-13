jump fushigi_common3_hatter
label fushigi_nightmare3_1:

scene map_bg_autumn_day with stripe_l_medium

scene b_aut_01 with stripe_l_medium

scene br_01 with stripe_l_long

play music hatter_corridor_p_ali

show bra_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice blo_f0342
Blood "「やあ、お嬢さん。\n
この前のエリオットとのデートは楽しかったかな？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「あなたって、一体いくつ目と耳があるの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（耳聡いというべきか、変なタイミングで出てくるというか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋屋敷のドアの前でエリオットを待っていたら、ブラッドが現れた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お茶会でもないのに、ブラッドが昼の時間帯に出てくるなんて珍しい。\n
そう思ったら、どうやら彼は私をからかいに来ただけのようだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（忙しいのに、暇そうに見せたがるブラッドらしいといえばらしいけど）"

hide bra_t_02_8
show bra_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice blo_f0343
Blood "「ふふふ、おかしなことを言う。\n
私の持っている目と耳なんて、君に見える範囲だけさ」"

hide bra_t_02_1
show bra_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice blo_f0344
Blood "「私は……、君のところの夢魔とは違うのでね。\n
見えないものにまで手を出すような器用さも、業も、持ち合わせてはいない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「何が言いたいの？」"

play sound se_0313
hide bra_t_03_4
show bra_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice blo_f0345
Blood "「いや、そんなにエリオットと仲がいいのなら、あいつに乗り換えるのもいい手だと思ってね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……は？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（乗り換える？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おもむろに肩へ手を置かれて、首を傾げる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "話の流れからすると、私がナイトメアからエリオットに乗り換えると言いたいのだろうが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（あり得ないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットとは仲がいいが、友人の一人だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恋愛対象として、最初から見ていない。\n
それは私もエリオットも同じだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「エリオットは、私に対してそういう気持ちを持っていないでしょう。\n
馬鹿なことを言わないでよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "分かっているくせに、あえて言っているであろう相手に溜息をつく。"

hide bra_t_03_9
show bra_t_03_18 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0346
Blood "「ふむ……。\n
まあ、君がそう言うのならそれはそれで構わないが……」"

hide bra_t_03_18
show bra_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0347
Blood "「君が屋敷に滞在してくれるのなら、塔と事を構えるのも悪くないと思ったんだがね」"

hide bra_t_03_6
show bra_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0348
Blood "「少なくとも、退屈はしない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「暇潰しに人を巻き込まないで」"

play sound se_0108
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本心の読めない言葉に、肩にかけられた手を振り払う。面白いかどうかで物事を判断するマフィアのボスなんて、相手にしたほうが負けだ。"

hide bra_t_03_10
show bra_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0349
Blood "「おや、残念だ。\n
機嫌を損ねてしまったかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……私がここにずっといるなんて思っていないのに、悪ふざけがすぎるわ」"

play sound se_0584
hide bra_t_01_8
show bra_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Blood "「…………」"

hide bra_t_01_4
show bra_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice blo_f0350
Blood "「ふむ、君がそう言うならそういうことにしておこうか。\n
お迎えが来たようだし、行ってくるといい、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「……だから、デートじゃないって言っているのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が指差した方向には、見慣れた長い耳と、大きな身体。"


hide bra_t_01_2
show bra_t_01_2 at left
show eri_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0251
Elliot "「[firstname]、待たせたな！\n
さ、行こうぜ」"

hide bra_t_01_2
show bra_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0351
Blood "「それでは、うちのウサギとのデートを楽しんでおいで、お嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（しつこいわね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（デートと言い張るし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にやにやとした顔を見ていると、思わず足を踏んでやりたくなる。"

hide eri_t_01_4
show eri_t_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot "「？？」"

hide eri_t_01_5
show eri_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0252
Elliot "「何かあったのか、二人とも？」"

hide bra_t_03_9
show bra_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0352
Blood "「いや、何もないさ。\n
お嬢さんを任せるぞ、エリオット」"

hide eri_t_02_11
show eri_t_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0253
Elliot "「ああ、分かった。\n
任せてくれよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの言葉の意図が分かっているのかいないのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼を心の底から尊敬しているエリオットには、任されたという事実のみが大切なのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "胸を張って声に応じていた。"

hide eri_t_02_1
show eri_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0254
Elliot "「じゃ、行こうぜ、[firstname]！\n
今度はまた別のところに案内してやるから」"

play sound se_0492
hide eri_t_01_3

hide bra_t_03_4

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「あ、わ……っと」"

play sound se_0773
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引っぱる手につられて、私まで走り出してしまう。"


show bra_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

hide bra_t_03_3

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後で笑う気配がしたので振り返ったが、もうそこにブラッドの姿は見えなかった。"


$ hi_mes()

scene br_01
with stripe_l_medium

scene b_aut_01
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_medium

scene bg_gen05_sm_aut
with stripe_l_long
play sound se_0483
pause 1
play sound se_0698

play music cheerful_a_ali

show t_nai3_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice eri_f0255
Elliot "「いやっほー！\n
ははは、気持ちいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

play sound se_0040
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「エ、エリオット……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice eri_f0256
Elliot "「ん？何だよ、[firstname]。\n
しっかり掴まっていないと落ちるぜ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それは分かっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットは前回同様、全力疾走、どうしてこの速度で自転車にわざわざ乗りたがるのか分からないような速さで漕いでいるのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（その不条理さは、この際目を瞑るけど……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「私が言いたいのは……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「どうして、こんなに岩がごろごろしているような場所を{size=+25}自転車が走れるのかっていうところよ！？{/size}」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice eri_f0257
Elliot "「何でって……、そりゃあ俺が頑張って漕いでるから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「そういう問題じゃないっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどから、がたがたと揺れる自転車から振り落とされないように必死だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0258
Elliot "「細かいことを気にするなよ。\n
いいだろ、走れているんだから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（このウサギは……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "信じられないことに、エリオットは本当に自分の脚力だけで、この岩場としかいえないような場所を突き進んでいるのだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0259
Elliot "「まあ確かに少し揺れるけど。\n
これぐらい大したことじゃないだろ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「大したことあるわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（気を付けないと、話しているときに舌を噛みそうになるし）"

play sound se_0040
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二つの車輪から伝わってくる振動は、かなり激しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この前もエリオットにしがみついていたが、今回は相手のことを考えず力任せに掴んでいないと、落ちてしまいそう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（横座りじゃなくて、きちんと正面から座ればよかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今更自分の体勢を後悔したが、こんな足場の悪いところで立ち上がるのは自殺行為以外の何ものでもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（案内してくれるっていうのに、邪魔するのも悪いし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これが悪意だったらすぐに止めているが、好意だと分かるので、何も言えない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「……そういえば、私、まだ目的地を聞いていないんだけど。\n
一体どこに連れて行ってくれる気なの、エリオット？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice eri_f0260
Elliot "「どこって……、特に目的地があるわけじゃないぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「は？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice eri_f0261
Elliot "「だから、特に行きたい場所があるわけじゃねえんだ。\n
ただ何となく、ぶらぶらしているだけで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "{size=+25}（ただ何となくで通る道なの、これが！？）{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドが言うなら疑うのだが、エリオットはこんな手の込んだ嫌がらせをするような人ではないから……、本気のようだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0262
Elliot "「あんたもこの世界に来て、結構経つだろう？\n
うちの領地だって、回っているし」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……それは、勿論、あちこち見させてもらっているけど。\n
でも、ちゃんとブラッドにも許可を取っているわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "右も左も分からない、文字通りの余所者が領土内を歩くのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "特に帽子屋屋敷の中はマフィアの本拠地、ボスにきちんと話を通すのは当然のことだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0263
Elliot "「ああ、それは分かってるんだけどさ。\n
なんていうのか……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0264
Elliot "「そんなあんたを普通のところに連れていってもつまらないだろうし」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0265
Elliot "「俺、ガキどもやブラッドみたいに要領よくないから、いつもあんたにご馳走してもらったりしてばっかりだろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0266
Elliot "「だから、あんたが一人じゃ行きそうもないところを案内してやりたかったんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0266_5
Elliot "「俺らの領地で、あんたの知らない場所がまだこんなにあるって教えてやりたくてさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "意外な言葉に声を失う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（私のため……、ね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は精一杯、私を楽しませようとしてくれていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0267
Elliot "「あ……、迷惑だったか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ううん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ごつごつした岩場。\n
前回滑り降りた急勾配の坂道。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の知らなかった、そして彼がいなければきっと知らないままでいた場所。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（そうね、確かにこんな場所に一人で来ようとも思わない）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ブラッドの屋敷からじゃ、この景色は見られないものね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "アウトドア好きのどこかの騎士なら別だが、私だけでここまで来ることはないだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見えないもの、見せないものは互いにたくさんある。\n
それでも、積み重ねてきたものがあるから、少しずつ縮めていける。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（全部を知る必要なんてない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（すべてを知ることだけが、信頼のかたちじゃないわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私も、彼も。\n
こうやって、ときには目的地を決めずに出掛けられるような、そんな気楽な関係が心地いい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（大分、石が減ってきたわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "岩場を抜けたのか、木々が生い茂る森に出たのを見計らって、私は手に力を入れた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「よいっしょっと」"

play sound se_0210
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice eri_f0268
Elliot "「お、おい、動かないほうがいいぜ、[firstname]！？\n
落ちたら危ない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_2")
T "「大丈夫よ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（元の世界でだって、自転車の立ち乗りぐらいしていたし。\n
先刻までの振動に比べたら、これぐらい可愛いものじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思い切って自転車のフレームに足をかけて立ち上がり、エリオットの肩に手を置いてバランスを取る。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0269
Elliot "「お、バランス感覚いいんだな、あんた。\n
うまいもんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「人並み程度にはね。\n
あなたの体力には完敗だわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相変わらずのペースで漕いでいるのに、エリオットは息を乱した様子もない。\n
目の前にある耳が風を切って、左右にふわふわと揺れている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（握りたいけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここで握ったら、さすがにエリオットが可哀想なので、我慢する。\n
代わりに肩に乗せた手に体重をかけて、身を乗り出した。"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot "「！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0270
Elliot "「[firstname]、何するんだよ？\n
俺じゃなかったら、倒れているぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ええ、エリオットだから出来るのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の人に、こんな力業を出したりなどしない。\n
絶対に落としたりしないと信頼出来る彼だからこその悪ふざけだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭一つ分高くなって、見えていなかった前の景色が目に映る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「ねえ、エリオット」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Elliot "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「あなたにも仕事があって、私もずっとここにいられるわけじゃないから、はっきりとは約束出来ないけど……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_14")
T "「また、機会があったら、あちこち連れて行ってくれない？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_14")
Elliot "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あなたと出掛けるのが、楽しかったから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Elliot "「！！」"

play sound se_0697
play sound se_0483

scene bg_gen_sky_aut_day
with dis
hide t_nai3_1

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「うわわわっ！？\n
急にスピードを上げないでよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "返事がないので、どうしたのだろうと顔を覗き込みかけたところで、速度が上がる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までもすごい速さだったが、更に加速したエリオットは私から視線を外すや否や、猛然と漕ぎ始めた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0271
Elliot "「まったく……。\n
あんた、それ反則だぜ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0272
Elliot "「そんなこと言われたら、帰したくなくなっちまうのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「……何か、言った？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（風の音が大きすぎて、よく聞き取れなかったんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大声でもう一度言ってほしいと求めるが、エリオットは首を左右に振った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0273
Elliot "「ああ、もう……。\n
何でもねえよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0274
Elliot "「飛ばすから、しっかり掴まっていろって言っただけだ！\n
だああああ！！」"

play sound se_0483
pause .1
play sound se_0697
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「わっ、あ、危ないわよ！\n
そんなにスピードを上げなくてもっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（もう少しゆっくりこの景色を見ていたいのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "猛スピードで駆け抜けるウサギの自転車の速度は落ちることなく、街まで疾走を続けた。"

$ hi_mes()

scene bg_gen_sky_aut_day
with stripe_l_medium

scene bg_gen05_sm_aut
with stripe_l_medium

scene bg_gen04_km_day
with stripe_l_long

play music honobono2_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「あ……、エリオット、自転車止めてくれる？」"


show eri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice eri_f0275
Elliot "「ん？\n
何か用事か、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「用事っていうほどじゃないけど……。\n
少し休憩してもいい？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「その……、あそこで」"

hide eri_t_01_8
show eri_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Elliot "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が指差しているのは、以前エリオットが連れてきてくれた、ナイトメアがいた喫茶店だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（あ、あからさますぎる？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たまたま自転車の行き先に見つけたあの店。\n
今回も彼がいるとは限らないが……、ひょっとしたら会えるかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（だって、いまだに夢にも出てこないんだもの。\n
どこかで倒れているんじゃないかって心配にもなるわ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（自分でも、言い訳にしか聞こえない）"

hide eri_t_02_7
show eri_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice eri_f0276
Elliot "「ああ、別に構わないぜ。\n
ちょっと、待てよ」"

hide eri_t_02_12

play sound se_0482
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は器用にハンドルを切って、道の端へと停車させた。"


show eri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0277
Elliot "「気を付けて降りてくれよ。\n
こんなところであんたに怪我をさせたら悪いからさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「ええ、分かっているわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の身体を伝いながら、慎重に地面に下りる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットと出掛けてからまだ一時間帯も変わっていないはずなのに、踏みしめる地面の感覚に思わずほっとした。"

hide eri_t_01_8
show eri_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0278
Elliot "「よっと……」"

hide eri_t_02_7

play sound se_0180

scene bg_gen04_kn_day with ImageDissolve("gui/stripe_l.png", 1, ramplen=128, reverse=True)

play music forest_town_square_p_ali

show tenin_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kaz_f0019
Clerk "「いらっしゃいませ。\n
お二人様ですか？」"

hide tenin_1
show tenin_1 at left
show eri_t_03a_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0279
Elliot "「ああ、そうだけど……。\n
奧、埋まってるのか」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（あ、本当だ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "店に入ると、この前私達が座っていた席は、別の客が使っていた。"

hide eri_t_03a_2
show eri_t_03b_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「エリオット？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（まさか、退けなんて言って無理矢理取ったりしないでしょうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の仕事柄を考えるのであればない話でもないが、トラブルは避けたい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうするのかとひやひやしながら見守っていると、彼は仕方なさそうに肩を竦めた。"

hide eri_t_03b_11
show eri_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0280
Elliot "「……まあ、いいか。\n
空いている席でいいよな、[firstname]？」"

hide eri_t_01_4

hide tenin_1

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の心配が通じたのか、彼は窓際の椅子へと歩き始めてくれる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「う、うん……。\n
私はどこでもいいけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（……そんなに奧の席がいい理由って何かしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が見たところ、場所によってソファの質が違うわけではないよう思える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットもどちらかというとその辺りについては大らかなほうだから、気にすることもないと思っていたのだが。"

play sound se_0251

show eri_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0281
Elliot "「……まあ、この前片付いたばっかりだし。\n
俺が近くにいれば問題はねえか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「エリオット？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（何を言っているんだろう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ソファに座り、彼の言葉の意味が分からず首を傾げていると、後ろから聞き慣れた声がかかった。"

hide eri_t_01_7
show eri_t_01_7 at left
show nai_w_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0280
Nightmare "「いらっしゃい。\n
来てくれて嬉しいよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ナイトメア……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（あなた、まだここにいたの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔色の悪い夢魔は、あのときと同じようにウエイター姿でテーブルの傍に立っていた。"

hide eri_t_01_7
show eri_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0282
Elliot "「よう、ナイトメア。\n
おまえ、まだここにいたのかよ？」"

hide nai_w_01_1
show nai_w_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0281
Nightmare "「まあな、ただの気分転換ではないのでね。\n
目的を達成するまでは、そう簡単に帰れないな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「目的？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（この前は、余暇活動とか言っていたのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼も口でいうほど暇ではない……、いや、むしろ多忙というほうが正しい。"

hide nai_w_01_11
show nai_w_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0282
Nightmare "「それはそうと……。\n
お客様、ご注文……」"

hide nai_w_01_2
show nai_w_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「！？」"

hide eri_t_01_5
show eri_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot "「！」"

play sound se_0052
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然ソファから立ち上がったエリオットに疑問を覚えたと同時に、彼が叫んだ。"

hide eri_t_02_10
show eri_t_02_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0283
Elliot "「[firstname]、伏せろ！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「……きゃっ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットの突然の言葉に応じるよりも早く、ナイトメアが私の身体を引き寄せた。\n
そして。"

play sound se_0519
pause .3
play sound se_0519
pause .1
play sound se_0318
$ flash(.1)
pause .5
play sound se_0281
$ flash(.1)
$ flash(.1)

play music tension_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃声と、ガラスが砕ける音が室内に響く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（これって……、襲撃？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "窓から見える位置にいた人間で、襲われる可能性があるとすれば、二人。"

play sound se_0515
hide eri_t_02_9
show eri_t_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0284
Elliot "「ちっ。\n
まったく、雑魚がしつこいんだよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "硝子が割れて、銃声が響く。\n
エリオットは銃を持ち出し、表情がマフィアのそれに変わった。"

hide nai_w_01_3
show nai_w_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0283
Nightmare "「おやおや。\n
……お客様、揉め事を持ち込まれては困りますね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「そ、そんなことを言っている場合じゃないでしょう、ナイトメア！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（何を悠長に構えているのよ、あんたはっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の声にちらりと視線を向けたナイトメアは、何でもないように続けた。\n
緊迫感の漂う店内で、彼だけはいつもと変わらない。"

hide nai_w_01_2
show nai_w_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0284
Nightmare "「これはエリオットの……、いや、正確には帽子屋の揉め事だ。\n
私が口や手を出すのは分不相応というものだよ」"

hide nai_w_01_1
show nai_w_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0285
Nightmare "「それに、心配しなくても、エリオットのほうが強い」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「そ、それにしたって……。\n
きゃっ！」"

play sound se_0519
pause .3
play sound se_0519
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアと話す間にも銃弾が飛んでくる。\n
身を縮める私をかばいながら、ナイトメアはエリオットに言った。"

hide nai_w_01_11
show nai_w_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0286
Nightmare "「ここはおまえの属する領土だろう、エリオット。\n
不始末のツケは自分で片付けろ」"

hide eri_t_02_3
show eri_t_01_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0285
Elliot "「けっ、言われるまでもねえよ！」"

play sound se_0591
hide nai_w_01_9

hide eri_t_01_7

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットはそう告げると、銃を向けてきた相手を追って割れた窓から外に出る。"

play sound se_0021
pause .3
play sound se_0519
pause .3
play sound se_0021
pause .1
play sound se_0021

show woman_a_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0001
Customer "「きゃああ！」"

hide woman_a_3
show woman_a_3 at left
show man_c2_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0039
Customer "「な、何だ、銃声が！？」"

hide woman_a_3
show woman_a_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0002
Customer "「は、早く逃げないとっ」"

play sound se_0312
hide woman_a_5

hide man_c2_3

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T "（うわ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に来たばかりの頃に比べれば私も大分銃声に慣れたものだが、やはり間近で響く破壊音にはいつまで経っても慣れない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ううん、慣れたくない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "命が軽い世界。\n
誰でも代えがきくと皆が言う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（でも、私にとっては、代えがきかない人ばかりだもの）"



show nai_w_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
Nightmare "「…………」"

hide nai_w_01_9
show nai_w_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
Nightmare "「！」"

play sound se_0313

show t_nai3_2 onlayer master
with dis
hide nai_w_01_8

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ナイトメア？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "テーブルの影に並んで座っていた彼が、突然私を引き寄せた。\n
見上げた先で、色素の薄い顔が私以外を睨んでいる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0287
Nightmare "「君達の標的は、外で暴れている彼だろう？\n
彼女に用はないはずだが？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0044
Thug "「……帽子屋に関わりのある女だ。\n
交渉の材料ぐらいにはなるだろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつの間にそこに立っていたのか、銃を構えた男が私とナイトメアを見下ろしていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その背後には、また別の男。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0025
Thug "「遊んでいる暇はない。\n
さっさと片付けていくぞ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0288
Nightmare "「さっさと片付けて……、ね。\n
私もずいぶんと安く見られたものだな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（ナイトメア？\n
何をするの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を抱き寄せたまま、ナイトメアは物騒に笑っている。\n
普段、彼が私には見せることのない顔。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "色の薄い瞳が、前髪の奧で光った。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（……怖い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まるで夢で会うときのような、ぞっとする雰囲気が今の彼にはある。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0289
Nightmare "「引き金を引く気なら、ちゃんと狙うことだな」"


play music opposition1_a_ali
play sound se_0512
hide t_nai3_2
show t_nai3_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え……。\n
な、何を言っているのよ、あなた！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（挑発するようなこと、言わないでよっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相手が持っていた銃を、ナイトメアは自分の胸に当てた。\n
その行動に、圧倒的に有利な状況にあるはずの男の目が怯えを映す。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0026
Thug "「……三月ウサギが戻るまで注意を逸らす気か？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0045
Thug "「いくら夢魔とはいえ、この距離なら即死だぞ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0027
Thug "「それでも俺達に勝てる気でいるんだろ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0046
Thug "「馬鹿にしやがって……。\n
そんなに死にたいのなら、望み通りにしてやる！」"

play sound se_0354
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は動かないまま、私ではなく銃を持つ男を見ている。"

menu:
    "止める。":
        jump fushigi_nightmare3_5a
    "かばう。":
        jump fushigi_nightmare3_5b

label fushigi_nightmare3_5a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が本当に撃たれる気があるとは思わない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "病院が嫌いで、目に見える武器も持たないナイトメアだが、紛れもなく役持ちの一人。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "当然、男達に対しても何か勝算があるのだろうが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……どうするつもりなのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先刻から心の中で問いかけているのに、彼は一向に私を見ない。\n
その徹底ぶりは、無視されているのではないかと思うほどだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「……ナイトメア」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（馬鹿な真似はやめてよ？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice nig_f0290
Nightmare "「撃たなくていいのか？\n
三月ウサギは気が短いからな……、おまえらの仲間などあっという間に撃ち殺して戻ってくるぞ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice hos_f0047
Thug "「……そうだな。\n
目的はあくまでその女だ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice hos_f0048
Thug "「おまえには、用はない」"

play sound se_0354
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ナイトメア、止めて！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃口を突き付けているのは彼だというのに、私のほうが顔色を変えている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（手を離してっ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（万が一暴発でもしたら……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
Nightmare "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice nig_f0291
Nightmare "「……心配してくれるのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「当たり前でしょう！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（そんなことにいちいち嬉しそうな顔を見せないでよ！）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（心配しないはずがないでしょう！？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（馬鹿なことを言っていないで……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくら制止しても、ナイトメアは銃から手を離さなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0028
Thug "「殺せ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「駄目！！」"

play sound se_0503
hide t_nai3_3
show black onlayer master with close_short
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "響く銃声に、私は無力だ。\n
反射的に目を閉じて、身体を強ばらせることしかできなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0029
Thug "「う、ぐ……、がは！」"

play sound se_0579
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし聞こえてきた苦痛の声は、私のよく知る夢魔のものではなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「ナ、ナイトメア？」"

hide black
show t_nai3_3 onlayer master with open
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

hide t_nai3_3
show t_nai3_4a onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一体何が起こったのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃を突き付けられていたのは、ナイトメアだったのに、撃たれて倒れているのはもう一人の刺客だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（ナイトメアが、何かしたんだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何をしたのか、まったく分からない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0292
Nightmare "「おや、まだ息があるな。\n
可哀想に、痛そうだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0293
Nightmare "「ちゃんと狙えと言っただろう？\n
まあ、彼女を攫おうとしたんだから、簡単に死なせてやる気はなかったがね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0049
Thug "「な……。\n
ど、どうして、おまえじゃなくて、こいつが……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0050
Thug "「俺はおまえを狙っていたのに……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "男の疑問はそのまま私の疑問だ。\n
銃口がナイトメアの胸に当たっていたことは、確かに見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし当の本人だけは平然としたままだった。"

hide t_nai3_4a


show nai_w_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0295
Nightmare "「……私を誰だと思っているんだ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にたり、と。"

hide nai_w_01_9
show nai_w_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0296
Nightmare "「こんな形をしていても、夢魔だぞ？\n
人を夢に落とすぐらい、容易い」"

hide nai_w_01_1
show nai_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0297
Nightmare "「さあ、一体この場にいる人間で、誰が私の夢に落ちていたのかな？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "酷薄な笑みを浮かべて、彼は緩やかに指を動かす。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そしてその指で突然、もう一人の刺客の胸を突き刺した。"

hide nai_w_01_11
show nai_w_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0298
Nightmare "「これだって、私の指ではないかもしれないぞ」"

hide nai_w_01_2
show nai_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0299
Nightmare "「鋭利なナイフ、いや、剣……。\n
ああ、銃や焼けた杭かもしれないな」"

hide nai_w_01_11
show nai_w_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0300
Nightmare "「覚めない夢に落ちていると、どうして気付かない？」"

hide nai_w_01_1
show nai_w_01_1 at left
show punk_e1_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Thug "「！！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらりと、男は自分が撃ってしまった味方に視線を動かす。\n
それから、ナイトメアの指を振り払った。"

play sound se_0313
hide punk_e1_3
show punk_e1_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0051
Thug "「こ、この……。\n
化け物が！」"

play sound se_0512
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "錯乱した男が再びナイトメアに銃を向けた。\n
しかしナイトメアは……、動かない。"

hide punk_e1_7
show punk_e1_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0052
Thug "「し、死ね！！！」"

play sound se_0022

show white onlayer master
hide punk_e1_9
show punk_e2_6 at right
with dis
hide white ##instant

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0053
Thug "「……あ、ぎゃあ！？」"

play sound se_0579
hide punk_e2_6

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、生まれた悲鳴は彼自身のものだった。"

hide nai_w_01_1


show eri_t_03a_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0286
Elliot "「……まだ遊び足りねえのか？\n
俺らに刃向かった時点で、末路なんて決まっているのによ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「エリオット」"

hide eri_t_03a_7
show eri_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice eri_f0287
Elliot "「とりあえず、この場は借りておくぜ、ナイトメア。\n
後始末はつけておかねえとな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "外を片付けて戻ってきたエリオットが、後ろから男を撃ちぬいた。"

hide eri_t_01_6
show eri_t_01_6 at left
show nai_w_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0301
Nightmare "「ふ……、私は何もしていないんだがね。\n
貸せというのなら貸しておくことにしよう」"

hide nai_w_01_11
show nai_w_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0302
Nightmare "「ああ、エリオット、待ってくれ。\n
彼に言い忘れていたことがあった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットに腕を取られている男の耳元に、ナイトメアはそっと話しかけた。\n
慈愛のこもったともいえる、柔らかな表情で。"

hide nai_w_01_2
show nai_w_01_1 at center
hide eri_t_01_6
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0303
Nightmare "「言っただろう、早く引き金を引けと。\n
のんびりしているからこうなるんだ」"

hide nai_w_01_1
show nai_w_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0304
Nightmare "「おめでとう。\n
夢よりも残酷な現実が待っているよ」"



hide nai_w_01_6
show nai_w_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Thug "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "氷よりも冷たい声で、最終通告を告げたのだった。"

hide nai_w_01_6

jump fushigi_nightmare3_6
label fushigi_nightmare3_5b:

show t_nai3_4b onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（何のつもりか知らないけど、現実で撃たれたらナイトメアだって無事じゃすまない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むしろ、身体の弱さは折り紙付きだ。\n
撃たせるわけには、いかない。"

play sound se_0216

scene t_nai3_4b with dis
hide t_nai3_4b

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「用があるのは私でしょう。\n
彼を巻き込まないで」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（少なくとも交渉に使う気なら、手荒なことはしないでしょう）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……どこまでかは分からないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアをかばうように立った私を見て、男達は与しやすいと判断したらしい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0054
Thug "「は……。\n
これはいい、こいつのほうが身の程をよく分かっているぜ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "げらげらと笑った男はそのまま私の手を掴もうと手を伸ばした。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「いいから、黙っていてっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（他領土の争いに領主が出張るなんてまずいでしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "強い口調で言い切ると、ナイトメアは驚いたように目を見開き。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0305
Nightmare "「そこだと近いから……、君のほうが危ないんだ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（え？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T "（それってどういうこと？）"

play sound se_0313
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が振り返るよりも早く、一気に引き寄せた。"

play sound se_0439
pause .4
play sound se_0060
$ flash_red(.1)

show splatter onlayer master with Dissolve(.05)
hide splatter with Dissolve(1.5)

scene bg_gen04_kn_day with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0055
Thug "「ぎ、あああああ！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "男の手は、私に触れてもいなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアが私を引っ張ったからではなく、伸ばしかけていた手を押さえ込んでいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むっと香る血の匂いに、止まっていた思考がようやく動き出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（何で？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ナイトメアが何かしたの？）"

play sound se_0440
pause .4
play sound se_0644

show black onlayer master with grad_b_short
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同じく、布よりも重いものを断ち切る音が響いて目を向けようとしたが、突然視界が閉ざされた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の背後から目隠しが出来る人物なんて、一人しかいない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「……ナイトメア？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice nig_f0306
Nightmare "「女性には少々刺激が強すぎるな。\n
当然の処断と言えばそれまでだが」"

play sound se_0676
pause .4
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice gra_f0132
Gray "「余計なことでしたか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice nig_f0307
Nightmare "「いや……、おまえが出て来なければ私が手を出していたからな。\n
こいつらにとってはよかったんじゃないか」"


play music heartrending_a_ali

show nai_w_01_9 at left

show gre_t_02_12 at right
hide black with open
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice nig_f0308
Nightmare "「……大丈夫か、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ようやく目隠しを外されて見開いたそこには、グレイがいた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "立ちこめる血臭の中で、グレイとナイトメアは塔での風景のように、普通に話している。"

hide gre_t_02_12
show gre_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0133
Gray "「[firstname]、君も怪我はないか？\n
君に何かあったら元も子もない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……何もないけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「でも、どうしてグレイが？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔の重鎮が揃って他領土で何をしているのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメア一人ならまだ余暇活動でも、脱走でも納得がいくが、グレイまでいるとなると話が違ってくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「あなた達、ここで何をしていたの？」"

hide gre_t_02_7
show gre_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Gray "「…………」"

hide nai_w_01_9
show nai_w_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Nightmare "「…………」"

hide gre_t_02_4
show gre_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice gra_f0134
Gray "「その……、[firstname]。\n
驚かずに聞いてほしいんだが」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（……もう十分驚いているわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いるはずのないナイトメアに続いて、グレイまで出てきたのだ。\n
ただの偶然ということはないだろう。"

hide nai_w_01_3
show nai_w_01_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0309
Nightmare "「あー、あーあーあー！\n
駄目だ、それ以上言うな、グレイ！」"

hide nai_w_01_12
show nai_w_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0310
Nightmare "「命令だ！\n
それ以上何か言ったら、決裁はすべてストライキするぞ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「雇い主にストライキ権は認められていないわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（仕事をダシにしないと交渉も出来ない上司……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それ以外に部下に強く出る言い訳を思いつかないのだろうか、この男は。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（病院に行くよりはましと判断したのかもしれないけど、情けない）"

play sound se_0098
hide nai_w_01_10
show nai_w_01_10 at left_center
hide gre_t_02_11
show gre_t_02_11 at center

show eri_t_02_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice eri_f0288
Elliot "「まったく、手間取らせやがって……。\n
って、あれ、どうしてトカゲまでいるんだ？」"

hide gre_t_02_11
show gre_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice gra_f0135
Gray "「はあ……。\n
またやっかいな相手と一緒にいますね」"

hide gre_t_03_6
show gre_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice gra_f0136
Gray "「これ以上ここにいたら、ますます厄介そうですから、俺は一足先に塔に戻りますよ」"

hide gre_t_01_14
show gre_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice gra_f0137
Gray "「後はご自身でどうにかしてください」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "外を片付けて戻ってきたエリオットを見て、グレイは溜息をつく。"

hide nai_w_01_10
show nai_w_01_4 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0311
Nightmare "「ま、待てグレイ！？\n
後始末は全部私任せか！？」"

hide gre_t_01_13
show gre_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0138
Gray "「……つい先刻、ご自分で口止めをしたじゃありませんか」"

hide gre_t_02_10
show gre_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0139
Gray "「今回ばかりは俺ではフォローは出来ませんし、しません」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呆れたように溜息をついて、グレイは事情の分からない私とようやく視線を合わせてくれる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「グレイ、どういうことなの？」"

hide gre_t_02_12
show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice gra_f0140
Gray "「口止めされてしまったからな。\n
詳しくはナイトメア様から聞いてくれ」"

hide gre_t_03_10
show gre_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice gra_f0141
Gray "「君にとって、悪い話ではないはずだから。\n
では、これで」"

play sound se_0774
hide nai_w_01_4
show nai_w_01_4 at left
hide eri_t_02_5
show eri_t_02_5 at right
hide gre_t_01_3
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一方的に言い切って、グレイはすたすたと外へと出て行ってしまう。\n
先ほどの襲撃で開いた大きな窓の穴を軽々と抜けて。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（逃げたわね）"

hide nai_w_01_4
show nai_w_01_4 at left
hide eri_t_02_5
show eri_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice eri_f0289
Elliot "「は？へ？\n
何なんだよ、一体……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私よりも状況が分からないエリオットがのんびりと周囲を見渡しているのを見て、ようやく私も肩の力を抜いた。"

hide eri_t_02_6

hide nai_w_01_4


jump fushigi_nightmare3_6
label fushigi_nightmare3_6:
$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME

play music truth_a_ali

show nai_w_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0312
Nightmare "「つまり、帽子屋がこの前潰した連中の残党が、報復のために君を狙って襲撃しに来たというわけだ」"

hide nai_w_01_9
show nai_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0313
Nightmare "「勿論、帽子屋はそれを知っていたからこそ、君にエリオットを付けたんだろうが……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0313_5
Nightmare "「やれやれ、まさか私まで巻き込まれるとは思わなかったな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（それは私も同じよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットは帽子屋屋敷に連絡を取るために、今は席を外している。\n
店内は血塗れの酷い有様だったから、私達がいるのは屋外のテラスだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（どうして、あなた、こんな場所にいたの？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（そんな格好で、一体何をしていたのよ？）"

hide nai_w_01_10
show nai_w_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先刻からずっと心の中で話しかけているのに、ナイトメアは答えてくれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞こえていないはずがないのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（聞かなくていいことばかり聞いているくせに……。\n
こういうときには、無視するんだから）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……ナイトメア」"

hide nai_w_01_7
show nai_w_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0314
Nightmare "「何だ、[firstname]？\n
な、なんでそんなに睨むんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「当然でしょう、無視されれば私だって気分が悪いわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（ほら、きりきり答えなさい！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼とは口に出すよりも前に会話が成立してしまうことが多いから、私もついいつものように声にせず聞いてしまう。"

hide nai_w_01_4
show nai_w_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0315
Nightmare "「ん？\n
……ああ、なるほど、そういうことか」"

play sound se_0468
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然納得したように頷いた彼は、指をパチンと打ち鳴らした。"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま私のほうへ顔を近付けて、小さな声で続ける。\n
まるで内緒話をするような仕草。"

hide nai_w_01_2
show nai_w_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0316
Nightmare "「君の期待を裏切るようで悪いが……。\n
私は、君が塔を出てから君の心の声を聞いていないよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「い、今なんて言ったの？」"

hide nai_w_01_9
show nai_w_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0317
Nightmare "「私は君が塔を出ていってから、今までずっと、君の心の声を聞いていない」"

hide nai_w_01_2
show nai_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0318
Nightmare "「聞こえるものを聞かないようにするのも、存外大変なんだがね。\n
それが聞きたい人の声だから尚更……、必死に抑えている」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（聞こえていなかった？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに、この店にいるときのナイトメアの様子を思い浮かべれば思い当たる節はあったが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "理由が、分からない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「何でそんなことをしていたのよ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（聞かないでって言ったときには、嫌だとか何とか言っていたのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず胸の内から呼びかけて、気が付く。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（……あ、そうか。\n
これも聞こえていないのか）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（便利というか、不便というか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心を読む力は、彼だけの能力だ。\n
誰にでも出来ることではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それだけに、その相手とのやりとりが染みついた今では、他の方法に切り替えきれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（慣れって怖いわ）"

hide nai_w_01_10
show nai_w_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice nig_f0319
Nightmare "「さて……。\n
何でだと思う？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「知らないわよ。\n
私にはあなたの心を読むなんてこと、出来ないもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "冷たく答えた私を彼は何故か優しく見つめた後、小さく首を振った。"


play music forest2_p_ali
hide nai_w_01_1
show nai_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0320
Nightmare "「……少しだけ、怖くてね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「怖いって、何が？」"

hide nai_w_01_11
show nai_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_4")
voice nig_f0321
Nightmare "「覗いてしまえば、聞いてしまえば、一瞬で答えが分かってしまうだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "囁くように寄ってきた唇が、私の頬に触れる。"

hide nai_w_01_10
show nai_w_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0322
Nightmare "「君があの屋敷のほうが好きになってしまったら、夢でも呼んでくれなかったら……。\n
どうしようかと思ったんだよ」"

hide nai_w_01_7
show nai_w_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0323
Nightmare "「どんな夢を渡っても、君に会えないなら引きこもる意味もないからね。\n
こうして、君の近くをうろうろしていたというわけだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「そう。\n
じゃあ、夢の中で呼ばなくてよかったわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相手に聞こえていると分かっていれば呼びかけるのも悪くない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、相手が自分の声に耳を塞いでいる状況でいくら呼んでも、意味がない。\n
ただの、徒労だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「どうせ呼んでも聞いてくれなかったでしょうから」"

hide nai_w_01_4
show nai_w_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Nightmare "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（冷たい、指先）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのとき、塔を出るときに触れたときと同じ、ひんやりとした体温が、私に触れる。"


play music honobono1_a_ali
show t_nai3_5 onlayer master
with dis
hide nai_w_01_5

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………ん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Nightmare "「…………っ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まだ硝煙が漂うような場所で、キスを交わした。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0324
Nightmare "「私を呼ぼうとしてくれていたと、自惚れてもいいのかな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0325
Nightmare "「それに、聞こえないはずがないよ。\n
聞こえないようにしたところで、君が私を呼ぶ声が聞こえないはずがない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……だって、聞こえないようにしていたんでしょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここで彼に会うたびに、どれだけ心の中で声を送ったか分からない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、それが彼の元に届いていなかったというのなら、どんな呼びかけなら届いたというのか。"

hide t_nai3_5
show t_nai3_6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0326
Nightmare "「いや、それでも……、君が私のことだけを考えて呼んでくれれば、いつだって聞こえていた」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0326_5
Nightmare "「君の声は、私が全部拾い上げて、包み込んであげよう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0327
Nightmare "「夢にくるんで、誰にも触らせたりしない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「難しい注文ね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一人のことだけを考えるなんて、私には難しいことぐらい、彼にだって分かっているだろうに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（大切なものを一つだけに絞りきれない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……一番大切な人は、あなただけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声が聞こえないのをいいことに、日頃口に出来ない気持ちが素直に胸の中に込み上げてくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦笑いを浮かべたまま、もう一度唇を重ねようとしたのか、ナイトメアの顔が迫ってきて。"

play sound se_0098

play music elliot_t_ali
hide t_nai3_6


show eri_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0290
Elliot "「……何やってるんだ、あんたら」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「エ、エリオット！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "横から顔を覗かせたエリオットの存在に、我に返った。"

hide eri_t_01_9
show eri_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0291
Elliot "「まったく、人が仕事から戻ればこれかよ。\n
あんたも嫌なタイミングで見せ付けてくるよな、ナイトメア」"

hide eri_t_02_6
show eri_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0292
Elliot "「性格悪いぜ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達を見ているエリオットは、心底呆れているのだろう。\n
頭をかきながら、あからさまに溜息をついた。"

hide eri_t_02_3
show eri_t_02_3 at left
show nai_w_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0328
Nightmare "「ははは、私の性格の悪さなど君の主に比べれば可愛いものだよ。\n
さて、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤くなった顔の私を立ち上がらせる。"

hide nai_w_01_6
show nai_w_01_11 at center
hide eri_t_02_3
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0329
Nightmare "「私にとってはね、聞こえる恐ろしさよりも、聞こえない不安のほうが大きいんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「それ、普通は逆じゃないの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だったら、耐えられない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "好意も悪意も持ち合わせているのが人ならば、その両方に常に晒され続けるほうが、ずっと、恐ろしい。"

hide nai_w_01_11
show nai_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0330
Nightmare "「そうだな、いつも心の声を聞いているうちに感覚がおかしくなってしまったのかもしれない」"

hide nai_w_01_10
show nai_w_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0331
Nightmare "「でも、君の声が聞こえないのは、嫌だ。\n
それだけは確信している」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「…………」"

hide nai_w_01_9
show nai_w_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice nig_f0332
Nightmare "「どんな声も、どんな言葉も大切にするから……。\n
君の心に、触れさせてくれないか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつだって勝手に踏み込んでくる夢魔が、ここまで真摯な態度で確認してきたのはこれが恐らく初めてだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「当然でしょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「……あなた以外に触らせたりしないんだから、ちゃんと責任を取ってちょうだい」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（素直じゃない私を分かってくれるのは、あなただけよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心と言葉が裏腹になっても、ナイトメアには知られてしまう。\n
怖くもあるが、醜い部分を知っていても私を好きだと言ってくれるのは、嬉しい。"

hide nai_w_01_13

$ hi_mes()

scene bg_gen04_kn_day
with stripe_l_medium

scene bg_gen04_km_day
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_long
##endmemory
label fushigi_end_check_tower1_n:
if renpy.seen_label("fushigi_end_nightmare1") == True:
    jump fushigi_end_check_tower2_n
if renpy.seen_label("fushigi_end_julius1") == True:
    jump fushigi_end_check_tower2_n
if renpy.seen_label("fushigi_end_gray1") == True:
    jump fushigi_end_check_tower2_n
else:
    jump fushigi_end_nightmare1
label fushigi_end_check_tower2_n:
if fushigi_common3_hatter2_nightmare2a_seen == True:
    jump fushigi_end_nightmare1
else:
    jump fushigi_end_tower1
