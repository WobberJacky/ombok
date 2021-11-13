label fushigi_common2_castle:
$ hi_mes()

scene map_bg_spring_day
with dis
$ clockanim()


scene charasel_bg_castle_day
with dis

play music castle_mae_p_ali

scene hm_spr_01 with Dissolve(1.2)
play sound se_0624
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目に痛いほどの強い、赤。\n
最初にこの城を訪れたときには、あまりの配色に頭痛さえ覚えたものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……でも、慣れたわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薔薇も、壁も、人さえも。\n
鮮やかな赤で彩られた、ハートの城。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "既に幾度も訪れているから、赤い城でなくなってしまったら違和感を覚えそうだ。"


show heisi_t_02_08 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0021
Soldier "「ようこそ、ハートの城へ」"

hide heisi_t_02_08
show heisi_t_02_08 at left

show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0021
Maid "「いらっしゃいませ。\n
皆様、お揃いですよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「皆様って……、今、何かやっているの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城の兵士とメイドが、私を見つけて話しかけてくる。\n
こちらも慣れたものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今回は約束もせずに来てしまったから全員には会えないと思っていたが、この様子では城の主要人物は揃っているらしい。"

hide heisi_t_02_08
show heisi_t_02_01 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0022
Soldier "「今は……、ちょうど裁判中でして」"

hide siro_t_02_01
show siro_t_02_07 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0022
Maid "「何やら、処刑の方法で揉めているようです」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（最悪のタイミングだったのかもしれないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "早くもここに来たことを後悔しはじめたが、今更帰るわけにも行かない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何よりも会いに来ておきながら、顔も見せずに帰ったら機嫌を損ねる人ばかりがここには揃っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（私を引き止められなかったというだけで、この人達が殺されるのも嫌だしね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自意識過剰にも思えるが、実際にあったことだから気を付けている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「分かったわ、じゃあ行ってくる」"

hide heisi_t_02_01

hide siro_t_02_07

$ hi_mes()

scene hr_01
with stripe_l_medium

play music castle_audience_p_ali

scene he_01
with stripe_l_long

show viv_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0238
Vivaldi "「斬首に決まっておる、首を刎ねてしまうのが一番よい。\n
多少血が出たところで、どうせすぐ消えるのだから、構わぬ」"

hide viv_t_01_13
show viv_t_01_13 at left
show per_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0247
Peter "「ですから、そういつも斬首ばかりではマンネリでしょう。\n
処刑方法が斬首ばかりでは、裁判の意味がありません」"

hide per_t_01_4
show per_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0248
Peter "「……何とかの一つ覚えじゃないんですから」"

hide viv_t_01_13
show viv_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0239
Vivaldi "「何か申したか、ホワイト？」"

hide per_t_02_4
show per_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0249
Peter "「いいえ、何でもありません」"


show ace_t_03_3 at center
hide viv_t_03_9

hide per_t_02_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0290
Ace "「だったら、裁判なんかしなければいいじゃないか。\n
皆無罪放免、これで万事解決だ」"


show viv_t_02_7 at right
hide ace_t_03_3
show ace_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0240
Vivaldi "「そうはいかぬ。\n
ああ……、そうだ、おまえがいたな、エース」"

hide viv_t_02_7
show viv_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0241
Vivaldi "「ちょうどいい。\n
たまにはおまえが処刑をせい、それぐらいならおまえにも出来るじゃろう」"

hide ace_t_03_3
show ace_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0291
Ace "「ははは、陛下、冗談きついなあ。\n
俺は騎士ですよ、罪人の始末は俺の仕事じゃありません」"

hide ace_t_02_4
show ace_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0292
Ace "「ここでは……、ね」"

hide ace_t_03_11
show ace_t_03_11 at left_center
hide viv_t_03_2
show viv_t_03_2 at center
show per_t_03_2 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0250
Peter "「じゃあ、代わりにエース君が処刑されるっていうのはどうですか？」"

hide ace_t_03_11
show ace_t_01_4 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0293
Ace "「ペーターさんも、面白いことを考えるよね！\n
陛下といい、冗談が好きだなあ、あはははは」"

hide ace_t_01_4

hide per_t_03_2

hide viv_t_03_2


scene hr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（殺伐としているわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "裁判が行われているというホールに辿り着いたものの、中から聞こえる物騒な単語に顔が引きつってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本人達はいたって普通に話しているが、内容がおかしい。\n
しかし、いつまでも壁に隠れていても仕方がない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（……よし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "意を決して、開いたままの扉の中へと顔を出した。"

play sound se_0277
pause .4
play sound se_0276

scene he_01
with dis

play music peter_t_ali

show per_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0251
Peter "「どうせ処刑するにしても見せしめの意味を考えて、効果的に……」"

hide per_t_03_7
show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「！！！」"

hide per_t_02_3
show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0252
Peter "「[firstname]！\n
ああ、僕の愛しい人……、僕への愛の告白でしたら、呼んでくださればいつでも飛んでいくのにっ」"

play sound se_0527
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を見つけたペーターは、手にしていた裁判資料を投げ出して、上機嫌に手を振っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さっきまでの無表情さが嘘のような変わり様だが、いつものことだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……相変わらずね、ペーター」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（どこまでも電波なウサギだわ）"


show viv_t_01_3 at center
hide per_t_02_13
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice viv_f0242
Vivaldi "「おお、[firstname]。\n
よく来たな、わらわに会いたかったのであろう？」"

hide viv_t_01_3
show viv_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice viv_f0243
Vivaldi "「うむ、やはりこのような面倒な仕事は他のものにやらせることにしよう。\n
というわけで、働け、男ども」"


show per_t_01_3 at right
hide viv_t_03_9
show viv_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice pet_f0253
Peter "「あっ、陛下、抜け駆けとはずるいですよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを言いながらビバルディは、ペーターに先んじて階段を下りようとしている。"


show ace_t_03_9 at center
hide per_t_01_3

hide viv_t_03_9
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0294
Ace "「二人とも、早とちりしすぎだよ。\n
[firstname]、まだ誰に会いに来たのかって言っていないのにさ」"

hide ace_t_03_9
show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0295
Ace "「君は俺に会いに来てくれたんだよな、[firstname]？」"

play sound se_0117
hide ace_t_01_4

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「…………」"

play sound se_0609 volume .7
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「エース」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は言葉と同時に、階段を使わずに、ホールに備えつけられた席から飛び降りてきた。\n
目の前に現れたエースに、苦笑が零れる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普通なら受け身を取ることもままならない高さだが、彼は平然としていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の役持ちの身体能力の高さにも慣れているので驚きはしないが、ショートカットしすぎだ。"


show viv_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0244
Vivaldi "「エース……。\n
ホワイトの言う効果的な処刑方法の実験台になりたいというのなら、止めはせぬが？」"

hide viv_t_03_7
show viv_t_03_7 at left
show per_t_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0254
Peter "「まったく、君の図々しさには呆れますよ。\n
それで、[firstname]、僕に何のご用でしょうか！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "わらわらとホールの一階に下りてきた三人は、好き勝手に言いたいことだけを言ってくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（まあ、少なくとも話を聞いてくれようとするだけ、いいほうかも）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の住人は軒並み人の話を聞かない人間が揃っているのだから、是とすべきだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「実は、お願いがあるのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう切り出した私は、続きを求める眼差しを受けながら、ここまでの経過を話し始めたのだった。"

hide viv_t_03_7

hide per_t_03_1

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play music honobono2_a_ali

show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0255
Peter "「そうだったんですね、それで僕のところに身を寄せたいと。\n
よくここを選んでくださいました、僕が絶対にあなたを幸せにします！！」"

hide per_t_02_5
show per_t_02_5 at left
show viv_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0245
Vivaldi "「ほんに……、騒がしいウサギじゃな。\n
ホワイトの戯言はさておき、ここに滞在したいというのならわらわも歓迎するぞ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「ありがとう。\n
お手伝いでも何でもするから、扱き使ってね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "かいつまんで事情を説明し、城にしばらくの間滞在したいと告げると、三人は快く私を受け入れてくれた。"


show ace_t_03_2 at center
hide per_t_02_5

hide viv_t_01_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0296
Ace "「君は働き者だなあ。\n
ここに来てまで仕事なんかしなくてもいいはずなのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースはそう言うが、何もせずただお世話になるのも申し訳ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（いくら一時的な居候でも、礼儀は守りたいもの）"


show viv_t_03_6 at center
hide ace_t_03_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice viv_f0246
Vivaldi "「そうと決まれば、部屋を決めねばな。\n
そうじゃ、わらわの部屋に来ればよい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え……。\n
それはさすがにまずいんじゃ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（私、これでも一応、他領土の人間なんだけど）"

if routechara == "Blood":
    jump fushigi_common2_castle2_hatter
if routechara == "Deedam":
    jump fushigi_common2_castle2_hatter
if routechara == "Julius":
    jump fushigi_common2_castle2_julius
label fushigi_common2_castle2_hatter:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が滞在する帽子屋屋敷とハートの城は、領土を巡って戦っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこを飛び出したとはいえ、敵対する領主の部屋に泊まるのは、さすがにまずいだろう。"

if routechara == "Blood":
    jump fushigi_common2_castle3
if routechara == "Deedam":
    jump fushigi_common2_castle3
label fushigi_common2_castle2_julius:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔は中立の立場を取っている。\n
だからこそ特定の領土の領主と同じ部屋というのはまずい気がした。"
if routechara == "Julius":
    jump fushigi_common2_castle3
label fushigi_common2_castle3:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、それを伝えるより早く過剰に反応した人物がいた。"

hide viv_t_03_6
show viv_t_03_6 at left
show per_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0256
Peter "「何を言うんですか、陛下。\n
彼女が住むなら、雑菌がいなくて、住み心地のいい僕の部屋に決まっているでしょう！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（そ、そういうのも求めていないんだけど）"

hide viv_t_03_6
show viv_t_03_6 at left_center
hide per_t_01_4
show per_t_01_4 at center
show ace_t_03_11 at right_center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice ace_f0297
Ace "「客室なんてどこだっていいじゃないですか。\n
君も、部屋にこもるよりもアウトドアのほうがいいよな、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースはエースですっかり私を連れて、城の外に出るつもりでいるらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（どうしよう……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰の意見を採ったとしても、選ばれなかったほうが拗ねる展開だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の人ならともかく、彼らの場合、銃や剣が飛び出してくることが簡単に予想できる。"


show king_t_02_08 at center
hide per_t_01_4

hide ace_t_03_11

hide viv_t_03_6
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0009
King "「お、おまえ達、彼女も困っておるようじゃし。\n
ここは普通の客室に案内するのがいいと思うんじゃが……」"

hide king_t_02_08
show king_t_02_08 at left

show viv_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0247
Vivaldi "「何じゃと？\n
キング、おまえ、わらわとこの子の憩いを邪魔する気か？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐る恐る声をかけたキングに対して、ビバルディがぴしゃりと言うと、彼はそのまま口を噤んでしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_5")
T "「いたのね、キング」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "{size=+20}（どこにいたのか分からなかったわ）{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この城では、キングの立場が限りなく低い。\n
存在感も薄いのだが……、一番まともでもある。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「え、ええと、ビバルディ。\n
私、普通のお部屋でいいわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「そうすれば、会いに行くのも楽しみになるし……ね？\n
部屋を決めている間にも遊べるじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "わざとらしいほどに可愛い子ぶってお強請りをすると、彼女は「ふむ」と頷いてくれた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同じようにして視線を向けると、ペーターは深く頷き、エースは残念そうに承諾する。"

hide viv_t_01_8
show viv_t_03_11 at center
hide king_t_02_08
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0248
Vivaldi "「……そうじゃな、ここでくだらぬ言い争いをしている間も惜しいわ。\n
おい、おまえ、この子を客室に案内するのじゃ」"

hide viv_t_03_11
show viv_t_03_11 at left
show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0011
Maid "「はい、畏まりました」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らの陰でひっそりと存在を主張していたキングの言葉が今回は（珍しく）通ったらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（よかった。\n
さすがに来た早々、銃やら剣やら取り出されたら私も頭が痛くなるもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ようやく表に出てきたキングをあわせた四人にもう一度笑顔を向けて、私は一礼した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「それじゃあ、ありがたくお言葉に甘えさせてもらうわ」"

hide viv_t_03_11

hide siro_t_02_01

$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium
if routechara == "Blood":
    jump fushigi_blood2_2
if routechara == "Deedam":
    jump fushigi_dad2_2
if routechara =="Julius":
    jump fushigi_julius2_2
label fushigi_common3_castle:

scene charasel_bg_castle_day
with dis
$ clockanim()


scene hm_spr_01
with dis

play music castle_audience_p_ali

scene bg_gen02_hs_day with Dissolve(1.2)

show viv_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0326
Vivaldi "「……飽きた」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ビバルディ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまではそれなりに集中して仕事に当たっていたはずのビバルディは、不満げに溜息をついている。"

hide viv_t_03_11
show viv_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0327
Vivaldi "「どいつもこいつもわらわに仕事を持ち込みおって……、もう少し自発的に片付けようという者はおらぬのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま書類を睨んでいた彼女はそう言うと、げんなりとした様子でペンから手を離した。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その上、机の上に頬杖をついて、溜息まで漏らしてしまう。"

play sound se_0530
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "書類の何枚かは床に落ちてしまった。"

hide viv_t_03_9
show viv_t_03_9 at left
show per_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0271
Peter "「……陛下の元に届く前に、大分減らしてあると思ったんですけどね。\n
どこかの誰かさんが押し付けられる前に手を出したらしいですから」"


show king_t_01_07 at center
hide per_t_02_4
hide viv_t_03_9
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
King "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の言うところのどこかの誰かさんは、鋭い視線が突き刺さると同時に視線を逸らした。"


show viv_t_02_6 at center
hide king_t_01_07
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0328
Vivaldi "「ふん、どうせならすべて片付けるぐらいの甲斐性を見せればいいものを」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（……それじゃあ、職務怠慢でしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの女王は心底仕事に飽きてしまったらしい。\n
書類から視線を逸らすと、私に向かって手招きをしてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「どうしたの、ビバルディ？」"

hide viv_t_02_6
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0329
Vivaldi "「どうせ仕事が進まぬのなら、堂々とサボろうではないか。\n
わらわの部屋においで、[firstname]」"

hide viv_t_01_3
show viv_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0330
Vivaldi "「新しい子が来たのだ。\n
おまえもきっと気に入るぞ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "新しい子。\n
可愛いものが好きな彼女の部屋に、どうやら新入りが来たらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（興味はあるけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "残された書類を見る限り、首を縦に振るのは良心がちくちくと痛む。"


show ace_t_02_8 at center
hide viv_t_03_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0298
Ace "「ずるいですよ、陛下。\n
こういうときには上に立つ者らしく、びしっと部下の手本になるようにしてもらわなくちゃ」"

hide ace_t_02_8
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0299
Ace "「そういうことを言っていると、下の者が真似しちゃいますよ。\n
……こんなふうに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！？」"

play sound se_0051
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（先刻までいなかったのに、いつのまに来ていたのよ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声と同時に、ビバルディから引き離される。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の神出鬼没ぶりには慣れているつもりだが、まさかこのタイミングで現れるとは思っていなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もう少し気配をさせて登場してくれないと、心臓に悪い。"

hide ace_t_03_11
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0300
Ace "「陛下がサボるんだったら、俺も心置きなく便乗させてもらおうかな。\n
うん、上司の意向に従うあたり、騎士っぽいよな、はははは」"

play sound se_0515
pause .5
play sound se_0020
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「今度は何よ！？」"

hide ace_t_03_3
show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_9")
voice ace_f0301
Ace "「ははは、ペーターさん、危ないなあ。\n
彼女に当たったらどうするの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飛んできた銃弾から身を逸らし、私から離れて、エースはからからと笑う。\n
いまだに硝煙が立ち上る銃を構えているペーターとは、真逆の爽やかさだ。"

hide ace_t_01_4
show ace_t_01_4 at left
show per_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0272
Peter "「いらぬ心配ですよ、エース君。\n
君に当たることはあっても、彼女に当たるはずがありません。当然でしょう」"

hide per_t_03_2
show per_t_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0273
Peter "「[firstname]、あなたは僕のすべて……。\n
ええ、あなたを傷つける輩なんて、全部僕が撃ち殺してあげますからね」"

hide per_t_02_13
show per_t_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0274
Peter "「というわけで、手始めに……。\n
この男からでいいですよね？」"

play sound se_0023
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「やめなさい」"

hide ace_t_01_4

hide per_t_01_2

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（いつものやりとりとはいえ、相変わらず物騒な……）"

if routechara == "Blood":
    jump fushigi_common3_castle2
if routechara == "Deedam":
    jump fushigi_common3_castle2
if routechara == "Julius":
    jump fushigi_common3_castle2_julius1
label fushigi_common3_castle2:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものやりとり。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の本来住む屋敷でも、銃弾や刃物による金属音なんて珍しくもないことだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（そういえば、構図的には似ているのかもしれないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "我関せず、と傍観者の主。\n
からかう騎士は、悪戯好きの双子。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（イメージは違うけど、ウサギはウサギだものね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（そういえば、エリオットにはにんじんチョコを作ってあげるって約束していたのよね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ブラッドの紅茶は、お気に入りの在庫が尽きかけていたし。\n
ディーとダムからは、今度新しい玩具を見せてあげるって言われていた）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何でもない日常に紛れてしまうような、小さな約束\n "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思い返すだけで苦しくなる約束ではないが、ちくちくとした小さな痛みは、それでもゼロにはならない。"


show viv_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0331
Vivaldi "「ん？\n
どうしたのだ、[firstname]」"

hide viv_t_01_11
show viv_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0332
Vivaldi "「浮かぬ顔をして……。\n
こやつらのことが目障りだというのなら、そうお言い」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「あ、ち、違う、違うわよっ」"

hide viv_t_03_8
show viv_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice viv_f0333
Vivaldi "「ふむ、そうか？\n
おまえを苛立たせる原因など、わらわが消してやるぞ」"

hide viv_t_03_11
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice viv_f0334
Vivaldi "「だから、ここにいる間は、そんな浮かぬ顔を見せてはならぬよ。\n
わらわにも勿論じゃが、わらわ以外の人間にも……、な」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ビバルディ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（……気を遣ってくれたのかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同性の貴重な友人ということも手伝ってか、彼女は私のことがよく分かってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひょっとしたら私以上に、私の気持ちに詳しいのではないかと思うこともあるぐらいに。"

hide viv_t_01_3
show viv_t_01_3 at left
show per_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0275
Peter "「そうですよ」"

play sound se_0052
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースと睨み合っていたはずのペーターが、突然現れる。"

hide per_t_02_8
show per_t_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0276
Peter "「僕だって放っておきません。\n
[firstname]、あなたを苛立たせるものも害するものも全部消しますから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（私が、苛立っている？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "白いウサギの言葉に、僅かに驚いた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋屋敷の皆が私にだけ隠していることに対して、最初に感じたのは戸惑いと、受け入れられていないという苛立ち。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それは確かに今も胸の中にある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（ショックだったっていうのもあるけど……。\n
むしろ、頭に来たというか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供っぽい反抗心なのかもしれないと、思い返すこともあった。\n
だが、納得のいかない気持ちに変わりはない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……ペーターに指摘されて気付くなんて、私って鈍いのかしら？）"

hide viv_t_01_3

hide per_t_03_1
show per_t_03_1 at left
show ace_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice ace_f0302
Ace "「ははは、ペーターさんってば過激だなあ」"

hide per_t_03_1
show per_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice pet_f0277
Peter "「過激で結構です。\n
[firstname]、あんな連中の元へなんか戻らないで、ずっとここにいてくださいね」"

hide ace_t_01_4
show ace_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice ace_f0303
Ace "「まあ、確かに帽子屋さんのところも似たり寄ったりだよな。\n
君だって、どこにいたって同じだろう、[firstname]？」"

hide ace_t_03_2
show ace_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice ace_f0304
Ace "「顔と役。\n
配置が違うだけで、根本的なところは、何も変わりはしないんだから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……エース？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "含みのある言葉に思わず声をかけたときだ。"

play sound se_0121
pause .3
play sound se_0121

show viv_t_02_6 at center
hide per_t_02_8
hide ace_t_03_12
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0335
Vivaldi "「いい加減におし、おまえ達。\n
いつまでうろうろしておる気じゃ。\n
無駄口を叩く間があれば、わらわのために少しでも働け」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「大変そうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕切り直すように響いた音に、改めて見てみれば、ビバルディの前にはいまだに積み上がった書類がある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "裁判の資料や、政治的なものなど、私にはちんぷんかんぷんだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……手伝えなくて、ごめんね」"

hide viv_t_02_6
show viv_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice viv_f0336
Vivaldi "「[firstname]、おまえはほんに可愛いことを言うのう。\n
そこの無能どもに見習わせたいぐらいじゃ」"


show per_t_01_4 at center
hide viv_t_01_6
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice pet_f0278
Peter "「僕は無能じゃありません、エース君と一緒にしないでください」"

hide per_t_01_4
show per_t_01_4 at left
show ace_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice ace_f0305
Ace "「俺だって、別に無能ってわけじゃ……。\n
単に迷うことが多いだけで、仕事はちゃんとしていますよ」"


show viv_t_03_7 at center
hide per_t_01_4

hide ace_t_03_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice viv_f0337
Vivaldi "「……まったく、この～～～～～～どもが。おまえがいるからまだそれほどイライラしないが、そうでなかったら兵士の首を刎ねておるぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「は、ははは」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「私は少しでも、あなたの役に立っている？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただ、こうやって執務室に顔を出すだけの、図々しい客。\n
仕事を手伝えるわけでもなく、どうでもいい雑談の相手ぐらいしか出来ない。"

hide viv_t_03_7
show viv_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0338
Vivaldi "「勿論じゃ。おまえがいるから、我慢しようという気になる。\n
仕事も……、この馬鹿な男どもの相手もな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディに茶目っ気たっぷりに微笑まれて、私も微笑みを返していた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（役に立っているといえるほどじゃないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "受け入れられていることは分かる。"

hide viv_t_01_2


play music heartrending_a_ali

scene bg_gen_sky_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（帽子屋屋敷でも、それは同じなのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らに好かれていることは、分かっている。\n
嫌いだから爪弾きをしたのではないのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（でも、理解と納得は別問題よ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見せないように隠しきれず、騙しきれもしないなんて、意地悪なだけだ。\n
約束を放置しているという感覚が胸を痛めるが、少しは反省すればいい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（いなくなって寂しいなんて言うような人達じゃないし）"

if routechara == "Blood":
    jump fushigi_common3_castle2_blood1
if routechara == "Deedam":
    jump fushigi_common3_castle2_deedam1
label fushigi_common3_castle2_blood1:
$ fushigi_common3_castle2_blood2a_seen = False
menu:
    "心配なんてしないわよね、ブラッドは……。":
        jump fushigi_common3_castle2_blood2a
    "気にするような人達じゃないわよね。":
        jump fushigi_common3_castle2_blood2b

label fushigi_common3_castle2_blood2a:
$ fushigi_common3_castle2_blood2a_seen = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まず最初に考えてしまうのは、ブラッドのこと。"

jump fushigi_common3_castle2_blood3
label fushigi_common3_castle2_blood2b:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも、皆のことを考えてしまう。"

jump fushigi_common3_castle2_blood3
label fushigi_common3_castle2_blood3:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（平気でいるって、分かっているのに……。\n
出て行った私のほうが気にしている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤を纏った面々に囲まれながら、そんなことを思った。"



scene map_bg_spring_day
with stripe_l_long
jump fushigi_blood3_1
label fushigi_common3_castle2_deedam1:
$ fushigi_common3_castle2_deedam2a_seen = False
menu:
    "ディーやダムだし心配いらないわよね。":
        jump fushigi_common3_castle2_deedam2a
    "気にするような人達じゃないわよね。":
        jump fushigi_common3_castle2_deedam2b

label fushigi_common3_castle2_deedam2a:
$ fushigi_common3_castle2_deedam2a = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心配はいらないだろう。\n
だが、それでもまず最初に考えてしまうのは、ディーとダムのこと。"

jump fushigi_common3_castle2_deedam3
label fushigi_common3_castle2_deedam2b:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、それでも考えてしまうのは、皆のこと。"

jump fushigi_common3_castle2_deedam3
label fushigi_common3_castle2_deedam3:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（私がいなくても何とかやるでしょう、きっと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い人に囲まれながら、そんなことを思った。"



scene map_bg_spring_day
with stripe_l_long
jump fushigi_dad3_1
label fushigi_common3_castle2_julius1:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものやりとり。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうこれはハートの城での、いつものやりとりだ。\n
私が本来いる場所ではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ユリウスの部屋は直ったかしら）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（ナイトメアはやっぱり吐血していたし）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_5")
T "（グレイはグレイで、後始末に追われていたけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔を出てきたときの彼らの様子を思い出すと、申し訳ない気持ちでいっぱいになる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大変な時期に塔を出てきて、自分のやりたいようにやるなんて、どんな我侭だろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（……悪いことをしているわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでもあの塔にいることは出来なかった。\n
優しさに居た堪れなくなっていただろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（受け入れられているのに、辛いなんて）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ねえ、ペーター。\n
あなたはお詫びにもらうなら、何がいい？」"


show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice pet_f0446
Peter "「お詫び？\n
[firstname]、あなたが僕に謝る必要なんて、どこにもないじゃないですか！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで銃を握っていたはずの宰相は、いつものストーカーに早変わりすると私に抱きついてきた。"

hide per_t_02_3
show per_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0447
Peter "「僕はあなたが望むなら、殴っても、蹴られても、～～～～～されて、更に～～～～したとしても、本望です！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（このストーカーウサギ、私を何だと思っているのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "出会った早々に口移しで薬を飲ませた彼を拳で殴ったのは事実だが、私だって誰にでもアグレッシブに振る舞うわけではない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ね、ねえ、ビバルディは？」"



hide per_t_01_7
show per_t_01_7 at left
show viv_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0423
Vivaldi "「わらわに詫び？\n
ふ……、決まっておろう」"

hide viv_t_01_4
show viv_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0424
Vivaldi "「女王に対して不敬を働いたものにかける温情などない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "マニキュアを塗った指先が優雅に動く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（そうね、あなたはそういう人だったわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "明らかに首切りを暗示する動きに、遠い目になった。"


show ace_t_03_7 at center
hide per_t_01_7
hide viv_t_03_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0423
Ace "「あれ、[firstname]、俺には聞いてくれないの？\n
仲間外れなんて冷たいなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「あなたに、{size=+20}お詫び？{/size}」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分で言っていて、とても違和感がある。\n
そもそも彼に対して詫びを入れさせるような状況が思いつかない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "{size=+20}何よりも、この男を怒らせるような命知らずな真似など、誰が出来るのだろう。{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（倍返しどころか……、とんでもないことになりそう）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「なら、一応参考までに聞いておくけど……。\n
エースは？」"

hide ace_t_03_7
show ace_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0424
Ace "「うーん、そうだな。\n
相手にもよるけど……」"

hide ace_t_02_6
show ace_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0425
Ace "「君みたいな可愛い子がお詫びをしてくれるのなら、ずっとずっと傍に置いておこうかな」"

hide ace_t_02_1
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0426
Ace "「どんなものを貰うより、どんなに謝られるよりも……。\n
近くに置いておくほうが、安心だからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（それはつまり……、うろうろせずに目の届くところにいろって言いたいわけ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は私が何のためにこの場所にいるのか、何をしようとしているのか、既に察しているのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞いてみたい気もするが、正面から聞くのもどこか気恥ずかしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（……傍にいることを証明するようなもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相手を思い出すときは、珈琲にいい点数をもらおうと躍起になっていたことも、同時に思い出す。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……ありがとう、参考になったわ」"

hide ace_t_03_3
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice ace_f0427
Ace "「どういたしまして。\n
俺は騎士だから、女の子の味方だよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "軽く告げられた言葉に、何故か今はほっとする。"

hide ace_t_01_10


scene bg_gen_sky_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（離れているだけじゃ解決にならないのは分かっている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "でも、何かで報いたい。\n
私の居場所になってくれたあの場所にいる、優しい人に。"
$ fushigi_common3_castle2_julius2a_seen = False
menu:
    "ユリウスには何がいいんだろう。":
        jump fushigi_common3_castle2_julius2a
    "皆に何かしてあげたい。":
        jump fushigi_common3_castle2_julius2b

label fushigi_common3_castle2_julius2a:
$ fushigi_common3_castle2_julius2a_seen = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まず最初に考えてしまうのは、ユリウスのこと。"

jump fushigi_common3_castle2_julius3
label fushigi_common3_castle2_julius2b:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "皆のことを考える。"

jump fushigi_common3_castle2_julius3
label fushigi_common3_castle2_julius3:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ああ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（まだしばらくは帰れそうもないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分が納得できる形で、塔に帰るために、もう少し時間帯が必要だ。"



scene hm_spr_01
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_long
jump fushigi_julius3_1
