label gakuen_op2:

scene bg06_sk_h_eve
with stripe_l_medium

scene bg06_sk_h_nig with Dissolve(.8)

scene bg06_sk_h_day with Dissolve(.8)

play music school_front_day_p_wam

scene bg10_sb_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして……、ついに私がシンフォニア高位魔法学校に入学する日がやってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア高位魔法学校は、基本的には年齢を問わず優秀な魔法使いを迎え入れる。そのため、同じ学生とはいっても年齢は様々だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "卒業せず、研究のために残る者、卒業しても戻ってくる研究者。\n
シンフォニアは研究機関としても有名で、外部からの研究者も受け入れている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他、編入生に、留学生。\n
特別な事情で学園預かりの者。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういった様々な者まで混じって、かなり雑多な集まりとなっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（共通するのは、皆が皆、魔法使いとしてとびきり優秀だってこと）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういう学校なだけに、誰が新入生だか分かりにくい。\n
しかし、傾向はある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲で緊張したような表情を浮べる生徒達は私よりも幾分幼く見えた。\n
やはり、私のように途中までは一般の学校で、というのはあまりない事例らしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "厳かな式典はつつがなく進行していく。\n
ただ神妙な顔で座っていればいいだけと分かっているのだが、それでもどうしたって緊張する。"

$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（緊張しているのに……、退屈するなんて矛盾だわ）"

$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中がぴっと伸びるような緊張はあるのに、長々と続く壇上の挨拶に気だるさを覚えてしまう。"

$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "式典が無事に終了した時には深々と息を吐き出してしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（……疲れた）"

$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "式典が終わった後はそれぞれのクラスに移動する、とあったが……。"

$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0000
Hatena "「よ、疲れているみたいだな。\n
……こういう式典ってのは、どうも肩が凝る」"

$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「……っ！」"

play sound se_0449
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後より聞き覚えのない男の声が響くと同時に、ぽん、と肩に手が乗った。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（まずいところを見られた？）"


play music gowland_t_ali

show m_op2_1_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "はっ、と表情を引き締めて振り返った先には、声と同じく見知らぬ男が、のんびりとした笑みを浮べて立っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒ではないことだけが、すぐに分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（さすがに、生徒ではないわよね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice gor_r0001
Gowland "「ああ、悪いな。驚かせたか？\n
俺はゴーランド。あんたのクラスの担任で、担当科目は現代魔法史だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ゴーランド……、先生」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（何故かしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "{size=+20}（ものすごく、違和感を覚える）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "初めて会うクラス担任だというのに、「先生」と呼ぶことに対して強烈な違和感が……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0002
Gowland "「？\n
どうした？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「い、いえ……。\n
なんでも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「あの……。\n
私に、何か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_r0003
Gowland "「担任なんだから、もうちょっと打ち解けてくれよ。\n
やりにくいだろ～……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「はあ……、すみません」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪いとは思いつつ、そう簡単に打ち解けられるような性格はしていない。\n
どうしても硬くなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0004
Gowland "「……次、教室移動だからな。\n
あんた、教室の場所が分からないんじゃないかと思ってよ。余計な世話だったか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「いいえ、助かりました。\n
ありがとうございます、ゴーランド先生」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

hide m_op2_1_1
show m_op2_1_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "違和感がさらに大きくなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……何故だろう。\n
硬くなりはするものの、この担任に対して敬語を使う気になれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（私、簡単に打ち解けられる性格じゃない……、はずなのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までにない奇妙な感覚だ。\n
対応として間違ってはいないはずなのに、違和感が強すぎて自分がまずい対応をしているような気になってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは私の言葉を受け取る側である、ゴーランドのほうも同じだったらしい。\n
私の言葉を聞いて、露骨に顔を引きつらせている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0005
Gowland "「な……、なんか、気持ち悪いな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……ええ、とても」"

play sound se_0559
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
Gowland "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice gor_r0006
Gowland "「いいや、ゴーランドって呼んでくれ。\n
敬語もいらねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「でも、そんなわけには……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いかない、と言いたいのに言えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0007
Gowland "「あんたも、気持ち悪いだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……そうね。\n
気持ち悪いっていうか、違和感が……」"

play sound se_0559
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
Gowland "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「…………」"

hide m_op2_1_2
show m_op2_1_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「わ、私のことも[firstname]でいいわ。\n
[firstname]＝[familyname]が私の名前よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気を取り直して、改めてゴーランドへと名乗る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく担任であるゴーランドはすでに私の名前など把握しているだろうが、自己紹介は円滑な人間関係を築くための基礎だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0008
Gowland "「そうか、んじゃ遠慮なく名前で呼ばせてもらうぜ。\n
よろしくな、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0009
Gowland "「うっし、それじゃあ行くか？\n
教室に案内してやるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「ええ、お願い！」"

play sound se_0460
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに促され、私は入学式の会場を後にした。"

with dis
$ hi_mes()
hide m_op2_1_3


play music corridor_day_p_wam

scene bg27_rk_day
with stripe_l_long
play sound se_0560

show girl_a1_1 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice may_g0049
Seito "「あれ……？」"

hide girl_a1_1
show girl_a1_1 at left

show boy_a1_3 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice suz_g0095
Seito "「お……」"

hide girl_a1_1

hide boy_a1_3
show boy_a1_3 at left
show girl_b2_3 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice tak_g0150
Seito "「……留学生？」"

hide boy_a1_3

hide girl_b2_3
show girl_b2_3 at left

show boy_b1_2 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice oni_g0054
Seito "「あの子、留学生……、だよな？」"

hide girl_b2_3

hide boy_b1_2

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……留学生？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すれ違う複数の生徒達の間から聞こえる囁き。\n
ゴーランドに案内されて廊下を歩いて行く中、漏れ聞こえる内容に首を傾げた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "雰囲気から察して、留学生というのはどうやら私のことらしいのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は別にこの国で珍しい髪や目の色をしているわけではない。\n
彼らと特別違った格好をしているわけではないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、どうして私をさして「留学生」なんて言葉が出てくるのだろうか。"


show go_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0010
Gowland "「はは、気にしないでやってくれ。\n
あんたぐらいの年での新入生は珍しいんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "戸惑っている私に気づいたのか、隣を歩いていたゴーランドが鷹揚に笑って見せた。"

hide go_m_01_8
show go_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0011
Gowland "「ここ、シンフォニアは、年齢よりも実力で入学を決めるからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0011_5
Gowland "「魔法の腕に自信のある奴は最初からここに来るし、無理な奴はそのまま諦めちまうことのほうが多い」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……そうね。\n
新入生も、年下の子たちの方が多かった気がするわ」"

hide go_m_01_11
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_r0012
Gowland "「だからあんたぐらいの年で、見慣れない生徒がいると留学生と判断しちまうわけだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_r0012_5
Gowland "「他学校からの編入生、留学生ならちょくちょく受け入れているからな、シンフォニアは」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「へえ、それでなのね。\n
そう聞くと、ますます授業についていけるかが不安になってきたわ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の成績を提出して、校長から入学の許可が下りたのだから大丈夫だとペーターは言っていた。だが、シンフォニアの実情を耳にすると不安が膨らんでいく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆は私よりも早くシンフォニアの生徒として、英才教育を受けてきていて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなところに今更来てしまった私は、はたして、ちゃんとついていけるのだろうか。"

hide go_m_03_9
show go_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0013
Gowland "「うん？そんな心配するってことは……。\n
あんた、まだこの学校のシステムがよく分かっていなかったりするのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（ぎくっ！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの声に、肩を竦めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「……実は。\n
パンフレットにはしっかり目を通したつもりではいるんだけど……、あまりぴんときてない部分もあるの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "特に、入学へ備えての準備で忙しく、ペーターに確認をとる時間すらなかったのだ。入ってしまえばなんとかなる、と思っていなかったと言ったら嘘になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……もうちょっと、下調べしておけばよかったな）"

hide go_m_03_1
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice gor_r0014
Gowland "「はは、パンフレットを読んだだけじゃあ、そりゃぴんとこなくてもしょうがないよな。\n
よし、俺が説明してやるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「本当に？\n
助かるわ」"

hide go_m_03_9
show go_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_r0015
Gowland "「それが俺の仕事だからな。\n
あんたら生徒が、楽しく学べるのが一番だ」"

hide go_m_02_8
show go_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_r0016
Gowland "「まず、これから案内するクラスだが、そこがあんたの基礎クラスとなる」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_r0016_5
Gowland "「学校側からの連絡事項を受けたり、ホームルームといったのはそこでやることになるな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「授業は、そこではしないの？」"

hide go_m_02_13
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_r0017
Gowland "「俺がやる現代魔法史の授業は、その教室でやるぜ。\n
それ以外は、受ける授業にあわせて移動する形になる」"

hide go_m_02_12
show go_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_r0018
Gowland "「各クラスの基礎教室は、そのクラスを受け持つ担任次第だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「それで、現代魔法史を教えるあなたの受け持つ生徒は、現代魔法史の教室が基礎教室になるのね」"

hide go_m_02_5
show go_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_r0019
Gowland "「はは、飲み込みが早いな、あんた。\n
そういうことだ」"

hide go_m_02_8
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_r0020
Gowland "「んで、クラス自体は年齢や在籍年数に関係なく習熟度で組んである」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_r0020_5
Gowland "「だから、あんたが俺のクラスにいるってことは、あんたは俺のクラスに相応しいってことなんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……安心したわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "在籍年数や、年齢に関係なく、実力でクラスが振り分けられるというのは、ある意味とてもシビアだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、私にとってはそれがありがたい。\n
このクラスにいていいのだと思って、臨むことができる。"

hide go_m_03_9
show go_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0021
Gowland "「お、着いたぜ。\n
ここが、あんたの教室だ」"

hide go_m_01_7
show go_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0022
Gowland "「これからあんたの拠点になる教室だから、しっかり場所を覚えるようにしてくれよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「分かった……」"

play sound se_0556
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わ、と最後まで言うより先に、遠くのほうで何か大きな声が聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「？？？」"

play sound se_0556
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大声で言い争っているのか、廊下中に声が響き渡っている。"

hide go_m_01_5
show go_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0023
Gowland "「この声は……。\n
帽子屋のところの……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドはその声に聞き覚えがあったのか、きょろきょろと周囲を見渡した。\n
声の主を探そうとしているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私には心当たりはないものの、ここまで聞こえるほど大声で争っている人物だ。\n
それが誰だか分からなくとも、見つけるのは容易いはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに倣って、きょろきょろと周囲を見渡す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……って）"


play music battle_a_wam

show m_op2_2_1 onlayer master
with dis
hide go_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "騒ぎの元凶は、いともあっさりと見つけられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むしろ見つけられないほうがおかしい。\n
何故なら……、彼らは猛スピードで廊下を箒で飛行しているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_r0000
Hatena "「これなら新記録だよ、兄弟！\n
ボリスに自慢できる数字が出せそうだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_r0001
Hatena "「そうだね、兄弟！\n
廊下飛行レースに、僕らの名が輝かしく刻まれるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きゃっきゃっと、無邪気な会話を繰り広げながら先頭を飛ぶのは、二人の子供だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よく見ると背丈も、顔つきもまったく一緒の双子。\n
高速で飛行していなくとも判別がつかないだろうと思うほど、瓜二つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、その双子を背後から追い上げるのは……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_r0000
Hatena "「てめえら、いいかげんにしろ！！\n
ブラッドは謹慎が解けたばっかなんだ\n
ぞ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_r0001
Hatena "「おまえらが騒ぎを起こしたら、ますますブラッドの立場がまずくなるだろうが！！\n
もうちょっと考えてから行動しろよ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "{size=+20}（考えたほうがいいのは、おまえのほうだ）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つい、そんな突っ込みを入れたくなってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "状況はよく分からないが、騒ぎを起こしてはまずいというなら、まずは自身がおとなしくするべきだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子を止めるためとはいえ、彼までが箒で校内を暴走しまくれば、余計騒ぎになってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_r0002
Hatena "「この新記録は、あのウザいひよこウサギが追いかけてくれたおかげだよ、兄弟」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_r0003
Hatena "「僕ら、追い詰められると本領発揮できるからね。\n
お礼をしないといけないよ、兄弟」"

play sound se_0743
hide m_op2_2_1

play sound se_0765
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子達が、猛スピードで私の目の前を通りすぎていったタイミングで、ポケットから取り出した何かを、ぽーいっと背後へと放り投げた。"


show white onlayer master
play sound se_0123
hide white ##instant
show m_op2_2_2 onlayer master with spread_short
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Hatena "「！！！？」"
$ flash_color("light_yellow", .2)
$ flash_color("light_pink", .2)
$ flash_color("light_orange", .2)
$ flash_color("light_pink", .2)
pause .1
$ flash_color("light_pink", .2)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "甲高い連続した破裂音と一緒に、光が乱舞する。双子を後ろから追いかけていた青年の箒が、一瞬コントロールを失って大きく蛇行する。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_9")
voice gor_r0024
Gowland "「っ！？\n
危ねえ……！！」"


play music corridor_day_p_wam
play sound se_0051
camera at hpunch
camera at vpunch
hide m_op2_2_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その大幅に揺れた箒に、危うく接触しそうになった私の腕をゴーランドが引き寄せてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おかげで箒にひっかけられるなんていう、間の抜けた大惨事には巻き込まれずにすんだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「あ、ありがとう。\n
ゴーランド」"


show go_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice gor_r0025
Gowland "「いいってことよ。\n
……ったく、エリオット＝マーチの奴、す～ぐ周りが見えなくなっちまうんだからよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……エリオット＝マーチ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あの人……、いえ、ウサギ？\n
あのウサギが、エリオット＝マーチ？」"

hide go_m_02_11
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_r0026
Gowland "「ああ、名前はいいだろ。\n
マーチなんて、音楽家の俺としちゃあ、憎めない名前っつーか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice eri_r0002
Elliot "「お～ま～え～ら～！！\n
今日という今日は許さねえ、ぶっ殺す……！！」"

play sound se_0743
hide go_m_02_12
show go_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_r0027
Gowland "「……と、まあ、行進曲どころの騒ぎじゃない、暴走ウサギだけどな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ついに、双子を追いかけていた青年は、当初の目的すら忘れてしまったようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子の暴走を止める、ではなく、双子を捕まえてとっちめる、という方向に考えがシフトしてしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結果、止めようとしていたはずの彼までが、一緒に暴走行為を繰り広げている。"

play sound se_0510
##special anime juugeki
##special anime juugeki
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、もっとまずい。\n
暴走どころか、校内で攻撃魔法やらマジックアイテムの乱用まで……。"


show boy_c2_2 at center
with dis
hide go_m_03_12

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0071
Seito "「今、ツインズが使ったのって、何のマジックアイテムだ？\n
見てたら欲しくなってきたんだけど、購買で買えるかな」"

hide boy_c2_2
show boy_c2_2 at left

show boy_d1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0058
Seito "「購買で売ってる普通のマジックアイテムを、双子が改造してああなってるんじゃないか？\n
あんなの、購買で見たことないぜ？」"

hide boy_c2_2
show boy_c2_1 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0072
Seito "「へえ……。\n
だったら改造方法聞いてみるかなー」"

hide boy_d1_3
show boy_d1_5 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0059
Seito "「ってか、おまえ何に使う気だよ」"

hide boy_c2_1
show boy_c2_2 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0073
Seito "「はは」"

hide boy_d1_5
show boy_d1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0060
Seito "「はは、じゃないだろ。\n
あ、まさか……」"

hide boy_c2_2

hide boy_d1_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒が校内を箒で暴走。\n
さらには魔法の乱用。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私にとっては大事件だったのだが、周囲の会話を聞いてみるに、ここシンフォニアではそうでもないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆、日常の一部としてそれを受け入れてしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……ある意味大物揃いなのかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "攻撃魔法が飛び交っていても、普通に受け入れられてしまう世界。\n
さすがシンフォニアだ……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……いや、ここ、感心するところなのかしら）"


show go_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice gor_r0028
Gowland "「さ、俺たちも教室に入ろうぜ！\n
ほら、[firstname]、こっちだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに呼ばれて、意識を教室へと戻す。"

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教室の中からは、賑やかな喧騒が漏れ聞こえてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来ならばそれなりに緊張してもおかしくない状況なのだが、さきほどの追走劇のせいか、彼らと同時に張り詰めていたものまで飛んでいってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いい具合に、脱力できたといえるのだろうか。\n
気が抜けた。"

hide go_m_01_2
show go_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0029
Gowland "「準備はいいか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「ええ、ばっちり」"

hide go_m_01_6
show go_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice gor_r0030
Gowland "「じゃあ……、行くぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の返事に、ゴーランドが満足げに頷いて、教室のドアへと手をかける。"

with dis
$ hi_mes()
hide go_m_03_4


scene black with Dissolve(.8)
pause .8
play sound se_0586

scene bg01_cr_day with stripe_l_long
play sound se_0667

play music classroom_day_p_wam

show go_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0031
Gowland "「うーっし、おまえら静かにしろよー！\n
今日は新入生がいるからな！」"

hide go_m_02_11
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0032
Gowland "「引かれちまわないよう、いい子にしてろよ？\n
んじゃ[firstname]、入ってこい！」"

play sound se_0776
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに促されて、教室へと足を踏み入れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどの廊下での一幕のせいか、教室の中にはどこか浮ついた空気が残っていた。"



show girl_a2_2 at center
with dis
hide go_m_02_12

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0089
Seito "「わあ……っ、編入生？」"

hide girl_a2_2
show girl_a2_2 at left

show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0123
Seito "「留学生でしょ？」"

hide girl_a2_2
show girl_a2_3 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0090
Seito "「このクラスに決まったのね！」"

hide girl_a2_3

hide girl_b1_3
show girl_b1_3 at left

show boy_a2_2 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0055
Seito "「新入生を迎えるなんてラッキーだな！\n
占いにも、今日のラッキーアイテムは新しいものって出てた」"

hide girl_b1_3

hide boy_a2_2
show boy_a2_2 at left
show boy_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0096
Seito "「……いや、新入生はアイテムじゃないだろ」"

hide boy_a2_2

hide boy_b1_5
show boy_b1_5 at left

show girl_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0124
Seito "「どこから来たのかしら……」"

hide boy_b1_5

hide girl_b2_5
show girl_b2_5 at left
show boy_a1_8 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0056
Seito "「名前、なんていうんだろ？」"

play sound se_0667
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの声に、少しの間は静かになっていた教室。\n
だが、私が入室したことにより再び賑やかになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒の数は大体二十人程度、だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア高位魔法学校とはいえ、その辺りのクラス構成は私がよく知る学校とそう変わらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いっせいに好奇の眼差しを向けられると、怯みそうになってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなふうに騒がれた経験なんて、今までにない。\n
自己紹介をしなければいけないのは分かっているのだが……。"

play sound se_0667
hide girl_b2_5

hide boy_a1_8

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（ど、どのタイミングで口を開いたらいいのか……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大勢がいくつかのグループにわかれてがやがやと話しているせいで、会話の切れ目が見つけられない。\n
ゴーランドに助けを求めたくなる。"


show bor_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0000
Hatena "「ねえねえ。\n
あんた名前なんていうの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "困りきっているタイミングで、賑やかな喧騒の中より私宛の声が一つ響いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他のクラスメイト達のように私についてがやがや周囲で騒ぐよりも、そうやって直接聞いてくれたほうが私としても答えやすい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「[firstname]＝[familyname]よ。\n
[firstname]って呼んで？」"

hide bor_m_02_6
show bor_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice bor_r0001
Hatena "「ふうん？\n
[firstname]……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日当たりのいい窓側の列の後ろのほうに座った生徒が、私の答えに満足そうに目を細めて笑う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピンク色の派手な髪色をした、男子生徒だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……あえて一番目立つであろう特徴には触れない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なぜなら、それがこの世界の摂理だからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（そう……、ペーター同様、そこは置いておくとして……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "派手な外見をしてはいるが、とっつきにくそうな印象はない。\n
不思議と人懐っこそうな笑顔だ。"

hide bor_m_02_1
show bor_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0002
Boris "「可愛い名前だね。\n
俺はボリス。ボリス＝エレイだ。よろしくね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「ええ、よろしく。\n
……他の皆も、よろしく」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とボリスの会話を聞いていたクラスメイト達へと視線を流して、にっこりと笑う。彼を利用する形にはなってしまったが、これでどうにか名乗ることはできた。"


show girl_a2_4 at center
with dis
hide bor_m_02_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0091
Seito "「あ……、ボリス、自分だけずるいわ」"

hide girl_a2_4
show girl_a2_4 at left

show boy_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0057
Seito "「なあなあ、俺はさ……」"

hide girl_a2_4
show girl_a2_7 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0092
Seito "「あ、抜け駆けはずるいわよ。\n
あたしはね……」"

play sound se_0667
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分で話しかけたほうが早いと思ったのか、彼らは堰を切ったように話しかけてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（わ、わわわわわっっ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲で騒がれるよりは私個人に話しかけてくれたほうが……、という先ほどの感想に嘘はない。だからといって、こんなにいっぺんだとやはり困る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（極端すぎよ）"

hide girl_a2_7
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice mat_g0093
Seito "「なんの科目が得意？」"

hide boy_a1_2
show boy_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice oni_g0058
Seito "「飛行術って好き？\n
俺は箒派なんだけど、最近モップとかで飛ぶ奴もいてさあ……」"

hide boy_a1_3
show boy_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice oni_g0059
Seito "「ああいうの、邪道だよな？\n
そう思うだろ？」"

hide girl_a2_3


show boy_b2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice suz_g0097
Seito "「動物を使役することについて、どう思う？」"

hide boy_a1_2


show girl_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice mat_g0094
Seito "「動物といえば、使い魔ってどんなの使ってる？\n
私はねえ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……っ。\n
ね、待って、そんないっぺんに言われても……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口々に話しかけてくるクラスメイトたちを交互に見やる。\n
おろおろと、慌ててしまう。"

hide girl_a1_2

hide boy_b2_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "助け舟を入れてはくれないか、と見やった先のゴーランドは、何が楽しいのか満足げな笑みを口元に浮べているばかりだ。\n
助けてくれる気配はゼロ。"

play sound se_0667
play sound se_0754 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、がやがやと響く喧騒の中、足音が聞こえた。\n
全力疾走しているかのような、激しい足音だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その足音は次第にこちらへと近づいてくる。"

play sound se_0667
play sound se_0273
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぱんっと、勢いよくドアが開く。"


play music pierce_t_ali

show pia_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0000
Hatena "「遅刻だ！遅刻だよ遅刻だよ……！\n
遅刻はまずいよね、うん、まずいよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教室の中へと飛び込んできたのは、幼い印象の男子生徒だった（あえて一番目立つ以下略）。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見た感じは、私より年下のようにも見える。"

hide pia_m_02_6
show pia_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0001
Hatena "「……ふう。\n
遅刻しそうだった……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……明らかに、遅刻よね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遅刻しそうも何も、現時点で確実に遅刻だ。\n
なにしろ、先生よりも、新入生である私よりも遅く来ている。"

hide pia_m_02_11
show pia_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0002
Hatena "「ああ、よかった……。\n
間に合った……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、本人は教室に飛び込んできて、いかにも間に合ったかのような雰囲気を醸し出していた。"

hide pia_m_03_5
show pia_m_03_5 at left

show bor_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0003
Boris "「よくねえよ。\n
間に合ってないし、遅刻に決まっているだろ、馬鹿ネズミ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_6")
T "{size=+20}（……あ）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "{size=+20}（……ネズミって言った）{/size} "

hide pia_m_03_5
show pia_m_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice pie_r0003
Hatena "「え？俺、走ってきたよ？\n
走ってきたのに遅刻なの？」"

hide pia_m_03_3
show pia_m_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice pie_r0004
Hatena "「なんで、遅刻？\n
おかしいよ、馬鹿はボリスだよ」"

hide bor_m_03_3
show bor_m_01_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice bor_r0004
Boris "「俺は猫であって、馬や鹿じゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（ああ、猫って……）"

hide pia_m_01_4
show pia_m_01_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice pie_r0005
Hatena "「俺だって、ネズミであって、馬や鹿じゃないよ。\n
やっぱりボリスは馬鹿なんだ」"

hide bor_m_01_8
show bor_m_02_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice bor_r0005
Boris "「ふ～ん？ネズミのくせに生意気……。\n
世界観違うからって、ネズミが猫に歯向かって無事ですむと思っているんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（あああ、禁句を……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "禁句を言いつつ、ボリスはナイフやフォークは取り出さなかった。\n
彼は世界観の違いについて知っている、賢いチェシャ猫なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、別のものは取り出した。"

hide bor_m_02_13
show bor_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0006
Boris "「……食らえ！」"

play sound se_0246
$ flash(.2)

play music gag1_a_wam

show m_op2_3_1 onlayer master
with dis
hide bor_m_02_2

hide pia_m_01_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴしっと、ボリスが指で作ったゴム鉄砲から放たれた輪ゴムが、彼の体に当たる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（杖じゃないあたり……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いまいち、世界観とかごにょごにょの事情を理解しているとは思えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0006
Hatena "「ぴ！？痛いよ！酷いよ！\n
ボリスがいじめるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0007
Boris "「にゃははは。\n
ネズミのくせに生意気なことを言うからだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0006_5
Hatena "「ううう……。\n
ボリス嫌いだよ、意地悪猫……、くすん、くすん」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（猫とかネズミとか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "禁句が出放題。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いじめの現場かとも思うが、それにしてもクラスメイトはおろか、担任であるゴーランドまで止めようとしていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、この二人のやりとりはいつものことであるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いじめられっこはくすんくすん、と鼻を鳴らしながらも空いている席につこうとして……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その途中で私の存在に気づいたのか、ぴたり、と目の前で足を止めた。"


play music classroom_day_p_wam
hide m_op2_3_1


show pia_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0007
Hatena "「あれ？あれ？\n
こんな子、いたかな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょこん、といった感じに首をかしげて、じいっと真っ直ぐに見つめてくる。"

hide pia_m_01_3
show pia_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0008
Hatena "「君、誰？\n
俺、君のこと忘れちゃった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「[firstname]＝[familyname]というの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「新入生よ。\n
今日からあなたと同じクラスになるわ」"

hide pia_m_01_8
show pia_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pie_r0009
Hatena "「！！」"

hide pia_m_01_3
show pia_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pie_r0010
Hatena "「新入生！？\n
君、新入生なの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え、ええ」"

hide pia_m_03_3
show pia_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice pie_r0011
Hatena "「俺、新入生好きだよ！\n
新入生は、俺のこといじめないからね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「そ、そう。\n
まあ、いじめる気なんかないけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言うと、彼はにこにこと人懐こい笑顔をうかべた。"

hide pia_m_03_6
show pia_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0012
Hatena "「でしょ、でしょ、いじめないよね。\n
だから、好き！」"

hide pia_m_03_5
show pia_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0013
Pierce "「俺はね、ピアス＝ヴィリエ。\n
ねえ、君は俺のこと好き？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "{size=+20}「はい？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いきなりぶっとんだことを聞かれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「初対面で、好きも嫌いも……」"

hide pia_m_03_10
show pia_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice pie_r0014
Pierce "「俺はね、君のこと好きだよ！\n
君も俺のこと好きになってほしいな？ね、いいよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「え、えええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、これでも年頃の女。\n
そして、彼だって年頃の男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなふうに、幼い子のように好き嫌いを言われても困る。"


show m_op2_4_1 onlayer master
with dis
hide pia_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0033
Gowland "「……ピアス。\n
おまえ、新入生を困らせてるんじゃねえよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ようやく私が困っていることを察知してくれたのか、ゴーランドがピアスの襟首をひょいと引っつかんで引き寄せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0015
Pierce "「うう～、俺、困らせてなんかないよ？\n
仲良くなりたいだけだもん。なんで、駄目なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずるりと引き離されて、ピアスは抵抗するように身を捩る。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0034
Gowland "「そんな、初対面でいきなり好きか嫌いかなんて聞かれても困るだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Pierce "「？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gowland "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0035
Gowland "「……困らないか、おまえの場合は」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0016
Pierce "「困らないよ？\n
俺、もう好きになっちゃったもん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「す、好きに……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "初対面なのに、と繰り返そうとするが思い留まる。\n
なんとなく、言っても無駄だと察知できた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_11")
T "「それは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他に答えようがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0017
Pierce "「ふふ、どういたしまして。\n
君にはね、俺の友達も紹介してあげる！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0009
Boris "「馬鹿ネズミ！\n
やめろよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0095
Seito "「ピ、ピアス！\n
それはやめて！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0060
Seito "「そうだよ！\n
やめとけ、ピアス……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスが、「友達」を紹介することがそんなにまずいことなのだろうか。クラスメイト達は口々に制止の声をかけるが、ピアスはそんなものを聞いてはいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0018
Pierce "「俺と友達になるんだし、俺の友達の友達にもなってほしいな。\n
きっと、俺の友達も君が好きになるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にこにこと上機嫌に私へと手を差し出し……。"

play sound se_0136

play music gag1_a_wam
hide m_op2_4_1
show m_op2_4_2 onlayer master with expand
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（ネ……、ネズミ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "茶色っぽい毛色の、ネズミ。\n
それが、ピアスの手のひらの上でおとなしく丸くなっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「この子が……、ピアスのお友達なの……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスの拙い喋り方のせいだろうか。\n
クラスメイト相手だというのに、年下の子でも相手にするような口調になってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0019
Pierce "「うん、そうだよ！君、ネズミが嫌いじゃないんだね？\n
他にもいっぱいいるんだ！全部、紹介するよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「ネズミは……、嫌いじゃないけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（……好きでもないけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（い、いっぱい……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice suz_g0098
Seito "「や、やめろ！\n
ピアス～～！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice nos_g0125
Seito "「ピアス！やめなさい！\n
雷を食らわすわよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice suz_g0099
Seito "「それもよせ！\n
ネズミのウェルダンなんて見たくない！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは騒ぎはするものの、魔法を使うかは逡巡し……。\n
そうこうするうちに……。"

play sound se_0105
##special anime pierce_friends
hide m_op2_4_2
show m_op2_4_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さーっと、自分の血の気が引いていく音を聞いたような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ネズミ、だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、ネズミは怖くない。\n
ピアスに言ったのも、強がりというわけではなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "虫ならともかく、ネズミが出たくらいでぎゃあぎゃあ騒ぎ立てたりするほど、私は神経質ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女らしくないともいうのかもしれないが……、度胸はあるほう。\n
しかし、限度もある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスの手の上、腕の上、頭の上。\n
懐、ズボンの裾、その影。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ありとあらゆる場所から、ネズミがうぞっと顔を出していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……っっ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悲鳴をあげそうになる。\n
一匹なら可愛く見えないこともないネズミも、これだけいるとホラーだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0020
Pierce "「ネズミ、好きなんだよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「い、いや……、嫌いじゃないけど……、好きだとも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice pie_r0021
Pierce "「嫌いじゃないなら、好きってことだよ！\n
君が、ネズミのこと嫌いじゃなくてよかったよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_9")
T "{size=+20}（今、嫌いになりそうよ）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスは、にこにこと嬉しげに無理やりな理屈を言ってくる。\n
その間にも、足元をてててて、とネズミが駆け回る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その背後では、床を大量のネズミで占拠されたクラスメイトたちが、無言で恐怖に慄いていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声を出す元気もないらしい。\n
単体なら可愛くとも、小さなものが集団になると不気味だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0036
Gowland "「ピアスは、潜在的に動物との相性がいいんだが……。\n
今のところその才能はネズミにのみ、特化してるんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が固まっていると、傍らのゴーランドがこそっと耳打ちするようにして教えてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「召喚術の才能があるってこと……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gor_r0037
Gowland "「……ネズミに限って、な」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gor_r0038
Gowland "「……はあ。おい、ピアス、おまえのお友達を戻してくれ。\n
ホームルームを始めるからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gor_r0039
Gowland "「そいつらは生徒じゃないし、部外者……、いや、部外ネズミは邪魔だ。\n
ほら、席につけ」"


play music classroom_day_p_wam
hide m_op2_4_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドが疲れたように溜息を吐き出して、ピアスの襟首を捕まえていた手をぱっと放す。"


show pia_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0022
Pierce "「そっか、ホームルームなら仕方ないよね。\n
皆おいで、授業が始まるからね」"

play sound se_0105
##special anime pierce_friends
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大量のネズミは、ピアスの言うことを理解したのか、現れたときと同じようにするするとピアスの元へと戻っていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……ピアスのどこに、あれだけのネズミが収まっているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法を使ったようにも見えなかったので、何かのマジックアイテムを使用したのかもしれない。"

hide pia_m_03_13

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスは、ゴーランドに促されるまま、おとなしく席につく。"


show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0040
Gowland "「んじゃ、ピアスとピアスの友達も落ち着いたことだし……、ホームルームを始めるぞ。[firstname]、あんたも席についてくれるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え……、でも、どこに……」"

hide go_m_03_9
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_r0041
Gowland "「席は空いてるところに適当に座ってくれたらいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、席は埋まっているように見える。"

hide go_m_02_12


show bor_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「…………」"

play sound se_0496
hide bor_m_03_7
show bor_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「！」"

play sound se_0736
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しゅわっと椅子と机が流れてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこから出てきたのかは分からないが、それはボリスの席の近くで止まった。"

play sound se_0167
hide bor_m_03_2


show girl_a2_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0096
Seito "「わ！」"

play sound se_0167
hide girl_a2_4
show girl_a2_4 at left
show boy_a1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0061
Seito "「こら！？\n
ボリス、何するんだよ！？」"

play sound se_0167
hide girl_a2_4
show girl_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0097
Seito "「勝手に、人の席を移動させないでよ！？\n
わわ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「！？」"


show bor_m_01_10 at center
with dis
hide girl_a2_5

hide boy_a1_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice bor_r0010
Boris "「……はい、どうぞ。\n
ここが、あんたの席」"

play sound se_0167
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かしゃんかしゃんと他の机が移動して、ボリスの席の隣に場所があく。\n
そこに、先刻の机がはめ込まれ、完成。"

hide bor_m_01_10
show bor_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0011
Boris "「パズルみたいだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは尻尾を軽く揺らして、得意げだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「うん……、どうも。\n
でも……、いいの？」"

hide bor_m_02_3
show bor_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice bor_r0012
Boris "「そりゃあ、もちろん……」"

hide bor_m_02_2
show bor_m_02_2 at left
show girl_a1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice mat_g0098
Seito "「よくないわよ！\n
ボリス、あんた勝手に……」"

hide bor_m_02_2
show bor_m_02_2 at left_center
hide girl_a1_7
show girl_a1_7 at center
show boy_a1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice oni_g0062
Seito "「俺の席、さぼりやすかったのに……」"

hide boy_a1_5
show boy_a1_4 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice oni_g0063
Seito "「……もが！？」"


show go_m_01_9 at center
with dis
hide bor_m_02_2

hide girl_a1_7

hide boy_a1_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gor_r0042
Gowland "「……はい、口にチャック。\n
よし、それじゃあ、まずは連絡事項から伝えていくぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつのまにか、ゴーランドは杖を持っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さぼりやすいだのと失言した生徒は、口を押さえ、もがもが……。\n
魔法で、口を閉じられてしまったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、なにごともなかったかのように、通常のホームルームが始まる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遅刻した生徒に紛れ、私もいつのまにやら、一員になっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれで、ピアスの登場は私を助けてくれたのかもしれない。\n
……後ろから見る限り、考えあってのこととは思えないが。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（遅刻しておいて、爆睡……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（眠りネズミね……）"

hide go_m_01_9

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play music classroom_day_p_wam
play sound se_0497
play sound se_0560
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日のホームルームは、明日以降の授業の日程などの説明を中心にして無事に終わった。本格的に授業が始まるのは明日からになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "クラスメイトのほとんどにとっては、今日までは春休みの延長なのだろう。ゴーランドが教室を出て行くと、皆思い思いに集まっては雑談に花を咲かせている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の周りにも多くのクラスメイトが集まってきてくれていて、各々が自己紹介など賑やかなことになっていた。"


show girl_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0099
Seito "「それでね、私は……」"

hide girl_a2_2
show girl_a2_2 at left
show boy_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0064
Seito "「俺はさあ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「うんうん。\n
私も……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "内容のないような話でも、コミュニケーションは非常に大切。が、残念ながら、私は皆と同じようにのんびり雑談を楽しんでいるわけにはいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ、まだ寮の部屋が決まっていないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法を使えば荷物の移動はあっという間だが、それでもその運び込んだ荷物の整理などをする時間は必要となる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（荷解きは気が重いなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "詰め込みすぎてしまったかもしれないと、入れてきたものを思い返す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ともかく、慣れない寮生活のスタートだ。\n
時間に余裕は持っておいたほうがいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「私、そろそろ事務室のほうに行かなくちゃ。\n
まだ、寮が決まっていないの」"

hide girl_a2_2
show girl_a2_9 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice mat_g0100
Seito "「あら、まだ寮が決まっていなかったの？\n
それなら、こうしてのんびりもしていられないわね」"

hide girl_a2_9
show girl_a2_3 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice mat_g0101
Seito "「早く決めてしまったほうがいいわ。\n
ちなみに私は、赤薔薇寮よ」"

hide boy_a1_3
show boy_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice oni_g0065
Seito "「寮選びって難しいよなあ。\n
俺は、帽子屋寮だぜ」"

hide girl_a2_3

hide boy_a1_2
show boy_a1_2 at left
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice nos_g0126
Seito "「あたしは遊園地寮！\n
ゴーランド先生もいるのよ」"

hide boy_a1_2

hide girl_b1_3
show girl_b1_3 at left

show boy_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice suz_g0100
Seito "「僕は、雰囲気が好きで、塔。\n
他のところと違って、落ち着いているんだ」"

hide girl_b1_3
show girl_b1_2 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice nos_g0127
Seito "「唯一、ね」"

hide boy_b1_8
show boy_b1_3 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice suz_g0101
Seito "「そうそう、塔は唯一落ち着いた場所だ」"

hide girl_b1_2

hide boy_b1_3
show boy_b1_3 at left
show boy_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice oni_g0066
Seito "「落ち着いていてどうするんだよ、賑やかに楽しまなくちゃ！」"

hide boy_b1_3
show boy_b1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice suz_g0102
Seito "「まあ、どの寮もそれぞれの特色があって面白いよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（そう言われちゃうと……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「迷うわね……」"

hide boy_b1_2

hide boy_a1_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、シンフォニアの学生寮には、それぞれ個性的な名前がついているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校案内のパンフレットには、「４つの学生寮があり、生徒がそれぞれ選ぶことができる」という風にしか書いていなかったのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前だけでなく、寮によって雰囲気まで違うらしい。\n
選ぶのが難しくなりそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんせ、学生生活の拠点となる場所。\n
うかつに、合わない場所を選択しては後が大変だ。"

$ gakuen_op3a_read_seen = False
$ gakuen_op3b_read_seen = False
$ gakuen_op3c_read_seen = False
$ gakuen_op3d_read_seen = False

jump gakuen_op3
