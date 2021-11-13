label fushigi_joker1_memory:
label fushigi_joker1:
$ hi_mes()
hide screen fushigi_map1
scene map_bg_joker_day
with fade
$ clockanim()


play music forest_door_road_p_ali

scene s2_01 with Dissolve(1.8)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "滞在地を出て、森へと向かう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（サーカスはもうないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰もいない場所に行きたがるなんて、まるで逃げるみたい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "色とりどりの舞台、芸達者な団員達。\n
そして、団長と所長の二つの顔を持つ、あの人。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカス興行の終わりと共に、彼らもまた去っていったはずだ。"


scene bg_gen_sky_all_day with Dissolve(1.6)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……あれ？」"

play sound se_0045
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（何の音？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスの行われていた頃の森は、遊園地にも負けない賑やかな音で溢れていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、開演期間に該当しなければ、森は人がいるかも定かではないほど、静かな空間だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "団員は黙々と練習に身を費やし、そして彼は……。"

$ hi_mes()

play music forest_circus_p_ali
pause 1

scene circus with stripe_l_extralong
pause .5

show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0031
White_Joker "「いらっしゃい、[firstname]。\n
季節を変えたいの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……{size=+20}え？{/size}」"

hide jo_t_03_1
show jo_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice jok_f0032
White_Joker "「せっかく来てくれたのに悪いね。\n
サーカスが終わっちゃったから、今の俺に季節は変えられないんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ジョーカー！？\n
あなた、まだいたの！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "木々の間から姿を見せた黒装束の道化師の姿に、声が跳ね上がる。"

hide jo_t_01_12
show jo_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jok_f0033
White_Joker "「まだって……、酷いな。\n
まるでいなかったほうがいいみたいに言わないでよ、傷つくだろう」"

hide jo_t_01_4
show jo_t_03_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jok_f0034
White_Joker "「俺は皆を楽しませてあげたいだけなのに、どうしてそう嫌がるかなあ。\n
君にまで嫌われるなんて、本当に俺って報われない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "はははと乾いた笑いを浮かべたジョーカーは、季節を変えにこの場所に通っていた頃と、全く変わっていなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（夢じゃなさそうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "かつては夢にも出てきたことがあるジョーカーだが、今、目の前にいる彼の姿はどう見ても現実のように思えた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「だって、サーカスは閉幕だって自分で言っていたじゃない。\n
なのに、どうしてまだいるのよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もう一度会いたかったような、もう二度と会いたくなかったような……。\n
彼に会うとき、私の中にはいつも相反する気持ちが浮かぶ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（苦手っていうわけでもないし、はっきりと好きというのも何か違う気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "友達といえるほど彼を知っているわけではないが、踏み込むのが怖いような、そんな複雑で曖昧な気持ち……。"

hide jo_t_03_17
show jo_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0035
White_Joker "「舞台は終わったように見えても、片付けなんてそう簡単に終わるものじゃないんだ」"

hide jo_t_02_4
show jo_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0035_5
White_Joker "「こうなってくると団長も団員も関係なし、全員一致団結して撤収作業に当たっているってわけ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言われて見渡すと、確かに梱包のための資材やサーカスで使う大道具が、いくつか地面に散らばっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きっとテントの中では団員達が、解体作業を進めているのだろう。"

hide jo_t_02_1
show jo_t_02_1 at left
show jo_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0036
Black_Joker "「てめえ、ジョーカー。\n
こんなところで油を売ってんじゃねえよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同じ顔、だが浮かべている表情はまるで対照的な男が、その背後から現れる。"

hide jo_t_03_10
show jo_t_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0037
Black_Joker "「俺まで駆り出して手伝わせてるっつうのに、余裕じゃ……、ん？\n
またこのガキ相手にサボりやがって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「……あなたもいたのね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（まあ、ホワイトさんがいるなら、ブラックさんもいないとおかしいのかもしれないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大きな荷物を持ったブラックさんは、むすっとした顔のまま私を見て、犬でも追い払うように手を振った。"

hide jo_t_03_4
show jo_t_03_17 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0038
Black_Joker "「いいから、とっととどっかに行けって。\n
ジョーカーも言っただろうが、うちは今片付けで忙しいんだ」"

hide jo_t_03_17
show jo_t_02_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0039
Black_Joker "「おまえみたいな～～～～なガキに構っている暇はねえんだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相変わらず口の悪い男だ。"

hide jo_t_02_1
show jo_t_03_14 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0040
White_Joker "「そういえば、どうしてサーカスに来たんだ、[firstname]。\n
もうここは残骸しか残っていない場所なのに……、遊びに来たの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……自分でもよく分からないわ。\n
何となく、足が向いただけ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰もいない閑散としたサーカスの跡地。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それを予想してこの場に来たはずなのに……、彼らに会って少しほっとしたような気持ちになっているのも事実だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まるで彼らが最初からここで私を待っていたことを、どこかで分かっていたような気さえしてくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（何でだろう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "嘘つきの季節は終わり、サーカスとともにジョーカーもまた去った。\n
ここに彼らが留まっていると思うこと自体、おかしなことのはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（やっぱり、この人に会いたかったのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の気持ちなのに、よく分からない。"

hide jo_t_03_14
show jo_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0041
White_Joker "「[firstname]？\n
どうしたの、そんな強ばった顔をして……？」"

hide jo_t_01_1
show jo_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0042
White_Joker "「撤収中とはいえ、ここはサーカスだよ。\n
楽しまなきゃ駄目だろう？」"

hide jo_t_02_15
show jo_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0043
Black_Joker "「ったく、辛気臭い顔しやがって……。\n
ガキを宥めるような菓子なんか、俺は持ってねえぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（私は子供か）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とことんこっちのジョーカーは私を子供扱いしたいらしい。"

hide jo_t_01_5
show jo_t_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0044
White_Joker "「ジョーカーは持っていないって言うけど、俺は持っているよ。\n
[firstname]、キャンディーを食べない？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「いらない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お菓子につられるほど、子供じゃない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこからともなく取りだした飴を差し出してくる相手から顔を背ける。\n
しかし、相手はそう簡単に逃がしてくれるような男ではなかった。"

hide jo_t_03_1
show jo_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0045
White_Joker "「そんなこと言わないで、食べてみなよ。\n
これ、美味しいよ……、はい、どうぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！？\n
ジョ、ジョーカー！」"


show t_jo1_1 onlayer master
with dis
hide jo_t_03_9

hide jo_t_03_10

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0046
White_Joker "「あーん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚いた拍子に開いた口に小さなものが放り込まれてしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「う……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口の中に広がる甘い味。\n
だが、簡単に手玉に取られてしまったことが悔しくて、味わうどころではない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0047
White_Joker "「そんなに警戒しないでよ。\n
本当にただのキャンディーだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0048
White_Joker "「公演中に露店で売っていたのと同じものさ。\n
結構、人気商品なんだよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然押し込まれた飴玉を吐き出すわけにもいかず、怒るべきか、迷いながら口の中で飴を転がすことしかできない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0049
White_Joker "「どう、美味しい？\n
食べたことなかったかな、この味」"

hide t_jo1_1
show t_jo1_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………。\n
そうね、あなたのサーカスでは食べたことのない味だわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「でも、私、この味を知っているような気がするの。\n
どこだったかしら……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たかがキャンディーなのに、気になって仕方がない。\n
ジョーカーがくれたそれは、記憶のどこかで引っかかるような味をしていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "果物とも違う、甘いのにどこか苦い気さえする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "甘さの奧に隠れている味が、私の気持ちを惹き付ける。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（どこで食べたんだったっけ……。\n
一度味わったら忘れられないような、そんな味なのに……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思い出せない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0050
Black_Joker "「そういう割にはすっきりしねえ顔だな。\n
おまえ、本当に知っていたのか、この味」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ホワイトさんの手から無断で一粒飴を取ると、ブラックさんは口の中へと放り込んだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0051
Black_Joker "「普通のキャンディーだろう。\n
何てことねえ味だぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「そうかもしれないけど……。\n
どこかで食べたようなそんな気がしたのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、ちょっとだけ気になってしまった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（それだけ……、よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それ以上の理由なんてないはずだ。"

hide t_jo1_2


show jo_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0052
White_Joker "「ふうん、そうか。\n
君にそこまで味わってもらえるのなら、ご馳走した甲斐があったよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「味わったんじゃなくて、あんたが放り込んだんでしょうがっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さも美味しそうに食べたように言わないでほしい。"

hide jo_t_01_2
show jo_t_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0053
White_Joker "「細かいことを気にしないでよ。\n
いいじゃない、まずくは……、なかったんだろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこりと笑ったジョーカーは、私の手を取って急に歩き出す。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「わっ、な、なによっ」"

hide jo_t_03_14
show jo_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice jok_f0054
White_Joker "「撤収前で散らかっているけど、うん、ちょうどいいかな。\n
中を見せてあげるよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「中……？\n
この中なら何度も入っているから知っているけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "公演中にはそれこそ何度も何度も訪れた場所だ。\n
光と闇のパレードが見せた技の数々は、私の記憶にも新しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、ジョーカーは笑ったまま首を横に振る。"

hide jo_t_01_6
show jo_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0055
White_Joker "「そうだね、君は客席からの風景はよく知っているだろうけど……。\n
逆の風景は見たことがないだろう？」"

hide jo_t_01_11
show jo_t_01_11 at left
show jo_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0056
Black_Joker "「おい……、ジョーカー。\n
俺は反対だぜ、こんなガキを舞台裏に連れていくなんて」"

hide jo_t_02_2
show jo_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0057
Black_Joker "「何もねえところですっ転んで、そこらへんの物を壊すに決まってんだろうが」"

hide jo_t_02_8
show jo_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0057_5
Black_Joker "「壊れてもいずれ直るとはいえ、片付けの最中に余計なことをして散らかしてどうするんだよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "反対する相方の言葉にも、ホワイトさんは気にした様子もない。"

hide jo_t_01_11
show jo_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0058
White_Joker "「ははは、いいじゃないか。\n
彼女によって壊されるものなら、それは仕方がないってことだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ちょ、ちょっと、ジョーカー！\n
私、行くなんて……！！」"


show black onlayer master
with dis
hide jo_t_01_3

hide jo_t_02_2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "天幕に引き込まれて、視界すべてが一瞬暗転する。\n
代わりに見えたものは……、公演中にも目にした舞台。"


play music circus_a_ali


hide black

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ……！」"

play sound se_0415
play sound se_0417

show j-boy_a_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice mat_f0017
Danin "「ジョーカー、ずるいよ。\n
僕達にばっかり片付けさせて……」"

hide j-boy_a_11
show j-boy_a_11 at left
show j-girl_a_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nos_f0008
W "「そうよ、そうよ。\n
なかなか戻ってこないんだもの」"

hide j-boy_a_11
show jo_t_03_2 at center
hide j-girl_a_9
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jok_f0059
White_Joker "「ごめん、ごめん。\n
その代わり、素敵なお客さん……、いや、違うな」"

hide jo_t_03_2
show jo_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jok_f0060
White_Joker "「珍しい見学者を連れてきたから、そんなに責めないでよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスで親しくしていた子供達が、ジョーカーの元へ駆け寄ってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の足下にやってきた子供達は、その言葉を聞いてようやく私の存在に気が付いたらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "公演中にも何度か顔を合わせた彼らには、私も覚えがあった。"

hide jo_t_03_7
show jo_t_03_7 at left
show j-boy_a_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0018
Danin "「あ、本当だ！いらっしゃい。\n
見学に来たの？」"

hide jo_t_03_7
show jo_t_03_7 at left_center
hide j-boy_a_3
show j-boy_a_3 at center
show j-girl_a_9 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0009
W "「ジョーカー、やっぱりずるいわ。\n
私達を除け者にして、自分だけ相手をするなんて」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きゃっきゃっとジョーカーに纏わり付いていた彼らは、一転して私に飛びついてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「……っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きゅっと手首を掴んでくる力は、見た目とは裏腹にかなりの強さだ。\n
痛みを覚えないぎりぎりの力加減。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舞台の上で無邪気な笑みを浮かべている子供達が見た目通りではないことを、嫌でも思い出してしまう。"

hide j-boy_a_3
show j-boy_a_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0019
Danin "「よかった、ここを引き払う前に来てくれて。\n
ねえ、ジョーカー、お姉さんも僕達と一緒に来るの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「は？」"

hide j-girl_a_9
show j-girl_a_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nos_f0010
W "「だって、中に連れて来るってことはそういうことなんでしょう？\n
部外者には中は見せないもの、そうよね？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ちょ……、何言っているのよ、あなた達！？\n
私はたまたま森に来ただけで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "このサーカスと一緒に行く気なんてない。\n
私には、帰る場所があるのだから。"

hide jo_t_03_7
show jo_t_02_14 at center
hide j-boy_a_5
hide j-girl_a_2
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0061
Black_Joker "「ガキはガキ同士で勝手にじゃれてろよ。\n
ああ、面倒くせえな……」"

hide jo_t_02_14
show jo_t_03_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0062
Black_Joker "「おい、ジョーカー。\n
こっちはおまえの管轄だろう、あとは適当にどうにかしろよ」"

hide jo_t_03_17
show jo_t_03_17 at left
show jo_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0063
White_Joker "「こらこら、自分だけ楽をしようなんてそれはないだろう、ジョーカー。\n
君達も、彼女は大事な見学者なんだから、いじめたら駄目だよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って彼は、難なく子供達から私を引き離す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "掴まれた手首に加えられた力が弱まった様子はなかったのに、一体どんな方法を使ったのか、痛みはまったくない。"

hide jo_t_03_17
show jo_t_03_9 at center
hide jo_t_01_13
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0064
White_Joker "「片付けは、一端中止」"

hide jo_t_03_9
show jo_t_03_9 at left
show j-boy_a_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0020
Danin "「え？片付け、しなくてもいいの？」"

hide jo_t_03_9
show j-boy_a_6 at left
hide j-boy_a_6
show j-girl_a_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0011
W "「私達、お休みになるの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「……？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（休みが嬉しくないのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで私にじゃれついていたときとはまったく違う顔。\n
何故か中止を言い渡された彼らの顔は、困っているように見えた。"

hide j-boy_a_6
show jo_t_03_15 at center
hide j-girl_a_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0065
White_Joker "「心配いらないよ、休みになるっていうんじゃない。\n
ただせっかくこれだけ間近で技を振るう機会があるんだ」"

hide jo_t_03_15
show jo_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0066
White_Joker "「腕試し、したくない？」"

hide jo_t_01_1
show jo_t_01_1 at left
show j-boy_a_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0021
Danin "「うん、したい！\n
僕、ブランコ上手になったんだ、見せてあげたいっ」"

hide jo_t_01_1
show j-boy_a_4 at left
hide j-boy_a_4
show j-girl_a_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0012
W "「私だって、綱渡り上手くなったもの！」"

hide j-boy_a_4
show j-boy_a_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0022
Danin "「僕のほうが上手だよっ」"

hide j-girl_a_4
show j-girl_a_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0013
W "「違うわ、私のほうが上手よ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "練習用の投げナイフなのか、互いに刃物をちらつかせる二人に私のほうが引きつってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（こ、この世界の人間ときたら、誰も彼も……っ）"

hide j-boy_a_9
show jo_t_01_12 at center
hide j-girl_a_9
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice jok_f0067
White_Joker "「こらこら、ここで睨み合うんじゃない。\n
まだ彼女はお客さんなんだから、見せるなら別のものを見せてあげないと」"

hide jo_t_01_12
show jo_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice jok_f0068
White_Joker "「ナイフ投げはまだ練習中だから、見せちゃ駄目だろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひょいひょいと軽い手付きで二人の手からナイフを回収したジョーカーが笑うと、二人は仕方なさそうに歩き出した。"

hide jo_t_01_11
show jo_t_01_11 at left
show j-boy_a_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0023
Danin "「まずはブランコからだよね」"

hide jo_t_01_11
show j-boy_a_11 at left
hide j-boy_a_11
show j-girl_a_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0014
W "「違うわ、綱渡りからよ」"

hide j-boy_a_11
show jo_t_02_9 at center
hide j-girl_a_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0069
Black_Joker "「どっちも大して上手くねえんだから、同じだろうが。\n
さっさとやることやって、追い返せ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「……あなた、よっぽど私のことを追い出したいわけ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくらこの世界で好かれやすい余所者とはいえ、何の前触れもなく突然やってきたのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "絶対に歓迎されるとは思わないが、彼の言葉は妙に棘がある。"

hide jo_t_02_9
show jo_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0070
Black_Joker "「当ったり前だろうが、頭の悪いガキなんて一番質が悪いぜ。\n
……見るもの見たら、とっとと帰れよ」"

hide jo_t_03_12

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言いたいことだけ言って、ブラックさんは姿を消してしまった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「あの人、私のことが本当に嫌いなのね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あからさまに冷たくあしらわれなくてはいけないほど、交流もないと思うのだが。"


show jo_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0071
White_Joker "「ジョーカーが君を嫌っている？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「だって、そうでしょう。\n
私のことが嫌いじゃなければ、あそこまで素っ気なく追い払うかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の人は余所者に好意的だ。\n
それに馴染んではいけないと思いつつ、その反応が普通だという意識も芽生えていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰にでも好かれるなんて、最初は気持ち悪いとさえ思っていたのに。\n
慣れとは恐ろしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "当然ではなかったことがいつからか当たり前になってしまって、その秩序が乱れると不安になる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "傲慢な考えが馴染むようで、少し、怖くなった。"

hide jo_t_01_1
show jo_t_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0072
White_Joker "「ふふ、それは誤解だよ、[firstname]。\n
ジョーカーは君のことが嫌いなわけじゃない」"

hide jo_t_03_14
show jo_t_03_19 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0073
White_Joker "「むしろ、気に入られているんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「……あれで？」"

hide jo_t_03_19
show jo_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice jok_f0074
White_Joker "「うん。だって、俺も君のことを気に入っている。ということは、ジョーカーだって君のことを気に入っているに決まっているからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（またわけの分からないことを）"

hide jo_t_02_4
show jo_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice jok_f0075
White_Joker "「俺達は二枚同時に存在する同じカードだから、間違いないよ。\n
さあ、おいで」"

hide jo_t_02_6
show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice jok_f0076
White_Joker "「中からしか見えない、君だけのサーカスが待っているから」"

$ hi_mes()
hide jo_t_03_1


$ time_effect()##PLEASE MANUALLY ADJUST ME

play music cheerful_a_ali
pause .5
$ hi_mes()
$ show_mes("frame_gen_chara")
voice mat_f0024
Danin "「行くよ～っ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice nos_f0015
W "「いいわよーっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice mat_f0025
Danin "「せえの！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice nos_f0016
W "「せえの！」"

play sound se_0697
show t_jo1_3 onlayer master
with dis




$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「わっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぶんという風斬り音が真上から響いてくる。\n
客席とはまた違った視界。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもだったら観客席で遠目に見ている光景は、どこか遠い世界の出来事のようだったのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（すごい……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供達はまるで風船のように軽やかに空中を行き交い、真下にいる私に手を振る余裕さえある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は真下にいるせいで、その高さをますます実感してしまいそれどころではないというのに、子供達は少しも恐怖を感じていないようだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（だからって、下にネットも敷かないなんて、どんな練習をさせているのよっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに今までの公演中にもネットを敷いている様子はなかったが、観客がいない場で見せるにはあまりに危険すぎる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "技術と自信を得るための練習なのに、失敗すると怪我ではすまないかもしれない……、そんなことでは命がいくつあっても足りない。"

hide t_jo1_3

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「あ、危ないっ。\n
落ちちゃう！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「片足だけでぶら下がっているのに、あの子を受け止めるなんて無茶よ！」"


show jo_t_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jok_f0077
White_Joker "「平気だよ、ほら」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "空中を飛んできた少女がぶつかった瞬間、少年は片手だけでその身体を支えてしまった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その上、彼の身体を伝って、少女がブランコの上に立つ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あまりの早業に声も出ない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0078
Mask "「けっ、あれくらい朝飯前だろ。\n
あいつらはこれが役割なんだぜ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0079
Mask "「間抜け面がますます間抜けに見えるから、口を閉じろよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「あなた、引っ込むんじゃなかったの？」"

hide jo_t_03_14
show jo_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice jok_f0080
White_Joker "「なんだい、ジョーカー。\n
やっぱり君も気になるんだったら、出てくればいいのに」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice jok_f0081
Mask "「はっ……。\n
誰がこんな馬鹿の近くになんているかよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「馬鹿って……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（いや、確かに賢いとはいえないかもしれないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "はっきりとした目的もないまま、このサーカスに居続けていること自体、賢いことではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "滞在地以外で過ごすなら、ここ以外に他にもいくつかの候補地があったはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（本当に、なんでここに来ちゃったのかしら）"

hide jo_t_01_1
show jo_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
White_Joker "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「なに？\n
あ……！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちょっと視線を逸らしている間に、二人は動きを止めていた。\n
不満そうに舞台にいる私を見下ろして。"

hide jo_t_01_7
show j-boy_a_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0026
Danin "「……空中ブランコじゃ物足りなかった？」"

hide j-boy_a_12
show j-boy_a_12 at left
show j-girl_a_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0017
W "「やっぱり綱渡りのほうがよかったのよ。\n
だから言ったじゃない」"

hide j-girl_a_9
show jo_t_02_5 at center
hide j-boy_a_12
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0082
White_Joker "「ははは、ごめんごめん、ジョーカーが話しかけてきたから、気が逸れたんだよ。\n
ほら、そんなところで睨み合っていないで、こっちに下りておいで」"

hide jo_t_02_5
show j-boy_a_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0027
Danin "「うん、分かった」"


show j-boy_a_1 at left
hide j-boy_a_1
show j-girl_a_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0018
W "「ジョーカー、次は絶対に綱渡りをやらせてよ。\n
ジョーカーも、今度は邪魔をしちゃ嫌よ」"

hide j-boy_a_1

hide j-girl_a_5

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "するすると天井から垂れ下がるロープを伝って、二人は軽々と舞台へと下りてきた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……この子達、どうしてこんなに私のことを見ているのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "好奇心というのなら分かる、今までにも何度も受けた眼差しだからだ。\n
しかし、彼らのそれは興味というよりも、期待の眼差しに近い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とても一生懸命に見える。\n
まるで……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（本気で私を連れて行きたがっているような……、そんな気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこまで好かれるようなこともしていないし、そもそも私がサーカスの団員になんてなれるわけがないのに……。"


show jo_t_02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0083
White_Joker "「うーん……、どうしようか。\n
[firstname]、君は何がしてみたい？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「…………。\n
は？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「何がしてみたいって、どういう意味よ？」"

hide jo_t_02_15
show jo_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0084
White_Joker "「どういう意味も何も、言葉の通りだよ。\n
君は何がしてみたい？」"

hide jo_t_02_12
show jo_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0085
White_Joker "「空中ブランコ、綱渡り、猛獣使い……。\n
何でもやりたいものをやらせてあげるよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（何でそういう話になった！？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ジョーカー、私、サーカスの体験入門に来たわけじゃないんだけど？」"

hide jo_t_03_7
show jo_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice jok_f0086
White_Joker "「いいじゃないか。\n
見ているだけなんて退屈だろう？」"

hide jo_t_01_11
show jo_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice jok_f0087
White_Joker "「団員以外入れない舞台にまで上がったんだから、何か一つぐらい身に付けていけばいいじゃない。\n
何が似合うかな？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーの問いかけに、子供達はうきうきしながら手をあげている。"

hide jo_t_01_5
show jo_t_01_5 at left
show j-boy_a_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0028
Danin "「もちろんブランコだよ、僕が絶対に受け止めてあげるからっ」"

hide jo_t_01_5
show jo_t_01_5 at left_center
hide j-boy_a_4
show j-boy_a_4 at center

show j-girl_a_9 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0019
W "「何を言っているのよ、今度は綱渡りだって言ったじゃない。\n
最初にやるならそっちよ」"

hide jo_t_01_5
show jo_t_01_3 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0088
White_Joker "「ははは、人気者だね、[firstname]。\n
ここまでうちの団員が誘うなんて、滅多にないんだよ」"

hide jo_t_01_3
show jo_t_03_1 at center
hide j-boy_a_4
hide j-girl_a_9
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0089
White_Joker "「どう、少しはやってみる気になったんじゃない？」"

menu:
    "やめておく。":
        jump fushigi_joker1_2a
    "少しなら、やってみる。":
        jump fushigi_joker1_2b

label fushigi_joker1_2a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「そもそも、参加するなんて言っていないでしょう。\n
それに、私はあなた達みたいな真似なんか出来ないわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の人間、特に役持ちと呼ばれる人間の身体能力は、もはや異常なレベルだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほど空中ブランコを披露した彼らは役持ちではないが、あれだけの動きを可能としているのは日頃の練習によるものだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（一朝一夕どころか、見様見真似で出来るようなことじゃないわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "プロとしてそれを生業としている人間に対しても、それは失礼なことに当たる。"

hide jo_t_03_1
show jo_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0090
White_Joker "「そんなことないよ、やってみれば意外とうまくやれるさ」"

hide jo_t_03_2
show jo_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0091
White_Joker "「それに、[firstname]、サーカスは一人じゃ出来ない。\n
仲間がいて、初めてうまくいくんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……それでも無謀すぎるわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（運動神経が極端に悪いほうじゃないけど、チャレンジしようなんて思えないもの）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0092
Mask "「おっ、少しは分をわきまえているじゃねえか。\n
そうだ、そうだ、おまえみたいにいかにもどんくさそうな女には、向かねえよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0093
Mask "「出来ねえって分かるだけ、少しはマシだったな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（この仮面、一発ぶん殴ったら少しはすっきりするかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口の悪いジョーカーは一体私を何だと思っているのか。"

hide jo_t_01_11
show jo_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0094
White_Joker "「ジョーカーにここまで言われて、それでもやらないの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

hide jo_t_03_13
show jo_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice jok_f0095
White_Joker "「ふふ、悔しくない？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（この人も私の心が読めるのかしら。\n
それとも、私、よっぽど分かりやすい顔をしているのか）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……{size=+20}やるわ{/size}」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice jok_f0096
Mask "「は！？何言っているんだよ、この～～\n
～～～女っ！\n
おまえに出来るはずがねえだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「最初から決めつけられていると、頭に来るのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "チャレンジしたいなどという前向きなものではなく、見返してやりたいと思うあたり、いかにも私らしい発想だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（乗せられている気がするけど……、少しは反撃してやりたいもの）"

hide jo_t_02_6
show jo_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice jok_f0097
White_Joker "「ふふ、そう来なくちゃ」"

$ hi_mes()
hide jo_t_02_11


scene circus
with stripe_l_medium

scene map_bg_joker_day
with stripe_l_long
##endmemory
jump fushigi_joker_2 ## I think
label fushigi_joker1_2b:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（嫌だって言っても……、あっさり引いてくれそうにはないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "残念なことに、この世界の住人がどれほど人の話を聞かないかは、今までの経験上嫌というほど分かっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーも、拒否したところで簡単に引いてくれるような性格はしていないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（まあ、いいか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "滞在地を出て、どこかに行かなければいけないと最初から決まっていたわけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "せっかくサーカスに来たのだから、それらしいことをしてみるのも悪くはない。"

if renpy.seen_label("fushigi_joker1_memory") == True:
        jump fushigi_joker1_4
if place_of_stay == "Castle":
    jump fushigi_joker1_3b
if place_of_stay == "Hatter":
    jump fushigi_joker1_3a
if place_of_stay == "Amuse":
    jump fushigi_joker1_3a
if place_of_stay == "Tower":
    jump fushigi_joker1_3b

label fushigi_joker1_3a:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（少しぐらい心配させたほうが、いい薬かも）"

jump fushigi_joker1_4
label fushigi_joker1_3b:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（反省しに来たのに、サーカスにいるっていうのも変な話だけど……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（でも、少なくとも、エイプリル・シーズンは終わったんだし、おおごとにはならないはずよね）"

jump fushigi_joker1_4
label fushigi_joker1_4:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「少しなら試してもいいけど……。\n
危なくないもの限定で」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jok_f0098
Mask "「はあ！？\n
おまえ、やれるのかよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jok_f0099
Mask "「無理無理、やめておけって。\n
怪我したって、うちじゃ責任はとらねえぞ」"


show jo_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jok_f0100
White_Joker "「ジョーカー、最初から怪我を前提に話してどうするんだよ。\n
怪我をさせないようにするのが、俺達の役目だろう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jok_f0101
Mask "「ふざけんなよ。\n
こんな鈍そうな女のお守りなんて、俺はごめんだぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……私もあなたに面倒を見てもらおうなんて思っていないわよ」"

hide jo_t_03_4
show jo_t_03_4 at left
show jo_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice jok_f0102
Black_Joker "「ほう、言いやがったな、この～～～～女」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "売り言葉に買い言葉。\n
言い返すと、先ほど姿を消したはずのブラックさんが現れた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……消えたり、出てきたり、慌ただしいわね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（落ち着きがないのは、あなたも同じじゃない）"

hide jo_t_03_4
show jo_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0103
White_Joker "「ふふ、仲がいいなあ。\n
[firstname]、ジョーカーとそんなに仲がいいなんて、意外だよ」"

hide jo_t_01_10
show jo_t_01_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0104
White_Joker "「ちょっと……、妬いちゃいそうだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私と睨み合っていた彼の前に、もう一人のジョーカーが割り込んでくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ジョ、ジョーカー！！？」"

hide jo_t_01_9
show jo_t_03_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice jok_f0105
White_Joker "「冗談だよ、冗談。\n
さて、[firstname]」"

hide jo_t_03_8
show jo_t_03_19 at left
hide jo_t_02_8
show jo_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice jok_f0106
White_Joker "「君は何に挑戦するのか、もう決めたかな？\n
早く決めないと、俺が勝手に決めちゃうよ」"

$ hi_mes()
hide jo_t_03_19

hide jo_t_02_8
with dis

scene circus
with stripe_l_medium

scene map_bg_joker_day
with stripe_l_long
##endmemory
jump fushigi_joker_2 ##I think
