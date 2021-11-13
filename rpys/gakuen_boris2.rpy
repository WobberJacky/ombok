label gakuen_boris2:
scene bg_map_day
with dis
$ clockanim()


scene bg10_sb_day
with dis

play music corridor_day_p_wam

scene bg27_rk_day with Dissolve(1.2)
play sound se_0541
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業が終わって、教室を出る。"


show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0208
Boris "「なあ、[firstname]！\n
あんた、寮に戻るなら一緒に行ってもいい？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中から声をかけられて、振り返る。\n
ボリスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……珍しい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段なら、夕食を終えてから寮に戻るのがボリスの常だ。\n
こんな早い時間から、寮に戻るのはあまり見かけない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「もちろん、いいけど……。\n
今日は早いわね」"

hide bor_m_01_10
show bor_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0209
Boris "「ちょっとね。\n
昨日思いついた仕掛けがあってさ、早速試したいんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……また、何か悪巧みしているの？」"

hide bor_m_02_2
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice bor_g0210
Boris "「ひっでーの。悪巧みだなんてさ。\n
俺は、遊園地寮の名に相応しいアトラクションを作ろうとしているだけだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初の頃、遊園地寮の名前の由来は、ゴーランドによるものだとばかり思っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "事実、芸術家かぶれ（芸術家と称するには勇気がいる）のゴーランドは、よく謎のオブジェをこしらえている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、そんなゴーランドの作った奇怪なオブジェに、いらない機能を魔法で追加するのはボリスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前思わぬ体験をしてしまったレクリエーション室以外にも、彼の「作品」は様々。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目からビームが出る防犯石膏像など、不穏なものが遊園地寮内には潜んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、ボリスはそのシリーズに追加を行おうとしているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……で、今度は何をしようとしているの？」"

hide bor_m_01_11
show bor_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0211
Boris "「え、なになに。\n
俺のすることに、興味あるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（なんだか、前にも似たようなことを聞かれたけど……）"

menu:
    "興味がある。":
        jump gakuen_boris2_2a
    "ない。":
        jump gakuen_boris2_2b
label gakuen_boris2_2a:
$ lovechara_boris_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……我が身の安全のためにも、是非。\n
知っておきたいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知らずに何か恐ろしい仕掛けにひっかかるよりは、あらかじめどこにどんな危険が潜んでいるのかを把握しておきたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスの「作品」は、悪戯仲間である双子との共同開発のケースも多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "罠（のつもりはないアトラクション）にひっかかって痛い目にあうのは、ピアスを見て思い知っている。"

hide bor_m_01_5
show bor_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0212
Boris "「なんか、望んでたのと方向性の違う返事だけど……、ま、興味は興味でいっか。\n
それじゃあ、行こう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……え？\n
な、なんで！？どこに！？」"

hide bor_m_03_11
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice bor_g0213
Boris "「え？あんた興味あるんだろ？\n
だから、一番に楽しませてやるよ」"

jump gakuen_boris2_3
label gakuen_boris2_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「ないない。\n
興味なんてちっともないわよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "はっきりきっぱりと言っておく。\n
そうでもないと、実験台にされてしまいかねないというのを、私はもう学んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスの「作品」は、悪戯仲間である双子との共同開発のケースも多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "罠（のつもりはないアトラクション）にひっかかって痛い目にあうのは、ピアスを見て思い知っている。"

hide bor_m_01_10
show bor_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0214
Boris "「にゃはは。\n
それはあんたが、この画期的なアイディアをよく知らないからだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……別に、知りたくないし」"

hide bor_m_02_6
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice bor_g0215
Boris "「遠慮するなって。\n
知れば、興味がわくこと間違いなしだから」"

jump gakuen_boris2_3
label gakuen_boris2_3:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「いらないわよっっ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（このノリ……。\n
ゴーランドの音楽と変わらない……）"

hide bor_m_01_10
show bor_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice bor_g0216
Boris "「新作が完成したんだよね～。\n
試してみてよ。すぐ気も変わるよ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「いらないってばっ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「新作」を「新曲」に変えれば、ゴーランドそのものではないか。\n
同じ寮だと性質も似るのか、ボリスも相当にタチが悪い。"

hide bor_m_01_6
show bor_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0217
Boris "「まっさきに楽しませてあげたいんだよ。\n
俺の気持ちを汲んでって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうにいうと響きはいいが、早い話が実験台だ。\n
断固遠慮しておきたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……が。\n
跳ね除けられない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずるずると腕を引かれて、私は遊園地寮への帰路を辿る。"

hide bor_m_02_3
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg27_rk_day with Dissolve(.8)

scene bg_map_day with stripe_l_medium

scene bg_par15_rg_amu_day
with stripe_l_medium

scene bg_par20_re
with stripe_l_long

play music entrance_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスによって連れてこられたのは、遊園地寮のエントランスだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま正面に進んでいけば、男女共用区域があり、左右に分かれれば男子寮・女子寮になっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かつてゴーランドがリサイタルをしたこともあり、ホールにはそれなりの広さがある。\n
恐ろしい記憶が蘇ってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……？\n
ゴーランドの新しいオブジェが増えたようには見えないけど……」"

##[rchara1 PAY ATTENTION="false"]
show bor_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0218
Boris "「ふふーん。\n
今回はね、おっさんのオブジェが元じゃないんだよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「それじゃあ……、今回はあなた主導ってわけね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしくは、双子との共同制作。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……危なさそう」"

hide bor_m_03_2
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice bor_g0219
Boris "「おっさんのと違って、騒音には繋がらないだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「まあね。\n
音に関しては」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの芸術センスというのは、その音楽センスもそうだが、全体的に一般人の理解できる範疇を越えてしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結果、ボリスが何らかの魔法処理をする前から、異彩を放っているのだ。\n
その上、オブジェなのに音付きだったりするものだから……。"

hide bor_m_01_10
show bor_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0220
Boris "「音以外でも、俺が作ったりアレンジするのは、おっさんのとはまるで違うって。\n
一緒にしないでくれよ」"

hide bor_m_03_6
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0221
Boris "「あんたさ、タイルの話聞いたことない？\n
矢印の方向に進んでいくタイル」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……ええと」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "記憶を探る。\n
入学当初、寮を決めようとしているときに、そんな話を聞いたことがあるような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも、いい噂ではなかった。\n
遊園地寮には、そんな恐ろしいアイテムがある……、というような。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ニュアンスからして、いいものでもなさそうだ。\n
だが、実際入寮してみて、私は未だその動くタイルに遭遇したことがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「なんだったかしら……。\n
どこの寮に決めるかで悩んでいるときに、遊園地寮にはこんなものがあるって教えてもらったことがあるのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「ああ、でも……。\n
私が聞いたのは、踏むと自動的に目的地に連れて行ってくれるっていうやつだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「何でも今は故障中で、とんでもないところに連れて行かれてしまうとか。\n
……本当にとんでもないわよね、そんな危険なタイル」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "入学式なんて、つい先日のことのような気がするのに、ずいぶんと懐かしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのときはまだどこの寮に住むかも決めていなくて、どこがいいのかと悩んでいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして遊園地寮に馴染んだ今になって思い返すと、遠い昔のような気すらしてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_16")
T "「……それ、あなたが言うのと同じタイルのことなのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「目的地まで自動的に運んでくれるっていうのと、矢印の方向へ流すタイルって結構意味合いが違ってくると思うんだけれど」"

hide bor_m_01_11
show bor_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0222
Boris "「そうなんだよね、そこだよポイントは。\n
そこが分かってないから、事故が起きたりするんだよ」"

hide bor_m_03_13
show bor_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0223
Boris "「おかげで故障物扱いで、魔力供給ストップされちまっているんだぜ？\n
もったいないよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「もったいないかどうかはさておき……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いずれにせよ、危険なマジックアイテムだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「すっごく危険だって聞いたわ。\n
あれ、本当に実在しているの？」"

hide bor_m_01_3
show bor_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice bor_g0224
Boris "「ああ、もちろん。\n
あんたが今踏んでるの、そのタイルだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "{size=+20}「ええ！？」{/size} "

play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われて、反射的に飛び退ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "矢印のほうへどんどん流されるタイル。\n
二度と目的地に辿り着けなくなってしまいそうな気がする。"

hide bor_m_02_2
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0225
Boris "「本当はワープ装置なんだよな、それ。\n
目的地に向かって、短距離ワープを繰り返して、移動時間を短縮しようって試みだったんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスがかがみこむのにつられて、私もホールにしゃがみこんだ。"


play music school_front_day_p_wam

show m_bor2_1 onlayer master
with dis
hide bor_m_01_10

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の足元にあるタイルがそうだとボリスは言っていたが、そんなふうには見えない。いたって普通のタイルで、小さく草花が描かれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0226
Boris "「よ～く見てみろよ。\n
気付かないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……気付く？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じっとタイルを見つめる。\n
描かれた草花には、咲き誇るそれと、まだ蕾のものがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんとなく別のタイルにも目をやる。\n
少し離れたところにある別のタイルにも、同じように草花が描かれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "色合いや形は違うが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あれ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0227
Boris "「気付いた？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ええ、気付いた……、と思うわ。\n
蕾の向きが違うのね？」"

hide m_bor2_1


show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice bor_g0228
Boris "「大正解！\n
んじゃ、その蕾の向く方向の先には何がある？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声に促されて、私はその蕾が向く方向を視線で追いかける。しばらく直線で進んで……、そこにはやっぱり、別の草花が描かれたタイルがあった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「また別のタイル……」"

hide bor_m_01_10
show bor_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0229
Boris "「その蕾の先には……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……あ。\n
また別のタイルがあるのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "段々私の声にも興奮が滲む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段何気なく、何も気にすることなく踏み、通っていたホールのタイル。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（この向きが、矢印になっているんだ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "隠された意味があったなんて面白い。"

hide bor_m_03_2
show bor_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0230
Boris "「壊れて止められる前は、このタイルはちゃんと使用者をどこかへ誘ったはずなんだ。\n
気にならないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……なるわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスに乗せられているのは分かるが、それでも気になるものは気になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一体誰が、何のためにこんなタイルを仕込んだのだろう。\n
わくわくとしてきてしまう。"

hide bor_m_03_4
show bor_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0231
Boris "「はは、本格的に興味が出てきただろ？\n
それじゃあ、魔力供給してみるとしようか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「え？\n
でも、壊れているんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（ボリスが修理したの？）"

hide bor_m_01_5
show bor_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice bor_g0232
Boris "「ふふ。ばっちり直ってる。\n
俺を信じろよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「うう……。\n
本当に、信じて大丈夫なんでしょうね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しっかと正面から視線を重ねたボリスの目が、悪戯っぽく瞬く。\n
信用ならない猫の目だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だというのに、興味を誘う。\n
乗ってみようという気にさせるのだからずるい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……どうしたらいいの？」"

hide bor_m_02_2
show bor_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0233
Boris "「そうこなくっちゃ。\n
ちょっとついてきてくれる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスはひょいと立ち上がると、タイルを目で追いながら、何かを探すように歩き始める。\n
私はその後をおとなしく追いかけた。"

hide bor_m_02_6
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0234
Boris "「あったあった、これだ。\n
ここにさ、手を重ねてくれる？」"


show m_bor2_2 onlayer master
with dis
hide bor_m_01_10

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "再びかがみこみ、ボリスが一枚のタイルの上に手を乗せる。\n
促されるままに、私も彼の手の上から自分のを重ねた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（……わ。\n
意外と大きいのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男の子の手だ。\n
当たり前だが、猫の手ではないし、肉球もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段同じ教室で気安く接しているせいか、こうして改めてボリスが男の子だと感じさせられるとドキっとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごつい、というよりも骨ばっている手。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0235
Boris "「せえの、で魔力流し込んでみてくれる？\n
行くぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え、ああ、うん……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice bor_g0236
Boris "「せえのっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「……！！」"

play sound se_0742
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔力が通る。"

play sound se_0364
pause .5
hide m_bor2_2
show white onlayer master with expand_long
pause .1
show m_bor2_3 onlayer master with expand_long
hide white
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱあっとタイルが光り始めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「わ、わあ……！\n
これ、どうするの、ボリス！」"


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice bor_g0237
Boris "「そりゃあ、もちろん……」"


play music laboratory_day_p_wam
hide m_bor2_3 with Dissolve(1.5)

show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
Julius "「…………」"

hide yuri_m_02_9
show yuri_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice jul_g0070
Julius "「……おまえ達。\n
また厄介なものを起動してくれたな」"

hide yuri_m_03_12
show yuri_m_03_12 at left
with dis

show bor_m_01_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
Boris "{size=+20}「！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "{size=+20}「！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後から響く、呆れ半分恫喝半分、といった声に私達は弾かれたように立ち上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振り返ると、ずーんと影を作ってそこに立つ長身の正体は、ユリウス＝モンレーだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の責任者であり、風紀委員長。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（ユリウスが、どうして遊園地寮に？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも、今はなんだかちょっと、くたびれている。\n
普段はぱりっと着こなした制服が、今はよれているようにも見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それになんだか粉っぽい。\n
制服が埃まみれだ。"

hide yuri_m_03_12
show yuri_m_02_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0071
Julius "「各寮の施設については、ある程度の自治権を認めてはいるが……。\n
ボリス、おまえはやりすぎだ」"

hide yuri_m_02_7
show yuri_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0072
Julius "「おまえの作った諸々の罠で、どれだけの被害や怪我人が出ていると思うんだ。\n
……勧告のために風紀委員を送っても、返り討ちにされるときた」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「か、返り討ち……」"

hide bor_m_01_1
show bor_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0238
Boris "「罠ってなんだよ、ただの仕掛けだろ。\n
別に危ないものなんてないぜ？」"

hide bor_m_01_12
show bor_m_03_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0239
Boris "「風紀委員さん達はあれだよ、遊び心が足りないから……」"

hide yuri_m_03_7
show yuri_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jul_g0073
Julius "「……ほほう。\n
私がこんなナリをしているのも、遊び心が足りないからということなんだな？」"

hide yuri_m_01_3
show yuri_m_03_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jul_g0074
Julius "「……はは、目から怪光線を放つ石像とは斬新だったな。\n
つい手が滑って、粉砕してしまったぞ」"

hide bor_m_03_12
show bor_m_03_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0240
Boris "「うええええ！？\n
あれ、自信作だったのに……！！」"

hide bor_m_03_1
show bor_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0241
Boris "「おっさん作の人智を超えた石像に相応しい、それっぽい演出だっただろ？\n
結構好評だったんだぜ？」"

hide yuri_m_03_1
show yuri_m_02_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jul_g0075
Julius "「誰にどのように好評を博していたかは知らないが……」"

hide yuri_m_02_11
show yuri_m_03_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jul_g0076
Julius "「……いや、そうだな。\n
その怪光線のせいで制服が焼き切られるまでは、私も遊園地寮に似合いのインテリアだと思っていたとも」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……あ、本当だ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスには珍しく着崩れた印象があると思っていたのだが、ところどころ黒く焼き切られた制服が原因のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（埃っぽいし……、他にも色々とあったんだろうな）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……ボリス。\n
悪戯は結構だけど、他寮の人まで巻き込むのはよくないわよ？」"

hide bor_m_01_11
show bor_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice bor_g0242
Boris "「……う」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮の人間はもう慣れているので、今更仕掛けに引っ掛かったりするようなことはないが、他寮の人間ならば一度は引っ掛かったるだろう。"

hide yuri_m_03_13
show yuri_m_01_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0077
Julius "「少しは反省を覚えろ。\n
猫といえど、悪戯にも程があるぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは、トラップのような仕掛けを力技で粉砕して、このホールまでやってきたらしい。\n
口うるさくなるのも当然だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「でも、そんな思いをしてまで、ユリウスはここに何をしにきたの？」"

hide yuri_m_01_8
show yuri_m_03_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0078
Julius "「馬鹿げたトラップを取り除くためだ。\n
いつ大怪我をする者が出てもおかしくない」"

hide bor_m_01_3
show bor_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0243
Boris "「大怪我まではいかないように工夫してるって」"

hide yuri_m_03_12
show yuri_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0079
Julius "{size=+20}「工夫のしどころが違うだろう」{/size} "

hide bor_m_02_2
show bor_m_01_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0244
Boris "「だって、完全に安全にしちゃったら、スリルがないだろ～？」"

hide yuri_m_01_3
show yuri_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0080
Julius "「学校にスリルなど求めるな！\n
遊園地寮と名前はついているものの、ここは学校施設の一つなんだぞ！？」"

hide yuri_m_03_7
show yuri_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0081
Julius "「いいかげん、目に余ると私自らが見に来てみれば……。\n
また新しい罠を仕掛けているところときた」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じろりとユリウスが半眼で私達が発動させたタイルへと視線を流す。\n
私も釣られたようにタイルへと一度視線を落とし……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……あれ？）"

hide bor_m_01_9
show bor_m_03_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice bor_g0245
Boris "「別に、罠ってわけじゃなくて、娯楽設備の一環！\n
委員長さんは心配しすぎなんだよ」"

hide bor_m_03_13
show bor_m_03_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice bor_g0246
Boris "「これぐらいの仕掛け、皆楽しんでるって。\n
な？だからお願い、見逃してよ」"

hide yuri_m_02_8
show yuri_m_03_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice jul_g0082
Julius "「……私の部下の風紀委員は、遊園地寮がトラウマになっているらしい。\n
トラウマになるような仕掛けを、おまえは楽しめるというのか？」"

hide bor_m_03_6
show bor_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice bor_g0247
Boris "「そ、それは～……。\n
塔の奴らは皆固すぎるんだよ、遊園地寮の皆なら楽しめるのに」"

hide yuri_m_03_4
show yuri_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice jul_g0083
Julius "「主に施設を利用する者ならそうかもしれないが、他の寮の者だって訪ねてくるだろう。\n
そういった者から苦情が来るんだ」"

hide bor_m_01_3
show bor_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice bor_g0248
Boris "「……{size=+20}来なけりゃいいのに{/size}」"

hide yuri_m_01_3
show yuri_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice jul_g0084
Julius "「方向性が違うと言っているだろう！\n
根本的に改めるほうへ考えを向けろ！」"

hide bor_m_02_7
show bor_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice bor_g0249
Boris "「そんなに危険なものはないって。\n
慣れ、そうそう、慣れの問題だよ！」"

hide yuri_m_03_7
show yuri_m_02_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice jul_g0085
Julius "「慣れてたまるか！\n
慣れるほど、遊園地寮に通い詰めるつもりはない！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは、ボリスが仕掛けを解除するまで譲りそうにない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まあ、あんな姿になっていれば当然だろう。\n
風紀委員長として、見過ごせるはずもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（これは、日を改めるしかないかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日のところは、仕掛けを解除しておいて……。\n
日を改めて、タイルの謎に再挑戦するのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先刻、新たな発見もあった。"

hide yuri_m_02_7
show yuri_m_03_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0086
Julius "「解除したトラップについては、風紀委員会に提出してもらうぞ。\n
そのタイルも、そうだ」"

hide yuri_m_03_13
show yuri_m_01_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0087
Julius "「発動しないように、ブロックをかけさせてもらう。\n
そうでもしないと、おまえの悪さは防ぎようもない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……ええっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予想以上に厳しい処置に、声をあげてしまった。\n
それでは、つい今しがた興味を持ち始めたものに対して何も出来なくなる。"

hide yuri_m_01_8
show yuri_m_03_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0088
Julius "「……なんだ？\n
文句でも？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じろりっとユリウスに睨まれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……いいえ、何も」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（せっかく、これから面白くなりそうだったのに……）"

hide bor_m_01_10
show bor_m_01_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice bor_g0250
Boris "「あるある、おおあり。\n
文句だらけだよ」"

hide yuri_m_03_12
show yuri_m_01_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jul_g0089
Julius "「おまえには聞いていない。\n
主犯に、文句を言う資格はないぞ」"

hide bor_m_01_8
show bor_m_02_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice bor_g0251
Boris "「ちぇ……、固いなあ。\n
塔の代表格なだけあるぜ……」"

hide bor_m_02_13
show bor_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice bor_g0252
Boris "「……あ～、それじゃあさ？\n
俺達に、一度だけ試させてよ」"

hide bor_m_01_10
show bor_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice bor_g0253
Boris "「そしたら、後はあんたの好きにしていいからさ。\n
一回だけ。な？」"

hide yuri_m_01_13
show yuri_m_03_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jul_g0090
Julius "「駄目だ。危険だ。\n
おまえ達は知らないかもしれないが、そのタイルはかつて怪我人を出したことがある」"

hide yuri_m_03_10
show yuri_m_02_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jul_g0091
Julius "「だから、そうやって魔力を遮断してあるんだ。\n
……そんな危ない実験、認められるか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは重々しい口調で言い切る。\n
その言い分が正しいのは私にも分かった。"

hide yuri_m_02_9
show yuri_m_02_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0092
Julius "「そもそも、最後の一回なんていう言い回し自体、危険を示している。\n
大体において、そういう場合、羽目をはずしておおごとになる」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……いわゆる、失敗フラグね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後の一回とか、これを最後に、とか、大体ろくでもない結果に終わる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風紀委員長ともなれば、生徒が危険なことに手を出そうとしているのを止めるのも道理だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それでも。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……試してみたかったなあ）"

menu:
    "自分からも頼んでみる。":
        jump gakuen_boris2_4a
    "諦める。":
        jump gakuen_boris2_4b
label gakuen_boris2_4a:
$ lovechara_boris_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「ねえ、ユリウス。\n
私からもお願い」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「一度だけでいいの。\n
試させてくれない？」"

hide yuri_m_02_7
show yuri_m_03_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice jul_g0093
Julius "「……愚か者め。\n
みすみす私の目の前で、そんな危険なことをさせられるか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "案の定、けんもほろろに断られてしまった。"

jump gakuen_boris2_5
label gakuen_boris2_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……やっぱり、諦めるしかないのかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかく、ボリスがいろいろ調べて、修理までしたのに。\n
試す前からまた封印されてしまうなんて、もったいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ユリウスが言っていることは正しい。\n
危険なことには、手を出すべきではないのだ。"

jump gakuen_boris2_5
label gakuen_boris2_5:
hide bor_m_03_4
show bor_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0254
Boris "「……分かったよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスが諦めたように、俯いた。\n
今日の放課後に話を聞いただけの私が、こんなにもわくわくとしたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前から修理などをしてきたボリスは、どれだけ気落ちしたことか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（……やっぱり、可哀想よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ねえ、ゴーランドに聞いてみたらどうかしら。\n
教師監督のもとだったら、実験してもそんなには危なくないでしょう？」"

hide yuri_m_03_12
show yuri_m_03_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice jul_g0094
Julius "「……そうだな。\n
教師がつくならば、その一度限りなら考えても……」"

hide yuri_m_03_4
show yuri_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice jul_g0095
Julius "「……いや、その一度限りというのが曲者なんだ。\n
やはり、駄目だ」"

hide bor_m_03_9
show bor_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_g0255
Boris "「どうあっても、認めてくれないってわけ。\n
……なら、もういいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_3")
T "「ボリス……」"

hide yuri_m_01_3
show yuri_m_03_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_3")
voice jul_g0096
Julius "「……ああ、探求熱心という点では気の毒だが、諦めろ。\n
おまえは悪戯がすぎるんだ」"

hide bor_m_01_12
show bor_m_02_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_3")
voice bor_g0256
Boris "「ああ、もういいよ。\n
……許可なんか求めないからさ」"

hide yuri_m_03_9
show yuri_m_02_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_3")
Julius "「！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、一瞬のスキをついてのことだった。"

play sound se_0051

play music magic_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスが私の手を取る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あ。\n
もしかして）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんとなく、ボリスがしようとしていることを察してしまった。\n
それはきっと、先ほど見たタイルのせいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔力を流し込んだときには、ボリスの手の下にあったせいで気づかなかった。\n
私達が手を重ねていたタイル、そこに描かれていたのは蕾だけの草花だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "花が一つも咲いていない。\n
他のタイルとは違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまりそれが、一番最初。\n
スタート地点のタイルなのではないのだろうか。"

hide yuri_m_02_5
show yuri_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0097
Julius "「……っ！？\n
やめろ、おまえ達！！」"

hide bor_m_02_12
show bor_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……！！」"

hide yuri_m_03_3

hide bor_m_01_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう、魔力は流してあったのだ。\n
タイルにかかった魔法は、発動している。"

play sound se_0593
pause .5
play sound se_0403

show white onlayer master with grad_b_short
hide white with grad_b_short
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とボリスは手を繋いだまま、背後へとバックステップでタイルへと飛び乗った。\n
ユリウスの怒声を置き去りに、びゅんっと景色が変わる。"

play sound se_0127

scene bg_par20_re_wa with spread_short
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……！！」"

play sound se_0400 volume .6 ##loop="true"


play music fly_wam
play sound se_0127
show t1me onlayer master with spread_short
hide t1me onlayer master with spread_short
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Boris "「……！！！」"


scene white with spread_short
play sound se_0127
show t1me onlayer master with spread_extrashort
hide t1me onlayer master with spread_extrashort
pause .4
play sound se_0127

scene bg_par25_rr_wa_day with spread_short
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……～～～！！」"


scene white with spread_short
play sound se_0127
show t1me onlayer master with spread_extrashort
show t1me onlayer master with spread_extrashort
pause .1
play sound se_0127
show t1me onlayer master with spread_extrashort
show t1me onlayer master with spread_extrashort
pause .1
play sound se_0127

scene bg_par02_ct_amu_wa_day with spread_extrashort
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
Boris "「……～～～！！」"

play sound se_0127

scene white with spread_extrashort
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "めまぐるしく目の前の景色が変わっていく。"


scene bg_par25_rr_wa_day with spread_extrashort
show t1me onlayer master with spread_short
show t1me onlayer master with spread_short
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "{size=+20}「わっ、わわわわっ！！！？」{/size} "

show t1me onlayer master with spread_short
show t1me onlayer master with spread_short

show bor_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice bor_g0257
Boris "「おわわ……っ！？\n
どわ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ぶ、ぶぶぶ、ぶつか……っ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "時折、人影らしきものが目の前をちらちらと過ぎていくのが心臓に悪い。\n
ぎゅっと目を閉じる。"

play sound se_0055
show black onlayer master with close_m
hide bor_m_01_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "タイルからタイルへと私達が高速で移動しているのだとしたら、その間に誰か人がいた場合、確実に大事故になってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……止められるはずだわ、これ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自ら危険を承知で実験に乗り出した私達が怪我をするのはともかく、誰かに怪我をさせてしまうというのは恐ろしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0258
Boris "「はは、大丈夫だよ。\n
ほら、目ぇ開けろって」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「だ、大丈夫って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそるおそる、目を開ける。"

hide black
show m_bor2_4 onlayer master with open_long
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……{size=+20}！！！{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前に誰かがいて、喉で悲鳴がひきつった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_6")
T "（ぶつかる！！！！！）"

play sound se_0338
hide m_bor2_4
show m_bor2_5 onlayer master with spread_short
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice bor_g0259
Boris "「言っただろ？\n
これ、短距離のワープを繰り返しているだけなんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ワープ……、っていうと……。\n
あれ、よね……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_3")
T "「えっと……、ゲートポイントと、ポイントを繋いで……っ。\n
そこを通り抜けるショートカット……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやって話している間にも、私達はびゅんびゅんと高速移動を続けている。\n
そのせいか思考までうまくまとまらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ワープや空間移動、高速移動なんて、難易度はともかく知識としては初歩的なものしかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0260
Boris "「そうそう。\n
だから、高速移動しているように見えるのは、残像だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0261
Boris "「俺達、実際にはゲートポイントを潜り抜けて移動しているわけだからさ。\n
人に当たる心配は、最初からないんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……っ、そ、そうなの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice bor_g0262
Boris "「ああ。\n
見ろよ、誰にもぶつかってないだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスがおどけた仕草で肩をすくめてみせる。\n
余裕に満ちたその所作に、ようやく少し心臓が落ち着きを取り戻した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "パニックになりかけていた私と違い、ボリスは冷静そのものだ。\n
それどころか、この高速移動を楽しんでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「で……っ、でも、怪我人が出たって、ユリウスが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice bor_g0263
Boris "「ああ、そう、ワープの連結部分がうまくいっていなかったみたいでさ。\n
繋ぎの部分で人に当たったとき、物理的にもぶつかっちゃうんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「だっ、駄目じゃない、それ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、当たるということだ。\n
ちっとも安心できない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0264
Boris "「大丈夫だって。\n
ちゃんと、そこは直したから」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（直したっていっても……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かつては、壊れていたものだ。\n
しかも、長期間使われていなかった装置。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……ボリスは怖くないの？\n
こんなスピードで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice bor_g0265
Boris "「へ？なんで？\n
このスピードが最高なんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice bor_g0266
Boris "「怖いどころか、超楽しい～！\n
にゃははははは～～～！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……スピードマニアだったのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思えば、時折双子と一緒に廊下で箒勝負をしているのを見かけたことがあったような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは叱るために追いかけていたが、ボリスが一緒のときはいかにも仲間といった様子で……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0267
Boris "「……あんたは？\n
怖い？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……そりゃあ、ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とはいえ、不思議と落ち着いていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……どうしてなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスの「大丈夫」を信用してしまっているのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0268
Boris "「そう、俺は楽しいけど……、あんたが怖いのは困るな。\n
……これで、どう？ちょっとは怖くなくなる？」"


play sound se_0551
hide m_bor2_5
show m_bor2_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐいっと肩を抱き寄せられた。\n
しっかりとボリスの体に寄り添う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるでベルトのようにするりとボリスの尻尾が私の腰に絡みつく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（しっぽベルト……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな状況だというのに、ほのぼのしてしまいそうになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやって肩を抱かれていると、びゅんびゅんと高速移動を続ける中で、どこかに投げ出されてしまいそうな心もとなさはなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「…………」"

play sound se_0055

scene m_bor2_6 ##instant]
hide m_bor2_6 with Dissolve(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅっと自分からも手を伸ばして、ボリスの上着を手繰った。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0269
Boris "「……ふふ。\n
よかった、お気に召したみたいだね」"

play sound se_0403
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

play sound se_0127
show t1me onlayer master with spread_short
show t1me onlayer master with spread_short
pause .4
play sound se_0127
show t1me onlayer master with spread_short
show t1me onlayer master with spread_short
pause .4
play sound se_0127

show m_bor2_7 onlayer master with spread
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "落ち着くと、今度は考える余裕が出てくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ねえ、ボリス。\n
これ、どこまで続くのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0270
Boris "「……んんー？\n
ちゃんと終わりはあるはずなんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……ボリス、これ、ちゃんと修理したのよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0271
Boris "「修理はしたけど、終着地点までは知らない」"


play music battle_ali
play sound se_0042
hide m_bor2_7
show m_bor2_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがに眩暈がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「お、下ろしてっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0272
Boris "「無茶言うなって。\n
途中下車なんか出来るわけないだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「無茶を言っているのは、あなたよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice bor_g0273
Boris "「乗る前にテストしようと思ったんだけど、風紀委員長さんが邪魔するから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「……ユリウスの言うことは正しいと、今しみじみ思っているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「まさかだけども……。\n
同じところを高速でぐるぐる回っているだけだったりしないわよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだと、永遠にループする。\n
強制的に止める以外、下りる方法がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、高速移動するワープ空間から、強制分離などしたら……。\n
……考えたくもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0274
Boris "「え～と……。\n
とりあえず今は、このスピードを楽しもうぜ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「何も考えてないの！？\n
いや、私だって、考えたくもない心境だけど！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とんでもないことをしてしまった感がひしひしとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0275
Boris "「大丈夫だって、委員長がホールにいたし。目の前で発動したんだから……、ぐるぐる回ってても、そのうち委員長が止めてくれるって」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "{size=+20}ものすごく、他人任せだ{/size}。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_13")
T "（……{size=+20}信用なんて、絶対にすべきじゃなかった{/size}）"


scene m_bor2_8 ##instant]
hide m_bor2_8 with Dissolve(.1)
play sound se_0127
show t1me onlayer master with spread_short
show t1me onlayer master with spread_short
pause .4
play sound se_0127
show t1me onlayer master with spread_short
show t1me onlayer master with spread_short
pause .4
play sound se_0127
show t1me onlayer master with spread_short
show t1me onlayer master with spread_short
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「！！！」"

play sound se_0400 volume .7 ##loop true
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ますますスピードが増しているような気もしてならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「～～～～……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_4")
T "「ボ、ボリス……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_4")
voice bor_g0276
Boris "「すっげースピード！\n
たっまんねえ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……マニアには何を言っても無駄だった。"

play sound se_0127
show t1me onlayer master with spread_short
show t1me onlayer master with spread_short
play sound se_0127
show t1me onlayer master with spread_short
show t1me onlayer master with spread_short
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「～～～～～～……！！」"

play sound se_0127
pause .7
play sound se_0173

scene white with Dissolve(.05)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か、スイッチを踏むような音がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "{size=+20}「！！？？」{/size} "

play sound se_0739

scene bg_sky_wa_day with spread_short
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、思った瞬間、私達の体は勢いよく空中に投げ出されていた。\n
ぶわっっと体が浮く感覚がする。"

play sound se_0402
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自由落下とは違う。\n
ぐんぐんと、どこまでも上昇していく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_6")
T "{size=+20}「っきゃ、きゃああああああああ！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_6")
voice bor_g0277
Boris "「{size=+20}にゃはははははは！！！{/size}\n
上下移動もアリなんて、すげー！！！！」"

play sound se_0401

scene white with spread_short
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_3")
T "「～～～～～～……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_3")
T "「～～～～～～……！！」"





pause .5
play sound se_0053
pause .3
play sound se_0216

scene bg06_sk_h_day with compress_short
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "終わりは、唐突だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……？」"


play music evening_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……あ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice bor_g0278
Boris "「にゃ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ワープの特性なのか、慣性はない。\n
まるで最初からそこに立っていたかのように、私達はその最終地点のタイルの上に立っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「え、えええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きょろきょろとする。\n
室内ではない。"

show m_bor2_9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外だ。\n
しかも、とんでもなく高い場所にいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "足元には、例のタイル。\n
始まりのタイルとは逆に、描かれた草花はすべて花として咲いており、蕾は一つもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0279
Boris "「へえ……。\n
ここ、遊園地寮のてっぺんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「て、てっぺん？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われてみれば、屋根の色などに見覚えがあるような気もする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔のように縦に長い建築物というわけではないが、それでも遊園地寮にはそれなりの高さがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら私達は、いつもエントランスに入るときに、何気なく見上げている位置にいるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0280
Boris "「やったあ……。\n
感激……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「？\n
箒や、浮遊の魔法でもこられそうだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0281
Boris "「そうだけどさあ、ロマンだよ、ロマン。\n
俺達、今新しいルートを開発することに成功したんだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0282
Boris "「シンフォニアで、今のところ誰も知らない道を、俺達だけが知っている。\n
なんか、わくわくしねえ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「する……、かな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice bor_g0283
Boris "「な～んだよ、煮え切らないなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「これでも、対応としてはマシなほうでしょう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆が知らない方法。\n
とっておきの場所に到達できる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男の子としては、特別なことなのだろう。\n
特に、ボリスのようなタイプなら。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

hide m_bor2_9
show m_bor2_10 onlayer master with compress_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "改めて、そこからの景観に目をやった。\n
夕暮れが始まり始めた空の端が、燃えるように赤く染まっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "眼下にはシンフォニアの学園が広がっているのだ。\n
景色を贅沢に感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……ねえ、ボリス」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_g0284
Boris "「んん？\n
あんたも感激した？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_14")
T "「いや、先刻の装置のこと」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「壊れているって言われていたじゃない？\n
直したっていっても、試してもいなくて、よく平気だったわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice bor_g0285
Boris "「実は、俺、最初から、壊れているとは思っていなかったんだよね。\n
正しい方法で動かせば、正しい結果が出ると思ってた」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「正しい方法？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0286
Boris "「たとえば俺達は最初のタイルから乗ったけど、もし途中のタイルから乗っていたら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0287
Boris "「もしくは、さっきあんたが勘違いしたみたいに、誰かにぶつかると思って何か別の魔法を使っちゃったとしたら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ワープ中の魔法は変に作用する……、って聞いたことあるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice bor_g0288
Boris "「そういうこと。\n
そんな事故があったせいで、これ、壊れているって言われていたんじゃないかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……確証はなかったのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice bor_g0289
Boris "「ふふ、今こうしてここにいる俺達が、その確証だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……格好よさげなセリフで、うやむやにしようとしているでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "元から平気だと思っていた。\n
つまり、確認以前に修理をまともにやっていなかった恐れがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0290
Boris "「はは、バレた？\n
でも俺……、あんたに怪我させるつもりはなかったよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いい加減な猫男が、真面目な顔で言う。\n
ぱふんと腰に絡みついたままだったピンクの尻尾が、私の腰を叩くようにして揺れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思えば肩も抱かれたままなのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もぞもぞと、居心地悪い。\n
身じろいで、離れようとする。"


scene bg06_sk_h_eve ##instant]
hide m_bor2_10

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0291
Boris "「逃げないでよ。\n
このまま、一緒に夕日見よう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐいっと引き戻された。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夕日が、赤く燃える。\n
見るものすべてが、赤く染まっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の顔が赤かったとして、もちろんそれは夕日のせいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……うう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私ばかりが居心地悪い。\n
ボリスはいつも余裕だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0292
Boris "「ねえ、[firstname]、俺さ……。\n
あんたが危なくなったら、何をしてでも助けるし……、怪我をしたら責任をとるつもりだったよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見やった隣、ボリスの顔も朱色に染まっていたのは、やっぱり夕日のせいなのだろうか。"

with dis
$ hi_mes()

scene bg06_sk_h_eve with Dissolve(.8)

scene bg_par15_rg_amu_eve
with stripe_l_long

play music entrance_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人で夕日を見て、それから今度は空中浮遊で玄関へと戻った。"


show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

hide yuri_m_02_9
show yuri_m_02_9 at left
with dis

show bor_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0293
Boris "「……うっ。\n
い、委員長さん、眉間に皺寄っているよ？」"

hide yuri_m_02_9
show yuri_m_03_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0098
Julius "「はは、どうしてだろうな？\n
誰のせいだと思う？」"

hide bor_m_03_11
show bor_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0294
Boris "「え、え～と……。\n
やっぱ、眉間に皺寄せてたほうがいいや」"

hide bor_m_01_3
show bor_m_03_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0295
Boris "{size=+20}「笑ってると、尚怖い」{/size} "

hide yuri_m_03_5
show yuri_m_02_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0099
Julius "「ふ、そうか……。\n
では、リクエストにお応えしよう」"

hide yuri_m_02_12
show yuri_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0100
Julius "「……{size=+20}来い！！\n
[firstname]、おまえもだ！！{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……はーい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前でユリウスの制止を振り切って、危険（だと言われている）なマジックアイテムを動かしてしまったのだから、お小言を食らうのは仕方がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "覚悟を決めて、ボリスの隣に並んだ。"

hide yuri_m_03_7

hide bor_m_03_1
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_amu_eve with Dissolve(.8)

scene bg_map_eve
with stripe_l_medium

scene bg_par15_rg_tow_eve
with stripe_l_medium

scene bg06_sk_h_eve
with stripe_l_long

play music drawingroom_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやらユリウスは、動きだしてしまったタイルに下手に干渉しては余計に危ない、ということを見抜き、しばらくその場で待機していてくれたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その間に万が一怪我人が出たら、ということで塔にも連絡をしてあったようで、連行された先の塔では学校医のナイトメアまでが待機状態に入っていた。"


scene bg_par16_rs_tow_eve
with dis

show nai_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0018
Nightmare "「やあ、君もずいぶんと遊園地寮に染まったようだな。\n
はは、連絡を受けてこうして待機していたが……、元気そうじゃないか」"

hide nai_m_01_6
show nai_m_01_6 at left
with dis

show gre_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0000
Gray "「笑いごとじゃありませんよ、ナイトメア先生。\n
……ふう、まさか君までが、こういうことに手を出すとは思わなかった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "傍らでグレイも呆れ顔だ。\n
ボリスが連行されてくるのは日常茶飯事だが、そこに共犯として私が名を連ねるのは予想外だったらしい。"

hide nai_m_01_6

hide gre_m_02_7
show gre_m_02_7 at left
with dis

show yuri_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0101
Julius "「まったくだ。今回は怪我がなかったからよかったものの……、他に休止しているマジックアイテムが同じように無事に作動するとは限らない」"

hide yuri_m_03_4
show yuri_m_02_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0102
Julius "「禁止するには禁止するだけの理由がちゃんとあるんだ。\n
分かっているのか、おまえ達は」"

hide gre_m_02_7

hide yuri_m_02_9
show yuri_m_02_9 at left
with dis
##[rchara1 PAY ATTENTION="false"]
show bor_m_01_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0296
Boris "「ちゃんと安全面は確認しているよ。\n
何か問題があっていざってときも、俺がなんとか出来る範囲のものしか使わないし……」"

hide bor_m_01_9
show bor_m_02_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0297
Boris "「この子を怪我させたりしないから安心してよ。\n
トラブルがないとはいえないけど……、俺が守れる範囲の無茶しかしないからさ」"

hide yuri_m_02_9
show yuri_m_02_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0103
Julius "{size=+20}「そんな弁解で、誰が安心できるか！」{/size} "

hide yuri_m_02_7
show yuri_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0104
Julius "「いいか、おまえ達、いくら魔法学校とはいえ何でも魔法で解決できるものではないんだぞ？」"

hide yuri_m_03_7
show yuri_m_03_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0104_5
Julius "「危険に飛び込もう、スリルを求めようなどという若者にありがちな暴走は……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスが腰に手をあて、仁王立ちで小言を並べたて始める。\n
私達を「若者」というあたり、彼は年長者の風格がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "面倒をかけてしまったから、怒られるのも当然で……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……心配をかけて、申し訳ないな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、思う一方で、心配してもらえたことが嬉しかったりもする。\n
これが、悪童の気持ちなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまで、比較的優等生だった私にとっては新しい感覚だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらり、と視線を流した先、ガミガミと私以上に怒られながらもボリスはこっそりと私にウィンクを飛ばしてくれた。"

play sound se_0783
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意味はすなわち。\n
……「またやろう」、だ。"

hide yuri_m_03_13

hide bor_m_02_1
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par16_rs_tow_eve
with stripe_l_medium

scene bg_par15_rg_tow_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_long
##endmemory
jump gakuen_boris3
