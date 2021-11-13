label gakuen_elliot2:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_hat_day
with dis

play music flower_day_p_wam

scene bg_par03_nb_nn_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中庭に出て、カフェテリアから見えていた場所へと行ってみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓からは建物の陰になって見えなくなっていた部分、日当たりのいい一帯が、本当に開墾されていた。黒々と耕された土は、ほくほくと柔らかそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただし、そこに植物の姿はない。\n
何も、生えていなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「にんじん畑……、じゃなかったっけ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ季節ではないのだろうか。\n
考えてみれば、魔法の発達のおかげで年がら年中見かけるせいで、にんじんの旬の季節というのがよく分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつ種を蒔き、いつ頃収獲するのが自然のサイクルにあっているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "綺麗に耕された畑の傍らに屈み、より近くで土の表面を見てみる。\n
しかし、それでも……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「ない、わよね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、芽らしきものは見当たらない。\n
あれだけ頻繁にエリオットが通っているのだから、すでに栽培を始めているはず……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（ちょっと、にんじん栽培について調べてみようかな）"

menu:
    "調べてみる。":
        jump gakuen_elliot2_2a
    "やめておく。":
        jump gakuen_elliot2_2b
label gakuen_elliot2_2a:
$ lovechara_elliot_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いわゆる、知的好奇心というやつだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好奇心というものが危険だと、あれほど身に染みたはずなのに、私はちっとも学習していなかった。"

with dis
$ hi_mes()

scene bg_par03_nb_nn_day with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg15_lb_o_day
with stripe_l_medium

scene bg15_lb_i_day
with stripe_l_long
play sound se_0566

play music library_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早速、図書館で、にんじんの栽培について書いてある本を借りてきたものの……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "{size=+20}（専門用語が分からない）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "『潅水』だとか『被覆』だとか。\n
『被覆』に関しては字面からなんとなく雰囲気を察することが出来るが、『潅水』に関してはお手上げだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "水をどうにかすることなのだろうが、何をどうしたらいいのか。\n
にんじんの発芽にはそれが大事らしいのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「意外と手強いのね、にんじん栽培」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "店などに行くと、一山幾らでごろごろ売られている。\n
しかし、素人が簡単に育てられるわけではなさそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば、シンフォニア魔法学校には、園芸部なる部活動が存在している。\n
そこの部員に聞けば、もっと分かりやすく解説してくれるのではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（こんなふうに知りたがるなんて、こだわりすぎかもしれないけど……。\n
せっかく調べようと思ったんだし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（気になるし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うじうじと自分に言い訳をしつつも、園芸部の部室を訪ねてみることにした。"

with dis
$ hi_mes()


scene bg15_lb_i_day with Dissolve(.8)

scene bg15_lb_o_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg27_rk_day
with stripe_l_medium

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後、園芸部の部室を訪ねてみた。"

play sound se_0302
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0019
Engei_head "「は～い。\n
開いてるよ～」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中から、間延びした声が返ってくる。\n
これは勝手に開けて入ってこい、ということでいいのだろうか。"

play sound se_0397
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……おじゃましま～す」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアを開けて園芸部の部室へと足を踏み入れる。"


scene bg_par08_eb with stripe_l_medlong

play music laboratory_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「！\n
わあ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすが園芸部、といったところだ。\n
部屋の中にはいたるところに、観葉植物の鉢植えが置かれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その中央の大きめのデスクの傍らに、制服の上から白衣を纏った生徒達が何人か立っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……園芸部員？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いでたちは園芸部員というよりも、実験中の科学者のよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのうちの一人が、何気なくといった様子で私を振り返り、そして驚いたように目を丸くした。"


show boy_e1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Engei_head "「！！！」"

hide boy_e1_4
show boy_e1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0020
Engei_head "「新入部員だ……！！！」"


show girl_e1_4 at center
with dis
hide boy_e1_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0024
Engei_Buin "「新入部員……！！？」"


show boy_d1_2 at center
with dis
hide girl_e1_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0015
Engei_Buin "「新入部員だって……！！？」"


show girl_f1_2 at center
with dis
hide boy_d1_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0021
Engei_Buin "「ついに、この園芸部にも……！！？」"

hide girl_f1_2

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "机を囲んでいた園芸部員達が、一斉に私を振り返る。\n
四人もの見知らぬ人間に凝視され、後退ってしまう。"


show boy_e1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0021
Engei_head "「入部希望？」"

play sound se_0198
##special anime"kirakira_center"loop="false"time="1000"]
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（う、うわあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きらきらと、期待に満ちた視線を向けられて申し訳ない気持ちになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「え、ええと、その……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「ごめんなさい！\n
私、入部するつもりはないの……！」"

hide boy_e1_3
show boy_e1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice hos_g0022
Engei_head "「……ち、違ったのか～……」"

hide boy_e1_1
show boy_e1_1 at left
with dis

show girl_e1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice mat_g0025
Engei_Buin "「……違うのね」"

hide boy_e1_1
show boy_e1_1 at left_center
hide girl_e1_5
show girl_e1_5 at center
with dis

show boy_d1_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice oni_g0016
Engei_Buin "「早とちり……」"

hide boy_e1_1

hide girl_e1_5
show girl_e1_5 at left_center
hide boy_d1_1
show boy_d1_1 at center
with dis

show girl_f1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice tad_g0022
Engei_Buin "「今なら、園芸部特製マンドラゴラの鉢植え、漏れなくプレゼントするのに……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これ以上期待させてしまう前に、と慌てて誤解を解くべく口を開いた私に、園芸部員達はあからさまにがっかりしたように肩を落とした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（うう、申し訳ない……っ）"


show boy_e1_5 at center
with dis
hide girl_e1_5

hide boy_d1_1

hide girl_f1_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice hos_g0023
Engei_head "「そ、そっか……、はあ。\n
新入部員じゃないのは残念だけど……」"

hide boy_e1_5
show boy_e1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice hos_g0024
Engei_head "「何か、俺達に用があって来たんだよね？\n
どうしたの？何の用？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "白衣を着た男子生徒の一人が、改めて私へと向き直る。\n
他の三人は、また何やら作業に戻ったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（何をしているんだろう……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（園芸っていうより、実験みたいだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "疑問が顔に出ていたらしい。\n
彼は、口元に笑みを浮かべる。"

hide boy_e1_9
show boy_e1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0025
Engei_head "「ああ、あれはね、魔法植物の若木に、別の魔法を付加して成長の度合いに変化が見られるかの実験をしているんだよ」"

hide boy_e1_3
show boy_e1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0026
Engei_head "「運がいいと、新種が育つようになるんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「そうなの……！？\n
すごいわ、こんなに本格的なことをしているとは思わなかった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もっと、庭いじり的な、校内の花壇を管理するような部活だとばかり思っていた。"

hide boy_e1_3
show boy_e1_3 at left
with dis

show girl_f1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0023
Engei_Buin "「うふふ、いろんな魔法植物を栽培しているのよ。\n
よかったら、園芸部特製マンドラゴラの鉢植えもらってくれない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「えええ？\n
でも、私、新入部員じゃないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（それにマンドラゴラって……、まずいんじゃないの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "希少価値の高い植物だ。\n
マンドレイクともいう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薬に重宝されることも多く、魔法使いには馴染みがあるが、希少価値だけでなく危険度も高い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "引き抜くときに悲鳴を上げ、それを聞いた人間は死んでしまうという曰くがあるのだ。"

hide girl_f1_3
show girl_f1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0024
Engei_Buin "「いいのよ、遠慮しないで。\n
……新入部員がくるアテもないし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女は、にこやかに鉢植えを差し出してくれた。\n
そんなに大きくもない、部屋に置くにはちょうどいいぐらいの花鉢だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ええ？本当に？\n
貰ってしまっていいの？」"

hide girl_f1_3
show girl_f1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tad_g0025
Engei_Buin "「ええ、いいの。\n
だって、あなた私達の部室に訪ねてくる程度には、植物に興味があるんでしょう？」"

hide girl_f1_3
show girl_f1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tad_g0026
Engei_Buin "「部活への勧誘も大事だけど……。\n
やっぱり、同じ植物好きがいるだけでも嬉しいものなの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女の言葉に背中を押されて、その鉢植えを受け取る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「ありがとう。\n
大事に育てるわ」"

hide girl_f1_2
show girl_f1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice tad_g0027
Engei_Buin "「どういたしまして。\n
育て方で分からないことが出てきたら、いつでも訪ねてきてね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「ええ、そうさせてもらう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "園芸部特製、ということは、普通のマンドラゴラとは違っているのだろう。\n
どこがどう違うのか、育ててみるのも面白そうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（……危険そうでもあるけど）"

hide girl_f1_3
show girl_f1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice tad_g0028
Engei_Buin "「で、何の用だったの？\n
まだ肝心の用件を聞いていないわ」"

hide boy_e1_3
show boy_e1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice hos_g0027
Engei_head "「はは。\n
ごめんね、普段あんまり人がこない地味な部活なものだからさ」"

hide girl_f1_8
show girl_f1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice tad_g0029
Engei_Buin "「人がくるとはしゃいじゃうのよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは、改めて用件を促してくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自ら言うように、園芸部というのはあまり華やかではない部活だ。\n
だが、居心地よさそうな雰囲気を感じた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（いい人達ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らなら、きっと私の疑問にも答えてくれるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「えっとね、ちょっと植物の栽培についてなんだけど……。\n
にんじんの育て方を、教えてほしいの」"

hide girl_f1_2

hide boy_e1_2
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par08_eb with Dissolve(.8)

scene bg10_sb_day
with stripe_l_medium
jump gakuen_elliot2_3
label gakuen_elliot2_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「いやいやいやいや、やめておこう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脳裏を過ぎっていった考えに、頭をぶんぶんと左右に振る。\n
好奇心を抱くことの危険性を学んだそばから、私は一体何を考えているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（触らぬ神に祟りなし、よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう自身に言い聞かせて、私はその場を後にした。"

with dis
$ hi_mes()

scene bg_par03_nb_nn_day with Dissolve(.8)

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg06_sk_h_day
with stripe_l_long

play music high_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットのにんじん畑のことを気にしつつも、特に自分から関わることなくおとなしく日常を過ごす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好奇心はろくなことを引き起こさないと学んだばかりだ。"


scene bg_par03_nb_nn_day with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、それでも完全にその気持ちを絶つのは難しく、つい足が中庭へと向いてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……まだ、芽は出ていないのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日も、エリオットとはタイミングをずらして、そのにんじん畑を眺めていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相変わらずほくほくと耕された土は軟らかそうだが、にんじんと思わしき芽生えはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（何が原因なのかしら？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうに思いながら眺めていると、中庭の少し離れたところに白衣の集団がいることに気づいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "集団といっても、人数は四、五人程度。\n
よくよく見ていると、彼らは中庭の植物の観察をしているようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手元に広げたノートへと、観察の結果を書き込んでいるのが分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「もしかして……」"

play sound se_0624
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は彼らのもとへと、歩み寄った。"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ねえ。\n
あなた達、園芸部じゃない？」"

##[rchara1 PAY ATTENTION="false"]
show boy_e1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice hos_g0028
Engei_head "「んん？\n
そうだけれど、どうかしたのかな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "代表者らしき男子生徒が、訝しげにしながらも私へと向き直ってくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（やっぱり）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこの学校にでもあるが、地味な部活だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……好奇心には負けない、って決めたはずだったのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、機会さえあれば、好奇心には勝てない。\n
私は、彼へと切り出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「聞きたいことがあるの」"

hide boy_e1_9
show boy_e1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice hos_g0029
Engei_head "「何？\n
植物についてなら、なんでも聞いてくれていいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心強い返事だ。\n
ここの園芸部は、親切らしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「えっとね、植物の栽培についてなんだけど……。\n
にんじんの育て方を教えてほしいの」"

hide boy_e1_9
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par03_nb_nn_day with Dissolve(.8)

scene bg_par15_rg_hat_day
with stripe_l_medium
jump gakuen_elliot2_3
label gakuen_elliot2_3:

scene bg_map_day
with dis

scene bg_par15_rg_hat_day
with dis

scene bg_par03_nb_nn_day
with dis

play music flower_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次の日の放課後。\n
私は、にんじん畑でエリオットを待ちうけていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この時間帯にエリオットがやってくるというのは、これまでの観察から分かっていることだ。"

play sound se_0625
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ほら、来た）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゆっくりと足音が近づいてくる。"

##[rchara1 PAY ATTENTION="false"]
show eri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは畑の前に立つ私の姿に気づくと、一度驚いたように足を止め、それからずんずんと大股でこちらまでやってきた。"

hide eri_m_02_12
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0032
Elliot "「あんた、こんなところでどうしたんだ？\n
俺に、何か急ぎの用か？」"

hide eri_m_01_8
show eri_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0033
Elliot "「寮内で問題でも……、あ、また、あの双子共が面倒をやらかしたのか？\n
それとも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（やっぱり、面倒見いいなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「違う違う。\n
私、あなたに用があってきたの」"

hide eri_m_01_12
show eri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice eri_g0034
Elliot "「だから、俺に用事だろ？\n
なんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、完全に副寮長として話を聞く態勢に入ってしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がエリオット個人に話があるなんて、ちっとも考えていないというようなふうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "身構えられている、というのとはまた少し違うかもしれないが、それに近いものを感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……にんじんのこと、なんだけど」"

hide eri_m_02_12
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice eri_g0035
Elliot "「……へ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごにょごにょ、と切り出すとエリオットの目がきょとんと丸くなった。"

hide eri_m_01_10
show eri_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0036
Elliot "「にんじん？\n
にんじんって……、ここの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ。\n
……にんじんの育て方、調べてきたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（な、なんだか恥ずかしくなってきた……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「なかなか芽が出ないみたいだったから、気になって」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言っている途中から、恥ずかしさに声がトーンダウンしてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頼まれたわけでもないのに、わざわざ園芸部に聞いてきたなんて、余計なお世話もいいところだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（かなり、お節介よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットならきっと喜んでくれる。\n
根拠もなく、そんなふうに思っていた自分が恥ずかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本人を目の前にして気づいてしまったのだが、それはすなわち、私はエリオットを喜ばせたかったというのと同義だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気になるというのは、エリオット自身を気にしていたからで……。\n
……だいぶ照れくさい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（たいして知りもしない人なのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしてだか、気になるウサギさん。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……迷惑、だったかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が、一方的に気になっているだけ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが黙り込んでしまっているので、その反応が気になる。いつのまにか俯いていた視線をそろっと持ち上げ、エリオットの顔色を伺うが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "息を呑んでしまった。\n
エリオットは、涙ぐんでいるようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎょっとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（ええ？\n
なんで？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（そんなに嫌だったの？\n
いや、そんな酷いようなことはしていないし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……エリオット？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（こういうとき、どうしたらいいのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "泣いている女の子をどうしていいか分からない、という男性側の意見を聞くことはある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、泣いているウサギさんをどうしたらいいのかというのも、それに並ぶぐらいの難題だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "泣くほど嫌だったのか、謝るべきか。\n
だが、何を謝るというのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭の中をぐるぐると回りだす。\n
居た堪れなくなって、後ずさろうとした腕を掴まれ、そのままぐいっと引き寄せられた。"

play sound se_0052
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……っ！？」"


play music gag1_a_wam
hide eri_m_02_7
show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice eri_g0037
Elliot "「あんた……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「は、はい！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice eri_g0038
Elliot "「あんたって奴は、なんて親切なんだ！！\n
困っているときに、こうして助けてくれるなんて……」"

play sound se_0055 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「ぐ！？」"

hide eri_m_01_5
show eri_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice eri_g0039
Elliot "「そうなんだよ、困ってたんだ、俺！\n
でも、他に察してくれる奴なんかいなかったぜ！？」"

hide eri_m_02_8
show eri_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice eri_g0040
Elliot "「あんた、まるで女神様みたいだ……！！！」"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ぐぐ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（たしかに、天に召されそうな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……っく、くるし……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "感極まったエリオットに、力任せにぎゅうぎゅうと抱きしめられ、息が詰まる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男性に抱きしめられるなんていうシチュエーションでありながら、感じるのは胸のときめきではなく、別の種類の危機感だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すなわち、{size=+20}骨が折れるんじゃないか{/size}、という。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（く、熊に襲われたらこんな感じかしら……。\n
いや、エリオットはウサギなんだけれども）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "熊サイズの大きなウサギさんは、私の声にはっとしたように手を放し、解放してくれた。"

play sound se_0313
hide eri_m_01_4
show eri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0041
Elliot "「す、すまねえ……！！\n
俺、嬉しくって、つい……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「あなたねえ……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "力加減を考えなさいよ、だとか怒鳴ってやろうと構えるが、申し訳なさそうにしょんぼりとたれたウサギ耳の前に文句はどこかへ行ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（うう……っ、卑怯だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私より頭一つ分以上長身で、体格もいい男の人を相手に当てはまる言葉ではないと分かっていても、可愛い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その上、エリオットはただの気のいい兄貴分ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前覗き見てしまったように、シンフォニアにおける不良グループ（！）のＮｏ．２なんていう物騒な顔も持っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（不良グループ……なんていう言い方も可愛らしすぎて似合わない気がするけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らときたら、マフィアさながらの威圧感がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、申し訳なさそうに長いウサギ耳を萎れさせている様は……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（反則なぐらいに、可愛い）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何をされても許してしまいそうだ。\n
……骨を折られそうでも。"


play music high_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「まあ、いいわ。\n
それで、にんじんのことなんだけど……」"

hide eri_m_01_9
show eri_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice eri_g0042
Elliot "「おう！\n
芽が出ない原因が分かったのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「ええ、分かったわ。\n
にんじんって、発芽までが難しい植物なのね」"

hide eri_m_02_1
show eri_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice eri_g0043
Elliot "「そうなのか？\n
なかなか芽が出ねえな、とは思ってたんだが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……そうなのよ。\n
もしかしてあなた、にんじんのことを何も知らずに育てようとしていたの？」"

hide eri_m_02_7
show eri_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice eri_g0044
Elliot "「にんじん料理のことならよく知っているぜ！」"

hide eri_m_01_4
show eri_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice eri_g0044_5
Elliot "「素材の味を活かしたにんじんスティックにしてもうまいし、にんじん茶にしても、お菓子にしてもうまいんだ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……それ、育て方に関する知識じゃないわよね？」"

hide eri_m_02_4
show eri_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice eri_g0045
Elliot "「にんじんについてよく知っていることには違いねえだろ？\n
俺の、にんじん料理に対する愛は誰にも負けないぜ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「…………。\n
……そりゃ、芽が出ないわけだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とてもとても、納得してしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "園芸部の人達から聞いた話によると、にんじんというのは繊細な植物のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日常無造作に料理に入っていることもあり、あまり意識しないが、実は結構気難しい性質を持っているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「にんじんの種は、乾燥に弱いのよ。\n
それでいて、過湿にも弱いの」"

hide eri_m_01_2
show eri_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice eri_g0046
Elliot "「乾いても駄目、水が多すぎても駄目ってことか？\n
……難しいな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「ええ、難しいの。\n
だから、まずは土作りからしないといけないんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちら、っとすでに畑としては完成しているにんじん畑を見やる。\n
ここには、すでにエリオットが種を蒔いてある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、土作りからやり直すとなれば、もう一度耕すところから始めなければいけないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "調べてきたのは私だが、実際にそうした作業をすることになるのはエリオットだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（園芸部では、植物を扱うには愛情と根気強さが必要だって言っていたけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットには、もう一度始めからやり直すつもりがあるだろうか。"

hide eri_m_02_7
show eri_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0047
Elliot "「土作りからだな！\n
おっし！じゃあ、始めるか！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逡巡する間すら挟まない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……両方とも、充分に備わってそうね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私だったら、もう一度土作りからやり直せなんて言われたら、にんじんの栽培そのものを諦めてしまいそうだ。諦めはしなくとも、少しはそれを考えるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、エリオットは、迷うことすらしなかった。"

menu:
    "（素直なのね）":
        jump gakuen_elliot2_4a
    "（馬鹿正直というか……）":
        jump gakuen_elliot2_4b
label gakuen_elliot2_4a:
$ lovechara_elliot_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（素直なんだわ）"

jump gakuen_elliot2_5
label gakuen_elliot2_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（馬鹿正直というか……）"

jump gakuen_elliot2_5
label gakuen_elliot2_5:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呆れるような気持ちと、どこかじんわりとした嬉しさ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の調べた知識が、エリオットにすんなり受け入れてもらえたのが嬉しい。"

hide eri_m_01_1
show eri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0048
Elliot "「それで、まずは何からしたらいいんだ？\n
あんたの指示に従うぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「それじゃあ、まずは、肥料を貰いにいきましょう。\n
園芸部の人達に相談したら、わけてくれると言ってくれたの」"

hide eri_m_02_12
show eri_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice eri_g0049
Elliot "「分かった！\n
園芸部の部室に取りにいけばいいのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「いえ、許可は得ているわ。\n
肥料を置いてある場所を聞いてあるの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_2")
T "「必要だったら、そこから必要なだけ貰って行っていいんですって」"

hide eri_m_01_1
show eri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_2")
voice eri_g0050
Elliot "「へえ、園芸部の奴らも太っ腹だな。\n
それじゃあ、[firstname]、その肥料が置いてあるって場所まで案内してくれるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（…………）"

hide eri_m_02_12
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice eri_g0051
Elliot "「[firstname]？\n
どうかしたか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……ううん、なんでもないわ。\n
いきましょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……驚いた）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がエリオットに名乗ったのは、一番最初、半透明矢印に案内されて帽子屋寮へとやってきたときだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それ以来、寮や学校で顔を合わせれば会釈をしたり、挨拶をしたりといった会話はあったが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼ばれたこともなかったので、すっかり忘れられているものだと思っていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つい先刻だって、「あんた」と連呼していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、急に名前を呼ばれて、焦った。\n
心臓がどくどくと跳ねる。"

hide eri_m_01_8
show eri_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0052
Elliot "「今日中に種まきまでいけるといいな。\n
ほら、急ごうぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「え、ええ。\n
そうね、急ぎましょう」"

hide eri_m_02_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットに促されて、胸のあたりをそっと押さえたまま、倉庫へと向かって歩き出した。"

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music elliot_t_ali
play sound se_0072
pause .15
play sound se_0462
pause .3
play sound se_0072
pause .15
play sound se_0462
pause .3
show m_eri2_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "制服のジャケットを脱ぎ、ズボンの裾をたくしあげた格好でエリオットが鍬をふるって畑を耕していく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなに広い面積ではないとはいえ、根野菜のにんじんを育てるためには深く耕す必要があるため、その分体力は使う。"

play sound se_0072
pause .15
play sound se_0462
pause .3
play sound se_0072
pause .15
play sound se_0462
pause .3
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ざくざく、ざっざ。"

play sound se_0072
pause .15
play sound se_0462
pause .3
play sound se_0072
pause .15
play sound se_0462
pause .3
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ざくざく、ざっざ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次第互いのテンポが分かってくると、まるで餅つきのようなリズムが生まれる。\n
それが楽しくて、しばらく無心の作業が続く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（楽しい……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（けど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……私、何学校に入ったんだっけ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "農業の学校に入ったような気分になる（実際に大陸内では農業を学ぶ学校も多い）。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "裏庭で、外部から遮断されたように感じるので、尚のこと。\n
私とエリオットだけが、まったく違う場所にいるように感じてしまう。"

hide m_eri2_1
show m_eri2_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0053
Elliot "「……っふう！\n
こんなもんでいいか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "畑をムラなく耕したエリオットが鍬に重心を預けるようにして、一息つく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……え？\n
え、ええ、いいと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中腰での作業が続いていたのだ。\n
いくらエリオットが体力に自信があるとしても、さすがに疲れただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「お疲れ様。\n
エリオット」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_2")
voice eri_g0054
Elliot "「ああ、あんたもな。\n
ふ～、いい汗かいたぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "爽やかに汗をぬぐう、ウサギさん。\n
まったくもって、ここは何学校なのかと疑問がわく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……でも、同意する。\n
いい汗かいたわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達の前には、少し灰色がかった土がふかふかと盛り上がった畑が広がっている。\n
その灰色こそが、私達が土に混ぜ込んだ肥料だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "木灰をベースに、園芸部が開発した肥料で、土の性質をアルカリ性よりにする役目と、水はけをよくする役目の両方を果たしてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にんじんは酸性の強い土地では、うまく育たないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0055
Elliot "「農作業っていうのは、気持ちいいよな～」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そうね。\n
やり遂げたっていう感じで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……いや、まだ生えてもいないんだから、何もやり遂げていないんだけどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice eri_g0056
Elliot "「だけど、やった～って感じだろ？\n
ビールでも飲みたい気分だ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice eri_g0057
Elliot "「あんたも、どうだ？\n
後で一杯……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……いやいや、それはちょっと」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice eri_g0058
Elliot "「ああ、もうちょっと進めないとな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……いやいやいや。\n
進めてからでもちょっと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「とにかく、エリオット、種まきをよろしく。\n
私は土を被せていくわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice eri_g0059
Elliot "「分かったぜ。\n
こっち側から蒔いていくからな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「了解」"

hide m_eri2_2
show m_eri2_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、にんじんの種をぱらぱらと列を作るように蒔いていく。\n
そしてその上から、私が篩いを使ってさらさらと薄く土を被せていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "列は全部で五つ。\n
五つの畝に万遍なくにんじんの種を蒔く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（ああ、綺麗に蒔けている……。\n
うっとり……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（ああ、農業って素晴らしい……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……{size=+20}私、何学校に入ったんだっけ？{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本格的に、分からなくなってくる。"

with dis
$ hi_mes()
hide m_eri2_3


scene bg_par03_nb_nn_day with Dissolve(.8)

scene bg_par03_nb_eve with Dissolve(1.2)

play music evening_a_wam

show eri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0060
Elliot "「……っと、これで終わりか？\n
そろそろ夕食の時間も近いけどよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そうね、後はこのマジックアイテムを設置するだけ。\n
ちょっと待っていてね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "懐から合計四本になる、小さなシャワーノズルのようなスティックを取り出す。\n
これも、園芸部の人達が貸し出してくれたものだ。"

hide eri_m_02_12
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「？」"

hide eri_m_01_8
show eri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0061
Elliot "「それ、なんなんだ？\n
見たことねえけど……、それも園芸部からか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ。\n
これはね、種を乾燥から守るためのアイテムなの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「土が乾燥したら、自動的に水を散布してくれる仕掛けになっているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教えると、まるで自分の手柄のようだ。\n
他にも色々と聞いていたのだが、端的に話す。"

hide eri_m_02_12

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「こうして……」"

play sound se_0240
pause 1
play sound se_0240
pause .5
play sound se_0240
pause 1
play sound se_0240
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それぞれ畑の四隅へと差し込んで固定する。\n
後は呪文を唱え、マジックアイテムを起動するだけだ。"

play sound se_0496

show magic_b onlayer master with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

hide magic_b
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の唱えた呪文に反応して、マジックアイテムがぽうっと薄暗くなり始めた畑の四隅で微かな光を放つ。"

play sound se_0610
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "畑の上を覆うように、雨雲が発生した。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……あ。\n
ちょっと嫌な予感が……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何が起こるのか、その先のことが予想できてしまった。\n
だが、時すでに遅し。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……っ！」"

play sound se_0629

scene bg_par03_nb_ks_eve with grad_t
play sound se_0628
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さああああああっと早速土を湿らせるべく柔らかな霧雨が畑へと……。"


show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「！！！」"

hide eri_m_01_5
show eri_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0062
Elliot "「のわっっ！！？\n
ちょ、うわっ、つめて……っっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ついでに、まだ畑の中にいたエリオットにまで降り注いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、私にも。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！！！」"

hide eri_m_02_5
show eri_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
Elliot "「～～～～～～！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「～～～～～～！」"

hide eri_m_02_6
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
Elliot "「！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「…………」"

hide eri_m_01_10
show eri_m_03a_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「…………」"

hide eri_m_03a_3
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
Elliot "「…………」"

hide eri_m_01_10
show eri_m_03a_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice eri_g0063
Elliot "「……ふ。\n
はは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_5")
T "「……ぷ。\n
あはっ、ははは」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ウサギ耳をぺったりと伏せ、雨から耳を守る様。\n
笑ってしまうのは悪い気もしたが、彼も笑っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか、楽しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「ふふ。\n
びしょ濡れね」"

hide eri_m_03a_5
show eri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice eri_g0064
Elliot "「あんただって、だろ……？\n
笑うなんて、ひでえよ！」"

hide eri_m_01_9
show eri_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice eri_g0065
Elliot "「あー、畜生、濡れた！\n
……っはは」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人して、慌てて畑から脱出する。\n
エリオットは恨めしげな視線を私に向けるものの、すぐに笑い出してしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "びしょ濡れなのも、笑ってしまうのも、二人お揃いだ。"

hide eri_m_02_4
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par03_nb_eve
with dis

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music school_front_nig_p_wam
##[rchara1 PAY ATTENTION="false"]
show eri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0066
Elliot "「……ふう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "暮れかかった夕焼け空の下、二人並んで出来たばかりのにんじん畑を見下ろす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらっと隣のエリオットの顔を見上げると、エリオットはとても満足そうな顔をしていた。きっと、私も似たような顔をしているのだろう。"

hide eri_m_01_9
show eri_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0067
Elliot "「俺、さ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「んん？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろそろ片付けて寮に戻らないと、と私が言おうかどうかを迷っているタイミングで、エリオットがぽつりと口を開いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おしゃべりなら、歓迎だ。\n
こうして二人で畑を眺める時間が居心地よくて、それを終わらせてしまうのが惜しかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、彼の口調は楽しい今日の思い出を語るにしては、やけに深刻なもので。"

hide eri_m_02_1
show eri_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0068
Elliot "「俺……、あんたに、怖がられていると思ってた。\n
……ほら、あんなとこ見られちまったからさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……ああ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（やっぱり気付かれていたんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、気付かれずにすんだんじゃないか、とも思っていたのだが。\n
やはりそういうわけにもいかなかったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子生徒を、壁際に手慣れた身のこなしで追い詰め、凄んでいた彼の姿を思い出す。副寮長にしては過剰なほどの迫力があった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのときは、怖いとも思った。\n
間違いなく、あのときは。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「そうね。\n
確かに、怖いと思ったわ」"

hide eri_m_01_6
show eri_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice eri_g0069
Elliot "「しばらく、俺を見るとあんたびびってただろ？\n
避けはしなかったけど……、困っているみたいで」"

hide eri_m_02_11
show eri_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice eri_g0070
Elliot "「だから……、近づかないほうがいいかなって思ってたんだぜ、俺」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこまで、気付かれていたのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（まるで隠せていなかったってわけ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……気を遣わせちゃって悪かったわね」"

hide eri_m_01_11
show eri_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice eri_g0071
Elliot "「や、あんたの反応は正しい。\n
あんたみたいなお嬢さんは、俺みたいなのには関わらないほうがいいんだ」"

menu:
    "そんなことはない。":
        jump gakuen_elliot2_6a
    "そうかもしれないわね……。":
        jump gakuen_elliot2_6b
label gakuen_elliot2_6a:
$ lovechara_elliot_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そんなことないわ。\n
あなたと関わるのは私が自分でしていることだし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「大体、お嬢さん、なんて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_1")
T "（……お嬢さん）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ふふ」"

hide eri_m_02_7
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice eri_g0072
Elliot "「……？？？\n
何笑ってんだ、あんた」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「いえ。\n
私、あなたが思うほどいい子じゃないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「お嬢さん」なんて言い方。\n
そんなの、私には似合わない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、彼は本気で言っているようだ。\n
だから、笑ってしまう。"

hide eri_m_01_8
show eri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0073
Elliot "「んなことねえだろ……。\n
俺らに比べりゃ、天と地ほどの違いが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「だって、考えてもみなさいよ。\n
いい子なお嬢さんが、わざわざ不良の巣窟と名高い帽子屋寮に入寮すると思う？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「選んだ時点で、私だって一員でしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帽子屋寮には、私が望んでやってきたのだ。\n
同じように、私は私が望んでエリオットに近付いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "偶然や、無理やりな展開ではない。\n
私は、望んで今ここにいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんて、分かりやすく、迷いのない境遇。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「これからも手伝っていいかしら。\n
もちろん、エリオットの迷惑になるようだったら控えるけど……」"

jump gakuen_elliot2_7
label gakuen_elliot2_6b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「そうかもしれないわね……。\n
あのときのエリオットは、本当に怖かったもの」"

hide eri_m_02_12
show eri_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice eri_g0074
Elliot "「あんたを怖がらせたかったわけじゃないんだぜ？\n
でも……、悪かったな、あんなところ見せて」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、しゅんとその長い耳を垂らして私へと謝る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（私が勝手に立ち聞きして、勝手に見ただけなのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやって私に対して情けないともいえる態度をとる彼の姿が、あの日の記憶とは重ならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれは勘違いだったんじゃないか、とまで思ってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "『怖い人』、という目盛りに振れていた彼に対するイメージの針が……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "『ちょっと気が短くて、ちょっと乱暴ものの、でも気のいい皆のお兄さん』という元々の私のイメージへと戻っていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "『ちょっと気が短くて、ちょっと乱暴ものの、でも気のいい皆のお兄さん』。\n
それだって、充分、警戒するに足るもののような気もするが。"

hide eri_m_02_11
show eri_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0075
Elliot "「それなのに、こうして手伝ってくれたあんたって、本当にいい奴だよな！\n
マジで助かったぜ！ありがとうな！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怖い人、であるはずだ。\n
それなのに、私に対しては不器用ながらもこんなにも気を遣い、優しくしてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……ふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先刻までの、笑える感覚。\n
馬鹿にするわけではなく、嬉しくなるような、くすぐったい感じ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これは、好意からくるものだ。\n
私は、『ちょっと気が短くて、ちょっと乱暴ものの、でも気のいい皆のお兄さん』である彼と親しくなりたいと願っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ふふ。\n
これからも手伝ってあげましょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽろりと、唇からそんな提案が零れていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「もちろん、エリオットの迷惑になるようだったら、やめておくけど……」"

jump gakuen_elliot2_7
label gakuen_elliot2_7:
hide eri_m_01_1
show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice eri_g0076
Elliot "「迷惑なわけねえよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後まで言うより早く、力強く否定される。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その後、エリオットはなぜか頬を赤らめた。\n
視線が逸らされる。"

hide eri_m_01_5
show eri_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0077
Elliot "「俺……っ、あんたが手伝ってくれてすげえ嬉しかった。\n
あんたさえよかったら……、これからも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

hide eri_m_02_8
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
Elliot "「……[firstname]？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「…………」"

hide eri_m_01_8
show eri_m_03a_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice eri_g0078
Elliot "「あ……、嫌なら嫌で……。\n
その……、嫌だよな」"

hide eri_m_03a_3
show eri_m_03b_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice eri_g0079
Elliot "「あんたってやっぱりお嬢さんだし、社交辞令とか言えるのかもしれないけど……。\n
俺みたいなのには、よしたほうがいいぜ？」"

hide eri_m_03b_10
show eri_m_03a_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice eri_g0080
Elliot "「……冗談とか、通じねえから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……エリオット。\n
ちょっと屈んでくれるかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度は、私が彼の言葉を遮る番だった。"

hide eri_m_03a_4
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は私の真意を掴みかねながらも、それでもおとなしく屈んでくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その、屈んだ彼の。\n
金色の頭からのびる柔らかそうなウサギ耳を……、私はぎゅむっと引っ掴んだ。"

play sound se_0492
hide eri_m_01_8
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0081
Elliot "「い……！！？」"

hide eri_m_01_10
show eri_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0082
Elliot "「痛い！痛い痛い痛い！！\n
いててててててっっ！！！」"

play sound se_0055
hide eri_m_02_5
show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「～～～～～～……！」"

hide eri_m_01_5
show eri_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「～～～～～～……！！！」"

hide eri_m_02_3
show eri_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0083
Elliot "「い、いきなり何するんだよ……っ！？\n
い、いた、いたたたたたっ、痛い！痛いんだって……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_2")
T "「あんたが可愛すぎるからいけないのよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "両手で握り締めたウサギ耳は、想像以上にやわらかくて、手触りがいい。\n
ずっとこうして触っていたくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（いやもう、ずっと前から触っていたような気がするわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふかふか、手に馴染む感触。"

hide eri_m_02_5
show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0084
Elliot "「はあ！？か……っ、可愛いってなんだ可愛いって……！！\n
俺は可愛くなんか……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「可愛いんだからしょうがないでしょう！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "長身で、立派な体格。\n
肩書きも持っている怖そうなお兄さんなのに、可愛い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は思う存分、もぎもぎ、とエリオットの耳の手触りを堪能する。"

play sound se_0055
hide eri_m_01_5
show eri_m_03a_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「～～～～～～……！」"

hide eri_m_03a_2
show eri_m_03a_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「～～～～～～……！！！」"


hide eri_m_03a_3
show eri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0085
Elliot "「あんたひでえよ……！！\n
俺の耳が伸びたらどうしてくれるんだよ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "解放する頃には、彼は涙目。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "{size=+20}「これ以上は、伸びないと思うわよ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恨めしげなエリオットの声に、私はきっぱりと言い切る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（でも、伸びたら伸びたで、きっと可愛らしいわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、私に揉みたくられた耳の毛並みを整えるように、撫で撫でとしている。\n
そんな姿もやっぱり……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（……可愛い）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本気で抵抗すれば、私なんて簡単に撥ね退けられるだろうに、そうはしない。\n
そういったところが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……ふふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ほら、エリオット。\n
帰りましょう？」"

hide eri_m_01_9
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「帰らないの？」"

hide eri_m_01_10
show eri_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice eri_g0086
Elliot "「……帰る」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いきなり耳を引っ張られて、痛い目を見せられたのだから怒ってもいいところなのに、拗ねては見せても怒らない。"

hide eri_m_01_11

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（あのときは怖かったけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（今は……、ちっとも怖くない）"

with dis
$ hi_mes()

scene bg_par03_nb_eve with Dissolve(.8)

scene bg_par15_rg_hat_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_elliot3
