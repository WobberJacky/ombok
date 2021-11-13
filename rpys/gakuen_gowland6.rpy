label gakuen_gowland6:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_amu_day
with dis

play music gowland_t_ali

scene bg_par09_os_day with Dissolve(1.2)

show go_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice gor_g0173
Gowland "「なあ、[firstname]。\n
ちょっと聞いてくれ、新しいメロディラインが頭の中に浮かんだんだ！」"

hide go_m_01_5
show go_m_03_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice gor_g0174
Gowland "「これはきっと女神の祝福に違いねえ。\n
聴いてくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「嫌。\n
あなたの祝福は私の絶望よっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもの音楽室。\n
いつもの放課後だ。"

hide go_m_03_14
show go_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0175
Gowland "「そんなつれねえこと言うなって！\n
な？絶対に最高だから！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「分かった！\n
私が一曲弾いてあげるから！」"

hide go_m_02_8
show go_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice gor_g0176
Gowland "「え？\n
いや、あんたに弾いてほしいわけじゃなくて、俺が……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「いいから！\n
音楽に飢えているんでしょう！？」"

play sound se_0787
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドが反論するより先に、私は鍵盤の上へと指を滑らせる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすが音楽の寵児を自称するだけはあって、ゴーランドは人の演奏を邪魔するようなことはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのことから私が学んだ彼への一番効果的な対処法は、彼が演奏するより先にこっちが弾く、ということだった。"


play music alice_piano
hide go_m_03_3
show go_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gowland "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは目を閉じて、私の奏でるメロディに聞き惚れている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……そこまで上手くはないはずなんだけれどな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "感動するほど上手いとは、とてもじゃないが言い切れない腕前だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアノを習っていたのはもうだいぶ昔のことだし、楽譜が読めるので何とか新しい曲に挑戦することも出来るが、初見ですらすらと弾くというようなことは無理。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私よりピアノの弾ける子なんて、大勢いるだろう。それなのに、ゴーランドは、いつも素晴らしい音楽を聴いているような顔で私のピアノに耳を傾ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（この人、本当に音楽が好きなんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだけは認められる。\n
彼は間違いなく、音楽を愛している。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（若干、空回り気味だけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「…………」"


show bg06_sk_h_day onlayer master
with dis
hide go_m_01_12

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（空回り……、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの音楽室で過ごす時間というのは二人っきりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮の住人は皆、ゴーランドの破壊音波を恐れているため、音楽室に近づこうとすらしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから甘い時間を過ごすにはちょうどいいはず……、なのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは、あの日以来ちっとも私に触れなくなった。\n
癖のようだった頭を撫でることすら、しないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（そりゃあ、人目が気になるのは分かる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは教師で、私の担任だ。\n
そして、私は彼の生徒だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくらシンフォニアが生徒の自主性を重んじる学校だとはいっても、やはり教師が教え子に手を出したとあっては問題になるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは私だって承知している。\n
けれど、まるであの夜のことを忘れたように振る舞われると不安にもなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（好きにも色々あるし、私はまた、空回っているだけなのかもしれない）"


play music view_day_p_wam
play sound se_0787
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……あ」"

hide bg06_sk_h_day


show go_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gor_g0177
Gowland "「お、珍しいな。\n
あんたがミスするなんて」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……ちょっと、ね。\n
考え事をしながら弾いていたら間違えちゃった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこで曲を止めて、鍵盤から指を下ろす。"

hide go_m_03_10
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0178
Gowland "「それじゃあ、次は俺の番だな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ねえ、ゴーランド」"

hide go_m_02_12
show go_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice gor_g0179
Gowland "「ん？なんだ？\n
俺の天才的な演奏が聴きたくなったって？」"

hide go_m_03_5
show go_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice gor_g0180
Gowland "「よっしゃ、まかせろ！\n
あんたのために一曲弾くぜ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやって弓を構える姿が、まるで誤魔化そうとしているように見えるのはどうしてなのだろう。"

menu:
    "（……むなしいなあ）":
        jump gakuen_gowland6_2a
    "（……難しい）":
        jump gakuen_gowland6_2b
label gakuen_gowland6_2a:
$ lovechara_gowland_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……むなしいなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの夜にはあんなにも気持ちが通じ合ったような気がしたのに、今はたった一言聞くことすら怖いと感じてしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（私は、好きなのに）"

jump gakuen_gowland6_3
label gakuen_gowland6_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……難しい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たった一言の質問を、切り出すのがとても難しい。"

jump gakuen_gowland6_3
label gakuen_gowland6_3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このもやもやした気持ちも、ブリーズの夜には晴らすことができるのだろうか。"

play sound se_0222
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！」"

play sound se_0496
pause .4
play sound se_0403 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、口の中で小さく、消音魔法を呟く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドと付き合う上では必須ともいえるこの魔法を、今では空で呟くことができるし、媒体が必要なくなるほどに上達もした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（ブリーズ、成功させるには情報が必要よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手がゴーランドである以上、誰にでも相談できるわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……ボリス）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頼りになるクラスメイト兼寮長の姿を脳裏に思い浮かべて、私は完全なる静寂の世界へと逃げ込んだ。"

hide go_m_01_1
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par09_os_day with Dissolve(.8)

scene bg_par15_rg_amu_day
with stripe_l_medium

scene bg_map_day with stripe_l_medlong

scene bg_map_eve with Dissolve(1)
jump gakuen_common_breeze
label gakuen_gowland6_4:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ゴーランドの部屋は三階だから、まずは階段を探さなくちゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とんとんと額を指先で叩いて、記憶を辿る。\n
これで、お目当ての人に会えるはずだ。"

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "辿り着いた一室、部屋番号をしっかりと確かめた。\n
これで部屋を間違えていたりなどしたら、笑えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もともと職員は塔に部屋を持っていたはずなのだが、ゴーランドは賑やかさと自由を求めて遊園地寮へと越してきたのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（たぶん……、騒音問題よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアやグレイ、そしてユリウスが耐えられなかったのだろう。\n
そうでなければ、規則にうるさいユリウスが、こんな例外を認めるはずもない。"

play sound se_0217
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ノックをしてしばらく待つと、ゆっくりと扉が内側から開いた。"

play sound se_0397
##[rchara1 PAY ATTENTION="false"]
show go_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gowland "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは、私を見て少し驚いたようだった。\n
それから無言で後ろに半身を引き、私を中へと招き入れてくれた。"

play sound se_0664
hide go_m_02_4


scene bg_par24_rht_nig
with dis

play music residence_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……寮監だから、かしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮に住む教員、ということで特別な扱いを受けているのか、ゴーランドの部屋は私の部屋よりも広いようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "派手な色合いの家具や、様々なオブジェが置かれた部屋はなんとも彼らしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ゴーランド？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼ぶ。\n
ゴーランドの様子は、あからさまにおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が期待しすぎているのだろうか。\n
こういう反応に戸惑っている。"


show go_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0181
Gowland "「ああ、どうかしたか？」"
if lovechara_gowland_points == 8:
    jump gakuen_gowland6_5
jump gakuen_gowland6_6a
label gakuen_gowland6_5:
menu:
    "……なんでもない。":
        jump gakuen_gowland6_6a
    "喜んでくれないの？":
        jump gakuen_gowland6_6b
label gakuen_gowland6_6a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの夜に、私が彼を訪ねたことを喜んでほしいなんていうのは思い上がりだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（自惚れて……、それでもいいんだと思ったのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……なんでもないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、勇気を出すことができなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もし、そこでゴーランドを問い詰めることが出来ていたならば、その後の展開ももっと別なものになっていたのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど……、私は肝心の場面で聞けなかったのだ。\n
声が出なくなり、動けなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（あのときと、一緒だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "渡せなかったラブレターの苦味を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "苦笑いのような、変な顔になってしまう。\n
泣けないなら、笑うしかない。"

hide go_m_02_10
show go_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0182
Gowland "「……そうか。\n
なあ、あんた……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……何？」"

hide go_m_03_7
show go_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice gor_g0183
Gowland "「いや、俺のほうこそなんでもねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドも、何かを言いかけて途中でやめた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お互いに、聞きたいことがあるのに、それを口に出してしまうことを躊躇うような沈黙が続く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかくのブリーズだというのに、空気はひたすら重苦しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、何も言い出せないままに、ブリーズ終了の合図を聞くことになってしまった。"

play sound se_0626
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「！」"

hide go_m_02_2
show go_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
Gowland "「…………」"

hide go_m_03_1
show go_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gor_g0184
Gowland "「……早い、な」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早い。\n
だが、長く感じた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……帰るわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言って、窓辺へと向かう。\n
中庭へと飛び降りて、そのまま部屋へと帰ろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "胸の中がぐらぐらと熱くて、油断するとそれが涙になって溢れそうになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（みっともないわ）"

play sound se_0585
pause .3
play sound se_0693
hide go_m_01_7


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓を開けた。\n
涼しい夜風がさあっと吹き込んでくる。"

play sound se_0216
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後、窓枠を蹴って飛び降りる間際。\n
ゴーランドの苦い声を聞いたような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0185
Gowland "「学生同士のが、お似合いだよ。\n
……俺は、あんたには年寄りすぎる」"

pause .5
play sound se_0348
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、幻聴だったのかもしれない。"

with dis
$ hi_mes()

scene bg06_sk_h_nig with Dissolve(.8)

scene bg06_sk_h_day
with dis

scene bg06_sk_h_eve
with dis

scene bg06_sk_h_nig
with dis

scene bg06_sk_h_day
with dis

play music stream_eve_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの夜からしばらくして、ゴーランドは塔へと帰っていった。"


scene bg_par15_rg_amu_day_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0186
Gowland "「やっぱり教師がよ、学生寮に住むもんじゃねえよな！\n
ケジメつけねえとまずいって、うん」"


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言って笑っていたものの、見送る私も、ボリスも、苦い顔をするしかなかった。ゴーランドの言うケジメというのは、私に対するものもあるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は教師で、私は生徒だ。\n
付き合おうとしたときに、私とゴーランドとでは対等にはなりえない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの夜、彼と同じ位置にいたと思ったのに。\n
これから、だったのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（付き合いかけた……と思っていたのは、私だけなのかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "付き合ったというほど、関係が変わる時期はなかった。\n
だが、これから始まるはずだったのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……私がもっと大人だったら。\n
生徒じゃなかったら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなのは、仮定の世界だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が大人で、彼と対等な立場にある人間だったとしても、もしかしたらまた別の理由でやっぱり私は彼に去られてしまうのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（…………）"


scene bg25_rr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮の、男女共同区域にある音楽室へと向かう。\n
いや、今では元音楽室だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのほとんどの楽器を、ゴーランドは塔へと持ち帰っていった。\n
この部屋に残されているのは、ピアノだけだ。"

show m_go_badend3_s onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0187
Gowland "「あんた、ピアノ好きだろ？\n
俺がいなくなっても、ピアノは続けておけよ」"

hide m_go_badend3_s
show m_go_badend3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "リボンを返す時にゴーランドはそう言った。\n
そうして、ピアノだけが残されたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……持っていってくれればよかったのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "渡せなかったラブレターと同じ。\n
手元に残っても仕方のないものだ。"

hide m_go_badend3
show m_go_badend4 onlayer master
with dis

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "椅子に座り、鍵盤へと指を乗せる。"


play music alice_piano
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつも心地よさそうに私のピアノを聴いてくれていたゴーランドを思い出して弾き始める。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_5")
T "（窓は、開けたままにしておこう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この音が、風にのって届くかもしれない。\n
恨みがましい音色かもしれないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_3")
T "「……同じ学校にいるんだもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ、終わったわけではない。\n
彼のように破壊的に、私はでたらめな音を奏でる。"

hide m_go_badend4 with Dissolve(5)
hide ali_m_06_16
hide frame_par_togaki
with Dissolve(5)
stop music
##endmemory
jump gakuen_c

label gakuen_gowland6_6b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は両手を腰にあてると、わざとらしいぐらいに拗ねた調子でゴーランドを睨み付けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「何よ。\n
私がブリーズにやってきたっていうのに、喜んでくれないの？」"


show go_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gor_g0188
Gowland "「……意味、分かって言ってんのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……分かるわけがないでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "半眼で睨み付けてやる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "第一、ストームの夜に続きはブリーズで、といったのはゴーランド本人だ。\n
その本人がいまさら腰が引けているなんて、ずるい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「意味が分からないわ。\n
全然、分からない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズのことではない。\n
ゴーランドのことが分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脳裏をよぎっていったのは、白いシンプルな封筒。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "渡せなかったラブレター、伝えられなかった想い、それらはずっと私の胸に沈殿し続けてきていた。\n
今は、分からなくても向かっていける。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……この人は、安心感をくれる人だから）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "過去の想い人、ボリスやエースや、他の誰とも違う。\n
怖くない人。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「ゴーランド。\n
私は、あなたが好きよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「あなたが、私から逃げるならそれでも構わない。\n
けれど、言いたいことは言うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "付き合ったというほど、関係が変わる時期はなかった。\n
だが、何もなかったわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何もなかったことにはしたくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（もう、後悔はしたくないのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "渡せなかったラブレターなんて、反吐が出る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真っ直ぐに、ゴーランドを見据えた。\n
ゴーランドは、目を瞠ったまま私の言葉を聞いている。"

hide go_m_03_2
show go_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0189
Gowland "「……はは」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それから視線を伏せて、小さく自嘲するように笑った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「？」"

hide go_m_01_8
show go_m_03_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice gor_g0190
Gowland "「いや……、情けねえな。\n
あんたにそこまで言わせちまうなんて、それこそ本物のジジイじゃねえか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……？？？」"

play sound se_0584
hide go_m_03_14

pause .15
play sound se_0210
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つかつかとゴーランドが私へと距離を削り、ひょいっと抱き上げた。\n
そのままソファまで運ばれて、彼の膝の上へと下ろされた。"


play music starlit_sky_a_wam
show m_go6_1 onlayer master
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「ええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "宥めるような口付けが一度額へと触れて、それから彼はぎゅうっと私を力強く抱きしめた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0191
Gowland "「……悪かったな。\n
俺が言わなきゃならねえようなこと、あんたに全部言わせちまった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳元で囁かれる声音は、まるで懺悔するように響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0192
Gowland "「あんたが、ボリスと仲いいのを見て妬いてたんだ。……俺みたいなおっさんなんかよりも、あんたにとってはあいつのほうがいいんじゃねえかとも思った」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……なんで、ボリス？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「私と、ボリス？\n
仲が悪いとは言わないけれど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どちらかというと悪友といった感じだ。\n
特に今回のブリーズについては、ずいぶんと助けてもらった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他に相談できる人がいない分、特にそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "でも、そうやって私がボリスとつるんでいるのを見て、ゴーランドはやきもきしていたのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……誤解だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とボリスは、作戦会議をしていただけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0193
Gowland "「あんた、猫好きだって言ってただろ？\n
あいつにゃ、猫耳と尻尾がついている」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……私、猫は好きだけど。\n
別に、あなたに猫耳がついていなくても気にしないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gor_g0194
Gowland "「……それは、{size=+20}ついてるほうが気にするだろ{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（まあ……、想像するとちょっと怖いかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "動物を愛好する気持ちと、恋愛感情はけして同じものではないし、混同できるものではないと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして言いながらも、以前の授業風景を思い出していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれはストームの次の日だったはずだ。\n
私はボリスに追及されていて、じゃれあっていて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思い返せば、あのときから、ゴーランドの様子はおかしかったような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（ヤキモチで身を引いちゃうなんて、弱気な……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とはいえ、そんな単純なものでもないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は教師で、年齢差もある。\n
私の気持ちを、一時の気の迷いかもしれないからと距離を置く心情も理解できた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……{size=+20}理解は出来ても、納得は出来ないけど{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の立場上難しいだろうが、もっと強気になってもらいたいものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「とにかく、誤解よ。\n
私が好きなのは、メリー＝ゴーランド、あなただから」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_g0195
Gowland "「……すげえ嬉しい告白のはずなのに、嬉しくねえのはどうしてだ。\n
くそう、なんだかあんたのほうが余裕だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "フルネームを呼ばれたことで顰められる顔に、唇が緩む。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（私だって、余裕があるわけじゃないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "余裕があるのではなく、覚悟があるのだ。\n
体当たりで、玉砕しても……、いや、そうならないように頑張ろうという覚悟。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……それで、どうなのよ。\n
私は、言ったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次は、ゴーランドの番だ。\n
彼はまだ言葉にしてくれていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして抱く腕からも、体温と一緒に伝わる気持ちはある。\n
けれど、やはり言葉でほしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が言葉にした分を、彼にも言葉で返してほしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0196
Gowland "「……俺も、あんたが好きだ。\n
年が離れていようが、あんたが俺の生徒だろうが、関係ねえ」"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐ、っと抱く腕に力がこもる。\n
痛いぐらいの抱擁が、嬉しい。"

hide m_go6_1
show m_go6_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0197
Gowland "「ボリスのやつにも、他の誰だろうが。\n
あんたのことはやらねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0198
Gowland "「本当は、そういうふうに言いたかったんだ。\n
今度からは、遠慮なく、そう言うようにする」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな宣言とともに、唇を塞がれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Gowland "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_3")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "宣言どおりに独り占めをするかのようなキスだ。\n
呼吸すら奪われて、頭の中がくらくらとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段のゴーランドならば、手加減してくれそうなところにそれが見えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……本気ってことなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼんやりと、教師だとか年上だとか関係なく、今私にキスをしているのはメリー＝ゴーランドという一人の男性なのだと感じた。"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろりと持ち上げた腕を彼の首裏に絡めて、深いキスに呑まれて溺れる。\n
やがて唇が離れたときには、くたりと彼の懐にもたれかかってしまった。"

hide m_go6_2


show go_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0199
Gowland "「……いい、んだよな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最終確認というように聞かれる。\n
ここまできて、駄目だと言うわけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（私は……、あなたがいいな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "年の差があっても。\n
生徒と教師でも。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さく顎を引いて頷けば、くるりと世界が反転して組み敷かれた。"

play sound se_0328 volume .8
play sound se_0327 volume .6
camera at hpunch
camera at vpunch

show m_go6_3 onlayer master
with dis
hide go_m_02_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0200
Gowland "「……好きだぜ、[firstname]。\n
責任でも、なんでも、とってやる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「……うん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういうふうに言いたかった、と、彼は言う。\n
私も、そういうふうに言われたかった。"

with dis
$ hi_mes()
hide m_go6_3


scene bg_par24_rht_nig with Dissolve(.8)

scene bg_par15_rg_amu_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_gowland_end
