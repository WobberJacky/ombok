jump fushigi_common3_castle
label fushigi_julius3_1:

scene map_bg_spring_day
with stripe_l_medium

scene hm_spr_01
with stripe_l_medium

scene hn_spr_01
with stripe_l_long
play sound se_0083

play music castle_garden_p_ali

show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（エース？）"

hide ace_t_03_10

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城にある、広大な庭。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "買い物を終えて、そろそろ塔へ戻ろうかと考え始めている。\n
ただ、きっかけだけが掴めずに、ふらふらと庭を歩いていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すると、真っ赤なその色彩の中に、少しだけ色を違えた赤が浮かんでいるのが見えて、私は足を止めた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「……何をしているのかしら？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城の中で見かけても、あちこちへ動き回っている彼が、じっと座っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬、剣の鍛錬として瞑想をしているのかとも思った。\n
しかし、エースのいるあたりから何やら硬い音が響いている。"

play sound se_0083
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「？？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_16")
T "（エースがじっとしているのもすごく珍しいんだけど。\n
それに、何だか楽しそうよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースは分かりやすく、同時にとても分かりにくい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今はユリウスが同じ国にいるおかげか、不安定そうでも、比較的平穏な気配ではある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、笑いながら斬りかかることも珍しくないし、気持ちが不安定なときにはただでさえ他の追随を許さない迷い癖が悪化する。"




scene bg_gen_sky_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（あの後、どうしたんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "森の中で久しぶりに顔を合わせた尾行姿を思い出す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子、サングラス、マフラー、手袋、ロングコート。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "昼間に歩いていたら、間違いなく「見なかった振りをしよう」と本能的に避けたくなる格好で現れた、大事な人。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（私が勝手に出てきたんだもの。\n
帰ってこいなんて……、言うような人じゃないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒らせて喧嘩をしたことも今までにだってある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースは倦怠期だとか何とか揶揄していたが、私達だってまったく喧嘩をしなかったわけではないのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声を荒げて言い合うだけが喧嘩ではない。\n
口に出せないからこそ、こじれてしまう関係だってあるのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ただでさえ、言葉が足りないものね、私達の場合）"

$ hi_mes()

scene bg_gen_sky_spr_day_s with Dissolve(1)

scene ts_01_s with Dissolve(1)

scene ts_01 with Dissolve(1.2)

play music tower_room2_p_ali

show yuri_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice jul_f0220
Julius "「言っただろう、これは私の仕事なんだ。\n
おまえが手を出す必要はない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「それは分かっていたんだけど……」"

hide yuri_t_03_7
show yuri_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice jul_f0221
Julius "「分かっていただと？\n
つまり、おまえは私の邪魔になることが分かっていて、それでも手を出したのか？」"

hide yuri_t_02_7
show yuri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice jul_f0222
Julius "「ずいぶんな嫌がらせだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「そこまで言わなくたっていいじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計の修理は、時計屋である彼だけの仕事だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それは重々分かっていたのだが、ユリウスは数時間帯を徹してまで修理することが続いていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、彼の留守に、私でも直せそうな部品を弄ったのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……手を切るなんて、間抜けよね）"

play sound se_0494

show t_yuri3_1 onlayer master
with dis
hide yuri_t_02_11

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計は金属製だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "取り扱いには気を付けていたつもりだが、手の平をざっくりとやってしまった。\n
彼に見つかる前に手当てをしようと思ったのだが、間に合わなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「邪魔をしようと思ったわけじゃないわ。\n
ただ……、最近、あなたも仕事を詰めすぎていたから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice jul_f0223
Julius "「これぐらいで音を上げるほど、柔な身体はしていない。\n
夢魔でもあるまいし……、私を馬鹿にしているのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（そういう言い方しか出来ないって分かっているけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（でも……、落ち込む）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "邪魔だというのなら、私の怪我など放って仕事をすればいい。\n
そう思いはするものの、似ているからこそ、分かってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ユリウスはそんなこと、しない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "甘えているのかもしれない。\n
誰にも頼らず、自分で生きていけるようになりたいと思っているのに、彼には寄りかかってしまう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0224
Julius "「これでいい。\n
しばらくは余計なことに手を出すな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「余計なこと？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
voice jul_f0225
Julius "「余計なことだろう。\n
これは本来余所者のおまえには、関わりのないことだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
voice jul_f0226
Julius "「無意味なものなんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（突き放さないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私自身が余所者なのは、今更どうしようもない。\n
変えることも、やめることも出来ないのだから。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それを理由にされてしまえば、反論の余地を失う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「私にとって無意味だってあなたは言ったけど、ユリウスにとっては、関わりの深いものでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「だったら、私にとっても無意味なんかじゃないわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice jul_f0227
Julius "「だが、現におまえは怪我をした」"

play sound se_0055
$ flash_red(.1)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きゅっと結ばれた拍子に、小さな痛みが腕に走る。\n
顔を顰めた私を困ったように見ながら、ユリウスは息をつく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0228
Julius "「……おまえが怪我をするぐらいなら、私が仕事で倒れるほうがいい。\n
自業自得だからな」"

hide t_yuri3_1
show t_yuri3_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0229
Julius "「それに……。\n
これには、あまり触れさせたくない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私に向かっていた眼差しが、壊れた時計に注がれる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっと見下ろす目は悲しんでいるようにも、哀れんでいるようにも、イラついているようにも見えた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「それでも……。\n
もし、仕事のしすぎでユリウスが倒れたら、私が怒るわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「時計にだって、妬くかもしれない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（そんな眼差しでじっと見つめられるなんて、羨ましい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達は共通している部分を多く持っている。\n
鬱陶しい性格に、素直じゃない言葉。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手放されたくないと思っていても、それを口に出すだけの勇気がない。"

hide t_yuri3_2
show t_yuri3_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0230
Julius "「……まだ、痛むか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「いいえ、もう痛くないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "傷そのものは鋭利な切り口だったから、無理をしなければすぐに治るだろう。\n
時間帯が過ぎれば、私の傷だって治る。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0231
Julius "「そうか」"

hide t_yuri3_3
show t_yuri3_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0232
Julius "「おまえが怪我をしたことを喜ぶわけじゃないんだが……。\n
怪我をした原因が、私のためというだけマシなんだろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0233
Julius "「他の誰かのためにおまえが傷ついていたのだとしたら、私は自分を責めることも出来ない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を包み込まれて、暖かさを感じる。\n
ユリウスは冷たいふりをして……、すごく優しい人だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0234
Julius "「おまえが傷つくのを止めるだけの力はないが……、他の誰かのために怪我をするのだけはやめてくれ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0234_5
Julius "「仕事を放棄するだけの気概のない私には、おまえのためにすべてを捨てられない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「捨てなくていいわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（私は近くにいて傷つけられてもいいけど、仕事を放棄してしまうユリウスなんて、想像がつかない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らにとって役割とルールは大切なものだと知っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（私のためになんて言われても、怖いだけよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ルールを破れば、ペナルティが科せられることは知っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それがどんなものなのかを私は正しく理解しているわけではないが、この世界ではルールが大きな位置を占めている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私のためにこの人が罰せられるのは、認めたくない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
Julius "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「あなたはあなたのままでいいわ。\n
だから、私もここにいられるんだもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大切にされているのは分かる。\n
愛されていることも自覚している。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから少しでも近くにいて、役に立ちたい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「無理はしないでいいと思うわ、ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（あなたは私のために、傷つかないで）"

$ hi_mes()
hide t_yuri3_4


scene ts_01_s with Dissolve(1)

scene bg_gen_sky_spr_day_s with Dissolve(1)

scene bg_gen_sky_spr_day with Dissolve(1.2)

play music truth_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（……馬鹿みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が私を追い出したのではなく、私が自分から離れたのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（甘えすぎよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もしかしたら、迎えに来てくれたんじゃないかとか。\n
心配してくれたんじゃないかとか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が勝手に期待をして、勝手に残念がっただけの話。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼には何の落ち度もない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（ここにユリウスはいないのに。\n
エースといると、ユリウスのことを考えずにはいられない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔を出てから身を寄せる場所は、ハートの城の他にもあった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この城に来たといっても、他の人……、たとえばビバルディやーペーターと過ごすことだって出来るはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも、気が付けば、この城での多くの時間帯を彼と一緒に過ごしている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースの中にある、ユリウスへの気持ちの一部は、私の中にあるものと近い。\n
嘘をつかない、不器用な性格を、好ましく思っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（……下りていってみよう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "庭でじっとしている騎士の背中は、いまだ動く気配を見せないが、いつまでもあそこにいるとは限らない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迷子の彼が旅立つ前に、声をかけに行くことにした。"

play sound se_0383

scene hn_spr_01
with stripe_l_long

play music forest2_p_ali
play sound se_0083
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "階段を下りて、庭に出る。\n
緑の絨毯に腰を下ろしたエースは、手にナイフを持ったまま何かを弄っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の気配に彼は気付いているはずだが、振り返る様子はない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「エース」"



show ace_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice ace_f0428
Ace "「ふんふん……、と、あれ？\n
[firstname]、どうしたんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「上からあなたがここにいるのが見えたから、下りてきたのよ。\n
何をしているの？」"

hide ace_t_01_3
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice ace_f0429
Ace "「ああ、これか。\n
見てみる？」"

play sound se_0262
hide ace_t_03_11


scene t_cut_yuri3u
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうぞというように差し出されたのは、小さな工芸品だった。"


scene t_cut_yuri3
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（イヤリング……、ううん、ピアス？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "丸く削られた石を貫通するように、金属の細い線が延びている。\n
全体のデザインは細く、しなやかで、女性もののようだ。"


show ace_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0430
Ace "「どう、結構うまく出来ただろう？\n
こういう細かいものに金具を通すのって、難しいんだよなあ」"

hide ace_t_02_1
show ace_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0431
Ace "「ははは、何回か石ごと壊して全部作り直してさ。\n
本当に俺ってついていないよな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「どうしたの、これ。\n
誰かへの贈り物？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（エースが女性に贈りものなんて、想像がつかないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "贈る相手もなかなか思いつかないが、彼がプレゼントをするというのも何だか意外だ。"

hide ace_t_02_3
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0432
Ace "「そうだよ。\n
手作りのアクセサリーなんて、好きな子以外にあげたりしない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首を傾げると同時に、立ち上がったエースに距離を詰められた。\n
ナイフを握ったほうとは逆の手が、目の前に差し出されている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「何のつもり？」"

hide ace_t_03_10
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice ace_f0433
Ace "「この石に、見覚えがない？\n
この前、君が見つけたあの石だよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゆっくりと開かれた相手の手のひらには、キラキラと光る石。\n
私が椅子代わりにしようとしていた石からエースが切り取ってきた、宝石だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「あのときの……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この宝石と、エースの答えで、私はユリウスへのお詫びの品を決めたのだ。\n
今は、ハートの城の客室においてある、傍にいられるような証。"

hide ace_t_01_10
show ace_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0434
Ace "「俺、あのときにも言ったよな？」"

hide ace_t_03_9
show ace_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0435
Ace "「君に似合うものを作ったら、貰ってくれるか……って。\n
このピアスじゃ、君には似合わない？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目の前で石が揺れる。\n
陽の光を反射してきらきらと輝いていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（エースが私のために作ったの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本来だったら喜ぶべき状況かもしれない。\n
工芸なんて縁のなさそうな男が、手ずからアクセサリーを作ってくれたのだ。"


scene hn_spr_01
with dis


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、私は首を横に振る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「もらえないわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（答えなんて、分かっているでしょう）"

hide ace_t_03_12
show ace_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice ace_f0436
Ace "「どうして？\n
君と俺は仲よしだろう？」"

hide ace_t_03_2
show ace_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice ace_f0437
Ace "「君だって、俺のことが好きだって言ってくれたじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "森の中で問いかけられた言葉に、私は確かにそう答えた。\n
エースのことも好きだと思う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これは間違いないこと。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「ええ、好きよ。\n
でも、あのときにも言ったでしょう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（だけど、それは……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「友達として好きなの。\n
こんな贈り物なんてもらっていい仲じゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手作りのアクセサリー。\n
友情の延長でもらうには、私の気持ちが追いつかない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（それに、エースが何を考えているのか……、分からない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "嫌われているわけではないだろうが、好きという言葉の意味通りには受け取れない。"

hide ace_t_03_7
show ace_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0438
Ace "「せっかく作ったんだから、もらってくれればいいのに」"

hide ace_t_02_8
show ace_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0439
Ace "「元は君が見つけた石だろう？\n
だったら……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースの言い分も分かる。\n
誰だって自分の贈り物を、それも自分で作ったものを断られれば落ち込むものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（私だってその気持ちは分かるけど……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「もらえないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "深い意味はないのかもしれない。\n
エースのことだ、単なる思いつきで始めたのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、もらう私の気持ちはそこまで軽くはすませられない。"

hide ace_t_02_11
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0440
Ace "「ユリウスが怒る？\n
そう思っているのかな、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

hide ace_t_03_11
show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice ace_f0441
Ace "「大丈夫さ、ユリウスは仕事のことは別だけど、それ以外じゃ滅多に怒らない。\n
君がこれをつけて帰っても、気にはしても何も言わないと思うな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（よく分かっているわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースの言葉はそのまま私の予想通りだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐らく、私がこれをつけて帰ればユリウスは気にはするだろう。\n
だが、自分からはなかなか切り出せない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらちらとこちらを見ながら問いかける言葉を探す、そんな姿まで簡単に想像がついてしまった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（でも、何も言ってもらえないかもしれないって思うのも嫌なのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問い詰めてくれればいい。\n
しかし、うじうじした性格の私達はお互いに気まずい思いをするだけだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（そんな思いをするなんて、自虐的すぎる）"

hide ace_t_01_4
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
Ace "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「私に、ピアスホールはないの。\n
だから、もらっても付けようがないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つけられないものは貰えない。\n
そう断った。"

hide ace_t_01_10
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースはピアスを手にしたままじっと私を見ていたが、やがて口元を少し緩めた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "楽しそうな、それでいて……。\n
何かを企んでいるような顔だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（その笑い方は何だか嫌な予感がするんだけど）"

hide ace_t_03_10
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice ace_f0442
Ace "「なら、開けてあげる。\n
耳を貸してくれよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「…………」"

play sound se_0492
camera at hpunch
camera at vpunch

play music cornered_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「エース！\n
悪い冗談はやめてよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "宝石を持っている手が下げられて、ナイフを握っていた手が私の耳を掴む。\n
抵抗したくても、動くと耳が切れてしまいそうだ。"

hide ace_t_03_3
show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0443
Ace "「ははは、冗談なんかじゃないよ。\n
冗談なんかで女の子に傷を付けたりしないぜ、俺は」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「冗談じゃないほうがずっと質が悪いわ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「……や、いたっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T "（強く引っ張らないでよ！）"

hide ace_t_02_4
show ace_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_10")
voice ace_f0444
Ace "「どこがいいかな……。\n
君の耳は、どこも柔らかくて触り心地がいいから迷うなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「やだってば！\n
エース！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "冗談か本気か区別のつかないエースの言葉が恐ろしく、体の力が入らない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、たとえ力が入ったとしても、私の手でエースを引き離せるかどうかは、あやしい。"

hide ace_t_03_9
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0445
Ace "「大丈夫だよ。\n
俺、短いナイフの使い方はそれほど得意じゃないけど、穴を開けるぐらいなら何とかなるから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "{size=+20}「ピアスホールはナイフで開けるものじゃない！！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（耳ごと切り落とされちゃうわよ！！）"

hide ace_t_01_10
show ace_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice ace_f0446
Ace "「そんなことはないぜ、大は小を兼ねるって言うだろう？\n
平気平気」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「へ、平気じゃな……！」"

play sound se_0675
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "耳に走った冷たい感触に、思わず声が止まる。\n
手の中で持ち方を変えたエースは、ナイフの先端を私の耳たぶに触れされた。"

hide ace_t_01_1
show ace_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0447
Ace "「暴れるとかえって手元が狂っちゃうだろう？\n
じっとしていなよ」"

hide ace_t_03_2
show ace_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0448
Ace "「痛くしないように、優しくするからさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T "（優しくされても、されなくても、そんなのを振り回す段階で問題よ！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "低い声が笑いを含んでそう告げたのを感じつつ、それでも声が出て来ない。\n
どうしようもない事態に、痛みを堪えるように目を閉じる。"


show black onlayer master with close_short
pause .5
play sound se_0020
hide ace_t_03_12

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0449
Ace "「……ははは、どうしたんだ、ユリウス？\n
いきなり撃つなんて危ないぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_4")
T "（今、ユリウスって……？）"

play sound se_0020
pause .3
play sound se_0020

play music opposition2_a_ali
hide black
show t_yuri3_5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視線だけを向ければ、エースの言葉どおり、木々の間に人影が見える。\n
この前と同じように、長いコート等で変装をした長身の男が立っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃声の発生元は、ユリウスのようだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

play sound se_0020
$ flash(.1)
play sound se_0439
pause .5
hide t_yuri3_5 with dis
show white onlayer master ##instant
play sound se_0191
hide white with spread_extrashort
pause .5
play sound se_0020
$ flash(.1)
pause .3
play sound se_0020
$ flash(.1)
pause .4
play sound se_0191
pause .2
show white onlayer master
play sound se_0191
hide white with spread_extrashort
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスはエースの言葉には応えず、淡々と銃を発砲し続けている。\n
おかげで拘束が解けた私は、慌てて距離を取る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "発砲されたほうを向くと、ユリウスがいた。\n
サングラスとマフラーのせいで、その表情を伺うことは出来ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（よく顔の半分以上を隠した状態で、銃なんて撃てるわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなどうでもいいことを思う。"

show t_yuri3_6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0450
Ace "「ははは、危ないなあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつの間に抜いたのか、銃弾を剣で弾きながらエースは一人だけ妙に楽しそうだ。\n
生き生きしていると言ってもいい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

play sound se_0020
$ flash(.1)
pause .3
play sound se_0191
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "獣じみた動きでエースは銃弾をかいくぐると、一気にユリウスのほうへと身体を寄せた。"

play sound se_0440
pause .4
play sound se_0117
##special anime"kiseki02"loop="false"with Dissolve(1)
pause .15
play sound se_0684
hide t_yuri3_6
show t_yuri3_7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0451
Ace "「いつまでもそんなのつけていたら見えにくいだろう？\n
このほうが、俺もよく見えるし」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サングラスとマフラーを一瞬にして斬り捨てたエースに、ユリウスは苦い眼差しを向けている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0235
Julius "「どういうつもりだ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0452
Ace "「ん？\n
ユリウスの顔が見えないままだったから、よく見えるようにしたんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0453
Ace "「俺って、友達思いだろう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0236
Julius "「そんなことは聞いていない。\n
あいつに……、何をしようとしていたんだと聞いているんだ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……怒っている？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段から笑顔でいるほうでもないが、明らかに怒っているのが分かる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（でも、どうして？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice ace_f0454
Ace "「何って……、彼女が落ち込んでいるみたいだから、慰めてあげようと思っただけだよ。\n
ちょっと痛い方法だけどね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice jul_f0237
Julius "「エース、おまえ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴりっとした声でユリウスが睨み付ける。\n
しかし、エースが気にした様子はなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0455
Ace "「どうして怒るんだよ、ユリウス。\n
この前だって、様子を見に来たのに結局何もせずに帰っちゃうしなあ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0456
Ace "「俺、うじうじしているユリウスが大好きなんだ。\n
君だって、そう思うよな、[firstname]？」"

play sound se_0454
hide t_yuri3_7
show t_yuri3_8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こちらを振り返ったエースに、嫌な予感がした。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0238
Julius "「おい、待てエース。\n
おまえ、何を……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0457
Ace "「この子がいなくなったら、もっと後ろ向きになるのかな。\n
うん、何だかそれって……、ちょっと見てみたいなあ」"


play music opposition1_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

play sound se_0675
pause .3
play sound se_0117
play sound se_0484
hide t_yuri3_8
show t_yuri3_9 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤が翻る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまでユリウスの間近にいたエースがあっという間に私のほうへと走ってくる。\n
その手に、剣を構えたままで。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！」"
$ fushigi_julius3_5b_seen = False
menu:
    "ユリウス！":
        jump fushigi_julius3_5a
    "馬鹿なことをしないで、エース！":
        jump fushigi_julius3_5b

label fushigi_julius3_5a:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "走ってくるエースの姿に、心臓が凍りつく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（本気で斬るつもり？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よくも悪くも表や裏のないエースだ。\n
斬ると言ったら本気で斬りかかるだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何の躊躇いもなく、表情も変えずに斬り捨ててきた彼を、私はよく知っている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「……！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「ユリウス！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤に続いて、コートを靡かせながらユリウスが走る。\n
しかし、エースのほうが早い。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

play sound se_0678
hide t_yuri3_9
show bg_gen_sky_spr_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この城にやってきたときと同じように。\n
彼は爽やかな笑顔で、私に向かって剣の切っ先を突き出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（斬られるっ！）"

play sound se_0020
pause .1
play sound se_0437
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（あれ、痛くない）"

hide bg_gen_sky_spr_day
show t_yuri3_10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice jul_f0239
Julius "「……誰がこいつを斬れなどと言った？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0458
Ace "「誰も言っていないよ。\n
ただ俺がそうしたほうがいいのかなって思ったから、そうしようとしただけで」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice jul_f0240
Julius "「……そうか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "身体に走るはずだった痛みの代わりに、赤い城の庭に響いたのは、二人の男の冷たい声。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "固く閉じていた目を開ければ、私に背を向けているエースの背中と、そんな彼に銃口を向けるユリウスがいた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（ユリウスが撃って、エースが弾いたんだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものユリウスならば、声で制止をしているはずだ。\n
それがどうして……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（いや、そのおかげで助かったのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスが止めてくれなければ、どうなっていたか分からない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0241
Julius "「そいつにそれ以上手を出すな」"
jump fushigi_julius3_6
label fushigi_julius3_5b:
$ fushigi_julius3_5b_seen = True
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「ば……。\n
馬鹿なことをしないで、エース！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice ace_f0459
Ace "「馬鹿なことじゃないよ、これは」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は言いながらも足を止めない。\n
先ほどまで開いていた距離が一気に詰まっていく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0460
Ace "「君にとっても、ユリウスにとっても、これは一つの答えだろう？\n
俺は、二人とも好きだから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0461
Ace "「[firstname]、君とユリウスが望むなら。\n
悪役になってもいいんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0462
Ace "「恨まれたって、憎まれたって……、ね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悪役。\n
告げられた言葉の意味が分からない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（それに、私はあなたにそんな『役』を持たせたいなんて思わない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "役持ちであることを厭っているエース。\n
特別なものを持ちたくないし、特別になりたくないという、ハートの騎士。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（顔は嬉しそうだけど、気持ちもその通りとは限らない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "笑っているからと言って、本心からとどうして言い切れるだろう。\n
笑顔さえ仮面のように使ってしまえる人ならば、簡単に欺してしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（斬られちゃ、いけない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスのためにも、私のためにも。\n
そしてエースのためにも、私はここで黙って斬られるわけにはいかない。"

hide t_yuri3_10
show bg_gen_sky_spr_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「[firstname]！」"

play sound se_0020
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスが私の名前を呼ぶと同時に、銃を撃つ。\n
エースは飛んできた銃弾を器用に避けて、ようやく足を止めた。"

hide bg_gen_sky_spr_day
show t_yuri3_10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私にちょうど背を向ける姿勢。\n
ユリウスと私の間に割り込むような位置だった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0242
Julius "「やめろと言っただろう、エース！」"

jump fushigi_julius3_6
label fushigi_julius3_6:
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0463
Ace "「……どうして？\n
だって、ユリウスは別にこの子がいなくてもいいんだろう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0464
Ace "「いらないんだったら、俺がもらって、傷物にしたっていいじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0243
Julius "「いいわけがないだろう、この～～～～～～っ！」"

play sound se_0509
hide t_yuri3_10
show t_yuri3_11 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「ユリウス！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（銃を工具に戻してどうするの？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Ace "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice jul_f0244
Julius "「おまえ、銃は好きじゃないんだろう。\n
何がしたいのかは知らんが、本当の狙いは私のはずだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice jul_f0245
Julius "「そいつに手を出すな。\n
あと一歩でも近付いたら、今度は威嚇ではすまんぞ」"

play sound se_0348
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "工具を握り締めたユリウスはそう言って、ずっと羽織ったままだったコートを投げ捨てた。"

hide t_yuri3_11
show t_yuri3_12 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0465
Ace "「へえ……。\n
ユリウスが、俺の鍛錬に付き合ってくれるんだ？」"

play sound se_0674
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0466
Ace "「手合わせするのは久しぶりだよな。\n
楽しみだ」"

play sound se_0117
play sound se_0484
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "満足そうに言ったエースの言葉が、始まりの合図となった。"

hide t_yuri3_12
show bg_gen_sky_spr_day onlayer master
with dis
play sound se_0679
pause .2
play sound se_0686
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……あ」"

play sound se_0677 volume .8
pause .3
play sound se_0677 volume .6
pause .3
play sound se_0677 volume .4
pause .5
play sound se_0318 volume .4
pause 1
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（あっさりと決着ついちゃった）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（当たり前だけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "剣とスパナではそもそも武器と工具という大きな違いがある。\n
その上、持ち主がエースとユリウスだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（金属バットを持った野生児と、コンパスを持ち出したガリ勉くんが喧嘩をするようなもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最初からどちらに軍配が上がるかなんて、問うだけ無駄というものだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも私がこんなに冷静にしていられるのは、争っている相手が二人だからだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（エースもユリウスも……、お互いを消したりはしない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お互いにお節介をしたくなるほど、大切にしているのだから。"

hide bg_gen_sky_spr_day


show yuri_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

hide yuri_t_03_11
show yuri_t_03_11 at left
show ace_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0467
Ace "「降参する？」"

play sound se_0242
hide yuri_t_03_11
show yuri_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "からかうようなエースの言葉にユリウスは無言で別の工具を取り出してみせる。\n
続行の意を汲んだエースは、再び剣を握り締めた。"

hide ace_t_03_12
show ace_t_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0468
Ace "「行くぜ、ユリウス」"

hide yuri_t_02_11
show yuri_t_02_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（今、ユリウスが私を見たような……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらりと彼が私に目配せを送ってきたことに気が付いたが、その意味は分からない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（何だったの、今のは）"

play sound se_0440
pause .3
play sound se_0506
$ flash(.2)
pause .4
play sound se_0677
pause .3
play sound se_0441
pause .2

show white onlayer master ##instant]
play sound se_0043
hide white ##instant
show t_yuri3_13 onlayer master with spread
hide ace_t_01_10

hide yuri_t_02_9

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice jul_f0246
Julius "「この馬鹿力が……。\n
いい加減言わせてもらうぞ」"

play sound se_0439
pause .4
play sound se_0191
$ flash(.3)
pause .3
play sound se_0677 volume .8
pause .3
play sound se_0677 volume .6
pause .3
play sound se_0677 volume .4
pause .5
play sound se_0588
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二本目の工具が遠くへと弾き飛ばされて、生け垣に突っ込んだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0469
Ace "「何？\n
言いたいことを言わないでいるのはストレスになるだろ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0470
Ace "「ただでさえユリウスは細かい仕事で神経を張り詰めすぎなんだから、溜めるのはよくない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0471
Ace "「……あ。\n
今は別のほうが溜まっているかもしれないけど」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0247
Julius "「迷子で遅刻魔なのは今更どうしようもないとは思っているが……。\n
そういうデリカシーのないところを、改めたらどうだ！？」"

play sound se_0678
pause .2
play sound se_0685
$ flash(.1)
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0472
Ace "「えー、デリカシーがないなんて酷いなあ。\n
俺は親友の身体を気遣ってあげているだけなのに」"

play sound se_0605
pause .3
show white onlayer master ##instant
hide t_yuri3_13
play sound se_0043
show bg_gen_sky_spr_day onlayer master with spread_short
hide white ##instant
pause .2
play sound se_0677 volume .8
pause .3
play sound se_0677 volume .6
pause .3
play sound se_0677 volume .4
pause .5
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（……三本目）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "スパナは虚空に放物線を描いて飛ばされていく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"


play music heartrending_a_ali
hide bg_gen_sky_spr_day with Dissolve(.4)


show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0473
Ace "「どうする、まだ続ける？」"

hide ace_t_01_10
show ace_t_01_10 at left
show yuri_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0248
Julius "「…………。\n
おまえ相手に接近戦で勝てるとは思っていない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "弾き飛ばされた手が痺れたのか、右手を撫でながらユリウスは言う。"

hide yuri_t_02_8
show yuri_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

hide yuri_t_02_11
show yuri_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0249
Julius "「それで、おまえは一体こんな面倒な真似までして、何がしたかったんだ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一拍置いてから、ユリウスは静かに問う。\n
元から戦って決着をつけようとしていたわけではないらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでもエースに付き合って戦うあたり、真面目だと思った。"

hide ace_t_01_10
show ace_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0474
Ace "「ははは、言ったじゃないか。\n
俺は二人とも好きなんだ」"

hide ace_t_01_1
show ace_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0475
Ace "「だから、二人がお互いにうじうじしているのを見ているのも悪くないなあと思っていたんだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

hide yuri_t_03_12
show yuri_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice jul_f0250
Julius "「……{size=+20}悪趣味な話だ{/size}」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（同感だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "話に入っていこうとは思わないが、激しく頷く。"

hide ace_t_03_11
show ace_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0476
Ace "「冷たいなあ、ユリウス。\n
……まあ、いいや」"

hide ace_t_03_2
show ace_t_02_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0477
Ace "「ええと……、そういうわけで、俺は愛のキューピッドならぬ二人の仲を取り持つ愛の騎士になったわけだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「は？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（意味が分からない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこがそういうわけなのだろうか。\n
ユリウスにも視線を向ければ、彼は彼で複雑そうな顔をしている。"

hide yuri_t_03_13
show yuri_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0251
Julius "「おまえの説明にまともさを求めてはいないが……、それではあまりにも言葉が足りない」"

hide ace_t_02_1
show ace_t_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0478
Ace "「彼女がハートの城に来た理由を聞いて、ピンときたんだ。\n
きっと二人は放っておいたら、ずるずるいつまでも落ち込み続ける、ってね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースの言葉は耳に痛い。\n
確かにこのままいたら、何もせずに終わりそうだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（帰り損ねていたのは事実だし……）"

hide ace_t_03_7
show ace_t_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice ace_f0479
Ace "「だから、俺が一肌脱いでみたんだ。\n
二人を仲直りさせるためなら、俺は悪役だって引き受けてやるぜっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誇らしげに言われて、しばし思考が止まった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "{size=+20}「かえってこじれただけじゃない」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（別に喧嘩をしていたわけじゃないし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "森でユリウスに再会したときも、今回も。\n
彼の行動がなければ、もう少し話は早かったのではないかと思う。"

hide ace_t_01_4
show ace_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0480
Ace "「そんなことはないと思うぜ、[firstname]」"

hide ace_t_03_9
show ace_t_03_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0481
Ace "「だって、ユリウスなんだ。\n
君が自分の意志で出ていったのに、心配してついてきたからって素直に出て来られると思う？」"

hide ace_t_03_12
show ace_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0482
Ace "「無理だよな、ユリウス？」"

hide yuri_t_03_11
show yuri_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視線を逸らした上で沈黙ということは、是なのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（確かに、そういう人だった……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "冷たいふりをしていても、人一倍周囲に気を遣うユリウスらしい。"

hide ace_t_03_3
show ace_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0483
Ace "「君が取られちゃうのは心配だし、でも正面切って帰ってきてほしいとも言えない」"

hide ace_t_02_10
show ace_t_02_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0483_5
Ace "「ほんと、ユリウスってうじうじしていて俺は大好きだぜ！」"

hide yuri_t_02_8
show yuri_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0252
Julius "「いいから、おまえ、少しは黙っていろ！」"

play sound se_0051
camera at hpunch
camera at vpunch
play sound se_0055
hide ace_t_02_1
show ace_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0484
Ace "「ふぐ、むりうぐ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段からは想像できない素早さで、ユリウスはエースを羽交い締めにする。\n
もごもごと動くエースを押さえつけながら、ユリウスに躊躇いがちに聞かれた。"


play music forest2_p_ali
hide yuri_t_03_7
show yuri_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「……[firstname]」"

hide yuri_t_01_8
show yuri_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0253
Julius "「その……、何だ。\n
いつまで、この城にいるつもり……」"

hide yuri_t_01_13
show yuri_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0254
Julius "「いや、私は別におまえがいたいというのなら呼び戻す気はないんだが……。\n
いつまでもこいつの傍に置いておくと、いらぬ苦労ばかりさせるというか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

hide ace_t_02_8
show ace_t_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice ace_f0485
Ace "「……はあ。\n
焦れったいなあ、ユリウス」"

hide yuri_t_01_9
show yuri_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jul_f0255
Julius "「何だと！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "するりとユリウスの拘束から逃れたエースが、ぐいっと顔を近づけてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「？？？」"

hide ace_t_03_7
show ace_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice ace_f0486
Ace "「なあ、[firstname]。\n
このままここに住んじゃえば？」"

hide ace_t_03_2
show ace_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice ace_f0487
Ace "「案外君がここにいたほうが、ユリウスも部屋から出てきてくれるかもしれないし……。\n
な、ユリウス」"

hide yuri_t_03_12
show yuri_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice jul_f0256
Julius "「……ふざけるな！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

play sound se_0051
camera at hpunch
camera at vpunch

show t_yuri3_14 onlayer master
with dis
hide ace_t_02_11

hide yuri_t_03_7


play music night_garden_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声の大きさに驚くと同時に、ぐいっと腕をつかまれ、ユリウスに抱き寄せられる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0257
Julius "「こんなところにいつでも来られるほど私は暇じゃない！\n
おまえもおまえだ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「は、はい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勢いづいているのか、いつもよりも早口で、そして切羽詰まった口調でユリウスは私に言った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0258
Julius "「おまえは、とっとと私の部屋に帰って来ればいい。\n
いつまでもこんな場所に預けておく気はないんだ、私は！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_6")
T "「ユ、ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（うわ、顔が真っ赤だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言い終えてから自分の発言が恥ずかしくなったのか、ユリウスは耳まで真っ赤に顔を染めている。\n
それでも、私を抱き締める手は離さない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jul_f0259
Julius "「私は不器用だから、これ以上気の利いたことなど言えない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jul_f0260
Julius "「帰ってきてくれ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「うん。\n
……迎えに来てくれて、ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い顔のまま、ようやくユリウスが頷いたときだ。"

hide t_yuri3_14


play music knights1_a_ali
play sound se_0620 volume .7

show heisi_t_01_03 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0058
Soldier "「あそこだ、時計屋がいるぞ！」"

hide heisi_t_01_03
show heisi_t_01_03 at left
show heisi_t_02_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0036
Soldier "「早く捕らえないと、陛下がますますお怒りになる！\n
かかれ！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……あれ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（何で急に城の兵がこんなに……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足音高らかに庭へと下りてくる兵士達は、皆一様に殺気立っているように見えた。"

hide heisi_t_01_03

hide heisi_t_02_05


show yuri_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0261
Julius "「何で私を……。\n
私は中立だぞ、兵に追われる理由も囚われる理由も……」"

hide yuri_t_03_11
show yuri_t_03_11 at left
show per_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0448
Peter "「……あるんですよ、時計屋・ユリウス＝モンレー」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ペーター！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞き慣れてしまった声がして振り返れば、兵の中から出てきたのは、城の宰相その人。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "眼鏡の奥から冷淡な輝きを漂わせて、彼は腕を組んでいる。"

hide per_t_02_10
show per_t_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0449
Peter "「先ほど、陛下のいた部屋にこれが飛んできましてね……」"

hide per_t_03_9
show per_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0449_5
Peter "「残念ながら陛下に当たることはなかったんですが、すっかりへそを曲げてしまって困っているんです」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の手には、見慣れたスパナが一本。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（……そういえば、最初の工具はやたらと遠くに飛んでいったわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "金属だからそれほど遠くには飛ばないと思っていたのだが、エースの力に弾かれた金属がどこに行ったのかまでは確認していなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうやらそれは場内にいたビバルディの元まで飛んでいってしまったらしい。"

hide yuri_t_03_11
show yuri_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0262
Julius "「くだらんな」"

hide per_t_02_11
show per_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0450
Peter "「まったくです、どうせ降らせるのなら、頭にでも落としてくれればまだよかったのに。\n
……こほん、それはさておき」"

hide per_t_02_4
show per_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0451
Peter "「その上、彼女を連れ帰ろうなんて図々しい。\n
彼女は僕の愛しい人です、横取りしようなんて烏滸がましい」"

hide per_t_01_1
show per_t_01_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0452
Peter "「というわけで、恋人に付きまとうお邪魔虫は、ここで死んでいってください」"

play sound se_0515
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（いつから私とあんたが恋人になったのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃を構えるペーターに、溜息が出そうだ。\n
突っ込みどころは山ほどあるが、電波なウサギに何を言ったところで改めるとも思えない。"

hide yuri_t_02_11
show yuri_t_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

play sound se_0093
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「ユリウス？」"

hide yuri_t_02_2
show yuri_t_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice jul_f0263
Julius "「私は荒事が好きではないんだがな。\n
せっかくの機会だ、ストーカーを始末するぐらいの手間ならかけてやる」"

play sound se_0517
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは銃を構えているが、ここはハートの城、その上ペーターだけでなく兵士までいるのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "圧倒的に不利な状況である。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「あなたは中立の立場なんだから、手を出せないんじゃないの！？」"

hide yuri_t_03_1
show yuri_t_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jul_f0264
Julius "「普通はそうだが、向こうからしかけてきたものに対抗するだけだ。\n
構わんだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「そんなアバウトな……」"


show ace_t_01_10 at center
hide yuri_t_01_13

hide per_t_01_15
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
Ace "「…………」"

play sound se_0093
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "珍しく臨戦態勢になったユリウスよりも先に、赤い影が立ちふさがっていた。"


show yuri_t_03_11 at right
hide ace_t_01_10
show ace_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice jul_f0265
Julius "「エース？」"

hide ace_t_01_10
hide yuri_t_03_11
show per_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice pet_f0453
Peter "「……どういうつもりですか、エース君？\n
そこをどきなさい」"

hide per_t_03_10
show per_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice pet_f0454
Peter "「あのヒステリー……、じゃなかった。\n
女王陛下の命令ですよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私とユリウスを背に、エースが兵士達と向き合う。"



hide per_t_02_9
show per_t_02_9 at left
show ace_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0488
Ace "「ペーターさんにとってはそうかもしれないけど、俺は直接その命令を聞いてないからね」"

hide ace_t_02_12
show ace_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0489
Ace "「それに、この前も部下の鍛錬に間に合わなかったから、埋め合わせしないと。\n
俺って、部下思いの軍事責任者だから」"

hide ace_t_03_11
show ace_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0490
Ace "「次の鍛錬を前倒しってことで……。\n
いいよな？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこっ、とさわやかに笑って見せるエースに、ペーター以外の兵士達全員が怯むのが分かった。"

hide per_t_02_9
show heisi_t_01_04 at center
hide ace_t_03_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Soldier "「！」"

hide heisi_t_01_04
show heisi_t_01_04 at left
show heisi_t_02_09 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0037
Soldier "「エ、エース様……」"


show ace_t_01_10 at center
hide heisi_t_01_04
hide heisi_t_02_09
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0491
Ace "「いいよ、全員まとめて相手をしてあげる」"

hide ace_t_01_10


show per_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0455
Peter "「ほら、何をのろのろとしているんです！？\n
早く行きなさい！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……可哀想に）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "戦ってもエースには勝てないだろうが、引いたとしてもペーターに撃たれる。\n
どちらにしろ一介の兵士達に勝ち目はなさそうだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも、止めようとしないあたり、私もずいぶん悪人かもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（ユリウスが傷付くのは、嫌だもの）"

hide per_t_01_7
show heisi_t_01_02 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice hos_f0059
Soldier "「か、畏まりました、ホワイト卿」"

hide heisi_t_01_02
show heisi_t_01_02 at left
show heisi_t_02_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice oto_f0038
Soldier "「やあああ！！」"

play sound se_0004
hide heisi_t_01_02

hide heisi_t_02_05


show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
Ace "「…………」"


show yuri_t_02_8 at center
hide ace_t_03_10
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
Julius "「…………」"

hide yuri_t_02_8
show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice jul_f0266
Julius "「行くぞ、[firstname]。\n
こんな場所にこれ以上長居する気はない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらりと視線を交わしてから、城にユリウスは背を向ける。\n
それから私の腕をとって、走り出した。"

play sound se_0484
play sound se_0618
hide yuri_t_03_9

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「でも、いいの？\n
あれ……」"


show yuri_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice jul_f0267
Julius "「役なしのカードが何枚来たところで、エースには何でもない。\n
私達が引けば、あいつも適当なところで手を止める」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（羨ましいぐらいに、よく分かっているわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "必要以上に言葉なんていらない。\n
互いにメリットのある、仕事上の関係だとユリウスは言うが……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「親友だものね」"

hide yuri_t_02_1
show yuri_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Julius "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（よく分かっていなければ、背中なんて任せられないもの）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（…………）"

hide yuri_t_02_4


scene bg_gen_sky_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（今度エースにお礼に来なくっちゃ。\n
ユリウスと一緒に）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私がここに来たときに、会えるかどうかは分からない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、いつもやって来るのを待つだけではなく、たまには会いに来るのも悪くないはずだ。"

$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_long
##endmemory
label fushigi_end_read_julius:
if renpy.seen_label("fushigi_end_julius1") == True:
    jump fushigi_end_choice_julius
else:
    jump fushigi_end_check_tower1_j
label fushigi_end_choice_julius:
if fushigi_common3_castle2_julius2a_seen == True:
    jump fushigi_end_choice_julius2
else:
    jump fushigi_end_check_tower2_j
label fushigi_end_choice_julius2:
if fushigi_julius3_5b_seen == True:
    jump fushigi_end_julius_ace1
else:
    jump fushigi_end_check_tower2_j
label fushigi_end_check_tower1_j:
if renpy.seen_label("fushigi_end_nightmare1") == True:
    jump fushigi_end_check_tower2_j
if renpy.seen_label("fushigi_end_julius1") == True:
    jump fushigi_end_check_tower2_j
if renpy.seen_label("fushigi_end_gray1") == True:
    jump fushigi_end_check_tower2_j
else:
    jump fushigi_end_julius1
label fushigi_end_check_tower2_j:
if fushigi_common3_castle2_julius2a_seen == True:
    jump fushigi_end_julius1
else:
    jump fushigi_end_tower1
