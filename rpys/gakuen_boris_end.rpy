label gakuen_boris_end:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_amu_day
with dis

scene bg25_rr_day with Dissolve(1.2)

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次の日の朝。\n
眠いやらくたびれたやらで重い体をのそのそと引きずってカフェテリアへと向かっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、朝方のどさくさまぎれに自室へ戻ったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一応、姿隠しの魔法を使ったとはいえ、使用人に見つからなかったのは奇跡に近い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……使用人や職員も、寝不足なのかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばふりとベッドに倒れこむようにして眠りにつき、どうにかこうにか、いつもの時間に起床した。\n
のろのろと身支度を整え……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜の名残でか、ざわつくカフェテリアの中へと足を進める。"


play music dining_day_p_wam

scene bg_par02_ct_amu_day with stripe_l_medlong
play sound se_0559
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……？）"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がカフェテリアに入った瞬間、空気がざわついたような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気のせいだろうか。\n
いつものように空いている席……、というか、いつも同席する彼女達を探す。"

play sound se_0185

show amuse_a2_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「……[firstname]！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこかで勢いよく立ち上がる音がした、と思った次の瞬間には、感極まったというような声で名前を呼ばれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振り返ると、彼女達だ。\n
まずは、協力してくれたお礼を言わねば。"

hide amuse_a2_4
show amuse_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0054
Seito "「おめでとう……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「は？」"

hide amuse_a2_2
show amuse_a2_2 at left
with dis

show amuse_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sam_g0138
Seito "「おめでとう、[firstname]……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「はあ？」{/size} "


play music district_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "変な声が出てしまう。\n
何故なら、そこだけテーブルがおかしなことになっていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やたらと知り合いが密集している。\n
クラスメイトの率が高すぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その中でも目立つ長躯。\n
担任であるゴーランドまでが、テーブルに頬杖をついて、にやにやと笑いながらこちらを見ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "傍らで寝潰れているのはピアスだ。\n
……ここにいたっては、何をしにカフェテリアに来たのか謎だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆がにやにや笑いで私を見つめている中、ピアスだけが机に突っ伏して爆睡している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今は、それが非常にありがたく思えてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……一番、無意味に騒ぎそうだものね）"

hide amuse_a2_2

hide amuse_b1_2


show boy_c1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice suz_g0049
Seito "「いやー、よかったよ！\n
俺との浮気が原因で別れたとか言われたら、責任重大だもんな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、展示会に一緒に行った男子生徒。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……浮気の事実はないわよ？」"

hide boy_c1_2
show boy_c1_2 at left
with dis

show boy_d1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice kaz_g0041
Seito "「俺は関係ないけど、安心したよ！\n
同じクラス内で破局なんかされたら、残り一年の空気が怖いぜ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……それは分かる気がするけれど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かといって、引っ付くことを祝うのは分からない。"

hide boy_c1_2

hide boy_d1_2
show boy_d1_2 at left
with dis

show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0073
Seito "「おめでとう！\n
あなた達、お似合いのカップルだと思うわ！」"

hide boy_d1_2

hide girl_b1_2
show girl_b1_2 at left
with dis

show girl_c1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0042
Seito "「末永くお幸せにね！！」"

play sound se_0654
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……何、このノリ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知人や友人のお祝いムード。\n
まるで……、あまり認めたくはないが、結婚式のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（親戚の結婚式に参加したとき、こんなふうだったなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……って、なんで？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当なら、朝食の時間を削ってでも惰眠を貪っていたかった私が、こうしてわざわざカフェテリアにやってきたのは……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "色々と助言をくれた食事仲間に報告をするためだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他のクラスメイトや、ゴーランドに関しては、ホームルームやら授業のときなどいくらでも伝えるタイミングはある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、こうして朝のこの時間にやってきた。しかし、これではまるで、皆もう結果がどうなっているのかを知っているかのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "祝福モードのクラスメイトやら、友人達を前に、私は固まるしかない。\n
動けずにいた私に、苦笑を浮べたゴーランドが種明かしをしてくれた。"


play music gowland_t_ali

show go_m_01_8 at center
with dis
hide girl_b1_2

hide girl_c1_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0256
Gowland "「あんた、昨日帰ってこなかっただろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……{size=+20}っ！！{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "びくっとする。\n
いくらゴーランドとはいえ、相手は教師だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "門限破りがバレるのはまずい。"

hide go_m_01_8
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0257
Gowland "「……ま、その辺は気にしなくていい。\n
昨日のは、俺もそそのかしたようなもんだし、同罪だ」"

hide go_m_03_9
show go_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0258
Gowland "「あ。\n
間違っても塔の連中には言うんじゃねえぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「い、言うわけないわよっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "懲罰行為を、喧伝するような趣味はない。\n
けれど、同罪というのはどういうことなのか。"

hide go_m_01_6


show girl_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0074
Seito "「本当なら、生徒の点呼は寮長のボリスの仕事なのよ。\n
けど……、昨日ボリスはあなたと一緒だったわけでしょう？」"

hide girl_b1_3
show girl_b1_3 at left
with dis

show girl_c1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0043
Seito "「それで、ゴーランド先生が代わりに点呼をとったってわけ。\n
ついでにあなたのことと、ボリスのことを誤魔化したのもゴーランド先生よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ゴーランド」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……{size=+20}それって、どうなの{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "感謝するより、呆れてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他のクラスメイトや、友人らが私に協力してくれるのとはわけが違う。\n
彼は教師なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来ならば、生徒を管理し、生徒が校則に反した場合には罰しなければいけない立場。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「え～と……。\n
ありがとう、ゴーランド」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とりあえず、感謝しておこう。"

hide girl_b1_3

hide girl_c1_2


show go_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0259
Gowland "「いいってことよ。\n
ああ、でも今回だけだからな？」"

hide go_m_01_1
show go_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0260
Gowland "「女子寮と男子寮の行き来は禁止事項だ。\n
次からは容赦なくとっ捕まえるからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「はーい、気をつけるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざとらしく難しい顔をしてみせたゴーランドへと、私もよい子の返事を返しておいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……それで、筒抜けだったのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来ボリスのしなければならない仕事を、ゴーランドが肩代わりしている様というのは……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ある程度事情を知っている者にとっては充分にピンとくる光景だったに違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（そっか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（筒抜け……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_14")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_7")
T "（……うう）"

hide go_m_03_6


show amuse_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_7")
voice tad_g0055
Seito "「ふふ、うまくいったんだから、落ち込んだりしないでよ」"

hide amuse_a1_3
show amuse_a1_3 at left
with dis

show amuse_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_7")
voice sam_g0139
Seito "「あら、落ち込んでいるんじゃなくて、照れているんでしょう。\n
顔が赤いわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……っ！\n
もう、からかわないでよっ」"

hide amuse_a1_3
show amuse_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice tad_g0056
Seito "「はは、からかっているわけじゃないの。\n
祝福しているのよ」"

hide amuse_b1_2
show amuse_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice sam_g0140
Seito "「……応援、してあげたでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……～～～～っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言われてしまうと、反論しづらくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、からかっていないと言うものの、笑っているし……。\n
どう見ても、からかわれている。"


play music dining_day_p_wam
hide amuse_a1_2
show amuse_a1_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0057
Seito "「……ん？」"

hide amuse_b1_3
show amuse_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0141
Seito "「あら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人混みの向こうに、ちらりとピンク色が見えた気がした。\n
ピンクときたら……、ボリスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は私を探すように視線をぐるりとめぐらせて……。"


show bor_m_01_1 at center
with dis
hide amuse_a1_9

hide amuse_b1_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0461
Boris "「ん？\n
いぃ……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にやにやと笑いながら待ち構える集団に、ぎょっとしたような顔をした。\n
その気持ちはとてもよく分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ほんの数分前に、私が通った道だ。"

hide bor_m_01_1
show bor_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0462
Boris "「にゃ、にゃに……！？\n
何なの？」"

hide bor_m_03_1
show bor_m_03_1 at left
with dis

show boy_c1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0050
Seito "「ボリス、おめでとう！！！」"

hide bor_m_03_1
show bor_m_03_1 at left_center
hide boy_c1_2
show boy_c1_2 at center
with dis

show boy_d1_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0042
Seito "「両思いおめでとう！！！\n
よかったな、ボリス！！！」"

hide bor_m_03_1

hide boy_c1_2
show boy_c1_2 at left_center
hide boy_d1_2
show boy_d1_2 at center
with dis

show girl_b1_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0075
Seito "「うまくいってよかったわね！\n
末永くお幸せに！」"

hide boy_c1_2

hide boy_d1_2
show boy_d1_2 at left_center
hide girl_b1_2
show girl_b1_2 at center
with dis

show bor_m_01_9 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0463
Boris "「う……、うん？\n
幸せになるのも、幸せにするのもやぶさかではないんだけど……」"

hide bor_m_01_9
show bor_m_01_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0464
Boris "「これ、何の騒ぎなんだ？\n
……暇人の集まり？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、ボリスはなかなか酷いことを言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……まあ、当たっているんだけどね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "暇を持て余した人達のやることに、間違いはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……バレバレなのよ。\n
ほら、あなた、昨日点呼とってないでしょ」"

hide boy_d1_2

hide girl_b1_2

hide bor_m_01_3
show bor_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0465
Boris "「……{size=+20}あ{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こそこそっと近くにやってきたボリスに、簡潔に説明する。\n
点呼、との言葉に、ボリスはすぐに事情を察したらしい。"

hide bor_m_01_1
show bor_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0466
Boris "「……そっか。\n
だよなあ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あちゃあ、という顔をしている。"

hide bor_m_03_11
show bor_m_03_11 at left
with dis

show go_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0261
Gowland "「何はともあれ……、うまくいったならいいじゃねえか！\n
ほら、おまえらもさっさと飯を食え！」"

hide go_m_03_4
show go_m_02_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0262
Gowland "「ホームルームに間に合わなくなるぞ！」"

hide bor_m_03_11

hide go_m_02_11


show boy_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0051
Seito "「は～い……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「うん。\n
ほら、からかうから、時間がなくなっちゃうわよ」"

hide boy_c1_3
show boy_c1_3 at left
with dis

show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice nos_g0076
Seito "「はいはい。\n
朝は食べないとね～……」"

hide boy_c1_3
show boy_c1_3 at left_center
hide girl_b1_3
show girl_b1_3 at center
with dis

show pia_m_02_12 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice pie_g0021
Pierce "「むにゃ……。\n
俺、もう食べられないよ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに促されて、私達もテーブルについた。\n
端っこから、ピアスの幸せそうな寝言が聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それぞれ、朝食を呼び出す。"


play music gag1_a_wam
hide boy_c1_3

hide pia_m_02_12

hide girl_b1_3
show girl_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0077
Seito "「あ、ねえ、お祝いなんだし、やっぱりケーキを出すべきかしら……」"

hide girl_b1_3
show girl_b1_3 at left
with dis

show girl_c1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0044
Seito "「でも、朝からケーキはちょっと重くないかしら」"

hide girl_b1_3
show girl_b1_3 at left_center
hide girl_c1_5
show girl_c1_5 at center
with dis

show boy_c1_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0052
Seito "「女子は、甘いものって別腹なんじゃないのか？」"

hide girl_b1_3
show girl_b1_3 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0078
Seito "「偏見よ～」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "{size=+20}「お祝いでケーキっていうのも、偏見だから、出さないでね？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女らのテンションならば、本気でやりかねない。\n
朝からケーキなんて呼び出された日には……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（応援してくれたのは有り難いけど、お祝いは遠慮したい……）"

hide girl_c1_5
show girl_c1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice ari_g0045
Seito "「そうよね……。\n
いくらカフェテリアの魔法が軽食向きでケーキの種類も豊富だからって、ウェディングケーキはないわよね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "{size=+20}「そういう意味じゃないわよ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ケーキの種類を言っているのではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、ウェディングケーキとは。\n
悪乗りしすぎだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……そうよ、今すぐに学生結婚なんて。\n
考えられないわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "考えられない、とか。\n
そういう時点で、考えてしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……浮かれているなあ、私も。\n
冷静にならなくちゃ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "サラダ、トースト、オレンジジュースといつもの定番メニューを呼び出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "黙々とそれらを口に運ぶが、ひたすら聞こえてくる話題は無視できるものではなかった。"

hide girl_b1_3
show girl_b2_5 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0079
Seito "「やっぱりメイドさんに頼んで特注かしら……」"

hide girl_c1_5
show girl_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0046
Seito "「いえ、ここはやはり新婦友人作、ということで……。\n
私達で作るべきじゃないかしら」"

hide girl_b2_5

hide girl_c1_3

hide boy_c1_3
show amuse_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0058
Seito "「クラスメイトじゃないけど、私達も混ぜてくれる？」"

hide amuse_a1_2
show amuse_a1_2 at left
with dis

show amuse_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0142
Seito "「及ばずながら力になりたいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "{size=+20}（ならなくていい、ならなくていい）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさか、本気ではないだろうが、彼女達のノリならやりかねない。\n
少なくとも、食事中のネタにされることは確定しているようだ。"

hide amuse_a1_2
show amuse_a1_2 at left_center
hide amuse_b1_2
show amuse_b1_2 at center
with dis

show girl_b1_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0080
Seito "「もちろんよ！\n
皆で祝いましょう」"

hide amuse_a1_2

hide amuse_b1_2
show amuse_b1_2 at left_center
hide girl_b1_2
show girl_b1_2 at center
with dis

show girl_c1_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0047
Seito "「そうよ、皆で祝ったほうが面白……、ごほん、ボリスとこの子も喜ぶわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……今、本音が出たわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん私を祝ってくれる気持ちに嘘はないだろうが、それと同等か、それ以上に面白がっている節がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じろりと半眼を向けてれば、ボリスが私の代わりに口を開いた。"

hide girl_b1_2

hide amuse_b1_2

hide girl_c1_2
show bor_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0467
Boris "「おまえらなあ……。\n
勝手なこと言うなよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（そうよそうよ）"

hide bor_m_01_8
show bor_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice bor_g0468
Boris "「気が早すぎ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（そうそう……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頷きながらも、浮かれかけていた自分をも諌められているような気になる。"

hide bor_m_03_13
show bor_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0469
Boris "{size=+20}「まだ、ご実家へ挨拶にも行ってないんだぜ？」{/size} "

play sound se_0015
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……{size=+20}え？{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「ボ、ボリス！？\n
何を言っているのよ……っ！」"

hide bor_m_01_9
show bor_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice bor_g0470
Boris "「え？\n
何って……、今年の夏の予定？」"

play sound se_0212
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「げふっ！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むせた。\n
まさかそれは、今年の夏の長期休暇に、私の実家を訪ねたいということなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「駄目よっ、ダメダメ！！\n
あなたこそ、気が早すぎるわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "家族に激震が走る。\n
むしろヒビが入りかねない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "浮き立ちかけたものの、私は現実主義。\n
現実的に考えて、いらぬ波風はたてないほうがいい。"


hide bor_m_02_7


show amuse_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0060
Seito "「いいじゃない！」"

hide amuse_a1_2
show amuse_a1_2 at left
with dis

show amuse_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0144
Seito "「真剣なお付き合いなのね！」"

hide amuse_a1_2
show amuse_a1_2 at left_center
hide amuse_b1_2
show amuse_b1_2 at center
with dis

show girl_b1_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0082
Seito "「素敵！」"

hide amuse_b1_2
show amuse_b1_2 at left_center
hide girl_b1_3
show girl_b1_3 at center
with dis
hide amuse_a1_2
show boy_c1_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0053
Seito "「男だな～。\n
応援するぜ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わあわあきゃあきゃあと盛り上がるクラスメイトやらボリスに、私はもはや言葉を失ってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（これ……、どこまでが本気なの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "半分以上、ノリにまかせた冗談なのだと思っていた。\n
だが、恐ろしいことに全部本気という可能性もある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……関わってはいけない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まともに相手をしては、恐ろしいことになりそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、周囲を拒絶するポーズをとりつつ、もぐもぐと口の中へとトーストを詰めていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（これで、話しかけるなという意思表示は伝わるはず……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しは、冷静になってくれればいいのだが。"

hide girl_b1_3

hide boy_c1_2

hide amuse_b1_2
show pia_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0022
Pierce "「おめでとう、[firstname]！\n
何がどうおめでたいのか分かんないけど、おめでたいんだよね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いきなり、意思表示も何もまったく読み取れないネズミが話しかけてきた。\n
この騒動の間、ずっと眠っていたピアス。\n
ようやく目覚めたらしかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（……寝ていればいいのに）"

hide pia_m_01_2
show pia_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice pie_g0023
Pierce "「あ！おめでたいって俺知っているよ、子供が出来ることだよね！？\n
先刻、ウェディングがどうとか言ってたし！」"

hide pia_m_03_5
show pia_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice pie_g0024
Pierce "「君のつがいはボリスだから～……、ん？\n
っていうことは君、猫を産むの！？」"


show gaaan2 onlayer master
with dis
play sound se_0042
hide pia_m_01_3
show pia_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice pie_g0025
Pierce "「猫を増やすの！？\n
猫の増量キャンペーン！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

hide gaaan2

hide pia_m_02_6
show pia_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pie_g0026
Pierce "「やだやだ、やだよ！\n
猫なんか増やさなくていいよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……{size=+20}寝てろ{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつのまにか現れていた巨大ケーキ（さすがにウェディングケーキは呼び出せなかったらしいが）を、ピアスの口に詰め込んでやる。"

hide pia_m_01_4
with dis
$ hi_mes()

scene bg_par02_ct_amu_day with Dissolve(.8)

scene bg_par15_rg_amu_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg06_sk_h_day with Dissolve(1)

scene bg06_sk_h_eve with Dissolve(1)

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_day with Dissolve(1.2)

play music daytime_a_wam
play sound se_0158
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……ふう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮にも、夏が近づいてきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……あっつい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮に向かって歩きながら、空を見上げる。\n
日差しは、日に日に強くなってきている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろそろ、制服を夏服に替えてもいいのではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（ああ、でも天気が悪いと肌寒かったりもするのよね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "難しい時期だ。\n
晴れていると暑くて、曇りや雨だと、肌寒い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "衣替えの時期は決められているものの、明確にこの日という指定はない。\n
クローゼットの整理の判断に悩む季節である。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（……季節が変わるのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもなら、ホームルームの後にボリスと一緒に寮に帰るのが常。\n
今日は私に用事があったため、ボリスには先に帰ってもらった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "図書館に今日中に返却しなければいけない本があったのだ。\n
それにせっかく図書館へ行くのなら、新しい本も見繕いたい。"

with dis
$ hi_mes()

scene bg06_sk_h_day with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg15_lb_o_day
with stripe_l_long

play music library_front_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_8")
T "（ふふ、掘り出し物を見つけたわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゆっくりじっくり本棚を見て歩いて、なかなか面白そうな本をいくつか見つけることができた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアでの紅茶の時間、あるいは夕食の後などの読書タイムは、私にとって至福の時だ。"


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法による本の転送システムを頼んだので、今頃はもう部屋に届いているだろう。\n
いつものように私は遊園地寮のエントランスへと足を踏み入れて……、驚いた。"


play music entrance_p_wam

scene bg_par20_re_bu
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮の名前が具現化されたよう。\n
まさしく遊園地だ。"

play sound se_0785
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エントランスの中には、色とりどりの風船が漂っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……透けている？\n
シャボン玉に近いのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初は風船かと思ったが、それほどの強度はなさそうだ。\n
だが、シャボン玉にしては大きい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人の顔ほどのサイズはある。\n
普通にシャボン玉ならば、すぐに割れてしまいそうなものだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "試しにそっと手を伸ばし、きらきらと光を弾きながら漂っているその一つを、つん、と指先で突いてみた。"

play sound se_0006
play sound se_0722
$ flash_light_blue(.2)
pause .2
play sound se_0771
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「わ、ひんやり……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちんっと風船が弾ける音とともに、さあああっと湿った冷気が降ってきた。\n
外を歩いて帰ってきて、汗ばんだ体には気持ちいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風船の中に、冷気が閉じ込めてあったのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（こんなことをする犯人は……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きょろきょろ、とエントランスの中を見渡す。"


show bor_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0471
Boris "「ああ、お帰り、[firstname]。\n
……ねえねえ、それどう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（やっぱり）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "犯人はボリスだった。\n
どうやら新しいマジックアイテムを試していたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（いや、犯人なんて言っちゃ悪いわね。\n
こんな試みなら大歓迎）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「涼しくって、いい気持ちだわ。\n
シャボン玉なの？」"

hide bor_m_02_3
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice bor_g0472
Boris "「精製水に、粘度を足すためにグルーン溶液を混ぜてある、特製のシャボン玉だよ。グルーン溶液は気化が早いから、すぐに乾くだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「そうね……。\n
はじけた瞬間はひんやりして濡れたように感じるけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「……ああ、本当だわ。\n
もう乾いている」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "弾けたシャボン玉の直撃を受けたはずの指先を擦りあわせてみるが、ちっともべたついたような感触はない。\n
さらさらと乾いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「へえ、面白いわね。\n
夏場、涼しくていいかも」"

hide bor_m_01_10
show bor_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_g0473
Boris "「最近、暑い日が続いていただろ？\n
それで、何か涼しくて面白いものを作ってみようかなって思ったわけ」"

hide bor_m_03_4
show bor_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_g0474
Boris "「あんたが気に入ってくれたならよかったよ。\n
あ、一緒に作ってみる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「え？」"

menu:
    "私にも作れるの？":
        jump gakuen_boris_end2a
    "見ているだけで充分。":
        jump gakuen_boris_end2b
label gakuen_boris_end2a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「私にも作れるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（作れるのなら、試してみたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふわふわとエントランスに漂うシャボン玉は、色とりどり。\n
とても綺麗だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "通常のシャボン玉を膨らませるようにして、作れるのだろうか。"

hide bor_m_01_5
show bor_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0475
Boris "「簡単だよ。\n
溶液と、枠は作ってあるから、後は普通のシャボン玉と一緒だ」"

hide bor_m_02_6
show bor_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0476
Boris "「このわっかの部分を溶液にひたして、後は振るだけ。\n
……ほら」"

play sound se_0551
pause 1
play sound se_0068 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスが目の前で実践して見せてくれる。\n
ぷわわわんっと、緑色のシャボン玉が生まれた。"

play sound se_0738 volume .3
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふわんと、それもまたエントランスに漂う風船の中へと加わっていく。"

jump gakuen_boris_end3
label gakuen_boris_end2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……いえ、見ているだけで充分だわ。\n
私には、難しそうだもの」"

hide bor_m_02_7
show bor_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice bor_g0477
Boris "「そんなことないぜ？\n
このわっかの部分を溶液にひたして……、ほら」"

play sound se_0551
pause 1
play sound se_0068 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぶんっとボリスがわっかから繋がった柄の部分を握って腕を振ると、ぷわわわんっと大きなシャボン玉が生まれた。"

play sound se_0785 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きらきらと輝きながら、そのシャボン玉もエントランスを漂うシャボン玉の中に加わる。"

jump gakuen_boris_end3
label gakuen_boris_end3:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……面白そう）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「この枠にも、何か魔法がかかっているのよね？\n
そうじゃなきゃ、中に冷気を閉じ込めたりできないもの」"

hide bor_m_02_7
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice bor_g0478
Boris "「そうそう。\n
そのわっか自体に弱冷気の魔法をかけてあるから、自然と中に閉じ込められる空気が冷たくなるんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスが差し出してくれた、溶液の入った皿と、その枠とを受け取る。\n
ちょんちょんと溶液をつけて、ゆっくりと振った。"

play sound se_0551
pause 1
play sound se_0068 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "溶液が多すぎたのか、重たげではあるものの、ゆっくりとそのシャボン玉も浮かび上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "通常のシャボン玉と違って、地面に落ちていかないあたりにも、ボリスの工夫があるのかもしれない。"

hide bor_m_01_10
show girl_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0154
Seito "「わあ、綺麗！」"

hide girl_a1_2
show girl_a1_2 at left
with dis

show boy_a1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0036
Seito "「すっご……。\n
なんだ、これ」"


play music pierce_t_ali
hide girl_a1_2

hide boy_a1_4


show pia_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0027
Pierce "「わ！わ！何があったの！？\n
寮の中がシャボン玉でいっぱいだよ！？」"

hide pia_m_03_3
show pia_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0028
Pierce "「綺麗だね、綺麗だよ！\n
ボリス！？ボリスが作ったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エントランスの入り口のほうから、賑やかな声が聞こえた。\n
他の生徒と同じに、ピアスも帰ってきたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あんぐりと口を開けて、エントランスをただようシャボン玉を見上げている。"

hide pia_m_01_2
show pia_m_01_2 at left
with dis

show bor_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0479
Boris "「お、ピアス。\n
いいところに帰ってきたな」"

hide bor_m_01_10
show bor_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0480
Boris "「ちょっとそれ、割ってみろよ。\n
怖くないからさ」"

hide pia_m_01_2
show pia_m_02_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0029
Pierce "「う。ボ、ボリスは信用できないよっ。\n
そう言って俺をいじめるんだ！」"

hide pia_m_02_5
show pia_m_01_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0030
Pierce "「このシャボン玉も何か怖いことがあるんでしょっ！？\n
俺はもう騙されないよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……おお）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょっと感動してしまった。\n
いつもは面白いように騙されるピアスが、珍しく警戒心を働かせている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "びくびくっと後ずさって、壁に背中を貼り付けてシャボン玉から逃げている。\n
珍しく、賢い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（でも……、やっぱり馬鹿だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな反応をしてしまったら、余計にボリスが面白がるということについては学んでいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "案の定、ちらりと見やったボリスは、楽しくて仕方がないといった笑みを浮べていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "獲物をロックオンした猫の顔。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後はボリスが満足するまで、ピアスは面白おかしく遊ばれるに違いない。\n
そんな未来がやすやすと想像できてしまう。"

hide pia_m_01_7

hide bor_m_02_2


show boy_b1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0068
Seito "「……うお！？\n
なんだこりゃ、風船？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょうど、帰寮の時間に合ったのか。\n
続いて帰ってきた生徒が、エントランスの光景に驚いたように声を上げた。"

hide boy_b1_4
show boy_b1_4 at left
with dis

show girl_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0155
Seito "「綺麗ね……！\n
ふふ、本物の遊園地みたいだわ」"

hide boy_b1_4
show boy_b1_4 at left_center
hide girl_a1_2
show girl_a1_2 at center
with dis

show boy_a1_4 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0037
Seito "「これ……、何で出来ているんだ？\n
って、おわ！？」"

play sound se_0006
play sound se_0722
$ flash_light_blue(.2)
pause .2
play sound se_0771
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰かが、うっかりシャボン玉に触れてしまったのだろう。\n
ぱちんと弾けて、冷気が散る音が聞こえた。"

hide boy_b1_4
show boy_b1_2 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0069
Seito "「おおおおっ！\n
涼しくていい感じだな！！」"

hide girl_a1_2

hide boy_a1_4

hide boy_b1_2


show bor_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0481
Boris "「だろだろ～？\n
ほら、ピアス、全然怖くないだろ？」"

hide bor_m_02_1
show bor_m_02_1 at left
with dis

show pia_m_01_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0031
Pierce "「ほ……、本当に？本当に安全なの？？？\n
怖くない？痛くない？」"

play sound se_0006
play sound se_0722
$ flash_light_blue(.2)
pause .2
play sound se_0771
hide bor_m_02_1

hide pia_m_01_1


show girl_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0156
Seito "「わあ……！！\n
涼しくって気持ちいい～！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスが怯えた様子でボリスに確かめている間にも、他の生徒達は涼を求めてシャボン玉を割っていく。"

hide girl_a1_2


show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0482
Boris "「自分の目で見てみろよ。\n
誰も痛がったり怖がったりしてないだろ？」"

hide bor_m_01_10
show bor_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0483
Boris "「平気だよ。\n
見ての通り、な？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういいながらも、ボリスの尻尾はゆっらゆっらと獲物を狙うリズムで揺れている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……何を仕掛けているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シャボン玉には様々な色があるものの、色によって効果が違うということもなさそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次第に増える生徒達も、皆好きにシャボン玉を割っては涼を楽しんでいる。"

hide bor_m_02_9
show bor_m_02_9 at left
with dis

show pia_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0032
Pierce "「……そ、それじゃあ、俺も試してみるよ！\n
黄色のシャボン玉がいいな、黄色はチーズの色だからね！」"

hide bor_m_02_9
show bor_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0484
Boris "「うんうん、試してみろよ。\n
大丈夫だって……、ハズレをひかない限りは」"

hide bor_m_02_2

hide pia_m_03_11


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0033
Pierce "{size=+20}「え？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その瞬間、私はボリスの口がにんまりと意地悪な笑みを浮べるのを見た。"

play sound se_0006
play sound se_0722
$ flash_indigo(.2)
pause .3
play sound se_0109
$ flash_medium_blue(.1)
$ flash_indigo(.1)
$ flash_sky_blue(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0034
Pierce "{size=+20}「ぴい！？」{/size} "


play music gag4_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0485
Boris "「やっぱりな！！！\n
おまえなら黄色を選ぶと思って、黄色だけ多めに水風船を仕込んでおいたんだ！！」"


scene bg_par20_re_bu
with dis

show pia_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0035
Pierce "「ひ、酷いよ！！！\n
危なくもないし怖くもないし、痛くもないって言ったじゃないか！！」"

hide pia_m_02_5
show pia_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0036
Pierce "「ボリスの嘘つき！！！\n
嘘つき猫！いつもいつも、猫だからって酷すぎる！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「ピアス、ピアス」"

hide pia_m_01_8
show pia_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice pie_g0037
Pierce "「見てよ、[firstname]！！\n
ボリスったら嘘つきなんだよ、酷いよね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ピアス。\n
ボリスは、嘘はついていないわ」"

hide pia_m_01_4
show pia_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pie_g0038
Pierce "「え？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、大騒ぎするピアスへと、子供に言い聞かせるように諭した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「嘘はついていないわよ。\n
痛くないし、怖くないし、危なくもないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際、ピアスは文字通り濡れネズミになっただけだ。\n
痛めつけてもいないし、危ない目にあわせたわけでもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怖がらせはしたかもしれないが……、いや、それもあえていうならば、驚かせたぐらいだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ただの納涼グッズでしょう？\n
そんなにムキになって怒らないで……」"

hide pia_m_03_12
show pia_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pie_g0039
Pierce "「怒っているんじゃなくて脅えているんだよ！」"

hide pia_m_01_1
show pia_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pie_g0039_5
Pierce "「うう、[firstname]、ボリスと付き合うようになってから意地悪になったっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「そんなことないわよ。\n
私は、元からこうだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "元から、合理的だし、現実主義。\n
ただ、ボリスと付き合うようになってから……、いろんなことを楽しみ始めたかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（まあ、別にピアスを苛めるのが楽しいっていうわけじゃないけど）"

hide pia_m_01_4
show pia_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_6")
voice pie_g0040
Pierce "「[firstname]、君までが俺を苛めるなんて酷いよ……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「いや、苛めては……」"

hide pia_m_03_13
show pia_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice pie_g0041
Pierce "「いいや、苛めてるよ！\n
俺の安住の地はどこに行っちゃったの！？」"

hide pia_m_01_9
show pia_m_01_9 at left
with dis

show bor_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice bor_g0486
Boris "「ないんじゃないか？\n
ネズミに安住の地なんて」"

hide pia_m_01_9
show pia_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice pie_g0042
Pierce "「ネ、ネズミにだって安らかに暮らす権利ぐらいあるよ！！\n
あるよね！？」"

hide bor_m_03_4

hide pia_m_02_8


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……さあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんでも、ピアスは元々は帽子屋寮にいたらしい。だが、あんまりにも双子に苛められたもので逃げ出し、遊園地寮に移住したのだそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（赤薔薇寮……、はビバルディが許すわけがないわよねえ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディは、ピアスを毛嫌いしている。\n
なんでも、ネズミが耐え難いほどに苦手なのだそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアス自体はネズミではない（ということになっている。限りなくネズミっぽい魔法生物である可能性はある）が、そのお友達は大量のネズミだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "極度の潔癖症であるペーターも、受け入れは不可だろう。\n
ともなると、残りは塔しかないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……{size=+20}ユリウスがヒステリーを起こしそうね{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生真面目、規律を重んじるユリウスと、本能の赴くままに生きるピアス。\n
きっと……、間違いなく、相性はよろしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスにとっては安住の地になりうるかもしれないが、ユリウスが耐えられなくなりそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ピアス、残念だけど……。\n
諦めたほうがいいんじゃないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼に残された選択肢は、帽子屋寮か遊園地寮かの二択だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（それなら、こっちのほうがいいと思うんだけどなあ）"


play music school_front_day_p_wam

scene bg_par20_re_bu
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「住めば都。\n
ここが一番いいわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_12")
T "「家みたいに感じられるでしょう？」"


show pia_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_12")
voice pie_g0043
Pierce "「ええ～？\n
でも、猫のいるおうちだなんて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「いい寮だと思うけど？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう思ってしまうのは、私自身がすっかりこの遊園地寮に馴染んでしまったからだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今更、他の寮に移動することなんて、想像も出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "時々ゴーランドの破壊的な音楽が披露され、ボリスの開発したマジックアイテムが暴発したり、ピアスがうるさく騒いだりしたとしても。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここが、私にとっての「おうち」だ。"

hide pia_m_03_8
show pia_m_03_8 at left
with dis

show boy_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0038
Seito "「はは、ピアス、おまえ又ボリスにはめられたのか。\n
ばっかだな～」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呻くピアスに馬鹿にしたように声をかける男子生徒。\n
彼は、ピンク色のシャボン玉へと手を伸ばした。"

play sound se_0006
play sound se_0722
$ flash_indigo(.2)
hide pia_m_03_8

hide boy_a1_2


scene bg06_sk_h_day
with dis
play sound se_0109
$ flash_medium_blue(.1)
$ flash_indigo(.1)
$ flash_sky_blue(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0039
Seito "{size=+20}「わああああ！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Pierce "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「……っぷ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice pie_g0044
Pierce "「……っふ。\n
はは、引っ掛かってる！俺とおんなじだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice hos_g0040
Seito "「な、なんでだよ、ボリス！！\n
水風船は黄色だけじゃなかったのか！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice bor_g0487
Boris "「にゃはははは、何言っているんだよ。\n
言っただろ、黄色に{size=+20}多めに{/size}仕込んであるって」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつのまにか帰宅した生徒で賑やかになっていたエントランスに、動揺が走る。\n
皆、危険なのは黄色だけだと思っていたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0157
Seito "「こ、こっちのオレンジは大丈夫なのかしら。\n
……うう、ドキドキするっ」"

play sound se_0006
play sound se_0722
$ flash_blue(.2)
pause .2
play sound se_0771
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0158
Seito "「ああよかった～。\n
これは当たりだわ、気持ちいい～」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0070
Seito "「お、俺だって挑戦するぞ！\n
俺はこっちの緑だ！」"

play sound se_0006
play sound se_0722
$ flash_indigo(.2)
pause .3
play sound se_0109
$ flash_medium_blue(.1)
$ flash_indigo(.1)
$ flash_sky_blue(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0071
Seito "「わああ！！？\n
く、くそ～、濡れた～！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲から賑やかな声が響きあう。\n
ボリスめ、なんて愚痴めいた声が聞こえたりもするものの、皆楽しそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんといったって、懲りてやめようとする生徒がいない。水風船を引き当てた生徒も、次こそはとまた新しいシャボン玉へと手を伸ばしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当たり外れがあっても、どちらも納涼グッズ。\n
弾ける怖さも、涼やかさに変わる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（……グルーン溶液っていうのがいいわよね）"

play sound se_0551
pause 1
play sound se_0068 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふよんっと新しいシャボン玉を追加しながら、思った。\n
濡れた直後こそはびしょ濡れになるものの、普通の水よりも気化する速度が早い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グルーン溶液を使っているおかげで、すぐに制服が乾く。\n
いつまでも濡れっぱなしということにならないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐに、また、次のシャボン玉に挑戦したくなる。"

play sound se_0449

scene bg_par20_re_bu
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱたん、と軽く腰のあたりを叩かれる感触に振り返った。\n
ボリスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「な、なあに？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（？\n
い、嫌な予感が）"


show bor_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice bor_g0488
Boris "「ふふ、あんたも涼みたいだろ？\n
作るばかりじゃ、涼めてないだろうし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にやーっと口角を吊り上げたボリスが、私の頭上へとぽんっとシャボン玉を放つ。"

play sound se_0068 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「ボ、ボリス！！！\n
怒るわよ！！？」"

hide bor_m_03_2
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice bor_g0489
Boris "「大丈夫大丈夫、すぐに乾くから。\n
ね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ね、じゃないわよ！！！！」"

play sound se_0468
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慌ててそのシャボン玉の下から逃げ出そうとするが、それより早く、ぱちんっとボリスが指を鳴らした。"

play sound se_0006
play sound se_0722
$ flash_indigo(.2)
pause .4
play sound se_0109
$ flash_medium_blue(.1)
$ flash_indigo(.1)
$ flash_sky_blue(.1)

play music cheerful_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それが合図だったように、シャボン玉がはじけて大量の水が私に向かって降り注ぐ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「っぶ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「あああっ、もう！！！\n
ボリス！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐに乾くと分かっていても、べしょべしょに濡れそぼるのはいい気分ではない。"

play sound se_0153
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「う～……。\n
びしゃびしゃ……」"

hide bor_m_01_10
show bor_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice bor_g0490
Boris "「にゃはははっ！\n
たまには水遊びもいいもんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……それじゃあ、{size=+20}あんたも濡れなさい！！{/size}」"

play sound se_0126
$ flash_sea_green(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスに倣って、彼の頭上にあるシャボン玉めがけ、小さな風の魔法を放つ。"

hide bor_m_02_3
show bor_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0491
Boris "「にゃはは。\n
はっずれ～！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「こっの……！！」"

play sound se_0126
$ flash_sea_green(.2)
play sound se_0126
$ flash_sea_green(.2)
pause .3
play sound se_0126
$ flash_sea_green(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは、身軽にひょいひょいと逃げ回る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのやりとりは、周囲に対しても新たな楽しみ方を示唆したらしかった。\n
こういう方法で遊ぶことも出来るのだ、と。"

hide bor_m_02_6


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までロシアンルーレット的に楽しんでいた生徒達が、互いの頭上にあるシャボン玉を割りあう。\n
そして、阿鼻叫喚の場が出現した。"

play sound se_0126
$ flash_sea_green(.2)
play sound se_0006
play sound se_0722
$ flash_indigo(.2)
pause .3
play sound se_0109
$ flash_medium_blue(.1)
$ flash_indigo(.1)
$ flash_sky_blue(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0072
Seito "「わああ！？」"

play sound se_0006
play sound se_0722
$ flash_indigo(.2)
pause .3
play sound se_0109
$ flash_medium_blue(.1)
$ flash_indigo(.1)
$ flash_sky_blue(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0036
Seito "「きゃああああ！？\n
よ、よくもやったわね！！！？」"

play sound se_0006
play sound se_0722
$ flash_blue(.2)
pause .2
play sound se_0771
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0037
Seito "「せ、セ～フ！！\n
危なかったわ！！！」"

play sound se_0006
play sound se_0722
$ flash_indigo(.2)
pause .3
play sound se_0109
$ flash_medium_blue(.1)
$ flash_indigo(.1)
$ flash_sky_blue(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0073
Seito "「うお、冷て……！！？\n
誰だよ、今の！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちんぱちん、とシャボン玉の割れる音が響いては、生徒達の悲鳴、歓声があがる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "室内で水遊びなんて、もってのほか。\n
しかし、これだけ大騒ぎをしても、使用人達が駆けつけてこないあたり、前もって許可をとっているのかもしれない。"


scene bg_par20_re_bu
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（皆、楽しそう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスに仕返しするべく追いかけていたのも忘れて、その光景に見入ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆が楽しくて、私も楽しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（いつのまにか、本当に「家」になったんだなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "感慨深い。\n
不思議な気分だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん、私の家は別にある。\n
だが、ここも「家」だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "家族ではないものの、同様に過ごす友人がいて……、恋人もいる。"


show bor_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0492
Boris "「……あ、そこのあんた！\n
そうそう、あんただよ、あんた」"

hide bor_m_03_10
show bor_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0493
Boris "「これ使ったら、どんどんシャボン玉作れるからさ。\n
皆で楽しんでよ」"

hide bor_m_03_10
show bor_m_03_10 at left
with dis

show boy_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0074
Seito "「え？\n
いいのか、ボリス？」"

hide bor_m_03_10
show bor_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0494
Boris "「いいんだよ、ほら。\n
楽しめよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは自分の持っていた分を、たまたま通りすがった男子生徒へと押し付ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、続いて、私が持っていた分も取り上げてしまう。\n
これまた同じように、別の生徒へと押し付けてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「？\n
ボリス？」"

hide bor_m_02_4
show bor_m_01_13 at center
with dis
hide boy_b1_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0495
Boris "「いいから、こっちこっち」"

hide bor_m_01_13

play sound se_0312
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手を引かれて、するりと二人でエントランスを抜け出した。"

with dis
$ hi_mes()


scene bg_par20_re_bu with Dissolve(.8)

scene bg25_rr_day
with stripe_l_long

play music residence_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大騒ぎになっているエントランス。\n
二人こっそり抜け出して、ボリスが私を連れていったのは、男女共同区域の中にある談話室だった。"


scene bg19_lg_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ティーテーブルと、いくつかのソファやカウチ以外は何も置かれていない。\n
純粋に会話を楽しむための部屋、といった感じだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段ならば常に誰かしらがいるはずなのだが、今は皆エントランスの騒ぎに出払っているのか、私達の他に人の気配はない。"

play sound se_0399
pause 1
play sound se_0450
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは、それを確認すると談話室のドアを閉め、ついでにがちゃりと鍵をかけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「…………。\n
……ボリス？」"


show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice bor_g0496
Boris "「これで、あんたと二人っきりになれた。\n
……うまくいってよかったよ」"

hide bor_m_01_10
show bor_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice bor_g0497
Boris "「これでここに誰か残っていたなら、叩き出すところだ。\n
お祭り好きの寮だから、そうはならないと思ってたけどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……まさか、そのためのマジックアイテムだったの？」"

hide bor_m_02_4
show bor_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0498
Boris "「暑いから涼みたかったってのも本当だよ？\n
副産物として……、そっちに皆が引き付けられるっていう効果もある」"

play sound se_0551
pause 1
play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりとボリスの腕が私の腰へとかかる。\n
引き寄せられそうになって、私は慌てて腕を突っ張った。"

hide bor_m_02_9
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0499
Boris "「？\n
どうかした？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「誰かさんのせいで、びしょ濡れなのよっ。\n
あなたまで濡れるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくらグルーン溶液がすぐに乾くとはいっても、まだ完全には乾いていない。"

hide bor_m_01_11
show bor_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0500
Boris "「構わないよ。\n
どうせ、すぐ乾くし……、あんたと一緒なら濡れてもいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「あっ」"


show m_bor_end1 onlayer master
with dis
hide bor_m_01_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっぽりと、ボリスの腕の中に閉じ込められてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "濡れた布地が、体に張り付く感じが不快だ。\n
だが、その分より強くボリスの体温を感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人分の体温が濡れたシャツに馴染んでいく。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0501
Boris "「……はあ、学生恋愛って、面倒だよな。\n
あんたは人に見られるの嫌がるし」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「当たり前よ。\n
露出趣味はないんだから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これは、付き合い始めの頃にも思ったこと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学園という公共の場に生活する寮生の場合、意外に思ってしまうほどに二人きりになれる場所というのは少ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "互いの部屋への行き来が禁じられている分、なおさらだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前に一度、空き教室でいい雰囲気になったことがある。\n
……忘れ物を取りに来たのだという女子生徒に乱入されて、とても気まずかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ベタなタイミングで、ベタな邪魔が入る。\n
立て続けにそういうことがあって以来、私は触れようとするボリスを拒否し続けていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教室だと誰が来るか分からないし、寮内の空き部屋でも同じ。\n
いつ、使用人が顔を出すか分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……それに焦れて、今回のシャボン玉作戦ってこと？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賑やかなイベントを引き起こし、衆目を集めることで死角を作った。\n
今この空間は、完全なるエアーポケットだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通なら、鍵をかけてはいけないような、共同利用の場。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この部屋に誰かが足を踏み入れるには、まず鍵を開けなくてはいけない。\n
時間稼ぎには充分だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0502
Boris "「最近、ろくなスキンシップをとれなかったから……、寂しかったよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……前に、自分から距離をあけたこともあるくせに」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice bor_g0503
Boris "「そ、それ……。\n
時効にしてくれよ、あのときは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_2")
voice bor_g0504
Boris "「……ね、キスしてもいい？\n
あんたに触れたいんだ」"

hide m_bor_end1
show m_bor_end2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「ねえ……、今、あなた……。\n
いい、って言うより先に、しなかった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "質問しておきながら、答えを必要としないのはボリスの常だ。\n
まるで、でたらめな、なぞなぞ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0505
Boris "「ふふ、あんたのことなら何でも分かるんだよ。\n
だから、先回り」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……じゃあ、質問する必要もないじゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice bor_g0506
Boris "「そうだね。\n
……聞いたりする必要もない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちゅ、と触れるだけのキスが鼻先に落ちる。\n
しばらく戯れるように何度も触れるだけのキスが繰り返される。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（……好きだなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じゃれるように触れ合う唇から、気持ちが伝わるような気がする。\n
まだまだ大人ではない私達の、児戯めいたキスだ。"


play music quiet_a_wam
hide m_bor_end2
show m_bor_end3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Boris "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Boris "「……[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "子供でもなく、大人でもない。もどかしいくらいに甘酸っぱくもなれば、大人には難しいような大胆さを見せることもあって、簡単に境界を越えたりする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「……ボリス」"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅっとボリスの背に腕を回す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなにしっかりと抱き合っているから、私の纏っていた水気はボリスにも伝わっただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐ乾くはずが、じっとりとした熱気はおさまる気配がない。"

hide m_bor_end3
show m_bor_end4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……ね、どれくらいもつと思う？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唇を触れ合わせた距離のままに、囁いた。\n
耳をすませば、未だエントランスからは賑やかな歓声が響いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この調子なら、夕食くらいまで時間を稼ぐことが出来るだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0507
Boris "「……持つよ。\n
邪魔する奴は……、猫がひっかく」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「ふふ、馬に蹴られるんじゃなくって？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice bor_g0508
Boris "「馬なんか呼ぶより、猫がひっかいたほうが確実だよ。\n
俺の邪魔するやつは、俺が許さない」"

play sound se_0250
hide m_bor_end4
show m_bor_end5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "強気に囁いたボリスにそっと導かれて、カウチへと押し倒された。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「っ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice bor_g0509
Boris "「……ん？\n
ぶつけた？痛かった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……ううん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校内の片隅、人目を盗んでの逢瀬なんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……ベタベタだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_9")
voice bor_g0510
Boris "「……好きだよ、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「私も、大好きよ。\n
ボリス」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かつて告げられなかった言葉を、すんなりと私は口にする。\n
見上げるボリスの唇が嬉しそうに緩んで、キスが降る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（……見つかったらマズイって、分かっているのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、ボリスを拒絶することが出来ない。\n
理性で歯止めがかけられないなんて、まるで動物だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（動物で、いいのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ、私達はまだまだ若い。\n
理性よりも、本能の勝ってしまうお年頃なのだ。"



hide frame_gen_togaki
hide ali_m_06_16
with Dissolve(2)
hide m_bor_end5
show white onlayer master
with compress_extralong
hide white
with compress_extraextralong
pause 1
stop music
##endmemory
jump gakuen_a
