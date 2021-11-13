label gakuen_boris5:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_amu_day
with dis

play music dining_day_p_wam

scene bg_par02_ct_amu_day with Dissolve(1.2)
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの翌日の朝は、イベントの熱気が未だ残っているのか、いつもよりもざわざわと騒がしいようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな中、いつものように空いている席を探す。"


show amuse_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0035
Seito "「あら、[firstname]。\n
空いている席を探しているなら、ここ、空いているわよ」"

hide amuse_a2_3
show amuse_a2_3 at left
with dis

show amuse_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0119
Seito "「こちらにいらっしゃいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「あ、ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔見知りの女子生徒二人に招かれて、そちらへと歩み寄った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業などでは一緒になることがなくとも、同じ寮で生活していれば自然と親しくなる友人というのがいる。\n
彼女達も、そんな友人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……朝から食べるわねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人分とはいえ、テーブルの上には料理で一杯だ。"

hide amuse_a2_3
show amuse_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0036
Seito "「そのかわり、夜を控えめにしているのよ」"

hide amuse_b1_3
show amuse_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0120
Seito "「そうそう。\n
朝こそ、食べなくちゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「私は、朝から重いのは無理」"

play sound se_0034

show white onlayer master with Dissolve(1.5)

$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はオレンジジュースにトースト、そしてサラダと、朝食の定番メニューをテーブルの上へと呼び出す。"

hide amuse_a2_3
show amuse_a2_9 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0037
Seito "「そういえば、[firstname]、あなた今日ちょっと雰囲気が違わない……？\n
なんだか……、いつもより……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「？」"

hide amuse_a2_9
show amuse_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice tad_g0038
Seito "「なんていうか……、血色がいいわよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「え？\n
そう？」"

hide amuse_b1_3
show amuse_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice sam_g0121
Seito "「うん、そういえば。\n
お化粧しているわけじゃあ……、ないわよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「特に、何かした覚えはないんだけど……」"

hide amuse_b1_9
show amuse_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice sam_g0122
Seito "「そうよねえ……？？？\n
何が違うのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（特別なことはしていないけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達の言うとおり、化粧のようなことはしていない。特に何か特別なことをしたわけではないのだが……、強いていうならば早起き、だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもより早い時間に起きて、シャワーを浴び、いつもよりも丁寧に身支度を整えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちなみに、今しているリボンは予備としてしまってあったものを、引っ張り出したものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じなのに、すべてが微妙に違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……我ながら、恥ずかしい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨日の今日。\n
カフェテリアでボリスと会ってしまったら、なんて考えてしまったら、自然と念入りになってしまったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "現金というべきか、乙女心というべきか。\n
意識しているのは間違いない。"

hide amuse_a2_9
show amuse_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0039
Seito "「あ、分かった。\n
ねえねえ、昨夜のストームで何かいいことがあったんでしょう？」"

hide amuse_b1_9
show amuse_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0123
Seito "「その充足感が顔に出ているんだわ。\n
そうなんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……う」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あながち間違ってもいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さく唸るが、否定は出来ない。\n
彼女達はそれを肯定と看做したようだった。"

hide amuse_a2_3
show amuse_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0040
Seito "「へえ～？\n
初めてのストーム、楽しめたみたいでよかったわね」"

hide amuse_b1_3
show amuse_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0124
Seito "「ふふ、そりゃあ顔に出るくらいですもの。\n
とってもいい経験になったのよ」"

hide amuse_a2_3
show amuse_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0041
Seito "「で、あなたの部屋には誰が……、って、そっか。\n
あなた新入生だものね、同じ新入生？」"

hide amuse_b1_3
show amuse_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0125
Seito "「それなら、ちょっと分からないなあ。\n
新入生の男の子は、まだなかなか名前覚えられないのよね……」"

hide amuse_a2_2
show amuse_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0042
Seito "「うん、授業が重なったりしていると、知り合いになりやすいんだけれど。\n
参ったなあ、これじゃ、冷やかそうにも冷やかせないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……冷やかさなくていいわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業のレベル的にも新入生と同じ授業というのはあまりなさそうだし、同じ寮とはいえ男女で寮が分かれているため、新入生と出会う機会は少ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誤解してくれているなら、そのままでいい。"

hide amuse_a2_3
show amuse_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0043
Seito "「名前を聞いても分からないわね、きっと。\n
こういうのは両者ともに知り合いだったりすると、盛り上がれるんだけれど」"

hide amuse_b1_9
show amuse_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0126
Seito "「新入生の男の子達とも親睦を深めてくるべきかしら。\n
……問題は何をきっかけにするか、だけれども」"

hide amuse_a2_8
show amuse_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0044
Seito "「昨日のストームではきっかけがなかったって暴露しているようなものね」"

hide amuse_b1_9
show amuse_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0127
Seito "「だって～……、ああいうのって、知り合いのほうが来やすいでしょう。\n
クラスメイトが来ちゃったから……」"

hide amuse_a2_8
show amuse_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0045
Seito "「え？\n
誰、誰？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「…………」"

play sound se_0617
hide amuse_a2_2

hide amuse_b1_5

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……このまま、話が逸れていってくれれば）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人とも、すっかり私の相手は新入生だと決め付けてしまっている。\n
しかも、だんだん話は脱線していく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誤解だが、それを正すつもりはない。\n
昨夜、私を訪ねてきた相手は……。"


play music boris_t_ali

show bor_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0379
Boris "「おはよ、[firstname]。\n
隣、空いてる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょうど噂をしていたところに影がさした。\n
本人であるボリスがやってきたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どきりと心臓が跳ねるものの、なんでもないふうを装う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「おはよう、ボリス。\n
珍しいわね、あなたがこの時間にカフェテリアにくるなんて」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスほどではないが、ボリスも遅刻が多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ違うのは、ピアスは授業にも間に合っていないが、ボリスの場合は意図的に朝のホームルームだけをサボっている感があるというところだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業が始まる前には、自分の席にいつのまにか座っていたりする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのため、私が朝登校する前、私の朝食の時間とボリスの朝食の時間は今までずれていた。"

hide bor_m_02_4
show bor_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0380
Boris "「ちょっとでも早く、あんたに会いたかったんだよ。\n
……健気じゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「自分で言うあたり、どうかしら」"

hide bor_m_01_13
show bor_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0381
Boris "「自治会の書記さんじゃないけどさ、俺の妄想とか、夢だったら嫌だろ？\n
だから、早くあんたに会って確かめたかったんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_4")
T "「どうやら、夢じゃなかったみたいね。\n
……もしくは、私もあなたと同じ夢を見ているってことになるわ」"

hide bor_m_03_4
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_4")
voice bor_g0382
Boris "「ふふ、ありがたいね。\n
……で、[firstname]、この子達は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「私の友達よ。\n
朝食の席に呼んでもらったの」"

hide bor_m_01_10
show bor_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice bor_g0383
Boris "「へえ？\n
……俺も一緒していい？」"

hide bor_m_02_7
show bor_m_02_7 at left
with dis

show amuse_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice tad_g0046
Seito "「……も、もちろんよ。\n
ねえ？」"

hide bor_m_02_7
show bor_m_02_7 at left_center
hide amuse_a1_3
show amuse_a1_3 at center
with dis

show amuse_b1_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice sam_g0128
Seito "「ええ、もちろん構いませんっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は大歓迎といった風にボリスを迎えてくれた。\n
自寮の寮長なのだから、普通の反応なのかもしれないが意外だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……萎縮されたりするんだ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこまで気安い存在ではないらしい。\n
クラスメイトであり、親しく付き合っている身からすると、不思議に思えた。"

hide bor_m_02_7
show bor_m_02_1 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0384
Boris "「ありがと」"

play sound se_0161
hide bor_m_02_1

hide amuse_a1_3

hide amuse_b1_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは私の隣へと腰掛ける……、ついでのように、ちゅっと私の頬へと軽く口付けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！？\n
ボリス、人前で何考えて……！」"


show bor_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
Boris "「？」"

hide bor_m_02_7
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice bor_g0385
Boris "「何って、おはようのキス。\n
恋人同士なんだから、これくらい普通だろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは悪びれもなく言う。"

hide bor_m_01_10
show bor_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0386
Boris "「ね？\n
普通だよね？」"

hide bor_m_03_10
show bor_m_02_1 at left
with dis

show amuse_a1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0047
Seito "「！！！\n
はい、普通です！！」"

hide bor_m_02_1
show bor_m_02_1 at left_center
hide amuse_a1_4
show amuse_a1_4 at center
with dis

show amuse_b1_4 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0129
Seito "「ええ！\n
普通ですとも！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「いやいやいやいや」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言わされている感が満載だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（たしかに、恋人同士なら挨拶のキスくらい普通かもしれないけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアでは、仲のいい学生カップルを見掛けることもあった。\n
若い恋人達、キスをかわす場面も、そう珍しくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、自分のこととなると話は別。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "友人達だって、視線を時折ちらちらと向けてきている。\n
その視線の意味は……、後でたっぷり事情を聞かせなさいということだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……気付かなかったふりをしてもいいかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、こちらに好奇心満々の視線を向けているのは、目の前にいる二人だけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分達の寮の寮長。\n
彼が、いつもと違った時間にカフェテリアに現れているのだから、そりゃあ注目だってされる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（身近にいたし、クラスメイトだから意識が薄かったけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリス＝エレイは、注目されるべき有名人らしい。"

hide bor_m_02_1
show bor_m_01_5 at center
with dis
hide amuse_a1_4

hide amuse_b1_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0387
Boris "「なあ、[firstname]。\n
今日は一緒に教室に行こうぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……ええ。\n
そうね、一緒に行きましょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気付いていないのか……、気付いていてわざと知らないふりをしているのか。\n
気にしていないのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは、恋人がどうとかいうこと以外、いつもとなんら変わりない。\n
自然に誘ってくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、私にとってはまったく自然なことではなかった。"

hide bor_m_01_5
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par02_ct_amu_day with Dissolve(.8)
scene bg_map_day
with stripe_l_medium

scene bg10_sb_day
with stripe_l_medium

scene bg27_rk_day
with stripe_l_long

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……ねえ。\n
なんというか……、アレじゃない？」"

##[rchara1 PAY ATTENTION="false"]
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0388
Boris "「んー？\n
アレって何が？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人、並んで教室へと向かいながらそんな会話を交わす。\n
ボリスが加わってきたこともあって、なんだか朝食を食べた気がしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おなかは膨れているのだけれど、何を食べたのか覚えていない……。\n
そんな感じだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……その。\n
アピールしすぎ、じゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がこれまで誰かと恋人関係になったことがないから、そう思ってしまうだけなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスに望まれ、それを断りきれなかった私。\n
現在、通学路で手を繋ぐなんていう、非常に恥ずかしいことを実践している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "通学途中のほかの生徒達が、私達へと視線をとめては、にやっとした笑みを浮べて去っていくのがなんとも言い難い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（恋人同士でこういうふうに過ごしている人はいるけど……。\n
自分が当事者側になるとは……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けして嫌な笑みでも、悪質なからかいというわけではない。\n
それでも、やはり冷やかされるのは恥ずかしい。"

hide bor_m_01_11
show bor_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0389
Boris "「そう？実際カップルなんだから、いいと思うけど？\n
他にもいるだろ、そういう奴等」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「いる、けど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それは自分ではない。\n
いや、これまではなかったと過去形でいうべきか。"

hide bor_m_02_7
show bor_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0390
Boris "「別に、見苦しいほどイチャついてはいないと思うけどなあ。\n
恥ずかしいんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「と、当然でしょ……」"

hide bor_m_02_2
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice bor_g0391
Boris "「ふうん？俺、あんたと一緒にいるの好きだぜ？\n
……あんたは、嫌？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「い、嫌じゃないけど……っ。\n
今までしたことが、ないから……」"

hide bor_m_01_10

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "戸惑ってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前の恋は、一方的な片思いで終わってしまった。\n
だから、好きになって、告白して、その先の関係なんていうのは手探りだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……ボリスは、慣れているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと、疑問に思った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは人気があるし、近寄りがたいと思われている面もあるようだ。\n
今まで意識が薄かったが、立派に寮長として見られている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そもそも人望がなければ、寮長などしていないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "困っている人がいれば、助けるかの判断はさておき、ひとまず声をかけてみる程度のことは行う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本人はあまりそういう評価が好きではなさそうだが、面倒見だって悪いほうじゃない。女生徒にだって、それなりにもてるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（そんなボリスが、どうして私なのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "疑問と……、不安。\n
真っ白な紙にぽたりと落ちたインクのように、私の心の中にじわじわと広がっていった。"

with dis
$ hi_mes()

scene bg27_rk_day with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg06_sk_h_day with stripe_l_medlong

play music classroom_day_p_wam

scene bg_map_day
with stripe_l_medium

scene bg10_sb_day
with stripe_l_medium

scene bg01_cr_day
with stripe_l_long
play sound se_0497
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「……ふう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ようやく一日の授業が終わって、一息つく。\n
ホームルームも、とくに何事もなかったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……平和、ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスが私と交際していることをオープンにし始めてから、そろそろ一週間になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初の頃こそ、好奇心の塊になった友人らに話を聞かれたりしたものの……、私達の関係は至って普通だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "クラスメイトだったのが、次第に意識しあうようになり、そしてイベントをきっかけにくっついた。\n
それ以上でも、以下でもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これといったトラブルもなく、順調な交際。\n
私にとっては一大事だが、別に燃えるようなロマンスがあったわけでもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次第に私達の関係は当たり前のように受け入れられ、以前となんら変わらない生活を続けていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（よかった……んだけど、拍子抜けというか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後になればカフェテリアで読書に励んでみたり、ボリスに誘われれば、一緒に改造マジックアイテムの実験に付き合うこともある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな、至って平和な日常が私達の間には流れ始めていた。\n
贅沢にも、そうした日々に、私は少しだけ不満を持つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、不満というよりも、不安に近いのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ねえ、ボリス……」"


show pia_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_g0020
Pierce "「うわあああん！\n
猫怖いよう！猫怖いよう～～…！！」"

play sound se_0119
hide pia_m_02_5

pause .5

show bor_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_g0392
Boris "「にゃはははっ！！\n
待てネズミ！俺から逃げられると思うなよ！！！」"

play sound se_0590
hide bor_m_02_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が呼び止めるよりも先に、ボリスはピアスを追いかけながら、教室を出て行ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（……あーあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これで何度目だろう。\n
非常に肩透かしを食らったような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（一緒に帰ろうと思っていたのにな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨日は確か、双子との約束だったか邪魔されたか何かで、結局ボリスと話すことが出来なかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして恋人が出来ると分かるが、シンフォニア高位魔法学校というのはカップルには不親切だ。もとより、そうしたものに親切にする必要はないのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校とは公共の場所。\n
だから、そう簡単に二人きりになれるような場所を手に入れることは出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……ブリーズのこと、相談したかったんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽつり呟いて、私も寮に戻る準備をし始める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とボリスが付き合い始めてから約一週間。\n
ということは、つまり、ストームからの一週間ということだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの後にはブリーズというイベントがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逆にしたようなイベントで、今度は女子が男子寮へと侵入し、ストームの夜に奪われたものを取り返すことになるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の場合は、ボリスからリボンを奪い返すことになるわけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ストームと似たイベントというからには、二人きりになれるのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃は固く禁じられ、区別されている男子寮と女子寮の境界が曖昧になる、稀有なイベントだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際にその日が来る前に、これまではどんなふうに過ごしていたのだとか、具体的にどんなふうに行われるのかを聞いておきたかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（なのに、ボリスったら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別に、ボリスに私だけを優先してほしいと思っているわけではない。\n
彼にだって友人はいるだろうし、その付き合いは大事だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私にだって、友人はいる。\n
しかし……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（……馬鹿猫）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスはその猫耳や尻尾からも分かるとおり、猫のような性質を持っている。\n
それは彼の趣味からもよく分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "マジックアイテムの改造にどっぷりと浸かり、時間さえあればひたすらそれをいじり続ける日がしばらく続いたかと思うと……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度はぱったりと触ろうともしない日が続いたりもする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスに構い倒すことがあったかと思えば、ふいっと見向きもしなくなるようなこともある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……気紛れ、なのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間近で見ているからこそ分かり、そして、だからこそ不安になる。\n
私にも飽きているのではないかと、怖くなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……せっかく、貰ってきたのになあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相談なんて、口実。\n
そして、これも口実の一つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ノートに挟んであった二枚のチケットを手にとって、一人、眺める。"


show boy_c1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0034
Seito "「あ、いいなあ！\n
それ、人気あるよな！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "突然脇から声をかけられて、顔を上げる。\n
そこにいたのはクラスメイトの青年だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きらきらと顔を輝かせて、私の手元にあるチケットを見ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ああ、そうなの。\n
ボリスと行こうかと思っていたんだけど……」"

hide boy_c1_2
show boy_c1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice suz_g0035
Seito "「あ～……。\n
ボリス、ピアスのやつ追いかけて出て行っちゃったから……」"

hide boy_c1_8
show boy_c1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice suz_g0036
Seito "「やっぱり猫とネズミだからなのか、ボリス、たまに夢中になっちまうんだよな。\n
……でも、それ、今日までだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……そうなのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "現在、シンフォニアの美術館では世界各国、各地で発見された珍しいマジックアイテムを集めた展示会が行われているのだ。"

hide boy_c1_8
show boy_c1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0037
Seito "「俺、それにすごく行きたかったんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらっと、期待するような目。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（う～ん……。\n
私も、興味があったのよね、これ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっとボリスも見たがるだろうと思って、先行予約までして手に入れたのだが……。その本人ときたら、ネズミに夢中で捕まらないときた。"

menu:
    "チケットをあげる。":
        jump gakuen_boris5_2a
    "男子生徒を誘う。":
        jump gakuen_boris5_2b
label gakuen_boris5_2a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（でも、一人で行ってもなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「よかったら、これ、貰ってくれない？\n
せっかくのチケットなんだけど……、無駄になっちゃいそうだし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼がそういうものが好きで、興味があるのなら是非使ってほしい。\n
このまま私が持っていても、ゴミになってしまうだけだ。"

hide boy_c1_8
show boy_c1_4 at center
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
T "すいっとチケットを差し出すと、彼は驚いたようにしながらも受け取ってくれた。"

hide boy_c1_4
show boy_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0038
Seito "「なあなあ、せっかく二枚あるならさ。\n
今から一緒に見にいかないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え？\n
あなたと一緒に？」"

hide boy_c1_3
show boy_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice suz_g0039
Seito "「俺も、今から、誰か付き合ってくれる奴を探すの大変だし。\n
一人で行っても、感想を言う相手がいないとつまらない」"

hide boy_c1_3
show boy_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice suz_g0040
Seito "「[firstname]、君だって、興味あるジャンルなんだろ？\n
どう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（それは……、いいかもしれない）"

jump gakuen_boris5_3
label gakuen_boris5_2b:
$ lovechara_boris_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ねえ、提案なんだけれども。\n
私と一緒に見に行かない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「せっかく二枚あるんですもの。\n
ああ、でも、もし誰か一緒に行きたい相手がいるのなら別よ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼が断りやすいように、わざと軽い調子で誘う。"

hide boy_c1_3
show boy_c1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0041
Seito "「え？俺なんかでいいの？\n
ボリスを誘おうとしてたんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「……いない人が悪いのよ。\n
無駄にしちゃうのももったいないし、どうかしら」"

hide boy_c1_4
show boy_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice suz_g0042
Seito "「そういうことなら、付き合うよ。\n
俺も、興味のあるジャンルなんだよな」"

hide boy_c1_3
show boy_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice suz_g0043
Seito "「[firstname]、君の言うとおり、チケットを無駄にするなんてもったいなさすぎる」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（いいわよね？）"

jump gakuen_boris5_3
label gakuen_boris5_3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "というわけで、彼と一緒に美術館を目指すことにした。"

hide boy_c1_3
##[chara3 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg01_cr_day
with dis

scene bg_map_day
with stripe_l_medium

scene bg_map_eve
with stripe_l_medium

scene bg22_ms_o_eve
with stripe_l_long

play music gallery_front_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "美術館の展示物はどれも目新しく、面白いものばかり。"

##[rchara3 PAY ATTENTION="false"]
show boy_c1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0044
Seito "「なあなあ、楽しかった？\n
俺は楽しかった！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同行者の彼も、答える前に感想を言わずにいられないほど、興奮状態のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「ええ、私も楽しかったわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "趣味が合うもの同士。\n
感想を交わしながら遊園地寮へと戻ってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あらかじめチケットが必要になるのが分かるぐらい、充実した展示内容だった。"

hide boy_c1_2


scene bg22_ms_i_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ見て回るのならば、いつものように入館者を制限しなくてもよさそうなもの。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今回は、展示されているマジックアイテムのほとんどを実際に発動させてくれるという体験コースつきだったため……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こういうチケットによる人数制限が必要になったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（どれも面白いアイディアだった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使われている魔法としては、難しいものから簡単なものまでピンからキリまであるのだが、その使われ方がどれも特徴的だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ああ、こういうやり方もあるのか、と見ていてわくわくとした。\n
同好の連れがいるので、なおさら有意義に過ごせる。"


scene bg_par15_rg_amu_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……ボリスに見せてあげたかったなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "隣にいる人を差し置いてこんなふうに思うのは、失礼なこと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、やっぱりそう思ってしまうのは仕方ない。\n
ボリスは……、恋人なのだから。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……と。"


play music gloomy_a_wam

show bor_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0393
Boris "「……どこに行ってたんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮の門扉をくぐったところで、ゆらりとその影がさした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ボリス？」"

hide bor_m_01_8
show bor_m_01_8 at left
with dis

show boy_c1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice suz_g0045
Seito "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一緒にいた彼が、分かりやすく慌てる。\n
下手に疑われたくないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それが分かるから、私も慌ててフォローする。\n
ぱたりと、手を揺らした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「彼とはちょっと美術館に行ってきただけよ。\n
ボリスったら、誘う前にいなくなっちゃうんだもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょいと肩を竦めて、軽い調子で言う。\n
もともとはボリスを誘うつもりだったという事実をこめて口にする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスを誘わなかったのではなく、誘えなかったということを伝えたい。\n
実際、悪意などどこにもないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手持ち無沙汰なもの同士で、ちょっと美術館を見に行っただけにすぎない。\n
そこにボリスが疑いを差し挟む余地はどこにもない……、はずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、彼は悔しそうな顔をしている。"

hide bor_m_01_8
show bor_m_03_5 at center
with dis
hide boy_c1_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0394
Boris "「……俺が悪いのかよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！！\n
違うわよ、そんな意味じゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ボリスが悪いわけじゃないわ、たまたまタイミングが合わなかっただけよ」"

hide bor_m_03_5
show bor_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice bor_g0395
Boris "「タイミングが悪いと、あんた浮気しちゃうんだ？\n
はは、ひでえの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスが鼻で笑う。\n
酷い言葉だが、私を責めるというよりも、どこか自嘲するような響きに聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「そんなふうに……」"

hide bor_m_03_9
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Boris "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずんずんとボリスが距離を削って、私のもとへとやってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、私が危害でも加えられるのかと思ったのか、傍らにいたクラスメイトの青年が慌てて私の前に立ちはだかった。"

play sound se_0313
hide bor_m_01_11
show bor_m_01_11 at left
with dis

show boy_c1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0046
Seito "「ボリス……！\n
やめろよ、おまえらしくもない！」"

hide bor_m_01_11
show bor_m_02_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0396
Boris "「……どけよ。\n
どかないと、怪我するぜ？」"

hide boy_c1_7
show boy_c1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0047
Seito "「……っ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスの瞳は、冷えた色を浮べている。\n
今ならば、口だけでなく本当に、友人に対しても酷いことをしてしまいそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮長になるくらいだから、強さではボリスのほうが上。\n
だが、実際にそんなことをすれば、力を振るったほうだって後から傷つく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……行って」"

hide boy_c1_1
show boy_c1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice suz_g0048
Seito "「でも……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「いいから、行って」"

play sound se_0580
hide boy_c1_7

hide bor_m_02_12
show bor_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、私の声に叩かれたように、びくっと身を竦ませた。\n
それから、こちらを何度も振り返りながら、寮の中へと入っていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の姿が見えなくなるまで待つことなく、ボリスが一歩を踏み出した。\n
身構えた私の頬へと、するりと彼の手のひらが触れる。"


play music view_nig_p_wam

show m_bor5_1 onlayer master
with dis
hide bor_m_02_12

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……ボリス？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までと変わらない、優しい仕草だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0397
Boris "「……あんたってさ、分かんないよね。\n
そんなお嬢さんみたいな顔しているのに……、たいした悪女だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……はあ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice bor_g0398
Boris "「教えてよ。\n
俺はどうしたら、あんたを独り占めにできるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice bor_g0399
Boris "「俺の恋人だって宣言して、周囲を牽制して……。\n
なのに、あんたはほいほい他の男と出掛けていっちゃう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「だって、それは……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice bor_g0400
Boris "「俺、あんた以外の女の子と二人きりで遊んだりしないよ？\n
あんた以外に撫でられてもない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（……でも）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスだって、私のことを構ってくれなくなっていた。\n
私よりもピアスや双子達とばかり、遊ぶようになっていたじゃない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言い返してやろうと思ったのに、その言葉は次のボリスの言葉で、完全に止められてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0401
Boris "「押して駄目なら引いてみろっていうから、我慢して実践してみたらさ。\n
そのままふらふら浮気だなんて酷いだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0402
Boris "「知ってた？\n
あんた……、俺に好きって言ってくれたことないんだぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉に詰まった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……その通りだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、一度も自分の気持ちを言葉にしてボリスに伝えていない。\n
ボリスの好意に甘えて、好きだと言ってくれたのに頷いただけだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0403
Boris "「あんたにとっての俺ってさ。\n
……嫌いじゃない、って程度なんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……そういうふうに言ったのは、ボリスよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice bor_g0404
Boris "「うん、それで、あんたは頷いてくれた。\n
スタートは、それでよかったんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice bor_g0405
Boris "「そこからって意味で……、もっとを望んでるんだよ？\n
俺はさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……もしかして）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスも、不安だったのだろうか。"

play sound se_0551
play sound se_0693 volume .6
hide m_bor5_1
show m_bor5_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっと、ボリスの手が下りる。\n
頬に触れていたぬくもりが離れるのが、いやに心細かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夕暮れ時の風が、冷たい。\n
ボリスは俯いて、深々と息を吐き出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0406
Boris "「……はあ、もう飯の時間だな。\n
行けば？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食堂へ移動するように、促される。\n
けれど、一緒に行こうとは言ってくれなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……うん」"

hide m_bor5_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さく頷いて、食堂へと向かってとぼとぼと歩き始める。\n
頷きは消極的なもので、あの夜とはまったく違っていた。"

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music stream_eve_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夕食を終えた後、遊園地寮の入り口近くで涼む。\n
部屋に戻る気になれなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エントランスへと続く階段に腰掛けて、ぼんやりとする。\n
考えるのは、ボリスのことと自分のことだ。"


show go_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0229
Gowland "「……[firstname]。\n
あんた、顔が死んでねえか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声をかけてきたのは、ゴーランドだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……うるさいわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら彼は見回りの途中らしい。\n
私の様子に足を止めて、傍らまでやってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "酷い顔をしている自覚はあったので、そのまま立ち去ってくれないかと思うのに、彼は私の隣に腰を下ろしてしまう。"

hide go_m_02_5
show go_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0230
Gowland "「よっこらせ、っと」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

hide go_m_03_12
show go_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gor_g0231
Gowland "「……あ。\n
今あんた、俺のことおっさんくせえとか思っただろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「思ってないわよ。\n
被害妄想よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正確には、ゴーランドのことを考える余裕すらない。\n
私の頭の中はボリスのことだけで、いっぱいいっぱいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……早く、立ち去ってくれたらいいのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今の私は、態度も可愛くない。\n
一緒にいて楽しい相手とはいえない。"

hide go_m_01_6
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0232
Gowland "「そんなツラして、どうしたんだ？\n
ボリスの野郎と喧嘩でもしたか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "図星をつかれて、動揺する。\n
私はどんな顔をしているというのだろう。"

hide go_m_03_9
show go_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0233
Gowland "「はは、図星か。\n
で、どんな悪さをしたんだ、あいつは」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……ボリスは、悪くないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（悪いのは、私よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「……酷い顔をしているでしょう、私」"

hide go_m_01_8
show go_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
Gowland "「…………」"

hide go_m_03_1
show go_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
voice gor_g0234
Gowland "「……ったく、ボリスのやつもまだまだガキだな。\n
好きな女、不細工にしてどうするんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「不細工って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（まあ、可愛くない態度だっていうのは分かっているけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔も態度につりあっているということだろうか。"

hide go_m_02_10
show go_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0235
Gowland "「……辛気臭い顔じゃ、美人も台無しだってことだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽん、とゴーランドの大きな手が私の頭にのった。\n
くしゃくしゃ、と無造作に頭を撫でられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（……どう見ても、美人ってタイプじゃないのに、私）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この手が、あの破壊的な音楽を紡ぐのだとは思えないほどに、優しい感覚だった。\n
じんわりとぬくもりが伝わってきて、涙腺が緩みそうになる。"

hide go_m_03_12
show go_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0236
Gowland "「俺に話してみろよ。\n
少しはマシな気分になるかもしれないぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……そうね。\n
話せば、美人になれるかも」"

hide go_m_03_4
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME

play music moon_night1_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは、私の話を最後までしっかりと聞いてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か答えをもらったわけでもないのに、気分が落ち着く。\n
話すことで、状況を自分なりに整理が出来たからだろう。"

##[rchara2 PAY ATTENTION="false"]
show go_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0237
Gowland "「はは。\n
若いっていいよなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……{size=+20}オヤジ{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "話をすべて聞いての感想が、それとは。\n
落ち込んでいたのも忘れて、つっこんでしまった。"

hide go_m_03_5
show go_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0238
Gowland "「あ、やっぱり！\n
言ったな！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「だって、実際にそうだもの……」"

hide go_m_02_11
show go_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gor_g0239
Gowland "「まあ、あんたからすりゃあな。\n
オヤジだろうさ」"

hide go_m_03_11
show go_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gor_g0240
Gowland "「そこまで、青春～みたいなのは、無理だもんなあ。\n
ボリスやあんたみたいに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「っ……、厭味……」"

hide go_m_01_12
show go_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice gor_g0241
Gowland "「はは。\n
学生らしくていいと思うぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは、楽しそうに笑うばかりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやって笑われると、今抱えている問題がなんでもないことのように感じてしまう。いくらでも修復可能な、他愛もないことのように。"

hide go_m_01_8
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0242
Gowland "「あんたは、ボリスが好きなんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……ええ」"

hide go_m_03_9
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice gor_g0243
Gowland "「ボリスも、あんたのことが好きなんだ。\n
そうだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……でも、そんなに簡単じゃないわ」"

hide go_m_02_12
show go_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice gor_g0244
Gowland "「簡単だよ。伝え合えばいいんだ。\n
ささいな誤解なんだからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「その……、伝え合うっていうのが難しいのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がすっかり、引っ掻き回してしまった。\n
ボリスは私が浮気をしたと思って怒っているし、もしかしたらもう、私のことを嫌いになってしまったかもしれない。"

hide go_m_02_8
show go_m_03_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0245
Gowland "「そんなに難しいことでもないと思うが……、それもまた青春ってやつか」"

hide go_m_03_14
show go_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0246
Gowland "「……よしっ。\n
それじゃあ俺が、とびきりの仲直りの方法を教えてやろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……信用ならないわ」"

hide go_m_01_2
show go_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice gor_g0247
Gowland "「ひでえな、あんた！\n
担任の先生だぜ？信用しろよ、先生を！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「無理……って、わあ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わしゃわしゃわしゃっと髪をぐちゃぐちゃにしながら頭を撫でられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「ちょ……っ、やめてよ！\n
髪がぐちゃぐちゃになっちゃう……！！」"

hide go_m_03_7
show go_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
voice gor_g0248
Gowland "「ははっ。\n
ほら、耳貸せって」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、言われるままにゴーランドの口元へと耳を寄せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "溺れるものは藁をも掴む、という心境だったのかもしれない。\n
……が、そんなことを口に出せば、また頭をぐしゃぐしゃにされそうだ。"

play sound se_0688
pause 1

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「ええっ！？\n
そ、そんなこと……」"

hide go_m_03_5
show go_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gor_g0249
Gowland "「まあ、実行するしないはあんた次第だけどな？\n
効果はあると思うぜ～」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、と言葉を続けて、ゴーランドがちらりと私を見る。\n
子を心配する、保護者のような色が浮かんでいた。"

hide go_m_01_3
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0250
Gowland "「やれること全部やって、素直にならなきゃ駄目だろ？\n
あんたも」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……っ！！」"

menu:
    "その通りだ。":
        jump gakuen_boris5_4a
    "それでも……。":
        jump gakuen_boris5_4b
label gakuen_boris5_4a:
$ lovechara_boris_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その通りだ。\n
今もなお、昔の夢を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "繰り返し夢見てしまうのは、彼への未練というより自分の行動への後悔という面が大きい。\n
あのとき、私は逃げてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きちんと引導を渡されていたのならば、もっと早くに思い切れていたのではないだろうか。"

jump gakuen_boris5_5
label gakuen_boris5_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの言うことは分かる。\n
正面からぶつかって、素直になれば、失敗しても諦めはつくだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも……、やはり完全に駄目になると分かるのは怖い。\n
諦めてしまうのも、また辛いのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は結果を突きつけられたくなかったから、過去、あのときもラブレターを渡すことなく逃げ帰った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "傷つくことから逃げた。\n
そして、代わりにいつまでも終わらない夢の中に閉じ込められてしまった。"

jump gakuen_boris5_5
label gakuen_boris5_5:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（……あんな夢は、もうたくさん）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう、あの夢を見たくない。\n
あんな思い出を増やしたくはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……そうね。\n
やれることは、全部やってみようと思うわ」"

hide go_m_03_9
show go_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gor_g0251
Gowland "「おう。そうしろ、そうしろ。\n
行動してこその青春だぜ？」"

hide go_m_02_8
show go_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gor_g0252
Gowland "「それにしても、ボリスのやつもなあ。\n
まったく、青春ってのは青臭い春つーか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……青春青春って、連呼しないでよ。\n
こっちのほうが恥ずかしくなるわ」"

hide go_m_03_2
show go_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gor_g0253
Gowland "「見栄が強いのも、年頃ゆえだよなあ」"

hide go_m_02_10
show go_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gor_g0254
Gowland "「……玄関先で座り込んでいる女子生徒がいるから……なんて。\n
俺を行かせるぐらいなら、最初っからいじめるなって話だ」"

hide go_m_03_1
show go_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gor_g0255
Gowland "「……あれで、相当に子供っぽいから。\n
絶対近くで聞いてるか、魔法を仕掛けて見張ってるだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるで、ここにいない誰かに話しかけるように。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばりばり、と頭をかきながら呟かれたゴーランドのぼやきは、よく聞こえなかった。"

hide go_m_01_6
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_amu_eve with Dissolve(.8)

scene bg_map_eve
with stripe_l_long
##endmemory
jump gakuen_boris6
