
scene map_bg_winter_day
with dis
label fushigi_end_tower1:
$ clockanim()


scene map_bg_winter_night
with dis

scene charasel_bg_tower_night
with dis

play music tower_room1_p_ali

scene co_03 with Dissolve(1.2)
play sound se_0087 volume .8

show t_end_tou1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0545
Nightmare "「この鉄板の上に生地を流して焼くという話だったが……、これでいいのか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0373
Gray "「ええ、彼女の話では溶いた生地をこの鉄板の上で焼くということでしたから。\n
これで間違ってはいないと思うんですが」"

play sound se_0087 volume .8
$ hi_mes()
$ show_mes("frame_gen_chara")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice jul_f0358
Julius "「おまえら、もう少し鉄板をうまく使えないのか？\n
特にトカゲ、どうしてそんなに無節操に広がるんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0374
Gray "「仕方ないだろう、こうも柔らかい生地ではうまくいかない。\n
むしろ、型で抜いたように円形を作れるおまえのほうがおかしい」"

$ hi_mes()
$ show_mes("frame_gen_chara")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
Gray "「…………」"

hide t_end_tou1

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（また睨み合っている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスもグレイも立派な大人のはずなのに、どうして彼らはこうも口論を繰り返すのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（それもエリオットがディーやダムと喧嘩するのとは違って、空気がピリピリするような感じ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本来の領土は違えど、それぞれ中立の立場で、今はドア一枚を隔てたところに住んでいるのだから、もう少し仲よくしてくれればいいのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（…………。\n
無理かな、やっぱり）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までのやりとりを思い出してみても、関係の改善は難しそうだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これでもお互いを見て言い合うだけましだとナイトメアが言っていたので、気長に付き合うしかないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それよりも今は、鉄板の上にある生地をうまく焼くほうが先のようだ。"


show toustaff_a2_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0050
Tower_Employee "「キャベツの準備、整いましたよ」"

hide toustaff_a2_2
show toustaff_a2_2 at left
show toustaff_c_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0055
Tower_Employee "「生地もよく混ざりましたから、こちらも準備オッケーです」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「あ、ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ごめんなさいね、こんなことを手伝わせて」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔にある広い部屋で、私達は鉄板を囲んでいる。\n
テーブルには、野菜や生地が広がっていた。"

hide toustaff_a2_2
show toustaff_a2_2 at left_center
with dis
hide toustaff_c_2
show toustaff_c_2 at center
show toustaff_b2_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0082
Tower_Employee "「そんな、気にしないでください。\n
それに、異国の料理に触れる機会って貴重ですから、勉強になります」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「勉強？\n
あなた達もグレイみたいに料理の勉強をしているの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "食事会の準備を手伝ってくれている彼らの手付きは、確かに慣れた人間のものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（本人には言えないけど、グレイよりも上手よね）"

hide toustaff_a2_2

hide toustaff_c_2
show toustaff_c_2 at left_center
hide toustaff_b2_2
show toustaff_b2_2 at center
with dis

show toustaff_d_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice oto_f0057
Tower_Employee "「あれだけ料理に熱心なグレイ様がいると、つい自分も手を出したくなってしまって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「ああ、なるほど。\n
それは分かる気がするわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰かが一生懸命なことには、誰でも多少なりとも興味を抱くものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "特にグレイほど真剣に取り組んでいる人がいれば、周りにも影響が出てもおかしくない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（成果が出ていないのが不思議なくらい、熱心なんだもの）"

hide toustaff_c_2

hide toustaff_b2_2
show toustaff_b2_2 at left_center
hide toustaff_d_1
show toustaff_d_1 at center
show toustaff_a2_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice kat_f0051
Tower_Employee "「それに、ナイトメア様の病人食も色々と工夫して差し上げたいですしね」"

hide toustaff_b2_2

hide toustaff_d_1
show toustaff_d_1 at left_center
hide toustaff_a2_1
show toustaff_a2_1 at center
show toustaff_c_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice tan_f0056
Tower_Employee "「そういえば、あの鉄板って……、どこから調達したんですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_2")
T "「ああ、あれはユリウスの部屋にあったのを借りたの。\n
ついでに火力の強いコンロを持ってきたのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らが立っている前に置かれているのは、即席の鉄板コーナーだ。\n
バーベキューで使うことも出来るらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（でも、さすがに小火騒動を起こしたばかりで、煙の多い料理は……、ちょっとね）"

hide toustaff_d_1
show toustaff_d_1 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice oto_f0058
Tower_Employee "「……どうして時計屋さんの部屋にあんな鉄板があるんですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「さ、さあ、色々と事情が複雑みたいだから細かくは聞かなかったけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "適当なことを言って誤魔化しているが、彼の疑問は私も感じたことだ。\n
当然、持ち主に理由は聞いている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……まさか、エースが置き忘れていったキャンプ道具とは言えないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "味気なく見えるユリウスの部屋だが、探せば意外とアウトドアグッズが隠されているのかもしれない。"

hide toustaff_a2_1
show nai_s_02_2 at center
hide toustaff_d_1

hide toustaff_c_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0546
Nightmare "「おい、[firstname]。\n
君もいつまでも離れたところにいないで、こっちに来たらどうだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"


play music cheerful_a_ali

show t_end_tou2 onlayer master
with dis
hide nai_s_02_2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの声に呼ばれて戻れば、そこではまだグレイとユリウスが金属の道具を持って、鉄板を睨んでいた。"

play sound se_0037
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_14")
T "（あ、うまい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "火が通ったところを見計らって、ユリウスが最初に生地をひっくり返す。"

play sound se_0087 volume .8
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（……おいしそうな音）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、鉄板の上に出てきた面は、綺麗なきつね色だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "続いてグレイが真剣勝負でも挑むのかと思う表情で、手を動かした。"

play sound se_0037
pause .4
play sound se_0146
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（あ、ぐちゃっていった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイのお好み焼きはひっくり返りかけたところで、型崩れしてしまった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（タイミングが悪かったのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gra_f0375
Gray "「何故、おまえの生地は少しも崩れずひっくり返るんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0359
Julius "「不器用なおまえと一緒にするな。\n
特におまえの場合、ひっくり返すのが早すぎるのが原因だろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心底驚いたような表情を浮かべるグレイに、ユリウスが無愛想に返す。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0547
Nightmare "「ふ、では次は私の番だな、よく見ていろ！\n
よ……、たあ！」"

play sound se_0037
pause .6
play sound se_0087
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0548
Nightmare "「ふ、ふふふ。\n
どうだ、見たか、私の華麗なヘラ捌きを！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「…………」"

hide t_end_tou2

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（でも、ナイトメアのが一番小さいのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "火の通りもよければ、ヘラを二本使えば十分支えきれる大きさだ。\n
当然、難易度も低い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（それをひっくり返したからって、得意げになられてもなあ）"


show nai_s_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice nig_f0549
Nightmare "「[firstname]、そんな冷たいことを言わなくても。\n
うまく焼けたら、君にあげようと思っていたのに」"

play sound se_0128
$ flash_yellow(.1)
hide nai_s_02_9
show nai_s_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice nig_f0550
Nightmare "{size=+20}「うわちっ！？」{/size} "

hide nai_s_03_2
show nai_s_03_2 at left
show gre_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice gra_f0376
Gray "「大丈夫ですか、ナイトメア様！？」"

hide nai_s_03_2
show nai_s_03_2 at left_center
hide gre_t_03_2
show gre_t_03_2 at center
show yuri_t_01_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice jul_f0360
Julius "「油が跳ねただけだろう、いちいち騒ぐな」"

hide yuri_t_01_3
show yuri_t_01_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice jul_f0360_5
Julius "「……おいトカゲ、そこは火が集中している、焦がしたくなければずらしたほうがいいぞ」"

hide gre_t_03_2
show gre_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice gra_f0377
Gray "「何？」"

play sound se_0087
hide gre_t_01_5
show gre_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
Gray "「…………」"

hide gre_t_01_12
show gre_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice gra_f0378
Gray "「悔しいが、確かにおまえの言うとおりだな、時計屋」"

play sound se_0143
hide yuri_t_01_8
show yuri_t_03_13 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice jul_f0361
Julius "「……ふん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（ユリウスって、鉄板奉行？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイは自分の生地をちらりと見やってから、ヘラで動かした。\n
文句を言いながら、やることに手を抜かないのがユリウスらしい。"

hide nai_s_03_2
show nai_s_01_10 at center
hide gre_t_01_11
hide yuri_t_03_13
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0551
Nightmare "「うう、痛い、少しは労ってくれたっていいだろう。\n
……あー、ショックだ、ショックで気持ちが悪くなってきた」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「……食事中に食べ物が美味しくなくなるようなことは、しないわよね？」"

play sound se_0344
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "テーブルに肘を突くナイトメアに、ボールを置いてから尋ねる。\n
食事をしている最中に気持ちが悪くなられても困るのだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「今回は私が皆にご馳走するために準備したのよ？\n
それとも、気に入らない？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（今回ばかりは、吐血も、～～～～も、とりあえず～～関係だけはＮＧよ。\n
ビジュアル的に、全部台無しになるから）"

hide nai_s_01_10
show nai_s_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice nig_f0552
Nightmare "「……う、分かった、肝に銘じておこう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口を押さえながら、ナイトメアはなんとも頼りなく頷く。"


show gre_t_02_3 at center
hide nai_s_01_4
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0379
Gray "「ところで、[firstname]。\n
鉄板で焼く料理だということは聞いていたが、これは一体何なんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「ああ、これはね、この前読んだ本に出ていた料理なんだけど。\n
生地に入れる具材も色々試せるみたいで、今、焼いているのはお肉がメインなの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「シーフードを入れてもいいらしいし、チーズなんかもおいしいんですって。\n
次のはまた違う具材にしてみるわね」"

hide gre_t_02_3
show gre_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0380
Gray "「具材を色々と試せる……、か。\n
なら、こういったものを入れてみてもいいんだろうか」"

play sound se_0203
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが期待を込めた眼差しで手にしたものは、硝子瓶に詰められた薬だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T "（一体どれだけ普段から隠し持っているんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隙あらばナイトメアに飲ませるつもりなのだろうが、グレイは本当に用意がよすぎる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「いや、さすがにそれは……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（混ぜ込んだら、確実に生地よりも薬のほうが多そうだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなものを鉄板で焼いたら、謎の化学反応を起こすに決まっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T "（小火のときの煙よりもずっと凶悪な有毒ガスが出てもおかしくないんじゃ……）"

hide gre_t_02_4
show gre_t_02_4 at left
show nai_s_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_10")
voice nig_f0553
Nightmare "「却下だ、却下！\n
そんなもの誰が食うんだ、単なる焼き薬じゃないか」"

hide gre_t_02_4
show gre_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_10")
voice gra_f0381
Gray "「いえ、これならナイトメア様もおいしく食べられるのではないかと。\n
どうも俺の料理ではご不満なようですし」"

hide nai_s_02_10
show nai_s_03_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_10")
voice nig_f0554
Nightmare "「薬を焼いて食わせようとする奴の料理なんか食えるか！！」"


show yuri_t_02_11 at center
hide gre_t_02_10
hide nai_s_03_6
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_10")
voice jul_f0362
Julius "「……うるさいぞ、生地が焦げる。\n
ナイトメア、おまえのはそろそろ下ろさないと、裏が完全に焦げるぞ」"

hide yuri_t_02_11
show yuri_t_02_11 at left
show nai_s_03_3 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_10")
voice nig_f0555
Nightmare "「な、なに！？」"

play sound se_0544
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鉄板を真剣に見つめているユリウスに忠告され、慌ててヘラを握ったナイトメアが生地を手元の皿に移す。"

hide nai_s_03_3
show nai_s_03_7 at center
hide yuri_t_02_11
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0556
Nightmare "「ふう、危ないところだった。\n
私まで食えないものを作ってしまうところだった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「今回の食材調達は私がやっているんだけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（食べられないものなんて出さないわよ）"

hide nai_s_03_7
show nai_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice nig_f0557
Nightmare "「あ、いやそういうわけじゃなくて……。\n
焦がしたらもったいないだろう、なにしろこの私が作ったんだからな！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「はいはい、分かったわ。\n
あ、仕上げにこのソースをかけるのを忘れないでね」"

play sound se_0087
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「あとは好みでマヨネーズをかけてもいいらしいから、ご自由にどうぞ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鉄板からは、調味料の香ばしい匂いが漂ってきた。"

hide nai_s_02_3
show nai_s_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0558
Nightmare "「これはまた香ばしくて、いい匂いだ。\n
では、早速……」"

play sound se_0545
hide nai_s_03_1
show nai_s_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "{size=+20}「！！！？」{/size} "

hide nai_s_03_4
show nai_s_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0559
Nightmare "「あ、あふ、あふいーーーっ！！？」"

hide nai_s_03_2
show nai_s_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0560
Nightmare "「は、ふ、ほほ、ふへっ！？」"

hide nai_s_03_3
show nai_s_03_3 at left
show gre_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0382
Gray "「ナ、ナイトメア様！？\n
落ち着いてください、すぐに水をお持ちしますからそのまま……」"

hide nai_s_03_3
show nai_s_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「！！！」"

play sound se_0065
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勢いよくぱくついたナイトメアは、慌てて水を飲み干している。\n
身体の弱い夢魔は舌もまた、熱に弱いシロモノだったらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（あれだけ無警戒に食べれば驚くでしょう。\n
それ以前に少しは警戒することを覚えたほうがいいわ、あの病人は）"


show yuri_t_01_13 at center
hide nai_s_03_7
hide gre_t_03_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice jul_f0363
Julius "「まあ、口に入れたものを出さないだけマナーは守ったか」"

play sound se_0087
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一人我関せずのユリウスだが、さりげなくグレイの分を火の弱い場所に移している。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、自分の分を皿に乗せて、私のほうに視線を動かした。"

hide yuri_t_01_13
show yuri_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0364
Julius "「そういえば、おまえの分は？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「あ、いいのよ、今回私は皆を食べさせる役目だから。\n
そのボール、もう中身が空っぽでしょう、新しく作ってくるから待っていて」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（お世話係はまたあとでゆっくり食べればいいもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エプロンに三角巾という格好をしていると、三人のお姉さんやお母さんになった気分だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分が焼いたわけではないが、作った生地を食べてくれると嬉しくなる。"

hide yuri_t_03_2
show yuri_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0365
Julius "「お、おい、本当に食べなくてもいいのか、おまえ」"

hide yuri_t_03_3
show yuri_t_03_3 at left
show gre_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0383
Gray "「時計屋の言うとおりだ、本を読むくらいなんだから、君だって食べたいだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「……うん、でもいいわ。\n
こんなものでしかお詫び出来ないなんて情けないけど、皆がおいしく食べてくれれば、それでいいもの」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（皆がいるところにいられるだけで、いい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お詫びの食事会を提案したとき、彼らは口を揃えて「そこまでしなくても」と言ってくれたが、それでは私の気がすまないと押し通した。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（ここが私のいる場所）"

hide yuri_t_03_3

hide gre_t_02_7

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここが大切で、好きだからこそ、曖昧にしたくない。"

$ hi_mes()

scene co_03
with dis

scene bg_gen_sky_win_nig
with dis

play music honobono2_a_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kat_f0052
Tower_Employee "「あれ、一緒に召し上がらなくていいんですか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice tan_f0057
Tower_Employee "「準備なら、あとは俺達だけでも出来ますから、気にしないでいいのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キッチンに戻ると、私を気遣った言葉がかけられる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ありがとう、でも、外で充分すぎるぐらいにもてなされてきたから。\n
自分の家では、ちゃんとさせて」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice hos_f0083
Tower_Employee "「自分の家だったら、そんなに肩肘を張らなくていいんですよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice oto_f0059
Tower_Employee "「ええ、任せるのも同じ場所に住んでいるからこそですし」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_2")
T "「自分でも面倒な性格をしているとは思うんだけどね。\n
気持ちだけもらっておくわ、ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大事だから、ちゃんと筋を通したい。\n
他にもっと楽な方法もあるかもしれないが、私はこういう形でしか表せない。"

$ hi_mes()

scene bg_gen_sky_win_nig
with dis

scene co_03
with dis

play music moon_night1_a_ali

show yuri_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jul_f0366
Julius "「……ふむ、騒がしい料理だが、こういうスタイルは珍しいな」"

hide yuri_t_02_1
show yuri_t_02_1 at left
show nai_s_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0561
Nightmare "「あー、うまかった、それにナイフとフォークを使わない食事というのも珍しい。\n
このヘラも二本の棒も、使っていれば慣れるものだな」"

play sound se_0663
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「行儀が悪いわよ、ナイトメア。\n
そういうのは不作法なんですって」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（……って、私も聞きかじりならぬ、読みかじりだからどこまで本当かは知らないけれど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それぞれ自分が焼いたものを食べ終えたらしい三人は、三者三様の感想を告げる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "このばらばらで、しかし彼ららしいやりとりを聞くと、塔に帰ってきたという実感がわく。"

hide yuri_t_02_1

hide nai_s_01_1
show nai_s_01_1 at left
show gre_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0384
Gray "「そうですね、確かにこれは便利な道具です」"

hide gre_t_02_10
show gre_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0384_5
Gray "「先端を研いでおけば、いざというときの護身にも使えますし、この軽さならナイトメア様でも使えるかも」"

hide nai_s_01_1
show nai_s_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0562
Nightmare "「……そんな物騒なもので食事をさせられるのは、遠慮したい。\n
食べ物がまずくなりそうだ」"

hide nai_s_01_10

hide gre_t_02_3

play sound se_0087 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（あら、でもまだ焼いている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "満腹を訴える彼らの前では、まだ三枚の生地が焼かれていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（余っちゃったのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "生地のままでは保存も出来ないから、焼いてしまうほうがいいのは確かだが。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「この三枚はどうするの？\n
後でおやつにでも食べる？」"


show yuri_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice jul_f0367
Julius "「いや、私はもう充分食べたからしばらくはいい」"

hide yuri_t_02_2
show yuri_t_02_2 at left
show gre_t_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice gra_f0385
Gray "「うまかったよ、[firstname]、ありがとう。\n
それで、これは、その……、君に食べてもらおうかと思って焼いたものなんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「え、わ、私の分まであなた達が焼いてくれたの？」"

play sound se_0087 volume .8
hide yuri_t_02_2
show yuri_t_02_2 at left_center
hide gre_t_01_7
show gre_t_01_7 at center
show nai_s_02_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_10")
voice nig_f0563
Nightmare "「君はさっきから下ごしらえや片付けで、まともに食べていないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「で、でも……」"

hide gre_t_01_7
show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice gra_f0386
Gray "「君が仲直りの食事会だと言ったんだ、君が食べていないのに終わるのはおかしい」"

hide gre_t_01_4
show gre_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice gra_f0386_5
Gray "「一緒に食べてくれ、片付けは俺も手伝おう」"


play music night_garden_p_ali

show t_end_tou3 onlayer master
with dis
hide gre_t_01_3

hide nai_s_02_2

hide yuri_t_02_2

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目の前には三枚の生地。\n
綺麗な円形をしているもの、小振りなもの、形が少し歪なもの。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（同じものから作っているのに、こんなに違うなんて……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それぞれの性格が出ているようで、それが何だかおかしい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0368
Julius "「早くしないと焦げるぞ。\n
焦げる前なら、どれを食べても味は変わらんから安心しろ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（どれも美味しそうで、迷っちゃうわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "味は変わらないはずだが、見た目がはっきり違うせいで、目移りする。\n
それは彼らも同じようだった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0564
Nightmare "「おすすめは当然、私の焼いたものだけどね。\n
他のものより小ぶりだから、君でも食べやすいように考えられている！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（本当に考えているかは別として、確かに食べやすそうよね）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0387
Gray "「それはナイトメア様がひ弱なせいではありませんか。\n
[firstname]、その……、見た目はうまくないが、味は保障しよう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice jul_f0369
Julius "「だから味はどれも同じだと言っているだろう。\n
こいつらのとは違って、私の作ったものが形も含めて一番うまいとは思うがな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「ああもう、そうやってすぐに睨み合わないでよね！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアだけを蚊帳の外に険悪になりかけた二人に声をかける。\n
どれをとっても、立場が悪くなりそうだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（……それなら）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「全部を少しずつ食べることにするから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "三者三様の形。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元になったものを作ったのは私なのに、それがこの人達の手にかかるとこれだけ違う顔を見せる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さな鉄板の中に、色々なものが溶けているのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（……私が生地みたいなものに、なれているのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "具材は、一つだけではばらばらと崩れてしまう。\n
繋ぐものがあるからこそ、こうやって一つの形になれる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（私にそんな価値があるなんてまだ思えないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな関係になることが出来たらいいと、心から思った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0565
Nightmare "「さあ、選ぶ権利は君にあるんだ、好きなものから召し上がれ」"

play sound se_0267

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手渡してもらった箸を持って、私は手を合わせた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「ええ、いただきます」"

scene black with dis

hide frame_gen_heroine
hide ali_t_01_10
with Dissolve(5)
pause 1

##endroll_b
