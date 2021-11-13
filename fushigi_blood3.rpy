jump fushigi_common3_castle
label fushigi_blood3_1:
$ fushigi_blood3_6a_seen = False
scene charasel_bg_castle_day
with stripe_l_medium

scene hm_spr_01
with stripe_l_medium

scene v_01
with stripe_l_long

play music vivaldi_t_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「………ねえ、ビバルディ」"


show viv_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice viv_f0339
Vivaldi "「なんじゃ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「これは……、ひょっとしてまたこの前と同じで、取り寄せたの？」"

hide viv_t_01_4
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice viv_f0340
Vivaldi "「おお、可愛いだろう？\n
この前は服ばかりで、小道具が足りなかったからな」"

hide viv_t_01_3
show viv_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice viv_f0341
Vivaldi "「今回は靴等も幅広く集めてみた」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城に仮住まいして、数十時間帯が経った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "てっきり一度で飽きたと思っていたのだが、ビバルディは再びお人形遊びをしようと言い出した。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（この調子で増やされたら、衣装部屋がいくつあっても足りないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "前回のドレスと同じように、今回は装飾品が山のようにビバルディの部屋に持ち込まれていく。"

hide viv_t_01_10
show viv_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0342
Vivaldi "「これは紐で結ぶタイプの靴でな、先端の飾りが可愛いだろう？\n
おお、確かセットでバッグも付いておったはず」"

hide viv_t_01_4
show viv_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0343
Vivaldi "「どこにしまったかのう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（何だか、ますますパワーアップしている気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "楽しそうに小さな靴を見ているビバルディは終始上機嫌だ。\n
これで無闇な斬首が減るのなら、いくらでも遊びに付き合うところだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（確か、あれは私の人形遊びって言っていなかったっけ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飾り立てられるべき人形（ただし女王様）のほうが楽しんでいるような気がしないでもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（まあ、ビバルディが楽しんでくれているのならいいんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何だかんだと彼女が私に甘いように、私も彼女に甘い。\n
友達が楽しそうにしているのを見て、悪い気はしない。"

hide viv_t_01_11
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0344
Vivaldi "「それに、ドレスはあやつが持ってくると申しておったからのう。\n
さて、どんなものを持ってくるのか、考えるだけでも楽しみじゃ」"

hide viv_t_01_3
show viv_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0345
Vivaldi "「粗末なものを持ってきたら、首を刎ねてくれる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「……私は楽しみというよりも不安だけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ普段の彼の服は、{size=+20}あれ{/size}だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（今までに贈られたドレスは、頭に来るぐらいにセンスがよかったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドが贈ってきたものは、服だけに留まらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "装飾品を含んでいたこともあったし、ときには補整下着まですべてセットで贈られたことさえある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（あれだけ人の身体の寸法を知っておきながら、いまさら採寸なんて……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鏡の前で採寸された記憶が蘇って、口元が引きつった。\n
いくら口実にしてもやりすぎだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（ビバルディとは結構うまくやっているように見えたのに、あの～～～～～～）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「…………」"

hide viv_t_01_4
show viv_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice viv_f0346
Vivaldi "「む？\n
どうしたのだ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここはハートの城の、女王様の部屋だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本来であれば彼らの関係を口にするのは、あの場所だけだと決めているが、聞いてみてもいいのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「ビバルディは、ブラ……。\n
ううん、あの人とああいうふうに過ごして、どうだった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「楽しかった？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の知らない、二人。\n
ビバルディがハートの女王に選ばれるまでは続いていたであろう、姉弟の過去。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（もし、役持ちにならなかったら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らはあんな風に、過ごしていたのかもしれない。"

hide viv_t_01_11
show viv_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0347
Vivaldi "「どうだったとは？\n
おまえも変なことを聞くね、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふっと口元を緩めたビバルディは小道具から手を離して、私を手招きしてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誘われるままに近づいて、床に腰を下ろした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……何だか、意外と楽しそうに見えたから」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（多分、元々の姉弟仲はそれほど悪くなかったんだろうな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "役を持つ前のビバルディとブラッドがどう過ごしていたのか、私はほとんど知らない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドに聞いたこともあるが、彼は当時のことを知られるのを嫌がってほとんど語ってくれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たまにビバルディがそれを匂わすことを言うだけでも、過敏に反応する。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（でも、それだけ親しかったっていうことだものね）"

hide viv_t_01_5
show viv_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice viv_f0348
Vivaldi "「……そうだな。\n
楽しくなかったとは言わぬよ」"

hide viv_t_01_11
show viv_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice viv_f0349
Vivaldi "「どんなゲームであれ、楽しまなければならぬからのう。\n
それはわらわだけに限ったことではない」"

hide viv_t_02_12
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice viv_f0350
Vivaldi "「あやつも同じようなものだろう。\n
遊ぶと決めた以上は、徹底する」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの細い指が私の腕を掴んだ。\n
優しく引き寄せられ、温かな膝に迎え入れられる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「ゲームだから。\n
それだけが理由？」"

hide viv_t_01_3


show bg_gen_sky_spr_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（本当は大切なんじゃないの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城と帽子屋屋敷が争っているのは、今に始まったことではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が来る前から戦いは続いていた。\n
きっとこれからも遊園地を含めての三すくみは、変わらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だって、それはずっと前から知っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（こんなことを気にしてしまうのは、多分、姉さんやイーディスのことを思い出したからなんだろうな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "妹がいたら。\n
姉がいたら。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "置いてきたものに対しての苦い責任感と、罪悪感。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0351
Vivaldi "「そうじゃ、役についた以上ゲームを続けなければならない。\n
ルールを破れば、おまえとこうして過ごすことも出来なくなる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭を撫でるビバルディの指が気持ちいい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（いい匂い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女はいつでも薔薇の香りを身に付けている。\n
私の本来滞在している場所で、あの人が付けているものと似て非なる香り。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0352
Vivaldi "「おまえも知っているように、わらわは可愛いものが好きじゃ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0353
Vivaldi "「そして、ゲームは本気でやらねばつまらぬ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0354
Vivaldi "「感傷に流され、手抜きなどしてみよ。\n
馬鹿にされたあれの顔もさぞかし見物だろうが、わらわは負ける気はない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「……手強いものね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドは今までに何度かゲームを制しかけたのだと聞いたことがあった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのたびに、自分でぶち壊したのだと聞いたが……、実力者であることに変わりない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0355
Vivaldi "「ああ。\n
相手があれでなければ、とうにこのゲームはわらわがもらっておる」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（……認めているんだな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手強い敵として、また全力で争う相手として。\n
きっと本人には言わないこの言葉は、彼女なりの最大の賛辞に違いない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（私は、姉さんにどう思われていたんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "答えは見えなくて、今はもう確認することも出来ないが、聞いてみたいと叶わぬことを思った。"

hide bg_gen_sky_spr_day


show viv_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0356
Vivaldi "「だが、別のゲームも出来るようになった。\n
領地だけではなく、おまえを奪ってやりたい気持ちもある」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……冗談ばっかり」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は笑って流そうとしたのに、彼女はそれを許してくれなかった。"

play sound se_0267

show t_bra3_1 onlayer master
with dis
hide viv_t_01_10

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首筋にちくりとした痛みが走る。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0357
Vivaldi "「冗談ではないぞ。\n
女王が欲したら、拒めるものなどおらぬ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0358
Vivaldi "「牢獄など味気ない場所ではなく、わらわの部屋で囲ってやろうか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「…………」"

hide t_bra3_1

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっと見下ろしてくる目は笑っていて、本気かどうかは分からない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（でも……）"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭を撫でてくれていた手を今度は私が捕まえる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「……お姉さんが、弟から横取りしちゃ、駄目でしょう？\n
仲よくしてよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「せめて、ゲーム以外では」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（私には出来なかったから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "姉は、私には最初から手の届かない人だった。\n
妹とは、最後まで本気で喧嘩も出来なかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（……羨ましい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "血で血を洗う関係になっても、二人は自分達だけのものを持っている。\n
他人には踏み込めないものを、持ち続けている。"


show viv_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

hide viv_t_01_11
show viv_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0359
Vivaldi "「わらわは、奪われるほうが間抜けだと思うのだがな。\n
それにな、[firstname]」"

play sound se_0466
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を膝に乗せたまま、ビバルディはまたあの子供姿になった。"

hide viv_t_01_13
show viv_chil02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0360
Vivaldi "「言ったであろう、わらわといるときにはわらわのことだけ考えておればよい」"

hide viv_chil02_2
show viv_chil02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0361
Vivaldi "「わらわは誰かと同じで、嫉妬深いからのう。\n
妬いてしまうぞ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「うふふ、いいわよ。\n
ビバルディになら、いくらヤキモチを焼かれても嬉しいもの」"

hide viv_chil02_7
show viv_chil02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_8")
voice viv_f0362
Vivaldi "「まったく。\n
本当に失礼な子」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "紅葉のような手が私の額を小突く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口を尖らせる小さな顔は、それでもきらきらと輝いていた。"

hide viv_chil02_6

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play sound se_0303
pause .35

show siro_t_02_08 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hei_f0028
Maid "「……お楽しみ中、申し訳ありません、陛下。\n
あの……、例のお客様が」"


show viv_chil02_8 at center
hide siro_t_02_08
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0363
Vivaldi "「なんだ、もう来たのか。\n
せっかくこの子と遊んでおったのに」"

hide viv_chil02_8
show viv_chil02_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0364
Vivaldi "「やれやれ、来たのなら顔を見せぬわけにはいかぬ。\n
……[firstname]、おまえもついてくるだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ、やっぱり私も一緒なのね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "採寸で酷い目にあったので、今回はとぼけていようと思ったのだが、そうはいかないらしい。"

hide viv_chil02_16
show viv_chil02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0365
Vivaldi "「勿論じゃ。\n
おまえを隠しておくのも一興じゃが、嫌なことはさっさと片付けるに限る」"

hide viv_chil02_2

play sound se_0774

scene hr_01 with Dissolve(2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おいでというように手招きする彼女について行く。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（……例のお客様ってことは、多分またあの格好なんだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（他の変装の選択肢はなかったのかしら。\n
ただでさえ胡散臭いのに、ますます怪しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何だか、あの怪しい格好のブラッドでは、ツボや健康グッズを売りつけられそうだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（しかも、商売上手っぽい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、一度買ってしまえばクーリングオフなど受け付けてくれなさそうだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「マフィアっていうよりも詐欺師って感じよね、あれじゃあ」"


play music castle_audience_p_ali

scene he_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを言いながら案内された場所は、この前と同じく謁見室。\n ・
そして、前回ペーターと睨み合っていた自称・商人は、今は一人で立っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その背後には布に覆われた何かがおいてある。"


show bra_d_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0077
Blood "「これはこれは……。\n
ご機嫌麗しゅう、女王陛下」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こちらを見て一礼してくるその顔は、前回と同じく、ちゃちな変装が施されていた。"

hide bra_d_01_2
show bra_d_01_2 at left
show viv_chil02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0366
Vivaldi "「麗しいかどうかは、おまえの仕事次第じゃろう。\n
……それで、仕上がったのであろうな？」"

hide bra_d_01_2
show bra_d_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0078
Blood "「ええ、勿論。\n
そうでなければ、ここまで足を伸ばしません」"

hide bra_d_01_1
show bra_d_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0079
Blood "「……そう、動くからには、すべての下準備をすませておくのが道理というもの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（何、今の嫌な感じ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬だけ私を見た瞳の中に、奇妙な違和感を覚えたのだが、気のせいだろうか。"

hide viv_chil02_2
show viv_chil02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0367
Vivaldi "「ふむ。\n
それでは、早く見せよ」"

hide bra_d_01_11
show bra_d_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0080
Blood "「では……」"

play sound se_0750
show t_cut_bra3_1 onlayer master
with dis
hide viv_chil02_3

hide bra_d_01_10

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後のマネキンに被せていた布を取り去ると、そこには二枚の赤いドレスが並んでいた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「……うわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（本当に、真っ赤）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディが着ているドレスにも負けない赤だ。\n
大きさの違うドレスはそれぞれ装飾も趣を変えていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さいものはフリルが多くついた、可愛らしいデザイン。\n
そして、もう一着は膨らみを抑えた大人しい仕上がりになっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とはいえ、使っている色は原色の赤だから、存在感はかなりある。"

hide t_cut_bra3_1
show t_cut_bra3_1u onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（でも、これだけ目に痛い色なのに……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（上品に、綺麗に作ってある）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "女王への納品なのだから、当然と言えば当然なのかもしれないが、意外だ。"

hide t_cut_bra3_1u


show viv_chil02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0368
Vivaldi "「ふむ、まずまずじゃな。\n
思っていたよりは、よい仕事だ」"

hide viv_chil02_7
show viv_chil02_7 at left
show bra_d_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0081
Blood "「そうでしょう？\n
手は抜きませんよ、仕事ですから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（不気味だ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディとブラッドの会話は穏やかに進んでいるのに、私は落ち着かない。\n
先ほど、一瞬だけ見せたブラッドの眼差しがどうにも気になってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（何ごともなければいいんだけど）"

hide viv_chil02_7
show viv_chil02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice viv_f0369
Vivaldi "「まあよい。\n
支払いについては……」"

hide bra_d_01_1
show bra_d_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice blo_f0082
Blood "「いえ、支払いの前にやはりきちんと身体に合っているかを確認して頂きませんと、お代は貰えません」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "控えていたメイドに言伝ようとしていたビバルディを制して、ブラッドが口を挟んだ。\n
むっとしたように彼女は疑問の声を生む。"

hide viv_chil02_2
show viv_chil02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0370
Vivaldi "「なに？」"

hide bra_d_01_11
show bra_d_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0083
Blood "「信用第一の仕事ですから。\n
万が一、不備などがあったら今後の仕事に差し支えるでしょう？」"

hide bra_d_01_1
show bra_d_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0084
Blood "「ぜひ、ご試着して頂きたい」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（一理はあるんだけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "オーダーメイドの服で仕上がりを気にかけるのは当然のこと。\n
しかし、強く言うブラッドの言葉に疑問が抑えきれないのも事実だった。"

hide viv_chil02_4
show viv_chil02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「？」"

hide viv_chil02_11
show viv_chil02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice viv_f0371
Vivaldi "「おまえ、先に試着してまいれ。\n
わらわはその後にする」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え？\n
いや、試着するのならビバルディのほうが先なんじゃ……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（私はただのおまけだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "やんわりと断ったつもりだったが、ビバルディはドレスを指差して繰り返してくる。"

hide viv_chil02_10
show viv_chil02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0372
Vivaldi "「いいから、早く着替えてくるのだ。\n
それとも、メイドを付けねば着替えられぬか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供の癇癪を起こしたような言葉に、びくっと身体が反応してしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「わ、分かったわ。\n
行ってきます……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "このままでは強制的に着替えさせられかねない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの目が真剣なのを感じて、ドレスを受け取りに行くとブラッドと視線が合った。"

hide bra_d_01_2
show bra_d_01_11 at center
hide viv_chil02_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「な、何よ？」"

hide bra_d_01_11
show bra_d_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice blo_f0085
Blood "「いや。\n
きっと、君によく似合うだろうと思ってね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（すごく嫌な予感がするんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさか、ここで断ることが出来るとは思えない。\n
手早くドレスをマネキンから外すと、別室へと持ち込んだ。"

hide bra_d_01_2

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "着替えは思ったよりも早くすんだ。\n
デザインだけでなく、着やすさも計算されているのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（……着替え終わってしまった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "試着というのなら一度袖を通したのだから、いつもの服で戻ってもいいのだろうが、恐らくそれでは納得しないだろう。\n
ブラッドも、ビバルディも。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「ビ、ビバルディ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こそこそとドアを少しだけ開いて部屋の中を覗くと、二人はすぐに私を振り返った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0373
Vivaldi "「遅いぞ、[firstname]。\n
早く出て来ぬか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「いや……、だって何だか、これ恥ずかしい」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
voice blo_f0086
Blood "「おや、お嬢さんに恥ずかしい思いをさせるように仕立てた覚えはないんだが。\n
それはぜひ確認しなければ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（あんた、絶対に分かっていて言っているでしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、苛つくビバルディの様子から考えても、扉の影から声をかけるのは限界だろう。\n
諦めたように、謁見室へと戻った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すぐさま吸い付くような視線を感じて、居たたまれなくなる。"

$ hi_mes()

play music happy_a_ali
show t_bra3_2 onlayer master
with dis
pause .5
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0374
Vivaldi "「おや、まあ……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「な、何よ？\n
おかしいなら、おかしいって言えばいいでしょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人揃って溜息をついてくるので驚いてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（だから、こういう色は私には似合わないって言ったのに）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice viv_f0375
Vivaldi "「何を言う。\n
正直、頭に来るほど似合っておるわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice blo_f0087
Blood "「ああ、やはり会心の出来だったな」"

play sound se_0776
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice blo_f0088
Blood "「よく、似合っているよ。\n
お嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「あ、ありがとう……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "満更お世辞でもない様子でブラッドはそう言いながら私の近くにやってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕立てた服と私の顔を交互に見ながら、頷いた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0089
Blood "「ああ、これが報酬なら悪い仕事ではなかったな。\n
面倒だったが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（どうして私を見ながら、報酬なんて言葉が出てくるの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わずブラッドと呼びかけそうになって、言葉を止めた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0090
Blood "「君はこういう機会でもないと、なかなか私に着飾らせてくれないからな。\n
仕事を口実に君をドレスアップ出来たのは、一石二鳥だったよ」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "満足そうにそう言って、彼は身に付けていた眼鏡とローブに手をかけた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T "（ブラッド！？）"

play sound se_0108
play sound se_0339
hide t_bra3_2
show white onlayer master with expand_extrashort
hide white
show t_bra3_3 onlayer master with compress_short
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が止める間もない。\n
一瞬で変装を解いた男は悠然と立っていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「なっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（ちょっと、何をしているのよ！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この部屋にいるのは私達だけではない。\n
ビバルディ付きのメイドだっているのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城に勤めている以上、彼女達だって飾られるだけの存在ではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（こんなところで形ばかりの変装を取り払うなんて、一体彼は何を考えているのよ！？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice blo_f0091
Blood "「ん？何をそんなに驚いているんだ、お嬢さん。\n
ああ、私の正体に驚いているのか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「ち、違うわよ、馬鹿！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ここはハートの城よ！\n
そんな中で、変装を解いてどうするのよ\n
！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice blo_f0092
Blood "「ふむ、最初はあのまま帰ろうかとも思ったんだが、気が変わった」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice blo_f0092_5
Blood "「それに、こんな姿の君を目の前にして、あんなふざけた格好をしたままなんて冗談じゃない」"

play sound se_0269

play music blood_t_ali
hide t_bra3_3
show t_bra3_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一体どこに隠し持っていたのか。\n
トレードマークとでもいうべき帽子を被れば、もう言い逃れは出来ない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ブラッド……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice blo_f0093
Blood "「それに、君に名前を呼んでもらえないというのも、存外退屈だ。\n
私は我慢が嫌いでね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice blo_f0094
Blood "「さて……」"

play sound se_0125
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、手にした杖の先端が向かう先は、小さい姿ながらも、この場においては絶対の権力者だ。"

hide t_bra3_4


show viv_chil02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0376
Vivaldi "「……ほう、化けの皮を剥いだか？\n
いつかこうなるだろうとは思っておったが」"

play sound se_0126
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディが杖を振るう。\n
ただそれだけの動作だが、意図は明確だった。"

play sound se_0312
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまでひとけの少なかった謁見室に、あっというまに兵士が詰め掛けてくる。"

hide viv_chil02_4
show viv_chil02_4 at left
show heisi_t_02_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0023
Soldier "「あれは……、帽子屋！」"

hide viv_chil02_4

hide heisi_t_02_05
show heisi_t_02_05 at left
show heisi_t_01_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0018
Soldier "「女王陛下、ご無事ですか！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "兵が声をかける間も、二人の役持ちは睨み合ったまま動かない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視線を逸らしたほうが負けとでもいうように、見えない火花が散っているようだった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「ブラッド。\n
早く帰りなさいよっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（何をのんびりとしているの、あんたはっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "出口を指差している私に、彼は呆れたように言う。"


show bra_t_01_11 at center
hide heisi_t_02_05

hide heisi_t_01_03
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0097
Blood "「帰る？\n
失礼なことを言わないでくれないか、お嬢さん」"

hide bra_t_01_11
show bra_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0098
Blood "「まるで私が逃げるようじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "{size=+20}「だから、面倒なことになる前に逃げろって言ってあげているのよ、～～～～！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（余裕ぶっているんじゃないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の武器は確かに一対多でも不自由はしない、大量火力のマシンガンだ。\n
だが、引き金を引くのなら、ここではやめてほしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（敵対するのは避けられないって分かっているけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さくても、大きくても変わらない。\n
ビバルディは私にとって大切な、女友達なのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いずれつけなければならない決着ならば、今ではなくてもいいはずだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「エリオット達も来ていないんでしょう？\n
面倒が嫌いだって言うなら、避けなさいよ」"

hide bra_t_01_3
show bra_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
Blood "「…………」"

hide bra_t_01_4
show bra_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice blo_f0099
Blood "「……ふ。\n
意外だったよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言葉に何故か彼は戯けたように目を見開いて見せた。"

hide bra_t_01_2
show bra_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0100
Blood "「いや、私を殴って屋敷を飛び出した君にそこまで心配してもらえるとは。\n
あの張り手もそう悪いものではなかったらしい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「殴られ足りないのなら、いくらでも追加してあげるわよ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（馬鹿じゃないの、この人）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを言う間にも謁見室に集まってくる兵士の数は増え続けているのだ。\n
こんな悠長にしている場合ではないのに、ブラッドは態度を改めなかった。"


show viv_chil02_16 at center
hide bra_t_01_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0377
Vivaldi "「まったくじゃ。\n
どうせなら、張り手どころか、銃弾をお見舞いしてやろう」"

hide viv_chil02_16
show viv_chil02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0378
Vivaldi "「わらわの遊びを邪魔したのじゃ。\n
その命を以て贖ってもらうぞ、帽子屋」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "静かな口調。\n
まるで、お茶会の始まりを告げるような声だ。"


play music battle_ali

show t_bra3_5 onlayer master
with dis
hide viv_chil02_8

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0379
Vivaldi "「城に立ち入った不届きものの首を刎ねよ。\n
……行け」"

play sound se_0126
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "金の杖がブラッドを示す。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0024
Soldier "「かかれっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0019
Soldier "「帽子屋を討ち取るぞ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kaz_f0008
Soldier "「行けええ！」"

play sound se_0679
pause .6
play sound se_0680
pause .8
play sound se_0681
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "女王の命を受けて、兵士達が一斉に動き出した。\n
圧倒的な数に息を飲む。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず後退ると、ブラッドの腕が私の身体を受け止めていた。\n
ひきつる私と違い、彼はどこまでも余裕だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0101
Blood "「ふ……、それは困る。\n
こんな面倒なことまでしてここに来たんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0102
Blood "「どうせだったら、もう少し楽しませてもらいたいものだな。\n
女王陛下」"

play sound se_0525
hide t_bra3_5
show t_bra3_6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの杖がマシンガンに変わる。\n
そして、その銃口は自身へ群がろうとしていた兵士達に向けられた。"

play sound se_0501
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0025
Soldier "「ぐ、あ！」"

play sound se_0502
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0020
Soldier "「が……、ぐふっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃声が響く度に、兵士が一人二人と倒れていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（あれ、いつもよりも……、音が小さい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの銃は片手でも撃てる、改造型のマシンガンだ。\n
連射も可能なはずだが、彼は連続して撃っていない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（どうして？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問いかけるような私の視線に気付いたのか、彼は何でもないように言った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0103
Blood "「撃ったら、君のドレスまで汚れてしまうだろう？\n
なかなか目に楽しい光景なんだ、すぐに終わらせたくない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0104
Blood "「いずれ綺麗になるとはいえ、君には硝煙も血生臭さも似合わない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「あんたは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この状況で何を言うのか。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kaz_f0009
Soldier "「ちっ、怯むな！\n
今こそ好機だぞ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0105
Blood "「……とはいえ、いつまでもこいつらの相手をするのもだるいな。\n
行くぞ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え？\n
行くって……」"

play sound se_0051
hide t_bra3_6
show t_bra3_7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひょいっとブラッドは私の膝の下に手を入れると、あっさりとその身体を抱き上げてしまった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「ちょ、ちょっと、ブラッド！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice blo_f0106
Blood "「静かにしていなさい。\n
ああ、銃声よりは、君の声のほうが楽しいんだが……」"

play sound se_0772
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice blo_f0107
Blood "「ここでは余計なギャラリーが多すぎる。\n
二人っきりになったらゆっくり聞いてあげよう」"

play sound se_0417
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "馬鹿なことを言っている間にも、ブラッドは走り出している。"

hide t_bra3_7
show t_bra3_8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "謁見室の出口に向かってマシンガンを向けた。\n
だが、その銃口の先にも兵士が待ち受けている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0108
Blood "「邪魔だ」"

play sound se_0501
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice suz_f0002
Soldier "「ぐ、は！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice tan_f0012
Soldier "「ぎゃっ」"

play sound se_0273
hide t_bra3_8

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呻き声を上げながら倒れる男達には目も向けず、ブラッドは手が塞がっているためだろう、ドアを蹴り開けた。"

play sound se_0591

scene hr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0380
Vivaldi "「ええい、情けない！\n
侵入者の一人ぐらい、さっさと片付けられぬのかっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0381
Vivaldi "「あやつの首を持ってこなければ、おまえらの首が飛ぶと思うがいい！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0013
Soldier "「た、直ちに……」"

play sound se_0312
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遠ざかっていく部屋からそんな声が聞こえたが、振り返るだけのゆとりはない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0109
Blood "「……さて、どこから出たものかな。\n
門番達ではないが、この追いかけっこは楽しめそうだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "皮肉げに笑う男の声だけしか、もう聞こえなかった。"

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

pause .5
play sound se_0773

play music castle_corridor_p_ali

show t_bra3_9and3_11 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice blo_f0110
Blood "「ふむ……。\n
とりあえず撒いたか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……本気で撒く気なら、その格好をどうにかしなさいよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "トランプ模様の帽子に、白い上着。\n
何もしなくても目立ちまくっているのに、その上、真っ赤なドレスを着た私を抱いて走っているのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（これで目立たないほうがおかしいわよ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（……って、私もいつまで抱かれているの！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さくなったビバルディを抱えているわけではない。\n
ひと一人を抱えているのだから、けして軽いとは言えないだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「下ろしなさいよ！\n
だいたい、どうして私まであんたに付き合わされなくちゃならないのよっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……って、そうじゃないでしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私一人なら、ビバルディは危害を加えたりしない。\n
だが、帽子屋としてのブラッドは別だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "兵士をけしかけてきたように、けして逃がしてくれなどしないだろう。\n
彼が私を抱えていてもデメリットこそあれ、得るものなど何もない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（私を抱えてまで逃げる必要なんて、どこにあるのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じたばたと暴れると、ブラッドは心外そうに言った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0111
Blood "「やれやれ、久しぶりに会った恋人に、君はずいぶんと冷たいことを言うな、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0112
Blood "「悪漢に攫われる姫君というのは悲鳴を上げるもので、毒舌を吐くものじゃないぞ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（悪役だっていう自覚はあるわけね？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「悲鳴がお好みなら、そうしてあげましょうか？\n
この位置からだと、さぞかしよく聞こえるでしょうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ私の目の前には、彼の顔がある。\n
この距離では避けようもないだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0113
Blood "「……遠慮しておこう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0114
Blood "「やれやれ。\n
そんなに下りたいというのなら、下ろすとするか」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0115
Blood "「気を付けなさい、いつもよりも大分ヒールが高いだろう」"

hide t_bra3_9and3_11

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の視線が多少は効いたのか、ブラッドは苦笑を浮かべながらも一応床に下ろしてくれた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言われたとおり足をくじかないように気を付けながら、慎重に床に下りる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「……ふう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（やっぱり自分の足で立つのって、落ち着くわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お姫様抱っこに憧れを持つ年頃の女の子に言ってやりたいが、あれは思っているほどいいものじゃない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（安定感がないし、万が一手を滑らせられたら落ちるしかないもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぱんぱんとドレスを叩いていると、ブラッドの視線に気が付いた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「なによ？」"


show bra_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice blo_f0116
Blood "「いや、ずいぶんあの女と仲よくなったものだと思ってね」"

hide bra_t_03_13
show bra_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice blo_f0117
Blood "「私もあの女について少しは知っているつもりだったが、まさか自分を玩具にしてもいいなんて酔狂を許したのは、君が初めてだろうよ」"

hide bra_t_01_3
show bra_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice blo_f0118
Blood "「気に入られたものだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呆れているような、感銘を受けているような。\n
何とも判別しがたい言い分だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「あら、羨ましいの？」"

hide bra_t_01_11
show bra_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice blo_f0119
Blood "「まさか。\n
私は自分を材料に遊んでほしいなんて、そんな愚かなことは言わない」"

hide bra_t_03_4
show bra_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice blo_f0120
Blood "「人形遊びをするような趣味もないさ。\n
そして……」"

pause .2
play sound se_0682
$ flash(.5)
play sound se_0535 volume .8
hide bra_t_03_3
show bra_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice blo_f0121
Blood "「自分から役を放棄したがるような奴と、馴れ合う気もない」"

play sound se_0093

play music ace_t_ali

show ace_t_03_2 at center
hide bra_t_03_10
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice ace_f0306
Ace "「あっれー。\n
今のはいけると思ったんだけどなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「エ、エース！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（エースまでブラッドの追跡に来ているの！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭上から斬りつけたエースの一撃をブラッドは杖で受け止めていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま弾かれたように後ろに飛んだ騎士は、大剣を構えながら何でもないように爽やかに笑っている。"

hide ace_t_03_2
show ace_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0307
Ace "「でもおかしいな、どうして帽子屋さんがここにいるんだ？\n
いつもなかなか屋敷から出てきてくれないのに」"

hide ace_t_03_12
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0308
Ace "「こんなところで会えるなんて思ってもみなかったぜ」"

hide ace_t_03_10
show ace_t_03_10 at left
show bra_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0122
Blood "「それだけは同感だな。\n
いつも私の領地に迷い込んでばかりのおまえが、今回に限って城にいるとは」"

hide bra_t_03_13
show bra_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0123
Blood "「まったく、鬱陶しい」"

play sound se_0525
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エース相手に接近戦をするつもりはないのか。\n
ブラッドは再び杖をマシンガンに変えた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、すぐさま引き金に手をかける。"

play sound se_0521
play sound se_0686
$ flash(.3)
$ flash(.3)
$ flash(.3)

show t_bra3_10 onlayer master
with dis
hide bra_t_01_3

hide ace_t_03_10

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0309
Ace "「ははは、鬱陶しいだなんて酷いなあ。\n
俺は壮大な冒険の最中に、ちょっと迷っているだけなのに」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0310
Ace "「でも、これってついているのかな」"

play sound se_0682
$ flash(.5)
play sound se_0683
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自身に放たれる弾丸を剣で弾き飛ばしながら、騎士は爽やかに笑う。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0124
Blood "「ついている？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0311
Ace "「うん、だって……。\n
これだけ距離が近ければ、外さないだろ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0312
Ace "「迷いやすい俺でも……、さ！」"

play sound se_0521
play sound se_0686
$ flash(.3)
$ flash(.3)
$ flash(.3)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0125
Blood "「ちっ、面倒な奴が出てきたものだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドが舌打ちを漏らすのも仕方ない。\n
ここは屋内、城の廊下である程度広さがあるといっても、マシンガンを振り回すにはそれ自体の火力が強すぎる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（普通の兵士ならともかく、相手がエースじゃ相性が悪い）"

play sound se_0682
pause .3
play sound se_0683
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice ace_f0313
Ace "「最近、調子もいいんだよなあ。\n
だから、遠慮なく……、相手をしてくれよ、帽子屋さん！」"

play sound se_0523
$ flash(.2)
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "距離を縮められないように一定を保ちながら、ブラッドはマシンガンを操るが、エースは巧みに距離を詰めてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "長身に見合わない敏捷さに、ブラッドも舌打ちを漏らした。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0126
Blood "「本当に厄介な男だな。\n
しつこい上に、嫌なタイミングで出てくる」"

play sound se_0436
$ flash(.2)
play sound se_0506
$ flash(.3)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0316
Ace "「でも、彼女を置いていってくれるのなら、今回は見逃してあげてもいいよ……？\n
陛下が上でそんなことを言っていたみたいだし」"

play sound se_0081
$ flash(.1)
play sound se_0436
$ flash(.3)
play sound se_0507
$ flash(.5)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0127
Blood "「ふざけるな。\n
おまえが出てきたぐらいで、どうしてそんなことをする必要があるんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0317
Ace "「ははは、余裕だね」"

play sound se_0523
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（言うほど余裕なんてないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドは思ったことを素直に言うほど正直ではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私と同じぐらい、いや、ある意味私以上に捻くれた性格をしている。\n
余計なことを言っている段階で、それは強がりにすぎない。"


play music serious_a_ali
hide t_bra3_10

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（どうしよう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドは私を置いていく気はないらしい。\n
だがエースとブラッドの戦いが、そう簡単に決着がつくとも思えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして長引けば、兵士が来るだけだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドのことだから、奥の手の一つや二つぐらい用意していることだろう。\n
しかしそれを使っても、無事にすむ保証なんてどこにもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屋敷を飛び出す前に、感じていた気持ちが蘇る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（血が、流れている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "中心にあるものは違っていても、不死身ではない。\n
傷つかないわけではないのだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

play sound se_0682
play sound se_0514

show white with Dissolve(.1)
hide white with Dissolve(.2)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬の交錯。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "剣の先端が掠めたのだろう、ブラッドの頬に一筋の傷が生まれていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同じように、エースの髪の一房が切れて、床に散っていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（どっちもこのままじゃ……）"

play sound se_0590

show per_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_11")
Peter "「[firstname]……、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遠くから駆け寄ってくる赤い影に、私は振り向いた。"

hide per_t_01_11
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0279
Peter "「ああ、やっと追い付きました。\n
今回だけは、エース君も役に立って……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼もまた走ってきたのか、息を切らせて現れた白ウサギに私は飛びついた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（どこかの諺で『地獄に仏』っていうらしいけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いるかどうかも分からない神様よりも、目の前にいるウサギのほうが手を伸ばしやすい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「ペーター、止めて！」"

hide per_t_02_8
show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
Peter "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言葉が意外だったのか、はたまた抱きつかれたことに驚いたのか。\n
ペーターは珍しいものを見るような目で私を見つめてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「お願い、ブラッドとエースを止めて！\n
止めて！！」"

hide per_t_02_3
show per_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_6")
Peter "「[firstname]……」"

hide per_t_02_9
show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_6")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「お願いだから、止めてよ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（私が帽子屋屋敷を出てきたのは、怪我をさせたかったわけじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大切にしてくれていると思っていたのに、突然、遠ざけられたことが嫌だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界では引っ越しというわけの分からない常識によって、居場所さえ簡単に引き裂かれてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_4")
T "（これが次の引っ越しの予兆だったら……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな不安感もあったから、余計に苛ついた。"

hide per_t_02_10
show per_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_02_4
show per_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0280
Peter "「泣かないでください、[firstname]。\n
あなたにそんな顔をされると、僕も哀しくなります」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の頬を撫でたペーターは、ふっと柔らかい笑みを浮かべている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものストーカーじみた雰囲気ではなく、何故かもっと、深い感情を感じさせる表情だ。"

hide per_t_01_8
show per_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0281
Peter "「[firstname]、この廊下の奥に階段があります。\n
とりあえず、そこまで行ってください」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「ペーター……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「大丈夫なの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（私、最低だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "助けを求めておきながら、今になって彼の安全を確認するなんて……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（自己満足でしかないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦い気持ちで声を絞った私の肩に手を添えて、彼は言った。"

hide per_t_03_7
show per_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0282
Peter "「心配はいりませんよ。\n
ルールに反して、あなたを哀しませたりはしません」"

hide per_t_03_6
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0283
Peter "「僕は、今回直接陛下からは何も聞いていませんからね。\n
不審者についても、真正面から顔は見ていませんし……」"

hide per_t_02_8
show per_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0284
Peter "「さあ、行って。\n
……そして、振り返らないでください」"

play sound se_0373
hide per_t_01_10

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とんと。\n
背中を軽く押された先には、マシンガンを持つマフィアと、剣を構えた騎士。"

play sound se_0502
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後から響いた銃声に思わず足が止まりかけたが、そのまま踏み込んだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（振り返っちゃ駄目）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "託した以上、振り返るなと言った言葉を信じるしかない。"


show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0318
Ace "「おっと、よ！」"

hide ace_t_01_10
show ace_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0319
Ace "「あれ、ペーターさん。\n
俺のほうを狙わないでよ、珍しく仕事をやる気になったのに」"

hide ace_t_03_9
show ace_t_03_9 at left
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0285
Peter "「どうせだったら、もっと別の形でやる気を出してもらいたいものですね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不満げなエースと、苦々しいペーターの声。\n
けれど。"

play sound se_0682
play sound se_0502
$ flash(.8)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「ブラッド、行くわよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの手を引き、駆けだす。\n
今の私に出来ることは早くここから離れることだ。"


show bra_t_01_2 at center
hide ace_t_03_9

hide per_t_02_7
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0128
Blood "「……お嬢さん。\n
まったく、君は本当に退屈させないな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……きゃっ！」"

play sound se_0051
camera at hpunch
camera at vpunch
show t_bra3_9and3_11 onlayer master
with dis
hide bra_t_01_2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然視界が揺れたかと思うと、次の瞬間には再び抱きかかえられていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0129
Blood "「この私が主導権を握るのも一苦労だなんて。\n
実に貴重なお嬢さんだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0130
Blood "「君みたいな女、二人といない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "満足げな声が、耳元で囁かれる。\n
だが、甘さを感じている暇はない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「いいから、とっとと走りなさいよ！\n
抱きかかえた以上は、それがあんたの役割でしょう！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_13")
voice blo_f0131
Blood "「そうだな。\n
宰相閣下に貴重な貸しを作ってしまったことだし……今は、君の意思を尊重するとしよう」"

play sound se_0682
play sound se_0523
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後から響く甲高い音に後押しされるように、私達は階段へと駆けていく。"

$ hi_mes()
hide t_bra3_9and3_11


scene hm_spr_01
with stripe_l_long

play music tension_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、階段は所詮階段。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "上下を塞がれ、逃げ場があるかと言われれば、難しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（エースとあそこで殺し合いに発展するよりはよかったけど）"


show heisi_t_02_05 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice hos_f0026
Soldier "「追い詰めたぞ、帽子屋！」"

hide heisi_t_02_05
show heisi_t_02_05 at left
show heisi_t_01_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice oto_f0021
Soldier "「陛下は……、どちらにっ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "前後を塞がれた私達は、屋根のない踊り場に追い詰められていた。"


show bra_t_02_3 at center
hide heisi_t_02_05

hide heisi_t_01_03
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0132
Blood "「……まったく、仰々しいことだな。\n
私だったら、こんな面倒なことはごめんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「……ブラッド」"

hide bra_t_02_3
show bra_t_02_3 at left
show viv_chil02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice viv_f0382
Vivaldi "「ふん、ようやく観念したか。\n
城の中を這い回るなど、まるでネズミじゃな、帽子屋」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "兵士の間からビバルディが姿を見せる。\n
見下ろす眼差しの鋭さに、私と一緒に遊んでいたときの面影はなかった。"

hide bra_t_02_3
show bra_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0133
Blood "「あいにく、部下にネズミはいるが、私自身は宗旨変えしたつもりはないな」"

hide viv_chil02_8
show viv_chil02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0383
Vivaldi "「言うではないか。\n
まあ、いい」"

hide viv_chil02_5
show viv_chil02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0384
Vivaldi "「[firstname]、おまえはこちらにおいで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ビバルディ……」"

hide viv_chil02_8
show viv_chil02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice viv_f0385
Vivaldi "「その男は見逃せぬが、おまえを傷つけるつもりはない。\n
ちょうどいい、その男と縁を切ってここに残ればよい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（縁を切る？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（ブラッドと？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "囁きは空気に溶けて消える前に、私の中に染み込んでくる。"

menu:
    "申し出は嬉しいけど……。":
        jump fushigi_blood3_6a
    "首を横に振る。":
        jump fushigi_blood3_6b

label fushigi_blood3_6a:
$ fushigi_blood3_6a_seen = True
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「あなたの気持ちは嬉しいけど、それはやめておくわ、ビバルディ」"

hide viv_chil02_13
show viv_chil02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Vivaldi "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「遊びは、もうおしまい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女は女王で、私は帽子屋屋敷に住む人間だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（一緒に遊ぶのは、本当に楽しかったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊びはいつか終わるものだ。\n
始まりがあれば、いずれ終わりが訪れるゲームのように。"

hide bra_t_03_10
show bra_t_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0134
Blood "「ふっ。\n
振られたな、女王陛下」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勝ち誇ったように言うブラッドに、ビバルディは冷たく鼻で笑った。"

hide viv_chil02_9
show viv_chil02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0386
Vivaldi "「ふん、女一人満足に迎えに来られぬ男に言われる義理はない」"

hide viv_chil02_10
show viv_chil02_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0387
Vivaldi "「それで、どうするのじゃ。\n
まさか、この高さから飛び降りるなどと言うつもりはなかろうな、帽子屋」"

hide viv_chil02_14
show viv_chil02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0388
Vivaldi "「おまえは何とかなるだろうが、その子は保たぬぞ。\n
傷つけるぐらいなら、わらわに寄越せ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（ここから飛び降りるって）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後を振り返れば、恐ろしく下に地面が見えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（怪我じゃすまない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の役持ちは不思議な力があるが、私には何もない。\n
ここから落ちれば、命はないことは明白だった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「……ブラッド」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうするつもりかと問うように彼を見上げれば、ブラッドはいつものように気だるげに笑ったままビバルディを見ている。"

hide bra_t_01_11
show bra_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0135
Blood "「ふ、はははは。\n
あなたも、私を見くびってくれたものだな」"

play sound se_0053

play music denouement_a_ali

show t_bra3_12aand3_12b onlayer master
with dis
hide bra_t_02_8

hide viv_chil02_13

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0136
Blood "「私を誰だと思っているのかな。\n
簡単に始末出来ると思われるのは、些か心外だな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を抱えたまま軽やかに手すりの上に立った男は、高らかな笑い声を上げた。"

jump fushigi_blood3_7
label fushigi_blood3_6b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「行かないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "行けば、私はきっと無事だろう。\n
だが、色々なものに目を瞑ってくれたペーターの気持ちを踏みにじることになる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（それだけは許されない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "我が身を省みずなんて綺麗ごとを言うつもりもないが。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「最初から約束していたもの。\n
少しの間だけ、お邪魔させてって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……だから、その少しが終わったら、帰らなくちゃ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（好き勝手なことを言っている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飛び出してきて居座った挙げ句に、自分の帰りたいときに帰るなんて。\n
嫌われても仕方ない。"


show viv_chil02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

hide viv_chil02_9
show viv_chil02_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0389
Vivaldi "「……そう。\n
おまえがそう言うのなら、仕方あるまい」"

play sound se_0126
hide viv_chil02_14
show viv_chil02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0390
Vivaldi "「庇うのなら、止めぬ。\n
運がよければその男が守るやもしれぬ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "命令を下すべく、小さな手が持ち上げられた。\n
あの手が振り下ろされたときが、執行のとき。"


show bra_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0137
Blood "「決めつけるのが早いんじゃないか、女王陛下。\n
逃げ場なら、まだあるじゃないか」"

play sound se_0178
hide t_bra3_12aand3_12b
show t_bra3_12aand3_12b onlayer master
with dis
hide bra_t_03_10

hide viv_chil02_13

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "固い音。\n
ブラッドの靴と、手すりが擦れるような音がした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は、私を抱えたまま手すりの上に立っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ブラッド？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（あなた、何をするつもりなの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問いかける眼差しを送っても、彼は答えてくれなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0391
Vivaldi "「この高さじゃぞ。\n
おまえ、その子を道連れにするつもりか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0392
Vivaldi "「それとも、犠牲にするつもりか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "睨んでいたビバルディの眼差しがいっそう鋭くなった。\n
こんな状況になっても、彼女は私を心配してくれている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice blo_f0138
Blood "「道連れ？犠牲だと？\n
はっ、私が我が身可愛さにお嬢さんを犠牲にするとでも？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice blo_f0139
Blood "「それこそ、まさかだな。\n
私のものは、私が私でいる限り私のものだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice blo_f0140
Blood "「奪わせるぐらいなら、私の手で潰すさ」"

jump fushigi_blood3_7
play sound se_0729
label fushigi_blood3_7:
play sound se_0402
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ごうっと。\n
背後から風が吹き上がっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらりと見えた地面は、まだ遙か下。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（落ちたら、痛いとかそういうレベルじゃないわよね、これ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice blo_f0141
Blood "「なあ、お嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「ブラッド……？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（何か考えがあるのよね、そうよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目線で問いかけるも、彼は戯けたように肩を竦めて。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0142
Blood "「串刺しになって醜い死に様を晒すよりは、君だって一思いに散ったほうがいいだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！！？」"

play sound se_0126
play sound se_0764


hide t_bra3_12aand3_12b

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「い……。\n
{size=+20}いやあああああっ！！！！！{/size}」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T "（何を考えているのよ、この～～～～～～！！！！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あろうことか、ブラッドは私を抱えたまま手すりを蹴っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "支えるものの何もなくなった身体は、まっすぐに地面へと落ちていく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「！」"

play sound se_0468
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "風斬り音に混じって、指を鳴らすような音が聞こえた気がした。\n
そして……。"

play sound se_0656
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "真下から吹き付けてくる熱と爆風に私はようやく目を開いた。\n
見れば、どんどん近づいていく地面が吹き飛んでいる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「え……。\n
な、なに、よ、これ！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice blo_f0143
Blood "「火薬だよ。\n
ああ、君の目の前で爆薬を使うのは初めてだったな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドは何でもないように言うが、何でもないわけがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "下から吹き付けてくる爆風は、地面に吸い込まれそうになっている私達をはじき返さんばかりに強い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落下の速度が弱まったのを感じて、ふと気が付く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「まさか、あんた、この爆風で衝撃を殺そうって言うんじゃないでしょうね！？\n
無理よ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひと二人にかかる重力は伊達ではないのだ。\n
ブラッドともあろう男が、そんな私でも分かるような間違いを犯すだろうか。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0144
Blood "「そうだな、これだけではまだ不充分だが」"

play sound se_0516
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0145
Blood "「反動を与えるものなら、まだあるさ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "杖から姿を変えたままだったマシンガンを手にして、マフィアのボスは引き金を引いた\n "

play sound se_0521
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "爆発音に続いて、立て続けに銃声まで響く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほど兵士達に向けたときとは明らかに威力が違う。\n
一斉掃射の銃声だけが私の聴覚を支配した。"

play sound se_0521
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "爆発音に続いて、立て続けに銃声まで響く。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（耳がおかしくなりそう）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の身体に巻き付いたブラッドの腕に力がこもる。\n
大きな音がしている割に、私の身体にはほとんど衝撃などない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（意地っ張り）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私にかかるべき衝撃がどこにいっているかなど、考えるまでもなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0146
Blood "「……ふう」"

play sound se_0609

play music castle_mae_p_ali

scene hn_spr_01
with dis

show bra_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0147
Blood "「着いたぞ、お嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とんと。\n
あっけないほどの音を立てて、私達は地面に下りた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "滞空していたのは、それほど長い間ではなかったはずなのに、地面に足が着いた途端にほっと力が抜けてしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「い、生きた心地がしなかった……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（というより、本当に死ぬかと思った）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターに初めてこの世界に引き込まれたときといい、この世界の人間は私を落下させる趣味でもあるのだろうか。"

hide bra_t_01_2
show bra_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0148
Blood "「おや、これぐらいで死んでいたらキリがないぞ。\n
うちの者なら、こんなことで簡単に死なないさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「ブラッド」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目の前に差し出された手。\n
白い手袋で覆われたそれを握り返して、そして……。"

play sound se_0424
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "未だに恐怖で力の入らない手で、ブラッドの頬を叩いた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の顔を叩くのは、短くない付き合いでもこれが二回目だ。"

hide bra_t_01_3
show bra_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「死にそうな思いをさせた罰よ。\n
自分で歩け……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが歩き出した途端に、膝が笑ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……情けない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目の当たりにした爆破に腰が抜けたのか、はたまた緊張の糸が切れたのかは分からないが、足腰が立たなくなっていた。"


play music secret_a_ali

show t_bra3_13 onlayer master
with dis
hide bra_t_03_3

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0149
Blood "「やれやれ、仕方のないお嬢さんだ。\n
どうせ強がるなら、こんな場所ではなくもっと別の場所でそうしてくれ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言うが早いか、ブラッドはまたも私を抱き上げていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！\n
いいわよ、自分で歩くから！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice blo_f0150
Blood "「そうはいかない。\n
君は一人で放っておくとどこに駆け込むか分からないからな」"

hide t_bra3_13
show t_bra3_14 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「…………っ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "唇に触れる熱に、声が出なくなる。\n
そのまま深く交わろうとするブラッドを受け入れることしか出来なかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「……は、ん……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "抵抗する気力を根こそぎ奪っていくキスに吐息を漏らすと、間近から見下ろしてくる瞳に捕まった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0151
Blood "「逃げ道は全部塞いで、閉じ込めておくに越したことはない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_7")
T "（逃げ道なんて、最初から探してないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逃げられるぐらいなら、もうとっくに逃げていただろう。\n
絡みついた鎖のような感情は、しっかりと胸の内にまで忍び込んでいる。"

$ hi_mes()
hide t_bra3_14


scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_long
##endmemory
label fushigi_end_read_blood:
if renpy.seen_label("fushigi_end_blood_rose1") == True:
    jump fushigi_end_choice_blood
else:
    jump fushigi_end_check_hatter1_b
label fushigi_end_choice_blood:
if fushigi_blood3_6a_seen == True:
    jump fushigi_tag_rose1_b
else:
    jump fushigi_end_check_hatter1_b
label fushigi_tag_rose1_b:
    jump fushigi_end_blood_rose1
label fushigi_end_check_hatter1_b:
if renpy.seen_label("fushigi_end_blood_rose1") == True:
    jump fushigi_end_check_hatter2_b
if renpy.seen_label("fushigi_end_elliot1") == True:
    jump fushigi_end_check_hatter2_b
if renpy.seen_label("fushigi_end_dad1") == True:
    jump fushigi_end_check_hatter2_b
else:
    jump fushigi_end_blood_rose1
label fushigi_end_check_hatter2_b:
if fushigi_common3_castle2_blood2a_seen == True:
    jump fushigi_end_blood_rose1
else:
    jump fushigi_end_hatter1
