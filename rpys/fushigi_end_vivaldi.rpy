
scene map_bg_spring_day
with dis
label fushigi_end_vivaldi1:
$ clockanim()

scene charasel_bg_castle_day
with dis

scene hm_spr_01
with dis

scene hr_01
with dis

play music castle_audience_p_ali

scene bg_gen02_hs_day with Dissolve(1.2)

show per_t_01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0015
Peter "「それで、いつまでそのけったいな格好で仕事をするつもりなんですか、陛下？」"

hide per_t_01_15
show per_t_01_15 at left
show viv_da_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0105
Vivaldi "「けったいとは何じゃ、けったいとは。\n
わらわにはよく似合っているであろう、なあ、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「え、ええ。\n
すごくよく似合っている」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（女の人だって分かっていても、どきどきしちゃうくらい）"

hide viv_da_01_9
show viv_da_01_4 at center
with dis
hide per_t_01_15

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の返事にビバルディは満足げに頷いた後、それみたことかとペーターに視線を移す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地から帰っても、ビバルディは男装のまま執務を執行していた。\n
どうやら気に入ってしまったらしい。"

hide viv_da_01_4
show viv_da_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0106
Vivaldi "「ふふふ、おまえのような～～～なウサギには分からぬだろうな。\n
美人は何を着ても美人なのだ」"

hide viv_da_01_3
show viv_da_01_3 at left
show per_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0016
Peter "「[firstname]、いえ、僕はあえてあなたの目を覚まさせるために言いましょう。\n
この際、その服のことは何も言いません」"

hide per_t_02_11
show per_t_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0017
Peter "「ええ、陛下が裸で仕事をしようが、～～～～～な格好で仕事をしようが、僕にはどうでもいいんです！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（いや、それはどうでもいいレベルじゃないような気がするんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仮にも城を率いる女王が、そんな姿では示しが付かないという以前に、人が寄りつかなくなる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（……別の意味では、既に寄りつかない城だけど）"

hide per_t_03_9
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice pet_f0018
Peter "「問題なのは……、問題なのは。\n
その姿勢です！」"

hide per_t_02_7
show per_t_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice pet_f0019
Peter "「どうして、どうして……。\n
{size=+20}彼女を膝に乗せて執務をする必要があるんですか！！？{/size}」"

hide viv_da_01_3

hide per_t_01_7


show t_viv_end1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice viv_f0107
Vivaldi "「決まっておる、このほうが仕事が進むからじゃ。\n
溜めるな、サボるなと口うるさいのはおまえじゃろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice viv_f0108
Vivaldi "「仕事をしている上司に、何を言うか。\n
文句があるのなら、わらわは仕事をせぬぞ」"

play sound se_0335
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "有言実行の女王様は早くもペンを放り出しているが、ペーターは止めなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0020
Peter "「ええ、構いません。\n
こんな羨ましい……、もとい、見ていて嘆かわしい光景など、いりません！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0004
King "「いや、それでは本末転倒というもので……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慌ててキングがぼそぼそと口を挟むが、いつものように誰も聞いていない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（まあ、座れって言われて素直に座っちゃった私も悪いんだけどね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ビバルディ、重いでしょう？\n
そろそろ下りたほうが……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口論の原因になるのは避けたいので、小さな声で提案してみる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0109
Vivaldi "「おまえが気にすることはない。\n
むしろ軽いぐらいじゃ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「そんな……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ずっしり重いとは言わないが、羽毛のようとも言えない。\n
見た目通りの重量が私の中には詰まっているはずで、決して軽いはずがない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0110
Vivaldi "「そういえば、この格好をしたときに思いついたのだがね。\n
[firstname]、いっそおまえが女王になればいいのにと」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？\n
でも、そうしたら、ビバルディはどうするの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0111
Vivaldi "「……決まっておろう。\n
この城には、もう一つ、玉座がある」"

play sound se_0433
hide t_viv_end1
show t_viv_end2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0112
Vivaldi "「椅子取りゲームも悪くないと思わぬか？」"

play sound se_0454
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
King "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ざざざと思わず後退った男を見て、ビバルディは残念そうに口を尖らせた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0113
Vivaldi "「だがな、あの男の役割を受けてしまうと、わらわの仕事を代わりにやるものがいなくなってしまうのでな……、諦めた」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「そ、そう、よかったわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（何がいいのかよく分からないけど）"

hide t_viv_end2


show per_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice pet_f0021
Peter "「仕事をしないのなら、早く彼女を下ろしてください！\n
いちゃいちゃするだけだったら、執務室でやる必要はないでしょう！！」"

hide per_t_01_7
show per_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice pet_f0022
Peter "「これでは……、生殺しです！！」"

hide per_t_01_1
show per_t_01_1 at left
show viv_da_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice viv_f0114
Vivaldi "「ほんに、男どもは言うことが皆一緒じゃな……。\n
ここはわらわの城じゃ、どこで何をしようとわらわの勝手であろうに」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぶつぶつと文句を言いながらも、ビバルディは私を床に下ろして、自分も立ち上がった。"

hide viv_da_02_2
show viv_da_01_3 at center
hide per_t_01_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0115
Vivaldi "「無粋でうるさい男のいないところに行くとしよう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの言葉で、公務はいつも通り進まないことが決まった。"

$ hi_mes()
hide viv_da_01_3

if renpy.seen_label("fushigi_end_vivaldi1") == True:
    jump fushigi_end_rose2_1
else:
    jump fushigi_end_vivaldi2

label fushigi_end_vivaldi2:

scene hm_spr_01
with stripe_l_medium

play music vivaldi_t_ali

scene v_01
with stripe_l_long

show viv_da_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0116
Vivaldi "「遊園地は楽しかったのか、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「……そうね、楽しかったわ」"

hide viv_da_01_11
show viv_da_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice viv_f0117
Vivaldi "「ふうん……、わらわがいなかったというのにか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "余程気に入っているのか、ビバルディは自室に戻っても男装姿のままだった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今は私と床に座ってお茶を飲みながら、遊園地にいたときの話を聞きたがっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あなたといるときとは別の楽しさよ。\n
……ビバルディが何をしているんだろうって、ずっと考えてばかりだったもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この城にいるときのビバルディを心配する必要なんてない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女は女王だ。\n
自身の領地にいる限り、害が及ぶことはないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大抵、この城にいるときに案じるのは、彼女のイライラで処刑されてしまう兵士やメイドのことばかりだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（でも離れてみると、やっぱり心配だった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "また薔薇で怪我をしていないか、とか。\n
知らないところで傷ついていないか、とか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（離れてみないと、普段どれだけ自分がビバルディのことを気にしているかなんて分からなかったわ）"

hide viv_da_02_1
show viv_da_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
Vivaldi "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ビバルディは？\n
私がいない間、どうだった？」"

play sound se_0174
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飲み終わったカップを置いて、ビバルディが望むままに、膝枕をする。\n
手入れの行き届いた髪や、美しい顔は、いくら見ていても飽きるものではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "女王様でいるときの彼女とは違う、そんな一面を見ることが出来て、嬉しいと思ってしまう。"

hide viv_da_02_7
show viv_da_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0118
Vivaldi "「どうということもない。\n
おまえが来る前に戻っただけじゃ」"

play sound se_0551
hide viv_da_01_11
show viv_da_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0119
Vivaldi "「決められた仕事を放っておいたり、エースとホワイトのうるさい声にイライラしたり」"

hide viv_da_01_11
show viv_da_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0119_5
Vivaldi "「メイドの淹れる茶はいつも通りで、特に不便などなかった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「そうでしょうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "変わらず過ごしていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それは喜ばしいこと。\n
いや、当然のことだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "居候の余所者一人がいなくなったぐらいで乱れるほど、ハートの城の統治者は甘くない。"

hide viv_da_01_12
show viv_da_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0120
Vivaldi "「そう……、戻っただけだというのにな。\n
イライラしているのに、処刑もしなかった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "{size=+20}「……え？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ビバルディ、今、あなたなんて言ったの？」"

hide viv_da_02_7
show viv_da_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice viv_f0121
Vivaldi "「む……、聞いていなかったのか、[firstname]。\n
イラついて仕方ないのに、処刑をする気も起きなかったと言ったのだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「……一人も？」"

hide viv_da_01_8
show viv_da_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice viv_f0122
Vivaldi "「ああ、首を刎ねると聞いても、ちっとも楽しくなかったからな。\n
無駄なことは止めた」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "{size=+20}「ビバルディ、何か変なものでも食べたの？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この女王様が処刑をしなかったことなんて、どんなに夕方が続いても今までなかったことだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "料理が気に入らなかったから斬首。\n
ドレスにほんの少し皺があったから斬首。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首を刎ねよが口癖のハートの城の女王とは思えない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（いやいや、それを考えたら、私ひょっとしてここに戻ってこないほうがよかったとか？）"

hide viv_da_01_11
show viv_da_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice viv_f0123
Vivaldi "「何を考えておるのか、だいたい想像が付くがな、[firstname]。\n
それはわらわには許されておらぬこと」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の心情を読み取ったように、ビバルディが口を開いた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「…………？」"

hide viv_da_02_2
show viv_da_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice viv_f0124
Vivaldi "「わらわには女王としての役割がある。\n
役割から外れたことばかりしていたら、いずれ盤から弾かれる」"

hide viv_da_02_1
show viv_da_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice viv_f0125
Vivaldi "「とはいえ、おまえも戻ってきたことだ。\n
これで遠慮なく、また首を刎ねられるのう」"

hide viv_da_01_2
show viv_da_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice viv_f0126
Vivaldi "「ふふふふ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（そこは適度に加減してほしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "女王様の機嫌一つで、ハートの城の人間の安寧が大きく左右されるのだから、困ったものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、何よりも大切な役に反するほど、私の存在はビバルディにとって大きい。\n
そう暗に伝えられているようだった。"

hide viv_da_01_4
show viv_da_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0127
Vivaldi "「それで……、[firstname]。\n
あとは遊園地でどうしていた？」"

hide viv_da_02_10
show viv_da_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0128
Vivaldi "「何やらネズミの家に行っていたとは聞いたが……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「あ、うん、ピアスの家に行ったのと。\n
あとは……、そうね、風邪をひいてちょっと熱を出したかしら」"

hide viv_da_02_2
show viv_da_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice viv_f0129
Vivaldi "「……なんじゃと？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までだらしなく寝っ転がっていたビバルディの目が、突然光った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「といっても、大したことは全然なくて……」"

play sound se_0052
hide viv_da_02_6
show viv_da_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice viv_f0130
Vivaldi "「馬鹿者！\n
何故それを早く言わなかった！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……ビバルディ？」"

play sound se_0328
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一気に起き上がると、彼女は私を引っ張ってベッドに放り込んだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ちょ、ちょっと……！？」"

hide viv_da_01_9
show viv_da_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice viv_f0131
Vivaldi "「ネズミめ……、おまえに病気をうつすなんて……。\n
やはり、あのとき撃ち殺しておけばよかった」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（な、何だか盛大な勘違いをしている気が……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「違うのよ、ビバルディ。\n
風邪をひいたのは、ピアスのせいじゃなくて……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし私の制止の声を聞くよりも早く、彼女は近くにあった呼び鈴を手に取った。"

play sound se_0329
pause 1
hide viv_da_02_1
show viv_da_02_1 at left
show siro_t_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0002
Maid "「はい、お呼びでしょうか、陛下」"

hide viv_da_02_1
show viv_da_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0132
Vivaldi "「今すぐ、医者を呼ぶのだ。\n
そして、わらわがいいと言うまでこの部屋には誰も入ることは許さぬ！」"

hide viv_da_01_13
hide siro_t_01_01
show siro_t_01_01 at left
show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0000
Maid "「畏まりました。\n
では、早速手配を」"

hide siro_t_01_01

hide siro_t_02_01

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの剣幕に押されたのか、疑問を口にすることなく二人のメイドはあっという間に去っていった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その間、ビバルディと言えばクローゼットの中から何枚もの服を出している。"

play sound se_0117

show viv_da_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0133
Vivaldi "「多少サイズは違うだろうが、その服よりは楽じゃろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？それって……、ビバルディの寝間着じゃ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（何でそれを私に渡してくるわけ？）"

play sound se_0251
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「あの、ビバルディ……？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベッドの上に座った相手に、疑問符を浮かべてみる。"

hide viv_da_01_11
show viv_da_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0134
Vivaldi "「心配せずともよい。\n
おまえが治るまで、わらわが付きっきりで看病してやろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "優しい口調は嬉しいのだが、それ以前に私の風邪はもう治っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「いいわよ、もう風邪だって治っているし……」"

hide viv_da_02_9
show viv_da_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_14")
voice viv_f0135
Vivaldi "「何を言うのだ、病原菌の塊のようなネズミと一緒にいたのだぞ？\n
おまえの身体にどんな病気をうつしたのか、しかとわらわが見極めてあげる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「……え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_15")
T "（見極めるって……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T "（い、一体どうやって？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "強ばったまま動きが取れなくなった私を、美しい顔がじっと見下ろしていた。"

hide viv_da_02_1
show viv_da_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0136
Vivaldi "「さて。\n
看病の定番と言えば、やはり……」"

hide viv_da_01_4
show viv_da_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0137
Vivaldi "「着替えの手伝いからだろう、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（これって）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（やっぱり城を出て行ったことを暗に責めているんだろうな、やっぱり）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "威圧感たっぷりに笑いかけてくる男装の女王様から逃れる術など、この状況であるはずがなかった。"

$ hi_mes()
hide viv_da_01_2


$ time_effect()
play music vivaldi_t_ali
pause .5

show viv_da_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0138
Vivaldi "「ふむ……。\n
やはり、こっちのほうがよいか」"

hide viv_da_01_9
show siro_t_01_01 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hei_f0003
Maid "「でも、こちらもとてもお似合いですわ」"

hide siro_t_01_01
show siro_t_01_02 at left
show siro_t_02_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice sam_f0001
Maid "「うーん、お色としてはこちらも捨て難いですし」"

hide siro_t_01_02
show siro_t_01_02 at left_center
hide siro_t_02_05
show siro_t_02_05 at center
show siro_t_02_01 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ari_f0000
Maid "「悩みますわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"


play music honobono2_a_ali

show t_viv_end3 onlayer master
with dis
hide siro_t_01_02
hide siro_t_02_05
hide siro_t_02_01
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（まさか、ビバルディに加えて、同僚にまで着せ替え人形にされるとは思わなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "病原菌騒動が落ち着いたと思ったら、今度は着せ替えだ。\n
何着かのドレスを前に、ビバルディは唸っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（しかも、まだ例の男装姿だし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すぐに飽きると思っていたのだが、ブームは意外と続いている。"

play sound se_0186
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0139
Vivaldi "「おまえには、こちらの色も合うと思うのじゃが……。\n
確かに、メイドの言うようにこれも悪くない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0004
Maid "「迷ってしまいますわね、女王様」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0140
Vivaldi "「ああ、困ったな。\n
せっかく面白いものが手に入ったのだから、服も手を抜きたくないのだが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……面白いもの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0141
Vivaldi "「ああ。\n
珍しいものだから、おまえもきっと気に入るぞ」"

play sound se_0067
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0142
Vivaldi "「しかし……、肝心の服をどれにしたものか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "真剣に悩んでいるビバルディは、服を私に合わせては首を傾げる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0002
Maid "「どれもよくお似合いですから、目移りしてしまいますわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女達の前にあるのは、色とりどりのドレスだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "既に袖を通したものも何着かあるが、届いたばかりでまだ試着もしていないものもある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（とはいえ、これ全部着ていたら、何時間帯かかることやら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "既に着せ替えを始めてから、二時間帯目だ。\n
これ以上長引くのは、さすがにそろそろ遠慮したい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0143
Vivaldi "「……ええい、悩むなど、わらわらしくもない！\n
これじゃ、これに決めた！」"

play sound se_0117
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（選んでくれるのは嬉しいけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "正直、もうどれでもいい。"

play sound se_0121
pause .4
play sound se_0167
hide t_viv_end3
show t_viv_end4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0144
Vivaldi "「うむ、よく似合う。\n
さすがわらわの見立てじゃ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0145
Vivaldi "「あとは……、化粧じゃな。\n
おいで、[firstname]」"


play music vivaldi_t_ali
hide t_viv_end4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悩んでいた時間帯が馬鹿らしく思えるほど、一瞬で着替えを終える。\n
手招きされるままに近付くと、控えていた同僚が静かに椅子を出してくれた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「化粧なんて……、似合わないかも」"


show viv_da_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice viv_f0146
Vivaldi "「心配するな。\n
おまえにはおまえのよさがあるのだから、それを出すだけじゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "椅子に腰を下ろして顔を持ち上げると、ビバルディの指がそっと頬を撫でてくれた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま化粧品を手にとって、肌に付け始める。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「ん……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（花の香り……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "乳液やファンデーションにも薔薇の香りがついているのか、優しい花の香りがする。"

hide viv_da_02_10
show viv_da_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0147
Vivaldi "「ふふふ、悪くない気分じゃな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………？」"

hide viv_da_01_10
show viv_da_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice viv_f0148
Vivaldi "「この格好で、おまえに化粧していると……。\n
まるで自分の花嫁を磨き上げておるような気分になる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……は、花嫁って」"

hide viv_da_01_6
show viv_da_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice viv_f0149
Vivaldi "「今のわらわが言うならそれほどおかしくはあるまい？\n
見た目だけならな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（……そ、それはそうなんだけど）"

hide viv_da_02_9
show viv_da_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice viv_f0150
Vivaldi "「……これは、若さ故じゃろうな。\n
おまえは本当に少し付けるだけで、十分だ」"

hide viv_da_02_5
show viv_da_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice viv_f0151
Vivaldi "「あとは……、唇か」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「あ……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "紅筆で口紅を塗られ、じっと黙り込む。"

hide viv_da_01_5
show viv_da_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0152
Vivaldi "「うむ、可愛いぞ。\n
仕上げに……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこで何かを思いついたのか、ビバルディは手にしていた紙を筆と一緒にメイドに手渡すと、一度指を鳴らした。"

play sound se_0468
hide viv_da_01_2
show viv_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「……ビバルディ？」"

hide viv_t_01_10
show viv_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice viv_f0153
Vivaldi "「何じゃ、あの格好のほうがよかったのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「そういう訳じゃないけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（何でこのタイミングで、服を変える必要があったんだろう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その疑問を口にするよりも早く、ビバルディが顔を近付けてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え……！！？」"


play music secret_a_ali

show t_viv_end5 onlayer master
with dis
hide viv_t_03_10
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_6")
voice viv_f0154
Vivaldi "「……っ、ふ。\n
さすがのわらわも、あの格好に口紅を合わせる気にはなれぬからの」"

hide t_viv_end5
show t_viv_end6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_6")
voice viv_f0155
Vivaldi "「これで、お揃いじゃ。\n
[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔が赤いどころではない。\n
息が止まっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭の中が沸騰しているようだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（お揃いって、口紅のお揃いって……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "満足げに化粧が終わった私を見下ろしてくるビバルディの唇と、私の唇に付いているものが同じだなんて思えなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（あんな綺麗な赤を、私の唇もしているなんて……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鏡で確かめたいとは思わなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同じ色だったとしても、少し色味が違って見えたとしても。\n
触れた瞬間のあの甘さは、間違いなく……、本物だったから。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（友達同士で、唇にキスなんてしないけど……。\n
でも、ビバルディに他意はないんだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城の女王様は、無邪気で、そうしたいと思ったことを実行してしまう。"


play music vivaldi_t_ali
hide t_viv_end6

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「と、ところで……。\n
先刻から面白いものが手に入ったって言っていたけど……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「何か買ったの、ビバルディ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ彼女の買い物の仕方は独特だ。\n
欲しいものを買うのではなく、苛立ちを紛らわせるために買うのである。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（何か家とか、建物を買ったとかかな。\n
それとも、ドレスに着替えているくらいだから、劇団を買い上げたとか？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思うとおり看病をされた後、ドレスに着替えている理由を教えてもらってはいない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、何の意味もなく私を着飾らせたりはしないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（それにしても……、いくら使っちゃったのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ女王様のお買い物だ。\n
桁がいくつになったかなど考えも及ばないのが、凡人の悲しいところ。"


show viv_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0156
Vivaldi "「ああ、おまえが帰ってきたら一緒に乗ろうと思っていてな。\n
ふふふ、ちょうどいい」"

hide viv_t_03_2
show viv_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0157
Vivaldi "「皆、わらわ達は出かける。\n
すぐに準備をせよ！」"

hide viv_t_01_13
show viv_t_01_13 at left
show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0005
Maid "「はい、畏まりました」"

hide viv_t_01_13

hide siro_t_02_01
show siro_t_02_01 at left
show siro_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0003
Maid "「お茶とお食事の準備もしなければ」"

hide siro_t_02_01
show siro_t_02_01 at left_center
hide siro_t_01_02
show siro_t_01_02 at center
show siro_t_02_01 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0001
Maid "「すぐにご用意を致しますわね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（お茶と食事がいるようなお出かけ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこか別荘にでも行くのだろうか。\n
しかし、それにしてはビバルディの笑い方が気になる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……まあ、少なくとも、ビバルディがいるから大丈夫よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この女王様がいるのなら、友人としても、部下としても、付いていくだけだ。"

$ hi_mes()
hide siro_t_02_01

hide siro_t_01_02

hide siro_t_02_01


scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium

play music forest_town_street_p_ali

scene bg_gen_sky_spr_day with Dissolve(2)
$ renpy.sound.play("audio/voice/se_0486.wav", loop=True)

$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0158
Vivaldi "「ははは、どうだ、[firstname]？\n
楽しいだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0159
Vivaldi "「この赤が気に入ってのう。\n
おまえが遊園地に行って間もなく買っておいたのじゃ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「そ、そうね。\n
綺麗な、赤よね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（乗っている人間にとっては、車体の色なんて、ほとんど関係ないけど）"

stop sound
show t_viv_end7and10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "真っ赤なスポーツカーを運転するビバルディに、そう相槌を打つ。\n
私は助手席に座って、膝の上にウサギ姿のペーターを乗せていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0023
Peter "「何を言っているんですか、こんな暴走するものに彼女を乗せて……。\n
事故でも起こしたらどうするつもりなんです、陛下！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0160
Vivaldi "「事故だと？\n
馬鹿なことを申すな、ホワイト」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0161
Vivaldi "「わらわはハートの女王ビバルディじゃ。\n
わらわの車にぶつかるような愚か者は、皆、処刑してくれるわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「ぶつかった後に処刑しても、遅いと思うんだけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（少なくとも、走る場所が城の裏手でよかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この速度を出すのはさすがに無謀と思ったのか、領地の中でも比較的ひとけのない場所でビバルディは愛車を走らせている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう、愛車。\n
真っ赤な、真っ赤な……、高級車を。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（デタラメすぎる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "燃料はどうしているんだろうとか、一体どこからこんなものを持ってきたんだとか、色々と突っ込みたいところはあるが、私も自分の命のほうが大事だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先刻からシートとベルトに身体を固定させて、身動き一つ取れずにいる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（下手に喋ったら舌を噛みそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舗装されている道ではないから、先ほどから車体は上下に激しく揺れていた。"

hide t_viv_end7and10
show t_viv_end8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0162
Vivaldi "「だいたい、どうしておまえがわらわの車に乗っておるのだ、ホワイト。\n
おまえの乗車を許可した覚えはないぞ、疾く降りよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0163
Vivaldi "「それともつまみ出されたいのか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0024
Peter "「こんな～～～も逃げ出すような車に、彼女だけ乗せられるはずがないでしょう。\n
いざというときには、僕が身を挺して守りますからね、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0164
Vivaldi "「失礼なことを言うウサギじゃな。\n
わらわの車を整備不良とでも疑うつもりか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0165
Vivaldi "「エアバッグならちゃんと作動する！\n
前回キングで試したばかりじゃ、問題はない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0025
Peter "{size=+20}「事故を前提で運転なんかしないでください！！！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0026
Peter "「陛下が一人でクラッシュして、～～～～～～になるのならともかく、彼女までそんなことになったら……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0027
Peter "「僕は死んでも死にきれません！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "危険な会話をずっと聞いていると、不安からだろう、眩暈がした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（そういえば……、後ろの皆はどうなのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "力を入れ続けたせいか強ばった身体を少し傾けて、サイドミラーを覗いてみる。\n
森の木立の中に、目に痛い赤い上着がひらひらと翻っているのが見えた。"

hide t_viv_end8
show t_viv_end9 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0032
Ace "「ははは、ずるいよなあ、陛下。\n
自分だけ最高級車で、俺達は中古車だもんなあ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0033
Ace "「……それも、以前に陛下が乗り潰したやつなんてさ。\n
まあ、これもまだいけそうだからいいけど」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0005
King "「わわわ、エ、エース！\n
ハンドルを切るでない！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0006
King "「そっちに行ったら森の中にしか行けぬ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（あっちに乗っていたら、乗っていたで不安要素が山盛りだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それ以前に、どうしてあの男にハンドルを持たせてしまったのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこでも迷える彼に、車のハンドルなんて持たせたらどういうことになるのか、すぐに想像が付くだろうに。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0028
Peter "「あなただっていやですよね、[firstname]？\n
あんな～～～～の運転する車なんて……、自殺行為ですっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その自殺行為の中で必死に頑張っている人がいるのだが。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「まあ、確かに……。\n
キングならともかく、エースの運転する車に乗ろうとは思わないわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちなみに、メイドや兵士達は彼らの乗っているものよりも更にランクが低いので、木立の向こうに消えてしまっていて、姿が見えない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（お弁当とか、お茶とかは、皆あっちなのにな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "車を乗り回したいという理由で決まった目的地の丘まで、競争になっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "重鎮達が揃ってハートの城をあけていいのかとも思うが、メイドが優秀なので、問題ないだろう。"

play sound se_0455
hide t_viv_end9
show t_viv_end7and10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「と、ところで、ビバルディ。\n
何で、車に乗るのに、わざわざ……、ドレス、着る必要があった、の？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舌を噛まないように慎重に口を開くと、ビバルディは「うむ」と頷いた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0166
Vivaldi "「この手の車に乗るのならば、助手席には恋人を乗せるものなのだろうが。\n
男のために運転する気になどならぬからの」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0167
Vivaldi "「わらわが一番好きなものを乗せることにした」"

hide t_viv_end7and10
show t_viv_end11 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（一番……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（好きなもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉に聞き間違いがないかどうか不安になって、ビバルディを見たが、彼女もまた視線を私のほうに向けていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0168
Vivaldi "「わらわの宝物、わらわだけのかわいいお人形。\n
……まあ、そのいらぬウサギが付いてきたことだけは、不満じゃが」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0029
Peter "「不満は僕も同じです！\n
ですが、それよりも……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0030
Peter "{size=+20}「前を見て運転してください！！！」{/size} "

hide t_viv_end11

play sound se_0751
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「きゃっ」"

play sound se_0753
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "道などほとんどないような場所なのだ。\n
当然、木の枝が伸びたところでは、こうやって車にぶつかったりもする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（……ある意味、先行している段階でこの車が一番危ないのかもしれないわね）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice pet_f0031
Peter "「ほら、言ったそばから……。\n
大丈夫ですよ、[firstname]、何があってもあなただけは僕が必ず……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice viv_f0169
Vivaldi "「ええい、先刻からやかましいぞ、ホワイト！」"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ビ、ビバルディ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice pet_f0032
Peter "「な、何をするんですか、陛下。\n
放してください！」"

play sound se_0046
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディに襟首を捕まれたペーターは、足をばたつかせて抵抗する。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0170
Vivaldi "「お黙り。\n
やかましいウサギは、同じくやかましい男どものところにいくがよい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、ビバルディは……。"

play sound se_0133
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「！！！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「ペーター！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
Peter "「[firstname]！！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぽーんと投げられて、白いウサギは遠くへ遠くへ流れていき、そして。"

play sound se_0062
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0007
King "「ふぐ、な……！？\n
ふぐ、ほ、わい……？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0034
Ace "「あれー、ペーターさんが降ってきた。\n
この森って、おかしなものが空から降ってくるんだね！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0035
Ace "「ははは、でもこんなウサギさんが降ってきても、喜ぶのは腹を空かせたクマさんぐらいかもしれないけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キングの顔面に着地する形で落下したペーターは、エースの笑い声に負けず劣らずの大きな声を上げた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0033
Peter "「ば、馬鹿なことを言ってないで、早く追いかけなさい、エース君！」"

play sound se_0331
pause 1
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0034
Peter "「いえ、君にハンドルを任せたままだと、永遠に追いつけなさそうですから、そこをどきなさいっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0035
Peter "「僕が運転します！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人型に戻ったペーターは、エースからハンドルを奪おうともみ合っている。\n
キングのことを踏みつけているが……、まるで気にはしていない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0036
Ace "「えー、せっかく調子が出てきたのに。\n
それに、運転手交替なんかしていたら、ますます離されちゃうぜ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「～～～～っ！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0036
Peter "「ああ、[firstname]！\n
必ず僕が行きますから、もうしばらく待っていてくださいね！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「何だか後ろの車でごちゃごちゃ言っているようだけど……。\n
とりあえず、落ち着いたのかな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice viv_f0171
Vivaldi "「あいつらのことじゃ、殺しても死なぬ。\n
気遣うだけ無駄というもの」"

play sound se_0487

show t_viv_end12 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐん、と。\n
身体にかかる圧迫感が強くなる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディが更に加速したのだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ビバルディ！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice viv_f0172
Vivaldi "「もうそろそろ目的地の丘じゃ。\n
着いたら、後ろののろまどもを待ってやるとしよう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice viv_f0173
Vivaldi "「それまでは、二人っきりじゃ。\n
わらわのことだけ考えていればよい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（そんな顔したら、怒れないじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まるで自慢するような、嬉しくて仕方ないような顔。\n
彼女がたまに私に見せてくれる、魅力的な表情に私は滅法弱いのだ。"

$ hi_mes()
hide t_viv_end12

play sound se_0485

play music forest_town_square_p_ali

scene map_bg_spring_day
with stripe_l_medium

scene bg_gen14_ok
with stripe_l_long
pause .5

show viv_t_02_11 at center
with dis
pause .5
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0174
Vivaldi "「ふむ、このあたりでよかろう。\n
おや、[firstname]、足下がふらついているようじゃが……」"

hide viv_t_02_11
show viv_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0175
Vivaldi "「まさか、車酔いか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「ううん、酔ったわけじゃないんだけど……。\n
身体に力が入っていたみたい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "がたんと車体が揺れる度に力を込めていた反動だろう。\n
全身がぎしぎしと軋んでいる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（まあ、無事に下りられただけマシかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスといい、ビバルディといい、私の周りにいる人間は、どうしてハンドルを握ると暴走してしまうのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（ビバルディは人が変わるというよりは、いつもの調子で乗っていた感じだけど）"

hide viv_t_01_7
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0176
Vivaldi "「そうか、ならばよいが。\n
わらわも少しはしゃぎすぎた」"

hide viv_t_01_3
show viv_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0177
Vivaldi "「後ろが追い付くまで、しばし休憩にしよう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そういって、ビバルディは近くの木の下に腰を下ろした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ちょうどいいわ」"

hide viv_t_03_6
show viv_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Vivaldi "「？\n
[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言葉に顔だけ向けてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は彼女の横に同じように座ると、持っていた小さなポーチを開けた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（いつにしようかと思って、ずっと持っていた甲斐があった）"

hide viv_t_03_12
show viv_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice viv_f0178
Vivaldi "「おまえ、それは……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「約束していたマニキュアよ。\n
この前、街で買ってきたの」"

hide viv_t_01_5


scene t_cut_viv_end1u
with dis
pause 1

scene t_cut_viv_end1
with dis

show viv_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（今ひとつ上手に塗れる自信はないけど……。\n
少なくとも、今なら誰かの目に付くこともないし）"

hide viv_t_01_5
show viv_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_14")
voice viv_f0179
Vivaldi "「色は……、ああ、赤か」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「安全策を選んだわけじゃないのよ。\n
……やっぱり、ビバルディにはこれが一番似合うと思って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「違うほうがよかった？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "化粧品は赤と一口に言っても、様々な種類がある。\n
私が選んだものは、特に濃い真っ赤なものだ。"

hide viv_t_03_10
show viv_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0180
Vivaldi "「いや、おまえが選んだものならば何でもいい」"


play music happy_a_ali

scene bg_gen14_ok
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「……気に入らなかったら、そういってね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相手が差し出す手を取る。"

hide viv_t_02_5
show viv_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0181
Vivaldi "「心配せずとも、わらわは女王だ。\n
我慢などせぬよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（嘘つき）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "日頃は癇癪持ちのように傲慢な命令ばかり下す女王様が、私に甘いことは知っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのためにも、甘えないように自己暗示をかけていたのだが、きっと彼女にはお見通しだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「じゃあ、早速……」"

hide viv_t_01_1
show viv_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0182
Vivaldi "「お待ち。\n
塗るのは、この指からじゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの手を取って下地を塗ろうとしたところで、彼女は小指を立てて見せた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「小指？」"

hide viv_t_03_10
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0183
Vivaldi "「ホワイト達が追い付くまでに、全部を塗るのは無理じゃろう？\n
だから、まずはここから塗っておくれ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（それもそうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "多少性能が落ちるとはいえ、向こうの足も決して遅くはないのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（だったら、あまり欲張らないほうがいい）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「分かったわ」"

$ hi_mes()

play music dream_tsuduki_a_ali
hide viv_t_01_3


show t_viv_end13 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Vivaldi "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "静かに、けれど心地よい緊張感の元で、私はビバルディの爪に色を付けていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "練習では、はみ出さないようにと慎重になればなるほど失敗したが、今は自然と手が動いてくれる。"

hide t_viv_end13
show t_viv_end14 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「……！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「出来た！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice viv_f0184
Vivaldi "「うむ、うまいではないか。\n
慣れぬようだったら、わらわが教えてやろうと思ったのに……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「女王様の手を煩わせたら申し訳ないもの。\n
練習してきたのよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（でも、本当にうまく出来たわ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_1")
T "（練習でもこんなに上手に出来たこと、ないかも）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "はみ出してもいないし、まずまずの出来映えだった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "アクセントとして中央にハートの石を置いてみたが、意外と子供っぽくなく、落ち着いたデザインになっている。"

hide t_viv_end14


show viv_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0185
Vivaldi "「勉強熱心な子だこと。\n
[firstname]、わらわにそれをお渡し」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「はい、どうぞ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（別の指に塗るのかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が塗ったのは彼女の左の小指だけだ。\n
慣れているのなら、もう一つぐらい塗れるだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "……しかし。"


show t_viv_end15 onlayer master
with dis
hide viv_t_03_10

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0186
Vivaldi "「礼に、わらわもおまえの指を染めてあげる」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "反対に腕を取られ、その言葉に驚く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え……、いっ、いいわ！\n
マニキュアなんて、私にはまだ早いもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城ではメイドの仕事もしているのだ。\n
飾り付けてもらっても、すぐに駄目にしてしまう可能性のほうが高い。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0187
Vivaldi "「わらわがおまえに付けてやりたいと言っておるのだ。\n
文句を言うなら不敬罪じゃぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「で、でも……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "うまくもない自分がつけたマニキュアと、ビバルディの付け方では、全然比較にならないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それぐらい彼女にも分かっているだろうが。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「あ」"

hide t_viv_end15
show t_viv_end16 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（すごい、早い上に綺麗）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず見とれてしまうほどに、ビバルディは上手に私の爪を染めていく。\n
彼女の小指に灯った赤と同じ色に。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ビバルディのことだから、こういうのは全部メイドさんのお仕事かと思っていたわ」"

hide t_viv_end16

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただじっと見入っているのも申し訳なくてそんなことを言うと、ビバルディは小さく肩を揺らした。"


show viv_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0188
Vivaldi "「そうじゃな。\n
城では滅多に自分では付けぬ……、ましてや女王自ら誰かに塗ってやるなど初めてのことだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「…………」"

hide viv_t_02_11
show viv_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
voice viv_f0189
Vivaldi "「おまえはわらわに心をくれたからな。\n
これは、そのお返しじゃ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首をかしげると、ビバルディは目を細めて小指を見せる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「た、確かにハートっていうけど、それは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "爪の上に乗せた石は、ただ形がハートと言うだけだ。\n
それも既製品でしかない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（こんなに喜んでくれるのなら、もう少し凝ったものを探してくればよかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "店にいくつもの飾りはあったが、所詮素人の私に扱えるものはシンプルなものしかなかったのだ。"

hide viv_t_02_4
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0190
Vivaldi "「形だけではないぞ。\n
おまえがわらわのことだけを考えて、染めてくれたのだ」"

hide viv_t_01_3
show viv_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0191
Vivaldi "「嬉しくないはずがないだろうに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうこう話す間に、既に下地は塗り終えたのだろう。\n
ビバルディは一度筆を戻すと、小さな瓶を取り出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あ……。\n
それ、薔薇？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小瓶の中に入っているのは、小さな花のように見えた。"

hide viv_t_03_3
show viv_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0192
Vivaldi "「ああ、そうじゃ。わらわの一番好きな薔薇から作ったのだ。\n
乗せるだけで、凹凸もなく密着する優れものだぞ」"


show t_viv_end17 onlayer master
with dis
hide viv_t_01_2

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T "「綺麗」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤の中にあっても、埋没しない強い赤が、指の中で咲いている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0193
Vivaldi "「それが取れたら、また新しいものを付けてあげる。\n
取れてしまったら、わらわのところに来るのだよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……いいの？\n
そんなことを言っていたら、何度もビバルディのところに行くことになっちゃうわよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0194
Vivaldi "「構わぬ。\n
いや、取れてもわらわのところに来ないようであれば、そのほうが問題じゃ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0195
Vivaldi "「約束するだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_10")
T "（あ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（だから、小指だったの？）"

hide t_viv_end17
show t_viv_end18 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城を離れるときにも交わした、指切り。\n
あのときと同じ二本の指には、同じ赤が灯っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（なんだろう、どきどきする）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「ええ、約束するわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice viv_f0196
Vivaldi "「嘘をついたら……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_6")
T "「首を刎ねる？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "指を絡めながら、戯れるように聞いてみる。\n
針千本と言うよりも、彼女の場合にはしっくり来る罰だろう。"

hide t_viv_end18
show bg_gen_sky_spr_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0197
Vivaldi "「……いや」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "意外にも彼女は首を横に振って、そして……。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0198
Vivaldi "「あの姿で、押し倒してしまうよ、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小指を引かれて、掌にそっと、女王様からのキスが落ちる。"

hide bg_gen_sky_spr_day


show viv_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0199
Vivaldi "「ふふふ、おまえ、あの姿のわらわにもときめいただろう？\n
だから、あの格好でいじめてあげる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（首を斬られるよりも怖い……）"

hide viv_t_03_2
show viv_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_9")
voice viv_f0200
Vivaldi "「だから、この指はわらわがもらってあげる。\n
他の誰にも、あげてはならぬよ」"

hide viv_t_01_4
show viv_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_9")
voice viv_f0201
Vivaldi "「代わりに、わらわのこの指も、おまえにあげるから」"

hide viv_t_02_9
show viv_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_9")
voice viv_f0202
Vivaldi "「……約束したぞ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大きく頷くと、彼女もまた頷いてくれた。"


play music forest_town_square_p_ali
hide viv_t_02_4


scene bg_gen_sky_spr_day
with dis
play sound se_0486
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「……ん？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（あの音は）"

play sound se_0485
play sound se_0455

scene bg_gen14_ok
with dis
pause 1

show ace_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0037
Ace "「ふう、やっと追い付いたぜ。\n
陛下の車って、本当に速いんだなあ」"

hide ace_t_02_8
show ace_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0038
Ace "「引き離されるばっかりで、全然追い付けなかった」"

hide ace_t_03_7
show ace_t_03_7 at left
show per_t_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pet_f0037
Peter "「引き離されたのは、君のせいでしょう、君の！」"

hide per_t_01_7
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pet_f0038
Peter "「切るなと言っているのにハンドルを右に左に切って……。\n
あれさえなければ、もう少し早かったはずですよ、エース君！」"

hide ace_t_03_7
show ace_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0039
Ace "「えー、俺だけが悪いの？」"

hide ace_t_03_9
show ace_t_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0040
Ace "「そういうペーターさんだって、ウサギの姿のままでいたほうが軽かったのに、わざわざ大きくなるから重くなったんだと思うんだけどなあ」"

hide ace_t_01_6
show ace_t_01_6 at left_center
hide per_t_02_7
show per_t_02_7 at center
show king_t_02_07 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
King "「…………」"

hide king_t_02_07
show king_t_02_08 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice kin_f0008
King "「気持ち、悪い」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（どんな運転をしてきたんだろう、あの人達）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エース達のほうを見やれば、乗っていた車は木にぶつかって大破してしまっていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キングはナイトメア並の顔色の悪さで、突っ伏している。\n
平然としているのは、エースとペーターの二人だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（……あの二人が調子を崩すこと自体、まずないだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らはまだこちらの存在に気付いていないようだ。\n
少し遅れてやってきたメイド達が、先に丘の上まで到着する。"

hide per_t_02_7

hide king_t_02_08

hide ace_t_01_6
show siro_t_02_01 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0006
Maid "「ああ、陛下。\n
やっと追い付きました」"

hide siro_t_02_01
show siro_t_02_01 at left
show heisi_t_02_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0005
Soldier "「もう少しスピードを落として頂かないと……。\n
我々の車ではとても追い付けません」"

hide siro_t_02_01
hide heisi_t_02_03
show heisi_t_02_03 at left
show viv_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

hide viv_t_02_7
show viv_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0203
Vivaldi "「ふん、お邪魔虫共が……。\n
せっかくわらわとこの子がいい雰囲気だったというのに」"

hide heisi_t_02_03

hide viv_t_01_8
show viv_t_01_8 at left
show siro_t_02_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0004
Maid "「……あら、お邪魔してしまいましたか？」"

hide viv_t_01_8

hide siro_t_02_04
show siro_t_02_04 at left
show heisi_t_01_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0004
Soldier "「それは大変失礼致しました」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え……、いいのよ、そんな気にしないでっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（な、何で皆して私に頭を下げるわけ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "残念がっているのはビバルディなのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何故彼らが私に頭を下げるのかわからなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "するとメイドの一人が私とビバルディを指差す。"


show t_viv_end18 onlayer master
with dis
hide siro_t_02_04

hide heisi_t_01_06

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0002
Maid "「だって、そんなにしっかりと指切りされていたら……。\n
ねえ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（そういえば、指……。\n
繋いだままだった）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！！！」"

hide t_viv_end18

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭の中が浮かれていた。\n
しかし、真っ赤になる私とは逆にビバルディは堂々としたものだ。"


show viv_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0204
Vivaldi "「邪魔だと思うのなら、少しは察して席を外せばよかろう。\n
図々しい」"

hide viv_t_01_9
show viv_t_01_9 at left
show siro_t_02_08 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0007
Maid "「も、申し訳ありません」"

play sound se_0307
hide viv_t_01_9

hide siro_t_02_08
show siro_t_02_08 at left
show siro_t_02_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0005
Maid "「でも、せめてお茶などはお持ちしなければ申し訳ないかと」"

play sound se_0038
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言いながら彼女達は持参したポットやお弁当を広げていき、あっというまにピクニックの用意をすませた。"

hide siro_t_02_08

hide siro_t_02_02
show siro_t_02_02 at left
show siro_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0003
Maid "「さあ、どうぞ」"

hide siro_t_02_02

hide siro_t_01_02


show viv_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0205
Vivaldi "「……おいで、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "指を繋いだまま、ビバルディが座る。\n
当然、私もその横に座る形になる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「ビバルディ……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（いつまでこうしているつもりなのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視線でそう伺うと、ビバルディは答える。"

hide viv_t_02_10
show viv_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0206
Vivaldi "「ふふふ、離してもいいが。\n
離す前に、もう一度約束しておくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「約束……」"

hide viv_t_02_10
show viv_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice viv_f0207
Vivaldi "「ああ」"

hide viv_t_03_10
show viv_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice viv_f0208
Vivaldi "「おまえの薔薇が見つからないときには、わらわの元に来ると約束しておくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薔薇が見つからないときに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その言葉をしばらく反芻してから、私は首を傾げた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「見つからないときだけしか、行っちゃいけないの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（違うわよね？）"



hide viv_t_03_1






show t_viv_end19 onlayer master
with dis
play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の意図を察したのだろう、彼女は驚いたように一度目を大きく見開いて。\n
そして、指を外すと強く抱き締めてきた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0209
Vivaldi "「……いや」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0210
Vivaldi "「約束の指は交換しただろう。\n
いつでも、おいで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「……ええ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "指を解かれても。\n
同じ赤が、あなたの元に続いていると確信出来るから。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「あなたも、いつでも私のところに来てね、ビバルディ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あなたの行き先に、いつでも私がいるように。\n
薔薇と心は、いつでも繋がっている。"




hide t_viv_end19
show white onlayer master
with compress_extralong
scene black with compress_extraextralong
pause 1

stop music
$ renpy.movie_cutscene("endroll_a.mpg")
#return
