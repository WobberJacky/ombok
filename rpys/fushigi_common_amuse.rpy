label fushigi_common2_amuse:
$ hi_mes()

scene map_bg_summer_day
with dis
$ clockanim()


play music forest1_p_ali

scene bg_gen_sky_sum_day with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "森の木々の向こうから、陽気で賑やかな音楽が流れてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "有力者でもあるゴーランドの経営する遊園地は、この世界でも常に人の絶えない場所の一つだ。"

play sound se_0793 volume .6
pause 1
play sound se_0620 volume .4
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……でも、どうしてそこから人がこんなに出てくるのかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この道を進むときには、遊園地に向かう流れと、遊び疲れて帰ってくる流れと、大きく二極化しているはずなのだが……。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0001
Child "「ねえママーまだ乗りたいよー！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oda_f0000
Mother "「分かっているわ。\n
でもそれはまた今度来たときに乗りましょう！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0000
Child "「わあ～！\n
パパ、どうしてそんなに早く歩くの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sat_f0000
Father "「ほら、なるべく急げ。\n
始まったら、えらいことになる」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今は、何故か私一人が流れに逆らうような形で歩いている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（……何だろう、嫌な予感がする）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（それも、予想の付く事態のような気が……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この場所を選んだ時点で、覚悟はしていたつもりだったが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……最初から選択を間違えたかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だとすれば、ずいぶんと幸先の悪い話だ。"

play sound se_0221
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0038
Gowland "「たらったららん、らった、らったんたん！\n
ららら、たんっ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞き慣れたくなかった不協和音。\n
それが徐々に大きくなるにつれて、私の顔も引きつっていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（……やっぱり）"

$ hi_mes()


play music gowland_t_ali

scene yum_sum_01_1
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地の入り口付近、そこに立った影を見つけた瞬間、私の予感は正しかったのだと悟ってしまった。"


show go_t_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0039
Gowland "「ららら、らんっ！\n
たんたた、らん、たたん！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……聞き間違えようもないわよね、これは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想通りというべきか。\n
入り口近くで、演奏する見慣れた友人の姿に、私は溜息を隠せなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（ここはやめて、他の場所に行こうかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引き返すなら今しかない。\n
半ば本気でそんなことを考え始めたときだ。"

play sound se_0022
$ flash(.1)
pause .4
hide go_t_03_14
show go_t_03_14 at left
show bor_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0017
Boris "「だ・か・ら、おっさん！\n
あんたが音害撒き散らすのはもう諦めているけど、客がいるときにはやめろって言っているだろう！」"

hide bor_t_01_4
show bor_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0018
Boris "「同じ廃業なら、もっと前向きな方向で閉めてよ。\n
耳が腐る音で営業停止なんて、格好悪い……」"

hide go_t_03_14

hide bor_t_03_13
show bor_t_03_13 at left
show pia_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0015
Pierce "「ううう、耳……、俺の耳……。\n
ああ、ついているよね、よかった」"

hide pia_t_02_6
show pia_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0016
Pierce "「取れてないや。\n
すごい音を聞いたから、腐って取れちゃったかと思ったよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "発砲したボリスから離れた場所では、今にも泣きじゃくりそうなピアスがぼそぼそと呟いている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "近くにいた従業員達も顔を顰めながらも、いつも通りテンション高く苦情を口にした。"

hide bor_t_03_13

hide pia_t_02_11


show yuuen_man_02_02 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0003
Employee "「オーナー、子連れ客がすごい勢いで帰っていきますよ！\n
子供から大人を狙った営業に路線変更ですか？」"

hide yuuen_man_02_02
show yuuen_man_02_02 at left
show yuuen_woman_02_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0002
Employee "「でも、大人も裸足で逃げ出す演奏ですよね！\n
さすが、うちのオーナーです！！」"


show go_t_01_6 at center
hide yuuen_man_02_02
hide yuuen_woman_02_03
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0040
Gowland "「おまえら、ちっとも褒めているように聞こえねえぞ……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（誰も褒めていないって）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、当の演奏家本人にはその苦情は届かないらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（いつも思うけど……、あの音を聞いていて、どうして聴覚が無事なのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人の話が聞こえないわけではないのに、特殊な耳なのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（耳のいい動物さん達にとっては、迷惑な話よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "居候している二匹の身を思わず案じてしまう。"

hide go_t_01_6
show go_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0041
Gowland "「まったく、うちの奴らときたら……。\n
芸術への理解度が低くて困ったもんだぜ」"

hide go_t_03_2
show go_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0042
Gowland "「そもそも、ボリス！\n
廃業するほど、うちは落ちぶれちゃいねえっ！」"

hide go_t_02_9
show go_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0043
Gowland "「景気の悪いこと言うんじゃねえよ！\n
その上、せっかく新曲のインスピレーションが高まっていたっていうのに……、邪魔しやがって」"

hide go_t_02_1
show go_t_02_1 at left
show bor_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0019
Boris "「あんたの場合は、新曲じゃなくて、\n
{size=+20}デスマーチの間違いだろうが{/size}」"

hide bor_t_01_3
show bor_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0020
Boris "「先刻から客が軒並み逃げていっているのが、見えないわけ？\n
そんな立派な眼鏡まで付けているのに……、あ、ひょっとして、{size=+20}老眼{/size}？」"

hide go_t_02_1
show go_t_02_1 at left_center
hide bor_t_02_8
show bor_t_02_8 at center
with dis

show pia_t_01_8 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0017
Pierce "「ぴ、可哀想なオーナーさん。\n
耳が悪い上に、目まで悪いなんて……」"

play sound se_0093
pause .4
hide pia_t_01_8
show pia_t_03_5 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0018
Pierce "「ナイフで削げば、少し耳もよくなるかな。\n
やってみてもいい？」"

hide go_t_02_1
show go_t_02_9 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0044
Gowland "{size=+20}「ならねえよ！\n
いいわけあるかっ！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（……相変わらずだなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "話し始めたおかげでゴーランドの手も止まり、周囲は一応平穏を取り戻している。\n
近付くなら今だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（またあの演奏を再開されたら、堪らないもの）"

play sound se_0010
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "木の陰から姿を見せて近付いていくと、人の輪の中心にいた三人は私に気付いたのか、一斉に振り向いた。"

play sound se_0142
pause .3
play sound se_0142
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私と視線を合わせるとそれぞれ大きく手を振ってくれる。"

hide go_t_02_9
show go_t_02_12 at center
hide pia_t_03_5

hide bor_t_02_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0045
Gowland "「お、よく来たな、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「こんにちは、ゴーランド。\n
ボリスとピアスも一緒だったのね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスはふらふらとどこかに行ってしまうし、ピアスは帽子屋ファミリーの一員だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなわけで三人が揃うのは珍しいため、いいタイミングだったらしい。"

if routechara == "Vivaldi":
    jump fushigi_common2_amuse2_castle
if routechara == "Ace":
    jump fushigi_common2_amuse2_castle
if routechara == "Elliot":
    jump fushigi_common2_amuse2_elliot
label fushigi_common2_amuse2_castle:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城を出てきた私は、遊園地に滞在させてもらおうと思っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（ずっといるわけじゃないけど……。\n
騒音さえなければ、一番平和なところだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "女王様の八つ当たりや宰相のサボりのとばっちりを受けて処刑されるお城よりは、穏やかなはずだ。"

hide go_t_02_12
show go_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0046
Gowland "「そうなんだが……。\n
それよりも、[firstname]、聞いてくれよ」"

hide go_t_03_2
show go_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0047
Gowland "「うちの動物どもときたら、芸術をちっとも理解しなくてよ……」"

if routechara == "Vivaldi":
    jump  fushigi_common2_amuse3
if routechara == "Ace":
    jump  fushigi_common2_amuse3
if routechara == "Elliot":
    jump fushigi_common2_amuse2_elliot
label fushigi_common2_amuse2_elliot:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスと同じく帽子屋を家出してきた私は、遊園地に滞在させてもらおうと思っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（ずっといるわけじゃないけど……。\n
騒音さえなければ、一番平和なところだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "マフィアの本拠地である帽子屋屋敷なんかより、ずっと快適なはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（……隠しごとだって、されないわ）"

hide go_t_02_11
show go_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice gor_f0046
Gowland "「そうなんだが……。\n
それよりも、[firstname]、聞いてくれよ」"

hide go_t_03_2
show go_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice gor_f0047
Gowland "「うちの動物どもときたら、芸術をちっとも理解しなくてよ……」"

if routechara == "Elliot":
    jump fushigi_common2_amuse3
label fushigi_common2_amuse3:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（いや、あなたの演奏が理解できない原因はそこじゃない。\n
むしろ、誰だったら理解出来るのか教えてほしいくらい……）"

hide go_t_02_11
show go_t_02_11 at left
show bor_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice bor_f0021
Boris "「あんたのは芸術でも何でもなく、ただの破壊兵器だって」"

hide go_t_02_11

hide bor_t_03_11
show bor_t_03_11 at left
show pia_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice pie_f0019
Pierce "「そうだよ。\n
にゃんこに追いかけられるのと同じぐらい酷いよ」"

hide pia_t_02_10
show pia_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice pie_f0020
Pierce "「生命の危機を感じるもん……。\n
俺、酷い音楽で死ぬような最期は、嫌だなあ」"

hide bor_t_03_11
show bor_t_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice bor_f0022
Boris "「ピアス、おまえ……。\n
まだ追いかけられ足りないわけ？」"

play sound se_0089 volume .6
$ flash(.2)
pause .5
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きらりとナイフとフォークを両手に構えたボリスがにやりと笑うと、ピアスはびくっと身体を縮めた。"

hide pia_t_01_13
show pia_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0021
Pierce "「ぴ！\n
だ、だって……、俺にとっては、生命の危機という意味では同じだもん！」"

hide bor_t_02_2
show bor_t_01_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0023
Boris "「だからって、俺と{size=+20}あれ{/size}を一緒にするんじゃねえよ！\n
俺の本能と、先天的な破壊音を混同されるなんて、我慢できねえ」"

hide bor_t_01_8
show bor_t_01_8 at left_center
hide pia_t_02_6
show pia_t_02_6 at center
show go_t_03_6 at right_center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0048
Gowland "「おまえら、好き勝手なことを……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（本当に、この世界の人達ときたら、人の話を聞かないんだから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "やってきた客を放ってすっかり自分達の会話に入っている。\n
しかし、いつまでも放置されていては話が進まない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "睨み合う三人の間に割り込んで、手を叩く。"

play sound se_0122
pause .5
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……さてと、盛り上がっているところ悪いんだけど。\n
ちょっと頼みごとがあるの、ゴーランド」"

hide go_t_03_6
show go_t_01_11 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0049
Gowland "「は？\n
あんたが、俺に頼みだなんて珍しいな？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きょとんと私を見た遊園地のオーナーに頷いて、簡単に事情を話した。"

$ hi_mes()
hide pia_t_02_6

hide bor_t_01_8

hide go_t_01_11


$ time_effect()##PLEASE MANUALLY ADJUST ME

play music amuse_gate_p_ali

show go_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0050
Gowland "「なるほど、そういうことか。\n
別に構わないぜ」"

hide go_t_02_12
show go_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0051
Gowland "「あんたの滞在地の連中を引き連れてっていうんじゃ大騒ぎだが……。\n
あんた個人が遊びに来てくれる分には、大歓迎だ」"

hide go_t_03_4
show go_t_03_4 at left
show bor_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_f0024
Boris "「うんうん。\n
俺も歓迎するよ」"

hide bor_t_03_10
show bor_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_f0025
Boris "「あんたと一緒なら、遊び甲斐あるし……、なにより、ネズミよりも美味しそうだし」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（……美味しそう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何やらとても不穏当な発言が聞こえた気がした。\n
気のせいか、ボリスの視線が妙に生々しいものに見えてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（気のせいよ、気のせい）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（気のせい……）"

hide go_t_03_4
show go_t_03_4 at left_center
hide bor_t_02_9
show bor_t_02_9 at center
show pia_t_01_7 at right_center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice pie_f0022
Pierce "「だ、だめだよ、ボリス！\n
この子は食べちゃ駄目！」"

hide pia_t_01_7
show pia_t_03_10 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice pie_f0023
Pierce "「[firstname]、君を食べていいのは、俺だけだよね？\n
少しずつ囓ってあげるから」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "{size=+20}「どっちもごめんよ」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "非日常的な彼らと違って、私はおいしくもないし、食べられたくもない。\n
齧られるのも嫌だ。"

hide go_t_03_4
show go_t_03_5 at center
hide bor_t_02_9
hide pia_t_03_10
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0052
Gowland "「ははは。\n
まあ、こいつらのことはさておき、あんたがしばらくいるっていうのは、構わないぜ」"

hide go_t_03_5
show go_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0053
Gowland "「せっかくだ、ゆっくりしていけよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「ありがとう、ゴーランド」"

hide go_t_01_2

$ hi_mes()

scene charasel_bg_amuse_day
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_medium
if routechara == "Vivaldi":
    jump fushigi_vivaldi2_2
if routechara == "Ace":
    jump fushigi_ace2_2
if routechara == "Elliot":
    jump fushigi_elliot2_2


label fushigi_common3_amuse:

scene charasel_bg_amuse_night with Dissolve(1.5)
$ clockanim()


scene yum_sum_03_1
with dis

scene yun_sum_03
with dis

play music night_garden_p_ali

scene bg_gen_sky_sum_nig with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_chara")
voice tan_f0004
Employee "「営業妨害って、こういうことを言うんですよね！\n
うちの来場人数が減ったらどうしてくれるんですか！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice may_f0003
Employee "「もう……、客商売には、迷惑以外の何ものでもないですよ。\n
訴える前に始末しちゃったけど、よかったですか、オーナー？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0054
Gowland "「まったくだぜ。\n
最近は、客……、いや、客にもならねえ客のマナーが悪くて、本当に困るよなあ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_f0026
Boris "「そうだよねえ。\n
何も遊園地まで来て、撃たれることはないと思うんだけどなあ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_f0027
Boris "「どうせなら、他の領地で仕掛けてくれればいいのに。\n
遊んでほしいなら、それなりの用意をしてから来てよね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（直視しないようにしよう）"


scene t_cut_yuu3_1u
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "賑やかな音楽が鳴り響く、遊園地の一角。\n
そこで起きた銃撃戦を物語るように、今、私の目の前にあるのは大きな赤だ。"


scene t_cut_yuu3_1 with Dissolve(1.2)
pause .4

show pia_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0053
Pierce "「うわー、派手だなあ。\n
お掃除、これじゃ大変だよ……、ちゅう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "倒れた男達の傍で屈んだピアスは、深刻そうに見えない顔でそんなことを言う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（そういう問題じゃないでしょう。\n
大体、ピアスは一応帽子屋ファミリーの一員じゃない……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……ここでも、こんな揉めごと、結構多いの？」"


scene yun_sum_03
with dis
hide pia_t_02_11
show pia_t_02_11 at left
show go_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice gor_f0055
Gowland "「まあ、ゼロとはいわねえよ。\n
こう見えても、俺はここの有力者だからな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ライフルをいつものバイオリンに戻したゴーランドは、なんでもないように言う。\n
その顔は、凄惨な現場には似つかわしくない、優しい顔だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（何で、あんな顔で笑えるんだろう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰でも銃を携帯しているこの世界で、銃撃戦などいつもの光景だと言ってしまえば、それまでかもしれないが。"

hide pia_t_02_11

hide go_t_01_8


scene bg_gen_sky_sum_nig
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（私には……、無理だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうなりたいとも思えない。\n
だが、この世界を選んだのは、私自身だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（混じり合えそうで、混じりきれない）"

if routechara == "Vivaldi":
    jump fushigi_common3_amuse2_castle
if routechara == "Ace":
    jump fushigi_common3_amuse2_castle
if routechara == "Elliot":
    jump  fushigi_common3_amuse2_elliot
label fushigi_common3_amuse2_castle:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから私はいつまでも余所者なのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城で無事でいられるのも、きっとそのおかげ。"

if routechara == "Vivaldi":
    jump  fushigi_common3_amuse3
if routechara == "Ace":
    jump  fushigi_common3_amuse3
label fushigi_common3_amuse2_elliot:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、私はいつまでも余所者だ。\n
エリオット達が信用してくれないのも、そのせいだろうか。"

jump fushigi_common3_amuse3
label fushigi_common3_amuse3:

scene yun_sum_03
with dis

show bor_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「…………」"

hide bor_t_01_11
show bor_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0028
Boris "「そういやあ、おっさんがわざわざ相手をするなんて珍しいよなあ。\n
年寄りの冷や水って言葉、知っている？」"

hide bor_t_02_2
show bor_t_02_2 at left
show go_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0056
Gowland "「年寄りって言うな！\n
俺はまだまだ若いんだってっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスの軽口にも反応せずにはいられないゴーランドは、本当に付き合いがいい。\n
いつものやりとりに少しほっとした。"


show pia_t_03_13 at center
hide go_t_01_9
hide bor_t_02_2
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0054
Pierce "「どうしたら綺麗になるかな。\n
片付けるにも、これだけの数だとことだしなあ」"

hide pia_t_03_13
show pia_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0055
Pierce "「どうしよう、どうしよう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ピアス……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（あっちはあっちで仕事モードに入っているし）"

if routechara == "Vivaldi":
    jump fushigi_common3_amuse4
if routechara == "Ace":
    jump fushigi_common3_amuse4
if routechara == "Elliot":
    jump fushigi_common3_amuse4_elliot1

label fushigi_common3_amuse4:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………あ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（寒い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬目の前の赤に血の気が引いたのかと思ったが、違う。\n
これはもっと直接的な……、悪寒だ。"

hide pia_t_01_13
show pia_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0056
Pierce "「あれあれ、[firstname]。\n
どうしたの、君、顔が真っ赤だよ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「何でもな……、くしゅん！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "くしゃみが出始めると、さすがに気のせいとは言えなくなった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（そういえば、この前もちょっと寒気がしていたけど……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（これは風邪なの、やっぱり？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今まで体調不良を起こした人間など、ナイトメアを除いては怪我人以外で見たことがなかったのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（ま、間抜けすぎる……）"

play sound se_0593
hide pia_t_01_3
show pia_t_01_3 at left
show go_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice gor_f0057
Gowland "「おい、足下大丈夫かよ、ふらふらしているぜ？\n
おまえら、ここは適当にしておくから、部屋まで送っていってやれ」"

hide pia_t_01_3

hide go_t_02_4
show go_t_02_4 at left
show yuuen_woman_01_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice may_f0004
Employee "「分かりました！\n
さあ、行きましょうっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「い、いいわよ。\n
多分、ちょっと疲れか何かが出ただけだから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を引いて送ろうとする従業員に慌てて声を上げるが、私の顔を見た彼らは一様に首を横に振る。"

hide go_t_02_4

hide yuuen_woman_01_03


show bor_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0029
Boris "「そういう顔色じゃないよ、[firstname]。\n
それとも、俺が添い寝してあげたほうがいい？」"

hide bor_t_01_10
show bor_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0030
Boris "「あったかい抱き枕、いる？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「なっ」"

hide bor_t_03_8
show bor_t_03_8 at left
show pia_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice pie_f0057
Pierce "「だ、駄目だよ、猫なんかに添い寝されたら、寝ている間にぱっくり食べられちゃうよ、[firstname]！」"

hide pia_t_03_3
show pia_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice pie_f0057_5
Pierce "「添い寝するなら、俺のほうがいいよね、そうだよね？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（……いつから添い寝が前提になったのよ）"

play sound se_0481 volume .7
pause .6
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも通り騒ぐ二人に、頭痛までしてきた。"


hide bor_t_03_8

hide pia_t_03_13
show pia_t_03_13 at left
show go_t_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0058
Gowland "「ほら、おまえら、いい加減にしておけって。\n
[firstname]、固まっているだろう」"

hide go_t_01_6
show go_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0059
Gowland "「あまり困らせるんじゃねえよ。\n
じゃ、後は任せたぜ、医者は呼んでおくからよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "我先にと自己主張している二人を押しのけて、ゴーランドがもう一度従業員に合図を送った。"

hide pia_t_03_13
hide go_t_02_12
show go_t_02_12 at left
show yuuen_woman_01_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0005
Employee "「はい、お任せくださいっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あ、ちょ、ちょっと……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのままずるずると引っ張っていく彼女の手に逆らえる力など、私にあるはずもなく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あっという間にゴーランドの屋敷へと引っ張って行かれてしまったのだった。"

$ hi_mes()
hide go_t_02_12

hide yuuen_woman_01_01


scene yun_sum_03 with Dissolve(1.2)

scene yum_sum_03_1
with stripe_l_medium

scene map_bg_summer_night
with stripe_l_medium

scene map_bg_summer_day with Dissolve(1.2)

scene yum_sum_01_1
with stripe_l_medium

play music amuse_guestroom_p_ali

scene yug_01
with stripe_l_long

show go_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0060
Gowland "「……って、だから、おまえら、病人を看病するときにはな、胃に優しくて滋養のあるものがいいんだ」"

hide go_t_03_6
show go_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0061
Gowland "「魚やチーズを持ち込むんじゃない！\n
消化不良を起こしたら大変だろうがっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

hide go_t_02_9
show go_t_02_9 at left
show bor_t_01_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice bor_f0031
Boris "「はあ……、おっさん、知らないの？\n
お魚だって、栄養たっぷりだよ」"

hide bor_t_01_12
show bor_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice bor_f0032
Boris "「これを食べれば風邪なんか吹き飛ぶぐらいに元気になるって」"

hide go_t_02_9
show go_t_02_9 at left_center
hide bor_t_02_8
show bor_t_02_8 at center
show pia_t_03_9 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice pie_f0058
Pierce "「違うよ、チーズだよ、チーズ！\n
元気になれる食べ物って言ったら、やっぱりこれだよ！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（病人の看病だというなら、もう少し静かにしていてほしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "貸してもらっている客室のベッドに潜り込んだ私の元に、お粥と魚とチーズを持ってきた三人が、ずっとそんな口論を繰り返している。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（本当にただの風邪なんだから、大人しく寝ていればよくなるのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の中で、私はとても弱い存在ということを気にしてか、彼らは時間帯が変わるごとに顔を見に来ていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それぞれが何かしらの手土産を持って。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（病気のときには寂しくなるっていうけど、寂しがっている暇もないわ）"

hide go_t_02_9
show go_t_03_6 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice gor_f0062
Gowland "「だから、おまえらのそれはマンネリなんだよっ」"

hide bor_t_02_8
show bor_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice bor_f0033
Boris "「あんたのは考え方が古いんだよ！」"

hide pia_t_03_9
show pia_t_01_9 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice pie_f0059
Pierce "「チーズっていったら、チーズだよ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「早く、治そう」"

hide go_t_03_6

hide bor_t_01_8

hide pia_t_01_9


scene bg_gen_sky_sum_day with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（大切にされているのに贅沢な悩みだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦い薬だろうが何だろうが早く使って治さなければ。\n
頭の中に浮かんだ顔は、今、ここにはいないあの人の顔。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（あの人達も大分濡れていたけど、風邪なんかひいていないわよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "早く帰らなければという気持ちと、でもこんな状態で帰ったら何と言われるか分からないという気持ち。\n
それらが混ざり合っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（…………）"

if routechara == "Vivaldi":
    jump fushigi_common3_amuse4_vivaldi1
if routechara == "Ace":
    jump  fushigi_common3_amuse4_ace1

label fushigi_common3_amuse4_vivaldi1:
$ fushigi_common3_amuse4_vivaldi2a_seen = False
menu:
    "ビバルディ、待っているかな。":
        jump fushigi_common3_amuse4_vivaldi2a
    "あの人達のことだから、大丈夫だろうけど。":
        jump fushigi_common3_amuse4_vivaldi2b

label fushigi_common3_amuse4_vivaldi2a:
$ fushigi_common3_amuse4_vivaldi2a_seen = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思い浮かぶのは、一人のこと。"

jump fushigi_common3_amuse4_vivaldi3
label fushigi_common3_amuse4_vivaldi2b:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思い浮かぶのは、城の皆。"

jump fushigi_common3_amuse4_vivaldi3
label fushigi_common3_amuse4_vivaldi3:
$ hi_mes()

scene bg_gen_sky_sum_day
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_medium
jump fushigi_vivaldi3_1
label fushigi_common3_amuse4_ace1:
$ fushigi_common3_amuse4_ace2a_seen = False
menu:
    "エースは、戻れたのかしら。":
        jump fushigi_common3_amuse4_ace2a
    "あの人達のことだから、大丈夫だろうけど……。":
        jump fushigi_common3_amuse4_ace2b

label fushigi_common3_amuse4_ace2a:
$ fushigi_common3_amuse4_ace2a_seen = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まず最初に考えてしまうのは、エースのこと。"

jump fushigi_common3_amuse4_ace3
label fushigi_common3_amuse4_ace2b:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "皆のことを考える。"

jump fushigi_common3_amuse4_ace3
label fushigi_common3_amuse4_ace3:
$ hi_mes()

scene bg_gen_sky_sum_day
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_medium
jump fushigi_ace3_1
label fushigi_common3_amuse4_elliot1:


$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「仕事か……」"


scene bg_gen_sky_sum_nig
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（皆に、理由も言わないで飛び出してきたなんて、初めてだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "役持ちと言われる彼らではなく、同僚達の顔を思い出しながら、小さく息をつく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "有事の際の抜けを埋めるために配置してもらったはずなのに、自分が穴を開けていれば世話のない話。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（メイドの皆には悪いけど……、あの人達には、たまにはいい薬かもしれないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "家族のように受け入れてくれた場所、何よりも大切な彼がいる場所。\n
帽子屋屋敷に対しての愛着は、離れても変わらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ずっと家出を続ける気もないが、すぐに戻ろうという気持ちにはなれなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（すぐに戻ったら、軽く思われそうだもの）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（今回は、私、本気で怒ったんだから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らの全部を知りたいなんて思わない。\n
しかし、あからさまに隠されては頭に来る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隠すなら私が気付かないように念入りに隠して……、あるいは気付かない振りが出来るように誤魔化して。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが暗黙のルールだったのに、先に破ったのは彼らのほう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（私の我侭かもしれないけど。\n
それくらい、甘えさせてほしい）"


scene yun_sum_03
with dis

show go_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice gor_f0217
Gowland "「どうした、[firstname]？\n
暗くなったり、笑ったりして……」"

hide go_t_03_1

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドの言葉に顔を拭っていたボリスが私のほうを向く。"


show bor_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0102
Boris "「え？どうしたんだよ、[firstname]。\n
おい、ピアス、どけってっ、邪魔だっ」"

play sound se_0446
camera at hpunch
camera at vpunch
hide bor_t_01_1
show bor_t_01_1 at left
show pia_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0108
Pierce "「ぴぎゃっ！！\n
な、何で、俺蹴られるのっ」"

hide pia_t_01_8
show pia_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0109
Pierce "「ボリス、酷いよ……、あれ、[firstname]。\n
君まで変な顔をしているなんて……、にゃんこにいじめられたの？」"

hide bor_t_01_1
show bor_t_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0103
Boris "「……おまえ、本気で食われたいの？」"

hide pia_t_01_13
show pia_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Pierce "「！！」"

hide bor_t_02_2

hide pia_t_02_3

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ささっと姿を消したピアスの逃げ足の速さは、折り紙付きだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "でも、何故だろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（……皆、元気かな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元気じゃない、無事ではない彼らなんて、想像するのも難しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、こんな賑やかなやりとりを見ていると、つい屋敷のいつもの風景を覗いているような気になってしまう。"


show go_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「……[firstname]？」"

hide go_t_01_11

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「何でもないわ」"


scene bg_gen_sky_sum_nig
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ホームシックなんて、私の柄じゃないし）"
$ fushigi_common3_amuse4_elliot2b_seen = False
menu:
    "皆のことだから、心配いらないもの。":
        jump fushigi_common3_amuse4_elliot2a
    "エリオットなら平気よね。":
        jump fushigi_common3_amuse4_elliot2b

label fushigi_common3_amuse4_elliot2a:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私がいなくとも、皆元気でやっているだろう。"

jump fushigi_common3_amuse4_elliot3
label fushigi_common3_amuse4_elliot2b:
$ fushigi_common3_amuse4_elliot2b = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私がいなくとも、エリオットは元気でやっているだろう。"

jump fushigi_common3_amuse4_elliot3
label fushigi_common3_amuse4_elliot3:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（私がいなくても大丈夫）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "硝煙と血臭。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "以前は恐怖だけを感じていた、危険な滞在地を思い出す空気。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今でも慣れたとは言いがたいそれに、不思議な懐かしさを覚えている。"

$ hi_mes()

scene charasel_bg_amuse_day
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_long
jump fushigi_elliot3_1
