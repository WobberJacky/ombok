scene map_bg_summer_day with dis
label fushigi_end_boris1:
$ clockanim()
scene map_bg_summer_day with dis

play music amuse_gate_p_ali

show yum_sum_01_1 with Fade(1.2)

show yuuen_man_02_03 at center
with dis
$ show_mes("frame_gen_chara")
voice tan_f0033
Park_Employee "「あー、帰ってきましたよ！！！\n
お帰りなさいっ」"
$ hi_mes()
hide yuuen_man_02_03
show yuuen_man_02_03 at left
show yuuen_woman_02_03 at right
with dis
$ show_mes("frame_gen_chara")
voice may_f0045
Park_Employee "「よかった、これで仕事がはかどりますっ」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「……ただいま」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（この無駄に元気な声にもすっかり慣れちゃったわね）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最初の頃は、エネルギーが有り余っているとしか思えなかった従業員の反応。\n
それが今ではこれが当たり前と思っている自分がいる。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（…………）"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（ここが、私が帰るって決めた場所だもの）"
$ hi_mes()

show go_t_02_12 at center
hide yuuen_man_02_03
hide yuuen_woman_02_03
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_03_14")
voice gor_f0357
Gowland "「おお、[firstname]！\n
帰ってきてくれたのか」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「ゴーランド！」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "久しぶりに顔を合わせたオーナーはいつものようにバイオリンを片手に持ったまま、私のほうへ手を振ってくれた。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地の入り口は、より一層賑やかになる。"
$ hi_mes()
hide go_t_02_12
show go_t_02_2 at center
with dis
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0358
Gowland "「あのときは……、本当に悪かったな。\n
俺からもボリスやピアスにはよく言っておいたんだが……」"
$ hi_mes()
hide go_t_02_2
show go_t_03_7 at center
with dis
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0359
Gowland "「そういう俺も大人げなかったよな。\n
悪かった」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（大人げなかったのは、私も一緒だわ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "開口一番謝ってくれるゴーランドに申し訳ない気持ちになった。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「もういいわよ。\n
そういえば……、あのとき話していた新しいアトラクションって決まったの？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのときには、なかなかいい案が出なくて唸っていたゴーランドだが、私がクローバーの塔に家出していた間に名案が浮かんだかもしれない。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思っての質問だったのだが、彼は渋い顔で首を横に振った。"
$ hi_mes()
hide go_t_03_7
show go_t_01_6 at center
with dis
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0360
Gowland "「いいや、全然っ！\n
あんたがいないとインスピレーションわかなくて、いいものが思い浮かばなくてよ」"
$ hi_mes()
hide go_t_01_6
show go_t_03_1 at center
with dis
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0361
Gowland "「ピアスやボリスもふらふらしていてばっかりで、役に立たねえし。\n
八方塞がりだ」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「そう」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（間に合わないかと思ったけど、無駄にならなくてよかったわ）"
$ hi_mes()
play sound se_0470
hide go_t_03_1
show go_t_01_11 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice gor_f0362
Gowland "「ん？何だ、[firstname]。\n
その資料は……」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_2")
T "「使えるかどうか分からないけど……、こんなのはどうかと思って」"
$ hi_mes()
hide go_t_01_11
show go_t_03_10 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_05_2")
Gowland "「？？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首を傾げるゴーランドに、私は書類を渡しながら説明を始めたのだった。"
$ hi_mes()
hide go_t_03_10
$ hi_mes()

show yum_sum_01_1 with Fade(.8)

scene bg_gen11_yuy_sum_day with stripe_l_medium
show bg_gen11_yuy_sum_eve with Fade(1)

play music amuse_mae_p_ali
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（ボリス、戻っているかしら？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あちこちの空間と空間を繋げること。\n
それがチェシャ猫の役割だということは聞いている。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのせいか、ボリスは捕まえようと思ってもなかなか捕まらないことも多い。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（予定より早く帰ってきたし……、仕方ないか）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼に帰ると約束したのは次の時間帯だった。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの後、塔に戻り、ナイトメア達に挨拶をして、失礼でない程度に急いでここに戻ってきた。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……ナイトメアなんか、いなかったくせに状況をよく知っていそうな顔だったわよね）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "物言いたげな塔の主の顔を思い出すと、何だか手のひらの上で踊らされているようで、釈然としない。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋の片付けなんかいい、またいつでも遊びにおいでと見送ってくれたグレイへの感謝とは対照的だ。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ボリス、戻っている？」"
$ hi_mes()
play sound se_0290
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の部屋をノックするが、声は返ってこない。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（まだいないみたいね）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "このまま自分の部屋に戻ることも考えたが、ボリスはいつ戻ってくるか分からない。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（鍵がかかっているわよね、きっと）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさか鍵もかけずに出ていくなんてことはないだろう。\n
そう思いながらもダメ元でノブを回すと……。"
$ hi_mes()
play sound se_0275
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「鍵もかけていないわけ？」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（抜けているのか、それとも気にしないのか分からないけど）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "カチャリと開いたドアに、首を傾げた。"
$ hi_mes()

play music boris_t_ali
show bo_02 with dis
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「お邪魔します」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰もいないと分かっていながらも、思わずそんなことを言いながら入る。\n
馴染みのあるボリスの部屋に、彼の姿はなかった。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（やっぱりまだ留守か）"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「早く帰ってこないかな」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "話したいこと、一緒にしたいことがある。\n
そう考えたら、この場所で待っていようと思い、ベッドに腰掛ける。"
$ hi_mes()
play sound se_0327 volume 0.6
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま重みに体を預けて、仰向けに転がった。"
$ hi_mes()
play sound se_0328
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（あ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベッドからの気配に、懐かしいものを感じる。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_8")
T "（やっぱりここ、ボリスのベッドだわ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "油や花の匂いとも違う。\n
ただ、彼のいる場所には不思議な香りが集まっている。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "森林浴をしているような、そんな心地よさがある。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（気持ちいい、匂い）"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_1")
T "（ボリスの匂いがする）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目を閉じて部屋の主の気配を感じているだけで、ほっとする。\n
こんな行動も、いつもの私らしくもないことは分かっていた。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰もいない部屋に上がり込んで、その上ベッドで一人ごろごろとしているなんて、無礼にも程がある。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（好きな人の匂いだから、つい図々しくなっちゃう）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "寂しかったのは彼だけではない。\n
私だって同じぐらい、寂しく思っていたのだ。"
$ hi_mes()
$ hi_mes()

$ time_effect()
pause 1


pause 0.5
scene bo_01 with dis

play music honobono1_a_ali
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……ん？\n
眩しい……」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうやらボリスを待っている間に時間帯が変わったらしい。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（いつの間にか寝ちゃったんだわ、私）"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（……あれ？\n
身体の上に、何かいる？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まだ寝惚けた頭を刺激するように、ざらざらとしたものが私の顔を舐めてきた。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（…………）"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（舐める？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薄く目を開くと、視界には……、強烈なほどのピンク。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（ボリス……？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、違う。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あなた、この前の……」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice chi_f0047
Cat "「にゃあ」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔に滞在しているときに出会った、ピンク色をした猫だ。\n
それが私の顔をぺろぺろと舐めている。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（この猫も、夢だったりして）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスのことを思い出させ、安らぎをくれた猫。\n
その正体を、私は知っている気がした。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"
$ hi_mes()
play sound se_0551

show t_bor_end1 onlayer master with dis
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_1")
T "「ん……。\n
やっぱり、あなた」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（あったかい）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふわふわの毛並みに眼を閉じていると、耳元で鳴き声が聞こえたような気がした。"
$ hi_mes()
$ hi_mes()
hide t_bor_end1 with dis

$ time_effect()

play music moon_night2_a_ali
scene bo_03 with dis
hide bo_01
$ show_mes("frame_gen_chara")
Boris "「[firstname]」"
$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_f0263
Boris "「[firstname]、ほら、そろそろ起きようぜ。\n
俺としてはこの姿勢も悪くないけどさ……」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「ん……」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「ボリス？」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（戻ってきたの？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "寝惚け眼をどうにか持ち上げると、目の前にボリスがいた。\n
それも、鼻先がくっつくほどの近距離に。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（あれ？）"
$ hi_mes()

show t_bor_end2 onlayer master with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice bor_f0264
Boris "「おはよう、[firstname]。\n
いい夢は見られた？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目覚めの挨拶というように私の頬にボリスがキスをしてくる。\n
そう、私の腕の中に包まれたボリスが。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「え？あれ、何で……。\n
ボリスがいるの？」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（先刻まで抱き締めていたのは、あの猫のはず）"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice bor_f0265
Boris "「何でって……、それはないだろう、[firstname]。\n
ここ、俺の部屋だぜ」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「いや、そういう意味じゃなくて」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "{size=+20}「どうして、あなたが私の上に乗っているのかを聞いているんだけど」{/size} "
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（どうりで重いわけだわ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "細身に見えても、ボリスの身体はしっかりと筋肉が付いている。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（完全に乗っかっているわけじゃないんだろうけど……、それでも結構重い）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おまけに。\n
この体勢では、今すぐにでも別の方向に話が傾きかねない。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0266
Boris "「何だよ、[firstname]。\n
覚えていないの？」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0267
Boris "「あんたが俺をベッドに引っ張り込んだんだぜ？」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「え？\n
わ、私が！？」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice bor_f0268
Boris "「ああ、帰ってきたらあんたがベッドの上で気持ちよさそうに寝ていたから、声かけたんだけどさ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice bor_f0269
Boris "「そのままぐっと引っ張られて、それでずっとあんたの腕の中にいたってわけ。\n
本当はもっと色々としたかったけど……」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を見つめているボリスは、まさに猫の眼をしている。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスを見るときにたまに見せる、彼にとって「美味しいもの」を見つめる眼差しだ。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0270
Boris "「あんたがあんまり無防備に気持ちよさそうに寝ているから、何もしなかったけどさ。\n
食べちゃいたかったな、あんたのこと」"
$ hi_mes()

play music boris_t_ali
show t_bor_end3 onlayer master with dis
hide t_bor_end2 with dis
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あ、ちょっ、ちょっと」"
$ hi_mes()
play sound se_0007
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔を寄せてくるボリスから身を捩って逃げだそうとしたが、ベッドの上で乗りかかられているような体勢ではどうにもならない。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ま、待ってってば……、ん！」"
$ hi_mes()

$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（ざら舌で首筋を舐めないでよ、この～～～～猫っ）"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice bor_f0271
Boris "「待たない。\n
あんたがいない間、ずっとお預けだったんだから」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice bor_f0272
Boris "「俺、もう腹ぺこぺこなんだよね。\n
……食わせて」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「！」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あ、あのね、ボリス！\n
私が飛び出していく原因になった新しいアトラクションなんだけど！」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "無理矢理にでも話を切り替えねば、このまま頭からぱっくりと食べられてしまいかねない。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思って口を開くと、彼は不思議そうに私を見下ろしてきた。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0273
Boris "「ああ……、そういえばそんな話もしていたよね。\n
それで、新しいアトラクションが何？」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（よし、会話を逸らしたっ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "出て行く原因という言葉は、彼の行動を制止する効果があったようだ。\n
これを逃すことはない。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「あ、あのね、先刻ゴーランドに話してきたの。\n
クローバーの塔にいるとき、皆に相談に乗ってもらったのよ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
Boris "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「まあ、ナイトメアの案も今ひとつだったし、ユリウスは仏頂面だったけど……。\n
グレイは結構色々といい意見をくれて……」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Boris "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（…………）"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（あれ？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気のせいだろうか。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（何だか、ボリスの機嫌がどんどん悪くなっていっているような）"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
Boris "「[firstname]」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「……な、なに？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一度離れかけてくれた顔が、すぐ目の前にある。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0274
Boris "「こんな状況で、他の男の名前を出すなんて、警戒心が足りないよね。\n
久しぶりだから、忘れちゃった？」"
$ hi_mes()
show t_bor_end4 onlayer master with dis
hide t_bor_end3 with dis
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「っ」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迫った顔に後ずさろうとすると、首筋に軽いキスを落とされる。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0275
Boris "「腹減っている動物にお預けは、逆効果だよ。\n
たっぷり、思い出させてあげる」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ざらりとした舌で味見をした猫は、そう言って笑った。"
$ hi_mes()
$ hi_mes()
hide t_bor_end4 with dis
scene bo_03 with Fade(.8)
scene yum_sum_03_1 with stripe_l_medium

scene map_bg_summer_night with stripe_l_medium

scene map_bg_summer_day with Fade(1)

scene yum_sum_01_1 with stripe_l_medium

scene yun_sum_01 with stripe_l_long

play music amuse_inside_p_ali
play sound se_0755

show man_a2_2 at center
with dis
$ show_mes("frame_gen_chara")
voice suz_f0004
Customer "「へえ、新しい店が出来たんだな」"
$ hi_mes()
hide man_a2_2
show man_a2_2 at left
show man_d1_1 at right
with dis
$ show_mes("frame_gen_chara")
voice sat_f0004
Customer "「少し寄っていってみないか？」"
$ hi_mes()

show yuuen_woman_02_03 at center
hide man_a2_2
hide man_d1_1
with dis
$ show_mes("frame_gen_chara")
voice may_f0046
Park_Employee "「ありがとうございます！\n
いってらっしゃいませ！！」"
$ hi_mes()
hide yuuen_woman_02_03
show yuuen_woman_02_03 at left
show yuuen_woman_01_01 at right
with dis
$ show_mes("frame_gen_chara")
voice chi_f0048
Park_Employee "「この時間帯のお勧めはこちらのレモン・グレープです！\n
一緒に、ライムクッキーはいかがですか？」"
$ hi_mes()
hide yuuen_woman_02_03
hide yuuen_woman_01_01
show yuuen_woman_01_01 at left
show man_a1_9 at right
with dis
$ show_mes("frame_gen_chara")
voice suz_f0005
Customer "「うーん、どうするかなあ」"
$ hi_mes()

show bor_t_02_12 at center
hide yuuen_woman_01_01
hide man_a1_9
with dis
$ show_mes("frame_gen_chara")
Boris "「…………」"
$ hi_mes()
hide bor_t_02_12


show go_t_03_4 at center
with dis
$ show_mes("frame_gen_chara")
voice gor_f0363
Gowland "「おお、繁盛しているなあ。\n
さすが、[firstname]、あんたの読みはばっちりだぜ」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_5")
T "「ふふふ、そうだったら嬉しいけど。\n
まだオープンしたばっかりだもの、これからでしょう」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（でも、こんなにお客さんが来ると嬉しくなっちゃうわ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "新しく出来た店舗の前には、長蛇の列とまでは行かないが、それなりの人数が並んでいる。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "全体的に果物がモチーフの店は、見た目も可愛い。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（こういうお店だと女の子も入りやすいし）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地には飲食店がたくさんあり、レストランだけでなく、露店のような形や、移動式のものもある。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今回私が提案したのは、一種の喫茶店だ。\n
ゴーランドと新商品巡りをしたときのことを思い出して、浮かんだアイディア。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「アトラクションもいいけど、なかなかこの遊園地で斬新なものっていうのも難しいでしょう？」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「遊園地でも、ゆっくりお喋りしながら腰を落ち着けられるような場所があってもいいと思っていたのよね」"
$ hi_mes()
hide go_t_03_4
show go_t_01_2 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice gor_f0364
Gowland "「そういうところはさすがあんたらしいよなあ。\n
うちの従業員じゃなかなかそういう静かな目線には立てなくてな」"
$ hi_mes()
hide go_t_01_2
show go_t_01_3 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice gor_f0365
Gowland "「そうだな、大人の方向で攻めるっていうのも手だよなあ。\n
おまえもそう思うだろ、ボリス？」"
$ hi_mes()
hide go_t_01_3
show go_t_01_3 at left
show bor_t_01_12 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice bor_f0276
Boris "「……おっさん。\n
あんた、分かっていて、わざと言っているだろう？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一人私達から離れてベンチに座っているボリスは、不満顔だ。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（まあ、予想の範囲だけど）"
$ hi_mes()
hide go_t_01_3
show go_t_03_5 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gor_f0366
Gowland "「んー、何のことだ？\n
名案じゃねえか、女の子にも人気の喫茶店」"
$ hi_mes()
hide go_t_03_5
show go_t_02_12 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gor_f0367
Gowland "「うちにはなかった発想だぜ。\n
おまえだって、こういうところ嫌いじゃねえだろう？」"
$ hi_mes()
hide bor_t_01_12
show bor_t_01_8 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice bor_f0277
Boris "「嫌いっていうか、そういう問題じゃなくてさ」"
$ hi_mes()
hide go_t_02_12

hide bor_t_01_8


show pia_t_01_11 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice pie_f0136
Pierce "「うんうん、俺も好き。\n
ここなら窓もいっぱいあって、たくさん逃げ場があるし」"
$ hi_mes()
hide pia_t_01_11
show pia_t_03_6 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice pie_f0137
Pierce "「ジュースも甘くておいしいよ、[firstname]！\n
もうちょっと甘くてもいいかも」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「うーん、でもそれライムとオレンジのジュースでしょう？\n
多少は酸味がないとおいしくないわ」"
$ hi_mes()
hide pia_t_03_6
show pia_t_01_8 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pie_f0138
Pierce "「ちゅう……。\n
そうなの、でももっと甘くしてもおいしいよ、きっと」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（まあ、これにチーズを入れると言わないだけまだいいほうかしら）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスが持っているのは、店のジュースだ。\n
新しくオープンしたばかりだから、すべてが新製品。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスを除いて私達自身も、それぞれ何かしらの飲み物を手にしていた。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（さすがにこの中にチーズを入れると言ったら、殴りたくなるけどね）"
$ hi_mes()

show go_t_03_9 at center
hide pia_t_01_8
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice gor_f0368
Gowland "「ボリス、もっとこっち来いよ。\n
いいじゃねえか」"
$ hi_mes()
hide go_t_03_9
show go_t_03_5 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice gor_f0369
Gowland "{size=+20}「柑橘類専門の喫茶店だからって、遠慮するこたあねえだろう」{/size} "
$ hi_mes()

show bor_t_03_11 at center
hide go_t_03_5
with dis

$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice bor_f0278
Boris "「……絶対に、嫌がらせだろう、あんた」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふるふると肩を震わせていたボリスは、挑発に乗るように動き出してはみるものの……。"
$ hi_mes()
hide bor_t_03_11
show bor_t_01_4 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「～～～～っっ！！」"
$ hi_mes()
play sound se_0313
hide bor_t_01_4
show bor_t_03_3 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0279
Boris "「無理、やっぱり絶対に無理！！\n
この匂いはどうにもならないっ」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結局一定距離で足を止めると、そのまま後ろに飛び退いてしまう。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「あー」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（やっぱり、ちょっと可哀想だったかな）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "（本人の出来映えは別として）料理に関心の高いグレイから、飲食店の提案を受けたときに思いついたのだが、やはりボリスには辛いらしい。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "柑橘類は女性に人気があるし、遊園地で遊び疲れた体にもいい。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夏の季節になればさっぱりとしたものも好まれるが、猫にはやはり刺激が強すぎるようだ。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あら、じゃあ……。\n
これも嫌？」"
$ hi_mes()
play sound se_0666
hide bor_t_03_3
show bor_t_03_9 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
Boris "「……？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "警戒するように、苦い顔をしながらボリスが近付いてくる。\n
じっと、私の手元にある飲み物を凝視していた。"
$ hi_mes()
hide bor_t_03_9
show bor_t_01_9 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0280
Boris "「それ、何？」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ジュースよ。\n
これは比較的酸っぱくないタイプだけど……、いらない？」"
$ hi_mes()
hide bor_t_01_9
show bor_t_03_6 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Boris "「…………」"
$ hi_mes()
hide bor_t_03_6
show bor_t_03_6 at left
show pia_t_01_2 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice pie_f0139
Pierce "「あ、それもおいしそうだね、[firstname]！\n
ボリスが飲まないなら、俺が一緒に飲んであげる！」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ピ、ピアス？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私とボリスの間を割るように、ピアスがストローに口をつけようとする。"
$ hi_mes()
hide pia_t_01_2
show pia_t_03_1 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0140
Pierce "「ちゅう……」"
$ hi_mes()
hide pia_t_03_1
play sound se_0107
camera at vpunch
camera at hpunch
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0140_5
Pierce "{size=+20}「ぶっ！！」{/size} "
$ hi_mes()
hide bor_t_03_6
show bor_t_01_12 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0281
Boris "「……調子に乗るなよ、ピアスのくせに」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「ボリス……」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（こういうときには早いんだから）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "無理矢理吹っ飛ばされて、地面に倒れこむピアスを見やる。\n
どうやら無事のようなのだが……。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……でも、ボリスは飲んでくれないんでしょう？」"
$ hi_mes()
hide bor_t_01_12
show bor_t_02_1 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice bor_f0282
Boris "「飲むよ。\n
でも……、ストローはいらない」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「え？\n
じゃあ直接飲むの？」"
$ hi_mes()

play music boris_t_ali

show t_bor_end5 onlayer master with dis
hide bor_t_02_1

$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手許のカップを持たれたと思ったら、ボリスが口をつけ、そのまま私にキスをしてくる。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「……んん！」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
Boris "「……………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……っ」"
$ hi_mes()
hide t_bor_end5 with dis
show t_bor_end6 onlayer master with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice bor_f0283
Boris "「は……、うん、これなら飲める。\n
うまい」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！！」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぺろりと、口の周りまで舐め取ったボリスが満足げに言うが、私の顔は真っ赤だ。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0284
Boris "「[firstname]、もっと、飲ませてくれる？\n
これなら全然匂いも気にならないし、ずっとうまい」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジュースではなく私を見てボリスはそんなことを言う。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（こ、こんな飲ませ方は、さすがに毎回やっていられないわよっ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚いて声の出ない私の代わりに、ゴーランドが割って入った。"
$ hi_mes()

play music gowland_t_ali
hide t_bor_end6 with dis
show go_t_02_11 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0370
Gowland "「おいおい、ボリス。\n
遊園地でいかがわしいことするんじゃねえ」"
$ hi_mes()
hide go_t_02_11
show go_t_03_6 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0371
Gowland "「するなら、もっと物陰とかそういうところにしろって。\n
悪さする猫には、お仕置きだな」"
$ hi_mes()
hide go_t_03_6
show go_t_03_6 at left
show bor_t_01_1 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0285
Boris "「ん？お仕置きって……。\n
{size=+20}ぎゃっ！！！{/size}」"
$ hi_mes()
play sound se_0246 volume 0.6
$ flash_orange(.1)
hide bor_t_01_1
show bor_t_03_1 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「～～～～っ！？？？」"
$ hi_mes()
play sound se_0630
play sound se_0007
hide bor_t_03_1

hide go_t_03_6

$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ミカンの皮を潰して目潰しをするゴーランドと、それを受けて地面を転がるボリス。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "復活してきたピアスは、既に次の商品に夢中で周囲をまるで無視している。"
$ hi_mes()

show go_t_03_3 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0372
Gowland "「まったく、あいつ、あんたが帰ってきてからちょっと浮かれすぎだ。\n
少しはこれで目が覚め……って、うわ！」"
$ hi_mes()
play sound se_0022
$ flash(.2)

play music battle_ali
hide go_t_03_3
show go_t_03_3 at left
show bor_t_01_4 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0286
Boris "「おっさん、途中から割り込んできていきなり何するんだよ！\n
～～～～～～って、～～～～るぞ！！」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まだ目つぶしが効いているのだろう、ボリスは眼を擦りながらも銃を構えている。"
$ hi_mes()
play sound se_0509 volume 0.5
hide go_t_03_3
show go_t_01_9 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0373
Gowland "「てめえ、出来たばっかりの店に風穴開ける気か、ボリス！！」"
$ hi_mes()
play sound se_0355
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言いながら、ゴーランドも銃を構えて既に応戦体勢をとっている。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（本当に……、懲りない人達）"
$ hi_mes()
hide bor_t_01_4
show bor_t_03_3 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice bor_f0287
Boris "「だいたい、猫に優しくないような店なんてなあ……！」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「店なんて、何かしら、ボリス？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドとボリスのちょうど中間地点にいる私が、静かに口を開くと、ボリスの耳が垂れた。"
$ hi_mes()
hide bor_t_03_3
show bor_t_01_9 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「私の提案したお店がそんなに気に入らないの？」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（新店舗だって言うのに、こんなところで銃撃戦なんかしたら、最初からケチが付くでしょうが）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃弾飛び交うこの世界では、銃撃戦など珍しくもない普通のことなのかもしれない。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それがこの世界の人間の言い分だというのなら、新しく開いたばかりの店の前で怪我人を出したくないと思うのは、私の常識だ。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "譲る気はなかった。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「ボリス？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にっこりと笑みを向けると、ボリス達は視線を交わした。"
$ hi_mes()
hide bor_t_01_9
show bor_t_01_3 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0288
Boris "「な、何でもありません。\n
猫にも優しいいい店だって褒めていたんだよ、な、おっさん！」"
$ hi_mes()
hide go_t_01_9
show go_t_01_3 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0374
Gowland "「んー……、そうだったか？\n
俺にはまったく違うようにも聞こえたんだが」"
$ hi_mes()
hide bor_t_01_3
show bor_t_01_8 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0289
Boris "「だ、だから、余計なこと言うなってっ」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"
$ hi_mes()

play music honobono2_a_ali
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_4")
T "「ふふ」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（ちょっといじめすぎたかな）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "猫は匂いの強い柑橘類は苦手なことが多い。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "喫茶店の話になったときも、ここまで一点集中タイプにする気はなかったのだが……。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（従業員として、売り上げも考えていかないとね）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただの居候ではなく、お客さんでもなく、私は遊園地の一員。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "アクの強い遊園地には、個性的な店のほうがいいということで、特徴を前面に押し出す形となったのだった。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（いつかは、ボリスと来られたらいいな）"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（……苦手な場所にも入ってくれれば、だけど）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこまでの存在になれるかどうかは分からない。\n
それでも、真剣に考える程度には、私の頭も浮いている。"
$ hi_mes()
hide bor_t_01_8

hide go_t_01_3
$ hi_mes()
show yun_sum_01 with Fade(.8)
scene yum_sum_01_1 with stripe_l_medium

scene map_bg_summer_day with stripe_l_medium

scene bg_par27_im with stripe_l_long

play music forest4_p_ali
##play sound se_693 volume 0.6
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "森の中、柔らかな風に揺られるように釣り糸が水面の上で動いている。"
$ hi_mes()
play sound se_0320

show t_bor_end7 onlayer master with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0290
Boris "「よ……っと。\n
よしよし、これであとはかかるのを待つだけだなあ」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「……本当に、こんな穴場があったのね」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice bor_f0291
Boris "「勿論、猫はあちこちに行くから、誰も知らない穴場ぐらい持っているよ。\n
いい場所があるって言っただろう」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ、そうだったわね」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（というか、釣り場の話なんて忘れかけていたわよ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "家出をしたあのとき。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドと企画の件で話していた私に告げたように、彼は見つけたばかりの『穴場』につれてきてくれていた。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「今回はゴーカードじゃないのね」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達の背後にあるのは、彼が出したドアが一つだけ。\n
フレームも壁も何もない中、ドアはしっかりと立ってそこにある。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0292
Boris "「あ、車のほうがよかった？\n
せっかくタイミングよくあんたを連れ出せたから、急がなくちゃと思ってさ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0293
Boris "「何なら今から一台持ってこようか、ゴーカート？」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「いい、持ってこなくていいっ」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（あんな命がけの運転は見ているだけで心臓に悪すぎる）"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_9")
voice bor_f0294
Boris "「遠慮するなって。\n
この前の改造は結構うまくいったから、また速くなったんだぜ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_9")
voice bor_f0295
Boris "「その代わりブレーキの性能が犠牲になったけど、車なんて最後に止まってくれればブレーキなんて大して必要ないよな！」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（い、一体どういう方法で止めるつもりよ！？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "暴走運転をするボリスにとってはいいことなのかもしれないが、一緒に乗らされる身としては堪らない。"
$ hi_mes()
play sound se_0056 volume 0.5
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あ、ボリス！\n
糸、引いているわよっ、早くっ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice bor_f0296
Boris "「お、ほんとだ。\n
よし……っと、まず一匹ゲット！」"
$ hi_mes()
play sound se_0568 volume 0.7
pause 1
play sound se_0320
hide t_bor_end7 with dis
show t_bor_end8 onlayer master with dis
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "魚が釣り上げられ、ぽちゃんとバケツに入る。\n
ゴーカートの話題から逸れたことに、ほっと胸を撫で下ろした。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0297
Boris "「ふんふん、あんたがいるせいかな。\n
今回は大漁の予感がするぜ」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "魚釣りに勤しむボリスは、機嫌がいいようだ。\n
尻尾も耳も、ぴくぴくと動いている。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（こういう仕草を見ると、あの猫を思い出すわ……）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔のある街のバーで二回。\n
そして、夢現の中ではあったが、ボリスの部屋で一回。"
$ hi_mes()

play music forest2_p_ali
hide t_bor_end8 with dis
show t_bor_end9 onlayer master with dis
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ねえ、ボリス」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice bor_f0298
Boris "「ん？何、[firstname]。\n
やっぱり車一台持ってこようか？」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……そうじゃなくて」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（蒸し返さないでよ）"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あのね、クローバーの塔にいるとき。\n
変わった猫に会ったのよ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice bor_f0299
Boris "「変わった猫……？\n
そんなのあの街にいたっけ？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言葉に彼は首を傾げている。\n
尻尾がぴくりと反応するのを見ながら私は続けた。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「飼い猫らしくないんだけど、野良猫って言うには……、躾がされているというか」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "具体的に言おうと思うと、なかなか言葉が出て来ない。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（私の言葉もよく分かっている感じだったわよね）"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_6")
voice bor_f0300
Boris "「ふうん、でもそんな猫なんて大して珍しくないだろう？\n
たまたま機嫌がよかっただけかもしれないよ」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "適当な相槌を打つと、ボリスは釣り竿を持ち上げて、遠くへと糸を飛ばした。"
$ hi_mes()
play sound se_0439
pause 1
play sound se_0320
hide t_bor_end9 with dis
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（でも……。\n
雰囲気はボリスに似ていたわ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が不安定なときに寄ってきてくれる。\n
頬が腫れていたときには慰めるように触れてくれた。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「優しい猫だったの」"
$ hi_mes()

show bor_t_02_12 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
Boris "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_8")
T "「あの猫なら、私、飼ってもいいなって思うぐらいには」"
$ hi_mes()
hide bor_t_02_12
show bor_t_02_10 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_04_8")
Boris "「！！？」"
$ hi_mes()
hide bor_t_02_10
show bor_t_01_8 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_04_8")
voice bor_f0301
Boris "「何言っているんだよ、[firstname]！\n
あんた、余所の猫に浮気した挙げ句にそういうことを言うわけ？」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（浮気って……）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちょっと外の猫の話をしただけで浮気と取られては敵わないが、今は何故か話したい気持ちのほうが勝っていた。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……だって、可愛かったのよ。\n
毛並みもピンクの縞々模様で、ボリスっぽかったし」"
$ hi_mes()
hide bor_t_01_8
show bor_t_01_2 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Boris "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「私が触っていると大人しいのに、グレイが触ろうとすると警戒したりね。\n
顔の毛が長いあたりも、ボリスにそっくりで……」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「落ち着くまでじっと近くにいてくれるところも、あなたみたいだったから」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（…………）"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（……って、あれ？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで不満げだったボリスの顔が、今はどこか赤くなっているように見える。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ボリス、どうして照れているの？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隣にある顔を覗き込もうとするが、そっぽを向かれてしまう。"
$ hi_mes()
hide bor_t_01_2
show bor_t_03_13 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0302
Boris "「て、照れてなんかいないよっ。\n
ただ……、その……」"
$ hi_mes()
hide bor_t_03_13
show bor_t_01_6 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0303
Boris "「何だか、あんたに口説かれているみたいで、嬉しいなって思って」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……え？」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（私が、ボリスを口説いていた？）"
$ hi_mes()
hide bor_t_01_6
show bor_t_02_5 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_05_6")
voice bor_f0304
Boris "「その猫が俺に似ていたから飼いたかったって言われているような気がしたんだけど……？\n
違う？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "伺うように視線を向けられて、固まる。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉の意味が頭に染み込んで、今度は私のほうが赤くなった。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（い、言われてみれば……、そう聞こえてもおかしくない）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスっぽかった。\n
ボリスにそっくり。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことばかりを繰り返してしまっていた。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（は、恥ずかしい……）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "惚気るにしても程がある。\n
思わず俯いてしまうと、頬に手が触れてきて、結局上向きにされてしまった。"
$ hi_mes()
hide bor_t_02_5
show bor_t_01_13 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0305
Boris "「隠さないでよ。\n
俺の恥ずかしい顔だって見たんだから、あんたのも見せて」"
$ hi_mes()
hide bor_t_01_13
show bor_t_01_5 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0306
Boris "「おあいこ、だろう？」"
$ hi_mes()

play music happy_a_ali

show t_bor_end10 onlayer master with dis
hide bor_t_01_5

$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（あ、分かった）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頬にキスをされて、あの猫を飼いたいと思った理由が、すとんと胸に落ちる。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「飼ってもいいって思った理由も、ちゃんとあるの。\n
……私、きっと羨ましかったんだわ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
Boris "「？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "動物は言葉にしない代わりに、ボディランゲージで訴えてくる。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "余計なものを含ませない。\n
だから、伝えたいことだけしか入らない。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「私も猫になれたらよかったのになって思ったの」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（伝えたいものだけ、大切なものだけ）"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（身体で訴えられるような存在だったらよかったのに）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "素直になれない自分には、高すぎるハードルだからこそ、憧れる。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0307
Boris "「……あんたは、猫にならなくていいよ」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「え？」"
$ hi_mes()
play sound se_0551
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0308
Boris "「あんたが猫になったら、それこそ……、俺が飼っちゃうよ？\n
首輪を付けて、俺の部屋から一歩も出さない」"
$ hi_mes()
hide t_bor_end10 with dis
show t_bor_end11 onlayer master with dis
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
Boris "「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「……ん」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "重ねられた唇に答えるように、私もボリスに腕をまわす。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（……伝わっているかしら）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉も行動も、素直になるのは難しくて、気恥ずかしい。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0309
Boris "「……は」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「っ……、ふ」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「…………」"
$ hi_mes()
hide t_bor_end11 with dis
show t_bor_end12 onlayer master with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice bor_f0310
Boris "「あんたが猫になるってそういうことだよ。\n
それでも……、いい？」"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_13")
T "（…………）"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「ボリスが、私を飼うの？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "囁く響きが、何だか可笑しい。\n
だが……、悪くないな、と思った。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0311
Boris "「結構いい案だろう。\n
いかにも、あんたは俺のって感じがするし……、あ、いいかも」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目をきらきらさせているボリスは満更でもなさそうだ。\n
以前は私に飼ってくれと何度も言っていたのに、意見が変わっている。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（でも……、ボリスが飼ってくれるのなら。\n
私の家が、この人になるのかもしれないわね）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人に懐くのではなく、家に懐くのが猫の本質だ。\n
あの猫だって、今は私の腕に帰ってきている。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（ボリスが飼ってくれるのなら、私、猫になってもいい）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この人のいたいと思える家になれる自信は、未だに持てない。\n
だが、もし、繋げられるというのなら……。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_2")
T "（いつでも、この手が撫でてくれるなんて……。\n
とびきり贅沢だわ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "掴み所のないチェシャ猫に飼われる、余所者の猫。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飼って、飼われて。\n
繋ぎ合いながら、確かめていけたらいい。"
hide frame_gen_togaki with Dissolve(2)
hide t_bor_end12 with dis
show white with compress_long
show black with compress_extralong
pause 1

$ renpy.movie_cutscene("endroll_a.mpg")
#return
