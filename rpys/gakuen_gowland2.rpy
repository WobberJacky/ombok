label gakuen_gowland2:
scene bg_map_day
with dis
$ clockanim()


play music library_day_p_wam

scene bg15_lb_o_day with Dissolve(1.2)
play sound se_0566
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつものように、授業終了後のホームルームに参加した後、私は図書館へと向かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（……圧巻よね）"


scene bg15_lb_i_day with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア高位魔法学校に付属する図書館の蔵書量というのは、とんでもないことになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく、司書ですら具体的な数字は把握できていないのではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんでも毎日のように新しい本が仕入れられては、内部を魔法で改築して書架を増やしているとのこと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見つけるのに時間はかかってしまうが、大体の本はシンフォニアの図書館で揃えることができる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、読書好きの私にとっては、この上なく魅力的だ。\n
最近は週に何度か、学校帰りに図書館に寄って本を借りるのが習慣になっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（転送システムもあるし、便利なのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "借りた本を、自動的に部屋まで転送してくれるシステムもあるので、どんなに分厚い本を借りても運搬に困らずにもすむ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当にいたれりつくせりなシステム付きの図書館なのだ。\n
何冊か、興味のある分野の本を借りて、自室への転送システムを利用した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が部屋に戻る頃には、送り届けられているだろう。\n
手続きを終わらせてから、のんびりと寮へ戻る。"

with dis
$ hi_mes()


scene bg15_lb_i_day with Dissolve(.8)

scene bg15_lb_o_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_par20_re
with stripe_l_long

play music entrance_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あら？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮のエントランスへ足を踏み入れたところ、珍しい一団に出会った。\n
ゴーランドに、ボリス、そしてエースという組み合わせだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドとボリスという組み合わせは、決して珍しくない。\n
ボリスは遊園地寮の寮長だし、ゴーランドは遊園地寮の責任者だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この二人が一緒になって寮内にいるのは、ああ仕事なのかといったふうに理解できる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だがそこにエースが加わると、一気に何の集団なのかが分からなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……一人加わるだけで、その場を混沌におとしめる男）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よく知らない相手なのに、それがエースという人だと言い切れてしまう。\n
なんだか、彼は自寮にいるときでさえ違和感のようなものがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（二人とも、授業が終わってすぐに戻ったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスはともかく、ゴーランドは教師だ。\n
放課後とはいえ、こんな早い時間にすでに寮に戻っているというのは珍しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人は連れ立って歩きながら、談笑（？）している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子寮へと向かいながら、気になってそちらへと視線をやっていれば、エースと目が合ってしまった。"


show ace_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0446
Ace "「やあ、[firstname]！\n
こんなところで君に会えるとは奇遇だね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……そう？\n
私、遊園地寮の人間だから、ここにいてもおかしくはないわよ？」"

hide ace_m_01_10
show ace_m_01_10 at left
with dis

show bor_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice bor_g0094
Boris "「ああ、おかえり、[firstname]。\n
遅かったね、図書館に寄っていたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「正解よ、図書館に寄ってから戻ってきたの。\n
でも、遅い……、っていう時間でもなくない？」"

hide bor_m_02_6
show bor_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice bor_g0095
Boris "「やあ、ほら。俺達と同じ時間に解放はされているはずだろ？」"

hide bor_m_01_10
show bor_m_02_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice bor_g0095_5
Boris "「それなのに俺達より帰宅が遅いってことは、どこかに寄ったんだろうなって思ってさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「それで、すぐ図書館って言われるあたり、私って行動が分かりやすいのかしら」"

hide ace_m_01_10

hide bor_m_02_1
show bor_m_01_10 at left
with dis

show go_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice gor_g0035
Gowland "「そりゃあ、あんたの本好きはいかにもって感じだしな。\n
いいことだと思うぜ？そこの馬鹿猫に爪の垢でも飲ませてやりたい」"

hide bor_m_01_10
show bor_m_01_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice bor_g0096
Boris "「にゃにおう……。\n
俺、これでも成績はいいって知ってるだろ？」"

hide go_m_01_10
show go_m_03_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice gor_g0036
Gowland "「実技はな。\n
筆記試験になると、からきしなんだよ、おまえは」"

hide go_m_03_1
show go_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice gor_g0037
Gowland "「呪文でも、スペルミスが目立つし……。\n
古代語も苦手だったよな？」"

hide bor_m_01_8
show bor_m_03_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice bor_g0097
Boris "「う……。\n
でも、筆記テストの点もそこまで悪くない……」"

hide go_m_01_6
show go_m_03_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice gor_g0038
Gowland "「選択問題を当てまくってるからだろ。\n
……勘はいいもんな、勘は」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……勘は駄目でしょう。\n
動物の勘とはいえ……、実力じゃないわよ」"

hide bor_m_03_5
show bor_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice bor_g0098
Boris "「な……っ。\n
あんたまで、いじめないでよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_4")
T "「いじめていないわよ。\n
諭しているの」"

hide bor_m_01_3

hide go_m_03_7


show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_4")
voice ace_g0447
Ace "「……ふ、はは、遊園地寮は仲良しだよねえ。\n
羨ましくなっちゃうぜ」"

hide ace_m_03_3
show ace_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_4")
voice ace_g0448
Ace "「赤薔薇寮じゃ、まず望めないもんな。\n
そういう会話は」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（赤薔薇寮は、仲がいいのか悪いのか、微妙きわまりないものね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薔薇の女王こと傲岸不遜なビバルディに、潔癖症の書記・ペーター。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自治会の風紀をしているエースとで、この三人は常日頃からいがみ合っているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "常人なら耐えられなさそうな罵りあいや厭味の応酬だが、日常化しているらしいから平気なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……で、その赤薔薇寮のエースが、遊園地寮で何をしているの？\n
まさか、引っ越してくるつもりじゃあないわよね？」"

hide ace_m_02_4
show ace_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice ace_g0449
Ace "「あはは、君のいるところに引越ししたがっているのはペーターさんだけで充分だよ。\n
俺は、仕事で来ているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……仕事？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースの仕事というと、塔にも出入りする風紀担当だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風紀というからには、学校内の校則違反などをチェックしているはずなのだが……。"

hide ace_m_03_11
show ace_m_03_11 at left
with dis

show go_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0039
Gowland "「この寮は、そこのボリスが勝手にいろいろと改造を加えているからな。\n
その安全確認ってところだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「ああ、なるほど。\n
危なさそうなこといっぱいやっているものね」"

hide ace_m_03_11
show ace_m_03_11 at left_center
hide go_m_02_10
show go_m_02_10 at center
with dis

show bor_m_03_11 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice bor_g0099
Boris "「……そこで、さくっと納得しちゃわないでよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「納得せざるをえないような仕掛けを山ほど作っているくせに」"

hide go_m_02_10
show go_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice gor_g0040
Gowland "「怪我人を出してからだと遅いからな。\n
今から他のところも見せて歩こうと思っているんだが、あんたも一緒に来るか？」"

menu:
    "一緒にいく。":
        jump gakuen_gowland2_2a
    "行かない。":
        jump gakuen_gowland2_2b
label gakuen_gowland2_2a:
$ lovechara_gowland_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し考えた結果、特に用事があるわけでもないので、一緒に行くことにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "安全確認は大事だ。\n
それが自分の住んでいる寮のことともなれば尚更。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（私が関わるようなことじゃないんだろうけど……、住人だもの）"

hide ace_m_03_11
show ace_m_03_3 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice ace_g0450
Ace "「お、同行者が増えたなっ！\n
旅は道連れ、一緒に楽しもうぜ！」"

hide bor_m_03_11
show bor_m_03_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice bor_g0100
Boris "「旅じゃないって、風紀さん。\n
この面子で旅だなんて、胃が痛くなっちゃうよ……」"

hide ace_m_03_3
show ace_m_03_2 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice ace_g0451
Ace "「猫の胃って小さいんだっけ？」"

hide bor_m_03_1
show bor_m_03_13 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice bor_g0101
Boris "「……知らない」"

hide ace_m_03_2
show ace_m_02_12 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice ace_g0452
Ace "「かっさばいたら、分かるかな。\n
……ところで、猫って食べられたっけ？」"

hide bor_m_03_13
show bor_m_01_4 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice bor_g0102
Boris "「……{size=+20}知りません。\n
食べられません{/size}」"

hide go_m_01_11
show go_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice gor_g0041
Gowland "「はっはっは。\n
んじゃ、行こうぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに促されて歩き出す。"

jump gakuen_gowland2_3
label gakuen_gowland2_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「遠慮しておくわ。\n
……私が行っても、何が出来るわけでもなし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自寮とはいえ、私が関わるような役目ではない。\n
ついていったとして、役立たずで終わってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "役に立たないだけならまだしも、何かあった際には足手まといになってしまいそうだ。"

hide bor_m_01_4
show bor_m_01_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0103
Boris "「え～？そんなこと言わずに、一緒に行こうよ。\n
この面子じゃむさくるしすぎて、やる気でない」"

hide ace_m_02_12
show ace_m_03_7 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0453
Ace "「むさくるしいなんて酷いなあ、猫くん。\n
俺、悲しいよ」"

hide go_m_03_5
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0042
Gowland "「まあ、確かに男三人で歩き回ってもなあ。\n
[firstname]、特に用事がないなら一緒に行こうぜ？」"

hide ace_m_03_7
show ace_m_01_4 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0454
Ace "「そうだね、君がいたほうが楽しそうだ。\n
一緒に、冒険の旅に出かけようよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……胡散臭いわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスとゴーランドの言い分はともかく、エースの誘い文句はどこまでも胡散臭い。だが、ここまで誘われたならば、断るのも面倒だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は改めて頷くと、三人の安全点検に付き合うことにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（何もないといいんだけど……）"

jump gakuen_gowland2_3
label gakuen_gowland2_3:
play sound se_0745
hide ace_m_01_4

hide bor_m_01_3

hide go_m_03_9
##[chara3 PAY ATTENTION="false"]
pause .15
with dis
$ hi_mes()


scene bg_par20_re with Dissolve(.8)

scene bg25_rr_day
with stripe_l_long

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "安全確認の旅、というからには堅苦しい義務的なものを想像していたのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……このメンツだものね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠い目になってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "基本的にシンフォニアの建物には、何かトラブルがあった際にはそれに対処する形で魔法が発動するよう、あらかじめ仕掛けが備わっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たとえば室内で火事が起こったときには、速やかに消火のための魔法が発動するといった形だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他にも、避難用とされているゲートがきちんと発動するか、といったようなチェックが必要となる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それらを確実にチェックする手段というのが……、ひたすらに実践なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "古典的だが、確実。\n
そして、危険。"

play sound se_0659
camera at hpunch
camera at vpunch
$ flash_color("dark_red", .2)
$ flash_color("darkest_red",.2)
$ flash_color("blood_orange",.2)
pause .15
play sound se_0770

scene bg_par25_rr_sc_day with grad_t

play music gag1_a_wam

show ace_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0455
Ace "「はははっ！\n
よしよし、遊園地寮はこれで火事になっても大丈夫だな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「……っエース！！」"

hide ace_m_01_4
show ace_m_01_4 at left
with dis
##[rchara3 PAY ATTENTION="false"]
show go_m_03_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice gor_g0043
Gowland "「……やると思っていたんだ、やると」"

hide ace_m_01_4
show ace_m_01_4 at left_center
hide go_m_03_7
show go_m_03_7 at center
with dis

show bor_m_01_9 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice bor_g0104
Boris "「びっちょびちょだよ……。\n
俺思うんだけど風紀さん、この仕事向いていないって」"

hide ace_m_01_4
show ace_m_02_2 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice ace_g0456
Ace "「え？なんで？\n
汚れ仕事を厭わず、立派に風紀を正していると思うけどなあ」"

hide bor_m_01_9
show bor_m_03_11 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice bor_g0105
Boris "「……いや。\n
汚れ仕事とか、風紀に必要ないでしょ」"

hide ace_m_02_2
show ace_m_03_11 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice ace_g0457
Ace "「はは。甘いなあ、猫くん。\n
クリーンな学生生活には、掃除が必要なんだよ」"

hide go_m_03_7
show go_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice gor_g0044
Gowland "「おまえは、間違いなく掃除下手だろ……。\n
見ろよ、この廊下！水浸しじゃねえか！！」"

hide bor_m_03_11
show bor_m_01_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice bor_g0106
Boris "「ああもう、使用人に連絡しなきゃ……。\n
風紀さんが一人で怒られてよね」"

hide ace_m_03_11
show ace_m_01_3 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice ace_g0458
Ace "「ええ～？\n
なんで俺が怒られなきゃいけないんだよ～」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……それはね、エース。\n
あなたがいきなり炎系の魔法をぶちかまして、消火魔法の効果を確認するなんて暴挙に出たからよ」"

hide ace_m_01_3
show ace_m_03_4 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice ace_g0459
Ace "「暴挙なんかじゃないさ。\n
安全かどうかを確認するには、実践が何より確実なんだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……だとしても、いきなり火炎はないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……それ自体、安全じゃないし）"

hide ace_m_03_4

hide bor_m_01_8

hide go_m_01_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひとけのない廊下を選んだことが、せめてもの心遣いといった感じだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "床には水溜りができているし、壁紙はエースの放った火炎魔法のせいで焦げている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "安全確認というよりも、テロリストに近い。\n
廊下の惨状を見渡して、溜息をついた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法による被害は魔法で修復可能だが、だからといって好き放題に破壊活動をしていいというわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校内で魔法を使って、物を壊したりした場合。\n
修復をしたとしても、もちろんペナルティがあるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大体は反省文や、課題といったところだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……エースは役職があるし、本人も気にしなさそうだけども）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は迷いなく、己の行動が正しかったと信じている。\n
……道では常に迷いまくりのくせに。"


play music secret_day_p_wam

scene bg25_rr_day with grad_b

show go_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0045
Gowland "「……はあ。\n
んじゃ、これで大体の確認作業は完了したな？」"

hide go_m_03_1
show go_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0046
Gowland "「濡れた服が気持ち悪いだろ。\n
ここで解散するとしようぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドが、気持ち悪そうに濡れた髪をかきあげる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……そうね、私も着替えたいわ」"

hide go_m_02_1
show go_m_02_1 at left
with dis

show bor_m_03_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice bor_g0107
Boris "「同感。\n
俺もさっさと乾いた服に着替えたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスはぷるぷると体を震わせ、滴を落とす。\n
まるきり、猫の仕草だ。"

hide go_m_02_1
show go_m_02_1 at left_center
hide bor_m_03_13
show bor_m_03_13 at center
with dis

show ace_m_02_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0460
Ace "「なんだよ、皆堪え性がないなあ。\n
サバイバルでは着替えができないことも多いんだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「ここは寮の中だし、誰もサバイバルなんてしなくていいのよ。\n
……あなたには、必要なことなんでしょうけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここで解散して、エースがスムーズに赤薔薇寮に戻り、着替えにありつけるかといったらおそらく無理だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（付き合う気はない……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "短い付き合いだが、すでに散々なめにあわせられた経験がある。\n
この男とは最低限の付き合いに留めておこうと、教訓が出来ていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「ああ、もう。\n
本当にびちゃびちゃ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「早く着替えなきゃ、風邪ひいちゃいそうだわ」"

play sound se_0253
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅうっと制服の裾を絞ると、水滴がぽたぽたと落ちる。"

pause .5
hide go_m_02_1
show go_m_03_9 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0047
Gowland "「だな。\n
特にあんたは女の子なんだし、体を冷すもんじゃないぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽん、とゴーランドの手が肩にのり、早く部屋に戻ったほうがいいと促される。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「そうね、先に部屋に戻らせてもらう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……なんだかんだと、楽しかったわ。\n
誘ってくれてありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずぶ濡れになったのは歓迎できないが、ゴーランドとボリス、そしてエースなんていう面白い取り合わせと行動できたのはよかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はそう辞去の挨拶をのべて、くるりと踵を返そうとする。\n
その後ろで、エースが口を開いた。"

hide ace_m_02_8
show ace_m_03_3 at center
with dis
hide bor_m_03_13

hide go_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0461
Ace "「じゃあ、これで全部チェックは終了だ。\n
ちゃんと会長や塔に報告しておくから、安心してくれよな、メリーさん！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き慣れない名前を聞いた。"

hide ace_m_03_3
show ace_m_03_3 at left
with dis

show bor_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0108
Boris "「……っばか、風紀さんあんた何を！？\n
ああああ、俺知らないからな！！！」"

hide ace_m_03_3
show ace_m_03_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0462
Ace "「へ？なに？\n
まずかった？」"

hide bor_m_01_4
show bor_m_03_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0109
Boris "「まずいに決まってるだろ！\n
それ、禁句……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振り返る。\n
エースが呼んだ、ということはエース以外の人物の名前だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスのフルネームは、ボリス＝エレイ。\n
そして私の名前は、[firstname]＝[familyname]。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "{size=+20}（メリーさん？？？）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線は、その可能性がもっとも高い最後の一人へと。\n
つまり、ゴーランドだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（そういえば……）"

hide bor_m_03_1

hide ace_m_03_9


scene bg25_rr_day_s with expand
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0092
Boris "「なあなあ、あんたさ。\n
仲良くなったわけだし、おっさんのフルネームって聞いた？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0093
Boris "「ふふふふふ～。\n
今度是非おっさんに聞いてみろよ、快く教えてくれるはずだからさ」"


scene bg25_rr_day with compress
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな会話を、以前ボリスと交わしたような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（メリー……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの背中は、ふるふるふると震えているようだった。"

play sound se_0669

play music gag3_a_ali

show m_go2_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0048
Gowland "「～～～～っ、{size=+20}エースっっ！！{/size}\n
てめえ、この子は俺の名前を知らない貴重な子だったんだぞ！？」"

play sound se_0640
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるで噴火でもするように、ゴーランドがキレた。\n
常日頃肌身離さず持ち歩いているバイオリンに、光が灯る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（え、演奏する気！！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確かに今のゴーランドならば、怒りという感情のこもった鬼気迫る演奏が出来そうではある。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0110
Boris "「[firstname]、逃げるよ！！\n
おっさんがバーサークすると誰も止められないんだ……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「バ、バーサークって……！？」"

play sound se_0004
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐいっとボリスに腕を引かれ、駆け出す。"

play sound se_0525
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その間際ちらりと振り返った先で、バイオリンがぐにゃりと溶けるように形を変えるのを見た。\n
銃のような形状……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "銃のような、ではなくて、銃。\n
あれは……、ライフルだ。"

play sound se_0355
hide m_go2_1
show m_go2_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……{size=+20}！！！！！{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice ace_g0463
Ace "「やあ、メリーさんったら怒りっぽくて困るよなあ！\n
落ち着いてよ、メリーさん！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice gor_g0049
Gowland "「やかましいっ！！！！\n
その名で俺を呼ぶな、ぶっ殺す……！！！」"

play sound se_0522
$ flash(.1)
hide m_go2_2

play sound se_0522
$ flash(.1)
play sound se_0312

show bor_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0111
Boris "「ちょ……っ！！！\n
風紀さん、俺達と同じ方向にくるのやめてっ！！！」"

hide bor_m_01_8
show bor_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0112
Boris "「俺達まで巻き込まれるだろ！！？\n
おっさんに殺されるのは、あんた一人で充分だ！！！」"

hide bor_m_03_3
show bor_m_03_3 at left
with dis

show ace_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice ace_g0464
Ace "「冷たいなあ、猫くん！！\n
苦楽をともにしてこその仲間だろ？」"

play sound se_0025
$ flash(.1)
hide ace_m_03_11
show ace_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice ace_g0465
Ace "「[firstname]、君もそう思うよな？\n
ははは、仲間って素晴らしいよな！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「……っ！！！\n
あなただけは仲間にしたくないわ！！！」"

play sound se_0025
$ flash(.1)
play sound se_0025
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "{size=+20}（仲間じゃないし！\n
他人だし！）{/size} "

hide ace_m_02_4
show ace_m_03_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice ace_g0466
Ace "「どうしてだろうなあ。\n
不思議と、皆、そう言うんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "「……っ自覚しなさいよ！！！！」"

play sound se_0312
hide ace_m_03_7

hide bor_m_03_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスに手をひかれ、水浸しの廊下を走る。\n
結構なスピードで息が切れるが、隣を並走するエースは余裕たっぷりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……憎らしい）"

play sound se_0025
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「エース……っ！\n
いつもやっているみたいに、弾けないの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターとじゃれあっているときなど、エースはその剣でいつも銃弾を弾いている。"


show ace_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0467
Ace "「相手はシンフォニアの教師だぜ？\n
剣が折れちゃうよ！」"

hide ace_m_01_3

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぞっとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースだって私から見れば、充分腕のいい魔法使いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターの魔法ですら弾く彼が、真っ向からは受け止められないというゴーランドの魔法。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当たったらどうなることか。\n
想像するだけで恐ろしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（回復魔法があるとはいえ……、すっごい痛そう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後で治せばいいというものではない。"

play sound se_0025
$ flash(.1)
play sound se_0025
$ flash(.1)

show bor_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0113
Boris "「おっさんの魔法は……！\n
一撃一撃が重いし、破壊力がとんでもないんだ……！！」"

hide bor_m_01_4
show bor_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0114
Boris "「受けるなんて、考えないほうがいいぜ……！？\n
怪我するだけだ！」"

hide bor_m_03_6

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「そんな……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうなるともはや私達に残された道は逃げることしかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（……いやいや、私達は逃げる必要なんてないのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とボリスは、悪い事など一切していない。\n
悪いのはエースだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（人を怒らせるようなことをして……。\n
絶対、分かっていてやっているのよね、この男は）"

play sound se_0312
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「つ、ついてこないでよ！エース！\n
あなたが悪いんだから、責任とって殺されてきなさいよ！！！」"


show ace_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice ace_g0468
Ace "「え～？」"

hide ace_m_03_2
show ace_m_03_2 at left
with dis

show bor_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice bor_g0115
Boris "「その通り……っ、だよ！！\n
死ぬなら、あんた一人で死んでよね！！」"

hide ace_m_03_2
show ace_m_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice ace_g0469
Ace "「何言っているんだよ！\n
一人で死ぬなんて寂しいだろっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "{size=+20}「寂しく死んで！！！」{/size} "

hide bor_m_01_3

hide ace_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "憎たらしいほどに、隣を走るエースには余裕がある。\n
私は……、そろそろ限界だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もともと体力に自信があるほうでもないのだ。\n
足元が縺れそうになる。"

play sound se_0024
pause .3
play sound se_0025
$ flash(.1)
$ flash(.1)
pause .5
play sound se_0280
play sound se_0665
pause .7
play sound se_0707
camera at hpunch
camera at vpunch

show m_go2_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの放つ魔法は、壁をいともあっさりと粉砕する。\n
他の生徒の魔法のように、壁に穴を空けたり、焦がしたりするのではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "文字通り、粉砕するのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（こ、怖すぎる……っ！！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自信を持って言えるが、今までみたどんな悪夢の中で追いかけてきたものよりも、今のゴーランドのほうが恐ろしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0050
Gowland "{size=+20}「逃がすかぁあああああ！！！」{/size} "

play sound se_0025
$ flash(.2)
play sound se_0025
$ flash(.2)
play sound se_0025
$ flash(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（ひぃいいいいいっっ！！）"

hide m_go2_2


show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
Boris "「……っ！！」"

play sound se_0312
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうにかゴーランドを撒こうとしているのだろう。\n
ボリスが廊下の角を曲がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「っ……！」"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私もそれに倣おうとするものの、そろそろ体力の限界だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うまく曲がりきれずに、ボリスに腕を引かれていた体が遠心力に振り回されて大きく膨らんだ。"

hide bor_m_01_11
show bor_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「[firstname]……っ！！！？」"

hide bor_m_01_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずるっと繋いでいた手が滑って、すっぽ抜ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たたらを踏んでなんとか転ぶのだけは回避しようとするものの、減速……、どころかへたりこまないようにするのがやっとだった。"


play music disquieting_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とん、と私の背が何かにぶつかる。\n
それが何か、確認する前に勝手に喉がひっと鳴った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振り返らなくとも分かる。\n
ぬうっと頭上に差す影の正体は……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……っあ、う」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あんまりの怖さに、息がつまって、膝から力が抜けた。"


show go_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gowland "「…………」"

hide go_m_03_1
show go_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0051
Gowland "「……おっと」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その、へたりこみかけた私の腰を抱くようにして支えてくれたのは、バーサークモードに突入、暴れまわっていたはずのゴーランド本人だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お腹の前に腕が回り、背後から抱きかかえるようにして支えられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「ご、ゴーランド……？」"

hide go_m_01_11
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice gor_g0052
Gowland "「おう。どうした、[firstname]。\n
大丈夫か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「ど、どうした……、って……っっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（よ、よかった……。\n
いつもの、ゴーランドだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう安心した瞬間、膝からぐにゃりと力が抜けた。"


play music corridor_day_p_wam
hide go_m_03_9
show go_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gowland "「！！！？」"

hide go_m_02_4
show go_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0053
Gowland "「お、おい、あんたしっかりしろって！\n
大丈夫か、本当に！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（いやいや、本当に……。\n
大丈夫じゃないわよ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言い返したいが、今は息を整えるので必死だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あんな全力疾走なんて、どれくらいぶりだろう。\n
子供の頃だって、ああまで走った覚えはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずるずると抱きかかえられたまま引きずられて、壁側に移動させられた。\n
ゆっくりと床に下ろされて、一息つく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一緒にかがんで、私を覗き込むゴーランドはいつもの気のいい先生の顔をしている。バーサークモードとやらは、どうやら収まってくれたらしい。"

hide go_m_03_3
show go_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0054
Gowland "「だ、大丈夫か？\n
ナイトメア、呼んだほうがいいか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……だ、大丈夫」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "単に、日頃の運動不足が祟っているだけだ。この程度で学校医であるナイトメアを呼んでしまったら、後から恥ずかしい思いをするのが目に見えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぜえはあと呼吸を落ち着けようとしている間、ゴーランドはずっと背中をさすっていてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_9")
T "（……ようやく、落ち着いた）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「……ゴーランド」"

hide go_m_02_5
show go_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
voice gor_g0055
Gowland "「ん？\n
なんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……名前、あったのね」"

hide go_m_03_10
show go_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
Gowland "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「からかおうっていうんじゃないのよ。\n
……ただ、知らなかったから驚いたの」"

hide go_m_02_2
show go_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice gor_g0056
Gowland "「……あんたには、知られたくなかったんだよ。\n
間抜けな名前だろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（メリー……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（メリー＝ゴーランド……）"

menu:
    "メルヘンな名前だ。":
        jump gakuen_gowland2_4a
    "おかしな名前だ。":
        jump gakuen_gowland2_4b
label gakuen_gowland2_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（メルヘンな名前だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メルヘンすぎる。\n
大柄なゴーランドと、すぐには結びつかない。"

jump gakuen_gowland2_5
label gakuen_gowland2_4b:
$ lovechara_gowland_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（おかしな名前だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "でも、愛嬌がある。\n
聞いたら忘れないような名前だ。"

jump gakuen_gowland2_5
label gakuen_gowland2_5:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（冗談みたいな名前）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、気にしている様子からしてみても、本名らしい。"

hide go_m_03_7
show go_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0057
Gowland "「……メリー＝ゴーランドなんて、さ。\n
はあ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "改めてフルネームで名乗られると、確かに……、風変わりな名前だ。"


play music view_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「可愛い名前じゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_5")
T "（フォローになっていないか……）"

hide go_m_01_6
show go_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_5")
voice gor_g0058
Gowland "「……あんたなあ。\n
俺みたいな、ごっつい野郎の名前が可愛くてどうするんだよ」"

hide go_m_03_11
show go_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_5")
voice gor_g0059
Gowland "「あんたみたいな可愛い女の子なら、メリーでもいいかもしれないけどよ。\n
……俺には不似合いだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（私が……、可愛い女の子？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……そういう反応、ゴーランドだって可愛いじゃない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやって、自分には似合わない名前だと気にする姿は、可愛いような気がした。\n
自分より年上の、大人の男相手に言う言葉ではないと分かっているはずなのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それも、先刻のバーサーク状態の恐ろしさを目の当たりにした直後。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……でも）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「私は、好きだわ」"

hide go_m_02_5
show go_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice gor_g0060
Gowland "「……{size=+20}へ？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きょとんとゴーランドの目が丸くなるのを見て、自分が今何を口走ったのかを理解する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かあっと、走り回った名残以上の熱が頬に昇った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「な、名前が……」"

hide go_m_03_3
show go_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gor_g0061
Gowland "「名前……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_7")
T "「親しみやすくていいっていうか……」"

hide go_m_01_11
show go_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_7")
voice gor_g0062
Gowland "「そ、そうか……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "のろりと腕を持ち上げ、待ったのポーズをとる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……酸欠で、頭がまわっていないの」"

hide go_m_03_7
show go_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice gor_g0063
Gowland "「は……、はは、そう、だよな！\n
ははは、そうだよな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……ええ、そう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（そうよ。\n
そうに決まっている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深く考えず、ぽろりと漏れた。\n
だからといって、自覚もしないような本心が出てしまったというようなことではない……、はずだ。"

hide go_m_01_8
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0064
Gowland "「あんたが落ち着いたら、女子寮の入り口まで送っていってやるよ。\n
……怖がらせて、悪かったな」"

hide go_m_03_9
show go_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0065
Gowland "「この名前、どうもトラウマがあってさ……。\n
ガキの頃からからかわれ続けると、大人になってもこう……、ムキになっちまう」"

hide go_m_01_13


show m_go2_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽんと大きな手が私の頭の上に乗る。\n
ゴーランドは、よくこうして私の頭を撫でてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうしていると小さな女の子にでもなったような気になってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（子供の頃のトラウマ、か……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大人である彼にも、そういうものがあるのが、なんだか不思議だ。\n
こんなに……、私よりもずっと、大人なのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……分かるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
Gowland "「？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「子供の頃のコンプレックスって、消えにくいわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice gor_g0066
Gowland "「あ～……、まあな。\n
ガキっぽいとは思うが……、どうも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "親しみやすくていい。\n
先刻のは咄嗟に出た言葉だが、私の彼への印象を端的に表していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じように危険でも、エースなんかとはまったく異なる。\n
人を警戒させない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（そういうところ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（……好きだわ）"

with dis
$ hi_mes()
hide m_go2_3


scene bg25_rr_day with Dissolve(.8)

scene bg_par15_rg_amu_day
with stripe_l_long

scene bg_map_day
with stripe_l_long
##endmemory
jump gakuen_gowland3
