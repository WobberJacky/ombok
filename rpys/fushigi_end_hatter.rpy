
scene map_bg_autumn_day
with dis
label fushigi_end_hatter1:
$ clockanim()


scene map_bg_autumn_night
with dis

scene b_aut_03
with dis

play music hatter_guestroom_p_ali

scene bg_03_1
with Dissolve(1.2)

show bousi_t_01_08 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice may_f0059
Maid "「まあ……、とても可愛いです～」"

hide bousi_t_01_08
show bousi_t_01_08 at left
show bousi_t_02_07 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice chi_f0054
Maid "「よく似合っていますから、きっと皆さん喜ばれますよ～」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……ねえ、もしかしてとは思うんだけどね。\n
あなた達が私に黙っていたのって、このことだったわけ？」"

hide bousi_t_01_08

hide bousi_t_02_07


scene bg_03_1_s with Dissolve(8)

scene bg_gen08_bn_aut_nig_p with Dissolve(1.6)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屋敷に戻った私を待ち構えていたのは、これでもかと飾り立てられた広大な庭。\n
そしてそこに準備された、パーティ会場だった。"


scene bg_03_1_s with ImageDissolve("gui/stripe_l.png", 1.6, ramplen=128, reverse=True)

scene bg_03_1
with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「私、このお屋敷に来てから誰かの誕生日を祝うなんて、初めて聞いたけど。\n
それもこんな大規模なものなんて」"


show bousi_t_01_02 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice may_f0060
Maid "「ふふふ、驚かれましたか～？」"

hide bousi_t_01_02
show bousi_t_01_02 at left
show bousi_t_02_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice chi_f0055
Maid "「皆でお嬢様をびっくりさせたくて、急ピッチで準備を進めたんですよ」"

hide bousi_t_02_02
show bousi_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice chi_f0055_5
Maid "「こんなに集中したことなんて、大きな組織を襲撃するのと同じぐらい久しぶりです～」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（そういうたとえ方をされても……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そういう場面とは縁遠い私にはよく分からないが、彼女達が浮き足立っているのは間違いないらしい。"

hide bousi_t_01_02
show bousi_t_02_05 at left
hide bousi_t_02_01
show bousi_t_02_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0061
Maid "「多分……、初めてだと思いますよ。\n
ここまで、屋敷をあげて誰かの誕生日を祝うことなんて、今までなかったですから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「初めて……？」"

hide bousi_t_02_05
show bousi_t_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice chi_f0056
Maid "「ええ。\n
ここでは誕生日なんてあってないようなものですもの～」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（……そういえば、最初にここに来たときにも同じようなことを言っていたわよね、ブラッド）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誕生日を祝ってやると言われたのは最初のお茶会。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誕生日ではないことを告げると、誕生日でない日を祝えとか、滅茶苦茶な論理を展開された。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（そもそも時間が狂っているのに、誕生日も何もないわよね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「それなのに私の誕生日を祝うだなんて……、矛盾していない？」"

hide bousi_t_02_05
show bousi_t_02_01 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice may_f0062
Maid "「名目はなんでもいいんです。\n
お嬢様を中心に何かしたかったんだと思いますよ～」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこにこと笑う使用人達は、そう言いながら私をドレスへ着替えさせてくれた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隠されていた内容が、自分の誕生日パーティなだけに、不機嫌になったことが恥ずかしい。"

hide bousi_t_02_01

hide bousi_t_01_01

play sound se_0580
pause .40
play sound se_0300

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鏡を確認していると、足音がして、部屋のドアがノックされた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0525
Dee "「ねえねえ、お姉さんの準備、まだなの！？\n
僕達待ちくたびれちゃったよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0526
Dam "「手伝いが足りないなら、僕達が手伝ってあげるよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「ディー、ダム」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアの向こう側からは、急かすような二人の声が聞こえる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0527
Dee "「準備万端なんだから、早く早く！\n
食べ物も、飲み物も全部とられちゃう」"


show bousi_t_02_06 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0063
Maid "「はいはい、今行きますよ～」"

hide bousi_t_02_06
show bousi_t_02_06 at left
show bousi_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0057
Maid "「では、お嬢様、皆さんがお待ちですから、行きましょう～」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え……。\n
う、うん、分かったわ」"

hide bousi_t_02_06

hide bousi_t_01_02

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "使用人に付き添われて、部屋の外へと向かう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（うわ、ヒールが高い……。\n
転ばないように気を付けなくちゃ）"

play sound se_0275

play music hatter_corridor_p_ali

scene br_03
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアを開ければ、そこには見慣れたいつもの顔が待っていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「お、お待たせ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（……って言うのも変だけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、私の姿を見た双子は口を半開きにしたまま呆然としていた。"


show dee_p_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0530
Dee "「……っ、うわああ、すごい！可愛い！\n
いつも可愛いけど、今回は更に可愛い」"

hide dee_p_02_6
show dee_p_02_6 at left
show dam_p_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0531
Dam "「お姉さん綺麗だよねえ。\n
いつもと違うお姉さんもいいなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T "「……ありがとう。\n
あなた達も、素敵ね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手放しで誉めてくれる双子は、いつもと違う服装だ。"

hide dee_p_02_6
show dee_p_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0532
Dee "「だってパーティだもん、びしっとしないとね。\n
どうかなあ、この格好も似合っているでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ、とても似合っていて格好いいわ」"

hide dam_p_02_4
show dam_p_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice dad_f0533
Dam "「ふふ、よかった。\n
舞踏会のときみたいに笑われたら嫌だもんね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人はそこでタイミングを合わせて私に向かって、一礼してきた。"


show t_end_bousi1 onlayer master
with dis
hide dee_p_02_10

hide dam_p_02_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0534
Dee "「[firstname]、お手をどうぞ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0535
Dam "「足下にはお気を付けて……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_8")
T "「あ、う……、うん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（大人の姿で言われるのも変な気分だけど。\n
子供の姿でこういう扱いをされると、なんだか……、恥ずかしい）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「よろしくお願いします」"

play sound se_0267
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "片方ずつ手を取られて、エスコートされる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0536
Dee "「うん、任せて。\n
なんていったって、今夜はお姉さんが主役だもん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0537
Dam "「お姉さんが楽しめるのが一番だよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人につられて、私もようやく自然に笑顔を浮かべることが出来た。"

$ hi_mes()
hide t_end_bousi1


scene b_aut_03
with stripe_l_medium

play music map_hatter1_ali

scene bg_gen08_bn_aut_nig_p
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "庭に出れば、私を歓迎するように同僚が声をかけてくる。"


show situji_t_01_04 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0044
Servant "「ああ、お嬢様、お待ちしていました。\n
門番さんも、エスコート、お疲れ様です～」"

hide situji_t_01_04


show dee_p_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0538
Dee "「あんまりじろじろ見ないでよ、お姉さんが減っちゃうだろ。\n
着席するまでは僕達しか案内をしちゃいけないんだ」"

hide dee_p_02_8
show dee_p_02_8 at left
show dam_p_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0539
Dam "「そうだよ、そうだよ。\n
エスコート役は僕達がもらったんだから」"


show situji_t_02_01 at center
hide dee_p_02_8
hide dam_p_02_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0047
Servant "「もちろん分かっていますよ。\n
ボスも、あちらでお待ちです」"

hide situji_t_02_01

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すっと指し示されたほうを見れば、夜の時間帯にも鮮やかなオレンジの髪が浮かんでいる。"


show eri_s_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0321
Elliot "「お、ようやく主役が出てきたな。\n
[firstname]、待っていたぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「エリオット……。\n
お待たせしちゃってごめんなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "既にテーブルに着席しているエリオットとブラッドも、スーツ姿だった。\n
会場に着くと、本当に祝ってくれるのだと実感が沸いてくる。"

hide eri_s_01_1
show eri_s_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0322
Elliot "「いいって、気にするなよ。\n
そのドレスだってよく似合っているもんな」"

hide eri_s_01_3
show eri_s_01_3 at left
show dee_p_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0540
Dee "「そうだよ、そうだよ。\n
ひよこウサギを待たせたぐらい、なんでもないじゃない」"

hide dee_p_02_4
show dee_p_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0541
Dee "「むしろこの機会に待てを覚えさせたほうが効率的かもしれない。\n
馬鹿ウサギのことだから、次の時間帯には忘れちゃいそうだけどさ」"

hide eri_s_01_3

hide dee_p_02_4
show dee_p_02_4 at left
show dam_p_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0542
Dam "「今夜はお姉さんの相手で忙しいから、ウサギの躾までやっていられないよね。\n
特別手当をはずんでくれても、お断りだよ」"


show eri_s_02_9 at center
hide dee_p_02_4
hide dam_p_02_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0323
Elliot "「おまえらいい加減にしろよ……。\n
誰がウサギだって？」"

play sound se_0295
pause .4
play sound se_0354
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "机を叩いて銃を取り出したエリオットを制止しようとするが、私が言うよりも先に声がかかった。"

hide eri_s_02_9
show eri_s_02_9 at left
show bra_s_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0526
Blood "「エリオット、この距離で発砲すると紅茶が硝煙臭くなるから、やめろ。\n
ダージリンの繊細な香りが台無しになってしまう」"

hide eri_s_02_9
show eri_s_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0324
Elliot "「ブラッド……、でもよ！」"

hide bra_s_02_3
hide eri_s_02_6
show dee_p_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0543
Dee "「そうだよ、今夜は銃や刃物は御法度だってボスが言っていただろう。\n
パーティのルールだよ！」"

hide dee_p_02_6
show dee_p_02_6 at left
show dam_p_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0544
Dam "「もう忘れちゃったの？\n
本当に馬鹿だよね」"

hide dee_p_02_6
hide dam_p_02_1
show eri_s_03a_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot "「～～～～っ！！」"

play sound se_0160
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "椅子から立ち上がったエリオットが、懐に銃をしまうと同時に手を持ち上げたが。\n
やはり、彼の横からかけられた制止の声のほうが早かった。"


show bra_s_02_18 at center
hide eri_s_03a_6
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0527
Blood "「その辺りにしておきなさい。\n
着飾った主役の前で持ち出す話題としては、マンネリすぎてつまらない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "{size=+20}「諸悪の根源が偉そうに」{/size}"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_13")
T "（私の反応まで予測していて黙っているなんて、質が悪すぎるわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットの横に座ってカップを傾けているブラッドを睨むと、彼は楽しそうに肩を震わせた。"

hide bra_s_02_18
show bra_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0528
Blood "「そう冷たくしないでくれ、君を驚かせたかっただけさ。\n
びっくり箱の中身を最初に教えてしまったら、感動が薄れるだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「びっくり箱だっていう自覚はあったわけ？\n
誕生日プレゼントにしては、刺激が強すぎるわよ」"

hide bra_s_03_10
show bra_s_03_10 at left
show eri_s_03a_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_16")
voice eri_f0325
Elliot "「だ、だから、悪かったってば！\n
ほら、いい加減立ちっぱなしっていうのも変だろ、あそこが空いているから座れよ」"

hide bra_s_03_10

hide eri_s_03a_4

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「あそこって……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "{size=+20}「あそこ！？」{/size}"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットが指している席は、上座だ。\n
普段であればブラッドが座るべき、トップの席である。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「い、いいわよ、そんなところに座らなくても。\n
席は、いっぱいあるし……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（そういえば、なんで上座にブラッドが座っていないの？）"


show bra_s_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice blo_f0529
Blood "「……エリオット。\n
お嬢さんは慣れない靴で難儀している、ご案内してやれ」"

play sound se_0468
hide bra_s_01_10
show bra_s_01_10 at left
show eri_s_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice eri_f0326
Elliot "「おう、任せておけって。\n
よっと……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！？」"

play sound se_0051

show t_end_bousi2 onlayer master
with dis
hide bra_s_01_10

hide eri_s_02_2
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「エ、エリオット！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドが指を打ち鳴らすと、エリオットがこちらへやってきて、私を肩に乗せる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0327
Elliot "「ん？\n
何だ、別の抱え方のほうがよかったのか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0530
Blood "「ふむ、そうだな。\n
この距離では物足りないというのなら……、庭を一周してくるといい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「いい！\n
このままでいいから、早く下ろして！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（こんな格好で庭なんか回らないでよ！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットにとってブラッドの言葉は鶴の一声だ。\n
はっきりと言っておかないと、彼のことだ、本当に連れて行かれてしまう。"

play sound se_0624
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0328
Elliot "「ちゃんと席に着いたら降ろしてやるから、ちょっと待ってな」"

hide t_end_bousi2


show dee_p_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0545
Dee "「あー、ずるいよボス、お姉さんを席に案内するのは、僕達の役目だったのにっ。\n
ちゃんと公平にくじ引きで決めたんだから、約束は守ってよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "文句を言う双子に、彼らの主は態度を変えない。\n
わざとらしく溜息をついて、首を傾げた。"

hide dee_p_02_13
show dee_p_02_13 at left
show bra_s_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0531
Blood "「公平か……、おまえ達が用意したくじには、少し特殊な細工がしてあったようだが。\n
あれは、私の気のせいかな？」"

hide dee_p_02_13
show dee_p_02_13 at left_center
hide bra_s_01_10
show bra_s_01_10 at center
show dam_p_02_7 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam "「！！」"

hide dam_p_02_7
show dam_p_02_11 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0546
Dam "「もちろん、気のせいだよ！\n
僕達がイカサマなんてするはずがないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（ばれているわね、完璧に）"

hide dee_p_02_13

hide bra_s_01_10

hide dam_p_02_11
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、いつものブラッドなら双子のイカサマに気付いた時点で指摘しそうなものだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（今回はわざと黙っていたみたいだし……、最初からこの予定だったんじゃ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドをじっと見ても、ポーカーフェイスは相変わらず崩れなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その間にもエリオットに運ばれた私は椅子の上に下ろしてもらったが、座らされた席にどうしても抵抗を覚えてしまう。"

play sound se_0160

show t_end_bousi3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0329
Elliot "「着いたぜ、[firstname]。\n
パーティの主役の席は、ここだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「……落ち着かないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "椅子の作りは他のものと変わらないはずなのに、いつもと違う視界にそわそわしてしまう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0330
Elliot "「ははは、そうだよなあ。\n
俺も座ったことねえもん、ここ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（そうでしょうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドに心酔しているエリオットが、その主を差し置いて一番の席に座るはずがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……むしろ腹心としては、私なんかを座らせちゃっていいのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットにとっては、面白くないのではないだろうか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice eri_f0331
Elliot "「ん？\n
どうした、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「私なんかが本当にここに座っていいの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "傍に立っているエリオットを見上げて聞くと、彼は首を傾げた。\n
長い耳も、ひょこりと揺れる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0332
Elliot "「何言っているんだよ、ブラッドがあんたの席を決めたんだぜ？\n
俺に文句があるわけねえだろ」"

hide t_end_bousi3


show bra_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0532
Blood "「そうとも、この屋敷では私がルールだ。\n
私が許可したことに文句を言うような輩はいない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子をやり込めたブラッドは静かに私の横にやってくる。\n
テーブルに片手を突き、斜めの角度から緑の眼に覗き込まれた。"

hide bra_s_03_10
show bra_s_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0533
Blood "「さて……、お嬢さんへのプレゼントだが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……いいわよ、そんなの。\n
お祝いをしてもらえるだけで、充分だわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドレスも、庭の装飾も、どれもこれも手が込んでいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段の仕事をこなしながら、これだけの準備をするのは、けして楽なことではなかっただろう。"

hide bra_s_01_2
show bra_s_01_2 at left
show dee_p_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0547
Dee "「あのね、あのね、僕達も色々探したんだよ！\n
玩具とか、お菓子とか……」"

hide bra_s_01_2

hide dee_p_02_6
show dee_p_02_6 at left
show dam_p_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0548
Dam "「でも、軒並み、ひよこウサギとボスに駄目出しされたんだよね」"

hide dee_p_02_6
hide dam_p_02_8
show dam_p_02_8 at left
show eri_s_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0333
Elliot "「当たり前だろうが。\n
ナイフの練習用人形とか、～～～～とか、～～～～とか……」"

hide dam_p_02_8
hide eri_s_02_9
show eri_s_02_9 at left
show bra_s_02_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0534
Blood "「そんなものを渡したら、今度こそお嬢さんが我が屋敷に戻ってこなくなるからな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに、そんなものをもらったところで強固にお断りしていたことだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（まだ八つ当たりくんとか、お風呂の玩具のほうがマシだわ）"


show dee_p_02_8 at center
hide bra_s_02_14

hide eri_s_02_9
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice dad_f0549
Dee "「そういうひよこウサギだって、いつものにんじんケーキしか言わなかったじゃないか。\n
おまえこそマンネリだろうっ」"

hide dee_p_02_8
show dee_p_02_8 at left
show eri_s_03a_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice eri_f0334
Elliot "「馬鹿かおまえら、にんじんケーキは老若男女誰にも受けるんだぜ。\n
あれを喜ばねえ奴なんているはずがない、そうだよな、ブラッド！？」"


show bra_s_02_9 at center
hide eri_s_03a_7
hide dee_p_02_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice blo_f0535
Blood "「……だそうだが、せっかくのパーティにわざわざオレンジ色の物体を陳列しても新鮮味がない。\n
むしろ、興醒めもいいところだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（確実に私よりもダメージを受けそうな人が目の前にいる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、エリオットはめげたりはしなかった。"


show eri_s_02_2 at center
hide bra_s_02_9
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0335
Elliot "「定番もいいと思うんだけどなあ。\n
新しいものを取り入れるってのも、悪くないと思うけどよ！」"

hide eri_s_02_2
show eri_s_02_2 at left
show dee_p_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0550
Dee "「それは僕達だって同じだよ、いいプレゼントだと思ったのになあ……。\n
大人って、よく分からないや」"

hide eri_s_02_2

hide dee_p_02_12
show dee_p_02_12 at left
show dam_p_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0551
Dam "「大人になると面倒が多いなんて、子供のほうが楽でいいよね」"

play sound se_0491
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "意見をまとめるように、ブラッドが手を叩いた。"


show bra_s_03_19 at center
hide dee_p_02_12
hide dam_p_02_12
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0536
Blood "「まあ、色々あったわけだが、エリオットと双子の意見をまとめるだけでも面倒でね。\n
主役である君に選んでもらうことにした」"

play sound se_0267
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（私が選ぶ？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「何を選ぶの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "肩に手を置かれ委ねられても、何のことだか分からない。"

hide bra_s_03_19
show bra_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0537
Blood "「プレゼントの基本はもらった相手が喜ぶものだろう。\n
だったら、君に聞いてしまったほうがいい」"

hide bra_s_03_10
show bra_s_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0538
Blood "「欲しがるものを用意するのは、少々面白味に欠けるとは思うがね。\n
サプライズも、何度も繰り返しては、楽しさが薄れてしまうだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

hide bra_s_03_9
show bra_s_03_9 at left
show eri_s_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice eri_f0336
Elliot "「なんでもいいぜ、あんたの欲しいものを言ってくれよ。\n
どんな難しいもんだって、絶対に持ってきてやるからさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「私の欲しいもの？」"

hide bra_s_03_9

hide eri_s_01_8
show eri_s_01_8 at left
show dee_p_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice dad_f0552
Dee "「ものじゃなくてもいいよ。\n
お姉さんが遊んでほしいなら、休暇を全部使ってもいいから」"

hide eri_s_01_8

hide dee_p_02_2
show dee_p_02_2 at left
show dam_p_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice dad_f0553
Dam "「うん、お金のかからないものに越したことはないけど。\n
お姉さんがお強請りしてくれるなら、僕達も頑張るよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「ディー、ダム……」"


show bra_s_01_11 at center
hide dee_p_02_2

hide dam_p_02_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_10")
voice blo_f0539
Blood "「今、この屋敷の中心は君だよ、[firstname]。\n
君のために動く者は、いくらでもいる。こいつらのようにな」"

hide bra_s_01_11
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドが私から視線を外して振り返れば、そこにはじっと聞き耳を立てている同僚達の顔。"


show situji_t_01_06 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0045
Servant "「ええ、気に入らない奴がいれば片付けてきますよ」"

hide situji_t_01_06
show situji_t_01_06 at left
show bousi_t_02_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0064
Maid "「私達だって、お祝いして差し上げたいんですもの～」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「……あなた達」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（気持ちは嬉しいけど……、そういう祝い方は、いらない）"

hide situji_t_01_06

hide bousi_t_02_02
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「……本当になんでもいいのね？」"


show bra_s_03_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice blo_f0540
Blood "「ふふっ、私は嘘もつくが、今はそういう気分じゃない。\n
叶えると言った以上、翻すつもりはないから安心して言ってくれていいぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

hide bra_s_03_15
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッド達だけではなく、周囲にいる同僚もじっと私を見つめてくる。\n
私がどんなことを言うのか、期待を込めた眼差しで。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（……願いなら、もう叶えてもらっているのに）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「なら、今度は私が皆を祝いたいわ」"


show eri_s_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice eri_f0337
Elliot "「へ？\n
あんたが俺達を祝うって……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「私だけ誕生日パーティをしてもらうんじゃ不公平だもの。\n
だから、今度は、私にも準備をさせてよ」"


show dee_p_02_4 at center
hide eri_s_01_5
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice dad_f0554
Dee "「ええっ、お姉さんが誕生日をお祝いしてくれるの！？\n
だったら、僕が一番最初にお祝いしてほしいよ！」"

hide dee_p_02_4
show dee_p_02_4 at left
with dis

show dam_p_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice dad_f0555
Dam "「あー、ずるいよ、兄弟。\n
僕じゃなくて、そういう場合は僕達だよ、僕達は双子なんだから」"


show eri_s_01_6 at center
hide dee_p_02_4
hide dam_p_02_6
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice eri_f0338
Elliot "「何を勝手なこと言ってやがる。\n
こういう場合は、トップが先って決まってんだよ！」"

hide eri_s_01_6
show eri_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice eri_f0339
Elliot "「ボスを差し置いて、おまえらが先に祝われるはずがねえだろうが。\n
おまえらなんか最後だ、最後！」"


show dee_p_02_6 at center
hide eri_s_02_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice dad_f0556
Dee "「それこそ横暴だよ！\n
子供なんだから、楽しいことは先に体験させてくれるのがいい大人ってものだろう！」"

hide dee_p_02_6
show dee_p_02_6 at left
show dam_p_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice dad_f0557
Dam "「ウサギの誕生日なんて一番最後でも上等すぎるよね」"

hide dee_p_02_6

hide dam_p_02_3

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "武器を持ち出さないというパーティのルールが効いているのか、三人は睨み合っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、さりげなく近くにあるフォークやナイフを手に構えているあたり、穏便に済ませるつもりはないらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（あれだって立派な凶器よね、使い方にもよるけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "なにしろ、遊園地の猫の愛用品だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（さすがに誕生日パーティのときまで流血沙汰は勘弁してほしいんだけどなあ）"


show bra_s_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice blo_f0541
Blood "「……欲のないお嬢さんだ。\n
もっとすごいものを強請ればいいのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "騒ぎを面白そうに眺めているブラッドに止める気はないらしい。\n
近くに置いてあったグラスに何かを注いで、私に差し出してくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「すごいもの、ねえ……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「それって……、たとえば、長すぎる休暇とか、高いお給料とか。\n
私よりも大きいにんじんケーキとか？」"

hide bra_s_02_2
show bra_s_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice blo_f0542
Blood "「……ふ。\n
そうだな、あとは、退屈しない時間帯などはいかがかな？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「いらないわ。\n
そんなものもらったところで、持て余すのが分かっているもの」"

hide bra_s_03_1


scene bg_gen_sky_aut_nig with Dissolve(2)
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（退屈なんてここにいる限り縁遠いし。\n
それに……、私が欲しいって言うつもりがないことぐらい、あなたにはお見通しでしょう）"

play sound se_0410
pause .5
play sound se_0410
pause .4
play sound se_0410
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice eri_f0340
Elliot "「クソガキ共が……。\n
祝いの席で暴れるんじゃねえ！」"

play sound se_0410
pause .3
play sound se_0410
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice dad_f0558
Dee "「パーティにウサギが紛れているほうが問題だよ。\n
ネズミほどじゃないけど、衛生的じゃない」"

play sound se_0410
pause .2
play sound se_0410
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice dad_f0559
Dam "「芸の一つも出来ないのに、動物がいるほうがおかしいよね」"

play sound se_0410
pause .1
play sound se_0410
pause .1
play sound se_0410
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice eri_f0341
Elliot "「俺はウサギじゃねえって言ってんだろうが！」"

play sound se_0410
pause .15
play sound se_0410
pause .15
play sound se_0410
pause .15
play sound se_0410
pause .15
play sound se_0410
pause .15
play sound se_0410
pause .15
play sound se_0410
pause .15
play sound se_0410
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "武器は持ちだしていないが、とうとう手を出し始めた三人の怒声と、金属音が響いてきた。\n
物騒な音に罵り合う声。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の場所で聞いたら、きっと聞かなかった振りをしてしまうそれらに、今は耳を傾ける。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_2")
T "（ああ、帰ってきた）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな感覚に笑ってしまう自分がいた。"


scene bg_gen08_bn_aut_nig_p with Dissolve(2)
show bra_s_03_18 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Blood "「…………」"

hide bra_s_03_18
show bra_s_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice blo_f0543
Blood "「……やれやれ。\n
結局騒ぎを起こさずにはいられないようだな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言い合いに混ざる金属音を聞きながら、ブラッドはだるそうに告げた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「そうみたいね。\n
……それで、ブラッド、私はまだ返事をもらっていないんだけど？」"

hide bra_s_01_3
show bra_s_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice blo_f0544
Blood "「返事とは、どういう意味かな？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_14")
T "「ここはあなたのお屋敷だもの、ちゃんと許可を取らないといけないでしょう。\n
今度は私に、皆をお祝いさせてくれる？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっ、と私から覗き込むと、相手はきょとんとした後に、口端をあげた。"


show t_end_bousi4 onlayer master
with dis
hide bra_s_01_10

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0545
Blood "「……まったく、本当に退屈しないお嬢さんだな。\n
マフィアの誕生日を祝いたいなんて言い出してくるのは、君ぐらいだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0546
Blood "「約束を違えないと言ったからね、君がそれを望むなら、したいようにすればいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「……ありがとう、ブラッド」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "感謝を込めて、受け取ったグラスを傾けるとブラッドも自分のグラスをあわせてきた。"

play sound se_0359
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "硝子の心地よい音が響く。"

hide t_end_bousi4


show bousi_t_01_08 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0058
Maid "「でしたら、私達のこともお祝いしてくれるんですか？」"

hide bousi_t_01_08
show bousi_t_01_08 at left
show situji_t_01_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0048
Servant "「そういうことですよね？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「そうね、全員終わるまでにどれだけかかるか分からないけど……」"

hide bousi_t_01_08
hide situji_t_01_05
show situji_t_01_05 at left
with dis
show situji_t_02_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice kat_f0046
Servant "「やった～。\n
それじゃあ、順番がくるまで元気にばりばり働きますね」"

hide situji_t_01_05
hide situji_t_02_06
show situji_t_02_06 at left
show bousi_t_02_07 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice may_f0065
Maid "「皆のお祝いのときには、私達もお手伝いしますから」"

hide situji_t_02_06
hide bousi_t_02_07
show bousi_t_02_07 at left
show dee_p_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0560
Dee "「駄目だよ！\n
皆は僕らの後だって言っているじゃないか」"

hide bousi_t_02_07

hide dee_p_02_6
show dee_p_02_6 at left
show dam_p_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0561
Dam "「そうだよ、そうだよ！\n
お姉さんが祝ってくれる誕生日は僕達が一番だよねっ」"


show eri_s_02_9 at center
hide dee_p_02_6
hide dam_p_02_6
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice eri_f0342
Elliot "「だから、おまえらなんて最後のほうだって」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつのまにか戻ってきた三人が、同僚を押しのけながら文句を言う。"


show bra_s_02_17 at center
hide eri_s_02_9
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0547
Blood "「……騒々しい、おまえ達はもう少し静かに出来ないのか？」"

hide bra_s_02_17
with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドが苦言を呈する光景も含めて、この屋敷に帰ってきたのだと思う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（そうよ、もらってばかりじゃ不公平だもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚かされて、苛立ったり、不安になったりもした。\n
色々な気持ちでぐらぐら揺れかけた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T "（でも、仕返しを、この人達は許してくれる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いいものも、悪いものも。\n
平等に返していきたい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_1")
T "（それが家族……、ファミリーっていうものじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一緒に過ごせば、毎日が誕生日。"



hide frame_gen_togaki
hide ali_t_06_16
with Dissolve(5)
scene black
with compress_extraextralong

$ renpy.movie_cutscene("endroll_b.mpg")
#return
