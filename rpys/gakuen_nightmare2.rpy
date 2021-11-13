label gakuen_nightmare2:
scene bg_map_day
with dis
$ clockanim()


scene bg27_rk_day
with dis

play music classroom_day_p_wam

scene bg01_cr_day with Dissolve(1.2)
play sound se_0497
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつものように登校し、いつものようにホームルームを受けていたところ、担任であるゴーランドが爆弾発言を落とした。"


show go_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0333
Gowland "「んじゃ今から身体測定を始めるからな。\n
カードを受け取ったら各自、塔に移動するようにー！」"

hide go_m_01_2
show go_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0334
Gowland "「身体測定が終わったら各自解散なー？\n
今日は授業ないから気をつけろよ～」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……{size=+20}え？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "初耳だ。\n
身体測定があるというのも初耳ならば、それが今日だというのも初耳。"

hide go_m_01_2
show go_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0335
Gowland "「お？どうした、[firstname]。\n
そんなびっくりした顔して」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「き、昨日、そんなこと言っていなかったわよね！？」"

hide go_m_02_4
show go_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice gor_g0336
Gowland "「あー……。\n
言ってなかったっけか？」"

hide go_m_03_3
show go_m_03_3 at left
with dis

show bor_m_02_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0540
Boris "「言ってねえよ。\n
忘れてたな、おっさん」"

hide go_m_03_3
show bor_m_02_8 at left
with dis
hide bor_m_02_8
show pia_m_03_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice pie_g0269
Pierce "「身体測定って身長とか測るやつだよね！\n
俺、身長伸びているかな！伸びているといいな！」"

hide bor_m_02_8

hide pia_m_03_5


show girl_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice mat_g0054
Seito "「ふふ……。\n
身長だけじゃないのよ？」"



hide girl_a1_3
show girl_a1_3 at left
with dis

show girl_b2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice nos_g0100
Seito "「ふふふ、そうそう。\n
身長だけじゃないの、もっと深刻なのは体重よ……」"

hide girl_a1_3
show girl_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice mat_g0055
Seito "「ええ、そっちが増えていたら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無邪気に、己の成長っぷりを気にしているピアス。わくわくと瞳を輝かせる彼とは反対に、女子生徒達の瞳はどんよりと暗く澱んでいく。"

hide girl_a1_1
show girl_a1_1 at left_center
hide girl_b2_1
show girl_b2_1 at center
with dis

show bor_m_02_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0541
Boris "「お～い、おまえら怖いぜ～？そんなに嫌なもんなの？\n
女の子って、ちょっとぽっちゃりしているほうが……」"

play sound se_0582 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「ボリス、それ以上言ったら口の中に椅子をねじ込むわよ」"

hide bor_m_02_2
show bor_m_01_4 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice bor_g0542
Boris "「椅子！？」"

hide girl_a1_1
show girl_a2_9 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice mat_g0056
Seito "「チョークでもいいけど？」"

play sound se_0184
hide bor_m_01_4
show bor_m_01_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
Boris "「～～～！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスがガタッっと竦みあがった。\n
教室にいる女子全員の、怨嗟のこもった視線にゴーランドもたじたじとなる。"

hide girl_a2_9

hide girl_b2_1
show girl_b2_1 at left_center
hide bor_m_01_3
show bor_m_01_3 at center
with dis

show go_m_03_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0337
Gowland "「だ、大丈夫だって！俺のクラスの女子は皆美人と可愛い子揃いだからな！\n
体重なんて……、なあ、ボリス！？」"

hide bor_m_01_3
show bor_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0543
Boris "「ああ、そうだね！！\n
そうそう、何も心配することなんてないよ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

hide girl_b2_1

hide bor_m_03_11
show bor_m_03_11 at left_center
hide go_m_03_3
show go_m_03_3 at center
with dis

show girl_a2_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
Seito "「…………」"

hide bor_m_03_11

hide go_m_03_3
show go_m_03_3 at left_center
hide girl_a2_1
show girl_a2_1 at center
with dis

show girl_b1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
Seito "「…………」"

hide girl_b1_5
show girl_b1_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice nos_g0101
Seito "「……前日に教えておいてくれれば、食事抜いておいたのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子生徒全員の、冷えた視線がゴーランドを襲う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "凍てつく冷気にも襲われ（実際に誰かが魔法で冷気を起こしていた）、最終的にゴーランドは開き直ることにしたらしい。"

hide go_m_03_3
show go_m_01_9 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0338
Gowland "「前日に言おうが当日に言おうが、変わんねえだろー？\n
っつうか、そういうふうに食事抜くとか無茶しだすから、抜き打ちなんだよ……」"

hide girl_a2_1
show girl_a2_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0057
Seito "「……食事抜かなくたって、運動するとか色々あるでしょー！？」"

hide girl_b1_1
show girl_b1_9 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0102
Seito "「……そうよ、そうよ！\n
魔法使いまくるとかー！」"

hide girl_a2_7
show girl_a2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0058
Seito "「そうすれば、大分カロリー消費になったのに！\n
事前連絡なしなんて、ゴーランド先生、酷い！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……せめて一週間は前に告知してほしかったわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだけあれば、体重はおおいに変動する。"

hide go_m_01_9
show go_m_03_11 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0339
Gowland "「変えてどうすんだよ……。\n
いつもの値を計らなきゃ、診断にならないだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの言うことは、いちいちもっともだ。\n
だが、正しいことが納得できることかというと話は別。"

hide go_m_03_11
show go_m_01_13 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0340
Gowland "「大体、おまえらに事前に告知しとくとろくなことがねえ……。\n
魔法で外見を変えちまったり、風船みたいに体重を軽くしたり……」"

hide go_m_01_13
show go_m_01_9 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0341
Gowland "「……しないって、保証できるか？\n
毎回、絶対にそういう奴が出てくるんだよ……」"


show bor_m_03_11 at right
with dis
hide go_m_01_9
show go_m_01_9 at left
with dis
hide girl_a2_5

hide girl_b1_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0544
Boris "「おっさん、よしとけよ。\n
今の女子に何言っても無駄だから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正論も通じない、と。\n
とりあえず進めようと、健康診断のカードが配られ始めた。"

hide bor_m_03_11

hide go_m_01_9
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg01_cr_day with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg_par15_rg_tow_day
with stripe_l_long

play music school_front_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子はひとしきり不満を漏らしたが、カードを配られた以上はどうしようもない。\n
身体測定に参加するために塔を訪れた。"


scene bg25_rr_day with stripe_l_medlong
play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒の義務だ。\n
測定からは逃げられない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……シンフォニアでの身体測定か。\n
初めてだと、なんでも珍しくて新鮮だな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くるり、と手の中にある身体測定用のカードを回してみる。\n
サイズとしては葉書より一回り大きいくらいだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "材質は学生証によく似ているものの、それよりももう少し薄い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その表面には、身長や体重などなど、今回の身体測定で分かった情報を反映させるための空欄が用意されている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「測定がすんだ後の数字を、誰かが読み上げたりはしないのね？」"


show girl_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice mat_g0059
Seito "「ないない。\n
そんなことされたら、雷を落とす子が出るわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆が皆、優秀な魔法使いの卵だけあって、なんでもありだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……でも、これだけの名門校の生徒でも、体重とか気にするんだ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中身は普通。\n
親近感がわく。"

hide girl_a2_3
show girl_a2_3 at left
with dis

show girl_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0103
Seito "「え？\n
まさか、他の学校では読み上げたりするの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……するわね。\n
もちろん記述を担当している人にしか聞こえないような小声でなんだけれど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「自分のすぐ後ろの人ぐらいには聞こえるんじゃないかしら。\n
ま、女子と男子は完全に別だから聞こえたとしても女子だけにだけど」"

hide girl_a2_3
show girl_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice mat_g0060
Seito "「ふうん、それでも嫌っていうか、恥ずかしいなあ……」"

hide girl_a2_9
show girl_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice mat_g0061
Seito "「……あれ？測定するのが保健の先生だとしたら記述は誰がやるの？\n
生徒にやらせたりはしないわよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……保健委員の生徒がやることもあったわ。\n
けれど基本的には、担任ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の語る他校の身体測定事情に、周囲のクラスメイトは難しそうな顔になる。\n
担任という言葉から、ゴーランドを思い浮かべたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（そういう習慣がないからか、反発がすごそうね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は一般校にいたせいで、シンフォニアにしかいたことのない彼女達とは常識も異なる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「担任が男性の場合、保健委員の仕事になるの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの名誉のためにいうならば、ゴーランドだから嫌だというのでなく、男の人に知られるのが嫌なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "太っていない子でも体重を知られるのは、なんとなく嫌がるもの。そう考えると、この身体測定カードの提出先である学校医のナイトメアも男性だから……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（皆は、それは嫌じゃないのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ねえ、ナイトメアはいいの？\n
ナイトメアだって、男の先生よ？」"

hide girl_a2_5
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice mat_g0062
Seito "「…………。\n
……そう、よね」"

hide girl_b1_4
show girl_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice nos_g0104
Seito "「……言われてみれば、男よね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌がられてしまったゴーランドとは正反対の意味で哀れかもしれない。\n
ここまで男であることを意識されていないというのは、どうなのだろう。"

hide girl_a2_1
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0063
Seito "「[firstname]、あなたはどうなの？\n
嫌？それとも気にならない？」"

menu:
    "嫌だ。":
        jump gakuen_nightmare2_2a
    "気にならない。":
        jump gakuen_nightmare2_2b
label gakuen_nightmare2_2a:
$ lovechara_nightmare_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……私は、嫌だなあ。\n
女性のほうが気楽」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "年頃ゆえの潔癖さか。\n
たとえ相手がナイトメアでも、嫌だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……だって、あの人だって一応、男の人なんだし）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よくいえば、男性として意識しているということだろうか。"

jump gakuen_nightmare2_3
label gakuen_nightmare2_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「そうね。\n
ナイトメアなら気にならないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教師だからという理由以上に、ナイトメアは男として意識しづらい部分があると思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "病弱で頼りなかったり、仕事から逃亡していたりと、日頃の行いが行いだからだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（気にならない……、わよね？）"

jump gakuen_nightmare2_3
label gakuen_nightmare2_3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返事自体はほとんど考える間も挟まずに返したものの、その後考え込んでしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……一般校とは、皆ちょっと感覚が違うのよね。\n
他にも、違いはあるのかしら）"

hide girl_a2_3
show girl_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice mat_g0064
Seito "「さあ、さっさと終わらせてしまいましょう。\n
こうしていても、体重は減らないし」"

hide girl_b1_9
show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice nos_g0105
Seito "「ええ、そうね！\n
ほら、行きましょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「ええ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たかが身体測定。\n
しかし、シンフォニアでの……と考えると構えてしまう。"

hide girl_a2_5

hide girl_b1_2
##[chara4 PAY ATTENTION="false"]
with dis
$ hi_mes()


scene bg25_rr_day with Dissolve(.8)

scene bg_par16_rs_tow_day
with stripe_l_long

play music drawingroom_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア流身体測定というのは、やはり私が今まで受けてきたものとは違っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "身長や体重といった基本的なものはもちろん、日ごろの魔力量や、魔法を使う際の生成量が適正であるかどうかなどのチェックが入る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校内で何かトラブルがあって医務室に運び込まれた際に、こういった基礎情報があれば、スムーズに手当てをすることが出来るのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その測定の仕方も、いかにもシンフォニア流といったものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「次が魔力測定なんだけど……。\n
自分の持っている魔力量なんて、どうやって測るの？」"


show girl_a1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice mat_g0065
Seito "「え？\n
今までに測ったことなかったの？」"

hide girl_a1_4
show girl_a1_4 at left
##[rchara4 PAY ATTENTION="false"]
show girl_b2_5 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nos_g0106
Seito "「自分の魔力量が分からないと、魔法を使うときに危険じゃない？\n
どうやって判断するの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達は、私の問いに驚いたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「えっと、指示魔法っていう比較的暴走しにくい、安全な魔法があってね？\n
それが各レベルで設定されているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「で、その魔法を発動させることができたら、そのレベルの魔法を使いこなすだけの魔力があるというふうに判断するの」"

hide girl_a1_4
show girl_a1_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice mat_g0066
Seito "「ああ、魔法をレベルで分類して管理しているのね？\n
でも、それだと、魔法との相性によっては魔力酔いを起こしてしまいそう」"

hide girl_b2_5
show girl_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice nos_g0107
Seito "「シンフォニアでは、もっと具体的にどれくらいの魔法まで使いこなせるかということや、魔法との相性まで調べてくれるわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「へえ、便利ね」"

hide girl_a1_9
show girl_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice mat_g0067
Seito "「もちろん、練習や成長によって魔法使いとしての技術や保有魔力も多少変わるけど、相性はそうそう変わらないから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「ふむふむ……。\n
一般校でも導入できたらいいのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（でも、実際に導入されていないってことは難しいんだろうな。\n
シンフォニアって、やっぱり特殊なのね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達は、それが当たり前であるように言っているが、魔法の適正なんて人それぞれ皆違うものを持っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを測定し、個人の持つ魔力特性を細かく判明させるなんていうのは、普通であれば手間がかかるもの。身体測定程度でできるようなものではないはずだ。"

hide girl_a1_3

hide girl_b2_2

play sound se_0397

scene bg25_rr_day with stripe_l_medlong

show girl_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0068
Seito "「それじゃあ、行くわよ」"

hide girl_a2_3
show girl_a2_3 at left
with dis

show girl_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0108
Seito "「初めてだと、ちょっと驚くかもしれないけど……。\n
別に痛くも怖くもないから、心配しないでね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……そんなふうに怯むような検査なのね？」"

hide girl_a2_3
show girl_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice mat_g0069
Seito "「新入生だとね。\n
でも、怖くないわ」"

play sound se_0745
hide girl_a2_2

hide girl_b1_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達に促されて、その魔力量を調べるための部屋へと向かう。\n
そこは普段は使われていない塔の一室だった。"

play sound se_0397

scene bg_par18_ri_tow with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の傍らに小さな机があり、そこにメイドが一人待機している。"


show maid_d_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0094
Maid "「『結晶』がとれましたら、こちらに提出してくださいね。\n
分析結果は、後ほど身体測定の結果と一緒に返却されますので」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（結晶？？？）"

hide maid_d_3
show maid_d_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice tad_g0095
Maid "「私のほうからの説明は必要でしょうか？\n
ご友人がいらっしゃるようなので、大丈夫かとは思うのですが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の表情から新入生ということを察したのか、メイドに尋ねられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ええ……、危険ではないのよね？\n
それなら彼女達に教えてもらうわ」"

hide maid_d_9
show maid_d_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tad_g0096
Maid "「はい、もちろん危険なものではありません。\n
それでは……、どうぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メイドは、入り口のドアを指し示してくれた。\n
それを押し開けて、中へと三人で足を踏み入れる。"

play sound se_0199
hide maid_d_2


show black onlayer master with stripe_l_medlong

play music view_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の中に灯りはなく、カーテンも閉め切られているのか光源が一切ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（何も見えないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真っ暗だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ねえ……。\n
こう暗いと何も見えないんだけど、どうしたら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice mat_g0070
Seito "「大丈夫よ、すぐに出てくるから」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nos_g0109
Seito "「ええ、すぐよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かを待つように、彼女達は暗闇の中で動こうとはせず入り口近くで立ち止まったままだ。\n
私もそれに倣って、おとなしく待つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、部屋の中央に気配が生まれた。"

play sound se_0724
hide black
show m_nai2_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（何だろう……、魔法植物？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たくさんの蔓が絡み合って伸びたかのような、神秘的な姿をしている。\n
が、うっすらと纏った淡い光のせいか、悪い印象はなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0071
Seito "「行きましょう。\n
あれはね、魔力測定を手伝ってくれるマジックアイテムなの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0110
Seito "「私達の血液から結晶を作ってくれるのよ。\n
その結晶の大きさや色から、魔力量やその傾向が分かるようになっているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「け、血液……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "吸血植物なのだろうかと、怯む。\n
しかし、彼女達は気にした様子もなく、すたすたとその植物に向かって歩み寄っていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「ま、待って」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（危険はないって言っていたし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "警戒はしてしまうが、それでも彼女達についていくことにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0072
Seito "「いきなりじゃ不安でしょう？\n
まずは私がやって見せるわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「あ、順番なのね。\n
……ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女は私の不安を察したのか、先に一歩前に出てくれた。\n
植物に向かって、右手を差し出す。"

play sound se_0744 volume .7
hide m_nai2_1
show m_nai2_2and2_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0073
Seito "「……っ。\n
……あ、これね、チクっとする程度だから」"


with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（指先に、ちょっとだけ血が滲んでいる？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "針で刺したように、小さく丸い血玉が彼女の指先に浮かぶ。\n
それに植物の蔦が触れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこからの反応は、とても幻想的。"

play sound se_0738
pause 1
play sound se_0785
hide m_nai2_2and2_4
show m_nai2_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "蔓の先がぷくりと膨らんで、蕾へと変わる。そしてそれはみるみるうちにほころんで、うつむき加減の百合のような花をつけた。"

play sound se_0722
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女がそっとその花の下に手を差し出すと、その花の中からころりと小さな結晶が落とされた。\n
淡い水色の澄んだ結晶だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0074
Seito "「これが、私の魔力結晶ってわけ。\n
これを分析してもらうと、私の魔力傾向や、魔力量が正確に分かるの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0075
Seito "「どう？\n
怖くも、危なくもなかったでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「うん。\n
安心した」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice mat_g0076
Seito "「次は、あなたがやってみるといいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「分かったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一歩退く彼女とは逆に、植物に向けて足を踏み出すと右手を差し出した。"

play sound se_0744 volume .7
hide m_nai2_3
show m_nai2_2and2_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほど見たのと同じように蔓が伸びてきて、私の指先に絡みつく。"
$ flash_color("red", .1)
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……っ、痛！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "針で刺すような、チクリとした痛みを指先に感じた。\n
だが、先刻教えてもらったようにたいしたものではなく、一瞬のこと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "注射などに比べても、ぜんぜん痛くない。"

play sound se_0738
pause 1
play sound se_0785
hide m_nai2_2and2_4
show m_nai2_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "蔦の先が膨らんで蕾に変わり、その蕾がするすると花開く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（あ……、先刻とは色が違う）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "形としては似たような花なのだが、私の血液に反応して咲いた花は薄い朱色をしていた。"

play sound se_0722
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "差し出した掌の上に、ぽとりと落とされた結晶も同じ色をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0077
Seito "「ふふ。\n
あなたの石、とても綺麗な色をしているわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ええ……、あなたのとは違うのね。\n
サイズは同じなのに、色には違いがあるんだ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nos_g0111
Seito "「たまたま私達の持っている魔力量が似通っているから、サイズが近いのよ。\n
まあ、同じクラスにいるぐらいなんだから、力量的には均衡しているわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ああ、確かに。\n
そう考えたら、サイズが似ているのは当然か」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "似た力量、レベルの生徒を集めてクラスを編成するのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結晶の大きさが魔力量を象徴しているのならば、クラスメイト同士の私達の結晶の大きさが近くなるのは当然のことだろう。"

play sound se_0738
pause 1
play sound se_0785
hide m_nai2_5
show m_nai2_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一歩退くと、最後に残った一人が足を踏み出し、同じように結晶化の手順を踏む。\n
彼女の結晶は緑がかった色をしていた。"

play sound se_0722
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予想通り、サイズは私達と変わらない。\n
そうして三人それぞれ結晶を手に入れると、その部屋を後にした。"

hide m_nai2_6


play music drawingroom_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……はあ」"


show girl_b2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice nos_g0112
Seito "「緊張した？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「初めてだからね。\n
でも、先に見せてくれたおかげで怖くなかったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋を出たところで、受付のメイドへと手に入れた結晶を提出する。"


show maid_d_3 at center
with dis
hide girl_b2_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0097
Maid "「はい、お疲れ様でした！\n
まだ別の検査が残っているようでしたら、そちらへどうぞ！」"

play sound se_0397
hide maid_d_3


scene bg25_rr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（あと残っているのは、どれくらいかしら……）"


show girl_a1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice mat_g0078
Seito "「……そろそろ覚悟を決めて、例の測定に赴くべきかしら」"

hide girl_a1_1
show girl_a1_1 at left
with dis

show girl_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nos_g0113
Seito "「……そうね、残っているのコレだけだものね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ああ、残りってアレだけだったのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのほとんどの欄が埋まったカード。\n
空欄は一つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "例の……、体重測定。"

hide girl_a1_1

hide girl_b2_5
##[chara4 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_par20_re
with stripe_l_long

play music entrance_p_wam
play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "渋々ながら体重を量り、記録し、塔のエントランスへと戻ってきていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「……これは、一般校とまったく変わらない測定なのに、一番気疲れしたかも」"


show girl_a2_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice mat_g0079
Seito "「息を詰めちゃうわよね……」"

hide girl_a2_1
show girl_a2_1 at left
##[rchara4 PAY ATTENTION="false"]
show girl_b1_9 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice nos_g0114
Seito "「おなかをひっこめたからって、軽くなるわけじゃないのにね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「お風呂前に体重を量ったりするときは普通に出来るのに……。\n
測定だと、妙に力が入るのはどうしてかしら……」"

hide girl_a2_1

hide girl_b1_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ともかく、これで身体測定は終了だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エントランスでは、ナイトメアがカードの回収を行っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、正確に言うと実際に回収作業をしているのはグレイで、ナイトメアはその傍らで折りたたみの椅子に座って寛いでいるだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は私を見つけると、立ち上がってこちらへとやってきた。"


play music nightmare_t_ali

show nai_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0048
Nightmare "「ああ、[firstname]、君も来ていたのか。\n
結果はどうだったのかな、私に見せてごらん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふふふと口元に笑みを浮かべて、こちらへと手を差し出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（…………）"

menu:
    "拒否する。":
        jump gakuen_nightmare2_4a
    "渡す。" :
        jump gakuen_nightmare2_4b
label gakuen_nightmare2_4a:
$ lovechara_nightmare_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（学校医だから、見せなきゃならないんだろうけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か明確な理由があるわけではない。\n
それでも、なんとなくナイトメアにこの結果を見られるのは嫌だと思ってしまった。"

hide nai_m_02_1
show nai_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0049
Nightmare "「ぬ。どうして渡そうとしないんだ。\n
私は学校医だぞ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「そ、そうだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うろうろと視線が彷徨う。\n
どうして、ナイトメアにカードを渡すのが嫌なのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……ナイトメアのことを意識しちゃっているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、身長や体重、自分の体調に関することを知られるのがこんなにも……、気恥ずかしいのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……いやいや）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……ないない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までの彼とのやりとりの、どこに意識を促す何かがあったというのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（でも……、気になっているのは確かなのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その意味合いはともかく、意識しているというのは認めざるをえない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の生徒達はと見れば、友人やクラスメイト達には見られないように気遣いながらも、ナイトメアやグレイ相手には無造作にカードを提出している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "職員や先生は、立場が違う。\n
彼らの態度こそ、正しいものなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷った末、私はつつつっとナイトメアを迂回するとグレイへとカードを差し出すことにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうせ最終的には学校医の管理管轄ということで見られてしまうのだろうが、今この場で見られるよりはだいぶマシだ。"

##[rchara2 PAY ATTENTION="false"]
show gre_m_03_1 at center
with dis
hide nai_m_01_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gray "「……[firstname]？」"

hide gre_m_03_1
show gre_m_03_1 at left
with dis

show nai_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「！？」"

hide nai_m_03_3
show nai_m_03_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0050
Nightmare "「差別だ！！！差別はよくないぞ！！？\n
どうして私では駄目で、グレイならいいんだ！！」"

hide nai_m_03_2
show nai_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0051
Nightmare "「理由を言ってみろ、理由を！！\n
ちゃんと説明してくれないと納得しないからな！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「なんで説明が必要なのよ……」"

hide nai_m_02_6
show nai_m_02_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice nig_g0052
Nightmare "「気になるだろう！？\n
そんな避けられ方をしたら！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「はあ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ナイトメアの言うことももっともだ。\n
適当な言い訳でもあげておくべきかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そうねえ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「……{size=+20}人徳？{/size}」"

hide nai_m_02_13
show nai_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
Nightmare "「！？」"

hide nai_m_03_3
show nai_m_03_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice nig_g0053
Nightmare "「私よりもグレイのほうが人徳があるというのか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「だから、そう言っているじゃない」"

hide gre_m_03_1
show gre_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice gra_g0001
Gray "「……どうも」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは少し面映そうにしている。\n
一方、納得のいっていないナイトメアは地団太を踏む。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（この反応……、子供みたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……そっか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中で何気なく呟いた言葉に、すんなりと納得がいく。\n
私はナイトメアが子供に思えたから、嫌だったのだ。"

play sound se_0526

show bg06_sk_h_day onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0054
Nightmare "「ほほ～、君見た目のわりに結構体重があるんだな。\n
私とそんなに変わらないぞっ！」"

hide bg06_sk_h_day

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（とか、いかにも言いそう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の想像に腹が立つ。\n
そうだ、だから私はナイトメアにカードを提出するのが嫌だったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（そうよ。\n
意識っていっても、そっちのほうで……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「印象ばかりはどうしようもないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう一度、彼と自分の両方に言い聞かせるように、そう言った。"

hide nai_m_03_7

hide gre_m_02_8
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()
jump gakuen_nightmare2_5
label gakuen_nightmare2_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（ナイトメアは、学校医なんだから）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくら親しくしていて、仲のいい男友達に近い感覚があるからといっても、彼は医者だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "医者である彼に、身体測定の結果を提出して、何かおかしなことがあるだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ないない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はなるべく自然に、無造作に、ナイトメアへとカードを提出した。"


show nai_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

hide nai_m_02_11
show nai_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice nig_g0055
Nightmare "「なんだ、渡すのを躊躇うから問題があるのかと思えば、ちっとも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……それ以上の感想を漏らしたら、二度と吐血の心配をしなくてもいいようにしてやるわよ」"

hide nai_m_03_11
show nai_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice nig_g0056
Nightmare "「なんだその二択の意味を持ちつつも、明らかに健康にする気はない感じの脅し文句は！！？\n
殺意が溢れるほどに滲んでいるぞ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「そりゃあ、殺意も滲むわよ。\n
いい？ナイトメア、あなたは乙女の繊細な秘密を管理する人間なの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「それに相応しいだけのデリケートさを持ち合わせないと……。\n
ただでさえ短そうな寿命を、ますます縮めることになるわよ？」"

hide nai_m_03_3
show nai_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice nig_g0057
Nightmare "「こ……、こわっ！！\n
君、目が据わっているぞ！？」"

hide nai_m_03_7
show nai_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice nig_g0058
Nightmare "「……冗談でなく、本気に聞こえる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「そう聞こえるのは、本気だからよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "更に、脅しておく。\n
余計なことを喋ったら、ただではおかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……まあ、太っているほうじゃないんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかしながら、まったく体重を気にしないほど痩せているわけでもない。"

hide nai_m_03_9
show nai_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0059
Nightmare "「……分かったよ。\n
ほら、これで身体測定は終了だ」"

hide nai_m_02_9
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()
jump gakuen_nightmare2_5
label gakuen_nightmare2_5:

scene bg_par20_re with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg06_sk_h_day
with stripe_l_long

play music daytime_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice mat_g0080
Seito "「ふう、終わったわね！\n
ねえ、[firstname]、カフェテリアでお茶していかない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice nos_g0115
Seito "「疲れたでしょう？\n
何か甘いものでも食べましょうよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そうね、測定も終わったことだし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "身体測定が終わってしまえば、もう怖いものはない。\n
多少、その後の値が変わっても……、それこそ一時的なものだ。"

with dis
$ hi_mes()

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
jump gakuen_nightmare3
