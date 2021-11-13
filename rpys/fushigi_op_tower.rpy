label fushigi_op_tower1:
$ place_of_stay = "Tower"

scene map_bg_winter_day
with stripe_l_medium

scene charasel_bg_tower_day
with stripe_l_medium

play music tower_stairs_down_p_ali

scene cr_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔の重鎮は、二人揃って愛煙家である。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、正確には愛煙家と言えるのは一人で、もう一人は哀煙家というほうが正しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（煙を吸い込んでは吐血しているんだもの……。\n
あれじゃあ、とてもとても）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むしろ、煙に哀れまれているような気さえしてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私自身、煙草は吸わない。\n
だが、個人が個人の意志で吸う分には自己責任なので、とやかく言う気もない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（言う気は……、なかったんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今まで特に誰かに文句を言ったことはなかったが、あの困った夢魔だけは例外だ。"

play sound se_0580 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"



show gre_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gra_f0000
Gray "「ああ、[firstname]。\n
ここにいたのか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「グレイ、どうしたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも多忙なクローバーの塔の副官は、私と同じようにこの時間帯は休憩のはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分だけ置いてけぼりにしてずるい、鬼だ、悪魔だと喚き立てる上司の部屋から一緒に出てきたのだから、間違いなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、どうしてか彼の近くには何人か同僚も一緒にいる。"

hide gre_t_02_9
show gre_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0001
Gray "「ナイトメア様を見なかったか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ナイトメア？\n
ううん、見ていないけど……、まさか」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（休憩中のグレイまで加わって、居場所を探すということは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今まで何度も何度も何度も……、そう、{size=+20}哀しいぐらいに何度も{/size}繰り返されたやりとりの原因は、二つに一つだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "体調の悪い上司が倒れたか。\n
あるいは逃走を図ったか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "倒れたのなら、彼の居場所を探すまでもない。\n
動けない身体を確保して、早々に医者を呼んだほうが賢明だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（いつもお医者さんを呼ぶ前に目覚めて、駄々を捏ねるけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔の領主ナイトメア＝ゴットシャルクの病院嫌いは徹底している。\n
何度吐血しようとも、絶対に病院や薬は嫌だと言って譲らないのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、グレイが休憩中にまで捜索しているのだから、答えは一つしかない。"


show toustaff_a1_11 at center
hide gre_t_02_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0001
Tower_Employee "「先刻から探しているんですが、お部屋にお姿がなくて……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「やっぱりなの！？\n
でも、私達が部屋を出るときには、仕事をしていたわよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サボっては駄目だと念押ししたのだが、無意味だったようだ。"


show gre_t_03_6 at center
hide toustaff_a1_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0002
Gray "「ああ……。\n
俺達が離れた直後に逃げ出したらしい」"

hide gre_t_03_6
show gre_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0003
Gray "「まったく、仕事が嫌で逃げ出すにしても、もう少し減らしてから逃亡してくださればいいものを」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「油断も隙もない……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（病弱なのに、どうして逃げ足だけはあんなに早いのよ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「私も探すのを手伝うわ」"

hide gre_t_01_6
show gre_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0004
Gray "「いや、君は休憩中だろう？\n
休みはちゃんと取ってくれ」"

hide gre_t_01_11
show gre_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0005
Gray "「最近忙しかったからな、これ以上無理をさせるわけにはいかない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（その言葉、そのまま返したい）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「それを言うならグレイだって同じじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事をしない上司のせいもあって、グレイの気苦労と仕事は絶えない。\n
休みを取れなんて、この塔の誰よりも休みの少ない人が言う台詞ではないだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「あなたこそ、働きすぎよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "休憩の時間帯でも、副官であるグレイのもとには部下が質問にやってくる。\n
けして断らず相談に乗っているから、常に仕事をしているようなものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（それに、私が休憩を取れないことはないもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは意外と目を光らせていて、私が休めない事態に陥ることは稀だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その本人が吐血したりとか、逃げ出したりだとか、仕事で駄々を捏ねたときを除けば……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（いい上司と素直に評価できないところが辛いわよね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「一緒に探したほうが、少しは早いかも知れないじゃない？」"

hide gre_t_01_14
show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0006
Gray "「いや、いいんだ。\n
その気持ちだけで充分だよ、ありがとう」"

hide gre_t_01_4
show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0007
Gray "「君にここできちんと休んでもらわないと、俺の休憩中にナイトメア様を任せられる人材がいない」"

hide gre_t_03_10
show gre_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0008
Gray "「そのためにも、今はちゃんと休んでくれ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（大人の答えだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイは本当に、私をその気にさせるのがうまい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この上更に言えば、自己満足の我侭になるだけだ。\n
素直に頷くと、彼は続けた。"

hide gre_t_03_4
show gre_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0009
Gray "「もしナイトメア様を見つけたら教えてくれ。\n
すぐに{size=+20}捕獲に{/size}、いや、迎えに行くから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「うん、分かったわ」"

play sound se_0580 volume .6
hide gre_t_02_13

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大きな背中が遠ざかるのを見送りながら、私も再び歩き始める。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（とはいうものの……、この先に、ナイトメアがいるとは思えないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ、私が向かっているのは、偏屈と引きこもりを自称する、時計塔の主の部屋。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の領地に住む友人との約束もなかったので、ユリウスのところに向かう途中だったのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（でも、どこかで見つけたら……、そのときは即グレイに通報しなくちゃね）"

$ hi_mes()

scene charasel_bg_tower_day
with stripe_l_long

play music tower_room2_p_ali
play sound se_0303
pause .5

scene ts_01 with Dissolve(1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋の前でいつものように二回ノックをして、私はそっとドアを押し開いた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ユリウス、お邪魔……、あれ？\n
いない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引きこもりがちな時計屋の指定席である作業台は、今、もぬけのから。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少し高い位置にあるベッドにもひとけはない。\n
どうやら本当に不在らしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（珍しい……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はこの世界でも一、二を争うくらいのインドア派だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐らく仕事絡みで出掛けたのだろうが（むしろそれ以外の理由で彼が出かけるとは思えない）、タイミングが悪かったのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「……ん？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋全体を見渡して、首を傾げる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この部屋は、ユリウスの作業場。\n
染み込んだ機械油の匂いと、珈琲の香りが広がる空間だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこに、いつもなら感じることのない香りが混じっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（煙草……？\n
ユリウスは煙草を吸わないわよね？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（あとこの部屋に来る人なんて、エースぐらいだけど……。\n
あの人が煙草を吸うなんて聞いたことないし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすがにクローバーの塔の職員全員までは把握していないが、この部屋で煙草を吸うような人など、咄嗟に思いつかない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、作業台の端から、煙を燻らせる金色の長いものがひょっこりと姿を見せていた。"

play sound se_0580
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"



play music nightmare_t_ali

show t_op_tou1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「何をしているの、あんたは？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_13")
voice nig_f0000
Nightmare "「な、何もしていない。\n
私は君に怒られるようなことなんか、何一つとしてしていないぞ、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が入ってきたことには気付いていたのか、白々しくもサボリの常習犯は言った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_11")
T "「物陰に隠れてこそこそ煙草を吸いながら、何を言っているのよ。\n
病弱なくせにっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（グレイが見つけられなかったはずだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の場所ならともかく、ここはユリウスの仕事場。\n
つまりこの部屋の主はナイトメアではなく、ユリウスだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この塔内を誰の許可を得ずとも入れるグレイでも、さすがに主不在の部屋を家宅捜索する気にはなれなかっただろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（グレイはそういうところ、常識があるもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他人の部屋に勝手に入り込みサボッているナイトメアとは、全然違う。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0001
Nightmare "「失敬な、私は別に隠れていたわけではなくてだな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（嘘つけっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただ煙草を吸うだけなら机の陰に隠れる必要なんてない。\n
こそこそしていた段階で、後ろ暗いと自分で告白しているようなものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の仕事の時間帯に、ユリウス不在の部屋にいる時点で疑いようがない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0002
Nightmare "「ひ、酷いっ……。\n
だいたい、君達が私を置いてさっさと休憩に入るからっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「私達は、ちゃんと予定通りの休憩よ。\n
自分の仕事だってすませてあるもの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「あんたの場合は、逃げ続けたせいなんだから、{size=+20}自業自得なの{/size}」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "決裁待ちの書類がどれだけ積み上げられているかは、彼の部屋を見るまでもない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「ほら、さっさと部屋に戻って仕事の続きをしなさいってば。\n
グレイにこれ以上迷惑をかけたら、あの人、そのうちハゲるわよ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice nig_f0003
Nightmare "「ハゲるものか。\n
グレイめ、薬を飲めだの病院に行けだの、私が倒れる度に提案してくるんだぞっ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「それはあんたのためでしょう……。\n
使命感のあるいい部下じゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もはやナイトメアの捕獲は、グレイの仕事の一つになっていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事をさぼる上司は、この世界には何人かいるが、逃亡先で倒れるのは彼だけである。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "休みも関係なく上司の回収義務に追われるグレイは、苦労させられていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、当の本人は不満そうに口を尖らせるばかりだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0004
Nightmare "「少しくらい見逃してくれたっていいじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「見逃していたら仕事が終わらないわよ！\n
ハゲないにしろ、心労で髪の毛が白くなりそうだからやめなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイは何も休憩をするなと言っているのではない。\n
ただ、病弱でサボり魔なナイトメアは、仕事の進みが遅いのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼にしか出来ない仕事だってある。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0005
Nightmare "「白いグレイ……。\n
それはそれで見てみたい気もするが、この世の終わりが来る気がするぞ」"

play sound se_0492
hide t_op_tou1
show t_op_tou2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_9")
T "「いや、そんなことはどうでもいいのよ？\n
くだらないことを言ってないで、さっさと戻りなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "蹲ったままだったナイトメアの手から煙管を取り上げる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0006
Nightmare "「あー、酷いっ。\n
私のささやかな癒しだというのに！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0007
Nightmare "「君はグレイの肩ばかり持って……、私にも優しくしてくれたっていいじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「あなたにとって、煙草のどこが癒しだって言うのよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（吸いながら、吐血ばっかりしているくせに）"

hide t_op_tou2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの作業台を借りて、その上に煙管を置き、呆れたように上司でもある男を睨み付けた。"


show nai_s_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0008
Nightmare "「い、癒しだと言ったら癒しなんだ。\n
煙草を吸っている間は、嫌なことを忘れられる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「ふうん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "{size=+20}（誰かの受け売りっぽい台詞ね）{/size} "

hide nai_s_02_5
show nai_s_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_17")
voice nig_f0009
Nightmare "「ち、違うっ。\n
違うぞ、[firstname]！」"

hide nai_s_03_3
show nai_s_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_17")
voice nig_f0010
Nightmare "「……ぐ、はぁっ！ごふっ、げほっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「あー、ほら言っている傍から」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口の端からどばどばと血を流す夢魔の背中をさすってしまうのは、もはや反射と言えるレベルだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（吐血にも驚かなくなったわよね、私）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この塔に来たばかりの頃はナイトメアの吐血のレベルが分からなくて、毎回右往左往したものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが最近では、吐血のレベルを判断できるようになってしまった。\n
この程度なら医者を呼ぶまでもないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハンカチで口元を抑える上司に、出来る限りの優しさを込めて言葉を重ねる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「だから、大人しく部屋に戻りましょう……、ね？」"

hide nai_s_03_2
show nai_s_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice nig_f0011
Nightmare "「嫌だっ！\n
聞こえたぞ、今、『部屋に戻ったら、グレイと二人がかりで監視だわ』とか思っているだろうっ！？」"

hide nai_s_03_8
show nai_s_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice nig_f0012
Nightmare "「君と二人ならともかく、あいつとずっと一緒にいたら息が詰まって、更に吐血する！」"

play sound se_0378 volume .25
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "{size=+20}「……そこまで病弱なら、病院に行きなさいよ」{/size} "

hide nai_s_02_10
show nai_s_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice nig_f0013
Nightmare "「病院は嫌だ！\n
私だって君と一緒に休憩に入りたかったのに……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「休憩に入れるだけ仕事が進んでいなかったじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私と一緒に休憩したいなら、他の時間帯にサボらなければいいだけの話だ。"

hide nai_s_01_4
show nai_s_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0014
Nightmare "「いや、いい部下とは、模範的な部下とは……。\n
すなわち、私の体調に合わせたスケジュール管理が出来る部下であってだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「その体調に合わせて立てたスケジュールをぶっちぎって遅らせているのは、他でもないあんたでしょうがっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（吐血している上司相手に、何をムキになっているんだろうとは思うけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここで言いくるめられたら、ますます塔の業務が滞るだけだ。\n
妥協は出来ない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「煙草はやめない、珈琲は飲めないくせに無理矢理飲もうとする、病院にも行かない……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「ただでさえ悪い体調を更に悪化させているのは、他でもない自分でしょうっ」"

hide nai_s_02_5
show nai_s_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice nig_f0015
Nightmare "「う……、うう、冷たい……。\n
やはり夢の中にしか、私の安住の地はないのか」"

hide nai_s_01_7

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "更にいじいじと丸くなったナイトメアは、どこからともなく毛布を取り出して蹲った。"

play sound se_0282
pause .3

play music tower_room1_p_ali

show t_op_tou3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0000
Julius "「何だ……？\n
おまえ達、私の仕事場で一体何をしている？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ユリウス！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "床から立とうとしないナイトメアに、どうしたものかと考えていると、ドアが開く音がした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視線を向ければ、この部屋の主が、怪訝そうな表情でこちらを見ている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0001
Julius "「やれやれ、出たくもない外から戻ってみれば、騒がしい……。\n
仕事の邪魔をするのなら、とっとと……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0002
Julius "{size=+20}「おい、何だ、それは！？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「は？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「それって……？\n
見たとおり、毛布を被ったナイトメアだけど」"

play sound se_0055
pause .5
play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐいぐいと毛布を引っぺがしながら返す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この部屋の主が帰ってきたのだ、逃亡者にいつまでも油を売らせるわけにはいかなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0016
Nightmare "「そ、それ扱い……。\n
[firstname]、何かますます私の扱いが酷くなってないかっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0003
Julius "「違う！\n
芋虫のことなどではない、おまえらの横だっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（横？\n
でも、私達の横にあるものなんて……、ユリウスの作業台ぐらいよね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（あ……、そういえば、なんとなく、焦げ臭いような気が）"

play sound se_0378
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアから毛布を奪うことに集中しすぎて気付かなかったが、言われてみればどこからともなく煙の臭いがする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（それも……、かなり近い場所から）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice nig_f0017
Nightmare "「！\n
な、なんだなんだ、この臭いはっ！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice jul_f0004
Julius "「悠長な……、火事以外のなんだと言うんだっ！\n
机の上が燃えている！」"


play music gag3_a_ali
hide t_op_tou3
show t_op_tou4 onlayer master
with dis
play sound se_0781 volume .85
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "はっと振り返れば、ユリウスの机の上に鮮やかな炎が灯っていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（ナイトメアの煙管！！\n
もしかして、あれが原因！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "中心で燃えている長いものを見て、思わず息を飲んだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慌てて何か火を消すようなものがないか確認したが、ここは他でもない時計屋・ユリウスの部屋だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の仕事に関わるもの以外に、余計なものがあるはずがなかった。"

hide t_op_tou4
show t_op_tou5 onlayer master
with dis
play sound se_0322
$ flash_red(.1)
$ flash_red(.1)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0018
Nightmare "「あち……、あち、あつつ……っ！\n
な、何で私の背中も熱いんだっ！？」"


$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ナ、ナイトメア！\n
毛布にも火がついているわ、早く取りなさいよっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice nig_f0019
Nightmare "「な、何ーっ！\n
くっ、この……」"

play sound se_0700
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice nig_f0020
Nightmare "「ああ、先刻取れないようにしっかり結んだせいで、解けないっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jul_f0005
Julius "「何をしているんだ、おまえは！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの怒声が響く中、二人がかりで毛布の結び目に手を伸ばす。\n
だが、焦っているせいかなかなか解けない。"

play sound se_0322
$ flash_red(.1)
$ flash_red(.1)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0021
Nightmare "「あち、あつ……！\n
く……、まさかこんなところで焼け死ぬとは」"


$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0006
Julius "{size=+20}「おまえが死ぬのは勝手だが、私の仕事場ではやめろ！」{/size} "

play sound se_0313
pause .3
play sound se_0313

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスはナイトメアを睨み付けながら、上着を火に叩き付けているが、油がついてしまったのか、火は消えない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0022
Nightmare "「あ、あつ……。\n
や、やっぱり焼け死ぬのは痛いっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0023
Nightmare "{size=+20}「痛いのは嫌だっ！！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスが大元の消火活動をしている間に、私達は急いで手を動かすが、毛布の結び目はなかなか解けてくれなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_4")
T "（お願いだから、解けてよっ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
voice jul_f0007
Julius "「ちっ……。\n
ナイトメア、早く外に出ろ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
voice jul_f0008
Julius "「ここは私が」"

play sound se_0282

play music battle_ali
hide t_op_tou5
show t_op_tou6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
voice gra_f0010
Gray "「時計屋、近くの部屋からこのあたりが焦げ臭いと聞いてきたが……。\n
な、何だ、これはっ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「グレイ！\n
……ごほ、ごほんっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞こえた声に、思わず声が上がった。\n
そのせいで、反射的に煙を吸い込んでむせてしまったが、それぐらい大したことではない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0011
Gray "「[firstname]、君まで……。\n
そこにいるのは、ナイトメア様！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0012
Gray "「あなたまで何をしていらっしゃるんですか！\n
部屋から姿を消したと思ったら……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0024
Nightmare "「今はそんなことを言っている場合じゃないぞ、グレイっ。\n
くう……、この毛布さえ外れれば何とかなるんだが」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0009
Julius "「トカゲ、おまえの上司だ！\n
自分でどうにかしろ！私はこいつの相手で手があかないっ」"

play sound se_0313
pause .3
play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "作業台を叩くユリウスにしても、全身煤まみれになっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事道具があるから彼も必死なのだろう。\n
だが、それだけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "火がナイトメアや私がいるほうに飛び散らないように気を付けているのが分かる。\n
端から見ればさぞかし奇妙な光景だろうが、さすがにグレイの反応は早かった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0013
Gray "「おまえに言われるまでもない。\n
[firstname]、少しだけ下がっていてくれ、危ない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（危ないって……、どういうこと？）"

play sound se_0674
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鞘から固いものが引き抜かれる音に、私よりも早くナイトメアが反応する。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、その顔からは、いつもにも増して血の気が引いていた。"

hide t_op_tou6
show t_op_tou7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0025
Nightmare "「……な、何をする気だ、グレイ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0014
Gray "「解いているだけの余裕はありませんからね。\n
ナイトメア様、失礼します」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

play sound se_0679
##special anime kiseki01
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬の出来事だった。"

##[anime]
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイのナイフは、ナイトメアに掠ることなく毛布を結び目ごと真っ二つに切り裂いていた。"

hide t_op_tou7
show t_op_tou8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呆然とする私とナイトメアに構わず、彼は火のついた毛布を手早く奪い取る。\n
残った火を視界に収めながら、短く告げた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0015
Gray "「ここは俺と時計屋でどうにかするから、君はナイトメア様を頼む。\n
他の連中にも声をかけてきてくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「あ、うん。\n
分かったわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二つ返事で頷いて、ナイトメアを引き摺るように歩き出す。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（……って、どうして自分で歩こうとしないのよ、この芋虫っ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice nig_f0026
Nightmare "「し、仕方ないだろう！\n
腰が抜けて、足が動かないんだ……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（情けない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仮にも領主が、自分の部下の刃に脅えてどうするのだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0027
Nightmare "「君はそう言うがな、ナイフを持ったグレイなんて真っ正面に見るものじゃない！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0027_5
Nightmare "「毛布どころか、{size=+20}私ごと真っ二つにされるかと思ったぞっ{/size}」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0016
Gray "「はははは。\n
まさか、俺は自分の上司を斬ったりしませんよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスと共に消火を続けるグレイの声は、何故か、火の傍とは思えないほど涼しげだった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0017
Gray "「この小火が落ち着いたら、ゆっくりとお話ししましょう、ナイトメア様」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0018
Gray "{size=+20}「仕事をさぼってまで、ここで何をしていたのかについても、たっぷりと」{/size} "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（怒っている、怒っている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "穏やかな口調だけに、これは相当に根が深そうだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「二人とも……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice jul_f0010
Julius "「いいから、行け。\n
[firstname]、その芋虫を投げ捨てたら、水を持って帰ってきてくれ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice gra_f0019
Gray "「いや、彼女は避難して……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice jul_f0011
Julius "「勝手なことを言うな、トカゲ。\n
早くしないと、私の部屋が仕事の出来ない空間になるだろうが！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice jul_f0012
Julius "「今は人手がいるんだっ。\n
私の部屋だけでなく、おまえの職場も炎上させたくないのなら、余計なことを言うんじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの切羽詰まった声と、苦言を呈するグレイの声。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（二人とも、ごめんなさい……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それらを聞きながら、私はようやく部屋の外に出たのだった。"

hide t_op_tou8

$ hi_mes()

stop music
show black with fade
$ renpy.movie_cutscene("Opening_video.mpg")
label fushigi_op_tower_skip:

scene charasel_bg_tower_day with stripe_l

play music truth_a_ali

scene cg_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（こんなおおごとになるとは思わなかった……、なんて無責任なこと言えないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぶすぶすと煙が立ち上るユリウスの作業場を見て、身が竦む思いだった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "幸い……、というべきかどうかは定かではないが、この世界の時計は多少火を受けても壊れるものではないらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（時計を壊して監獄送りなんて事態になったら、皆に合わせる顔がない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "多少焦げていても、修理可能ということは当のユリウスから聞いたばかりだが、だからといって「はい、そうですか」と終われるはずがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ナイトメアは煙を吸って寝込んでいるし……。\n
グレイはその世話に加えて、始末書やら報告書やらが増えて）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（ユリウスに至っては、唯一の自分の部屋が……、あの有様）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元はといえばナイトメアがユリウスの部屋に逃げ込んでいたのが問題だが、火のついたものを安易に放置した私にも非はある。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「謝りに行こう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの小火騒動に関わった全員に頭を下げなくてはいけないだろうが、最初に謝りに行くべきなのは、やはり彼だろう。"

$ hi_mes()

play music map_winter_jok

scene charasel_bg_tower_day
with dis
show screen tower_man_choice
$ ui.interact()
