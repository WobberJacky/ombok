label fushigi_end_bad_hatter1:
scene md_01
play music forest2_p_ali
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T "「……いつでも帰れるのなら、少しだけ行ってみようかしら」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_17")
T "（飽きられてしまったのかもしれない） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "元々彼は自他と共に認める、気紛れな男だ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "余所者としての珍しさが薄れたのなら、ブラッドにとって私は、取り戻すだけの価値を持たない人間ということになる。 "


show jo_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0414
Joker "「そうだね、君は自分がどこにいるべきなのか、誰よりもよく知っている子だ。\n
……さあ、行こう」 "


show j-boy_a_7 at center
hide jo_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice mat_f0053
Danin "「こっちだよ、早く！」 "

hide j-boy_a_7 at center
show j-boy_a_7 at left

show j-girl_a_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice nos_f0050
W "「待ちくたびれちゃったわ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "ドアのノブはジョーカーの手の中にある。\n
誘うように手招きをする子供達のほうへ足を向けて。 "

hide j-boy_a_7 at left

hide j-girl_a_8 at right
with dis
play sound se_0521

scene bg_gen_sky_sum_day with dis
pause 1
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_6")
T "「！！？」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_6")
voice jok_f0415
Joker "「おや……。\n
今頃になって来たのかな？」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_6")
voice mat_f0054
Danin "「ジョーカー！\n
危ないよっ」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_6")
voice nos_f0051
W "「後ろにいるわ！」 "

play sound se_0347
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "突然の銃声は、私の背後から響いている。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T "（誰？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "まさかと思った。\n
だが、このタイミングで他の誰かが来るとも思えない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T "（ブラッドが、迎えに来てくれたの？） "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_15")
T "「ブラッ……」 "

play sound se_0126
pause .7
play sound se_0646
show splatter onlayer master
$ flash_red(.2)
hide splatter
pause 2
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T "「え」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_6")
T "「！！？」 "


play music opposition1_a_ali fadein 1
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "振り返り様、身体に走った衝撃に目を見開く。\n
銃声で気付かなかったが、私の真後ろに誰かがいたらしい。 "


scene md_01 with dis

show dee_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0562
Dee "「……ごめんね、お姉さん。\n
でも、これ以上痛いことはしないから」 "

hide dee_s_03_10 at center
show dee_s_03_10 at left

show dam_s_03_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0563
Dam "「一回だけで、すませたよ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "聞いたこともない苦い声。\n
しかし、その声の主を私は知っている。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T "「！？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_11")
T "「ディー、ダム……？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_16")
T "（これ以上痛いことはしない？） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_8")
T "（一回だけですませた？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "言われている意味が分からない。\n
私の横を通り抜けた双子のほうに顔を向けようとして、視界が乱れた。 "

hide dee_s_03_10 at left

hide dam_s_03_14 at right
camera at hpunch

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T "「え……」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T "「あっ」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_16")
T "（どうして？） "
play sound se_0553
camera at hpunch
camera at hpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "足に力が入らない。\n
身体を支えきれずに、そのまま地面に倒れてしまう。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_8")
T "（一体どうしたのよ） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "地面に手を着いてから、足を見て。 "

$ hi_mes()
pause 2
show t_end_confined1and3 onlayer master with dis
pause .5
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_15")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_13")
T "（え？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "靴下が真っ赤に染まっている。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0416
Joker "「おやおや、可哀想に。\n
いくら彼女が惑わされているからって……」 "

play sound se_0638 volume .5
play sound se_0550 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T "「あ……」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_3")
T "「うそ」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_4")
T "（私、今、一体どうなっているの？） "
$ flash_red(1)
pause 3
$ flash_red(1)


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "ずきんずきんと、鈍い痛みが今更のように生まれてくる。\n
靴下の模様も分からないほど、両足が血に濡れていた。 "
pause 1
play sound se_0678
pause .3
play sound se_0439

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0564
Dee "「黙れよ、ジョーカー。\n
元はといえば、おまえがお姉さんに余計なことをするからだろう」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0565
Dam "「おまえは足なんかじゃなくて、首を斬ってあげるよ」 "

play sound se_0677
pause .2
play sound se_0678
pause .5
play sound se_0441
play sound se_0440
pause .2
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "斧を振り回しながら、帽子屋ファミリーの門番、ブラッディ・ツインズは怒りを露にしていた。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0417
Joker "「八つ当たりするんじゃねえよ、ガキ。\n
そのお嬢ちゃんがここに来たのだって、元を辿ればおまえらのせいだろうが」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "二人のジョーカーは、その斧をかわしながら、笑っている。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0418
Joker "「甘やかして、いい顔を見せて、最後は翼を落として、籠の中に……。\n
ふふふ、面白いなあ、君達にはお似合いの結末じゃないか」 "
play sound se_0021
$ flash(.1)
pause .3
play sound se_0021
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0419
Joker "「おやおや、ずいぶん大所帯で来たものだね」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "派手な銃声が響いて、ジョーカーが溜息をつく。 "

show t_end_confined2 onlayer master with dis
hide t_end_confined1and3 with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0343
Elliot "「とっとと失せろ、ジョーカー。\n
いつまでもだらだらと長居してんじゃねえ」 "
play sound se_0021
$ flash(.1)
pause .1
play sound se_0021
$ flash(.1)
pause .4
play sound se_0021
$ flash(.1)

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_4")
T "「エリオット？」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_4")
Elliot "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "私の横を抜けていったエリオットは、一瞬だけ私を見たが、何も言わなかった。\n
ただ、一瞬だけ、哀しそうな目をしたように見えたのは気のせいだろうか。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T "（痛い） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_12")
T "（痛いはずなのに……、何も考えられない） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "血が流れすぎているせいか、体も冷たくなっていく。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0344
Elliot "「ほら、さっさと退場しろって言ってるんだよ！」 "
play sound se_0772
$ flash(.1)
pause .1
play sound se_0677
$ flash(.1)
pause .1
$ flash(.2)
play sound se_0678
pause .5
play sound se_0440
pause .2
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "銃を撃つエリオットと、斧を振り回しているディーとダム。\n
彼らは、私に見せないようにしてくれていた、マフィアの顔をしていた。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_5")
T "（……どうして？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "そんな彼らを見て怖いと思う気持ちよりも、哀しいと思ってしまったのかは、私にも分からない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_3")
T "（動けなくなったのは私なのに） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "彼らも同じぐらい、傷ついた顔をしているように見えた。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0420
Joker "「危ないなあ、俺は武闘派じゃないっていつも言っているじゃないか。\n
ジョーカーなら相手をしてくれるかもしれないけど……、どう、代わってみる？」 "

play sound se_0678
pause .4
play sound se_0439
pause .4
play sound se_0677
pause .3
play sound se_0678
pause .2
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "その中で二人のジョーカーだけが、遊んでいるかのように会話を続ける。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0421
Joker "「俺だって、こんな～～～～共の相手を押し付けられるのはごめんだぜ。\n
撤収作業にでずっぱりで疲れてんだよ、俺様は」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0345
Elliot "「だったら、とっとと消えろよ！\n
こいつの前に、二度と出てくるんじゃねえ！！」 "
play sound se_0021
$ flash(.1)
pause .3
play sound se_0021
$ flash(.1)
pause .1
play sound se_0021
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "緊張感のないジョーカーのやりとりに苛立ったエリオットは、さっきから銃を撃ち続けている。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0422
Joker "「おお、怖い怖い。\n
そうだね、幕はもう引いたんだし、このあたりがちょうどいい頃合いかな」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0423
Joker "「いいものも、見せてもらったしね。\n
ふふふ、この後、君達が彼女をどうするのかも見てみたいけど……」 "

play sound se_0677
pause .2
play sound se_0678
pause .5
play sound se_0441
play sound se_0440
pause .4
play sound se_0021
$ flash(.1)
pause .2
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0424
Joker "「それはまた次の楽しみにとっておくよ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "飄々と攻撃を避けて言いながら、二人のジョーカーはドアの近くへと身体を寄せていく。 "

hide t_end_confined2 with dis


show j-boy_a_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice mat_f0055
Danin "「ジョーカー……」 "

hide j-boy_a_12 at center
show j-boy_a_12 at left

show j-girl_a_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice nos_f0052
W "「ええー、もう行くの？\n
この子と一緒に行けると思ったのに、結局連れていけないの？」 "

hide j-boy_a_12 at left
show jo_t_02_8 at center
hide j-girl_a_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0425
Joker "「そんなに連れていきたいんだったら、てめえでどうにかしろよ。\n
あのいかれたウサギと、ガキ共を追っ払ってな」 "

hide jo_t_02_8 at center
show jo_t_02_8 at left

show j-boy_a_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Danin "「…………」 "

hide jo_t_02_8 at left
show j-boy_a_12 at left
hide j-boy_a_12 at right
show j-girl_a_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
W "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "ブラックさんの言葉に子供達は声を失ったまま私を見たが、やがて諦めたように首を振った。 "

hide j-boy_a_12 at left
show j-boy_a_16 at left
hide j-girl_a_12 at right
show j-girl_a_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice mat_f0056
Danin "「……仕方ないか」 "

hide j-boy_a_16 at left
show j-boy_a_16 at left
hide j-girl_a_12 at right
show j-girl_a_16 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice nos_f0053
W "「ええ、残念だけど」 "

hide j-boy_a_16 at left

hide j-girl_a_16 at right

play sound se_0678
pause .4
play sound se_0439
pause .4
play sound se_0677
pause .3
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "逃がさないように双子が追撃を仕掛けるが、彼らの斧でさえもジョーカーには届かない。 "


show jo_t_03_17 at center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0426
Joker "「そういうこった。\n
じゃあな、俺はお先に失礼させてもらうぜ」 "

hide jo_t_03_17 at center
show jo_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0427
Joker "「どうぞ……。\n
おっと、さすがに狙いが一人に絞られると厳しいな」 "

hide jo_t_01_13 at center

play sound se_0772
$ flash(.1)
pause .1
play sound se_0677
$ flash(.1)
pause .2
$ flash(.1)
play sound se_0678
pause .5
play sound se_0440
$ flash(.1)
pause .2
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "厳しいと言いながらもジョーカーの身体に銃弾や刃が掠った様子はない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "サーカスの団長は軽やかに身を翻しながら、もう一人の道化の後を追うように、ドアへと入った。 "


show dee_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0566
Dee "「逃がさないよ！」 "


show jo_t_03_9 at center
hide dee_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0428
Joker "「それは無理だよ、君達に、俺は殺せない。\n
それに捕まえるのは、君達でも、俺の役割でもないだろう」 "

hide jo_t_03_9 at center
show jo_t_03_14 at center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice jok_f0429
Joker "「それじゃあ、[firstname]。\n
またの機会に」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "私を見たジョーカーは、無機質な笑みを浮かべて、ドアに入っていった。 "

play sound se_0276
pause .6
play sound se_0664
hide jo_t_03_14 at center

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "そうして、ドアはぱたりと閉まる。 "

play sound se_0441
pause .3
play sound se_0782
pause .1
play sound se_0280
$ flash(.1)
pause .15
play sound se_0280
$ flash(.1)
stop music fadeout 1
play music forest1_p_ali fadein 1
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "ドアが閉まったその直後に、斧と銃弾がドアに食い込んだが、既にサーカスの一団は姿を消していた。 "


show dam_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0567
Dam "「ち……。\n
逃げられた」 "

hide dam_s_02_3 at center
show dam_s_02_3 at left

show eri_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0346
Elliot "「くそ……。\n
～～～～～～～～！！！」 "

play sound se_0286
camera at hpunch
camera at vpunch
play sound se_0286
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "怒ったようにエリオットは何度も何度もドアを蹴っている。\n
何かどうしようもない苛立ちを、それで紛らわせようとするように。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_12")
Blood "「[firstname]」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T "「！！！」 "

hide dam_s_02_3 at left
show bra_t_02_14 at center
hide eri_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_12")
voice blo_f0548
Blood "「こんなところに迷い込むなんて……、困ったお嬢さんだな、君は」 "


show t_end_confined1and3 onlayer master with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_3")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "斬りつけられたのは、足だけ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "手も、首も、喉も、他はすべて無事だ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "なのに、私の身体は凍りついたように動けずにいた。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T "（声まで、出ないなんて） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "背後に立つ男の空気に、呼吸さえままならなくなる。 "

play sound se_0550 volume .7
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "傷の痛みなのか、それとも心臓の鼓動なのか。\n
一定のリズムで脈打つ何かが警報のように鳴っていた。 "


hide t_end_confined1and3

hide bra_t_02_14 at center
show bra_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0549
Blood "「ああ、足が痛くて動けないのか。\n
それは悪かった」 "

play sound se_0142
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "ブラッドは白い布で手際よく私の足を包み込んでいく。 "

hide bra_t_01_5 at center
show bra_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0550
Blood "「屋敷に帰ったら、ちゃんとした治療をしてあげよう。\n
もう歩けないだろうが、君の身体に傷が残るのは私としても不本意だ」 "


show t_end_confined4 onlayer master with dis
hide bra_t_01_11 at center

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_8")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "足に触れられている。\n
自分の目でも確認しているはずなのに、どうしても現実だとは思えない。 "

hide t_end_confined4


show dee_s_01_1 at left

show dam_s_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_16")
T "（ディーとダムが、私の足を斬って） "


show eri_t_03b_12 at center
hide dee_s_01_1 at left

hide dam_s_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_3")
T "（エリオットが哀しそうな顔をしていて） "


show bra_t_02_18 at center
hide eri_t_03b_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_5")
T "（ブラッドが傷に布を巻いている） "

play sound se_0055 volume .6

show t_end_confined4 onlayer master with dis
hide bra_t_02_18 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T "「あ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "軽い圧迫感を覚えて、ようやく状況が頭に染み込んでくる。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "双子が私を斬ったのだ。\n
私を慕ってくれていた、物騒でも可愛い彼らが。 "

play sound se_0638 volume .8
play sound se_0550 volume .6
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_4")
T "（どうして？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "問いかけたい。\n
斬られた私には、その権利があるはずだ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "だが、言われるまでもなくその理由を私は知っている。 "



hide t_end_confined4


show dee_s_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0568
Dee "「僕達だってお姉さんに傷なんか残したくない。\n
だから、神経だけをすぱっと斬ってあげたんだよ、痕は残らないから大丈夫」 "

hide dee_s_02_10 at center
show dee_s_02_10 at left

show bra_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0551
Blood "「そうだな。\n
そのあたり、刃物を使い慣れているおまえ達に任せたのは正解だった」 "

hide dee_s_02_10 at left
show bra_t_01_13 at left
hide bra_t_01_13 at right
show dam_s_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0569
Dam "「……いつもならボーナスを要求するところだけど、今回はいいや。\n
お姉さんを斬るなんて、いい気分がしないしね」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_3")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_3")
T "（皆、何を話しているんだろう） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_5")
T "（どうして私は地面に倒れていて、皆の会話をぼうっと聞いているの？） "

hide bra_t_01_13 at left
show eri_t_03b_11 at center
hide dam_s_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_5")
Elliot "「…………」 "

hide eri_t_03b_11 at center
show eri_t_03b_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_5")
voice eri_f0347
Elliot "「[firstname]、痛むか？\n
すぐに帰るから、それまでは悪いな……」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_3")
T "「…………」 "

hide eri_t_03b_13 at center
show eri_t_03b_13 at left

show bra_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_3")
voice blo_f0552
Blood "「どうしたんだお嬢さん、ずいぶん静かじゃないか。\n
聞きたいことがありそうな顔をしているのに……」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_12")
T "（聞きたい） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T "（でも、声が出ない） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "この人は、私のよく知っている人だ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "周囲にいる彼らも、家族と言っていい存在なのに。\n
見えない糸で縛られたように、身体が動かない。 "

play sound se_0051
camera at hpunch
camera at vpunch
hide eri_t_03b_13 at left
show bra_t_03_18 at center
hide bra_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0553
Blood "「聞きたいことがあるのなら、屋敷でゆっくりと聞いてあげよう。\n
ここは、長居をするには不向きな場所だからな」 "

hide bra_t_03_18 at center
show bra_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0554
Blood "「ああ、先刻、門番も言っていただろう。\n
心配しなくてもこれ以上、君の身体を傷つけるようなことはしない」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "ブラッドは動けずにいる私を抱き上げて、優しく囁く。 "

hide bra_t_03_4 at center
show bra_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0555
Blood "「私の元を去ろうとする悪い足は、もういらないが。\n
手がなければ、一緒に紅茶も飲めないだろう？」 "

hide bra_t_02_13 at center
show bra_t_02_18 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0556
Blood "「それでは、あまりに不憫だ。\n
これからずっと私の屋敷にいるのに……、楽しみがなくなってしまう」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T "（いらない足） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "感覚を失った、布が巻かれた私の足。\n
まるで物のような……。 "

hide bra_t_02_18 at center
show dee_s_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0570
Dee "「でも、外に出るのなら僕達が足になってあげればいいよね、兄弟。\n
お姉さんが自分の足で歩かなくても、僕達がいるよ」 "

hide dee_s_01_6 at center
show dee_s_01_2 at left

show dam_s_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0571
Dam "「うん、安心して。\n
どこにでも、連れて行ってあげるから」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "普段の表情に戻った双子が、遊びに行く約束を楽しそうに話している。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T "（どこにでも連れて行ってくれるって言うけど） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "どこかで分かっている。\n
私の足は、もう動かない。 "

hide dee_s_01_2 at left
show eri_t_01_4 at center
hide dam_s_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0348
Elliot "「……そうだな、うちにいるなら、危険なこともねえし。\n
歩けなくても、困らねえよな」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_3")
T "「…………」 "

hide eri_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T "「皆……」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_3")
T "（酷い声） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "ようやく生まれた声は、掠れてほとんど空気のようだ。\n
からからに渇いた口の中から響いても、自分の声だと認識出来ない。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_4")
T "「どうして、こんな……」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "斬り刻まれた木々、銃痕を残した大地。\n
そして、先ほどまで蹲っていた場所に出来ている、赤い水溜まり。 "


show bra_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0557
Blood "「どうして……、か。それは何に対しての、どうして、なのかな？\n
ジョーカーを追い払ったことか、それとも、君の足を斬ったことか」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_5")
T "（…………） "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_3")
T "「ブラッドが、斬らせたのね」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "ブラッドは彼らの雇い主だ。\n
双子への絶対の命令権を持っている。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "否定されるとは思っていなかった。\n
問いかける必要もない、確認にすぎない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "私の言葉にブラッドは顔色一つ変えずに、頷いた。 "

hide bra_t_01_4 at center
show bra_t_02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0558
Blood "「ああ、そうだよ、君の足が動かないように、私が彼らに斬らせた。\n
うちの門番は優秀だからね、現にこうして君を捕まえた」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_15")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "その言葉に。\n
胸の中央に銃弾が撃ち込まれた気がした。 "

hide bra_t_02_15 at center
show bra_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0559
Blood "「そんなに驚くとは思わなかったな。\n
君がジョーカーの元に行くのを、私が見逃すとでも思ったのか？」 "

hide bra_t_03_13 at center
show bra_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0560
Blood "「だとしたら、君らしくもない。\n
いくらあれに惹かれていたとしても、私が君を手放すことなどありえないよ」 "

hide bra_t_03_10 at center
show bra_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Blood "「…………」 "

hide bra_t_02_9 at center
show bra_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Blood "「[firstname]」 "

play sound se_0462

show t_end_confined5
hide bra_t_02_11 at center

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T "（鍵？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "首にかけられた鎖と、中央にかかる鍵。\n
感覚は薄れてきているはずなのに、それが酷く重いことは分かった。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0561
Blood "「君にあげよう、今となっては、無意味なものだがね。\n
……私が本当にかけたかった鍵は、なかなかかけさせてもらえそうもないからな」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_3")
T "（どこに鍵をかけたかったの？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "私にはわからない。\n
そして、この答えはきっとずっと見つけられない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "言葉にならない確信だけが、鍵と一緒に胸の中に落ちた。 "

hide t_end_confined5


show dee_s_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0572
Dee "「ボス、もう帰ろうよ。\n
ここに来るまで結構面倒だったから、疲れたよ」 "

hide dee_s_01_9 at center
show dee_s_01_9 at left

show dam_s_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0573
Dam "「うん、疲れた。\n
慣れないことはするものじゃないよね」 "

hide dee_s_01_9 at left
show eri_t_02_2 at center
hide dam_s_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0349
Elliot "「そうだな、腹も減ったし。\n
家に帰って飯にしようぜ、ブラッド」 "

hide eri_t_02_2 at center
show eri_t_02_2 at left

show bra_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0562
Blood "「やれやれ。\n
堪え性のない」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_3")
T "「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "笑い声さえ混じっている会話に、私だけが浮いている。\n
彼らのやりとりは、いつもと何も変わりない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_3")
T "（だったら、変わってしまったのは私なの？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "足を斬られたから？\n
それとも、迷ってしまったから？ "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_3")
T "（分からない） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_4")
T "（でも、答えが出ても出なくても、何も変わらない） "

hide eri_t_02_2 at left
show bra_t_02_8 at center
hide bra_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_05_4")
voice blo_f0563
Blood "「さあ、[firstname]、我が家に帰ろうじゃないか。\n
心配することはない、監獄なんて味気ない場所より余程快適な場所だ」 "

hide bra_t_02_8 at center
show bra_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_05_4")
voice blo_f0564
Blood "「足の不自由さなど感じないように、私がずっと閉じ込めて、可愛がってあげよう」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T "見えない鍵は、既に私の全身にかかっている。 "

hide bra_t_01_10 at center
with dis
$ hi_mes()

scene map_bg_joker_day with Dissolve(1.5)
pause 5
$ hi_mes()
pause 5

$ renpy.movie_cutscene("endroll_c.mpg")
# return
