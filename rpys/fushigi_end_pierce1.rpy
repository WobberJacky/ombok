
scene map_bg_summer_day
with dis
label fushigi_end_pierce1:
$ clockanim()


scene map_bg_summer_day
with dis

scene charasel_bg_amuse_day
with dis

play music pierce_t_ali

scene s2_01 with Dissolve(1.2)

show pia_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Pierce "「[firstname]、[firstname]！」"

play sound se_0051
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ピアス、あなた、どこから……！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "間もなく遊園地に入るというところで、緑の小道から飛び出してきたピアスが抱きついてくる。"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きゅっと力を込めたピアスは、耳と尻尾を動かしながら私の顔を見上げてきた。"

hide pia_t_03_6
show pia_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0221
Pierce "「ぴ、だってだって、君が帰ってきてくれるって聞いたから。\n
俺、ずっと待っていたんだよ」"

hide pia_t_01_10
show pia_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0222
Pierce "「ここで待っていれば、誰よりも最初に君を迎えられるもんね、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「……ずっとって、まさか、私が帰るって約束してから、ずっと！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子に『最後にもう一回遊んでくれなきゃ、帰さない』と半ば引き摺られるように帽子屋屋敷に連れて行かれてから、既に五回は時間帯が変わっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（何だかんだと、あそこの人達って引き留めようとするわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気紛れな主はお茶会の席を整えて、「無駄にする気か？」と嘆いて見せ（勿論わざとだ）。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットはエリオットで、大量のにんじん料理で「ここにいればいつでも食わせてやるのに」と神妙な顔で告げ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気が付けば時間帯が変わっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（もっとも、一番付き合ったのはあの子達だけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスの前で遊んでいたトランポリンだけでなく、鬼ごっこ、隠れんぼといった定番の遊び。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それに加えて、手榴弾を使ったキャッチボールやら、ナイフを使ってのお手玉。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（あれって、ひょっとして……。\n
あの子達なりの仕返しだったのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らがピアスにいつもにも増してきつく当たったのは、私のことを思ってのこと。\n
それが伝わってきていたので、無碍にも出来なかった。"

hide pia_t_01_6
show pia_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0223
Pierce "「うん、そうだよ。\n
あそこでね、じっとして君が帰ってくるのを待っていたんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスが指差しているのは、森の奥。\n
木が生い茂っていてよく見えないが、少なくとも屋外には変わりない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（あんなところで、一人でじっとしていたの……？）"

hide pia_t_02_11
show pia_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice pie_f0224
Pierce "「不思議だね、[firstname]。\n
君が遊園地から出て行ったときには、俺、寂しくて泣きそうだったんだよ」"

hide pia_t_01_12
show pia_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice pie_f0225
Pierce "「でもね、でもね。\n
君が帰って来てくれると思ったら、全然寂しくなかった」"

hide pia_t_03_4
show pia_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice pie_f0226
Pierce "「ううん、それどころか、わくわくしたんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「わくわく？」"

hide pia_t_03_5
show pia_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pie_f0227
Pierce "「お仕事でもね、こういう気分になるときがあるんだけど……。\n
それとはちょっと違ったんだ」"

play sound se_0624
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言いながら、ピアスは私の手を引いて遊園地へと歩き出す。\n
徐々に近付いていく賑やかな音楽と、人の気配。"

play sound se_0755 volume .3
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の領地にはない、ざわついた雑多な雰囲気が遠くからも感じられる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（私が好きな場所）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのとき、ピアスの様子を見に行くという名目で来たときにも、同じ気持ちになった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、こうやって帰ってきて、やはりここが自分の場所だと強く感じる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「仕事とは……、どう違ったの？」"

hide pia_t_01_11
show pia_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice pie_f0228
Pierce "「だって、全然怖くなかったから！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（怖くなかった？）"

hide pia_t_02_3
show pia_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pie_f0229
Pierce "「お仕事のときには、どこから誰が出てくるか分からない中で、じっとしていなくちゃいけないでしょう。\n
騒ぐとエリーちゃん達にも怒られるし」"

hide pia_t_01_13
show pia_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pie_f0230
Pierce "「だからって、逃げ出したらもっと怒られるし……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「それはそうでしょうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくら真っ正面からの遊撃人員ではないとはいえ、敵前逃亡などマフィアには許されないことだろう。"

hide pia_t_03_13
show pia_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0231
Pierce "「そうなんだ。\n
でも、今回は君を待っていても、全然怖くなかったよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「……ピアス」"

hide pia_t_03_10
show pia_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice pie_f0232
Pierce "「だって、いつもならお仕事の後、俺に『お帰りなさい』って言ってくれる君に。\n
今回は、俺が『お帰り』って言えるんだもん！」"

play sound se_0551 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きゅっと繋いだ手が引き寄せられる。\n
地面に押し倒してきたときと同じ、柔らかな眼が私を映しこむ。"

hide pia_t_01_2
show pia_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0233
Pierce "「遅くなっちゃったけど……。\n
[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「？」"

hide pia_t_01_12
show pia_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice pie_f0234
Pierce "「お帰りなさい！\n
ちゅうしてあげるっ」"

hide pia_t_03_5


show t_pia_end1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "掠めるように柔らかく唇を触れ合わせてきたピアスは、そのままぺたぺたと私に触ってくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ピ、ピアス……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice pie_f0235
Pierce "「もっとちゅうしたいなあ、ずっとずっと君とちゅうしていたいなあ。\n
君って、ちゅうすると更に可愛いくなるんだもん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice pie_f0236
Pierce "「俺だけがちゅうして、君を一番可愛く出来たらいいのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（可愛いのは、どっちよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "血にも、硝煙にも染まることが珍しくない眠りネズミ。\n
だというのに、どうして私を見る顔はそんなにも可愛いのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（……ずるいわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "可愛いからといって、何でも許されるほど世の中は甘くない。\n
それは捻くれた性格をしている私にとっては、常識のはずだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（怒って出てきたはずなのに、もう許しちゃっている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悪意のない全力の行動は、疑う余地がない。"

hide t_pia_end1

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「そういえば、ピアス。\n
ゴーランドは新しいアトラクションを何か思いついたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この前遊園地に来たときには、特に目新しいものはなかったように思う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もっともここの敷地は冗談のように広いので、私が見落としていた可能性もあるのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（それに、あのときはピアスを探すのに必死だったし）"


show pia_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice pie_f0237
Pierce "「ぴ？\n
新しいアトラクションって……、そんなのあったの？」"

hide pia_t_02_9
show pia_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice pie_f0238
Pierce "「俺、君のところに行ってばっかりだったから気付かなかったけど……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「そう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（まあ、そんなことだろうと思ったわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結局新しい企画は決まったのだろうか。\n
思いついたら即実行のゴーランドのことだ、名案と判断されれば実行に移していると思う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（そういえば、ピアスも何か考えたのかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのときにはチーズの滑り台という提案だったはずだ。\n
他に思いついてもまたいつものようにチーズの方向に走る可能性もある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の手を掴んでいるピアスの顔を見ながら、そんなことを考えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（ピアスの案を聞いてあげようかな。
それとも、私の企画をゴーランドに持ち込もうかな……）"
$ hi_mes()
show charasel_headline_gen:
    xalign .5
    yalign -.05
show screen pierce_zoo_choice
$ ui.interact()

label fushigi_end_pierce2:
hide charasel_headline_gen
hide screen pierce_zoo_choice
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（聞いても、どうせまたチーズ関連が出てきそうよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも自分から喧嘩を蒸し返すようで、不毛な気がする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋屋敷にいる間に書き込んだ資料は、荷物の中に入っているから、後でゴーランドのところに持っていって相談したほうが賢明だろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドも私に甘い人だが、遊園地に相応しくないと判断すれば、すぐさま却下といってくれるはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（甘やかさずに、従業員としても扱ってくれる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この場所の一員と認められていることは、私にとっても嬉しい。"

hide pia_t_01_13
show pia_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0239
Pierce "「ねえねえ、[firstname]。\n
何を先刻からぶつぶつ言っているの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ。\n
ごめんなさい、つい考えごとをしていたわ」"

hide pia_t_01_10
show pia_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pie_f0240
Pierce "「難しいこと？\n
俺じゃ分からないようなことを考えていたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "歩みを止めたピアスに覗き込まれて、首を振る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……ううん。\n
ピアスがいるから考えていたのよ」"

hide pia_t_03_8
show pia_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Pierce "「？？？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_2")
T "「そうね。\n
後でまた教えてあげるから、楽しみにしていて」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（ゴーランドがいいって言えばの話だけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この企画なら、ピアスにとってそう悪いものではないだろう。"

hide pia_t_03_1
show pia_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0241
Pierce "「うん、分かったよ。\n
君が教えてくれるっていうなら、俺、いい子で待っている」"

hide pia_t_01_2
show pia_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0242
Pierce "「俺、いいネズミだからね、[firstname]」"

play sound se_0361
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きゅっと握り込んでくる手に力が入る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_8")
T "（温かい）"

play sound se_0624
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "再び歩き出したピアスについていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのとき、地面に縫い止めてきた手と同じ手だというのに。\n
それでも、私に触れようとするピアスの手にいつでも絆されてしまう。"

hide pia_t_02_7

$ hi_mes()

scene yum_sum_01_1
with stripe_l_medium

scene go_01
with stripe_l_long

play music gowland_t_ali

show go_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0380
Gowland "「ああ、話していたアトラクション？\n
あれなら、全然だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（全然っていうことは……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この場合は「全然進んでいない」ととるべきか、あるいは「作ったものの、全然客が来ない」ととるべきか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、ゴーランドのしょんぼりとした顔を見ている限りでは、前者だろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（作ったけど、お客さんが来ないっていうなら、もっと目の色を変えていそうだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問題点を見つけ出し、その上で改良なのか改悪なのか分からないような処理を施す、それがこのオーナーの性格だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「私がここを離れている間にもう大分決まったとばかり思っていたんだけど……？」"

hide go_t_02_10
show go_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice gor_f0381
Gowland "「うちの連中にも色々と話を聞いたし、客にもアンケートを採ったりしたんだけどなあ。\n
どうもこう、あまりぱっとしねえ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………。\n
具体的には？」"

hide go_t_03_2
show go_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
Gowland "「…………」"

play sound se_0470
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぺらっと。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "無言のまま、机の引き出しから薄い紙を取り出し、ゴーランドは私に向かって差し出してくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうやら彼の言ったアンケート用紙らしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "『今のままでも充分楽しんでいます』 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "『新しいものを作るより、今あるものをパワーアップさせてください』 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "『これ以上作ったら、遊びきれません』 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "等々。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（現状維持思考のお客さんが多かったのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうりでゴーランドの勢いが弱いわけだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "単に案が出ないというだけで彼がここまで落ち込むことはないと思っていたが、その勘は外れていなかったらしい。"

hide go_t_02_2
show go_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0382
Gowland "「まったく、最近の若い奴は張り合いがねえっていうか。\n
もっと、こう……、ときめくような展開をだな！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「でも、オーナーとしてはアンケートを完全無視にも出来ないわよね？」"

hide go_t_03_7
show go_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gor_f0383
Gowland "「それを言われると……、俺も、弱い」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "アンケートを採る以上は、その意見を反映しなければならない。\n
単なる市場調査とはわけが違う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地も利益がゼロでは困るが、それ以前に楽しんでもらいたいというのがゴーランドの趣旨のはずだ。"

hide go_t_03_11
show go_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0384
Gowland "「うちの遊園地を気に入ってくれているのはいいんだけどよ。\n
なんつーか、違ったものも取り入れてみたいと思うんだが」"

hide go_t_01_6
show go_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0385
Gowland "「何か、いい案はねえかなあ……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「じゃあ、ちょうどよかったわ」"

play sound se_0471
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "机に肘をついて項垂れているゴーランドに、帽子屋屋敷で作っていた資料を差し出す。"

hide go_t_03_12
show go_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、ゴーランドはそれが何か咄嗟には分からなかったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きょとんとした顔で紙面に目を通していくうちに、今まで冴えなかった顔にみるみる熱意が戻る。"

hide go_t_01_11
show go_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0386
Gowland "「[firstname]、あんたこれ……。\n
か、考えてきてくれていたのか！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「といっても、私も新しいアトラクションが思いつかなかったから、別の方向にしちゃったんだけどね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（こういうのも怪我の功名っていうのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の声が聞こえているのかいないのか。\n
ゴーランドは真剣な顔で書類を読んでいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまでのだれた態度とは違う、真剣な表情だ。"

hide go_t_03_13
show go_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「何？\n
あくまで提案の一つとして考えたものだし使えないようだったら、あっさり蹴ってもらっても構わないんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までも遊園地の企画に関わったことはあるが、ここでは私はサポートする立場の人間だ。\n
出すぎた真似をするつもりはなかった。"

play sound se_0395
camera at hpunch
camera at vpunch
hide go_t_02_13
show go_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0387
Gowland "「違う、逆だ、逆！\n
いいじゃねえか、こういうの！」"

play sound se_0198
##special anime kirakira_center
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ばしっとテーブルの上に手をついて立ち上がったゴーランドの目は、きらきらと輝いていた。"

hide go_t_03_5
show go_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0388
Gowland "「これなら、ちょうどいい。\n
大量に持ち込まれたあれも処分出来て、一石二鳥だ！！」"

hide go_t_01_2
show go_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0389
Gowland "「これで行くぞ、これで！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え……、いいの、そんなあっさりと」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "即決してしまったらしい企画書をもう一度見返していた私が聞いても、ゴーランドの決意は変わらない。"

hide go_t_03_4
show go_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0390
Gowland "「オーナー権限だ。\n
俺がいいと言えば、それでいい！」"

hide go_t_01_3
show go_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0391
Gowland "「ようは客が満足して帰って行ければ、それに越したことはねえんだからな」"

hide go_t_01_4
show go_t_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0392
Gowland "「あんたのこれは、そういう意味では問題なく楽しめそうだ。\n
ありがとう、[firstname]」"

play sound se_0492
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "信頼と感謝の証のように握手を向けられる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_2")
T "「ええ。\n
こちらこそ、使ってもらえて嬉しいわ、ゴーランド」"

play sound se_0361
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "差し出された手を握り返す。\n
友人として、雇い主として。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（この人がいる場所にいられて、よかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の居場所を与えてくれることに、心から感謝を込めた。"

hide go_t_03_14

$ hi_mes()

scene yum_sum_01_1
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_medium

scene map_bg_summer_night
with stripe_l_medium

scene map_bg_summer_eve
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_medium

scene yum_sum_01_1
with stripe_l_long
play sound se_0557

play music map_summer_jok

scene bg_gen_sky_sum_day
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice suz_f0006
Customer "「何だ、この人だかりは……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice mat_f0015
Customer "「何か催し物をやるみたいだけど……。\n
何でも、自由参加ですって」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice sat_f0005
Customer "「おい、見ろよ。\n
役持ちがあんなに……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地の一大イベントということで、この時間帯にはいつもにも増して、来場者が多いようだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（企画の発案者としては嬉しい限りだけど……、あそこにいるのは？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どんなに大勢の客がいても埋没しない、豪奢な存在感。\n
見慣れた顔が見えたので近づいた。"


scene yum_sum_01_1
with dis

show viv_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0407
Vivaldi "「……ええい、鬱陶しい。\n
どうしてわらわがこのような埃の多い場に来なければならぬのだっ」"

hide viv_t_03_9
show viv_t_01_8 at left
show king_t_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0011
King "「ビバルディ、落ち着け。\n
ルールなら仕方ないと自分でも言っていただろう？」"

hide viv_t_01_8
show viv_t_01_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0408
Vivaldi "「気に入らぬ……。\n
何よりも気に入らぬのは、あのウサギや騎士を呼び出すのではなく、わらわを名指しとは……」"

hide viv_t_01_9
show viv_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0409
Vivaldi "「説明してもらおうではないか、ゴーランド」"

hide viv_t_02_6

hide king_t_01_01
show king_t_01_01 at left
show go_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0393
Gowland "「ははは、そう目くじら立てんなよ、女王様。\n
……せっかくの化粧が崩れるぜ？」"

hide king_t_01_01

hide go_t_01_8
show go_t_01_8 at left

show viv_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

##special anime kaminari
hide viv_t_02_12
show viv_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0410
Vivaldi "「わらわと争いたいと言うのなら、その首に未練はないということであろうな？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……とても、催し物とは思えない空気）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "びりびり。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地の入り口をくぐったところにある広場。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこで寒々しい空気を漂わせている女王とオーナーを見ていると、背後から服を引っ張られた。"


show pia_t_02_10 at center
hide go_t_01_8
hide viv_t_01_13
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0243
Pierce "「[firstname]、どうしたの？\n
どうして遊園地に女王様達がいるの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の陰にこそこそと隠れながら、ピアスは小さな声でそんなことを言う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「知らないわよ、ゴーランドが観客を呼んでやるって言っていたから何かするつもりだとは思っていたけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の企画書を元に自分流にアレンジしたゴーランドは、あっという間にイベントの準備を進めると、何人かの役持ちに招待状を送り付けたらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（そのうち、あの人は私が率先して呼びたいって言ったけど）"

hide pia_t_02_10
show pia_t_02_10 at left
show bra_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice blo_f0330
Blood "「……だるい、眩しい、騒がしい、面倒だ」"

hide pia_t_02_10
show pia_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice pie_f0244
Pierce "「あ、ボス！\n
ボスが昼に遊園地に来るなんて、すっごく珍しいね、どうしたの、どうしたの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T "（噂をすれば何とやら……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "明らかに呼び出されたことが不満と顔に書いたブラッドが、私達の横に立っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相変わらず、彼らは気配を断つことに長けている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「いらっしゃい、ブラッド。\n
この前お世話になったお礼に、招待させてもらったのよ」"

hide bra_t_01_13
show bra_t_03_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice blo_f0331
Blood "「……君も、あの性悪オーナーに似てきたな。\n
よりにもよって、昼にこの私をこんな場所に呼び付けるとは」"

hide bra_t_03_6
show bra_t_02_18 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice blo_f0332
Blood "「君の連名で、更に言えば、ルールでなければこんなところまで来なかったよ。\n
はあ……、終わったらすぐに帰らせてもらうぞ」"

hide pia_t_01_3
show pia_t_01_10 at center
hide bra_t_02_18
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice pie_f0245
Pierce "「催し物って……、何かやるの、[firstname]？\n
俺、何も知らないんだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_4")
T "「そうでしょうね、ピアスには内緒にしていたし」"

play sound se_0042
hide pia_t_01_10
show pia_t_02_10 at center
with dis

show gaaan1 with Dissolve(.1)
hide gaaan1
show gaaan2 with Dissolve(.1)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice pie_f0246
Pierce "「え……、ええ！？\n
どうして、どうして！？」"

hide gaaan2 with dis

hide pia_t_02_10
show pia_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice pie_f0247
Pierce "「君まで俺を除け者にするの、[firstname]！？\n
そんなの酷いよ……、くすんくすん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あっさりと答えた私の言葉に、ピアスはわかりやすく落ち込んだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「除け者にしたんじゃなくて……。\n
あなたにも楽しんでもらおうと思って、内緒にしていたの」"

hide pia_t_01_4
show pia_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Pierce "「？？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ショックを受けた表情を浮かべるピアスに、もう少しで分かると告げておく。"


show bor_t_02_8 at center
with dis
hide pia_t_03_8
with dis


$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0324
Boris "「やーっと見つけたぜ、ピアス。\n
おまえ、こんなところで油を売ってないで、とっとと受付に行って来いよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "「受付はこちら」と書かれた立て看板を持ったボリスが、不満げに現れてそんなことを言う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ボリス、お疲れ様」"

hide bor_t_02_8
show bor_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice bor_f0325
Boris "「……ほんと、これって貧乏くじだよね。\n
何で俺がこんな手伝いなんかしているんだろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "立て看板を渡されて逃げだそうとしたボリスに「また家出していい？」と圧力をかけた本人としては、労っておくのが筋だろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「あら、ぴったりじゃない。\n
エントリーが少なかった場合に、選手を引っ張ってくるのも大事な役割だもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地は広いのだ、受付に着く前に諦めてしまう人もいるかもしれない。\n
その点、好きな場所に繋げられるボリスが案内係なら、もってこいだ。"

hide bor_t_01_12
show bor_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「…………」"

hide bor_t_03_11
show bor_t_03_11 at left
show bra_t_02_17 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0333
Blood "「本当に、商魂逞しいお嬢さんだ。\n
ピアスにもその逞しさを分けてもらいたいぐらいだよ……ああ、だるい」"

play sound se_0624
hide bor_t_03_11
show bor_t_03_11 at center
hide bra_t_02_17
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぶつぶつと文句を言いながら、ブラッドは人波の中へと姿を消していく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "騒がしいところが嫌いな彼だが、正式な招待である以上、催し物が終わるまでは帰らないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（ありがとう、ブラッド）"

hide bor_t_03_11
show bor_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice bor_f0326
Boris "「ほら、行くぞ、ピアス。\n
いつまでもべたべたしてないで、とっとと受付すませて、控え室に行っていろよ」"

hide bor_t_03_9
show bor_t_03_9 at left
show pia_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice pie_f0248
Pierce "「え……、嫌だよ。\n
だって、そんなことしたら、この子と離れなくちゃいけなくなるもんっ」"

hide pia_t_01_1
show pia_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice pie_f0249
Pierce "「せっかく、俺のところに帰ってきたのに……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大きな目に涙を溜めているピアスは今にも泣き出しそうだが、ボリスが叫ぶほうが先だった。"

hide bor_t_03_9
show bor_t_01_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0327
Boris "「ああ、うざったいなあ。\n
いいから、とっとと行け！！これ以上ごねると、参加の前に俺が食うぞっ」"

hide pia_t_02_10
show pia_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Pierce "「！！！」"

play sound se_0131
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスに首根っこを掴まれて、バタバタと暴れながら、ピアスが声をかけてくる。"

hide pia_t_01_3
show pia_t_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0250
Pierce "「あ、待って、だったら君も行こうよ、[firstname]！\n
ね、それだったら、俺も安心して行けるからっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（そういうわけにはいかないのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この後待ち構えている事態を想像すると、私如きでは混じることは出来ない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ピアス」"

hide pia_t_02_5
show pia_t_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Pierce "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_2")
T "{size=+20}「頑張ってきてね～」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手をぱたぱたと振ると、一瞬期待した顔が再び項垂れた。"

hide bor_t_01_8
show bor_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0328
Boris "「まったく、ネズミのくせに猫の手を借りるってどういうことだよ。\n
おまえ、いつからそんなに忙しくなったわけ？」"

play sound se_0365
hide bor_t_01_3

hide pia_t_01_2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ずるずるずるずる。\n
文字通り引き摺られていくピアスを見送る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（さて、そろそろ始まるわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、くるりと振り返ると、そこでは。"


show viv_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0411
Vivaldi "「だいたい、観客が欲しいのなら、最初からキングを呼び付ければよかったのじゃ」"

hide viv_t_03_7
show viv_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0411_5
Vivaldi "「こんなところにくるほどわらわは暇ではない」"

hide viv_t_03_9
show viv_t_03_9 at left
show king_t_02_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0012
King "「わしには招待状がなかったのなら……、何故わしを？」"

hide viv_t_03_9
show viv_t_01_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0412
Vivaldi "「……決まっておろう、わらわを一人でこんな場所に呼び付けるなど、納得がいかぬ。\n
付き合え」"

hide king_t_02_04
show king_t_02_08 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0013
King "「いや、それだったら、メイドや兵士を伴ったほうが……」"

hide viv_t_01_9
show viv_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0413
Vivaldi "「いいから、おまえは黙ってついてくればよいのだ！\n
それ以上つべこべ申すのなら、首を刎ねるぞ！」"

hide king_t_02_08
show king_t_01_07 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
King "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（あれで意外とうまくいっているのよね……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディが一方的に八つ当たりをしているのだが、キングの首を刎ねたりすることはないので大丈夫はなずだ。"

hide viv_t_02_6

hide king_t_01_07

play sound se_0624
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こちらには気付いていないようだったので、主催であるゴーランドを探す。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（あれ？\n
いつの間にかゴーランドがいない）"


scene bg_gen_sky_sum_day
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0394
Gowland "「あー、マイクテスト、マイクテスト」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（？\n
園内放送？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段は遊園地内のアトラクションに合わせた音楽が流れている近くの拡声器から、オーナーの声が聞こえてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "園内で一斉放送をかけるなんて、珍しい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0395
Gowland "「よし、大丈夫そうだな。\n
それでは、これより、遊園地一大イベント……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0396
Gowland "{size=+20}「チーズころころ祭を開催する！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0397
Gowland "「出場を希望する奴は、まだ余裕があるから、観覧車下の受付まで来るように……って、おい！\n
ピアス、何暴れて……」"

play sound se_0052
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0251
Pierce "「チーズ、チーズどこ！？\n
どこに俺のチーズがあるのっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0329
Boris "「だから、おまえのじゃねえって……。\n
ほら、こんなところに逃げ込むんじゃ……」"

play sound se_0638
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「～～っ、い、一体何をしているのよ、あの人達は」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きんと耳障りな音を立てているマイクに、顔を顰めながら私も移動を始めた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "会場は遊園地の広い土地の一部を開拓した、小さな丘だ。"

$ hi_mes()

scene bg_gen16_yusk
with stripe_l_long
play sound se_0557

play music amuse_inside_p_ali

show go_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0398
Gowland "「おお、ずいぶん集まったなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「そうね、大盛況」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "丘の上には予想以上の人が集まっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_6")
T "（思っていた以上に大がかりなイベントになったけど、盛り上がっているなら嬉しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私とゴーランドがいるのは、丘の向かい側に立てられた司会の席。\n
集まった人がよく見える、最高の場所だ。"


show pia_t_02_6 at center
hide go_t_02_12
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0252
Pierce "「ぴいい、高いよ、すごい坂だよ。\n
こんなところで一体何をさせる気なの、[firstname]！」"

hide pia_t_02_6
show pia_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0253
Pierce "「助けてよ、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちょろちょろと人の間を動き回っているピアスが私のほうを見て、必死にＳＯＳを送ってくる。\n
しかし。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_1")
T "「心配しなくても、下にはたくさん緩衝材を置いておいてあげたから、大丈夫よ。\n
安心して転がってちょうだい」"

hide pia_t_01_8
show pia_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_1")
voice pie_f0254
Pierce "「ぴっ！\n
君、まだ怒っているの？」"

hide pia_t_03_3
show pia_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_1")
voice pie_f0255
Pierce "「俺、俺……、君をそんなに怒らせるようなことをしたの！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（怒ってはいないんだけどなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不安げな顔を見ていると、ちょっと可哀想な気もしてくるが、祭が始まればピアスのことだ、目の色を変えるに違いない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（転がるチーズを追いかけるお祭りなんて、ピアスのためにあるような祭だもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が遊園地を出たときに、ピアスが持ち込んだ大量のチーズを、順番に坂に転がし一番多くのチーズを拾ったものが勝ちという祭だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T "（どこかの地方にもあるらしいけど……、何しろあれだけのチーズだもの。\n
せっかくだから１個と言わず、大量放出しちゃったほうがいいわよね）"

hide pia_t_01_4


show man_c1_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice suz_f0007
Customer "「結構な高さだな」"



hide man_c1_3
show man_c1_3 at left
show woman_a_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice mat_f0016
Customer "「あなた、頑張ってね」"

hide man_c1_3
hide woman_a_2
show woman_b_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice chi_f0050
Customer "「怪我をしないように」"

hide woman_b_2
show woman_b_2 at left
show man_d1_2 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice sat_f0006
Customer "「ああ、頑張るよ」"

hide woman_b_2

hide man_d1_2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "祭のルールは既に受付時に知らされている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "観客席にいるもの、丘の上で待機するもの。\n
あちこちから声が飛び交っていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（……あれ？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_16")
T "（丘の上にいる、あの髭の男の人って）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見慣れた顔に思わず視線が向かうと、観客席にいた赤い女性が声を上げた。"


show viv_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0414
Vivaldi "「……キング。\n
くだらぬ催し物とはいえ、負けたらどうなるか、分かっておろうな」"

hide viv_t_01_4
show viv_t_01_4 at left
show king_t_02_08 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kin_f0014
King "「なんで、わしが……。\n
こういうのは、エースやホワイトのほうがまだ」"

hide viv_t_01_4
show viv_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0415
Vivaldi "「ふん。\n
わらわの顔に泥を塗るでないぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（可哀想に）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声には出さない分、胸の中で手を合わせておくことにする。"


show yuuen_man_02_03 at center
hide viv_t_03_2
hide king_t_02_08
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0036
Employee "「オーナー、受付完了です！\n
選手は全員、移動しました」"

hide yuuen_man_02_03
show yuuen_man_02_03 at left
show go_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0399
Gowland "「よし、それじゃあそろそろ始めるか」"

play sound se_0491
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "周囲の状況を見ていたゴーランドは大きく手を打つと、声を張り上げた。"

hide go_t_02_12
show go_t_03_4 at center
with dis
hide yuuen_man_02_03

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0400
Gowland "「じゃあ、始めるぜ！\n
ルールは知っての通りだ」"

hide go_t_03_4
show go_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0401
Gowland "「細かいことはさておき、一番チーズを拾った奴の勝ち。\n
優勝した奴には……、これだ！」"

play sound se_0239
$ flash(.3)
hide go_t_02_8
show go_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0402
Gowland "{size=+20}「遊園地の完全フリーパスポート、ペアでどんっと贈ってやる！！」{/size} "

play sound se_0387
hide go_t_03_5
show go_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0403
Gowland "「優勝目指して、頑張ってくれ！\n
用意……」"

play sound se_0502
$ flash(.2)

play music cheerful_a_ali

show yuuen_woman_01_03 at center
hide go_t_01_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0050
Employee "「行きますよーっ」"

hide yuuen_woman_01_03
show yuuen_woman_01_03 at left
show yuuen_man_02_03 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0037
Employee "「それえええっ！！」"

hide yuuen_woman_01_03

hide yuuen_man_02_03

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "合図と共に控えていた従業員が、一気にチーズを坂に転がしていく。"

play sound se_0356
pause .5
play sound se_0356

scene bg_gen_sky_sum_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「……スターターピストルに使うような銃じゃないと思うんだけど、それ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice gor_f0404
Gowland "「ははは、何事も景気づけって大事だからよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の銃を空に向かって撃ったゴーランドはそう言って笑った。\n
そうこうしている合間にも、坂道を参加者達は落ちるように走っていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（あれ、本当にすっころんで落ちているような……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice suz_f0008
Customer "「ぎゃあああ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice sat_f0007
Customer "「うわ、こっちに来るなっ。\n
巻き込むんじゃ……、うわわわわわっ」"

play sound se_0553
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（やっぱり医者の手配をしておいて正解だったわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "坂の下には救助班が待ち構えていて、怪我人を収容する手はずになっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "……すると。"

play sound se_0356
pause .5
play sound se_0356

show t_pia_end2and4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0256
Pierce "「チーズ、チーズ！！\n
うわー、すごい、おいしそう、こっちもあっちもおいしそう！！」"

play sound se_0356
pause .5
play sound se_0356
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一人、明らかに幸せそうに飛び回りながらチーズを回収しているピアスが見える。"

play sound se_0356
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0257
Pierce "「[firstname]、[firstname]！\n
これ、皆拾っちゃっていいの、食べていい、食べていい！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「食べるのは後にしなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は次々と脱落者が出る中、異様な速度を誇っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの様子なら食べられなくはないと思うが、食べてしまったら数が数えられなくなってしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……？」"

play sound se_0356
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0482
Dee "「まったく、馬鹿なネズミだよね。\n
本当にチーズしか見えていないんだから」"

play sound se_0356
pause .5
play sound se_0356
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0483
Dam "「僕達のほうが、ずっと賢く拾えるよね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（い、今の声は……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そういえば、ハートの城の代表としてはキングが参加していたが、ブラッドが参加していた様子はない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "催し物には、参加することがルールだ。\n
そして、一緒に来ている場合、エリオットがブラッドの傍を離れることはない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つまり、彼は別の仕事でこの場所に来ていないことになる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ということは……、帽子屋領から出ているのは。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「ディー、ダム」"

hide t_pia_end2and4
show t_pia_end3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "台の下を覗き込んでみれば、次々と転落していく参加者を余所に、悠々とチーズを拾う双子の姿があった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（だから先刻、ブラッドは一人だったのね……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさか、彼らが参加しているなんて思わなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0484
Dee "「あ、お姉さん！\n
見て見て、大人の姿だとね、身体が大きいからこんなに拾えるんだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0486
Dam "「うん。\n
チーズや優勝賞品はどうでもいいけど……、売れば少しはお金になりそう」"

hide t_pia_end3

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼ら自身も言うように、長い手足を最大限に活かしてチーズを拾っていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一方、チーズしか見えていないピアスは急勾配の坂で、チーズが出てくるのを目で追っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「あれじゃあ……、効率、悪いわよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、言ったところでピアスには聞こえないような気がする。"


show t_pia_end2and4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0258
Pierce "「チーズ、チーズ。\n
俺のチーズがこんなにたくさん！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_6")
T "（ま、いいか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子の存在を知らないせいか、チーズの魅力に取り憑かれているのか。\n
今のピアスはいつもにも増してにこにこと楽しそうに走り回っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本人が楽しいのなら、それでいい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（元々、半分はピアスが楽しめるように考えたものだしね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼との仲直りを狙ったわけではないが、あの可愛らしい笑顔を見ていると、細かいことなど気にするだけ野暮というもの。"



hide t_pia_end2and4

$ hi_mes()

$ time_effect()
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして……、祭は終わった。\n
大量のチーズは丘を黄色く染めている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……ちなみに、取りこぼしたチーズはどうするの？」"


show yuuen_man_01_04 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice tan_f0038
Employee "「これから、チーズフォンデュとピザに回しますっ。\n
参加賞だそうです！」"

hide yuuen_man_01_04
show yuuen_man_01_04 at left
show yuuen_woman_01_02 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice may_f0051
Employee "「これだけの人数がいれば、さすがに食べきれますよ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「……無事な人がそんなにいたかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "かなりの人数が病院送りになっている。\n
具体的な数字を聞くと目眩がしそうだから、聞いていないが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（……最初の予定よりも、大分坂の角度を変えていたものね、ゴーランド）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あれで怪我人が出ないはずがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（見間違えでなければ、キングも運ばれていた気がしたけど……。\n
確かめるのが怖いからやめておこう）"

hide yuuen_man_01_04

hide yuuen_woman_01_02
show yuuen_woman_01_02 at left
show go_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice gor_f0405
Gowland "「お、こんなところにいたのか、[firstname]。\n
今、やっとチーズの集計が終わってよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「お疲れ様。\n
……それで、結果は？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの様子では入賞出来そうなのは、双子かピアスといったところだろうが、どちらが勝ったんだろう。"

play sound se_0052
camera at hpunch
camera at vpunch
hide go_t_02_12
show go_t_03_3 at center
hide yuuen_woman_01_02
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「！！？」"

hide go_t_03_3
show go_t_03_3 at left
show dee_s_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0487
Dee "「僕達が勝ったに決まっているじゃない、お姉さん！\n
あんな馬鹿ネズミに負けるはずがないよ」"

play sound se_0051
camera at hpunch
camera at vpunch
hide go_t_03_3
show go_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「！」"

hide go_t_02_4

hide dee_s_01_6
show dee_s_01_6 at left
show dam_s_01_2 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0488
Dam "「そうだよ。\n
くだらないお祭りだけど、あんなのに負けていられない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドと私の間に割って入った双子は、得意げに告げる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「その代わり、全身チーズの匂いね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "転がしていたのは、衝撃にも強い固いチーズだったが、その分匂いもしっかりとついている。"

play sound se_0624 volume .6

show pia_t_01_4 at center
hide dee_s_01_6
hide dam_s_01_2
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0259
Pierce "「ううう、ずるいよ、二人とも。\n
二人がかりで一位と二位を取るなんて……、俺だって、こんなに頑張ったのに！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「ピアス」"

hide pia_t_01_4
show pia_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice pie_f0260
Pierce "「……くすん。\n
俺、チーズのことじゃ誰にも負けないと思っていたのに」"

play sound se_0622 volume .4
pause .5
play sound se_0622 volume .4
pause .2
play sound se_0622 volume .4
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "両手に持ったチーズをぼとぼとと落としながら、ピアスは泣いている。\n
どうやら悔し泣きらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……先刻まではあんなに楽しそうだったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "動物の機嫌はよく分からない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ピアスは何位だったの？」"

hide pia_t_02_11
show pia_t_02_11 at left
show go_t_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0406
Gowland "「三位だよ、三位。\n
というか、二桁拾ったのはこいつらだけだ」"

hide go_t_03_1
show go_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0407
Gowland "「あとは持っていても、一個か二個ってところで……」"

hide pia_t_02_11
show pia_t_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pie_f0261
Pierce "「俺、今回は一番だと思ったのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（賞品がもらえるのは、一位だけだっけ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子のことだから、恐らくペアチケットを二人で一枚ずつということにしたのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つまり、何ももらっていないのはピアスだけだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「なら、入賞賞品をあげないと、不公平よね」"

play sound se_0551
show t_pia_end5 onlayer master
with dis
hide pia_t_01_13

hide go_t_02_10
with dis

play music happy_a_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice pie_f0262
Pierce "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頬に手を伸ばすと、ピアスは大きな瞳でこちらを見つめてくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0489
Dee "「あ……、お姉さん。\n
ちょっと待って」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0490
Dam "「どうせするのなら、優勝した僕達に……」"

play sound se_0051
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0408
Gowland "「……おまえらはもらうものはもらっただろ、これは駄目だ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "傍に寄ってこようとする双子を、ゴーランドが首根っこを捕まえて止めた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「ん」"

hide t_pia_end5
show t_pia_end6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
Pierce "「……[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「三位なんでしょう、ピアスは。\n
だから、これは三位に入った人へのご褒美よ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Pierce "「…………」"

play sound se_0622 volume .4
pause .2
play sound se_0622 volume .4
pause .2
play sound se_0622 volume .4
pause .5
play sound se_0051 volume .4
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私のキスに呆然としていたピアスは、にこっと笑うと抱きついてきた。\n
両手に抱えていたチーズが床に散らばる。"

hide t_pia_end6
show t_pia_end7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0263
Pierce "「そっか、三位になると、君がもらえたんだね、[firstname]！\n
だったら、俺、三位でよかった！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0264
Pierce "「君は俺のだもんね、だったらもっとちゅうさせて、[firstname]！」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまでの悔し涙をあっという間に消し去って、ピアスは抱きつきながらキスを繰り返してくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（背後の視線が痛い）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（けど……、まあいいか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恥ずかしい気持ちは消えない。\n
しかし、私をもらって喜ぶピアスの顔を見ていると、そう悪い気分はしなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "感覚が違っても、彼は私を一番に考えてくれている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（毒されているなあ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice pie_f0265
Pierce "「大好きだよ、[firstname]。\n
このまま隠しておけたらいいのになあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「……それはやめて」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "土の上からでもピアスは私を見つけるかもしれないが、埋められてしまったら私にはもう彼を見つけられない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "喜んでいる顔も見られなくなるのは、私だって嫌だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T "「今だって、隠せていないんだから……。\n
このままにしておいてよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子とゴーランドの視線が突き刺さっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（今ぐらい、逆に見せびらかしてやりたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんなに嬉しそうな彼の顔。\n
私が独り占めするのはもったいないから。"


hide t_pia_end7
show white onlayer master
with compress_extralong
scene black with compress_extraextralong
pause 1

$ renpy.movie_cutscene("endroll_a.mpg")
#return
