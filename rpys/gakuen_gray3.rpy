label gakuen_gray3:
scene bg06_sk_h_day
with dis
$ clockanim()


scene bg06_sk_h_eve
with dis

play music room2_p_wam

scene bg06_sk_h_nig with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの夜の差し入れは、しばらく続いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日中は、それぞれの仕事や授業で忙しい。\n
そのため医務室を訪ねでもしない限りはなかなか会うことが難しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな彼と、夜のほんの一時、庭と部屋と離れていても時間を共有できる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今夜も、メイドを通じて届けられた温かいココアを啜りながら、私は庭を見下ろす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こちらを見上げるようにして、ランタンの灯りが揺れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "応じるように、私もゆっくりと手を振り返す。\n
明確な意味こそないが、それは確かに会話だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "揺れる光は、ベッドに行きなさいと促すかのように見える。"

menu:
    "おとなしくベッドに行く。":
        jump gakuen_gray3_2a
    "まだ見ている。":
        jump gakuen_gray3_2b
label gakuen_gray3_2a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……おやすみなさい）"

play sound se_0165 volume .7

scene bg24_rj_nig_lon
with dis
pause 1
play sound se_0177
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中で彼へとそう挨拶して、カーテンを閉じると一度机に向かった。\n
その上に、飲み終えたココアのカップを置く。"

jump gakuen_gray3_3
label gakuen_gray3_2b:
$ lovechara_gray_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（嫌よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手を揺らす。\n
彼を見送りたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、私が窓辺から離れて部屋の明かりが落ちるのを見届けたいと思っているのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、私のほうは、彼が職務に戻るのを見送りたいと思っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ココアを飲み終えてもまだ、彼は動かない。\n
私も、動けない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夜闇に溶け込んで見えないはずなのに、庭に立ち尽くしてこちらを見上げる彼の姿が見えたような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……仕方ないわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアを相手にしているのを見ていても分かる通り、彼は粘り強い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして私と見詰め合っていては、いつまで経っても彼は見回りを終えられないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "諦めて、最後にもう一度ゆっくりと手を振る。"

play sound se_0165 volume .7

scene bg24_rj_nig_lon
with dis
pause 1
play sound se_0177
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カーテンを閉じると一度机に向かった。\n
その上に、飲み終えたココアのカップを置く。"

jump gakuen_gray3_3
label gakuen_gray3_3:

scene m_cut_gre2_2_gre3
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カップの傍らに転がっているのは、お馴染みとなった謎の生き物。\n
本日も、グレイからのメッセージを預かってきているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（朝になると、大抵いなくなっちゃっているけど……。\n
消さずにすむ方法はないのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "届けられる、おやすみのメッセージ。\n
出来ることならば、手元に残しておきたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見張ってみたり、籠を用意して閉じ込めてみたり。\n
いろいろ試してみたが、効果はなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝には忽然といなくなってしまっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらくそういう設定のマジックアイテムなのだろうが、せっかくのメッセージが消えてしまうのはとても残念だ。"


scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_1")
T "「……んんー」"

play sound se_0160 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "両腕を天井に向けて伸ばして、伸びをした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つい先刻終わらせたのが、最後の課題だ。\n
こうして課題をこなしているうちに、少しずつコツも掴めてきたような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん期末テストのような大きなものが近付いてきたら、きっとまた振り回されてしまうのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、こうして普段の授業や、ちょっとした研究課題のこなし方を身につけられたのは進歩だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これで、少しは時間を上手に使えるようになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（そろそろ……。\n
医務室に、遊びにいけるかしら）"


scene bg24_rj_nig
with dis
play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを思いながら、ベッドの中へと潜り込んだ。"

with dis
$ hi_mes()

scene bg24_rj_nig with Dissolve(.8)
jump gakuen_dream_other_2
label gakuen_gray3_4:
with dis
$ hi_mes()

scene bg01_cr_day with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg_map_eve with Dissolve(1)

scene bg_par15_rg_tow_eve
with stripe_l_medium

scene bg25_rr_eve
with stripe_l_long

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後、久しぶりにナイトメアの医務室を訪れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（グレイに会える。\n
ちゃんと、お礼を言わなきゃ……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不慣れな課題に追われる中、彼の差し入れてくれるココアやメッセージが、とてもモチベーションを上げるのに役立ってくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓越しに灯りを見るだけでなく、ちゃんと言葉を交わしたい。\n
話すと長くなりそうで、機を逃していたが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（やっと……）"

play sound se_0302
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice nig_g0278
Nightmare "「開いているよ」"

play sound se_0397

scene bg_par16_rs_tow_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの声に促されてドアを開けた。\n
いつもなら、グレイがドアを開けて出迎えてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の中に足を踏み入れて、ナイトメアの執務机の傍らまで歩を進めた。"


play music high_eve_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……グレイは？」"


show nai_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice nig_g0279
Nightmare "「ちょっと待て、[firstname]！\n
私の医務室に来て、開口一番尋ねるのがグレイの行方というのはどうなんだ！？」"

hide nai_m_03_8
show nai_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice nig_g0280
Nightmare "「嘘でもいいから、私に会いたかったと言うべきじゃないのか！\n
この部屋の主は私だぞ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「……嘘でもいいの？\n
会いたかったわ、ナイトメアー」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんともわざとらしい、棒読みだ。"

hide nai_m_02_5
show nai_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0281
Nightmare "「うう、ひ、ひど……！！\n
私だって、君が来てくれるのを楽しみにしていたというのに……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ふふ、冗談よ、冗談。\n
あなたにも、もちろん会いたかったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「でも、いると思っていた人がいなかったから……。\n
まずは、そっちが気になっても仕方ないでしょう？」"

hide nai_m_02_9
show nai_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice nig_g0282
Nightmare "「……まあ、な。\n
私が医務室にいて、グレイが見張っていないというのは珍しい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「それ、胸を張って言うセリフじゃないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、珍しいのは事実だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイがここでナイトメアの仕事の進捗状況を見張っていないのもおかしいし……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逆にナイトメアがグレイの不在時でも執務机におとなしく座っているというのも珍しい。"

hide nai_m_02_11
show nai_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0283
Nightmare "「今日は、特別な夜だからな。\n
グレイが忙しいのも仕方がない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「特別な……、夜？\n
もしかして、例のアレ？」"

hide nai_m_03_11
show nai_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice nig_g0284
Nightmare "「なんだ、君、もう知っているのか？\n
新入生には内緒というのがセオリーのはずなんだが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ええ、だから、私も何があるのかは知らないわ。\n
ただ、何かがあるってことだけは聞いているの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝から感じるそわそわとした空気や、おかしな行動をしていた使用人達のことを思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば、グレイは塔の管理をしており、塔の使用人達を統括する立場だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今夜ある「何か」に使用人も関係しているのならば、もちろんグレイも関わっているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ねえ、やっぱりあなたも秘密主義なの？\n
こっそり内緒で教えてくれたりはしない？」"

hide nai_m_03_4
show nai_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nig_g0285
Nightmare "「……ふふ。\n
ズルはいけないよ、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「だって、気になるんですもの。\n
グレイまでその準備に駆り出されるなんて、相当に力が入っているのね」"

hide nai_m_03_10
show nai_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice nig_g0286
Nightmare "「さあ？\n
それは、ことが起きてから君自身の目で確かめればいいことだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは白状しない。\n
私も、元より本気で教えてもらえるとも、教えてほしいとも思っていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それが分かっているからか、対峙する彼も本気で私を諌める口調ではなかった。"

hide nai_m_02_12
show nai_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0287
Nightmare "「何はともあれ、まだ夜までは少し時間がある。\n
私の休憩に付き合ってくれるだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……ええ、そうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一体、夜になれば何があるというのか。"

hide nai_m_01_1


scene bg06_sk_h_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらり、と顔を上げて景色を見やる。\n
夕日はすでに沈み、空のふもとをほの赤く染めるだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……グレイ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この時間帯に思い出すのは、塔の上、煙草を吸う彼の姿。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろそろ、夕食の時間だ。\n
夜は近い。"

with dis
$ hi_mes()

scene bg_par15_rg_tow_eve
with stripe_l_medium

scene bg_map_eve with Dissolve(1.2)
##endmemory
jump gakuen_gray4
