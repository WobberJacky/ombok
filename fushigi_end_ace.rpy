
scene map_bg_spring_day
with dis
label fushigi_end_ace1:
$ clockanim()


scene map_bg_spring_day
with dis

scene map_bg_spring_night
with dis

scene map_bg_spring_day with Dissolve(1.2)

play music forest_town_road_p_ali

scene bg_gen_sky_spr_day
with dis
play sound se_0652
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0178
Ace "「あれ～、おかしいな。\n
城を目指していたはずなのに、どうしてこんなところにいるんだろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0179
Ace "「今回は誰かが送ってくれる刺客もいなかったし、熊に追いかけられたわけでもないし。\n
うーん、謎だらけだなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「またいつものように迷ったんでしょう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（哀しいぐらいに予想通りの結果だけど）"


scene s2_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "馬に乗った私達は、森の中を移動している。\n
高い木立に囲まれた視界のどこにも、他の建物の影は見えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地から去って、数時間帯が過ぎた。\n
しかし、一向に目的地は見えてこない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（ハートの城じゃなくとも、帽子屋屋敷やクローバーの塔も見えないなんて。\n
一体、どこの領土なのかしら、ここは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼といると、思ったようには目的地に辿り着けない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迷って、迷って。\n
近道を使おうとすればかえって迷い込み、悪化することも珍しくない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（本当に面倒な人）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、その面倒な人の傍にいることを選んでしまったのは、他でもない私自身だ。"


show ace_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0180
Ace "「ん？どうしたんだ、[firstname]？\n
そんな怖い顔をして睨むなんて……、疲れちゃった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「……そうね。\n
さすがに、ずっと馬に乗せられたままじゃ疲れるわ」"

hide ace_w_01_11
show ace_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice ace_f0181
Ace "「そうなんだ。\n
ずっと静かに乗っていてくれたから、俺はてっきり飽きちゃったんじゃないかと思って心配しちゃったぜ」"

hide ace_w_01_10
show ace_w_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice ace_f0182
Ace "「ほら、俺って面白味のない男だからさ。\n
メリーさんと違って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………？\n
どうしてそこでゴーランドの名前が出てくるの？」"

hide ace_w_01_1
show ace_w_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0183
Ace "「だって、メリーさんは面白いところがいっぱいあるじゃないか」"

hide ace_w_01_12
show ace_w_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0184
Ace "「何もしていなくても、名前だけでもすごく面白い。\n
だから、君も簡単について行くんだろう？」"

hide ace_w_01_4
show ace_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0185
Ace "「俺は、君にあんなに笑ってもらうことなんて出来そうもない」"

play sound se_0086
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "響いていた馬の足音が消える。\n
私を抱きとめている男の顔は静かに、笑ったままだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（妬いている？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確信はない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は大抵笑っているから、見ているだけでは本当の気持ちにまで手が届きにくい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「それって……、ヤキモチ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "試しに聞いてみたが、エースの顔に変化はなかった。"

hide ace_w_01_10
show ace_w_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0186
Ace "「さあ……？\n
何だと思う？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「あなたに分からないことが私に分かるとは思えないんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただでさえ分かりにくいエースだ。\n
近い距離にいるようになっても、彼のことはよく分からないことが多い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一つの側面を知って、同時に二つ以上の分からないことを抱える。\n
彼といるとどんどん深みに嵌っていくような気になっていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（……そういえば、何でこの人は私なんかと一緒にいるんだろう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドのことを引き合いに出されて、思い出す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私といるときよりも、ユリウスといるときのほうがエースは安定している。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の不在時にどれほど不安定だったかは、今でも思い出すと顔が引きつるほど酷かった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（私は、この人を支えられないと思うし、何も出来ないのに）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「どうして、今回は迎えに来てくれたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が出かけることなんて、いつものことだ。今回は事情が事情だったが、いずれ戻る予定だったことは、彼にはちゃんと話してきたのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（エースが後から迎えに来るなんて、何だか不思議だわ）"

hide ace_w_01_4
show ace_w_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice ace_f0187
Ace "「俺が君を迎えに来たのは意外だった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「ええ。\n
あなたがちゃんと迎えに来られたこともそうだけど、迎えに来たという行動そのものが意外だわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は迷う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迷ってもいずれ目的地に辿り着くが、かかる時間帯が尋常ではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（私が城に戻ったときに入れ違った、とかいうほうがまだ納得もしやすいわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "会いたいと思ったときに会えず。\n
会えないだろう、あるいは会いたくないと思っているときに遭遇する。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースとの関わりは、それの繰り返しだ。"

hide ace_w_01_12
show ace_w_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0188
Ace "「ははは、酷いなあ。\n
君がいなくて寂しくて、追いかけてきたとは思わないの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_9")
T "「思わないわ」"

hide ace_w_01_2
show ace_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "即答すると、エースは少しだけ目を見張った。"

hide ace_w_01_11
show ace_w_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0189
Ace "「そうかな？\n
俺は寂しいから君を迎えに行けたんだと思っていたんだけどなあ」"

hide ace_w_01_6
show ace_w_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0190
Ace "「うん。\n
何だか、すごく残念だ」"

hide ace_w_01_8


scene bg_gen_sky_spr_day
with dis
play sound se_0742 volume .3

scene bg_gen_sky_spr_nig with Dissolve(2)

play music moon_night1_a_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

play sound se_0210
pause .6
play sound se_0086

scene s2_03
with dis

show ace_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0191
Ace "「時間帯も夜になったし、今夜はここでキャンプだな。\n
おいで、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "馬から下りた彼は私よりも少し低い位置に顔がある。\n
珍しい、私を見上げる体勢。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "白い服の中で、赤い目が一際目を引く。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（服のせいかもしれないけど、今は騎士というよりも、王子様みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "立派な体格を包み込む、白い服。\n
眩しくて、非の打ち所もないはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は、お姫様のピンチに駆け付ける王子様より、迷い続けている騎士のほうが似合っている。"

hide ace_w_01_10
show ace_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「何でもないわ。\n
手を借りるわね、エース」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ馬に乗ったことも、乗らされたことも、子供の頃を除けば記憶にない。\n
こんな高い位置から飛び降りるには、彼の手が必要だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「よいしょ……っ、うわわっ」"

play sound se_0313
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "降りようとしたところで、馬が動いて、思わずしがみつく。"

hide ace_w_01_11
show ace_w_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0192
Ace "「ははは、そんなにあちこちに力を入れていたら、かえって危ないぜ。\n
馬は臆病な生き物なんだから、乗り手の気持ちにも敏感なんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「う……、ごめんなさい」"

hide ace_w_01_4
show ace_w_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice ace_f0193
Ace "「ほら、まずは片足をゆっくりこっち側に下ろすから、少し腰を引いて。\n
そうそう、うまい」"

hide ace_w_01_1
show ace_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

hide ace_w_01_10

play sound se_0052

show t_ace_end1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "名前を呼ぶと同時に、腕が引き寄せられて、体が倒れそうになる。\n
そこをエースが支えてくれ……、唇も重なった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「…………っ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice ace_f0194
Ace "「ん……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「……っ、ふ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice ace_f0195
Ace "「……どうしたんだ、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_7")
T "「っ、ど、どうしたって……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（いきなりキスしてきたのは、あなたのほうでしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言い返そうとした唇は、難なく彼によって再び塞がれてしまう。\n
絡みついてくる熱の感触に、身体の力が抜けた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「…………！」"

play sound se_0210
hide t_ace_end1
show bg_gen_sky_spr_nig onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元々不安定な姿勢だったせいだろう。\n
馬の上から私の身体が滑り落ちる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（危ない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭の中では警告が響いているのに。\n
久しぶりに重ねた唇が離せない。"

play sound se_0767
camera at hpunch
camera at vpunch
hide bg_gen_sky_spr_nig
show t_ace_end2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0196
Ace "「あ、落ちちゃった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（暢気なことを言うだけの余裕がよくあるわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どさりと、私はエースの上に乗っかっている。エースにとっては、これぐらいたいしたことではないということなのかもしれないが。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「痛くないの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同じ高さで躓いて転んだのとはわけが違う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の体重がすべてかかっていたはずだが、下敷きになっているエースに変わりはないように見えた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0197
Ace "「……痛いよ。\n
くらくらする」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「い、痛いんだったら、こんなことしていないで、早く起きないとっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（ここから一番近い病院はどこだったかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "吐血ばかりする友人のおかげで、あちこちの病院事情には大分詳しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まずはこの森から出るところから始めなければと思うのに、引き寄せる腕にこもる力は強まるばかりだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0198
Ace "「痛くて動けないんだよ。\n
なあ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0199
Ace "「ここが痛い気がするんだ。\n
どうしてだろうな？」"


play music quiet_night_a_ali
hide t_ace_end2
show t_ace_end3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0200
Ace "「君なら、理由が分かる？」"

play sound se_0478 volume .4
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "寝転んだまま、エースは私の手を自分の左胸へ誘導する。\n
チクタクと、規則正しい音が聞こえた気がした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「知らないわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（どうして？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（そんなこと、私だって分からないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一緒にいて、胸を痛ませる理由なんて思いついたとしても、口には出来ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（やっぱり、私じゃ駄目なの？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（ユリウスじゃないと……、駄目？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼を支えられるようになりたいなんて言わない。\n
それでも私と一緒にいることが苦痛になるのなら、それは……。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0201
Ace "「まるで燻っているみたいだな。\n
中がぐちゃぐちゃしていて、気持ち悪い」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0202
Ace "「こんな場所を怪我した覚えはないんだけどなあ、ははは」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0203
Ace "「君がいないときのほうが酷かったけど、今もじくじくしているなんて変だよなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「今も痛いんじゃなかったの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice ace_f0204
Ace "「うん、今も痛いよ。\n
でも、君がメリーさんといたときのほうが嫌な感じだったな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉と同時に、エースの手が頬にかけられる。\n
赤い瞳へ引き込まれるように、唇を近づけた。"

play sound se_0551
hide t_ace_end3
show t_ace_end4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "唇が塞がれて、息苦しさよりももっと強い感覚が襲ってくる。\n
エースの手が、頭を押さえてくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（押さえ込まなくても……、急に傍を離れたり、逃げたりしないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この手から逃げられると思うほど、私も楽観視はしていない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "出て行くキッカケは違うものだったが、そのおかげで分かったこともあった。\n
離れてみて、離れられないんだとようやく気付く。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（どんどん深みに嵌っていく）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "底なし沼だとしたら、きっと今は腰のあたりまで埋まっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もうどんなにもがいても浮き上がることは出来なくて、ただ沈むのを少し早めるだけ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（だったら）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（最後まで、沈んでしまってもいい）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「……ん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「…………っ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice ace_f0205
Ace "「……ふ。\n
君にキスしているときは、痛くないんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice ace_f0206
Ace "「これって、君が原因なのかな。\n
それとも、君が特効薬っていうことなのかな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice ace_f0207
Ace "「それとも、麻痺しているだけ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice ace_f0208
Ace "「答えが出るまで。\n
こうしていてもいいよな、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（そんなの、私に分かるわけがないじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "唇を塞がれているせいで、声が出ない。\n
エースも答えが欲しいわけではないのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（答えが出るまで……、ずっと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仮面とは違った、人のぬくもりが唇から伝わってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、このままもうしばらく迷っていてもいいと思ってしまう。"

$ hi_mes()
hide t_ace_end4


scene s2_03 with Dissolve(.8)

scene map_bg_spring_night
with stripe_l_medium

scene map_bg_spring_day with Dissolve(1)

scene bg_gen_sky_spr_day with Dissolve(1.2)

play music peter_t_ali
play sound se_0020
$ flash(.2)
pause .6
play sound se_0683
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0238
Peter "「エース君！\n
君という人は、一体どこをうろついていたんですか！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0209
Ace "「やあ、ただいま、ペーターさん。\n
どこって言われると困っちゃうな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0210
Ace "「いやあ、何しろ今回の旅も壮大だったからさあ。\n
君もそう思うだろう、[firstname]？」"


scene hm_spr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "{size=+20}「私に振らないで」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（遊園地には、あの短期間中に二回も来られていたはずなのに。\n
今回は何であんなに迷っていたのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気が付いたら馬はどこかに消えていたので、結局徒歩で戻ってきたのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（時間帯が何回変わったのか、途中で数えるのを放棄しちゃったわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "三十ぐらいまでは数えていたのだが、それ以上は精神的に限界だった。"


show per_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0239
Peter "「ああ、[firstname]、可哀想に。\n
こんな疲れ果てた顔をして……、一体どんな酷い目に」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「思い出したくないから、突っ込まないでちょうだい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "狼の群れに突っ込んだり、岩石がごろごろしているような場所でロッククライミングもどきをさせられたり。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（よく五体満足で帰ってきたわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の頑丈さに呆れるべきか、幸運に感謝すべきか悩むところである。"

hide per_t_01_6
show per_t_01_6 at left
show ace_w_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0211
Ace "「ははは、今回の旅も結構スリリングだったけど。\n
ほら、これはペーターさんのいうところの愛の試練ってやつだよ」"

hide ace_w_01_4
show ace_w_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0212
Ace "「危険を乗り越えて生まれる愛って偉大だろう？\n
ちょっと暑苦しくて、うざったいけど」"

hide per_t_01_6
show per_t_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0240
Peter "「そんなもの、エース君一人で乗り越えればいいでしょう。\n
彼女を巻き込まないでください」"

hide per_t_02_7
show per_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0241
Peter "「……それに、その服は何ですか？\n
ただでさえ胡散臭い笑顔が数倍増しで悪趣味です」"

hide ace_w_01_13
show ace_w_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0213
Ace "「ああ、これ？\n
遊園地で借りたんだ」"

hide ace_w_01_3
show ace_w_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0214
Ace "「ペーターさんも着てみる？\n
ペーターさんの場合、頭から真っ白だから、それはそれですごそうだよなあ」"

hide per_t_03_10
show per_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0242
Peter "「結構です。\n
まったく、似合わない服など早く脱ぎ捨てて、着替えてください」"

hide ace_w_01_1
show ace_w_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0215
Ace "「そんなに言われるほどに似合わなくはないと思うけどなあ。\n
なあ、[firstname]、結構似合うだろ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を振り返ったエースは首を傾げて問いかけてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背景には、いつものように晴れ渡った、青い空。真っ白な衣装が陽の光を反射して輝き、爽やかで、晴れやかな笑顔が浮かんでいる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（空っぽの笑顔）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "太陽や空と同じで、手を伸ばしてもけして掴めない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……似合わないわ」"

hide ace_w_01_2
show ace_w_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0216
Ace "「えーっ！？君までそんなこと言うの？\n
がっかりだなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「だって似合わないものは似合わないもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い城に戻ってくれば、白一色の彼の服はますます浮き上がっているように見える。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あなたには、いつもの赤が似合っているわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（あなただって、本当は好きじゃないんでしょう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "好感を持っているか、嫌悪しているのか。\n
世の中はすべてその二つに分類されるわけではなく、彼は特に分かりにくい人だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、好きか嫌いかの一番根本的な見極めぐらいは、私にも出来る。"

hide ace_w_01_8
show ace_w_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

hide ace_w_01_6
show ace_w_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0217
Ace "「そうか。\n
君が言うなら、そうなんだろうけど」"

hide ace_w_01_11
show ace_w_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0218
Ace "「うーん、でも結婚式のタキシードって普通は白だと思っていたんだけどな。\n
君が言うなら、真っ赤でもいいか」"

hide ace_w_01_1
show ace_w_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0219
Ace "「いつもと代わり映えしないけどな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「そうそう、やっぱりエースには、赤が」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_8")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_8")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "{size=+20}「え？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（今、結婚式って……、言った？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかも、白のタキシードを式で着るのは、ただ一人だ。"

hide per_t_02_11
show per_t_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0243
Peter "「君に相応しいのは、結婚式なんていう晴れの舞台ではなく、むしろその逆の葬式です。そもそも、一体誰の隣で赤いタキシードを着るつもりです？」"

hide per_t_02_2
show per_t_01_15 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0244
Peter "「……返答によっては、撃ち殺します」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこりと、形だけの笑顔でペーターが告げた。\n
ハートの城の入り口で、私達は何をしているのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城門の脇に立つ兵士達は、早くも漂っている物騒な気配に緊張感を滲ませているというのに、エースは火に油を注ぐ発言をやめなかった。"

hide ace_w_01_10
show ace_w_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0220
Ace "「ははは、ペーターさんってば野暮だなあ。\n
分かっていて聞いているんだろう？」"

hide ace_w_01_4
show ace_w_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0221
Ace "「でも俺はちゃんと花嫁の意向に沿う立派な新郎を務めてみせるぜ。\n
ちゃんと招待するから、そのときにはペーターさんも来てくれよな！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（……会話が噛み合っていない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースは赤いタキシードを着て新郎として結婚式に出るつもりのようだが、彼が相手では花嫁は相当に苦労するに違いない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（エースの笑顔……、ものすごく物言いたげなんだけど。\n
……まさか、私と一緒にだなんて言わないわよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確認してみたいが、肯定されたときに反応に困るので、私からは何も言えないし、言いたくない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それともいつもみたいに冗談だと流されるだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（それも何だか悔しいような）"

hide per_t_01_15
show per_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice pet_f0245
Peter "「……君の頭は以前から壊れていて、～～～～～したところでどうしようもないと諦めていましたが、気が変わりました」"

hide per_t_02_4
show per_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice pet_f0246
Peter "「ここですっきり終わらせておくことにしましょう」"

hide per_t_03_10

hide ace_w_01_13


scene bg_gen_sky_spr_day
with dis
play sound se_0020
pause .4
play sound se_0043
pause .5
play sound se_0020
pause .2
play sound se_0020
pause .5
play sound se_0685
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice ace_f0222
Ace "「ははは、ご祝儀が銃弾かあ。\n
ペーターさんらしいけど、いつもどおりすぎて面白くないなあ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice ace_f0223
Ace "「でも、俺は同僚想いの誠実な騎士だから、ちゃんとお相手してあげないと……！」"

play sound se_0020
pause .3
play sound se_0437
pause .5
play sound se_0020
pause .3
play sound se_0020
pause .3
play sound se_0020
pause .45
play sound se_0193
pause .3
play sound se_0685
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものように、赤い城に銃声と金属音が高らかに響き渡っていく中、私はその場を動くことも出来ず視線を彷徨わせてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（花嫁って、私じゃないわよね？）"


scene hm_spr_01
with dis

show siro_t_01_04 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice hei_f0019
Maid "「どうされました？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "騒ぎを聞きつけてやってきたメイド達が、私に声をかけてくれる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（きっと、いつもの質の悪い冗談だわ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「え……。\n
う、ううん、何でもない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（そうよ。\n
エースの言うことなんだから、本気にとればこっちが疲れるだけ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きっといつもの質の悪い冗談に決まっている。\n
そう結論づけて話を切ると、彼女達は不思議そうに首を傾げてきた。"

hide siro_t_01_04
show siro_t_01_04 at left
show siro_t_02_07 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0009
Maid "「そうですか？\n
でしたらいいんですが……」"

hide siro_t_02_07
show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0010
Maid "「ねえ？」"

hide siro_t_01_04

hide siro_t_02_01
show siro_t_02_01 at left
show heisi_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0019
Soldier "「ええ。\n
何ごともないのならいいんですが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……何？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦笑しているような、堪えているような彼らの反応に私は首を傾げてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すると、声を潜めるようにしてメイドの一人がそっと教えてくれた。"

hide siro_t_02_01

hide heisi_t_02_01
show heisi_t_02_01 at left
show siro_t_02_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0020
Maid "「お顔が、赤くなっていらっしゃいますよ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「え、な……！？」"

hide heisi_t_02_01
show heisi_t_02_04 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice hos_f0020
Soldier "「ええ。\n
それも、首まで……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（首が赤いのは、恥ずかしいせいじゃなくて、エースが）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_9")
T "（……って、違う、違う！\n
そうじゃないでしょうっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同僚の視線を受けて慌てて顔を背けたが。頬に当てた手から伝わる熱は、確かに……、いつもよりも高い気がした。"

hide heisi_t_02_04

hide siro_t_02_04

$ hi_mes()

scene hm_spr_01 with Dissolve(.8)

scene map_bg_spring_day
with stripe_l_medium

scene map_bg_summer_day with Dissolve(.8)

scene yum_sum_01_1
with stripe_l_medium

scene yun_sum_01
with stripe_l_medium

play music amuse_inside_p_ali
play sound se_0755
play sound se_0756
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遠目に黄色いジャケットを見つけて、私は声をかけた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ゴーランド！」"


show go_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gor_f0191
Gowland "「ん？おお、あんたか。\n
よく来たな」"

hide go_t_02_12
show go_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gor_f0192
Gowland "「ついでに騎士、あんたもか」"

hide go_t_03_1
show go_t_03_1 at left
show ace_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice ace_f0224
Ace "「うん、ちゃんと入り口から入ったぜ。\n
入場券も買ったんだから、問題ないよな、侯爵さん」"

hide go_t_03_1
show go_t_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Gowland "「…………」"

hide go_t_01_13
show go_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gor_f0193
Gowland "「ああ、それならいいぜ。\n
一般客に迷惑をかけねえなら、問題はねえ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "入場券をぺらぺらと振ってみせるエースに、ゴーランドは忠告しながら頷いた。"

hide ace_t_03_10
show ace_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0225
Ace "「ははは、酷いなあ。\n
俺はただの騎士なんだから、一般客に迷惑をかけるようなことをするはずがない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（嘘をつけ、嘘を）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ショーに勝手に乱入したり、馬を駆って遊園地内を疾走するのは、どう考えても迷惑行為だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（本人は迷惑とも何とも思ってなかったんだろうけど）"

hide go_t_03_10
show go_t_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice gor_f0194
Gowland "「……それで、そんな目立つお供を連れて、どうしたんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「あ、ほら、この前のスタンプラリーの景品を交換しようと思って」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "スタンプを押したものの、そのまま帰ってしまったので、ラリーを制覇した証である紙だけが手元に残っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "景品は、フリーパスポートとお試し券ということだったので、交換に来たのである。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（エースが何で一緒に来たのかは、分からないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城から出ようとしたところで鉢合わせて、ついてきてしまったのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今のところ近道と称して別の道に迷い込むことも少なく大人しいが、何の考えもないとは思いにくい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（借りてきちゃった衣装は、先刻入り口で従業員に渡してきたし……。\n
ここまで一緒に来る理由なんて、思いつかないんだけどな）"

hide go_t_01_11
show go_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gor_f0195
Gowland "「どれどれ……。\n
ん、確かに全部押してあるな」"

hide go_t_03_9
show go_t_03_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gor_f0196
Gowland "「結構大変だっただろう、園内のあっちこっちに置いてあったから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「……そ、そうね。\n
難易度は結構高かったわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（実際にはスタンプを押すことよりも、馬から落とされないようにしているほうが大変だったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドにスタンプの用紙を渡し、話していると、前から賑やかな声が届く。"

hide go_t_03_5

hide ace_t_01_4
show ace_t_01_4 at left
show pia_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0105
Pierce "「あれ、[firstname]！\n
君も来ていたんだ……って、ぎゃーーー、騎士！」"

hide pia_t_01_3
show pia_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0106
Pierce "「何で、何で騎士までいるの！？\n
俺をいじめに来たの！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "現れた早々に笑顔と悲鳴を上げたピアスは、ささっとゴーランドの背中に隠れている。余程怖いのか、ふさふさの尻尾が大きく膨らんでいた。"

hide ace_t_01_4
show ace_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0226
Ace "「ははは、侯爵さんだけじゃなくて、ネズミ君まで失礼なことを言うなあ。\n
俺はただの騎士なのにさ」"

hide ace_t_03_3
show ace_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

hide ace_t_03_10
show ace_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0227
Ace "「あれー、侯爵さん。\n
何か虫が付いているよ」"

hide ace_t_02_11

hide pia_t_02_6


show go_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0197
Gowland "「は？虫だ？\n
どこだよ……ん？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然のエースの言葉にゴーランドは身の回りを確認するが、何も付いている様子はない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「虫っぽいものなんて、どこにもないじゃない、エース」"

hide go_t_03_3
show go_t_03_3 at left

show ace_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice ace_f0228
Ace "「えー、見えない？\n
おかしいなあ。ほら、あそこだよ、あそこ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って指でどこかを差すが、やはり彼の言うようなものは見つからない。"

hide go_t_03_3
show go_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0198
Gowland "「何だおまえ、方向感覚だけじゃなくて目まで悪いのか？」"

hide ace_t_01_11
show ace_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0229
Ace "「ははは、そんなことはないよ。\n
気付かないなんて、皆こそ目が悪いんじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「？？」"

play sound se_0443
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「エ、エース！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（何をしているのよ、あんたは！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "皆で首を傾げている状態の中、急に抜刀したエースに驚く。"

hide go_t_02_10
show go_t_02_10 at left_center
hide ace_t_03_3
show ace_t_03_3 at center
with dis

show pia_t_03_3 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0107
Pierce "「ぴっ！\n
何、何、騎士、やっぱり俺をいじめに来たの！？」"

hide ace_t_03_3
show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0230
Ace "「ははは、ネズミ君は面白いことを言うなあ。\n
俺はそんなことをするほど暇じゃないよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかしここはゴーランドの領地。\n
いくら剣の腕が立つエースとはいえ、意味もなく剣を振り回していい場所ではない。"

hide ace_t_01_4
show ace_t_01_10 at center
hide go_t_02_10

hide pia_t_03_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0231
Ace "「だって、皆が分からないみたいだからさ。\n
ほら……」"

play sound se_0676
pause .6
play sound se_0527
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "軽い音が響くと同時に、ゴーランドが持っていた紙が細切れになっていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "紙を持っていた彼の手に怪我はないようだが、一瞬の出来事に全員が息を飲んでいた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "例外は、剣を振るった張本人だけだ。"

hide ace_t_01_10
show ace_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0232
Ace "「あれ、おかしいなあ。\n
紙に止まっていたから一緒に切れたはずなんだけどなあ」"

hide ace_t_03_2
show ace_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0233
Ace "「残念、逃げちゃったみたいだね。\n
紙も一緒に切っちゃうなんて、失敗しちゃったよ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（最初からこれが狙いだったのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうりでここまで大人しくついてきたわけだ。ゴーランドと私が園内をまわっていたことが、それほどまで気に入らなかったらしい。"

hide ace_t_02_3
show ace_t_02_3 at left
show go_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0199
Gowland "「……ガキっぽい真似するなよ、騎士。\n
あんたもこれが相手じゃ大変だろう、色々と」"

hide go_t_03_2
show go_t_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0200
Gowland "「スタンプのほうは目で確認していたから、景品を渡してやってもいいんだが」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらりとそこでゴーランドはエースのほうを見る。\n
物言いたげな視線と、笑みを浮かべた目が一瞬火花を散らす。"

hide go_t_02_13
show go_t_02_13 at right
hide ace_t_02_3
show ace_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

hide ace_t_03_10
show ace_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0234
Ace "「何？\n
くれるの？」"

hide go_t_02_13
show go_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0201
Gowland "「今回は、見送っておいたほうがいいな。\n
また次の機会にな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「あ、ありがとう、ゴーランド」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "多分、この場でもらったとしても、ラリーシートと同じ末路を辿るだけだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐らく、ゴーランドも私と同じ様に考えたはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（……それにしても）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "細切れになって、地面に落ちているシートを見て溜息が漏れる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（気に入らないならそう言えばいいのに、いちいち刃物を取り出さないと駄目なのかしら、この男は）"

hide go_t_03_7

hide ace_t_03_11

$ hi_mes()

scene yun_sum_01 with Dissolve(.8)

scene yun_sum_01
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_medium

scene map_bg_spring_day with Dissolve(1)

scene hm_spr_01
with stripe_l_medium

scene hn_spr_01
with stripe_l_long

play music castle_garden_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「普通、結婚式って新郎は白いタキシードよね？」"


show viv_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice viv_f0222
Vivaldi "「そうじゃな、たまに例外はあるじゃろうが……。\n
オーソドックスなものを選ぶのならば、白だろう」"

hide viv_t_03_10
show viv_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
Vivaldi "「…………」"

hide viv_t_01_11
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice viv_f0223
Vivaldi "「何だ、エースの奴が何か言いだしたのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地から戻って、久しぶりの女王様とのお茶会。\n
メイドも下がらせてしまった今、私はビバルディと二人っきりでいる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「言い出したというか、この前ペーターと一緒に話していたというか。\n
赤いタキシードで式に出るとか、何とか言っていたの」"

hide viv_t_01_3
show viv_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
Vivaldi "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「うん、冗談よね。\n
多分、何となくの話の流れでそういうことを言っただけだと思うんだけど」"

hide viv_t_03_11
show viv_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_1")
Vivaldi "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_15")
T "「ん？」"

hide viv_t_01_12
show viv_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_15")
voice viv_f0224
Vivaldi "「既に手遅れじゃろうが……。\n
おまえ、男の趣味が悪いな」"

hide viv_t_02_2
show viv_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_15")
voice viv_f0225
Vivaldi "「嘆かわしい……。\n
よりにもよって、選んだのが{size=+20}あれとは{/size}」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "{size=+20}「ぶっ！」{/size} "

play sound se_0187
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「げほ、げふっ。\n
な、何を……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然の言葉に、思わず飲んでいた紅茶がつまる。\n
げほげほと咳き込む私に、ビバルディは呆れた声で続けた。"

hide viv_t_02_7
show viv_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0226
Vivaldi "「結婚式では男など添え物にすぎぬ。\n
だというのに、花嫁よりも目立つような男がどこにおる？」"

hide viv_t_01_8
show viv_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0227
Vivaldi "「そんな不届きもの、首を刎ねてもまだ飽き足らぬわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……でも、ほら、別に私が花嫁になるわけじゃないし」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（そもそもエースと結婚式というイメージが結びつかないのよね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（家庭を持って、子供がいて。\n
ペットに犬なんか飼っていたりして）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（駄目だわ、想像力が追い付かない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭の中でイメージしようにも、拒絶反応を起こしているらしく、思い浮かばなかった。"

hide viv_t_03_9
show viv_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

hide viv_t_03_12
show viv_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0228
Vivaldi "「やれやれ。\n
悪趣味と鈍感の組み合わせとは……」"

hide viv_t_01_7
show viv_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0229
Vivaldi "「これではどうしようもないな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

hide viv_t_01_12
show viv_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0230
Vivaldi "「何でもない。\n
呆れただけじゃ」"

play sound se_0174
pause .5
play sound se_0039
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉どおり呆れ顔のビバルディが無言のままに差し出したカップに、お代わりを注いだ。"

hide viv_t_02_7
show viv_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0231
Vivaldi "「ふう。\n
男など愚か者の集まりだが、あれはその中でも群を抜いた愚か者じゃぞ」"

hide viv_t_01_13
show viv_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0232
Vivaldi "「迷ってばかりで、行き着く先もろくでもない。\n
[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ビバルディ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を差し出されて、首を傾げながらもそっと重ねる。"

hide viv_t_03_11
show viv_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0233
Vivaldi "「あの面倒な男に見切りを付けたら、いつでも逃げておいで。\n
わらわがおまえを匿ってあげる」"

hide viv_t_03_10
show viv_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0234
Vivaldi "「女王が味方についておるのだ。\n
これ以上ない切り札じゃろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_8")
T "「ええ」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（この人は、優しくて、そして……、強い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "重ねていた手を、ぎゅっと握った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディは、弱い私に逃げ道をくれる。\n
その好意を裏切るかもしれない私を匿ってくれるという。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ビバルディ」"

hide viv_t_01_2
show viv_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0235
Vivaldi "「どうした、改まって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「あのね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この手は私が選んだ手ではない。\n
しかし、振り返ればいつでも待っていてくれる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だからこそ、私は揺らぐ。\n
ありえないと思っているのに、可能性を信じたくなる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「私、あなたと友達になれて嬉しいわ。\n
ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心からの感謝と愛情を込めて。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の誰にも伝えられない素直な好意を口に出来るのは、彼女が私にとって姉のような存在だからかもしれない。"

hide viv_t_02_9
show viv_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

hide viv_t_01_5
show viv_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0236
Vivaldi "「そうだな。\n
わらわも、おまえが好きだよ、[firstname]」"

hide viv_t_03_4
show viv_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0237
Vivaldi "「おまえがここにいて、よかった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鮮やかな微笑みを浮かべて、女王は笑う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼とは違う。\n
中身のある、本当の感情が伝わってくる笑い方だった。"

hide viv_t_03_6

$ hi_mes()

scene hn_spr_01 with Dissolve(.8)

scene hm_spr_01
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium

scene map_bg_winter_day with Dissolve(1)

scene charasel_bg_tower_day
with stripe_l_medium

scene ts_01
with stripe_l_long

play music tower_room1_p_ali

show yuri_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Julius "「…………」"

hide yuri_t_03_11
show yuri_t_03_11 at left
show ace_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースと何度も訪れた、ユリウスの仕事部屋。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あちこちに修理を待つ時計やその材料が置かれた部屋で、私達は全員沈黙していた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは困惑と諦めを滲ませた顔で。\n
私は頭痛と予想通りの反応に溜息をつく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースだけはいつものように、にこにこと笑っている。"

hide ace_t_03_3
show ace_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0235
Ace "「だからさ、いつか分からないけど。\n
ユリウスには絶対に来てほしいんだよなあ」"

hide ace_t_03_11
show ace_t_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0236
Ace "「来てくれるよな？\n
俺、そのためだったらばりばり仕事を片付けて、準備しておくからさ！」"

hide yuri_t_03_11
show yuri_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

hide yuri_t_02_8
show yuri_t_03_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0038
Julius "「寝言を言いたいのなら、私ではなく、ナイトメアに言え。\n
私には縁のない話だ」"

play sound se_0160
hide yuri_t_03_12

hide ace_t_02_1

pause .4
play sound se_0480
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（まあ、普通はそう言うわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの如く仕事の呼び出しに時計塔に行くと言ったエースに連れられて、ハートの城を出たのが二十時間帯前だっただろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものように迷いまくり、遅れて辿り着いたエースを迎えたユリウスは、最初はいつもどおりだった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迷う彼に何を言っても無駄だということを彼は私よりもよく分かっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（諦めているとも言えるけど）"


show ace_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice ace_f0237
Ace "「え、ユリウス、何だよ、それ。\n
親友に対して冷たくないか？」"

hide ace_t_03_7
show ace_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice ace_f0238
Ace "「こういうときは、諸手を挙げて喜んでくれるのが親友じゃないか」"

hide ace_t_01_8
show ace_t_01_8 at left
show yuri_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
Julius "「…………」"

play sound se_0479
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースの戯言に耳を貸すことなく、ユリウスは手元の仕事を続けていた。\n
無視したい気持ちが全身からありありと漂っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（気持ちはよく分かる）"

hide ace_t_01_8
show ace_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice ace_f0239
Ace "「ユリウス。\n
なあなあ、ユリウスってば」"

hide yuri_t_02_8
show yuri_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
Julius "「……………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "内心鬱陶しいと思っているに違いないユリウスは、それでも辛抱強く耐えている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、何度も何度も彼の名前を呼んでいる様子を見ていると、帽子屋屋敷にいる大きなウサギを連想してしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（あそこの上司だったら、適当なところで話を逸らすだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（ユリウスなら完全に無視するタイプよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よくも悪くも忍耐強い人だ。"

hide ace_t_03_9
show ace_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0240
Ace "「ユーリーウースー。\n
無視しないでくれよ！」"

hide ace_t_02_8
show ace_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0241
Ace "「俺、そんなに冷たくされると拗ねちゃうぜ？」"

play sound se_0440
pause .5
play sound se_0273
$ flash(.2)
hide yuri_t_02_11
show yuri_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「～～～～っ！」"

hide yuri_t_03_12
show yuri_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0039
Julius "「エース、おまえ！\n
何をする！？」"

hide yuri_t_03_7
show yuri_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0040
Julius "「私の作業台にこんな傷を作って！\n
邪魔をするなら出ていけ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースが躊躇いなくざくっ、と机に剣を突き刺した。\n
さすがのユリウスも黙っていない。"

hide ace_t_03_4
show ace_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0242
Ace "「ははは、だってユリウスが無視するからさ。\n
こうすればちゃんと聞いてくれると思って」"

hide ace_t_01_1
show ace_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0243
Ace "「それに、時計には傷一つ付けていないんだから、そんなに怒るなよ。\n
そのうち、綺麗さっぱり直るからさ」"

hide yuri_t_01_8
show yuri_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0041
Julius "「そういう問題ではない！！」"

hide yuri_t_03_13
show yuri_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0042
Julius "「先刻も言っただろう、寝言が言いたいんだったら、ナイトメアの元に行け」"

hide yuri_t_02_11
show yuri_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0043
Julius "「よりにもよって、{size=+20}そいつとの結婚式に神父役で出ろとはどういう意味だ！{/size}」"

hide yuri_t_02_7
show yuri_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0043_5
Julius "「ここから出るだけでも気が重いというのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの気持ちも分かるが、私は私で呆然としたまま動けずにいる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（エースが私と結婚？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（このエースと、私が？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地から戻って彼が繰り返していた結婚の相手は、私のことだったらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（いまだに現実感がないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だって年頃だ、そういう大きな転機にはある程度イメージというものを持っていたはずだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（どうしてかしら。\n
相手がエースというだけで、想像さえ出来ない）"

hide ace_t_03_10
show ace_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice ace_f0244
Ace "「ははは、だってユリウスだったら神父様が似合うと思って。\n
こうしかめっ面で、愛想のない神父だろうけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースが普段から赤い服を着ているように、ユリウスも黒い服を着ている。\n
そんな彼が果たして白い神父服を着てくれるのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_6")
T "（でも、エースが白を着るよりは似合うかな）"

hide yuri_t_03_12
show yuri_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_6")
voice jul_f0044
Julius "「だいたい、どうして突然結婚話なんか持ちかけてくるんだ。\n
おまえのキャラじゃないだろう」"

hide yuri_t_03_10
show yuri_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_6")
voice jul_f0045
Julius "「おまえもだ、[firstname]。\n
私を巻き込むんじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……それもそうなんだけど。\n
私に止められると思う、エースを？」"

hide yuri_t_02_8
show yuri_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さな声で囁くと、ユリウスは言葉に詰まった。\n
エースは人の話を聞いてはいるが、聞き入れることなど稀だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迷うくせに自分の意見は貫き通すタイプである。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（ビバルディの台詞じゃないけど……、本当に厄介な人よね）"

hide yuri_t_02_3
show yuri_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice jul_f0046
Julius "「そ、そうだとしてもだ。\n
おまえに結婚の意志はあるのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え、私？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "話を振られて思わず声が上ずってしまう。"

hide ace_t_02_4
show ace_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースは名指しされた私を見ても、表情を変えない。\n
私が何と答えるのかを楽しみにしているような、そんな印象だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "{size=+20}「結婚は、ちょっと考えたいわね」{/size} "

hide ace_t_03_10
show ace_t_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice ace_f0245
Ace "「えー。\n
君までそんなにつれないことを言わないでくれよ」"

hide ace_t_02_2
show ace_t_02_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice ace_f0246
Ace "「人生経験は多いほうがいいぜ。\n
嫌だったらやめればいいし」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「……離婚なんて、させてくれるの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（何だか軽い子みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結婚して嫌だったらすぐに別れようなんて、そんなお試し感覚に私はついていけない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼にそう思われていたのかと思うと、少し恨めしいとさえ感じた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「別れることが前提だったら、最初からしないほうが賢明だわ。\n
色々と面倒そうだし」"

hide ace_t_02_1
show ace_t_03_10 at center
hide yuri_t_03_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "軽口につい突っ込んでしまったが、その瞬間、エースが漂わせている空気の種類が変わる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "表情はまったく変わらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただ、気のせいか。\n
赤い目が一瞬で濃くなったような、そんな印象を受けた。"


play music secret_a_ali
hide ace_t_03_10
show ace_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0247
Ace "「えー、結婚する前から別れ話？\n
まあ、君は余計なことばっかり考える子だから仕方ないのかもしれないけど……、別れたいの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰と、とは言わなかったが、暗に告げられていた。\n
先ほどまで感じなかった汗が、背中を伝って流れ落ちていくのが分かる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（怖い）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（……殺されるかもしれない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "殺気には縁遠い私が無意識にそう思うほどの、空気。\n
一瞬も外れない視線は、私を押し潰しそうなほど強い。"

hide ace_t_03_12
show ace_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0248
Ace "「俺は騎士だから、君がどうしてもっていうなら考えてもいいけど」"

hide ace_t_01_11
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0249
Ace "「でも、覆すかどうかは約束できないぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

hide ace_t_01_10
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
voice ace_f0250
Ace "「別に今すぐっていう話じゃないし、いつか分からないけど。\n
俺と、結婚してくれる？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（これって、プロポーズなの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "好きな男から人生初のプロポーズと一緒に、殺されかねないプレッシャーをかけられている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ときめきによる鼓動よりも、身体に走る冷や汗のほうが気になった。"

hide ace_t_03_3
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

hide ace_t_01_10
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0251
Ace "「なあ、[firstname]、返事は？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……理由を聞いてもいい？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "椅子から立ち上がった彼を、じっと見つめる。\n
意外なほどに、問いかけの声はあっさりと出てきた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（理由が分からない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの騎士という役が嫌なエース。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "与えられた役を拒むように、ユリウスの元で仮面を付けて別の役を装っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（そんな彼がどうしてそれほど結婚に拘るの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これまでそんな話は出てこなかった。\n
安定を求めるなんて、彼らしくないとも思う。"

hide ace_t_03_11
show ace_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0252
Ace "「理由か。\n
君のことが好きだからじゃ、駄目？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「……駄目ね。\n
足りないわ」"

hide ace_t_01_11
show ace_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「女性を口説こうって言うのなら、それなりに手の内を見せなさいよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉だけで分かる部分など限りがある。\n
その上、嘘を交えて話されてしまえば、それまでだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（でも……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（エースは、嘘はつかない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスの団長であった道化師とは違う。"

hide ace_t_01_6
show ace_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0253
Ace "「夫婦って色んなものを分け合うんだろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しばらくの沈黙の末に、彼はそんなことを言った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「？」"


play music ace_t_ali
hide ace_t_03_2
show ace_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice ace_f0254
Ace "「ほら、喧嘩両成敗っていう諺があるじゃないか。\n
君が持つものを半分もらってあげようかと思って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「は？」"

hide ace_t_02_10
show ace_t_02_10 at left
show yuri_t_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice jul_f0047
Julius "「おまえ、何を言っているんだ。\n
エース？」"

hide ace_t_02_10
show ace_t_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice ace_f0255
Ace "「ええと、ほらあの定番の台詞があるだろう。\n
病めるときも、健やかなるときも……だっけ？」"

hide ace_t_03_7
show ace_t_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice ace_f0256
Ace "「夫婦になれば、君だけが責任を感じなくていい。\n
そうしたら、城から出て行く必要だってなくなるじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースはそこで言葉を切ると、私に向かって首を傾げて見せた。"

hide ace_t_01_11
show ace_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0257
Ace "「俺は君が自分を責めるのを止めたりしないし、必要以上に責めたりもしないよ」"

hide ace_t_01_10
show ace_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0258
Ace "「でも、他の誰かの前で落ち込まれるのは、面白くないからね。\n
だから、半分、奪ってあげる」"

hide ace_t_03_11
show ace_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0259
Ace "「全部取っちゃったら、面倒で大変だろう？\n
だから、半分くらいならちょうどいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「…………」"

hide ace_t_02_10
show ace_t_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0260
Ace "「これが理由なんだけど。\n
ははは、どうしたんだよ、二人とも」"

hide ace_t_02_3
show ace_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0261
Ace "「鳩が豆鉄砲を食らったような顔をしているぜ」"

hide yuri_t_01_10
show yuri_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice jul_f0048
Julius "「いや……。\n
{size=+20}予想以上にまともなことを考えていたので、驚かされた{/size}」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "{size=+20}「同じく」{/size} "

hide ace_t_03_3
show ace_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice ace_f0262
Ace "「えー、二人とも酷いなあ。\n
俺はいつだってまともな騎士じゃないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、明るく笑う騎士が見せたあの赤い瞳は、私の中からけして消えることはなかった。"

hide yuri_t_03_2

hide ace_t_01_3

$ hi_mes()

scene ts_01 with Dissolve(.8)

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_long

show black onlayer master with close_long

play music jail_p_ali

show t1me onlayer master with open_long
play sound se_0158
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（ここは……、もうないと思っていたのに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（どうして、ここに来ちゃったんだろう）"

play sound se_0389
play sound se_0035
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "嘘つきな季節の終わりと共に、終わったはずのサーカス。\n
そして、失われたはずの監獄。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスの公演中に来たときよりも、静かで、空っぽな空気が漂っている。"


show jo_k_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0000
Black_Joker "「監獄がなくなるはずがねえだろう」"

hide jo_k_02_8
show jo_k_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0001
Black_Joker "「罪は消えねえ、罪の意識に悩む奴がいる限り、ここが消えることもねえんだ。\n
全員が本物の悪党になるっていうなら、話は別だがな」"

$ flash_black(.2)
$ flash_black(.1)
$ flash_black(.1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薄い闇の中に、溶け込むような影。"

hide jo_k_03_4
show jo_k_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0002
Black_Joker "「そうしたら、俺達はお役ご免ってことで清々するぜ」"

hide jo_k_01_14
show jo_k_03_19 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0003
Black_Joker "「ああ、処刑人は大忙しになって、いいかもしれねえ。\n
あいつには仕事があったほうがいいだろうからな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……ジョーカー」"

$ flash_black(.1)
$ flash_black(.1)

hide t1me with expand
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が認識するに従って、影はその色を増して確かな形となる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラックさんのほうだ、傲岸な、見下すような表情ですぐに分かる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「あなたも、消えていないものね」"

hide jo_k_03_19
show jo_k_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice jok_f0004
Black_Joker "「ああ、そういうことだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「だったら……、ホワイトさんも？」"

hide jo_k_02_5
show jo_k_02_5 at left
show jo_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice jok_f0005
White_Joker "「ああ、いるよ。\n
俺のことも覚えていてくれたみたいで、嬉しいな、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「忘れるはずがないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "穏やかな声と共に、灰色の影がもう一つ増える。\n
二人の監獄所長が並び立つ。"

hide jo_t_01_11
show jo_t_03_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0006
White_Joker "「ねえ、[firstname]。\n
彼はああ言ったけど、半分、分けたいと思うの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らが私に起きた出来事を知っていることには、今更驚きはしない。"

hide jo_t_03_15
show jo_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0007
White_Joker "「重いものを背負わせて、苦しいものを分けたところで。\n
結局のところ、抱えるのは君一人だ」"

hide jo_t_02_10
show jo_t_03_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0008
White_Joker "「彼の言うことは、ただの綺麗事。\n
君だって、薄々気付いているだろう？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（そうね。\n
誰かに肩代わりできるようなものじゃないわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "唆すように囁く相手に、否定を返せない。"

hide jo_t_03_14
show jo_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0009
White_Joker "「彼は、捕らえられたお姫様を救い出す王子様じゃない。\n
あいつは捕らわれることを拒むもの、罪の意識に縛られないものを裁くものだ」"

hide jo_t_02_4
show jo_t_03_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0010
White_Joker "「城にいても、ここでも、その本質は変わらない。\n
だから、仮面を付けていられる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

hide jo_t_03_14
show jo_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jok_f0011
White_Joker "「つまり牢に入っているこれを、彼はけして殺してくれない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！」"


play music serious_a_ali
show t_jo3_1 onlayer master
with dis
hide jo_k_02_5

hide jo_t_01_1

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「……あ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_3")
T "「姉さん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "牢獄の中に、姉の姿が見えた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0012
White_Joker "「これが牢の外に出ようとするのなら、話は別だろうけど。\n
君を見ている限り、その気はないようだね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "指先が格子に触れると、ひんやりとした感触が伝わってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "牢獄の中にいる姉は私達をじっと見ているだけで、声も出さなければ、動く気配もなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（出ようともしない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（でも、どうして？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この姉が偽物であったとしても、牢に捕らわれたままでいられる人間なんていない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "なのに、どうして彼女は今もここでじっとしているのだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0013
Black_Joker "「どうするんだ、それを出すのか？\n
出せば末路は一つだけだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0014
Black_Joker "「あいつ、迷うくせに仕事はするからな。\n
遅かれ早かれ……、処刑されるだけだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0015
White_Joker "「それは君にしか出せない。\n
でも、出すことが、解放することが本当に君の望みなのかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「私は……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐらぐら揺れているのは、頭なのか。\n
意識なのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（出したら、罪人）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（処刑される）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（……あの人に？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice ace_f0263
Ace "「そのぐらいにしておいてくれないかな、ジョーカーさん」"

hide t_jo3_1

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「エース！？」"


show t_ace_end5 onlayer master
with dis

play music tension_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーの背後に、エースは一人立っている。\n
身に付けているのは、いつもの赤い騎士服。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その色を見ただけで、何故か力が抜けそうになった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0016
Black_Joker "「何だ、おまえ。また迷ってきたのかよ。\n
いい加減、仕事は片付いたのか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0264
Ace "「うーん、なかなか厄介だからさ。\n
まだ迷っているんだよね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0265
Ace "「脱獄した本人か、それとも唆した相手か……。\n
どっちを殺すのが筋かな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0017
Black_Joker "「面倒くせえな。いいじゃねえか、まとめて始末すれば。\n
いつものおまえならそうだろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0266
Ace "「ははは、まあ仕事の話は別として。\n
……ねえ、ジョーカーさん」"

play sound se_0089
hide t_ace_end5
show t_ace_end6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースはブラックさんからホワイトさんのほうへと視線を変えて、剣を抜く。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0267
Ace "「彼女の中で結論はまだ出ていないんだから、今はまだジョーカーさんのものじゃない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0268
Ace "「あまり、余計なことはしないでくれないかな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの穏やかな口調。\n
その中に不快な感情を僅かに拾ったのは、私の気のせいだったのか。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0018
White_Joker "「俺から手を出したみたいに言われるのは釈然としないなあ。\n
迷い込んできたのは、彼女のほうだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0019
White_Joker "「君と一緒にいるおかげかな。\n
ますます、不安定になって、ここに近付いてきている」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0269
Ace "「俺は、処刑する役目だろう。\n
ジョーカーさんや夢魔さん、猫君のように、迷わせたりするのとは違う」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0020
White_Joker "「そうだね。\n
なら、処刑せずにここに収監させる？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0021
White_Joker "「それも一つの答えだね。\n
少なくとも、彼女にはその資格があるようだし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そういって片眼が見つめたのは、いまだ牢獄の中で動かない姉。\n
彼女は人形のようにじっと座って、私達の会話を聞いている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、聞いているのかも分からない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただ、そこに存在していた。\n
消えることなく、残り続けている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_3")
T "「っ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（何で？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少し、息苦しい。\n
胸の中央が痛いような気がする。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0270
Ace "「駄目だよ。\n
ジョーカーさんには、あげない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0022
White_Joker "「なら、君がいつか始末をつける気かな？\n
彼女が完璧な囚人になる、その前に」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0271
Ace "「……さあね」"

play sound se_0439
hide t_ace_end6
show t_ace_end7 onlayer master
with dis

play music opposition1_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「エース……？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice ace_f0272
Ace "「ははは、そんな顔しないでよ、[firstname]。\n
言っただろう」"

play sound se_0439
pause .6
play sound se_0645
$ flash_purple(.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の剣は、いつもの大剣。\n
魔法の光を帯びたわけでも何でもないのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が剣を振るうと空間が少しずつ切れていく。"

play sound se_0441
pause .5
play sound se_0645
$ flash_indigo(.2)
hide t_ace_end7
show t_ace_end8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0273
Ace "「君の荷物、半分は俺が奪ってあげるって。\n
だから、終わりも同じだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0274
Ace "「それに、君もよく知っているように俺はよく迷うんだ。\n
ちょっとの重しぐらいじゃ、変わりようがない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice jok_f0023
Black_Joker "「迷った挙げ句に、取り逃がすなよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice ace_f0275
Ace "「ははは、ジョーカーさんは面白いことを言うなあ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice jok_f0024
Black_Joker "「当たり前だ。\n
おまえみたいな囚人も、罪人も、俺はごめんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice jok_f0025
Black_Joker "「さっさとその半端者を連れて、帰るんだな」"

play sound se_0679
pause .5
play sound se_0645
$ flash_indigo(.2)
play sound se_0645
$ flash_purple(.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "空気が裂ける。\n
小さな傷が徐々に広がって、捲られていく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0026
White_Joker "「仮にこれを君が背負ったとしても、君は何も変わらない。\n
そして、これは消えるわけでもなければ、軽くなるわけでもない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0027
White_Joker "「だったら、俺に預けたほうがいいと思わない？\n
俺なら、これも、彼女も閉じ込めておいてあげる」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0028
White_Joker "「……どこにも行かせないよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0276
Ace "「それは……、嫌だね」"

play sound se_0439
pause .5
play sound se_0645
$ flash_red(.1)
hide t_ace_end8
show t_ace_end9 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0029
White_Joker "「くっ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今まで空気を裂いていたはずのエースの切っ先が、僅かにジョーカーの袖を引き裂いている。\n
じわりと漂う血の香りに、心臓が跳ねた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0277
Ace "「言っただろう、俺はよく迷うんだって。\n
だから、一緒に迷っていれば目を離した隙に取られることもない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0278
Ace "「まだジョーカーさんの出番じゃないんだ。\n
引っ込んでいてよ、邪魔だから」"

play sound se_0441
hide t_ace_end9


show jo_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0030
White_Joker "「やれやれ。\n
どちらにせよ、大した差はないと思うけどね」"

play sound se_0537
hide jo_t_01_14


play music truth_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「エース……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後に残った彼に駆け寄るよりも早く、赤い影に包み込まれる。"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「っ！」"


show t_ace_end10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice ace_f0279
Ace "「ん、ふ……っ。\n
迷子は迷子を引き寄せるのかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「は……、エース……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背中越しに当たる格子の向こうには、姉の影があるというのに、彼は気にしてくれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（苦しい）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（痛い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが悲鳴を上げているのは身体なのか、それとも心なのか。\n
そもそも心に痛みを感じるような機能など、本当にあるのか分からない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「や……だ、だめ……」"

hide t_ace_end10


show ace_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_4")
Ace "「…………」"

hide ace_t_01_11
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_4")
voice ace_f0280
Ace "「そうだね。\n
ここじゃ、何をするにも不自由だ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "笑った顔は私を見て、もう一度剣を振り上げる。\n
薄暗い監獄の中、白い刃だけが目を奪った。"

hide ace_t_03_10
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0281
Ace "「戻ろうぜ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

hide ace_t_01_10

play sound se_0441

scene black with close_m
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後に剣が切り裂いたのは、果たして何だったのだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
Julius "「[firstname]、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「ん……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice jul_f0049
Julius "「おい、いい加減起きないか！」"

play sound se_0391

play music tower_room1_p_ali

scene ts_02 with open_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「……ん。\n
ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（い、痛い……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "寝起きなのでよく分からないが、私は頬を叩かれた気がする。\n
女に何をするのかと恨み言を告げたい気持ちだ。"


show yuri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0050
Julius "「まったく、いつまでも人の部屋に居座るな。\n
さっさとあれを連れて、帰れ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "指で指し示されたほうを見れば、床に転がって寝息を立てている赤い騎士がいた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あれ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「私、いつの間に」"

hide yuri_t_02_11
show yuri_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice jul_f0051
Julius "「まだ寝惚けているのか？\n
エースと一緒に結婚がどうだ、参列がどうだとか喋っていただろうが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「そうだったわよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものように騒ぐエースに呆れつつ、確かどうでもいいようなことを話して。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少し座りたいといってソファを借りたところまでは覚えているが、それから先の記憶がない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（転寝しちゃったのね、私）"

hide yuri_t_03_10
show yuri_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jul_f0052
Julius "「……目は覚めたか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ええ、ありがとう。\n
？」"

hide yuri_t_01_12
show yuri_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice jul_f0053
Julius "「ついでに淹れただけだ。\n
いらないなら、適当にその辺に置いておけ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「……ううん、頂くわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "珈琲の入ったカップを受け取って口を付ける。\n
立ち上ってくる蒸気に、ほっと力が抜けた。"


play music night_garden_p_ali
hide yuri_t_01_4
show yuri_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0054
Julius "「先刻の話だがな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（先刻の話って……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「あ、ひょっとして、エースと私の……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結婚式という言葉がどうにも出て来なくて、中途半端に声が止まる。"

hide yuri_t_03_8
show yuri_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0055
Julius "「そ、そうだ。\n
まったく馬鹿げた話だが……」"

hide yuri_t_02_8
show yuri_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

hide yuri_t_03_13
show yuri_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0056
Julius "「仕事が落ち着いていたら、顔ぐらいは出してやる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_13")
T "（それって）"

hide yuri_t_02_6
show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_13")
voice jul_f0057
Julius "「あまりに参列者がいない式では、哀れだからな。\n
神父役をやるなんて冗談じゃないが」"

hide yuri_t_03_9
show yuri_t_03_9 at left
show ace_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_13")
voice ace_f0282
Ace "「そんなこと言うなよ、ユリウス！」"

play sound se_0051
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

hide yuri_t_03_9
show yuri_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jul_f0058
Julius "「くっ、エ、エース！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "寝ていたかと思ったエースが、ガバッと勢いよく背後から抱きつく。"

hide ace_t_01_1
show ace_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0283
Ace "「親友なんだから、勿論特等席だよなあ。\n
やっぱりそうすると、神父役が一番いいと思うんだ、俺」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースがにこにこと楽しそうに続けるのとは対照的に、ユリウスは迷惑そうだ。"

hide yuri_t_01_3
show yuri_t_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0059
Julius "「だ、から、なんで……、そんなに、私に、神父をやらせたいんだ、おまえはっ」"

play sound se_0313
camera at hpunch
camera at vpunch
hide ace_t_03_3
show ace_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0284
Ace "「ははは、だって、神様に誓うなんて俺の柄じゃないし、君だって嫌だろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り払われてもめげないエースが続ける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「エース？」"

hide ace_t_02_10
show ace_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0285
Ace "「俺、ユリウスにだったら誓約を立てられる。\n
ええと、病めるときも、健やかなるときも……だっけ」"

hide ace_t_03_11
show ace_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0286
Ace "「うん、ユリウスにだったら約束できる気がする」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「普通、そういうのって神父役に誓うものなの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（根本的なところがずれている気がするんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かにエースらしいといえばエースらしい言い分なのだが、仮にもプロポーズをされた側としては実に複雑だ。"

hide yuri_t_03_7
show yuri_t_01_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0060
Julius "「まったく、だったらわざわざ面倒なことをしなくてもいい。\n
やはり式はなしだ、そんなことのために引っ張り出されるなんて冗談じゃない」"

hide ace_t_01_4
show ace_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0287
Ace "「そう言うなって、ユリウス。\n
親友だろう？」"

play sound se_0055
hide yuri_t_01_8
show yuri_t_03_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0061
Julius "「ええい、鬱陶しい、纏わり付くなっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（そうね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（私は、ここがいい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの言わんとすることが分かって、知れず笑みが浮かぶ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計が置かれた、必要以上に物のない時計塔の一室。\n
あるいは、赤に染め上げられたハートの城。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_1")
T "（どこでも、一緒に迷っていければいい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰かに新たに閉じ込められるまでもなく、私は既に捕まっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（結婚は人生の墓場だっていうけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「……結婚してもしなくても、そういう意味では変わらないわよね」"

hide ace_t_01_3
show ace_t_03_2 at center
hide yuri_t_03_12
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_13")
Ace "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「何でもないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつか半分だけでもこの人に託せるだろうか。\n
そして、逆に私がこの人の半分を預かることが出来るのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（やっぱり、すぐには想像出来ない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それだけの決意が定まったら、監獄の鍵よりももっと重いもので、私は繋がれる。\n
しかし、それぐらいのほうが、安心できる気がした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（私には、まだ「時間」が残されているもの）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「あなたと一緒なら、迷うのも悪くないと思ったのよ」"

hide ace_t_03_2
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice ace_f0288
Ace "「そうだね。\n
俺もそれは同感だよ」"

hide ace_t_03_3
show ace_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice ace_f0289
Ace "「君と一緒なら、どんなに迷っても安心だ。\n
だって、帰れなくなったって……、出口がすぐそこにあるようなものだからな」"

hide ace_t_02_1 with dis
hide ali_t_06_2
hide frame_gen_chara
with Dissolve(2)

scene white
with compress_extralong
scene black with compress_extraextralong
stop music

$ renpy.movie_cutscene("endroll_a.mpg")
#return
