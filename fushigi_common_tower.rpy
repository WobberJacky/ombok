label fushigi_common2_tower:
$ hi_mes()

scene map_bg_winter_day
with dis
$ clockanim()


play music map_tower_ali

scene charasel_bg_tower_day with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "天高く聳え立つ、緑の塔。\n
クローバーの塔と呼ばれるそれを見つめて、私はほっと息をついた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "会合の時期には当たらないせいか、周囲を歩く職員達も、比較的穏やかな雰囲気を出している。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃弾飛び交う危険な世界でも、ここだけは中立を保っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（まあ、それでも、誰かさんが迷い込んできたりするから、完全に安全とは言えないけど）"

$ hi_mes()

scene cr_01
with stripe_l_long

play music tower_corridor_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「さてと……。\n
いるかしら、皆」"

play sound se_0774
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "作業場にこもることが多いユリウスはともかく、仕事から逃亡を企てるナイトメアやその補佐で多忙なグレイがいるかどうかは分からない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とりあえず、ユリウスの仕事部屋を目指して歩いていたときだった。"


show gre_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0020
Gray "「[firstname]……？\n
また遊びに来てくれたのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「グレイ」"

play sound se_0773
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見慣れた黒い長身の姿に、駆け寄る足取りも軽くなる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、近付いてその手に持った書類の山がはっきりしてくると、私の顔色も変わってしまった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「まさか、それ全部仕事の書類？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（ナイトメアがまた溜め込んだのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが両手に抱えているのは、白い白い山。\n
私が持ったら前が見えなくなってしまうほどの量だ。"

hide gre_t_01_11
show gre_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0021
Gray "「あ……、いや、これは違う。\n
プライベートというか、余暇活動というか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（こんな大量の書類が？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誤魔化そうとするグレイの様子が珍しくて、手の中にある書類を覗き込んでみた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……『包丁の達人レシピ』、『味付け百科』、『健康レシピ』」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（こ、これは、ひょっとしなくても……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっ、とグレイを見つめると、彼は観念したように息を吐く。"

hide gre_t_03_2
show gre_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0022
Gray "「ナイトメア様があまりに頻繁に血を吐かれるから、少しでも身体にいいものを食べて頂こうと思って」"

hide gre_t_02_11
show gre_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0022_5
Gray "「俺はこれから休憩だからな、少し目を通してみるつもりなんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "なんて部下の鏡のような台詞だろうか、（色々な意味で）涙が出そうになる。\n
病院に行かないと駄々を捏ねている誰かさんに聞かせてやりたい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし哀しむべきことは、グレイの料理音痴ぶりはもはや一種の才能という点だろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（本人に悪意があればまだいいんだけど……、この人の場合、本気だからなあ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……グレイ」"

hide gre_t_02_8
show gre_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice gra_f0023
Gray "「この前もきちんと本のとおりにしてみたんだが、どうにもうまくいかなくてな。\n
今回はレポートを中心に集めてみたんだが」"


play music nightmare_t_ali
hide gre_t_03_3
show gre_t_03_3 at left
show nai_s_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0028
Nightmare "「おまえの場合には、テキストの問題じゃないだろう、テキストの！\n
あれはそういう次元じゃないぞ！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ナイトメア」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（いきなり出てこないでよね……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "階段の踊り場で話していた私とグレイの頭上に、ぷかぷかと黒いスーツが浮いていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこから現れたのか、髪にホコリがついている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（またサボっていたのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大方、ひとけのない場所に隠れて煙草でも吸っていたのだろう。"

hide gre_t_03_3
show gre_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0024
Gray "「ナイトメア様、この時間帯は仕事ではありませんでしたか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「あなたのサボり癖はグレイの料理を責められるものじゃないわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どちらも治りそうにないが、努力を試みている分、グレイのほうが偉い。\n
二人で、責める視線を投げると、ナイトメアは言葉を詰まらせた。"

hide nai_s_01_8
show nai_s_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0029
Nightmare "「うっ、うるさい！\n
私がサボっているんじゃなく、仕事が多すぎるんだっ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「仕方ないでしょう、あなたは塔の領主なんだから……。\n
ナイトメアにしか出来ない仕事が多いのは当然だわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「大体グレイに押し付けて逃げているんだから、たいして仕事なんてしていないじゃないの」"

hide gre_t_01_5
show gre_t_03_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice gra_f0025
Gray "「彼女の言うとおりですよ。\n
俺がいなくなるとすぐに逃げ出すんですから、料理を作っている暇もありません」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（それは……、なくてもいいけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たまに好意で差し出されるナイトメア用の健康食（ものすごい色だ）を思い出した。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が思い浮かべたものはどうやら心を読むナイトメアにも伝わってしまったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただでさえ青い顔色から血の気を引かせている。"

hide nai_s_02_6
show nai_s_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0030
Nightmare "「いいか、グレイ。\n
人には得手不得手があるんだから、料理音痴のおまえが料理を作る必要はないんだっ」"

hide nai_s_02_9
show nai_s_03_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0031
Nightmare "「むしろ、あれを食べるほうが天国に近くなる気分だぞ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（……否定できない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすが、食べさせられ続けている人は言うことに説得力がある。\n
命がけとなれば、誰でも必死だろう。"

hide nai_s_03_5
show nai_s_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0032
Nightmare "「うう、分かってくれるか、[firstname]。\n
君はいい子だなあ」"

hide nai_s_02_8
show nai_s_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0033
Nightmare "「今回も私に会いに来てくれたんだろう？\n
歓迎するよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「あ、違うの。\n
特に誰ってわけでもないんだけど……」"

hide gre_t_03_8
show gre_t_02_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Gray "「？」"

hide nai_s_01_1
show nai_s_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice nig_f0034
Nightmare "「ふむ、話が色々複雑なようだな。\n
立ち話もなんだ、ゆっくり座って聞こうじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（……こういうとき、ナイトメアの能力は便利よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心を察してくれる彼がいれば、説明は簡単に終わりそうだ。"

play sound se_0384
hide gre_t_02_9

hide nai_s_02_12

$ hi_mes()

scene charasel_bg_tower_day
with stripe_l_medium

play music tower_room1_p_ali

scene ts_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "諸々の説明が終わり、最初に口を開いたのはユリウスだった。"


show yuri_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0013
Julius "「話は分かったが……。\n
どうしてわざわざ私の部屋でそんな説明会をする必要があったんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「だって、ここならユリウスにも話を聞いてもらえるし」"

hide yuri_t_01_12
show yuri_t_01_12 at left
show nai_s_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice nig_f0035
Nightmare "「何よりもあの場から一番近かったからな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言葉を継ぐ形で口を挟んだナイトメアに、彼は呆れた眼差しを向けると顔を背けてしまう。"

hide yuri_t_01_12
show yuri_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0014
Julius "「…………。\n
勝手にしろ」"

play sound se_0480
hide yuri_t_03_10

hide nai_s_02_11

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その言葉を最後に彼は修理中の時計に向いたが、私が事情を話している間、その手を止めていてくれたことに気付いていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（だって、出て行けとは言わなかったものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは無愛想に見えて、人を放っておけない優しさを持っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何も言わず、聞かず、傍にいてくれるから、私は彼と共にいる時間帯に安らぎを感じるのだ。"


show gre_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0026
Gray "「客室なら空いている。\n
好きな場所を使ってもらって構わない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「ありがとう、グレイ。\n
お世話になるわね」"

if routechara == "Peter":
    jump fushigi_common2_tower2_peter
if routechara == "Gowland":
    jump fushigi_common2_tower2_amuse
if routechara == "Boris":
    jump fushigi_common2_tower2_amuse

label fushigi_common2_tower2_peter:
hide gre_t_03_9
show gre_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0027
Gray "「気にしないでくれ。\n
君がいてくれると、俺も嬉しい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "反省したいと言った私に「ナイトメア様もそれぐらい殊勝でいてくだされば」と本音が漏れていたことは、聞かなかったことにした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアがつまらなそうに口を挟む。"

jump fushigi_common2_tower3
label fushigi_common2_tower2_amuse:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地であったことを気の毒に思っているのか。\n
グレイも好意的に受け入れてくれた。"

hide gre_t_02_2
show gre_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0027
Gray "「気にしないでくれ。\n
君がいてくれると、俺も嬉しい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頷いてくれるグレイに答えていると、ナイトメアがつまらなそうに口を挟む。"

if routechara == "Gowland":
    jump fushigi_common2_tower3
if routechara == "Boris":
    jump fushigi_common2_tower3


label fushigi_common2_tower3:

show nai_s_03_8 at right
hide gre_t_02_2
show gre_t_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0036
Nightmare "「おい、こら！\n
この塔の主は私なんだぞ、私抜きで話を進めるんじゃないっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（まさか、ナイトメア……。\n
この期に及んで出て行けなんて言わないでしょうね？）"

hide nai_s_03_8
show nai_s_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0037
Nightmare "「……言うわけがないだろう。\n
君は私にとっても大切な友人だ」"

hide nai_s_02_9
show nai_s_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0038
Nightmare "「君の力になれるのなら、ずっといてくれてもいい。\n
自分の家のつもりで寛いでくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T "「……ありがとう」"

hide nai_s_01_1

hide gre_t_02_2

$ hi_mes()

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_long

if routechara == "Peter":
    jump fushigi_peter2_2
if routechara == "Gowland":
    jump fushigi_gowland2_2
if routechara == "Boris":
    jump fushigi_boris2_2

label fushigi_common3_tower:
$ hi_mes()

scene charasel_bg_tower_day
with dis
$ clockanim()


play music tower_t_ali

scene bg_gen_sky_win_day with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0092
Nightmare "「グレイ……。\n
いくら何でもこの状況はどうかと思うぞ……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0093
Nightmare "「おまえは、尊敬する上司を一体何だと思っているんだ！？\n
うう……、足が冷える、びりびりする」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0035
Gray "「尊敬していますよ、もちろん。\n
ですが、これ以上仕事を溜められるなら、手段なんて選んでいられません」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どんとナイトメアの前に積まれた書類を嘆かわしそうに見ながら、グレイは言う。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0036
Gray "「ノルマが終わったら、部屋に戻して差し上げますが、それまではここで仕事をしてください」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0036_5
Gray "「足が痺れて立てなかったら、負ぶってでも戻してあげますから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0094
Nightmare "{size=+20}「……それだけは絶対に嫌だ\n
！！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0015
Julius "「騒がしい……、私の部屋を間借りするなと何度言ったら分かるんだ、おまえらは。\n
邪魔だ、とっとと出ていけ！」"

play sound se_0455

play music tower_room1_p_ali

scene ts_01
with dis

show gre_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0037
Gray "「間借りには違いないが、少なくともこの姿勢ならいつものように脱走も出来ないことは証明されている。\n
協力しろ、時計屋」"

hide gre_t_02_13
show gre_t_02_13 at left
show toustaff_a1_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0009
Tower_Employee "「この前も逃亡されたばかりですからね。\n
いい加減仕事を進めて頂かないと、他にも影響が出てしまいます」"

hide gre_t_02_13

hide toustaff_a1_11
show toustaff_a1_11 at left
show toustaff_b1_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0007
Tower_Employee "「というよりも……。\n
正確には、もう出ているんですよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同時に溜息をついたナイトメアの部下を見ながら、ユリウスは嫌そうに顔を顰めている。"


show yuri_t_01_8 at center
hide toustaff_a1_11
hide toustaff_b1_7
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0016
Julius "「まったく……。\n
私の部屋は独房でもなんでもないんだぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「……確かに、正座していたらすぐには立てないだろうから、逃亡防止にはいいかもしれないわよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "床の上に直に座らせられて、正座をしているナイトメアを見ていると、溜息が漏れた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（あれじゃ、初等部のお子様にする罰と大差ないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隣にいるグレイが立っている今の様子は、まるで教師と怒られている生徒の構図のようにも見える。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（でもよくいる鬼教師のようにお仕置きと称して、教鞭で理不尽に叩かれたりはしないだけマシなのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少なくともナイトメアは痛がっていないし（足は痺れていても）、彼の目の前にあるものが書類である以上、あれは彼の役割であってお仕置きにはならない。"

hide yuri_t_01_8
show yuri_t_01_8 at left
show nai_s_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0095
Nightmare "「ちっともマシじゃない！！\n
この仕事の山だぞ、罰ゲーム以外の何だというんだっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「でも溜めたのは、あなただし……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むらっ気があるナイトメアの仕事の進行が不安定だということは、私もよく知っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイは私以上に分かっているから、この缶詰体制を思いついたのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（まあ、正直ちょっとは同情するけど……）"

hide nai_s_02_6
show nai_s_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice nig_f0096
Nightmare "「うう、同情されるとは格好悪い……。\n
早く終わらせてあったかい布団の中に入りたい……」"

hide yuri_t_01_8
show yuri_t_01_8 at left_center
hide nai_s_01_10
show nai_s_01_10 at center
show gre_t_02_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice gra_f0038
Gray "「そうですよ、ナイトメア様。\n
あなたはやれば出来る方なんですから、その力を今こそ発揮してください」"

play sound se_0531
pause .3
play sound se_0529
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイは張り切って大量の書類をナイトメアの横に積み上げている。\n
これではナイトメアが温かい布団に入れるのは、かなり先になりそうだ。"

hide yuri_t_01_8
show yuri_t_03_12 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0017
Julius "「私の仕事場は、軟禁場所か……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの部屋は彼にとって必要なものがあるだけだ。\n
ナイトメアの気を逸らすようなものは何もない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（確かにここなら仕事以外のことは何も出来なさそうよね）"

if routechara == "Peter":
    jump  fushigi_common3_tower2_peter1
if routechara == "Gowland":
    jump fushigi_common3_tower2
if routechara == "Boris":
    jump fushigi_common3_tower2

label fushigi_common3_tower2:
hide gre_t_02_2

hide yuri_t_03_12

hide nai_s_01_10


scene bg_gen_sky_win_day
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……仕事、か）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "脳裏に過ぎったのは、あのとき、無残にぼろぼろにされた企画書。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドの遊園地には、既に奇をてらったアトラクションが山のようにある。\n
むしろ、ノーマルなものを探すほうが難しいぐらいだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（新しい企画って、結局、決まったのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飛び出してきてしまったので、迷惑もかけてしまっている。\n
僅かながらよぎる罪悪感に、かぶりを振った。"


scene ts_01
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（折角考えた企画書だったもの。\n
……でも、遊園地に戻るまでには、何か考えなくちゃ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一度台無しにされたとはいえ、放り出す気はない。"


show yuri_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0107
Julius "「どうした、[firstname]？\n
何かあったか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ううん……。\n
遊園地に新しいアトラクションを作るなら何がいいかなって考えていたんだけど……」"

hide yuri_t_02_10
show yuri_t_02_10 at left
show nai_s_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice nig_f0210
Nightmare "「そうだな……。\n
私だったら、動物との触れ合いコーナーだなあ」"

hide nai_s_02_12
show nai_s_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice nig_f0211
Nightmare "「無邪気な生き物と、ぬくぬく癒されるなんていいだろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事以外の話題に食いついてきたナイトメアに、グレイが同意する。"

hide yuri_t_02_10

hide nai_s_01_13
show nai_s_01_13 at left
show gre_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0071
Gray "「それは……、いい案ですね。\n
可愛い生き物で癒される空間……、ああ、考えるだけでも癒される」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ほわほわとした顔で塔の主従は天井を見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私にはただの時計塔の天井にしか見えないが、彼らにはきっといくつもの動物の影が見えているのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（グレイが癒しを求めるのは分かるけど。\n
ナイトメアに必要なのは、精神的な癒しじゃなくて、治療でしょうが）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの病弱さは、どんな怪我も時間帯さえ経過すれば完治するこの世界では異質だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくら病院を薦めても、行こうともしない。"

hide nai_s_01_13

hide gre_t_01_8


show yuri_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0108
Julius "「下らん。\n
どうせどんなものを考えたところで、あの遊園地に作られた時点で、別物になっているだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……何だか、経験があるような口振りだけど。\n
ユリウス、何か手伝ってあげたことがあるの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こと設計や物作りという分野において、彼以上に器用な人を私は知らない。\n
アトラクションの制作に彼が関わったとしたら、それはすごいものが出来そうだ。"

hide yuri_t_01_3
show yuri_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0109
Julius "「一度だけ……、上手く設計できないと言うから、仕方なく手伝ってやったが」"

hide yuri_t_03_13
show yuri_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0109_5
Julius "「螺子は吹っ飛ばすし、勝手に資材を変えられたせいで、十時間帯と経たずに壊れた」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「……それは、酷い話ね」"

hide yuri_t_02_9
show yuri_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice jul_f0110
Julius "「ああ、二度と奴の仕事は手伝わないと心に決めたな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "職人気質のユリウスなら、自然な反応だろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（何を考えているのよ、あのオーナーは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼のことだ、より遊び心のあるものを目指した果ての暴走だったのだろうが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……ユリウスが設計したものなら、余程のことでもない限り壊れそうもないけど。\n
一体何をしたのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのときの惨状を知らなくてよかったと思ってしまうあたり、この世界に慣れたものだと思う。"

hide yuri_t_02_7


show gre_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0072
Gray "「どうせなら癒される動物がいいですよね。\n
猫もいいし、ウサギもいい……、ああ、タヌキやキツネというのも可愛いだろう」"

hide gre_t_01_7
show gre_t_01_7 at left
show nai_s_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0212
Nightmare "「そうだな、元々あの遊園地には猫とネズミがいるんだ。\n
ちょっと動物を足すだけでも、十分動物園になるじゃないか」"

hide nai_s_02_1
show nai_s_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0213
Nightmare "「アニマルセラピーの効果を体験するには、最高の環境かもしれない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "{size=+20}（だから、そういう精神的な癒しじゃなくて、あんたの場合はまず病院でしょうが）{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（身体を治してから、精神の癒しを求めなさいって）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもなら私の心の声に反応するナイトメアは、まだほわほわとした顔で現実逃避を続けている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手元の仕事が進んでいないことにグレイが気付くのも間もなくだろう。"

hide gre_t_01_7

hide nai_s_03_11


scene bg_gen_sky_win_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「……新しいアトラクションか」"

if routechara == "Gowland":
    jump fushigi_common3_tower2_gowland1
if routechara == "Boris":
    jump fushigi_common3_tower2_boris1
label fushigi_common3_tower2_gowland1:
$ fushigi_common3_tower2_gowland2a_seen = False
menu:
    "何か考えていってあげようかな。":
        jump fushigi_common3_tower2_gowland2a
    "ゴーランドならどんなものを考えるかしら？":
        jump fushigi_common3_tower2_gowland2b

label fushigi_common3_tower2_gowland2a:
$ fushigi_common3_tower2_gowland2a_seen = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何か出来ないか、と。\n
離れていても、つい考えてしまう。"

jump fushigi_common3_tower2_gowland3
label fushigi_common3_tower2_gowland2b:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドなら、と。\n
離れていても、つい考えてしまう。"

jump fushigi_common3_tower2_gowland3
label fushigi_common3_tower2_gowland3:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（何だかんだいっても、すっかり遊園地の住人なのね、私は）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "戻ることを前提としてしまっている。"

$ hi_mes()

scene bg_gen_sky_win_day with Dissolve(.8)

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium
jump fushigi_gowland3_1
label fushigi_common3_tower2_boris1:
$ fushigi_common3_tower2_boris2b = False
menu:
    "何か、考えていってあげようかな。":
        jump fushigi_common3_tower2_boris2a
    "ボリスは、また魚関連かしら？":
        jump fushigi_common3_tower2_boris2b

label fushigi_common3_tower2_boris2a:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何か出来ないか、と。\n
離れていても、つい考えてしまう。"

jump fushigi_common3_tower2_boris3
label fushigi_common3_tower2_boris2b:
$ fushigi_common3_tower2_boris2b = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスなら、と。\n
離れていても、つい考えてしまう。"

jump fushigi_common3_tower2_boris3
label fushigi_common3_tower2_boris3:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（何だかんだいっても、すっかり遊園地の住人なのね、私は）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "戻ることを前提としてしまっている。"

$ hi_mes()

scene bg_gen_sky_win_day with Dissolve(.8)

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium
jump fushigi_boris3_1
label fushigi_common3_tower2_peter1:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_9")
T "「……くしゅんっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「あれ？」"


show nai_s_01_3 at center
with dis




$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
Nightmare "「！！」"

hide nai_s_01_3
show nai_s_01_3 at left
show gre_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice gra_f0039
Gray "「[firstname]、どうしたんだ？\n
君、顔が真っ赤じゃないか、熱でもあるのか！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（熱？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「そんなにいうほど赤いかしら？\n
まさかそんな……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイの気遣う言葉にきょとんしたのは私のほうだ。\n
確かに少し温かい気もするが、高熱というほどではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（それに風邪をひくようなことも、思い当たら……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（あった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城での水撒き事件。\n
確かに濡れたメイド服でふらふらとしていたことは事実だが、まさかあれが原因だろうか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「平気よ、平気。\n
大したことなんか」"

hide nai_s_01_3

hide gre_t_02_4
show gre_t_02_4 at left
show yuri_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice jul_f0018
Julius "「笑っている場合じゃないだろう。\n
見せてみろ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「あ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の額に触ったユリウスは、眉間に皺を寄せて首を横に振った。"

hide yuri_t_02_9
show yuri_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0019
Julius "「……やっぱりな。\n
微熱と言える温度じゃない、さっさと休め」"

hide gre_t_02_4
show gre_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0040
Gray "「おい、すぐに医者の手配を。\n
……って、ナイトメア様までどうして逃げるんです？」"

play sound se_0052
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "医者という単語に私よりも素早く反応したのは、病弱を代表する夢魔だ。\n
部下に首根っこを押さえられたままの姿勢で、ナイトメアは慌てて弁明し始めた。"

hide gre_t_03_11

hide yuri_t_02_11


show nai_s_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0097
Nightmare "「いや、私は彼女の部屋の準備を手伝おうかと……。\n
女性を休ませるんだ、何か不手際があってはいけないだろう」"

hide nai_s_03_7
show nai_s_03_7 at left
show gre_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0041
Gray "「少なくとも、この塔の人間で病人慣れしていないのは、当の病人ご本人だけです」"

hide gre_t_01_13
show gre_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0041_5
Gray "「……部屋まで送ろう、大丈夫か、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「……大袈裟にしなくていいのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスから私を受け取ったグレイは、手を引いて歩き出そうとしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まるで重病人の扱いだと思っていると、私から手を離したユリウスが呆れたように言った。"

hide nai_s_03_7
show nai_s_03_7 at left_center
hide gre_t_03_3
show gre_t_03_3 at center
show yuri_t_03_4 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0020
Julius "「いいから寝てこい。\n
トカゲが言うように、ここの連中は看病には慣れているから安心して休めるだろう」"

hide nai_s_03_7
show nai_s_01_11 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0098
Nightmare "「時計屋の言うとおりだ。\n
こういうときぐらいしか、君はゆっくり休めないだろう」"

hide nai_s_01_11
show nai_s_02_2 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
voice nig_f0099
Nightmare "「少しぐらい、面倒を見させてくれ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここまで言われて、固辞すればかえって彼らに悪いだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（せっかくだから、甘えさせてもらおうかな）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_8")
T "「ありがとう、じゃあお世話になります」"

hide gre_t_03_3

hide yuri_t_03_4

hide nai_s_02_2

$ hi_mes()

scene charasel_bg_tower_day
with stripe_l_medium

play music gray_t_ali

scene cg_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ああ、失敗したわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大したことはないと思っていた熱は、時間帯が変わる前に高熱へと変わっていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭の下に敷いた氷枕の冷たさを感じるよりも、頬にたまった熱を意識してしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "医者に診てもらったあと、眠っていた意識がようやく浮上してきたのだが、耳慣れない音に目を開いた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "病人の部屋にいたのは、三人の男性。\n
そのうち二人が同じような姿勢でリンゴを持って、皮を剥いていた。"

play sound se_0357
pause 1
play sound se_0357

show gre_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

play sound se_0357
pause 1
hide gre_t_02_11
show gre_t_02_11 at left
show yuri_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

play sound se_0083
hide yuri_t_03_11
show yuri_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0021
Julius "「トカゲの食生活は知らんが、こいつはりんごの芯を食うような女じゃない。\n
いい加減諦めたらどうだ」"

hide gre_t_02_11
show gre_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0042
Gray "「ナイフは使い慣れているはずなんだが……。\n
なぜ、俺のりんごはどんどん実が削れていくんだ？」"

hide gre_t_03_11
show gre_t_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0043
Gray "「時計屋のりんごは普通に剥けているんだから、りんごの差ではないと思うんだが」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "りんごの実を大きく抉って皮を剥いたグレイと、対照的に薄皮一枚だけ剥きあげたユリウス。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼自身がいうようにナイフの扱いならば、グレイには慣れたもののはずなのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（ここまで行くと、本当に才能よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベッドに潜り込んだままそんなことを思う。"


show nai_s_03_6 at center
hide gre_t_01_6
hide yuri_t_01_13
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0100
Nightmare "「それは、手先の器用な時計屋とおまえを一緒にしたら罰当たりというか……」"

hide nai_s_03_6
show nai_s_03_7 at left
show gre_t_02_13 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「！」"

hide nai_s_03_7
show nai_s_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0101
Nightmare "「睨むな、睨むな。\n
人には得手不得手があるんだ、りんごの皮が剥けなくても、別に今まで困りはしなかっただろう？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（まあ、確かにあなたにりんごを剥いてもらおうとは思わないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアではかえって自分の指まで切ってしまいかねない。"

hide nai_s_03_3
show nai_s_02_9 at center
hide gre_t_02_13
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0102
Nightmare "「うっ……、酷い。\n
私だって、君のために精いっぱい頑張ったのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "訝しむ私に、ユリウスと睨み合っているグレイを見つめながら、彼は小さな声で囁いてくる。"

hide nai_s_02_9
show nai_s_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0103
Nightmare "「君に栄養をつけさせようとするグレイの好意を、どれだけ必死に止めたと思う？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "{size=+20}「ありがとう、ナイトメア」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイの心遣いには感謝するが、気持ちだけで充分すぎる。"

hide nai_s_01_12


scene bg_gen_sky_win_day
with dis

play music heartrending_a_ali
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（それにしても風邪なんてひいたの、久しぶり）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも、寝込むほど酷いものは子供のとき以来ではないだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（城の皆も結構派手に濡れていたわよね。\n
風邪をひいていなければいいけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そろそろ戻ろうかと思っていたのに、こんな状態で帰ればかえって心配をかけてしまうだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、心配をかける程度ならまだいいが、変な言い掛かりをここの人達に向けかねない。"
$ fushigi_common3_tower2_peter2b_seen = False
menu:
    "そういうところだけは仲がいいものね。":
        jump fushigi_common3_tower2_peter2a
    "ペーターならやりかねない。":
        jump fushigi_common3_tower2_peter2b

label fushigi_common3_tower2_peter2a:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "皆のことを考えてしまう。"

jump fushigi_common3_tower2_peter3
label fushigi_common3_tower2_peter2b:
$ fushigi_common3_tower2_peter2b_seen = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まず最初に考えてしまうのは、ペーターのこと。"

jump fushigi_common3_tower2_peter3
label fushigi_common3_tower2_peter3:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（身体の調子が戻るまでは、帰らないほうが皆のためかもしれないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "万が一誰かに感染してしまったら、目も当てられない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何のために城の外に頭を冷やしに来たのかわからなくなってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……別の意味で、頭を冷やすことになっちゃったけど）"


scene cg_01
with dis

show nai_s_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice nig_f0104
Nightmare "「ん？\n
どうしたんだ、[firstname]？」"

hide nai_s_01_2
show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice nig_f0105
Nightmare "「溜息なんかついて。\n
風邪で寝込むぐらいなんだというんだ」"

hide nai_s_01_11
show nai_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice nig_f0106
Nightmare "「私なんて、いつも吐血しては倒れているんだぞ。\n
それに比べれば、君の体調不良なんて可愛いものじゃないか」"

hide nai_s_02_3
show nai_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice nig_f0107
Nightmare "「……もう少し図々しくなっていいんだよ、君は」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「あんたはもう少し謙虚さを覚えなさいよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（威張って言うことじゃないでしょう、そのどれも）"

hide nai_s_03_10

$ hi_mes()

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium
jump fushigi_peter3_1
