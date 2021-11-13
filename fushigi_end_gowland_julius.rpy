
scene map_bg_winter_day
with dis
label fushigi_end_gowland_julius1:
$ clockanim()


scene map_bg_winter_day
with Dissolve(1.2)

scene charasel_bg_tower_day
with dis

play music tower_room1_p_ali

scene ts_01
with Dissolve(1.2)
play sound se_0282

show go_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0438
Gowland " 「よう、邪魔するぜ、時計屋」"

hide go_t_01_1
show go_t_01_1 at left
show yuri_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jul_f0339
Julius " 「……ゴーランド？\n
なんの用だ。おまえのところの仕事なら、この前、渡したばかりだろう」"

hide yuri_t_02_10
show yuri_t_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jul_f0340
Julius " 「よほど緊急の仕事でもない限り、しばらくは待ってもらうぞ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ノックもなくドアを開き、部屋に入ったのは、遊園地のオーナー。\n
ユリウスはもう慣れたというように、溜息をつきながら、そう忠告した。"

hide go_t_01_1
show go_t_03_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0439
Gowland " 「おまえは本当に仕事人間だよなあ、よくやるよ。\n
でも今回は仕事の話じゃないんだ、なあ、[firstname]？」"

hide yuri_t_03_9
show yuri_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius " 「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T " 「お邪魔します、ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドの横から顔を出した私に、ユリウスは怪訝な顔をしている。"

hide yuri_t_03_2
show yuri_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius " 「…………」"

hide yuri_t_02_9
show yuri_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0341
Julius " 「……おまえがいるということは、仕事の話ではないのだろうが。\n
なんだ、その家出をしてきたような大荷物は？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ユリウスの視線は、私とゴーランドが持った箱に向かっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 色とりどりのラッピングがされた外装を見れば、遊園地から持ってきたものであることはすぐに分かっただろう。"

hide go_t_03_5
show go_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0440
Gowland " 「ああ、うちの新製品の試供品だ。\n
この子が世話になったからな、おまえにも分けてやろうと思って」"

hide yuri_t_02_10
show yuri_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0342
Julius " 「おまえのところの新製品だと？その上試供品とは……。\n
{size=+20}毒入りじゃないだろうな？{/size}」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T " （ユリウスらしい発想よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " とはいえ、私も試供品の中身まではゴーランドから教えてもらっていない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T " （ラッピングの感じからすると、お菓子だと思うんだけど……。\n
何しろ発案者がゴーランドだものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 見た目が中身を裏切っていてもおかしくない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T " （持った感じでは軽いから、クッキーとか、チョコレートとかのはず）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " もし本当に危ないものだったら、責任をもって回収しようと思う。"

hide go_t_02_8
show go_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0441
Gowland " 「失礼なことを言うなよ。\n
おまえには色々迷惑かけたからな、その礼みたいなもんだ」"

hide yuri_t_03_12
show yuri_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0343
Julius " 「いらん、持って帰れ。\n
そんな物を押しつけられるほうが迷惑だ」"

hide go_t_03_3
show go_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0442
Gowland " 「そう言うなって、せっかく遊園地から持ってきたんだから開けてみろよ」"

play sound se_0662
hide go_t_03_4

hide yuri_t_02_11


scene t_cut_end_go_yuri1u
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「わあ……、綺麗」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドが持っていた箱を開けば、中から更にカラフルな色が現れる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T " （やっぱり、お菓子だったのね）"


scene t_cut_end_go_yuri1
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 一つ一つ個別包装されたお菓子は、殺風景なユリウスの作業場の中で酷く浮いているが、可愛い包装は見ているだけでも楽しくなってくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「これ、中身は何なの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 思わず、ユリウスよりも先に私が聞いてしまった。"


show go_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0443
Gowland " 「それは食べてからのお楽しみだな。\n
ネタバレは最初にするもんじゃねえよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T " （それもそうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 期待と不安があるからこそ、楽しめるものもある。"

play sound se_0472

scene ts_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T " 「はい、ユリウス。\n
あなたの分」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " お菓子を手に取り、作業台から動かないユリウスに渡す。"

hide go_t_01_2
show go_t_01_2 at left
show yuri_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0344
Julius " 「いらんと言っているだろう、見たとおり私は仕事中なんだ。\n
菓子なんか悠長に食べる暇は……」"

hide go_t_01_2
show go_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0444
Gowland " 「そうつれないことを言うなって。\n
ほら、食えよ、時計屋！」"

play sound se_0051
camera at vpunch
camera at hpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T " 「！！」"

hide yuri_t_03_12
show yuri_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
Julius "{size=+20}「！！！？」{/size}"

play sound se_0007
hide yuri_t_03_3
show yuri_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jul_f0345
Julius " 「な、なにふぉ、する、ご……、らん！？」"

hide go_t_01_3
show go_t_03_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice gor_f0445
Gowland " 「だいたいなあ、おまえ、部屋に閉じこもりすぎで前々から栄養失調が心配だったんだよ。\n
せっかくの機会だ、しっかり食いやがれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T " 「ゴ、ゴーランド……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T " （それはさすがに入れすぎじゃ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " いつのまにラッピングを取り払ったのか、それとも試供品の一部は未包装だったのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 両手にお菓子を握り締めたゴーランドは一気にユリウスの口へと突っ込んでいく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T " （嫌がらせ、じゃ、ないのよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドに悪意はないようだが、苦しそうなユリウスを見て、止めるべきか迷う。"

hide yuri_t_02_3
show yuri_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0346
Julius " 「む、ぐ……、ん、は、おまえ、ゴーランド、何をする！！\n
しかもこれは……、酒が入っているじゃないか！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T " 「え、お酒ってどういうこと？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 手にしたお菓子は相変わらず軽い音を立てていて、お酒の気配など感じない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ラッピングを外してみたが、私の目にはただのチョコレート菓子にしか見えなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T " （そういえば、何となく部屋の中にアルコールの匂いがまざっている気がするけど……）"


play music gag2_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 二人で運んできた箱とゴーランドを交互に見つめてしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T " 「ゴーランド、まさか、これ全部同じお菓子？\n
そして……、全部、お酒入りだったりするわけ？」"

hide go_t_03_6
show go_t_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice gor_f0446
Gowland " 「当たり前だろ、[firstname]。\n
酒の入っていないウイスキーボンボンなんてあるかよ」"

hide yuri_t_03_7
show yuri_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice jul_f0347
Julius " 「そんなものを、問答無用で人に食わせる奴がいるか！\n
う……、酒の匂いがして気持ち悪い」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T " 「だ、大丈夫、ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 大量のウイスキーボンボンを食べさせられた挙げ句に大声を出したせいだろう、顔を顰めて蹲るユリウスの背中をさする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T " （どこかの夢魔を思い出すわ）"

hide yuri_t_01_8
show yuri_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice jul_f0348
Julius " 「……大丈夫なものか。\n
さすがに胸焼けがする」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T " （それはそうでしょうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " しっかりとチョコレートでコーティングされたウイスキーボンボンは、高級感もあるが、その分一粒でもかなりのボリュームだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " それを一気に大量食いさせられれば、胸焼けを起こしたとしても仕方ない。"

hide go_t_02_3
show go_t_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0447
Gowland " 「日頃から食ってねえから、そんなにすぐ胸焼けを起こすんだよ。\n
ほれ、[firstname]、あんたも食いな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T " 「え？」"

play sound se_0313
camera at vpunch
camera at hpunch

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T " 「！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_9")
T " 「む、ぐ……！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T " （何よ、これ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 少しアルコールを入れました、というレベルではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T " （ウイスキーの味しかしない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 包み込んでいるチョコレートが香り付け程度にしかなっていない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ユリウスが気持ち悪くなるのも頷けた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T " （どれだけ詰め込んだのよ、ゴーランド\n
！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 口の中に放り込まれては吐き出すわけにもいかず、お酒の匂いと戦う。"

hide go_t_03_1
show go_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0448
Gowland " 「うん、悪くねえな。\n
これならすぐに商品化しても、充分売れそうだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " むせそうな私と違い、ゴーランドは平然とお菓子を頬張りながら笑っている。"

hide yuri_t_01_9
show yuri_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0349
Julius " 「実験なら、もっと別の場所でしろ。\n
私を巻き込むんじゃない！」"

hide go_t_02_8
show go_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0449
Gowland " 「そう言うなって、ほら、まだ別の味もあるんだぜ。\n
ソーダに、ミルク、ミント、変わり種ではソース味や塩味なんてものもある」"

hide go_t_03_9
show go_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0450
Gowland " 「先刻は一度に食わせちまったから、味も分かんなかっただろうけど、今度はゆっくり味わってくれよ」"

play sound se_0548
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " そう言ってゴーランドは、どっさりとお菓子を取り出して見せた。"

hide yuri_t_03_13
show yuri_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius " 「…………」"

hide yuri_t_02_11
show yuri_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0350
Julius " 「これが礼だと？\n
嫌がらせ以外の何だと言うんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T " （今回ばかりは返す言葉がないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 知らなかったとはいえ、一緒に件の新製品を持ち込んでしまった私も共犯者になるだろう。"

hide go_t_01_1

hide yuri_t_03_12

$ hi_mes()

$ time_effect()


play music honobono2_a_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
Julius " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T " 「ユリウス、ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 仕事机の上で突っ伏しているユリウスに声をかけると、彼はすっかり寝入ってしまっていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 肩を軽く揺すってみたが、起きる気配はない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T " （まあ、これだけ食べさせられれば当然か）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " いつもは時計のパーツと工具しか乗せられていない机の上は、今、お菓子の包装紙でいっぱいになっている。"


show go_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0451
Gowland " 「ん？何だよ、時計屋。\n
もう寝ちまったのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「……あれだけ食べさせられたら寝ちゃうのも仕方ないでしょう」"

hide go_t_01_6

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 床に転がっている空箱は一つや二つではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T " （一体どれだけ空けたんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 私も試しに味見はしたが、三つ目でもう降参していた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T " （味見しようにも、ウイスキーの味しかしないんじゃどうしようもないというか、味見の意味がないわよ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
Julius " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T " 「……ユリウス、起きそうもないわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 私とゴーランドが間近で喋っているのに、彼は一向に起きる気配がない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T " （多分、仕事で疲れていたんだろうな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 私が居候していたときよりも、今、この部屋に置いてある時計の数が増えている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T " （口は悪いけど、優しいわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 私が押しかけたときもそうだ。\n
彼は口では色々と文句を言うが、その実、付き合いはいい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T " （確か……、あのあたりに毛布があったからかけておこうかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 雑多に物が置かれた仕事部屋。\n
棚に収められた私物の位置も大体把握している。"

play sound se_0067
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 勝手知ったる他人の部屋の中で、毛布を取り出すとゴーランドと視線が合った。"


show go_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「…………」"

hide go_t_03_10
show go_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0452
Gowland " 「……ずいぶん、よく知ってるんだな、あんた」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T " 「よく知っているって、何を？」"

hide go_t_03_11
show go_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice gor_f0453
Gowland " 「この部屋のことだよ。\n
俺にはどこに何があるかなんてさっぱりだが、あんたには分かるんだな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " いつのまにか頬杖をついてユリウスの隣に座ったゴーランドは不満そうにそんなことを言う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「まあ、しばらく居候していたし。\n
この毛布は私が転寝したときに借りたこともあったから」"

hide go_t_03_1
show go_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Gowland " 「…………」"

hide go_t_02_2
show go_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gor_f0454
Gowland " 「はあ……、あんたのことだから無意識にそう言っているんだろうけどよ。\n
恋人としては、複雑だぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T " （ユリウスの部屋のことを知っているのが、どうしてそんなに複雑なの？）"

hide go_t_02_5
show go_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice gor_f0455
Gowland " 「帽子屋やハートの城に家出されるよりは、時計屋のほうがマシだと思っていたんだけどよ。\n
やっぱり、あんまり面白くねえな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T " 「……ゴーランド？」"

hide go_t_03_6

play sound se_0055

show t_end_go_yuri1 onlayer master
with dis
camera at hpunch
camera at vpunch

play music transparent1_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 洋服の裾を掴まれて、引き寄せられる。\n
抵抗する理由もなかったので、そのまま抱きしめられた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T " 「……お酒くさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " いつものゴーランドにはない、人を陶酔させるような気配がする。\n
くらくらしてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T " （でも、あのバニラの匂いよりはずっといい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドの中にウイスキーの香りが混じっているのなら、いいと思ってしまった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0456
Gowland " 「じゃ好都合だな。\n
酔っているってことにしておいてくれよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「ん」"

play sound se_0472
hide t_end_go_yuri1
show t_end_go_yuri2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドは、作業台の上にあったチョコレートの包装を器用に外し、私の口に運んでくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「もういいってば、これ以上食べさせられたら、悪酔いしそう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice gor_f0457
Gowland " 「あんたが少しぐらい悪酔いしても、平気だって。\n
むしろ、少し酔っていてくれたほうが、俺も……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「ゴーランド？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0458
Gowland " 「酔っているって理由があれば、許してくれるだろ？\n
俺がこうやって独占していても、酔っているから抵抗できないって理由も立つ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_10")
voice gor_f0459
Gowland " 「いつものあんたなら、こんなこと簡単にさせてくれねえからよ。\n
今は、俺だけのものって思わせてくれ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T " （そんな言い方、ずるいわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 今だけだから許してほしい。\n
そう聞こえてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T " （地位も名誉もある人なのに。\n
……私なんかを相手に、不安になるなんてね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 口の中に放り込まれたチョコレートは、半分くらい溶けてしまっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T " 「…………」"

play sound se_0551
hide t_end_go_yuri2
show t_end_go_yuri3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_8")
Gowland " 「！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T " 「……ん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ほとんどお酒の味しかしないチョコレートを、ゴーランドの口に戻した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_4")
T " 「悪酔いさせてほしいなら、こういう形で応えてあげてもいいけど？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
Gowland " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice gor_f0460
Gowland " 「……っぷ、はははは、参ったな！\n
まったく、あんたには完敗だよ、とても勝ち目なんかねえや」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T " （本当に勝ち目がないのは私のほうよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " むせ返るようなチョコレートと、ウイスキーの香り。\n
頭の芯から溶けていきそうになる。"

hide t_end_go_yuri3

show yuri_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0351
Julius " 「……おまえ達、べたべたするのなら、何もこんな場所でやらなくともいいだろう。\n
さっさと遊園地に戻ったらどうだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T " 「ユ、ユリウス！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T " （いつから起きていたの！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 先ほどまで机の上に伏せていたはずの彼は身を起こして、私達を見ていた。\n
まだ眠気が残っているのか、いつもよりも少し気怠そうな眼差しだ。"

hide yuri_t_03_12
show yuri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0352
Julius " 「まったく。\n
おまえが来るといつも調子が狂う」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T " 「……ごめんなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ユリウスは睨んでくるが、酔っぱらった顔では今ひとつ迫力が足りない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T " （なんだか……、可愛い）"

hide yuri_t_02_11
show yuri_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice jul_f0353
Julius " 「またにやにやと。\n
いいか、私の仕事部屋は逢い引きのための場所でもなければ、駆け込み寺でもなくてだな」"

hide yuri_t_02_9
show yuri_t_02_9 at left
show go_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice gor_f0461
Gowland " 「そう言いながら、まだ足下がふらついているぜ、時計屋。\n
そんなのじゃ繊細な仕事は出来ねえんだから、気にせず食えって」"

hide yuri_t_02_9
show yuri_t_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice jul_f0354
Julius " 「押し付けてくるんじゃない！まったくエースといい、おまえといい……。\n
どうして私の周りにいるやつは、余計なちょっかいばかり出してくるんだ！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T " （放っておけないからよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ぎゃーぎゃー言うユリウスと、まとわり付くゴーランドを見ながら思わず笑ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T " （……なんでだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 二人がこうして一緒にいる姿を見ているだけで。\n
胸の中がとても温かくなるような気がする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T " （なくなったものが、埋まっているような。\n
そんな安心感がある）"

hide yuri_t_03_7

hide go_t_02_8
$ hi_mes()

$ time_effect()

play music night_garden_p_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jul_f0355
Julius " 「ん……。\n
これは次の時間帯に仕上げて、それから……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0462
Gowland " 「むにゃ……、ボリス、それはそうじゃ……。\n
ああピアス、そんなところに物を置くんじゃねえ……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T " （結局二人揃って寝ちゃったわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " まるで酒場の風景のようだが、ここはこの世界で一番仕事熱心な時計屋の職場のはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T " （酒瓶の代わりにゴミが散らかっているあたり、ちょっと違うけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「二人とも、こんなところで寝ていたら風邪をひくわよ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jul_f0356
Julius " 「……だから、それはこっちのパーツで。\n
勝手に弄るなと何度言ったら、壊すんじゃない、エー……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gor_f0463
Gowland " 「だーかーらー、そうじゃねえって。\n
スピードが足らねえよ、スピードが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T " 「…………」"

play sound se_0551
show t_end_go_yuri4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T " （どんな夢を見ているんだか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " いつのまにか眠ってしまった二人に毛布を掛け直して、その寝顔を覗き込む。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T " （こういうときには、ナイトメアの能力がちょっと羨ましいわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 一人素面で残されてしまった身としては、何だか置き去りにされたようで少し残念だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T " （だからといって、二人ほど食べられないし……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
Julius " 「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
Gowland " 「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T " 「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 二人は眠っているはずなのに、まったく同じタイミングで名前を呼ばれてどきっとする。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T " 「……な、何？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T " （実は起きているとか？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " どきどきする胸に手を当てながら聞き返すと、二人は寝返りを打ちながらもごもごと何か言ってくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0357
Julius " 「今は……、手が離せない。\n
隣の部屋から、予備のぜんまいを……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0464
Gowland " 「最新作には、一番に……、あんたを乗せてやるって。\n
遠慮なんかするなよ、あんたは俺の好きな女なんだから当たり……うん、むにゃ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T " （寝言？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " そのまま再び寝入ってしまった二人をしばらく見ていたが、起き出す気配はない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T " 「……気持ちよさそうに寝ちゃって」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドとユリウス。\n
性格もまったく違う二人なのに、彼らが一緒にいる今の風景は何故かほっとする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T " （起きたら、珈琲でも淹れてあげようかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 珈琲党の二人が揃っているから、ちょうどいいかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 甘さが残った口に、とびきり苦みの効いた美味しい珈琲を入れたらどんな顔をするだろうか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「ユリウスのことだから、豆も常備しているだろうし。\n
少し見せてもらおうかな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " そして、立ち上がりかけたところで、もう一度振り返る。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 大の大人が一枚の毛布を引っ張り合うように眠っている光景。\n
おかしくも、微笑ましい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T " 「おやすみなさい、二人とも」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_19")
T " （二人が目覚めたとき、最初に目に入るのが、どうか私でありますように）"

hide t_end_go_yuri4
with Dissolve(5)
hide ali_t_02_19
hide frame_gen_monologue
with Dissolve(4)

$ renpy.movie_cutscene("endroll_c.mpg")
#return
