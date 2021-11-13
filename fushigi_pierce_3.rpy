jump fushigi_common3_hatter
label fushigi_pierce3_1:
$ hi_mes()

scene map_bg_autumn_day
with stripe_l_medium

scene b_aut_01
with stripe_l_medium

scene bg_01
with stripe_l_long

play music hatter_guestroom_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（そういえば、あれからピアスの姿を見ないけど……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（今頃、どうしているのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスは、帽子屋ファミリーの一員だ。\n
となれば、仕事絡みでこの屋敷に来ることもあるだろうと思っていたのだが……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……全然来る気配がないのよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットにも聞いてみたところ、少なくとも屋敷の中で最近見たことはないらしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「外に、仕事に出突っ張りとか？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（少し、様子を見に行ってみようかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼もマフィアの一員だ。\n
何も出来ない私に心配されなければならないほど弱くはない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とはいえ、またどこかで泣いているんじゃないかと思うと、つい気になってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（悪いことが分からないネズミなのに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（悪いことをしたのは、向こうなのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "置いてきたという状況に私のほうが罪悪感を覚えるなんて、不条理だ。\n
行動したなら、割り切ればいい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつまでも悩み続けるのは私の悪い癖。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「いいわ、とりあえず会いに行っちゃおう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（元気な顔を見たら、それはそれで頭に来るかもしれないけど……。\n
このまま考えてばかりじゃ仕方ないもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "滞在先に戻るわけではなく、一目見るだけなら問題ないはずだ。"

play sound se_0275
pause .5
play sound se_0774

scene br_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう決まれば、あとは早い。\n
借りている客室から出て、歩き出すと……。"

play sound se_0554
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あ、ご、ごめんなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "角を曲がったところで、誰かとぶつかった。"


show eri_t_03a_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0193
Elliot "「おっと……、悪い、あんたか。\n
いきなり飛び出してくるから、誰かと思ったぜ」"

hide eri_t_03a_4
show eri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0194
Elliot "「どうした？\n
出かけるのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋から飛び出した私を受け止めたエリオットは、首を傾げて聞いてくる。\n
彼自身仕事の途中なのか、片手には書類を持ったままだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ええ、ちょっと外に行ってくるわ」"

hide eri_t_01_8
show eri_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice eri_f0195
Elliot "「外、か……、まあ、あんたならいいか。\n
気を付けて行ってこいよ」"

play sound se_0773
hide eri_t_01_3

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットはそんなことを言いながら、慌ただしく歩いて行く。\n
あの方向からすると、恐らくブラッドの部屋に行くのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（……エリオットには一応断ったし、皆に言付けなくてもいいわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "客という分を弁えるのであれば、恐らく主に外出の旨を伝えるのが筋かもしれないが、エリオットが行ったあとに割り込んでは、仕事の邪魔になってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（少しの間だけだもの。\n
すぐに行って、戻ってくればいいものね）"

$ hi_mes()

scene charasel_bg_hatter_day
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_medium

scene charasel_bg_amuse_day
with stripe_l_medium

scene yun_sum_01
with stripe_l_long
play sound se_0556

play music amuse_gate_p_ali

show dee_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0429
Dee "「うわー、兄弟、見てよ、あれ。\n
また変なのが出来ているよ！」"

hide dee_t_02_4
show dee_t_02_4 at left
show dam_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0430
Dam "「あっちの玩具もすごいよ、兄弟。\n
買って帰るのは嫌だけど、試しに遊んでみようよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "左右から聞こえてくる弾んだ声は、遊園地の喧噪にも負けていなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（一人で遊園地に行って、さっさと戻ってくるだけだと思っていたのに）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「ディー、ダム。\n
どうして、あなた達まで一緒に来ているの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "門番の彼らがサボるのはいつものことだが、だからといって居候の私についてくる理由はないだろう。"

hide dee_t_02_4
show dee_t_01_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0431
Dee "「護衛だよ、護衛。\n
お姉さんは可愛いから、誰かに取られちゃわないように見張っていなくちゃ」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「見張るって……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（そもそも、ここは私の住んでいる場所でもあるんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず絶句した私の前で、今度はダムが手を引いて言う。"

play sound se_0055
hide dam_t_02_4
show dam_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0432
Dam "「そうだよ。\n
僕達、いい子だから……、お姉さんをどっかの馬鹿ネズミになんて、攫わせたりはしないからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え……、ピアス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界にどれだけネズミがいるのかなど知らないが、彼らがそういう呼び方をするのはたった一人しかいない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ピアスが私を攫うって……。\n
どういうことよ？」"

hide dee_t_01_7
show dee_t_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice dad_f0433
Dee "「……何でもないよ。\n
お姉さんには内緒の話」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慌ててダムと目配せをしたディーはそう言ったが、私の中の疑問は消えない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_16")
T "（ひょっとして、ピアス、帽子屋屋敷に来ていたの？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（だったら会いに来てくれればよかったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "知らない間に来て、そして知らない間に帰っていくなんて冷たい話だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（顔を合わせづらかったなんて、殊勝な性格とも思えないし）"

hide dam_t_01_3
show dam_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice dad_f0434
Dam "「そんなことよりも、お姉さん。\n
せっかく遊園地にいるんだもん、遊ぼうよ」"

hide dee_t_01_11
show dee_t_02_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice dad_f0436
Dee "「お勧めのところに連れて行ってよ。\n
お姉さんがどんな物が好きなのか、僕達は知りたいんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「わっ、ちょ、ちょっと！\n
案内って言ったって……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（私がここから飛び出していった人間だってこと、忘れていない！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "園内については、彼らよりも詳しいだろうが、こっそり入るはずだった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが正面から双子と共に入園したものだから……、入り口にいた従業員の驚いた顔が思い出される。"

hide dam_t_01_9
show dam_t_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0437
Dam "「僕達、お姉さんの護衛でついてきたんだよ。\n
だから、ご褒美に僕達を楽しませてくれなくちゃ」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐいっと引っ張る二人の手は、半強制的に私を連れて行く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あ……、待ってってばっ」"

hide dee_t_02_1
show dee_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice dad_f0438
Dee "「あっちに行こうよ、兄弟。\n
ぐるぐるぐらぐら滑り台だって……、どの程度ぐるぐるでぐらぐらなのか気になるよ」"

hide dam_t_02_1
show dam_t_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice dad_f0439
Dam "「あっちのスピード・シーソーもいいな。\n
ねえ、お姉さん、どっちがお勧めかな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（だから、案内するなんて言ってないでしょうがっ）"

hide dee_t_03_4

hide dam_t_02_5

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play sound se_0624

play music amuse_inside_p_ali

show dee_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0440
Dee "「あー、楽しかった！\n
遊園地はいいよね、遊ぶ場所に事欠かないや」"

hide dee_t_01_6
show dee_t_01_6 at left
show dam_t_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0441
Dam "「お姉さんがいるおかげで、乗り物もフリーパスだし。\n
ただで乗り放題なんて、最高」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「あれは、フリーパスというのとは違う気がするんだけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（何というか、こう……。\n
これ以上機嫌を損ねないように気遣われていたような）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私がどんな理由で遊園地を飛び出していったのかは、同僚も知っているはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その私を咎めることもなく、むしろ歓迎するかのようにアトラクションに案内してくれていたということは……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ゴーランドあたりが、何か言ってくれているのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼のことだから、私が遊園地に来ていることぐらいどこかで察しているのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（それにしても……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子と一緒に出歩きながら、あちこち見て回ったが、ピアスの姿は見つからなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「遊園地にいないのかしら」"

hide dee_t_01_6
show dee_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice dad_f0442
Dee "「お姉さん、どうしたの？\n
何か捜し物があるなら、一緒に探してあげる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「そういう訳じゃないんだけど……」"

hide dam_t_01_7
show dam_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice dad_f0443
Dam "「じゃあ、どうしたの、お姉さん？\n
先刻からあっちこっち見てばかりじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（よく見ているわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊ぶのに夢中になっているのかと思えば、どうやらそれだけではなかったらしい。\n
外見のせいで忘れそうになるが、この子達は隙がない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（でも、この子達と一緒にいたら……。\n
間違いなく、ピアスは逃げるわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "哀しき、いじめられっ子属性。\n
二人の姿を見たら、本能的に逃げ出すに決まっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（この子達がいないところで、会いに行くには……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「ねえ、二人とも。\n
せっかくだから、鬼ごっこしましょうよ」"

hide dee_t_02_11
show dee_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice dad_f0444
Dee "「鬼ごっこ？\n
でも、ここには遊園地の従業員しかいないけど……」"

hide dam_t_02_9
show dam_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice dad_f0445
Dam "「あの人達、うるさいからあんまり追いかけ甲斐がないんだよね」"

play sound se_0675
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "チャキッ、と斧を出し始める双子に、慌てて違うと言葉を続ける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「そうじゃなくて、あなた達が逃げて、私が追いかけるの」"

hide dee_t_01_5
show dee_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Dee "「……？」"

hide dam_t_02_12
show dam_t_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Dam "「？？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……あまり、楽しくない？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（別行動したいのがばれちゃったかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きょとんと揃って首を傾げている二人に確認すると、彼らは一瞬視線を交わしたあと、手を叩いた。"

hide dee_t_01_10
show dee_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0446
Dee "「お姉さんが追いかけてくれるなんて……。\n
これってすごいことだよ、兄弟！！」"

hide dam_t_01_10
show dam_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0448
Dam "「うん、楽しみだね。\n
どこまで逃げても追いかけてきてくれるお姉さんなんて……、可愛い」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（気付かれていない？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさかこうもうまく話が進むとは思っていなかったのだが、単独行動が出来るのならそれに越したことはない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「ええ、早速鬼ごっこをはじめましょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「ただし、範囲は、遊園地園内にすること。\n
終了は、この時間帯が変わるまでよ」"

hide dee_t_02_6
show dee_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice dad_f0449
Dee "「うんうん、分かったよ、お姉さん」"

hide dam_t_01_13
show dam_t_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice dad_f0450
Dam "「ふふふ、どこに逃げようかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「それじゃあ、私が数えるから逃げていいわよ」"

hide dee_t_02_10
show dee_t_03_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice dad_f0451
Dee "「うん、負けないよ」"

hide dam_t_02_5
show dam_t_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice dad_f0452
Dam "「行こう、兄弟」"

play sound se_0004
hide dee_t_03_13

hide dam_t_03_4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "早速走り出していく双子の姿に、少し胸が痛む。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「ごめんね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（顔だけ見たら、ちゃんと追いかけるから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "青と赤の制服が見えなくなるのを確認してから、私はそっとその場を離れた。"

$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME

scene bg_gen_sky_sum_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「ピアスの家って、確かこのあたりだと思ったんだけど……。\n
やっぱり見つからないわよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスの家は特別製だ。\n
ただし、帽子屋屋敷やハートの城といった大きな領地にある建物とは、逆の意味で。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ボリスに見つからないように、すごく小さくなっているのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の家に入るには、身体を小さくするしかない。\n
その薬は簡単に買えるようなものではないらしいということも聞いていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（何しろ、「私を飲んで」って喋る薬だもの……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこらへんでほいほいと売られていては堪らない。"

play sound se_0518 volume .4
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（銃の音？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後から聞こえてきた音に振り返るが、そこには誰もいない。\n
しかし……。"

play sound se_0502 volume .4
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「幻聴って感じじゃないわよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何度か、遠くで音が繰り返されている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の人間が銃を携帯していることなんて、珍しくもない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひょっとしたら、ピアスがいるかもしれない。\n
ただそれだけの理由で、足を向けてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（危ないと思ったら、離れよう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子を巻いてまで行った先で怪我をしたのでは、彼らに合わせる顔がない。"

$ hi_mes()

scene bg_gen12_yuk
with stripe_l_long
play sound se_0240

play music amuse_inside_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あの音は……！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞き慣れてしまった不吉なスコップの音に、今は駆け寄ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "長い時間帯を離れていたわけではないが、姿が見えないと心配になる。\n
家出してはいるものの、ピアスのことを嫌いになったわけではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（ただ……、分かってほしかっただけなのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に来たときと同じで、私の常識を理解してほしいという、我侭だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0184
Pierce "「あーあ……。\n
困ったなあ、早く片付けが終わらないと、またあの子に会いに行けないよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0185
Pierce "「困ったな、困ったな。\n
でも、綺麗に片付けないといけないし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "森の木々に遮られて姿は見えないが、確かにピアスの声がする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（……？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（あれ、でもピアスにしてはシルエットが少し大きいような……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "木々の合間からちらちらと見えるものは、いつもの帽子でもなければ、上着のようにも見えない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（赤っぽく見えるけど……。\n
まさか、返り血とかじゃないでしょうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事中のピアスだったら充分ありうることだけに、思わずげっそりとしてしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……ピアス？」"


show pia_f_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
Pierce "「！！」"

hide pia_f_01_3
show pia_f_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice pie_f0186
Pierce "「[firstname]、え、どうして、どうしてここに来てくれたの！？\n
俺、君のことずっと考えていたんだよっ！」"

hide pia_f_01_11
show pia_f_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice pie_f0187
Pierce "「ナイトメアみたいに、君も俺の声が聞こえたの？\n
嬉しい、嬉しいなあ……」"

play sound se_0125
pause .5
play sound se_0240
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "スコップを放り出したピアスは感動しているらしいが、私の思考は完全に凍りついている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "返り血は、まだ予想の範囲だ。\n
仮に身体についているものが、もっと物騒なものだったとしても、ここまで驚かない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……何で、そんな服を着ているの？」"

hide pia_f_01_2
show pia_f_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice pie_f0188
Pierce "「あ、これ？\n
えへへ、可愛いでしょう？」"

play sound se_0379 volume .8
hide pia_f_01_6
show pia_f_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice pie_f0189
Pierce "「オーナーさんの家にあったから、借りてきたんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "くるくると回るピアスは、人形のように可愛らしいと言ってもいいだろう。\n
しかし、問題はピアスの着ているものにある。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（可愛いというよりも不気味だし、何よりも）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "{size=+20}「返り血がついたお花じゃ、可愛いとはとても言えないんだけど」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い花弁も、緑の茎部分も……、どこもかしこもまんべんなく血がついている。\n
これでは血の花だ。"

hide pia_f_01_10
show pia_f_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0190
Pierce "「えっ、ええ、そうなの？\n
でも、仕方ないんだ、仕事が入っちゃったから、早く片付けないとボスに怒られるし」"

hide pia_f_01_3
show pia_f_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0191
Pierce "「この格好なら、君に会いに行っても怒られないと思ったんだけどなあ……、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「……怒りはしないけど、少なくとも、その格好で出てきたら驚くわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もう慣れてしまって感覚が麻痺しているが、いつもの服装よりも奇抜だ。\n
着ぐるみとまではいかないが、派手な色の服になにやら花が散りばめられていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも以上にメルヘンなのにも関わらず、血で染まっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つまり、いつもよりますますシュールさが増していた。\n
下手なホラー映画よりも恐ろしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（Ｂ級映画みたいな、食虫植物を思い出しちゃったじゃない）"

hide pia_f_01_8
show pia_f_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice pie_f0192
Pierce "「そうか、銃で撃って埋めるんじゃなくて、別の方法にすればよかったんだね。\n
そうすれば、血がつくこともなかったし……」"

hide pia_f_01_13
show pia_f_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice pie_f0193
Pierce "「あれ、そういえば……。\n
[firstname]、君、遊園地にいなかったはずなのに、帰ってきてくれたの！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「帰ってきたというのとはまたちょっと違うんだけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この困ったネズミさんが何かしでかしてはいないかと、心配になって様子を見に来たというのが正解だ。"

hide pia_f_01_2
show pia_f_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0194
Pierce "「よかった、よかった！\n
俺もね、君に会いたかったんだよ、[firstname]！！」"

play sound se_0051
hide pia_f_01_6

camera at hpunch
camera at vpunch
show t_pia3_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「うわっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "返り血がべっとりとついたピアスが抱きついてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、安心したように私を見上げている顔を見ていると……、無碍には振り払えなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0195
Pierce "「うわー、君に触るの、すごい久しぶりだなあ。\n
俺ね、君がボスのところにいるって聞いて、何回か会いに行ったんだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……？\n
ピアスに会えたのは、ディーやダムとトランポリンをしていたときだけじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋屋敷の領地内で彼の姿を見たのは、あれっきりだ。"

hide t_pia3_1
show t_pia3_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0196
Pierce "「だって、双子が酷いんだよっ。\n
あいつら、俺のこと、中に入れてくれなかったんだもん！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0197
Pierce "「俺、こんなに……、こんなに君のことが好きなのに、酷いよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "酷い酷いと繰り返すピアスは既に半泣き状態になっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（ディーとダムが？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……二人とも、ピアスが私に会いに来たなんて、私には言っていなかったけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ディーとダムが零した言葉から、ピアスが帽子屋屋敷に来ていただろうことは察していた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "てっきり仕事に来ていたのかと思っていたが……、違うようだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0198
Pierce "「君は俺が拾ったのに……、なのに。\n
あいつら、俺から君を盗ろうとしているんだよ、[firstname]」"

play sound se_0553
camera at hpunch
camera at vpunch
hide t_pia3_2
show t_pia3_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不意に、ぐいっと肩を押されて、バランスを崩し地面に座り込む。\n
何が起きたのかと首を傾げれば、膝をついたピアスに押し倒されていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「あの、ピアス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "花のスーツを着たネズミを見上げても、現実感がない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その上、綺麗な顔に笑みを浮かべながら、ナイフを突きつけられては、ますます冗談のような光景だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0199
Pierce "「[firstname]、君、あいつらのものになっちゃったの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice pie_f0200
Pierce "「ねえ……、君も俺のこと、嫌いになっちゃったの？\n
俺から離れていくの、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "シュール過ぎる視界の中で、間近に迫った眼だけが、酷く真剣に見える。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（……寂しそう）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice pie_f0201
Pierce "「誰かに取られるくらいなら……、君も、俺が隠しちゃっていい？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……いいわけがないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "投げ捨てられたスコップ。\n
彼にとって隠すということは、あれのお世話になるということだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0202
Pierce "「大丈夫だよ。\n
俺、隠すのと片付けるのは上手だから、誰にも見つけさせない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「そういう問題じゃないわよ。\n
私は埋められるのも、隠されてしまうのも、嫌だもの」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice pie_f0203
Pierce "「……どうして？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「あなたと同じよ、私も、一人は嫌い」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "地面の下に埋められて、寂しく眠るなんて……。"

hide t_pia3_3
show white with Dissolve(.1)
hide white
show t_pia3_4 with Dissolve(.1)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何故だろう、その光景を思った瞬間、胸が痛んだ。"

hide t_pia3_4


show pia_f_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0204
Pierce "「ぴ？\n
[firstname]、[firstname]、どうしたの、苦しいの？」"

hide pia_f_01_8
show pia_f_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0205
Pierce "「わわわ、どうしよう、どうしよう。\n
何かあったかな、チーズは持っていないし……、ええとええと」"

play sound se_0052
pause .5
play sound se_0086
play sound se_0086
hide pia_f_01_3
show pia_f_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Pierce "「！！！！？」"

hide pia_f_01_9
show pia_f_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0206
Pierce "「ぎゃあああっ、ディー、ダム！！？\n
な、なんでこんなところにっ」"


play music opposition2_a_ali
hide pia_f_01_4
show pia_f_01_4 at left
show dee_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0453
Dee "「このネズミ、まだ懲りていなかったんだね」"

hide pia_f_01_4

hide dee_t_01_8
show dee_t_01_8 at left
show dam_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0454
Dam "「……馬鹿だから、忘れちゃったんだろうけど。\n
今回ばかりは、もう見逃さないよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「二人とも……」"

play sound se_0676
##special anime kiseki01
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "前触れなく現れた双子は、ピアスに斧を振りかざす。\n
ギリギリのところで避けたものの、二対一では分が悪い。"

play sound se_0565
##special anime kiseki02
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の上から退いたピアスを、ダムが続けて攻撃した。"

hide dam_t_01_8
show dam_t_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0455
Dam "「今度お姉さんに近付いたら、切り刻むって言っておいただろう、馬鹿ネズミ！」"

hide dee_t_01_8
show dee_t_02_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0456
Dee "「お姉さん、大丈夫？」"

play sound se_0063
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って伸ばしてくれた手を借り、立ち上がる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子は斧を構え、私を背後に庇うように立っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどの鬼ごっこを提案したときとは真逆の、「ブラッディ・ツインズ」の呼び名が相応しい、物騒な笑みを浮かべて。"

hide dee_t_02_9
show dee_t_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0457
Dee "「すぐ片付けるから、ちょっとだけ待っていてね。\n
見たくないなら、少し離れていたほうがいいかも」"

hide dam_t_02_13
show dam_t_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0458
Dam "「僕達、片付けはあんまり上手じゃないけど、でも、頑張るからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「な」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（何を待って、何を頑張るっていうのよ、あんた達はっ！？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「ちょっと待ちなさい！\n
ピアスは仲間でしょう、何でそんなに本気モードになっているのよっ」"

hide dee_t_03_1
show dee_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_9")
Dee "「…………」"

hide dam_t_03_1
show dam_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_9")
Dam "「…………」"

hide dee_t_03_11

hide dam_t_03_11


show pia_f_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_9")
voice pie_f0207
Pierce "「ぴっ！\n
あわわわ、あわわ、逃げたいけど……」"

hide pia_f_01_8
show pia_f_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_9")
voice pie_f0208
Pierce "「でも……、逃げたら、君を盗られちゃうし。\n
うう……」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスは青ざめながらも、必死にナイフを握っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（逃げない？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの彼なら、とっくに尻尾を巻いて逃げ出している場面だ。\n
天敵のボリスではないが、彼にとって双子は大きな脅威のはず。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その態度を不思議に思ったのは、私だけではなかったらしい。"

play sound se_0674
hide pia_f_01_4
show pia_f_01_4 at left
show dee_t_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0459
Dee "「ふうん、やる気なんだ？\n
ピアスのくせに、やる気を出すなんて……」"

play sound se_0674
hide pia_f_01_4

hide dee_t_02_13
show dee_t_02_13 at left
show dam_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0460
Dam "「馬鹿なネズミだから、勝ち目がないのが分からないんだよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後通牒のように刃を打ち鳴らしたディーとダムは、そう言って斧を構えた。"

hide dee_t_02_13

hide dam_t_02_2
show dam_t_02_2 at left
show pia_f_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0209
Pierce "「だ、だって、俺だってその子を盗られるのは嫌だよ！\n
誰にだってあげたくないよっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ピアス……」"

play sound se_0676
##special anime kiseki03
hide dam_t_02_2

hide pia_f_01_7

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「！！！」"

menu:
    "ピアス！！":
        jump fushigi_pierce3_5a
    "二人ともやめなさい！":
        jump fushigi_pierce3_5b

label fushigi_pierce3_5a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「ピアス！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らの強さも、怖さも充分知っているはずだった。\n
その手に持つ斧の切れ味も。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ならばどうして、反射的に躍り出てしまったのか。"


show t_pia3_5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0462
Dee "「っ！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0463
Dam "「……っ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子の振りかざした斧が二丁、ぎらぎらと陽光を弾いて私の目の前にある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで間違いなく殺気に染まっていた双子の雰囲気が、少し緩んでいた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Pierce "「[firstname]……？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……そこまでにしてよ、三人とも」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後にいるピアスの気配もまた、落ち着かないのは変わらないが、少なくともナイフを振り回すようなことはないらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（あと、一歩ずれていたら……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスではなく、私がざくざくされていたことだろう。\n
無茶、無謀の塊のような行動だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも……。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0210
Pierce "「え、君……、俺のこと、庇ってくれたの、[firstname]？\n
どうして？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "泣き出しそうな声で後ろからかけられる声に、力が抜ける。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（……本当は腰が抜けそうだけど、もう少しだけ格好をつけさせてよ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「いいから、とりあえず状況説明をしてちょうだい。\n
あと、三人とも……」"

play sound se_0444
camera at hpunch
camera at vpunch
pause .5
play sound se_0445
camera at hpunch
camera at vpunch
pause .5
play sound se_0446
##special anime hit_center
camera at hpunch
camera at vpunch
hide t_pia3_5
show bg_gen_sky_sum_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットほどではないが、固く握りしめた拳の威力は、
頑丈に出来ている彼らにも有効だったらしい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice dad_f0464
Dee "「つううっ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice dad_f0465
Dam "「いったい……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice pie_f0211
Pierce "「ちゅうう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "三人全員に対して平等に一発ずつげんこつをお見舞いしてから、私は腰に手を当てて言った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「仲間同士で争ってどうするの！\n
悪い子にはお仕置きよ、反省しなさいっ」"

hide bg_gen_sky_sum_day

jump fushigi_pierce3_6
label fushigi_pierce3_5b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「二人とも、いい加減にしなさい！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今にも飛び出しそうになっている二人の服を掴むと、彼らは驚いたように私を振り返った。"


show dee_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0466
Dee "「えー？\n
僕、この馬鹿ネズミを斬り刻みたい」"

hide dee_t_01_4
show dee_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0467
Dee "「こんなのにお姉さんが優しくしてあげる必要なんてない」"

hide dee_t_01_1
show dee_t_01_1 at left
show pia_f_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0212
Pierce "「うう、ひどい。\n
俺、確かに頭はよくないけど……」"

hide dee_t_01_1

hide pia_f_01_8
show pia_f_01_8 at left
show dam_t_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0468
Dam "「馬鹿だから、馬鹿なんだよ。\n
おまえなんか、もういらない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いらない。\n
端的な言葉だが、それは私にも突き刺さる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（この二人は……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（いらないなんて、言わないでよ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

play sound se_0446
camera at hpunch
camera at vpunch
play sound se_0445
##special anime hit_center
camera at hpunch
camera at vpunch
hide pia_f_01_8

hide dam_t_02_13
show dam_t_02_13 at left
show dee_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice dad_f0469
Dee "「いったあ！！」"

hide dam_t_02_13
show dam_t_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice dad_f0470
Dam "「うう……、じんじんする」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "痛そうに頭をさする二人を見下ろしながら、私は息をついた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「いくらなんでも言いすぎよ。\n
それ以上言ったら、ブラッドに言って休憩減らしてもらって、減給してもらうからね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすがにこの脅しは利いたらしい。\n
一瞬にして双子の顔色が変わる。"

hide dee_t_02_7
show dee_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dee "「！！？」"

hide dam_t_02_3
show dam_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普通に考えれば、客の身分である私が言ったぐらいで部下の休暇や給料が変わるはずもないが、何しろ帽子屋屋敷の主は気紛れな男だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "面白いと判断すれば、本当にやりかねない。"

hide dam_t_02_6
show dam_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0471
Dam "「ひ、酷いよ、お姉さん。\n
お姉さんを思ってのことだったのに……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもなら彼らの涙ぐんだ眼差しに私は滅法弱いが、今回ばかりは許容出来ない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「泣いても駄目！\n
あと、ピアスも……、いい加減そのナイフを下ろしなさい！」"

hide dam_t_01_5

hide dee_t_02_6
show dee_t_02_6 at left
show pia_f_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice pie_f0213
Pierce "「ぴっ。\n
う、うん、分かったよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そろそろとナイフをしまうネズミを見て、ようやく私も腰に当てていた手を下ろした。"

hide dee_t_02_6

hide pia_f_01_3

jump fushigi_pierce3_6
label fushigi_pierce3_6:
$ hi_mes()

scene yum_sum_01_1
with stripe_l_medium

scene s2_01
with stripe_l_long

play music forest1_p_ali

show dee_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0472
Dee "「だって、この馬鹿ネズミがお姉さんを哀しませたって聞いたから……。\n
お姉さんを傷つけるような遊園地になんて、帰さなきゃいいと思ったんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「それで、帽子屋屋敷に来たピアスを追い出していたわけ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子は私の確認するような声に、こくんと頷いた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスの片付けが終わった現場で話すのは気が引けたので、少し離れた森の一角に、私達は座っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（端から見たら、何の集会かと思うわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とりわけ、花のスーツを着たネズミなんて、シュールの極みだろう。"

hide dee_t_01_1
show dee_t_01_1 at left
show dam_t_01_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0473
Dam "「なのに、ピアス、性懲りもなく何度も来るから……。\n
もうこれは片付けるしかないと思って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「……極端な結論でしょう、それは」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "物騒な子供達なのは知っているが、多少の喧嘩を理由に仲間を刻むのはいきすぎだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今も二人がピアスを見る眼は、険悪そのもの。\n
ぴりぴりしている。"

hide dee_t_01_1
show dee_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0474
Dee "「だって、僕達のお姉さんを独り占めしているだけでも許せないのに、そのお姉さんを哀しませたんだ」"

hide dee_t_01_5
show dee_t_02_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0475
Dee "「そんなの、許せないよ」"

hide dee_t_02_9

hide dam_t_01_12
show dam_t_01_12 at left
show pia_f_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0214
Pierce "「ちゅう……。\n
[firstname]、君、そんなに哀しかったの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（こっちはこっちで状況がよく分かっていないみたいだし）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「……哀しかったわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒っていることも、哀しんでいることも分かってもらえないなんて、辛かった。\n
罪悪感を持たないネズミでも、感情を知らないわけではないはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（伝わらないのが、一番きつい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地で一番近くにいたのは、彼だったからこそ、そう思う。"

hide pia_f_01_13
show pia_f_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0215
Pierce "「……ごめん、[firstname]。\n
あれがそんなに大事なものだなんて、思わなかったんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「もういいわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（とっくに怒りなんか冷めちゃったわよ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「だって、私の分まで……。\n
二人のほうが怒ってくれたみたいだし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ようやく表情を緩めると、双子ははっと顔を上げた。"

hide dam_t_01_12

hide pia_f_01_8
show pia_f_01_8 at left
show dee_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0476
Dee "「……お姉さん。\n
僕達のことも、もう怒っていないの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「……うん、怒っていないわよ」"

hide pia_f_01_8

hide dee_t_03_10
show dee_t_03_10 at left
show dam_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice dad_f0477
Dam "「……じゃあ、また僕達とも遊んでくれる？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「ええ、危なくないものならね。\n
鬼ごっこも途中になっちゃったし、また遊びましょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒っていないと示すように提案すると、二人は飛び上がって喜んだ。"

hide dee_t_03_10
show dee_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice dad_f0478
Dee "「やったあ！\n
よかった、僕、このままお姉さんに嫌われたらどうしようかと思ったんだ」"

hide dam_t_03_10
show dam_t_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice dad_f0479
Dam "「うん、僕もすごい心配だったんだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「どうしたの、ピアス？」"

hide dee_t_02_4

hide dam_t_02_5


show pia_f_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pie_f0216
Pierce "「だって、ディーやダムと遊ぶってことは……。\n
君、まだボスのところにいるんでしょう？」"

hide pia_f_01_1
show pia_f_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pie_f0217
Pierce "「俺、君が遊園地に帰ってきてくれると思っていたのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しょんぼり。\n
そんな擬音を書き込みたくなるような様子で、ピアスは肩を落としていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「そういうときにはね、ピアス」"

hide pia_f_01_13
show pia_f_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Pierce "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「帰って来てって、お願いするものよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（馬鹿みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "花のスーツに包まれたファンシーなネズミに、お願いを強請るなんて。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし。"

hide pia_f_01_3
show pia_f_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0218
Pierce "「分かったよ、[firstname]！\n
俺のところに帰ってきてほしいから、帰ってきて！」"

##play sound se0051
hide pia_f_01_7

camera at hpunch
camera at vpunch

show t_pia3_6 onlayer master
with dis

play music happy_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然唇を重ねられて、驚きに目を見開く。\n
左右にいる双子からは、不満の声があがる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0480
Dee "「あーー！\n
おまえ、お姉さんに何しているんだよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0481
Dam "「お姉さんから離れろっ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0219
Pierce "「約束のちゅうだよ。\n
君は賢いから大丈夫だろうけど、忘れないようにおまじない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0220
Pierce "「俺は臆病なネズミだから、何か記憶に残るようなものがないと安心出来ないんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ピ、ピアス……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこっと微笑まれて、顔が真っ赤になる。\n
久しぶりのキスにはどこか血の香りさえ漂っていたのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（ピアスらしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思ってしまったことが、何故か気恥ずかしい。"

hide t_pia3_6

$ hi_mes()

scene charasel_bg_amuse_day
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_long
##endmemory
label fushigi_end_check_amuse1_p:
if renpy.seen_label("fushigi_end_gowland1") == True:
    jump fushigi_end_check_amuse2_p
if renpy.seen_label("fushigi_end_boris1") == True:
    jump fushigi_end_check_amuse2_p
if renpy.seen_label("fushigi_end_pierce1") == True:
    jump fushigi_end_check_amuse2_p
else:
    jump fushigi_end_pierce1
label fushigi_end_check_amuse2_p:
if fushigi_common3_hatter2_pierce2b_seen == True:
    jump fushigi_end_pierce1
else:
    jump fushigi_end_amuse1
