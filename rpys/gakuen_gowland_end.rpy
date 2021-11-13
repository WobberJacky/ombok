label gakuen_gowland_end:
scene bg_map_day
with dis
$ clockanim()


scene bg06_sk_h_day with Dissolve(1.2)

play music daytime_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は生徒で、ゴーランドはその担任だ。\n
立場を考えれば、私のブリーズの成功は表だって祝えるようなものではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……いや、成功っていうのかな。\n
戦利品は取り戻せたけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もっと多くを、奪われた気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスのおかげでストームに参加しそびれたということになっている私は、ブリーズにも参加しなかったということになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下手に嘘をついて、ストームのときのように追及されてしまっても大変だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、誰かにブリーズを行った、なんてことにしてしまえば、意外と嫉妬深いことが判明したゴーランドが妬くのが分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……でも、恋人が出来たって、誰にも話せないのは残念）"


play music dining_day_p_wam

scene bg_par02_ct_amu_day
with dis
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの翌日の朝。\n
その名残にざわつくカフェテリア。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "合流したクラスメイトの女の子達に、今回のブリーズには参加しなかったことを告げる。\n
彼女達は、ショックを受けたようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……というわけで、結局、今回のブリーズには参加しないことにしたの。\n
いろいろ教えてくれたのに、参考にできなくてごめんね」"


show girl_b2_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice nos_g0058
Seito "「とても残念だけど、仕方ないわよね……。ストームにろくに参加できなかったのなら、ブリーズの盛り上がりについていけない部分もあるだろうし……」"

hide girl_b2_1
show girl_b2_1 at left
with dis

show girl_c1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice ari_g0037
Seito "「ブリーズはあくまでストームの仕返しっていった意味合いが強いものね。\n
出だしをしくじっちゃうと……」"

hide girl_c1_9
show girl_c1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice ari_g0038
Seito "「……ああ、でも、残念だったわね、本当に」"

hide girl_b2_1
show girl_b2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice nos_g0059
Seito "「仕方ないわ。\n
ブリーズだけで参加するっていうのは、やっぱり難しいわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は、明らかにしょんぼりした様子だ。\n
私のかわりに悲しんでくれていることに、罪悪感を覚える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……ごめんね、本当のこと言えなくて）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この二人は、ブリーズに参加しなかったと告げた私を責めなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "楽しめないイベントに無理に参加する必要はないと思ってくれていて、だが、一緒に参加できなかったことを残念に思ってくれているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一緒に楽しむことを、目的にしてくれている。\n
そのことに感謝した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「あのね、だから話を聞かせてほしいの。\n
来年こそは、ちゃんと参加したいじゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が話せない分、彼女達の話を聞きたい。\n
彼女達が経験してきたストームやブリーズの話を教えてほしい。"

hide girl_b2_9
show girl_b2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の言葉に、二人の顔がぱあっと輝いた。"

hide girl_b2_3
show girl_b2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0060
Seito "「ええ、もちろんよ！」"

hide girl_c1_1
show girl_c1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0039
Seito "「どんな話がいいかしら。\n
今回のブリーズの話をしても、参考にならないわよね……」"

hide girl_c1_8
show girl_c1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0040
Seito "「私達が新入生の頃の話がいい？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_16")
T "「そうね、あなた達が新入生だった頃の話がいいわ。\n
ストームのときには、さぞ驚いたんでしょうね」"

hide girl_b2_2
show girl_b2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0061
Seito "「そりゃあもちろんよ。\n
もう、本当にびっくりしたんだから」"

hide girl_c1_2
show girl_c1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0041
Seito "「聞いてよ、この子ったらね？\n
相手の男の子を変質者と間違えて……」"

hide girl_b2_3

hide girl_c1_2
##[chara4 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par02_ct_amu_day with Dissolve(.8)

scene bg_par15_rg_amu_day
with stripe_l_medium

scene bg_par09_os_day
with stripe_l_long

play music gallery_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のブリーズを応援し、手伝ってくれたボリスにだけは本当のことを報告した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後の音楽室。\n
絶対にゴーランドの演奏だけはないと言い聞かせて呼び出したのだ。"


show bor_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0148
Boris "「……何もないと聞かされても、怖いぜ。\n
この部屋って、スリルが溢れすぎ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの演奏には警戒しつつも、ボリスも顛末は気になったのか音楽室に顔を出してくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「いろいろありがとうね、ボリス。\n
点呼だとかも、してくれたんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来寮生の管理はゴーランドの仕事だ。\n
ボリスはそれを代理でやってくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その上、私がブリーズの終了時間をオーバーして寮に戻ったことについても、しっかりフォローしてくれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "持つべきものは友人だ。\n
その友人は、現在微妙極まりない顔をしている。"

hide bor_m_01_3
show bor_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0149
Boris "「まあ、あんたが戻ってこなかった時点で、成功は分かっていたんだしさ。\n
乗りかかった船だから、最後までフォローしてやったのはいいんだけど」"

hide bor_m_02_12
show bor_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0150
Boris "「……{size=+20}なに、その背後霊{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「気にしないでちょうだい」"


play music district_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは、げんなりとした目で、私の背中におんぶお化けよろしく張り付いているゴーランドへと呆れかえった視線を向ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他にはひとけのない音楽室だからか、ゴーランドは遠慮なくベタベタとしてくる。\n
……今はボリスがいるのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むしろ、ボリスへと見せ付けるようにベタベタしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（こういうところ、わりと子供っぽい……のかな？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私よりずっと年上であるはずなのだが、時折見せるこういう顔は、若いというよりも幼い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん普段はしっかり大人として振る舞ってくれるし、とても頼りになる……、はず。"

hide bor_m_02_8
show bor_m_02_8 at left
with dis

show go_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0201
Gowland "「そうだそうだ、おまえは気にするな、ボリス。\n
ちょっと耳と尻尾が生えているからって調子にのるなよ！」"

hide bor_m_02_8
show bor_m_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0151
Boris "「はあ！？\n
調子にのるも何も……、猫なんだから、耳と尻尾くらい生えてて当たり前だろ！」"

hide go_m_01_5
show go_m_03_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0202
Gowland "「この子は、おまえの耳と尻尾だけが好きなんだ。\n
猫だからな。猫が好きなんだ」"

hide bor_m_01_4
show bor_m_03_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0152
Boris "「……ははあ。\n
そういうことなわけ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……そういうことなのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスはそれだけの会話で、諸々を悟ってくれたらしい。\n
私とボリスがお似合いなんてふうに誤解したゴーランドより、よほど聡い。"

hide bor_m_03_11
show bor_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0153
Boris "「ふ～ん……、ねえねえ、[firstname]。\n
あんた、猫が好きなら、俺でもいいよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……はい？」"

hide bor_m_02_2
show bor_m_02_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice bor_g0154
Boris "「おっさんなんかやめて、俺にしておきなよ。\n
若いし、将来有望だよ？」"

hide go_m_03_1
show go_m_02_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice gor_g0203
Gowland "「な……っ！！？\n
ボリス、てめっ！！」"

hide bor_m_02_3
show bor_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice bor_g0155
Boris "「こんなくたびれたおっさんなんてやめておきなよ。\n
ね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言って、ボリスは、私の手をとると上目遣いにそっと笑ってみせる。\n
明らかに、私に向けてのアピールというよりも、対ゴーランドだ。"

hide bor_m_02_2
show bor_m_02_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0156
Boris "「猫って飼いやすいよ？\n
飼ってみない？」"

hide go_m_02_9
show go_m_02_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0204
Gowland "「……っ！？」"

hide bor_m_02_3
show bor_m_02_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0157
Boris "「同年代の猫だし、扱いやすいと思うけど？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私をダシにして、ゴーランドをからかって遊んでいる。\n
それが分かるから、いくら甘ったるく囁かれても動揺するようなことはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それを真に受けるのがゴーランドだ。\n
やっぱり私より年上であることを、変なふうに意識している。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……ま、私だって完全に意識しないっていうのは無理だけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今は、それを、ネックというふうには感じていない。私を間に挟んで火花を散らしあっている二人を他所に、のんびりとそんなことを思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（ゴーランドは……、私を安心させてくれる）"

hide bor_m_02_6
show bor_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_19")
voice bor_g0158
Boris "「悔しかったら、おっさんも猫耳と尻尾を生やしてみなよ！\n
そしたら、もっと好きになってもらえるかもしれないぜ？」"

hide go_m_02_1
show go_m_02_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_19")
voice gor_g0205
Gowland "「言ったな！？\n
この子は俺が好きなんだ、その俺に猫耳と尻尾なんてついたら鬼に金棒だぞ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "売り言葉に買い言葉、とんでもないことになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！？\n
ゴーランドにそれは危険だと……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前に自分でも言っていたくせに。\n
そんなもの、ついているほうがおかしい。"

hide bor_m_02_2
show bor_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0159
Boris "「……う。\n
……ごめんおっさん、{size=+20}無理{/size}」"

hide bor_m_02_4
show bor_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0160
Boris "「口が滑った。なかったことにして。\n
無理だから、それ」"

hide bor_m_02_4
show bor_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0161
Boris "「想像しちゃった……。\n
……うぷ」"

hide go_m_02_9
show go_m_03_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0206
Gowland "「何が無理だ、何が！！\n
見てろよ！？」"

play sound se_0468
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が止めるよりも先に、ゴーランドがぱちん、と指を鳴らす。"

play sound se_0379
$ flash_color("pink", .2)
$ flash_color("pastel_yellow", .2)
$ flash_color("pink", .2)
$ flash_color("pink", .2)
pause .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "簡単な魔法ならば、杖や呪文といった媒体を一切使わずにやってのける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "技術はさすがだと思うが……、{size=+20}こんなふうになりたいとは思わない{/size}。"


play music gag1_a_ali

show m_go_end1 onlayer master
with dis
hide go_m_03_6

hide bor_m_02_4

play sound se_0056
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "{size=+20}↑こんなふう。{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0162
Boris "「……っうぷっ！\n
モザイク、誰かモザイクかけて……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0207
Gowland "「どうだ、[firstname]！\n
参ったか！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（……参らせてどうするのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振り仰いだ先、ゴーランドの頭に山吹色の三角耳が出現しているのを確認した。\n
おそらく同じ色の尻尾も生えているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「に、似合うんじゃないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言いながら、そっと視線を明後日の方向へとそらす。\n
直視はできない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0163
Boris "「お、老いらくの恋って、多分こういうことをいうんだな……。\n
こええよ、自分を客観視してみろよ客観視！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0164
Boris "「おっさんに猫耳って、誰に対するサービスだよ！？\n
誰が喜ぶんだ、ンなもの！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0208
Gowland "「この子が喜ぶに決まってんだろ！！\n
なんていったって猫好きなんだから、なあ、[firstname]！！！」"

menu:
    "ええ、そうね。":
        jump gakuen_gowland_end2a
    "…………。":
        jump gakuen_gowland_end2b
label gakuen_gowland_end2a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……ええ、そうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線が合わせられない。"

jump gakuen_gowland_end3
label gakuen_gowland_end2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無言で視線を逸らし続ける。"

jump gakuen_gowland_end3
label gakuen_gowland_end3:
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「[firstname]！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0165
Boris "「あんたも、おっさんを甘やかすな！！！\n
おっさんのセンスは音楽関係でよく分かってるだろ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……まあ、でも、これなら被害は少ないし」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（目を合わせなければいいのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう、どちらとも目が合わせられない。\n
ショッキングピンクの猫耳青年と、山吹色の猫耳のおっさん。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人並べば、シュール極まりない。\n
ボリスは、ゴーランドが自分と同じになったとは思いたくないようだが……同種だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（相乗効果なのか、結構すごいな……）"

hide m_go_end1
show m_go_end2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice bor_g0166
Boris "「……っ！\n
猫耳のプライドにかけて、おっさんを認めるわけには……！！」"

play sound se_0051
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスが懐から杖を取り出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、その杖の先端をゴーランドへと突きつけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！？\n
ボリス！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本気で術を使うつもりかと焦る。\n
私が止めるより先に、ボリスの魔法が発動した。"

play sound se_0496
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「…………！」"

play sound se_0371
hide m_go_end2
show m_go_end3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きらきらしい光がボリスの杖の先から溢れ、ゴーランドへと降りかかる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（あ……。\n
なんだ、攻撃魔法とかじゃないのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかして、強制的に猫耳猫尻尾を解除する魔法だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"

play sound se_0138
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どんな変化が現れるのかと、不安と好奇心とで見守る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……ぶはっ！」"

play sound se_0042
hide m_go_end3
show m_go_end4 onlayer master
with dis

play music gag3_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "光が形になって、私は盛大に噴き出していた。\n
ボリスは完全に有言実行をしたのだ。"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……モ、モザイク？」"

play sound se_0137
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "モザイクというより雲だが、もわもわとしたそれは綺麗に猫耳を隠している。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gowland "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0209
Gowland "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分では確認できないこともあって、ゴーランドはいったん私から離れると、窓へと駆け寄る。そしてガラスの反射で己の状態を確認したらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0210
Gowland "「ボリス……っ！！！てめえ、俺の邪魔ばかりしやがって……！！こんな格好じゃ外に出れねえじゃねえか！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0167
Boris "「いや、先刻のほうがまずいだろ！？\n
視覚に対する暴力だ！聴覚だけじゃ足りないわけ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "互いに罵りあいながら、それぞれに杖を構える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……平和だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "猫耳をつけた男二人の喧嘩なんて、その言葉だけを聞けばずいぶんとほのぼのとしている……。そして、絵面的には非常に奇妙な光景……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……それにしても、しみじみ、ここが防音でよかったと思う。"

with dis
$ hi_mes()
hide m_go_end4


scene bg_par09_os_day with Dissolve(.8)

scene bg_par15_rg_amu_day
with stripe_l_medium

scene bg06_sk_h_day
with stripe_l_medium

scene bg06_sk_h_eve with Dissolve(1)

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_eve with Dissolve(1)

play music view_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "互いに想いを伝え合い、恋人関係になった。\n
とはいえ、私達は依然として教師と生徒の関係だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人目がない場所や、事情を知るボリスの前では少々羽目をはずすこともあるが、校舎においては常に一線を引いている……、つもりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（……こういうのって、態度に出たりしないのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法生物学の野外演習中に、ふと顔をあげたところ。\n
空き時間らしきゴーランドが芝生に腰掛けてこちらを眺めているのに気づいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょうど待ち時間だったこともあって、軽く手をあげて合図を送る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドもすぐに気づいたのか、同じよう小さく手を揺らしての挨拶が返って来た。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たったそれだけのやりとりでも、得をした気になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……こういうの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段の態度に出てしまっていないだろうか。"

with dis
$ hi_mes()

scene bg06_sk_h_eve with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg10_sb_day
with stripe_l_medium

scene bg10_sb_day
with stripe_l_medium

scene bg_iro_kuro
with stripe_l_long

play music high_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本日の魔法生物学は、前に受けたゴーランドの授業と連動している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達は召喚の種類についてを学び、第二種召喚魔法の実践を行った。\n
この授業では、第一種の召喚魔法で召喚される魔法生物についてを学ぶのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "特に今日は、実際に担当教師が第一種召喚魔法を行い、ケンタウルスを呼び出してくれるのだという。"


show girl_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0041
Seito "「わくわくするわね、[firstname]。\n
あなた、ケンタウルスって見たことある？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「まさか。本の中だけだわ。\n
契約者に対しては医術などの知識を与えるけど、敵に対しては残虐で凶暴だっていうわよね」"

hide girl_a2_2
show girl_a2_2 at left
with dis

show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nos_g0062
Seito "「こう、小さめの魔法生物なら何度か召喚したことがあるんだけど……。\n
ケンタウルスっていうと、もう魔法生物っていうよりも魔獣よね」"

hide girl_a2_2

hide girl_b1_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "着々と召喚の準備を整えていく教師の姿を眺めつつ、私達はそんな会話を交わす。\n
やがて、地面に描かれた複雑な魔法陣が完成する。"

play sound se_0496

show white onlayer master with expand
play sound se_0725
hide white

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呪文詠唱の声音が響くと同時に、その魔法陣が光を放ち始めた。\n
そして、その中央にすうっと人影が浮かぶ。"

play sound se_0738

show m_go_end5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（人……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……違う。\n
人じゃない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "上半身は石膏像のように端正な男でありながら、その臍から下に繋がるのは獣のそれだ。"


play music disquieting_a_wam
play sound se_0559
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が息を呑むのとほぼ同時に、周囲で見守っていた生徒達の間にざわめきが生まれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆も気づいたのだろう。\n
あれは、ケンタウルスではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、半人半獣の魔獣の総称としてケンタウルスを使うのならば間違ってはいないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通ケンタウルスといえば、人の体に馬の体が繋がったものとしてとらえられている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、今私達の目の前にいる魔法生物の下半身は、赤黒い蛇のものだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0042
Seito "「なんだか……、違わない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0029
Seito "「禍々しい感じが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0063
Seito "「ええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Kyousi "「……！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "召喚した本人である担当教師の顔にも動揺の色が過ぎる。\n
どこかで召喚のプロセスを間違えてしまったのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "召喚したものが目的としたケンタウルスでないということは、すなわち契約が成立していないということだ。"

hide m_go_end5
show m_go_end6 onlayer master
with dis
play sound se_0266
play sound se_0264
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0042
Monster "「シュルシュルシュル……」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0030
Seito "「なんか、まずくないか、これ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0043
Seito "「え？\n
召喚事故？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0064
Seito "「ええ～？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "え～、とか。\n
驚いている場合ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「皆、下がったほうがいいわっ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "契約が成立していない以上、今私達の目の前にいる魔獣は教師の制御下にない。"

play sound se_0266
play sound se_0264
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0043
Monster "「シュルシュルシュル……」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "失敗したとはいえ、シンフォニアの教師が呼び出したシロモノだ。\n
危険すぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の声に我に返ったというように、同じ授業を受けていた生徒達がじりじりと後ずさっていく。"

play sound se_0313
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私自身も後ろへと引こうとして、足が動かないことに気づいた。"

hide m_go_end6
show m_go_end7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（……え！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何が起こったのか分からずに、自分の足元を見る。"

play sound se_0106
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ{size=+20}！！！！{/size}」"


play music tension_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "喉の奥で悲鳴が引きつった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "痛みも、何の感触もないままに私の足が石化している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "はっとして召喚者である教師を見やれば、真っ先に狙われたのか完全に石像と化してしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他にも石化している人間はいないかと見渡すが、私と彼の他はまだ無事なようだ。\n
皆、怯えた顔で立ち竦んでいる。"

play sound se_0266
play sound se_0264
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0044
Monster "「シュルシュルシュル……」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……もしかして）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が大声を出したから、だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（この魔獣は音に反応している？）"

menu:
    "試してみる。":
        jump gakuen_gowland_end4a
    "考える。":
        jump gakuen_gowland_end4b
label gakuen_gowland_end4a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうせ、私はもう動けない。\n
だが、この魔獣さえなんとかしてしまえば、すぐに助けてもらえるだろう。"

jump gakuen_gowland_end5
label gakuen_gowland_end4b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "考える。\n
冷静に考えれば、何か手はありそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが……。"

play sound se_0106
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、私にはあまり時間が残されていない。\n
じわじわと石化が進んでいる。"

jump gakuen_gowland_end5
label gakuen_gowland_end5:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せここはシンフォニアだ。\n
石化の呪いを解く方法ぐらい、いくらでもあるはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "石になっている男がこの授業の担当教師というのは心許ないが、おおごとになれば、もっと優秀な先生や職員も駆けつけるはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（よし）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しでも、被害を少なく、解決の方法を探る。\n
足を石化された私が試せばいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「皆、音を出さないで！」"

hide m_go_end7
show m_go_end8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "叫ぶ。\n
同時に、魔獣が私を見た。"

play sound se_0266
play sound se_0264
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0045
Monster "「シュルシュルシュル……」"


play sound se_0396
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「！！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "石化の魔眼を持つというモンスターがいる、という知識はあった。\n
体験したくはなかったが、これがそうなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "上半身は人の姿をしているのに、その眼は完全に爬虫類のものだった。"

play sound se_0106
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "眼があった瞬間に、足元から石化現象が再び這い上がる。先ほどまでは足首より少し上までが石化していたのに対し、今は膝上まで石化が及んでいる。"

play sound se_0266
play sound se_0264
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0046
Monster "「シュルシュルシュル……」"

hide m_go_end8

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（でも、これで分かった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やっぱり、この魔獣は音を頼りに周囲を探っているのだ。\n
動かない足はそのままに、私はゆっくりと体を捻ってゴーランドを探す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（いた）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業内容が連動しているため、彼はメインで教鞭をとってはいないものの、その場に控えていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもの魔法媒体であるバイオリンではなく、杖を構えて、臨戦態勢だ。\n
鋭く魔獣を睨み付ける一方で、私へと心配そうな視線を送ってきている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、声を出さない。\n
私も、これ以上に音はたてない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……大丈夫。\n
いや、全然大丈夫ではないけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の石化はゆっくりと、着実に進んでいる。\n
だが、パニックに陥ってはいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういう意味では、まだ大丈夫だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドが魔獣に対してすぐに何も仕掛けないのは、やはり石化の魔眼を恐れてのことなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今ここでゴーランドまで石化してしまったら、この場において対処できる教師が誰もいなくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先刻考えたように、しばらくすれば異常事態を察知して使用人や他の教師が駆けつけてくるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それまでに石化ではすまない被害が出てしまうかもしれない。"

play sound se_0266
play sound se_0264
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0047
Monster "「シュルシュルシュル……」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思いきった真似をしたが、こうしてじわじわと石化されていくと、恐怖もじわじわとこみ上げてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（勢いもあって行動しちゃったけど……。\n
手詰まりだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このままただ石化が完了するのを待っているだけでは、無駄死にならぬ無駄石化だ。完全に石化する前に、何か、出来ることはないだろうか。"

play sound se_0266
play sound se_0264
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0048
Monster "「シュルシュルシュル……」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この魔獣は音に反応する。\n
眼が見えていないか、もしくはほとんど見えないぐらいに悪い、といったところだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、一番近くにいた教師を石化させた以降は、声をあげた私ぐらいにしか石化の魔眼を使っていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……ん？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今何か閃きかけた。\n
音で索敵するというのならば、逆に音をたてまくったならばどうだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "木を隠すならば森の中、音を隠すならば音の中だ。\n
それならば、ゴーランドが攻撃に出るチャンスを作ることができる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、もう一度身体をひねってゴーランドを振り返ると、そっと手を差し出した。"


show go_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0211
Gowland "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さっきよりも振り返るのが辛いのは、石化がじわじわと這い上がってきているせいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐに私の意図を察したらしきゴーランドが、首を横に振る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "（いいから……！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぶんぶん、っと手を振って早く寄越せとアピールをする。\n
動けなくなる前に、少しでも現状を打破しておきたいのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じ石化するなら、多少は役に立ちたい。\n
後で解除してもらうための手伝いにもなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……！」"

hide go_m_03_6
show go_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice gor_g0212
Gowland "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな私とゴーランドの無言のやり取りを、他の生徒達は意味も分からずにただただ見つめている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やがて、ゴーランドが折れた。\n
すいっとその手を揺らすと、差し出していた手の上にずしりと質量が出現する。"

play sound se_0306

show m_go_end9 onlayer master
with dis
hide go_m_02_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランド愛用のバイオリンだ。\n
弓を右手に、バイオリンを左に構える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "バイオリンの弾き方など分からないが、問題ない。\n
騒音でいいのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それこそ、普段のゴーランドのように。"


play music battle_a_wam
play sound se_0222
play sound se_0396
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！！」"

play sound se_0106
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予想以上に石化の進行スピードが速い。\n
これでは充分な時間を稼ぎきれるか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がバイオリンを弾き始めると同時に、ゴーランドは片手に杖を携え、踏み切っている。"

play sound se_0458
hide m_go_end9
show m_go_end10 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gowland "「……！！！」"

play sound se_0611
pause 1
play sound se_0414
$ flash_color("blue_2", .7)
$ flash_color("blue", .7)
$ flash_color("blue_2", .7)
$ flash_color("blue", .7)
play sound se_0426 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0049
Monster "「キイイイ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの放った魔法から、しゅるしゅると身をくねらせて逃げながら、魔獣が威嚇するような声をあげる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はその間も、ひたすらバイオリンをかき鳴らしてゴーランドの気配をかき散らす。魔法の出元がどこなのかも分からないはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（いい感じ……。\n
名案だったわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自画自賛している余裕はない。\n
次第這い上がってきた石化の呪いが腕にまで及び始める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このままでは、ゴーランドが魔獣を倒すよりも私が石になるほうが早い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（このままじゃ……、完全に石に……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "焦燥に泣きそうになった瞬間、その声は聞こえた。"


play music quiet_a_wam
play sound se_0496
$ flash_color("pastel_yellow",.1)
hide m_go_end10
show m_go_end11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0416
pause .15
play sound se_0496
$ flash_color("pastel_blue",.1)
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0379
pause .15
play sound se_0496
$ flash_color("sky_blue",.1)
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0589
pause .15
play sound se_0496
$ flash_color("pink",.1)
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0592
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（何？\n
なんの魔法を使おうとしているの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もうほとんど身動きのできなくなった身体で振り返る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じく足元から石化の始まった女子生徒が、眉尻を下げながらも呪文を紡ぐ。"

play sound se_0496
$ flash_color("mauve",.1)
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0416
pause .15
play sound se_0496
$ flash_color("pastel_orange", .1)
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0379
pause .15
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法を使おうというよりは、その呪文の詠唱自体が……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（輪唱？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達に石化の魔眼が向けられたことにより、私の石化のスピードが下がる。\n
それを見ていたほかの生徒達までもが、詠唱に混じりだす。"

play sound se_0496
$ flash_color("pastel_yellow",.1)
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0589
pause .15
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0496
$ flash_color("fuschia_pink", .1)
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0592
pause .15
play sound se_0496
$ flash_color("mauve", .1)
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0138
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "元々、召喚されるケンタウルスを観察するという目的で集まっていた私達は、魔法陣を中心に円を描くように配置されている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのあちこちから、歌声が上がるのだ。"

play sound se_0264
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0050
Monster "「シュルシュル……、キイイイ……」"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔獣の視線がくるくると忙しなく動いては翻弄される。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔眼が分散されることにより、一人あたりの石化スピードは緩やかだ。"

play sound se_0221
play sound se_0496
$ flash_color("blue_3",.1)
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も最後の力を振り絞ってバイオリンをかき鳴らし、一緒になって詠唱する。"


play sound se_0439
pause .3
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0213
Gowland "「……歌に救われるってのはこういうことだな！」"

play sound se_0509 volume .7
hide m_go_end11
show m_go_end12 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは手にしていた杖を一閃、それを大剣へと変えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もはやゴーランドの声に反応することすら出来ず、魔獣は歌の壁に閉じ込められて身をくねらせるばかりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0214
Gowland "「……っせい！！」"

play sound se_0441
pause .6
play sound se_0782
$ flash(.2)
hide m_go_end12
show m_go_end13 onlayer master
with dis
play sound se_0426 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0051
Monster "「キイイ……！！」"

play sound se_0069
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、そんな魔獣をゴーランドの大剣が一刀両断にした。\n
傷口からは血の代わりに砂が舞う。"

play sound se_0427 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0052
Monster "「キイイイイイイイイイ……」"

play sound se_0696 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0053
Monster "「……シュルシュルシュル」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔獣はあっというまに砂になって、分解されていってしまった。\n
それを見届けて、ゴーランドが私のもとへと駆けつける。"


hide m_go_end13


play music forest_thick_nig_p_wam

show go_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gowland "「[firstname]……！！」"

hide go_m_02_4
show go_m_02_4 at left
with dis

show girl_a1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0044
Seito "「[firstname]、大丈夫！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドだけではない。\n
クラスメイト達も私のもとへと駆け寄ってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当然、駆け寄れるということは動けるということで……。\n
……私は動けないまま。"

hide go_m_02_4
show go_m_02_4 at left_center
hide girl_a1_4
show girl_a1_4 at center
with dis

show girl_b1_4 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「！！！？」"

hide girl_b1_4
show girl_b1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0065
Seito "「ゴーランド先生！\n
なんで彼女と、オリバー先生の石化だけ治らないんですか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "輪唱に加わることにより、石化の影響を受けていたはずの生徒達は皆普通に動き回っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "モンスターが消滅するのと同時に、解けたようだ。"

hide go_m_02_4
show go_m_01_9 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0215
Gowland "「おまえらと違って、石化の魔眼に曝された時間が長いからだな。\n
早く解呪しねえと」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "軽症と重症の違いであるらしい。\n
実際、私はもう首の下あたりまで石化が進んでいるし、先生にいたっては完全に石像状態だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（あ、だんだん意識がぼんやりしてきた……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外側だけでなく、内臓まで石になってきているのだろうか。\n
どういう原理か分からないが、痛みはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "石像になる恐怖から逃れるため、石化の仕組みに考えを飛ばす。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ゴーランド、早く……、ナイトメア……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呼んできて、と伝えたいのに、口がうまく回らない。\n
眠いような痺れるような、妙な感覚だ。"

hide go_m_01_9
show go_m_03_6 at center
with dis
hide girl_a1_4

hide girl_b1_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0216
Gowland "「呼びに行くより、あんたを運んだほうが早え！！\n
担ぐぞ！！」"

hide go_m_03_6

play sound se_0052
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういいきるや否や、がっしと硬直した私の身体をゴーランドが抱き上げた。"


scene bg27_rk_day
with dis
play sound se_0417
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……もったいないなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼんやりとした思考で思う。\n
せっかくこうして抱き上げてもらっているというのに、石化した身体ではゴーランドの体温すら分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな非常事態でもなければ、皆の前でこんなふうに彼と接触するなんて出来ない。非常事態だからこその境遇ではあるのだが、もったいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は私を運び、石化されてしまった先生も呪文で浮かせた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……ゴーランドに任せておけば、もう大丈夫）"

show black onlayer master with close_medlong
hide black
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は安心して、意識を手放した。"

with dis
$ hi_mes()


scene bg_par18_ri_tow
with dis

play music view_day_p_wam
show black onlayer master with open_long
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「ん……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼんやりと瞬いて、眼を覚ました。\n
誰かが私を覗き込んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何度か瞬いて、ぼやけていた視界が焦点を結んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ナイトメア？」"


show nai_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nig_g0011
Nightmare "「ああ、気づいたか。\n
どうだ？具合の悪いところ、気持ちの悪いところはないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「……平気、みたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "足のつま先、指先、と力を入れて開閉してみる。\n
石化していたときのように、何も感じないというようなことはない。"

hide nai_m_02_11
show nai_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0012
Nightmare "「驚いたよ、ゴーランドが石像みたいになった君を担ぎこんできたんだからな！\n
……かちんこちんだったぞ、君」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そりゃあ、石化されたわけだしね。\n
ありがとう、ナイトメア」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらくここは医務室だろう。\n
むくりと身体を起こす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれだけ派手に石化の呪いを受けたのだから、何か後遺症が残ってはいないかと構えたものの、ナイトメアの腕がよかったのかなんともない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ゴーランドは？」"

hide nai_m_02_1
show nai_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0013
Nightmare "「魔獣騒動の事後処理に行っているよ。\n
ああ、そうそう、もう一人の先生のほうも無事だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……よかった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ほうっと息を吐く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアだから大丈夫、とある意味盲信していたからこそ無茶をしてしまったわけだが、今考えると冷静なつもりでいて私もパニックになっていた。"

hide nai_m_01_11
show nai_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0014
Nightmare "「無茶をして……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「うん、分かってる……」"

hide nai_m_01_12
show nai_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice nig_g0015
Nightmare "「……クラスメイト達も心配していた。\n
動けるようなら、顔を出してきてあげるといいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「そうするわ。\n
私……、どれぐらい眠っていたの？」"

hide nai_m_03_10
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
voice nig_g0016
Nightmare "「二時間ほどじゃないかな。\n
ああ、立てるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「大丈夫みたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "医務室のベッドから降りて、大きく伸びをする。身体が凝っているような気がするのは、やはり石化されてかちんこちんに固められたせいだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（……これくらいの影響しかないのを感謝すべきよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「本当に、ありがとう。\n
あなたは名医ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はもう一度改めてナイトメアに礼を告げると、医務室を後にした。"

hide nai_m_02_4
show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0017
Nightmare "「ふふん、えっへん！\n
当然、私は偉大な……、げほ！げほごほ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……自分も治せば？」"

hide nai_m_02_10
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par18_ri_tow with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg_par15_rg_amu_day
with stripe_l_medium

scene bg_par02_ct_amu_day
with stripe_l_long

play music dining_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮に戻ると、とりあえず無事であることを知らせようとカフェテリアに向かった。"

##[rchara1 PAY ATTENTION="false"]
show girl_a2_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「！！！！」"

hide girl_a2_1
show girl_a2_1 at left
with dis

show girl_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「！！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がカフェテリア内に足を踏み入れると同時に、机に座っていた一団がばっとこちらを振り返る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……皆、魔法生物学の子達だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "固まっているところを見て、例の一件で集まっていたらしい。\n
いいところへ来た。"

hide girl_a2_1
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「[firstname]……！」"

hide girl_a2_3
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0045
Seito "「よかった……！\n
無事だったのね！」"

hide girl_b1_1
show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0066
Seito "「あのまま戻らなかったらどうしようかと思ったわ！\n
今も、ちょうどあなたの話をしていたところで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、タイミングがよかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「見ての通り、完全に回復したわ。\n
先生のほうも、無事らしいし……」"

hide girl_a2_3
show girl_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice mat_g0046
Seito "「本当……！？\n
よかった……！」"

hide girl_a2_2
show girl_a2_2 at left_center
hide girl_b1_2
show girl_b1_2 at center
with dis

show boy_a1_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice oni_g0031
Seito "「回復するまでは面会謝絶っていうからさあ……。\n
ここの学校医の補佐って、厳しいよな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「心配してくれたのね。\n
ありがとう」"

hide girl_b1_2
show girl_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice nos_g0067
Seito "「お礼を言うのは、私達のほうよ。\n
まだ新入生のあなたに助けられるなんて……」"

hide boy_a1_8
show boy_a1_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice oni_g0032
Seito "「俺達が助かったのって、あんたのおかげだもんな！」"

hide girl_a2_2

hide girl_b1_3
show girl_b1_3 at left_center
hide boy_a1_2
show boy_a1_2 at center
with dis
##[rchara4 PAY ATTENTION="false"]
show boy_b1_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice suz_g0030
Seito "「君が警告してくれなかったら、皆、悲鳴や呪文詠唱でもっと石にされていたよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……う）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口々に私を迎えてくれる。\n
まるで英雄のような言われように、背中がぞわぞわとくすぐったくなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……あれは無謀な行動であって、褒められるような類のものじゃないと思うんだけどなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振り返って考えると青ざめるような、無謀さだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「私、下手なバイオリン弾きまくっていただけよ？\n
それよりも、皆の輪唱のほうがすごかったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呪文の詠唱で、輪唱とは。\n
いかにも魔法使いらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私にバイオリンが弾けたのならば、詠唱に加わるのではなく、伴奏でもつけたかったところだ。"

hide girl_b1_3

hide boy_a1_2

hide boy_b1_3


show girl_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0047
Seito "「きっかけを作ってくれたから、歌えたのよ」"

hide girl_a1_3
show girl_a1_3 at left
with dis

show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0068
Seito "「ええ、そう。\n
あのままだと、硬直したままでいたわ」"

hide girl_b1_3
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0069
Seito "「すごくいい体験になった。\n
実戦演習ってああいうのを言うのよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……そういう授業ではなかったはずなんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「でも、実戦となれば、私なんかより皆のほうが絶対に強いわよ。\n
あそこで助けてもらえなかったら、私もゴーランドも石になって終わっていたわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのままでは、どう考えても私が完全に石化してしまうほうが早かった。\n
実戦演習とやらを最後まで見届けられることが出来たのも、彼らのおかげだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分散した魔眼を受けてくれたからこそ、最後までゴーランドをフォローできた。"

hide girl_a1_3
show girl_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

hide girl_a1_5
show girl_a1_5 at left_center
hide girl_b1_3
show girl_b1_3 at center
with dis

show boy_a1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……ん？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がゴーランドの名前を出した途端、微妙に視線を逸らされた。\n
何かあったのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ゴーランドがどうかしたの？」"

hide girl_a1_5
show girl_a1_4 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice mat_g0048
Seito "「い、いいえっ？\n
なんでもないわ」"

hide girl_b1_3
show girl_b1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nos_g0070
Seito "「事後処理だとか報告だとかが終わったら、ゴーランド先生もこっちに戻ってくるんじゃないかしら。その……、あなたのこと、とても心配していたから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うんうん、と彼女達は深々と頷きあっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか少し、嫌な予感がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（まさか、あれからゴーランドに何か……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "モンスターは倒したはず。\n
いや、ああまであっさりと魔獣が倒せるわけがないから、元の場所へ還しただけなのかもしれないが。"

play sound se_0417
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ん？」"

hide girl_a1_4
show girl_a1_8 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice mat_g0049
Seito "「……あ」"

hide boy_a1_5
show boy_a1_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice oni_g0033
Seito "「お」"

hide girl_a1_8

hide girl_b1_5
show girl_b1_5 at left_center
hide boy_a1_8
show boy_a1_8 at center
with dis

show boy_b1_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice suz_g0031
Seito "「ゴーランド先生だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆が、私の後ろより聞こえてきた足音の主の名を呼ぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ゴーラン……」"

play sound se_0051

play music flower_eve_p_wam
show m_go_end14 onlayer master
with dis
hide girl_b1_5

hide boy_a1_8

hide boy_b1_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振り返るより先に、力いっぱい抱きしめられていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0217
Gowland "「[firstname]……！！\n
無事でよかったぜ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……その。\n
ゴーランド？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice gor_g0218
Gowland "「なんだ？どうした？\n
まだ具合よくないのか？ナイトメアの野郎がドジったか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「いえいえ、ナイトメアはちゃんと治してくれたわ。\n
具合も悪くない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「ただ、その……。\n
……生徒と担任にしてはちょっといきすぎてないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こそこそと囁く。\n
密着しすぎだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒を心配した先生にしても、過剰接触な気がする。\n
注目をひいてしまうと、心配する私が自意識過剰なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……気にするほどのことでもないのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たくさん心配をかけてしまった自覚はあるから、ゴーランドのことを責めることはできない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、だからといってこんな衆人環視の状況でイチャつくわけにもいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とゴーランドは、あくまで秘密の関係なのだ。お互いどれだけ好きあっていても、対外的には教師と生徒しての節度を持って……。"

hide m_go_end14


show go_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0219
Gowland "「あー……。\n
すまん、[firstname]、あんたに謝らなきゃいけねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "{size=+20}（……嫌な予感がする）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むくむく、と嫌な予感が胸の内で膨らんでいく。\n
その間もゴーランドは腕を緩めることなく、しっかりと私を抱きしめたままだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲のリアクションが怖くて、抱きしめられたままちらりと視線を流すと、眼が合いそうになった子達は皆そっと視線をそらしてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……う、うわあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさか。"

hide go_m_02_4
show go_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0220
Gowland "「はは、バレちまった」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「…………」"


play music study_a_wam
play sound se_0042
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「ええええええええええ！？」{/size} "

pause 1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "軽い失敗のような口調で、簡単に。\n
しかし、これは大変なことだ。"

hide go_m_02_8
show go_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0221
Gowland "「クラス内にだけだぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「じゃ、じゃあ、離れてよ！\n
これ以上、広まったら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賑やかなカフェテリア。\n
あまり周囲のことなど気にせず、誰しもが自分達の輪の会話に夢中。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも慌てて身を離す。\n
大慌ての私に、周囲からは楽しそうな笑い声が聞こえてきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この様子。\n
クラスメイトには完全にバレているらしい。"

hide go_m_01_2
show girl_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0050
Seito "「だって……ねえ？\n
普通、先生とあんなに息合わないだろうし……」"

hide girl_a1_5
show girl_a1_5 at left
with dis

show girl_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0071
Seito "「石化したあなたを運ぶゴーランド先生の必死さと来たらもう……、ね」"

hide girl_a1_5
show girl_a1_5 at left_center
hide girl_b1_5
show girl_b1_5 at center
with dis

show boy_a1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0034
Seito "「なあ？」"

hide girl_a1_5

hide girl_b1_5
show girl_b1_5 at left_center
hide boy_a1_5
show boy_a1_5 at center
with dis

show boy_b1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0032
Seito "「うん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が石になっている間に、カミングアウト状態になってしまっていたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「ゴ、ゴーランド……っ？」"


show go_m_03_9 at center
with dis
hide boy_a1_5

hide boy_b1_5

hide girl_b1_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gor_g0222
Gowland "「なんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……認めたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "念を押す。\n
もう、こんなふうに聞いてしまうあたりで、彼らの疑惑を肯定しているようなもの。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも諦めきれずに聞いてしまった。\n
またもや、冷静に見せかけたパニック状態だ。"

hide go_m_03_9
show go_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0223
Gowland "「……ああ、認めた。\n
隠しても仕方がないしな、噂になったらどっちみちアウトだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「どっちみちアウトって……。\n
アウトにならない方法を考えようとは思わなかったの！？」"

hide go_m_02_6
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice gor_g0224
Gowland "「あんたとなら、アウトになってもいいかなって」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「よくないわよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭が痛い。\n
魔獣を倒したと思ったら、もっと手ごわい敵が出てきてしまったような気がする。"

hide go_m_02_12
show go_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0225
Gowland "「これでも魔法使いとしてはそこそこなもんだ。\n
教師をクビになったとしても、稼ぎ口くらい、すぐ見つかるさ」"

hide go_m_02_8
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0226
Gowland "「それに、真剣だって分かってもらえば、シンフォニアも無碍には扱わない。\n
かえって問題になるからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、簡単に将来を語る。\n
気負うこともなく、「真剣」であり、未来のあるものなのだ、と。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつも、ゴーランドは私を安心させてくれる。"

hide go_m_03_9
show girl_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0051
Seito "「大丈夫よ、[firstname]。\n
私達、あなた達のこと、応援しているから」"

hide girl_a1_2
show girl_a1_2 at left
with dis

show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0072
Seito "「ええ。\n
素敵だと思うわ、あなたとゴーランド先生」"

hide girl_a1_2
show girl_a1_2 at left_center
hide girl_b1_3
show girl_b1_3 at center
with dis

show boy_a1_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0035
Seito "「好きな人のために命かけるなんて、なかなかできないぜ？\n
ロマンスだよなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "オーバーだ。\n
これこそ、過剰反応。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確かに私はゴーランドを庇って、石化の魔眼を引き寄せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それは「愛する人を守ってみせる」的なノリではなく、単にあの魔獣をあの場で倒せるのがゴーランドしかいないと思ったからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別に恋愛思考のみで動いていたわけでなく、もっと合理的に考えてその結論に落ち着いた。……そこまで冷静であったかは疑わしいが。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、私の抗議は彼らの耳には届かない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっと彼らの中では、私達は困難に直面しながらもそれを乗り越えていこうとする清らかな年の差カップルに祭り上げられてしまっているのだろう。"

hide girl_a1_2

hide girl_b1_3
show girl_b1_3 at left_center
hide boy_a1_2
show boy_a1_2 at center
with dis

show boy_b1_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0033
Seito "「でも、騒ぎ立てないに越したことはないし、黙っておくよ。\n
クラス内だけの秘密ってことで」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……いいの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……そんな、アバウトで）"


show go_m_03_14 at center
with dis
hide girl_b1_3

hide boy_a1_2

hide boy_b1_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice gor_g0227
Gowland "「……いいんじゃないか？\n
皆、祝福してくれてるみたしだしよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……そうね、はあ」"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがに人目があるので、二度は抱きつかない。\n
軽く、腕に手を回される程度のスキンシップ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほど、石化されているときには感じることのできなかった体温だ。\n
わずかでもその温かさを感じると、ささいなこと（？）が気にならなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……あなたといると、気が緩むわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "安心する。"

hide go_m_03_14
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0228
Gowland "「……そいつはよかった。\n
これからもずっと、リラックスさせてやるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "時間の縛りなく。"

hide go_m_03_9
hide frame_par_togaki
hide ali_m_06_16
with Dissolve(2)

scene white
with compress_extralong
scene black with compress_extraextralong
pause 1
stop music
##endmemory
jump gakuen_a
