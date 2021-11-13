label gakuen_ace6:
scene bg_map_nig
with dis
$ clockanim()

jump gakuen_common_breeze
label gakuen_ace6_2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「エースの部屋は三階だから、まずは階段を探さなくちゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とんとんと額を指先で叩いて、記憶を辿る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子寮と女子寮では造りも違う。\n
迷わないよう、注意しなくては。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズへの参加を決めたあの日。\n
１週間という短い期間ではあったけれど、充分な量の情報収集が出来たと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、それは未だ新鮮な状態で、私の頭の中に刻み込まれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、男子寮の中、目的地であるエースの部屋を目指して移動を開始した。"

play sound se_0774
with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music night_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "途中何度か迷いそうになりつつ、無事にエースの部屋まで辿り着くことが出来た。"

play sound se_0300
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返事はない。"

if lovechara_ace_points == 9:
    jump gakuen_ace6_4a
label gakuen_ace6_3:
menu:
    "（も、もしかして）":
        jump gakuen_ace6_4a
    "（……やっぱり）":
        jump gakuen_ace6_4b
label gakuen_ace6_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……も、もしかして）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアノブに手をかける。"

play sound se_0282
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ガチャリと音がして、何の抵抗もなくドアが開いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……無用心すぎるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんと、エースの部屋は鍵がかかっていなかった。\n
暗い部屋の中へと足を踏み入れる。"


scene bg23_rd_nig
with dis
play sound se_0689
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薄暗がりに浮かぶ部屋は、驚くほど綺麗に整えられている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……いっそ見事なまでに、生活感のない部屋よね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "綺麗を通り越している。\n
これなら無用心なのも納得できる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ほとんど物のない、がらんどうの部屋。\n
彼らしくない気もしたし、いかにもという気もする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人に見つかってもまずいので、するりと素早く部屋の中へと滑り込む。\n
……静かだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……まあ、いるとは思っていなかったんだけれどもね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "負け惜しみのように、一人呟く。\n
普段部屋まで辿り着けないエースが、イベントだからといって自室にいるわけがないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、と。\n
一縷の望みをかけていたわけだが、やはり駄目だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（他にいそうな場所を探すのも、難易度が高すぎるし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少なくとも、イベントの時間内には無理だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「せめて、リボンだけでも奪い返したいわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生活感のない部屋の中、引き出しに手をかけてみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがに主がいない部屋で家捜しをするのは気がひけるが、触れてみたそれは異様に軽い。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「…………」"

play sound se_0630 volume .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそるおそる、引いてみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中に何か入っているようだったらすぐに戻そうと思ってはいたのだけれども、結果は案の定。\n
中には何も入っていなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「あのテント、やたら色々あると思っていたけど……。\n
……あんな人を魔法使いにしちゃいけないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "テントを持ち歩いている時点で色々言いたくなるが、この調子だとエースは生活に必要なものすべてを魔法でもって持ち歩いているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただでさえふらふらしているのに、ものの持ち運びという一番不便を感じないといけないところまで魔法で解決してしまっていては、どうしようもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ますます根無し草に磨きがかかるばかりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「私のリボンも、持ち歩いていそうよね……。\n
そもそも、ストームの夜から、こっちに戻ってきているのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "戻ってきてはいなさそうだ。\n
ベッドメイキングは完璧で、一切の乱れもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "はあ、と溜息をついて、皺一つないシーツへと腰掛けた。"

play sound se_0327
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろいろと覚悟を決めて、リボンを奪い返し、尚且つ気持ちの所在だとかまではっきりさせたかったのに、これではどうしようもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今から外に出ても、エースを見つけることは出来ないだろう。\n
使用人達が見逃してくれる外出の範囲は、中庭の往復程度だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それより外ともなれば、通常通りの警備体制であることが予想される。"


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……失敗ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼやいて、エースの部屋の窓辺で不貞腐れたように頬杖をついた。\n
さらさらと、頬を撫でていく夜風が気持ちいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

play sound se_0533
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ポケットから、惚れ薬を取り出した。\n
エースに飲ませてやろうと思っていたものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、この場に本人はいない。\n
手の中でその小瓶を弄びながら、深々と溜息を吐き出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……むなしい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、なんだか苛立ってきた。"



scene bg06_sk_h_day
with dis

scene bg06_sk_h_eve
with dis

scene bg06_sk_h_nig
with dis

scene bg06_sk_h_day
with dis

play music forest_thick_day_p_wam

show ace_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice ace_g0326
Ace "「……なんだか、苛立っている？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「……へえ？\n
分かるの？あなたのせいよ？」"

hide ace_m_01_2
show ace_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice ace_g0327
Ace "「俺のせい？なんで？\n
言いがかりは酷いぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「～～～～！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「リボンを返しなさいよっ！\n
予備がないと困るのよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "リボンなんて滅多に汚れるようなものではないが、それでも三日に一度ぐらいは洗いたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして洗濯に出している間は、どうしたって予備が必要なわけだ。"

hide ace_m_03_9
show ace_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0328
Ace "「だって君、ブリーズの夜に取りに来てくれなかっただろ？\n
それってつまり、俺にくれるってことじゃないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「違うわよっっ！\n
あなたの部屋まで行ったけど、あなたがいなかったの！！」"


scene bg13_fr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後、占い学の術を駆使して学園内でエースを探す。\n
今日は、限りなく学園の外側に近い森の中にいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこに行こうとしたら、こんな場所に辿り着いたのかが疑問だ。\n
そして、ここまで私が追い掛け回す理由も疑問。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "リボンの件があったとしても、ここまで追うほどに不便はない。"

hide ace_m_01_6
show ace_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0329
Ace "「へえ、君、俺の部屋に来てくれたんだ？\n
どうだった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……何にもない部屋だったわね。\n
生活に必要なものですら、何にも」"

hide ace_m_03_10
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice ace_g0330
Ace "「うんうん、生活に必要なものは常に持ち歩いていないとな！\n
占い学の授業で、どんなラッキーアイテムを言われても対応できる自信があるぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「……無駄な自信ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「とにかく、リボンを返してよ。\n
生活必需品じゃないでしょう」"

hide ace_m_03_3
show ace_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0331
Ace "「ははは、駄目だよ。\n
これは俺が貰ったんだ、戦利品を人に譲るわけにはいかないな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「戦利品の持ち主が返還を求めているんだから、おとなしく返しなさいよっ。\n
ないと困るの！」"

hide ace_m_01_4
show ace_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice ace_g0332
Ace "「それなら、今度の休み、一緒に街に出掛けようぜ。\n
ほら、最寄りの街までだったら外出許可が出るだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……それで、どうするのよ」"

hide ace_m_01_10
show ace_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice ace_g0333
Ace "「俺が君に、新しいリボンを選んであげるよ。\n
可愛いのを選ぶから、楽しみにしていてくれよな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「…………」"

hide ace_m_03_11
show ace_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice ace_g0334
Ace "「なんだよ、その微妙そうな顔。\n
物言いたげだなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「いえ、あなたと買い物に出掛けて、目的が達成できるのかしら、と思って。\n
……あなたを探すだけで一日が終わりそうな気がするの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目的地を決めて、そして片方が道を知っている状態でも平気で迷子に巻き込むのがエースなのである。"

hide ace_m_02_8
show ace_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0335
Ace "「ははは、君って心配性だなあ。\n
大丈夫だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「新しいのなんていらないわ。\n
返してくれればいいだけ」"

play sound se_0748
play sound se_0624
pause .5
play sound se_0748
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースが切り開く道なき道、その後を追って歩く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……学校内で、何をしているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「買い物に行っても、途中で迷っちゃって買えやしないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "通い慣れた……、どころか、住んでいる学校の中ですらこうなのだ。\n
学校の外になど出てしまったら、一体どんなことになるのか、想像すら出来ない。"

hide ace_m_02_1
show ace_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0336
Ace "「そうだなあ。\n
買い物が出来なかったら、また行けばいい」"

hide ace_m_03_11
show ace_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0337
Ace "「何度でも、一緒に買い物にいこうよ。\n
今と同じアウトドアデートでも、趣向が違っていいだろ？」"

play sound se_0624
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（デート？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（今の、これも？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人一緒に緑の木々の中を彷徨い歩くことを、エースの中ではアウトドアデートと呼ぶらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして森の中を歩いていて思い出すのは、ボリスの魚泥棒だったり、ヨッパライ茸の密栽培事件だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ありがたいことに、今日はまだ何のトラブルにも出くわしてはいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……このまま、平和にすめばいいんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースが言うには、私と一緒にいて遭遇するトラブルは、次第にパワーアップしていっているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "密栽培の次のレベルの非行が一体どんなものなのかは、あまり知りたくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「趣向なんて変えなくていいの！\n
リボンを早く返して欲しいのよ、私は！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "週末に何度も時間をかけて吟味してほしいわけではない。\n
手早く、エースが持っているものを返してさえくれれば、それでいいのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、エースは上機嫌にがさごそと木々を掻き分け、どこへとも知れない方向へと自信たっぷりに進んでいく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、ちらりと私を振り返って、片手を差し出した。"

play sound se_0313
hide ace_m_01_1

show m_ace_goodend1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0338
Ace "「だったらさ、俺が迷わないように、手を握っていてくれよ。\n
そうしたらきっと、買い物も無事にすむ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見返りざまに、爽やかに笑う横顔を見る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな様は、レディをエスコートする紳士の立ち振る舞いにも見えるが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼が私を連れて行こうとしているのは生い茂る緑の向こうの、いずことも知れないどこかだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこがどんなところかも分からない癖に、こうして迷いなく私を巻き込む。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……はあ。\n
あなたって本当、仕方のない人よね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice ace_g0339
Ace "「放っておけないだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ええ。\n
あまりに、どうしようもない人だから」"

play sound se_0361
hide m_ace_goodend1
show m_ace_goodend2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼやいて、私はそれでもエースのその手をとった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（魔法のせいよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice ace_g0340
Ace "「奇遇だね。\n
俺も、君のこと、放っておけないんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋の魔法などという、ふざけた暗示か。\n
その反動で。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0341
Ace "「君が、どうしようもない子だから」"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅっと大きな手に握り返されて、手を引かれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "片手で彼と手を繋ぎ、もう片手でポケットの中の小瓶を握り締めた。"

hide m_ace_goodend2
show bg06_sk_h_day onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（いつか……、どこかで、チャンスさえあれば）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "連れて行かれるのは一体どこなのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ポケットには、小瓶。\n
出鱈目な恋の魔法と、効き目も不明な惚れ薬。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この人と一緒だと、どんな世界を見ることになるのだろう。"

hide bg06_sk_h_day
with dis

hide  frame_par_togaki
hide  ali_m_06_16
with Dissolve(5)
scene black with Fade(5)

stop music
##endmemory
$ renpy.movie_cutscene("endroll_b.mpg")
label gakuen_ace6_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……やっぱり）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……覚悟はしていたけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予想通り、というかなんというか、ノックに対する反応はない。\n
おそらく……、いや、間違いなく、部屋の中はもぬけの殻だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（エースが自室にいるなんて、ありえないのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手は年がら年中彷徨い歩いているエースだ。\n
どうせ今日だって、どこかで迷子になっているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初から予想していたことだ。\n
試しにドアノブへと手をかけてみる。"

play sound se_0282
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……無用心すぎるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんと、エースの部屋は鍵すらかかっていなかった。\n
暗い部屋の中へと足を踏み入れる。"

play sound se_0689

scene bg23_rd_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薄暗がりに浮かぶ部屋は、驚くほどに綺麗に整えられている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……いっそ見事なほどに、生活感のない部屋よね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "綺麗を通り越している。\n
これなら無用心なのも納得できる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ほとんど物のない、がらんどうの部屋。\n
彼らしくない気もしたし、いかにもという気もする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「……さてと、始めますか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は自らに気合を入れるべく、そう呟いて行動に出る。\n
そのために、今日の昼、わざわざペーターに会いに行ってきたのだ。"

with dis
$ hi_mes()

scene bg23_rd_day_s
with dis

scene bg27_rk_day_s
with dis

scene bg27_rk_day
with dis

play music corridor_day_p_wam

show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0337
Peter "「[firstname]！！！\n
ああ、あなたが僕に会いに来てくださるなんて、まるで夢のようです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「いや、今夜、ブリーズがあるから……」"

hide per_m_02_5
show per_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice pet_g0338
Peter "「ああ、そういえば、今日はブリーズだとかいうくだらないイベントがあるんでしたよね！\n
……は！！」"

play sound se_0313
hide per_m_03_3
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice pet_g0339
Peter "「もしかして僕の部屋の場所を聞きに！？\n
ああ、それならくだらなくなんてありません！くだらなくなんてありませんとも！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「違うわよ。\n
……ブリーズのことで相談をしにきた、というのは当たっているんだけれども」"

hide per_m_02_13
show per_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice pet_g0340
Peter "「僕に、相談！？なんでしょう！？\n
あなたのためなら僕、なんでもします！」"

hide per_m_01_2
show per_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice pet_g0341
Peter "「ああ、分かりました！\n
使用人連中が邪魔だというのなら、全員僕がまとめて始末を……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「そういったことは結構よ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……あのね？\n
エースって、普段放浪しているじゃない？」"

hide per_m_02_2
show per_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice pet_g0342
Peter "「エース君？\n
そうですね、エース君は可哀想になるほどに頭が悪いので、常に迷子です」"

hide per_m_03_9
show per_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice pet_g0343
Peter "「それが、どうかしましたか？\n
ああ、エース君に死んでほしいんですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……落ち着きなさいよ、あんたは。\n
お願いだから、もうちょっと人の話を聞いてくれないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_16")
T "（そんなでっかい耳があるんだから……）"

hide per_m_03_7
show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_16")
voice pet_g0344
Peter "「はいっっ！！\n
あなたの言葉ですからね、一言一句聞き漏らしのないように、しっかり聞いていますとも！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「まあ、いいわ。\n
それで聞きたいんだけど……、エースって普段の授業はどうしているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは、学校なのだ。\n
通常の生徒ではなく、研究員だとしても、それに応じたゼミや会議がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、エースがまともにそれらに参加しているとは思えない。\n
何か、あるはずだ。"

hide per_m_02_5
show per_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「……？」"

hide per_m_02_10
show per_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0345
Peter "「どうして、あなたがエース君のことを、そんなに気にするんですかっ？\n
エース君のことなんか、どうでもいいじゃありませんか！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……いいのよ、別に。\n
ペーターが教えてくれないなら、誰か別の人に聞きにいくから」"

hide per_m_01_4
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
Peter "{size=+20}「！！！」{/size} "

hide per_m_02_3
show per_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice pet_g0346
Peter "「行っちゃ嫌ですっっ！！\n
話しますから！！僕がちゃんとお話しますから！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「最初から、そう言えばいいのよ」"

hide per_m_01_6
show per_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pet_g0347
Peter "「うう……、エース君ってほら、アレじゃないですか。\n
死んだほうがいいぐらいの方向音痴じゃないですか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……死んだほうがいいかどうかはさておき、方向音痴よね。\n
だから、自力じゃ授業に出ることも出来ないと思ったんだけど……」"

hide per_m_01_13
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice pet_g0348
Peter "「さすがはあなた……！！\n
そうです、エース君が自力で授業に参加出来るわけがありません！」"

hide per_m_02_13
show per_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice pet_g0349
Peter "「今日の授業に間に合わせようと思ったら、最低でも三日前には出発しないと着かないような男ですからね！！」"

hide per_m_03_2
show per_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice pet_g0350
Peter "「いえ、三日前でも辿り着くかどうか！\n
本当ろくでもない男なんです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「それじゃあ、どうやって学校活動に参加しているの？\n
まさか、まったく参加していないわけじゃないんでしょう？」"

hide per_m_03_9
show per_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
Peter "「…………」"

hide per_m_02_7
show per_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pet_g0351
Peter "「エース君が参加している授業や行事には、当番があるんですよ。\n
……忌々しいことに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「当番？？？」"

hide per_m_01_1
show per_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice pet_g0352
Peter "「時間が近付くと、エース君を召喚するんです。\n
魔法で」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「ええ！？\n
そんな大層な……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法学校では普通のことなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「まあ、確かにそれなら、エースでも授業に参加できるけど……」"

hide per_m_02_11
show per_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0353
Peter "「エース君なんて、永遠に学校内を彷徨い歩いて、新しく学校の七不思議にでも何でもなってしまえばいいんですよ」"

hide per_m_03_5
show per_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0354
Peter "「それで……、[firstname]、あなたはどうしてそんなことを知りたかったんですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「え？\n
いや、たいしたことじゃないんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ああ、そうだ。\n
ペーター、もう一つお願いがあるの」"

hide per_m_02_9
show per_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0355
Peter "「お願い！？何ですか、何をしたらいいんですかっっ？\n
僕、あなたのためなら、何でもします！！」"

hide per_m_02_12
show per_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0356
Peter "「何なりとおっしゃってください！\n
あなたの命令でしたら、何だってやり遂げてみせますから！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「本当？」"

hide per_m_01_2
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_3")
voice pet_g0357
Peter "「本当ですとも！\n
あなたに僕が嘘をつくとでも！？」"

hide per_m_02_3
show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_3")
voice pet_g0358
Peter "「さあ、何でもどうぞ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「それなら、その言葉に甘えさせてもらうんだけど……」"

hide per_m_02_5
show per_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice pet_g0359
Peter "「ええ、ええ！\n
さあ、どうぞ！遠慮なく！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「そのエースの召喚方法の詳細が知りたいの。\n
……ああ、それと、エースの部屋の位置もね？」"

hide per_m_03_11

with dis
$ hi_mes()

scene bg27_rk_day_s
with dis

scene bg23_rd_day_s
with dis

scene bg23_rd_nig
with dis

play music night_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……ペーター、ショックを受けていたわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真っ白に燃え尽きたようになっていたペーターのことを思い出す。\n
もちろん、その後はお決まりの大騒ぎ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは、私が悪い病気にでもかかったのか、それとも洗脳でもされたのかと大袈裟に騒ぎたてたが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局最後には私の命じるままに、私の欲しがった情報を教えてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がこうしてエースの部屋に辿り着けたのは、あの下僕体質の幼馴染のおかげだ。\n
彼も、ある意味、私に洗脳されていて最終的には言うことをきいてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（まあ、エースに対しての洗脳やら病気やらっていうのも、間違っていないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がここにいるのはエースの実験とやらのせいなのだから。\n
実験などでなくとも、あれからエースのことが気になってしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……私まで、迷子だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースに出会ってしまい、道筋はおおいに狂ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（シンフォニアに入って、恋愛関係で振り回されるようになるとは思わなかった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せいぜい、勉強で苦労するとしか予想していなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（まさか、恋愛関係で……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……恋愛関係？\n
恋愛、なのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋のまじないをやるくらいだ。\n
そうではないと否定は出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "懐からチョークとメモを取り出した。\n
メモには、ペーターが渋々ながらに書いてくれたエース召喚用魔法陣の見本が描かれている。"

play sound se_0472
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを正確に真似て、私は床の上へと魔法陣を完成させていった。"

play sound se_0459
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……よし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "我ながら上出来だ。\n
床に屈むと、そのチョークで書き上げたばかりの魔法陣へとそっと手で触れる。"

play sound se_0496

show magic_y onlayer master with Dissolve(1.5)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまた習ったとおりに、力ある言葉を解き放つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来召喚というのは、難易度の高い魔法なのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このエース召喚の魔法に関してはクラスで当番制ということもあり、教師が誰でも出来るようにと調整してあるのだそうだ。"

play sound se_0724
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手から伝わる魔力が、魔法陣へと流れ込んで光を放つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その光が段々と強くなっていき……。"

play sound se_0708
show white onlayer master with expand
hide magic_y
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あまりの眩しさに私も目を閉じる。\n
そして、次の瞬間。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0342
Ace "「あれ？\n
どうして俺が、こんな時間に召喚されるんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0343
Ace "「こんな時間に授業や用事があるとも思えないし……。\n
あれ？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "訝しげなエースの声が響いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……よかった）"

hide white

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "召喚魔法は、無事成功したらしい。\n
失敗して、何か得体のしれないモンスターでも呼んでしまったらどうしようかと思っていた。"


show ace_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0344
Ace "「[firstname]、君が俺を召喚したのか？\n
なんで、君が俺の召喚魔法を知っているんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ペーターに聞いたのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「どうやって授業や学校行事に参加しているのか、ずっと気になっていたんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「まさか毎回召喚魔法で呼ばれているとは思わなかった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いちいち召喚しないといけない風紀委員。\n
たいしたモンスターだ。"

hide ace_m_02_2
show ace_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0345
Ace "「ははは、風紀委員たるもの、何でも自力でやり遂げたいんだけどな。\n
状況が許さないこと、っていうのもあるんだよ」"

hide ace_m_02_3
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0346
Ace "「教授達ときたら、このままだと永遠に卒業できない、なんて脅かすんだぜ？\n
はは、酷いよな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……それ、脅しじゃなくて事実だと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……この人、研究員じゃなかったんだ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一般生徒の扱いらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（駄目な人……）"

play sound se_0695 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "スカートの裾をぱたぱたと払い、立ち上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースの自主性に任せていたら、一年のうちに何度授業に参加できるか、といったような惨状になるのは目に見えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア最長滞在記録を更新してしまいそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（いや……、不老不死の教授とかもいるらしいから定かじゃないな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "研究機関としてはままある話だが、学年をはじめ、どこまでが生徒か研究員か、境が曖昧なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "制服を着ていても、関係者であって生徒ではなかったりする。"

hide ace_m_03_3
show ace_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0347
Ace "「それにしても……。\n
ペーターさんが、よく君にその召喚魔法教えたよなあ」"

hide ace_m_01_3
show ace_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0348
Ace "「君、ペーターさんの弱みでも握っているの？\n
俺も知りたいな、それ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ペーターは、私の言うことなら何でも聞いてくれるの。\n
騒ぎながらも、最終的にはね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「だから、あなたの部屋の場所だって教えてくれたわ」"

hide ace_m_03_2
show ace_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice ace_g0349
Ace "「ああ、ここやっぱり俺の部屋だったんだな！\n
どうりで見覚えがあるはずだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の部屋だというのに、「見覚えがある」程度でしかないというのは大問題だと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は呆れて息を吐き、まるでそのタイミングを狙ったようにエースが言葉を続けた。"

hide ace_m_02_4
show ace_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0350
Ace "「それにしても、君、ペーターさんと仲いいんだね。\n
私の言うことなら何でもきく、なんて、普通なかなか言えない台詞だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまでと、何も変わらない調子だというのに、その言葉はどこか空寒く感じられる。\n
ストームの夜に感じたのと、同じ冷気だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……何を勘違いしているのか知らないけど。\n
ペーターは、私の幼馴染よ」"

hide ace_m_03_12
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0351
Ace "「うん、知っているよ？\n
ペーターさんに散々自慢されているからね！」"

play sound se_0216
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう答えながら、エースは魔法陣から抜け出て、私へと一歩を踏み出す。"

menu:
    "後ずさる。":
        jump gakuen_ace6_5a
    "逃げない。":
        jump gakuen_ace6_5b
label gakuen_ace6_5a:
play sound se_0593
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逃げる必要なんてないと分かっているのに、後ずさってしまっていた。\n
彼が距離を詰めた分だけ、後ろへ下がる。"

hide ace_m_03_3
show ace_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0352
Ace "「酷いなあ、そんな反応、傷つくぜ。\n
自分から男の部屋に来ておいて、今更逃げるなんておかしいと思わないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「そ、そういう言い方……」"

hide ace_m_02_8
show ace_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice ace_g0353
Ace "「言い方も何も、君が自分から来たんだよ。\n
遠慮なんか、するほうが失礼だよな！」"

jump gakuen_ace6_6
label gakuen_ace6_5b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無意識のうちに半身引きかけたのを意志の力で引き戻した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結果、私は距離を詰めてきた彼から逃げずに向かう。"

hide ace_m_03_10
show ace_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0354
Ace "「……逃げなくて、いいの？\n
ここは、俺の部屋だぜ？」"

hide ace_m_01_11
show ace_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0355
Ace "「女の子が男の部屋に一人で入るなんて……、どういう意味か君、ちゃんと分かっている？」"

hide ace_m_03_10
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0355_5
Ace "「……分かっていなくても、遠慮する気なんてないけどな」"

jump gakuen_ace6_6
label gakuen_ace6_6:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつも通りに爽やかな様子で、エースは行動に出た。"

play sound se_0210

show m_ace6_1and6_6 onlayer master
with dis
hide ace_m_03_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "右腕が素早く私の腰を攫って、足元が浮いたと思った次の瞬間には、ばふんっと音をたてて背中からベッドに着地していた。"

play sound se_0327
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま、私に抵抗する余地を与えることなく、エースは体の上に乗り上げてくる。流れるような、一連の動作に眉根を寄せる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……慣れているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice ace_g0356
Ace "「はは、当然だろ？\n
暴漢を取り押さえるのは風紀の仕事だから、そりゃあ慣れもする」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice ace_g0357
Ace "「あ、それとも女の子を押し倒し慣れているとでも思った？\n
[firstname]、君、妬いてくれたのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分かっていて聞いている。\n
笑顔の憎たらしい男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……ええ、そうよ。\n
妬いているの」"

hide m_ace6_1and6_6
show m_ace6_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
Ace "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "短く肯定してやれば、エースの目が丸くなった。\n
普段仮面でも貼り付けたように笑っている彼の顔から、笑顔が消える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "素の顔、とでもいえばいいのだろうか。\n
無防備な顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな彼に向けて、私はにっこりと笑って見せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「あのね、エース。\n
私、あなたに責任をとってもらいに来たの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Ace "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「責任、取ってくれるって言ったでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まっすぐに、エースを見上げて言う。\n
ほとんど告白のような言葉だというのに、まるで決闘を申し込むかのような緊張感があった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は答えない。\n
ぴりぴりと、刃のような空気だけが伝わる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「だから……」"

hide m_ace6_2
show m_ace6_3 onlayer master
with dis
play sound se_0533
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ポケットの中から、黒っぽい粉の入った小瓶を取り出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「あなたにかける、恋の魔法も用意してきたわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（こんな物まで用意した私を、どうするの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼が私にかけた、恋の魔法とやらを解いてしまうのか。\n
それとも……。"

hide m_ace6_3
show m_ace6_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Ace "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
Ace "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……間が長い）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴりぴりとした緊張状態が続くのはいただけない。\n
痛いほどの空気に、私のほうがもたなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……エース。\n
なんとか言ったらどうなのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice ace_g0358
Ace "「……なんとか」"

hide m_ace6_4
show m_ace6_5and6_11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "{size=+20}「……！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなときまで人を食ったようなことを言い出すエースに腹が立って、振りだけでも殴ってやろうと腕を持ち上げた。"

play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、その小瓶を握ったままに振りかぶった腕は、エースに届くより先にあっさりと捕らえられてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「何なのよ……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せめて大人しく殴られてくれれば、可愛げもあるものを。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（そんなガラじゃないのは、充分分かっているけど）"

hide m_ace6_5and6_11
show m_ace6_1and6_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0359
Ace "「それが、君が俺に用意してくれた魔法？\n
……飲むの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「一応、飲み薬よ。\n
飲ませるために作ったの」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……まあ、即効で効くようなものじゃないけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "料理か何かに混ぜて、意中の相手に少しずつ服用させるというのが正しい使い方だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（でも、毎食の料理に混ぜ物を出来るくらいなら、おまじないなんて必要ないわよね、普通）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "毎食盛れるくらいの距離ならば、その時点で恋に勝っている気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、あいにくエースとそんな関係にない。混ぜて効果があるのなら、一気飲みしてもらったならばきっともっと効果があるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……そういうことにしておこう）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_g0360
Ace "「惚れ薬……、なんだよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、胡散臭そうに私の手の中にある小瓶を眺めている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「ええ、せっかく作ったんだから飲んでよ。\n
リクエストに応えて、用意したんだから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋の魔法を自分にもかけてくれと言ったのは彼だ。\n
手首を彼に押さえつけられたまま、声だけでそれを彼へと突きつける。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0361
Ace "「恋の魔法薬か。\n
……材料、何か聞いてもいい？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「聞かないほうがいいと思うわ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イモリの黒焼きを筆頭に、あんなものやこんなものがミックスされていると知れば飲む気も失せてしまうだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0362
Ace "「……ふうん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "即答した内容に、エースは露骨に眉を寄せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Ace "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……困らせることが出来ているみたいだし、いいかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "半ば本気で、飲ませてやろうと思っていた。\n
だが、冷静になると、自棄としか思えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「エース、冗談よ。\n
別に本気でこれを……」"

hide m_ace6_1and6_6
show m_ace6_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0363
Ace "「……いや、いいんだ。\n
せっかく作ってくれたんだもんな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "眉を寄せたエース。\n
が、それがすぐにいつもの笑みに変わった。"

play sound se_0132
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょいと手の中の小瓶を奪われる。\n
まさか、飲む気になったのだろうか。"

hide m_ace6_7
show m_ace6_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！？」"

play sound se_0096
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の仕業なのか、蓋は閉じたままの小瓶の中にじわじわと黒く重たそうな色が生じた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "黒い液体に溶けて、なにやらどろりとしたとんでもない様子に変わっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（何をしたのよ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何であろうと、いいことには思えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「も、元から危険そうだったのに……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "更に危険そうに……。\n
……とても飲めそうもないようなものに変わっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0364
Ace "「あはは、強烈な毒薬っぽいよな。\n
これ、飲んだら死んじゃいそうだぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースの呟きは、いちいちもっともだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……どう見ても毒薬だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ねっとりと黒いそれは、いかにも飲みにくそうに見える。\n
作った私ですら、こんなものを飲むなんて冗談じゃないと思ってしまうのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくらなんでも、これを飲めというのは酷な話かもしれない。\n
……ここまでにしたのは、エースだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（むしろ、これを飲んでくれることが愛情というかなんというか、そういったものの証明になりそうよね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これを飲んだから、そういった感情が芽生えるのではなく。\n
こんなシロモノを飲んでくれるだけの愛情、というか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（いやいや、本来はバレないようにこっそり混ぜるのが正しい使用法なのよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真っ向から、魔法薬を飲め、だなんて。\n
半分嫌がらせのようなつもりだったとはいえ、使用法を間違えすぎている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0365
Ace "「仕方ないよな、君からの愛情だ。\n
……飲めばいいんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……っ！！\n
の、飲むの？本当に？」"

hide m_ace6_8
show m_ace6_9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice ace_g0366
Ace "「だって、これが君の俺への魔法なんだろう？\n
これを飲んだら……、君は俺を好きになる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「そ……っ、それ、意味が反対でしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice ace_g0367
Ace "「反対？そんなことないさ、同じだろ？\n
君を好きになった俺を、君は好きになる」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice ace_g0368
Ace "「自分の作った薬で君を好きになった俺を、君は好きになる。\n
だって、君にはその責任があるから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（責任……）"

hide m_ace6_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "縛られ、縛り付けるもの。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "胸が痛むような、高揚するような、不思議な感覚だ。\n
責任をとれといったのが逆の立場になっている。"

play sound se_0668
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の視線の先で、エースが小瓶へと口をつけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！！\n
待って……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "止めるより先に、どろりとした漆黒の液体をエースがあおった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Ace "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはりとんでもない味がしたのか、エースの眉間に皺が寄る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして……、彼は笑った。\n
ニヤリと、すこぶる嫌な予感をさせる顔で。"

play sound se_0051

show m_ace6_10and6_13 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼が何をするつもりなのか気付いたときにはもう手遅れだった。\n
焦げ臭いような異臭が押し付けられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "必死に抵抗して引き絞る唇を、器用に割り入って侵入してくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っん！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この男の舌を噛み切ってやりたい。\n
そんな衝動に駆られるものの、どろりと流し込まれる液体の衝撃に頭の中が真白になった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_6")
T "（お、おまじないなんて……っ、おまじないなんて……！\n
やっぱり当てにならないわ……！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなものを飲まされて、恋に落ちるわけがない。\n
こんな恐ろしいものを制作した相手に恋心など抱くわけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋心ではなく、殺意がわいてくる。\n
長く口の中に留めていたくなくて、必死に喉を鳴らして飲み込む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "水が欲しい。\n
新鮮な、ごくごく普通の水が欲しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、口移しで半分以上飲まされて、ようやく唇が離れていった。"

hide m_ace6_10and6_13
show m_ace6_5and6_11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0369
Ace "「……どう？\n
俺のこと、好きになった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……～～～～っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「殺したくなったわ……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice ace_g0370
Ace "「……へえ、それはそれは。\n
熱烈だね、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_5")
T "「……～～～～っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "涙目になっているのが分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "断じてキスのせいじゃない。\n
恐ろしい味のした毒薬のせいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0371
Ace "「おかしいなあ。\n
……ああ、でもそうだよな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0372
Ace "「君のことを好きになる薬だったなら、君が飲んでも意味がないのか。\n
それとも、ナルシストになるのかな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「知らないわよ！\n
もう、どいてよ！」"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「ああ、もうあなたなんて大っ嫌い！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_13")
voice ace_g0373
Ace "「嫌いになる薬じゃないはずだぜ？\n
……失敗作？君って、薬学の成績悪いんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_9")
T "「薬のせいじゃなくて、あなたが薬をあんなふうに無理矢理飲ませるような人だから嫌いなの！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_9")
voice ace_g0374
Ace "「やっぱり、薬が原因なんじゃないか。\n
薬学は勉強しておいたほうがいいぜ～？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_9")
T "「～～～～～～！」"

play sound se_0044
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の上に乗る彼を押しのけようと、無茶苦茶に暴れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0375
Ace "「あはは、可愛いなあ。\n
俺、君のそうやって泣きそうになりながらも、無駄に意地を張るところ大好きなんだ」"

play sound se_0044
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0376
Ace "「……でも、意地を張りきれなくなった君は、もっと好きだよ。\n
好きを飛び越えた好き……、なんて言えばいいのかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0377
Ace "「強い君が折れてくれるのって、すごくいい気分だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice ace_g0378
Ace "「……想像以上に、いいよ。\n
すごく、いい」"

play sound se_0044
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ろくでもない男が、さわやかな笑顔で、ろくでもないことをのたまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "暴れてもがく私の体を、器用に分散した体重で難なく押さえつけて言う。\n
好き、との言葉は薬の成果なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あんまり嬉しくない。\n
それどころか、いらっとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……部屋に、いなかったわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの日には、メイドを脅して私の部屋まで案内させた男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日だって、メイドなり使用人なりに案内させて自室に辿り着くことは出来たはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自室である分、女子寮にある私の部屋に案内させようとするよりも、簡単なことだ。\n
それなのに、エースはそうはしなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズというイベントの日に、わざと部屋を空けていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……試したの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意地っぱりな私を知っていて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が、苦労して彼を探し出すかどうか。\n
それだけ彼に、執着しているのかどうかを。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……っ！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かあっと頬に熱が昇る。\n
ペーターから彼召喚のための魔法陣や、手順を聞きだしてきた私は、まんまとそれにのせられてしまったということか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……あなたなんて、大っ嫌いだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice ace_g0379
Ace "「その台詞、先刻も聞いたぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「大嫌いを飛び越えた、大嫌いなの！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice ace_g0380
Ace "「俺の真似？\n
じゃあ俺は、君のこと、大好きを飛び越えて、大好きだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……嘘つき」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0381
Ace "「本当だよ。\n
君のことを好きにならせてくれて、ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「ふざけているようにしか聞こえない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice ace_g0382
Ace "「ふざけてなんかいないよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言う彼は、笑っているが、確かにふざけているようには見えない。\n
……目が笑っていないから。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（怖……）"

hide m_ace6_5and6_11
show m_ace6_12 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……あなたの傍にいると、私まで迷うの。\n
迷わされて、訳が分からなくなっちゃうのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "挙句、こんなおかしな薬まで作った。\n
正常なときの私なら、奇行としか思えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0383
Ace "「いいじゃないか、迷子。\n
一緒に迷えばいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ゴールがあるかも分からないのに？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目的地があるのかどうかすらも分からない、迷子だ。\n
この男は平気で、そんなろくでもない迷路に人を巻き込む。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0384
Ace "「一緒に探せばいいじゃないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返される言葉は、途方に暮れる迷子を励ます爽やかな男といったふうに響く。\n
まるで俺に頼っていれば何にも問題なんかない、というように。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……そもそも、迷子の原因はあなたでしょうに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷いやすいのは自分も同じと、知っているが。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0385
Ace "「ずっと……。\n
俺に迷っていれば、いい」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0386
Ace "「俺と……。\n
……迷おうよ、[firstname]」"

play sound se_0051
hide m_ace6_12
show m_ace6_10and6_13 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……っん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌がらせのような囁きと一緒に、キスが落とされる。\n
道には迷ってばかりいるくせに、行動がやたら素早いのもエースらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "押さえ込まれたまま、口付けられる。\n
今度は、まともなキスだ。"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、かすかな苦味は残っている。\n
自然、胸が浮き、その背に手を差し込まれ、引き寄せられるようにして距離が近くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "落とされたキスに、条件反射のように瞼を閉じたものの、エースがどんな顔をしているのか気になって、うっすらと覗く。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（～～～っっ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一気に頬に熱が昇った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "散々迷子になれだとか迷子は楽しいだとか言っていた癖に、私を抱きしめて口付けるその顔は、ようやくゴールに辿り着いた旅人か何かのように穏やかだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目が合いそうになってすぐに閉じたので、もしかしたら見間違いだったのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ああ……、先刻の顔、好きだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（……大嫌いな男だけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを打ち消すほど、好きだ。\n
先刻の顔は……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、すぐ目を閉じた。\n
開けない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好きなのに……。\n
……見ていられないほど、好きだと思った。"

play sound se_0055
hide m_ace6_10and6_13
show m_ace6_14 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースの背に、腕を回す。\n
ぎゅう、とその背中が皺になるほどに強く捕まえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0387
Ace "「……っ。\n
……なんだ、もっとキスしてほしいのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……違うわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice ace_g0388
Ace "「ふうん？\n
……はは、違っていてもするけどな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（じゃあ、聞かないでよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうしている間は、迷わないでいられる。\n
私も、エースも、迷わない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "捕まえていられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……責任、なんて）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この一時、囚われていることを忘れさせてくれる。"

hide m_ace6_14

with dis
$ hi_mes()

scene bg25_rr_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_ace_end
