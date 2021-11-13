label gakuen_joker5:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_tow_day
with dis

play music room2_p_wam

scene bg24_rj_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一晩ゆっくりと休んだ次の日の朝。\n
私は、ふとした思い付きとともに目覚めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_14")
T "「……塔のストームにいたってことは、ジョーカーって塔の住人？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨日お風呂からの帰り道でであった男子生徒の言葉を思い出す。"


scene bg25_rr_nig_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0003
Seito "「ストームっていうのは、シンフォニアの学生寮の伝統行事で、男子寮の生徒が女子寮に侵入を試みて親睦を深めるものなんだそうです」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子寮の生徒が、女子寮に侵入を試みて、親睦を深める。"


scene bg24_rj_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どの寮の男子生徒が、どの女子寮にというところまで指定はされていないが、聞いた印象によると、同じ寮内でのイベントのように聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ということは、ジョーカー達は塔に関係する人物なのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_14")
T "（……口が悪くないほうのジョーカーは、秘密の部屋も知っていたみたいだし）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれが本物の秘密の部屋なのかどうかは分からないが、誰でも入れる類の部屋ではないことだけは確かだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼんやりと、寝起きの頭でそんなことを考えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_1")
T "「……とりあえず、誰かに聞いてみようかな」"

play sound se_0052
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ベッドから降りて、食堂に行く準備に入る。顔を洗って、制服に着替えて……、そこでリボンとブラシを取られたことを思い出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "リボンは予備があるし、ブラシも部屋用のものがあるので今困るということはない。\n
だが、ないままだと後々困ることになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "出来るだけ早く取り返したいところだが、はたしてストームで奪われたものというのは取り返すチャンスがあるのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろいろと人に聞きたいことが出てきた。\n
頭の中でまとめながら予備のリボンを留める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鏡の前で身嗜みをチェックした。\n
制服に乱れはない。"

play sound se_0695
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「……よし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気合を込めるように呟いて、部屋を出た。"

with dis
$ hi_mes()

scene bg25_rr_day
with stripe_l_medium

scene bg_par02_ct_tow_day
with stripe_l_long

play music dining_day_p_wam
play sound se_0617
jump gakuen_storm_gow_nig_gra_jok1
label gakuen_joker5_2:

show tower_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0028
Seito "「[firstname]、おはよう。\n
席、こっちが空いているわよ」"

hide tower_a1_3
show tower_a1_3 at left
show tower_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0046
Seito "「おはよう、[firstname]。\n
一緒に朝食をとらない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声をかけられて、その声の主達を探す。\n
すぐ近くの席で、顔見知りの女の子二人が手を振って合図していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの前には孤独感に浸ってみたものの、クラスメイト以外に友達がいないわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "毎日同じカフェテリアを利用していれば、自然に知り合いも出来るものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業の程度が違うのか、校舎ではなかなか会う機会はない。\n
それでも、こうして食事のタイミングが重なると、互いに誘い合う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「ありがとう。\n
空いている席を探していたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人の言葉に甘えて、そちらへと移動する。"

play sound se_0034

show white onlayer master with Dissolve(1.5)

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "席について、いつものように朝食を呼び出す。\n
定番のオレンジジュースにサラダ、そしてトーストといったメニューだ。"

hide tower_a1_3
show tower_a1_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0029
Seito "「ねえ、昨日のストームどうだった？\n
あなた新入生だから、さぞ驚いたんでしょうね」"

hide tower_a1_8
show tower_a1_8 at left
with dis
hide tower_b1_2
show tower_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0047
Seito "「ふふ、私達みたいな在校生は、新入生の驚く顔を見るのが何よりの楽しみなのよ。まあ、私も初めてのときは相当驚いたけれど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ええ。\n
私も、すごく驚いたわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その驚きの種類が、他の新入生の女子とはちょっと違っているような気がするが、そのあたりは黙っておいたほうがいいだろう。"

hide tower_a1_8
show tower_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0030
Seito "「どんなふうだったの？\n
ほらほら、頼りになる先輩に聞かせてごらんなさい！」"

hide tower_b2_2
show tower_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0048
Seito "「そうよ、あなたの力になるわ！\n
ほら、上級生だし！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人とも目がきらきらとしている。\n
在校生にとっては、新入生女子の驚きようを楽しむイベントでもあるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学年というくくりが存在しないシンフォニアにおいては、先輩や後輩というような年齢の概念も他所に比べると薄い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だがそれでも、何かしら無茶を通そうというときに、わざとらしく強調して使われたりしているのをときどき見かける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの場合、シンフォニアに属している時間が長ければ長いほど年長・上級者として見られるようになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのため、分かりやすい例で言うのならば私と双子は、明らかに双子のほうが幼いが、どちらが上級生になるかというと双子のほうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（先輩の質問には答えるべき……、なのかしら？）"

hide tower_a2_2
show tower_a1_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice hei_g0075
Seito "「それで、どうだった？\n
うまくいった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「う～～ん。\n
あれはうまくいったと言っていいのかしら……」"

hide tower_b2_3
show tower_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice chi_g0094
Seito "「何よ、曖昧ねえ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「だって……。\n
なんだか、成功とも失敗とも言えないような感じだったから……」"

hide tower_b2_5
show tower_b2_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice chi_g0095
Seito "「……ますます曖昧」"

hide tower_a1_8
show tower_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice hei_g0076
Seito "「よくもなく悪くもなくってこと？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「そんな感じ……。\n
こういうのが一番微妙な結果よね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカー二人は、私から戦利品を奪って逃げた。\n
彼らにとって、成功ではあるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（奪取された私からしてみれば、成功なんてとても思えないけど……。\n
でも、イベントとして、成功したってことになるのよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、厳密に考えると、あの二人は私の部屋には来ていない。\n
部屋に侵入した証としては、紛い物だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ああ、そうだ。\n
ちょっと聞きたいんだけど、いいかしら？」"

hide tower_b2_9
show tower_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice chi_g0096
Seito "「なあに？\n
何かストームのことで分からないことでもあった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「ええ、あのね……。\n
戦利品っていう名目で、所有物を取られるじゃない？」"

hide tower_a1_5
show tower_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_16")
voice hei_g0077
Seito "「ああ、そうね。\n
取られるわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あれって、取られっぱなしになっちゃうの？\n
それとも、返却日のようなものがあるの？」"

hide tower_a1_2
show tower_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Seito "「…………」"

hide tower_b2_3
show tower_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Seito "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達は私の素朴な疑問に、少し驚いたように顔を見合わせた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（……何か、見当違いなこと言った？）"

hide tower_a2_9
show tower_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice hei_g0033
Seito "「え？\n
あなた、ブリーズのことは何も聞いていないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（ブリーズ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜のジョーカーとのやりとりを思い出そうとしてみるものの、そんな単語は出てこなかった。\n
初耳だ。"

hide tower_b2_5
show tower_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0052
Seito "「あらあら。\n
あなたから戦利品を取っていった男の子は、大事な説明を忘れちゃったのね？」"

hide tower_a2_4
show tower_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0034
Seito "「ストームから一週間後にね、今度はブリーズというイベントがあるのよ」"

hide tower_a1_2
show tower_a1_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0034_5
Seito "「ブリーズは、女子生徒が男子寮に忍びこんで、奪われたものを取り返すってイベントなの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……この学校って、意外とイベント好きよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どの学校も、学生寮のお祭り騒ぎは珍しくない。\n
ただ、学校公認のものとしては、多いのではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアは世界一の魔法学校という優等的なイメージが強いが、やたらとおおらかだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして実際シンフォニアの生徒になるまで、まさかこんなにも自由な学校だとは思っていなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「ねえ……、それって絶対に取り返しに行かなきゃいけないの？」"

hide tower_b2_3
show tower_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice chi_g0097
Seito "「行かなくてもいいけど、そうすると戻ってこないわよ？\n
取られたもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……取り返しに行かなきゃいけないのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまり、私がリボンとブラシを取り返すためには、ジョーカーを探し出す必要があるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、ストームから一週間後の夜にあるのだというブリーズというイベントで、取り返さなくてはいけない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（住んでいる場所さえ知らないんだけど……）"

hide tower_a1_6
show tower_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice hei_g0078
Seito "「残された一週間は、相手の部屋番号を調べたりするといいわよ。\n
経験者にどういう感じで進むのか聞いてみると分かりやすいかも」"

hide tower_b1_5
show tower_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice chi_g0098
Seito "「私達でもいいけど、これまで交流のなかった人に聞いてみるのもいいわ。\n
新しい付き合いも出来るし……」"

hide tower_b1_2
show tower_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice chi_g0099
Seito "「そうやって、聞いたり教えたりすることで、寮内での縦のつながりが生まれるわけ。こういう目的があると、いかにも学校公認のイベントっぽいでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば同じようなことを、昨夜にストームが何であるのかを教えてくれた男子生徒も言っていた。"

hide tower_a1_3

hide tower_b1_8


scene bg25_rr_nig_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0008
Seito "「使用人の目を掻い潜って侵入するわけだから腕試しと……、あと、実際には男女の交流ではなくて新入生と上級生との交流を深めるのが目的みたいです」"


scene bg_par02_ct_tow_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（じゃあ、さっそくだけど、助けてもらおうかな……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見知らぬ人に聞いてみて仲良くなるというのもいいだろうが、あまり余裕はない。\n
確実な線から、目の前の彼女達に当たってみるか。"

menu:
    "ジョーカーについて聞いてみる。":
        jump gakuen_joker5_3a
    "聞かない。":
        jump gakuen_joker5_3b
label gakuen_joker5_3a:
$ lovechara_jokbla_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ねえ、ジョーカーって知っている？\n
たぶん、職員だと思うんだけど……」"

jump gakuen_joker5_4
label gakuen_joker5_3b:
$ lovechara_jokwhi_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（でも、相手は得体の知れない人だし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞いても無駄かもしれない。\n
……というか、やぶへびでトラブルに巻き込まれる恐れもある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "（……いかにも、不審な人だし）"


show tower_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice hei_g0079
Seito "「遠慮しないで聞いてみてよ。\n
せっかくなんだから、私達だって新入生の役に立ちたいわ」"

hide tower_a2_2
show tower_a2_2 at left
with dis

show tower_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice chi_g0100
Seito "「ええ、そりゃあ私達だって、シンフォニアのことだったら何でも聞いてっていうほど詳しくはないけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか、聞かないほうが悪いような雰囲気だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……そこまで言ってくれるのなら、聞いてみようかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「それじゃあ、教えてほしいんだけど……。\n
ジョーカーって名乗る人物のこと、知っている？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「たぶん、職員だと思うの」"

jump gakuen_joker5_4
label gakuen_joker5_4:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（制服は着ていなかったものね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアではそれぞれ制服のアレンジが認められてはいるものの、基本は崩せない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どれだけ改造されていたとしても、制服であれば分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同様に、使用人の制服でもない。\n
ということは、制服を着なくても校内をうろつける立場の人間ということになるのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……まさしく、うろついているって感じよね）"

hide tower_a2_2
show tower_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice hei_g0080
Seito "「ジョーカー……」"

hide tower_a2_9
show tower_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
Seito "「…………」"

hide tower_a2_8
show tower_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice hei_g0081
Seito "「……用務員の？\n
用務員さんが、確かそんな名前だったような気がするけど……」"

hide tower_b1_5
show tower_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice chi_g0101
Seito "「ああ、あの、たまに校内で見かける人よね？\n
いつも、なんだか楽しそうな顔で散歩しているのを見かけるわ」"

hide tower_a1_5
show tower_a1_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice hei_g0082
Seito "「え？それ違う人なんじゃないかしら。\n
私が知っている用務員さんは、口と人相がとんでもなく悪いわよ？」"

hide tower_b1_3
show tower_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
Seito "「？？？」"

hide tower_a1_4
show tower_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
Seito "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人して、証言の食い違いに首を傾げあっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……同一人物なんじゃなくて、二人いるのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私と同じ勘違いをしている。\n
彼らはまったく同じ外見をしているくせに、一緒に行動することが少ないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのせいか、二面性のある同一人物だと思われているよう。\n
もしくは、二重人格か。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（それにしても……、用務員、って……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まったくもって似合わない。\n
不審者を取り締まる側の人間だとは。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……あれ、同じ人かと思うけど、実は二人なのよ。\n
帽子屋寮のツインズみたいに」"

hide tower_b1_1
show tower_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice chi_g0102
Seito "「え？ええ！？\n
そ、そうなの……？」"

hide tower_a1_5
show tower_a1_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice hei_g0083_b
Seito "「同じ名前の別人が二人いたわけじゃないのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「いえ、同じ名前だけど別人で……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（ややこしいなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっくりの双子でも、名前は違う。\n
だが、あの二人は名前も同じ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が話しているのは、それぞれがジョーカーと名乗る二人のことだ。\n
彼女達が話しているのは、別人だと思われていた用務員。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "情報の一部は合致しているが、だからといって彼女達の話す「用務員」がジョーカーだとは限らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "用務員というのが何人いるかも定かではないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、ジョーカーに似た響きの別人が二人、用務員をしているのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしくは、機嫌によって態度に差のあるジョーカーに似た名前の人物が、一人で用務員をしているのかもしれない。"

hide tower_b1_5
show tower_b2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0103
Seito "「もしかして……。\n
そのジョーカーって人に、ストームのイベントで戦利品を取られたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「ええ、そうなの。\n
……成り行きで」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（まさか、部屋に辿り着く前に捕まるとは思わなかった）"

hide tower_a1_4
show tower_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice hei_g0084
Seito "「職員が参加するのって、ありなのかしら……。\n
普通は、妨害側だと思うけど……」"

hide tower_b2_1
show tower_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice chi_g0104
Seito "「でも、そういう人がブリーズの相手って面白いわね。\n
相手が誰なのかを、探す過程も楽しそうだわ」"

hide tower_a1_5
show tower_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice hei_g0085
Seito "「ふふ、一週間の準備期間を思いっきり満喫できそうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……確かに）"

hide tower_a1_3

hide tower_b2_2


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一週間の準備期間とは言っているが、実際にはストームの一週間後がブリーズなので、あと６日しかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "はたして、そんな短期間でジョーカーの正体に迫ることが出来るのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（うう……、満喫っていうか、面倒。\n
ハードル高いわ……）"

with dis
$ hi_mes()

scene bg06_sk_h_day
with stripe_l_medium

scene bg27_rk_eve
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……駄目だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの翌日以来、ジョーカーについて周囲に聞いてまわっているのだが、彼女達から聞いた以上の情報を得ることが出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "各寮の主だった人にまで聞きにいったのに、得られた情報はわずかだ。"


scene bg_par15_rg_ros_day_s
with dis

show viv_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g
Vivaldi "「ジョーカー？\n
ああ、あの用務員……、いや警備員だったか？」"

hide viv_m_01_5
show viv_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0317
Vivaldi "「前に一度、薔薇の剪定をさせたことがある。\n
なかなかにいい腕をしておったな……」"

hide viv_m_03_10
show viv_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0318
Vivaldi "「……そういえば、庭師であったかもしれん。\n
ええい、どうも役職が出てこないな……」"

hide viv_m_03_9


scene bg_par15_rg_hat_day_s
with dis

show eri_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0355
Elliot "「ああ、ジョーカーか！\n
口は悪いが、結構親切な奴だぜ？」"

hide eri_m_01_3
show eri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0356
Elliot "「ガキ共がぶっ壊した、外壁の修理を手伝ってくれてな。\n
……まあ、後からちゃんと修理費用は請求されたけどよ」"

hide eri_m_01_9


scene bg_par15_rg_amu_day_s
with dis

show pia_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0287
Pierce "「ジョーカー怖いんだよ！\n
俺、ちょっとつまみ食いしただけなのに、トレイの角でどつかれたよ！」"

hide pia_m_02_5


scene bg_par15_rg_tow_day_s
with dis

show yuri_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0334
Julius "「用務員のジョーカーか……。\n
日頃からよく校舎を見ていて、気のつく男だ」"

hide yuri_m_02_1
show yuri_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0335
Julius "「学校の備品のどれが壊れていると、知らせてくれるので助かっている」"

hide yuri_m_02_8
show yuri_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0335_5
Julius "「そういえば……、おまえに言われるまで、奴がどこの寮に属しているのかなど気にしたこともなかったが……」"

hide yuri_m_03_2
show yuri_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0336
Julius "「用務員だから、全体を見ているんじゃないか？どこの寮の所属というのはないと思うが……、考えてみれば、これだけ広い学園だと奇妙な話だな」"

hide yuri_m_02_4


scene bg27_rk_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それぞれの寮を訪ねてまわり、聞き集めたというのに、分かったのはこれくらいのものだ。……ピアスの証言は、数にも入らなさそうだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（そういえば、どちらのジョーカーも、校内をふらふら散策しているようだっけ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれはただの散歩ではなく、用務員としての仕事のうちだったのだろう。\n
校内をまわり、雑務をこなしているということは分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それ以上のことは不明だ。\n
どこに行けば会えるのか、どこの寮に部屋があるのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういったことは、不思議なほどに誰も知らないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも、目撃情報は口が悪いほうのジョーカーとそうではないジョーカーとが入り混じり、皆その認識は曖昧だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段はそういう曖昧さを許さないタチの人でさえ、追及しない。\n
知ろうとすることに、セーブでもかかっているかのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_2")
T "（……何者なのよ、ジョーカー）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "調べれば調べるほどに、胡散臭くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆それなりに交流はあるようなのに、誰もジョーカーの素性までは知らない。\n
誰も、気にしてすらいなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……おかしい、わよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（何か、魔法でも使って印象を誤魔化しているのかしら……）"


scene bg06_sk_h_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「……あれ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆がその存在を知っているのに、実在する場所を知らない。\n
皆がその存在を知っているのに、会った人はいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らによく似た存在を、知っている。"

with dis
$ hi_mes()

scene bg_par15_rg_tow_nig
with stripe_l_medium

scene bg25_rr_nig
with stripe_l_long
play sound se_0774

play music corridor_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "探していると会わないのに、探していないとばったり出くわす。\n
彼は、そういう人。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……{size=+20}あ{/size}」"



show jo_m2_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice jok_g0098
Joker "「やあ、[firstname]。\n
ストームの日以来だね」"

hide jo_m2_01_2
show jo_m2_01_2 at left
with dis

show jo_m1_02_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice jok_g0099
Joker "「よお、ガキンチョ。\n
どうした、シケた面してんな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食堂で夕食をとった帰り、自室へと向かう塔の廊下でのことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "胡散臭いジョーカーは相変わらず意味ありげだし、口の悪いジョーカーは相変わらずの暴言三昧。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……本当に、ややこしい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前には二人の人間がいるというのに、その呼び名が一つしかないというのは非常に面倒だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「ねえ、あなた達、本当に両方ともジョーカーなの？\n
別の呼び名があったりしない？」"

hide jo_m2_01_2
show jo_m2_01_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jok_g0100
Joker "「ないよ。\n
俺はジョーカーだ」"

hide jo_m1_02_5
show jo_m1_02_15 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jok_g0101
Joker "「ねえな。\n
俺は、ジョーカーだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人して、まるでそれぞれが違う名前を名乗っているかのような雰囲気で、同じ名を名乗る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……変な感じ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人がそれぞれ名乗ると、聞いた瞬間はそれが違うものであるように響くのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「それじゃあ、分かりにくいのよ」"

hide jo_m1_02_15
show jo_m1_02_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice jok_g0102
Joker "「おまえが、だろ？\n
別に、俺達は困らねえ」"

hide jo_m2_01_11
show jo_m2_03_14 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice jok_g0103
Joker "「そうだねえ、俺達は困らない。\n
俺達が困らなければ、他に誰も困らないだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人の言い分は間違っていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは故意か、そうでないのかは分からないが、シンフォニアにおいて二人一役をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当はそれぞれ違う人間なのに、まるで一人であるかのように周囲には振る舞っているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結果として、会う人によって、イメージの違う用務員になる。二人で一人を演じるのならば、名前だって統一した一つであったほうがいいのは分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（……でも、私は二人いるって知っているもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人の差異が分かれば、名前が一つというのは紛らわしいだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……分かったわ。\n
あなた達にとっては、名前なんてどうでもいいのね？」"

hide jo_m1_02_8
show jo_m1_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice jok_g0104
Joker "「そう言ってんだろうが。\n
おまえ、耳も頭も悪いのかよ」"

hide jo_m2_03_14
show jo_m2_01_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice jok_g0105
Joker "「どちらでも問題ないからね。\n
俺も彼も、どちらもジョーカーだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「でも、あなた達は違う人間だわ。\n
だから……、私が名前をつけて区別するわ」"

hide jo_m2_01_5
show jo_m2_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice jok_g0106
Joker "「えっ？」"

hide jo_m1_03_4
show jo_m1_03_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice jok_g0107
Joker "「はあ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう、誰も彼らを区別せず、誰も彼らを名前で呼ぶことに意味を見出さないというのならば、私がその名前をつけてしまおう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは違う人間だ。\n
それは名案に思えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_3")
T "「口が悪いほうがブラックさんで、そうじゃないほうがホワイトさんよ。\n
どう、分かりやすいでしょう？」"

hide jo_m2_01_4
show jo_m2_03_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_3")
voice jok_g0108
Joker "「わ、分かりやすいっていえばそうだけど……。\n
ペーター＝ホワイトの親戚みたいで嫌だなあ」"

hide jo_m2_03_13
show jo_m2_02_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_3")
voice jok_g0109
Joker "「……そして、同じ苦情を前にもどこかで言ったことがあるような気がするよ、俺は」"

hide jo_m1_03_5
show jo_m1_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_3")
voice jok_g0110
Joker "「気が合うな、ジョーカー。\n
俺も、どっかで、同じ苦情を聞いたことがあるぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「……私もどことなく、似たような苦情を言われた覚えがあるような気がするけど。\n
いいのよ、分かりやすいのが一番だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「ブラックさんに、ホワイトさん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "交わす会話に妙な既視感を覚えながらも、わざとらしい無邪気さを装って、堂々と命名する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いちいち「口が悪いほうのジョーカー」「そうじゃないほうのジョーカー」なんて区別するよりは、ホワイト、ブラックと命名してしまったほうが余程簡単だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ホワイトさんなジョーカーはどこか面白がるような笑みを浮かべ、ブラックさんなジョーカーは苦虫を噛み潰したような顔をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（分かりやすくなったところで、聞きたいことが……）"

menu:
    "ブリーズについて聞く。":
        jump gakuen_joker5_5a
    "聞かない。":
        jump gakuen_joker5_5b
label gakuen_joker5_5a:
$ lovechara_jokbla_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（ブリーズについて、聞いておこう。\n
本人に聞くのが一番手っ取り早いわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「私、ずっとあなた達のことを探していたのよ」"

hide jo_m1_01_10
show jo_m1_03_19 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice jok_g0111
Joker "「なんだ？\n
俺に惚れたのか、ガキンチョ」"

hide jo_m2_02_3
show jo_m2_02_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice jok_g0112
Joker "「はは、何言っているんだよジョーカー。\n
俺に惚れたんだよ……、ね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_16")
T "{size=+20}「二人とも、自惚れ屋で勘違い気味なところまでそっくりね」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "冷た～く、切り捨ててやる。"

jump gakuen_joker5_6
label gakuen_joker5_5b:
$ lovechara_jokwhi_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……聞いて、この二人が教えてくれるかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誤魔化されて終わってしまいそうだ。"

hide jo_m2_02_7
show jo_m2_02_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0113
Joker "「そういえば……。\n
[firstname]、君、最近俺達のことを嗅ぎまわっている……、よね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どきりとした。\n
彼ら二人について調べている、探しているのは事実だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、「嗅ぎまわっている」なんて言葉で表現されてしまうと、悪いことでもしたような気になる。"

hide jo_m1_03_19
show jo_m1_01_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0114
Joker "「なんだと？\n
おいこら、てめえ、ストーカーかよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「そ、それは、ペーターよ。\n
私はただ、あなた達の居場所が知りたかっただけで……」"

hide jo_m2_02_12
show jo_m2_03_19 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice jok_g0115
Joker "「……{size=+20}そういうのをストーカーって言わない？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「{size=+20}違う！{/size}\n
言わない！」"

jump gakuen_joker5_6
label gakuen_joker5_6:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「あなた達、ストームで私からリボンやブラシを強奪したでしょう？\n
それを取り返したいの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「居場所を知らなきゃ、ブリーズを成立させられないから……」"

hide jo_m2_03_19
show jo_m2_03_14 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice jok_g0116
Joker "「ああ、そうか。\n
君、ブリーズに参加することにしたのか」"

hide jo_m1_01_7
show jo_m1_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice jok_g0117
Joker "「いいんじゃねえの？\n
俺は、楽しめることなら何でも大歓迎だぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「じゃあ、居場所を教えてよ。\n
あなた達がどこに住んでいるのか、皆知らないみたいで……」"

hide jo_m2_03_14
show jo_m2_01_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_16")
voice jok_g0118
Joker "「男には謎があったほうが魅力的っていうからね。\n
演出は大事だよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「演出なんて、結構よ。\n
私は、分かりやすいほうが好きなの」"

hide jo_m1_03_9
show jo_m1_02_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice jok_g0119
Joker "「けけ。\n
分かりやすいほうが好きなんざ、まんま、ガキだな……」"

hide jo_m2_01_5
show jo_m2_01_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice jok_g0120
Joker "「まあでも、ブリーズだって言うなら仕方ないか。\n
ほら、[firstname]、手を出してごらん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「手を？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（前みたいに、キャンディーでもくれるのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前、名前を覚えていたご褒美としてホワイトさんがキャンディーをどこからともなく取り出してくれたのを思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（手品で誤魔化されたりしないわよ？）"

play sound se_0262

show m_jo5_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、今回手のひらに落とされたのはキャンディーではなく、小さな鍵だった。\n
彼が、腰の鍵束から外したものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_13")
T "（これって、例の秘密の部屋の……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice jok_g0121
Joker "「君は、これがどこの鍵だか知っているはずだよ。\n
……使い方もね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice jok_g0122
Joker "「なくすんじゃねえぞ？\n
なくしたら、お仕置きだぜ？」"

hide m_jo5_1

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「子供じゃないんだから、なくしたりしないわよ！」"

hide jo_m1_02_1
show jo_m1_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice jok_g0123
Joker "「子供じゃない、ねえ？\n
どこをどう見たら、子供じゃねえように見えるんだろうな、ガキそのものだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にやにやと笑うブラックさんの視線は、あからさまなセクハラだ。\n
つうっと、私の体のラインを確かめるように上下に揺れる。"

hide jo_m2_01_11
show jo_m2_01_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0124
Joker "「こらこら、失礼なこと言うなよ、ジョーカー。\n
実は、脱いだらすごいかもしれないだろう？」"

hide jo_m1_02_4
show jo_m1_03_19 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0125
Joker "「はっ、むしろ脱いだらもっと貧相になりそうだぞ、このガキ」"

hide jo_m2_01_1
show jo_m2_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0126
Joker "「まあ、その辺はブリーズを楽しみにしておこうよ。\n
ね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「ね、じゃないわよ！\n
ブリーズに何するつもりよ、あんた達！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校公認のイベントなのだから、ブリーズだって健全であるべきだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "健全とはほど遠い諸々を口走る二人。\n
校内の鍵を生徒に渡してしまうあたりも、まったく職員らしくない。"

hide jo_m2_03_7

hide jo_m1_03_19
##[chara2 PAY ATTENTION="false"]
$ hi_mes()
##[clearmessage PAY ATTENTION="false"]

scene bg_par15_rg_tow_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_joker_end
