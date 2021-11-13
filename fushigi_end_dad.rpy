
scene map_bg_autumn_day
with dis
label fushigi_end_dad1:
$ clockanim()

$ hi_mes()

scene map_bg_autumn_night
with dis

scene charasel_bg_hatter_night
with dis

scene b_aut_03
with Dissolve(1.2)

scene black
with dis

play music deedam_t_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0246
Dee "「[firstname]。\n
ねえ、起きてよ、お姉さん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0247
Dam "「……[firstname]。\n
起きて」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「ん……。\n
ディー、ダム？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（そんなに揺さぶらないでよ……、まだ眠いわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "久しぶりに眠る、帽子屋屋敷の双子の部屋。\n
ベッドに沈み込んだまま、寝返りを打つと耳元に声が降ってきた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0248
Dee "「困ったね、兄弟。\n
お姉さんが起きないよ、頑張らせすぎちゃったせいかな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0250
Dam "「仕方ないよ、兄弟。\n
だって、お姉さん、可愛すぎて加減なんか出来ないよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice dad_f0251
Dee "「どうしようか、このまま僕達が着替えさせちゃおうか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice dad_f0252
Dam "「一枚ずつちゃんと着替えさせてあげないといけないよね。\n
ふふふ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「！！」"

play sound se_0052

scene f_03
with open
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子の危険な会話に耐え切れず、がばっとベッドから体を起こした。"


show dee_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0253
Dee "「あ、お姉さん。\n
いい夢、見られた？」"

hide dee_t_02_4
show dee_t_02_4 at left
show dam_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0254
Dam "「そんなに急に起きると危ないよ。\n
それとも、怖い夢でも見たの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_11")
T "「……そうね。\n
ある意味ナイトメアの悪夢よりも悪い夢だったかも」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（寝ている相手に一体何をしようとしていたのよ、あんた達はっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず声に出しかけたが、正直に言えばかえって悪い状況に立たされるだけだ。\n
ダムの台詞ではないが、沈黙は金なり、である。"

hide dee_t_02_4
show dee_t_01_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0255
Dee "「そんなに悪い夢だったのなら、もう少し寝かせてあげようか？\n
僕達、お姉さんにならいくらでも添い寝してあげるよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！\n
いい、そんなことしなくていいからっ」"

hide dam_t_02_9
show dam_t_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice dad_f0256
Dam "「遠慮しないでよ。\n
僕達のお姉さんに何かあったら、大変だもん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（この子達の場合……。\n
一緒に寝るほうが危険な予感がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そしてその予感は恐らく的外れではない。"

play sound se_0286

show eri_t_01_5 at center
hide dee_t_01_7
hide dam_t_01_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0165
Elliot "「ガキ共、まだかよ……って、あ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「エリオット？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアが乱暴に蹴破られる。\n
ひょこっと覗いた茶色い耳に続いて、見慣れた帽子が現れた。"

hide eri_t_01_5
show eri_t_01_5 at left
show bra_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0297
Blood "「おや、お嬢さん、君が寝坊とは珍しい。\n
相手が二人だ、よほど激しかったのかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（セクハラ上司）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を探しにディーとダムの部屋に来る時点で、分かって言っているに違いない。\n
相変わらず、性格の悪い男だ。"

hide bra_t_02_2
show bra_t_03_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0298
Blood "「ふふふ、そんなに睨まないでくれ、[firstname]。\n
君を怒らせに来たわけじゃない」"

hide bra_t_03_15
show bra_t_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0299
Blood "「主役の君がいつまでも姿を見せないから、エリオットと一緒に迎えに来たんだ。\n
門番に任せておくと、ずっと待たされそうだからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「主役？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何か催し物でもあるのだろうか。\n
それも、私に関わるものらしいが……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「私が離れている間に、何か決めたの？」"

hide bra_t_03_9
show bra_t_01_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice blo_f0300
Blood "「さて、どうだろうな。\n
二人とも、いつまでもじゃれていないでさっさとしなさい」"

hide bra_t_01_12
show bra_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice blo_f0301
Blood "「もっとも、お嬢さんを着替えさせる役目を誰かに譲りたいというのなら話は別だが」"

hide eri_t_01_5

hide bra_t_01_11
show bra_t_01_11 at left
show dee_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0257
Dee "「そんなことさせないよ。\n
お姉さんで人形遊びをしていいのは僕達だけだもん」"

hide bra_t_01_11

hide dee_t_01_4
show dee_t_01_4 at left

show dam_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0258
Dam "「ちゃんと着替えてもらってから行くから……、ボス達は席を外してよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぎゅっと私に抱きついてきて、彼らはそんなことを言う。\n
まったく状況の見えない私は、二人に挟まれたまま、視線を揺らすばかりだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T "（一体、何があるっていうのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッド達の様子から察するに、いつものお茶会とは違うらしい。\n
だからといって仕事に行くような雰囲気でもない。"

hide dee_t_01_4

hide dam_t_01_1
show dam_t_01_1 at left
show eri_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0166
Elliot "「ったく、おまえら、これ以上遅れるなら～～～で～～～～～だからな」"

hide dam_t_01_1
hide eri_t_02_9
show eri_t_02_9 at left
show bra_t_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0302
Blood "「ではお嬢さん、先に会場で待っているよ」"

play sound se_0774
hide eri_t_02_9

hide bra_t_01_2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言いたいことだけ言い終えると、ブラッドとエリオットは部屋を出て行ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……一体、何があるの？」"


show dee_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0259
Dee "「ふふふ。\n
パーティがあるんだよ！」"

hide dee_t_02_5
show dee_t_02_5 at left
show dam_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0261
Dam "「飲み放題食べ放題。パーティっていいよね。\n
お姉さんは主役だけど、僕達から離れたら駄目だよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……パーティ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（しかも、私が主役で？\n
どういうこと？）"

hide dee_t_02_5
show dee_t_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice dad_f0262
Dee "「さてと、じゃあ、皆も待っているみたいだし……。\n
見せびらかしに行こうか、兄弟」"

hide dam_t_02_4
show dam_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice dad_f0263
Dam "「そうだね、兄弟。\n
お姉さんはまだ寝惚けているみたいだから、手伝ってあげる」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "早々と私の身体に伸びてくる四本の手に、悲鳴にも似た声が上がる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！\n
いいってば……、ちょ、待ちなさい、服を脱がさないで！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この二人は、迂闊に物思いに耽る暇も与えてくれない。"

hide dee_t_01_6
hide dam_t_01_3
$ hi_mes()
scene bg_gen08_bn_aut_nig_p
with stripe_l_long
play sound se_0688

play music night_garden_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「祝勝会か何かだったの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だって帽子屋屋敷のメイドの一人として働いている身だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この屋敷にどの程度の人間がいるか、見当をつけているつもりだったが……。\n
今、目の前にいる人数はそれを超えている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（普段屋敷にいない人も多い気が……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋屋敷の庭に特別に用意された会場は、相当な広さがあった。\n
テーブルには食事や飲み物が、所狭しと置いてある。"


show dee_s_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0264
Dee "「違うよ、パーティだってば。\n
何度も言ったのに、もう忘れちゃったの、お姉さん」"

hide dee_s_02_5
show dee_s_02_5 at left
show dam_s_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0265
Dam "「お姉さんは照れているんだよ。\n
嬉しくて」"


show situji_s_01_07 at center
hide dee_s_02_5

hide dam_s_02_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0020
Kousei "「いいなあ、門番さん。\n
主役を二人占めですか」"

hide situji_s_01_07
show situji_s_01_07 at left
show bousi_s_01_07 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0033
Maid "「羨ましいです～。\n
私達もお祝いしにきているのに……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（お祝い？\n
私を？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさか家出した私が戻ったお祝いということはないだろう。\n
だが、周囲の視線が私に集中していることは間違いない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「一体、どういうことなの、ディー、ダム」"


show dee_s_02_1 at center
hide situji_s_01_07
hide bousi_s_01_07
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice dad_f0266
Dee "「お姉さん、まだ気付かないの？\n
ふふふ、これはお姉さんの誕生日パーティなんだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「私の……、誕生日？\n
でも、そんなの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時間帯の乱れたこの世界では、いつでも誕生日だし、逆に言えばいつでも誕生日ではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が初めてこの屋敷を訪れたときにも、同じようなことをブラッドが言っていた。"

hide dee_s_02_1
show dee_s_02_1 at left
show dam_s_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0268
Dam "「細かいことは気にしないで、名目はなんでもいいんだ。\n
お姉さんが一番幸せで、一番ちやほやされるように考えたんだから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ちやほや……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（なんだか、私にはずいぶん縁遠い言葉のような気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、この世界に来てからはいろんな人にずいぶんと構ってもらっている。"


show bra_s_02_15 at center
hide dee_s_02_1
hide dam_s_02_10
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0303
Blood "「そういうことだ、お嬢さん。\n
発案者としては、君の感想を聞きたいところだが……」"

hide bra_s_02_15
show bra_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0304
Blood "「ふふふ、その顔は満更ではなさそうだな。\n
面倒なことをした甲斐があったというものだよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "紅茶のカップを片手に背後から現れたブラッドは、私の顔を見てにやにやと笑っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その表情を見て、私の中にも一つの考えが思い浮かんだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうして気付かなかったのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（まさか……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……私に隠していたのって、このパーティのことだったの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問い詰める声に棘が含まれていたとしても、仕方ないだろう。\n
だが、睨まれた本人よりも、二人のほうが気になったらしい。"

hide bra_s_03_10


show dee_s_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0269
Dee "「……お姉さんを除け者にしようとしたわけじゃないんだよ。\n
だけど、びっくりさせて、とびきり嬉しくさせたかったんだ」"

hide dee_s_01_1
show dee_s_01_1 at left
show dam_s_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0270
Dam "「黙っていたこと……、まだ怒っている？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「そうね。\n
すっきりはしていないけれど」"

play sound se_0596
hide dee_s_01_1

hide dam_s_01_5


scene t_cut_twi_end1u
with Dissolve(.5)

scene t_cut_twi_end1
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さりげなく身体の向きを変えて、足を振り下ろせばいい手応えが返ってきた。"


show bra_s_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0305
Blood "「あ……、ぐっ！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「でも、もういいわ。\n
あなた達がお祝いしようとしてくれたのは、よく分かったから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこやかに双子へ告げながら、背後にあるブラッドの足を踵で踏みつける。"

play sound se_0597
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（ディーとダム、エリオットも私を驚かせようとしてくれただけでしょうね。\n
でも、ブラッドは私の反応を楽しんでいたに決まっているわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相手の表情を見なくとも、それくらいの性格は理解していた。"

hide bra_s_02_7
scene bg_gen08_bn_aut_nig_p
with dis

show dee_s_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0271
Dee "「お姉さん！\n
よかった、お姉さんがまだ怒ったままだったらどうしようかと思ったんだっ」"

hide dee_s_01_2
show dee_s_01_2 at left
show dam_s_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0272
Dam "「これで、本当に仲直りだね」"

play sound se_0054
hide dee_s_01_2

hide dam_s_01_6


scene t_cut_twi_end1
with dis

show bra_s_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0306
Blood "「お、お嬢さん……。\n
いい加減、その足を……、っ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（たまにはいい薬よ）"


scene bg_gen08_bn_aut_nig_p
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私がどういう反応をするかも全部分かっていて黙っていたに違いない家主の足に思いっきり体重をかけていると、二人は私の手を引いて歩き出した。"

hide bra_s_02_7
show bra_s_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0307
Blood "「ふう……、酷い目にあった。\n
おまえ達、お嬢さんのエスコートは任せたぞ」"


show dee_s_02_2 at center
hide bra_s_03_13
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0273
Dee "「勿論、任せてよ、ボス。\n
僕達、ばっちりリードしてくるから」"

hide dee_s_02_2
show dee_s_02_2 at left
show dam_s_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0274
Dam "「うん。\n
僕達は、お姉さんを喜ばせる担当だもんね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（喜ばせるって）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その言葉に不安よりも期待が勝ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（ああ、毒されている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "でも、悪い気はしない。"


show bra_s_03_4 at center
hide dee_s_02_2
hide dam_s_02_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

hide bra_s_03_4
show bra_s_03_4 at left
show bousi_s_01_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0034
Maid "「ボス～、こちらでちょっとお話が……」"

hide bra_s_03_4
show bra_s_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0308
Blood "「ああ、分かった。\n
では、お嬢さん、よい誕生日パーティを」"

play sound se_0625
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何か言いたげなブラッドはにやにやと私達を見ていたが、来客なのだろう。\n
メイドの一人に声をかけられて、その場を離れていく。"


show dee_s_01_9 at center
hide bra_s_01_1
hide bousi_s_01_05
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0275
Dee "「そうだ、僕達、お姉さんにすっごいプレゼントを考えたんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「プレゼント？」"

hide dee_s_01_9
show dee_s_01_9 at left
show dam_s_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice dad_f0276
Dam "「僕達にしかあげられない、特別なプレゼントだよ。\n
受け取ってくれるよね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（まさか、ナイフだったり、爆発物だったり、危険な～～～じゃないでしょうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らの趣向を考えるとそういう路線で言われても、おかしくない。\n
そんなものをもらっても困るのだが……。"

hide dee_s_01_9
show dee_s_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0277
Dee "「やっぱりこういうのは、僕達だけで渡すのが一番だよね。\n
向こうで、渡してあげる」"

hide dee_s_02_4
show dee_s_03_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0278
Dee "「こっちに来てよ、お姉さん！」"

hide dam_s_02_2
show dam_s_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0279
Dam "「早く、早く！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_12")
T "（この顔を見て、断るなんて出来るはずもないのだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の腕を片方ずつ塞いで見せる、嬉しそうな顔。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大人の姿になっても、子供の姿のままでも、こんなときに浮かべる表情は少しも変わらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不安など一片もない、確信と期待に満ちた眼差し。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（一体、何をくれるつもりなんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自然と私の期待も高まってしまう。\n
どきどきと心臓が高鳴るようだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どんなものを贈られるのかという不安にも、楽しみだという気持ちが混ざり合っていた。"

hide dee_s_03_13

hide dam_s_01_7

$ hi_mes()

scene bg_gen_sky_aut_nig
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0280
Dee "「よし、ここなら誰にも邪魔されないよね。\n
万が一誰か来たら、斬っちゃおう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（どうか誰も来ませんように）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "会場の外れ、ひとけのなくなったベンチに私は座らされている。\n
溢れるほどの人がいた会場とここでは、まるで空気の流れが違う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それだけに……、二人との距離を意識してしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_8")
T "（何をくれるのかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "物騒な武器でも、今なら受け取れる。\n
ありがとうと言う自分の顔まで想像できて、呆れてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（……それが二人の愛情だって分かるんだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "疑り深い私に、疑う余地を与えてくれない。\n
双子の恋人に囲まれて、悩む隙をなくす機会が増えていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0282
Dee "「じゃあ、これからプレゼントを渡すから……。\n
目を閉じていて、お姉さん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0283
Dam "「いいって言うまで、開けちゃだめだよ」"


show black onlayer master
with close_m
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「分かったわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
Dee "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
Dam "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっと座っていると手が持ち上げられた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（大きなものなのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "座って渡されるぐらいだから、手の中に収まるようなものを連想していたのだが、どうやら違うらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま待っていると、手首に暖かいものが触れた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0284
Dee "「ハッピー・バースデイ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0285
Dam "「おめでとう、[firstname]」"

hide black
show t_twi_end1 onlayer master
with open

play music dream_tsuduki_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「……あ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いいよと声をかけられるまで目を開けるつもりはなかったのに、手に触れた感触に思わず目を開けてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、二人は怒ったりせず、柔らかく笑っている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0286
Dee "「これが、僕達の贈り物」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0287
Dam "「受け取ってくれるよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もっと深いキスも、もっと際どいところにも何度も何度も触れられているのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "軽く膝をついて、手をとられている。\n
見上げるような眼差しにこもった感情は、どんな凶器よりも危険なものに見える。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（手の甲じゃなくて、手首にキス）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らに知識があるかは分からないが、傷ついたらたくさん血が溢れる場所だ。\n
残酷な子供の告白は、怖いと思うのに、惹かれていく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dee "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0288
Dam "「嬉しく、なかった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「そんなことないわ。\n
ありがとう、すごく嬉しい」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_12")
T "（キスが贈り物なんて、すごい女たらしみたいだけど……。\n
この子達の場合は、そう思えないのが不思議だわ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_12")
voice dad_f0289
Dee "「よかった、お姉さんなら絶対に喜んでくれると思ったんだ！\n
ね、兄弟？プレゼント作戦は、大成功だよっ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_12")
voice dad_f0290
Dam "「よかった。\n
僕達、ずっと、お姉さんに尽くしてあげるからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……尽くす？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然出てきた単語に首を傾げると、彼らは頷いた。\n
その笑顔を見て、思わず背筋が震える。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0291
Dee "「僕達がプレゼントだもの、お姉さんに尽くすのは当然じゃない。\n
ねえ……、どんなご奉仕をしてほしい？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0292
Dam "「お姉さんのお強請りなら、僕達、喜んで聞くよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

hide t_twi_end1
show t_twi_end2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……{size=+20}え？{/size}」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（何が一体どうしてそういうことに）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice dad_f0293
Dee "「返品は出来ないよ……、ううん、するはずがないよね？\n
そんな酷いこと言われたら、僕達泣いちゃうよ、お姉さん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice dad_f0294
Dam "「お姉さんは優しいから、遠慮するかもしれないけど……。\n
もう、受け取ってもらったから……、ね？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キスという隠れ蓑の奧に待っていたのは、私を圧倒する二人の恋人だった。"

$ hi_mes()

scene b_aut_03
with stripe_l_long
play sound se_0132
hide t_twi_end2
show t_twi_end3 onlayer master
with dis

play music quiet_night_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……はあ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（悪気がないのは分かるんだけど、正直、疲れる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一人で浴槽につかりながら、溜息が零れる。\n
私の誕生日パーティから、ディーとダムが傍を離れてくれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、近くにいること自体は悪いことではない。\n
元に戻っただけだと思えば、ある程度は受け入れられる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問題は……。"

play sound se_0075
hide t_twi_end3
show t_twi_end4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0295
Dee "「お姉さん、見つけた！\n
お風呂に入るのなら、ちゃんと言ってくれないと駄目だよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0296
Dam "「そうだよ、僕達、お姉さんに尽くすつもりなんだから。\n
意地悪しないで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「！！！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「な、何でいるのよっ。\n
あんた達、この時間帯は仕事でしょう！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今の時間帯は外にいるのを、彼らの上司に確認したからこそ、大浴場に来た。\n
それなのに、どうして彼らが乱入してくるのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（少しくらい落ち着きたいのに……！）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice dad_f0297
Dee "「そうだったんだけど、ボスが急に予定を変えたんだ。\n
いつものことだもん、珍しくないでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（まさか、この前足を踏んだことを根に持ってそんなことを言い出したんじゃないでしょうね、ブラッド）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "妙なところで大人げない彼ならありうる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0299
Dee "「そんなことより、お風呂に入るときには教えてって言ったじゃない。\n
一人で入るなんてずるい……、じゃなかった、つれないよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0300
Dee "「遠慮しないでいいんだよ、僕達、いくらでもお姉さんのために尽くしてあげるから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0301
Dam "「うん、たっぷり……、ご奉仕してあげる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！」"

play sound se_0706
hide t_twi_end4
show t_twi_end5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「ちょ、こら、待ちなさいって！\n
いいの、一人で入れるからっ！！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水音と共に迫ってくる双子に、後ずさる。\n
しかし、いくら広い浴槽とはいえ限度があり、壁際に追い詰められてしまった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（ど、どうしよう）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice dad_f0302
Dee "「また、遠慮して……。\n
もっと甘えてくれていいんだよ、お姉さん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice dad_f0303
Dam "「お姉さんがしてほしいだけ甘えさせてあげる。\n
だって、今は僕達のほうが大人だから」"


play music dream_tsuduki_a_ali
hide t_twi_end5
show t_twi_end6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「ん……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「……っ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
Dee "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
Dam "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice dad_f0304
Dee "「……ふ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice dad_f0305
Dam "「……は」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「……っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "唇や、肩、頬、二人に交互にキスをされて、息を継ぐ暇もない。\n
二人を相手にするときはいつも、いっぱいいっぱいになる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（だから……、余計なことも考えなくてすむんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らが双子だとか、常識から外れていることも、頭から飛んでしまう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0306
Dee "「可愛い、僕達のお姉さん。\n
大好きだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0307
Dam "「大好きだから、もっともっと尽くさせて」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（これ以上なんて、無理よ、無理！！！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今でさえ二人の愛情溢れすぎる（？）奉仕に体力の限界がきているというのに、これ以上なんてされたら、尽くされる前に私が潰れる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭の中ではそんな警告がぐるぐると回っているのに。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「……っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "触れられると、一気に力が抜けてしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逆上せてしまったのかもしれない。\n
ピンクのお湯に思考まで溶けていくようだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（ぐるぐるする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人の声も、体温も、私と一緒にお湯に混じってしまったのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（……振り払えない時点で、文句なんて言えないのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "嫌なら嫌だと拒否すればいい。\n
本当に嫌だと言えば、彼らはその違いを汲み取ってくれたはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし……。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0310
Dee "「僕達を置いて行ったりしないでよ。\n
僕達はお姉さんにあげたんだから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0311
Dam "「僕達はずっとお姉さんのものだよ。\n
責任は取ってくれるでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り切れない。\n
こんなことを言われて振り切れるほど、私は多くのものを持っていない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同時に彼らほどの体力も持ち合わせていないのだが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（そのうち、慣れるかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを期待してしまう程度には、今の私は考えがまとまらずにいる。\n
溶けてしまうことが悪いとは限らない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "互いの境界線が分からなくなれば、三人であるとか、良識を思い出さずにすむ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（……忘れようとして、どうするのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思っている時点で、私はこの双子が仕掛けた罠に、はまってしまっているのかもしれない。"

hide t_twi_end6
$ hi_mes()

scene charasel_bg_hatter_night
with stripe_l_medium

scene map_bg_autumn_night
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium

scene charasel_bg_castle_day
with stripe_l_medium

scene hm_spr_01
with stripe_l_medium

scene bg_gen03_hjm_spr_day
with stripe_l_medium
play sound se_0541

play music forest_town_square_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「……とはいえ、あまりに爛れすぎるのもどうかと思うのよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子達が仕事で外に出ていることを聞いて、足を伸ばしたハートの城の領地で、私は息をつく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（一度家出してから、私が外に出ることにすごく敏感になったし）"


scene bg_gen_sky_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこに行ったの、誰と一緒にいたの？\n
その程度の質問ならばいい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0312
Dee "「僕達を全部あげたのに、お姉さんが浮気するなんて……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0313
Dam "「僕達を捨てるの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供の姿で泣き脅しをかけてきたり。\n
あるいは……。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0314
Dee "「どうしようか、兄弟。\n
僕達に対してお姉さんはまだ欲求不満なのかな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0315
Dee "「でもこれ以上頑張るとお姉さんが壊れそうで、ちょっと心配なんだけど」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0316
Dam "「いや、それでも努力は必要だよ、兄弟。\n
不満があるなら解消しないと」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0317
Dam "「僕らは誠実な恋人だからね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大人の姿で、何やらあやしい相談を堂々と本人の前でしてきたり。"


scene bg_gen03_hjm_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（問題は、それでも拒否できない私にもあるんだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "改めて身に余るプレゼントなんてもらうものじゃないと痛感してしまう。\n
ただより高いものがない、というのはどうやら本当のことらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（返品させてくれるような相手じゃないから余計よね）"


play music truth_a_ali

show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice pet_f0417
Peter "「そこにいるのは……、ああ、やっぱり、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ペーター」"

hide per_t_02_3
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pet_f0418
Peter "「どうしたんですか、こんなところで一人でベンチに座っているなんて。\n
やはり、あのならず者どもの巣窟から逃げてきたんですね！」"

hide per_t_02_8
show per_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pet_f0419
Peter "「そうでしょう、そうでしょう。\n
あんな雑菌だらけの、ろくでもない場所にあなたがいることなどありませんから！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人混みから現れたペーターは、いつものように一気に話してくる。\n
どうやらまた私がハートの城に家出してきたのだと思っているらしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……逃げてきたわけじゃないわよ、ちょっと気分転換にきただけ」"

hide per_t_01_2
show per_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice pet_f0420
Peter "「ちょっとだけ……、なんですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「そうよ、ちょっとだけ」"

play sound se_0493
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "親指と人差し指で示すと、ペーターはあからさまに淋しそうな声を出した。"

hide per_t_01_13
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0421
Peter "「そうですか……。\n
でも、こんな場所でどうしたんです？」"

hide per_t_02_6
show per_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0422
Peter "「いつものあの騒がしい子供達の姿もありませんが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「あの子達は仕事中よ。\n
少し街を歩きたいと思って、遠出しにきたの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本当はペーターのことも気になっていたのだが、期待させてしまいそうで、黙っておく。"

hide per_t_03_7
show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0423
Peter "「そうですか」"

hide per_t_02_10
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0424
Peter "「……ねえ、[firstname]。\n
隣、いいですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「え！？\n
でも、これは街の普通のベンチよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分以外はすべて汚いと言い切る彼にとっては、不特定多数の人が使う街のベンチなど雑菌の宝庫としか思っていないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさか自分から座りたいなどと言ってくるとは思わなかった。"

hide per_t_02_8
show per_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0425
Peter "「構いません。\n
あなたの隣に座りたいんです」"

hide per_t_01_10
show per_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0426
Peter "「嫌ですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（そんな顔をしないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段は絶対に引く姿勢を見せないのに、こんなときだけ私の機嫌を伺うような目で見ないでほしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "駄目だと言ったら、どこかに行ってしまうような目で見るなんて、卑怯だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「いいわ、どうぞ」"

play sound se_0148
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "根負けして承諾すると、ペーターが隣に座った。"

hide per_t_01_8
show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（何だろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "静かだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視界には何人もの人達が行き交っているのに、ペーターの隣に座っているだけで、別の空間のように感じる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だからといって居心地が悪い沈黙でもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（静かなペーターなんておかしいのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらりと視線を動かせば、白いウサギは私を見ていなかった。\n
彼もまた道を行き交う人へ顔を向けている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、その赤い目が町の人を見ているかどうかは分からなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（……ペーターの目には、何が見えているんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不思議な赤の瞳。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一かゼロか。\n
彼の関心はいつでも両極端だから、視界に映っていても見えているかどうかは分からない。"


show t_twi_end7 onlayer master
hide per_t_02_10
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「あ、う、うん。\n
何？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然名前を呼ばれたことに驚いていると、彼は私の手を握ってくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0427
Peter "「僕が確かめたいことは、たった一つです」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0428
Peter "「あの双子は、あなたを幸せにしてくれますか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice pet_f0429
Peter "「僕よりもあなたを幸せにしてくれるなら、僕はそれでいい。\n
でも、あなたを幸せに出来ないのなら……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「ペーター」"

play sound se_0267
hide t_twi_end7
show t_twi_end8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "続きを口にしようとした彼を制するように、その唇に指を当てる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（その続きは言わないで）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私にとって、二人も、ペーターも大事な存在だ。\n
どちらかを選ぶことなんて、出来ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（普通は恋人を選ぶべきところなんだろうけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "捨てられない。\n
彼がこの世界に私を招いたことだけが理由ではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もっと深い場所。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心の奥の奧、深海のような場所で。\n
私と彼の間に繋がるものがある。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「私は、あの子達が好きよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ここにいるのは、あの子達の傍にいたいと思ったからよ。\n
私の性格だもの、幸せじゃなかったら、元の世界に帰っているわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「大丈夫よ、ペーター」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（この世界に招いてくれたのはあなたで……。\n
ここにいたいと思わせてくれたのは、あの子達）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくつもあった選択肢の中から、この世界にいることを選んだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ディーとダムは、私の暗い部分も、可愛くない性格も、理屈も吹き飛ばしてくれる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「私は、不幸になんてならないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "幸せになると簡単に約束することは出来ない。\n
だから、今の私に約束できることなんてこれぐらいだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0430
Peter "「あなたがそう言ってくれるなら、僕は見ているだけでも構わない。\n
でも、忘れないでください」"

play sound se_0267
hide t_twi_end8
show t_twi_end9 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターの手袋越しの指が、私の唇に触れる。\n
私が先ほど彼にした仕草と同じ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、そこに込められた意図は違う。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0431
Peter "「僕はいつでも、あなたを見ています」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0432
Peter "「あなたがあなたである限り、どんなときでも、繋がっている」"


play music forest_town_square_p_ali
hide t_twi_end9
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「{size=+20}そんなに堂々とストーカー発言をされても、困るんだけど{/size}……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目が真剣なところが、ますます恐怖を感じる。\n
今更ながらペーターの性格を心配してしまった。"


show per_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_02_4
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0433
Peter "「ええ……。\n
あなたを見ていられるのなら、ストーカーでも何でもいいです」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（いや、{size=+20}そこは否定しようよ{/size}）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "がくりと肩を落とした私を、ペーターは不思議そうに見つめていた。"

hide per_t_03_1
$ hi_mes()

$ time_effect()
show dee_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0318
Dee "「あー、お姉さんだ！！\n
お姉さん、こんなところまで僕達を迎えに来てくれたの！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ディー？\n
ダム？」"

play sound se_0149
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城の領地を歩いていると、二人が斧を振り回しながら私に向かって走ってくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（お願いだから、街中で斧を振り回すのはやめてよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らのことだから悪気はないのだと思うが、万が一通行人に当たったらと思うと肝が冷えてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（しかも、当たっても気にしなさそうだし）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「お疲れ様。\n
もう終わったの？」"

hide dee_t_02_6
show dee_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice dad_f0321
Dee "「うん、あとはピアスの仕事だからさっさと帰ってきたんだけど。\n
……お姉さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ん？\n
何？」"

hide dee_t_01_4
show dee_t_01_4 at left
show dam_t_01_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice dad_f0322
Dam "「……何で、そんなのを抱いているの？」"


show usape_5 at center
hide dee_t_01_4
hide dam_t_01_12
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pet_f0434
Peter "「そんなのとは何ですか、そんなのとは。\n
僕はれっきとしたウサギですよ、失礼なことを言わないでください」"


show dee_t_02_11 at center
hide usape_5
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice dad_f0323
Dee "「どういうこと？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「どういうことって……。\n
まあ、何となく成り行きで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターが街を案内したいというので、ウサギの姿でならいい、と告げてみた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迷っている彼に、ウサギ姿なら抱っこしてあげるのにと言うと、すぐさまこの姿になってくれたのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（この子達が通りがかるなんて……。\n
偶然っていうには、出来すぎているけどね）"

hide dee_t_02_11
show dee_t_02_11 at left
show dam_t_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice dad_f0324
Dam "「そんなウサギ、放っておいて僕達と一緒に遊ぼうよ。\n
ほら、離れろって」"

play sound se_0492
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子は私の腕の中にいるペーターを無理矢理引き剥がしにかかった。"


show usape_6 at center
hide dee_t_02_11
hide dam_t_02_13
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「！！」"

hide usape_6
show usape_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0435
Peter "「[firstname]、この子供達が僕をいじめるんです。\n
助けてください～っ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「う」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（中身はあのペーターだって分かっているけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ダ、ダム……。\n
そこまでしなくても」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「耳を引っ張るのは、可哀想よ」"


show dee_t_01_1 at center
hide usape_11
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice dad_f0325
Dee "「お姉さんだって、うちのウサギによくやっているじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「だって、エリオットは……、大きいし、しっかりしているけど。\n
このウサギは小さくて、可愛いし」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（苦しい言い訳）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大きい小さいで扱いを変えるのは間違っている。\n
どちらも可愛いと思っているなら尚更だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（でも、どうしてもこの姿のペーターには弱いのよね）"

hide dee_t_01_1
show dee_t_01_1 at left
show dam_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice dad_f0326
Dam "「僕達だって可愛いのに……。\n
お姉さんから離れろよ、この～～～～～～ウサギ！」"

hide dee_t_01_1
show dee_t_02_3 at left
with dis
hide dam_t_02_3
show dam_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice dad_f0327
Dee "「そうだよ、離れろって！\n
うちのウサギもうざったいけど、おまえはもっと大嫌いだ！」"


show usape_6 at center
hide dee_t_02_3
hide dam_t_02_3
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Peter "「[firstname]っ！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（これ以上抱きかかえていたら、確実に銃や刃物が飛び出るわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "腕の中の感触は手放すには、とても勇気が必要だったが。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ご、ごめん、ペーター」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "意を決して、縋りついてくるペーターから手を離す。"

play sound se_0148
hide usape_6
show usape_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………！！」"

hide usape_11
show usape_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "うるうるとした眼差しで見上げてくるペーターは、やがて大きな溜息をついた。"

play sound se_0337
$ flash(.2)
$ flash(.2)
play sound se_0331 volume .3
show white onlayer master
hide usape_15
show per_t_01_12 at center
with dis
hide white with compress_long
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0436
Peter "「まったく、堪え性のない子供達ですね。\n
そんなあなた達が本当に彼女を幸せに出来るんですか？」"

play sound se_0155
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人型に戻ったペーターは、埃を払いながら冷たく告げる。"


show dee_t_02_9 at center
hide per_t_01_12
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0328
Dee "「僕達がお姉さんを幸せにする？」"

hide dee_t_02_9
show dee_t_02_9 at left
show dam_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0329
Dam "「……何を馬鹿なことを言っているの、このウサギ」"


show per_t_02_11 at center
hide dee_t_02_9

hide dam_t_02_12
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0437
Peter "「彼女はとても繊細なんですよ。\n
あなた達のくだらない玩具とは違うのに、同じように壊してしまうのではないか不安です」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（何もそこまで言わなくても）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、彼の指摘は少なからず私自身も感じていたことだ。"


show dee_t_01_10 at center
hide per_t_02_11
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dee "「…………」"

hide dee_t_01_10
show dee_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0330
Dee "「本当に馬鹿なウサギ。\n
僕達は子供だよ、幸せかどうかなんて興味ない」"

hide dee_t_01_3
show dee_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0331
Dee "「理屈なんて、全部斬っちゃえばいいんだ。\n
僕達はお姉さんと一緒にいたいだけだからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……ディー」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（そうね、理屈なんて忘れてしまえればいいのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私はまだどこかで自分を縛っている。"


show per_t_02_10 at center
hide dee_t_01_6
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"


show dam_t_01_8 at center
hide per_t_02_10
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0332
Dam "「我慢したり、余計なことを気にする必要もない。\n
僕達が大切なのは、お姉さんだけって決まっているんだもん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ダム」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（余計なこと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "好き嫌いだけで物事を決める純粋さ。\n
それが残酷さと紙一重だということを、私は知っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（だけど、羨ましい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思ってしまう自分が確かにいる。"


show per_t_03_7 at center
hide dam_t_01_8
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0438
Peter "「それなら、よく覚えておいてください。\n
彼女を哀しませたり、傷つけたりしたときには、僕があなた達を殺します」"

hide per_t_03_7
show per_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0439
Peter "「彼女が泣いて止めたとしても、僕があなた達を許さない。\n
国を違えようと、どこに隠れようと……」"

hide per_t_02_9
show per_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0440
Peter "「必ず、殺します」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「ペーター……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（そんなこと、言わないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "名前を呼ぶと、ペーターが私のほうを向いた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それだけで、彼の雰囲気が、豹変という言葉が相応しいくらい、一瞬で柔らかくなる。"

hide per_t_02_11
show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_02_7
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0441
Peter "「もしもの話ですよ。\n
もしも、の」"

hide per_t_02_6
show per_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0442
Peter "「あなたを幸せにするだけの力がこの子供達にあれば、何の問題もありません。\n
だから、[firstname]」"


play music secret_a_ali
show t_twi_end10 onlayer master
with dis
hide per_t_02_12

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頬にキスをされて、小首を傾げる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分でもペーターが顔を寄せてきたことに、驚かなかった。\n
驚かなかったことに自分で驚いてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（どうして？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice pet_f0443
Peter "「どうか。\n
あなたが幸せでありますように」"


scene bg_gen_sky_all_day ##instant
hide t_twi_end10


play music forest_town_square_p_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice dad_f0333
Dee "「何が幸せでありますように、だよ。\n
この～～～～～～～～ウサギ！」"

play sound se_0084
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice dad_f0334
Dam "「お姉さんは僕達のだって、言っただろう！」"

play sound se_0672
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「ちょっと、二人とも！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いきなり斧を持って斬りかかり始めた二人に声をかけるが、彼らは聞く耳を持ってくれない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0335
Dam "「振られウサギのくせにしつこいんだよっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0444
Peter "「失礼な、僕は振られてなんていません！\n
僕と彼女は魂で結ばれた、運命の恋人なんですよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0445
Peter "「あなた達のような安い関係と一緒にしないでください！」"

play sound se_0501
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……結局こうなるのね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（先刻までは結構いい雰囲気だったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飛び交う銃弾は、いつだって平穏の影に隠れているらしい。"

play sound se_0506
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……ありがたくない）"

$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_medium

scene charasel_bg_hatter_day
with stripe_l_medium

scene f_01
with stripe_l_long

play music deedam_t_ali

show dee_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0336
Dee "「お姉さん！\n
どういうつもりなの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「どういうつもりも何もないわよ」"

hide dee_t_01_4
show dee_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
Dee "「…………」"

hide dee_t_01_1
show dee_t_01_1 at left
show dam_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
Dam "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋屋敷に戻って、二人の部屋へ連れ込まれた。\n
ソファーに座らされたきり、二人はじっと私の顔を睨んでいる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（そんなに浮気性に思われているのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただでさえ恋人が双子というだけでも、不誠実と思われているのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「……本当に何もないわ」"

hide dee_t_01_1
show dee_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice dad_f0338
Dee "「じゃあ、どうしてあのウサギと会うの？\n
僕達がいるだけじゃ駄目なの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「ディー」"

hide dam_t_01_1
show dam_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice dad_f0340
Dam "「こんなにお姉さんのことが好きなのに。\n
どうしてあんなウサギに会うの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「ダム……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「どうしてって、たまたま今回は顔を合わせただけよ。\n
約束していたわけじゃないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "では、もし……、二人のためにペーターに会うのをやめろと言われたら、私はどうするだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（……約束、出来ないんだろうな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼ら以外の誰とも会うなと言われたら、私は耐えきれない。\n
それはペーターに限らないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人が大事なことに変わりはないのに、二人だけのものになることが出来ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（これって、不誠実なことなのよね、きっと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らは私に全部くれると言ってくれている。\n
しかし、簡単に答えられるだけの勇気など、私にはない。"

hide dee_t_01_5
show dee_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dee "「…………」"

hide dam_t_02_9
show dam_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人は私から視線を移して、目だけで会話をする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（いっそ、あなた達の間に私を閉じ込めてもいいのにな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "混じり合えないことを感じる度に、そんな気分になってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "外からは見えない繋がりや、形はなくとも確固たる結束が二人にはある。\n
それを持たない私には、羨ましく映るものだ。"

hide dee_t_02_8
show dee_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0341
Dee "「お姉さんがそう言うなら信じるよ。\n
僕達は恋人思いだから」"

hide dee_t_02_4
show dee_t_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0342
Dee "「でも……」"

hide dam_t_02_8
show dam_t_03_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0343
Dam "「なんだか、ずるいや」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ずるい？」"

hide dee_t_03_7
show dee_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice dad_f0344
Dee "「全部あげたのに、僕達だけでお姉さんをいっぱいに出来ないなんて……。\n
お姉さんの中はどれだけ広くて、大きいの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（広くて、大きい？）"

hide dam_t_03_15
show dam_t_03_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice dad_f0345
Dam "「二人がかりでも埋めきれないなら、どうしたらいい？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「私は狭いわ。\n
広くもないし、ちっぽけなものよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（空いているから埋めきれないわけじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の中は狭くて、小さくて、たかがしれている。\n
二人の恋人を同時に収められるほどの許容量など最初からない。"

play sound se_0551

play music happy_a_ali

show t_twi_end11 onlayer master
hide dee_t_03_11
hide dam_t_03_6
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dee "「？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0346
Dam "「お姉さん？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "両側に座っている二人の手を、片方ずつ胸に当てる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「ほら、もういっぱいでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（充分すぎるほど、二人に満たされている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足りないのではなく、満たされているから不安になる。\n
その感覚を二人に分かってもらうのは難しい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0347
Dee "「……よく分からないよ。\n
どくどくしているのは分かるけど、僕達がどきどきさせているの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_2")
T "「そうよ。\n
他の人に、こんなにどきどきしたりしないわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_2")
voice dad_f0348
Dam "「僕達だけ？\n
僕達がいなくなったら、このどきどきもなくなっちゃうの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「……ええ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（心臓が止まらなくても、こんなに激しく脈打つことはなくなるもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人が、あるいは片方がいなくなってしまったら。\n
鼓動が止まりそうな予感が胸を震わせる。"

hide t_twi_end11
show bg_gen_sky_spr_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0438
Peter "「それなら、よく覚えておいてください。\n
彼女を哀しませたり、傷つけたりしたときには、僕があなた達を殺します」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0439
Peter "「彼女が泣いて止めたとしても、僕があなた達を許さない。\n
国を違えようと、どこに隠れようと……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0440
Peter "「必ず、殺します」"

hide bg_gen_sky_spr_day
show t_twi_end12 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ペーターはそう言っていたけど、そんなこと、あり得ない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が他の人と話しているだけでも気に入らないような、子供達。\n
壊れても代えがきく玩具とは違うのだと、そう信じていたい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（完全には、幸せにしてくれなくても）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "完全なものなどない。\n
不完全な私に相応しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（ずっと大切にしてくれるでしょう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大切にしたい相手以外に、自分のすべてをあげるなんて台詞、どうして言えるだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（私だって、簡単な気持ちで受け取ったわけじゃない）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「あなた達は私がもらったんだもの。\n
勝手にどこかに行ったら駄目よ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_12")
voice dad_f0349
Dee "「うん、そうだね。\n
お姉さんのこの心臓を動かすのに僕達が必要なら、嬉しい」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_12")
voice dad_f0350
Dam "「止めさせたりしないよ。\n
ずっと一緒にいて、動かしてあげる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「うん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_8")
T "（完全に解け合えないとしても。\n
この二人と、ずっと繋がっていたい）"


hide ali_t_02_8
hide frame_gen_monologue
with Dissolve(2)
hide t_twi_end12
show white onlayer master
with compress_extralong
hide white with compress_extralong
pause 1

$ renpy.movie_cutscene("endroll_a.mpg")
#return
