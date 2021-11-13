label fushigi_joker_3:
scene map_bg_joker_day
with dis
$ clockanim()


scene circus
with dis

play music transparent1_a_ali

scene bg_gen17_cst_a with Dissolve(1.2)
play sound se_0674

show jo_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0167
White_Joker "「これはジャグリング用のナイフ。\n
初心者用には、こっちのボールのほうがお勧めだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ふうん……」"

hide jo_t_03_7
show jo_t_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jok_f0168
White_Joker "「ふふふ、試してみる気になった、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「いいえ。\n
珍しいものがいっぱいあるなって思っただけ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "荷物を片付けているジョーカーに付き添われて、私は並べられた道具を見ている。\n
ジョーカーは私の視線を追うように、一つ一つ道具を説明してくれた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（意外と、暇なのかしら）"

hide jo_t_03_14

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーの態度はエイプリル・シーズンの最中、季節を変えに行ったときと変わらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とても人手が足りなくて、片付けに駆り出されている団長という雰囲気ではなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに物は散らばっているし、片付け真っ最中なのは分かるが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今回だけでなく、タイミングを見計らってはサーカスの内部を案内しようとするジョーカーは、とても楽しそうに見えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（もっとも、ピエロが楽しくないサーカスなんておかしいんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人を楽しませる場所がサーカスだとすれば、客を楽しませる役割は道化のものだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「ジョーカー、あなた、暇なの？」"


show jo_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice jok_f0169
White_Joker "「暇？\n
俺、そんなに暇そうに見える？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "{size=+20}「見える」{/size} "

hide jo_t_02_10
show jo_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jok_f0170
White_Joker "「そんなことはないよ。\n
俺は俺なりに、色々と忙しいんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jok_f0171
Mask "「そうそう、おまえと違って、忙しいんだよ。\n
～～～～～～」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「あなたには聞いてないわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仮面であっても、表に出てきても、こっちのジョーカーの口の悪さはいつも通りだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（それを言ったら、私も相当な暇人よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に来てから、こんなにぼうっとしたことなどなかった。\n
いつだって忙しなく、追い立てられるように動いて、働いて。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（私、何をしているんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元の世界よりも選んだ場所。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこを飛び出してやって来るには、ここはあまりにも複雑な思い出の残る場所だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "楽しいサーカスの顔と、薄暗い監獄。\n
どちらもジョーカーの領土であることに変わりはない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（今は、見えていないだけで……。\n
ここに監獄があることに、変わりはないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帰らなければと思うのに。\n
いつの間にか、ここに居心地の良さを感じていた。"

hide jo_t_02_12
show jo_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice jok_f0172
White_Joker "「どうしたの、[firstname]？\n
悩み事？」"

hide jo_t_03_2
show jo_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice jok_f0173
White_Joker "「ここはサーカスなんだから、楽しまなきゃ駄目だって言っただろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……そうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここへ来たときに、言われた言葉を繰り返される。\n
しかし今の私はとてもじゃないが、サーカスを楽しむ気分ではない。"


scene bg_gen17_cst_a_s
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（あのときに見た姉さんは、今、どこにいるんだろう）"


show t_jo3_1s onlayer master
with dis
hide jo_t_01_1

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスの公演中に何度も見た姉の姿。"

hide t_jo3_1s
show t_jo3_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "閉じ込められていなければいい。\n
どんな理由があれ、あの人があんな場所にいるなんて、間違っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（誰があの人を閉じ込めていたのかしら？）"

hide t_jo3_1
show t_jo3_1s onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのとき、鍵のかかった牢獄は、どうしても開かなかった。"

hide t_jo3_1s


scene bg_gen17_cst_a
with dis

show jo_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
White_Joker "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「？」"

hide jo_t_01_3
show jo_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice jok_f0174
White_Joker "「はい、あげる。\n
あーん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「ん！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ころん。\n
口の中に放り込まれたのは、この前と同じく何かのキャンディー。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ジョーカー！\n
あなた、また勝手に……」"

hide jo_t_01_5
show jo_t_03_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0175
White_Joker "「だって、君が浮かない顔をしているからさ。\n
元気出してもらおうと思って」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分も同じものを一つ口に放り込んで、サーカスの団長は笑う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手には缶を持っている。\n
恐らくはあの中からキャンディーを取り出したのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（問答無用で口の中に放り込むなんて……）"

play sound se_0388
hide jo_t_03_17
show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice jok_f0176
White_Joker "「うん、うまい。\n
味は変わっていないね、これもまた次の場所に持って行けそうだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（そうね、この味はこの前と同じだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "甘いのに、苦い。\n
苦いのに、癖になる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よく食べていたような、懐かしさを覚える、不思議な味。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（すっきりしているのはミントに近い感じだけど。\n
何だか、違うのよね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「これ、サーカスの公演中だけ売っていたの？\n
他の領地で売ったりとかはなかった？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "懐かしく感じるのは他の場所で食べたのに、忘れているだけなのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思って聞いてみると、仮面のジョーカーが呆れたような声で口をはさんできた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0177
Mask "「馬鹿じゃねえの。\n
客寄せの商品をそう簡単にあちこちで売るかよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0178
Mask "「価値が下がっちまったら、売れねえだろう。\n
それぐらい、すぐに分かれよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「……だから、あなたには聞いていないわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言っていることが一理あるのが、非常に腹立たしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "限定品という付加価値は、確かに大きな客寄せの因子になり得る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それはここに限らず、客を呼び込むという点では遊園地でも同じことが言えるが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（でも……。\n
遊園地にこんな味のキャンディーなんてない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "色とりどりのキャンディーを売っている遊園地の菓子屋にも、こんな味のものは売っていなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦い。\n
飲み込んでも、飲み込んでも残る苦さ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一度食べたら忘れられない、味。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（甘いのに……、変な味）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "でも、含まされたそれを吐き出そうという気持ちにはなれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "捨てるには、馴染みがあるのだ。\n
どこかで確かに私が口にしたことのある味。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただ、それがいつだったのか、どこだったのかが、思い出せない。"

hide jo_t_03_1
show jo_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0179
White_Joker "「ああ、そういえば、君には練習させてばっかりで、俺の技を見せてあげたことってなかったね。\n
[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0180
Mask "「は？\n
おい、ジョーカー、おまえ、何を考えているんだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0181
Mask "「俺は嫌だぞ。\n
面倒くせえ……、客でもねえ相手にサービスする気はねえからな」"

hide jo_t_02_11
show jo_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0182
White_Joker "「そうだね、彼女は客じゃない。\n
でも、舞台裏を覗いた、貴重な見学者だよ」"

hide jo_t_02_4
show jo_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0183
White_Joker "「特別に、少しぐらいサービスをしてあげてもいいんじゃないか、ジョーカー」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きょとんとする私をおいて、仮面と相談をしていたジョーカーは、遠くにいた子供達に手招きをした。"

hide jo_t_03_8
show jo_t_03_8 at left
show j-boy_a_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0032
Danin "「何、何かするの、ジョーカー？」"

hide j-boy_a_1
show j-boy_a_1 at center
show j-girl_a_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0027
W "「私達も一緒にやっていい？\n
ねえいいでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで離れたところで荷物を整理していた子供達もまた彼の言葉を聞きつけて、近付いてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「え？\n
一体何をするつもりなの、ジョーカー？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が何をするつもりなのか分からないのは、部外者である私だけ。"

hide jo_t_03_8
show jo_t_01_6 at center
hide j-boy_a_1

hide j-girl_a_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0184
White_Joker "「ふふ、決まっているだろう。\n
楽しいことだよ、素敵な見学者にいいものを見せてあげる」"

hide jo_t_01_6
show jo_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0185
White_Joker "「君達にも、手伝ってもらわないといけないな」"


show j-boy_a_3 at center
hide jo_t_01_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice mat_f0033
Danin "「うん、任せてよっ」"

hide j-boy_a_3
show j-boy_a_3 at left
show j-girl_a_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice nos_f0028
W "「分かったわ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0186
Mask "「まったく……、面倒なことを始めやがって。\n
俺はやらねえからな、やるなら勝手にやれよ、ジョーカー」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「……？？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（一体何をするつもりなんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この前、子供達の空中ブランコを見せてもらったばかりだ。\n
今度は一体何を見せるつもりなんだろう。"


show jo_t_01_5 at center
hide j-boy_a_3
hide j-girl_a_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0187
White_Joker "「君もすぐに帰らなくちゃいけないわけじゃないんだろう？\n
もうしばらく、ここにいればいいさ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "片目だけ覗かせた道化師は、そう言って私を案内した。"

hide jo_t_01_5

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME


play music tension_a_ali
pause .5
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「ジョーカー……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice jok_f0188
White_Joker "「何？\n
これぐらいじゃやっぱり物足りないのかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「違うわよ、逆よ、逆！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「その状態で、ひょいひょい歩かない\n
で！！」"


show j-boy_a_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice mat_f0034
Danin "「ジョーカー、残ったワイン、全部入れちゃっていいよね？」"

hide j-boy_a_14
show j-boy_a_14 at left
show j-girl_a_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice nos_f0029
W "「グラスは足りそうだから、いいわよね」"

play sound se_0575
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！！？\n
こ、これ以上、更に載せるの！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "流れる水音に、唖然としている暇もない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の悲鳴に、舞台の上で両手にグラスを持ったジョーカーは、大きく頷いて見せた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0189
White_Joker "「これぐらい大したことじゃないよ。\n
いいよ、あるだけ載せてくれる？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！？」"

show t_jo3_2 onlayer master
with dis
hide j-boy_a_14

hide j-girl_a_4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が手に持っているグラスは左右それぞれ一つだけだが、その上が恐ろしい。\n
グラスの上にトレイを載せ、その上には山のように別のグラスが載っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかも……、グラスの中にはなみなみと赤いワインを注いだ状態で。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（万が一にでもバランスを崩したら、すごいことになるわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "撤収作業どころではない、かえって悪化する。\n
その上……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（見ているほうが、心臓に悪い）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「ジョーカー、もうその辺りにしなさいよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0190
White_Joker "「ん？どうして？\n
まだまだ大丈夫だよ、このくらいで終わりにしたらつまらないじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あなたは大丈夫でも、あなたの足下のロープはたわんでいるわよ！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あろうことか、ジョーカーは綱渡りをしたまま、グラスの山を持っている。\n
この前、私が玉乗りの練習の際に頼りにしていたあのロープの上に乗って。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（どうしてこれでバランスを崩さないのか、分からないわ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "くるくると軽い足取りで行ったり来たりを繰り返すジョーカーは、スポットライトを浴びて平然としている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、見ているこっちはいつ落ちるんじゃないかと気が気ではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（客席で見るのとはまた違った臨場感よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遠目に見ているときには、あくまで演目の一つとして見られた。\n
崩れても、倒れても、それは非日常の一コマ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ガラス越しに見ている世界と、自分のいる場所は違うのだとそう思えたのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（今は、他人ごとじゃない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……あれ？\n
私、こんなにこの人のことを心配するような仲だったかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーには、特にホワイトさんには散々な目に遭わされたはずだ。\n
だが、今は落ちたら、怪我をしたらどうしようと心配している。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おかしな話。\n
私は、誰でも彼でも心配するような優しい性格ではないはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0191
White_Joker "「ははは、大丈夫だよ。\n
……っと、おや？」"

hide t_jo3_2

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐらぐらとバランスを崩したジョーカーの足下に思わず近付いて、周囲を見回す。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（何かクッションになるようなものはないかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ちるのは止めようがないとしても、グラスが砕けるのを止められれば……。"


show t_jo3_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0192
White_Joker "「君は、優しいね、[firstname]。\n
優しくて、そして……、とってもつけ込みやすい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……え？\n
ジョーカー？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（床に下りる音なんて、聞こえなかったわよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の横に立ったジョーカーはグラスを手にしたまま、首を傾げている。\n
それでも、手にしたグラスの水面は、少しも揺らいでいない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（着地しても零れないなんて、そんなことあるはずないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どんなにバランスがよくとも、これだけのグラスを落とさず、しかも中身も零さないなんて、不思議の国にしても出来すぎではないだろうか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……あなた、団長なんかにならず、どこかでウエイターでもやったほうがよかったんじゃないの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jok_f0193
White_Joker "「俺がウエイター？\n
面白いことを言うね、[firstname]」"

hide t_jo3_3

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーは少し目を開くと、突然、グラスから手を離した。\n
今までかろうじて保っていた絶妙なバランスが崩れる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「危ない！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（割れる！！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ロープの上から下りてきているから、先刻よりは衝撃も少ないだろうが、グラスが耐えられるはずがない。"


show black onlayer master with close_m
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その瞬間を見るのが怖くて、目を閉じたとき。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0194
White_Joker "「だから、ここから逃げられない」"

play sound se_0468
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（……え？）"

hide black with open_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "床に落ちて砕けるはずだったグラスは、ジョーカーの合図を受けて、姿を変えた。"

play sound se_0532

play music transparent1_a_ali
play sound se_0308
show t_cut_jo3u onlayer master
with dis


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "白い、白い鳩。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視界すべてを埋め尽くすような鳩の大群が羽ばたきの音を残して、飛んでいく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "天幕の近くまで彼らが飛び上がると、まるで出迎えるようにテントの一部が外れて空が覗いた。"

hide t_cut_jo3u
show t_cut_jo3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0035
Danin "「ばいばい～」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0030
W "「さすがジョーカーよねえ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "テントを操作していた子供達の感心したような声を聞いて、ようやく事態が飲み込める。"

hide t_cut_jo3

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……ひょっとして、ここまでが、出し物だったの？」"


show jo_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice jok_f0195
White_Joker "「出し物って……、子供の学芸会じゃないんだから。\n
せめて、技とか、もう少し言い方はあるだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「どちらにせよ、真面目に心配しただけ損した気分だわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不満を隠さず言うと、ジョーカーはますます楽しそうに続けた。"

hide jo_t_01_12
show jo_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0196
White_Joker "「君がそこまで俺のことを心配してくれるなんて、嬉しいよ、[firstname]」"

hide jo_t_01_5
show jo_t_03_19 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0197
White_Joker "「ふふふ。\n
どきどき……、したかな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "眼帯に隠されていない片目が、覗き込むように私の胸元を見てくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「……悪趣味」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その視線から逃れるように身を翻せば、そこには別の人影が立っていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！？」"

hide jo_t_03_19
show jo_t_03_19 at left
show jo_t_02_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice jok_f0198
Black_Joker "「心配っつーか、度胸がねえだけだろう、こいつの場合。\n
たかだかあれっぽっちで騒ぎやがって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「……悪かったわね。\n
慣れていないのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃弾や刃物なら、（幸か不幸か）この世界に来て大分見慣れたが、ああいった息が詰まるような緊張感を体験することには慣れたくない。"

hide jo_t_03_19
show jo_t_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0199
White_Joker "「そんなことを言うなよ、ジョーカー。\n
ジョーカーだって、心配してもらって悪い気はしないだろう？」"

hide jo_t_02_14
show jo_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0200
Black_Joker "「こいつに心配されて？\n
はっ、馬鹿馬鹿しい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「安心していいわよ。\n
あなたのことは、死にそうになっても心配してあげないから」"

hide jo_t_01_13
show jo_t_01_13 at left
hide jo_t_02_9
show jo_t_03_19 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice jok_f0201
Black_Joker "「……言うじゃねえか、この～～～～～\n
～！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぎりぎりと睨み合う私達の横で、ホワイトさんは、ぽんと手を打った。"

play sound se_0491
hide jo_t_03_19
show jo_t_03_19 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0202
White_Joker "「そうだ、ジョーカーも出てきたんだから、何かしていってよ。\n
ね？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……は？」"

hide jo_t_03_19
show jo_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice jok_f0203
Black_Joker "「ふざけんなよ。\n
見せ物になるなんざ、ごめんだぜ」"

hide jo_t_03_12
show jo_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice jok_f0204
Black_Joker "「やりたきゃ、ジョーカー、おまえがやれよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま今にも消えそうなブラックさんは、背を向けている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

menu:
    "逃げるのね？":
        jump fushigi_joker3_2a
    "見せられないの？":
        jump fushigi_joker3_2b

label fushigi_joker3_2a:
hide jo_t_01_13

hide jo_t_02_8

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（何よ。\n
偉そうなことを言っておきながら、結局口だけなの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ホワイトさんは先ほどのグラスを使った技だけでなく、他にもいろいろな手法を見せてくれている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、ブラックさんのほうは、この前の玉乗りぐらいしか見せていない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「別にいいわよ。\n
見せられるだけの芸がない人に無理矢理やらせても、可哀想だし」"


show jo_t_02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice jok_f0205
Black_Joker "「……あ？\n
今、何て言った、おまえ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "歩き出そうとしていた足を止めて、ジョーカーが振り返ってくる。\n
馬鹿にするな、とその顔には大きく書いてある。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「いるわよね。\n
口だけ達者で、実は大したことない人って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「玉乗りは上手だったけど、他には何も見せられるものがない団長さんか……。\n
あ、ごめんなさいね、馬鹿になんかしていないわよ」"

hide jo_t_02_15
show jo_t_02_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
Black_Joker "「…………」"

hide jo_t_02_14
show jo_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice jok_f0206
Black_Joker "「おまえ、俺を見くびってんのか？\n
この俺を誰だと思っているんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「誰って……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなのは、決まっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "{size=+20}「口の悪いだけの、ジョーカーでしょう」{/size} "

hide jo_t_03_10
show jo_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
Black_Joker "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "座った目で凄まれたが、私も負けずに睨み返す。\n
私達の間で再び火花が飛び散った。"

hide jo_t_03_11
show jo_t_03_11 at left
show jo_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0207
White_Joker "「ふふ、どうするの、ジョーカー？\n
言われっぱなしなんて、君らしくないけど」"

hide jo_t_03_11
show jo_t_03_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0208
Black_Joker "「……いいだろう、そこまで言うなら見せてやろうじゃねえか。\n
驚きすぎて、～～～して～～～～なことになっても、俺は責任とらねえぞ」"

$ hi_mes()
hide jo_t_03_5

hide jo_t_01_1

jump fushigi_joker3_3
label fushigi_joker3_2b:




$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（やっぱり、部外者には見せられないってことなのかしら）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「いいわよ、無理に見せてくれなくても。\n
私は元々ここの人間じゃないし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "控えめな言葉で返すと、彼は少し意外そうに振り返っていった。"


show jo_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0209
Black_Joker "「何だ、おまえ、意外と物分かりがいいじゃねえか。\n
見習えよ、ジョーカー」"

hide jo_t_02_8
show jo_t_02_8 at left
show jo_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0210
White_Joker "「えー、だって、せっかくの見学者だよ。\n
俺達にとっても、特別なお客さんなのに」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（特別なお客さんね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私はこの世界においては、いつまでも余所者のままだ。\n
どれだけの時間帯を滞在地で過ごしたとしても、それは変わらない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（それにしても、何だか今の言い方だとちょっと含みがあったような……。\n
気のせいかしら？）"

hide jo_t_01_4
show jo_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice jok_f0211
White_Joker "「君だって、見たいだろう？\n
ジョーカーに出来ることは俺にも出来るけど、俺だけじゃ物足りないだろうし」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「物足りないなんて言うつもりはないけど……。\n
そうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらりと向けた視線の先には、無愛想なもう一人の道化。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（ホワイトさんの愛想の良さと足して二で割ったらちょうどよさそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを思いながら、首を傾げる。\n
きっと拒否の返事が返ってくるだろうと思いながら。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「でも、見せてくれるのなら……。\n
見てみたいわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それは捻くれた言葉ばかり口にする私とは思えない、素直な言い方だった。\n
口にした私自身内心で驚いてしまうほどに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが驚いたのは、私だけではなかったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラックさんは目をぱちぱちとさせ、その隣ではホワイトさんが肩を揺らして笑いを堪えている。"

hide jo_t_03_2
show jo_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
White_Joker "「…………」"

hide jo_t_03_7
show jo_t_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice jok_f0212
White_Joker "「ジョーカー。\n
リクエストだよ、これでもまだ応えてあげないの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "楽しげに口の端を持ち上げたホワイトさんの言葉に、ブラックさんはしばらく黙っていたが、やがてがりがりと頭をかいて口を開いた。"

hide jo_t_02_8
show jo_t_02_17 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0213
Black_Joker "「分かったよ。\n
やればいいんだろう、やれば」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（何で、そんな簡単に）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "表情は苦々しいが、あっさりと頷いた彼の反応に私のほうが驚いてしまう。"

hide jo_t_02_17
show jo_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0214
Black_Joker "「何だよ、取り下げって言うなら聞くが……。\n
やってほしいのか、やめてほしいのか、どっちなんだよ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「や、やってくれるのなら、もちろん見たいけど……。\n
でも、いいの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラックさんの顔はとても納得している顔ではない。\n
無理強いさせてまで見たかったわけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思う私の心情とは裏腹に、彼はぶっきらぼうに是と答えた。"

hide jo_t_03_4
show jo_t_03_17 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0215
Black_Joker "「客のリクエストは断らねえ。\n
それがここのルールだからな」"

hide jo_t_03_17
show jo_t_01_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0216
Black_Joker "「見たいって言うなら見せてやるさ」"

$ hi_mes()
hide jo_t_01_9

hide jo_t_01_10

jump fushigi_joker3_3
label fushigi_joker3_3:

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music cheerful_a_ali
pause .5
play sound se_0237
show t_jo3_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「……っ、ひ、やっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice jok_f0217
White_Joker "「そんなにびくびくしないで見ればいいのに。\n
ナイフなら、君も見慣れているだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「確かに見慣れてはいるけど……。\n
こういう使い方は、見ていて落ち着かないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "刃物を持った知り合いは、この世界にごまんといるが、彼らの用途は仕事や戦いでの場面だけだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つまりその切っ先が自身に向かうことはない。\n
しかし、これは違う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（あ、また手に当たりそうっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "くるりと回転した刃の先端が、ジョーカーの手に落ちそうになる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0218
Black_Joker "「この程度のジャグリングなんて、基礎だぜ、基礎。\n
いちいち、びびっていたらきりがねえよ」"

play sound se_0237
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "息を飲む私の前で、軽々と切っ先を掴んだジョーカーは再びそれを空中へと放り投げる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何本もの刃が虚空でダンスを踊るように回転を続ける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（確かに言うだけのことはあるわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ホワイトさんがそうだったように、彼もただジャグリングを続けているだけではない。"

play sound se_0125
pause .2
play sound se_0563
hide t_jo3_4

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「ジャグリングしながら、的当てって……。\n
どれだけ器用なのよ、あの人」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかも、ナイフは綺麗にど真ん中を貫いている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（普通、的の真ん中に当てるだけでも大変だっていうのに）"


show jo_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jok_f0219
White_Joker "「ははは、やろうと思えばもっと難しい技も出来るけど……。\n
見てみたい？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「遠慮するわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（玉乗り一つまともに出来ない身としては、さすがに落ち込む）"

hide jo_t_01_2
show jo_t_01_2 at left
show jo_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice jok_f0220
Black_Joker "「ふん、これぐらいでへこむんじゃ、大したことねえな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後のナイフを投げて、的に当てたジョーカーは、腰に手を当てて私を見下ろしてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私はそれほど不器用なほうではないと思っていたが、彼らを見ていると自分がどうしようもなく不器用な人間に思えてくる。"

hide jo_t_03_10
show j-boy_a_5 at center
hide jo_t_01_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0036
Danin "「大丈夫だよ、練習すればうまくなるよ！\n
ジョーカーみたいにはいかないけど」"


show j-boy_a_5 at left
hide j-boy_a_5
show j-girl_a_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0031
W "「そうよ、そうよ。\n
私達だってうまくなったもの」"

hide j-girl_a_3
show j-girl_a_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0032
W "「ジョーカーよりは下手だけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その子供達の足元にも及ばない素人には、言葉がなかった。"

hide j-boy_a_5

hide j-girl_a_15


show jo_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0221
Black_Joker "「当ったり前だ。\n
おまえらに簡単に追い越されるぐらいだったら、俺はとっくにここを出ていってるぜ」"

hide jo_t_03_12
show jo_t_03_12 at left
show jo_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0222
White_Joker "「まあまあ。\n
実際、ジョーカーが一番うまいんだから、いいじゃない」"

hide jo_t_03_12

hide jo_t_02_6
show jo_t_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0223
White_Joker "「もっとも……、君が一番上手になりたいっていうのなら、手伝ってあげるけどね。\n
[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……そんな気はないわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ここにいつまでもいる気はないもの）"

hide jo_t_03_14
show jo_t_03_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jok_f0224
White_Joker "「ふうん、君がそれでいいならいいけど。\n
そうだ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぽんと彼が手を打てば、手の間には小さな缶が一つ現れた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（相変わらず手品じみたことを……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「これって……、先刻のキャンディーが入っていた缶？」"

hide jo_t_03_16
show jo_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice jok_f0225
White_Joker "「そうだよ。\n
せっかくだから、頑張っている君にあげる」"

hide jo_t_01_13
show jo_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice jok_f0226
White_Joker "「君も気になっていただろう？\n
まだたくさん入っているから、好きなだけ食べていいよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（確かに気になっていたけど）"

hide jo_t_01_5

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何故だろう。\n
確かめてしまうのが怖いような……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "知ってしまうと、後戻りはできない。\n
たかが飴なのにそんなふうに思ってしまう。"

play sound se_0388
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "缶を振ると、中からは固い音が聞こえた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "中に入っているのは、キャンディーのはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（もっと重いものを持っているような気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キャンディーとは比べようもないほど重いもの。\n
そう、例えば……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（何かの金属のような）"


show jo_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice jok_f0227
White_Joker "「君にとって、気になる味なら……。\n
それはきっと無視してはいけないもののはずだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（この人は何を知っているんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "笑う道化師と、愛想のない道化師。\n
どちらも同じ顔で、違う顔。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（何でだろう）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（キャンディーと同じでこの人に深入りしたら、もう二度と以前には戻れなくなりそうな……、そんな予感が……）"

$ hi_mes()
hide jo_t_01_1


scene circus
with stripe_l_medium

scene map_bg_joker_day
with stripe_l_long
##endmemory
jump fushigi_joker_4 ##I think
