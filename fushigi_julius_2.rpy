jump fushigi_common2_castle
label fushigi_julius2_2:

scene map_bg_spring_day
with stripe_l_medium

scene hm_spr_01
with stripe_l_medium

scene bg_gen_sky_spr_day with Dissolve(1.2)
play sound se_0217

play music castle_guestroom_p_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0350
Ace "「やあ、[firstname]、久しぶりだね。\n
こんなところで会うなんて奇遇だなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「…………。\n
今度はどこで迷ったのよ、エース」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0351
Ace "「ん、今回は違うぜ。\n
陛下に呼ばれてちゃんと謁見室に行ったんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0352
Ace "「まあ、呼ばれてから二十時間帯ぐらい経っていたから、俺への用はすんでいたみたいだけどね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0352_5
Ace "「ははは、俺にすぐに来いなんて、難しいことを要求しても無駄なのになあ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（普通の人なら充分間に合うように呼んだと思うんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相変わらず、方向感覚のおかしい男はやることが違う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼には一応軍事責任者という名目が付いているはずだが、エースにとってこの城での役割はその程度のものらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（この人は、旅に出ているときのほうが楽しそうだもの）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「まあいいわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「それで、どうして……{size=+20}いきなり上の階の窓からぶら下がって、私の部屋を覗いているわけ？{/size}」"


play music ace_t_ali

show t_yuri2_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice ace_f0353
Ace "「はあ、覗き？\n
君、騎士たる俺がそんな情けない真似をするように見える？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「見えはしないけど、この状況じゃその通りでしょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぶらーんと上の階のバルコニーにぶら下がったままエースは笑っている。\n
青空の中に真っ赤な騎士が浮いているようにも見えた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0354
Ace "「たまたまだよ、たまたま。\n
ちょっと窓から足を滑らせて落ちそうになったから掴まっただけ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0355
Ace "「それに、女の子のいる部屋に勝手に入るほうが問題だろう？\n
君の許可が得られるまで踏み行ったりしないよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、入っていいって言ってくれないかな？\n
言葉にはしないものの、そんな声が聞こえてきそうな雰囲気だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「…………。\n
いいわ、いつまでもそうしているわけにも行かないでしょう、どうぞ」"

play sound se_0450
pause .3
play sound se_0586
hide t_yuri2_1

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice ace_f0356
Ace "「あれ、入ってもいいんだ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鍵を開けて部屋の中に招けば、エースは驚いたように目を見張っていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「あのまま部屋の外にいられても落ち着かないもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさか足を滑らせて落ちるとは思わないが、私と同じように窓の外にぶら下がっているエースを見て、誰かが驚いたら気の毒だろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……私も、慣れたものよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に来た頃なら、もっと騒いでいたはずだが、周囲を気遣えるまでになってしまった。"


scene hg_01
with dis



show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0357
Ace "「へえ、こんな簡単に入れてくれるのなら、最初から入れてくれって言えばよかったかな。\n
ありがとう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースはそう言いながら、くるっと半回転して華麗に着地し、部屋に入ってくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「どういたしまして。\n
部屋の出口はあそこだから、今度は迷わないでよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（さすがにこの部屋の中でまで迷ったらどうしようもないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城は広い客室とは言え、ここで迷えるほどエースも器用（？）ではないはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見送るつもりで手を引こうとしたら、逆に掴まれた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……エース？」"

hide ace_t_03_3
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice ace_f0358
Ace "「うん、助けてもらって何もしないわけにはいかないよな。\n
お礼に旅に連れて行ってあげるよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何だか嫌な予感に、顔がこわばるが、何かを言う前にエースは続ける。"

hide ace_t_03_10
show ace_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0359
Ace "「君、ずっと部屋にこもりっぱなしだろ？\n
だめだぜ、若いうちはアクティブに外に出ないと……、というわけで、行こう！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「ちょ、ちょっと、エース！\n
私、旅なんて期待していない……って、聞きなさいってば！！」"

play sound se_0397
hide ace_t_02_1


play music castle_corridor_p_ali

scene hr_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "制止の声は届いているはずだが、まるっと無視された。\n
部屋から引っ張り出され、廊下を進み始める。"


show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0360
Ace "「今回の旅は、楽しそうだなあ。\n
はははは」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "爽やかな声が響く中、彼はずんずんと進んでいく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも迷う男のはずなのに、何故かこういうときにはまっすぐに城外へと進むのだから、世の中矛盾が多すぎる。"

hide ace_t_01_4
show ace_t_01_4 at left
show siro_t_02_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0035
Maid "「あら、エース様。\n
それに……」"

hide ace_t_01_4

hide siro_t_02_04


show viv_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0416
Vivaldi "「……なんじゃ、騒々しい。\n
その頭に響く笑い声をどうにかせぬか、エース」"

hide viv_t_03_7
show viv_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0417
Vivaldi "「イライラして、誰かを処刑したくなる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ビバルディ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城内を移動中なのか、メイドを連れたビバルディがこちらを見て目を見開いている。"

hide viv_t_03_9
show viv_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0418
Vivaldi "「む……？\n
なんだ、[firstname]、おまえもいたのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "通路の奧から現れた影に縋るような目で助けを求めたのは、ほとんど無意識だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女は私の手を引くエースと私にそれぞれ視線を向けると、呆れたように肩を竦める。"

hide viv_t_01_5
show viv_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0419
Vivaldi "「……なっておらぬ。\n
落第じゃな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「は？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（落第って、一体何が……？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然呟かれた言葉の意味が分からなかった。"

hide viv_t_03_7
show viv_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0420
Vivaldi "「落第と言ったら落第じゃ。\n
手を引くにしても、もう少しエスコートの方法を考えたらどうじゃ、エース」"

hide viv_t_01_8
show viv_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0421
Vivaldi "「力任せに引くだけとは。\n
女を誘うのに、ムードも何もあったものではない」"

hide viv_t_01_9
show viv_t_01_9 at left
show ace_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0361
Ace "「ははは、ムードはこれから作るんですよ。\n
最初からいい雰囲気だったら、お楽しみがなくなっちゃうじゃないですか」"

hide ace_t_02_4
show ace_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0362
Ace "「そうだよな、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「お楽しみって一体何よ、それ！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（それ以前に、私とあなたで一体どんなムードを作るって言うのよ！？）"

hide ace_t_03_12
show ace_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice ace_f0363
Ace "「この後は若い二人だけで……、ということで。\n
それでは、御前、失礼します」"

hide viv_t_01_9
show viv_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice viv_f0422
Vivaldi "「若い二人……？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴくりとビバルディの顔が引きつる。\n
しかし、行動は騎士のほうが早かった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0364
Ace "「ほら、行こうぜ、[firstname]！」"

play sound se_0492
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「わっ、ちょっと、エース！」"

play sound se_0312
hide ace_t_03_3

hide viv_t_02_6

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんなときだけ丁寧な礼を取るや否や、エースはさっさと走り出してしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後の女王様の表情を確認するよりも早く、あっという間に廊下を駆け抜けていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ビバルディにはちょっと悪いけど、今更戻れそうもないし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐいぐいと手を引かれながら、部屋に戻ることを諦める。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこまで意地になるだけの理由もない。\n
大きな手に引かれたまま、私もその背中に続いた。"


$ hi_mes()

scene hr_01
with stripe_l_medium

scene hm_spr_01
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium

play music forest4_p_ali

scene bg_gen_sky_spr_day with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（それが、どうしてこんなことになるんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースに引き摺られてハートの城を出てから、既に五回は時間帯が変わっている。\n
その間、ずっと歩き通しだというのに明るい日差しの下で彼だけは元気だ。"


scene s2_01
with dis



show ace_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0365
Ace "「うーん、おかしいなあ。\n
俺の予定ではそろそろ城に戻れるはずだったんだけどなあ」"

hide ace_t_02_8
show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0366
Ace "「まあ、予想出来ないからこそ旅は楽しいっていうしな、ははは」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（帰りたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものこととはいえ、体力の有り余っているエースと私では疲労の具合も比べものにならない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_9")
T "「少し休みましょうよ、エース。\n
さすがに疲れたわ」"

hide ace_t_02_4
show ace_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_9")
voice ace_f0367
Ace "「ん？\n
もう疲れちゃったなんて……、そんなに疲れさせること、まだ何もしていないだろう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "{size=+20}「あれだけ歩けば充分よ」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（だいたい疲れさせるようなことはまだしていないって、何よ、まだって！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "坂道、山道、獣道。\n
川に落ちかけ、沼に足を取られかけ、滝を飛び越えさせられ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（……ん？\n
でも、まだ実際に落ちてはいないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "以前彼に付き合わされたときには一緒に水浸しになったこともあったものだが、今回はそれがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たまたまだろうか、それとも何か理由があるのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（熊にも襲われていないし……。\n
比較的、いつもよりも平和なような気がする）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（…………。\n
……単に、比較する事件が飛び抜けているせいかもしれないわね）"

hide ace_t_03_2
show ace_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice ace_f0368
Ace "「もう少し行ってから休憩にしようと思っていたんだけどなあ。\n
君がそう言うなら仕方ないか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースが立ち止まってくれたのを見て、私は近場にある石に腰を下ろす。\n
アウトドアも随分こなしたとはいえ、相手と比べれば体力不足は否めない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（この世界の人達は常人離れしすぎなのよ）"

hide ace_t_01_6
show ace_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice ace_f0369
Ace "「あれ……、[firstname]。\n
それをちょっと見せてくれよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"


show t_cut_yuri2_1u onlayer master
with dis
hide ace_t_01_11

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が指差したのは、私が椅子代わりに使っている石だ。\n
転がっている石の中でも丸みを帯びていて、滑らかなもの。"


scene t_cut_yuri2_1 with dis

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（何か特殊な石なのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "石から腰を上げた私と入れ替わるように、彼はその表面を撫でている。\n
あちこち色々な角度から眺めて、大きく頷いた。"


show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0370
Ace "「へえ……、君、すごいもの見つけたね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「？\n
この石、珍しい価値でもあるの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私から見れば多少土が付いているだけの石にしか見えないのだが、エースには何か思い当たるものがあったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首を傾げている私に構わず彼は剣の柄に手をかけた。"

play sound se_0674
pause .5
play sound se_0443
hide ace_t_03_11
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0371
Ace "「よいしょ……、と」"

play sound se_0441
pause .3
play sound se_0411

show white onlayer master with spread_extrashort
show t_cut_yuri2_2u onlayer master with spread
hide white
hide ace_t_01_10

pause .5
scene t_cut_yuri2_2 with dis
hide t_cut_yuri2_2u

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！」"

show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice ace_f0372
Ace "「うん、やっぱりなあ。\n
どこかで見たことがある石だと思ったんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "カキィンという甲高い音と共に、石を切りつけたエースは告げる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が剣で割った断面は鮮やかなものだ。\n
灰色の表面に覆われた石の中は、様々な色に輝いていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（宝石の原石か何かかしら。\n
こうして見ていると宝石箱みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きらきら。\n
研磨も何もされていない状態だというのに、原石は見ているだけでも楽しめる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「これ……、宝石か何かなの？」"

hide ace_t_01_4
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice ace_f0373
Ace "「俺も種類までは知らないけど、多分そうじゃないかな。\n
これだけきらきらしているしね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「すごく綺麗……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（削られていないからこそ、自然の色合いが楽しめるのかもしれないわ）"

hide ace_t_03_10
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_14")
voice ace_f0374
Ace "「君が見つけたんだから、持って帰ればいいんじゃないかな。\n
値打ちものだと思うぜ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「こんな大きな石を？\n
持って帰れるわけがないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人ひとりとまではいわないが、かなりの大きさだ。\n
当然重量もある。"

hide ace_t_03_3
show ace_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0375
Ace "「そうか、ならもう少し小さくしていけばいいかな。\n
これぐらいに……」"

play sound se_0441
pause .3
play sound se_0411

show white onlayer master with spread_extrashort
hide white with spread
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースはそう言って、目の前にあった石をいとも簡単に切っていく。"

hide ace_t_02_11


scene t_cut_yuri2_3u
with dis
pause .15

scene t_cut_yuri2_3
with dis

show ace_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0376
Ace "「はい、どうぞ。\n
これなら、君も持って行けるんじゃないかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気軽にエースは渡してくれるが、対応に困ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（原石だけ渡されても、加工する技術もないし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それ以前に宝石が必要な立場かと言えば、そんなことはない。\n
むしろ、持て余すだけだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それはあの塔においても、ハートの城でも、変わらない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「いいわ、原石を貰ってもらっても使い道がないし」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（ユリウスなら、ひょっとしたら何か作れるかもしれないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手先が器用な彼ならば、応用して色々なものに加工できるかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……ユリウスにあげたところで、喜んではくれないだろうし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "綺麗だとは思うが、作業部屋を駄目にしてしまったお詫びにはなりそうにない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何か作ってもらうのも悪くないのだろうが、生憎とそういうものを贈られたいとは思わない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな飾り立てるためのものよりも、もっと確実に……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "傍にいられる証のほうが、ずっといい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（……何か、そういう証になるもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふと考え、自分が壊してしまったものを思い出す。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_6")
T "（そうだ、あれなら、ユリウスもきっと……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "喜んでくれそうなものに思いあたったところで、エースが返事をした。"

hide ace_t_02_10
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0377
Ace "「そう？\n
じゃあ、俺が代わりにもらっていこうかな……、いい？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「え？\n
ええ、元々エースが言わなければ気が付かなかったし、いいと思うわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "このまま炉端に転がっているよりは、石も本望だろう。"

hide ace_t_03_10
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0378
Ace "「うん、分かった。\n
じゃ、これは俺がもらっていこう」"


scene s2_01
with dis
hide ace_t_03_3
show ace_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0379
Ace "「なあ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「何？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "石から視線を外して、エースは笑った。"

hide ace_t_02_12
show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0380
Ace "「例えばだけど、この石で君に似合うものを作ったらもらってくれる？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「似合うものって……、どういうこと？」"

hide ace_t_02_4
show ace_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0381
Ace "「そうだなあ……、指輪とかさ。\n
この指に似合うような」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が指差しているのは、左手の薬指。\n
そこに填める意味を知らないわけではないだろうに、何を言うのだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「質が悪い冗談ね」"

hide ace_t_03_12
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice ace_f0382
Ace "「冗談じゃなかったら？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「もっと悪いわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "（あなただって、本気じゃないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの元に出入りをしているエースだ。\n
私が誰の元にいるかよく知っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その上でこんなことを言うなんて、酷い冗談だ。"

hide ace_t_03_3
show ace_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0383
Ace "「本気に取ってくれてもいいんだけどな、俺としては」"

hide ace_t_01_1
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0384
Ace "「なあ、[firstname]。\n
俺、君のことが好きだぜ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "感情のこもらない、無味の好意。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "偽りはない。\n
しかし、真実すべてが収められているわけではない言葉に踊れるはずがない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「ありがとう。\n
私も好きよ、エース」"

hide ace_t_03_10
show ace_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「ただし、友達としてだけど」"

play sound se_0551

play music secret_a_ali
show t_yuri2_2 onlayer master
with dis
hide ace_t_02_13

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「エース！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice ace_f0385
Ace "「雰囲気を作ってみたんだけど、これでも足りない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顎に手をかけられて、まるで唇を重ねるような姿勢を取らされる。\n
視界に映るのは……、しかし、悪戯を企むように笑う騎士の顔。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "真摯なものではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、面白がっているという雰囲気でもない。\n
あえて言うのであれば……、何かを待っている顔だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「？？？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（何を考えているのよ、エース？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず声を上げそうになった私の唇を、顎に触れていた指が押さえ込む。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0386
Ace "「静かにしてなよ……。\n
まだ隠れていたいみたいだからさ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（隠れている？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（一体誰が？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城から離れた、ひとけのない山の中で隠れるような人物とは誰か。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（また、ペーターか誰かが送ってきた刺客とか？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "咄嗟に思い浮かんだのはそれぐらいで。\n
それだけに、視界の隅で動くものを見つけたときには驚いて声が出そうになった。"


play music looking_for_a_ali
hide t_yuri2_2
show t_yuri2_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「エ、エース……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice ace_f0387
Ace "「見えた？\n
本当に、分かりやすいよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私に口説き文句を囁いていたときよりも、ずっとずっと楽しそうな声だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「だ、だって……。\n
あれって……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "木々の陰からちらちら見え隠れしているのは、長いコート。\n
頭に被った帽子と、一瞬だけ見えたサングラス。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首に巻いたマフラーは、冬でもない今には暑すぎるだろうに、きっちりと巻かれている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（いかにも不審者っていう姿だけど、あれは……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不審者にしか見えないが、間違いない。\n
他の人間ならともかく、彼を見間違えることなど、あるはずがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（何でそんな格好でここまで出てきたのよ、ユリウス！？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_9")
voice ace_f0388
Ace "「いい意味でも悪い意味でも、古典的というか。\n
うん、さすがユリウスって感じだよなあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言いながらも、エースは密着させた身体を離そうとしない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「分かっているなら、離れてよっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（ユリウスが誤解するとは思わないけど、余計な騒動は起こさないで！）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice ace_f0389
Ace "「何で？\n
見せ付けてやればいいじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice ace_f0390
Ace "「君と俺は……、こんなに、仲よしだってさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_9")
T "「……エース」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（何を考えているのよ、あなた）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何であれ、ろくなことでないのは確かだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは私達の会話が聞こえていないせいだろう、そわそわと木の合間から様子を伺っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、それも仕方ないのかもしれない。\n
端から見れば、ぴったりと身体を寄せ合っているのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただならぬ仲だと思われたとしても、否定するのは難しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（そうよ、こんな距離、恋人だっていつもするような距離じゃ……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（待て）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恋人しか見えなくなっているような、砂糖で頭がいっぱいのカップルしかやりそうもないということは。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（ユリウスから見ても、私とエースがそういうふうに見えている？）"

hide t_yuri2_3
show t_yuri2_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「は、離れてよ、エース！」"

play sound se_0007
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今更ながらにその意味に気付いた私が手足をばたつかせたが、エースは難なく私の身体を押さえ込んでしまう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0391
Ace "「おっと……。\n
暴れないでくれよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0392
Ace "「そんなに抵抗されると、かえって……、辛いことになるぜ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0393
Ace "「意地悪、されたい？\n
君が望むなら、それも悪くないけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「つ、辛いって……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（何をするつもりよ、あんた！？）"

play sound se_0373
camera at hpunch
camera at vpunch
hide t_yuri2_4
show t_yuri2_5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「きゃっ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま地面に押し倒されてしまう。\n
視点が変わったせいで、森の奧に隠れるユリウスの姿が遠退いた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0394
Ace "「ははは、どうしようか、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "{size=+20}「どうもしないわよ！！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何をどうしようというのか、この男は。\n
きっと睨み付けたが、騎士の微笑みは相変わらずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただ、酷く楽しそうという点だけが、気になった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「[firstname]……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "囁きと共に、エースの顔が近付いてくる。\n
抵抗しようにも、のしかかられてしまっているし、力で勝てる相手ではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（やだ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（嫌よ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースのことは嫌いではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一時ユリウスが離れていたときには、彼の不在を一緒に感じた点では親しみも覚えている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし……。\n
これは、違う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんな触れ合いなど、されたくはないし、されてはいけない。"

hide t_yuri2_5
show bg_gen_sky_spr_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「エース！」"

play sound se_0441
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が叫んだ瞬間、ぶんという音を立てて、何かが空を裂いた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

play sound se_0041
hide bg_gen_sky_spr_day


show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice ace_f0395
Ace "「ははは、危ないなあ。\n
頭に当たっていたら、血が出るだけじゃすまないぜ」"


play music tower_room1_p_ali
hide ace_t_02_4
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice ace_f0396
Ace "「親友に対して、それはあんまりじゃないのか、ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飛んできたスパナをさらりとかわして、エースは親友のほうを振り返った。"

hide ace_t_03_11
show ace_t_03_11 at left
show yuri_d_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0194
Julius "「馬鹿なことを言っていないで、そいつから離れろ、エース！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「ユリウス……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "木々の間から出てきたユリウスと視線が合うと、彼はとても苦々しい顔を向けた。\n
一瞬怒っているのかと思ったが、どうも違う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（怒っているというより……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……落ち込んでいる？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "伊達に彼と一緒にはいない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さな感情の変化も、視線一つで何となく察してしまう程度には、彼を知っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "理由は分からないが、彼の反応を見る限り、私の直感は間違いではないように思う。"

hide ace_t_03_11
show ace_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0397
Ace "「男の一人旅なんてつまらないだろう？」"

hide ace_t_03_2
show ace_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0398
Ace "「それに、俺の旅に彼女が一緒にいるのは、よくあることじゃないか。\n
今更、何を言うんだよ、ユリウス」"

hide yuri_d_03_7
show yuri_d_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

hide yuri_d_03_13
show yuri_d_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0195
Julius "「おまえもおまえだ。\n
何でエースと、こんなひとけのない場所に来たんだ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「何故って……。\n
エースが迷った……、からかな？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（はっきりとしたどこか目的地があったわけじゃないし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうしてと問うのは、エースがどうして迷子になるのかを問うのと同じぐらい、返答が難しい問いかけだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「そんなことを言ったら、ユリウスだってどうしてこんな場所にいるの？\n
いつも仕事部屋に閉じこもっているあなたがこんな場所まで出てくるなんて……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は余程の事情がない限り、あの部屋から出て来ない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドア一枚で繋がっているクローバーの塔内でさえ、必要最低限しか出歩かないのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼がこんな森の奧にいるほうがおかしい。"

hide yuri_d_03_7
show yuri_d_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0196
Julius "「……散歩だ。\n
わ、私だってたまには外を歩くことぐらいないわけじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "{size=+20}「裾の長いコート、マフラー、サングラスに、帽子まで被ってやる散歩？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（無理があるわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんな格好など、冬の季節であってもする人間はいない。\n
誰が見ても不審者だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（ここに来るまであの格好だったとしたら、何ごともなく来られたのかも疑問だわ）"

hide yuri_d_03_3
show yuri_d_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice jul_f0197
Julius "「たまたまそういう気分だったんだ！\n
細かいことを気にするんじゃない！」"

hide yuri_d_03_7
show yuri_d_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice jul_f0198
Julius "「これは、ちょっと風邪気味で……。\n
そうだ、身体を冷やさないためにだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（嘘っぽい。\n
病弱なナイトメアならまだしも、ユリウスよ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の言葉にもっとも矛盾を感じているのは彼自身だろう。\n
言いながら苦虫を噛み潰したような顔をしている。"

hide ace_t_03_3
show ace_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0399
Ace "「ふうん、そうか。\n
まあ、ユリウスにもたまには気分転換が必要だよなあ」"

hide ace_t_02_11
show ace_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0400
Ace "「だけど、それは彼女だって同じことが言えるんじゃないかな？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……エース？」"

hide ace_t_02_6
show ace_t_01_10 at center
hide yuri_d_03_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice ace_f0401
Ace "「[firstname]、君はユリウスとも仲がいいけどさ。\n
倦怠期を迎えた夫婦のような関係には、刺激も必要だろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「！！？」"

play sound se_0210
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「エ、エース！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "座り込んでいたところを、手を引っ張られて抱き寄せられる。\n
私からは、ユリウスが見えなくなってしまった。"

hide ace_t_01_10
show ace_t_01_10 at left
show yuri_d_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0199
Julius "「エース、おまえ、いい加減に」"

hide ace_t_01_10
show ace_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0402
Ace "「ユリウス、知らなかったのか？\n
俺、この子のこと、大好きなんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "騎士の声は大きく、そしてよく通る。\n
私にも、そして立ち尽くしているユリウスにも、しっかりと聞こえた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「は？」"


play music gag2_a_ali
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（大好き？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（エースが、私を、大好き？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬にしてフリーズした思考は、同じように一瞬で解凍された。\n
あまりの馬鹿げた発言だと、思考が止まるのも短いらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……絶対に、ない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースがユリウスを大好きというほうがまだ納得できる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本人はどう感じているかは分からないが、エースという人間にとってユリウスの存在は大きい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その理由までは聞いたことがないが、彼らの関係を見ていればそれはすぐに分かることだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「あなた、何を言っているの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（何を考えているの、ってほうが正しいかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースに嫌われているとは思っていない。\n
だが、彼の言う好きという言葉は、真実でも恋愛感情でもない。"

hide yuri_d_03_13
show yuri_d_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0200
Julius "「……おまえ、とうとう何か悪いものでも食ったのか？」"

hide yuri_d_03_3
show yuri_d_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0200_5
Julius "「迷った先で、どんなに腹が減っても拾い食いだけはするなと言っておいただろうが」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒っていたはずのユリウスも、戸惑っている。"

hide ace_t_03_3
show ace_t_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0403
Ace "「ははは、傷つくなあ。\n
別に俺はおかしくなったわけでも何でもないぜ」"

hide ace_t_01_4
show ace_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0404
Ace "「それに、おかしいのは、ユリウスのほうだろう？\n
すごい格好だもんなあ」"

hide ace_t_01_3
show ace_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0405
Ace "「そんなマフラーまで巻いて、暑くないのか？\n
サングラスに、帽子に……、うわあ手袋まで完備か」"

hide ace_t_03_2
show ace_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0406
Ace "「はははは、どこからどう見ても尾行していますって感じで、変質者っぽくって面白いと思うけど」"

hide yuri_d_03_4
show yuri_d_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0201
Julius "「うるさいっ！\n
私だって好きでこんな格好をしたわけでは……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「でも、ユリウスらしいと言えばユリウスらしいわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐいっ、とエースを押して、ユリウスに向き直る。\n
改めてみると、隠れる気ゼロな服装だ。"

hide yuri_d_03_7
show yuri_d_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0202
Julius "「何？\n
どういう意味だ、それは？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「どういうって……、言葉どおりよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（なかなかここまで徹底して変装が出来るような人っていないもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よくも悪くも、職人気質の彼らしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「そこまで徹底した格好が出来る人って、滅多にいないわ」"

hide yuri_d_03_9
show yuri_d_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
Julius "「…………」"

hide ace_t_01_1
show ace_t_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも、部屋から出ないユリウスが着てきたのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここで機嫌を損ねてしまったら、彼の性格から考えてますます引きこもりになってしまう可能性もある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（それだけは避けたいし。\n
どんな変な格好でも出てきたことは評価しないと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな奇妙な使命感に駆られて、私は更に続けた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「暑苦しいぎりぎりラインだけど、でもユリウスは仕事柄恨みを買うことも多いし……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「それを思えば、{size=+20}変質者寸前の変装のほうが安全よ{/size}」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「そうよ。\n
この姿なら、あなたが時計屋だって分からないもの！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここまで徹底された変装を見抜けるとしたら、私やエースのように彼に近しい人物ぐらいだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "単に『時計屋』という名前だけで襲うには、正体不明の姿である。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……ちょっと苦しいフォローかしら。\n
でも、外に出たことを評価するべきよね）"

hide yuri_d_03_11
show yuri_d_03_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
Julius "「…………」"

hide ace_t_03_1
show ace_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice ace_f0407
Ace "「ははは、心配されているみたいだぜ、ユリウス。\n
愛されていて、嬉しい？」"

hide yuri_d_03_8
show yuri_d_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice jul_f0203
Julius "{size=+20}「黙れ」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一生懸命褒めた私の努力とは裏腹に、ユリウスは口を尖らせている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（あれ、失敗しちゃった？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仏頂面でエースを睨むユリウスは、呆れたように溜息をついていた。"

hide ace_t_02_4

hide yuri_d_03_13

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music forest1_p_ali

show ace_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0408
Ace "「ああ、そういえば、俺、ユリウスにも呼ばれていたんだよな。\n
ははは、ごめんごめん、行くのが遅くなったな」"

hide ace_t_02_3
show ace_t_02_3 at left
show yuri_d_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Julius "「…………」"

hide yuri_d_03_13
show yuri_d_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jul_f0204
Julius "「おまえの遅刻など、いつものことだからな。\n
今更だ」"

hide ace_t_02_3
show ace_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0409
Ace "「うん、そうするとここで出会えたのはラッキーだったよなあ。\n
俺、今回はついているかも……」"

hide ace_t_03_9
show ace_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0410
Ace "「君も、そう思うだろう、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「え、ええ。\n
そうね、そうかもしれないわね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（普段が尋常じゃない迷いっぷりだものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔で待ち合わせをしていたのなら、出会う場所が違うとは思うのだが、言っても仕方のないことは黙っておく。"

hide yuri_d_03_12
show yuri_d_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0205
Julius "「ふん……、ついている？\n
こんな場所まで来たのに、私に邪魔されたんじゃないのか？」"

hide yuri_d_03_1
show yuri_d_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0206
Julius "「何をするつもりだったかまでは知らんがな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（何だか、ますます落ち込んでいるような……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が落ち込むようなことが何かあっただろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（エースが仕事に遅れるのなんて、いつものことだし。\n
今更、落ち込むようなことなんか……）"

hide ace_t_03_3
show ace_t_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice ace_f0411
Ace "「それで、仕事の話はどうする？」"

hide yuri_d_03_13
show yuri_d_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice jul_f0207
Julius "「資料は私の部屋に……。\n
ああ、今はないんだったな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（あ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その言葉の意味を察して、息を飲む。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の部屋。\n
唯一クローバーの塔から繋がっている、時計塔の一室。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（あれだけ焦げれば、資料だって無事じゃないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "修理に持ち込まれた時計を外へ出すことを最優先にしていたこともあり、その他は二の次だったのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "愛用の仕事道具の一部さえ無事ではすまなかったのだから、仕事の資料がどうなったかなど考えるまでもない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「……ごめんなさい」"

hide yuri_d_03_2
show yuri_d_03_11 at center
hide ace_t_01_11
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice jul_f0208
Julius "「その件については、もういいと言っただろう。\n
何度も謝るな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「だって……」"

menu:
    "邪魔をしちゃったでしょう？":
        jump fushigi_julius2_3a
    "足を引っ張っている。":
        jump fushigi_julius2_3b

label fushigi_julius2_3a:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "原因は不注意による事故で、悪意はなかったとはいえ、部屋を焦がしたという事実は消えない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（火傷だってさせて）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "機械油と、金属で荒れた手。\n
傷一つない、滑らかなものとは違って、彼の手はその仕事によって磨かれた手だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「火傷は、もういいの？」"

hide yuri_d_03_11
show yuri_d_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jul_f0209
Julius "「ああ。\n
もう何ともない」"

play sound se_0067
show t_cut_yuri2_4u onlayer master
with dis
hide yuri_d_03_9

pause .15
hide t_cut_yuri2_4u
show t_cut_yuri2_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って、証拠のように、彼は手袋を外して見せてくれる。\n
大きな手の平には、もう何も痕は残っていなかった。"

hide t_cut_yuri2_4


show yuri_d_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0210
Julius "「言っただろう、あの程度の火傷でどうにかなるほど柔じゃない。\n
小さなことを気にしすぎなんだ、おまえは」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（……小さなこと？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かにたかが火傷と言ってしまえばそれまでのものだろう。\n
だが、確かに怪我の原因を作ったのは間違いないのだ。"

jump fushigi_julius2_4
label fushigi_julius2_3b:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（手伝うどころか、逆効果）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の誰にも触れさせようとしない時計の修理だが、簡単なものならば、ユリウスは私に任せてくれるようになったのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "信頼を裏切ったという意識が、胸の中に重く積もる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「足を引っ張っちゃったわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自惚れていたわけではないが、少しでも彼の役に立ちたかった。"

hide yuri_d_03_13
show yuri_d_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0211
Julius "「……足を引っ張ったとは誰も言っていないだろう」"

hide yuri_d_03_4
show yuri_d_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0212
Julius "「責められるのは、おまえだけじゃない。\n
そもそもあの芋虫が逃亡を企てて、勝手に私の部屋まで来るから、あんなことになったんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今でも、彼の中に私を責める気持ちはないらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（でも、怒られたほうがいいときもあるのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "優しく見守られている。\n
その感覚は確かに伝わってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だからこそ、許されてばかりで何も返せないことが苦しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（私にはユリウスの好意に返せるものがない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼のために、私だけが出来ることなんて、何もない。\n
ずっと傍にいることも、出来なかった私には。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（あれ、いつ、ユリウスと離れたのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの国の引っ越しで彼と離れたことは覚えているが、では、いつ、彼が戻ってきたのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それがどこか煙に包まれているかのように、思い出せない。"

hide yuri_d_03_13
show yuri_d_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0213
Julius "「おい、聞いているのか、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（こんなときにまでぼうっとするなんて）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_4")
T "（情けない）"

jump fushigi_julius2_4
label fushigi_julius2_4:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_3")
T "「ごめんなさい」"

hide yuri_d_03_12
show yuri_d_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_3")
voice jul_f0214
Julius "「っ！」"

hide yuri_d_03_11
show yuri_d_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_3")
voice jul_f0215
Julius "「な、何で泣くんだ！？\n
私は、気にしすぎだと言っただけで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相手が慌てているのが分かるが、衝動的に崩れた表情は戻らない。"

hide yuri_d_03_3
show yuri_d_03_3 at left
show ace_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0412
Ace "「ははは、ユリウス酷いなあ。\n
[firstname]、泣きかけているぜ？」"

hide yuri_d_03_3
show yuri_d_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0216
Julius "「エース！！」"

hide ace_t_03_12
show ace_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0413
Ace "「俺に怒ったって仕方ないだろ？\n
だって、この子を泣かせているのは俺じゃないんだからさ」"

hide ace_t_03_2
show ace_t_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0414
Ace "「というわけで……。\n
女の子をいじめるなんて、親友としては許せないなあ、ユリウス」"

play sound se_0674
pause .5
play sound se_0443

play music kaigou2_a_ali

show t_yuri2_6 onlayer master
with dis
hide ace_t_01_10

hide yuri_d_03_7

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（な、何で、剣を抜いてユリウスに向けているの？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jul_f0217
Julius "「エース……。\n
どういうつもりだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice ace_f0415
Ace "「ははは、だって俺は騎士だよ。\n
ここはハートの城の領土だし、か弱い女の子は守ってあげなくちゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぎらりと。\n
輝く剣の刃はぴったりとユリウスへと向けられて、揺らがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（何を考えているのよ、あなたは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ちかけていた涙が、あまりの衝撃に引っ込んだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースにとってユリウスは唯一の親友であると同時に、もう一人の主でもある。\n
そんな彼に剣を向ける理由など、思いつかない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

hide t_yuri2_6


show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0416
Ace "「今は、お互い引こうぜ。\n
大丈夫、ちゃんと俺が城まで送るからさ」"

hide ace_t_03_10
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0417
Ace "「ここじゃムードも何もないし、今更って感じだろう？\n
な、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

hide ace_t_03_11
show ace_t_03_11 at left
show yuri_d_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jul_f0218
Julius "「そうか。\n
それなら構わない、好きにしろ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元々低い声が、今は更に低くなっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（怒っているんじゃなくて、これは落ち込んでいる……？\n
普通、この状況だったら怒るんじゃないの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が好きな人はエースではなく、ユリウスなのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（何でそんなにあっさりと……、引けるの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問いかけてみたい。\n
だが、何が言えるだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_3")
T "（私が勝手に、塔を出てきたんだもの）"

hide yuri_d_03_13
show yuri_d_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_3")
voice jul_f0219
Julius "「仕事の話は次だ。\n
いいか、今度こそ遅れるんじゃないぞ、エース」"

hide ace_t_03_11
show ace_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_3")
voice ace_f0418
Ace "「うんうん、分かっているぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

play sound se_0625
hide ace_t_03_3
show ace_t_03_3 at center
hide yuri_d_03_12
with dis

play music heartrending_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースへの言葉を最後に。\n
ユリウスは振り返ることなく、背を向けて立ち去っていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その背中が見えなくなってから、ようやくエースは口を開いた。"

hide ace_t_03_3
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0419
Ace "「じゃ、俺達も帰ろうか、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「何であんなことを言ったのよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達の間にあるものと、ユリウスと私の間にあるものはまったく違う。\n
それはエースにだって分かっているはずだ。"

hide ace_t_01_10
show ace_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0420
Ace "「ははは、君達って本当に仲がいいんだなあ。\n
同じことを聞いてばっかりだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（あなたがおかしなことを言うからでしょう）"

hide ace_t_01_1
show ace_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice ace_f0421
Ace "「簡単に言えば……。\n
俺は、君のこともユリウスのことも好きだから……、かな」"

hide ace_t_03_9
show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice ace_f0422
Ace "「俺、騎士だけど博愛主義って苦手だからさ。\n
好きな人の味方だけをしているほうが楽しくていいよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そういって笑った彼の言葉の意味は、私には結局分からずじまいだった。"

hide ace_t_02_4

$ hi_mes()

scene s2_01
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_long
##endmemory
jump fushigi_common3_castle ## I think
