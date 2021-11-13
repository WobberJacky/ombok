
scene map_bg_winter_day
with dis
label fushigi_end_gray1:
$ clockanim()


scene map_bg_winter_day
with dis

scene charasel_bg_tower_day
with dis

play music nightmare_t_ali

scene n_01
with Dissolve(1.2)

show nai_s_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0476
Nightmare " 「ああ、[firstname]！\n
帰ってきてくれたんだな……」"

hide nai_s_02_12
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0477
Nightmare " 「……おかえり」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「ごめんなさい、ナイトメア。\n
そのもう少し早めに帰ってこられるかと思ったんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは私の顔を見るなり、すぐに声をかけてくれた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "友人であり、上司でもある夢魔。\n
隻眼の瞳に浮かぶ安堵の色が嬉しくも、申し訳なく思う。"

hide nai_s_02_1
show nai_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0478
Nightmare " 「気にしなくていい。\n
君が帰ってきてくれた……、それだけで私は涙が出るほど嬉しいよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「ナイトメア」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（こんなに喜んでくれるなんて……。\n
留守が長引いて、悪かったかも）"

play sound se_0492
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今にも泣き出しそうな顔で私を見ていたナイトメアは、がしっと私の手を掴んだ。\n
顔色の悪い顔が、今は若干紅潮しているようにさえ見える。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（何だか、感動するにしても激しすぎない。\n
これ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私も歓迎されて嬉しくないわけではない。\n
だが、帰宅を告げに部屋にやってきた途端この対応では、さすがに疑問が浮かぶ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私がいない間、グレイのあの料理でも振る舞われたのだろうか。"

hide nai_s_03_10
show nai_s_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0479
Nightmare " 「いや、あの地獄のフルコースは一度もテーブルに出なかった。\n
そこは何とか乗り切ったんだが……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（じ、地獄のフルコース……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の料理は彼の一途さを知っていても、擁護することが出来ない代物だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "てっきり私がいない間に手料理が振る舞われて、阿鼻叫喚という場面を想像したのだが、そうではなかったらしい。"

hide nai_s_03_5
show nai_s_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0480
Nightmare " 「問題はそれじゃない」"

hide nai_s_02_5
show nai_s_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0481
Nightmare " 「君がいない間……。\n
{size=+20}グレイが、どんなに荒れていたことか{/size}」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T " 「え？\n
それって、どういうこと？」"

hide nai_s_01_12
show nai_s_01_12 at left
show toustaff_a1_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice tan_f0043
Assistant " 「ナイトメア様の仰るとおりです」"

hide nai_s_01_12

hide toustaff_a1_6
show toustaff_a1_6 at left
show toustaff_b1_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice oto_f0049
Assistant " 「あなたがいない間のグレイ様は、その……。\n
本当にイライラしていらして」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T " 「は？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（あのグレイがイライラしていた？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイと、イライラ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこぞの女王様ならともかく、グレイとそれは縁遠い単語の組み合わせではないだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（何しろ、普段からナイトメアの世話で忍耐力を試されているような人だし）"

hide toustaff_a1_6
show toustaff_a1_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice tan_f0044
Assistant " 「ほら、例の小火騒ぎがあったでしょう。\n
しばらく喫煙場所にも制限がかかりまして……、ご自分の部屋か談話室ぐらいでしか吸えなかったんです」"

hide toustaff_a1_4
show toustaff_a1_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice tan_f0045
Assistant " 「でも、グレイ様が部屋でゆっくり出来ることなんて……、ほとんどありませんし」"

hide toustaff_b1_9
show toustaff_b1_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice oto_f0050
Assistant " 「ぴりぴりしっぱなしだったんですよ、グレイ様」"

hide toustaff_b1_7
show toustaff_b1_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice oto_f0051
Assistant " 「何しろあなたがいない間……。」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice oto_f0051_5
Assistant " 「このナイトメア様が一度も脱走を図らず、{size=+20}執務室でちゃんと仕事をしていたぐらい{/size}なんですから」"

play sound se_0042
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T " 「！！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T " 「そんなにすごかったの、グレイ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに彼の机に積まれた書類はいつもよりも少ない。\n
日頃溜まっている量が量なので、最初は気付かなかったが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "決裁の判子一つ押すのにも、いつも駄々を捏ねるナイトメアが、一度も逃げ出さなかったなんて。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "{size=+20}（奇跡だわ）{/size}"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんな効果があるのなら、もう少し離れていたほうがよかっただろうか。"


show nai_s_02_5 at center
hide toustaff_a1_11
hide toustaff_b1_4
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0482
Nightmare " 「待て待て！\n
[firstname]、君は、驚くところを間違えているぞっ」"

hide nai_s_02_5
show nai_s_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0483
Nightmare " 「この場合、驚くべきところは、だ。\n
あいつがどれだけ周囲に負のオーラを撒き散らしながら、生活していたかということであってだな」"

hide nai_s_03_5
show nai_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0484
Nightmare " 「その上で、恐怖の大魔王から逃げ出さずに、真面目に仕事をしていた偉い上司を褒め称え……」"

hide nai_s_02_3
show nai_s_02_3 at left
show gre_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0274
Gray " 「……俺が、何ですか、ナイトメア様？」"

hide nai_s_02_3
show nai_s_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare " 「！！！！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「グレイ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "話題に上っていた当の本人は、何でもないように顔を見せた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その顔は私がよく知るグレイのもので、ナイトメアがいうような恐怖の大魔王とは思えないのだが。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔色を変えたナイトメアと背後の部下達の様子を見る限りでは、まったくのデタラメというわけでもないようだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（荒れていたグレイ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（見てみたいような、見てみたくないような、複雑な気持ちだわ）"

hide gre_t_01_11
show gre_t_02_4 at center
hide nai_s_03_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice gra_f0275
Gray " 「[firstname]、仕事のことで少し相談があるんだ。\n
俺の部屋まで来てくれるか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T " 「あ、うん。\n
大丈夫よ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不在にしていた間に、私の仕事も溜まっていることだろう。\n
そう考えれば自然な流れだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（ナイトメアでもあるまいし。\n
グレイが話を逸らすとも思えないもの）"

hide gre_t_02_4
show gre_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice gra_f0276
Gray " 「そうか、ありがとう。\n
おい……、おまえ達」"

hide gre_t_03_8
show gre_t_03_8 at left
show toustaff_a1_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Assistant " 「！」"

hide gre_t_03_8
show gre_t_03_8 at left_center
hide toustaff_a1_5
show toustaff_a1_5 at center
show toustaff_b1_6 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice oto_f0052
Assistant " 「は、はい……」"

hide gre_t_03_8
show gre_t_01_5 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice gra_f0277
Gray " 「無駄口を叩いている暇があるなら、手を動かしてもらおうか。\n
それとも……、余計な口が叩けないようにしてほしいか？」"

hide toustaff_a1_5
show toustaff_a1_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice tan_f0046
Assistant " 「い、いえ……。\n
それでは、俺達はこのあたりで」"

hide toustaff_b1_6
show toustaff_b1_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice oto_f0053
Assistant " 「ナイトメア様、終わった書類、頂いていきますね」"

play sound se_0311 volume .7
hide toustaff_a1_8

hide toustaff_b1_8
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの部屋に一緒にいた二人はそんなことを言いながら、あっという間に姿を消してしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（逃げ足の速さだけは上司譲りよね）"

hide gre_t_01_5
show gre_t_01_5 at left
show nai_s_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0485
Nightmare " 「あー、おまえ達！\n
上司を見捨てて逃亡とは、どういうことだ！」"

hide nai_s_03_3
show nai_s_03_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice nig_f0486
Nightmare " 「お、おーい………、酷い。\n
ずるいぞ……、私だって、逃げたいのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの声が徐々に弱々しくなり、そして彼は恐る恐る目の前に立っているグレイと視線を合わせた。"

hide nai_s_03_5
show nai_s_03_5 at right
hide gre_t_01_5
show gre_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0278
Gray " 「ずいぶん楽しそうなお話でしたね、ナイトメア様」"

hide nai_s_03_5
show nai_s_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0487
Nightmare " 「いや、あのな、グレイ。\n
別に、私はおまえのことを……っ！？」"

hide nai_s_02_10
show nai_s_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0488
Nightmare " 「な、こら……、隠せ、隠せ！！\n
おまえは、おい、なんてことを……！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見る見るうちにナイトメアの顔色が青くなっていく。\n
対するグレイはにこにこと楽しそうだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……一体、何を見ているのかしら）"

hide gre_t_03_4
show gre_t_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gra_f0279
Gray " 「ああ、申し訳ありません。\n
まだ心が荒れているようで、セーブが効かないんでしょうね」"

hide gre_t_02_3
show gre_t_01_15 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gra_f0280
Gray " 「何しろ、恐怖の大魔王ということでしたので……、大魔王ならこれぐらい、普通かと。\n
さあ、行こうか、[firstname]」"

play sound se_0551 volume .7
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイは、そのまま私の腕を引くと抱き寄せてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「グレイ？」"

hide gre_t_01_15
show gre_t_03_10 at center
hide nai_s_03_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice gra_f0281
Gray " 「君と少し話がしたいんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見上げた顔はいつになく真剣な表情をしていた。"



hide gre_t_03_10
with dis
$ hi_mes()

scene n_01
with stripe_l_medium

scene charasel_bg_tower_day
with stripe_l_medium

scene g_01
with stripe_l_long

play music dream_tsuduki_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "久しぶりに入ったグレイの部屋。\n
部屋に入るなり手を引かれて腰掛けたグレイの上に座らされてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっと見つめてくる視線は心地よくも、どこか怖かった。"

show gre_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0282
Gray " 「どうして……、突然、離れるなんて言い出したんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「それは……。\n
だって、皆にも迷惑をかけてしまったし」"

hide gre_t_02_13
show gre_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice gra_f0283
Gray " 「だが、君がいなくなって……。\n
一番迷惑を被ったのは、俺だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（怒っていたの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう、私には怒られるだけの理由がある。\n
私がいない間、グレイはずっとこの塔で働いていたのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（なのに、私は……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの誘いを断ることもせず居候という環境に甘えて、好きなように過ごしていただけだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T " 「……ごめんなさい。\n
グレイに悪いことをしたわ」"

hide gre_t_02_7
show gre_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
voice gra_f0284
Gray " 「本当に悪いと思っているのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T " 「……ええ、だから」"

hide gre_t_01_13
show gre_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice gra_f0285
Gray " 「だったら、あの言葉は撤回してくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "真剣な声で言うグレイとは対照的に、私はきょとんとした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「あの言葉？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（……何か、言ったっけ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイのこの雰囲気では、恐らくクローバーの塔を出てからのことではないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小火騒動が起きた直後か、その最中か……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（あのとき、ばたばたしていたから、グレイが何を指しているのか、よく分からないんだけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T " 「ええと……。\n
どの話かしら？」"

hide gre_t_01_11
show gre_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
Gray " 「…………」"

hide gre_t_02_11
show gre_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice gra_f0286
Gray " 「はあ……。\n
君が、俺と休憩をずらすと言った、あの発言だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T " 「だって、どちらかがずらさないと……。\n
{size=+20}誰がナイトメアに仕事をさせるの？{/size}」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何よりも、仕事が溜まって一番頭を抱えるのは塔の主ではなく、今、私の目の前にいる彼だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアが自業自得で書類に埋もれるのであれば、私も何も言わないし、ここまで仕事をせっつかない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（でも、そのしわ寄せは主にグレイに来るんだもの）"

hide gre_t_03_3
show gre_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice gra_f0287
Gray " 「……いや、仕事ももちろん大事なんだが」"

hide gre_t_02_12
show gre_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice gra_f0288
Gray " 「俺は、君と一緒に休憩出来ないほうが……、辛い」"


show t_gre_end1 onlayer master
with dis
hide gre_t_01_14
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「……！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "音を立てて、唇が額に触れる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0289
Gray " 「君とこういうことが出来ないなら……。\n
休憩なんて入れず、過労死したほうが、まだマシだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "馬鹿なことを真剣な表情で言う。"

hide t_gre_end1
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「グレイ……、あのね」"

play sound se_0472
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "リボンを解こうとする手を止めて、私は持っていた小さな袋を差し出した。"


show gre_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0290
Gray " 「これは？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「あなたへのお詫びに……、大したものは買えなかったけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むしろ、これでよかったのか、未だに自分でも自信がない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイは大人で、給料もしっかりと得ている立派な人だ。\n
私が渡すまでもなく、こんなもの、自分でも手に入れられるに違いない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（でも、自己満足でも、せめて申し訳なかった気持ちだけは伝えたい）"

hide gre_t_02_10
show gre_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice gra_f0291
Gray " 「開けてもいいのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T " 「……うん」"

play sound se_0470
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頷く私の返事を得て、彼は早速包装紙を剥がした。\n
中から出てきたものを見て、目を見張る。"


show t_gre_end2 onlayer master
with dis
hide gre_t_02_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0292
Gray " 「硝子製の灰皿と……、携帯灰皿？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T " 「グレイのことだから、もう持っているかとは思ったんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼のこの部屋にも灰皿は置かれている。\n
溜まっていない吸い殻が、ここしばらくの忙しさを物語っていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「携帯灰皿だったら、吸う場所も広がるし、使いやすいかと思って」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gra_f0293
Gray " 「ああ、そうだな。\n
ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gra_f0294
Gray " 「この硝子製の灰皿も、使わせてもらうよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T " 「あ、待って。\n
それは……、ちょっと違うの」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
Gray " 「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今にも新しい灰皿を下ろそうとしたグレイを制して、私は続けた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T " 「それは、その……。\n
私の部屋に置こうかと思って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T " 「勿論、グレイが使ってくれるなら、あなたの部屋に置いてもらってもいいんだけど」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
voice gra_f0295
Gray " 「君は、煙草を吸わないだろう？\n
まさか……、吸いたいなんて言い出す気じゃ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T " 「言わないわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイは大人だし、彼が自分で吸う分には止める気もないが、私自身は決して吸いたいとは思わない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "即答したので、グレイはほっとしたようだが、「では何故？」と目線で続きを促してくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T " 「煙草が原因の小火なんてあったから、しばらく塔の中で吸うのも難しいだろうと思って……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Gray " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T " 「だから、私の部屋に置いておけば……。\n
グレイが吸える場所が増えるかなって」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice gra_f0296
Gray " 「[firstname]……、君は……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（かなり悩んだのよね、これに決めるのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイはいつも私の前では吸わないようにしてくれていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが私に対しての優しさだと言うことは知っていたのに、こんなことをしていいのかと思った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の気持ちを踏みにじって、自己満足に押しつけるだけではないかと。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが……。"

hide t_gre_end2
show t_gre_end3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0297
Gray " 「[firstname]。\n
……君の部屋に行っていいのか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0298
Gray " 「煙草が理由でも、理由だけでは足りなくなりそうだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T " 「っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "耳元で、低い声が甘く囁いてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "身体の芯から燃えて、溶けてしまいそうな甘さ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背中を支えるグレイの手がなければ、後ろに倒れ込んでいたかもしれない。\n
それぐらい、私を簡単に籠絡する、声だった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T " 「……断るぐらいだったら、こんな贈り物しないわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ああ、本当に可愛くない答え）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "我ながら、愛想のない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0299
Gray " 「なら、最初から君の部屋に行けばよかったな。\n
そうすれば、すぐ、君の贈り物を使えたのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T " 「グレイ」"

play sound se_0551
hide t_gre_end3
show t_gre_end4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T " 「……んっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背中に回した腕とは違う手が、顎に触れてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "抗うことさえ思いつかないほど自然な動作で、唇を重ねた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T " 「……あ、ん……、う」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_3")
T " 「ふ、う……。\n
く……、ふ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（キスだけで、のぼせそう）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice gra_f0300
Gray " 「両方とも、ありがたく使わせてもらうよ。\n
君の部屋に行く理由が増えるのは、俺も嬉しい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T " 「…………。\n
使って、くれるの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_8")
voice gra_f0301
Gray " 「当たり前だろう。\n
使う理由は山のようにあるが、使わない理由は一つもない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_8")
voice gra_f0302
Gray " 「それに部屋に行くのは煙草のためだけじゃない。\n
君に会いたいから行くんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "間近で微笑む、金の目。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメア達が話したように、この目が、私のいない間どれほど変わっていたかを、知ることはない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（今のグレイは、嬉しそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少なくとも。\n
乾いていた彼に潤いを与えることには繋がっていると、分かったから。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな顔は、きっと知らなくても……、いい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0303
Gray " 「煙草は中毒性が強いが……。\n
今の俺は、もっと中毒性の強いものに溺れている」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（こんな満たされた顔以上に、欲しいものなんて、どこにもないもの）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice gra_f0304
Gray " 「切らしたりなんて……、させないでくれ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦い煙の味。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（中毒になっているとしたら、それは私も同じだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迎えに来てくれたこの人を。\n
少しでも、近くに留めておける理由が欲しかったのは、私も同じ。"

hide t_gre_end4
$ hi_mes()

scene g_01
with stripe_l_medium

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium

scene map_bg_autumn_night
with stripe_l_medium

scene bg_gen25_ym
with stripe_l_medium

scene bg_gen10_bc
with stripe_l_long
play sound se_0168

play music minigame_bj_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「……グ、グレイ。\n
やっぱり、私、どこか変なんじゃないの？」"


show gre_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice gra_f0305
Gray " 「君が？\n
俺にはそうは思えない」"

hide gre_t_03_1
show gre_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice gra_f0306
Gray " 「……よく、似合っている。\n
綺麗だ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "うっとりと満足げに私の頭から足下まで見つめたグレイは、そう言ってくれるが、落ち着かない。"

hide gre_t_01_3

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（この靴、ヒールも高いし）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（それに……、何だか恥ずかしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背中が大きく開いたデザインのドレスは、確かにこういった場面で女性が着る服としてはおかしくない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おかしくはないのだが、それは着ている人間との組み合わせにもよる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（私が来ても無理矢理背伸びしているようにしか見えないと思うんだけどな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイがとても嬉しそうに見ているから、辛うじて着ていられるが……。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0040
Customer " 「おや……、あのお嬢さんは確か……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0007
Customer " 「この前はブラッド様といたはずよね？\n
今回は連れが違うみたいだけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "周囲の視線がちくちくと肌を刺す。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（目立っている、目立っている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイがいつものスーツ姿でいることも理由の一つなのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイフホルダーを差しているとはいえ、この場で彼の姿はあまりにも浮き上がっている。"


show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「？」"

hide gre_t_03_10
show gre_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0307
Gray " 「どうかしたのか、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「いえ。\n
ただ、ここはあなたにとっていい思い出がないと思ったのに、よく来る気になったなって思って」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（絶対に断ると思ったんだけどな）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（それも、招待した人が人だし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "招待状が届けられたとき、最初は断ろうとしていた私の手を引いたのは、グレイだった。"

hide gre_t_02_4
$ hi_mes()

scene bg_gen10_bc_s
with dis

scene n_01_s
with dis

scene n_01
with dis

play music nightmare_t_ali

show nai_s_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0489
Nightmare " 「帽子屋からの招待状？\n
それも……、また例のカジノへか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T " 「ええ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T " 「どうしようかと思って」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔には大量の書類や通知が届く。\n
たまたま今回それを分ける仕事をしていたのは私だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから一番に気付けたのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いかにも高級そうな手紙の差出人は、勿論、件のカジノのオーナーである男から。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（嫌がらせ以外の何ものでもないわよね）"

hide nai_s_02_11
show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice nig_f0490
Nightmare " 「どうするも何もな。\n
君への招待だろう、行きたくないのなら断ればいい」"

play sound se_0472

show t_gre_end5 onlayer master
with dis
hide nai_s_01_11
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「それが私だけじゃないのよ。\n
ほら」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice nig_f0491
Nightmare " 「二通ということは……、君と、私か！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "{size=+20} 「そんなわけがないでしょう」{/size}"

hide t_gre_end5
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（変なタイミングでぼけを披露しないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "カジノでの一連の出来事は報告がてらに軽くだが、話してある。\n
なのにどうしてそういう発想が出てくるのか……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T " 「あなたにはカジノなんて似合わないわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "（勝負事に弱いくせに見栄をはろうとするんだから……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぼろぼろに負けて一文無しという事態も有り得る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして本人だけならまだいいが、私達も迷惑をこうむることになるに決まっている。"


show nai_s_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0492
Nightmare " 「そんなことないぞ、私だってそこそこくらいは……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T " 「心を読んでいるくせに、トランプゲームですら勝てないじゃないの、どうやって？」"

hide nai_s_02_5
show nai_s_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice nig_f0493
Nightmare " 「トランプゲームとカジノは違うぞ。\n
聞いて驚け、実は私は、賭けごとが大得意で……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T " 「ないわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きっぱりと言いきった私に、ナイトメアは心外だと眼差しで訴えたが、信憑性はない。"

hide nai_s_03_11
show nai_s_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0494
Nightmare " 「一刀両断だなんて。\n
……ちょっとしたお茶目なのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T " 「冗談は、状況を見てから言ってちょうだい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「これは、私と、グレイ宛よ。\n
また遊びにおいで、ですって」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少なくとも私宛の招待状にはそうある。\n
グレイに当てた文書もほとんど同じような内容だろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だけではなくグレイの分と合わせて二通送ってきたブラッドの真意は分からない。"

hide nai_s_03_9
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0495
Nightmare " 「ふむ……、そうか。\n
それで、君としてはどうしたいんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（分かっているくせに聞かないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "静かな表情で私の顔を見つめてくるナイトメアには、私の気持ちなど既に見越されているはずだ。"

hide nai_s_02_1
show nai_s_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0496
Nightmare " 「おや、断るのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T " 「だって……、グレイにこれ以上迷惑をかけるわけにはいかないでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これが他の人間からの案内ならまだいい。\n
だが、相手がブラッドとなれば、話はまったく違う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（絶対トラブルになるに決まっているもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "退屈凌ぎと称して何を言い出してくるか分からない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（この前だって、余興とか何とか言いながら、グレイを焚きつけたし）"

hide nai_s_01_2
show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice nig_f0497
Nightmare " 「君がどうしても行きたくないというのなら、断るのも悪い手ではないな。\n
だったら、当のグレイに見つかる前にそれを処分したほうがいいだろう」"

hide nai_s_01_11
show nai_s_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice nig_f0498
Nightmare " 「しかし残念だが、それは手遅れのようだぞ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「え？」"


play music gray_t_ali
show gre_t_02_10 at center
with dis
hide nai_s_02_12

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gra_f0308
Gray " 「そうですね、相手があの男では断ったことを理由に、かえって因縁を付けて来かねない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T " 「グ、グレイ！\n
ど、どうしてっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（この時間帯は休憩のはずじゃ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "音もなく部屋の中に現れたグレイは、私の手にある封筒を見ながら困ったように笑った。"

hide gre_t_02_10
show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0309
Gray " 「君の部屋に行ったら姿が見えなかったからな、探しているうちにここに来たんだが」"

hide gre_t_01_4
show gre_t_01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0310
Gray " 「……それが、帽子屋からの招待状か」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「あ」"

play sound se_0469
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "止める暇も与えずに、彼は素早く私の手から未開封の封筒を抜き取った。"

hide gre_t_01_15
show gre_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
Gray " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（何が書いてあるんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "紙面を追うグレイは一言も発しない。\n
表情も、身に纏う空気にも変化はないが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（この人の場合、うまく隠しちゃうから安心出来ないのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイはナイトメアにも心を読ませない限られた人だ。\n
心が読めない私の目ぐらい簡単に誤魔化してしまうだろう。"

hide gre_t_02_9
show gre_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「…………」"

hide gre_t_02_12
show gre_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「あ、は、はい？」"

hide gre_t_03_9
show gre_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice gra_f0311
Gray " 「君の次の休みは、確か五時間帯後だったな？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T " 「ええ、そうよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "多忙なはずのグレイの頭の中には、どうやら私のスケジュールまで収められているらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "複雑な仕事をいくつも抱えているというのに、どこにそんなことまで入れる余裕があるというのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（元々優秀な人だから、当然なのかもしれないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つくづく私なんかとは出来が違う。"

hide gre_t_02_3
show gre_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0312
Gray " 「休みを潰すようで悪いが、もう何か予定は入っているか？\n
君の都合がよければ、さっさとすませてしまおう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T " 「すませてしまおうって……、行くの、あのカジノに！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（グレイは行きたがらないと思っていたのに）"

hide gre_t_02_10
show gre_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice gra_f0313
Gray " 「帽子屋が招待すると言っているんだ、簡単に断らせてくれるとは思えないからな」"

hide gre_t_01_5
show gre_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice gra_f0314
Gray " 「それに……、今度は最初から俺が一緒に行けるだろう、[firstname]？\n
君に変な虫を寄せ付けずにすむ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「グレイ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（グレイと一緒にカジノに行くなんて……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "知らず知らずのうちに顔が赤くなってしまうあたり、私は不謹慎に違いない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの場所を歩いていたとき、来るのならグレイと一緒に来たかったという思いは、塔に戻ってからも変わらなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「でも、グレイこそいいの？\n
せっかくの休憩なのに」"

hide gre_t_01_1
show gre_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice gra_f0315
Gray " 「君と一緒にいられるんだ。\n
これ以上ないだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_8")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あっさりと出てきた言葉に、私の顔は更に真っ赤に染まってしまう。"

hide gre_t_01_3
show gre_t_01_3 at left
show nai_s_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0499
Nightmare " 「……おい、グレイ。\n
一応念を押しておくが、騒ぎは起こすなよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然聞こえてきたナイトメアの声は、どこか溜息混じりだった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤くなった私を揶揄しているのかと思えば、夢魔の眼差しは私ではなく、隣にいるグレイに向かっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T " 「騒ぎって……。\n
この前の騒動は、グレイのせいじゃなくて、ブラッドのせいじゃない」"

hide gre_t_01_3
show gre_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice gra_f0316
Gray " 「そうですよ、失礼なことを言わないでください」"

hide gre_t_02_8
show gre_t_02_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice gra_f0317
Gray " 「騒ぎなんて俺は起こしませんよ。\n
……俺は、ね」"

hide nai_s_03_4
show nai_s_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0500
Nightmare " 「行くなら行くで、もう少しまともな変装をしていけばいいものを、あんな悪目立ちする格好で行ったおまえにも原因はあると思うんだがな」"

hide nai_s_02_10
show nai_s_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0501
Nightmare " 「それに、おまえ、少し嫉妬深すぎやしないか？\n
彼女に知られたら……」"

hide nai_s_01_4
show nai_s_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
Nightmare " 「！！」"

hide gre_t_02_13
show gre_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice gra_f0318
Gray " 「言わなければ分かりませんよ、ナイトメア様？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこりと。\n
穏やかな表情を浮かべているグレイと違い、ナイトメアは逆に青ざめていくばかりだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T " 「？\n
どういうこと、ナイトメア？」"

hide nai_s_03_7
show nai_s_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
Nightmare " 「…………」"

hide nai_s_03_9
show nai_s_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice nig_f0502
Nightmare " 「何でもない。\n
君は本当に厄介な男にばかり気に入られると思っただけだ」"

hide gre_t_03_4
show gre_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice gra_f0319
Gray " 「それはそうと、俺達がいない間、ちゃんと仕事をしていてください。\n
ただでさえ彼女が帰ってきてから、ペースが元に戻ってきているんです」"

hide gre_t_01_10
show gre_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice gra_f0320
Gray " 「ナイトメア様がばりばりと働いていてくれないと、安心して休憩に入れません」"

play sound se_0719
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこで一度言葉を切って、彼は手にした書類を手で打った。"

hide gre_t_01_1
show gre_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0321
Gray " 「ああ、そうでした。\n
くれぐれも、また時計屋の部屋に逃げ込んで一服……、なんてことがないようにしてくださいね？」"

hide gre_t_03_9
show gre_t_03_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0322
Gray " 「いくら俺でも、彼女を抱えて帽子屋領からここまで飛んで戻るなんてごめんですから」"

hide nai_s_02_10
show nai_s_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0503
Nightmare " 「分かった、分かったって！！」"

hide gre_t_03_8

hide nai_s_01_10

$ hi_mes()

scene n_01_s
with dis

scene bg_gen10_bc_s
with dis

scene bg_gen10_bc
with dis
play sound se_0168

play music minigame_bj_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、いつの間にか私のドレスを準備していたグレイに連れられて、三度目のカジノへ来たのだ。"


show gre_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0323
Gray " 「そうだな。\n
面白い思い出ばかりではないのは事実だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（無理矢理付き合わせちゃった？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「嫌だったら、帰りましょうか？\n
顔だけ出せば、一応招待には応じたことになるし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ私達を招待したのはブラッドだ。\n
彼の暇潰しに付き合わせられれば、またトラブルを招きかねない。"

hide gre_t_03_9
show gre_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0324
Gray " 「君が帰りたいというのなら、俺は構わないが……」"

hide gre_t_03_6
show gre_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0325
Gray " 「せっかく、こんな可愛い恋人を連れ歩けているんだ。\n
見せ付けてやりたい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "差し出された腕の意味が分からないほど、私も子供ではない。"

hide gre_t_02_2
show gre_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T " 「っ」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おずおずと腕を絡めると、グレイは口元を緩めた。\n
その顔につられたように私も笑う。"

hide gre_t_01_3
show gre_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0326
Gray " 「……おかしいな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T " 「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T " 「何か、やっぱり変？」"

hide gre_t_02_11
show gre_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice gra_f0327
Gray " 「君じゃない。\n
見せびらかしたいと言ったばかりなのにな」"

hide gre_t_02_10
show gre_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice gra_f0328
Gray " 「君に他の奴の視線が絡みつくのは、何だか面白くない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞き慣れているはずの低音に、身体に痺れが走るようだった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T " 「！？」"

hide gre_t_03_8
show gre_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice gra_f0329
Gray " 「隠して俺だけのものにしてしまいたい気持ちと、俺のものだと触れ回りたい気持ち。\n
どっちのほうが、強いんだろうな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（そんなの、私に聞かれたって分からない……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぞくぞくと背筋を震わせる声に、顔が赤くなる。\n
ヒールのせいか、いつもよりも少しだけ近い顔を見上げて、早口に言い切った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T " 「そんなの、私だって同じよ」"

hide gre_t_01_11
show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Gray " 「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_1")
T "（こんな格好いい人が恋人だって見せびらかしたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "周囲の嘲笑だって気にならないくらいに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（でも、こんな顔を他の人に見せるのは嫌よ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「……グレイがエスコートしてくれるのは、私だけでしょう？\n
だったら、今夜はあなたを独り占めさせてちょうだい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ヒールで増えた分だけ。\n
この夜は視点だけでなく、言葉も少し背伸びしてみてもいいだろう。"

hide gre_t_01_4

$ hi_mes()

$ time_effect()
play sound se_0168
pause .5
play sound se_0358

show dealer_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hos_f0077
Dealer " 「おや、これはお嬢さん。\n
いらっしゃいませ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「……こんばんは」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "前回ルーレットを操作していた、お馴染みのディーラーが声をかけてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "通りがかった私の顔を見つけて社交辞令で挨拶をしてきたのかと思ったが、どうやら違うらしい。"

hide dealer_7
show dealer_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0078
Dealer " 「ボスもお待ちしていましたよ。\n
あちらのテーブルにいらっしゃいます」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうぞと誘うように彼は奧のテーブルへと促してくる。"

hide dealer_3
show dealer_3 at left
show gre_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「…………」"

hide gre_t_02_9
show gre_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0330
Gray " 「どうする？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T " 「どうするって……、それは」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（変な言い掛かりをかけられるぐらいなら、さっさと帰りたいけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかしそれですんなりと帰してくれるような人ではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よくも悪くも、付き合いのある人だ。\n
彼の考えなど読めないが、それぐらいは私も彼のことを知っていた。"


play music map_hatter1_ali
hide dealer_3

hide gre_t_02_10


show eri_s_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0308
Elliot " 「よう、[firstname]！\n
よく来たな、待ってたぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「エリオット？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "黒いスーツ姿のエリオットが手を振りながら、私達のほうへとやって来る。"

hide eri_s_01_1
show eri_s_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0309
Elliot " 「おお、ちゃんとめかし込んできたな。\n
可愛いぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「可愛いって……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ストレートな褒め文句に照れてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これがブラッド辺りの言葉なら裏があるのかと勘ぐってしまうが、エリオットは裏表のないウサギだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "くすぐったいが素直に賞賛を受け取ることが出来る。"

hide eri_s_01_4
show eri_s_01_4 at left
show dee_s_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0499
Dee " 「あー、お姉さんだ！いらっしゃい！\n
会いたかったよ、お姉さんっ」"

hide dee_s_02_4
show dee_s_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0500
Dee " 「酷いよね、この前は僕達に何も言わないで帰っちゃうんだもん」"

hide eri_s_01_4

hide dee_s_01_5
show dee_s_01_5 at left
show dam_s_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0501
Dam " 「そうだよ。\n
一緒に遊ぼうと思って、僕達、色々と準備していたのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「ディー、ダム？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（二人までどうして？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットがいるのならまだ分かる。\n
彼はブラッドの懐刀だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "主がいる場所についてくるのは、納得がいく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、双子は別だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（変に呼び出せば、時間外労働に対する休暇とボーナスを請求されかねない……。\n
この前、ブラッドもそう言っていたのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼らまで、どうしてここにいるのだろう。"

hide dee_s_01_5

hide dam_s_01_3


show gre_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「…………」"

hide gre_t_01_12
show gre_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0331
Gray " 「おい、三月ウサギ。\n
帽子屋はどこにいる」"

hide gre_t_01_5
show gre_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0332
Gray " 「招待しておきながら顔も見せないなら、帰らせてもらうぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T " 「グレイ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子と顔を合わせていた私を後ろからグレイが引き寄せる。\n
肩に置かれた手には、少し力が入っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（どうしたのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（先刻までは、いつもどおりだったのに）"



hide gre_t_02_13
show gre_t_01_9 at left
show eri_s_01_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice eri_f0310
Elliot " 「そこのディーラーも言っていただろう、ブラッドなら、奧だ。\n
ビリヤードのあるテーブルにいるぜ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイの態度の悪さを気にした様子もなく、エリオットは奥のテーブルを指差した。"

hide eri_s_01_12
show eri_s_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0311
Elliot " 「俺らは、あんた達の案内役ってわけ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T " 「案内？」"


show dee_s_01_2 at center
hide gre_t_01_9
hide eri_s_01_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice dad_f0502
Dee " 「ちょっと特別な場所だから、お姉さんだけならともかくトカゲさんがいるとなると、簡単に通せないんだって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「特別な場所、ね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（……つまり、ＶＩＰルームってことかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドは領主という立場以外に、ファミリーのボスという立場もある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼の所有するカジノだったら、ＶＩＰルームの一つや二つぐらいあってもおかしくない。"


show eri_s_02_12 at center
hide dee_s_01_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0312
Elliot " 「そういうことだ。\n
変な客は入れさせねえから、安心して遊んでいけよ」"

hide eri_s_02_12
show eri_s_02_12 at left
show gre_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0333
Gray " 「ずいぶんと歓迎されたものだな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイの嫌味も、彼らには通じない。\n
双子は跳ねるように近付いてきて、私の手を取った。"

hide eri_s_02_12
hide gre_t_01_11
show gre_t_01_11 at left
show dee_s_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0504
Dee " 「うん、だってお姉さんは僕達にとっても特別なお客さんだからね」"

hide gre_t_01_11

hide dee_s_01_6
show dee_s_01_6 at left
show dam_s_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0505
Dam " 「一緒に遊ぼうよ、お姉さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「あ、ちょ、ちょっと……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ディーに手を引かれそうになったところに、別の手が入ってくる。"

hide dee_s_01_6
show dee_s_01_6 at left_center
hide dam_s_01_2
show dam_s_01_2 at center
show gre_t_03_7 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0334
Gray " 「彼女は俺の連れだ。\n
エスコートは間に合っている」"

hide gre_t_03_7
show gre_t_01_4 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0335
Gray " 「行こう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「あ……。\n
うん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが抱え込むように私の肩を抱く。\n
剥き出しになった肩に彼の手が触れるだけで、どきどきしてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（……恥ずかしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "行動そのものよりも、赤くなっているだろう自分の顔を見られることが、恥ずかしくて堪らない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（でも、クセになりそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "甘ったるい感覚に中毒になりそうだ。"

hide gre_t_01_4


show eri_s_03a_7 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0313
Elliot " 「ほら行くぞ、おまえら。\n
ブラッドがお待ちかねだぜ、あまり余計な茶々を入れんなよ」"

hide dee_s_01_6

hide dam_s_01_2

hide eri_s_03a_7
with dis
$ hi_mes()

scene bg_gen10_bc
with stripe_l_medium

scene bg_gen10_bcb
with stripe_l_long
play sound se_0324

play music kaigou2_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T " 「あ……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（また失敗しちゃった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の突いたボールは狙ったコースを大幅に裏切って転がってしまう。"


show eri_s_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0314
Elliot " 「じゃ、今度はこっちの番だな。\n
ガキども、しっかりやれよ」"

hide eri_s_02_12
show eri_s_02_12 at left
show dee_s_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0508
Dee " 「僕達を誰だと思っているんだよ。\n
失敗なんてしないよね、兄弟」"

hide eri_s_02_12
show eri_s_02_12 at left_center
hide dee_s_03_1
show dee_s_03_1 at center
show dam_s_01_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0510
Dam " 「そうだよ。\n
それよりも、勝ったら臨時ボーナス、忘れないでよ」"

hide eri_s_02_12

hide dee_s_03_1
show dee_s_03_1 at left_center
hide dam_s_01_8
show dam_s_01_8 at center
show bra_s_01_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0478
Blood " 「分かっているさ。\n
さっさと始めろ」"

hide bra_s_01_5
show bra_s_01_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0479
Blood " 「あまり焦らすと、お嬢さんの連れが痺れを切らしそうだ」"

hide dee_s_03_1
hide dam_s_01_8
hide bra_s_01_3
show gre_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T " 「グレイ、ごめんなさい。\n
また失敗しちゃって」"

hide gre_t_01_13
show gre_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice gra_f0336
Gray " 「あ、いや、そんなことはない。\n
最初の一つを落としたのは、間違いなく君の腕だよ」"

hide gre_t_02_4
show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice gra_f0337
Gray " 「君は初めてなんだから、大したものだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T " 「でも……、その後は、ずっと失敗続きじゃない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ハンデはもらっているけど……、それにしてもお荷物だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすが、ＶＩＰルーム。\n
それもどうやら人払いがされているらしく、テーブルの周りに余計なギャラリーはいない。"

hide gre_t_01_4
show gre_t_01_4 at left
show bra_s_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0480
Blood " 「ふむ……。\n
二組ではなく、三組に分ければよかったか」"

hide bra_s_02_12
show bra_s_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0481
Blood " 「さすがに四人では、私の番が来るまでが長いな。\n
だるい……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの杖ではなく、キューを手にしたブラッドは退屈そうに欠伸なんかしている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（自分が決めたくせに偉そうに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ＶＩＰルームで待っていたブラッドが提案してきたのは、ビリヤード。"

hide bra_s_03_13
show bra_s_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0482
Blood " 「この前と同じものでもいいが、毎回同じでは飽きるだろう？\n
お互いに」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（どの口が言うか、どの口が）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドはにやにやと私たちを見ながら言ってきた。\n
彼を殴るのを我慢しただけで、感謝してほしいくらいだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_3")
T "（……実際には足を踏んでやったんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この前のような無茶な提案をされるよりはいいということで、グレイも了承した。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひとけの少ないＶＩＰルームでそのままビリヤードを始めたのだが、ブラッドもグレイもお互いを無視するように淡々とゲームを続けている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たまに視線が合ってぴりっとした緊張感が生まれるが、それ以外に口論になることもなく平和なものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（何だか、ユリウスとのやりとりに近いものがあるけど、それとはまた違うのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それに、招待した割には、ブラッドが大人しいことも気になった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とはいえ、そんなことを気にしているのは私だけらしく、双子はテーブルの傍であれこれと相談をしながらキューを握っている。"

hide bra_s_01_10

hide gre_t_01_4


show dee_s_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0511
Dee " 「ええと、今は６番が狙い目だね。\n
この位置からだと……、こんな感じかな」"

play sound se_0324
play sound se_0323
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ディーが突いた白球は、私が狙っていた球をポケットへ落としていた。\n
その様子に、ダムが自分のことのように喜んでいる。"



hide dee_s_02_11
show dee_s_02_11 at left
show dam_s_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0512
Dam " 「さすが兄弟、うまくいったよ。一つ落とす度に、ボーナスが近付くなんて素晴らしいよね。\n
ビリヤードって最高」"

hide dee_s_02_11
show dee_s_02_11 at left_center
hide dam_s_01_6
show dam_s_01_6 at center
show eri_s_01_10 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0315
Elliot " 「……おまえら、もう少しまともにゲームしろよな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（そういうあなたもね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビリヤード中は、咥え煙草はしないし、食べ物を置かないらしいのだが。\n
エリオットの大きな手にはにんじんスティックがしっかりと握られている。"

hide dee_s_02_11

hide dam_s_01_6
show dam_s_02_10 at center
hide eri_s_01_10
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0514
Dam " 「じゃあ、次は僕だよね。\n
ふふふ、ボーナス、ボーナス……」"

play sound se_0324
play sound se_0323
pause .5
hide dam_s_02_10
show dam_s_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0515
Dam " 「あれ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T " 「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ダムの打ったボールは途中で軌道を変えて、自分からテーブルの端にあるポケットに落ちて行ってしまった。"

hide dam_s_01_4
show dam_s_01_4 at left
show eri_s_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0316
Elliot " 「何やってるんだよ、ガキ。\n
これを落とせばまたブラッドの番だったのに」"

hide dam_s_01_4
show dam_s_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0516
Dam " 「おかしいな……。\n
変な回転なんか付けていなかったんだけど」"

hide dam_s_01_5
show dam_s_01_5 at left_center
hide eri_s_02_9
show eri_s_02_9 at center
with dis

show bra_s_02_16 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood " 「…………」"

hide bra_s_02_16
show bra_s_03_14 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0483
Blood " 「ふ、まあいいだろう。\n
これで手玉はフリーだ、向こうの出方を見るのも悪くない」"

hide dam_s_01_5

hide eri_s_02_9

hide bra_s_03_14


show gre_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0338
Gray " 「攻守交代だな。\n
[firstname]、こっちへ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T " 「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T " 「グレイ？\n
どうしたの、次はあなたの番でしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッド達は四人ということもあって、ミスをするか、ボールを一つ落とすごとに交替しているが、私達は交互にプレイするようにしていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどミスショットをしたのは私だから、そうすると今度はグレイの出番ということになるのだが。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はテーブルの上に手玉を置くと、私に向かって手招きしてくる。"

show t_gre_end6 onlayer master
with dis
hide gre_t_02_10

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0339
Gray " 「教えてあげよう。\n
おいで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「え……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T " 「！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T " 「グ、グレイ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（位置が、位置が近い）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice gra_f0340
Gray " 「指先に力が入りすぎているんだ。\n
もう少し腰を落として……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice gra_f0341
Gray " 「ああ、足ももう少し開いたほうが安定がいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T " 「っ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（そ、そういう声で、耳元で囁かないでっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悲鳴のような、甘い声のようなものが出そうになる度に、唇を噛んで耐える。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dee " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0517
Dam " 「ボス、いいの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0484
Blood " 「…………。\n
欲求不満なんだろう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（だ、誰が欲求不満よ、誰が！！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "四人の視線が痛々しい中、グレイの指は少しずつ私の身体をテーブルに沿わせていく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0342
Gray " 「……よく見て」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gra_f0343
Gray " 「７番のボールの横に、９があるだろう？\n
今なら、一緒に落とせる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T " 「そ、それは分かるけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（素人にそんな高度な技術を要求しないでほしい）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_13")
T " 「グ、グレイが狙ったほうが確実なんじゃ？\n
ね？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_13")
voice gra_f0344
Gray " 「いや、君が勝つほうがいい」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_13")
voice gra_f0345
Gray " 「……示しも付くしな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T " 「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（示し？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が仮にこのゲームに勝ったとして、誰に対して、どんな示しが付くというのだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T " 「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "低い声が私の名を呼んだとき、手に思わず力がこもっていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「あ」"

play sound se_0324
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「え？」"

play sound se_0324
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T " 「！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T " 「うそ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "狙いなど絞れていなかったはずの手玉は、吸い込まれるように７番にあたり、そして決め手となる９のボールを動かしていた。"

play sound se_0323
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、固いものが落ちる音。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T " 「…………」"

hide t_gre_end6

show eri_s_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice eri_f0317
Elliot " 「え……、まじかよ！？\n
[firstname]、すげえじゃねえかっ！」"

hide eri_s_01_5
show eri_s_01_5 at left
show dee_s_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice dad_f0518
Dee " 「えーーーっ、お姉さん、勝っちゃったの！？\n
トカゲさんの～～～～～～なレクチャー、そんなによかったの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T " 「そんなによかったのって、あんた……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "なんだか、別の意味があるように言わないでほしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（まあ、見方と聞き方によっては、そう捉えられても仕方ないけど）"

hide eri_s_01_5
show eri_s_01_5 at left_center
hide dee_s_02_6
show dee_s_02_6 at center
show dam_s_01_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice dad_f0519
Dam " 「でも、何だかボールが変な動きをしていたような」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不思議そうに首を傾げているのは、ダムだ。\n
その近くにいたブラッドもまた沈黙している。"

hide eri_s_01_5

hide dee_s_02_6

hide dam_s_01_5


show bra_s_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
Blood " 「…………」"

hide bra_s_02_12
show bra_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice blo_f0485
Blood " 「何はともあれ、ゲーム終了か。\n
つまらんな、もう少し遊びたかったんだが」"

hide bra_s_02_3
show bra_s_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice blo_f0486
Blood " 「……おや、何か動いたな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「え？\n
何かって……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの視線を追いかけると、何かの影が私にも見えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（え？\n
あれって……）"



hide bra_s_03_6
show bra_s_03_6 at left
show gre_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
Gray " 「！」"

play sound se_0347
$ flash(.3)
$ flash(.2)
$ flash(.1)
pause 1
hide gre_t_02_6
show gre_t_02_4 at left
hide bra_s_03_6
show eri_s_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice eri_f0318
Elliot " 「うわっ。\n
危ねえな、ブラッド」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドがいきなりマシンガンを撃つ。\n
彼が発砲した方向にいたエリオットが慌てて避けながら銃を引き抜くが、手が止まった。"

hide eri_s_02_5
show eri_s_03a_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0319
Elliot " 「ん？\n
あれ、おまえ、何を撃ったんだ、ブラッド？」"

hide eri_s_03a_2
show eri_s_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0320
Elliot " 「誰もいねえじゃねえか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう、エリオットの言うように、この部屋には私達以外の人間などいない。\n
彼が撃った場所も、ただの壁にしか見えなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（……まさか、どこかの組織が襲撃してきたとか？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だがそうだとしたら、エリオットや双子が気付かないはずがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（それに、ちらりとしか見えなかったけど……。\n
あれは多分）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず隣のグレイを見上げれば、彼は彼で苦々しい表情を浮かべていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の首筋は身長差が禍いして、私からは確認出来ない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T " 「グレイ？」"

hide gre_t_02_4

hide eri_s_01_5
show eri_s_01_5 at left
show bra_s_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice blo_f0487
Blood " 「ふふ。\n
驚かせてしまってすまないな、お嬢さん」"

hide bra_s_01_2
show bra_s_02_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice blo_f0488
Blood " 「私ともあろう者が、どうやら取り逃がしたらしい」"

hide eri_s_01_5

hide bra_s_02_15


show dee_s_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice dad_f0520
Dee " 「あれ、何か落ちているよ。\n
ボスが撃ったのって、これ？」"

hide dee_s_01_5
show dee_s_01_5 at left
show dam_s_01_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice dad_f0521
Dam " 「何だろう、これ。\n
黒くて小さいけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T " 「……欠片？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの銃撃によって、粉々に壊されてしまったのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず撃たれた跡を確認するが、銃弾の痕以外には何もないようで安心する。"

hide dee_s_01_5

hide dam_s_01_12


show gre_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「…………」"

hide gre_t_02_13
show gre_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0346
Gray " 「ゲームは終わったんだろう。\n
帰らせてもらうぞ、帽子屋」"



hide gre_t_03_7
show gre_t_03_7 at left
show bra_s_03_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0489
Blood " 「おや、一ゲームのみとはつれないじゃないか、トカゲ」"

hide bra_s_03_5
show bra_s_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0490
Blood " 「もう帰るのか？\n
今から、逃げ出した小さな生き物について、ゆっくりと話し合いたいと思っていたのだが……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（……小さな生き物ってやっぱり）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（アレよね……）"

hide gre_t_03_7
show gre_t_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice gra_f0347
Gray " 「あいにく、俺が仕事から自由になれるのはこの時間帯だけでな。\n
おまえの好奇心に付き合う義理はない」"

hide bra_s_02_2
show bra_s_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice blo_f0491
Blood " 「それは残念だ。\n
ああ、お嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T " 「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイにつれられるように部屋を出ようとしていた私を、ブラッドが引き留めた。"

hide bra_s_03_2
show bra_s_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0492
Blood " 「今度、珍しい生き物を捕まえたら、見せてあげよう」"

hide bra_s_02_8
show bra_s_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0492_5
Blood " 「可愛いものが好きな、業突く張りな生き物だが、珍しいことには変わりはないからね」"

hide gre_t_01_13
show gre_t_02_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「…………」"

hide gre_t_02_13
show gre_t_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0348
Gray " 「……戻ろう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T " 「あ、うん」"

hide gre_t_01_2

hide bra_s_01_1

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何かを言いかけたグレイだが、結局は口にせず出口に向かう。"


show dee_s_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice dad_f0523
Dee " 「また来てね、お姉さん。\n
今度は、他にもお姉さんが出来る遊びがないか探しておくね」"

hide dee_s_01_6
show dee_s_01_6 at left
show dam_s_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice dad_f0524
Dam " 「ダーツなんかいいかもしれないね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子がわいわいと騒ぐ声を聞きながら、私達はカジノを後にした。"

hide dee_s_01_6

hide dam_s_01_2

$ hi_mes()

scene bg_gen10_bcb
with dis

scene bg_gen25_ym
with dis
$ renpy.sound.play("audio/voice/se_0776 .wav", .65, loop=True)

play music moon_night2_a_ali

show gre_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0349
Gray " 「ふう、やはり外のほうが落ち着くな。\n
ああいう場も嫌いじゃないが、どうにも息苦しい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T " 「ええ、そうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首筋を確認すると、何ごともなかったようにトカゲはそこに戻っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（……そんなに勝負に勝ちたかったのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ディーとダムはそれぞれボーナスと休暇を報酬として賭けていたようだが、私達は何を賭けていたわけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "無理をしてまで勝つ必要はなかったはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T " 「…………」"

hide gre_t_01_14
show gre_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Gray " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しんと。\n
静まり返った街の中を歩く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "響いてくるのは私達自身の足音だけだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「……ねえ、グレイ」"
stop sound fadeout .6
hide gre_t_02_9
show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Gray " 「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T " 「どうして、カジノに行くって決めたの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（あのときは、気にならなかったけど、やっぱりおかしいわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔に属し、中立の立場であるグレイだ。\n
ハートの城や遊園地と違い、面と向かってブラッドと対立する立場にはない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、個人としての感情は別だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（日頃から絡んでくるエースとは違うけど、そんなに仲がいいわけじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むしろ、グレイはブラッドを警戒しているだろう。"

hide gre_t_03_10
show gre_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0350
Gray " 「……招待された以上は参加するのがルールだからな。\n
断るだけの自由は俺にはない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T " 「じゃあ、行ったのはルールのためだけ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界にいくつもある、制約。\n
逆らえないこともないが、もしそうすればたとえ役持ちであろうと、ペナルティを受けなければならない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの誘いを受ける理由には充分なのだが、他にも何か違う理由があるような気がした。"

hide gre_t_01_14
show gre_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0351
Gray " 「……挑まれた以上は、負かしてやるだけだ。\n
帽子屋だろうが、誰だろうがそれは変わらない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T " 「挑まれた？」"

hide gre_t_01_1
show gre_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice gra_f0352
Gray " 「ああ。\n
帽子屋が君へ送った文書には、何と書いてあった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T " 「……普通の文章よ。\n
また遊びにおいでって……、それだけだったわ」"

play sound se_0472
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "バッグの中に入れておいた招待状を取り出す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他はカジノの場所が書かれた案内図だけ。\n
手書きでわざわざ書き添えてあったのは、その一文。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T " 「グレイの招待状には何か書いてあったの？」"

hide gre_t_03_9
show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Gray " 「…………」"

hide gre_t_03_10
show gre_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice gra_f0353
Gray " 「……諦めさせてみろ、だそうだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T " 「は？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（諦めさせろ？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_14")
T "（ブラッドに？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「……あの人って、そう簡単に諦めるような人じゃないと思うんだけど、何を諦めさせろって言うわけ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "意図的に伏せられているとしか思えない目的に疑問が生まれた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それもあのブラッドに諦めさせるとなれば、骨が折れるのはいうまでもない。"


show t_gre_end7 onlayer master
with dis
hide gre_t_02_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0354
Gray " 「さあ……、君は何だと思う？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T " 「！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T " 「グレイ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちり、と口付けられたところが熱い。\n
背中なので見えないが、きっと痕になっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「誰かに見られたりしたらどうするの！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice gra_f0355
Gray " 「誰にも見せないよ。\n
時間帯も、お誂え向きに夜だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T " 「だ、だからって……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gra_f0356
Gray " 「心配なら、こうしておこう」"

play sound se_0551
hide t_gre_end7
show t_gre_end8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結い上げていた髪が解かれ、跡を隠すように背中に広がっていく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0357
Gray " 「これで、誰にも見えないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T " 「そ、そういう問題じゃ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice gra_f0358
Gray " 「狙われている自覚が足りないな、君は。\n
だから、俺みたいな男につけ込まれるんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T " 「んっ」"

hide t_gre_end8
show t_gre_end9 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "唇に触れた熱に、目の前が真っ赤に染まった気がした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（独占したいだけ？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_17")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_13")
T " 「グレイがキスするのは、ブラッドを遠ざけるためだけ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_13")
Gray " 「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（言うんじゃなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最初から一緒にいて、虫を遠ざけると言っていたグレイの言葉が頭の中を掠めてしまっていたせいかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ブラッドに取られるのが嫌だから、好きになってくれたの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "好きな人に対して疑惑を持つ以上に、こんなことを思うなんて最低だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0359
Gray " 「……あの男を諦めさせるためだけじゃない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0360
Gray " 「言っただろう、溺れているんだ。\n
他でもない君に」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T " 「グレイ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（そんなことを言ったら、溺れているのは私のほうなのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイといるだけでよかったはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "独占したいと言われて喜んで。\n
浅ましい自分に嫌気が差すのに、止められない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0361
Gray " 「夢中になっている。\n
頭の芯から指先まで、君のすべてを俺だけのものにしたくて、焦れているんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0362
Gray " 「子供騙しのイカサマだろうが、汚い手段だろうが。\n
どんなことをしても、誰にもやらない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_7")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この人が私に夢中になっているなんて、都合のいい話だと思うのに。\n
そう囁かれるだけで、胸の中が熱かった。"

hide t_gre_end9
$ hi_mes()

scene bg_gen25_ym
with stripe_l_medium

scene map_bg_autumn_night
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium

scene bg_gen_sky_all_day
with stripe_l_long

play music nightmare_t_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0504
Nightmare " 「うーあー、もう嫌だ。\n
もうやだ、何でこんなに書類が溜まっているんだ！！！」"


scene white with expand_short
play sound se_0527

scene n_01 with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの投げ出した書類が、ひらひらと床に散らばっていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T " 「子供っぽいことしないでよ。\n
それに手のつけようがないぐらいに溜め込んだ犯人はあなたでしょう、ナイトメア」"

play sound se_0528
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "音を立てて散開していく書類を拾っていると、グレイが息をついた。"


show gre_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0363
Gray " 「そうですよ。\n
俺達が出掛けている間に片付けておいてくださいとあれほど言っておいたのに」"

hide gre_t_01_5
show gre_t_01_5 at left
show nai_s_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0505
Nightmare " 「うるさいっ、自分だけいい思いをしてきておいて……。\n
私だって、たまにはいい思いをする権利がある！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（いい思いって……、別にカジノで儲けたわけじゃないのに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（こういうところが子供っぽいのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうしたものかと、二人顔を見合わせる。"

hide gre_t_01_5
show gre_t_03_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0364
Gray " 「いい思いと言われましても……。\n
せいぜい点滴か、薬をあげるぐらいしか今は持ち合わせがありませんよ」"

hide nai_s_01_8
show nai_s_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0506
Nightmare "{size=+20} 「それのどこがいい思いだ！？」{/size}"

hide nai_s_02_5
show nai_s_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0507
Nightmare " 「拷問の間違いだろう、まったく……。\n
もうやだ、疲れた」"

hide nai_s_03_9
show nai_s_03_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0508
Nightmare " 「休憩にしろ、休憩に。\n
休憩を入れるまでは、絶対に動かんぞ～」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボイコットというように書類の上にナイトメアは突っ伏してしまった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "テコでも動かないというように、微動だにしない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（本当に困った上司……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "駄々を捏ねる上司の面倒を見させられるこっちの気持ちも少しは分かってくれればいいのに。"

hide gre_t_03_6
show gre_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0365
Gray " 「……はあ。\n
仕方ありませんね、集中力も切れているようですし、休憩にしましょう」"

hide nai_s_03_8
show nai_s_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0509
Nightmare " 「うむ、そうだ。\n
グレイ、ココアを持ってきてくれ」"

hide nai_s_02_8
show nai_s_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0510
Nightmare " 「あれなら飲む。\n
いいか、絶対に他のものを混ぜるんじゃないぞ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "念には念を押すナイトメアに、グレイは呆れ顔だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（前科があるから仕方ないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飲み物や食べ物に彼は薬を混ぜ込んだことがある。\n
ナイトメアはグレイが持ってくるものはすべて疑ってかかっているらしい。"

hide gre_t_01_10
show gre_t_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0366
Gray " 「……はいはい、分かりました。\n
お持ちしますから、少し待っていてください」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「あ、いいわよ。\n
ココアなら私が……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋を出ようとしたグレイを追いかけると、彼は静かに首を横に振った。"

hide gre_t_01_13
show gre_t_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0367
Gray " 「いや、君の分も淹れてくるから、待っていてくれ。\n
すぐに戻るよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「……ありがとう」"

play sound se_0399
hide nai_s_02_6
show nai_s_02_6 at center
hide gre_t_01_4
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、部屋の中には私と仕事をボイコットした上司だけが残る。\n
グレイが立ち去ったのを確認して、彼は口を開いた。"

hide nai_s_02_6
show nai_s_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Nightmare " 「…………」"

hide nai_s_02_13
show nai_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice nig_f0511
Nightmare " 「では……。\n
グレイがいないところで内緒話といこうか、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「追い払ったみたいに言わないで。\n
機会を見ていただけよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人聞きの悪い。\n
だが私の言葉にナイトメアは、ふっと口元を持ち上げて見せただけだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（まるで、すべてお見通しとでも言わんばかりね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "実際心を見透かす夢魔である彼には、何も言わなくても私が聞きたいことなど分かっているのだろう。"

hide nai_s_03_10
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0512
Nightmare " 「グレイがいたら聞きにくいんだろう？\n
とはいえ、あいつは滅多に君の傍から離れないから、私だってタイミングを見計らっていたんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（どこまで本気だか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とはいえ、ナイトメアに聞きたいことがあったのも事実だ。\n
彼の好意に甘えて、尋ねることにした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「ねえ、ブラッドが言っていたけど、昔のグレイってああいう感じだったの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "昔のグレイ。\n
ナイトメアの命を狙ったこともあるという私の知らない頃のグレイ。"

hide nai_s_02_1
show nai_s_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0513
Nightmare " 「ふうん。\n
気になるのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T " 「そうよ、気になるの」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_16")
T "（悪い？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だって私はグレイのことを何も知らない。"

hide nai_s_02_12
show nai_s_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0514
Nightmare " 「ははは、そんなに怒らないでくれ。\n
いい傾向じゃないか、知りたいと思える相手に出会えたんだろう？」"

hide nai_s_03_11
show nai_s_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0515
Nightmare " 「だったら、好奇心を自分から殺すことはないさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（だったら、その笑い方はやめなさいよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "楽しそうな、それでいて不純なものを感じさせる、曖昧な笑み。\n
夢魔としての彼が見せる、顔だ。"

hide nai_s_02_4
show nai_s_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0516
Nightmare " 「そうだな、当時のグレイか。\n
あんなようなものだったかもしれないし、違っていたかもしれない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T " 「…………」"

hide nai_s_01_2
show nai_s_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
Nightmare " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくら次を待っても、ナイトメアはそれ以上話そうとはしない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「え、待って。\n
それで終わりなの！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（からかうだけからかって、誤魔化すつもりなの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず睨み付けると、彼は手を横に振って否定した。"

hide nai_s_01_9
show nai_s_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0517
Nightmare " 「誤魔化しているわけじゃない。\n
グレイが私の部下になるまでにはあまり興味がなかったからな」"

hide nai_s_02_8
show nai_s_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0518
Nightmare " 「だから、よく覚えていないんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T " 「よく覚えていないって。\n
役のない人じゃあるまいし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界では役の有無で顔の見えやすさも、存在感もまったく変わってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（少なくともグレイにはちゃんと役があるのに）"

hide nai_s_01_1
show nai_s_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice nig_f0519
Nightmare " 「言っただろう、興味がなかったんだ。\n
私は薄情な夢魔だからね、君のように個を認識するのは限られた状況だけだ」"

hide nai_s_01_2
show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice nig_f0520
Nightmare " 「それに……、君といるようになってからのグレイのほうが見ていて微笑ましい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（可愛い系の人には見えないんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスやボリスのような動物的な可愛さも、帽子屋屋敷の門番のような子供らしさも、グレイには縁遠いものだ。"

hide nai_s_01_11
show nai_s_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0521
Nightmare " 「そういう意味じゃないさ。\n
野心とは別のものを持つと、ああまで変わるのかと思うと……、な」"

hide nai_s_02_2
show nai_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0522
Nightmare " 「少なくとも、グレイ本人も君と会ってからの自分のほうが気に入っている。\n
君ももう少し自信を持っていいのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「でも、それは私が変えたからじゃないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私に誰かを変えるだけの力なんてあるはずがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（自分さえ変えられないのに）"

hide nai_s_03_10
show nai_s_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
Nightmare " 「…………」"

hide nai_s_02_13
show nai_s_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice nig_f0523
Nightmare " 「なら、ずっとあいつの近くにいてごらん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "日に当たっていない色素の薄い手に撫でられる。\n
昔、こうして姉にも頭を撫でられ、慰められたことがあった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（気持ちいい）"

hide nai_s_01_1
show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice nig_f0524
Nightmare " 「まだ信じられなくても、いつか分かる。\n
急ぐ必要もないからね、ここに溢れている時間は君を置いて行かないよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T " 「ええ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつか。\n
手の届くところにあるようで、まだ影さえも見えない遠い果て。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（そこに辿り着けるまで、ううん、辿り着けても）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この場所にいたいと思う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「グレイ、なかなか戻ってこないからちょっと様子を見てくるわ」"

hide nai_s_01_11
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice nig_f0525
Nightmare " 「ああ、任せたよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T " 「……念を押しておくけど、サボったり、逃走したらとびきり苦い薬を飲ませるからね」"

hide nai_s_02_1
show nai_s_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice nig_f0526
Nightmare " 「うっ……、それは嫌だな。\n
少なくともこの部屋で大人しくしていたほうがマシだ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（大人しくしているだけじゃなくて、仕事をしていてくれるのが一番なんだけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逃走防止効果が効いているうちに、グレイを呼び戻しに行ったほうがいいだろう。"

play sound se_0275
hide nai_s_02_10

$ hi_mes()


scene n_01
with stripe_l_medium

scene cr_01
with stripe_l_medium

scene bg_gen23_tkt
with stripe_l_long

play music happy_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_14")
T " 「一番近いキッチンはここのはずだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T " 「あ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（ココアの匂い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "徐々に甘い香りが空気に混じって流れてくる。\n
だが、その中に別の匂いが混じっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（煙草の匂いがする）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「グレイ？」"


show t_gre_end10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gra_f0368
Gray " 「あ……。\n
すまない、今戻ろうと」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り返ったグレイの手元には、私がプレゼントした灰皿があった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「あ、別にいいわよ。\n
……それ、使ってくれているのね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キッチンに備え付けられている窓。\n
その窓の横で、彼は煙草を咥えたところだったらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（火を付けたばかりで消させるのも悪いもの）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice gra_f0369
Gray " 「君からもらったものだからな。\n
大事に使わせてもらっている」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T " 「よかった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "並べて置かれたココアからは甘い香り。\n
だが、立ったままのグレイからは甘さのない紫煙の気配。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（不思議）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "混ざり合うはずのないものが、絡み合っている。"

play sound se_0546
hide t_gre_end10
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「これ、ナイトメアのカップよね。\n
届けておくわ」"


show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0370
Gray " 「あ、いいんだ。\n
俺が持っていくから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T " 「グレイは駄目よ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の手からカップを受け取ろうとした手を遮る。\n
代わりに残った二つのカップをグレイのほうへと押しやった。"

hide gre_t_01_4
show gre_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不思議な顔をするグレイに口を寄せて、小さく囁く。"

hide gre_t_01_11
show gre_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T " 「……駄目？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本来だったら、私達の休憩もまだ先。\n
だが、上司が仕事を溜めてしまっているのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアがココアを飲み終えるまで、私達も息を抜いてもいいだろう。"

hide gre_t_02_9
show gre_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
Gray " 「…………」"

hide gre_t_02_2
show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice gra_f0371
Gray " 「君の誘いを断るほど、俺は甲斐性なしじゃない」"


show white onlayer master
$ clear_mes()
hide white
show n_01_s onlayer master with Dissolve(1)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice nig_f0523
Nightmare " 「なら、ずっとあいつの近くにいてごらん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice nig_f0524
Nightmare " 「まだ信じられなくても、いつか分かる。\n
急ぐ必要もないからね、ここに溢れている時間は君を置いて行かないよ」"

hide n_01_s
show white onlayer master
$ hi_mes
hide white with Dissolve(1)
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（いつか本当に分かるのかどうかは、まだ分からないけど）"

hide gre_t_01_4
show gre_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice gra_f0372
Gray " 「君に求められるのなら、願ってもない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この人に捕らわれ、この人を捕らえて。\n
絡みついていけたなら、答えは見つかるのかもしれない。"



show white onlayer master
with compress_extralong
hide gre_t_01_1

scene black
with compress_extraextralong

$ renpy.movie_cutscene("endroll_a.mpg")
#return
