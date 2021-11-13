
scene map_bg_winter_day
with dis
label fushigi_end_julius1:
$ clockanim()


scene map_bg_winter_day
with dis

scene charasel_bg_tower_day
with dis

play music tower_room1_p_ali

scene ts_01
with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「部屋はもうすっかり元通りなのね」"


show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice jul_f0268
Julius "「ああ、そうだな。\n
元々勝手に汚れが落ちるのがこの世界のルールだ」"

hide yuri_t_03_9
show yuri_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice jul_f0269
Julius "「煤汚れでも、壊れない限りはそのルールが優先される」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「そうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "久しぶりに戻ったユリウスの部屋。\n
まるで巻き戻したように、元通りになっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（でも……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

hide yuri_t_01_2
show yuri_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達は黙ったまま、部屋の中を見ている。\n
あのとき、炭や煤で汚れていたとは思えないほど綺麗になっていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつでも仕事が出来るように整えられた、ユリウスの部屋だ。\n
しかし、時計は山積み。"

hide yuri_t_01_9


scene t_cut_yuri_end1u
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……仕事がずいぶん溜まっているのね。\n
私がいない間に、どこかで戦争があったわけでもないでしょうに」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（ユリウスがこんなに時計を溜めていたことってあったかしら）"


scene t_cut_yuri_end1
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の人間は時計で存在する。\n
ユリウスの元に運び込まれてくるのは、何らかの事情で壊れた、あるいは壊された時計だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つまり、それだけ誰かが倒れたと言うことなのだが、その背景について、今は考えないでおく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、誰もが銃を携帯し、三勢力が均衡しているこの世界において、時計屋の仕事は急に増減するものではないはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが……、今、天井に付かんばかりに積み上げられているのである。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（恐ろしい量ね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "地震でも来たら生き埋めになってしまいそうだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（ナイトメアが来たら、勝手に自爆して時計の下敷きになりそう）"


show yuri_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice jul_f0270
Julius "「そんな馬鹿げたことをしたやつはいない。\n
たまたま大口の仕事が重なっただけだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（本当かしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事の台帳とでも言うべき受付簿は、ユリウスの机の上に置かれている。\n
いつもの調子でページを捲れば、そこには……。"

play sound se_0717
hide yuri_t_02_8


scene t_cut_yuri_end2u
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

play sound se_0717
pause .5
play sound se_0717
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "{size=+20}「何、これ？」{/size}"


scene t_cut_yuri_end2
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐ろしい数字が並んでいた。\n
仕事が生活の中心を成しているユリウスとは思えないほど、仕事が溜まっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「これって、やっぱり部屋が元通りになるまでが長かったから、とか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "別室で仕事をしていたことは私も知っている。\n
慣れない環境下で腕が鈍るとは思えないが、多少は影響していたのかもしれない。"


scene ts_01
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（やっぱり……、悪いことしちゃったわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結局ハートの城の客室に買ったものも置いてきてしまった。\n
迷惑ばかりかけている自分に、落ち込みそうになる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、彼は首を横に振った。"


show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0271
Julius "「馬鹿なことを言うな。\n
部屋など、おまえが出て行ってから数時間帯で元に戻っている」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「じゃあ、何でこんなに仕事が溜まっているのよ？\n
もしかしてユリウス、どこか身体の調子が悪いんじゃないの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼だって機械仕掛けの人形ではないのだ。\n
不調のときだってあるだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（それにしても、これは前代未聞だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の不安げな言葉にもユリウスはいつも通りだった。"

hide yuri_t_03_9
show yuri_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0272
Julius "「……身体は何ということもない。\n
捗らなかっただけだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あなた、具合でも悪いの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "机の傍に立っているユリウスに近寄り、少し高い位置にある相手の額に手を添える。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（うん、熱があるっていうわけではなさそうだけど）"

hide yuri_t_03_13
show yuri_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
Julius "「！！」"

hide yuri_t_03_3
show yuri_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jul_f0273
Julius "「な……、ななな。\n
何をするんだ、おまえはっ！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「何って……。\n
どこか具合でも悪いのかと思って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「……今更これぐらいで照れないでよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（何だかもっと恥ずかしいことをしているような気になるじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口を尖らせると、ユリウスは困ったように視線を逸らして、溜息をついた。"

hide yuri_t_02_6
show yuri_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0274
Julius "「べ、別に照れたわけではない。\n
その、少し驚いただけだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（あれ、本当にあったかい？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "掌の下にじわりと湿気を感じる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（私が熱を出しているわけじゃなさそうだし）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ユリウス、やっぱりあなたは熱があるんじゃない？\n
何だか、どんどん熱くなっているような気がするわ」"

hide yuri_t_02_8
show yuri_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jul_f0275
Julius "「……気のせいだ。\n
いつもよりも仕事をしていないから、ちょっと調子が悪いだけだっ」"

play sound se_0584
hide yuri_t_03_13

pause .5
play sound se_0160
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の手を振り払って、彼は指定席へと戻った。\n
作業台の上にある黒縁の眼鏡を手にとって、それをかける。"


show t_yuri_end1and4and10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（あ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（顔が変わった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで少し赤らんでいた顔が、今は引き締まる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "几帳面そうな性格が滲み出るような丁寧さで時計を手に取ると、彼は仕事を再開した。"

play sound se_0480
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "硬い金属の音。\n
それを生み出す、ユリウス。\n
それだけで構成されている世界。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それだけで満たされている。"

hide t_yuri_end1and4and10

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（私がいてもいいのか分からないのは、変わらないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも、この音に包まれてこの部屋にいるのは、なんて心地がいいんだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城に置いてきたものは後回しにして、まずは私が出来ることをしようと立ち上がった。"

$ hi_mes()

scene charasel_bg_tower_day with stripe_l_medium

scene cr_01 with stripe_l_medium

scene bg_gen23_tkt with stripe_l_long

play music tower_corridor_p_ali

show gre_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0155
Gray "「[firstname]……？\n
それは、君の手料理なのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「あ、グレイ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「ええ、ユリウスに差し入れをしようと思って……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（ちょっと作りすぎちゃったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キッチンで料理をしていたら、後ろからグレイに声をかけられた。"

play sound se_0174
play sound se_0360
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（調子に乗りすぎたわよね）"


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ワゴンを動かしてみるが、結構重い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最初は簡単に食べられるサンドイッチとスープぐらいのつもりだったのに、デザートにクッキーを付けたり、野菜が足りないからとサラダを作り。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "せっかくだから、ハートの城にいる間に習ったキッシュにまで手を出し。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気が付けば、ワゴンで運ばないと持ち運びできない量が出来上がっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（どんな大所帯に持っていく気だったのよ）"

hide gre_t_03_1
show gre_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice gra_f0156
Gray "「大丈夫か？\n
よければ、運ぶのを手伝うが……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「あ、いいわよ。\n
グレイ、忙しいでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「ユリウスの部屋まで持っていくだけだから、大丈夫」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はとても多忙な人だ。\n
塔の業務と、体調管理の出来ない上司の面倒まで見ている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（迷惑をかけちゃいけないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この前の小火騒動でも仕事を増やしてしまったのだ。\n
これ以上、迷惑をかけるわけにはいかない。"

hide gre_t_02_10
show gre_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0157
Gray "「時計屋の……？\n
これは、つまり……、君と時計屋の分なのか？」"

hide gre_t_02_3
show gre_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0158
Gray "「……それにしては、大分」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「ええ、つい作りすぎちゃったみたい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あとで皆にも差し入れに行くわ。\n
とりあえずユリウスのところに持って行ってからだけど……」"

hide gre_t_03_11
show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Gray "「…………」"

hide gre_t_03_10
show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0159
Gray "「わざわざ運んでくれなくていい。\n
手伝おう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？\n
あ、グレイ！」"

play sound se_0174
hide gre_t_01_4

play sound se_0360
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の手からワゴンを攫うと、グレイは颯爽と歩き始めた。\n
慌ててその背中を追いかける。"


scene cr_01 with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「そんな……、悪いわ。\n
あとは押していくだけなんだから、あなたの手を借りなくても」"


show gre_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0160
Gray "「冷たいことを言わないでくれ。\n
うまいものをご相伴に与るんだ」"

hide gre_t_02_2
show gre_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0161
Gray "「これぐらいしないと、罰が当たりそうだからな」"

hide gre_t_03_4
show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Gray "「…………」"

hide gre_t_03_10
show gre_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0162
Gray "「それに俺も少しぐらい休憩したっていいだろう。\n
時計屋ばかりいい思いをするのは、汚い」"

hide gre_t_02_12
show gre_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0163
Gray "「時計屋のとこの騎士には面倒を掛けられているんだ、少しぐらい埋め合わせをしてもらおう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぶつぶつと何かグレイは呟いていたが、少し早い歩みに追いつこうとしている私には、よく聞き取れなかった。"

hide gre_t_02_6

$ hi_mes()

scene ts_01
with stripe_l_long

play music tower_room2_p_ali

show yuri_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Julius "「…………」"

hide yuri_t_02_8
show yuri_t_02_8 at left
show gre_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0164
Gray "「これはまたうまそうだな。\n
食べるのがもったいないぐらいだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「そんなことないわ、普通の料理だもの。\n
どうぞ、召し上がれ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの作業台に料理を置いて、傍の机に残りを並べた。\n
グレイと私は向かい合って、料理に手をつける。"

hide yuri_t_02_8
show yuri_t_03_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

play sound se_0544
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「……ユリウス、食事中ぐらいは手を止めたら？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一人作業台の前から動かない彼に声をかける。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（……食べていないわけじゃないのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想通りというべきか、片手で食べられるサンドイッチを選んだようだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "片手でパンをつかみ数口含んでは皿に戻す。\n
その間にまた手は時計を弄る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（器用と言えば器用なんだけど）"

hide gre_t_01_4
show gre_t_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_14")
voice gra_f0165
Gray "「行儀が悪いぞ、時計屋。\n
ガキじゃないんだ、ながら食いなどするな」"

hide yuri_t_03_13
show yuri_t_03_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_14")
voice jul_f0276
Julius "「……私がどうやって食べようと、私の勝手だ。\n
いちいち干渉するんじゃない、トカゲ」"

hide gre_t_01_5
show gre_t_03_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_14")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴりっとした緊迫感の中、二人は睨み合っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、それぞれが手にサンドイッチと、スープカップを持った状態では……、どうにも様にならない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_5")
T "（むしろ、コントのような）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仲が悪いように見えても、二人ともいい大人だ。\n
手を出さないあたり、まだ平和で助かる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「二人とも、食事中に喧嘩はやめてね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（ただでさえ、たいして美味しくもない私の手料理なんだから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "雰囲気まで壊されては、ますます味が落ちてしまう。"


show nai_s_01_11 at center
hide yuri_t_03_12
hide gre_t_03_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0458
Nightmare "「そうだぞ、二人とも。\n
食事とは、生命維持に欠かすことの出来ない重要な行動であると同時に、精神的な癒しでもある」"

hide nai_s_01_11
show nai_s_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0459
Nightmare "「うまいものを食べられる感動を素直に享受したらどうだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「ナイトメア？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつの間に現れたのか。\n
顔色の悪い夢魔は私の横に腰を下ろすと、近くにあったクッキーに手を出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「……それは、食後のデザートよ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（あなただって行儀が悪い）"

hide nai_s_02_4
show nai_s_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0460
Nightmare "「細かいことを言わないでくれ、[firstname]。\n
グレイが戻ってこないから逃げ……、探しに来たら、いい香りがしてね」"

hide nai_s_02_10
show nai_s_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0461
Nightmare "「うん、うまい……。\n
君の料理はいつ食べても幸せな気分になれるなあ」"

hide nai_s_01_6
show nai_s_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0462
Nightmare "「……誰かの作るものとは大違いだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しみじみとした声にはたっぷりと実感がこもっている。"

hide nai_s_02_8
show nai_s_02_8 at left
show gre_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0166
Gray "「俺の料理はナイトメア様の身体に少しでもいいものを入れているだけですよ。\n
あれを食べて、健康になられればきっと幸せな気分に……」"

hide gre_t_02_4
show gre_t_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0167
Gray "「身体も軽くなって、きっと仕事もばりばりと！」"

hide nai_s_02_8
show nai_s_03_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0463
Nightmare "{size=+20}「別の意味で、身体が軽くなってお空に上ってしまうだろうがっ」{/size}"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（こっちもコントね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とはいえ、グレイの手料理について現状を知っている身としては、余計な口を挟むわけにもいかない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人間、努力だけではどうにもならないことがあるのだ。"

play sound se_0177

show yuri_t_01_4 at center
hide gre_t_03_4

hide nai_s_03_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（あ、ユリウスのスープ、飲み終わっている）"

play sound se_0175
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ワゴンの上に乗せておいたポットを手にとって、お茶を注ぐ。\n
以前街で購入しておいた、買い置きの紅茶だ。"


$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「はい」"

play sound se_0177
hide yuri_t_01_4
show yuri_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice jul_f0277
Julius "「……ああ、すまん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「食後に珈琲も淹れるけど、今はお茶のほうがいいでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（珈琲を淹れるなら、ちゃんと豆から挽いて淹れたいし。\n
ハムが挟まっていたサンドイッチだから、口をすっきりさせたほうがいいものね）"

hide yuri_t_01_12
show yuri_t_01_12 at left
show gre_t_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
Gray "「…………」"

hide yuri_t_01_12

hide gre_t_01_6
show gre_t_01_6 at left
show nai_s_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
Nightmare "「…………」"

hide nai_s_02_9
show nai_s_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice nig_f0464
Nightmare "「何というか、新婚家庭に邪魔をしてしまったご近所さんの気持ちが、今は痛いほどよく分かるな」"

hide nai_s_01_4
show nai_s_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice nig_f0465
Nightmare "「……独り者には、目に痛すぎる」"

hide gre_t_01_6
show gre_t_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice gra_f0168
Gray "「同感です。\n
はあ……」"

hide gre_t_02_7
show gre_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice gra_f0169
Gray "「ここに来たのが、そもそも失策だったらしい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（何を言っているのかしら、二人とも）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "珍しく気が合ったのか、ナイトメアとグレイは二人して肩を落としている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「あ、ひょっとして口に合わなかった？\n
だったらまだ他にも……」"

hide nai_s_01_10
show nai_s_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice nig_f0466
Nightmare "「あ、いや、そういうわけではなくてだな。\n
……君が、あまりにも時計屋といい仲のようだから、少し当てられたんだ」"

hide nai_s_02_12
show nai_s_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice nig_f0467
Nightmare "「これで彼も落ち着いて仕事が出来るだろう。\n
よかったな、時計屋」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「落ち着いて仕事って……。\n
ユリウスはいつだってそうじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いい仲、と称されたことに否定を返すより先に、ナイトメアの言うユリウスが想像つかずに答えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "（書類と向き合うことに音を上げて逃走を図る夢魔とは違うわよ。\n
仕事をしないユリウスなんて、迷わないエースと同じぐらい変じゃない）"

hide nai_s_01_1
show nai_s_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_17")
voice nig_f0468
Nightmare "「私を引き合いに出すんじゃないっ。\n
私だって一生懸命片付けているんだ！」"

hide nai_s_02_6
show nai_s_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_17")
voice nig_f0469
Nightmare "「……こほん。\n
話を戻そう」"

hide nai_s_02_9
show nai_s_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_17")
voice nig_f0470
Nightmare "「時計屋がいつだって落ち着いている……、ね？\n
君がいない間も果たしてそうだったと思うのかな？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "うってかわって、ナイトメアはにやりと笑う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「だって……。\n
ユリウスはいつもどおりだったでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "マグカップを持った彼に声をかけるが、ユリウスは私と視線を合わせようとしなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むしろあからさまに目線をそらしてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（え？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（これって……、つまり）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "説明を求めて、グレイ達に視線を向ける。"

hide gre_t_02_11
show gre_t_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0170
Gray "「ああ、そういえば、部屋から出てこないのはいつものことでしたが、依頼人が受け取りに来ることは少なかったですね」"

hide nai_s_03_1
show nai_s_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0471
Nightmare "「その挙げ句に出ていくときには、完全な尾行姿だからな。\n
あれで目立つなというほうが無理だ」"

hide gre_t_03_1
show gre_t_03_1 at left_center
hide nai_s_02_4
show nai_s_02_4 at center
show yuri_t_02_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは沈黙を保っているが、聞こえないふりが出来るほどこの部屋は広くない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔の主従が口を開く度に、無表情を装った頬がぴくぴくと反応していた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "当然、そんな反応を見逃すような夢魔ではない。"

hide nai_s_02_4
show nai_s_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0472
Nightmare "「君がいないと、時計屋は集中力が足りなくなるらしい。\n
文字通り、寝ても覚めても……、というやつだな」"

hide yuri_t_02_8
show yuri_t_02_6 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「！！」"

play sound se_0295
play sound se_0174
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

hide yuri_t_02_6
show yuri_t_03_7 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice jul_f0278
Julius "「おまえ達、余計なお喋りをするつもりならとっとと出ていけ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドンッ、という音と共に、机を叩きながらユリウスが立ち上がって怒鳴る。\n
しかし、塔の主従はこれまた怯むことなく、言葉を続けた。"

hide gre_t_03_1
show gre_t_02_6 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0171
Gray "「当てつけたのはおまえが先だっただろう」"

hide gre_t_02_6
show gre_t_01_4 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0171_5
Gray "「……君の料理は美味かったよ、ありがとう」"

hide nai_s_01_6
show nai_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0473
Nightmare "「今度は、私のためにぜひその腕を振る舞ってくれると嬉しいよ。\n
君の手料理なら、いつでも歓迎……、ぶ！」"

play sound se_0050
camera at hpunch
camera at vpunch
##special anime hit_center
pause .7
play sound se_0553
hide gre_t_01_4
show gre_t_01_4 at left_center
hide yuri_t_03_7
show yuri_t_02_7 at right_center
hide nai_s_02_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0279
Julius "「トカゲ、おまえの上司だ。\n
責任を持って回収していけ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスが持っていたスパナが、ものすごい勢いでナイトメアに命中する。"

hide gre_t_01_4
show gre_t_03_11 at center
hide yuri_t_02_7
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0172
Gray "「……やれやれ。\n
馬に蹴られるのではなく、スパナにこづかれるとはな」"

hide gre_t_03_11
show gre_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0173
Gray "「帰りましょう、ナイトメア様。\n
ご馳走様、[firstname]」"

hide gre_t_01_3
show gre_t_01_3 at left
show nai_s_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0474
Nightmare "「うう……。\n
痛い……、手加減なしでぶつけたぞ、あいつ！」"

hide gre_t_01_3
show gre_t_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0174
Gray "「まあまあ、心配しなくても、しっかり手当てはいたしますから」"

hide gre_t_01_4
show gre_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0175
Gray "「手当てがすんだら、仕事に戻りましょう。\n
休憩を取ったんですから、たくさん働きましょうね」"

hide nai_s_03_2
show nai_s_03_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0475
Nightmare "「うう……っ、上司に優しくない……」"

play sound se_0284
hide gre_t_03_4

hide nai_s_03_6

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの投げた工具で倒れたナイトメアを担いで、グレイはさっさと部屋を出て行った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "残ったのは、空になった食器と、そして……。"


play music honobono2_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「ユリウス」"


show yuri_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "互いに言葉を探すように視線を逸らす、私達。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「その……、仕事は大口が来たんじゃなくて、溜まっていたの？」"

hide yuri_t_02_8
show yuri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice jul_f0280
Julius "「たまたま面倒な修理が重なっただけだ。\n
別に溜めていたわけじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（本当に？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問いかけてみたいような、意地悪をしたくなるようなそんな気持ち。\n
私と似ている部分を持つ彼は……、素直ではない。"

hide yuri_t_02_11
show yuri_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0281
Julius "「……何を笑っている？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「笑っていた？」"

hide yuri_t_02_3
show yuri_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice jul_f0282
Julius "「ああ、にやにやしていた。\n
そんなに仕事を溜めた私が珍しかったのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「違うわよ」"

play sound se_0551

show t_yuri_end2 onlayer master
hide yuri_t_03_4
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "机に寄りかかって、ユリウスの髪に触れてみる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「嬉しかったから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice jul_f0283
Julius "「嬉しい？\n
何がそんなに嬉しいんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「嬉しいわよ。\n
だって、時計の修理はユリウスの生活の一部でしょう？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_16")
T "（正確には、生活の中心といってもいい）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「その仕事が、私がいない間にうまく進まなかったなんて……。\n
不思議で、嬉しかった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "髪を撫でても振り払われないことも、自然に溶け込めることも、嬉しく思う。\n
それに、帰ってきたんだという実感も湧いた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "精密な機械のように動く、彼の指。\n
それを支える一因になれているのだと思うと、それは悪くない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（……ううん、違う）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（嬉しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "特別なことなど何も出来ないのに。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「ユリウスの一部になったみたいで、嬉しいわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_12")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_12")
voice jul_f0284
Julius "「おまえは私の一部なんかじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「っ」"


play music happy_a_ali
hide t_yuri_end2
show t_yuri_end3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "腕を引かれ、顔が近付く。\n
気付いたときには、唇が重なっていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………ん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice jul_f0285
Julius "「…………ふ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少しだけ離れて、ユリウスは告げる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0286
Julius "「おまえの一部に私はなれない。\n
同じように、おまえも私の一部になんてなれるはずがない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_5")
T "（それは中にあるものが違うから？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問いかける前に唇は再び塞がれてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不器用なキス。\n
不器用すぎて愛しさが込み上げるから、離したくなくなって。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ますます不器用になっていく。\n
私達は、から回っていく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0287
Julius "「私の一部になどなるな。\n
私は私に、こんなことをするような趣味はない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ええ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（一部になれなくても）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呼吸も、熱も、一緒に感じられるほど。\n
こんなに近くにいられれば、何も望むものなんてない。"

hide t_yuri_end3

$ hi_mes()

scene charasel_bg_tower_day with stripe_l_long

scene map_bg_winter_day
with stripe_l_medium

scene charasel_bg_tower_day
with stripe_l_medium

scene ts_01
with stripe_l_long

play music honobono1_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"


show t_yuri_end1and4and10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Julius "「…………」"

play sound se_0480
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "静かな空間。\n
ユリウスの隣に座ったまま、彼の仕事を見ている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（本当に綺麗）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声も出ないほどじっと見てしまうのは、彼の指先。\n
常に金属に触れている手は、男の人の中でも荒れているほうかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ざらざらとした感触は、一般的にいう『綺麗』とは結びつかないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（でも）"

play sound se_0480
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（動く姿が綺麗だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飾り立てた宝石のような煌びやかさなんてない。\n
しかし、この手はとても綺麗に見える。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0288
Julius "「いい加減、飽きただろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「いいえ、飽きたりなんかしないわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（ずっとこうしていてもいい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスがいて、金属の音が静かに響く空間。\n
その中に無理をしなくても溶け込めることが、不思議だといつも思う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「……ねえ、ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice jul_f0289
Julius "「何だ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「前から聞きたかったんだけど……。\n
どうして、私を置いてくれたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターにハートの国へ連れてこられたとき、最初は私を拒んだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（それも当然だけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの人嫌いは、筋金入りだ。\n
余所者だからという理由で受け入れてくれたというのは、何だか足りない気がする。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0290
Julius "「正確には、私がおまえを置いたのではなく、おまえが押しかけてきたんだろうが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「それもそうだけど……。\n
本当に嫌だったら、追い返したでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは、綺麗事で片付けるような人ではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "嫌だったら嫌だという。\n
出来ないことは、引き受けない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（困っている人を見捨てきれない人だけど……。\n
誰にでも、平等に優しいわけじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "初対面だった私に、帽子屋屋敷で会ったエリオットが即座に銃を向けたように。\n
あのときのユリウスにとっても、私はただの異物だったはず。"

hide t_yuri_end1and4and10
show t_yuri_end5 onlayer master
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
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計を修理する手を止めて、彼はじっと私を見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒っているわけではないらしい。\n
思いを馳せるような、懐かしむような眼差しだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jul_f0291
Julius "「ただの偶然だ。\n
……そう言えればいいんだがな」"

hide t_yuri_end5

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「偶然じゃなかった？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "伸ばされた手が髪に触れて、私はユリウスの膝の上に座る。"


show yuri_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0292
Julius "「そうだな。\n
興味もあったし、偶然や運が作用したことは間違いないんだが」"

hide yuri_t_01_4
show yuri_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

hide yuri_t_01_5
show yuri_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0293
Julius "「聞いてみたかったのかもしれん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「あ」"

play sound se_0551

play music dream_tsuduki_a_ali

show t_yuri_end6 onlayer master
hide yuri_t_01_6
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

play sound se_0550 volume .5
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（早い）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_7")
T "（心臓が飛び出ちゃいそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの耳が、私の胸に重なる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もっと深く触れ合うこともある。\n
もっと強く抱き締められたこともある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも、心臓の鼓動が早まることを止められない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0294
Julius "「壊れてしまったら、私でも二度と直せない。\n
そんな心臓の音を聞いてみたかった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

play sound se_0474 volume .2
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jul_f0295
Julius "「直せないことに安堵したかったのか、嫌悪していたのかは分からないが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

hide t_yuri_end6
show t_yuri_end7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
Julius "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの首に腕を回して、ぎゅっと抱きしめる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「興味があったんでしょう？\n
遠慮しないで聞いていいのに」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（今も、心臓が飛び出しそうなほど恥ずかしいのは変わらないけど）"

hide t_yuri_end7
show t_yuri_end8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
voice jul_f0296
Julius "「……これ以上聞いたら、示しが付かない気がするんだがな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「示しが付かないって、どういう意味よ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice jul_f0297
Julius "「……好きな女を引き留められもせず、悩んだ挙げ句に仕事を溜め込んで。\n
その上、溜めた仕事を片付ける前に手を付けるなど、無節操だろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの言葉に私は目を見開く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「だから、塔に戻ってからずっと仕事にかかりきりだったの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おかしいとは思っていたのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計塔に住み始めたばかりの頃とは違って、生活を共にしてから、一緒に寝ることのほうが多かった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが、ハートの城から戻ってからというもの、私のいない間に仮眠を取って、仕事に明け暮れている始末。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "避けられているのかと思えば、時々見せる柔らかな表情はいつもの彼のものだったから尋ねることも出来なかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_5")
T "「……自制心があるというか、それとも意気地がないというか」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_5")
voice jul_f0298
Julius "「……悪かったな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「…………」"

hide t_yuri_end8
show t_yuri_end9 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
Julius "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの前髪にそっと唇を寄せる。\n
抱きしめて聞こえる時計の音が、とても落ち着く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ねえ、ユリウス。\n
あなたが聞きたいだけ聞かせてあげる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「たくさん聞かせてあげるから、飽きたりなんかしないでね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice jul_f0299
Julius "「勘違いするな。\n
最初のきっかけはおまえの鼓動だったとしても」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "優しい目。\n
暖かくて、何故か泣きたくなる目。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（どうしてだろう）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（一緒にいればいるほど落ち着く。\n
……でも、寂しくもなる）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice jul_f0300
Julius "「私が迎えたのは、心臓じゃない。\n
おまえだ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice jul_f0301
Julius "「それに……。\n
飽きるというのなら、おまえが私の仕事を見飽きるほうが早そうだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「そんなことないわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（飽きたりなんかしない）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_14")
voice jul_f0302
Julius "「私は面白味のない男だからな……。\n
おまえの関心を惹けなくなるかもしれない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice jul_f0303
Julius "「それでも……。\n
ここからおまえがどこかに行くことがなければいいと思う」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice jul_f0304
Julius "「離したくないんだ。\n
おまえがどこか別の場所に行きたいと願っても」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice jul_f0305
Julius "「どこにも行かせたくない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_19")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「行かないわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（そんな哀しそうに言わないで）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ユリウスが私に飽きても、居座ってあげるんだから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jul_f0306
Julius "「ああ、そうだな。\n
私が出て行けと嘘をついたとしても……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jul_f0307
Julius "「おまえは、図々しく、私の言葉になど惑わされずに。\n
ここにずっといればいい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "興味より、関心より。\n
もっと強いもので私達はお互いに惹き付けあっている。"



hide t_yuri_end9

$ hi_mes()

scene charasel_bg_tower_day with stripe_l_long

scene map_bg_winter_day
with stripe_l_medium

scene charasel_bg_tower_day
with stripe_l_medium

scene cr_01
with stripe_l_long

play music tower_corridor_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（失敗したわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城からクローバーの塔、正確にはクローバーの塔から繋がっているユリウスの部屋に戻ったあのとき。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ばたばたと兵士に追いかけられていたので、仕方ないといえば仕方ないのだが。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは仕事が一段落付いたこともあって、ベッドで横になって眠っている。\n
彼の眠りを邪魔しないように塔の廊下に出てきたのだが……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「せっかく、買ったのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "近いうちにハートの城へ取りにいかなくては、下手をすれば片付けられてしまうかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「お礼も言いそびれちゃったし……。\n
はあ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（落ち込む）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "次にペーターやビバルディと会ったときには何かお礼を持っていかなければならないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "親しき仲にも礼儀あり、だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ユリウスへのお詫びを探しに行ったのに、皆へのお礼を持って城に行くなんて変な話だけど」"


show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0492
Ace "「平気だよ。\n
陛下も、ペーターさんも君には甘いから」"

hide ace_t_01_4
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0493
Ace "「顔でも見せてお茶に付き合えば、喜んで帳消しにしてくれるって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「……だといいんだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "{size=+20}「！！！？」{/size}"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「エ、エース！？」"


play music ace_t_ali
hide ace_t_01_10
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0494
Ace "「やあ、久しぶり。\n
元気そうだね、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "からっと笑って現れたのは、赤い騎士。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "神出鬼没の彼は、塔の裏道をよく知っているようだ。\n
唐突な登場に、別れたときのことを思い出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「エース。\n
あなた、あの後どうしたの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_5")
T "（何だか、ものすごい数の兵士が押し寄せてきた気がするんだけど……）"

hide ace_t_03_3
show ace_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_5")
voice ace_f0495
Ace "「ん？ああ、部下のこと？\n
せっかくだから、皆まとめて稽古を付けてあげたんだ」"

hide ace_t_03_2
show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_5")
voice ace_f0496
Ace "「いやあ、あれだけいるとさすがに役なし相手でもいい運動になるよなあ。\n
はははは」"

hide ace_t_02_4
show ace_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_5")
voice ace_f0497
Ace "「いい汗かいたぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（あれだけの兵士を片付けたわけ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ざっと見た感じでは、少なくとも十人や二十人ではきかなかったように思う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "軍事責任者の役職は伊達ではないということだろうが、そこまで行くと規格外すぎてイメージがつかない。"

hide ace_t_02_1
show ace_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0498
Ace "「ところが、珍しく気合いを入れて稽古を付けてあげたんだけど、陛下はむすっとしちゃうし、困ったんだよなあ」"

hide ace_t_03_7
show ace_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0499
Ace "「いくら綺麗にお化粧をしていても、あんなに顔に皺を作っていたら意味がないのにね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（それはビバルディの気持ちのほうが分かる気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "捕らえさせるために差し向けた部下を返り討ちにしてしまう軍事責任者がどこにいるというのだ。"

hide ace_t_01_6
show ace_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0500
Ace "「ペーターさんは君がいなくなったっていって、ずっと不機嫌だし。\n
おまけに俺に八つ当たりまでするんだぜ？」"

hide ace_t_03_9
show ace_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0501
Ace "「あの程度の刺客なんて山ほど送ってきても、鍛錬にもならないんだけどなあ。\n
くれるって言うならもらっておくけど、うまくお返しが出来ないし」"

hide ace_t_02_12
show ace_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0502
Ace "「あーあ、困ったなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（困った困ったって言っているけど……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（何だか楽しそうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこにこと饒舌に喋るエースは、いつもよりも更にエネルギッシュだ。\n
理由は分からないが、何かいいことでもあったのだろうか。"

hide ace_t_02_6
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0503
Ace "「ユリウスに仕事の話を聞きに来たんだけど、今、いるかな？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「いるにはいるけど……。\n
今、ようやく寝たばかりなのよね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……起こしたほうがいい？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（本当はもう少し寝かせておいてあげたいんだけど。\n
仕事に口を出したら、かえって気にするものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私に対して怒るのならばまだいいのだが、彼のことだ。\n
そんなタイミングで寝ていたことで自分を責めかねない。"

hide ace_t_03_10
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0504
Ace "「いや、寝ているなら寝かせておいていいや。\n
ユリウスが君を放って寝るってことは、疲れているだろうし」"

hide ace_t_01_10
show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0505
Ace "「それに……。\n
君に渡したいものもあったんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「私に？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

play sound se_0454
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "{size=+20}「ピアスならいらないわよ」{/size}"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何かを取り出そうとするエースの姿に思わず声が跳ね上がり、後退った。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（またナイフで耳に穴を開けようとするんじゃないでしょうね！？）"

hide ace_t_01_4
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice ace_f0506
Ace "「ははは、あれは冗談だよ、冗談。\n
本気にしてもらえるなんて、俺も予想外だったなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「ナイフまで耳に当てられて、『大は小を兼ねる』なんて言われたら、普通は警戒するに決まっているでしょう！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（エースならやりかねない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして予想以上に大きな穴が開いたとしても、「そのうち埋まるから大丈夫」とか平然と言いかねない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "穴を開けられそうになるこちらとしては、迷惑である。"

hide ace_t_03_3
show ace_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0507
Ace "「そんなに警戒しないでよ。\n
傷つくなあ」"

hide ace_t_02_8
show ace_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0508
Ace "「これ、君の忘れ物だと思ったから届けに来たのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……！」"

hide ace_t_02_13


scene t_cut_yuri_end3u
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（あの包装紙は……）"

play sound se_0783
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースが手にしているものを見て、ハッとした。"


scene t_cut_yuri_end3
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（私が買ったプレゼント！）"


show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice ace_f0509
Ace "「客室に残っていたのを、メイドがどうしようかって話していたから持って来たんだ」"

hide ace_t_01_10
show ace_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice ace_f0510
Ace "「ペーターさんに見つかったら、あの人のことだから後生大事に保管していただろうけど……」"

hide ace_t_01_2
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice ace_f0510_5
Ace "「こういうのは早く届けてあげるのが親切だろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「エース……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（警戒しすぎて悪かったかも）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ありがとう。\n
大切なものだから、助かったわ」"

play sound se_0472

scene cr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "差し出された荷物を受け取り、礼を言う。"

hide ace_t_03_3
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0511
Ace "「どういたしまして」"

hide ace_t_03_10
show ace_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0512
Ace "「まあ、早く届けようとしたんだけど。\n
こんなときにも迷って、結局これだけかかっちゃったんだけどな」"

hide ace_t_02_8
show ace_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0513
Ace "「本当に、俺ってついていないよな。\n
はははは」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「あなたらしいわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迷って迷って。\n
それでも、辿り着くあたりはいかにも彼らしい。"


play music secret_a_ali
hide ace_t_02_3
show ace_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"

hide ace_t_02_10
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice ace_f0514
Ace "「君は、ユリウスのこと、好きだろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一歩踏み込まれて、近い距離で問われる。\n
爽やかな表情は、感情を浮かべていないようにも見えた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ええ、好きよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の問いかけは突然だったが、私の中の答えもただ一つ。\n
だから、迷う間もなく答えられる。"

hide ace_t_03_10
show ace_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0515
Ace "「なら、俺がユリウスを裏切らないのと同じように。\n
君は、あいつの味方でいてくれる？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「それって……、どういう意味？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースはじっと私を見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い目。\n
迷ってばかりの騎士が、今はまっすぐに私だけを映した。"

hide ace_t_01_5
show ace_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0516
Ace "「時計屋は、業も深いし、恨みも買いやすいって知っているはずだ。\n
それでも君はユリウスの傍で、味方でいてくれるの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「分からない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今度は私が少し迷って、答えを出した。"

hide ace_t_01_9
show ace_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「ユリウスの傍にいたいと思うし、あの人と一緒にいたいと思うけど。\n
味方になってあげられるかは、分からない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（こんなこと言ったら、斬られるかもしれない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースの手は剣にかかっていない。\n
だが、彼がその気になったら、抜き手さえ見せずに私を切り捨てるはずだ。"

hide ace_t_03_4
show ace_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0517
Ace "「君が、ユリウスの敵になるの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……敵になんてならない。\n
そんな力も、気持ちもない私には、敵になんてなれない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（私になれるものなんて、たかが知れているもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃も持てない。\n
剣も使えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "特殊な能力なんて、あるはずがないから。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「それに私が味方をしたって、大して役に立たないもの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_2")
T "「でも私は……、ユリウスの家族になりたい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "離れても忘れられない存在に、なってみたいと思った。"

hide ace_t_02_5
show ace_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

hide ace_t_02_7
show ace_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0518
Ace "「家族って、味方じゃないのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「味方とは限らないわ。\n
この前みたいに勝手に飛び出すことだってあるかもしれない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "傍にいたいと思うのと同じぐらいに、求めてほしいと思う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "愛されていたい。\n
愛したい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "等価交換が出来ないものだからこそ、確信がほしくなる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（不安なのよね、結局は）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分に自信が持てないから、形になる何かを求めてしまう。\n
ユリウスも、私も、似たようなものだと、手の中にあるものを見て思った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「喧嘩もするだろうから、味方であり続けるなんて約束は出来ないわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「……でも、私がいる場所として選んだのは、ユリウスの隣だけよ。\n
だから、あの人と新しい家族になれたらいいって、今は思っているの」"

hide ace_t_03_4
show ace_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Ace "「…………」"

hide ace_t_01_6
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice ace_f0519
Ace "「そうか。\n
だったら、それが答えかもしれないな」"


play music tower_t_ali
hide ace_t_01_10
show ace_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice ace_f0520
Ace "「恋人なんて言われたら、惚気られているのかと思って笑うところだけど」"

hide ace_t_03_9
show ace_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice ace_f0521
Ace "「あいつの家族になってくれるのなら……、それはそんなに悪いことじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "急に手を取られ、騎士は、恭しい口付けを手の甲に落とした。"

hide ace_t_02_10
show ace_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0522
Ace "「君の手があいつから離れないように……。\n
おまじない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後にそんな気障なことを言って、エースは背を向ける。"

hide ace_t_02_1
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0523
Ace "「さてと。\n
それじゃあユリウスが起きるまで、トカゲさんにでも相手をしてもらおうかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「……あまり迷惑かけちゃ駄目よ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "早くも去っていく相手を、苦笑と共に送り出す。"

hide ace_t_03_11
show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0524
Ace "「ははは、トカゲさんと俺は仲がいいんだから、迷惑なんてことはないぜ。\n
持ちつ持たれつ、お互い様ってやつだ」"

play sound se_0774
hide ace_t_01_4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い背中が去っていく。\n
迷う足取りは、やはりどこか上機嫌に軽やかだった。"


$ hi_mes()

scene charasel_bg_tower_day with stripe_l_long

scene map_bg_winter_day
with stripe_l_medium

scene charasel_bg_tower_day
with stripe_l_medium

scene ts_01
with stripe_l_long

play music tower_room2_p_ali

show t_yuri_end1and4and10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Julius "「…………」"

play sound se_0480
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事を再開したユリウスの手元から時計が消えることはない。\n
硬い音を立てて、それらは再び動くための通過点を過ぎる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（そろそろいいかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界は時間の流れが曖昧だが、ユリウスが定位置に戻って、時間帯が一回変わったのは確かだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……ねえ。\n
ユリウス、珈琲を飲まない？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「少し休憩にしましょう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice jul_f0308
Julius "「ああ。\n
豆なら、前の時間帯に届いたものがあるから、いつものところから出してくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「分かったわ」"

hide t_yuri_end1and4and10

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの場所。\n
そう言われれば分かる程度に馴染んだ部屋。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（あれ、これ、それで全部分かるとまでは言わないけど……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（こういうやりとりって恥ずかしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一番恥ずかしいのは、それをする自分が嫌ではないということだ。"


scene bg_gen_sky_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの部屋と一緒に移ってきた、小さな水場。"

play sound se_0642
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ケトルに水を入れて火にかける。\n
そのまま棚に視線を向けて……、はたと気が付く。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（そうだった、もうここにはないのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの小火騒動で壊れたものは、ほとんどなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計も無事だったし、怪我人らしい怪我人も出なかったのだから、僥倖と言ってもいい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう、一つを除いて壊れたものは何もなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「私のカップも、新しいのを探してこなくちゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの作業台にあった私とユリウスのカップは、どちらも割れてしまった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "煤で汚れただけならば、いずれ勝手に戻ったかもしれない。\n
しかし、完全に壊れてしまったものまでは元には戻らないのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（ユリウスのほうにばかり……、目がいっちゃっていたわね）"

play sound se_0470
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースから受け取った包みを開け、新しいマグカップを取り出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_5")
T "（気に入ってくれるかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が選んだものを、傍に置いてくれたら、嬉しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（それが楽しみなんだもの）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「さあ、始めましょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お湯が沸くまでの間は、忙しい。\n
それまでに豆を挽いて、準備を整えなければならないのだから。"

$ hi_mes()
play sound se_0545 volume .6
pause 1
play sound se_0779
pause .15


scene ts_01
with dis

play music honobono2_a_ali
play sound se_0177
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「どうぞ」"


show yuri_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice jul_f0309
Julius "「ああ、ありがとう」"

hide yuri_t_02_12
show yuri_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
Julius "「…………」"

hide yuri_t_02_10
show yuri_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
Julius "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「何？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すぐに返ってきた反応に思わず顔がにやけてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（気付いてくれた？）"


show t_yuri_end11 onlayer master
with dis
hide yuri_t_02_4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が勝手に思いついた、小さな変化だ。\n
流されてしまう可能性も高かったはずだが、彼は不思議そうに目の前のマグカップを見ていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0310
Julius "「使っていたものが壊れたのは知っているが……。\n
こんなもの、あったか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「ふふっ。\n
それは、ユリウスに買ってきたのよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice jul_f0311
Julius "「……私に？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "休憩を取るつもりだったユリウスは眼鏡を外すところだった。\n
だが、彼はそのまま眼鏡を持って、マグカップから視線を外そうとしない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（そんなにじっと見るほどすごいデザインじゃないんだけどな）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（それとも、嫌だったかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あまり飾り気のない、シンプルなもののほうが彼の好みだろうと思って買ってきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、卑屈な私は後ろ向きに考えてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（やっぱり、自分のものを勝手に用意されたら面白くないのかもしれない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（ううん、それ以前に実は思い入れのあるものだったら……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「……気に入らなかった？\n
なら、違うものを探すけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（同じものはないかもしれないけど……、前のものと似たものを探そう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "カップを戻そうとして手を伸ばすが、ユリウスは首を振った。"

hide t_yuri_end11
show t_yuri_end12 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0312
Julius "「……別に、気に入らなかったわけではない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "制止するように触れた手が、私に重なる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「無理しなくていいわよ。\n
誰にだって好みはあるだろうし」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0313
Julius "「そういう意味ではなくてだ、その……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0314
Julius "「何というか、タイミングが悪いというか。\n
いや、これはいいというべきなのか……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（タイミング？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「ひょっとして、私がいない間に買い直していたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスのマグカップは私がこの世界に来てからずっと使っているものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事の合間に珈琲を飲む彼のこと、私が戻る前に買い直していたとしてもおかしくはない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「うわあ……、それはタイミングが悪かったわね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「新しいものはどこにあるの？\n
淹れ直してくるから教えてくれる？」"

hide t_yuri_end12

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何だか恥ずかしくなって、慌てて水場まで戻ろうとする。\n
しかし、そんな私をユリウスは再び引き留めた。"


show yuri_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0315
Julius "「違う。\n
そうじゃなくて、私が買ってきたのは……」"

hide yuri_t_03_3
show yuri_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0316
Julius "「私のカップじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（カップじゃない物を買ってきたのなら、どうしてここでそれが話題になるの？）"

play sound se_0585 volume .7
hide yuri_t_01_9
show yuri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
Julius "「…………」"

hide yuri_t_02_11
show yuri_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice jul_f0317
Julius "「……やる」"

play sound se_0472

play music happy_a_ali

show t_yuri_end13 onlayer master
with dis
hide yuri_t_01_5

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引き出しを開けたユリウスから、押し付けるように小さな包みを渡される。\n
簡易包装に包まれたそれは、ずっしりと手に重さを伝えてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手で触れると、円筒に取っ手のようなものが付いていることが分かった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_4")
T "（もしかして……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jul_f0318
Julius "「おまえに買ったものだ。\n
使うも、捨てるも好きにしろ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは、私のカップが壊れてしまっていたことに、気付いていたのだ。\n
そして、もしかすると彼も、なのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（……お互い、一つのことしか見えなくなる癖があるもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達は、自分よりもすぐに相手のことを見て、考えてしまうから。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「……ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「ねえ、開けてもいい？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice jul_f0319
Julius "「ああ」"

play sound se_0471
hide t_yuri_end13
show t_yuri_end14 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "許可を取ると同時に、包装に手をかけた。\n
子供のように、気持ちが逸る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（早く見たい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どきどきする。\n
中身の予想が付いているのに、それでも期待が高まっていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（びっくり箱とは逆みたい）"

play sound se_0469
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "中身が分からないから驚くのがびっくり箱だとしたら、これはどんな魔法仕掛けの贈り物だろうか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

hide t_yuri_end14
show t_yuri_end15 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "開けてみて、現れたマグカップをまじまじと見てしまった。\n
中身が予想通りだったからではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤くなっているユリウスに視線を合わせて、声をかける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「これって……、私が買ってきたものとお揃い？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice jul_f0320
Julius "「言っておくが、本当に偶然だぞ。\n
私だって、まさかおまえがこんなものを買ってくるとは思わなかったんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_14")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「……っ。\n
ふ、ふふふ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どんな顔をして彼はこれを選んでいたのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が店でユリウスのことを思い出しながら探していたように、彼もまた同じ気持ちだったのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0321
Julius "「な……、笑うことはないだろう、笑うことは！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「だってユリウス、これはメンズ用のカップよ？\n
私には大きいわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "取っ手が大きいほうが確かに持ちやすいが、彼の手と私の手では大きさが大分違う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（パジャマと違って、袖を折ればいいっていうものでもないんだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "以前に買ったお揃いのパジャマのことを思い出していると、彼は赤い顔のまま口を尖らせた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0322
Julius "「私が見た中で一番冷めにくそうだったマグカップがそれだったんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「……実用主義なあたり、あなたらしいわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちゃらちゃらとした飾りなんかよりも、ずっと思いやりを感じる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_19")
T "（同じものを、選んじゃった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが何だかくすぐったく、幸せな気持ちになる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0323
Julius "「別にいいだろう。\n
大きいほうがよく入るし、壊れにくい」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0324
Julius "「口の部分も厚く作ってあるから火傷しにくい作りだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0325
Julius "「それに……、大は小を兼ねると言うだろう！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "{size=+20}「ぶっ！」{/size}"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "状況はまったく違うのに、同じことを二人から言われたことに思わず吹き出してしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_5")
T "（こんなところだけ似ているなんて、不思議な人達）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_5")
Julius "「？？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_4")
T "「ふふ。\n
いえ、何でもないのよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（エースがここにいたら、どんな顔をしたかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "喜んだだろうか、それとも悪乗りして来ただろうか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ちょっと、エースのことを思い出しただけ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jul_f0326
Julius "「エースだと？\n
何だ、おまえ……、エースが作っていたもののほうがよかったのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「まあ、確かにユリウスが作るアクセサリーには興味があるけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はやりとりを見ていて、気にしてくれていた。\n
仕事第一の彼が、物陰に隠れて、我慢できずに迎えに来てくれたのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（宝石だって、嫌いじゃないわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手先の器用な彼のことだ。\n
きっと本職顔負けのすごいものを作ってくれるような気がした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「でも、私には、このカップのほうが似合っているでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「似合わない？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（あなたの選んでくれたものが似合うような、そんな私でいたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背伸びしようとは思わない。\n
この人は、私が私でいることを許してくれる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0327
Julius "「……そうだな」"

play sound se_0177
hide t_yuri_end15
show t_yuri_end16 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "カップを置いたユリウスにならって、作業台にもらったばかりのカップを置く。\n
お揃いのそれに、自然と笑みが零れる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視線が合って、キスを交わした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「………んっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "触れ合う身体から伝わるのは、硬い針の鼓動。\n
そして、机の上から見えない手を伸ばす、淹れたての珈琲の香り。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（この人の一部にならなくても、受け入れられている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな確信に胸が震えた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0328
Julius "「おまえには、そのカップのほうが似合っている」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0329
Julius "「不格好で……。\n
私によく似たカップがな」"



show white onlayer master
with compress_extralong
hide t_yuri_end16
scene black with compress_extraextralong
pause 1
$ renpy.movie_cutscene("endroll_a.mpg")
#return
