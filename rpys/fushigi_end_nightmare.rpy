
scene map_bg_winter_eve
with dis
label fushigi_end_nightmare1:
$ clockanim()


scene map_bg_winter_eve
with dis

scene charasel_bg_tower_eve
with dis

play music tower_stairs_down_p_ali

scene cki1_02
with Dissolve(1.2)

show toustaff_a1_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kat_f0030
Tower_Employee "「お帰りなさい！\n
お待ちしていました」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「皆……、久しぶり」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「突然抜けたりして、ごめんなさい。\n
悪いことしちゃったわね」"

hide toustaff_a1_2
show toustaff_a1_2 at left
show toustaff_b1_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice hos_f0056
Tower_Employee "「そんなことはないですよ。\n
息抜きだって必要ですし、休めるときには休んでくださいね」"

hide toustaff_a1_2
show toustaff_a1_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice kat_f0031
Tower_Employee "「そうですよ。\n
さすがに会合の時期だったら、縋ってでも留まってもらいますけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔の階段を上っている最中、顔を合わせた同僚はそんな冗談を言ってくれる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（受け入れられている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここには確かに私の居場所があるのだと、彼らの反応を見ていてそう感じた。\n
私にしか出来ない仕事なんて、この世界にもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（それでも、私が戻るのはこの場所）"

hide toustaff_b1_3
show toustaff_b1_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice hos_f0057
Tower_Employee "「ナイトメア様がお待ちですよ。\n
会いに行ってあげてください」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ、ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見送ってくれる彼らに背を向けて歩き出す。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ナイトメアにも会いに行くけど）"

play sound se_0636
hide toustaff_a1_1

hide toustaff_b1_9

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私にはその前に、どうしても会っておきたい人がいる。\n
彼らの言葉に曖昧な笑みで応えながら、階段を更に上へと上っていった。"

$ hi_mes()


scene cki1_02 with Dissolve(.8)
scene cr_01
with stripe_l_medium

scene ts_02
with stripe_l_long

play music quiet_night_a_ali
play sound se_0397

show yuri_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Julius "「…………」"

hide yuri_t_03_2
show yuri_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jul_f0165
Julius "「……戻ったのか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ、ただいま。\n
ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "久しぶりにやってきた時計塔にある、彼の仕事部屋。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "閉じこもりがちなユリウスがいないのでおかしいと思ったら、どうやら買い物に出ていたらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "買い物袋を手に自室に戻ってきた彼は、部屋の中で待っていた私を見て、不思議そうな顔をした。"

hide yuri_t_03_8
show yuri_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0166
Julius "「ああ、おかえり。\n
いや、そうではなくてだな……」"

hide yuri_t_01_13
show yuri_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0167
Julius "「おまえ、もうナイトメアには会いに行ったのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……ううん、これから行くところ。\n
でも、その前に……、あなたにちゃんと謝らなくちゃと思って」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉を一度切って、立ち上がる。\n
私よりもずっと高い位置にある顔を見上げて、それから頭を下げた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ごめんなさい」"

hide yuri_t_01_12
show yuri_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「時計も部屋も煤だらけにして……。\n
本当に、ごめんなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計塔とドア一枚で繋がってしまったこの部屋は、彼にとっては唯一自分の領土と言える場所。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その上、何よりも時計屋としての仕事に殉じる彼の仕事が中断するなど、本来ならばあってはいけない事態だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「小火騒動のときには、ばたばたしていて会えなかったでしょう？\n
出掛けるときにも声をかけに来たけど、会えなくて」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はこの塔とドア一枚で繋がっているだけの人間だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "居場所を把握している人がいなかった以上仕方ないが、謝れなかったことはずっと気になっていた。"

hide yuri_t_03_10
show yuri_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0168
Julius "「仕方ない。\n
あのときは替えの道具を探しに街に出ていたからな、擦れ違ったとしてもおかしくはないだろう」"

hide yuri_t_02_10
show yuri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0169
Julius "「おまえが気に病むようなことじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の言葉は余計な飾りはない。\n
ただ事実を告げてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが厳しくも優しく聞こえるのは、彼という人間を私が知っているせいだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（……でもね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ユリウスに謝れなかったことは、ずっと気掛かりだったのよ）"

hide yuri_t_02_11
show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice jul_f0170
Julius "「もうすんだことだ。\n
今更、蒸し返す必要はない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……うん、でも、ちゃんと謝りたかったの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「ごめんなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もう一度頭を下げ……、そして私は覗き込むように無愛想な彼に顔を近付けた。"

hide yuri_t_03_9
show yuri_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0171
Julius "「な、何だ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「もうあんなことはしないから……、また遊びに来てもいい？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（今度ばかりは、駄目と言われるかもしれない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事の邪魔だと彼に判断されたら、二度とこの部屋に入れてもらえない。\n
それは、とても……、哀しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ユリウスの傍は、居心地がいい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのふらふらと落ち着かない騎士が、彼のいる場所では安定するのが分かる気がする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私と同じように暗くて、擦れた部分を持っている彼の近くでは、自然でいられる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの近くとは違った意味で、ここは、とても暖かい場所。"

hide yuri_t_03_3
show yuri_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0172
Julius "「…………。\n
はあ……、どうせ来るなと行っても来るんだろう？」"

hide yuri_t_03_11
show yuri_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0173
Julius "「だったら、詫びなどいらない。\n
ただし居候する気があるのなら……、９０点以上の珈琲を出せよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ええ、点数なんて付けられないぐらい、おいしい珈琲を淹れるわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "許容の言葉に、顔が綻ぶ。\n
またこの場所に来ることを許されて、ほっとした。"

hide yuri_t_02_9
show yuri_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0174
Julius "「……まったく、私の部屋になど来ても何も面白いことなどないだろうに。\n
本当に、おまえは物好きな女だ」"

play sound se_0449
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、ぽんと肩を押される。"

hide yuri_t_02_12
show yuri_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0175
Julius "「おまえの帰りを待っている奴がいるんだろう。\n
早く、会いに行ってやれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「……うん、ありがとう、ユリウス」"

hide yuri_t_02_2

$ hi_mes()

scene ts_02 with Dissolve(.8)

scene cr_01
with stripe_l_long

play music honobono2_a_ali
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（この部屋に来るのも、すごく久しぶりな気がする）"

play sound se_0285

scene n_02
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「……ナイトメア？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "懐かしささえ覚えながらドアを開く。\n
部屋の中央に据えられた執務机の前には……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「あれ、いない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見慣れた細い姿は、いつもの定位置にはなかった。\n
慌てて周囲を見渡したが、どこにも隠れている気配はない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「……まさか」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（また仕事が嫌で、どこかに逃げ込んでいるんじゃ……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice nig_f0333
Nightmare "「君が帰ってきたのに、そんなことをするはずがないだろう？」"


show end_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然聞こえた声は、頭上からだった。\n
天井を仰ぎ見ればそこには……、頬杖をついた姿勢でどこかふて腐れた顔をする夢魔の姿。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0334
Nightmare "「……ふて腐れてなんかいない。\n
私はいつも通りだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0335
Nightmare "「ふん……、そうだとも。\n
ふて腐れてなんかいないんだからなっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（そうね、ふて腐れているんじゃないわね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "{size=+20}「拗ねているのね？」{/size}"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0336
Nightmare "「な……、違う、違うぞっ。\n
拗ねてなんかいない！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0337
Nightmare "「私はクローバーの塔の領主なんだぞ。\n
そんな子供っぽい真似なんか、誰が……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふんと視線を外したナイトメアは未だに宙に浮いたままだ。\n
この部屋は天井が高く、彼がいる場所には私ではどうあっても手が届かない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "癇癪を起こした子供がわざと見つかる場所に隠れているような、そんな気がした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（また子供っぽいことを）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice nig_f0338
Nightmare "「ちーがーう！\n
私は拗ねてなんかいないし、子供っぽいことなんか……、ない、ぞ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "空中でいじいじしている姿は、どう見てもいじけているようにしか見えないが、本人は断固として認めない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "変なところで頑固な彼らしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……だいたい、そんなところで何をしているの？\n
仕事もまた溜めて……、グレイが嘆くわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "主の座っていない机には、いつものように決裁待ちの書類が溜まっている。\n
その高さを見て、少しだけほっとする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（……よかった、少なくとも私が出掛けたときよりも悪化はしていないみたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋領にまでやって来るぐらいだから、どれほど仕事を溜めているかと心配していたのだが……。\n
これならいつもの範疇だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（そうよね、グレイが付いているんだもの）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（溜め込んだ状態で、外になんか出すはずがないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "初等部の学生が、初めて得た長期休みで遊びほうけて、課題を残すのはよくあること。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それをぴしゃりとコントロールするのは、やはりお母さんの役目だろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0339
Nightmare "「君はまたグレイ、グレイと……。\n
時計屋に続いて……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（ん？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（ユリウスに続いてってことは……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっと天井近くに浮いた影を見上げて、私は眉を寄せた。\n
すると私の視線を避けるように、彼はついと顔を背けてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口に出しては何も言っていないのに、タイミングがよすぎる。\n
つまり……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「心を読まないのは、もうやめたの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（あのときには読むのが怖いとか何とか、格好いいことをいっていたのに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……まあ、いいか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心を読むナイトメアと一緒にいることが多いせいか、読まれない状況には違和感を覚えてしまっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（ああ、慣れって怖い）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice nig_f0340
Nightmare "「君の許可があるのに、読まない理由はないからね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice nig_f0341
Nightmare "「君の心の声を大切にするといっただろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……ふうん。\n
だったら、どうしてそんなところでまだ浮いているわけ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0342
Nightmare "「……気分転換だ。\n
そうとも、拗ねているわけじゃないぞ、ああ、違うとも！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは意固地になっているのか、やけに繰り返してくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その様子を見て私は口の端を持ち上げた。\n
ようやく彼があんな場所でいじけている理由が分かった気がしたのだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「燃えたのは、ユリウスの部屋よ。\n
謝らずにそのままなんて出来るはずがないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「謝罪に行くのは当然のことよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の性格を知っているナイトメアならば、知ったところでいじけたりはしないと思っていたのだが、予想に反して彼はいじけてしまっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（心が読めるのだから、私の気持ちぐらい察しているでしょうに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（……本当に、そういうところは情けないというか、根性がないというか）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0343
Nightmare "「な、何だ、[firstname]、その顔は。\n
私は別にヤキモチなんか焼いていないんだからな！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0344
Nightmare "「私は理解のある、包容力のある優しい男だからな。\n
ははははは」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0345
Nightmare "「はは……。\n
……はあ」"

hide end_1
show end_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（……本当に、子供みたいなことを言って）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "宙に浮いた状態でのの字を書いている相手を、可愛いと思ってしまった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「ナイトメア」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手にした小さな包みを彼にも見えるように揺らしながら、もう一度名前を呼ぶ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「あなたに渡したいものがあるの。\n
そろそろ機嫌直して下りて来ない？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_14")
T "「あなたがいらないなら、持って帰るけど」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_14")
voice nig_f0346
Nightmare "「私に……、渡したいもの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ええ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不思議そうに見つめてくる顔を見上げて、続けた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼にもよく見えるように、もう一度袋を揺らしながら。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「あなたが気に入るかどうかは分からないけど……。\n
寝込ませちゃったお詫びを持ってきたんだけど、いらなかった？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Nightmare "「！」"

play sound se_0216 volume .40
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までどんな言葉にも決して降りようとしなかったナイトメアは、直ぐさま飛び降りてきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足音も立てずに降り立った今の彼には、先程までの拗ねた様子などどこにもない。\n
まるで新生物を見るように、私の手にした袋をじっと見つめている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0347
Nightmare "「君が、私に、お詫び？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「ええ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（期待されるほど大したものじゃないけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心の中でしつこいくらいに付け加えておく。\n
過剰に期待されても困る、本当に気持ち程度のものだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0348
Nightmare "「……逆ならともかく、どうして？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「いったでしょう、お詫びよ。\n
……半分はね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Nightmare "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「……残りの半分は、あなたとの、その」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（仲直り出来ればと思ったの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアと喧嘩をして飛び出してしまったわけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、病弱な彼の具合を更に悪くさせてしまった原因の一つは、紛れもない私の行動だった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「正確にいえば、喧嘩両成敗っていうところだけど……。\n
私なりにけじめを付けようと思って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……ごめんなさい、ナイトメア」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Nightmare "「[firstname]……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0349
Nightmare "「私こそ、君に悪いことをした。\n
君がどういう人か、よく知っていたつもりだったのにな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "贈り物を持っていない空の手を取られて、握られる。\n
こんなときにもひんやりと冷たい手。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その冷たい手のひらに、自分の熱が少しずつ伝わっていくのが……、どこか嬉しい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0350
Nightmare "「君にそこまで気を遣わせてしまうなんて、私もまだまだらしい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「まあ、あなたにまだまだなところなんて山ほどあるのは否定しないわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その筆頭は身体の弱さだが、残念ながらすぐに治るものでもない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0351
Nightmare "「う……、酷い。\n
こんなときにまで私のウイークポイントを突かなくとも」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「はいはい、分かったから……。\n
その、嫌じゃなかったら、受け取ってくれる？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐る恐る持ち上げた包みを差し出せば、彼は躊躇いなく、手に取った。"

play sound se_0472 volume .40
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0352
Nightmare "「ありがとう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「いいえ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（あれ……？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「ナイトメア、少し顔が赤いけど……、大丈夫？\n
また熱でも出た？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice nig_f0353
Nightmare "「あ、ああ、いや、熱は出ていない。\n
少しぼうっとしているが、平気だ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice nig_f0354
Nightmare "「なあ、[firstname]……、中を、開けても構わないか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「別に構わないけど……、本当に大したものじゃないのよ？」"

play sound se_0469
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の許可を得るや否や、彼はいそいそと包みを開け始めた。\n
といっても、ただの紙袋なのだから、すぐに中身は現れる。"

play sound se_0471

play music transparent1_a_ali
hide end_2
show end_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「…………。\n
ね、大したものじゃないでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "渡したのは、ナイトメアを模して作った、健康を祈願したプレートを持っている人形だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……これは、喜んでいるの、それとも外したの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は現れた人形の形をしたお守りを見て、動きを止めていた。\n
隅々まで確かめるようにじっと見つめている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………。\n
[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「う、うん……。\n
やっぱり、気に入らない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "静かな声で名前を呼ばれて、身体が震えた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0355
Nightmare "「馬鹿なことを言わないでくれ。\n
これ以上の贈り物なんてないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は愛おしそうに人形を抱き締めて、私に微笑みかけてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもは青ざめている顔色が、今はどこか赤い。\n
照れているのか、それとも恥ずかしがっているのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それは心の読めない私には分からない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（……嬉しい？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（少しは元気になれそうかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その顔を見ている私も、きっと似たような表情を浮かべてしまっているのだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0356
Nightmare "「嬉しいに決まっているだろう。\n
これには、君の心が詰まっている」"

hide end_3
show end_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "囁きながら、ナイトメアは人形に顔を寄せて、唇で触れた。\n
姿形は彼そっくりの人形だというのに……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな仕草をされると、作った私まで何故か恥ずかしくなってしまう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0357
Nightmare "「これ以上の贈り物なんて、どこにもないよ。\n
嬉しい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………。\n
だったら、ちゃんとお守りの効果も発揮してちょうだいよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人形に込めた願いは、ナイトメアの健康。\n
吐血が日常茶飯事の彼にとっては、これ以上ないお守りだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（せめて、もう少し血を吐く頻度だけでも下げてくれないと……。\n
本当にいつか、動かなくなりそうなんだもの）"

hide end_4


show nai_s_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice nig_f0358
Nightmare "「そうだな、努力はしたいと思うが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「だったら、病院に……」"

hide nai_s_02_9
show nai_s_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice nig_f0359
Nightmare "{size=+20}「病院は行かない！」{/size}"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（ちっ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう簡単に乗せられてはくれないらしい。"

hide nai_s_02_5
show nai_s_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0360
Nightmare "「それに……、病院に行くぐらいだったら、君のくれたお守りを持っているほうが御利益がありそうだからな」"

hide nai_s_02_2
show nai_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0361
Nightmare "「こうすれば、ますます効果が高まりそうだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひんやりとした指先が、私の頬に触れて、引き寄せる。\n
抵抗する間もなく、彼が持っていた人形が私の唇に触れた。"


show end_5 onlayer master
with dis
hide nai_s_03_10
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice nig_f0362
Nightmare "「[firstname]。\n
私は神様なんてものは信じないが……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice nig_f0363
Nightmare "「幸福を招いてくれる、幸運の女神は……、今、目の前にいる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ナ、ナイトメア……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人形が触れたのは一瞬だった。\n
だが、先ほど彼自身の唇が触れていたのも、同じ場所ではなかっただろうか。"

hide end_5


show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「あ……」"

hide nai_s_02_1
show nai_s_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice nig_f0364
Nightmare "「これは肌身離さず持っていることにする。\n
君が作ってくれたお守りだからね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "嬉しそうに人形を掲げられて、恥ずかしくなる。\n
口を付いて出るのは、やはり可愛くない言葉になった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……そんなお守りなんて必要ないくらいに、元気になる、くらい言えないの？」"

hide nai_s_02_12
show nai_s_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
Nightmare "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「だ、だから……。\n
お守りなんかに頼らなくてもいいぐらい、健康になればすむ話でしょう」"

hide nai_s_01_2
show nai_s_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice nig_f0365
Nightmare "「病院には行かないぞ、絶対にだ！」"


play music gag1_a_ali
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（……先刻までは、ちょっと格好よかったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こと病院が関わると、ナイトメアはどうしようもないほど頑なになる。"

hide nai_s_01_12
show nai_s_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0366
Nightmare "「頑固と言われようが、嫌なものは嫌だ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「回復祈願には、千枚の紙で鶴を折るといいっていう話も聞いたけど……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（何なら、グレイと一緒に折ってあげてもいいわよね。\n
あの人なら、喜んで折ってくれそうだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "出来上がりは……、言わぬが花というものだろうが。"

hide nai_s_02_6
show nai_s_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0367
Nightmare "「それは入院した患者に贈るものであって、私には必要ない！\n
私は入院しなくても、やっていける！」"

hide nai_s_02_10
show nai_s_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0368
Nightmare "「そうとも、千羽の鶴だろうが、一万の亀だろうが……、そんなものいらない！\n
そもそも、病院になんて行かないからなっ」"

hide nai_s_02_13
show nai_s_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0369
Nightmare "「そんな験担ぎでよくなる病弱具合なら、私はとっくに健康になっている！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（威張って言うことじゃないわよ、それ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "神頼みも通じないとなれば、あとは地味に医学の力を借りるしかないと思うのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（この様子じゃ、何を言ったところで病院に行きそうもないわよね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……まったく、もう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本当に仕方のない夢魔だ。\n
とは言うものの、健康を祈願するお守りを渡しておいて、興奮させてしまっては元も子もない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（少し、話の矛先を変えてみようかな）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「でも、健康体になれば堂々と煙草が吸えるわよ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「私やグレイに文句も言われず、格好よく、びしって吸えるでしょうね。\n
格好よく、上司らしく」"

hide nai_s_03_8
show nai_s_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice nig_f0370
Nightmare "「う……、それはそうだが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「まあ、元気になって煙草を吸ったらまた元の木阿弥なんだけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が持ったままの人形に指を添えながら、私は続ける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「このお守りなら、御利益があるんでしょう？\n
もう少しだけ元気になってみようとは思わない？」"

hide nai_s_03_9
show nai_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice nig_f0371
Nightmare "「そうだが……、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ん？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひんやりと。\n
今度は人形以外の感触が、私の唇に触れた。"


play music happy_a_ali

show end_6 onlayer master
with dis
hide nai_s_03_10
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「え……？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice nig_f0372
Nightmare "「ふふふ、君が言うほど健康にならずとも、病弱な私でもこれぐらいは出来るんだよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "得意げに笑った顔は、いつもの情けない上司の顔ではなく。\n
私の心を掻き乱す、綺麗で、不思議な笑み。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0373
Nightmare "「これ以上の御利益は、お守りよりも、幸運の女神さまから直接もらうとしよう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……ん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「……っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "重ねられる唇から、私の熱と心がナイトメアの中へと広がっていく。\n
それが嬉しくて、満たされる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（ああ、私は、この人が好きなんだな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな当たり前のことに笑みが零れた。\n
見つめる顔も、私と同じように微笑んでいる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0374
Nightmare "「その通り、私も同じだよ、[firstname]。\n
君以上の幸福なんて、どこにもない」"

$ hi_mes()
hide end_6


scene n_02 with Dissolve(.2)

scene charasel_bg_tower_eve
with stripe_l_medium

scene map_bg_winter_eve
with stripe_l_medium

scene map_bg_winter_day with Dissolve(.1)

scene map_bg_winter_night with Dissolve(.1)

scene map_bg_winter_eve with Dissolve(.1)

scene charasel_bg_tower_eve
with stripe_l_medium

scene n_02
with stripe_l_long

play music gray_t_ali

show gre_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Gray "「…………」"

hide gre_t_02_11
show gre_t_02_11 at left
show nai_s_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Nightmare "「…………」"

hide nai_s_03_10
show nai_s_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0375
Nightmare "「ふふ、うふふふ。\n
はははは」"

hide gre_t_02_11
show gre_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Gray "「…………」"

hide gre_t_03_2
show gre_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0142
Gray "「[firstname]、ナイトメア様に薬でも飲ませてくれたのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……いいえ。\n
薬なんて、一口も飲ませていないんだけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（グレイがそう聞きたくなる気持ちは、よく分かる）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "{size=+20}（分かりたくはなかったけど）{/size}"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達は、不気味な含み笑いを浮かべる上司を途方に暮れて見つめている。"

hide nai_s_03_1
show nai_s_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0376
Nightmare "「ふふ、ふふふふ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「いい加減、その気持ちの悪い笑い方は止めてよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（見ているこっちが恥ずかしくなる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が人形をあげたあのときから、ナイトメアは手元にそれを置いて離さない。\n
その上、人形を見つめては、今のように気色の悪い笑い声を上げる始末だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（取り上げたほうがいいかしら、あれ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "年端のいかない子供ならばさておき、クローバーの塔の領主ともあろう者が、人形と目を合わせては、にやにやと笑み崩れているなんて。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（……それも、自分に似せて作られた人形だなんて）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナルシストと取られるほうがまだ幸運かもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（かなり可哀想な人に見えているような……）"

hide gre_t_03_3
show gre_t_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice gra_f0143
Gray "「しかし……。\n
恐ろしいことに、仕事は進んでいるんだ」"

hide gre_t_01_6
show gre_t_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice gra_f0144
Gray "「早くはないが、溜まらない。\n
素晴らしい効果だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「そうなのよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これで仕事をしないのであれば、グレイが問答無用で取り上げていることだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、執務机に人形を置いたナイトメアはむらっ気を起こすことなく、真面目に仕事に取り組んでいるのである。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（あのにやけた顔と、笑い声だけに目を瞑れば……、いいこと尽くめなんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "プレゼントしたものを大切にしてもらえれば、私だって嬉しい。\n
しかも、仕事の能率も上がるというダブル効果だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが……。"

hide nai_s_02_4
show nai_s_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "満面の笑みで人形を見てはちらちらと私に向けてくる視線が、恥ずかしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（やっぱり、無理！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大切にされているのは嬉しい、それは確かだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、だからといって人形にでれでれするナイトメアを見るのは、何だかとてもむずむずする。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「取り上げましょう、グレイ」"

hide gre_t_01_11
show gre_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice gra_f0145
Gray "「いや、それはさすがに……。\n
血を吐かれる回数も減っているし、お守りとしてはこれ以上ない成果だと思うが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「クローバーの塔の領主があれじゃあ、沽券に関わるわよ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「ほら、ナイトメア！\n
いつまでも笑っていないで……」"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが動き出すよりも先にしびれを切らした私は、うっとりと眺めていたナイトメアの手から人形を奪い取った。"

hide nai_s_01_13
show nai_s_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice nig_f0377
Nightmare "「あーーーっ、な、何をするんだ、[firstname]！\n
私のお守りなのにっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「領主が自分の人形趣味の～～～～だなんて噂が立ったらどうするのよ！？\n
病弱の他に、変質者の冠までほしいわけ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "病弱で、夢に引きこもる、自分の人形が大好きな変態芋虫。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（自分で言っておいていうのも変だけど、すごいわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何というか、この世にある不名誉の塊のような称号を総ナメにしている気がする。"

hide nai_s_02_10
show nai_s_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0378
Nightmare "「そ、そこまでいうことはないだろう、そこまで」"

hide nai_s_02_8
show nai_s_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0378_5
Nightmare "「君の御利益のおかげか、ほら、最近は吐血することもなく、こんなにも元気で……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

hide gre_t_01_10
show gre_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice gra_f0146
Gray "「ナイトメア様？\n
何だか、顔色が悪くなったようですが」"

hide nai_s_02_7
show nai_s_03_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice nig_f0379
Nightmare "「いやいや、そんなことはない！\n
私は元気になったんだ、血など吐くも……」"

hide nai_s_03_6
show nai_s_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice nig_f0380
Nightmare "「ごふ、がは、げふほ！！」"

play sound se_0631
$ flash_red(.2)
hide gre_t_03_3
show gre_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice gra_f0147
Gray "「で、ですから、元々身体が弱いのに無理をするから！\n
大丈夫ですか？」"

play sound se_0432
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慣れた様子でグレイは背中をさすり始めている。\n
床に滴った血の赤を見て、何故か私は溜息をつきたくなってしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「何というか……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（吐血するナイトメアを見て、これが私の日常と思ってしまうなんて）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（慣れるにも程があるわよね）"

hide nai_s_03_2
show nai_s_03_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice nig_f0381
Nightmare "「げふ、がふ……！\n
い、いやいや、何を言うんだ、[firstname]」"

hide nai_s_03_5
show nai_s_03_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice nig_f0382
Nightmare "「わ、私は、本当に健康に……。\n
{size=+20}ごはあっ！！！{/size}」"

play sound se_0631
$ flash_red(.1)
hide gre_t_03_2
show gre_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice gra_f0148
Gray "「ですから、無茶しないでくださいと言っているじゃないですか、ナイトメア様！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつまでも吐血させたままにさせておくわけにはいかないので、私もグレイと一緒にナイトメアの介抱に回る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（そうね、これがここでの私の日常）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "急に心を読まれなくなるのも。\n
急にこの看病がなくなるのも。\n
それは何だか、ちょっともったいないような気もする。"

hide nai_s_03_8

hide gre_t_01_10

$ hi_mes()

scene n_02 with Dissolve(.1)

scene charasel_bg_tower_eve
with stripe_l_medium

scene map_bg_winter_eve with stripe_l_short

scene yume01 with Dissolve(.1)

scene yume02 with Dissolve(.1)

play music dream_inside_p_ali

scene yume03 with Dissolve(.1)

show nai_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0383
Nightmare "「うう……、おかしいな。\n
君が戻ってからは大分調子がよかったのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「……あなたのその体質がそう簡単に改善されるはずがないでしょうが」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふわふわと現実と同様に浮き上がっているナイトメアは、私の言葉に深い深いため息をついた。"

hide nai_t_01_7
show nai_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0384
Nightmare "「そこまで言わなくてもいいじゃないか。\n
現に、あのグレイから仕事が進んで嬉しいという心の声まで聞こえたぞ」"

hide nai_t_01_4
show nai_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0385
Nightmare "「普段は聞かないくせに。\n
ぜひこのままでいてください、とかわざとじゃないのか、あいつは」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（儚い望みね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "叶わないからこそ、願わずにはいられないのだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「そういえば……。\n
あなた、どうしてあのお店で働いていたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔に戻れば理由を教えてくれるかと思ったのに、ナイトメアはその件についていまだに理由を教えてくれない。"

hide nai_t_01_10
show nai_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0386
Nightmare "「言っただろう、声を聞かない分は君の近くにいれば安心だと思ったんだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「……嘘つき」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（それだけじゃないでしょう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "近くにいるのが目的ならば、何も喫茶店でアルバイトの真似事などしなくてもいい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それこそ堂々と帽子屋屋敷に顔を出せばよかったのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それをせず、私が立ち寄るかどうかも分からない場所に居座るなど、相応の理由がなければしないはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（それに、グレイだって認めないわ。\n
ただでさえ体調がよくない病弱な夢魔なんだから）"

hide nai_t_02_10
show nai_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice nig_f0387
Nightmare "「酷い言われようだな。\n
まあ、確かに目的があってあの店に行っていたことは事実だが……」"

hide nai_t_02_7
show nai_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice nig_f0388
Nightmare "「知りたいか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔を近付けてきた夢魔は、楽しげにそう問いかけてくる。\n
私がどんな気持ちでいるのかなど、彼にはお見通しのはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（分かっているのに、聞かないでよ）"

hide nai_t_02_12
show nai_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice nig_f0389
Nightmare "「言っただろう、君の声を大切にしたいんだ。\n
偽れない心の声も、唇から生まれる声も」"

hide nai_t_03_10
show nai_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice nig_f0390
Nightmare "「ここなら、他の誰にも横取りされることなく、聞こえるからね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢。\n
曖昧で上も下も、右も左もない空間。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼がいるから、私という存在を知覚できる。\n
ここは相対でなければとても孤独な場所だろう。"

hide nai_t_03_11
show nai_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0391
Nightmare "「そういうことだ。\n
君に出逢うまでは私もここで一人で引きこもっているのが一番楽だったんだがね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「今は違うの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢は彼の領域だ。\n
どんなものも、どんな形も、彼が望めばここではすべて叶えられる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（ある意味、クローバーの塔よりも夢の中が彼の領土かもしれない）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice nig_f0392
Nightmare "「そうだな、ここなら私は何でも出来る。\n
でも……、君は二人といない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（それは余所者だから？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界にとっての異物。\n
けして混じりきれない、別の存在。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが余所者と呼ばれる私だ。"

hide nai_t_02_1
show nai_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0393
Nightmare "「違うよ、余所者だからじゃないんだ、[firstname]。\n
私にとって、君に代わる人はいない」"

hide nai_t_02_13
show nai_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0394
Nightmare "「君と過ごして、大分考え方を改めたよ。\n
君がいてくれると、夢から出ていくのもそう悪いことじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

hide nai_t_02_1
show nai_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice nig_f0395
Nightmare "「君が夢を見る人でよかった。\n
現実でしか会えなかったら、君をこうして独占できなかったからね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……それは私も同じよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の人と夢で会うのとは、まったく違う。\n
夢の中のナイトメアは現実とは違う怖さと、不確かさを持っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（それでも……、恐ろしいと思う以上に、会えることが嬉しいわ）"

hide nai_t_02_2
show nai_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
Nightmare "「……[firstname]」"

hide nai_t_01_11
show nai_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice nig_f0396
Nightmare "「次の時間帯は休憩だろう？\n
一緒に出掛けよう」"

hide nai_t_01_1
show nai_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice nig_f0397
Nightmare "「君の質問に、答えるよ。\n
夢ではなく、現実でね」"

play sound se_0468
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「ここじゃ駄目なの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水中から急速に身体を持ち上げられるような、吸引力。\n
身体に意識が引き戻されているのか、不思議な感覚が身を包む。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目が覚める。"

hide nai_t_01_6
show nai_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0398
Nightmare "「ここでもいいが……。\n
三月ウサギとはデートをしてきたんだ、私ともデートをしてくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「デ、デートって……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（ブラッドみたいなことを言わないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦笑いを浮かべながらも、身体はどんどん夢から離れていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（じゃあ、また後で）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢でも、現実でも。\n
私を待っていてくれる人に、約束の言葉を送った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢から離れていく私を、夢魔は目を細めて見つめ返す。"

hide nai_t_02_8
show nai_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice nig_f0399
Nightmare "「ああ。\n
外でまた会おう、[firstname]」"

hide nai_t_02_1

$ hi_mes()

scene yume03 with Dissolve(.1)

scene yume02 with Dissolve(.1)

scene yume01 with Dissolve(.1)

scene map_bg_winter_day with Dissolve(.1)

scene map_bg_autumn_day with Dissolve(.1)

scene bg_gen_sky_aut_day with Dissolve(.1)
play sound se_0624
pause .3
play sound se_0622

play music transparent1_a_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0400
Nightmare "「はあ、はあ……。\n
どうして、こんなに急な坂なんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0401
Nightmare "「つ……、疲れる。\n
ああ、足が痛い」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「この前までは、どうやって通っていたのよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットと一緒のときには自転車で進んだ道を、今、徒歩で私達は歩いている。\n
とはいえ、店の位置が帽子屋領の端なので、当然結構な距離があるのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（本当に体力がないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の隣を歩くナイトメアは、慣れない坂道ですっかり体力を消耗しているらしく、全身に汗をかいている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "血こそ吐いていないが、このままでは遅かれ早かれ吐血騒ぎになりそうだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0402
Nightmare "「どうやってって……、夢を渡れば距離なんてないようなものだからな。\n
実際に足で向かうのはこれが初めてだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（納得してしまう自分が哀しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かにこの状態では、塔から店まで歩いて行ったら、間違いなく店ではダウンしていることだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ウエイターの仕事をするには、一時間帯は休まないと使いものになりそうもない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「だったら、今回も夢から行けばよかったじゃない。\n
私は先に歩いて向かっていてもよかったのに」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice nig_f0403
Nightmare "「そ……、それじゃあ意味がないだろう？\n
デートというものは、こう一緒にいくのが醍醐味であってだな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……無理して、後でまたひっくり返っても知らないわよ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすがに他領土で倒れた領主をグレイに迎えに来てもらうのは、気が引ける。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（いくら細くても、ナイトメアを担いで帰るのは私には無理よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "というより、そんなことをしたら二人揃って行き倒れになるのが目に見えていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0404
Nightmare "「か、担ぐって……。\n
私はまだ大丈夫だとも！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0405
Nightmare "「ほら、行くぞ、[firstname]！\n
目的地はもうすぐだ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「…………」"

play sound se_0693
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（まあ、たまにはこうやってゆっくり外を散策するのもいいわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "森林浴の効果か。\n
はたまた、握られた彼の手のおかげか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_1")
T "（一気に走るのもいいけど、一歩ずつ行くのも楽しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのとき、一瞬で通り過ぎていった森の風景がゆっくりと流れていく。"


$ hi_mes()

scene bg_gen_sky_aut_day with Dissolve(.8)

scene bg_gen04_km_day
with stripe_l_medium

scene bg_gen04_kn_day
with stripe_l_long

play music forest_town_square_p_ali
play sound se_0180

show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0406
Nightmare "「こんにちは、お邪魔するよ」"

hide nai_s_01_11
show nai_s_01_11 at left
show tenin_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kaz_f0020
Clerk "「あ、久しぶり。\n
先刻のあれのことかな」"

hide nai_s_01_11
show nai_s_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0407
Nightmare "「ああ、そういうことだ。\n
主はいるかな？」"

hide tenin_3
show tenin_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kaz_f0021
Clerk "「オーナーなら、奧のキッチンにいるよ」"

hide nai_s_01_1
show nai_s_02_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0408
Nightmare "「そうか、[firstname]。\n
私はちょっと話をしてくるから、座って待っていてくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「あ、うん。\n
分かったわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（話って何だろう？）"

hide tenin_1

hide nai_s_02_12
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "疑問を覚えなかったわけではないが、聞き返すよりも早くナイトメアはカウンターから中へと入っていってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうすると、いつまでも立って待っているわけにもいかない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（席は……、今回は結構込んでいるわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "店内のテーブルは一つの席を除いて、すべて埋まっている。\n
しかし、唯一のその席は、窓辺に接した見晴らしのいい席だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（……空いているのが、よりにもよってあの席だけなんて、どういう因果だろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この前エリオットと一緒に座って間もなく、襲撃を受けたあのテーブルだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（今回はナイトメアが一緒にいるから、マフィアの絡みで襲われることはないと思いたいんだけど）"


show tenin_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice kaz_f0022
Clerk "「お客様、いかがされました？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「あ、いいえ。\n
何でもないんです」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（とりあえず、座っていればいいわよね）"

hide tenin_2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつまでも店内でぼうっとしていた私を訝しむ声に押されて、とりあえず椅子に腰を下ろす。"

play sound se_0406
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「……窓も、同じもので直したのかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのとき、派手にぶち破られていたはずだが、今填め込まれている窓には傷一つない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時間帯が経って直ったのではなく、一刻も早く営業するために、人の手で修繕されたのだろう。"


play music elliot_t_ali

show eri_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0293
Elliot "「それはそうだな。\n
こんなでかい窓硝子、直そうと思ったらそのほうがかえって手間だぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「そうよね。\n
でも、これだけ大きな硝子となると、同じものを探すのも大変……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "{size=+20}「！！？」{/size}"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「エ、エリオット！」"

hide eri_t_01_5
show eri_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice eri_f0294
Elliot "「よう、[firstname]。\n
遊びに来ているなら、うちに寄ってくれればよかったのに」"

play sound se_0251
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どかっと断りもなしにソファに腰を下ろしたエリオットは、私を見た後、周囲に目を向けた。"

hide eri_t_02_12
show eri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0295
Elliot "「見たところ、一人みたいだし。\n
何だよ、ナイトメアの野郎、こんなところまで一人で来させたのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ナイトメアは、今、ちょっといないだけで……。\n
……って、あなたもどうしたの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「また仕事？」"

hide eri_t_02_11
show eri_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice eri_f0296
Elliot "「あー、違う違う。\n
単に見回りのついでに、ここの修復状況を確認しに来ただけだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「修復状況？」"

hide eri_t_01_5
show eri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice eri_f0297
Elliot "「ああ、この前結構派手に壊れていたからな。\n
修繕に金と人を出していたんだ」"

hide eri_t_01_8
show eri_t_01_8 at left
show tenin_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice kaz_f0023
Clerk "「ええ、おかげさまで、元通りですよ。\n
窓だけでなく、内装まで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水を運んできた店員の言葉には、畏怖よりも感謝の響きがこもっていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先に座っていた私よりも、エリオットに先に水を出しているあたり、彼の立場も分かっているのだろう。"

hide eri_t_01_8
show eri_t_03a_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0298
Elliot "「元はうちの揉め事なんだ。\n
きちんと落とし前は付けておかないと、ブラッドの顔に泥を塗ることになるからな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（なるほど、一応領主だものね、あの人も）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（本人が聞いたら顔をしかめそうだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "マフィアという性質柄か、ブラッドは自分のことをならず者だとか、悪人だと主張したがるが、それだけで領主などという立場が勤まるはずがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、私と一緒に来た彼もまた同じ領主なのだが……。"


play music nightmare_t_ali

show end_7 onlayer master
with dis
hide eri_t_03a_8

hide tenin_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0409
Nightmare "「お待たせしました、お嬢様」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「その呼び方は止めてよ、何だか落ち着かないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ウエイター姿のナイトメアは恭しく礼をしてみせる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0410
Nightmare "「だが、待たせたのは事実だろう？\n
やあ、エリオット、君も来ていたのか」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0299
Elliot "「まあな。\n
近くを通ったら姿が見えたから来たんだけどよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0300
Elliot "「……ん、ナイトメア、それ、何だよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは手にした銀のトレイに何か食べ物を載せている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0411
Nightmare "「目敏いな。\n
だが、残念ながら君の好きなオレンジ色のものは入っていないぞ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0412
Nightmare "「これは、君へのサービスだよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………？」"

play sound se_0546
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「あ」"

hide end_7


show nai_w_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice nig_f0413
Nightmare "「君が仲直りの贈り物を探していてくれたように、私も考えたんだ」"

hide nai_w_01_1
show nai_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice nig_f0414
Nightmare "「とはいえ、君は花も遠慮してしまうからね。\n
代わりに……、こういうものにしてみた」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の前に置かれたのは、可愛らしいプディングで。\n
最初にこの店を訪れたときの記憶が蘇った。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（そういえば、あのときも研究が足らないとか何とか言っていたけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「……まさか、あなたの手作り？」"

hide nai_w_01_11
show nai_w_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice nig_f0415
Nightmare "「な、何でそんなに驚くんだ。\n
少なくとも、うちのデストロイヤーシェフよりはマシだろう！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（自分の部下をデストロイヤー呼ばわりか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の料理の腕については私もよく知っているから、否定は出来ない。"

hide nai_w_01_12
show nai_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0416
Nightmare "「本当はケーキのようなしっかりしたものを作りたかったんだが……。\n
ここの店主に素人が練習するなら、ここからだと言われてしまってね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "練習。\n
つまり、本当にナイトメアが作ったのだ、これを。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かにケーキに比べればプディングのほうが楽だろうが、デコレーションは大分力が入っている。"

hide nai_w_01_11
show nai_w_01_11 at left
show eri_t_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0301
Elliot "「へえ、結構うまいじゃねえか。\n
……ん、あれ、でもここ、少しクリームが崩れていないか？」"

hide nai_w_01_11
show nai_w_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0417
Nightmare "「な、何だと！？\n
どこだ！？」"

play sound se_0551
hide eri_t_01_5
show eri_t_03a_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0302
Elliot "「ほら、このあたり……。\n
あとは、ここもせっかくのソースが混じっているし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋屋敷でよくデザートを食べている彼らしく、エリオットは食べ物について目が肥えている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "日頃口にしているのがオレンジ色のものばかりなのに、意外とよく見ているらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（むしろオレンジ色だけなのに、細かい違いが分かるんだからすごいわよね……）"

hide nai_w_01_3
show nai_w_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
Nightmare "「…………」"

hide nai_w_01_4
show nai_w_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice nig_f0418
Nightmare "「ああ、本当だ……。\n
くうう、今回は会心の出来だと思ったんだがな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「……何で、持っていくのよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悔しそうにいいながら皿を下げようとする彼の手を、私は止めた。\n
ナイトメアは不思議そうに目を見開いて、首を傾げている。"

hide nai_w_01_10
show nai_w_01_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0419
Nightmare "「何故って……。\n
作り直そうかと思って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「あら、私にくれたのに、勝手に捨てちゃうの？\n
それってずいぶんじゃない、ナイトメア」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔で一緒に過ごしていても、彼が家事らしいことをしたことは見たことがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼が私のために作ってくれたお菓子を、どうして捨てようなどと思うだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（塔ではもっとすごいのを見慣れているから、これなら上等すぎる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見た目もデザートには大切な要素だ。\n
一生懸命作ってくれたのか、おざなりだったのかは、素人目にも分かる。"

hide nai_w_01_12
show nai_w_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「[firstname]？」"

play sound se_0242

play music night_garden_p_ali

show end_8 onlayer master
with dis
hide nai_w_01_2

hide eri_t_03a_2
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「……ん、美味しい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "添えてあったスプーンを手に取り、プディングを口に含む。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0420
Nightmare "「ふ、ふふふ、ははは。\n
そうだろう、そうだろうともっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0421
Nightmare "「私が作ったものがうまくないはずがないっ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（その割には不安そうだったくせに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見た目に欠陥があると分かった途端に下げようとしたのは、自信がなかったせいだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "丁寧に作ってくれたのが分かる、柔らかな卵の味がする。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0422
Nightmare "「そう、もちろん私の才能の勝利でもあるが。\n
これのおかげでもあると思うぞ」"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「え？\n
……！！！？」"

hide end_8
show end_9 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「こ、こんなところにまで持ってきているの！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誇らしげに取り出されたのは、私があげた人形だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0423
Nightmare "「当然だとも。\n
お守りなんだ、肌身離さず持っていなければ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「だ、だからって……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice eri_f0303
Elliot "「ん？\n
なんだ、それ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice eri_f0304
Elliot "「ナイトメアの人形……？\n
あんた、そういう趣味があったのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が贈ったものだと知らないエリオットには、さぞかし奇妙な光景に見えたことだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怪訝な顔をしている彼に、ナイトメアは大威張りで説明を始めた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0424
Nightmare "「違う！\n
これは、彼女が私にだけ作ってくれた贈り物なんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0425
Nightmare "「ふふふ、羨ましいだろう？\n
全部手作りなんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "プディングを乗せていたトレイをテーブルに放り、両手で人形を握り締める。"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「……そんなにあっちこっち引っ張ったら、壊れるわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "特別な材料など使っていないのだ。\n
ずっと持っていてもらえることは嬉しいが、強度までは変わらない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（糸で縫い付けてあるだけなんだから）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice nig_f0426
Nightmare "「ふっ、何を言うんだ、[firstname]。\n
こんなにも君が丁寧に作ってくれた人形が、そう簡単に壊れるはずが……」"

play sound se_0140
hide end_9
show end_10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あ」"


play music gag2_a_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice nig_f0427
Nightmare "「え？\n
えええ！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぽろり。\n
そんな儚い音と共に、青白い手から何かが落ちた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0305
Elliot "「腕、取れたな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「！！！！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0428
Nightmare "「何と言うことだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「だから言ったのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまでの態度とは打って変わって、ナイトメアは落ちた腕と人形を見比べて呻いている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ち込んだ背中からは、じめじめした陰気な空気が漂っていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0429
Nightmare "「君の愛の証が……。\n
君が私のために作ってくれた人形が……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot "「……………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0306
Elliot "「あー、何ていうか。\n
元気だせって言うのもあれだけどよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0307
Elliot "「どうするんだよ、[firstname]。\n
これ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「どうするって……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すっかりいじけモードに入っているナイトメアに途方に暮れているのは、彼だけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうしようというのは、私の心境そのものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（そして、一体どうやって持って帰ろうかしら、この人）"

$ hi_mes()
hide end_10


scene bg_gen04_kn_day with Dissolve(.8)

scene bg_gen04_km_day
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_medium

scene map_bg_winter_day with Dissolve(1)

scene charasel_bg_tower_day
with stripe_l_medium

scene n_01
with stripe_l_long

play music tower_inside_p_ali

show gre_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Gray "「…………」"

hide gre_t_01_6
show gre_t_01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0149
Gray "「ナイトメア様、いい加減、気を取り直してください」"

hide gre_t_01_15
show gre_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0150
Gray "「いつまでもそうやってじめじめされていたら、俺達の気持ちまでじめっとしてきます」"

hide gre_t_01_14
show gre_t_01_14 at left
show nai_s_03_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0430
Nightmare "「うるさい……。\n
夢に引きこもりたいところを無理矢理に出てきているんだぞ」"

hide nai_s_03_8
show nai_s_03_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0431
Nightmare "「……はあ」"

hide gre_t_01_14
show gre_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0151
Gray "「…………。\n
これは相当に落ち込んでいらっしゃるな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「そうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものナイトメアなら「もう少し傷心の上司を労ったらどうなんだ！」ぐらいの反論をしてくるところだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが、机の上に突っ伏したまま動かないのだ。\n
当然、届けられる書類が進むはずもない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結局、帽子屋の領地からナイトメアを運び出すのは、エリオットが手伝ってくれた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の領土の、しかもマフィアのＮｏ．２から上司をお届けされたグレイの微妙な顔は忘れられない。"

hide nai_s_03_6
show nai_s_03_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

hide nai_s_03_5
show nai_s_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0432
Nightmare "「ううう……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（鬱陶しい）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「ナイトメア」"

hide nai_s_02_9
show nai_s_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
Nightmare "「[firstname]……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「いつまでもいじけている暇はないでしょう。\n
ほら、身体を起こして」"

hide nai_s_02_8
show nai_s_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice nig_f0433
Nightmare "「……放っておいてくれ。\n
君からのプレゼントを駄目にしてしまうなんて、私はどうせ駄目な領主なんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（キャラが変わっているわよ、あんた）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも、どちらかというと悪い方向に。"

hide gre_t_03_3
show gre_t_03_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0152
Gray "「ナイトメア様、彼女の言うとおりですよ。\n
いい加減しゃきしゃき仕事をしてください」"

hide gre_t_03_6
show gre_t_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0153
Gray "「彼女の様子を見に行きたいと帽子屋領に行っていた頃は、今の数倍の速さで仕事をしていたじゃありませんか」"

hide gre_t_03_7
show gre_t_03_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0154
Gray "「あなたは出来る上司なんです！\n
さあ、あのときの神業のような仕事をっ」"

hide nai_s_01_10
show nai_s_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0434
Nightmare "「はあ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "褒め称え、持ち上げるグレイの声にはいつもより力がこもっている。\n
しかし、その声も今のナイトメアを立ち上がらせるだけの力はなかった。"

hide gre_t_03_5
show gre_t_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（重症ね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口で反論しているうちは、多少の血を吐こうが、寝込もうが、心配いらない。\n
しかし、気力が落ちているとなれば話は別だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ナイトメア」"

hide nai_s_01_7
show nai_s_01_4 at center
hide gre_t_01_13
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Nightmare "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「壊れた人形、まだ持っているんでしょう？\n
直してあげるから、一度返してちょうだい」"

hide nai_s_01_4
show nai_s_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice nig_f0435
Nightmare "「え？\n
い、いや、そういうわけには……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「この前も言ったけど、自分じゃ直せないでしょう？\n
私が直したほうが早いわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイがこの前修理を申し出て、即行で断られていたのは私も知っている。\n
そのときにも私が直すことを提案したのだが、断られてしまったのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（意地だか知らないけど、いつまでもこの状態じゃ困るわ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（直したらすぐに渡してあげるから）"

hide nai_s_01_12
show nai_s_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心の中から呼びかけると、彼はようやく机の引き出しに手をかけた。"

play sound se_0067
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手渡された人形は、あのとき、片腕が取れた状態のままだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時間帯が経てばいつかは直るだろうが、喫茶店の窓と同じで、それを待っていては塔が立ち行かなくなる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あれ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（こんなところに赤い染みなんてあったかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔の部分に薄い染みが出来ている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（珈琲を零したとかそういう感じじゃない。\n
最近は吐血するだけの元気もなかったはずなんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちょうど染みが出来ている場所が場所だけに、まるで人形が吐血をしているようにも見える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "付いた汚れは、数時間帯で消えてしまう。\n
ということは、つい最近付いたばかりなのだろうが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "疑問符を浮かべる私にナイトメアは言いにくそうに口を開いた。"

hide nai_s_02_7
show nai_s_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0436
Nightmare "「壊したのは私だからね。\n
これでも直そうとしたんだが……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「あなたが、お裁縫をしたの？」"

hide nai_s_02_9
show nai_s_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こくんと縦に首が振れる。\n
改めて手の中にある人形を見た。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "細かいところをよく見れば、通しかけて、途中で切れた糸もある。\n
布の先端部分も少しほつれていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（成果はなかったみたいだけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「つまり、この汚れは……。\n
針で指を刺したってこと？」"

hide nai_s_03_9
show nai_s_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Nightmare "「…………」"

hide nai_s_03_5
show nai_s_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0437
Nightmare "「ああ……、注射や点滴並みに痛かったが、仕方ない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは、居心地悪そうに机の下に隠した手を動かしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "絆創膏は巻いていなかったはずだから、それほど酷いことにはなっていないと思う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（そこまでの怪我をしていたら、グレイが何か言っているだろうし）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「本当に……、仕方ない人ね」"

play sound se_0313
hide nai_s_03_6
show nai_s_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Nightmare "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「そこまでしてくれたのなら、私が直すのは止めるわ。\n
代わりに、お裁縫、教えてあげる」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って、ナイトメアに人形を返した。"

hide nai_s_03_4
show nai_s_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0438
Nightmare "「え？\n
君が私に教えてくれるのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（だって、自分で直そうとしてくれていたんでしょう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この前のプディングにしてもそうだ。\n
慣れないお菓子作りや裁縫をしてまで、報いようとしてくれた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その気持ちが、嬉しくないはずがない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「その代わり、ちゃんと仕事を片付けてからよ。\n
そのほうが集中できていいでしょう？」"

hide nai_s_02_11
show nai_s_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「嫌？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何とも言えない表情で私とグレイを見ていたナイトメアに念を押すと、彼は首を横に振った。"

hide nai_s_02_7
show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0439
Nightmare "「君からの申し出だ、勿論、受けるとも」"

hide nai_s_01_11
show nai_s_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0440
Nightmare "「ただし……、一つだけ条件があるんだ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「どんなことよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "裁縫を教えるのに条件をわざわざ付けたがるとは思わなかったので聞き返すと、彼は指先だけで器用に私に近付くように示してくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同時に、隣に控えていたグレイに離れるように目で合図するのも忘れなかった。"

hide nai_s_01_1
show nai_s_01_1 at left
show gre_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

play sound se_0284 volume .60
hide nai_s_01_1
show nai_s_01_1 at center
hide gre_t_01_1
with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼に忠実な部下は、言葉などなくとも眼差しだけで意図を察したらしい。\n
小さく会釈をすると、部屋を出て行った。"

hide nai_s_01_1
show nai_s_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0441
Nightmare "「簡単なことだよ。\n
直すまでの間、代わりのお守りがほしいんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……また、作るの？」"

hide nai_s_01_6
show nai_s_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nig_f0442
Nightmare "「いや……。\n
目の前にいるじゃないか、最高のお守りが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引き寄せられて、ナイトメアの膝に座ってしまう。\n
驚いているうちに、腕を掴まれ、顔が近付いた。"


play music happy_a_ali

show end_11 onlayer master
with dis
hide nai_s_02_2
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………っ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice nig_f0443
Nightmare "「……は」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「…………ふ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が人形にしていた軽いキスとは違う。\n
ナイトメアの心は読めなくても、好きだと伝わってくる口付けだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0444
Nightmare "「どんな薬より、どんな祈りよりも。\n
君が傍にいること以上に、私を元気にしてくれる効果はないからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（聞きようによっては、酷く卑猥なことを言われているような……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（しかもこんな体勢で）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice nig_f0445
Nightmare "「卑猥って……。\n
そんな解釈をしないでくれ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は少し困ったように顔をしかめたが、すぐに表情を改めてくる。\n
万華鏡のように、変わり続ける夢魔の笑み。"

hide end_11
show end_12 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_1")
T "（私にとっては……。\n
お守りなんかより、夢魔のほうがいいわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "変わり続けるものだからこそ、一瞬たりとも見逃したくないと思える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "情けないところも、怖いところも。\n
傍にいるからこそ、見られるものだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0446
Nightmare "「現実でも君のお守りになれるのなら光栄だよ、[firstname]。\n
ずっと君の手の届くところに私を置いておいてくれ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0447
Nightmare "「君の心が私のもっとも大切なものだ。\n
他の誰にも触らせず、私にだけ守らせてくれ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "格好つけてみせる病弱な夢魔。\n
彼に言葉は必要ない。"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "答える代わりに抱きしめた。"

$ hi_mes()
show white onlayer master
with compress_extralong
hide white with compress_extralong
pause .1

$ renpy.movie_cutscene("endroll_a.mpg")
#return
