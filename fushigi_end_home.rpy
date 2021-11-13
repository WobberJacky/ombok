label fushigi_end_home1:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「行けないわ。\n
だって、私には帰る家があるんだもの」
 "

show jo_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jok_f0384
White_Joker "「……君は、彼らのいる場所が、本当に君の家だっていうのかな」
 "
hide jo_t_03_9
show jo_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jok_f0385
White_Joker "「ここにいるのに迎えにも来なかった連中がいる場所が、本当に君の家？\n
同じ場所に住む仲間や家族なの？」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーに後ろから抱きしめられ、耳元で囁かれて、戸惑う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「それは……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（忙しかったのかもしれないし、来られない理由があったのかもしれないじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "皆、それぞれに役割があるから、私にばかりかまけていられない。\n
役を、顔を持っている彼らですら、この世界のルールには従わなくてはいけない。"

hide jo_t_02_12
show jo_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0386
White_Joker "「いいじゃないか、そんなに急いで帰らなくても。\n
いたいだけいて、戻る気になったら帰ればいい」"

hide jo_t_02_7
show jo_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0387
White_Joker "「この世界の人間は、誰も彼も、君には甘いんだから。\n
少しぐらい離れていたところで、君を責めたりしな……、ん？」"

play sound se_0273
pause .1
play sound se_0273
hide jo_t_02_4


scene bg_gen_sky_all_day
with dis
play sound se_0022
$ flash(.1)
play sound se_0028
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0049
Danin "「ジョーカー！！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0045
W "「ジョーカー、危ない！」"

##special anime juugeki
play sound se_0022
pause .3
play sound se_0028
pause .3
play sound se_0022
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0046
W "「きゃああっ」"

play sound se_0022
$ flash(.1)
play sound se_0028
$ flash(.2)
play sound se_0028
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

play sound se_0354
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくつもの銃声が唐突に鳴り響いて、団員の子供達は悲鳴を上げる。\n
銃撃を避けたジョーカーは、私の背後から離れた。"


play music opposition2_a_ali

scene md_01 with dis

show bor_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0330
Boris "「勝手なことを言わないでくれないかな、ジョーカーさん。\n
その子はやれないよ」"

hide bor_t_01_8
show bor_t_01_8 at left
show per_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0456
Peter "「不本意ながら、今回だけは僕も君の意見に賛成ですね。\n
彼女を離しなさい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「ボリス、ペーター！？\n
えっ、あなた達、どうしてここにいるのよ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスもペーターも、それぞれドアを開けたまま、ジョーカーに銃を突きつけている。"

hide bor_t_01_8
show bor_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0331
Boris "「へえ、宰相さんよく間に合ったね。\n
俺はどこにでも繋げられるけど、真っ向からここに来るのは結構面倒だったんじゃない？」"

hide bor_t_01_10
show bor_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0332
Boris "「ドアを使ったってことは、クローバーの塔まで行ったってことだもんね」"

hide per_t_03_7
show per_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0457
Peter "「面倒だなんて、少しも思いませんね。\n
彼女がこんな場所に引き込まれるほうがよほど問題です」"

hide per_t_02_11
show per_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0458
Peter "「それを思えば、どんな場所にでも行きますよ。\n
その結果、どんな代償を求められたとしても構いません」"

play sound se_0291
camera at hpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足で乱暴にドアを閉めたペーターは、ジョーカーを睨んだまま平然とそう言った。"


show jo_t_03_15 at center
hide bor_t_03_2

hide per_t_02_9
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0388
White_Joker "「おやおや、招かれざる客……、もとい、招かれざる獣達のお越しだね」"

hide jo_t_03_15
show jo_t_03_19 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0389
White_Joker "「悪いけど、うちはもう動物のほうは間に合っているんだ。\n
しかも、君達に業を覚えさせるのは酷く手がかかりそうだし」"

hide jo_t_03_19
show jo_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0390
White_Joker "「君の周りにいるのは、調教には向かなそうなのばっかりだよね。\n
トカゲに、ネズミもいたかな……、素直じゃないのばっかりだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "くくくと肩を震わせるジョーカーは銃を突きつけられているというのに余裕だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ホワイトさんとブラックさんで二人いるから、見た目の数では変わらないが、ブラックさんはあからさまに顔を顰めている。"

hide jo_t_01_6
show jo_t_01_6 at left
show jo_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0391
Black_Joker "「ちっ、野良猫と宰相ウサギか。\n
ああ、面倒くせえなあ」"

play sound se_0347
$ flash(.1)
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人を迎え撃つように二人のジョーカーもまた銃を構える。\n
しかし、彼らの銃が火を噴くよりも早く、再び銃声が響き渡った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ペーターやボリスのいる場所からじゃない。\n
一体、どこから？）"


show t_end_home1 onlayer master
with dis
hide jo_t_01_6

hide jo_t_02_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice blo_f0493
Blood "「そうか？\n
……ならば、もっと面倒にしてやろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
White_Joker "「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jok_f0392
Black_Joker "「ちっ、なんでてめえまで出てきてんだよ、ブラッド＝デュプレ！」"

play sound se_0521
$ flash(.1)
play sound se_0521
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこからともなく現れたブラッドの姿に、吐き捨てるようにブラックさんが声を荒げた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "名を呼ばれた本人は飄々としたまま、銃を操っている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice blo_f0494
Blood "「それはずいぶんな言われようだな、\n
ジョーカー。私の退屈を紛らわせてくれる貴重なお嬢さんが、どことも知れぬ場所に行こうとしているんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice blo_f0495
Blood "「邪魔をしないほうがおかしいというものだ。\n
……あまり、私を見くびってくれるな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ブラッド」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "マシンガンを構えたマフィアのボスは私の声に気付いたのか、口の端を持ち上げてみせた。\n
本心の見えない、彼らしい笑い方だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0527
Nightmare "「そうだぞ、ジョーカー。\n
私達がおめおめと、おまえに彼女を奪わせるとでも思っていたのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "煙管を手にした夢魔は、ふわりと浮きながら私の横に現れた。\n
ぽんと肩に乗せられた手は、体温が低く冷たい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ナイトメアまで……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（先刻までどこにもいなかったのに）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice nig_f0528
Nightmare "「夢で呼んでくれればすぐに迎えに来たのに。\n
おかげで、ずいぶん大きな荷物を持たされる羽目になったよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice blo_f0496
Blood "「ああ、おかげで私は楽が出来た。\n
今だけは礼を言っておこう、芋虫」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice blo_f0497
Blood "「まあ、夢の中ならともかく、こういう場所では戦力外なんだ。\n
それぐらいしてもらわなければな」"

play sound se_0521
$ flash(.2)
$ flash(.2)
play sound se_0519
pause .2
play sound se_0519
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（ナイトメアと一緒に、ブラッドもついてきたっていうことかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どういう方法なのかは分からないが、彼らの話を総合するとそうなる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（ペーターも、結構面倒なことをしたみたいだし……。\n
でも、どうしてそこまでして追いかけてきてくれたんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が飛び出してきた滞在地の人間ならまだ分かる。\n
でも、彼らの居場所はそれぞれ別だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（この顔ぶれが揃うこと自体、珍しい）"

play sound se_0520
$ flash(.1)
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃声が響き渡り、殺伐とした緊張感が漂っているにも関わらず、私はそんなことを思う。\n
どこか夢の中のような心地だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0529
Nightmare "「私達には、ここに来るだけの理由があっただけの話さ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0530
Nightmare "「チェシャ猫も言っていただろう。\n
君を、ジョーカーの仲間入りさせるつもりはないよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0459
Peter "「当たり前です。\n
どんな理由があろうと、あの道化にだけは渡すつもりはありません」"

## special anime
play sound se_0028
pause .1
play sound se_0028
pause .3
play sound se_0028
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアを使って銃弾を防いでいた少年達が、その言葉に怒ったように声を上げた。"

hide t_end_home1 with dis


show j-boy_a_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0050
Danin "「酷いよ！\n
その子だって、僕達と一緒に行きたいかもしれないじゃないか！」"

hide j-boy_a_11
show j-boy_a_11 at left
show j-girl_a_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0047
W "「そうよそうよ！私達だってその子が好きだもの！\n
横取りしないでちょうだい！！」"
show jo_t_02_5 at center
hide j-boy_a_11
hide j-girl_a_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0393
Black_Joker "「おうおう。\n
好かれたもんだな、お嬢ちゃん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（相変わらず、あなたには好かれていなさそうだけどね）"

hide jo_t_02_5
show jo_t_02_5 at left
show jo_t_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice jok_f0394
White_Joker "「それで、君はどうしたいんだ？\n
家に帰るの？\n
……俺達についてくるという選択肢も、悪くないと思うんだけどな」"

play sound se_0521
hide jo_t_01_5

hide jo_t_02_5
with dis

show white onlayer master ##instant
pause .5
hide white ##instant

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って笑ったジョーカーの頬を、銃弾が掠った。"

play sound se_0313

show jo_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0395
White_Joker "「おっと、話の途中で撃つなんて酷いことをするなあ」"

hide jo_t_03_2
show jo_t_03_2 at left
show bra_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0498
Blood "「お褒め頂き光栄だと言っておこう。\n
おまえも知っての通り、私は悪党だからな。不意打ちも遠慮なくさせてもらうさ」"

hide bra_t_03_10
show bra_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0499
Blood "「おい、いつまでのんきに話しているんだ、芋虫。\n
早く連れ戻せ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（連れ戻せ？）"

hide jo_t_03_2

hide bra_t_02_3
with dis

show t_end_home2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よくよく見てみれば、ナイトメア以外の三人は私から離れた場所にいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の近くにいるのは、ナイトメアとそして……。\n
ジョーカーだけだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0531
Nightmare "「ここはジョーカーの領域に近いからね。\n
君がその気になってくれないと、引き戻せない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0396
White_Joker "「……甘くなったものだね、ナイトメア。それは正解じゃない。\n
君は夢魔なんだから、無理矢理、力ずくにでも引き戻せるはずだろう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0397
Black_Joker "「夢に引き込んじまえば、こんなことしなくてもよかっただろうに。\n
本当に、甘えな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T "（ナイトメア、どういうこと……？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーの言葉を確かめるように彼を見れば、夢魔は苦笑いを浮かべていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice nig_f0532
Nightmare "「大したことじゃないさ、私は有能だが、万能じゃないのでね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice nig_f0532_5
Nightmare "「君を監獄に行かせるわけにはいかないが、後悔で傷だらけになった君を連れて帰るのもごめんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice nig_f0533
Nightmare "「私はね、[firstname]、君を迎えに来たんだよ。\n
帽子屋も、チェシャ猫も、白ウサギも同じくね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（迎えに来た？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_2")
T "「でも……、私だって帰るつもりだったのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの言い方では、私がずっとジョーカーの傍にいることを望んでいるように聞こえてしまう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0534
Nightmare "「……そうだね。\n
だけど、君がこの場所に惹かれているのも事実だろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「それは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "否定しきれない。\n
強く拒むことも出来ず、ずるずると引きずられてしまったのは事実だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0535
Nightmare "「だから、君の意志で私達のところに戻ってきてほしいんだ。\n
今の君の居場所は、サーカスでも監獄でもないだろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0333
Boris "「夢魔さんの言う通りだよ、俺はあんたがどこにいても、会いに行くけどね。\n
でも、近くにいてくれたほうがいいと思ってるんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice blo_f0500
Blood "「こんな面倒なところにまで出てきたんだ。\n
まさか、私を手ぶらで帰すようなことはしないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice blo_f0501
Blood "「……君がいないと、退屈だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice jok_f0398
White_Joker "「酷いなあ、これじゃあどっちが悪党だか分からない。\n
ナイトメア、君は俺に近いのに、そんなにこの子に嫌われるのが嫌なんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice mat_f0051
Danin "「そうだよ、僕達だって悪いことをしているわけじゃないのに！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアの陰から文句を言う彼らは、合間を見ては私に手招きをしてくる。\n
こっちにおいでというように。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0048
W "「早く来て、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice pet_f0460
Peter "「黙りなさい」"

play sound se_0028
$ flash(.3)
play sound se_0028
$ flash(.1)
play sound se_0028
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Peter "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_4")
voice pet_f0461
Peter "「戻りましょう、あなたの帰る場所に。\n
そこがどこであっても、サーカスの一員になるよりはずっとましです」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_3")
voice nig_f0536
Nightmare "「選ぶのは、君だよ、[firstname]。\n
さあ、どちらを選ぶ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（どちらを選ぶかなんて……、そんなの、最初から決まっているのに）"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスにずっといる気はなかったし、一緒には行けないとも言った。\n
私はナイトメアにそっと寄り添う。"


$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0537
Nightmare "「……ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "当然の選択だったはずなのに、私を引き寄せたナイトメアの声はどこかほっとしたように聞こえた。"


play music looking_for_a_ali
hide t_end_home2


show jo_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0399
White_Joker "「何だ、結局そっちに行くの。\n
残念だなあ、[firstname]」"

play sound se_0022
$ flash(.2)
play sound se_0022
hide jo_t_01_14
show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0400
White_Joker "「おっと危ない……。\n
まったく、君達は油断も隙もないね」"

hide jo_t_03_1


show bor_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0334
Boris "「油断も隙もないのはそっちだろう、ジョーカーさん。\n
人のものに横から手を出そうなんて、図々しいんだよ」"

hide bor_t_02_8
show bor_t_02_8 at left
show bra_t_02_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0502
Blood "「ふむ、今回ばかりはおチビさんの言うとおりだな。\n
邪魔者にはさっさと退場してもらうに限る」"


show nai_s_01_8 at center
hide bor_t_02_8
hide bra_t_02_14
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0538
Nightmare "「こっちだ、[firstname]」"

play sound se_0521
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃声が響く中、ナイトメアは私の手を引く。"

play sound se_0158
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一歩ずつ、一歩ずつ。\n
サーカスから離れていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逆に私を迎えるようにボリスとペーターは立ち位置をずらして、場所を確保しようとしていた。"


show jo_t_03_8 at center
hide nai_s_01_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0401
White_Joker "「ふふふ、好かれているね、[firstname]、君はとても人気者だ。\n
そういう人気者は、サーカスにいるのが一番なんだけどなあ、残念だよ」"

hide jo_t_03_8
show jo_t_03_8 at left
show per_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0462
Peter "「消えろと言っているんです。\n
しつこいですよ、ジョーカー！」"

play sound se_0028
pause .4
play sound se_0028

show jo_t_01_7 at center
hide jo_t_03_8

hide per_t_01_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0402
Black_Joker "「うぜえウサギ……、とはいえ、さすがにこいつらを相手にする気にはなれねえ。\n
俺は下りるぞ、ジョーカー。\n
ほらおまえら、そこどけ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "多勢に無勢のためか、ブラックさんはそう言うとさっさと銃を片付けて、ドアへと身体を踊らせた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "当然のようにドアの近くにいた子供達は不満そうに口を尖らせる。"

hide jo_t_01_7


show j-boy_a_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0052
Danin "「ええっ、ジョーカー、諦めるの？」"

hide j-boy_a_5
show j-boy_a_5 at left
show j-girl_a_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0049
W "「私は嫌よ。\n
だってせっかく彼女の近くにいられたのに……」"

hide j-boy_a_5

hide j-girl_a_9
show j-girl_a_9 at left
show jo_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0403
Black_Joker "「は……っ、あいつはどうせ逃げ切れやしねえよ。\n
安心しろ、どうせ、いずれまた巡るんだ、季節と同じでな」"

hide j-girl_a_9

hide jo_t_01_3
show jo_t_01_3 at left
show per_t_01_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0463
Peter "「いいえ、あなた達になんて捕まえさせません。\n
僕がそうさせない」"


show jo_t_02_4 at center
hide jo_t_01_3
hide per_t_01_14
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0404
White_Joker "「それは頼もしい言葉だね、ペーター＝ホワイト。\n
君の愛情には感動するよ、でもそれは……」"

play sound se_0521
$ flash_red(.2)
hide jo_t_02_4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "皮肉を含んだ言葉の続きは、ブラッドがジョーカーの肩を打ち抜いたことで阻止される。"


show bra_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0503
Blood "「退場しろと言っただろう、道化。\n
まだ殺され足りないのか？」"


show jo_t_02_7 at center
hide bra_t_01_9
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0405
White_Joker "「ふ、ふふふ。\n
さすがに、これでは分が悪すぎるな」"

play sound se_0041
pause .4
play sound se_0178
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぽーんと地面を蹴って、残っていたジョーカーもドアの傍に立つ。\n
開いたままのドアの下からは私の様子を伺う子供が見えた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "肩を撃たれているとは思えないほどのんびりとした口調で、ジョーカーは最後に私を見つめてくる。"

hide jo_t_02_7
show jo_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0406
White_Joker "「残念ながらサーカスの最終公演は、これにてお開きらしいね。\n
[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

hide jo_t_03_8
show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jok_f0407
White_Joker "「次のときには、もっと楽しい思いをさせてあげるよ」"

play sound se_0022
pause .1
play sound se_0022
pause .3
play sound se_0022
hide jo_t_03_1
show jo_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jok_f0408
White_Joker "「また季節が巡る頃に会おう。\n
それでは、また」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後の銃弾をかわして、ジョーカーはドアに手をかけた。"

hide jo_t_01_11

pause 1
play sound se_0664

show door1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"


play music forest1_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアが閉ざされ、森の中にようやく静けさが戻った。"

hide door1 with Dissolve(2)

show bor_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0335
Boris "「ちっ、仕留め損なったか。\n
本当に余計なちょっかいを出すのはやめてほしいよね」"

hide bor_t_03_13
show bor_t_03_13 at left
show nai_s_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0539
Nightmare "「それがジョーカーの役割だからな。\n
看守がルールを破っていたら、どうしようもない」"

hide bor_t_03_13

hide nai_s_02_11
show nai_s_02_11 at left
show bra_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0504
Blood "「やれやれ、面倒極まりない。\n
難儀な役割だな」"

hide nai_s_02_11

hide bra_t_03_13
show bra_t_03_13 at left
show per_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0464
Peter "「誰もあなたに手伝えなんて言っていませんよ、ブラッド＝デュプレ。\n
面倒は嫌いなんでしょう、だったらしゃしゃり出てこなくて結構です」"

hide per_t_02_4
show per_t_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0465
Peter "「彼女は僕が守ります。\n
足手まといはいりません」"

hide bra_t_03_13
show bra_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0505
Blood "「ふっ。\n
言うじゃないか、宰相閣下」"

play sound se_0376
$ flash(.2)
$ flash(.1)
$ flash(.3)
$ flash (.4)

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴりっと睨み合った二人は、銃を手にしたままだ。"

hide bra_t_01_3
hide per_t_03_9
with Dissolve (1.6)
play sound se_0515
pause .8
play sound se_0515
pause .4
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "共闘していたはずの彼らが撃ち合いを始めそうになると、ボリスが声をかけた。"

play sound se_0122

show bor_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0336
Boris "「ほらほら、せっかくジョーカーさんが消えたのに、二人がやりあったら意味がないだろう」"

hide bor_t_02_7
show bor_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0336_5
Boris "「な、あんたもそう思うよな、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「ボリスの言う通りよ。\n
銃声はもう結構だわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（これ以上聞かされたら、耳がおかしくなりそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスの団員達が消えると、どこか虚ろだった私の意識もはっきりしてくる。"

play sound se_0267
show bra_t_02_18 at center
hide bor_t_02_8
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0506
Blood "「……やれやれ、お嬢さんが言うのなら仕方ない。\n
私も、ウサギ退治などさほど興味もないからな」"

play sound se_0267
hide bra_t_02_18
show bra_t_02_18 at left
show per_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0466
Peter "「あなたこそ、彼女の寛大さに感謝することですね。\n
キャラが被っている男なんて、ジョーカーの次に撃ち殺したいのに」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（そこはまったく被っていないから安心しなさい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドとペーターの似ているところなんて、すぐに銃を持ち出すことくらい。\n
だがそれは、この世界の人間のほとんどに共通している。"


show nai_s_02_3 at center
hide bra_t_02_18
hide per_t_01_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0540
Nightmare "「……二人とも、その辺りにしておけ。\n
君も疲れただろう、そろそろ家に戻ろう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（……私の家）"

hide nai_s_02_3
show nai_s_02_3 at left
show bor_t_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice bor_f0337
Boris "「俺のドアを使えばすぐに帰れるから、あんたの帰りたい場所に繋げてあげる。\n
迷わせたりしないから、安心していいよ、[firstname]」"

play sound se_0282

show per_t_02_4 at center
hide bor_t_03_4
hide nai_s_02_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice pet_f0467
Peter "「いいえ、そんなものを使う必要はありません！」"

play sound se_0664
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスが開けてくれたドアをペーターは私の返事を聞く前に、閉めてしまった。"

hide per_t_02_4
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice pet_f0468
Peter "「そんな得体の知れないものを使わなくても、僕があなたを送っていって差し上げます、[firstname]！」"

hide per_t_03_1
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice pet_f0468_5
Peter "「あなただって、こんなどこに行かされるか分からないものを使うより、ずっといいでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_11")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（せっかくボリスが開けてくれたのに、即行で閉めなくても）"


show bor_t_02_8 at center
hide per_t_03_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice bor_f0338
Boris "「……宰相さん、喧嘩売ってんの？\n
俺、ダムじゃないからケチらないし、そういうつもりなら金を出してでも買うよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひくっと顔を引きつらせたボリスには構わず、ペーターはいそいそと私の肩を抱いて歩き始める。"

play sound se_0623

show per_t_02_8 at center
hide bor_t_02_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0469
Peter "「疲れているなら、抱き上げて帰ればいいですし。\n
どうやって帰りましょうか、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「いや、普通に帰れるから」"

hide per_t_02_8
show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice pet_f0470
Peter "「遠慮しないでください！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（……遠慮じゃないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何が哀しくて、知り合いの目の前でお姫様抱っこをされて森を抜けなければならないのか。"

hide per_t_02_5
show per_t_02_5 at left
show bra_t_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0507
Blood "「なら、私がエスコートをしようか？\n
宰相閣下よりもずっと快適に抱えていってあげよう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「結構よ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（いきなり横から出てきたと思ったら、こっちはこっちでろくなことを言わない）"

hide per_t_02_5
show per_t_02_5 at left_center
hide bra_t_03_1
show bra_t_03_1 at center
show bor_t_02_6 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice bor_f0339
Boris "「じゃあ、[firstname]、[firstname]。\n
俺がおぶろうか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「ボリス……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（なんで、あんたまで混ざってきているのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、この場にいる最後の一人はというと。"


show nai_s_03_5 at center
hide bor_t_02_6

hide bra_t_03_1

hide per_t_02_5
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0541
Nightmare "「……うう。\n
そもそも、この面子ではこと体力に関しては勝ち目がない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "木の陰で一人うずくまっていじけていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（あんたが体力で勝てる相手なんていないでしょうが）"

hide nai_s_03_5
show nai_s_03_5 at left

show bor_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice bor_f0340
Boris "「ああ、夢魔さんじゃ確かに無理だね。\n
抱きかかえようとしたところで力尽きそう」"

hide nai_s_03_5
show nai_s_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0542
Nightmare "「君まで酷いことを言うんじゃない、チェシャ猫！\n
ああ、大声を出したら気分が悪くなってきた」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「……はあ。\n
仕方がないわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターとブラッドの手を払いのけて、ナイトメアの元に戻る。\n
それから、ナイトメアが私にしてくれたように、手を差し出した。"

play sound se_0267
show t_end_home3 onlayer master
with dis
hide bor_t_03_11

hide nai_s_02_10
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_8")
T "「仕方ないから、森の入り口まで手を引いていってあげる」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T "（先刻のお返しよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーの傍から私を離したときに、ナイトメアがしてくれたことを返すだけ。\n
ただそれだけだ、深い意味はない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だというのに。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（振り返るまでもなく、背後の二人が睨んでいるのが分かる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "無言の圧力がひしひしと伝わってくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0543
Nightmare "「……心の中はもっと酷いことを考えているんだぞ。\n
心が狭い奴らめっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「はいはい、じゃあ帰りましょう」"

play sound se_0267
hide t_end_home3
show t_end_home4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_8")
voice nig_f0544
Nightmare "「ああ、そうだな。\n
君を待っている家に帰ろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは私の手を握って立ち上がり、歩き出した。"

hide t_end_home4

pause .4
$ hi_mes()

scene bg_gen_sky_all_day with Dissolve(1.6)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「ええ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この場所にいる人だけではなく、他にも私の帰りを待ってくれている人がいる。\n
ただいまと言える家に、私は帰るのだ。"

hide frame_gen_togaki
hide ali_t_06_16
with Dissolve(5)

scene black with Dissolve(5)

$ renpy.movie_cutscene("endroll_c.mpg")
#return
