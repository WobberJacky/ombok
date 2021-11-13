
scene map_bg_summer_day
with dis

scene charasel_bg_amuse_day
with dis
label fushigi_gowland1:
hide screen amuse_man_choice
$ clockanim()


scene bg_gen11_yuy_sum_day
with dis

play music gowland_t_ali

scene yug_01 with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0218
Gowland "「その……、[firstname]。\n
入ってもいいか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「どうぞ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分で聞いていても、無愛想な声だ。\n
恐らく、ドアの向こうにいるゴーランドには、もっと冷たく聞こえていることだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（今回ばかりは、私だって怒っているんだから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これがいつものじゃれあいだったら、ここまで腹を立てたりはしない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に私の常識が通じないことも分かっている。\n
世界が合わないのなら、自分が合わせるしかないのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし……。"

play sound se_0284
pause .4

show go_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0219
Gowland "「[firstname]。\n
悪い、さすがに悪ふざけがすぎたよな」"

hide go_t_03_7
show go_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0220
Gowland "「せっかく立ててくれたあんたの案を蔑ろにしたわけじゃなかったんだが……、その、つい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋にやってきたゴーランドは、失敗したと顔に大きく書いていた。\n
反省しているのが、十分伝わってくる様子だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……そうよ、何を考えているわけ？\n
せっかくいい出来だと思ったのに……、提案も出来ずに駄目にされたんだからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_11")
T "「私が怒るのって、そんなにおかしいことかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベッドの上に座ったまま睨み付けると、ゴーランドは自分の頭に手を添えながら、困った顔を見せる。"

hide go_t_02_5
show go_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0221
Gowland "「す、すまねえ……。\n
動物相手に音楽を説くのは、困難だって分かってはいたんだが……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「そういう問題じゃないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（音楽一筋なのは分かるけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドは、少なくとも、居候である私にとって大きな問題のない人だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大抵のことには寛容だし、子供のような柔軟な発想も持ち合わせている。\n
だが、音楽が絡むと、急に拘りが強くなってしまう。"

hide go_t_03_2
show go_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0222
Gowland "「ボリスもピアスも、耳は悪くないんだから、ちゃんとした音楽を聴けばもう少し感性がよくなると思うんだが」"

hide go_t_01_7
show go_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0223
Gowland "「俺がとっておきの演奏を聞かせてやろうとすると逃げ出すからな……、まったく、こんなところだけ遠慮深い奴らだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（それは、遠慮じゃなくて、生命の危機を感じて避難しているだけだと思う）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だって同じことをされたら、全力で逃げる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの演奏と歌に真っ正面から向き合う勇気など、誰が持ち合わせられるだろうか。"

hide go_t_03_1
show go_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0224
Gowland "「何はともあれ、あんたには悪いことをした。\n
今度はちゃんと、真剣に、全力で考えるから……、その、なんだ」"

play sound se_0267
hide go_t_02_2
show go_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0225
Gowland "「許してくれないか？\n
この通りだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ゴーランド……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地のオーナー。\n
帽子屋、ハートの女王と並ぶ有力者が、私に頭を下げてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "実力も何も持たない、こんな小娘一人に。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ゴーランドも、反省しているみたいだし……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒りをずっと保ち続けるのもなかなか大変だ。\n
それも、冷めたところのある私なら尚更というもの。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「……まあ、ちゃんと分かってくれたのなら」"

hide go_t_03_7
show go_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gor_f0226
Gowland "「ああ、反省している。\n
本当に悪かったと思って」"

play sound se_0273
pause .7
play sound se_0553
play sound se_0007
camera at hpunch
camera at vpunch
pause .7
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "和解しかけた途端、ドアが開いて、ドサッと人がなだれ込んでくる。"


play music gag2_a_ali

show bor_t_01_1 at center
hide go_t_03_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0165
Boris "「うわわ、おまえら。\n
後ろから押すなよ！」"

hide bor_t_01_1
show bor_t_01_1 at left
show pia_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0110
Pierce "「むぎゅ……！\n
つ、潰れるーっ」"


show go_t_03_11 at center
hide bor_t_01_1
hide pia_t_02_10
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「何やっているの、あなた達？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋にやってきたのは、ボリスとピアス、そして……。\n
お揃いのジャケットに身を包んだ、従業員の同僚達。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（まさか、ずっと聞き耳を立てていたわけ……？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「ボリス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一番初めに入ってきた相手に視線を向け、説明を求めた。"

hide go_t_03_11


show bor_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0166
Boris "「いや、ほら……。\n
おっさんがちゃんと説得出来なかったら、そのときは俺が頑張らなきゃと思って」"

hide bor_t_03_11
show bor_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0167
Boris "「そうしたら、何だか知らないうちにこいつらが……。\n
ピアス、おまえもだっ、勝手について来やがって」"

hide bor_t_01_4
show bor_t_01_4 at left
show pia_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0111
Pierce "「ええー、ボリス、ずるいよ。\n
オーナーさんが失敗したら、自分がおいしいところ持っていこうとしていたじゃないか」"

hide pia_t_01_4
show pia_t_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0112
Pierce "「自分だけずるい！\n
ずるい、ずるい！！」"

hide bor_t_01_4
show bor_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0168
Boris "「ピアス、おまえなあ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼らの上にのしかかっている従業員も口を揃えて言う。"

hide bor_t_03_3

hide pia_t_03_9
show pia_t_03_9 at left
show yuuen_man_01_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0017
Employee "「そうです、そうです！\n
自分だけいいところを見せようなんて、ずるいですよ」"

hide pia_t_03_9

hide yuuen_man_01_05
show yuuen_man_01_05 at left
show yuuen_woman_02_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0035
Employee "「それにオーナーは、今ひとつ押しが足りないんですから、ここは皆で押さないと！」"

hide yuuen_man_01_05
show yuuen_man_02_01 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0018
Employee "「そういうことです！」"

hide yuuen_man_02_01
hide yuuen_woman_02_05
show go_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0227
Gowland "「お、おまえらな……。\n
俺を何だと思っているんだ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（信頼されているんだろうけど……。\n
敬われてはいないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこかの塔の領主が聞いたら、あからさまに「尊敬されていない」と主張してきそうだ。"

hide go_t_02_1
show go_t_02_1 at left
show bor_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0169
Boris "「だって……、なあ？\n
おっさん一人に任せておくのは、やっぱり心配だし」"

hide go_t_02_1
show go_t_02_1 at left_center
hide bor_t_02_2
show bor_t_02_2 at center
show pia_t_03_11 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0113
Pierce "「でも、ボリスは、チャンスだって言っていたよね？\n
俺、ちゃんと聞いていたんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "従業員の下敷きになったまま、ピアスはにこにこと口を挟んだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "アピールするように大きな耳を動かすネズミの顔はどこか自慢気でさえある。"

hide go_t_02_1
show go_t_03_6 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0228
Gowland "「おまえら……。\n
人を扱き下ろしやがって……！」"

play sound se_0515
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ゴ、ゴーランド！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃を構えた相手に慌てて声を上げるが、頭に血が上った彼に私の声は届かなかった。"

hide go_t_03_6
show go_t_01_9 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0229
Gowland "「そもそも、書類を駄目にしたのは、おまえらがいらねえ茶々を入れたせいだろうが！\n
おまえらだって謝れ！」"


play music gag3_a_ali
play sound se_0522
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の部屋の中で大型銃を取り出したゴーランドは、ためらいなく引き金を引いている。"

hide bor_t_02_2
show bor_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0170
Boris "「うわ、わっ……と！\n
危ないだろうが、おっさん！」"

hide bor_t_01_1
show bor_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0171
Boris "「俺やピアスならまだしも……、危ないって！！」"

play sound se_0522
$ flash(.2)
hide pia_t_03_11
show pia_t_02_6 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0114
Pierce "「ぴ、ひゃっ！\n
オーナーさん、撃たないでってばっ！！」"

hide go_t_01_9
show go_t_03_6 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0230
Gowland "「うるせえ、いいところで邪魔しやがって！」"

hide go_t_03_6

hide pia_t_02_6

hide bor_t_01_4

play sound se_0522
$ flash(.2)
play sound se_0522
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（またこの繰り返し）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「ゴーランド、いい加減に」"

play sound se_0119

show pia_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice pie_f0115
Pierce "「うわわ、危ない、危ないよーっ！」"

hide pia_t_02_8

play sound se_0373
pause .5
play sound se_0701
camera at hpunch
camera at vpunch
pause 1
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃弾を避けようとしたピアスの尻尾が、私の机の上にあったものをひっくり返した。"

play sound se_0312
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他にも従業員の飾りが壁をひっかいたり、ボリスのファーが埃を落としたり。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "掃除が行き届いていたはずの部屋は、今やごちゃごちゃにかき乱されている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_9")
T "「…………」"


show go_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice gor_f0231
Gowland "「少し反省しろ、この～～～～～～ども\n
！！」"

play sound se_0522
$ flash(.2)
play sound se_0522
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（反省が必要なのは、あなたも同じでしょうが）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すっかり暴走モードに入ってしまったゴーランドを止めるのも、馬鹿馬鹿しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足下へところころと転がってきた（おそらく従業員が落としたのであろう）ボールを手に、狙いを定めた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「えい！」"

play sound se_0125
pause .5
play sound se_0309
hide go_t_02_9
show go_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice gor_f0232
Gowland "「いて！\n
な、何するんだ、[firstname]っ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「反省が足りないようだったから、当ててみたんだけど……。\n
一個じゃ、足りなかったかしら？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「ご希望なら、もう一ついかが？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "再び構えるようにボールを握った私を見て、ゴーランドは我に返ったらしい。"

hide go_t_03_7
show go_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0233
Gowland "「あ」"

hide go_t_03_3
show go_t_03_3 at left
show bor_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「[firstname]？」"

hide go_t_03_3
show go_t_03_3 at left_center
hide bor_t_01_11
show bor_t_01_11 at center
show pia_t_03_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Pierce "「……？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "動きを止めた彼らの視線は、私に集中している。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐らくは、先ほど彼らを止めたときと同じぐらい、いや、それ以上に引きつった表情を浮かべている私に。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「反省、しているのよね、ゴーランド？」"

hide go_t_03_3
show go_t_01_9 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice gor_f0234
Gowland "「あ、ああ！\n
勿論だとも！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "{size=+20}「これで？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋の中は、ボリスにピアス、従業員が駆け回ったせいで、ぐちゃぐちゃだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくらこの世界では汚れが勝手に消えるとはいえ……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の部屋をここまで荒らされれば、当然、収まりかけていた怒りも再燃しようというものである。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私はそれほど喧嘩っ早いほうではないが、何でも許せるほど善人ではない。\n
むしろ、その辺りは彼らと同じように子供っぽい。"

hide go_t_01_9
show go_t_03_2 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0235
Gowland "「これは、その……。\n
従業員教育の一環というか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「こんな傍迷惑な教育をしなくちゃいけないなんて、オーナー失格よ！」"

hide go_t_03_2
show go_t_02_4 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_13")
voice gor_f0236
Gowland "「うっ……。\n
か、返す言葉もない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_9")
T "「…………」"

play sound se_0456
hide go_t_02_4

hide pia_t_03_1

hide bor_t_01_11
show bor_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice bor_f0172
Boris "「あの、[firstname]？\n
荷物まとめて、一体、何を……？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「言ったでしょう、ついていけないって」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最低限の手荷物だけをまとめると、それを持って私は彼らの横を抜ける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「しばらくお休みを頂くわ。\n
その間、遊園地で何をしようが私は一切関わらないから、どうぞお好きに」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（皆で銃を撃ちまくろうが、危険なアトラクションを作ろうが、勝手にしなさい）"

hide bor_t_03_6
show bor_t_03_6 at left
show pia_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice pie_f0116
Pierce "「え、ええっ？\n
[firstname]、君も家出するの？」"

hide pia_t_01_3
show pia_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice pie_f0117
Pierce "「なら、俺もついていってあげ……、ちゅう！」"

play sound se_0373
camera at hpunch
camera at vpunch
hide bor_t_03_6
with dis
show bor_t_01_4 at center with Dissolve(.5)
hide pia_t_03_11 with Dissolve (.3)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice bor_f0173
Boris "「馬鹿ピアス！\n
これ以上、神経を逆撫でするようなこと言うんじゃないってっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の後ろを付いてこようとしたピアスは、ボリスに押さえ込まれて床に突っ伏した。"

hide bor_t_01_4
show pia_t_03_11 at left
show yuuen_man_01_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0019
Employee "「あ……。\n
俺達も、ちょっとふざけすぎちゃいましたか」"

hide pia_t_03_11

hide yuuen_man_01_03
show yuuen_man_01_03 at left
show yuuen_woman_01_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0036
Employee "「そうみたい。\n
あー、失敗しちゃったわっ」"

hide yuuen_man_01_03

hide yuuen_woman_01_04
show yuuen_woman_01_04 at left
show go_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「[firstname]……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しょんぼりと肩を落としたゴーランドの様子が気になったが、ここで甘い顔をすれば元の木阿弥だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（たまにはいい薬だわ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「それじゃあ、皆。\n
しばらくさようなら」"
play sound se_0399
hide yuuen_woman_01_04

hide go_t_03_7
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぱたん。\n
呆然とする彼らを残して、私はドアを閉めたのだった。"

$ hi_mes()

scene charasel_bg_amuse_day
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_long
play music map_summer_jok

scene bg_gen_sky_sum_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「さて、どこに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に住む友人は何人もいるが、しばらく滞在させてもらうことを考えると……。"

$ routechara = "Gowland"
$ show_mes("frame_gen_togaki")
T "Where do I want to visit?"
$ hi_mes()
show screen fushigi_map1
$ ui.interact()
