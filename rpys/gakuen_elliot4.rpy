label gakuen_elliot4:
scene bg_map_nig
with dis
$ clockanim()

jump gakuen_storm_hatter
label gakuen_elliot4_2:



scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（どうしよう？？？）"

menu:
    "部屋に隠れる。":
        jump gakuen_elliot4_3a
    "外に飛び出す。":
        jump gakuen_elliot4_3b
label gakuen_elliot4_3a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（こ、これ何が起こっているの……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とにかく、状況が掴めない。\n
安易に動くのは、危険に思えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲の様子から、決してそれが深刻な騒動ではないことは分かる。\n
だが、それでも眼下で行われている乱闘は普通じゃない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人と生徒が、魔法や武器をぶつけあっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは帽子屋寮、ならず者の寮といわれている。\n
しかし、まさか学園内で何かの抗争というわけでもないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（でも、戦っているし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「ま、巻き込まれたら、ただじゃすまなさそう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなことで怪我をするのは馬鹿らしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（君子危うきに近寄らず……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この寮の皆は好きだし、寮自体だって気に入っている。\n
だからといって無条件に、こんな暴力沙汰を認められるわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、この騒動が落ち着くまで部屋に篭ることにした。"

with dis
$ hi_mes()

scene bg24_rj_nig_lon with Dissolve(.8)

scene bg_par15_rg_hat_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_medium

scene bg_map_day with Dissolve(1)

scene bg_par12_hct_day
with stripe_l_long

play music view_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次の日になって、それがストームというイベントであったことを知った。\n
新入生に対するどっきりイベントでもあるため、あえて説明がなかったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……イベントだって分かっていたら参加したのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……って、分からないからこそのサプライズだったんだろうけど。\n
やっぱり、調べておけばよかったなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "残念だ。\n
そして、残念なことがもう一つあった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの夜以来、ほとんどエリオットと会うことができなくなってしまったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後のお茶会にも、中庭のにんじん畑にも、エリオットは顔を出さなくなってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ねえ。\n
エリオットはどうしたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう聞くと、また珍しくもエリオットの代わりのようにお茶会に顔を出していた双子と、そのボスであるブラッドは意味ありげに顔を見合わせた。"


show dee_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0065
Dee "「馬鹿ウサギなら、どこかで馬車馬のように働いているんじゃないかな！\n
でも、お姉さんが気にすることないよ」"

hide dee_m_01_10
show dee_m_01_10 at left
with dis

show dam_m_02_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0066
Dam "「そうだよ、お姉さんが気にすることはないよ！\n
馬鹿ウサギは好きで働いているんだから、放っておけばいいんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あんた達……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（この子達にも、仕事があるはずよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この二人がこうしてのんきにお茶などしているから、エリオットは余計に忙しくてここに顔を出せないのではないだろうか。"


show bra_m_03_15 at center
with dis
hide dee_m_01_10

hide dam_m_02_1

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0447
Blood "「……アレも馬鹿な男だからな。\n
放っておいてやりなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「ブラッドまで……」"

hide bra_m_03_15

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ寮長であるブラッドまでが、こうしてテラスでだるだると茶を嗜んでいる。\n
エリオットが忙しいのも当然だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（……でも、それは今までだって同じだった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までは忙しそうにしながらも、時間を作っては畑に顔を出したり、一緒に茶会に参加してくれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（もしかして……、避けられている？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな考えが脳裏に過ぎる。\n
しかし、エリオットに避けられてしまうようなことをした覚えはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……私、何かしちゃったかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不安になって、気付いたらそう口に出してしまっていた。"


show dee_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0067
Dee "「ええ！？お姉さんは悪くないよ！\n
悪いのはあの馬鹿ウサギと、ストームの晩に騒ぎを起こした馬鹿だよ！」"

hide dee_m_02_6
show dee_m_02_6 at left
with dis

show dam_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0068
Dam "「兄弟の言うとおりだよ！\n
馬鹿ウサギとストームに乗じた馬鹿が馬鹿なことしてるだけだから、お姉さんは気にしなくていいんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「ストームの晩に騒ぎ……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "馬鹿馬鹿言っている双子の言葉からすると、ストームの夜に、イベント以外にも何か騒ぎがあったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋に篭っていた私にとっては、外の喧騒はひとまとめにしての騒動だったのだが、どうもいっしょくたではないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドへと視線を向ける。"


show bra_m_03_2 at center
with dis
hide dam_m_02_4

hide dee_m_02_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0448
Blood "「……お嬢さんには、関係のないことだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（……っ！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもと変わらない緩い口調ではあったが、その中にはしっかりとした拒絶があった。私がそこに立ち入ることを、ブラッドは許さない。"


show dee_m_02_1 at left
with dis
hide bra_m_03_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0069
Dee "「うん、お姉さんが知る必要なんかないんだよ。\n
だって、馬鹿ウサギの問題だからね！」"

hide dee_m_02_1
show dee_m_02_1 at left
with dis

show dam_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0070
Dam "「解決したら、また顔を出すよ。\n
僕らがいるから寂しくなんかないでしょ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……そうね」"

hide dee_m_02_1

hide dam_m_01_2


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "沈んだ口調で双子へと返して、私は紅茶のカップを傾ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもどおり一流の茶葉で淹れられた紅茶であるはずなのに、なんだか味が薄いような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（解決したら……。\n
ケリがついたら、またエリオットは会いに来てくれる？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう願うことしか出来ないのが、ひどくもどかしかった。"

with dis
$ hi_mes()

scene bg06_sk_h_day with Dissolve(.8)

scene bg06_sk_h_eve
with dis

scene bg06_sk_h_nig
with dis

scene bg06_sk_h_day
with dis

scene bg06_sk_h_eve
with dis

scene bg06_sk_h_nig
with dis

scene bg06_sk_h_day
with dis

play music view_nig_p_wam

show m_badend1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、ストームの夜以来、エリオットには会うことがなかった。\n
いや、それは正確ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じ学校、しかも同じ寮にいるのだから、見かけることはある。\n
軽く、話すことも。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、エリオットは私を見かけても、いつも物言いたげな、辛そうな顔をして目をそらしてしまう。\n
話も続かない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな彼の様子を見るのが辛くて、私もいつの間にかエリオットを避けるようになってしまっていた。\n
私達は、次第に疎遠になっていく。"

play sound se_0693 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（あの夜、何があったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌われたわけではないと思う。\n
エリオットの目は、嫌いな人間を見る目ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（だけど、分からない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのとき、別の選択肢を選んでいたら、もっと別の形の今があったのだろうか……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふとしたことで人間関係が希薄になるなんて、よくあること。\n
これまでにも、うまくいかない付き合いというものはあった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、エリオットとのそれは特別で……。\n
それでも、もう先を望むことは出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（これだから……、向いていないのよ、私には）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ、始まりもしていなかったが……。"

hide m_badend1 with Dissolve(5)
hide ali_m_06_16
hide frame_par_togaki
with Dissolve(5)
stop music

##endmemory
jump gakuen_c
label gakuen_elliot4_3b:
$ lovechara_elliot_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（外に行こう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、好奇心には逆らえない。\n
何度それで痛い目にあっても、だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、賢くなんかなれない。"

play sound se_0742
show magic_g onlayer master with Dissolve(1.5)
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

hide magic_g with Dissolve(1.5)
play sound se_0216
pause .5
play sound se_0348
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早口に呪文を唱えると、窓を開けると同時に外へと飛び出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "飛行には箒という媒体を使うのが一般的だが、自由落下を和らげる程度の浮遊ならば、媒体がなくとも問題ない。"


play music opposition1_a_ali
play sound se_0216

scene bg20_gd_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "室内履きのまま、中庭の芝生の上に降りる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「エリオット、どこなの！？」"

play sound se_0794 volume .7
play sound se_0686 volume .6
pause .20
play sound se_0457 volume .7
pause .30
play sound se_0439 volume .6
pause .4
play sound se_0659 volume .8
$ flash("red",.2)
$ flash("off_red",.2)
$ flash("gray_red", .2)
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声に出して探してみるが、周囲の声や音にかき消されて返事は返ってこない。\n
周囲はまるで夜戦だ。"

play sound se_0792
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼんやりとした月明かりの下、どこか楽しそうで勇ましい声が響きあっては、金属のぶつかりあう音や魔法の炸裂音が響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下から見たエリオットがいた辺りを目指して、戦闘を避けて中庭を走る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中に飛び込んで分かるのが、その楽しそうな空気。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓から見たときには、ただの暴動にしか見えなかった騒動だが、戦う生徒も、応戦する使用人達も、皆口元に笑み浮べて楽しげだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あちこち服をほつれさせたり、怪我をしたりもしているが、皆イキイキとして口元には笑みが滲んでいる。"


show boy_c2_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0012
Seito "「これでどうだ……！！」"

play sound se_0439
pause .4
play sound se_0193
$ flash(.1)

show siyounin_a2_3 at right
with dis
hide boy_c2_7
show boy_c2_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0007
Servant "「まだまだ……！！」"

hide boy_c2_7

hide siyounin_a2_3
##[chara2 PAY ATTENTION="false"]
play sound se_0458
pause 1
play sound se_0665
$ flash("pastel_blue", .1)
$ flash("periwinkle_blue", .1)
$ flash("jean_blue", .1)

show boy_d2_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0017
Seito "「あっぶね……！！」"

hide boy_d2_4
show boy_d2_4 at left
with dis

show maid_b_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0111
Maid "「ふふ、逃げてばかりいていいんですか？」"

hide maid_b_9

hide boy_d2_4

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（本物の暴動ってわけじゃないのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ある程度察してはいたとはいえ、安心した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「……エリオットはどこかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "喧騒の中、先刻見かけたエリオットを探し、走り回る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深刻な危機ではないということは分かっていても、自分一人だけ状況が把握できていない状態で、夜戦の中をうろうろするというのは心細い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここにいるのは、同寮生と、普段お世話になっている使用人達だというのは分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分かっていても、それがこんな非日常的な状況で、さらには夜の闇の中だということもあって、知らない誰かに見えて……、不安になるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "影絵のように、顔が見えない人が動き回る。\n
誰かのでたらめな悪夢に迷い込んだような気分だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと、人垣の向こうにエリオットの耳が見えたような気がした。\n
ほっとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……間違いようがない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "長身に、特徴的な耳。\n
いや、ウサギなら他にも心当たりがあるが、耳がなくとも彼のことは分かる気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「エリオット……！」"


show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice eri_g0109
Elliot "「[firstname]！？\n
あんた、なんでこんなところに……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは窓から見たのと同じように、一歩引いていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "積極的に使用人と戦うというよりも、双子や、他の生徒達の援護をするような形で少し離れた木陰に立っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その手の中にあるのは、彼が扱いを得意とする、銃の形をしたマジックアイテムだ。これがブラッドの言っていた、彼にとっての魔法媒体なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大股に駆け寄ってくる彼の姿に、安心する。"


play music garden_nig_p_wam
hide eri_m_01_5
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0110
Elliot "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「エリオット？」"

play sound se_0052
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "近くまでやってきたエリオットは、ぎょっとしたように息を呑んで、それからばさりと着ていた制服の上着を脱ぐと私の肩へとかけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_2")
T "「へ？」"

hide eri_m_01_10
show eri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_2")
voice eri_g0111
Elliot "「あ、あんた、なんつー格好してんだよ……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「あ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば、私は風呂上がりで、パジャマ代わりのネグリジェ姿だったのだ。"

hide eri_m_01_9
show eri_m_03a_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0112
Elliot "「あんた、その格好で飛び出してきたのか？\n
髪も濡れてるし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "銃を握るのとは逆の手が、確かめるように私の頭へと触れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "タオルドライはすませているので、濡れている、というほどびちょびちょではないのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（あ～……、でも乾ききってもいないかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（冷静になると、結構恥ずかしい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなあられもない格好で、外を駆け回っていたなんて、姉さんに見られたら間違いなく怒られる。\n
やはり私は淑女にはなれそうにない。"

hide eri_m_03a_4
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0113
Elliot "「ああ、靴も室内履きじゃねえか。\n
痛くなかったか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「芝生だから平気よ。\n
それより、これは何の騒ぎなの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "へにょ、と眉尻と一緒に耳まで下げて心配そうにするウサギさんへと、一番の疑問をぶつけた。"

hide eri_m_01_10
show eri_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0114
Elliot "「ああ、これはストームっていうんだ。\n
シンフォニアの伝統行事の一つだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……男子生徒と使用人が夜の庭で乱闘もどきを繰り広げるのが？\n
それ、どんな伝統なのよ」"

hide eri_m_02_1
show eri_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice eri_g0115
Elliot "「戦うことが目的……、っつか。\n
使用人との戦闘を乗り越え、女子寮に忍び込んで、親睦を深めることが目的だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_3")
T "「……{size=+20}ずいぶんと不純な伝統ね{/size}」"

hide eri_m_01_4
show eri_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_3")
voice eri_g0116
Elliot "「はは。いやあ、夜這いとかじゃねえんだぜ？\n
どんちゃん騒ぎがしたいっつーか、修学旅行のノリだよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_8")
T "（でも、そういうのって、まったく不純じゃないってわけでもないでしょう）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（……エリオットも？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼がこうして、そのイベントに便乗していることが気になった。\n
副寮長だから、こういった寮ぐるみのイベントには参加して当然なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それとも……、誰か親睦を深めたい人がいて、こうしてやってきたのだろうか。\n
そうだとしたら……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（いやいや、エリオットが誰と仲良くしようが関係ないわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中にわき起こりかけた、正体不明の感情を散らそうとする。"

hide eri_m_02_2
show eri_m_03a_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0117
Elliot "「ガキ共は、使用人と戦うほうを楽しんでやがる。\n
到達したいってより、過程が優先だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……なるほど。\n
ふふ、あの子達らしいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人達の妨害の目をくぐり、女子寮に忍び込むのが目的だというイベント、ストーム。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子達においてはその目的と手段とが、見事に入れ違ってしまっているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（エリオットは？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "関係ない、と思おうとしているのに、質問が口をついてしまいそうになる。\n
それを誤魔化したくて、別のことを聞いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ブラッドは？\n
見当たらないようだけれど、ブラッドも参加しているの？」"

hide eri_m_03a_8
show eri_m_03b_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「エリオット？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一瞬エリオットが眉を寄せたように見えた。\n
気まずい沈黙が落ちる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（え？\n
なんで？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの話題を持ち出せば、エリオットは上機嫌で答えてくれる。\n
そうすれば、会話も弾むと思ったのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

hide eri_m_03b_11
show eri_m_03b_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
Elliot "「…………」"

hide eri_m_03b_12
show eri_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice eri_g0118
Elliot "「あんた……」"

play sound se_0097
$ flash(.1)
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_1")
T "「わ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが何かを言いかけたタイミングで、魔法の流れ弾が飛んできた。巻き込まれるほど近くではなかったが、次も同じように外れてくれるとは限らない。"

hide eri_m_01_7
show eri_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0119
Elliot "「ち、ここは危ねえな。\n
あんたの部屋にいこう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_4")
T "「へ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（私の部屋？）"

play sound se_0148
camera at hpunch
camera at vpunch
show m_eri4_1 onlayer master
with dis
hide eri_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き返すより先に、ひょいとエリオットの腕に抱きかかえられていた。\n
彼は、軽々と私の身体を片腕だけで抱き上げてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "母親が子供を抱きかかえるような、膝のあたりを腕で抱き支え、その腕に座らせるような形だ。"


play music battle_ali
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0120
Elliot "「強行突破するからな。\n
しっかり掴まってろよ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「きょ、強行突破って……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice eri_g0121
Elliot "「強行突破は強行突破だ。\n
行くぜ！！」"

play sound se_0618
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「わっ、わわわわ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが、楽しげに答えて走り出したものだから、私は慌ててその肩にしがみつく。\n
振り落とされてしまいそうだ。"

hide m_eri4_1

play sound se_0501
$ flash(.1)
pause .1
play sound se_0501
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが目の前に立ちはだかる使用人達を蹴散らす。\n
銃声が、すぐ近くから聞こえる。"


show boy_c2_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0013
Seito "「すげえ……！！\n
エリオット副寮長、女子を一人誘拐したぞ……！！」"

hide boy_c2_4
show boy_c2_4 at left
show siyounin_a1_4 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0008
Servant "「ええええ！？\n
なんで女子が攫われているんだ！？」"

hide boy_c2_4
show boy_c2_4 at left_center
hide siyounin_a1_4
show siyounin_a1_4 at center
show boy_d2_7 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0018
Seito "「ま、まじで！！？\n
俺らも負けてらんねー！！！」"

hide boy_c2_4

hide siyounin_a1_4

hide boy_d2_7


show maid_b_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0018
Maid "「ちょっと！？これはそういうイベントじゃありませんよ！？」"

play sound se_0794
hide maid_b_4
show maid_b_4 at left
with dis

show maid_b_5 at right
with dis




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0112
Maid "「つ、連れ出すのってありでしたっけ……？」"

hide maid_b_4
show maid_b_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0019
Maid "「なしです、なし！\n
不純異性交遊は禁止です！」"

hide maid_b_5
show maid_b_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0113
Maid "「でも、連れ出しているだけで、不純異性交遊とは……」"

hide maid_b_8
show maid_b_8 at left_center
hide maid_b_6
show maid_b_6 at center
with dis

show siyounin_a2_7 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0030
Servant "「と、とりあえず止めとけ……！！」"


show m_eri4_1 onlayer master
with dis
hide maid_b_8

hide siyounin_a2_7

hide maid_b_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0122
Elliot "「は！\n
止められてたまるかよ！！」"

play sound se_0618
play sound se_0772
$ flash(.1)
$ flash(.1)
$ flash(.1)
$ flash(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "低く獰猛に笑うエリオットの声は、まさしく誘拐犯といった迫力だ。\n
オレンジがかった金髪をなびかせ、私を抱えて夜を走りぬける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "至近距離から銃撃を浴びせ、敵が怯んだ隙に駆け抜けていく。\n
その様は、酷く凶暴で、魔法使いというよりもマフィアか何かのよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（でも……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の目の前には、その金髪の間からにょっきりと伸びたウサギ耳がある。\n
ふわふわと、なびくウサギ耳が目の前で揺れている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……怖いとは思えないなあ）"
menu:
    "（むしろ格好いいくらい）":
        jump gakuen_elliot4_4b
    "（むしろ可愛いくらい）":
        jump gakuen_elliot4_4a
label gakuen_elliot4_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（むしろ格好いいくらい）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……とは思わないけど。\n
暴力は反対だし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、そこも含め、それ以外の点で愛着を持っている。\n
愛着……、いや、明確な好意といっていい。"

jump gakuen_elliot4_5
label gakuen_elliot4_4a:
$ lovechara_elliot_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（むしろ可愛いくらい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "暴力的な面を見ても尚、愛着を持っている。\n
愛着……、いや、明確な好意といっていい。"

jump gakuen_elliot4_5
label gakuen_elliot4_5:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（この人に……）"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このままどこに連れて行かれても、それこそ本当に誘拐されてしまったとしても、怖くない気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0123
Elliot "「……っ悪い！\n
揺れたか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice eri_g0124
Elliot "「や、今あんた、しがみついただろ？\n
不安になるなってほうが無理だろうけど……、俺、あんたのこと絶対落としたりなんかしねえから」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice eri_g0125
Elliot "「怖がるなよ。\n
……な？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットに言われて、かっと頬に熱が集まった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（怖くない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怖くは、ないのだ。\n
不安もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、彼にしがみついたのは、きっと別の理由だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "上着を脱いで私に貸しているせいか、薄いシャツ越しに彼の体温を感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうしてくっついていると、彼が動くたびに私とは違うがっしりとした骨格、筋肉の躍動する様までが、リアルに感じられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_10")
T "（～～～っ！！）"

play sound se_0313
hide m_eri4_1
show m_eri4_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分でも、顔が赤くなっているのがよく分かる。\n
見られたくなくて、私はエリオットの肩に顔をうずめるようにしてしがみついた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_11")
T "（～～ぎゃあああ！\n
似合わない！）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（似合わないわよ、こんなの！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋愛なんて、似合わない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不相応だとすら思える。\n
私には、うまく向き合えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_5")
T "（自分の気持ちすら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ましてや、相手の気持ちなんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0126
Elliot "「なあ？怖いのか？\n
そうだよな、怖いよな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の戸惑いを、脅えととったのか。\n
ぎゅう、とエリオットの私を抱く腕に力がこもる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "立ちふさがる使用人達をかわし、撃破し、彼はどんどんと女子寮に近づいていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞こえるのは銃声と、牽制の声と、悲鳴と。\n
そして、彼の声だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "容赦なく敵を蹴散らして進むエリオットの横顔は、好戦的でいて、それでも凛々しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、私を見る目はどうしようもないほどに臆病だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0127
Elliot "「なあ……、そんなに怖がるなよ。\n
酷いことなんかしねえから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声にも、おろおろとした調子が混じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（大切に、されている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お嬢様どころか、お姫様にでもなったような気にさせてくれる。\n
まったく似合わない、殊勝な気持ちに。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……怖くないわ。\n
ちょっと……、この格好だからか、寒いだけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice eri_g0128
Elliot "「そ、そっか！\n
そうだよな！寒いよな！早く中に……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice eri_g0129
Elliot "「え、え～と、もうちょっとの辛抱だからな……！\n
すぐに終わらせる！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……うん」"

play sound se_0055 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "素直に頷いて、エリオットの肩にしがみつく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完全なるぶりっこだ。\n
可愛い振りをしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……ああ、似合わない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今はもう、顔も不明瞭な先生に対する態度を思い出す。\n
振り返れば、あれは本当の私ではなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットへは素の私も見せている。\n
今更ぶりっこしても意味がないのに……、えらく自然に、おとなしくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "演技じゃない。\n
それは、凶暴な彼が私に対して臆病なのと似ていて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（似合わない……、けど、前とは全然違う）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は相手に向き合っていて、彼も、他ではなく私を見てくれている。それが、どういった感情によるものにしても……、以前のような虚しさは感じない。"

play sound se_0734
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子寮のほぼ真下まで到着したところで、エリオットは呪文を小さく唱えた。\n
そして、大きく踏み込んで……。"

play sound se_0373
hide m_eri4_2
show bg06_sk_h_nig onlayer master with spread_short
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "{size=+20}「！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "{size=+20}跳ねた。{/size} "

play sound se_0268
play sound se_0698
pause .20
play sound se_0091
pause 1
play sound se_0387
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがウサギさん。\n
素晴らしい跳躍力だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……魔法で補助していたけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、エリオットがやると自力で跳んだように見えるのは、やはりウサギ耳効果だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後からは、悔しげだったり、感嘆するようなどよめきが聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0009
Servant "「あああああっ！！\n
一人突破しました！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0031
Servant "「エリオット＝マーチなら仕方ない……！\n
次に備えろ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0114
Maid "「あ～～っ！\n
悔しい！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0014
Seito "「エリオット副寮長、格好いい……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0019
Seito "「さすがウサ……、じゃなくてさすが副寮長だな」"


scene bg25_rr_nig
with dis

show eri_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

hide eri_m_02_7
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0130
Elliot "「……っと。\n
で、あんたの部屋はどこだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中庭の喧騒に気を取られていた私は、エリオットの声に慌ててきょろきょろと現在位置を確かめた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは適当に開いている窓を選んだようだったが、それこそ、さっき私が飛び降りた窓だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまり、今いるのは私の部屋の目の前だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そこが私の部屋よ。\n
鍵も開いているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょうど開錠して、部屋に入りかけたところで騒ぎが起こったのだ。\n
エリオットは私の声に頷いて、私を抱きかかえたまま部屋へと入った。"

hide eri_m_01_8
with dis
$ hi_mes()

scene bg25_rr_nig with Dissolve(.8)
scene bg24_rj_nig
with stripe_l_long

play music cliff_eve_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋に入っても、エリオットは私を抱きかかえたまま。\n
ベッドにまっすぐ向かって、ぽすんと腰掛ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その腕に抱かれていた私は、自然とその膝に乗せられる形になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……えっと。\n
エリオット？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろっとエリオットの膝の上から降りようとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくらなんでも、二人きりで、ベッドの上で膝に乗せられているという状況はあまりよろしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何が一番よろしくないって、それに対して胸を高鳴らせつつも、拒否感を覚えない自分が一番よろしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……まずい、わよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭の中に、ブラッドの言葉がよみがえる。"

hide bg06_sk_h_nig
show bg24_rj_nig_s onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0430
Blood "「今の君は……、深い穴に落ちていく最中に見える。\n
愚かしくも、退屈知らずの世界がひらけそうじゃないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0431
Blood "「……だが、賢い君は、どこか穴の途中で引っ掛かって、地上に戻るのかもな。\n
[firstname]」"

hide bg24_rj_nig_s

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_5")
T "（……私って、賢くないから）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれは、厭味にしか終わらない。\n
結論としては、どこにも引っ掛からず、まっさかさま。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ねえ、エリオット？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今はどことなく憮然とした顔で黙り込んでいるウサギさん。\n
道連れにすることは出来るのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……って、エリオット？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ灯りをつけられてはいないが、月明かりはある。\n
目はじょじょに夜闇に慣れ、次第に表情の詳細も分かってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットはむっつりと不機嫌そうな……、拗ねたような顔で黙り込んでいた。"

##[rchara1 PAY ATTENTION="false"]
show eri_m_03b_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

play sound se_0055 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは無言のまま、彼の膝の上から降りようと身じろいだ私のウエスト部分をぎゅうと抱いて引き寄せなおす。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_4")
T "「……エリオット？\n
どうしたのよ？」"

hide eri_m_03b_11
show eri_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_4")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、むすっと黙ったままだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "原因が分からない私も、何を言っていいのか分からない。\n
結局、相手が口を開くまで待つような、我慢比べのような沈黙が続く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どれくらい沈黙が続いただろうか。\n
エリオットがようやく口を開いた。"


play music flower_nig_p_wam
hide eri_m_01_7
show eri_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0131
Elliot "「…………。\n
……あんた、ブラッドが好きなのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「な」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（何ですって？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉を失う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意味もなく、口をパクパクとしてしまう。\n
どこをどう見て、何をどう聞いていたら、そんな勘違いが生じるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のそんな反応を、エリオットは肯定と取ったものらしい。\n
眉間に皺を寄せ、その顔つきが苦いものとなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……そんな反応、しないでよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "調子にのってしまいそうになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前とは、本当にまるで違う。\n
自惚れているのではと不安になりはしても、それでも何かしらのつながりは持てていると思えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一方的で、相手のことがまるで分からない恋とは違う。\n
過去のそれは憧れが先行していて、交流も何も持てなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（まあ、失恋するなら、今みたいに友達関係のほうがややこしそうだけど）"

hide eri_m_01_6
show eri_m_03b_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice eri_g0132
Elliot "「……好き、なんだな？\n
そんな格好で、飛び出してきて、探すぐらい……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……だったら、どうするのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……そうよ。\n
好きなんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先生への憧れと違い、こんなふうに生意気なことも言える。\n
おとなしく、しおらしくもなるが、それだけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "変な言い方だが、手応えを感じる。\n
ちゃんとやりとりを持って、好きになった、と。"

hide eri_m_03b_12
show eri_m_03b_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0133
Elliot "「……っ」"

play sound se_0372

show m_eri4_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_1")
T "「……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気づいたときには、視界がぐるりと回転していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「え？\n
は？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "天井を背景に、私を見下ろすエリオットの顔が見える。\n
今まで見たことのないような、苦味を帯びた顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0134
Elliot "「あんたを、俺のもんにする。\n
……ブラッドには、渡さねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_10")
T "{size=+20}「な」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "{size=+20}（何ですって？）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先刻と同じような思考。\n
だが、今回は言葉を失うわけにはいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "反論しようとしたが、思うほど簡単ではない。\n
咄嗟に言葉が出てこない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "押しのけようとした腕は、両手首をいともあっさりと片手でまとめて頭上に貼り付けにされた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……な、慣れている？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "出てきたのは、こんな言葉。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不良グループのＮＯ．２をやっているだけあって、荒事には慣れているだろう。\n
だが、こんなことには慣れていてほしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……女性の押し倒し方、なんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「や、やっぱり、ストームってこういう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice eri_g0135
Elliot "「違うっつってんだろ。\n
でなけりゃ、職員側が許すはずねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice eri_g0136
Elliot "「女子寮に侵入するっていっても、寝てる奴を叩き起こして馬鹿騒ぎするようなイベントだ。羽目をはずしすぎないよう、普段なら俺も監視側なんだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「か、監視役になっていないじゃない。\n
こんな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice eri_g0137
Elliot "「そうだな。\n
自分で破ってる」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice eri_g0138
Elliot "「……だが、ならず者の集まりっつうくらいだ。\n
俺なんかに監視役を任せるほうが悪いだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「そんなこと言って……。\n
副寮長でしょ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice eri_g0139
Elliot "「ああ。\n
……まあ、普通なら寮長が監視すべきなんだろうけどな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice eri_g0140
Elliot "「ブラッドは、ストームには参加してない。\n
今頃、いつものテラスで、一人で茶会でもやってるはずだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、冷たい声音で言う。\n
私に向かって、諦めろとでもいうように、淡々とその事実を突きつける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、私は別に堪えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「ブラッドのことなんか、聞いていないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが今どこで何をしていようが、私には関係のないことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0141
Elliot "「ブラッドは……。\n
……あんたのことなんか、好きじゃねえよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（私のことなんか、ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……そう。\n
それで？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドにどう思われているかなんて、どうでもいい。\n
私が知りたいのは、エリオットが私をどう思っているか、だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "組み敷かれたまま、私はまっすぐに彼を見上げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0142
Elliot "「だ、だから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットの声が、熱っぽく掠れた。\n
状況的に優位なはずの彼のほうが動揺しはじめる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「だから？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "毅然と見せながらも、私だって心臓がうるさい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼を振りほどくことを考えるよりも、そんな高揚をどう表に出さずにやり過ごすかのほうが、私にとっては大問題だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0143
Elliot "「……俺が、慰めてやるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「エリ……っ」"

hide m_eri4_3
show m_eri4_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼びかけた唇を、塞がれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相変わらずその金髪の間からウサギ耳が伸びている。\n
だが、今の彼はウサギではなく、何か別の……危険な肉食獣のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_3")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_3")
voice eri_g0144
Elliot "「は……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（食べられて、しまいそう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唇から、バリバリと。\n
口付けをされて息が苦しくなる。"

play sound se_0007 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っん！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "息苦しくて身をよじるものの、エリオットに押さえつけられてどこにも逃げようがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "蹴り飛ばしてやろうとするものの、察したらしきエリオットに器用に足の間に体を割りいれられて、それすらも無効化されてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（どれだけ慣れているのよ……っ！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いいようにされて口付けられる現状よりも、エリオットがこういったシチュエーションに慣れていることに腹が立つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（我ながら怒りの方向性がズレてきたような気がする……）"


hide m_eri4_4
show m_eri4_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "酸欠で頭がくらくらしてきたせいだろうか。やがてエリオットが顔をあげたときには、私は息を弾ませながらベッドにぐったりと伸びていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目元がじっとりと濡れているのは、息苦しさによるものだ。\n
……そういうことにしておきたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0145
Elliot "「……泣くなよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_3")
T "「……あなたが泣かせるようなことをするからでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これは、たしかに、以前とはまったく違う恋だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "告白もせずにこんな状況になろうとは、先生との関係においては想像も出来なかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、それどころか、こんなふうにキスをすることも……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（まったく、現実的じゃなかった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "始まりすらしないわけだ。\n
先生とのその先など見えず、失恋前提だったから。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0146
Elliot "「あんたを泣かせたかったわけじゃないんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "苦しそうに言う、大きなウサギさん。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが、指の背で私の目元を拭う。\n
これだけのことをやらかしておいて、その手つきは壊れ物を扱うようにそっと優しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不器用なのか、器用なのか。\n
過去が分からなくとも、距離感は感じない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……腕、痛いわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice eri_g0147
Elliot "「……っ、すまねえ。\n
でも……、分かっただろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice eri_g0148
Elliot "「あんたは、俺には勝てねえよ。\n
暴れても、泣いても……、俺には勝てねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の両手首を戒めていた片手を浮かし、解放しながらも囁く声は、低く脅しつけるようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0149
Elliot "「だから……。\n
俺に酷いことさせないように、抵抗とか……、嫌いだとか言わないでくれよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0150
Elliot "「……あんたに、酷いことしたくないんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中がぞくぞくとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怖いからじゃない。\n
独占欲を向けられていることが、なんだか……。"

play sound se_0551

play music residence_p_wam
hide m_eri4_5
show m_eri4_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "押さえつけられていた腕を、そっと持ち上げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは言葉どおり、私の抵抗なんてたいしたものじゃないと思っているのか、ちらりと視線を一度向けたものの、押さえつけはしなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（甘いわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、自分には弱点などないとでも思っているのだろうか。\n
私は、その手を彼の頬へと触れさせた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かあ、っとそれだけでエリオットの頬に朱がのぼる。\n
たった今私を無理矢理ねじ伏せてキスをした男とも思えない初心な反応だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その反応に、私は気を良くする。\n
慣れているような平静さよりも、ずっといい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……自分が触れられるのは、緊張するの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice eri_g0151
Elliot "「あ、あんたが嫌がらないとか……っ、予想外だから驚くだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「……嫌がったら酷いことをするって言ったのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice eri_g0152
Elliot "「そ、それは……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「嫌いって言わせて、酷いことをしたかったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice eri_g0153
Elliot "「……っ！\n
そ、そういうわけじゃ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな状況に関わらず微笑んでしまう。\n
可愛いウサギさんだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう、ウサギさん。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（私にだって、酷いことは出来るのよ？）"

play sound se_0373
camera at hpunch
camera at vpunch
hide m_eri4_6
show m_eri4_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice eri_g0154
Elliot "「……っいいい！！！？」"


play music gag1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが素っ頓狂な悲鳴をあげる。\n
私が、頬から滑らせた手でもってそのウサギ耳をむんずと鷲掴んだからだ。"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅうぎゅうっと、容赦なく引っ張ってやる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0155
Elliot "「いて！いてえ！いてえよ！！！\n
やめ……っ！いててててててっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0156
Elliot "「たたたたたた！\n
痛い！痛いんだって……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「ふふん。\n
私には勝ち目がないんじゃなかったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどのエリオットの発言をわざとらしくひっぱってきて、意地悪く笑ってやれば、エリオットは情けなさそうにへにょりと眉尻を下げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0157
Elliot "「分かった……！\n
分かったから放してくれよ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「へえ？\n
何が分かったのかしら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（ちっとも、分かっていそうに思えないけど？）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice eri_g0158
Elliot "「あんたは強い！\n
充分、俺に抵抗できる！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……{size=+20}そこなのか。{/size}\n
とんでもないお墨付きを、帽子屋寮のＮＯ．２からいただいてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0159
Elliot "「見くびって悪かったって！\n
いてててててて！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……謝るところはそこじゃないんじゃない？\n
私にキスしたことは謝らないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice eri_g0160
Elliot "「……！！\n
それは……、謝らねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは半ば涙目になりながらも、唇をへの字にして言い切った。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0161
Elliot "「あんたが好きだから……、誰にも渡したくないんだ。\n
それは、謝らねえ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽかん、としてしまった。\n
エリオットの私を見る目は真っ直ぐだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな真っ直ぐな目で、当たり前のように、好意を打ち明けられた。\n
いや、打ち明けるというよりも宣言された、というか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、そんな意図的なものでもなかったような。\n
本当に、当然のように彼はさらっと言ってのけた。"


play music night_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……私が、馬鹿みたいじゃない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やっていることは結構最低だと思うのだが、それにしても格好いいではないか。\n
先生よりも、私よりも格好いい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手に、直に向かっている。\n
怯まないし、言い切れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（言われたほうだって、気持ちいい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人づてに頼んだり、押し込めてしまうより、ずっと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう、私だって、躊躇うことなんかなかった。\n
こうすればよかったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最低なのに、理想像だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（こんなふうに）"

play sound se_0054
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice eri_g0162
Elliot "「ぎゃ……！！\n
いてえ！いてえええええええ！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後に一際強くぎゅむーっと引っ張ってから、私は手をエリオットの耳から離した。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐに逃げるかと思ったものの、彼は私の上からそれでもどこうとはしない。"

hide m_eri4_7
show m_eri4_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0163
Elliot "「ってえ……。\n
けど……、何してもいいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「え……。\n
{size=+20}痛いの、好きなの？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice eri_g0164
Elliot "「ば……っ。\n
ちげえよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice eri_g0165
Elliot "「俺、あんたが俺のものになるなら……。\n
あんたに何されてもいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……それ、男が言う台詞じゃないでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice eri_g0166
Elliot "「……言うよ。\n
あんたが俺のものになるなら……、何だって」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットの言葉はどこまでもまっすぐだ。\n
ストレート極まりない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "捻くれて変化球ばかりを好んでしまいがちな私には、どうしていいか分からなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……ばか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
voice eri_g0167
Elliot "「ああ、俺は馬鹿だ。\n
あんたみたいに真面目なお嬢さんとは……、釣り合わねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを言って、エリオットはここシンフォニアの生徒なのだ。\n
副寮長も務めているし、たいしたものだと思うのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0130_5_ell
Seinen "「ずっと憧れていたんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先生の声が響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0131_ell
Seinen "「素敵な人で……、声も掛けづらいほどで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0132_5_ell
Seinen "「かなわないとは分かっているんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういうものなのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（好きな人は……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の理想に見えてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「そうね。\n
あなたは本当に馬鹿だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
Elliot "「[firstname]……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しょぼん、と耳が垂れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「私がブラッドのことを好きだなんてとんでもない勘違いをするほど馬鹿だし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice eri_g0168
Elliot "「え……？\n
勘違い……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「そうよ。\n
それに……、私みたいな捻くれた女を好きになるところも、馬鹿よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice eri_g0169
Elliot "「いや、あんたは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「欠点だって、多いのよ。\n
近くにいたら、分かるでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前とは違う。\n
理想を持っていても、ろくに口もきけないような恋ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0170
Elliot "「分かんねえよ……。\n
いや……欠点なんて誰にでもあんだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0171
Elliot "「でも、俺はあんたが好きだよ。\n
欠点ってのがあったにしても……、好きだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "欠点なんて、山のように。\n
好奇心には勝てないし、冷静なつもりでとんでもない行動をとったりする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……こんな格好で窓から飛び出したのも、あなたを見たからだわ。\n
私が探していたのはブラッドじゃなくて、あなたよ、エリオット」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice eri_g0172
Elliot "「え……、っでも、あんた……！\n
ブラッドのことを一番最初に……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「私が、エリオットは誰に会いたくて降りてきたの、なんて。素直に言えるような女だと思っているなら、やっぱりあなたは私を誤解しているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、迷うようにうろうろと視線を逃した。\n
一応、私という女の人間性を理解しつつあるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これで、よかったのだろうか。\n
幻想上の私に好きだと言われても、私はそんな子ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0173
Elliot "「それじゃあ……。\n
あんたが、好きなのは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せがむ言葉が熱っぽく、そしてやはりまっすぐに私の心に届く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（恋愛なんて似合わないけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "似合う人なんて、いるのだろうか。\n
誰だって、みっともなくなるし、綺麗には振る舞えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分のことで精一杯で……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「……好き、よ。\n
エリオット」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉なのに、なぜだか、ラブレターを渡した図が思い浮かぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "派手すぎないレターセットで、何度も書き直した手紙。\n
忘れられないほど、記憶に残る、それ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、渡す相手は……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（言えた）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際に音として口にすると、とんでもない羞恥に襲われた。\n
かあああっと頬に熱が集う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな様を、真上からまじまじと見下ろされている。\n
じりじりと視線を感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（……うう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……{size=+20}目潰ししたくなる。{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、私だってムードというものは心得ている。\n
抗議するだけに留めておいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「み、見ないでよ。\n
恥ずかしいから……！！」"

hide m_eri4_8
show m_eri4_9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice eri_g0174
Elliot "「～～～っ！\n
……あんたって、本っ当可愛い女だよ\n
な！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "{size=+20}「はあ！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は可愛くなんかない。\n
態度も何もかも、可愛げのない女だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大体、私なんかを好きになるとは、エリオットはちょっとおかしい。\n
きっと、にんじんの食べすぎだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カロチンは目にいいと聞くが、きっと過剰摂取が祟ったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_4")
T "「エリオット、あなたちょっとにんじんを控えるべきだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_4")
voice eri_g0175
Elliot "「は？何言い出すんだよ。\n
にんじん料理なら分けてやるぜ？独り占めなんて、ケチな真似しねえって」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「いや、そうじゃなくて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice eri_g0176
Elliot "「遠慮すんなって。\n
あんたになら、何だって……」"

play sound se_0551
hide m_eri4_9

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりとウエストの裏に手をさしこまれ、そのまま引き起こされて抱きしめられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "力強くはあるが、決して私が苦しくない程度の気遣いの滲む抱擁だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットはくい、と片手で私の顎を持ち上げ……。"

play sound se_0627
hide eri_m_03b_11
show eri_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0177
Elliot "「……ち。\n
もう終わりか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外から響いた笛の合図に、苦虫でも噛み潰したかのように顔を顰める。"

hide eri_m_02_3
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0178
Elliot "「この笛が、ストームの終了の合図なんだ。\n
……男子寮に戻って、全員戻ってきてるかどうかの点呼をとらねえと」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「寮長にやらせなさいよ、寮長に」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの男はストームにも参加せずに、一人で優雅に茶会を決め込んでいるらしい。\n
それぐらいさせても、罰は当たらないと思う。"

hide eri_m_01_8
show eri_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0179
Elliot "「はは、俺もあんたともっといたいが……。\n
守らなきゃいけねえルールもある」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちゅ、とエリオットがし損ねたキスの代わりのように、私の額へと唇で触れた。\n
なんとも、甘ったるいやりとりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "似合わない。\n
私がこんなふうになるとは想像も出来ないような……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中が痒くなりそうなほどなのに、満たされてもいる。"


play music room2_p_wam
hide eri_m_01_3
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0180
Elliot "「さて……、と。\n
行く前に……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは立ち上がり、上着を羽織り直しながら、私の部屋をきょろきょろと見渡した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「どうしたの？」"

hide eri_m_01_8
show eri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice eri_g0181
Elliot "「ストームってイベントは、肝試しみたいなとこもあってさ。ちゃんと女子の部屋に辿り着けた証拠として、戦利品を持ち帰ることになってんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……傍迷惑なイベントね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "押しかけて、侵入して、さらにはモノまで強奪していくとは。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは物色するように視線を彷徨わせた結果、机の上に無造作に置いてあった私のリボンを手に取った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「だ、駄目よ、それは。\n
明日も使うんだから」"

hide eri_m_02_12
show eri_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice eri_g0182
Elliot "「へへ、大事なものだからこそ、奪い甲斐がある。\n
そしたらあんた、取り返しにきてくれるだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「……取り返す？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは私のリボンをその腕に緩く絡めたまま、窓辺へと向かう。\n
中庭を向いた窓だ。"

play sound se_0585
hide eri_m_02_4
show eri_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0183
Elliot "「ああ。一週間後に、今度はブリーズってイベントがあるんだよ。\n
そっちは、女子が奪われたものを取り返しに、男子寮に押しかけるんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……この学校って。\n
本当に、イベント好きよね」"

hide eri_m_01_1
show eri_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice eri_g0184
Elliot "「はは、楽しくていいじゃねえか。\n
あんたが、取り返しにきてくれるのを楽しみに……」"

play sound se_0125
hide eri_m_02_4
show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Elliot "「……っ！！？」"

play sound se_0318
$ flash(.2)
play sound se_0315
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「きゃ……！！？」"


play music gloomy_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "がしゃんっと窓ガラスが割れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法なら簡単に防げるが、こういった急な場面ではすぐに呪文も出てこない。\n
ガラスが降りかかってくる。"

hide eri_m_01_5
show eri_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0185
Elliot "「……ち！！」"

play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐいっとエリオットの腕の中へと引き寄せられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（誰よ、ガラスを割るなんて……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何もできなかった代わり、せめてこんなことをした犯人だけは見届けてやろうと思ったが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "暗い中庭、走り去る男子生徒の後ろ姿がちらりと見えただけだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "首を伸ばそうとするものの、エリオットの胸のうちにしっかりと抱きこまれてしまう。"

hide eri_m_02_5
show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0186
Elliot "「大丈夫か！？\n
怪我、してねえか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「だ、大丈夫よ。\n
エリオットのほうこそ……！」"

hide eri_m_01_5
show eri_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice eri_g0187
Elliot "「俺は平気だ。\n
制服の上着を着た後だったからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「よかった……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "上着の厚手の生地で受け止めたこともあり、ガラスはエリオットの体には届かなかったらしい。"

hide eri_m_02_13
show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0188
Elliot "「……！！\n
あんた、血が……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見れば、エリオットが庇ってくれた中でも間に合わなかったのか、右の二の腕に一筋の朱色が走っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "割れたガラスの破片が掠めて、切れてしまったのだろう。"

hide eri_m_01_5
show eri_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0189
Elliot "「すまねえ……！\n
俺がちゃんと庇ってやれなかったから……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「え、えええ！？\n
そんなこと……、エリオットのせいじゃないわよ」"

hide eri_m_02_3
show eri_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "切れたといっても、皮膚一枚切ったという程度で、深く切れているわけではない。\n
それでもガラスの破片ですっぱりと切れているせいなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "血玉が盛り上がり、今にも滴りそうに見えるせいで派手な怪我のように見える。"

play sound se_0252
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットはそれに泣きそうなほどに顔を歪め、それでも素早く手にしていた私のリボンで腕の上をしっかりと圧迫して結び、簡単な止血をしてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「もう……、なんなのかしら。\n
ストームって、こんな暴力的なイベントじゃないんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手当てに照れて、口早に喋る。\n
妙な沈黙が気恥ずかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あんな……、窓を割るなんて、下手したら大怪我しちゃうわ」"

hide eri_m_01_6
show eri_m_03b_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……エリオット？」"

hide eri_m_03b_12
show eri_m_03b_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
Elliot "「…………」"

hide eri_m_03b_13
show eri_m_03b_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice eri_g0190
Elliot "「……悪い。\n
今晩のことは、ひとまず忘れてくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え……」"

menu:
    "エリオットがそう言うなら……。":
        jump gakuen_elliot4_6a
    "納得できないわ。":
        jump gakuen_elliot4_6b
label gakuen_elliot4_6a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「エリオットがそう言うなら……。\n
従うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私には何がどうして、こんなことが起こっているのかが分からない。\n
現状を把握できないのなら、それが出来ている人間の指示に従うしかないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……でも、私らしくないな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当は、従うよりは対等でいたい。"

jump gakuen_elliot4_7
label gakuen_elliot4_6b:
$ lovechara_elliot_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「納得できないわ。\n
忘れるなんて嫌よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "初体験の連続。\n
そして、エリオットと気持ちの通じ合った大事なイベントだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後にケチがついたからといって、記憶を消せるはずもない。"

hide eri_m_03b_11
show eri_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは私に困ったような視線を流し、言葉に迷うような様子を見せた。"

jump gakuen_elliot4_7
label gakuen_elliot4_7:
hide eri_m_01_6
show eri_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0191
Elliot "「すぐに、使用人達が来る。\n
そしたらちゃんと医務室にいって、手当てしてもらってくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「な……。\n
エリオット！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の声に答えないエリオットに、苛立ちとともに焦燥が募る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（忘れろってどういうことよ？\n
何を忘れろっていうの？）"

play sound se_0216
hide eri_m_01_12

pause .5
play sound se_0348
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の言葉を黙殺して、言いたいことだけ言ったエリオットは身を翻す。\n
そのまま、なんと窓際から飛び降りてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慌てて見下ろすが、補助魔法でも使ったのだろう、危なげなく着地し、そのまま走っていく。すぐに、夜闇の中に見えなくなっていってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……なんなのよ、もう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントごとに相応しく、終わった後は夢のよう。\n
現実のことではなかったかのようだ。"

play sound se_0321
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下を走る足音が近づいてくる。\n
騒動に気づいた使用人達が駆けつけてくれたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大騒ぎの中でも、窓が割られるというのは特殊らしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見下ろした中庭、こちらを見上げ、指差している生徒の姿もちらほらあるようだから、もしかしたら誰かが使用人に連絡してくれたのかもしれない。"

$ flash_color("red", .1)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「つ……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今更になって、腕に出来たきり傷がひりひりと痛んだ。"

with dis
$ hi_mes()

scene bg24_rj_nig with Dissolve(.8)

scene bg_par15_rg_hat_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_elliot5
