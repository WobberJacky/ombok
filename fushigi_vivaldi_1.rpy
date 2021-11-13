
scene map_bg_spring_day
with dis

scene charasel_bg_castle_day
with dis
label fushigi_vivaldi1:
hide screen castle_man_choice
$ clockanim()

$ hi_mes()

scene hm_spr_01
with dis

play music castle_corridor_p_ali

scene hr_01 with Dissolve(1.2)
play sound se_0774
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……まだ、怒っているんだろうなあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ、花に撒く水だけならまだしも、泥水までかけられたのだ。\n
私だって怒る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも、プライドの高い、斬首が口癖の女王様となれば……。"


play music castle_audience_p_ali

scene he_01
with stripe_l_long

show viv_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0014
Vivaldi "「そこのおまえ、わらわのドレスの裾を踏んだな？\n
おい、そこのもの、早くそやつの首を刎ねよ」"

hide viv_t_01_12
show viv_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0015
Vivaldi "「ええい、面倒じゃな。\n
いっそこの場にいる全員の首を……」"

hide viv_t_03_9
show viv_t_03_9 at left
show king_t_01_07 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0000
King "「ビ、ビバルディ……。\n
そのあたりで、そろそろ落ち着いて……」"

hide viv_t_03_9

hide king_t_01_07
show king_t_01_07 at left
show heisi_t_02_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0004
Soldier "「陛下、どうぞお許しを」"

hide king_t_01_07

hide heisi_t_02_03
show heisi_t_02_03 at left
show siro_t_02_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0000
Maid "「い、今すぐ紅茶のご用意を……」"


show viv_t_03_7 at center
hide heisi_t_02_03

hide siro_t_02_03
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0016
Vivaldi "「茶など、今はいらぬ！\n
ああ、イライラする」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（予想以上の大荒れ模様だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドア一枚では抑えきれない殺気立った空気が、廊下にまで響き渡っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "謁見室でただいま裁判中と聞いてきたのだが、この様子では判決もだいたい予想が付く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キングが宥めているようだが、一度火が付いたビバルディはそう簡単に鎮火しない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一番いいのは、ある程度苛立ちが収まるまで好きにさせてあげることだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（そんなことをしたら、間違いなく、この城からメイドも兵士もいなくなるだろうし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "原因はエースにもあるが、彼に水やりを手伝ってもらっていた私だって悪い。\n
意を決し謁見室の扉を開ければ、鋭い眼差しが私の全身に突き刺さった。"

hide viv_t_03_7
show viv_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0017
Vivaldi "「今、この部屋に入ってきたもの、おまえも……！\n
あ……」"

show viv_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0018
Vivaldi "「[firstname]、おまえだったか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ビバルディ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "汚れが自然に落ちる世界とは言え、綺麗になるまで待っていたわけではないのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女はいつもと同じように、非の打ち所のない赤のドレスを纏って玉座に腰掛けていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先程までは苛立ちのままに斬首を命じていたであろう顔が、今は少し困ったように口を尖らせている。"

hide viv_t_02_6
show viv_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0019
Vivaldi "「おまえ、この時間帯は……、休憩であろう。\n
今まで何をしておった、わらわの元に顔を出すのが遅すぎる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「ごめんなさい、後片付けをしていたら遅くなっちゃって」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これは嘘ではない。\n
水浸しになってしまった彼女のティーセットの片付けには、私も関わった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（せめてそれぐらいしないと、ビバルディにも悪い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもにも増してぴかぴかに磨いたティーセットは、既に収納されている。"

hide viv_t_01_11
show viv_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0020
Vivaldi "「後片付けなど、他のメイドにやらせておけばよい……。\n
おまえは、わらわの元に最初から顔を出せばよかったのだ」"

hide viv_t_03_11
show viv_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0021
Vivaldi "「今も、おまえが来ないからむしゃくしゃして、五人ほど処刑させたところだぞ」"

hide viv_t_01_4
show viv_t_01_4 at left
show king_t_01_07 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0001
King "「いや、まだ判決は出ていないんじゃが……」"

hide viv_t_01_4
show viv_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0022
Vivaldi "「……何だ、文句があるのか？\n
わらわが死刑と言ったら、すべて死刑じゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴしゃり。\n
黄金の錫を片手に持った女王様はきっぱりとそう言いきった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「ビバルディ……」"

hide viv_t_02_6
show viv_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice viv_f0023
Vivaldi "「ちょうどよい。\n
わらわもおまえに話があるのだ、[firstname]」"

hide viv_t_02_10
show viv_t_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice viv_f0024
Vivaldi "「わらわの部屋までおいで」"

hide king_t_01_07
show king_t_02_08 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice kin_f0002
King "「いや、ビバルディ。\n
まだ……、裁判が……」"

hide viv_t_01_2
show viv_t_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice viv_f0025
Vivaldi "「ええい、面倒な……。\n
全員斬首でよかろう、あとくされなく首を」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「だ、だったら、皆、無罪でいいじゃない。\n
ね、女王様に対して不敬罪なんて大罪だもの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「簡単に首を切るんじゃ、あっさりしすぎているわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（無茶苦茶な理論）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、ここで押し切らなければ、彼らは軒並み処刑されてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも、お茶請けのスコーンのクリームが多すぎたとか、ビバルディの部屋に小さな埃を残したとか……、そんな理不尽な理由で。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「悪いことをしたのなら、たっぷり後悔するぐらい酷い目にあわせないと駄目よ。\n
でも、あなたは私と部屋に行くのよね、だから裁判は別の人に任せましょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私はなるべく笑顔で、ビバルディに話しかけた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（命がかかっているんだもの……、毎度のごとく、重いわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも美しい女王様は、私の言うことは聞いてくれる。"

hide viv_t_02_2
show viv_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0026
Vivaldi "「ふむ、おまえがそこまで言うのならいいが……。\n
まあよい、キング、後は任せるぞ」"

hide king_t_02_08
show king_t_01_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0003
King "「いや、これはおまえの仕事で……」"

hide viv_t_03_2
show viv_t_01_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0027
Vivaldi "「ええい、つべこべ申すな！\n
こんなときのためにおまえがいるのじゃ、精いっぱい働かぬか！」"

hide viv_t_01_8
show viv_t_03_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0028
Vivaldi "「女の役に立つためだけに、すべての男は存在する。\n
行くぞ、[firstname]」"

play sound se_0774
hide king_t_01_04
show king_t_01_07 at center
hide viv_t_03_12
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
King "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（ごめんね、キング）"

play sound se_0773
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "困ったように被告人と手元に残ったリストを見比べている彼を残して、私はビバルディの後を追った。"

hide king_t_01_07
with dis
$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

play music vivaldi_t_ali

scene v_01
with stripe_l_long

show viv_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Vivaldi "「[firstname]」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋に入るや否や、ビバルディの手は私を引き寄せて、床へと座らせた。\n
そのままぺたぺたと身体を触りながら、私の顔を覗き込んでくる。"

hide viv_t_02_9
show viv_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0029
Vivaldi "「おまえ、風邪などひいてはいないだろうね？\n
あの馬鹿二人のせいで、大分冷えておっただろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「ビバルディ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（何も言わなかったのに、よく見ている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "女性らしい視点とでも言うべきなのか。\n
先ほどまで処刑せよと癇癪を起こしていた人とは思えない心配そうな顔で、私を見てくる。"

hide viv_t_03_8
show viv_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0030
Vivaldi "「おまえに風邪などひかせていたら、エースのやつ、今すぐにでも……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「だ、大丈夫、大丈夫だから、落ち着いて。\n
ここは暖かいもの、風邪なんてひかないわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（元々病弱なナイトメアでもあるまいし）"

hide viv_t_01_9
show viv_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice viv_f0031
Vivaldi "「ならばよい。\n
おまえに何かあったら、わらわはイライラして何をしてしまうか分からない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不安げな、玉座に座っているときにはけして見せない、年頃の少女のような表情。\n
あれほど傲慢に斬首を命じていた人と同じ人物なのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（……可愛い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この女王様は、時々、私よりもずっと年下の女の子のように見えてしまう。\n
抱き寄せて、抱き締めてしまいたくなる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして……、恐らく、私がそうしたところで、彼女は私の首を刎ねない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（でも、けじめはちゃんと付けないと）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「あのね、ビバルディ。\n
私……、実はちょっとの間、城を離れようと思うの」"

hide viv_t_02_7
show viv_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice viv_f0032
Vivaldi "「？\n
何だと？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ようやくほんわりと柔らかくなりかけた空気が、一瞬にして張り詰める。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想していたとおりの反応に心構えはしていたつもりだったが、肝が冷えた気がした。"

hide viv_t_03_7
show viv_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0033
Vivaldi "「おまえがここを出て行くとは、どういうことじゃ、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……少し、反省してこようかなって」"

hide viv_t_01_13
show viv_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice viv_f0034
Vivaldi "「反省……？\n
おまえに反省させるようなことなど……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（あったじゃない、今の今まであなたが怒っていた件が）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「だって、メイドさん達にも迷惑かけちゃったし……。\n
何より、ビバルディに酷いことしちゃったから、少し、反省してこようと思うの」"

hide viv_t_03_12
show viv_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice viv_f0035
Vivaldi "「[firstname]、ならぬ、ならぬぞ。\n
おまえがここを出て行くだなんて、そんなこと、わらわは認めぬからな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想通りの、引き留める言葉。\n
彼女の気持ちを確かめようと思ったわけではないのに、予想以上に心配してくれるから……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ああ、好かれている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その好意を嬉しいと思うと同時に、好ましく思われている事実に安堵する。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ずっとじゃないわ。\n
本当にちょっとの間よ？」"

hide viv_t_01_8
show viv_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0036
Vivaldi "「ちょっとも、そうでないのも、この世界では関係ないわ。\n
従えぬと言うのなら……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「……私の首も、刎ねるの？」"

hide viv_t_01_9
show viv_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
Vivaldi "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉に詰まったビバルディの手を取って、私は繰り返した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「先刻の裁判のときにも言ったでしょう。\n
私は悪いことをしたんだから、罰を受けなくちゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここが好き。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薔薇の香りに包まれた、美しく、残酷で……、同時に誰よりも可愛らしい女王の部屋を、私は愛しく思っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「私はあなたがいる、この城が好きよ。\n
本当は離れたくない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「でも、この場所にいたら、甘えてしまうわ。\n
だから行かせて、ビバルディ」"

hide viv_t_02_7
show viv_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
Vivaldi "「……[firstname]」"

hide viv_t_02_1
show viv_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice viv_f0037
Vivaldi "「やれやれ、頑固な子」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕方ないと言いたげにビバルディは肩を落とし、小指を立てて私に示してきた。\n
何を意味されているのか、分からないほど私も鈍くない。"


show t_viv1_1 onlayer master
with dis
hide viv_t_03_8

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0038
Vivaldi "「首は刎ねぬが……、わらわを放っておくなど許さぬからな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「ええ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（指切りなんて、久しぶり）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "幼い頃、姉としたような柔らかな約束に、心が和む。\n
どんな冷たい命令よりも、守らなくてはいけない気にさせられた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「約束するわ、あなたのところにちゃんと帰ってくるから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice viv_f0039
Vivaldi "「……約束したぞ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不安げに揺れる眼差しに頷いて、私はそっと指を離した。"

$ routechara = "Vivaldi"
hide t_viv1_1
with dis
$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium
##endmemory

play music map_spring_jok

scene bg_gen_sky_spr_day
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「さて、どこに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に住む友人は何人もいるが、しばらく滞在させてもらうことを考えると……。"
scene map_gen_bg with fade
$ show_mes("frame_gen_togaki")
T "Where do I want to visit?"
$ hi_mes()
show screen fushigi_map1
$ ui.interact()
