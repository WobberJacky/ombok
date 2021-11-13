label gakuen_dormitory_common_castle1:
$ place_of_stay = "Castle"

scene bg_par29_js
with dis

play music entrance_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……赤薔薇寮、かな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷った結果、赤薔薇寮を選択した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の寮も充分に魅力的で、なかなか決めることができなかったのだが……。\n
自治会という存在が興味深くて、そこに決めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒会とは違う、独自のものらしい。\n
せっかくシンフォニアに入学したからには、シンフォニアらしいことをしてみたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（独自のルールに慣れるのは大変かもしれないけど……、赤薔薇寮がいいわ）"

jump gakuen_dormitory_common2
label gakuen_dormitory_common_hatter1:
$ place_of_stay = "Hatter"

scene bg_par29_js
with dis

play music entrance_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……帽子屋寮、かな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷った結果、帽子屋寮を選択した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の寮も魅力的で、なかなか決めることができなかったのだが……。\n
どこよりも自由な寮、というところに心惹かれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまで通っていた学校のように、校則に雁字搦めになるのではなく、帽子屋寮では独自のルールがあるのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはある意味、もっとも自立している寮と言うことができるのではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（独自のルールに慣れるのは大変かもしれないけど……、帽子屋寮がいいわ）"

jump gakuen_dormitory_common2
label gakuen_dormitory_common_amuse1:
$ place_of_stay = "Amuse"

scene bg_par29_js
with dis

play music entrance_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……遊園地寮、かな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷った結果、遊園地寮を選択した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の寮も魅力的で、なかなか決めることができなかったのだが……。\n
やはりクラスメイトや、担任のいる寮、というのは何かと心強い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それにとても楽しそうだ。\n
クラスで会った面々を思い出せば、自然と口元に笑みが浮かんだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（羽目をはずさないように注意が必要だけど……、遊園地寮がいいわ）"

jump gakuen_dormitory_common2
label gakuen_dormitory_common_tower1:
$ place_of_stay = "Tower"

scene bg_par29_js
with dis

play music entrance_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……塔、かな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷った結果、塔を選択した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "決め手となったのは、その堅実さだ。\n
取り仕切る上級生達の硬い立場は少し気になるが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアなんていう素晴らしい学校に入ることが出来たのだから、やはり真面目に勉強するべきだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（多少堅苦しくても……、塔がいいわ）"

jump gakuen_dormitory_common2
label gakuen_dormitory_common2:

show jimu1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice hei_g0088
Jimu_w "「分かりました。\n
それでは、さっそく手続きに入らせていただきますね」"

hide jimu1_8
show jimu1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice hei_g0089
Jimu_w "「今から行っていただきたいのは、学生証の発行と、自治会員の登録です。\n
この紙に簡略化した手順が載っていますので、どうぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（ふむふむ。\n
手続きが多いのね……）"

hide jimu1_2
show jimu1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice hei_g0090
Jimu_w "「ええと……」"

hide jimu1_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごそごそと、事務の女性が屈んで足元を探る。そうしてから差し出されたのは、なにやらでろん、とした半透明の矢印だった。"


show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐったりしている。\n
でろん、と……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（魔法生物か何か……？\n
それともアイテム？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（で、でも、なんだか……。\n
死んでいない……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生き物のようだが、ぐったりしていて……。\n
まるで、陸に打ち上げられたウミウシのようだ。"


show jimu1_3 at center
with dis
hide guide_1

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Jimu_w "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "事務の女性は、にこやかに笑いを口元に浮べたまま。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その矢印のしっぽ部分（？）を掴むと、機械の接触不良を直そうと試みるのと同じ要領で、ぶんぶんと勢いよく振った。"

play sound se_0441
pause .5
play sound se_0441
pause .25
play sound se_0441

show guide_5 at center
with dis
hide jimu1_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0023
Guide "「ふおあああああっ！\n
吐く、吐くからやめてっ、振るのやめてっっ！！！」"

hide guide_5
show guide_5 at left
with dis

show jimu1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0091
Jimu_w "「ああ、よかった、まだ使えますね。\n
……はい、どうぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悲鳴をあげた矢印を、彼女は私へと差し出す。"

hide guide_5
show guide_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0024
Guide "「う、ううう～～～……っっ。\n
吐きそう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "矢印は、断末魔っぽく呻きながらねじれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（う、受け取りたくない……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "死にかけのウミウシなど、あまり触りたいものではない。"

hide jimu1_2
show jimu1_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0092
Jimu_w "「さあ、どうぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう一度促されて、私は渋々その半透明のねじれた矢印を受け取る。"

hide guide_6

hide jimu1_6
show jimu1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（ぬめっとしていたら、嫌だな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "受け取った矢印はふわりと軽く、手のひらにはほとんど重さは感じられなかった。\n
ぷにぷにとした感触だけが、指先に伝わる。"

hide jimu1_2
show jimu1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0093
Jimu_w "「そのガイドがあなたを案内してくれますので、指示に従って手続きを行ってください」"

hide jimu1_3
show jimu1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0093_5
Jimu_w "「少々見えにくい色をしていますので、分かりやすく紐で繋いでおきますね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女は慣れた所作で、ペット用のリードのような紐をねじくれた矢印の頭にひっかけて、きゅっと締める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抵抗するように、矢印の尻尾がびくんっと小さく揺れた。"

play sound se_0245

show guide_2 at center
with dis
hide jimu1_2

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……うわあ。\n
ウミウシそのもの）"

hide guide_2
show guide_2 at left
with dis

show jimu1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice hei_g0094
Jimu_w "「では、こちらをお持ちください。\n
後はこのガイドが説明してくれますので、手続きのほうへどうぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は紐の持ち手を渡される。\n
ここでの手続きはこれで終了らしい。"

hide guide_2

hide jimu1_3
show jimu1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0095
Jimu_w "「次の方、お決まりでしたらどうぞ」"

hide jimu1_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな彼女の声に背中を押されて、私は事務室を後にした。"

with dis
$ hi_mes()

scene bg10_sb_day
with stripe_l_medium

play music garden_day_p_wam

scene bg_map_day
with stripe_l_long
play sound se_0559

show m_ryou1_guide1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「こういう仕組みになっていたのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "事務室の外には、私のような新入生が大勢うろうろとしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それぞれ、風船のように紐で繋がれた色とりどりの矢印に導かれ、ガイダンスを受けている。\n
魔法学校ならではの光景といえよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0137
Seito "「次はどこに行くの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0072
Guide "「次は、遊園地寮だよ。\n
賑やかだから楽しもうね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0096
Seito "「帽子屋寮、まだ登録始まらないみたいだな～」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0074
Guide "「そうですね、先に赤薔薇寮に行くことを、お勧めしますよ。\n
効率的にまわってきましょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0112
Seito "「赤薔薇寮のお庭、綺麗だったわね～。\n
次の遊園地寮はどんなところかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0042
Guide "「遊園地寮では、変なタイルは踏まないように気をつけてくださいね！\n
流されてしまうと、なかなか戻れませんから！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0105
Seito "「塔って、ここのすぐ後ろにあるあの建物のことだよな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0061
Guide "「ええ、そうです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0106
Seito "「どんなところ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0062
Guide "「雰囲気を知るには、行ってみるのが一番！\n
近いんですから、入ってみましょう！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手にした色とりどりの矢印は、風船のよう。\n
寮の名前ではないが、遊園地にいるみたいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わくわくとした、浮かれた雰囲気。\n
賑やかなざわめきが耳を打つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……だと、いうのに。"


play music gag1_a_wam
hide m_ryou1_guide1
show m_ryou1_guide2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の矢印ときたら、他の矢印と違って無色な上に、ひたすらに低空飛行だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Guide "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぬめぬめ。\n
じりじり。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな効果音が聞こえてきそうだ。\n
彼はのたのた、億劫そう……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……はあ。\n
ねえ、もうちょっと元気に案内しようって気はないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、矢印に繋がった紐をくい、と軽く引いた。\n
のろり、と矢印がわずかに頭を持ち上げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外に出ても、相変わらず。\n
死にかけのウミウシのままだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「他の矢印を見てみなさいよ。\n
皆、いきいきと頑張っているじゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice sat_g0025
Guide "「新入生のガイダンスなんて俺の仕事じゃないんだよ……っ！\n
ガイドが足りないからって、俺まで駆り出すなんて横暴だ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうも私の案内役は、自分の仕事に納得がいっていないらしい。\n
空中で器用にとぐろを巻いて、ふてくされている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（確かに……。\n
色からして、他の矢印とは違うわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の矢印たちよりも、はるかに見えにくい。\n
そして、本来の仕事と違うためなのか、やる気もなさそう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一体何のための矢印なのだろうか。"


play music garden_day_p_wam

scene bg20_gd_day
with dis
hide m_ryou1_guide2

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「あなた、新入生用のガイドとは違うの？」"

play sound se_0244

show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "足元でとぐろを巻いていた矢印が、いきなり目の前まで急上昇してくる。"

hide guide_5
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0026
Guide "「違うとも！\n
俺は本来、迷子を安心できるところまで導く、迷子用ガイドなんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「迷子用……？」"

hide guide_3
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice sat_g0027
Guide "「そう！\n
学園は広いから、迷子救済用のガイドなんだよ！」"

hide guide_5
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice sat_g0028
Guide "「新入生のガイダンス用なんて、シーズンものと同じににされたら困る！\n
俺のほうがベーシックで、日常的に必要とされるガイドなんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「どちらにしたって、ガイドはガイドじゃないの」"

hide guide_1
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice sat_g0029
Guide "「俺のほうが、より優秀なガイドなの！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……でも、ガイドでしょう。\n
より優秀なガイドが、そんな保護色で大丈夫なのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が校内で迷子になったとしても、果たしてこのガイドに助けを求めることができるだろうか。まずこのガイドを見つけるところから、躓いてしまいそうだ。"

hide guide_3
show guide_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0030
Guide "「いいんだよ。\n
とろくさくなきゃ、見つけられるさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「いや、よくないでしょ……。\n
大体、最初からそんな注意力があったら、迷子にだってならないだろうし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……ん？\n
ああ、でも）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「普段は、決まったところにいるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "定位置にいてくれるのならば、まだ何とか頼ることも出来るかもしれない。"

hide guide_6
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0031
Guide "「まさか！\n
常日頃から、迷子を捜し求めて学園内を彷徨っているよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（そ、それ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "駄目すぎる。\n
ひとところに留まらないなど、むしろ、ガイド自体が迷子の定番を踏んでいるではないか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくら有能な迷子案内ガイドだとしても、見つけられなかったら意味がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（まあ、でも、同じ場所に留まっていても、そこまで行き着けるのなら迷子にはならないでしょうし……。\n
ある意味、正しいのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ああ、それじゃあ……。\n
迷子を感知するスキルを持っているの？」"

hide guide_3
show guide_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice sat_g0032
Guide "「へ？そんなスキルはないよ？\n
だから俺は毎日巡回して、迷子を捜しているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「そ、そう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア高位魔法学校は広大な敷地を誇る世界一の魔法学校だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこで迷子になったとして、好き勝手に巡回と称して動きまわる半透明の矢印と出会える確率が、一体どれほどあるというのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「それじゃあ……、迷子にはあまり会えないでしょうね……」"

hide guide_4
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice sat_g0033
Guide "「まあね。大体、そんなしょっちゅう迷う奴なんていないよ。\n
新入生や編入生くらいのものさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「……じゃあ、新入生ガイダンス用の矢印で充分じゃない？」"

hide guide_1
show guide_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_6")
voice sat_g0034
Guide "「う……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が呆れているのが分かったのか、半透明矢印は少し焦ったようにくるくると回りながら力説する。"

play sound se_0244
hide guide_6
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0035
Guide "「ま、迷子を見つけるスキルはないけど、俺にはすごい能力があるんだ！\n
迷子を、その迷子が安心できる場所まで連れて行ってあげられるんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「安心できる場所？」"

hide guide_5
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sat_g0036
Guide "「ああ、そうだよ！安心できる場所だ！\n
迷子は心細いだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……迷っていれば、当然でしょうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幾つになっても、見知らぬ場所で迷子になるというのは心細い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、急ぎの用事で移動している途中での迷子だったりしたのなら、なおさら案内はありがたい……、が。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ちょっと待って」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「安心できる場所？？？\n
つまり、別に目的地に案内するわけじゃないってこと？」"

hide guide_3
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice sat_g0037
Guide "「そう、違うよ。\n
俺が案内するのは、安心できる場所」"

hide guide_5
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice sat_g0038
Guide "「迷子が行きたい場所じゃなくて、迷子になって不安な気持ちが吹っ飛ぶような安心できる場所へ連れて行くんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目的地には案内してくれないガイド。\n
安心できる場所に案内してくれるのも、充分ありがたい話ではあるのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（ちょっと方向性が違うんじゃない？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「……それって、ガイドっていえるの？」"

hide guide_1
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice sat_g0039
Guide "「立派なガイドだよ！\n
新入生ガイダンス用なんかよりよっぽどね！」"

hide guide_3
show guide_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice sat_g0040
Guide "「より複雑な魔法の力が働いている。\n
それなのに……！」"

hide guide_6
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice sat_g0041
Guide "「そのスキルが、今は調整されていて使えないんだ！\n
君のことだって、安心できる場所に連れて行ってあげたいのに！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（よかった……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくら安心できるからといって、家まで戻されたりしたら堪らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「有難いお申し出だけど……。\n
私は新入生用のガイダンスを受けたいわ、心から」"

hide guide_5
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice sat_g0042
Guide "「新入生用のガイダンスなんか、芸がないよ！\n
創意工夫がないと駄目だって、どこぞのプリンセスも言っていた！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（いやいや、そんなの知らないわよ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世界違い……。\n
いや、ゲーム違いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「今、私は迷子じゃないし、迷子用のガイドはいらないの」"

hide guide_1
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice sat_g0043
Guide "「いらない！？\n
いらないだって！？いらないの、俺！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……少なくとも、今はね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "安心できる場所になど、行っている暇はない。\n
ただ、新入生につきものの、様々な手続きをするためのガイドがほしいだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いっそのこと、その辺の新入生にガイドのトレードを申し出たくなってくる。"

hide guide_3
show guide_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0044
Guide "「……しゅん」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（う……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無色矢印は、しょんぼりと項垂れる。\n
なんだか、哀れな有様だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……ああ、ますます、寿命が近付いていそう。\n
このままじゃ、まともなガイダンスが受けられそうにないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほど事務の女性がやったように、しっぽを掴んで振り回してやったら、やる気になるだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "死にかけのウミウシモドキ。\n
完全な死体になってしまっては、ガイドもいなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……と、まあ、冷静な判断を除いても、なんだか可哀想）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、ガイドがいなくなって困るのは私だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「今、迷子用ガイドはいらないけど……。\n
あなた、一流のガイドなんでしょう？」"

play sound se_0058
hide guide_4
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice sat_g0045
Guide "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「迷子を、その迷子が安心できる場所に案内するなんて、普通のガイドじゃ出来ない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「その一流のガイドに、新入生ガイダンスを受けられるなんて光栄だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「きっと、新入生へのガイドだって、普通のガイドよりうまく出来るわよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とりあえず、おだててみる作戦に出る。\n
調子のよさそうなガイドだから、これにのってくれればいいのだが……。"

play sound se_0247
hide guide_3
show guide_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0046
Guide "「一流……。\n
一流……！」"

play sound se_0058
hide guide_2
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0047
Guide "「そうさ！\n
俺は一流のガイドなんだよ……！」"

hide guide_3
show guide_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "再び目の前まで浮かび上がった無色矢印が、もじもじくねくねとし始めた。"

hide guide_6
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "{size=+20}（なんて、分かりやすい）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気質が分かれば、非常に扱いやすい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こういう奴は、その気になるまでおだてるに限る。私だって、散歩嫌いのペットじゃあるまいし、ぐったりとした無色矢印を引きずって歩くのは嫌だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ、もちろん、そうでしょうね。\n
あなたは一流のガイド……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「だから、私のことを案内してくれるわよね？\n
新入生用のガイダンスとして……」"

hide guide_5
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice sat_g0048
Guide "「もちろん！\n
だって、俺は一流だし！一流だからね！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「そうそう、一流、一流……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……だから、案内してね。\n
普通でいいから、新入生向けに」"

play sound se_0078
##special anime"kirakira_center"loop="false"]
hide guide_1
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice sat_g0049
Guide "「任せとけ！\n
俺はなんだって出来る、万能ガイドだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しゃきーん、と今までのへろへろぐったりぶりが嘘のように、無色矢印が元気になった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴしっとした姿は半透明ながら、立派な矢印だ。\n
もう、ウミウシには見えない。"

play sound se_0058
hide guide_3
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "矢印は、今までのやる気のないぐったりぶりが嘘のように、空中でうねうねくねくねと忙しく身をくねらせている。\n
目まぐるしすぎて、若干目が回る。"

play sound se_0058
hide guide_5
show guide_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "事務の女性が紐で繋いだ理由が分かったような気がした。\n
この半透明の矢印を、ずっと目だけで追い続けるのは一苦労だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（うう、ちかちかする……。\n
残像が……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（残像って、怖いものばかりじゃなかったのね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……これも、ゲーム違い。\n
違っちゃいないが、今回は違う。"

hide guide_6
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0050
Guide "「さあ！！\n
君に一流の仕事を見せてあげるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……うん。\n
出来れば最初から見せてくれれば、ゲーム違いになったりならなかったりしなかったんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……まあ、いいわ。\n
行きましょう」"

hide guide_3
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice sat_g0051
Guide "「ああ、張り切っていこう！\n
で、君はどこの寮に決めたんだ？」"

if place_of_stay == "Castle":
    jump gakuen_dormitory_common_castle2
if place_of_stay == "Hatter":
    jump gakuen_dormitory_common_hatter2
if place_of_stay == "Amuse":
    jump gakuen_dormitory_common_amuse2
if place_of_stay == "Tower":
    jump gakuen_dormitory_common_tower2

label gakuen_dormitory_common_castle2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「え……？\n
赤薔薇寮だけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「手続きから先に行くんじゃないの？」"

hide guide_1
show guide_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sat_g0052
Guide "「手続きには、二種類あるんだ。\n
赤薔薇寮での自治会員加入手続きと、塔での学生証発行と」"

hide guide_4
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sat_g0053
Guide "「赤薔薇寮に住むことが決まっているなら、そこを最後にしたほうがいいな！\n
よし、行くぜ！行くぜ！」"

jump gakuen_dormitory_common3
label gakuen_dormitory_common_hatter2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「え……？\n
帽子屋寮だけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「手続きから先に行くんじゃないの？」"

hide guide_5
show guide_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sat_g0052
Guide "「手続きには、二種類あるんだ。\n
赤薔薇寮での自治会員加入手続きと、塔での学生証発行と」"

hide guide_4
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sat_g0089
Guide "「帽子屋寮に住むことが決まっているなら、そこを最後にしたほうがいいな！\n
塔から先に行こう！」"

jump gakuen_dormitory_common3
label gakuen_dormitory_common_amuse2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「え……？\n
遊園地寮だけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「手続きから先に行くんじゃないの？」"

hide guide_5
show guide_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sat_g0052
Guide "「手続きには、二種類あるんだ。\n
赤薔薇寮での自治会員加入手続きと、塔での学生証発行と」"

hide guide_4
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sat_g0097
Guide "「遊園地寮に住むことが決まっているなら、そこを最後にしたほうがいいな！\n
塔から行こう！」"

jump gakuen_dormitory_common3
label gakuen_dormitory_common_tower2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「え……？\n
塔だけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「手続きから先に行くんじゃないの？」"

hide guide_5
show guide_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sat_g0052
Guide "「手続きには、二種類あるんだ。\n
赤薔薇寮での自治会員加入手続きと、塔での学生証発行と」"

hide guide_4
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sat_g0101
Guide "「塔に住むことが決まっているなら……、そうだな。\n
まず塔で学生証を作って、それから他を巡ろう！」"

jump gakuen_dormitory_common3
label gakuen_dormitory_common3:
play sound se_0247
hide guide_5
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やる気みなぎった矢印に引っ張られて、手にしていた紐がピーンと張る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……っ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「ちょ、ちょっと……っ！？\n
待ってよ！？」"

hide guide_1
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_6")
voice sat_g0054
Guide "「待てない、待たない！\n
時間は待ってくれないんだ！」"

hide guide_5
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_6")
voice sat_g0055
Guide "「きりきり行くぞ！\n
新入生なんだ、てきぱき動かなきゃ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「そんなことないわよ、時間は曖昧で気まぐれなもので……。\n
……っと、これもゲーム違い」"

hide guide_3
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_16")
voice sat_g0056
Guide "「さあさあ！\n
急いで！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（白ウサギじゃあるまいし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……っ。\n
極端すぎじゃないの、あんた！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の新入生が、のどかに風船めいた矢印たちとガイダンスを進めていく中、私は無色の矢印に引きずられるようにして塔へと向かった。"

with dis
$ hi_mes()
hide guide_1

jump gakuen_dormitory_tower
label gakuen_dormitory_common4:

##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par20_re
with stripe_l_medium

play music gallery_front_day_p_wam

scene bg_par15_rg_tow_day
with stripe_l_long

show guide_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice sat_g0060
Guide "「塔での手続きは無事にすんだみたいだね！」"

play sound se_0058
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔から出たとたんに、ガイドの矢印がうねうねくねくねと賑やかになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……中では静かだったわね」"

hide guide_2
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice sat_g0061
Guide "「俺は一流のガイドだからね！\n
用事の間は、ちゃんとおとなしく待っているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「へえ、優秀……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（おとなしく待っていられるくらいでね……）"

hide guide_3
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice sat_g0062
Guide "「えへへ。\n
そう、優秀なガイド！」"

play sound se_0058
hide guide_5
show guide_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "半透明のガイドは、誉められたと思ったのか（実際には呆れていたわけだが）、嬉しげにくねくねと空中で身悶えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「はあ……」"

play sound se_0058
hide guide_6
show guide_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "途中でぴたっと止まって、矢印が首を傾げるように空中でクエスチョンマークの形になった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……？）"

if place_of_stay == "Castle":
    jump gakuen_dormitory_common_castle3
if place_of_stay == "Hatter":
    jump gakuen_dormitory_common_hatter3
if place_of_stay == "Amuse":
    jump gakuen_dormitory_common_amuse3
if place_of_stay == "Tower":
    jump gakuen_dormitory_common_tower3
label gakuen_dormitory_common_castle3:
hide guide_4
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice sat_g0063
Guide "「で、塔の次はどこへ行きたい？\n
帽子屋寮？それとも遊園地寮？」"

jump gakuen_dormitory_common5
label gakuen_dormitory_common_hatter3:
hide guide_5
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice sat_g0090
Guide "「で、塔の次はどこへ行きたい？\n
遊園地寮？それとも赤薔薇寮？」"

jump gakuen_dormitory_common5
label gakuen_dormitory_common_amuse3:
hide guide_5
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice sat_g0098
Guide "「で、塔の次はどこへ行きたい？\n
赤薔薇寮？それとも帽子屋寮？」"

jump gakuen_dormitory_common5
label gakuen_dormitory_common_tower3:
hide guide_5
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice sat_g0063
Guide "「で、塔の次はどこへ行きたい？\n
帽子屋寮？それとも遊園地寮？」"

jump gakuen_dormitory_common5
label gakuen_dormitory_common5:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「手続きで行く必要があるのは、塔と赤薔薇寮だけじゃなかったの？\n
他の寮にも行く必要がある？」"

hide guide_5
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice sat_g0064
Guide "「ないよ。\n
ないけど、場所の確認がしておきたいのなら案内してあげようかと思ったんだよ」"

hide guide_1
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice sat_g0065
Guide "「俺は一流のガイドだからね！\n
サービスもいいんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「……なるほど。\n
で、ここからだと、どちらが近いの？」"

play sound se_0056
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "尋ねながら、撫でてやった。\n
ぷにぷにとスライムめいた肌触りは、ひんやりと気持ちいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抑えるものの、力いっぱい握り締めたくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（いや、それは……。\n
でも、感触よさそう）"

play sound se_0056
hide guide_3
show guide_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice sat_g0066
Guide "「ふああ、気持ちいいな～。\n
君、テクニシャンだね！魔法使いにならなくても、マッサージ師を目指せばいいよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "矢印は、自分の危機的状況にも気付かず、気持ちよさそうに戯言を吐いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「はいはい。\n
分かったから説明してよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「まだ地理には疎いの。\n
ここからだと、他の寮へはどう行けばいいの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これ以上触っていると、本気できゅっと潰してみたくなってしまうので、私は矢印へと説明を求めて手を離した。"

hide guide_2
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0067
Guide "「了解！\n
各寮は、塔を中心に正三角形を描くように、等距離に配置されているよ」"

if place_of_stay == "Castle":
    jump gakuen_dormitory_common_castle4
if place_of_stay == "Hatter":
    jump gakuen_dormitory_common_hatter4
if place_of_stay == "Amuse":
    jump gakuen_dormitory_common_amuse4
if place_of_stay == "Tower":
    jump gakuen_dormitory_common_tower4

label gakuen_dormitory_common_castle4:
hide guide_3
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0068
Guide "「だから、巡るとしたら帽子屋寮、遊園地寮、そして赤薔薇寮といった順番がおススメだ！その順番で、学校の外周をぐるっと辿る形になるんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「ふむふむ。\n
それじゃあ、その順番でお願い」"

hide guide_5


scene bg06_sk_h_day
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice sat_g0069
Guide "「じゃあ、こっちからだよ。\n
こっちこっち！！」"

play sound se_0058
play sound se_0584
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賑やかに身をくねらせながら案内する矢印に引かれ、帽子屋寮に向かって歩き出す。"

with dis
$ hi_mes()

scene bg06_sk_h_day
with dis

scene bg_map_day
with dis
jump gakuen_dormitory_hatter_not1
label gakuen_dormitory_common_hatter4:

show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0091
Guide "「だから、巡るとしたら遊園地寮、赤薔薇寮、そして帽子屋寮といった順番がおススメだ！その順番で、学校の外周をぐるっとたどる形になるんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「ふむふむ。\n
それじゃあ、その順番でお願い」"

hide guide_5


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice sat_g0092
Guide "「任された！\n
こっちだよ、こっちこっち！！」"

play sound se_0058
play sound se_0584
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賑やかに身をくねらせながら案内する矢印に引かれ、私は遊園地寮に向かって歩き出した。"

with dis
$ hi_mes()

scene bg_map_day
with dis
jump gakuen_dormitory_amuse_not1
label gakuen_dormitory_common_amuse4:

show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0099
Guide "「だから、巡るとしたら帽子屋寮、赤薔薇寮、そして遊園地寮といった順番がおススメだ！その順番で、学校の外周をぐるっとたどる形になるんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「ふむふむ。\n
それじゃあ、その順番でお願い」"

hide guide_5


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice sat_g0092
Guide "「任された！\n
こっちだよ、こっちこっち！！」"

play sound se_0058
play sound se_0584
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賑やかに身をくねらせながら案内する矢印に引かれ、私は帽子屋寮に向かって歩き出した。"

with dis
$ hi_mes()

scene bg06_sk_h_day
with dis

scene bg_map_day
with dis
jump gakuen_dormitory_hatter_not1
label gakuen_dormitory_common_tower4:

show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0102
Guide "「だから、巡るとしたら帽子屋寮、遊園地寮、そして赤薔薇寮といった順番がおススメだ！」"

hide guide_5
show guide_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0102_5
Guide "「その順番で、学校の外周をぐるっとたどって、また塔に戻る形になるんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「ふむふむ。\n
それじゃあ、その順番でお願い」"

hide guide_2


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice sat_g0092
Guide "「任された！\n
こっちだよ、こっちこっち！！」"

play sound se_0058
play sound se_0584
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賑やかに身をくねらせながら案内する矢印に引かれ、私は帽子屋寮に向かって歩き出した。"

with dis
$ hi_mes()

scene bg06_sk_h_day
with dis

scene bg_map_day
with dis
jump gakuen_dormitory_hatter_not1
