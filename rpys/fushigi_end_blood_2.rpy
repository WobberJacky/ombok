label fushigi_end_blood_2:
scene map_bg_autumn_day with stripe_l_medium

scene bg_gen09_bm_aut_day_p with stripe_l_long

play music hatter_gate_p_ali fadein 1
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 木立を抜けて、見慣れた立派の門の前に辿り着く。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " すると私の姿に気付いた双子が嬉しそうに声をかけてきた。 "


show dee_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0036
Dee " 「あ、お姉さん、お姉さんだ！！\n
お帰りなさい！待っていたよ！」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_8")
T " 「ただいま、ディー。\n
久しぶり」 "

hide dee_t_01_2 at center
show dee_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_8")
voice dad_f0038
Dee " 「だって、主役がいないのにパーティなんて出来ないもんね」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 帰ってきたことを実感出来る彼らとのやりとり。\n
その中に聞き慣れない単語があったことに私は気付いてしまう。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T " 「……は？\n
パーティって何よ？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_5")
T " （うちの屋敷でパーティの予定なんてあったっけ？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " メイド見習いの立場なので、屋敷の大きな予定は頭に入れていたつもりだが、記憶にはない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " とはいうものの、この屋敷の主人はよく思いつきでイベントを企画する。\n
大方私のいない間に気まぐれでも起こしたのだろう。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_12")
T " （……また、皆に迷惑をかけて） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_2")
T " （一回だけじゃなくて、もう何回か踏んでおくべきだったかしら） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 踏みつけられたダメージが大きかったのか、私よりも遅れて屋敷に戻ろうとしている男の姿は、まだ森の奥から戻ってこない。 "

hide dee_t_01_6 at center
show dee_t_01_6 at left

show dam_t_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0039
Dam " 「うん、お帰りなさい、お姉さん。\n
お姉さんももう準備万端なんだね」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_10")
T " 「ダム、ただいま」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_14")
T " 「ねえ、ところでパーティって何のこと？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 二人にそう尋ねると、双子は同時に目を見開いて首を傾げた。 "

hide dee_t_01_6 at left
show dee_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0041
Dee " 「何を言っているの、お姉さん。\n
だって、ボスが言い出したんだよ、聞いたでしょう？」 "

hide dam_t_01_2 at right
show dam_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0042
Dam " 「そうだよ、そうだよ。\n
そのために僕達も一生懸命準備したのに」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_2")
T " （ブラッドが言い出した？） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （準備？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 何のことだかさっぱりだ。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T " 「いいえ、私、まだブラッドから何も聞いていないんだけど……」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「そもそも、パーティって何のことよ？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 聞き返した私の様子に、二人は揃って目を剥いた。 "

hide dee_t_02_11 at left
show dee_t_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0043
Dee " 「え……、ええ！？\n
お姉さん、何も聞いてなかったの、本当に！？」 "

hide dam_t_01_1 at right
show dam_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0045
Dam " 「どうしよう……、これはまずい展開だよ、兄弟。\n
ボスにばれたら超過勤務を言いつけられちゃうかもしれないよ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 二人は私を放って頭を抱えている。\n
この様子から考えて、彼らが私に隠していたのはこのパーティだったらしい。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （いつものお茶会のグレードアップ版みたいなものかしら？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " だったら使用人の一人でも私に話しておいてくれてもよさそうなものだが。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T " 「二人とも、一体どういうことなの？\n
そろそろ説明してくれないかしら」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " わたわたと慌てている双子に尋ねると、屋敷の奧から別のひとが出てくる。 "


show eri_s_01_4 at center
hide dee_t_02_7 at left

hide dam_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0026
Elliot " 「お帰り、[firstname]！\n
待っていたぜ！」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_6")
T " 「エリオット」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_15")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T " 「どうしたの、その格好？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T " 「衣装変えっていうわけじゃないんでしょう？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 会合のときに着ていたスーツと同じものだろうか。\n
きっちりと首にタイを絞めている。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_4")
T " （……普段の服が服だけに、普通の服を着ていると何か違和感があるわ） "

hide eri_s_01_4 at center
show eri_s_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_2")
voice eri_f0027
Elliot " 「まあ、こういう畏まった服なんて似合ってねえとは思うけどよ……。\n
今回の主役はあんただ。俺は全力でブラッドをサポートするつもりだからさ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 似合っていないなんてことはない。\n
むしろ体格のよさも手伝ってか、よく似合っている。 "

hide eri_s_01_1 at center
show eri_s_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0028
Elliot " 「それはそうと、もう準備も整っているからさ。\n
そろそろ始めようぜ、パーティ！」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_2")
T " 「……ねえ、エリオット。\n
ちょっと聞きたいんだけど」 "

play sound se_0493
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 中に戻ろうとする彼を引き留める。\n
そのままちょいちょいとエリオットを指で招き寄せた。 "

hide eri_s_02_4 at center
show eri_s_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0029
Elliot " 「ん、何だよ。\n
あんただってそんなドレスまで着て帰ってきたんだし、準備は終わって……」 "

play sound se_0016
hide eri_s_01_12 at center
show eri_s_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0030
Elliot " 「っ！！！！！」 "

hide eri_s_01_5 at center
show eri_s_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0031
Elliot " 「いってえ、痛いって、[firstname]！！」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 屈み込んできてくれたところを逃がさないようにしっかりと長い耳を掴む。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 痛々しい声を上げる姿に少し悪い気もするが、ここで聞き逃せばずっと誤魔化されてしまいそうだ。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_14")
T " 「先刻から皆してパーティパーティって言っているけど、そもそも何のパーティよ？\n
私、何も聞いていないんだけど」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_10")
T " （今度は逃がさないわよ） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 真っ向から問い詰めて逃げられた経験から、しっかりと握り込む。 "

hide eri_s_02_5 at center
show eri_s_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0032
Elliot " 「は！？\n
何を言ってるんだよ、[firstname]」 "

hide eri_s_02_6 at center
show eri_s_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0033
Elliot " 「今回は、あんたの……」 "

hide eri_s_01_10 at center

with dis
scene bg_gen_sky_aut_day with dis
play sound se_0502
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " エリオットの言葉を遮るように響いたのは、一発の銃声。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0185
Blood " 「誰が余計なことを言っていいと許可をしたんだ、エリオット」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T " 「ブラッド」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " いつのまに追い付いてきたのか、マシンガンを持ったブラッドが私達の背後に立っている。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （……口封じで、いちいち銃をぶっ放さないでよ） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 普段はエリオットに対して短気だと嘆いているくせに、自分だって大差がない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私達の陰にいた双子にも、銃弾は容赦しなかった。 "

play sound se_0501
pause .4
play sound se_0502
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0186
Blood " 「おまえ達も、余計なことを言う暇があるならもっと仕事を増やしてやるから、そのつもりでいることだな」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 逃げ出そうとしていた双子にマシンガンをぶっ放した我らがボスは、そんなことを言う間もだるそうだ。 "


scene bg_gen09_bm_aut_day_p with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_2")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_13")
T " 「大人げないわよ、ブラッド」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_1")
T " 「いいじゃない、うちの屋敷でパーティをするんでしょう。\n
それが何だって言うのよ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_16")
T " 「どうも、私を仲間外れにしてまで進めたかったことみたいだけど？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " いい加減種明かしにしてくれてもいいだろう。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 肝心の私はそう思うのに、彼は未だに不機嫌そうに自分の部下達を睨んでいる。 "


show bra_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Blood " 「…………」 "

hide bra_t_03_7 at center
show bra_t_03_7 at left

show eri_s_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0034
Elliot " 「ブラッド、もうそろそろいいんじゃねえ？\n
いや、それ以前にほとんどばれている気がするし……」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 助け船を出すように言ったエリオットの言葉に、彼は仕方なさそうに銃口を下ろした。 "

hide bra_t_03_7 at left
show bra_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0187
Blood " 「……ちっ。\n
まったく、お前達はこのお嬢さんに関わることでは、本当に口が軽い」 "

hide eri_s_01_10 at right
show eri_s_03a_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0035
Elliot " 「いや、だってほら、こんな格好で戻ってきていたし。\n
俺らだっててっきりブラッドから話してあるもんだと思って……」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " もごもごと反論するエリオットの言葉も、詫びる意味合いよりも、意外そうな響きのほうが強い。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_17")
T " （まあ、こんなドレス姿で戻ってきたら、普通パーティに合わせたとは思うわよね） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 何しろ、これ以上ない真っ赤なドレスだ。\n
普段着ているエプロンドレスとはまったく方向性が異なっている。 "

hide bra_t_02_10 at left
show bra_t_03_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0188
Blood " 「……はあ、仕方ない」 "

hide bra_t_03_13 at left
show bra_t_01_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0189
Blood " 「いいだろう、教えてあげよう。\n
ついてきなさい、[firstname]」 "

hide bra_t_01_12 at left

hide eri_s_03a_4 at right
with dis

play sound se_0625
pause .5
play sound se_0625
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_11")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「……偉そうに」 "

play sound se_0625
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 渋々という体で屋敷の中に戻る男の背後をついていく。 "


scene bg_gen08_bn_aut_day_p with stripe_l_extralong
play sound se_0385
stop music

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T " 「……？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_5")
T " （あれ、これってバイオリンの音？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 銃声と金属音が響き渡る帽子屋屋敷には似つかわしくない音が敷地内で響いている。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " よくよく見れば、広い庭のあちこちに並べられた外灯だけではなく、モニュメントなどにいくつもの飾りがぶら下がっている。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " これもパーティの一環なのだろうか。 "


play music hatter_garden_p_ali fadein 1

show bousi_s_01_02 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice may_f0014
Maid " 「お帰りなさいませ、お嬢様～」 "

hide bousi_s_01_02 at center
show bousi_s_01_02 at left

show situji_s_01_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice kat_f0014
Servant " 「お待ちしておりました～。\n
席はあちらですよ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T " 「……はあ」 "

hide bousi_s_01_02 at left

hide situji_s_01_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （席？） "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T " 「え……」 "


play music cheerful_a_ali fadein 1

show t_bra_end2 onlayer master with dis


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 指し示された方向を見て、足が止まった。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ずらりと使用人一同が整列している。\n
その先に誂えたように、一つの席が用意されていた。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice tan_f0013
Servant " 「おめでとうございます、お嬢様」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice chi_f0010
Maid " 「こんなおめでたい席に混ぜてもらえて、光栄です～」 "

play sound se_0654
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_7")
T " 「な、何のパーティなのよ、これ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 口々に祝いの言葉と拍手を向けられても、私の足はぴったりと止まったままだ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " だって彼らの並ぶ奧に備え付けられた席には、とびきり大きなケーキが置いてある。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " その上に置かれたプレートには、「ハッピーバースデイ」の文字と、見慣れた名前。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_7")
T " （私の名前があるってことは……） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ここまでされれば、誰を祝っているパーティなのかは私にも分かる。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0190
Blood " 「この世界では、いつでも誕生日だ。\n
同時に、いつでも誕生日ではない」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_10")
T " 「ブラッド？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " いつのまにいたのか。\n
私の横に立った男は当然のような顔をして、私を導いていく。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_03_10")
voice blo_f0191
Blood " 「だったら、いつ君の誕生日を祝うかは、祝う側の気持ち次第だろう」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_03_10")
voice blo_f0192
Blood " 「私は退屈が嫌いだからね。\n
君が一番喜ぶよう、祝いたいと思ったんだ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_11")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_03_11")
voice blo_f0193
Blood " 「サプライズ・バースデイは気に入ってもらえたかな、お嬢さん？」 "


scene bg_gen08_bn_aut_day_p with dis
hide t_bra_end2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私を席に案内した男はそう言って笑うと、手を持ち上げた。 "

play sound se_0468

show bra_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0194
Blood " 「さあ、パーティを始めよう」 "

play sound se_0473

scene bg_gen08_bn_aut_nig_p with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " それが開会の合図だったのだろう。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 先ほどまでは晴れ渡っていた空が暗くなる。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （じ、時間帯まで変えるなんて……） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 特別なときでなければ、役持ちであっても好きに時間帯を変えることは出来ない。\n
それはルールに触れるから。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 例外は時計屋と呼ばれるひとりだけだ。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_11")
T " （特別なとき……） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私の誕生日を祝うことが、この世界にとって特別なことだなんて、にわかには信じがたい。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " いつもの私なら、何を馬鹿なと否定している。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_7")
T " （なのに……、どうしよう。\n
嬉しい） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 特別扱いは嫌だと思っていたのに。\n
大切にされているのだという感覚に、胸が詰まった。 "


show situji_s_01_06 at center
hide bra_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice sat_f0002
Servant " 「おめでとうございます～！」 "

hide situji_s_01_06 at center
show situji_s_01_06 at left
show bousi_s_02_02 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice tad_f0008
Maid " 「お食事もお酒も、たっぷり用意しましたから、お好きなだけどうぞ！」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 開会の言葉でスイッチが入ったのか、庭の中は一気に騒がしくなった。 "

play sound se_0688

show bousi_s_01_02 at center
hide situji_s_01_06 at left

hide bousi_s_02_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice chi_f0011
Maid " 「ケーキ、お取りしますね。\n
これぐらいいけますよね？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_6")
T " 「え……、あ、いいっ、いい！\n
そんなにたくさんもらっても食べられないから！」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 三段重ねのケーキを一気に真っ二つにしようとした彼女を止めると、その横から長い耳がひょっこりと生えてきた。 "

hide bousi_s_01_02 at center
show bousi_s_01_02 at left
show eri_s_02_4 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0036
Elliot " 「けちけちすんなよ、[firstname]。\n
あんたのお祝いなんだぜ、ぱーっといけよ、ぱーっと！」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_9")
T " 「気持ちは嬉しいけど、いくらなんでも、そんなにたくさん食べられないわよ！」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 食べている途中で絶対に挫折するのが目に浮かぶ。 "

hide eri_s_02_4 at right
show eri_s_02_4 at left
hide bousi_s_01_02 at left
show situji_s_02_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice tan_f0014
Servant " 「小食なんですねえ。\n
エリオット様なら食べられるでしょうけど」 "

hide eri_s_02_4 at left
show eri_s_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0037
Elliot " 「そうだなあ、これがにんじんケーキだったら間違いなく食えるけどよ。\n
あ、そうか、あんたもこのケーキがにんじんケーキじゃないから食えないのか！」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 予想通りの反応。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_1")
T " （ああ、帰ってきたんだ） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " そう思うが、安堵に浸る暇も彼は与えてくれない。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_5")
T " 「違う、違う。\n
そうじゃなくて！」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 今にもキッチンに戻って手配をしようとするエリオットの服を掴んでいると、横から溜息が聞こえた。 "


show bra_t_02_14 at center
hide situji_s_02_02 at right

hide eri_s_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0195
Blood " 「今回はおまえの誕生日パーティじゃないんだ。\n
この会場まで、オレンジ色に染めるんじゃない」 "


show eri_s_02_6 at center
hide bra_t_02_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0038
Elliot " 「でもよ、ブラッド、やっぱりお祝いににんじんケーキがないなんて……」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_7")
T " 「い、いいのよ。\n
このケーキもとっても美味しそうだから！」 "

play sound se_0296
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_13")
T " 「うん、美味しい」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " お世辞ではなく本心からそう告げると、エリオットは一応納得してくれたらしい。 "

hide eri_s_02_6 at center
show eri_s_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0039
Elliot " 「ならいいけどよ。\n
遠慮すんなよ、今回のパーティはあんたが主役なんだからさ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_10")
T " 「ええ、ありがとう」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_14")
T " 「あ、よかったらエリオットも食べる？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 断ってしまったお詫びに提案すると、彼はぴくんと耳を立てた。 "

hide eri_s_01_12 at center
show eri_s_03a_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0040
Elliot " 「え？\n
い、いいのか！？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_1")
T " 「どっちにしろ、私一人じゃ食べきれないもの。\n
よかったら、一緒に食べましょうよ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " パーティに出されるケーキだ、そのうち小さく切り分けられて皆に振る舞われるだろう。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_15")
T " （でも、せっかく気を遣ってもらったし。\n
このパーティのためにきっと走り回ってくれたはずだもの） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " お礼に、少しだけフライングしても悪くはないだろう。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 既にあちこちで酒や食べ物が飛び交っているようだし、ここで少しぐらいエリオットにケーキを分けた程度、何でもないはずだ。 "


show t_bra_end3 onlayer master with dis
hide eri_s_03a_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_2")
T " 「はい、どうぞ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " フォークに乗せたケーキを差し出すと、エリオットは照れながら顔を寄せてきてくれた。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0041
Elliot " 「じゃ、じゃあ……。\n
頂きま……」 "

play sound se_0716
camera at hpunch
camera at vpunch
show t_bra_end4 onlayer master with dis
hide t_bra_end3 onlayer master with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Elliot " 「！！？」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0196
Blood " 「……ふむ、確かに悪くない味だ。\n
オレンジ色に染まっていないデザートは貴重だな」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_7")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「ブラッド、あんた、何をやっているの？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 先ほどまで目の前にあったはずの顔が消えたと思ったら、まだどこか不機嫌そうな男がそこにいる。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " しかも、がっちりと私の手を掴んでケーキまで食べて。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （にんじん料理以外のケーキが食べたかったのなら、自分で用意すればいいのに） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 少なくともあの大きなウサギさんをどかすだけの気力があるなら、そのほうがずっと早いだろう。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_2")
T " （よく分からない人） "


scene bg_gen08_bn_aut_nig_p with dis
hide t_bra_end4


show bra_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_2")
voice blo_f0197
Blood " 「たまには甘いものが欲しいときもある。\n
ふむ……、こちらのほうがもっと甘そうだ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T " 「え？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T " 「っ！？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 行儀悪くテーブルの上に乗ってきたブラッドはそのまま手を伸ばして、私の顔に触れてくる。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 舌先が猫のように動いたのを見た瞬間、私は椅子から立ち上がっていた。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_8")
T " （人前で何をするつもりよ、あんた！？） "

play sound se_0394
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 手を振り払って立ち上がった私を見ても、ブラッドは表情を変えない。\n
じっと見つめて、わざとらしい口調で続けた。 "

hide bra_t_02_2 at center
show bra_t_03_18 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Blood " 「…………」 "

hide bra_t_03_18 at center
show bra_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0198
Blood " 「ああ、忘れていた。\n
君の部屋にもう一枚ドレスを用意させておいたんだったな」 "

hide bra_t_02_6 at center
show bra_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0199
Blood " 「赤も似合うが、あのドレスもよく似合うだろう。\n
そろそろ着替えてくるといい、[firstname]」 "

hide bra_t_02_2 at center
show bra_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0200
Blood " 「君も着替えたいだろう？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T " 「は？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ブラッドは私がいかにも着たがっているように言うが、もう一枚のドレスの存在など私は聞いていない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （むしろ着替えるのなら、いつもの服で充分なんだけど） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 綺麗な服を着ることは嫌いではないが、華美な服はかえって疲れるものだ。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_17")
T " 「いえ……、別にこのドレスで充分よ」 "

play sound se_0468
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 辞退しようとしたが、彼は聞き入れてくれなかった。 "

hide bra_t_03_1 at center
show bra_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice blo_f0201
Blood " 「遠慮することはない。\n
君の謙虚さは知っているが、たまには着飾るのも悪くないだろう？」 "

hide bra_t_03_10 at center
show bra_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice blo_f0202
Blood " 「おまえ達、主役のお色直しだ。\n
手伝いに行きなさい」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ボスの合図一つで動く人間ばかりがここには揃っている。\n
すぐさま近くに控えていたメイドが私の周りに集まってきた。 "


show bousi_s_01_01 at center
hide bra_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice chi_f0012
Maid " 「かしこまりました～」 "

hide bousi_s_01_01 at center
show bousi_s_01_01 at left
show bousi_s_02_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice tad_f0009
Maid " 「はい、ではこちらへ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_6")
T " 「ちょ、ちょっと待って！」 "

hide bousi_s_01_01 at left
show bousi_s_01_01 at left_center
hide bousi_s_02_05 at right
show bousi_s_02_05 at center
show bousi_s_01_08 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_03_6")
voice may_f0015
Maid " 「お着替え、お着替え。\n
お嬢様を飾らせてもらえるなんて、人形遊びみたいで素敵です」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_7")
T " 「え！？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 聞き慣れたフレーズに思わずびくりと震える。 "


show bra_t_01_10 at center
hide bousi_s_01_01 at left_center
hide bousi_s_02_05 at center
hide bousi_s_01_08 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0203
Blood " 「人形遊びなんて、聞くだけでも気分が悪いが。\n
彼女のような人形なら悪くない」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_15")
T " （…………） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_4")
T " （まさか、ビバルディの遊びとは逆に、私を着替えさせて遊ぶ気なんじゃ……） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 人形遊びは女の子がやる分には可愛いですむが、ブラッドがすると不気味なだけだ。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （いや、むしろ気色悪い） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " そして、何をされるのかを考えるだけで気が滅入る。 "


show bousi_s_02_07 at center
hide bra_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_6")
voice chi_f0013
Maid " 「ふふふ、他の方の着替えなんて手伝うのは嫌ですけど、お嬢様なら話は別です」 "

hide bousi_s_02_07 at center
show bousi_s_02_07 at left
show bousi_s_01_08 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_6")
voice tad_f0010
Maid " 「せっかくですから、髪もセットし直しましょう～」 "

hide bousi_s_02_07 at left
show bousi_s_02_07 at left_center
hide bousi_s_01_08 at right
show bousi_s_01_08 at center
show bousi_s_02_07 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_6")
voice may_f0016
Maid " 「楽しみです～」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_12")
T " （姉が姉なら弟も弟で……） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_10")
T " （上司があれなら、部下もこうなるわ\n
け！？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 同僚でもある彼女達に屋内へと引きずられながら、そんなことを思った。 "

hide bousi_s_02_07 at left_center

hide bousi_s_01_08 at center

hide bousi_s_02_07 at right_center

$ hi_mes()

scene b_aut_03 with stripe_l_medium

scene bg_03_1 with stripe_l_long

play music hatter_guestroom_p_ali fadein 1

$ time_effect()





show bousi_s_01_08 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice may_f0017
Maid " 「うわあ、可愛いです～」 "

hide bousi_s_01_08 at center
show bousi_s_01_08 at left
show bousi_s_02_07 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice chi_f0014
Maid " 「ええ、お綺麗ですよ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ドレスを着せられた私は鏡の前に立たされていた。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 鏡の中に映っているように、身体にぴったりと吸い付くマーメイドラインのドレスは、裾が広がっている。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 少しでも身体のサイズが合わなければ、布が余ってしまって、窮屈に感じさせるデザインだ。 "

hide bousi_s_01_08 at left

hide bousi_s_02_07 at right
show bousi_s_02_07 at left
show bousi_s_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice tad_f0011
Maid " 「ぴったりですね」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_17")
T " 「そうみたいね」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （当たり前よ） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " まさか、あの男はこのドレスのために採寸をしたのではないかと、そんな邪推までしてしまう。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_5")
T " （採寸……） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_9")
T " （忘れたい） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ハートの城で行われた、彼の言うところの採寸を思い出して、頭が痛くなった。 "

hide bousi_s_02_07 at left

hide bousi_s_01_01 at right
show bousi_s_01_01 at left
show bousi_s_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice may_f0018
Maid " 「とってもお似合いですよ。\n
ボスもきっと喜びます」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_15")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_11")
T " （どうかしら） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼にしてみれば、姉と同じく、これも人形遊びの一環ではないだろうか。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T " 「……ねえ、皆も知っていたの？」 "

hide bousi_s_01_01 at left

hide bousi_s_01_02 at right
show bousi_s_01_02 at left

show bousi_s_02_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_11")
Maid " 「？」 "

hide bousi_s_02_06 at right
show bousi_s_02_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_11")
voice chi_f0015
Maid " 「知っていたとは？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_7")
T " 「このパーティのことよ。\n
皆に口止めしていたのは、ブラッドなんでしょう？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （黙っているにしても、もう少しうまく隠してくれればよかったのに） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " そうしたら、もう少し素直にこのパーティを迎えられたかもしれない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 仮定は仮定。\n
本当にそうなったかどうかは誰にも分からない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_1")
T " （でも、少なくともありがとうとは言えたわ） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " いまだにこのパーティの発案者に言えない言葉。\n
感謝を伝えたい気持ちはあるのに、胸の中で蟠って動けずにいる。 "

hide bousi_s_01_02 at left

hide bousi_s_02_04 at right
show bousi_s_02_04 at left
show bousi_s_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice tad_f0012
Maid " 「ええ、もちろん。\n
だって色々準備が必要ですから」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_2")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_16")
T " 「黙っているにしても、うまい方法があったんじゃないの？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_11")
T " （……八つ当たりだわ） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 自分の中で整理のつかない苛立ちをぶつけるなんて、最低だ。\n
怒るか、顔を顰めるかと思った同僚は、何故か楽しそうな顔で首を横に振った。 "

hide bousi_s_02_04 at left

hide bousi_s_01_01 at right
show bousi_s_01_01 at left
show bousi_s_01_08 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice may_f0019
Maid " 「だって、嬉しかったんですもの。\n
うきうきしちゃいました」 "

hide bousi_s_01_08 at right
show bousi_s_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice may_f0020
Maid " 「ねえ？」 "

hide bousi_s_01_01 at left

hide bousi_s_01_02 at right
show bousi_s_01_02 at left

show bousi_s_02_07 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice chi_f0016
Maid " 「ええ、どこかの組織を襲撃するよりも、ずっとどきどきしたんですよ！」 "

hide bousi_s_02_07 at right
show bousi_s_02_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice chi_f0017
Maid " 「爆弾を解除するよりも、ずっとずっとです」 "

hide bousi_s_01_02 at left

hide bousi_s_02_02 at right
show bousi_s_02_02 at left
show bousi_s_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice tad_f0013
Maid " 「私達だけじゃないです。\n
エリオット様も、門番さん達も……」 "

hide bousi_s_01_01 at right
show bousi_s_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice tad_f0014
Maid " 「それに、ボスだってきっと同じですよ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 浮かれるエリオットや双子なら私もよく目にしている。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " にんじん料理や休暇、給料をもらった直後の姿はまさに浮かれているとしか言えないだろう。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ブラッドの場合は、紅茶で浮かれることはあるが。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_15")
T " （私のことで、浮かれるブラッド？） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_5")
T " （珍しい紅茶を手に入れたときみたいに？） "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_11")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_4")
T " 「ごめん、想像出来ない」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼は嫌味な笑みを浮かべているか、傲岸な態度で踏ん反り返っているのが似合う人だ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 自分の立てた計画に浮かれる様なんて、イメージ出来るはずもない。 "

hide bousi_s_02_02 at left

hide bousi_s_01_01 at right
show bousi_s_01_01 at left
show bousi_s_01_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice may_f0021
Maid " 「あら、だって会場でもずっと嬉しそうだったじゃないですか、ボス」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T " 「……え？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_13")
T " （機嫌、悪そうだったけど？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼女達から見ると彼の様子はまた違ったものに見えたのだろうか。 "

hide bousi_s_01_01 at left

hide bousi_s_01_05 at right
show bousi_s_01_05 at left
show bousi_s_02_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice chi_f0018
Maid " 「浮かれているとまでは言いませんけど、でも、楽しそうでした。\n
お嬢様が屋敷を出て行ってから、ずっとつまらなそうだったんですよ」 "

hide bousi_s_01_05 at left

hide bousi_s_02_06 at right
show bousi_s_02_06 at left
show bousi_s_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice tad_f0015
Maid " 「あんなに楽しそうなボス、久しぶりに見ました～」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_11")
T " 「…………」 "

play sound se_0216
pause .4

show bra_s_01_12 at center
hide bousi_s_02_06 at left

hide bousi_s_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_03_11")
voice blo_f0204
Blood " 「着替えが終わったら下りてくるかと思えば、何を余計なことを喋っているんだ、おまえ達は」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_6")
T " 「あ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 話題に上っていた本人は、音もなく部屋の中に現れていた。\n
その顔はいつもどおりだるそうだ。 "


show bousi_s_01_02 at center
hide bra_s_01_12 at center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice may_f0022
Maid " 「お待たせしました、ボス」 "


show bra_s_01_10 at center
hide bousi_s_01_02 at center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0205
Blood " 「ああ、本当に待たされた。\n
時間帯が変わってしまうかと思ったぞ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_10")
T " 「ブラッド……」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 親しげに私の肩を抱いた男は、鏡越しに囁いてくる。 "

hide bra_s_01_10 at center
show bra_s_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0206
Blood " 「ご苦労だったな。\n
私はお嬢さんに話があるから、おまえ達は戻れ」 "


show bousi_s_01_01 at center
hide bra_s_01_3 at center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice tad_f0016
Maid " 「かしこまりました」 "

hide bousi_s_01_01 at center
show bousi_s_01_01 at left
show bousi_s_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice chi_f0019
Maid " 「それでは、失礼致します」 "

play sound se_0102
hide bousi_s_02_01 at right
hide bousi_s_01_01 at left
with dis

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_6")
T " 「え……、皆、待ってよ！」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_7")
T " （こんな状況で二人っきりになんてしないでよっ） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 命じられるままに下がっていく同僚達を呼び止めるが、彼女達は私の声など聞こえないふりして出て行ってしまった。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 残されたのは、私とブラッドだけ。 "


show bra_s_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0207
Blood " 「私とは話もしたくないのか？\n
メイドとはずいぶん楽しそうにしていたが……」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_4")
T " 「そ、そういうわけじゃないんだけど」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 本人のいないところで噂話をしていた居心地の悪さもあるが、今のブラッドには逆らいがたい雰囲気がある。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_17")
T " （このどこが楽しそうなのよ？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼の場合、一体どこに機嫌のスイッチがあるのか分からない。\n
ひょんなことで機嫌がよくもなるし、悪くもなる。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （本当に、分かりにくい） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 安易に他人に理解されたくないのだろう。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （……誤解されやすいんだってこと、分かっていてそうしているんだろうけど） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " じっと鏡の中の私を見ていたブラッドは、ふっと口元を緩めた。 "

hide bra_s_01_5 at center
show bra_s_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0208
Blood " 「思った通りだ。\n
よく似合っているじゃないか」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_1")
T " 「……それはどうも。\n
誰かさんの採寸がよっぽど的確だったんでしょう」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 棘のある言葉になってしまうのは、素直になれない私の性格だけが原因ではないと思う。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 手の内を隠している相手に、自分だけ無防備になれるはずがない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （……それも隙を見せたら、あっさりと食われそうな相手に） "

hide bra_s_03_9 at center
show bra_s_03_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_11")
voice blo_f0209
Blood " 「そうだな、測っておいてよかった。\n
この手の服は少しでもずれると、見栄えを損なう」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 出来映えを確かめるように手で触れてくる男に、心臓が跳ねそうになる。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_6")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T " 「ねえ、どうしてあんな下手な変装までして城に来たのよ？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T " 「正体がばれればただじゃすまないことぐらい、分かっていたでしょう」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 現にばらしたあと、兵士に追いかけられ、エースに絡まれた。\n
迎えに来るなら来るで、他にも色々と方法はあったはずだ。 "


play music truth_a_ali fadein 1

show t_bra_end5 onlayer master with dis
hide bra_s_03_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0210
Blood " 「悪党が誘拐をするのに、細かい理由が必要か？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「……最初はそういう雰囲気じゃなかったじゃない」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 少なくとも初めて城に来たときのブラッドには、私を取り戻す気はなかったように思う。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_2")
T " （ドレスを届けに来る前に決めていた？） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_11")
T " （それとも、本当に気紛れで決めたの？） "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_11")
voice blo_f0211
Blood " 「あの女王の元に君を置いておくのが癪に障っただけだ。\n
遅かれ早かれ私の手元に置くのなら、早いほうがいい」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_11")
voice blo_f0212
Blood " 「ちょうど、パーティの準備も整っていたしな」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_11")
voice blo_f0212_5
Blood " 「……君があの宰相殿に色目を使うつもりだったのなら、もっと早くに取り戻しておくべきだったな」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_5")
T " 「だから、違うって」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_10")
T " （……妬いていたのかしら？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 絡みついてくる手は、いつもにも増してしつこい。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " せっかく整えてもらったばかりのドレスを乱そうとしているかのように、動き回る。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " だというのに、その手を嫌がることもなく、自然に受け入れている私は何なのだろう。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_5")
T " （自分の部屋だから？） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （それとも、別の理由があるのかしら） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " どちらにせよ、パーティの衣装変えのときにやることではないと頭で分かっているのに、振り払えない。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_15")
T " 「…………」 "

show t_bra_end6 onlayer master with dis
with dis
hide t_bra_end5
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_13")
T " 「私が主役のパーティだって言うのなら、ちゃんと誘ってくれればよかったのに」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " つい不満ばかりが口をついてしまう。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_13")
Blood " 「[firstname]？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_8")
T " 「だって、こういうのってちゃんと招待されて参加するものでしょう？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_7")
T " 「招待状が欲しかったわけじゃないけど……。\n
せめて、ちゃんと誘ってくれればよかったのになって」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_7")
Blood " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 鏡に映るブラッドの顔が、ぽかーんとした。\n
彼にしては珍しく少し口が開いているが、そこから声が漏れる様子はない。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T " 「え、あの……、ブラッド？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T " 「私、何かそんな変なことを言った？」 "

show t_bra_end7 onlayer master with dis
hide t_bra_end6
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私の言葉に、彼はようやく我に返ったらしい。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_11")
Blood " 「！！！！」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_11")
voice blo_f0213
Blood " 「い、いや、何でもない。だが、君の言うことももっともだな。\n
私としたことが女性を誘うのに、言葉が足りなかったか」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_12")
T " （そうね） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_11")
T " （足りないのは、言葉だけじゃないけど） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私達の間に足りないもの。\n
間を埋めるものはきっとたくさんあって、溝なんて簡単に埋まってしまうはずなのに。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （いつも、必要にならないと埋められない） "


play music hatter_guestroom_p_ali fadein 1
hide t_bra_end7 with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼の言葉に乗るように、私もくだらないことを口にする。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_1")
T " 「そうよ。\n
せめて、誘い文句の一つぐらい言ってくれてもよかったんじゃないの？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_4")
T " 「一度ぐらい、跪いてお願いしてみたら？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 自分で言いながら失笑が浮かぶ。\n
彼のプライドの高さも、その器量も、私には不釣り合いだ。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_14")
T " （するはずがないわよね） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " されたらされたで、それはそれで、どんな仕返しが来るのかと気が気ではない。\n
だが、鏡の中のブラッドは何故か首を縦に振っていた。 "


show bra_s_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0214
Blood " 「……それもそうだな。\n
そういうことが君の望みなら、悪くない」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T " 「え？」 "

play sound se_0551

play music secret_a_ali fadein 1

show t_bra_end8 onlayer master with dis
hide bra_s_03_2 at center

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ずっと背後から絡みついていた温度がなくなったことに、私が驚く。\n
しかし、床に膝を付いた男の姿を見て私の頭は混乱のピークに達した。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_6")
T " 「！」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_10")
T " （うそでしょう） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 信じられない。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0215
Blood " 「[firstname]……。\n
いや、[firstname]＝[familyname]」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_10")
T " 「……ブラッド」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼は床に跪いて、私を見上げている。\n
あの、ブラッドが。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_7")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_7")
T " （心臓が止まるかと思った） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 城から落ちたときの衝撃なんて、これに比べればまだまだ軽い。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 息が出来ない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼が誰かに膝を折ることなんて、あるはずがない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_16")
T " （いいえ、あってはいけない） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼は組織の長で、そして領主だ。\n
誰かに簡単に屈していては、その立場にいる資格はない。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0216
Blood " 「君のエスコートは私にだけ、任せてくれないか。\n
これからも、ずっと」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_15")
Blood " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_15")
voice blo_f0217
Blood " 「君が望んだことだろう、何でそんなに顔を強ばらせているんだ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " くすりと笑みを零されて、手が伸びてくる。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " この手に捕まってしまったら、たとえ口では拒否しようとも肯定したのと変わらない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " なのに、逃げられなかった。 "

play sound se_0313
show t_bra_end9 onlayer master with dis
hide t_bra_end8 with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 引き寄せられるままに、私も床に崩れ落ちた。\n
跪いた男は、難なく私の身体を受け止めてくれる。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_3")
T " （……馬鹿みたい） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_11")
T " （あんなこと、言うんじゃなかった） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " あんなブラッドなど、心臓に悪いだけだ。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_12")
T " 「あなたが誰かにお願いなんて、似合わないわ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ふんぞり返って、気だるげに周囲を見下しながら紅茶を傾けているほうが、ずっと彼らしい。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0218
Blood " 「それは何よりだ。\n
私に膝を付かせる相手なんて、そういないからな」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0219
Blood " 「君ぐらいだろう。\n
私がたまには屈してやってもいいと思える相手は……、ね」 "

show t_bra_end10 onlayer master with dis
hide t_bra_end9
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 言葉の最後にキスを落とされて、目を閉じる。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Blood " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T " 「ん……、あ」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T " （あれ……？） "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_8")
T " 「ふ、あ……、ブラッド。\n
ちょ、ちょっと待って！」 "

show t_bra_end11 onlayer master with dis
hide t_bra_end10
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 背中を這い回る手が不埒な方向に動こうとしているのを感じて、慌てて声を上げる。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 何よりも、ブラッドの行動に乱れている心臓を知られたくなかった。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_5")
T " （早く、落ち着いてよ……） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 肌が密着するほどの距離だ。\n
彼には私の動揺なんてばれてしまっているのかもしれない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_1")
T " （こんな状態で触れられたら、全部、伝わってしまいそう） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 誰にも本音を見せない相手の、剥き出しの言葉。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " どんな美辞麗句よりも、余計なことを考えられないぐらいに絡みついてくる言葉が、心臓にまで染み込んでくる。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0220
Blood " 「何だ？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_8")
T " （何だ、じゃないわよ！） "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_9")
T " 「パーティの最中に、主役がいつまでも戻らなかったら、さすがにまずいでしょう！？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 何を平然としているのか、主催者が。\n
慌てて彼の胸を押しやるが、抱き締めてくる腕の強さに私が敵うはずがない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 逆に抱き留められてしまう。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0221
Blood " 「私が君を祝うために開いたパーティだぞ。\n
どうして我慢なんてしなければならないんだ、面倒臭い」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_17")
T " 「あんたね……」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （言い出した張本人が投げてどうするのよ） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 下で待つ部下を一体何だと思っているのか。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0222
Blood " 「それに、我慢ならもう充分したさ。\n
慣れないことはするものじゃない」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0223
Blood " 「君がいない退屈で疲れたんだ。\n
私はだるい」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T " 「は？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （退屈で疲れた？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 我が侭にも程がある。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 絶対に自分を曲げない、それだけの権力と実力を持っている男だから言える台詞だった。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「……どんな言い分よ」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_12")
voice blo_f0224
Blood " 「ずっと、我慢していただろう？\n
ハートの城から、ずっと……、な」 "

play sound se_0172
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 綺麗な形に結い上げていた髪を留めていた金具を外されて、長い髪が乱される。 "

play sound se_0117
show t_bra_end12 onlayer master with dis
hide t_bra_end11
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0225
Blood " 「この私を我慢させたんだ、その落とし前はつけてもらわないと」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_10")
T " 「だ、だから、我慢なんて……。\n
ん、ちょっと……、ブラッド！」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 屋敷に戻ってきたときと違い、床に下ろされた姿勢では足を踏んで逃げることも出来ない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 唇を奪われて、熱と鼓動だけが上がっていく。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0226
Blood " 「もう忘れてしまったのか？\n
君が欲しいと言ったばかりだろう」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0227
Blood " 「私が一度口にしたことを叶えないと思ったのか、お嬢さん？\n
だとしたら、考えは改めたほうがいい」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0228
Blood " 「私は欲しいものは絶対に手に入れる。\n
拒まれようと、逃げられようと、絶対に」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_17")
T " 「……ふ、う……、んっ」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_11")
T " （心臓がうるさい） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 落ち着けと言い聞かせても、胸の中は鼓動が駆け巡るばかりで少しも静かになってくれなかった。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_3")
T " （こんなの、期待しているみたいで……、恥ずかしいのに） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 平然と触れてくる男の冷静さが、悔しい。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Blood " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0229
Blood " 「私が傍におくと決めた……君がいないと、退屈で死んでしまう」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 聞き逃してしまいそうなほど、短い一言。\n
それを聞いただけで、力が抜けた。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_16")
T " （悔しいけど……） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_7")
T " （ああ、負けている） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 本人にはまだ伝えたくない敗北宣言。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_20")
T " （私だって、あなたがいなかったら死んでしまいそう） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼を殺すのが私の不在による退屈だとしたら。\n
私を殺すのは、彼を失う絶望だったらいい。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 誰かがいなくなったことで死ぬのなら、どんな理由をつけても結果は変わらないのだから。 "

hide t_bra_end12 with dis

$ hi_mes()

scene b_aut_03 with stripe_l_medium

scene bg_gen08_bn_aut_nig_p with stripe_l_medium

pause .8

scene charasel_bg_hatter_night with stripe_l_medium

scene map_bg_autumn_night with stripe_l_medium

scene map_bg_spring_day with stripe_l_medium

scene hm_spr_01 with stripe_l_long

play music castle_mae_p_ali fadein 1

show heisi_t_02_08 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hos_f0027
Soldier " 「おや、あなたは……。\n
ようこそ、ハートの城へ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 赤い城の兵士は私の顔を見るなり、ほっとした顔で一礼してくれる。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_18")
T " 「お久しぶり。\n
……ビバルディはいるかしら？」 "

hide heisi_t_02_08 at center
show heisi_t_02_08 at left

show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_18")
voice hei_f0029
Maid " 「ええ、いらっしゃいます。\n
今なら、ちょうど休憩中ですからお会いになれるかと」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_8")
T " 「そう。\n
じゃあ、お邪魔させてもらうわね」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 一時的に滞在していた場所というだけではなく、何度もこの場所に遊びに来ている私にとっては慣れた場所だ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 案内役などいなくても自分で行けるが、彼女は首を横に振った。 "

hide siro_t_02_01 at right
show siro_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice hei_f0030
Maid " 「いいえ、陛下より必ずご案内するように仰せつかっておりますから。\n
ご案内致します」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_7")
T " 「どうもありがとう」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_15")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_2")
T " （怒っているんだろうな……） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 堂々と侵入してきたマフィアに目の前で掻っ攫われたのだ。\n
プライドの高い女王に詫びを入れるのは、ハードルが高いだろう。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_15")
T " （でも、ちゃんと話をしないと） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " なおざりに出来ない。\n
彼女もまた私にとって大切な人だ。 "

$ hi_mes()
hide heisi_t_02_08 at left

hide siro_t_01_02 at right
with dis

scene hr_01 with stripe_l_long

play music castle_corridor_p_ali fadein 1
play sound se_0300

show siro_t_01_02 at center with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hei_f0031
Maid " 「陛下、お客様がお見えです」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0393
Vivaldi " 「……分かった。\n
客だけ入れ、おまえは入らなくてよい」 "

hide siro_t_01_02 at center
show siro_t_02_01 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hei_f0032
Maid " 「かしこまりました。\n
では、どうぞ」 "

hide siro_t_02_01 at center

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 扉の横に引いた彼女に会釈を返して、私はそっとドアのノブを握る。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_15")
T " 「……お邪魔します」 "

play sound se_0285

play music vivaldi_t_ali fadein 1

scene v_01 with stripe_l_long
pause 1.2
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_16")
T " （この前の衣装は片付けたのね） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 部屋の半分ほどを占めていた大量の衣装や小道具は、今は跡形もなく消えていた。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " しかし。 "


show viv_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice viv_f0394
Vivaldi " 「遅いぞ、[firstname]。\n
帽子屋の元に戻ってからずっと顔も見せぬとは……」 "

hide viv_t_01_8 at center
show viv_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice viv_f0395
Vivaldi " 「ああ、イライラする。\n
あの男の首を刎ねてしまえればどんなによいか」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_11")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_4")
T " （相変わらずだなあ） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 行儀悪くソファの上に寝転がった女王様は、子供のように口を尖らせている。\n
その仕草に、子供になったビバルディの姿が重なった。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_13")
T " （見た目が違うだけで、やっぱり中身はビバルディなのよね） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 大人の女性でも、私よりも小さな女の子でも。\n
どちらでも、彼女は可愛らしい。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_17")
T " （姉のようで、妹のような……） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_14")
T " （一緒にいると、落ち着く人） "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_15")
T " 「ごめんなさい。\n
ちゃんと挨拶に来ようと思っていたんだけど」 "

hide viv_t_02_2 at center
show viv_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_03_15")
voice viv_f0396
Vivaldi " 「ふん……、どうせあの嫉妬深い～～～～が邪魔でもしたのだろう。\n
ああ、やっぱりあのときに首を刎ねてしまうべきであったか」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_10")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_15")
T " （可愛いのに、可愛くないことを言っている） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " しかし、彼女の予想が見事に的中しているので、下手なことも言えない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_3")
T " （ブラッド、本当にしつこかったものね……） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " パーティのときだけではなく、以降もブラッドの部屋に呼び付けてきたり、私の部屋にやってきたり。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " なまじ私のスケジュールをすべて抑えている男だけに、暇を探すのも楽ではない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 帽子屋屋敷に戻ってからやっと訪れた自由な時間帯だった。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_13")
T " 「え、ええと、ビバルディ。\n
その、せめてものお詫びにお菓子と紅茶を持ってきたんだけど」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_15")
T " 「よかったら、一緒にお茶会にしない？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " お詫びになるかは分からないが、手にした荷物から小さな缶を取り出して見せると、不機嫌だった眼差しが少し変わった。 "

hide viv_t_02_7 at center
show viv_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_03_15")
voice viv_f0397
Vivaldi " 「何、紅茶だと？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_17")
T " 「ええ、珍しいものだと思うんだけど……。\n
これ」 "

play sound se_0335
hide viv_t_02_1 at center


scene t_cut_bra_end2u with dis

pause 1

scene t_cut_bra_end2 with dis

show viv_t_01_11 at center with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_17")
Vivaldi " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私が手にした紅茶の缶をビバルディはじっと見つめている。\n
私には缶だけで判別などつかないが、彼女なら分かるはずだ。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_5")
T " （確かこれで間違っていなかったと思うんだけど……） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 家出をするよりも前、彼が自慢げに語っていた紅茶の一つ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 隠しごとをしていたブラッドに対して、取引を持ちかけたときとは逆だ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ビバルディがブラッドを出し抜いて手に入れた紅茶があるように、ブラッドだけが確保している貴重な茶葉があってもおかしくない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " これは彼がビバルディから掠め取ったと自慢気に語っていた紅茶だった。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （姉弟だからって同じ手が通じるかは分からないけど……） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 少しでも早く彼女と仲直りをするきっかけが欲しかった。 "

hide viv_t_01_11 at center
show viv_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice viv_f0398
Vivaldi " 「おまえ、これは……？\n
帽子屋からのわらわへの貢ぎものか？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_15")
T " 「……違うわ、言ったでしょう。\n
あなたとのお茶会に持ってきたのよ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ビバルディとのお茶会のために、誰かさんのコレクションから、無断で持ってきたのである。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 発覚したら、彼はきっと不機嫌になるだろう。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （その分、色々なもので支払っているんだから、紅茶の一つや二つで目くじら立てないでほしい） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_1")
T " （本当に心が狭い） "


scene v_01 with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " あのボスは紅茶のこととなると、童心に返りすぎる。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " やがて紅茶の缶と私をまじまじと見ていたビバルディは、僅かに顔を俯かせた。 "

hide viv_t_01_5 at center
show viv_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Vivaldi " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_2")
T " 「ビバルディ？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_12")
T " （やっぱりこれじゃあ駄目かしら） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 不安げになる私の前で、彼女は肩を震わせたかと思うと、堪えきれなくなったように笑い出した。 "

hide viv_t_01_13 at center
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice viv_f0399
Vivaldi " 「ふ、ははは。\n
はははははっ、まったく、おまえは本当に可愛いことをしてくれる」 "

play sound se_0007
hide viv_t_01_3 at center
show viv_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice viv_f0400
Vivaldi " 「そうじゃな、男よりも女の友情は強いもの。\n
ふ、ふふふ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_2")
T " （そんなに目に涙が込み上げるほど笑わなくても） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （おかしかったのかしら、お茶会のお誘いに来るのが） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 確かに彼女から誘われることは多くとも、私からお茶会のお誘いをしたことはほとんどない。\n
珍しい事態には違いないが。 "

hide viv_t_03_1 at center
show viv_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice viv_f0401
Vivaldi " 「ははは、はははははっ」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （ここまで大笑いするビバルディって、何だかすごくレアな気がする） "

play sound se_0329
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 涙目になった女王は近くに置いてあった呼び鈴を手に取ると、ちりんと鳴らした。 "

play sound se_0300
hide viv_t_01_6 at center
show viv_t_01_6 at left
show siro_t_02_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_11")
voice hei_f0033
Maid " 「はい、お呼びでしょうか、女王陛下」 "

hide viv_t_01_6 at left
show viv_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_11")
voice viv_f0402
Vivaldi " 「うむ、これよりわらわはこの子と茶会をする。\n
準備をせよ」 "

hide siro_t_02_02 at right
show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_11")
voice hei_f0034
Maid " 「はい、かしこまりました」 "

hide siro_t_02_01 at right

hide viv_t_02_10 at left
show viv_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " だがいくら大爆笑していても、彼女は根っからの女王様だ。\n
寝転がって、いまだ笑った顔でも、その威厳は損なわれることはなかった。 "

hide viv_t_02_10 at center
show viv_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice viv_f0403
Vivaldi " 「ふふ、こんなに楽しい気分で茶会をするなど久しぶりじゃ。\n
おまえとのお茶会以上にわらわを満たしてくれるものはない」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_10")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T " 「ねえ、ビバルディ。\n
一つ、聞いておきたいんだけど」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 立ち上がった彼女の後ろに続きながら、小さな声で聞く。\n
ずっと気になっていたこと。 "

hide viv_t_01_4 at center


scene hr_01_s with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice pet_f0284
Peter " 「さあ、行って。\n
……そして、振り返らないでください」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0313
Ace " 「最近、調子もいいんだよなあ。\n
だから、遠慮なく……、相手をしてくれよ、帽子屋さん！」 "



$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_16")
T " （ペーターとエースがじゃれ合うのはいつものことだろうけど） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 気になったのは、エースの様子。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_3")
T " （何だか、少し……。\n
いつもと違ったような気がする） "


scene v_01 with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T " 「あの後、ペーターとエースは……」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ビバルディの部屋に来るまでに、現れなかった彼ら。\n
いつもなら呼ばなくても出てくるペーターと、神出鬼没のエース。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_5")
T " （たまたま出会わなかっただけならいいんだけど） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私とブラッドを逃がしてくれた白ウサギと、剣を振りかざしてきた騎士は今どこにいるのだろう。 "


show viv_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice viv_f0404
Vivaldi " 「ああ、あやつらか。\n
……おまえも気が多いな、愚か者共の心配までしておったのか」 "

hide viv_t_02_2 at center
show viv_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice viv_f0405
Vivaldi " 「心配するだけ馬鹿を見るぞ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T " 「え？」 "

play sound se_0319
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ノックの音も立てずに、ドアが勢いよく開く。 "


show per_t_01_2 at center
hide viv_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Peter " 「[firstname]！！！」 "

hide per_t_01_2 at center
show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice pet_f0286
Peter " 「[firstname]、[firstname]、[firstname]！\n
ああ、あなたが来てくれるまでが待ち遠しくて、待ち遠しくて」 "

hide per_t_02_13 at center
show per_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice pet_f0287
Peter " 「今度はずっとここにいてくれるんでしょう？\n
ねえ、そうですよね、ね！？」 "

hide per_t_02_12 at center
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice pet_f0288
Peter " 「あなたのためなら、僕はこの無駄に広いだけの城のワンフロアでもご用意致しますから、いつでも来てくれていいんですよっ！」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_7")
T " 「！？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_6")
T " 「ペ、ペーター」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ビバルディが横にずれたと思ったら、突然ドアが開き、そこから二人が飛び出てきた。\n
誰かなど、確認するまでもない。 "


show ace_t_03_9 at center
hide per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0320
Ace " 「冷たいなあ、[firstname]。\n
どうして陛下のところに直行なんかするんだ」 "

hide ace_t_03_9 at center
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0321
Ace " 「俺としても、君に会いたかったのにさ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T " 「エ、エース……。\n
あなたもいたの？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ペーターはともかく、また旅に出ていたのではないかと思っていたエースまで顔を出したので驚いてしまう。 "

hide ace_t_03_11 at center
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0322
Ace " 「ははは、酷いなあ。\n
俺だって壮大な冒険の旅に出ようとしたんだけど、城から外に出られなくて困っていたんだ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_17")
T " 「そ、そう」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " エースはまったく困った様子もなく、爽やかに笑う。\n
結構な時間が経っているというのに、まだこの男は城内で迷っていたらしい。 "

hide ace_t_03_3 at center
show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0323
Ace " 「ほんと、ついてないよなあ。\n
不幸体質って損なことばっかりだぜ」 "

hide ace_t_02_4 at center
show ace_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0324
Ace " 「あ、でもこうやって迷っていたおかげで君に会えたなら、それはそれでついているのかもな」 "

hide ace_t_02_1 at center
show ace_t_02_1 at left
show per_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice pet_f0289
Peter " 「あなたの迷子癖なんて今更でしょう。\n
ああ、死んだら直るかもしれません……、一度試してみましょうか？」 "

play sound se_0023
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 時計を銃に変えて、ペーターは提案してくる。 "

hide ace_t_02_1 at left
show ace_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0325
Ace " 「ペーターさん、直っても死んでいたら意味がないだろう？」 "

hide ace_t_03_2 at left
show ace_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0326
Ace " 「それに、それでも直っていなかったら殺してくれたペーターさんに申し訳なくて、俺、化けて出てきちゃうぜ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_10")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_12")
T " （本当にいつも通りね、この人達） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 少しでも心配した私の立場は一体なんだったのだろう。 "


show viv_t_03_11 at center
hide ace_t_01_1 at left
hide per_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice viv_f0406
Vivaldi " 「言ったであろう、心配するだけ無駄だ。\n
そんなことに気持ちを割くぐらいなら、仕事をしたほうがまだ前向きというものじゃ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " きっぱりと言いきるビバルディの言葉には頷くしかない。 "

hide viv_t_03_11 at center


scene bg_gen_sky_spr_day with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_13")
T " （でも……） "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_13")
voice pet_f0290
Peter " 「死んでからもわざわざ迷い出て来なくて結構です。\n
心置きなく、死んでください、エース君」 "

play sound se_0501
pause .1
play sound se_0682
pause 0.5
play sound se_0502
pause .1
play sound se_0683
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_13")
voice ace_f0327
Ace " 「ははは、照れなくてもいいのに。\n
仲間意識の違いかなあ、俺が死んだ後にペーターさんが嘆きそうで心配だよ」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_10")
T " （物騒だけど、いつものやりとり） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " この赤い城が変わらずにある。\n
そんな当たり前のことに、何故かとてもほっとした。 "

$ hi_mes()
pause
pause .8

scene map_bg_spring_day with stripe_l_medium

scene bg_gen03_hjm_spr_day with stripe_l_long

play music forest_town_square_p_ali fadein 1
play sound se_0580
pause .2
play sound se_0580
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ビバルディとのお茶会も終わり、屋敷へと戻る道。\n
ハートの城の城下町を歩く私の隣には、赤い騎士がいた。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「……エース、どうしてついてくるの？」 "


pause
pause .8


show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_12")
voice ace_f0328
Ace " 「言っただろう、俺、城の中から出られなくて困っていたんだ」 "

hide ace_t_03_11 at center
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_12")
voice ace_f0328_5
Ace " 「君は帽子屋屋敷に帰るって言うし、一緒に行けば少なくとも城からは出られるだろう？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_5")
T " 「それはそうだけど……。\n
屋敷の中にまでついてくるのは、なしにしてよ」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_12")
T " （この前みたいにいきなり銃撃戦になったら大変だもの） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " あのときはブラッドにとっての敵地だったが、今度はエースにとっての敵地だ。\n
その上、彼は人を怒らせることにかけては右に出る者がいない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （ディーやダムだってムキになるし、エリオットだって考えずに撃つタイプだし） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_12")
T " （ブラッドは、面倒なことは嫌だって最初から避けそう） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 何ごともなくすむ保証がない以上は、余計な騒動は極力避けてほしい。 "

hide ace_t_03_10 at center
show ace_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0329
Ace " 「ふうん。\n
俺が屋敷の中に入るのは、そんなに嫌なんだ？」 "

hide ace_t_03_9 at center
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0330
Ace " 「俺は君が城に遊びに来てくれるのを結構楽しみにしているんだけどなあ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「……ありがとう。\n
そう思うんだったら、もう少し城にいてくれればいいのに」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼はいつもふらふらと迷い歩いている。\n
領土外で顔を合わせたことも、一度や二度ではない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 会いに来ても会えなかったことなど、珍しくなかった。 "

hide ace_t_03_11 at center
show ace_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0331
Ace " 「仕方ないさ、自由を求める旅はそう簡単には終わらないものなんだ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_17")
T " 「……あなたの場合、迷ってばかりでしょうが。\n
自由を求めているのか、旅を求めているのか、分からないわ」 "

hide ace_t_02_1 at center
show ace_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
Ace " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 何気なく応じただけの言葉だったが、私の一言でエースはにこりと笑った。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ただし、その身に纏う空気はぐっと冷たいものになっていた。 "

hide ace_t_02_13 at center
show ace_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice ace_f0332
Ace " 「うん、そうかもな。\n
何を探しているのかも、迷っているのかもしれない」 "

hide ace_t_02_12 at center
show ace_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice ace_f0333
Ace " 「ぶれてばかりだ。\n
一つでも答えが決まったら、こんな俺でも迷わなくなるのかな」 "

hide ace_t_02_11 at center
show ace_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice ace_f0334
Ace " 「どう思う、帽子屋さん？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T " 「え？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_7")
T " （！！！） "


play music tension_a_ali fadein 1
hide ace_t_03_12 at center
show ace_t_03_12 at left
show bra_t_03_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_03_7")
voice blo_f0230
Blood " 「おまえの事情など知るか。\n
私と関わりのないところで、永遠に迷っていればいい」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T " 「ブラッド」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 人混みの中現れたブラッドの姿に私は目を剥く。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T " （昼間に出掛けてくるなんて……） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （それも、ハートの城の領土に） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 仕事絡みだろうかと思ったが、彼の周囲にはエリオットや他の構成員の姿はない。\n
ファミリーの用事ならば、誰か供を連れ立って来ているはずだ。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_10")
T " （……追いかけてきたの？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ここまで来たことに驚く私を置いて、二人はそれぞれ好き勝手なことを言っている。 "

hide ace_t_03_12 at left
show ace_t_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_11")
voice ace_f0335
Ace " 「ははは、冷たいなあ。\n
でもせっかくここで会えたんだから、もう少し相手をしていってもらおうかな」 "

hide ace_t_01_4 at left
show ace_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_11")
voice ace_f0336
Ace " 「この前の続きでも悪くないし」 "

play sound se_0443
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " あっさりと剣を抜いたエースと違い、ブラッドは相変わらずひとを食ったような笑みを浮かべている。 "

hide bra_t_03_14 at right
show bra_t_03_19 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_11")
Blood " 「…………」 "

hide bra_t_03_19 at right
show bra_t_02_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_11")
voice blo_f0231
Blood " 「くだらんな。\n
私にはやりあう理由がない」 "

hide bra_t_02_14 at right
show bra_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_11")
voice blo_f0232
Blood " 「それも、ハートの城の騎士殿がお相手となれば、尚のこと。\n
罪人の始末は、『騎士』の本業ではないだろう？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_2")
T " 「？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （何だか妙なところにアクセントが入っていなかった？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 気のせいだろうか。 "

hide ace_t_01_10 at left
show ace_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0337
Ace " 「うーん……、でも、俺、まだ迷っているし。\n
結論を出すための、ヒントの一つにでもなるかと思ってさ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 言いながら、エースは既に剣を構えている。\n
一方のブラッドはいまだステッキを持ったまま、微動だにしない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_8")
T " （ど、どうしよう） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 周りへの被害など気にしていられない。\n
ここでこのまま二人が仕掛けあえば、この前と同じように……。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice hos_f0028
Soldier " 「エース様、こんなところにいらしたのですね！」 "

play sound se_0312
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 背後から響いてきたのは、幾つもの足音。 "

hide bra_t_02_2 at right
show bra_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0233
Blood " 「何だ？\n
騒々しい」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T " 「足音？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_5")
T " （それも、一人じゃないみたいだけど） "


show heisi_t_02_10 at center
hide ace_t_03_2 at left
hide bra_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_5")
voice hos_f0029
Soldier " 「ああ、ようやく追い付きました。\n
エース様」 "

hide heisi_t_02_10 at center
show heisi_t_02_10 at left
show heisi_t_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_5")
voice oto_f0022
Soldier " 「よかった、まだ城下にいらっしゃった」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 安堵の表情を浮かべて私達の元に駆け寄ってきたのは、ハートの城の兵士達だった。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ブラッドに用かと思ったが、彼らの視線は赤い騎士へと向かっている。 "


show ace_t_03_2 at center
hide heisi_t_02_10 at left
hide heisi_t_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_5")
Ace " 「？」 "

hide ace_t_03_2 at center
show ace_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_5")
voice ace_f0338
Ace " 「どうしたんだ、俺に何か用？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " エースにも心当たりはないのか、不思議そうに問い返すがまだ剣を納める気配はなかった。 "


show heisi_t_02_01 at center
hide ace_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_5")
voice hos_f0030
Soldier " 「陛下がお呼びです。\n
すぐに戻るようにと」 "

hide heisi_t_02_01 at center
show heisi_t_02_01 at left
show heisi_t_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_5")
voice oto_f0023
Soldier " 「陛下直々のご命令です、どうか城にお戻りください」 "


show ace_t_02_12 at center
hide heisi_t_02_01 at left
hide heisi_t_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_5")
Ace " 「…………」 "

hide ace_t_02_12 at center
show ace_t_02_12 at left
show bra_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_5")
voice blo_f0234
Blood " 「どうする？\n
命令違反をするか、『騎士』殿？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " せせら笑うブラッドの言葉にも、しばらくエースは答えなかった。\n
ちらりと自分を追いかけてきた兵士達を見て、肩を竦める。 "

hide ace_t_02_12 at left
show ace_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0339
Ace " 「陛下の命令なら、それは優先されるべきだろうな。\n
逆らうなんて、騎士として失格だ」 "

hide bra_t_03_10 at right
show bra_t_03_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0235
Blood " 「……なら、とっととその子を返してもらおうか」 "

play sound se_0551
hide bra_t_03_14 at right
show bra_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0236
Blood " 「彼女は私のものだ。\n
女王でも、ましてや迷子のものでもない」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 引き寄せてきた腕の力は思った以上に強い。\n
顔を見上げれば、気怠げな表情が見えたが、それだけではない。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_16")
T " （…………） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_8")
T " （警戒、している？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " エースは引くといったのに、彼は何を警戒しているのだろう。 "

hide ace_t_02_6 at left
show ace_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice ace_f0340
Ace " 「そうだね、まだ迷っているんじゃ駄目そうだ。\n
帽子屋さんに相手をしてもらうのはまた次の機会にしよう」 "

play sound se_0438
play sound se_0769

play music forest_town_square_p_ali fadein 1
hide bra_t_02_11 at right
show ace_t_03_11 at center
hide ace_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 大剣をしまったエースは、そのまま何でもなかったように背を向けて歩き始めた。 "


show heisi_t_02_10 at center
hide ace_t_03_11 at center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice hos_f0031
Soldier " 「それでは、失礼致します」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T " 「……あなた達は、いいの？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 今回ブラッドは、何の変装もしていない。\n
前回のように見ないふりは出来ないはずだ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 互いに顔を見合わせた兵士達は、口元に指を押し当てて小さく首を振った。 "

hide heisi_t_02_10 at center
show heisi_t_02_10 at left
show heisi_t_01_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice oto_f0024
Soldier " 「私達は、エース様をお迎えにいくのが命令でしたから」 "


show bra_t_02_18 at center
hide heisi_t_02_10 at left
hide heisi_t_01_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0237
Blood " 「ふん、城にも分別を弁えている者はいるらしいな。\n
帰るぞ、[firstname]」 "

play sound se_0492
play sound se_0365
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_7")
T " 「あ、ちょ、ちょっと！」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 問答無用で引きずっていく手は、しっかりと私を掴んでいて離さない。 "

hide bra_t_02_18 at center
show bra_t_03_19 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0238
Blood " 「君とはよくよく話し合う必要がありそうだ」 "

hide bra_t_03_19 at center
show bra_t_03_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0238_5
Blood " 「私のお気に入りの茶葉まで持ち出して、何をするかと思えば……、ハートの城で騎士と浮気か？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_13")
T " 「エースはたまたまついてきただけよ。\n
紅茶はビバルディに……」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_7")
T " 「！！！」 "


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " しまったと思ったときには既に遅い。\n
酷薄に輝いている緑の瞳に睨まれてしまった。 "

hide bra_t_03_16 at center
show bra_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_03_7")
voice blo_f0239
Blood " 「ほう」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 溜息のような短い一言。\n
だが、そこに込められた迫力は私の唇を凍らせるほどの威力があった。 "

hide bra_t_01_9 at center
show bra_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0240
Blood " 「やはり、あの女は危険らしい。\n
君を誑かすとは、一体どんな手管を使ったのか、私もぜひ聞かせてもらうとしよう」 "

hide bra_t_01_10 at center
show bra_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0241
Blood " 「誰の邪魔も入らないよう。\n
私の部屋で、ゆっくりとね」 "

play sound se_0365
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_11")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_4")
T " （こんなことなら、エースと戦わせていたほうがよかったかしら） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 少なくとも彼とぶつかったあとなら、そんな元気もなかったのではないだろうか。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_10")
T " （ブラッドが無事だったけど……） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_9")
T " （代わりに、私のほうが保たなそう） "

$ hi_mes()
hide bra_t_01_3 at center


scene map_bg_spring_day with stripe_l_medium

scene map_bg_autumn_day with Dissolve(.8)

play music dream_inside_p_ali fadein 1
play sound se_0775
play sound se_0478

show black onlayer master with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T " 「……ん、んん」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_1")
T " （何の音だろう？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 身体がふわふわと浮くような感覚。\n
足下が定まらないような、そんな不安定な感覚がある。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 夢魔が夢に入ってきたのかと思ったが、違う。\n
身体も意識も半分起きて、半分がまだ眠っているのだ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 目を開けようとしても、なかなかそうすることが出来ない。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0242
Blood " 「もうすぐ着くから、それまではよく眠っていなさい」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_1")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_12")
T " （ブラッド？） "

play sound se_0478
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 抱き上げられているせいか、耳元に固い音が届く。\n
時計の音。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " この世界では、私以外の人は皆、この音を生み出している。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_1")
T " （音は固いけど） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_10")
T " （あったかい） "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_10")
Blood " 「…………」 "

play sound se_0775
play sound se_0284
pause .2
play sound se_0230
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_10")
voice blo_f0243
Blood " 「着いたぞ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T " 「…………？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_1")
T " （着いたって、どこに？） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ハートの城の領土から戻って以来、ずっとブラッドの部屋に押し込められていたはずだ。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 屋敷の外にでも出たのだろうか。\n
顔に風が当たってくる。 "


play music night_garden_p_ali fadein 1

scene bg_gen_sky_aut_nig with open_long
hide black

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_17")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_3")
T " 「…………ん、ブラッド？」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_3")
voice blo_f0244
Blood " 「こんばんは、お嬢さん」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_3")
voice blo_f0245
Blood " 「ふふ、ずいぶん気持ちよさそうに眠っていたじゃないか。\n
私の腕の中は、そんなに気持ちがよかったのかな」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_10")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_11")
T " 「あんたが無茶ばかりさせるからでしょう」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " よく寝ていたというのなら、熟睡する原因となったのは間違いなくこの男だ。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0246
Blood " 「そうつれないことを言わないでくれ。\n
私だってまったく傷つかないわけじゃないんだ」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0247
Blood " 「君がよりにもよって秘蔵の紅茶を持って女王に会いに行ったり、騎士とふらふらしたりしているから、しっかり繋ぎ止めておいてあげようと思っただけさ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_10")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_15")
T " （繋ぎ止めるどころか、生命に危機を感じたわよ） "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T " 「それはともかく、ここ……。\n
屋上？」 "


play music quiet_night_a_ali fadein 1

show t_bra_end13 onlayer master with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 眼下にはいつものお茶会用のテーブルや、庭を飾るオブジェが見える。\n
どうやらここは帽子屋屋敷の屋上らしい。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0248
Blood " 「ああ、あまりここには来たことがなかっただろう？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T " 「まあ確かにないけど……。\n
こんなところに連れてきて、何をする気なの？」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_15")
voice blo_f0249
Blood " 「ふ……。さあ、何をしようか。\n
君が喜ぶなら、多少の面倒は聞いてやってもいいが」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " わざといやらしい口調で言うが、何の目的もなしに彼がこんな場所に私を連れて来るはずがない。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_2")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_1")
T " 「あまりもったいぶるなら、帰るわよ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 屋上の床に下り立った私はそのまま背を向けようとしたが、からかうような声が引き留めた。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_1")
voice blo_f0250
Blood " 「おや、帰るのか？\n
どうやって？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_16")
T " 「決まっているじゃない、歩いて……」 "

play sound se_0262
show t_bra_end14 onlayer master with dis
hide t_bra_end13
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T " 「……それは、何？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_5")
T " （まさか、ブラッド） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 勝者の表情を浮かべながら鍵を手にしたブラッドは楽しげだ。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_5")
voice blo_f0251
Blood " 「ここには関係者、いや帽子屋ファミリーの中でも限られた人間しか入れないんだ。\n
鍵ぐらいかけてあって当然だろう？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_14")
T " 「一体何がしたいのよ、あんた」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_2")
T " （勝手にこんなところに連れてきた挙げ句、監禁宣言って） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 屋上には私達が抜けてきた扉があるが、そこには既に鍵かかかっているのだろう。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0252
Blood " 「欲しいか？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_7")
T " 「……いや、いらない」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼がこういうことを言うときは、間違いなく裏がある。\n
受け取ったが最後、見返りにとんでもないことを要求してきそうだ。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0253
Blood " 「おや、ではここからどうやって出る気かな？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 鍵を振るブラッドは私から視線を外そうとしない。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_13")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_2")
T " （どうあっても、受け取らせたいわけね） "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「分かった、じゃあ頂くわ」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_12")
voice blo_f0254
Blood " 「ああ、どうぞ」 "

play sound se_0262
show t_bra_end15 onlayer master with dis
hide t_bra_end14
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 手渡された鍵は、普通の鍵のようだ。\n
とてもそんな機密を抱えたものには思えなかった。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_11")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「これで、本当に開くんでしょうね？」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_12")
voice blo_f0255
Blood " 「ああ、開くよ。\n
ここに繋がるドアだけじゃない、この屋敷のどこにでも出入り出来る」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_2")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_4")
T " 「え？」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T " 「どこにでもって……。\n
どこにでも！？」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
voice blo_f0256
Blood " 「ああ、どこにでも出入りが出来る。\n
武器庫に、倉庫、君が今まで立ち入ったことのない場所であっても、それを持っている限りはね」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
voice blo_f0257
Blood " 「この屋敷のマスターキーというやつだな。\n
スペアはないから、なくさないように気を付けなさい」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T " 「…………」 "

play sound se_0313
show t_bra_end16 onlayer master with dis
hide t_bra_end15
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_8")
T " {size=+23}「い、いらない！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 手にした鍵が見た目以上の危険をはらんでいたことに遅まきながら私は気付かされて、顔色を変えた。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " こんなものを受け取れるほど私の器は大きくない "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 慌てて突き返そうとしたが、ブラッドは受け取ろうとはしなかった。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0258
Blood " 「そう言うな。\n
私からの誕生日プレゼントだと思ってくれ」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_9")
T " 「なくしたらどうするのよ、そんな大事なもの！？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " この屋敷の機密に関わる部分に、私は関わっていない。\n
だが、どこにでも入れるということは、それらを丸裸に出来るも同然だ。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T " （信頼されて嬉しいというよりも、何かあったらと思うと……。\n
こんな怖いものは受け取れない） "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_11")
voice blo_f0259
Blood " 「そう思うのなら、使わずに部屋に置いておけばいい。\n
鍵は鍵だ、使わないのであれば暴発する心配がない分、銃よりもずっと大人しい」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_8")
T " 「持っていることが嫌なのよっ。\n
いいから、返す、返すから！！」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_8")
voice blo_f0260
Blood " 「断る」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 眼前に突きつけるように鍵を差し出したが、ブラッドは腕を組んだまま動こうとしない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼の頑固さは私もよく知っている。\n
こうと決めたらテコでも動かないだろう。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_11")
T " 「そもそも、何で、いきなりこんなものを渡そうなんて思ったのよ」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_10")
T " （こんな合い鍵、一度でも欲しがったことはないのに） "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_05_10")
Blood " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_05_10")
voice blo_f0261
Blood " 「隠し事は嫌なんだろう？\n
だから、それを渡しておくことにした」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_2")
T " 「？」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_2")
voice blo_f0262
Blood " 「君を私のファミリーに加える気はないが、君が知りたいと思う気持ちを否定することもしない」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_2")
voice blo_f0262_5
Blood " 「なら、あとは君に選んでもらったほうが面倒でなくていい」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_2")
voice blo_f0263
Blood " 「屋敷内を隈なく探検しろというわけじゃないさ。\n
見たいものを見て、見たくないものは見ないでいることも自己防衛だ」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_2")
voice blo_f0264
Blood " 「道具は使い方次第でどうとでもなる。\n
持ち主次第さ」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_2")
voice blo_f0265
Blood " 「爆薬や銃弾と、大差ない」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 余計なことを知れば知るほど、誰かから狙われる可能性も高くなる。\n
帽子屋屋敷に滞在して、何度か銃撃戦に巻き込まれたこともあった。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " だから、見たくないのなら見ないままでいいと彼は言うのだろう。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 使うも使わないのも、私次第だと。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T " 「だったら、こんなものを渡さなくても……。\n
このままでいいのに」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （もらっても、もらわなくても変わらないのなら、重荷はいらない） "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_6")
Blood " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_6")
Blood " 「[firstname]」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T " 「？」 "

play sound se_0551
show t_bra_end17 onlayer master with dis
hide t_bra_end16
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " この鍵を持つということは、それらに手を伸ばせるということ。 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0266
Blood " 「言っただろう、鍵はただの鍵。\n
せっかくプレゼントすると言っているんだ、受け取っておきなさい」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0267
Blood " 「それに、いずれ鍵よりもずっと重いものを受け取ってもらう。\n
そんなもので怖じ気づいていては話にならない」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T " 「え？」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （この鍵よりも重いもの？） "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_17")
T " 「これ、たった一本の割に結構重いんだけど……？」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
Blood " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice blo_f0268
Blood " 「いや、それよりもずっとずっと重いものさ。\n
墓の下、棺桶の中にまで持ち込ませてやる」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice blo_f0269
Blood " 「この屋敷よりもずっと大きくて、そして誰にも肩代わり出来ないものだが。\n
君には受け取ってもらわなければ」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice blo_f0270
Blood " 「背負わせるつもりはなかったが、君にその覚悟があるなら、私はいつでも構わないよ」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_6")
T " （重くて、大きいもの） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼がここまで言うものだ。\n
脅されているわけでもないのに、肩が震えた。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T " 「……そんなものを私一人が背負うの？」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 明確な言葉にされなくとも、それが何なのか、頭に染み込んでくる。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 眼下に見下ろす屋敷の庭。\n
だが、そこにあるのはただの庭だけではない。 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼の部下が生きて、そして支配する領土がある。 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_16")
T " （耐えきれない） "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_3")
T " （潰れてしまいそう） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私には、重すぎるものだ。 "

show t_bra_end18 onlayer master with dis
hide t_bra_end17
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0271
Blood " 「君は私のものだろう？なら、私のものも君のものだ。\n
受け取らせる以上は、責任を持って最後まで付き合うさ」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_10")
T " （付き合うって……） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " その言葉の意味が分からないはずがなかった。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_7")
T " 「…………」 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_3")
T " 「ええ。\n
責任をとってもらわなくちゃ」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 選んだのは、ブラッド。\n
そして、受け取ったのは私。 "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_4")
T " 「ずっと巻き込んであげる」 "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_1")
T " （支え合うなんて、綺麗な言葉は似合わない） "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 引っ張り回してしまうほうが、ずっと私達らしい。 "

hide t_bra_end18 with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0272
Blood " 「ふ……。\n
それは退屈しなくていいな」 "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0273
Blood " 「他の男を巻き込むぐらいなら、いくらでも付き合ってやろう。\n
お嬢さんのお気に召すまま」 "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 慇懃無礼な唇が、手の甲に触れる。\n
手の中の鍵が、ほんの少しだけ軽くなったような気がした。 "
hide ali_t_06_16 with Dissolve(2)
hide frame_gen_togaki with Dissolve(2)

show white onlayer master with compress_extralong
show black onlayer master with ImageDissolve("gui/compress.png", 6, ramplen=128, reverse=True)
pause 1
stop music fadeout 1

$ renpy.movie_cutscene("endroll_a.mpg")
#return
