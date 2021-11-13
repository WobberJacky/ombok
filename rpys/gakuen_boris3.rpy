label gakuen_boris3:
scene bg_map_nig
with dis
$ clockanim()


scene bg25_rr_nig
with dis

scene bg24_rj_nig with Dissolve(1.2)
jump gakuen_dream_other_2
label gakuen_boris3_3:
with dis
$ hi_mes()

scene bg01_cr_day with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg27_rk_day
with stripe_l_long

play music corridor_day_p_wam
play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そわそわとした空気は、寮だけでなく校舎の中でもそうだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日一日の授業を終えて、ホームルームのある教室へと向かいながら周囲の様子を伺ってみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下を歩く生徒達は誰もが楽しげで、浮ついている。\n
私のようにそれに戸惑っているのは、おそらく新入生なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "入学してある程度時間がたったとはいえ、初めてのこともまだまだ多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かあるのだろうと予想することはできても、何がおこるのかはさっぱり想像がつかないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは世界一の魔法学校、シンフォニアだ。\n
どんなサプライズが仕掛けられているのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "経験者であるボリスや、クラスメイト達があんなにも楽しみにしているのだから、きっといい意味で期待を裏切ってくれることだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……気になるなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、ボリスを筆頭にしたクラスメイト達にも、そのときがくるのを待てと言われている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

play sound se_0774
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ホームルームのある現代魔法史の教室がある階まで降りるための、階段へと差し掛かる。"


show boy_c1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0054
Seito "「……ろよ」"

hide boy_c1_9

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "通りすがりの男子生徒が、ぽそりと私に向かって何かを言ったような気がした。\n
もしかしたら誰かと話していたのかもしれないが、私に向けられたような……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（誰……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこかの授業で一緒だった生徒だろうか。\n
歩きながらも、気になって振り返る……、と。"

play sound se_0244
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後ろを振り返りつつも、前へと踏み出した足が妙なものを踏みつけた。"


show m_cut_bor3u onlayer master
with dis
play sound se_0247
pause 1

play music tension_a_ali
hide m_cut_bor3u
show m_cut_bor3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え……っっ！？」"

play sound se_0245
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぬるぬると滑る軟体のようなものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（あぶな……っ！！）"

play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慌てて重心を戻そうとするものの、遅かった。\n
ずるりと足が滑る。"

play sound se_0091
play sound se_0246 volume .6
camera at hpunch
camera at vpunch
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「きゃっ……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下手に体勢を取り戻そうと体を捻ったのがよくなかったのか、勢いよく私の体は前へとつんのめった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通だったら、まあ転んでもちょっと恥ずかしいぐらいですむ。\n
だが、この場合場所が悪かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "階段だ。\n
悪い場所で足を踏み外してしまったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あまりにも咄嗟のことすぎて、普段なら空で暗唱できる呪文も出てこない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……うわ。\n
これ、かすり傷じゃすみそうにないな）"

play sound se_0638 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "スローモーションのように感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（せっかく何か、楽しいことがあったはずなのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これでは、何か行事があっても、欠席する羽目になるかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "浮かれすぎていたバチが当たったのだろうか。\n
覚悟を決めて、ぎゅっと目を閉じる。"

hide m_cut_bor3
show black onlayer master with close_m

pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「[firstname]……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「！？」"

play sound se_0052
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼ばれた気がした。\n
腰のあたりに、ぐっと強い力がかかる。"

play sound se_0538
play sound se_0553 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "落ちたはずなのに、ちっとも痛くない。\n
助かったのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと、目を開けてみる。"

hide black
show m_bor3_1 onlayer master with open_long
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ、ボリス！！？」"


play music boris_t_ali
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice bor_g0307
Boris "「ふー……っ。\n
間に合ってよかったぜ、あんた、心臓に悪いよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "至近距離にボリスの顔がある。\n
何が起こったのかは分からないものの、とりあえずボリスに助けられたのだということだけは分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「えっと……？？？\n
私……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice bor_g0308
Boris "「……あんたは、床に落ちてたスライムを踏んで転んだの。で、そのまま見事な階段落ちを披露しかけたもんだから、俺が引っ張ったってわけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（スライム？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐにゅりと変なものを踏みつけた感触を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「な……、なんだってそんなものが床に……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice bor_g0309
Boris "「まあ、シンフォニアだしね。\n
散歩中だったんじゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校内の階段を、スライムが散歩中。\n
まあ、猫やウサギだって生徒として在校しているくらいだから、なんでもありだ。"

play sound se_0590 volume .8
pause 1

hide m_bor3_1
show m_bor3_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0055
Seito "「だ、大丈夫か！？\n
ああもう、だから気をつけろよって言ったのに……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "駆け寄ってきた男子生徒は、どうやらさっき通りすがりに私へと声をかけた相手のようだ。\n
あれは、忠告だったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0056
Seito "「さっき、実験器具片付けている途中に、そこでビーカーを落として割ったやつがいたんだ。今、片付けのための道具取りにいってて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（それで気をつけろよ、と教えてくれたわけなのか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに私ときたらぼんやりしていて、その声に気をとられてスライムを踏みつけてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……うう、間抜けだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_3")
T "「ごめんなさい、ちょっとぼんやりしていて。\n
あなたのせっかくの忠告、ちゃんと聞いていなかったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "というか、すれ違い様に「気をつけろよ」なんて。\n
あまりいい意味には聞こえなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0057
Seito "「あ……、いや、もしかして逆に俺に気を取られて踏んじゃったとか？\n
わー、それなら逆に悪いことをしたな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「いいえ、あなたは悪くないわ。\n
せっかくの忠告を活かせなかった私が悪いのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はわざわざ、通りすがりの私に、その先にある危険についてを教えてくれていたのだ。その声を、ぼんやりしていて聞き逃した私が悪い。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0310
Boris "「ま、誰も怪我しなくてよかったよ。\n
あんたも無事だしさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ボリスもありがとう。\n
本当に助かったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice bor_g0311
Boris "「あんたが危なかったらこれぐらい当然だろ。\n
ってことで、そろそろ立ってもらってもいい？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice bor_g0312
Boris "「俺個人としては役得で嬉しいんだけどさ。\n
……でも、ちょっと別の体勢がいいな。見せつけるにしてもさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え？」"

hide m_bor3_2
show m_bor3_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われて、我に返る。\n
ボリスに抱き支えられていたが、体勢がどうなっているのかの全体像を把握していなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慌てて立ちあがる。どうやらボリスは、片手で手すりを掴み、それを支えに思いっきり前へと足を踏み出して私のことを掴まえてくれたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "片足は前に踏み出しているとはいえ、もう一方の足は頭より上の位置に置き去りにされるという不自然きわまりない体勢だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その状態で、ボリスは私を抱き支えていてくれたのだ。"

hide m_bor3_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下手したら、二人で階段を落ちていた可能性すらある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かっと胸の中が熱くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分への不甲斐なさだとか、ボリスを危ないことに巻き込んでしまったことに対する申し訳なさだとか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな危険を冒してまで彼が私を助けてくれた、嬉しさだとか。\n
そんなものを感じるのが、また申し訳なく……。"


show black onlayer master with close_m

play music dream_inside_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0130
Seinen "「これ……、君のお姉さんに渡してくれないかな。\n
頼む……、ずっと憧れていたんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭の中を、今朝の夢、過去の記憶がちらりと過ぎっていく。"

hide black with open_m
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……ああ。\n
まずいな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、ボリスに対して心揺れているのだろうか。"

menu:
    "揺れている。":
        jump gakuen_boris3_4a
    "そんなはずない。":
        jump gakuen_boris3_4b
label gakuen_boris3_4a:
$ lovechara_boris_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……そうなんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "揺れている。\n
毎日顔をあわせているうちに、私の中で進行してしまった。"

jump gakuen_boris3_5
label gakuen_boris3_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（そんなこと、ない。\n
……ボリスは友達だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "毎日顔をあわせ、楽しく過ごす。\n
それが私達の関係だ。"

jump gakuen_boris3_5
label gakuen_boris3_5:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの夢は、少しずつ私の中で大きくなるボリスの存在に対する、無意識の警告だったのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気づかされる諸々。\n
憂鬱になる一方で心が華やぐ。"


show bor_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0313
Boris "「どうかした？\n
なに、どこかぶつけてた？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いいえ、あなたのおかげで無事よ。\n
……本当にありがとう、おかげで助かったわ」"

hide bor_m_01_2
show bor_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice bor_g0314
Boris "「いいって、いいって。\n
あんたも今から教室だろ？一緒に戻ろうぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ」"

play sound se_0774
hide bor_m_02_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょいっと身を起こしたボリスと一緒に、教室に向けて歩き出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（憂鬱になるべきなのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……なんで、わくわくしてしまっているの。\n
こんなの、おかしいわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ざわつく気持ちは、イベントへの期待。\n
そう自分に言い聞かせる。"

with dis
$ hi_mes()

scene bg27_rk_day with Dissolve(.8)

scene bg10_sb_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
jump gakuen_boris4
