jump fushigi_common2_hatter
label fushigi_nightmare2_2:

play music hatter_corridor_p_ali

scene charasel_bg_hatter_day
with stripe_l_medium

scene b_aut_01
with stripe_l_medium

scene br_01
with stripe_l_long

show eri_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice eri_f0196
Elliot "「よう、[firstname]。\n
よかったら、一緒に出かけねえか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「エリオット？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋屋敷の前を散歩していたら、現れたエリオットに声をかけられた。\n
大方、サボリがちな門番の様子でも見に来たのだろう。"

hide eri_t_01_4
show eri_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0197
Elliot "「せっかくうちに来ているんだ、ずっとこもってばかりじゃ飽きちまうだろう？\n
領地内を案内してやるよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴこぴこ。\n
まっすぐに伸びたウサギ耳を動かしながら、エリオットは誘ってくれている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「領地内って……、ブラッドの領地のこと？」"

hide eri_t_01_2
show eri_t_03a_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice eri_f0198
Elliot "「ああ、今ちょうど仕事も落ち着いているし、うちに仕掛けてきた組織も潰したばっかりだからさ」"

hide eri_t_03a_1
show eri_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice eri_f0198_5
Elliot "「あんたの行きたいところ、どこにでも案内してやれるぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（潰したばかりって……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "改めてここがマフィアの本拠地だということを思い出させられる言葉だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、引っ越し直後には多かった抗争が、落ち着いてきているらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "搭に滞在していると、ユリウスの元に運ばれてくる時計の数で、ある程度予想がつく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（だからこそ、ここに来ようと思ったんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "抗争真っ只中の帽子屋を訪れる勇気はない。\n
今は誰も欠けることなく、揃っているからこそ滞在させてもらっているのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（欠ける？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の中に浮かんだ言葉に一瞬疑問が浮かんだが、それも騒々しい気配にあっという間に掻き消されてしまった。"

play sound se_0051
camera at hpunch
camera at vpunch
hide eri_t_01_4


show dee_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0491
Dee "「ひよこウサギのくせにお姉さんを誘うなんて……。\n
お姉さんは、僕達と一緒のほうがいいよね」"

play sound se_0051
camera at hpunch
camera at vpunch
hide dee_t_01_3
show dee_t_01_3 at left

show dam_t_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0492
Dam "「どうせひよこウサギが案内する場所なんて、たかが知れているよ。\n
ね、それよりも、僕達と遊ぼうよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ディー、ダム？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後から飛びついてきた双子は、そのまま左右にぶんぶんと私を引っ張る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……何で門番が屋敷から出てくるのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結論が一つしかない疑問は、私と話をしていたエリオットも感じているに違いない。"

hide dee_t_01_3
show dee_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0493
Dee "「お姉さんは子供の誘いを断ったりしないでしょう？\n
そんなことしたら、僕達哀しくて泣いちゃうよ」"

hide dee_t_01_1
show dee_t_01_1 at left_center
hide dam_t_01_6
show dam_t_01_6 at center
show eri_t_02_10 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot "「…………」"

play sound se_0446
##special anime hit_left
pause 1
##[anime]
play sound se_0446
##special anime hit_center
pause .6
hide eri_t_02_10
show eri_t_02_9 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0199
Elliot "「勝手なことを言うんじゃねえよ、このませガキが！\n
だいたい、おまえらはこの後ピアスと一緒に仕事だろうが！！」"

hide eri_t_02_9
show eri_t_01_6 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0200
Elliot "「堂々とサボる口実に誘おうったって、そうはいかねえからな」"

hide dee_t_01_1
show dee_t_02_3 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dee "「～～っ！！！」"

hide dam_t_01_6
show dam_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam "「……！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（うわ……、痛そう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "響いた音はとんでもない大きさだった。\n
何しろ口も手も出るあの二人が、一言も発せずに呻いているぐらいだ。"

hide eri_t_01_6
show eri_t_01_11 at center
hide dee_t_02_3

hide dam_t_02_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0201
Elliot "「ったく。\n
ほら、行こうぜ、[firstname]」"

play sound se_0774
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え……、ほ、放っておいていいの！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "蹲る双子を置いて、エリオットが私の手を引く。"

hide eri_t_01_11
show eri_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0202
Elliot "「いいって、いいって。\n
仕事前の景気づけにはちょうどいいだろう」"

hide eri_t_02_1
show eri_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0203
Elliot "「おい、後は任せたぜ。\n
引き摺ってでも、縛り付けてでもいいから、そいつら引っ張っていけよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "後からやってきた使用人達に、彼はそう命令する。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先程まで私たち以外人の気配がしなかった廊下には、白い服に身を包んだ使用人達が控えていた。"

hide eri_t_02_13
show eri_t_02_13 at left
show situji_t_02_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0023
Servant "「どうせだったら、エリオット様、縛るところまでしてくれればいいのに」"

hide eri_t_02_13

hide situji_t_02_03
show situji_t_02_03 at left
show bousi_t_01_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0052
Maid "「だって仕事前には解くんですよね。\n
私達だって、面倒なお仕事は嫌ですし」"

hide situji_t_02_03
show situji_t_01_07 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0024
Servant "「門番さん達、そろそろ行きますよ～」"

hide bousi_t_01_06
show bousi_t_02_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0053
Maid "「いつまでも呻いていないで、起きてください～」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（だ、だるだるすぎる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この屋敷の人間らしいと言えばそれまでだが、それにしてもやる気があまりにない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「あの子達放っておいて、本当にいいの、エリオット？」"

hide situji_t_01_07

hide bousi_t_02_06


show eri_t_03a_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice eri_f0204
Elliot "「いいんだよ、あいつらも少しはまともに働けって」"

hide eri_t_03a_2
show eri_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice eri_f0204_5
Elliot "「仕事が出来ねえわけじゃねえのに、口を開けば休みや給料を寄こせってうるせえからな」"

hide eri_t_01_11
show eri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice eri_f0205
Elliot "「あいつらのことはどうでもいいからさ。\n
俺もせっかく休みなんだ、[firstname]」"

hide eri_t_01_8
show eri_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice eri_f0206
Elliot "「今は、俺に付き合ってくれよ。\n
あんたの行きたいところ、どこにでも連れて行ってやるから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「それじゃあ、私がエリオットを付き合わせているんじゃないの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が彼に付き合うというのなら、彼が行きたい場所に私を連れて行くという流れになるはずだ。"

hide eri_t_01_1
show eri_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0207
Elliot "「そんなことねえよ、俺があんたと一緒にのんびりしたいだけなんだからさ。\n
俺に付き合わせているだろう？」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を引いていた彼はそこで一度足を止めると、恭しく頭を下げた。\n
ただそれだけでいつもの素朴な雰囲気とは違って見える。"

hide eri_t_01_5
show eri_t_03a_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0208
Elliot "「というわけで。\n
お付き合い願えますか、お嬢様？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「……ぷっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気障な台詞が板に付いているブラッドが言うのならともかく、エリオットがこんなことを言うのがおかしい。"

hide eri_t_03a_1
show eri_t_03a_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0209
Elliot "「な、何だよ。\n
笑うことないだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「ふふふ、ごめんなさい。\n
喜んで、お付き合い致します」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（格好いいのに、可愛い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "差し出された手を取ると、彼は嬉しそうに頷いた。"

$ hi_mes()
hide eri_t_03a_4


scene br_01
with stripe_l_medium

scene b_aut_01
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_medium

scene bg_gen05_sm_aut
with stripe_l_long
play sound se_0483
pause 1
play sound se_0698

play music cheerful_a_ali

show t_nai2_1and2_5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice eri_f0210
Elliot "「だあああああっ、どうだあああっ！！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

play sound se_0040 volume .4
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「エ、エリオット……。\n
これ以上速度を上げなくていいと思うんだけど」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice eri_f0211
Elliot "「んなことはねえよ、速ければ速いほどこういうのは気持ちいいんだぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「それは否定しないけど、限度っていうものがあるでしょう！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice eri_f0212
Elliot "「手加減なんかしたら、そのほうがつまんねえって。\n
というわけで、行くぜええ！！」"

play sound se_0698
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（こ、この世界の動物は、皆してスピードマニアなの！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットが領地内を案内してくれるというので、てっきりいつものように徒歩だと思っていたのだが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "案内された場所にあったのは、今私達が乗っている自転車だった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（油断したわ）"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "前にいるエリオットにしがみつきながら、素直に従ったことを後悔する。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地のゴーカートと違い、自転車は所詮自転車だ。\n
自力で漕ぐのなら、さほどスピードも出ないだろうと高をくくっていたのだが。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

play sound se_0698
play sound se_0040 volume .4
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（これ、ボリスのゴーカートといい勝負よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかも、漕いでいるのはエリオット一人だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "任せろと言われ、後ろに横座りで乗ったときは、こんなことになるとは思っていなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（私という荷物が載って、この速度なんて……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一体、このウサギさんの足はどれだけ健脚なのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（いや、これだけ速く走れるならわざわざ自転車なんかに乗らなくてもいいんじゃ……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice eri_f0213
Elliot "「気持ちいい～。\n
あんたもそう思うだろ、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「気持ちいいけど……。\n
も、もう少し景色を見ながら行きたいような……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "風の音に負けないよう、大声で伝えてみるが、意思は尊重されそうにない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0214
Elliot "「遠慮するなって。\n
ほら、ここなんかすげえぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え……？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！？」"

play sound se_0697
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice eri_f0215
Elliot "「あー、すげえ風だなあ！\n
ほら、うちの屋敷が見えるぜ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice eri_f0216
Elliot "「大分遠くまで走ってきたなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（み、見えない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "坂を急降下していく自転車の速度に、目を開けていられない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時折薄目で見えるのは、横にある木々の流れだけだ。\n
前はエリオットがいるので、景色など見えるはずもなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（だからって、体勢を変えて落ちても嫌だし……！）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice eri_f0217
Elliot "「ほら、あそこの原っぱなんだけどさ、うまいにんじん畑があってな。\n
うちの屋敷にも運んでくれてるんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice eri_f0218
Elliot "「いっつも新鮮でさ、美味いんだよなあ。\n
にんじんジュースなんて、特に最高でさ」"

play sound se_0483
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（ま、いいか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットは先刻からあちこち紹介してくれている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もっとも……、主ににんじん関係だが、それでもその声が弾んでいるのは、確かだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（そういえば、帽子屋屋敷の中以外でエリオットに会うのって、意外と少ないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が日頃どんな仕事をしているかは、うっすらと理解している。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、覗かない。\n
知りたがらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ずるい方法と知りつつも、彼らと付き合ううちにそのスタイルに落ち着いている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……こうやって、教えてもらうのってなんだか嬉しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "上手に隠してくれている部分のほうが多いことは知っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "教えられる部分がすべてとは思わないが、それでも心を許してもらえている気がした。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0219
Elliot "「今、ちらっと見えた青い屋根の店は酒場でさ。\n
この前ブラッドと一緒に飲みに行ったんだよなあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "楽しげに話す声を聞いているだけで、私まで嬉しくなる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……へえ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice eri_f0220
Elliot "「あそこのにんじんウォッカがまた格別なんだよなあ。\n
……って、あんたは酒飲まないんだっけ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「ええ、お酒は遠慮するわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（それもウォッカなんて強いのを飲む気にはなれないし）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（いや、そもそもにんじんウォッカっていうあたりで……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice eri_f0221
Elliot "「もったいねえなあ。\n
あんたさえよければ、酒場にも案内してやったのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（遠慮しておいてよかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迂闊にイエスと答えていたら、どんな強いものを勧められていたか分からない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（それも、絶対にオレンジ色……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ね、ねえ、エリオット。\n
あなたもずっと漕ぎ通しで疲れたでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「どこかで休憩しない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時間帯は変わっていないが、あの大きな屋敷が小さく見えるほど遠くに来ている。\n
ここの辺りで一度休憩しておくほうがいいだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0222
Elliot "「そうだな。\n
あ、ちょうどいい」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0223
Elliot "「この近くに喫茶店があるから、そこに行こうぜ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0224
Elliot "「というわけで……、うおおおおおおっ！！！」"

play sound se_0483
play sound se_0698
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「だ、だから、そんなにスピード出さなくていいんだってば！！」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "より一層上がるスピードに、私は今度こそ目を閉じる。\n
振り落とされないよう、エリオットにしがみつくのが精一杯だった。"

$ hi_mes()
hide t_nai2_1and2_5


scene bg_gen05_sm_aut
with stripe_l_medium

scene bg_gen04_km_day
with stripe_l_long
play sound se_0482

play music forest_town_square_p_ali

show eri_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice eri_f0225
Elliot "「ほら、ここだぜ。\n
……って、[firstname]、あんたどうしてそんなにくたびれてんだ？」"

hide eri_t_02_5
show eri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice eri_f0226
Elliot "「乗っているだけだったよな？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「そうね、乗っているだけだったわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（身体を支えるものがないとあんなに辛いとは思わなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自転車を降りた私の顔色に疑問を訴える相手に、棒読みで答える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーカートのほうがまだ安全ベルトも、フレームもあるから身体を支えやすいが、自転車に横乗りの状態では掴まるものが何もない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（エリオットの服だけは掴んでいたけど、もっとしっかり固定するものがほしい）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "{size=+20}（どんな自転車だ、それは）{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "後部シートにベルトが付いた自転車を連想して、思わず顔が引きつった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「何でもないわ、それよりもお店に入りましょう。\n
のど、渇いちゃった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "説明するだけ無駄な気がして、エリオットを促す。"

hide eri_t_02_11
show eri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0227
Elliot "「ああ、そうだな。\n
こっちだ」"

hide eri_t_01_8

play sound se_0180

scene bg_gen04_kn_day with ImageDissolve("gui/stripe_l.png", 1, ramplen=128, reverse=True)

show tenin_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kaz_f0018
Clerk "「いらっしゃいませ、お二人様ですね。\n
お好きな席へどうぞ」"

hide tenin_1


show eri_t_03a_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0228
Elliot "「さてと……、じゃあ、あそこでいいか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が指差したのは、店の中でも奥まった場所。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ、どこでもいいわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（窓際が空いているけど、奥のほうが好きなのかしら、エリオット）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "非常口が近い場所に位置を取るのは、彼のような職種上当然かもしれない。\n
窓辺の席のほうが景色もいいだろうが、文句を言うことでもなかった。"

hide eri_t_03a_1
show eri_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0229
Elliot "「さてと……、あんた、何にする？\n
俺のお勧めは、にんじんグラッセが入ったこのパフェだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「うーん、そうねえ」"

hide eri_t_01_2

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（店の感じは個人店っぽいけど、メニューは結構充実しているわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一つ一つ手間のかかるケーキや飲み物を見ているだけでも、目移りしてしまう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0252
Unknown "「いらっしゃいませ。\n
ご注文はお決まりですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……あ、もうちょっと待って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "{size=+20}「え！？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（い、今の声って……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "メニューに向かっていた顔を持ち上げれば、そこには……。\n
顔色の悪い、片眼を隠した男が一人いた。"


play music nightmare_t_ali

show t_nai2_2 onlayer master
with dis


$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（な、なんでここにいるのよ、ナイトメア！？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice eri_f0230
Elliot "「そうだな、もうちょっと待ってくれ。\n
決まったらまた呼ぶから」"

play sound se_0213
pause .5
play sound se_0213
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice nig_f0253
Nightmare "「畏まりました。\n
それでは、お決まりになられた頃にまた伺います」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "フロア係としては定番のお決まり文句を口にしながら、彼は水の入ったコップをテーブルの上に置く。"

play sound se_0774
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの眼帯を外し、代わりに前髪で目を隠した男はそのまま静かに私達のテーブルから離れていった。"

hide t_nai2_2

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（何で、何で、何で！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他人の空似というには、似すぎている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、百歩譲って顔がたまたま似ているだけだとしても、{size=+20}あんな顔色の悪い男が二人もいては堪らない。{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……エリオット、あれって」"


show eri_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice eri_f0231
Elliot "「ああ、ナイトメアだろ？\n
あいつが自分から外に出ているなんて、珍しいよなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「そ、そういうことじゃなくて！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（どうして平然としていられるのよ！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくら病弱であっても、ナイトメアはクローバーの塔の領主だ。\n
心の読める彼はあちこちで畏怖の対象となっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼が他領土で働いているというだけでも異常事態だというのに、エリオットは止める素振りすら見せない。"


show nai_w_01_11 at center
hide eri_t_01_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0254
Nightmare "「……奧のテーブル、オーダー待ちです」"

hide nai_w_01_11
show nai_w_01_11 at left
show tenin_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oni_f0000
Clerk "「分かりました」"

hide nai_w_01_11
show nai_w_01_11 at center
hide tenin_4
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何事もなかったように彼はカウンターの奧へと入り。"

hide nai_w_01_11
show nai_w_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらりと私を振り返って、手を振って見せた。\n
それは客に対してではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "親しい人間に見せる仕草だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

hide nai_w_01_6

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（やっぱり、ナイトメアなのね……）"


show eri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice eri_f0232
Elliot "「[firstname]、決まったのか？\n
言ってくれれば、一緒に頼むぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「注文は決まったけど……。\n
エリオットは不思議じゃないわけ？」"

hide eri_t_01_8
show eri_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice eri_f0233
Elliot "「不思議って……。\n
どこがだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「だって、ナイトメアが……」"

hide eri_t_01_12
show eri_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice eri_f0234
Elliot "「他領土に来ること自体は、別に珍しいことじゃないだろ？\n
俺だってよくやるぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「他領土で、ウエイターをする領主がどこにいるのよ！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（アルバイトをするほど、塔の経済情勢が悪いとは思えないし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "領主自らが出稼ぎをするような事態になるとしたら、その前にグレイが手を打っているだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つまり、ナイトメアの判断でここまでやってきたのだ。"

hide eri_t_01_5
show eri_t_03a_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0235
Elliot "「いるだろ、あそこに」"

hide eri_t_03a_2
show eri_t_03a_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0236
Elliot "「別に構いやしねえよ。\n
うちの領地で揉めごとを起こさねえなら、放っておくだけだし」"

hide eri_t_03a_1
show eri_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0237
Elliot "「いちいち他領土の奴が来たからって、目くじらを立てていたら、キリがねえや。\n
どこかの騎士みたいに、迷い込んできては道を尋ねるようなのは別だけどよ」"

hide eri_t_01_7

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「それはそうだけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらちらと視線を向けてしまうのは、クローバーの塔を出てきたときの彼の状態を知っているからだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元々体力のないナイトメアが、他領土で働くなど……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（倒れていないでしょうね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（吐血したときにはどうしているんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢魔の名は伊達でも何でもない。\n
私に心配されるほど弱い人ではないと知っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、気にならないと言ったら、嘘になってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（大丈夫なの、ナイトメア？）"


show nai_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼には心の声が聞こえる。\n
口に出さずとも、私の声が聞こえていないはずがないのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "カウンターの中にいるウエイター姿の夢魔は、私のほうを見つめ返すことはなかった。"

$ hi_mes()
hide nai_w_01_11


$ time_effect()##PLEASE MANUALLY ADJUST ME

play music elliot_t_ali
play sound se_0546
pause 1
play sound se_0213
show t_cut_nai2u onlayer master
with dis
pause .15
hide t_cut_nai2u
show t_cut_nai2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0255
Nightmare "「お待たせ致しました。\n
スペシャルにんじんパフェと、ハニープディングです」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice eri_f0238
Elliot "「お、サンキュ。\n
ああ、いつ見てもうまそうだなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_14")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（あなたがオレンジ色のものを見て、それ以外の感想を言ったところを私は見たことがないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ウサギさんにはにんじん。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "定番のようだが、本人が幸せならそれでいいのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、ウサギではない私には、届けられたスイーツよりも気になるものがある。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不躾なほどに目の前の顔を見る。\n
赤の他人に対してこんなことをすれば、不快な思いをさせてしまうだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、相手がよく知る人間であれば話は別だ。"

hide t_cut_nai2


show nai_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0256
Nightmare "「……？」"

hide nai_w_01_11
show nai_w_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0257
Nightmare "「いかがなさいましたか、お嬢様？\n
私に何か至らぬ点がございましたか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "{size=+20}「その口調が、変だわ」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（いつもみたいに話しなさいよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞こえていないはずがない。\n
聞くなと言っても、心の声を聞いてしまうのがナイトメアだ。"

hide nai_w_01_2
show nai_w_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0258
Nightmare "「……っぷ。\n
久しぶりに会ったのに、君は相変わらずだな、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "パフェをエリオットの前に、プディングを私の前に置いたナイトメアは、突然小さく吹き出した。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも、手付きだけは丁寧に。\n
よく教育された執事のように恭しい。"

hide nai_w_01_1
show nai_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0259
Nightmare "「こういうときには、もっと別の反応をしてもらえると思ったんだがね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「例えば？」"

hide nai_w_01_11
show nai_w_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0260
Nightmare "「それは……、格好いいとか、見違えたとか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

menu:
    "格好いいわよ。":
        jump fushigi_nightmare2_3a
    "別に変わらない。":
        jump fushigi_nightmare2_3b

label fushigi_nightmare2_3a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「そうね……。\n
言われてみれば意外と似合っているわよね、その服」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ウイングカラーの長袖、黒いタイ。\n
黒のソムリエエプロン。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "色合いとしては、いつも着ているスーツとさほど変わらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただ、飾り気のない衣装は着ている人間を引き立たせてくれる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……本当に、顔がいいって得よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "中身があのナイトメアだと分かっていても、見栄えがする。"

hide nai_w_01_6
show nai_w_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0261
Nightmare "「それはよかった。\n
私としても、給仕に回るなんて滅多にない経験だからね」"

hide nai_w_01_1
show nai_w_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0262
Nightmare "「外見から入って失敗していたら、示しがつかない」"

hide nai_w_01_2
show nai_w_01_2 at left
show eri_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0239
Elliot "「ん、はあ……。\n
うまいなあ、やっぱりこのにんじんグラッセがたまらねえや」"

hide eri_t_02_8
show eri_t_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0240
Elliot "「でも、いつもよりも早く出てきたな。\n
これ、結構手間がかかるはずなのに」"

hide nai_w_01_2
show nai_w_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0263
Nightmare "「ふふふ、君のことだからそれを頼むだろうと思って、早めに準備しておいたんだ。\n
正解だっただろう？」"

hide eri_t_01_5
show eri_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0241
Elliot "「おお、気が利くな、ナイトメア。\n
意外とここの職場が似合っているんじゃねえの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "好物を堪能しているエリオットは満足そうに話しているが、そういえば肝心の話題について、私は彼に聞いていなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「……それはそうと、どうしてあなたこんな場所でウエイターなんてやっているのよ。\n
それに、塔の仕事はどうしたの？」"

jump fushigi_nightmare2_4
label fushigi_nightmare2_3b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「そんな顔色の悪い人がおいそれとあちこちにいたら、病院は大繁盛でしょうよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（見違えるほど印象は変わってないわよ）"

hide nai_w_01_6
show nai_w_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice nig_f0264
Nightmare "「うっ……、か、顔色ばかりは仕方ないだろう。\n
病弱なのは、生まれつきなんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「だから、早く病院に行って身体を治しなさいって言っているのよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（薬が苦いとか、注射が痛いとか、子供っぽい言い訳ばかりして）"

hide nai_w_01_4
show nai_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice nig_f0265
Nightmare "「こ、こんな場所にまで来て病院の話は止めてくれ。\n
それに、今の私はただの病弱な夢魔じゃない」"

hide nai_w_01_10
show nai_w_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice nig_f0266
Nightmare "{size=+20}「ウエイターに勤しむ、病弱な夢魔だ！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（病弱というカテゴリーを外さないだけ、自覚があるのか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少しも問題の解決にはなっていないが。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「それに顔色だけじゃないわ。\n
格好いいとは言えない理由は他にもあるもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見た目だけならば、充分に格好いい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、中身を、ナイトメアという存在を知っている私は、細い猫背の身体が動く度に、気が気じゃなくなる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（身体が弱いのに、接客業なんて無謀すぎるわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心が読める彼ならば誤解を招くことはないだろうが、客との距離の取り方、対応一つで、トラブルになることもあるのだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「無茶ばかりするような人を格好いいとは言えないでしょう」"

hide nai_w_01_8
show nai_w_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
Nightmare "「…………」"

hide nai_w_01_7
show nai_w_01_7 at left
hide eri_t_01_3
show eri_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice eri_f0242
Elliot "「ナイトメアは元々ひらひらした服を着ているから、あんまりイメージは変わらないかもな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "パフェを食べながらも、しっかりと聞き耳を立てていたらしいエリオットが間に入ってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんなに長い耳では、情報が入ってくるのを防ぎようもないのかもしれない。"

hide nai_w_01_7
show nai_w_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0267
Nightmare "「ふむ……。\n
大分イメージが違うと思ったんだが、これでは駄目か」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の服を見下ろしながら、ナイトメアは首を傾げてみせる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただそれだけの仕草なのに、いつもの眼帯の代わりに前髪が顔にかかっているせいで、別人のようにも見えた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「そんなことよりも、どうしてあなたここにいるの？\n
グレイも近くにいないみたいだし……、仕事は？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（まさか、仕事嫌さにここまで逃亡してきたとか言ったら、本気で怒るわよ）"

jump fushigi_nightmare2_4
label fushigi_nightmare2_4:
hide nai_w_01_3
show nai_w_01_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice nig_f0268
Nightmare "「仕事って……。\n
[firstname]、君はグレイに洗脳されていないか？」"

hide nai_w_01_12
show nai_w_01_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice nig_f0269
Nightmare "「心配せずとも、塔の仕事もしているさ。\n
これはまあ……、余暇活動というか、そういうものだ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（視線を逸らしたあたり、あやしいわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が塔を出てきたときに溜まっていた仕事の量は、並ではなかった。\n
例え彼が全力を出しても、数時間帯で終わらないだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「……余暇活動っていうのは、仕事をきちんとしている人がいう台詞よ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（サボって逃げた人が使っていい言葉じゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じろりと睨み付けると、ナイトメアはそわそわしながら視線を避けた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どう見ても、仕事を片付けて堂々と余暇活動とやらを楽しんでいるようには見えない。"


play music honobono2_a_ali

show t_nai2_3 onlayer master
with dis
hide eri_t_02_7

hide nai_w_01_7

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0270
Nightmare "「そ……、それはそうと、[firstname]。\n
君のプディングの味はどうだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「プディング？\n
これのこと？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice nig_f0271
Nightmare "「ああ、それだ。\n
私の好きな味だから、君にも気に入ってもらえると思うんだが……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（話を逸らそうとしている？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに届いてから私は食べるどころか、ナイトメアのほうばかり見ていて、まだ口を付けていなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（注文しておいて、食べないのも失礼よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "答えの代わりに、スプーンを手に取った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0272
Nightmare "「どうだ？\n
蜂蜜の甘さと、卵の味が絶妙だろう？」"

hide t_nai2_3
show t_nai2_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「……美味しいけど、そこまで言うほどじゃないような？」"

play sound se_0042 volume .7
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice nig_f0273
Nightmare "「え？ええ！？\n
このプディングが、その程度の評価とは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "プディングを口に運びながらそう評すと、ナイトメアは目に見えて落ち込む。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0274
Nightmare "「く……。\n
まだ、研究が足らないということか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（研究って……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まるで自分が作ったような言い方だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（グレイじゃあるまいし、あなた料理なんてしないじゃない）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice eri_f0243
Elliot "「そうだよなあ、やっぱりにんじんパフェが一番うまいよな、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「いや、それとこれとはまた話が違うから」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（誰もがあなたと同じウサギさんじゃないのよ）"

hide t_nai2_4


show eri_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice eri_f0244
Elliot "「ま、いいや。\n
うまかったぜ、ナイトメア」"

hide eri_t_02_4
show eri_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice eri_f0245
Elliot "「じゃ、俺らそろそろ行くから」"

hide eri_t_02_12
show eri_t_02_12 at left
show nai_w_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_16")
voice nig_f0275
Nightmare "「ああ、しばらくはここにいるから、よかったらまた寄ってくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「しばらくいるって、どういうこと？\n
勝手に塔を抜け出してきているんだったら、グレイがまた心配するわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（仕事も溜まるし、体力的にも不安要素があるのに）"

hide nai_w_01_6
show nai_w_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice nig_f0276
Nightmare "「心配しなくても、ここにいることはグレイも承知ずみだ。\n
私だって、たまには外の空気を吸いたくなることもある」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（今まで夢に引きこもって出て来なかった人が何を偉そうに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呆れた眼差しで見たが、彼には通じなかったらしい。\n
本当はどうかは分からないが、ひとまず信じるしかなさそうだ。"

hide nai_w_01_1
show nai_w_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0277
Nightmare "「色々と思うところがあったのは、君だけではないということだよ、[firstname]」"

hide nai_w_01_11
show nai_w_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0278
Nightmare "「よかったらまた遊びにおいで。\n
ああ……、そうではなかったな」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "服に相応しく一礼をした後、片眼を隠したウエイターは静かに告げた。"

hide nai_w_01_2
show nai_w_01_6 at center
hide eri_t_02_12
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0279
Nightmare "「またのお越しをお待ちしております、お嬢様」"

$ hi_mes()
hide nai_w_01_6


scene bg_gen04_kn_day
with stripe_l_medium

scene bg_gen04_km_day
with stripe_l_medium

scene bg_gen05_sm_aut
with stripe_l_long

play music quiet_night_a_ali

show t_nai2_1and2_5 onlayer master
with dis
play sound se_0483
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（ナイトメア、あのお店で何がしたいのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットの背中に寄りかかりながらの、帰り道。\n
彼が漕ぐ自転車は、帽子屋屋敷へと向かっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（追いかけてきているわけでもないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらちらと背後を振り返ってしまうのは、あの病弱な夢魔が現れるのではないかと思ってしまうからだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……そういえば」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（帽子屋屋敷に来てから、一度も夢にも出てきていないわよね、ナイトメア）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもなら呼ばなくとも出てくるのに、珍しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（ウエイター業が馴染みすぎて、夢に引きこもっていられないとか？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（そんなわけないか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の本来の領域は、夢だ。\n
現実にも出て来られる存在だが、本来であれば夢の中にあるべき存在。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（会いに来ないなんて、思わなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "反省しに行ってくると告げておきながら勝手なことだが、塔を離れても、彼ならば夢に出てくると思った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（次の夢では会えるのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢の中で呼んでみてもいいのかもしれない。\n
だが、呼んでも出てこないかもしれないと思うと、怖くなる。"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0246
Elliot "「どうしたんだ？\n
疲れたのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……ううん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ホームシックなんて、私の柄じゃないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背に頭を預けると、エリオットは心配そうに声をかけてくる。\n
前を向いている相手には表情が見えないから、丁度いい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「何でもないわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（夢でも会えないなんて、思わなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "我侭なのは分かっている。\n
それでも、顔を見てしまえば、予想以上に会いたい気持ちが募っていたことを知った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢のように掴み所がない、不思議な夢魔。\n
夢でさえ会えなくなってしまうのなら、私は一体どこで彼を捜せばいいのだろう。"

$ hi_mes()
hide t_nai2_1and2_5


scene bg_gen05_sm_aut
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_long
##endmemory
jump fushigi_common3_hatter ##i think
