
scene map_bg_winter_day
with dis
label fushigi_end_julius_ace1:
$ clockanim()


scene map_bg_winter_day
with dis

scene charasel_bg_tower_day
with dis

play music tower_room1_p_ali

scene ts_01
with Dissolve(1.2)
play sound se_0590 volume .85
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "階段を上る音。"


show yuri_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（この足音は……）"

play sound se_0701 volume .85
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、豪快に転ぶ音。"

hide yuri_t_01_4
show yuri_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0370
Julius "「はあ。\n
まったく、誰が来たのかすぐ分かるな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「ふふ、そうね。\n
あれだけの勢いで昇ってきて、一気に転げ落ちる人なんてそうそういないもの」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（他の人なら、あの勢いで転んだら大怪我をしてしまうだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計塔ほどではないにしろ、クローバーの塔にも階段は多い。\n
その階段をバタバタと走り回る人は、彼を置いて他にはいない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔の職員が走り回る理由は、脱走した領主を捕らえるときと相場が決まっているし、その領主、ナイトメアがこの部屋に来ることは稀だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（だからこそ、見つからずに一服なんかしていられたんだろうけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小火騒ぎを思い出して、私は溜息をついた。"

hide yuri_t_01_13
show yuri_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0371
Julius "「五時間帯前に呼び出したんだが……、あいつにしては早いな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「珍しいこともあるわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースの迷い癖は、既に一種の才能といえる。\n
ユリウスによると、呼び出した時間帯に、平均で十時間帯は遅れてくるらしい。"

hide yuri_t_03_10
show yuri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0372
Julius "「……逆に厄介ごとを持ち込んでこなければいいんだがな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しみじみとした声には、実感がこもっていた。"

play sound se_0590 volume .85
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "再び階段を上る音。"

hide yuri_t_02_11
show yuri_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0373
Julius "「来たか」"

play sound se_0273

show t_end_yuri_ace1 onlayer master
with dis

play music gag2_a_ali
hide yuri_t_02_10

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0535
Ace "「やあユリウス、久し振り！\n
元気だった？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0374
Julius "「ぶ！！！\n
げふ、ごは……っ、エ、エース、なんだ、その格好は！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ノックをするという常識は記憶の彼方であろうエースが、勢いよく部屋に入ってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その姿に、私とユリウスは思わず目を見開いた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0536
Ace "「何って、ユリウスの忘れ物だろう、これ？\n
俺、親友の大事な忘れ物をちゃんと届けに来たんだぜ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0375
Julius "{size=+20}「ありがた迷惑だ！！」{/size}"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（なんて言うか……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（サングラスにあの格好っていうのも、相当な不審者だったけど。\n
あの仮面まで付くと、ただの変質者になるのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "わざわざ証明されなくてもいいことだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "変装をしたユリウスが不審者。\n
ちょっとだけ変えたエースは変質者。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "{size=+20}（どうしよう、友達をやめたくなってきた）{/size}"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今更やめられるはずはないが、ここまで友達をやめたいと思う機会はなかなかない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0537
Ace "「えー。\n
ペーターさんや陛下がすぐに捨てろって言ったのを、せっかく回収して届けに来たのに」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0538
Ace "「この子には甘いくせに、俺には冷たいよなあ、ユリウス。\n
男女差別なんて酷いことするぜ、はははは」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0376
Julius "「いいから、とっとと用件をすませて出ていけ！\n
おまえの仕事は、そのコートとマフラーを届けることではないだろう！？」"

hide t_end_yuri_ace1
show t_end_yuri_ace2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0539
Ace "「うん、仕事の話を聞きに来たんだ。\n
当たり前だろう、俺、こっちの仕事には手を抜かないよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "（こっちの仕事、ね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さらりと告げてはいるが、エースはハートの城の騎士。\n
時計屋であるユリウスの元で働くのは、本来であれば有り得ないことだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（でも、ここにいるときのエースのほうが落ち着いて見える）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice jul_f0377
Julius "「……手を抜くとは思っていないが、完了するのがいつになるか不安だな。\n
次の仕事はここだ、あまり余計なところに行くんじゃないぞ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice ace_f0540
Ace "「ああ、分かっているよ。\n
なるべく早く片付けてくるつもりだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice jul_f0378
Julius "「……おまえのは、いつも、つもり止まりだろう。\n
達成されたことはほとんどない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice ace_f0541
Ace "「ははは。でも、ほとんどってことは、ゼロじゃない。\n
今回は、その稀なケースに当てはまるかもしれないじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城だけではない。\n
この部屋のドアから一歩外に出た、クローバーの塔でも駄目だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城の騎士は、時計塔の主と共にいるときが、一番彼らしく見える。"

hide t_end_yuri_ace2
show t_end_yuri_ace3 onlayer master
with dis

play music ace_t_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「……？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0542
Ace "「どうしたんだ、[firstname]？\n
俺の顔に何か付いている？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「そういう訳じゃないけど……。\n
ユリウスとエースって仲がいいなと思っただけ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（私では入り込めない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それを寂しく思ったこともあるが、今は少し違う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（それに……、ユリウスの代わりにエースとの間に入れって言われても、無理）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だから駄目なのではない。\n
この世界では誰でも代えがきくと言うが、エースにとってユリウスの代わりは存在しない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（エースに言ったら、きっと否定されるんだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0543
Ace "「当たり前だろう。\n
友達とは仲よくしなくちゃね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「友達……、ね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（それだけじゃないでしょう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心の中で聞いてみるが、このおかしな男がそう捉えているのなら、私が口を挟むことではないのだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0544
Ace "「ああ、もちろん。\n
君もそうじゃないか、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「私があなたの友達なの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0545
Ace "「そうだよ。\n
君だって、俺の友達だよね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（友達）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "否定する材料はない。\n
ハートの城に滞在している間、私達はまさに友達として交流をしていたはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（なのに……。\n
なんでだろう、自分で言っても気にならないのに、エースが言うと酷く胡散臭く聞こえる）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「そうね、たしかにあなたとは友達だけど……」"


scene bg_gen_sky_win_day
with dis
hide t_end_yuri_ace3

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "{size=+20}「いい加減、その変装はやめてくれないかしら。\n
友達をやめたくなるから」{/size} "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice jul_f0379
Julius "「こいつの意見に賛成だ。\n
いいから早くいつもの格好に戻れ」"

play sound se_0067

scene ts_01
with dis

show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice ace_f0546
Ace "「あ、そうだ、ついでにこれを届けに来たんだっけ。\n
君にあげるって約束をしていただろう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一通り遊びつくしたとでもいうように、エースは普段の騎士服に戻った。\n
それから上着のポケットから何かを取り出し、私に差し出してくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「私に？」"

play sound se_0262
hide ace_t_03_11


scene t_cut_end_yuri_ace1u
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「！\n
これ……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あなたが作っていたピアス？」"


scene t_cut_end_yuri_ace1
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "原石から削りだした石は、きらきらと光っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、以前エースが見せてくれたときには金具が付いていたはずなのに、今は曲がっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（曲がっちゃった？\n
それとも、壊そうとしたのかしら？）"


show ace_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice ace_f0547
Ace "「うん、君にあげようとしていたピアスなんだけど……」"

hide ace_t_03_1
show ace_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice ace_f0548
Ace "「あー、さっき階段から落ちたときに、曲がっちゃったんだな、ぼろぼろだ。\n
やっぱりこういうのは、手先が器用なやつが作るのが一番だよな」"

hide ace_t_02_2
show ace_t_02_2 at left
show yuri_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice jul_f0380
Julius "「……なんで、そこで私を見るんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "作業台に座ったまま私達のやりとりを見ていたユリウスが、つまらなそうに口を開いた。"

hide ace_t_02_2
show ace_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0549
Ace "「ん？俺はまだ何も言ってないぜ、ユリウス。\n
ただ、ユリウスだったら手先が器用だとは思っているけどさ」"

hide yuri_t_02_10
show yuri_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0381
Julius "「……何が哀しくて、他の男からの贈り物を作り直してやらなければいけないんだ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひくひくとユリウスの口元が震えている。"


scene ts_01
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（まあ、気持ちは分かるわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手作りのプレゼントを贈るのに、友達の力を借りるのならまだいい。\n
だが、贈る相手がその友達の恋人では、喧嘩を売っているのと変わらないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（その上、腕っ節の強さじゃ、確実に負けているし……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城であっさりと返り討ちにあったのは、まだ記憶に新しい。"


play music gag2_a_ali
hide ace_t_02_10
show ace_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0550
Ace "「え……、ユリウス、そんなに俺からのピアスが欲しかったのか！」"

hide ace_t_01_3
show ace_t_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0551
Ace "「俺、ユリウスのことは好きだけど、そういう方向での好きとはちょっと違うんだよなあ。\n
親友の思いに応えられなくて、ごめんな」"

play sound se_0579
play sound se_0212
hide yuri_t_02_7

camera at hpunch
camera at vpunch

show yuri_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「～～～～っ！！！！」"

hide yuri_t_02_11
show yuri_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0382
Julius "「～～～～っ、エース！！！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "机に頭を盛大にぶつけたユリウスとは対照的に、エースはわざとらしく溜息なんかついている。"

hide ace_t_03_7
show ace_t_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0552
Ace "「……はあ、こういう場合、女の子を男二人が取り合うっていう構図ならまだいいんだけどな」"

hide ace_t_01_6
show ace_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0552_5
Ace "「[firstname]、俺、君とユリウスに奪われあうなんて、騎士らしくないと思うんだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「…………。\n
私のことは気にしないで、二人で仲よくしたら？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悪乗りしたエースに付き合って冗談で言うと、ユリウスは顔色を変えた。"

hide yuri_t_03_7
show yuri_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0383
Julius "「[firstname]、おまえ……！\n
私にそういう趣味はないし、私が好きなのは、その……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "立ち上がってみたものの、言葉がうまく出ずに口をぱくぱくさせているユリウスを見ていると、さすがに気の毒になってきた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（これ以上からかったら、ユリウスが風船みたいに弾けちゃいそう）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「エース。\n
そろそろユリウスが本気にしそうだから、やめておきましょう」"

hide ace_t_01_5
show ace_t_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice ace_f0553
Ace "「ははは、それもそうだな。\n
ユリウスって本当に騙されやすいっていうか、乗せやすいよなあ」"

hide yuri_t_03_3
show yuri_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice jul_f0384
Julius "「……おまえ達、私をからかっていたのか！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あっけらかんと笑ったエースと、私の様子にユリウスはしばらく呆然としていたが、立ち直るのも早かった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "わざと厭味な笑みを浮かべると、私とエースを交互に見てくる。"

hide yuri_t_02_3
show yuri_t_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0385
Julius "「いや、私などよりずっと、おまえ達のほうが仲がいいだろう。\n
そんなに馬鹿な話がしたいのなら、勝手にしろ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あら、拗ねているの、ユリウス？」"

hide yuri_t_03_1
show yuri_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice jul_f0386
Julius "「誰が拗ねるか。\n
私は仕事があるんだ、くだらないことに付き合う暇は……」"

hide ace_t_01_4
show ace_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice ace_f0554
Ace "「そうか、彼女がいない間、ずっと一人だったもんな。\n
寂しかったんだよな、うん、じゃあそんなユリウスには、これをあげるよ」"


play music tower_room1_p_ali
play sound se_0273
camera at vpunch

hide ace_t_03_11

hide yuri_t_01_9


scene t_cut_end_yuri_ace2u
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice jul_f0387
Julius "「……なんだ、これは？」"


scene t_cut_end_yuri_ace2
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いきなり自分の作業台に現れた大きな石に、ユリウスが怪訝な顔をする。"


show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0555
Ace "「石だよ。\n
正確に言えば、宝石の原石」"

hide ace_t_03_3
show ace_t_03_3 at left
show yuri_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0388
Julius "「そんなことは見れば分かるが……。\n
どうして、そんなものがここに出てくるんだ」"

hide ace_t_03_3
show ace_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0556
Ace "「だって、俺のピアスは直してくれないんだろう？\n
だったら、幸い材料は沢山あることだし、ユリウスがこの子に作ってやれよ」"

hide yuri_t_03_2
show yuri_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0389
Julius "「な……、おまえ、これで作れと言うのか！？\n
原石なんて、取り扱いが一番面倒なんだぞ！！」"

hide yuri_t_03_3
show yuri_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0390
Julius "「削り出すだけならともかく、研磨もあるようなものを」"

hide ace_t_02_10
show ace_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0557
Ace "「うん、でも、俺はやったよ。\n
好きな子のためならそれぐらいの苦労は何でもないもんなあ、ははは」"

play sound se_0449
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぽん、と軽く肩を叩かれ、ユリウスは反論する言葉を失う。"

hide yuri_t_02_7
show yuri_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「……っ」"

hide ace_t_02_4
show ace_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0558
Ace "「大丈夫だよ、結構柔らかい石だから、ユリウスなら削るのも得意そうだし」"

hide yuri_t_02_3
show yuri_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0391
Julius "「そういう問題ではないと言っているだろうが……」"

hide ace_t_03_3
show ace_t_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0559
Ace "「それじゃあ、俺、そろそろ仕事に行ってくるぜ。\n
次に報告に来たときには、完成品を見せてくれよな！」"

play sound se_0284
hide yuri_t_03_13
show yuri_t_03_13 at center
hide ace_t_01_4
with dis

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

hide yuri_t_03_13
show yuri_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「嵐のように現れて、嵐のように出て行ったわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアから出て行った騎士を見送り、息をつく。"

hide yuri_t_03_11
show yuri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0392
Julius "「本当だな、あいつめ……、こんなもの置いて行って、嫌がらせか！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計のパーツが広がるユリウスの机の上には、今や大きな石が鎮座している状態だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（とりあえずどけないと仕事にもならないわよね）"

hide yuri_t_01_8
show yuri_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice jul_f0393
Julius "「はあ、これでは作業の邪魔になる。\n
どかさないと……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「結構重そうだけど、ユリウス一人で大丈夫？」"

hide yuri_t_01_13
show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0394
Julius "「私だって男だ、これぐらい持てないはずが……」"

play sound se_0055
hide yuri_t_03_9
show yuri_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0395
Julius "「も、持てないはずが……、な……」"

play sound se_0784
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "石を持ったユリウスは、明らかに無理をしている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ユリウス、下ろして、下ろして！！足下ふらふらしているから！！\n
そのまま無理に持ったら、ぎっくり腰になっちゃうわよ！」"

play sound se_0273
camera at vpunch

hide yuri_t_02_8
show yuri_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jul_f0396
Julius "「はあ、はあ……、～～～～、くっ。\n
なんであいつはこれを片手で持てるんだ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何とか原石を元の位置に戻したユリウスの顔は苦かった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「元々の身体のつくりが違うんじゃないかしら、エースはほら、よく出歩いているし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、よく出歩いているというようなレベルではない。\n
歩きすぎだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……というか、エースは色々規格外すぎる。\n
インドアなユリウスじゃ、比較するのも厳しいわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結局、作業台の上に石は置かれたままだ。\n
震える手をさすりながら、ユリウスはぼそぼそと口を動かした。"


scene ts_01
with dis

play music transparent1_a_ali
hide yuri_t_02_7
show yuri_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0397
Julius "「……私のことを情けないと思っているんだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「そんなことないわよ。\n
ユリウスにはユリウスのいいところがあるもの」"

hide yuri_t_03_12
show yuri_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Julius "「[firstname]……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「この世界に、あなた以上に手先が器用な人なんていないわ。\n
私には出来ないから羨ましいし、本当にすごいと思っているのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の器用さは誰にでも誇れるものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（少なくとも、私にはないものだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "特別なものは心臓だけ。\n
誰かの役に立つことなんて出来ない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「私はユリウスの手が好きよ。\n
触るのも、好き」"

hide yuri_t_03_2
show yuri_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_8")
voice jul_f0398
Julius "「……はあ。\n
おまえといると、真面目に落ち込んでいるのが馬鹿馬鹿しくなる」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう呟いて、ユリウスが私を抱き寄せる。\n
それから、ちらりと作業台を見やって、口を開いた。"

hide yuri_t_01_13
show yuri_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0399
Julius "「……作ってやる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ユリウス？」"

hide yuri_t_01_6
show yuri_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0400
Julius "「こんな原石が作業台にあったら邪魔だからな。\n
ピアスでもなんでも、作ってやると言っているんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "皮肉に聞こえる言葉は、照れ隠しだと知っている。\n
だからこそ、思わぬ台詞に嬉しくなった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（エースは、こういうユリウスの性格を理解していたってことよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相変わらず真意を読ませなかった方向音痴な友人は、私よりも彼を知っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（やっぱり、ちょっとだけ悔しい）"

hide yuri_t_03_13
show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jul_f0401
Julius "「それに、おまえの言うことにも一理ある」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「何が？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "間近にある顔との距離がじわじわと縮まっていく。"

hide yuri_t_03_9
show yuri_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0402
Julius "「あれが持てなくても、おまえを抱えることに苦労はしない。\n
それでいいのかもしれない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_19")
T "「……ええ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスがいて、エースがこの場所の空気を掻き回す。\n
私はそれを見ながら、どっちつかずで、騒動に巻き込まれていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_13")
T "（……すごく自然で、楽しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が一緒にいるからこそ、愛しいと思える騒動があることを、私達はきっと知っている。"

hide yuri_t_01_2 with dis
hide ali_t_06_16
hide frame_gen_togaki
with Dissolve(5)


show black with Dissolve(5)

$ renpy.movie_cutscene("endroll_b.mpg")
#return
