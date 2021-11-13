
scene map_bg_winter_day
with dis
label fushigi_end_peter1:
$ clockanim()


scene map_bg_winter_day
with dis

scene charasel_bg_tower_day
with dis

play music tower_stairs_down_p_ali

scene cki1_01
with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔の出入り口。\n
城から持ってきた荷物を手にした私は、改めて見送りに来てくれた彼らに礼を言った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「本当に長居しちゃってごめんなさい。\n
こんなに長くなるとは思わなかったんだけど……」"


show gre_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0048
Gray "「気にすることはない。\n
こう言っては何だが、うちの人間は病人の看病には慣れているからな」"

hide gre_t_01_11
show gre_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0049
Gray "「たまには別の人間にそのノウハウを活かすのも悪くないだろう」"

hide gre_t_03_4
show gre_t_03_4 at left
show yuri_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice jul_f0028
Julius "「慣れているという割には、出てくる料理は怪しいものが多かったようだが……」"

hide gre_t_03_4
show gre_t_02_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0050
Gray "「怪しくなんかない。\n
どれも滋養強壮、体力回復効果のあるものばかりだ」"

hide gre_t_02_13
show gre_t_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0051
Gray "「結局ナイトメア様に止められたから食べてもらうことは出来なかったが。\n
何なら、城への土産にどうだろうか、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「ええ、気持ちだけもらっておくわ、グレイ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（あれを持ち帰ったりしたら、城と塔で戦争になりかねない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "余計な火種はないに越したことはない。\n
グレイは残念そうな顔をしたものの、更に強行に押し進めてくることはなかった。"

hide gre_t_02_2

hide yuri_t_02_9
show yuri_t_02_9 at left
show toustaff_a1_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0010
Tower_Employee "「まだ病み上がりなんですから、無理をしないよう気を付けてくださいね」"

hide yuri_t_02_9

hide toustaff_a1_1
show toustaff_a1_1 at left
show toustaff_b1_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0017
Tower_Employee "「そうですよ。\n
本当はあと数時間帯はうちでゆっくりしてもらいたいぐらいなんですから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「ありがとう。\n
でも、もう熱も引いたし、食欲も出てきたから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「休みを貰っているとはいえ、そろそろ仕事も気になるし、ね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔で食事を運んでくれたのは、グレイ達だけではない。\n
役を持たない彼らにもかなりお世話になってしまった。"


show yuri_t_03_11 at center
hide toustaff_a1_1
hide toustaff_b1_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0029
Julius "「そう言って、また無茶をするんじゃないぞ。\n
おまえは無防備に出歩きすぎるんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「……ユリウスもありがとう。\n
結構顔を出してくれたでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事以外のことで部屋から出ることが極めて稀な彼が、私の部屋に何度も来てくれた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "熱が酷かった頃は意識が朦朧としていたが、その後、面倒をみてくれた人達から聞いている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "礼を告げると、彼は私から視線を逸らしてそっぽを向いてしまう。"

hide yuri_t_03_11
show yuri_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0030
Julius "「知らんな。\n
人違いだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_5")
T "「うん、ならそう言うことにしておくわ」"

hide yuri_t_02_6
show yuri_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_5")
voice jul_f0031
Julius "「……にやにやとするな、顔が歪んでいるぞ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（そういうあなただって、顔が笑っているわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本当にわかりにくい形でしか優しさを発揮できないひとだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつまでも話していたいが、そうもいかない。\n
持ってきた荷物を手に、頭を下げる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「突然押しかけてきた挙げ句に熱まで出して、本当にお騒がせしました。\n
ありがとう、皆」"

hide yuri_t_02_9
show yuri_t_02_9 at left
show toustaff_a1_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice kat_f0011
Tower_Employee "「そんな大仰な……。\n
俺達はむしろ助かったぐらいですよ」"

hide yuri_t_02_9

hide toustaff_a1_3
show toustaff_a1_3 at left
show toustaff_b1_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice hos_f0018
Tower_Employee "「そうですよ。\n
ねえ、グレイ様？」"

hide toustaff_a1_3

hide toustaff_b1_2
show toustaff_b1_2 at left
show gre_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice gra_f0052
Gray "「勿論だ。\n
君が来てくれたおかげで、ナイトメア様に点滴を受けさせることに成功したんだ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "奇跡だと物語るようにグレイは何度も頷いていた。\n
握り拳を固めて力説する夢魔の腹心などという姿は滅多に見られるものではない。"

hide gre_t_01_11
show gre_t_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0053
Gray "「俺達がどんなに説得しても決して首を縦に振らなかったあの方が……。\n
君は素晴らしい偉業を果たしたんだ、[firstname]！！」"

hide gre_t_03_4
show gre_t_02_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0054
Gray "「心から感謝している」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイの目は今までにないぐらいきらきらとしている。\n
医者嫌いの上司が点滴を打ったということが、余程嬉しかったらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（そっちのほうが大袈裟だと思うけど……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「でも、結局は私の風邪が感染っちゃったでしょう？\n
むしろマイナスなんじゃ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここに見送りに来ていない友人は、現在私室で眠っている。\n
きっと復調してからまた山のような仕事に追い立てられることだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（そう考えると、申し訳ないなとは思うけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（あんなに簡単に感染るなんて思わなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは私の隣で点滴を受けていたのだが、私が復調するのとほぼ同じ時期に熱を出した。"

hide gre_t_02_14
show gre_t_03_9 at center
hide toustaff_b1_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0055
Gray "「いや、あの方が点滴を受けたという事実が大事なんだ。\n
既成事実を作れば、次もまた何かの口実になる可能性もある！」"

hide gre_t_03_9
show gre_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0056
Gray "「こうなれば根比べだ。\n
ナイトメア様の体調がよくなるまでに、俺が口説けるか、あの方が自力で体質を改善させるかの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（上司に治療をするように口説く部下……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は今このときも自室のベッドで横になっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアが描く理想の上司像とはかなり隔たりがあるが、部下に体調管理を任せなければならないあたり、その溝を埋めるのは難しい。"

hide gre_t_02_1
show gre_t_02_1 at left
show yuri_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0032
Julius "「どちらが先でも構わんが。\n
少なくとも人の風邪をもらうようでは、後者の望みは薄いな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（ユリウスに同感するわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少し距離があると見方が変わるのか、クローバーの塔の部外者であるユリウスの言葉のほうが、正しく聞こえてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（血を吐くわ、だらだら汗は掻き出すわ。\n
一体何ごとかと思ったわよね、あれは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアが発熱したときは、大騒ぎだった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "青白い顔が少し上気しているから、血色がよくなったと期待したのだが……、実際は発熱による火照りだったと気付いたとき、グレイは盛大に落ち込んだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもなら「もっと上司の心配をしろ」と喚くナイトメアも、さすがにあれだけ喉が腫れると動く気力がわかないらしい。"

hide yuri_t_03_10
show yuri_t_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0033
Julius "「いつまでもたもたしているんだ。\n
早く帰れ、待っている奴がいるんだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「うん、ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背中を押すようにかけてくれたユリウスの言葉に、ようやく私は塔の外へと踏み出す。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「グレイ、ナイトメアにもよろしく。\n
今度、風邪を感染しちゃったお詫びとお世話になったお礼を兼ねて、お見舞いを持ってくるからって伝えておいて」"

hide gre_t_02_1
show gre_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice gra_f0057
Gray "「ああ、分かった、必ず伝えておくよ。\n
君こそ、気を付けて。また、いつでもおいで」"

hide gre_t_03_4

hide yuri_t_01_7


scene bg_gen_sky_win_day
with dis

play music forest_town_road_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「それじゃあ……」"

play sound se_0625
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "荷物を手に塔の入口から離れる。\n
最初は一人一人がはっきりと見えていたが、距離が開くと共にだんだんと見分けが付かなくなった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らの影が完全に見えなくなってから、私はようやく前を向く。"

play sound se_0623
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「さて……。\n
じゃあ、帰らないと」"


scene s2_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひとけのない森。\n
けれど、胸の中に込み上げてくるものは寂しさとは別の感情。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔から城まではかなりの距離がある。\n
急いても仕方ないと思っているのに、足下から響く音は少しずつ早くなっているような気がした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（まだ待っているかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭の中に浮かんだのは、あのとき、門で再会した白いウサギ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T "（最初にお帰りって言いたい、なんて……。\n
変なところで可愛いことを言うんだから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "酷薄な顔で気に入らない人間を撃ち殺す宰相のくせに、どうして私にだけはあんなに甘いのだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「…………」"

play sound se_0619
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見えない私を捜していた眼差し。\n
重なるはずのない目線があったと感じた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの瞬間を思い出すと、もう止まらなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「私も人のことは言えないわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "荷物を持った手に汗が滲む。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "久しぶりの早足、いや、既に走り出している身体は、まだ風邪の余韻を残しているのか思ったように早くならない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（早く早く）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（……ペーターが、待っている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "風邪は治ったはずなのに、身体の中にはまだ熱が残っているように感じた。"

$ hi_mes()

scene map_bg_spring_day
with stripe_l_medium

scene charasel_bg_castle_day
with stripe_l_long

play music map_castle_ali
play sound se_0621
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……はっ、はあ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（さすがに息が切れてきた）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔からハートの城までは決して短い距離ではない。\n
それを全力疾走とまではいわないが、かなりの速さで走ってきたせいだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "額からぽたぽたと汗が滴ってきた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「でも、もうすぐ……、着く」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城の領土に入って街を抜けて。\n
薔薇の庭を最短コースで突っ切った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もうすぐ、城の門が見えてくる。"

$ hi_mes()

scene hm_spr_01
with dis

play music castle_mae_p_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「……[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「！」"

play sound se_0073
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞き慣れた声が私の名前を呼んでくる。\n
項垂れかけていた顔を上げれば、白く揺れるものが見えた。"


show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0131
Peter "「お帰りなさい！！\n
待っていました！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「ペーター……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（やっぱりここにいたの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "待っていてくれた。\n
それは確かに嬉しいことなのだが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（宰相がずっと城の門の前で待ち構えているのって……。\n
いいの、それで！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この城の軍事責任者にしても、旅に出てばかりで城に居着かない男だが。\n
宰相まで仕事を放り出してはまずいだろう、さすがに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……またキングに仕事が押し付けられているんだろうな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城の実情を知るメイドとしては複雑だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（嬉しそうな顔）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突っ込みたいところはいくつもあるが、あの顔を見ているとつい飲み込んでしまいそうになる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それではいけないのだと分かっているのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（私も、ペーターには絆されているわよね……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「ただいま……って、きゃっ！」"

hide per_t_02_13

play sound se_0553

show t_per_end1 onlayer master
with dis
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が言い終えるよりも先に、飛びついてきた白ウサギに押し倒されてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもなら舞った土埃に文句を言う潔癖症だというのに、ペーターには見えていないようだった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0132
Peter "「お帰りなさい、[firstname]。\n
ああ、やっと会えました！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0133
Peter "「大丈夫ですか？\n
どこか怪我なんてしていませんか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0134
Peter "「あなたがこんなに塔に長居するなんて……。\n
もしかして、ナイトメアから何か変な病気でも感染されて……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「……あのねえ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（怪我なら今まさにしかけたわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ため息をついた私を抱き締めながらペーターは弾んだ声で続けている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0135
Peter "「[firstname]、あなたは僕のすべて、僕の愛しい人。\n
あなたに何かあったら、僕は生きていけません！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "余程感極まっていたのだろうか、抱きつくことはあってもここまで堂々と押し倒してくるペーターは珍しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（綺麗好きのくせに、周りが見えていないのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも真っ白な髪は、私と一緒で薄く埃が付いてしまっている。\n
しかし、それを指摘するよりも切実な問題があった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「ペーター、重い……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今にも潰されると言うほどではないが、私よりも身長も体重もある彼にのし掛かられているのだ。\n
ずっとこのままの体勢ではさすがに辛い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_11")
T "（いい加減下りてよ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_11")
voice pet_f0136
Peter "「あなたは繊細なんですから、あんな病原菌が大量にありそうなところで生活してい……」"


scene bg_gen_sky_spr_day ##instant
hide t_per_end1

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "{size=+20}「重い！！」{/size}"

play sound se_0637
##anime
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉で言っても通じなかった相手に、とうとう私のほうが痺れを切らす。\n
遠慮できずに思いっきり振り切ったせいか、結構痛い音がした。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0137
Peter "「ぐはっ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0138
Peter "「な、何で急に殴るんです？\n
僕はあなたの身体を心配して……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「あんたが全身の体重をかけてのし掛かってくるからに決まっているでしょうが！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「重いのよ！\n
私を潰す気なの、あんたはっ！？」"


scene hm_spr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ようやく身体の上からペーターを下ろして、息をつく。\n
埃を払って立ち上がると、殴られた頬を押さえているペーターを見下ろした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "土の上にきちんと正座をしたペーターはしゅんと項垂れている。"


show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0139
Peter "「……すみません、[firstname]。\n
あなたが戻ってきたと思ったら、嬉しくて嬉しくてつい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「だからって全力で抱きつかないでよ。\n
打ち所が悪かったら、大怪我をするところだったじゃない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（頭でも打っていたら、怪我じゃすまなかったわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "風邪で寝込んだ挙げ句に、路上で押し倒されて意識不明では、あまりにもお粗末すぎる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ち込んでいるウサギを睨み付けると、彼は肩を落として弱々しい声で口を開いた。"

hide per_t_02_6
show per_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_01_13
show per_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0140
Peter "「本当にすみません。\n
あなたの顔を見たら、居ても立ってもいられなくて」"

hide per_t_01_8
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0141
Peter "「この前のように声だけではないことを確かめようと思ったら、触りたくなってしまいました」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……あ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（そういえば、あのとき、ペーターには私の姿は見えていなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "姿が見えていた私と違い、ペーターは私の声しか聞こえていなかった。\n
視覚と、聴覚。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "許された五感が一つ違うだけで、覚える不安感が違っていてもおかしくはない。\n
とは言うものの、素直には頷けないが。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「触るにしても、もう少しやり方があるでしょうが」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（空を飛んでくるのは、病弱な夢魔だけで結構よ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呆れたようにそう言うと、彼は少し困ったように首を傾げてみせた。\n
いつもの私を見る顔とは違う、どこか自虐的な笑い方だ。"

hide per_t_02_6
show per_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0142
Peter "「ただ触るだけでは……、安心なんて出来ません」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「ペーター？」"

hide per_t_03_4
show per_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice pet_f0143
Peter "「あなたに嫌われても、あなたのために僕は出来る限りのことをしたい。\n
でも、何をしたらあなたが喜ぶか、僕には分からないんです」"

hide per_t_03_5
show per_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice pet_f0144
Peter "「だから、どんな小さなことでもすぐ近くにいて、一番に感じ取れるようにしたい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何の前触れもなく私の手を取ったペーターは、そっと口を寄せた。\n
白いウサギの真っ赤な舌が、手に触れる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「や、やめなさいよ、泥で汚れているし……」"

hide per_t_02_11
show per_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice pet_f0145
Peter "「そうですね。\n
でも、触りたい」"

hide per_t_03_6
show per_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice pet_f0146
Peter "「手だけじゃ足りない。\n
唇で、目で、肌で、あなたのすべてを確かめたいと思っている……、僕はおかしいでしょうか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い瞳が私を見上げる。\n
うっとりと陶酔するような、そんな眼差しだ。"

hide per_t_03_11
show per_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0147
Peter "「あなたのことなら、誰より一番、知っておきたい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（熱を出していたのは、私のほうなのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "潤んだ真っ赤な目は、まるで彼が熱病に冒されているようにも見える。\n
燻るような、どんな名医でも、薬でも、消せない熱の色だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ペーター、そろそろ立ったら？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "放っておいたらいつまでも舐め続けていそうな相手に、そう言った。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_8")
T "（風邪、治ったはずなのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の顔に上る赤は、きっと今も鮮やかなままだろう。"

hide per_t_02_12
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0148
Peter "「でも……。\n
まだ、触り足りません」"

hide per_t_02_6
show per_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0149
Peter "「もっと触りたいのに……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "握ったままの私の手をじっと見つめるペーターは、不満そうだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「何もこんなところでいつまでも座り込んでいる必要はないでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……私も、あなたも汚れちゃっているし。\n
早くお風呂に入りましょう」"

play sound se_0492
hide per_t_01_13
show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pet_f0150
Peter "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚くペーターに構わず、思いっきり力を込めて引き上げる。\n
しかし私の力など必要なかったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飛び上がるように立ち上がった。"

hide per_t_02_3
show per_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0151
Peter "「[firstname]、今、お風呂にって……。\n
そ、それは僕と一緒にという意味ですよね、そうですよねっ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私のさりげなく告げた言葉を、彼は聞き逃していなかったのだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（いちいち確認しないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思いながらも、頷いてしまう自分が更に恥ずかしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「あんたが嫌なら一人で入る。\n
ペーターは、ここで座っているのが気に入っているみたいだし」"

play sound se_0051
camera at hpunch
camera at vpunch
hide per_t_01_3
show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice pet_f0152
Peter "「行きます、戻ります！\n
待ってくださいっ、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "立ち上がるや否や、勢い込んで彼は私に飛びついてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

hide per_t_02_5


scene bg_gen_sky_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ま、待ちなさい、ペーター！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（そんな勢いで飛びついたら、また！？）"

play sound se_0553
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "全力で飛びついてきたペーターがもう一回私を地面に押し倒したのは、言うまでもない。"

$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_long

scene charasel_bg_castle_day
with stripe_l_medium

scene hm_spr_01
with stripe_l_long

play music castle_garden_p_ali
play sound se_0046

show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_f0041
Ace "「やあ、お帰り、[firstname]。\n
君のほうが先に城に戻っていたなんて、意外だなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「そういうあなたは、旅から戻ってきたところかしら？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（また頭に葉っぱをくっつけて）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薔薇の生け垣を掻き分けながら現れたエースは、からっと笑っていた。\n
相変わらず、見た目だけなら他の追随を許さない爽やかさだ。"

hide ace_t_01_4
show ace_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0042
Ace "「う～ん、まあそんなところかな。\n
やっと城に戻ってきたから自分の部屋に行こうしていたところなんだけど、迷っちゃって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「まあ、あなたの場合はいつものことだけど……。\n
ひょっとして私が城を出て行っている間も外にいたの？」"

hide ace_t_03_1
show ace_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice ace_f0043
Ace "「うーん、どうかなあ。\n
少なくとも、かんかんに怒った陛下に君を連れ戻してこいと言われていたのは確かだけど」"

hide ace_t_02_6
show ace_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Ace "「…………」"

hide ace_t_02_10
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice ace_f0044
Ace "「でも、君はちゃんとここに戻ってきたんだね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見下ろしてくる赤い騎士は、感心したように言う。\n
まるで私が戻ってこないと思っていたような言い方だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「……どこにでも迷い込むあなたと一緒にしないで。\n
自分の家がどこなのか、分かっているもの」"

play sound se_0624
play sound se_0623
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "庭を抜けようとする私の後ろをエースはついてくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……どういう風の吹き回しかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "珍しいと思った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものようにいつのまにか横道に逸れるということもなく、まっすぐについてくるなんて。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースが誰かを連れ回すことはあっても、誰かの背後を静かに追うことは珍しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼にとって旅は自由なもので、道案内されるのもあまり好きではないらしいということも知っていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（その割に、あちこちで迷って道を聞いたりもしているみたいだけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（従う気はないわよね、いつものことながら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼が私の後を黙って付いてくる。\n
不思議というより、おかしな感じがした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_9")
T "「言っておくけど、私は城の外に行くのよ。\n
付いてきたら、また外へ逆戻りすることになるのが分かっているの、エース？」"

hide ace_t_03_3
show ace_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice ace_f0045
Ace "「え？\n
君、城の外に行く気だったのか？」"

hide ace_t_01_3
show ace_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice ace_f0046
Ace "「何だ、てっきりペーターさんのところに行くつもりだと思ったから、途中までついていこうと思ったのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "{size=+20}「思いっきり城に背中を向けているじゃない」{/size}"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（目は悪くないはずなのに、どうしてあの悪目立ちする城が見えないのよ、あんたは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後にそびえる城は大きく、赤い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私のこの世界での居場所。\n
だが彼にとってはまた別のものなのかもしれない。"

hide ace_t_03_7
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0047
Ace "「それに城の外にって……、何をしに行くんだ？\n
また家出？」"

hide ace_t_01_10
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0048
Ace "「ペーターさんと喧嘩でもした？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「違うわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（どうしてそういう発想になるんだか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エース以上に引っかき回す人を私は知らない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔から戻ってきて最初の休憩。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しばらく不在にしていた分を取り戻すべく仕事をしていたときには、まったく姿を見せなかったというのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターと顔を合わせるよりも早く彼に会ってしまったのは、予想外だった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（ペーターが来る前に出かけようと思ったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "わざわざ狙って現れたのではないかと思うような、実に嫌なタイミングである。"

hide ace_t_03_11
show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0049
Ace "「それじゃあ、この前みたいにどこかでいじけてくるの？\n
ははは、君って本当に後ろ向きだよなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「いじけてって……」"

hide ace_t_01_4
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice ace_f0050
Ace "「違うの？\n
俺はてっきりそうだと思ったんだけどな、はは」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（ああ、殴りたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかしこんな人の神経を逆撫でするような男でも、紛れもなく軍事責任者だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "簡単にあしらわれて、また爽やかな笑顔で馬鹿にしたようなことを言われるだけに決まっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「私がどこで何をしようが、あなたには関係がないことでしょう。\n
私には私の用事があるの」"

hide ace_t_03_3
show ace_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice ace_f0051
Ace "「うーん、それはそうなんだけど……。\n
言っただろう、俺、陛下から君を連れ戻すように言われているんだ」"

play sound se_0089
hide ace_t_02_8
show ace_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice ace_f0052
Ace "「だから、一度君を陛下の前に連れて行かないといけないと思わない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問答無用で抜刀してきたエースに、私は顔を引きつらせた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "{size=+20}「思わないわよ」{/size}"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "平静を装って答えたつもりだが、いつの間にか嫌な汗がじわりと滲んでいる。\n
突き付けられた刃が陽の光を弾いて、きらりと光った。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（これって、脅されているの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "軽々と剣を引き抜いたエースは切っ先を私に向けて、首を傾げて見せる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "雰囲気だけはいつもどおり爽やかなのに、圧迫感を感じさせる笑みを浮かべている。"

hide ace_t_02_1
show ace_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0053
Ace "「そんなことを言わないでさ。\n
陛下の機嫌が悪いんだから、一緒に怒られようぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「……屁理屈よ。\n
それに、もうビバルディにも会ってちゃんと謝ったし」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（それでも機嫌は悪かったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帰ってきた早々ペーターと一緒にお風呂に入る羽目になった私を、彼女は嘆かわしそうに見ていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だからそんなウサギはやめておけと言ったのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "溜息混じりに言われたその台詞は、彼女にしては最大級の哀れみが入っていたように思う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少なくとも、彼にここで剣を突き付けられて脅されなければならない理由はない。"

hide ace_t_03_7
show ace_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0054
Ace "「何だ、ずるいな、[firstname]。\n
抜け駆けなんて」"

hide ace_t_03_2
show ace_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0055
Ace "「それに、誘ったのに断られるなんて、男にとっては結構ショックなんだぜ？\n
ペーターさんとは夢でも会う仲なのに、俺だけ無視するなんて冷たいよなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「夢でも会うって……、それは一回だけで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「な、何でそれをあんたが知っているのよ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まだクローバーの塔に居候していたとき、夢の海に確かにペーターは現れた。\n
だが、そのことを知っているのは私とペーター、そして夢魔ぐらいだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（あのときのペーターがあの後、皆に吹聴して回るとは思えないんだけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、分からない。\n
ペーターなら、自慢げに語るかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（僕達はやっぱり心の奥底から結ばれているんです！\n
……とか何とか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、あのとき。\n
ナイトメアに対して泡にして消させるつもりかと問い詰めたペーターは、怒っているように見えた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼が喜んで話すようには思えないのだが。"

hide ace_t_01_8
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0056
Ace "「ははは、すごい大騒ぎだったんだぜ。\n
ペーターさんは、君を追いかけるって言って聞かないし、陛下は陛下で癇癪を起こすし」"

hide ace_t_03_3
show ace_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0057
Ace "「挙げ句に、俺に君を連れ戻せなんて命令をしてくるぐらいだからさ。\n
俺も城を追い出されちゃったんだぜ」"

hide ace_t_02_10
show ace_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0058
Ace "「どうせ追い出すなら、本気で追い出してくれればいいのに。\n
そうはしてくれないんだから、意地悪だよな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……エース？」"

play sound se_0492
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉の中に含まれた、何かの感情の欠片。\n
それにひっかかりを覚えた私を彼は難なく引き寄せた。"

hide ace_t_03_12
show ace_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0059
Ace "「あ、そうだ！\n
陛下のところに戻るのが嫌なら、俺と旅に出ようぜ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「は？」"

hide ace_t_01_13
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0060
Ace "「君は城に戻りたくなくて、どこかに行くところだったんだから、そのほうがいいだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「あんたね……。\n
先刻と言っていることが真逆じゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディのところに連れていくと言ったり、逆に旅に出ようと言ったり。\n
くるくる回ってばかり。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どっちが本心なのか、私には分からない。"

hide ace_t_03_10
show ace_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0061
Ace "「連れないなあ。\n
……っと！」"

hide ace_t_02_2


scene bg_gen_sky_spr_day
with dis
play sound se_0028
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0062
Ace "「ははは、危ないぜ、ペーターさん。\n
気付くのがちょっと遅れていたら、頭のど真ん中に風穴が開いていたじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0153
Peter "「当然でしょう。\n
その空っぽな頭をぶち抜いてやろうと思ったんですから」"


scene hn_spr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「ペ、ペーター」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつからそこにいたのか。\n
赤い城を背負うように、ペーターが立っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "発砲したばかりの銃口からは、まだ硝煙の煙がうっすらと立ち上っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（何で、あんたまでここにいるのよ！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここは城の外へと続く道だ。\n
仕事以外で出掛けたがらないペーターが現れるはずがないのに。"

play sound se_0023
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴたりと銃口をエースに向けたまま、ペーターは冷たい声で続ける。"


show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0154
Peter "「早くその手を離しなさい。\n
そんな汚れた手で触って、彼女に雑菌を付けないでください」"

hide per_t_02_7
show per_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0155
Peter "「君の雑菌に汚染されたら、そう簡単に落ちなくなってしまう。\n
彼女が君みたいな～～～～～～になったらどう責任をとるんです？」"

hide per_t_01_1
show per_t_01_1 at left
show ace_t_03_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0063
Ace "「酷いなあ、まるで俺がばい菌まみれみたいじゃないか。\n
結構これでもこまめに綺麗にしているのに」"

hide ace_t_03_8
show ace_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0064
Ace "「まあ、旅の途中で川とか、池に落ちることは多いけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "からからと笑う男の声に、白いウサギは耳を傾けなかった。"

hide per_t_01_1
show per_t_02_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0156
Peter "「エース君」"

play sound se_0515
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃を突き付けたまま、ペーターはエースを睨んだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その指は引き金にかけたままだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の住人は誰彼構わず引き金を簡単に引き、命の扱いが軽い。\n ・
特に、ペーターは一・二を争うほどの速さだったはずだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（……少しは銃を連発するなって言った言葉、効果があったのかしら）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ペーター……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_3")
T "（繰り返し言い聞かせてきた意味はあったのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただ、問題は向かい合っているのがエースだということだ。"

play sound se_0093
hide ace_t_02_8
show ace_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0065
Ace "「いいよ、ペーターさん。\n
彼女の代わりに、俺と遊んでくれる？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ちょ、ちょっと、やめなさいよ、あんた達！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターとエースがじゃれ合う（？）のはいつものことだが、何だか今はまずい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（ペーターの機嫌が悪いのは何となく分かるけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（何だかエースにも、棘がない？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段から掴み所のないエースだが、あまり刺激したくない空気を漂わせているような気がした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T "（ビバルディからの命令がどうのって言っていたあたりから、ちょっとおかしかったけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（いや、元々エースはおかしいんだけど、いつもとは何かが違うというか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "このままではいけない。\n
そして、こういう悪い予感はまず外れないものだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「ペーター！\n
もういいでしょうっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の制止を彼らのうちどちらがより聞き入れてくれるか。\n
それを考えれば、ペーターを止めるしか私には方法がなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の声にペーターは僅かに顔をしかめたが、反論はしない。\n
渋々といった体ではあったが、銃口を下ろしてくれた。"

hide per_t_02_9
show per_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

play sound se_0512
hide per_t_02_11
show per_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0157
Peter "「はあ……、分かりました。\n
命拾いしましたね、エース君」"

hide per_t_03_9
show per_t_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0158
Peter "「彼女に感謝してください。\n
僕としてもいい加減、君のその軽そうな頭を吹き飛ばしたくて仕方ないんですから」"

hide ace_t_03_11
show ace_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0066
Ace "「あれ、やらないの？\n
楽しそうだったのになあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃を時計に戻したペーターはエースの軽口は無視して、私のほうへとやって来る。"

hide per_t_02_7
show per_t_01_12 at center
hide ace_t_01_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「な、なに？」"

hide per_t_01_12
show per_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice pet_f0159
Peter "「他の場所へ出かけるなとは言いません。\n
でも、せめて……、出かけるのなら一言僕に言ってください」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「だって、そんなことを言ったら、ペーターもついてくるでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "余所者とはいえ、メイドの一人にすぎない私と違って、彼には立場がある。\n
今までにも私の供を買って出て仕事をすっぽかしたことだってある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（ただでさえ、上司と同僚がああなんだから、これ以上迷惑をかけるわけにはいかないでしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターの負担をこれ以上増やしたくはなかった。"

hide per_t_01_8
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0160
Peter "「……待っていますよ。\n
あなたがそうしてほしいのなら、いつまでも」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想外の言葉に、間の抜けた声が出てしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ペーター、今、なんて……」"

hide per_t_02_8
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice pet_f0161
Peter "「待つと言ったんですよ。\n
[firstname]、あなたが待っていてほしいなら、僕はいつまでだって待っています」"

hide per_t_03_1
show per_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice pet_f0162
Peter "「何百時間帯でも、何千時間帯でも。\n
あなたが僕の傍に戻ってきてくれるのなら」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "{size=+20}「頭でも打ったの、ペーター\n
！？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず漏れた本音に、ペーターはかくんと体勢を乱した。"

hide per_t_02_12
show per_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0163
Peter "「な……、何でそう言うことになるんですか！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「だって、ペーターがそんなまともなことを言うなんて思わなかったから」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（驚くのも当然でしょう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までどこへ行くにもついていくと言い張っていたペーターが、どういった風の吹き回しなのだろう。"

hide per_t_01_5
show per_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_01_13
show per_t_01_13 at left
show ace_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0067
Ace "「ははは、さすがだよ。\n
ペーターさんのことをよく分かっているよなあ」"

hide ace_t_01_4
show ace_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0068
Ace "「首輪なんかなくても、充分すぎるほど飼い慣らしちゃっている。\n
君って猛獣使いの素質があるんじゃないのか、[firstname]」"

hide per_t_01_13
show per_t_01_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0164
Peter "「エース君！！」"

play sound se_0023
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「……ペーター？」"

hide per_t_01_7
show per_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
Peter "「…………」"

play sound se_0512
hide per_t_02_6
show per_t_03_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice pet_f0165
Peter "「分かりました、撃ちません。\n
我慢……、します」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「よろしい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃を再び時計に戻したペーターに笑いかけて、私はその手を掴んだ。"

hide per_t_03_5
show per_t_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「？\n
[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あのね、ペーター。\n
私は、外に出掛けたいの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「一緒に来てくれる？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不思議そうに見返す眼差しに、わざとらしくねだる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのときには合わせることも難しかった視線がすぐに合った。\n
ただそれだけのことが、当たり前のことが嬉しい。"

hide per_t_02_3
show per_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「！！！」"

hide per_t_01_3
show per_t_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0166
Peter "「ぼ、僕も今度は一緒に行っていいんですか？\n
ついていっていいんですか、[firstname]！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（出かけるときには言えって、今自分で言ったばっかりでしょう）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「いいわよ。\n
そうじゃなかったらわざわざ誘ったりなんかしないわ」"

hide per_t_01_2
show per_t_02_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
Peter "「！」"

hide per_t_02_12
show per_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice pet_f0167
Peter "「行きます、どこに行けばいいんですか？\n
今度は本物の海ですか？」"

hide per_t_03_11
show per_t_02_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice pet_f0168
Peter "「それとも……、ああ、でもどこでもお供します！\n
あなたがいる場所なら、どこにでもっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（嬉しそうな顔）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただ外に出かけようと誘っただけ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも、ペーターに待っていてと約束したときよりも、ずっとずっと嬉しそうな顔を見せてくれる。"

hide ace_t_03_3
show ace_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0069
Ace "「へえ、やっぱり……、君って猛獣使いだね」"

hide ace_t_03_2
show ace_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0070
Ace "「飴と鞭の使い方が、うまい。\n
今度俺にもコツを教えてよ、[firstname]」"

hide per_t_02_13
show per_t_02_13 at center
hide ace_t_02_4
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつの間にか剣を鞘に戻したエースはそんなことを言いながら、私の横を抜けていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "からっと爽やかに、そして……、本心の見えない笑みだけを残して。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（一体何だったんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこか不機嫌そうなエースは久しぶりだ。\n ・
エイプリル・シーズン以降もユリウスがいるせいか、落ち着いていたはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（何がそんなに面白くなかったんだろう）"

hide per_t_02_13
show per_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice pet_f0169
Peter "「[firstname]、[firstname]。\n
それで、どこに行きたいんですか？」"

hide per_t_01_2
show per_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice pet_f0170
Peter "「どこにでもお供しますよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴこぴこと立てた耳を揺らしながら、ペーターは声を弾ませている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（これも確かに、『猛獣』と言えなくはないのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃を持ち歩いているだけではなく、ペーターというウサギの性質は草食動物とはまったくの別物だ。"

hide per_t_02_1
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「うん、じゃあ一緒についてきて」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（私は、こんなことを言うような人間じゃなかったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を無条件で寄りかからせる雰囲気は、猛獣の牙や爪よりも、もっと怖いもの。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飴と鞭を使い慣れているのは、むしろこの白い生き物なのかもしれない。"

hide per_t_03_1

play sound se_0624
play sound se_0623
$ hi_mes()

scene hm_spr_01
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium

play music forest_town_road_p_ali

scene bg_gen_sky_win_day
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0171
Peter "「どこへ行くのかと思えば、クローバーの塔ですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ。\n
この前ずいぶんお世話になったから、せめてお見舞いぐらい行こうと思って」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（それに、風邪を感染しちゃったのも事実だし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターにはその辺りの事情は伏せている。\n
風邪をひいて寝込んでいたことも、話していない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ばれたりしたら大騒ぎになるから、その辺りはグレイ達にも黙っていてもらったほうがいいだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ、ちょっと待ってね」"

play sound se_0113

play music forest_town_square_p_ali

scene mm2_win_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまままっすぐに塔に向かう足を止めて、近くの店に顔を出す。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「すいません。\n
お花をお願いしたいんですけど」"


show flower_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice oda_f0009
Clerk "「いらっしゃいませ……、ああ、あなたですか。\n
いつもご贔屓にしてくださってありがとうございます」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔の領土内にある花屋。\n
何度か立ち寄ったことのある店員に声をかけると、彼女は手入れの手を止めてやってきた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「こんにちは。\n
お見舞いに行くのに、少し花を包んでもらえたらと思って」"

hide flower_1
show flower_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice oda_f0010
Clerk "「分かりました。\n
どんなものがいいですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「そうねえ……。\n
ペーターはどんなのが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「……ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "花屋の前には色とりどりの花が並んでいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目移りしそうなほどの量を見つめながら隣を見ると、ペーターは先ほどまでの上機嫌さが嘘のようにむっとした顔でそこにいた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（何をふくれた顔をしているのよ）"

hide flower_3
show flower_3 at left
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pet_f0172
Peter "「……不満です」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「は？」"

hide per_t_02_7
show per_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice pet_f0173
Peter "「納得出来ません！\n
どうして、どうしてあなたがあの～～～～～～～～夢魔にお見舞いの品なんて差し入れをするんですか！？」"

play sound se_0073
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "文字通り地団駄踏んでいるペーターは、何も知らない店員を睨む。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を見るときには煮詰められたジャムのようになっている目が、冷えた紅玉に変わっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぞっとするほどの敵意は、彼女も充分感じたらしい。"

hide flower_3
show flower_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oda_f0011
Clerk "「え……、ええと。\n
あの……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「あ、この人は気にしないでいいので。\n
普通に包んでください、普通に」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（善良な花屋さんを脅すんじゃないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隣に立つペーターをぎりっと睨み付けるが、彼はまだぶつぶつと口を尖らせている。"

hide per_t_01_1
show per_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0174
Peter "「それも、あなたから花をもらうなんて……。\n
ずるいです、許せません」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_15")
T "「ペーター、言っておくけど。\n
あんたに持たせたその果物もお見舞いの品だから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「潰したり、落としたり、投げたりしたら……。\n
もう二度と一緒になんて出かけないからね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここに来るまでに買った品物は、背後でぶつぶつ言い続けている彼が持っている。\n
万が一にも八つ当たりしないように釘を刺した。"

hide per_t_01_9
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_02_7
show per_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0175
Peter "「[firstname]、あなた……。\n
背中にも目があるんですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "{size=+20}「あるわけがないでしょうが」{/size}"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（どうしてこういうときだけ予想通りなのかしらね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ますます顔を引きつらせる花屋さんに曖昧に笑っている私の背後で、ペーターの落胆した声が聞こえた。"

hide per_t_03_3
show per_t_03_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0176
Peter "「だって……、あなたから何かを贈られるなんて、そんなこと許せません。\n
果物だろうが、服だろうが、路傍の石だろうが」"

hide per_t_03_5
show per_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0177
Peter "「あなたからプレゼントをもらうなんて、そんなこと……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（背中に目はないけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（何となくどんな顔をしているか分かってしまうあたり、伊達に付き合いが長くないというか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り返ったらきっと絆されてしまう。\n
それが分かるからこそ、振り返ることは出来ない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "外してほしい予想ほど外してくれないあたり、困ったウサギである。"

play sound se_0494
hide flower_2
show flower_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oda_f0012
Clerk "「あの……、こんな感じでいかがでしょうか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐る恐る差し出された花束を受け取ると、柔らかな香りがした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「ええ、ありがとう。\n
綺麗」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（背後に物騒なウサギがいるのに、仕事はきちんとしてくれるあたり、さすがはプロ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを思いながら代金を手早く渡した。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他のお見舞いの品もそうだが、早くすませてしまわないとペーターが払うと言い張るのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（ナイトメアへの見舞いだって知っていても、押し切られかねない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だがこれはあくまで私がお世話になったお礼。\n
自分で払わなければけじめが付かない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（本当に面倒な性格をしているわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呆れていると、いつの間にか隣で静かにしているペーターが気になった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の視線の先を見て、私の顔が引きつる。"


show t_per_end2 onlayer master
hide flower_1

hide per_t_02_6
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0178
Peter "「……あの夢魔に贈るのなら、どうせならあの花にでもすればいいのに。\n
あれでよければ、僕が箱詰めにして贈ってあげますよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「不吉なことを言うんじゃない！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（よくは知らないけど……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（あれって確か、献花用）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただでさえ寝込みがちな病人に間違っても贈っていいものではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（相手は、常時血を吐くのが当たり前の病弱夢魔なんだから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あんなものを贈ったら、見ただけでダメージを受けてしまう。"

$ hi_mes()
hide t_per_end2


scene mm2_win_01
with stripe_l_medium

scene co_01
with stripe_l_long

play music tower_inside_p_ali

show gre_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0058
Gray "「[firstname]。\n
それに……、珍しいな、白ウサギ」"

hide gre_t_01_12
show gre_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0059
Gray "「おまえが塔に来るとはどういう用件だ。\n
女王から何か……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔には幾つもの部屋がある。\n
その中でも比較的大きな一室で、私達はグレイと顔を合わせていた。"

hide gre_t_03_7
show gre_t_03_7 at left
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0179
Peter "「僕だって好き好んで来たわけじゃありま」"

play sound se_0716
## anime hit right
hide per_t_02_7
show per_t_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0180
Peter "「～～～～っ！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_11")
T "（会って早々にいらない手間を掛けさせないでよっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "余計なことを言おうとしたウサギの顔に軽く一発お見舞いして、私は話を逸らした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「ね、ねえ、グレイ。\n
ナイトメアの具合はどう？」"

hide gre_t_03_7
show gre_t_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice gra_f0060
Gray "「あ、ああ。\n
あの方はまあいつもどおりなんだが……」"

hide gre_t_01_6
show gre_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice gra_f0061
Gray "「白ウサギのほうは、いいのか？\n
声も出ていないようだが」"

hide gre_t_03_11

hide per_t_01_6
show per_t_01_6 at left
show yuri_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice jul_f0034
Julius "「見事に鳩尾に決まっていたからな。\n
まったく、ペーター＝ホワイトらしくもない、油断しすぎだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔の談話室。\n
珍しく仕事部屋から出てきていたユリウスと、仕事の資料を抱えたグレイがそこにいた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "病弱でも、ナイトメアはこの塔の主だ。\n
私一人で来る分には問題はないが、ハートの城の宰相付きともなれば、グレイに断っておくのが筋というもの。"

hide per_t_01_6
show per_t_01_15 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0181
Peter "「ふっ……、羨ましいでしょう？\n
ここまで遠慮なく殴ってもらえるのは、彼女の信頼の証」"

hide per_t_01_15
show per_t_02_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0182
Peter "「そう、これが僕達の愛情表現なんです\n
！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T "（……どんな愛情表現だ、それは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "歪むどころか、明らかに方向性を間違えているとしか思えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターの言葉にグレイは困ったように聞き返してきた。"

hide per_t_02_13

hide yuri_t_01_3
show yuri_t_01_3 at left
show gre_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0062
Gray "「……そうなのか？」"

hide yuri_t_01_3
show yuri_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0035
Julius "「そんなはずがないだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「当たり前でしょう！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「ペーター！\n
{size=+20}盛大に誤解を招くような発言をするんじゃない！{/size}」"

play sound se_0444
##anime hit

show per_t_01_5 at center
hide yuri_t_03_4
hide gre_t_02_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice pet_f0183
Peter "「がふっ」"

hide per_t_01_5
show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice pet_f0184
Peter "「もう……、[firstname]、あなたが照れ屋なのは分かりますが、もう少し手を抜いても」"

play sound se_0716
camera at hpunch
camera at vpunch
hide per_t_02_13
show per_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice pet_f0185
Peter "「ぐふ！」"

play sound se_0393
camera at hpunch
camera at vpunch
hide per_t_01_4
show per_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice pet_f0186
Peter "「げはあっ！」"

play sound se_0553
hide per_t_01_6

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「まったく……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふざけた発言を繰り返す白ウサギがへたりと崩れ落ちたとき、背後から微妙な視線を感じた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私とペーターのやりとりを見ていた二人の男性は、それぞれ別の反応をしている。"


show gre_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

hide gre_t_03_2
show gre_t_03_2 at left
show yuri_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

hide yuri_t_01_3
show yuri_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0036
Julius "「はあ、どつき漫才をしたいなら自分のところでやれ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイはなんと言っていいのか分からず、ユリウスは完全に呆れ返っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（べ、べつに、いつもいつもこんなことをしているわけじゃないのよ！\n
……そんなにしょっちゅうは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "微妙な空気をごまかすように、声を上げた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「それはそうと……。\n
そうよ、ナイトメアの具合なんだけど、まだ寝込んでいるの？」"

hide gre_t_03_2
show gre_t_02_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice gra_f0063
Gray "「まだというか、またというべきか悩むところだが……。\n
部屋で休まれている」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「熱は？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（あの風邪、熱が高く出るから体力を消耗するし。\n
質が悪いわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私もかかったひとりだから、辛さはよく分かる。"

hide gre_t_02_12
show gre_t_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0064
Gray "「ああ、もう心配はいらない。\n
氷枕も氷嚢ももうたくさんだと、この前投げ返されたぐらいだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイの様子からは、私が帰ってから悪化はしていないらしい。\n
だが、まだ休んでいるということは、体調不良は続いているということだろう。"

hide yuri_t_03_11
show yuri_t_01_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0037
Julius "「ほとんど下がっているが……、元々体力のない病人だからな。\n
なかなか床上げには至らないらしい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「そう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（顔を見に行ったら迷惑かしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お見舞いに来たつもりだったが、体力のないナイトメアをますます疲れさせるだけだろうか。"

hide gre_t_02_2
show gre_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0065
Gray "「花束に、果物の籠ということは……。\n
[firstname]、君はナイトメア様を見舞ってくれたのか？」"

hide gre_t_03_10
show gre_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0066
Gray "「君自身もまだ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "労るような眼差しを向けてくれるグレイには悪いが、その続きを口にさせるわけにはいかなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「いいの、いいの。\n
あれだけ長居させてもらったのに、最後にちゃんと挨拶も出来なかったから顔を見に来ただけで」"

hide gre_t_01_10

hide yuri_t_01_12
show yuri_t_01_12 at left
show per_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
Peter "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "復活したペーターが問いかけるような目で私を見てくるが、その視線をわざと無視する。問い詰められたら、うまく誤魔化せる自信がない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（危ない、危ない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ただでさえ病人を抱えている場所で、怪我人を出すわけにはいかないものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "発端が城での水事件だとしても、ペーターのことだ。\n
ここの人達にどんな言い掛かりを付けることか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「すぐ帰るから、顔を見るぐらいなら行ってもいいかしら？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の確認に、ナイトメアの状態を一番分かっている彼は大きく頷いてくれた "

hide yuri_t_01_12

hide per_t_02_9
show per_t_02_9 at left
show gre_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0067
Gray "「勿論だ、君の見舞いを勝手に断ったと言ったら、ナイトメア様に後で恨まれる」"

hide gre_t_01_11
show gre_t_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0068
Gray "「ぜひ、会いに行ってくれ」"

hide per_t_02_9
show per_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0187
Peter "「僕も一緒に行きます。\n
構いませんね、グレイ＝リングマーク」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？\n
ペーターも？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が城からついてきたことには驚かなかったが、まさかそこまで付き合うとは思っていなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（ナイトメアに会いたそうにも見えなかったんだけど？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターの提案を意外に感じたのは、私だけではなかったらしい。\n
グレイも真意を問うようにじっと睨み返している。"

hide gre_t_03_4
show gre_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0069
Gray "「おまえが？\n
面会は構わないが……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイの言葉にこもる温度が僅かに下がったように感じた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はナイトメアの護衛も兼任している。\n
危害を加える恐れがあるものを無闇に近付けるわけにはいかないと考えているはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その意図はペーターにも伝わっている。\n
自分には敵意はないというように肩を竦めてみせた。"

hide per_t_03_10
show per_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0188
Peter "「僕は、彼女と一緒にいるだけです。\n
何もしません」"

hide per_t_02_4
show per_t_01_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0189
Peter "「しようとしたところで、ここは夢魔の領土でしょう。\n
夢ほど確かな領土ではありませんが、分が悪い手出しをする気はありません」"

hide gre_t_01_9
show gre_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0070
Gray "「分かっているならいい。\n
俺も、彼女の前でおまえに斬りつけるのはあまり気乗りがしない」"

hide per_t_01_12
show per_t_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_02_7
show per_t_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0190
Peter "「行きましょう、[firstname]。\n
彼にはこの前の悪趣味な夢についてきちんと話をしなければと思っていたんです」"

hide per_t_03_1

hide gre_t_03_7

play sound se_0774

scene cr_01 with stripe_l_short
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「……悪趣味な夢？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（それって、この前の海の夢のこと？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、どうしてそれが今、問題になるのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城に戻ってから彼があの夢のことを口にしたことはなかった。\n
私もたいして気にしていなかったのだが。"

play sound se_0384
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（どういうこと？）"


show per_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先を進んでいる背中に問いかけるが、彼から返事が返ることはなかった。"

hide per_t_01_12

$ hi_mes()
$ hi_mes()

$ time_effect()

play music tower_corridor_p_ali
play sound se_0300
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_14")
T "「……ナイトメア？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（寝ているのかしら）"

play sound se_0300
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もう一度ノックを繰り返したが、室内からは何の反応もない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の場合眠りにつくときには、身体ごと夢の中に引きこもってしまうことがほとんどだと聞いたことがある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今回も同じようにこもってしまっているのだとしたら、空振りと言うことになるが。"


show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_02_10
show per_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0191
Peter "「入りますよ、ナイトメア」"

hide per_t_03_10

play sound se_0285

play music tower_stairs_up_p_ali

scene n_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の後ろにいたはずのペーターが一歩前に出たかと思えば、彼は躊躇いなくドアを開けてしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ペ、ペーター！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（な、何をいきなりドアを開けているのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相手は病弱で、血を吐いて倒れる夢魔とは言え、ここの領主だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "せめて返事を待ってからと思ったのだが、ペーターは勝手にずんずんと中に入ってしまう。"


show nai_s_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0181
Nightmare "「……ふ。\n
これはまたずいぶんと気の短い来客だ」"

hide nai_s_02_11
show nai_s_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0182
Nightmare "「君にしては気の短い話じゃないか、白ウサギ。\n
エリオットに似てきたか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "室内に響く声は、私のよく知るものだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（声が掠れていないってことは、喉の腫れはもう引いたみたいね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの体調がよくなっていたことに、少しほっとした。"

hide nai_s_03_1
show nai_s_03_1 at left
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0192
Peter "「冗談はやめてください、誰があんな～～～～～～に似てきたなんて……。\n
侮辱以外の何ものでもありません」"

hide per_t_02_7
show per_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0193
Peter "「それに、いるなら返事ぐらいしてください。\n
見舞いに来た客に対して失礼でしょう」"

hide per_t_02_11
show per_t_01_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0194
Peter "「残念なことに、元気そうですし」"

hide nai_s_03_1
show nai_s_03_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0183
Nightmare "「心の底から残念そうに言うな、聞こえているぞ！\n
まったく、病人の見舞いに来たという割に図々しいウサギだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「本当に、元気そうね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（ベッドから動けないことを除けば）"

hide nai_s_03_8
show nai_s_02_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0184
Nightmare "「そう言わないでくれ。\n
……精神的にはかなり回復したんだが、まだちょっと体が辛くてね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうは言うものの、広い私室に備え付けられたベッドの上で呻いているナイトメアは、私が最後に見たときよりも大分元気そうだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（顔色の具合もいつもどおりだし……。\n
まあナイトメアらしいといえばナイトメアらしいか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベッドの上で踏ん反り返る必要がどこにあるのかは分からないが、彼がこういうことに力を入れるのはいつものことだ。"

play sound se_0307
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その病人の枕元にまで詰め寄ると、ペーターはずっと持ったままだった籠を押し付けた。"

hide per_t_01_14
show per_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0195
Peter "「見舞いの品です。\n
彼女が、わざわざ、あなたのために、持ってきたんですよ」"

hide per_t_02_9
show per_t_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0196
Peter "「神棚に飾って、毎時間帯拝みなさい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「……ペーター」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（ただの果物と花でしょうが）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どんな理不尽な宗教絡みの規則でもそこまでは求めないだろうに。"

hide per_t_03_9
show per_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0197
Peter "「当たり前じゃないですか、[firstname]！\n
僕だったら、毎時間帯といわず、常に拝みますよ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（この～～～～～～～～）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少しはマシになったが、ペーターの言動が暴走するのもいつものことだ。"

hide nai_s_02_9
show nai_s_01_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0185
Nightmare "「何というか……、君も、大分免疫が付いたな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「おかげさまで。\n
自分の適応力の強さに感謝しているわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（ううん、本当はそう言えるほど適応なんてしていない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "胸の奥には、今も棘が残っている。"

hide per_t_02_3
show per_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0198
Peter "「ちょうどいい、あなたに聞かなければならないことがあるんです。\n
ナイトメア」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私と彼の間に割り込んできたペーターはそう切りだした。"

hide nai_s_01_12
show nai_s_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0186
Nightmare "「何だ？」"

hide per_t_01_11
show per_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0199
Peter "「あなたなら、わざわざ聞かなくても聞こえているでしょう。\n
答えてください」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心を読める夢魔ならそれも当然のことだが、彼は曖昧に口元をあげて見せた。"

hide nai_s_02_3
show nai_s_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0187
Nightmare "「ふふ、そうだな。\n
私には確かに聞こえているが」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは私のほうに意味ありげな視線を向けた。"

hide nai_s_03_1
show nai_s_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0188
Nightmare "「彼女には聞こえていない。\n
当事者を除け者にするのはよくないだろう」"

hide per_t_01_4
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターは言うことを躊躇っているようだが、私には大体見当がついていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ペーターが聞きたいことって、あの絵本のこと？」"

hide per_t_02_7
show per_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pet_f0200
Peter "「絵本？\n
それがあの悪趣味な夢の元凶ですか？」"

hide nai_s_02_4
show nai_s_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nig_f0189
Nightmare "「悪趣味、悪趣味と酷いな、白ウサギ。\n
彼女は結構楽しんでいてくれたのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは同意を求めるように私を見てくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……そうね、悪いものばかりじゃなかったわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "美しい深海の世界。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "写真で見るよりもずっと深い青。\n
溶けていく泡。\n
そして……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（……なんで、姉さんの声が聞こえたのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの世界をペーターは私の深層意識だと言っていたが、どうしてあの人の声が遠くで響いていたのかは分からない。"

hide nai_s_01_4
show nai_s_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0190
Nightmare "「ほら、私の言ったとおりだろう？\n
なかなか海になど連れて行ってやれないからな」"

hide nai_s_02_3
show nai_s_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0191
Nightmare "「現実であんな深い場所に連れていったら、それこそ本当の意味で人魚姫の仲間入りだ。\n
夢だからこそ出来る業だよ」"

hide per_t_03_3
show per_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0201
Peter "「なら質問を変えます。\n
どうして、人魚姫だったんです？」"

hide per_t_02_11
show per_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0202
Peter "「童話なら他にいくらでもあるでしょう。\n
よりにもよって、泡になって消えるものを選ぶ必要がどこにあったというんですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（やけにしつこいわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人魚姫の結末はこの世界でも変わらないのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "地上の王子に心を惹かれた人魚姫。\n
声を失った彼女は、想いを伝えきれないまま、最後の選択を迫られる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "王子の命と引き替えに、人魚に戻るのか。\n
海の泡になって消えるのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、物語の最後、彼女は泡になることを選び、何も残さぬまま消えていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（報われない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供の頃に読んだときには、王子の薄情さに不条理さを覚えたものだ。"

hide nai_s_03_10
show nai_s_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0192
Nightmare "「ペーター＝ホワイト。\n
……君なら、どうする？」"

hide per_t_01_11
show per_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然の問いかけに白ウサギは訝しげに目を細めている。"

hide nai_s_02_4
show nai_s_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0193
Nightmare "「仮に君が溺れて、救ってくれた彼女がすべてを捨てても会いに来てくれたら、どうする？\n
嬉しいのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ナイトメア？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアがどんな意図で、そんな質問をするのかが分からない。\n
しかし、ペーターは真剣に答えを考えているようだった。"

hide per_t_01_4
show per_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide nai_s_03_10
show nai_s_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0194
Nightmare "「本来の場所にいたら、幸せになれたかもしれない。\n
だが、それをすべて捨てて、それでも君に会いたいと彼女が願ったら……」"

hide nai_s_03_1
show nai_s_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0195
Nightmare "「どうする？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉こそ単純なものだが、そこに込められた内容は複雑なのだろうか。\n
私に関することならいつでも即答するペーターが、沈黙するなど余程のことだ。"

hide per_t_02_4
show per_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_02_11
show per_t_03_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0203
Peter "「分かりません」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "長い沈黙の末。\n
絞り出すように告げた言葉は、短く、重かった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（ペーター）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い目が酷く哀しげに、私を見てくる。"

hide per_t_03_5
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0204
Peter "「……離したくないんです。\n
幸せにしたいと思うのと同じぐらい、僕は彼女を手放したくない」"

hide nai_s_02_4
show nai_s_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

hide nai_s_01_11
show nai_s_02_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0196
Nightmare "「それでいいさ。\n
[firstname]」"

play sound se_0720
show t_per2_1and_end3 onlayer master
with dis
hide per_t_02_7

hide nai_s_02_12

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこから取り出したのか。\n
ナイトメアは、見覚えのある本を私に差し出してきた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「これ……、あの絵本？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nig_f0197
Nightmare "「ああ。\n
君にあげるよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nig_f0198
Nightmare "「城に戻ったら、彼と一緒に読んでごらん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"

hide t_per2_1and_end3

play sound se_0718
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「読めないままなんだけど？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（相変わらずミミズがのたくったような文字……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手渡してくるぐらいだから、読めるものになっているかと思ったのに。\n
中身は、最初に見せてもらったときと同じだった。"


show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0199
Nightmare "「ああ、ここでは読めないようにしているからね。\n
忘れたのか、ここは私の領域だ」"

hide nai_s_01_11
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0200
Nightmare "「城に戻れば、白ウサギのほうが優位になる。\n
そうしたら、もう一度開いてみればいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「……？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（まるで内容が変わるように言うけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "絵本は、もう完成されている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "物語の始めと終わりは、私の手に預けられる前にもう出来上がっているものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが本。\n
完成したものには、誰も、何も、加えることは出来ないし、変えられない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（場所によって中身が変わる本なんて、本って言えるの？）"

hide nai_s_02_1
show nai_s_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice nig_f0201
Nightmare "「疑り深いな。\n
……ペーター＝ホワイト」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の心の声に苦笑したナイトメアは、沈黙したままのペーターを呼んだ。"

hide nai_s_03_6
show nai_s_03_6 at left
show per_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0205
Peter "「何ですか？」"

hide nai_s_03_6
show nai_s_02_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0202
Nightmare "「そう警戒しないでくれ。\n
病み上がりの病人に殺気は結構堪えるんだぞ」"

hide per_t_01_9
show per_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0206
Peter "「万年病人のあなたに、病み上がりじゃないときがあったとは知りませんでした」"

hide nai_s_02_9
show nai_s_01_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0203
Nightmare "「余計な茶々を入れるんじゃない！\n
……うう、大きな声を出したら、急に気分が」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「……あのねえ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ミステリアスになったり、病人になったり……。\n
忙しい人）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ち着きがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（グレイ達、本当に苦労しているものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "寝込む前には塔で普通に過ごしていたのだ。\n
この主に部下達が振り回されているのは、私も何度も目の辺りにしていた。"

hide nai_s_01_7
show nai_s_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0204
Nightmare "「少しは心配してくれればいいのに。\n
はあ……、私は疲れた、君の見舞いの花でも見て、心を癒すとしよう」"

play sound se_0750
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "嘆くように言って、ナイトメアはごろんと寝返りを打った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベッドの向こうにある顔がどんな表情を浮かべているのか、心が読めない私にはもう分からない。"

hide nai_s_01_4
show nai_s_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0205
Nightmare "「ほらほら、君達もいつまでも病人の部屋に長居するんじゃない。\n
感染っても知らないぞ？」"

hide nai_s_02_11
show nai_s_03_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0206
Nightmare "「ごほ、ごほんっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "わざとらしい咳払い。\n
本当に調子が悪いときとは違っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（本当にいつも通り）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "体調を理由に人を煙に巻くあたり、彼らしい。"

hide per_t_02_2
show per_t_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「！！」"

hide per_t_01_5
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0207
Peter "「[firstname]、行きましょう」"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし平然としていられたのは私だけだったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "がしっと私の手を掴んだペーターは、颯爽と部屋の入り口に向かって歩き出している。"

hide per_t_02_7
show per_t_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0208
Peter "「早くこんな部屋から出て、消毒しなければあなたに変な病気が感染ってしまいます！～～～～とか、あまつさえ～～～～～～なことになってしまったら、僕は！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（どれだけ突然変異を起こせば、風邪がそこまでグレードアップ出来るのよ）"

hide nai_s_03_13
show nai_s_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Nightmare "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦笑いするような声に引かれて、振り返る。\n
ベッドの上で色素の薄い夢魔は、手を振っていた。"

hide nai_s_03_11
show nai_s_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0207
Nightmare "「地上に残り続けるのが幸せとは限らない。\n
中には、一緒に海に行くことを願う王子だっているかもしれないだろう」"

hide nai_s_02_11
show nai_s_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0208
Nightmare "「……泡にも、人にもならない。\n
そんな人魚姫を、私は応援するよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ナイトメア？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問いかけの声は夢魔の元に届いていたのだろうが、彼は笑ってばかりで応えようとしなかった。"

hide nai_s_01_6

hide per_t_01_7

$ hi_mes()

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium

scene hm_spr_01
with stripe_l_medium

scene p_01
with stripe_l_long

play music peter_t_ali

show per_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0209
Peter "「すぐに浴槽の準備をしますから、待っていてくださいね！\n
消毒薬も出しておきますから、雑菌を始末しないとっ！」"

play sound se_0591
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（城に戻った早々何を言い出すかと思えば）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問答無用でペーターの部屋まで連れてこられたかと思ったら、彼は奧の浴室へと飛んでいった。"

play sound se_0699
play sound se_0094
hide per_t_01_5
show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0210
Peter "「[firstname]、もうすぐ準備が出来ますからっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「はあ。\n
別にそんなに急がなくていいのに」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（雑菌が心配なのは、むしろあんたのほうじゃないの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "汚いことが嫌なのは私も同感だが、ペーターほど極端ではない。\n
しかし、彼には私の衛生管理が最優先のようだ。"

hide per_t_02_7
show per_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0211
Peter "「あなたが風邪をひいたりしたら大変です！\n
身体の芯から温まって、悪いものはすべて落とさないと」"

play sound se_0045
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "潔癖症のウサギさんはそう言って、ばたばたと慌ただしく準備を整えていく。\n
一方の私と言えば、やることもないまま、手にした本を膝に載せているだけだ。"


show t_per_end4 onlayer master
with dis
hide per_t_03_3

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（泡にも、人にもならない人魚姫？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（そんな展開、今まで見たこともなかったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人魚姫の終わりは、泡になって消えることが本来のストーリーだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、中には、取引を持ちかけた魔女を敵役にして、王子と共に魔女と戦って勝つ展開もある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（足を望んだのは自分なのに、都合がいい話よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "王子に会いたいと願ったのは人魚姫。\n
ゲームに勝てなかったのだから、退場は仕方ないことだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（ペーターと一緒に見ろって言っていたけど）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pet_f0212
Peter "「ああ、忙しい、忙しい。\n
愛しいあなたに万が一のことがあったら、僕は……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（お風呂の準備で本を読むどころじゃないみたいだし）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（とりあえず、捲ってみようかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "このまま一人でぼうっとしていても仕方ない。\n
期待せずページを捲ってみることにした。"

play sound se_0718
hide t_per_end4
show t_per_end5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「嘘……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（ちゃんと読める）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までは象形文字にしか見えなかった文字が、普通の言葉に変わっていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「……船の沈没と、王子との出会い」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（挿し絵もちゃんと入っているし）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……ひょっとして最初に見せてくれたもののほうが、夢だったのかしら？）"

play sound se_0718
hide t_per_end5

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「魔女の誘い、陸に上がって……」"


show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice pet_f0213
Peter "「[firstname]、何を見ているんです？」"

hide per_t_02_3
show per_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice pet_f0214
Peter "「これは……、ナイトメアの渡した本でしょう？\n
こんなおんぼろの本、あなたには相応しくありません」"

hide per_t_02_4
show per_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice pet_f0215
Peter "「いかにも汚いですし……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「いいから、続きを見せてよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不満顔をするペーターを振り返らずにそう言うと、彼は黙って私の隣に座ってきた。納得はしていない顔だが、取り上げる気はないらしい。"

hide per_t_01_4
show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隣から本を覗き込んでいる目が動いている。\n
私が熱心に読んでいることもあってか、彼もこの本には関心があるらしい。"

play sound se_0718

show t_per_end6 onlayer master
with dis
hide per_t_02_7

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（王子に気付いてもらえないところまでは、私が知っているものと同じね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二本足の魔法が解ける刻限が、迫ってきている。\n
人間になった姫の元に現れるのは、同じ海の姫だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0006
Mermaid "「さあ、この短剣で王子を貫きなさい。\n
その血を浴びれば、あなたはまたこちらに戻れるわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

play sound se_0718
hide t_per_end6
show black onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（でも、姫は結局王子を刺せない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "残る結末は、やはり一つだけだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（泡になって消える）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "報われない最期。\n
それでも望んだものならば、彼女は本望なのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後の章に手をかけた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（……………）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「え？」"

play sound se_0649

play music badend_gohome_ali
hide black
show t_per_end7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私はペーターの部屋にいたはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、目に痛いギンガムチェック模様の壁紙も、隣に座っていたペーターも今はどこにも見つけられなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、そもそも部屋そのものがここにはない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "潮騒の響く、静かな海辺。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「な……、何よ、これ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（これも、ナイトメアの仕業なの！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、足下を流れる海の水の感触は本物と思うほど、真に迫っている。\n
この前、夢で見せてもらった海と同じように。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして私の手には、短剣。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで私が読んでいた本の主人公がいる位置だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（何で私が人魚姫になっているのよ！？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice sam_f0006
Mermaid "「姫、早くしないと……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice may_f0007
Mermaid "「間に合わなくなってしまうわ。\n
ほら、足がもう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水辺ぎりぎりから顔を出している人魚達が私の足を指差していた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（まさか……）"

play sound se_0068
play sound se_0082
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "海水に触れていた足を見下ろせば、そこからは無数の泡が浮き上がっている。\n
海に溶け出しているのだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0007
Mermaid "「ああ、早くしなければ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_14")
T "（だ、だからって……。\n
どうしろって言うのよっ！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "物語に沿うのなら、王子を思って消えるのが本来の結末だ。\n
だが……。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0008
Mermaid "「あなたをここから連れだしたのは、あの王子でしょう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0009
Mermaid "「消えたくないでしょう。\n
元に戻りましょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_4")
T "（ええ、消えたくない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（どんな理由があっても、泡になって消えるような結末なんて、私は嫌）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だって、消えたら会えなくなってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の姿が見えないだけでも不安がった、あの白いウサギを残していくなんて、そんなことは夢でも出来ない。"

play sound se_0068
play sound se_0082
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

hide t_per_end7
show t_per_end8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Peter "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ペーター！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "絵本の世界の中に、赤い服を着たウサギが現れる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を見つけて、嬉しそうにほっと笑って。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「ペーター？」"

play sound se_0675
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何故か、彼は自分の胸元に短剣を押し付けようとする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（何をしているの？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice pet_f0216
Peter "「あちらに……、戻りたいですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（……え？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の言うことが分からない私は震えそうになる手で、短剣を握りしめることしかできない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0217
Peter "「だったら、僕があなたを帰します。\n
他の誰にも手伝わせない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0218
Peter "「どんな形であれ、あなたを幸せに導くのは、僕だけの役目ですから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "儚く、綺麗な笑顔。\n
すべてを悟りきったような顔で、彼は私の手ごと握り締めた短剣で胸を突こうとしていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（やめて）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "王子の血で、人魚姫は泡になる運命から逃れられる。\n
しかし……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女が望んだものは、きっと、恋を知る前に戻ることではなかったはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_9")
T "（やめて！！）"

hide t_per_end8
show bg06_sk_h_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「駄目！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声と共に、身体に力が戻る。\n
無我夢中で手を動かして、そして。"

play sound se_0564
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "音が、響いた。"

play sound se_0649
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]……」"

hide bg06_sk_h_day
show t_per_end9 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「……消えないでよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "切り裂かれた髪が潮騒に乗って散っていく。\n
だが、それがどれほどのものだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_3")
T "（あなたまで）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_5")
T "（私を、置いていかないで）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は、二度と海に帰れなくてもいい。\n
いつかこの選択を悔いるときが来たとしても。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何度でも、同じ結末を選ぶ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（だって……。\n
ペーターがいない海の底に、意味なんてない）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice pet_f0219
Peter "「分かりました」"

play sound se_0332
hide t_per_end9
show t_per_end10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_5")
voice pet_f0220
Peter "「でしたら、僕があなたの行くところについていきます」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_5")
voice pet_f0221
Peter "「それならいいですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（ついていく？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想もしなかった言葉に、強ばった身体から力が抜けた。\n
しかし、私のことなど構いもせずに、ウサギはずんずんと海へと入っていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まるで、初めて会ったあの昼下がりで私を穴に引っ張り込んできたときの焼き直しのようだった。"

play sound se_0076
hide t_per_end10
show bg06_sk_h_nig onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「あ、待って。\n
ペーター、そんなに深くに入っていっても私」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（この前はナイトメアがいたから問題なかったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "既に水は私の胸元まで迫ってきている。\n
ウサギ姿になったペーターはもう身体のほとんどが沈んでしまっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（これ以上は無理よ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_5")
voice pet_f0222
Peter "「何を言っているんですか？\n
あなたなら泳げますよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！」"

play sound se_0068
hide bg06_sk_h_nig
show bg_gen07_sc2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちゃぽんという音が響いたときには、世界は切り替わっていた。\n
視界のすべてを埋め尽くすのは、鮮やかなブルー。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、私の姿もまたあのときの人魚に変わっていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

hide bg_gen07_sc2
show t_per_end11 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（なんて、ご都合主義な）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢にしても出来すぎだ。\n
人がどうして勝手に人魚の姿に変わるのか。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0223
Peter "「人魚にはなれなくても、僕はあなたのウサギです。\n
どこにでも連れて行ってあげます」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0224
Peter "「そして、どこにでもついていきますから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0225
Peter "「だから、置いて行ったりしません」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0226
Peter "「あなたには見えなくても、声が聞こえなくても。\n
誰よりもあなたの傍に、いつでもいます、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誇らしげな、そして宣誓のような言葉。\n
その声に導かれるまま、私は海の中へと進んでいく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（でも、私は迷わない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の手を握っているのは、小さな白い手。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迷うはずがない。\n
私を導くのは、いつでも……、白ウサギの役目だ。"

play sound se_0738

play music dream_tsuduki_a_ali
hide t_per_end11

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"


show per_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Peter "「[firstname]、[firstname]！」"

hide per_t_01_3
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice pet_f0227
Peter "「どうしたんです？\n
しっかりしてください、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_16")
T "（ウサギじゃない）"

hide per_t_02_6
show per_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_16")
voice pet_f0228
Peter "「大丈夫ですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「ペーターは、今の夢、みた？」"

hide per_t_03_5
show per_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice pet_f0229
Peter "「夢？\n
何を言っているんです、あなたはずっと起きていたじゃありませんか」"

hide per_t_02_4
show per_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice pet_f0230
Peter "「……！\n
やはり、何か悪い病気でも拾ってきてしまったのでは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見当違いのことで顔色を変えるペーターは、やはり私と同じ夢をみていないらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（そうよね。\n
変な夢だったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頬を濡らすものを感じると、声が出なかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_5")
Peter "「！！」"

hide per_t_03_3
show per_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_5")
voice pet_f0231
Peter "「ど、どうしたんですか、[firstname]？\n
泣かないでください」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心配されている、そう思うのに、涙の糸が頬を伝って止まらない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_3")
T "（何で、哀しくもないのに涙が出るんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "優しくて、少し哀しくて。\n
きっと、忘れてはいけない夢。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_4")
T "（ペーターがいなかったら、泡になる終わり方しか出来なかったかもしれない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢で引き留めてくれたペーターが本物かどうかは分からないままだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（でも、きっと、ペーターはいてくれる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこがたとえ光の届かない深海であろうと。\n
私の一番近くにいるのは、この先ずっと。\n
この白い生き物。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T "「……ありがとう」"

hide per_t_01_8
show per_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_8")
voice pet_f0232
Peter "「え？」"

hide per_t_02_9
show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_8")
voice pet_f0233
Peter "「[firstname]、僕、あなたに何かしましたか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「ええ。\n
たくさん、してくれているわ」"

hide per_t_02_3
show per_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
Peter "「…………」"

hide per_t_03_4
show per_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
Peter "「[firstname]」"


show t_per_end12 onlayer master
with dis
hide per_t_02_12

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "優しいキスは涙を忘れさせてくれるように、身体の中に残っていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice pet_f0234
Peter "「ん……。\n
ふふ、僕は、おかしなウサギですね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice pet_f0235
Peter "「あなたを泣かせたくないと思うのに。\n
そんな嬉しそうな顔を見せてくれるあなたをもっと見ていたいとも思ってしまう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「……変な顔をしているわよね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（泣き笑いなんて、私には似合いそうもないのに）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice pet_f0236
Peter "「いいえ。\n
泣いているのに、幸せそうに見えるなんて僕の目のほうがおかしいんです」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頬を拭う手の強さに、更に涙が溢れそうになる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（ああ、止まらない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "甘えたくないのに、甘えてしまう。\n
ここにはどんなに泣いても拭ってくれるひとがいるから。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を導いて、どこにても付いてきてくれる。\n
そして、私を待っていてくれる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を案内する、白ウサギ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0237
Peter "「だから、確信させてください。\n
あなたの笑顔が本物だと……、これはあなたが笑っているから生まれるものなんだと教えてください」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢の中で人魚と王子は海へと帰っていった。\n
その結末が幸福なものであるかどうかは、私には分からない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（だって、自分の結末さえ分からないのに、人の幸福を願うだけのゆとりなんてないもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達の物語の最後が、まだ描かれていないのなら。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（どんなおかしな顔でもいいから）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_12")
T "（ペーターと同じ表情を浮かべながら。\n
満たされた気持ちで、本を閉じられますように）"

$ hi_mes()


hide t_per_end12
show white onlayer master
with compress_extralong
hide white  with compress_extralong
pause .5

$ renpy.movie_cutscene("endroll_a.mpg")
#return
