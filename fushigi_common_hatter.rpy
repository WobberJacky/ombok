label fushigi_common2_hatter:
$ hi_mes()

scene map_bg_autumn_day
with dis
$ clockanim()


scene charasel_bg_hatter_day
with dis

play music hatter_gate_p_ali

scene bm_aut_01_2 with Dissolve(1.2)
play sound se_0625
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すっかり通い慣れた道を進めば、やがて大きな屋敷の門が視界に入ってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃弾飛び交うこの世界でも、特に危険度の高い場所。\n
帽子屋ブラッド＝デュプレが率いるマフィア、帽子屋ファミリーの本拠地だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（皆、いるかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "マフィアという仕事柄か、この屋敷の人間は外での仕事も珍しくない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（一度に話すことが出来れば楽なんだけどな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを思いながら進んでいくと、門の前で、退屈そうにしていた小さな影が振り返った。"


show dee_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0351
Dee "「あ、お姉さんだ！\n
兄弟、兄弟、僕達、ついているよ」"

hide dee_t_02_4
show dee_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0352
Dee "「ちょうどこれから休憩っていうタイミングで、お姉さんが遊びに来てくれるなんて！」"

hide dee_t_01_6
show dee_t_01_6 at left
show dam_t_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0353
Dam "「そうだね、兄弟。\n
僕達、いつもの行いがいいからだよ……、ちゃんと給料分働いたご褒美だね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ディー、ダム」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "青と赤の双子の門番、ディーとダム。\n
二人はそれぞれ長い柄のついた斧を持って、ぶんぶんと振り回すように私に示してきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らにしてみれば「早く来て」という合図なのだろうが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "はっきりいって{size=+20}振り回している斧が怖くて、すぐには近付きたくない。{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（悪気がないのは分かっているんだけど……、毎度毎度心臓に悪い光景よね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「え、ええと……、ディー、ダム。\n
こんにちは、仕事中にごめんなさい」"

hide dee_t_01_6
show dee_t_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice dad_f0354
Dee "「気にしないでよ。\n
僕達勤勉な門番だから、これから労働に見合った休憩に入るところなんだ」"

hide dam_t_01_2
show dam_t_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice dad_f0355
Dam "「こうしてお姉さんが来てくれるなんて、ちょうどお客さんもいなくてよかった」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（いないというか……、あなた達が片付けちゃったんじゃないでしょうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "浮かべられた笑顔は無邪気な子供のそれだが、彼らは『ブラッディ・ツインズ』の二つ名を持つ。\n
ファミリーの中でも、相当の実力者達だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "門番を任されている双子は、帽子屋屋敷を訪れるものを片っ端から殺してしまう癖がある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（……今更斬られるとは思わないけど、ちょっと不安が残るのよね。\n
この子達の場合）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私も殺されかけたうちの一人なので、身の危険を感じてしまう。\n
ゆっくりと近付いていくと、彼らの背後からまた別の影が出てきた。"

hide dee_t_01_2
show dee_t_01_2 at left_center
hide dam_t_01_7
show dam_t_01_7 at center
show eri_t_01_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0167
Elliot "「おまえら、またサボりやがって……、お、[firstname]？\n
よく来たな！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「こんにちは、エリオット。\n
あなたが屋敷にいるのって、珍しいわね」"

hide eri_t_01_5
show eri_t_03b_11 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice eri_f0168
Elliot "「ああ、ちょうど外から戻ったところでさ……。\n
ほら、おまえら、いつまでも斧を振り回してんじゃねえよ」"

hide eri_t_03b_11
show eri_t_01_8 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice eri_f0169
Elliot "「近付けなくて、困ってるだろう。\n
悪いな、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子を諌めたのは、帽子屋ファミリーのＮｏ.２。\n
そういえば、彼にも撃たれそうになったことがある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……私、よく生きているわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "初めは恐怖を抱いていた相手だ。\n
しかし、私の視線はついその頭部へと向かってしまう。"

hide dee_t_01_2
show dee_t_03_12 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0356
Dee "「うるさいなあ。\n
ひよこウサギは黙っていろよ」"

hide dam_t_01_7
show dam_t_03_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0357
Dam "「そうそう、いつも同じ台詞しか言えないなんて。\n
これだから単細胞ウサギは困るよね」"

hide eri_t_01_8
show eri_t_02_9 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0170
Elliot "「おまえらな……！\n
だったら真面目に働けっつーんだよこのガキ共！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「えっと……、ひとまず落ち着きなさいよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットの大柄な身体の一番上には、茶色いふさふさとした耳。\n
三人を諌めつつも、私の意識は別のところにあった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_8")
T "（……ああ、可愛い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼がマフィアとは知りつつも、うっとりと見つめてしまう。\n
ぎゅっと掴んでは、彼に嫌がられているのだが、この衝動は止められない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（だって、可愛いんだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、今回はいつまでも門でぼうっとしているわけにはいかない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「突然のお願いで悪いんだけど……。\n
ブラッドに、会えるかしら？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「忙しいなら、少し中で待たせてもらえればと思っているんだけど」"

hide eri_t_02_9
show eri_t_01_12 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice eri_f0171
Elliot "「ブラッド？\n
ああ、ブラッドなら、今ちょうど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屋敷のほうを振り返ると、目的の人物は気配を感じさせないまま現れた。"


show bra_t_02_8 at center
hide dee_t_03_12

hide dam_t_03_15

hide eri_t_01_12
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0309
Blood "「これはいいタイミングで遊びに来てくれたな、お嬢さん」"

hide bra_t_02_8
show bra_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0309_5
Blood "「ちょうどお茶会をするのに客がほしいと思っていたところだ……、本当によく来てくれた」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「ブラッド……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "昼嫌いの家主が表に出てきたことに驚いたが、その目がちらちらと隣の腹心に注がれているのを見て、事情はすぐに分かった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（例によって例の如く、オレンジ色のお茶会が嫌で押し付けたいわけね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「お茶会に招かれるのも悪くはないけど……。\n
一つ、条件を聞いてもらえるかしら？」"

hide bra_t_02_7
show bra_t_03_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice blo_f0310
Blood "「おや、君が私の招待に条件をつけるなんて珍しい。\n
ぜひ聞かせてもらおうじゃないか」"

hide bra_t_03_15

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屋敷の主とその部下達と共に、庭へと案内されながら、私は簡単に状況を話した。"

$ hi_mes()

scene bm_aut_01_1
with stripe_l_medium

play music hatter_garden_p_ali

scene bn_aut_01
with stripe_l_long
play sound se_0038

show bousi_t_01_01 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice may_f0049
Maid "「お待たせしました～」"

hide bousi_t_01_01


show bra_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice blo_f0311
Blood "「どうぞ、お嬢さん。\n
今回は届いたばかりの珍しい茶葉でね」"

hide bra_t_01_2
show bra_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice blo_f0312
Blood "「話も終わったし、のどが渇いただろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「ありがとう、頂くわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "馴染みのメイドさんが淹れてくれたお茶を手にとって、一口含む。\n
爽やかな味わいと自然な甘さに、紅茶のグレードを思わず推し量ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（相変わらず、いい紅茶に目がないわよね、この人も）"

play sound se_0175 volume .3
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分のカップにもさりげなくお代わりを注がせた男は、目の前に並ぶ食べ物から視線を背けている。"


$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（この光景も……、相変わらずよね）"

hide bra_t_03_9


show eri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice eri_f0172
Elliot "「[firstname]、このにんじんパフェも食ってみろって。\n
うまいぜ、この前同じのを街で見かけてさ」"

hide eri_t_01_8
show eri_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice eri_f0173
Elliot "「気に入ったから、うちでも作ってもらったんだ」"

hide eri_t_02_4
show eri_t_02_4 at left
show dee_t_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice dad_f0360
Dee "「……毎度毎度、よく探してくるよね。\n
見ているこっちが飽きちゃった」"

hide dee_t_02_13
show dee_t_02_13 at left
show dam_t_02_13 at right
hide eri_t_02_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice dad_f0361
Dam "「髪の毛だけじゃなくて、肌の色もひよこ色になっちゃえばいいのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぶつぶつと文句を言う双子の手には、オレンジ色に染め上げられていないクッキー。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ブラッドの台詞じゃないけど、確かにこれをずっとやられたら辛いわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも、本人からすれば好意故の行動である。\n
正面から断れない以上、搦め手で断らざるを得ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（まあ、ウサギさんに言っても仕方ないのかもしれないけど）"


play music honobono2_a_ali
hide dee_t_02_13

hide dam_t_02_13


show bra_t_03_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice blo_f0313
Blood "「さて、話をまとめると、こういうことかな。\n
君は、しばらく我が屋敷に滞在したいと？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「そういうこと」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にんじん料理やお菓子を薦めてくるエリオットを軽く流して、頷く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "広い屋敷の庭の中で、ブラッドはどちらともつかない顔で頷いているが、彼の部下達は全員首を縦に振っている。"

hide bra_t_03_16
show bra_t_03_16 at left
show eri_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0174
Elliot "「部屋ならいくらでも空いているし、問題ないよな、ブラッド？」"

hide bra_t_03_16

hide eri_t_01_8


show dee_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0362
Dee "「わあ……。\n
お姉さんがうちに来てくれるなんて、僕達、大歓迎だよ！」"

hide dee_t_02_4
show dee_t_02_4 at left
show dam_t_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0363
Dam "「うん。\n
ざっくざっくお客さんを片付けて、たくさん遊ぼうね、兄弟」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（……ざっくざっく？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一部聞こえた効果音は、とりあえず聞かなかったことにする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、この屋敷において決定権を持つ男は、いつものように気だるげに頷いて、難なく告げた。"


show bra_t_02_4 at center
hide dee_t_02_4

hide dam_t_02_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0314
Blood "「そうだな、君が滞在してくれればいいと思っていたんだ、[firstname]。\n
君がいれば、退屈せずにすむ」"

hide bra_t_02_4
show bra_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0315
Blood "「一時といわず、ずっとでもいいぞ。\n
いっそ、本当に引っ越してきてもらっても構わないんだが……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（よく言うわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "社交辞令にしても、リップサービスがすぎる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この男は気だるげで、やる気を見せようとしない。\n
その実、人の本質を見抜く目利きは確かなものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もっともそうでなければ、マフィアなどやっていられない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "当然、私がいずれ元の場所に戻ると分かっていて、こんなことを言っているのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（しばらくいたとしても、口も手も出さないだろうけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はとても気紛れで、周囲を引っかき回して楽しむ性格だ。\n
しかし、懐に入れたものには存外甘い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（私がその範疇に入るのかは、いまだに分からないけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ありがとう、お言葉に甘えさせてもらうわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らは物騒で、とびきり危険。\n
そんな彼らなりに私に好意を持っていてくれると、もう知っている。"

hide bra_t_02_1

$ hi_mes()

scene charasel_bg_hatter_day
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_medium

if routechara == "Pierce":
    jump fushigi_pierce2_2
if routechara == "Nightmare":
    jump fushigi_nightmare2_2
if routechara == "Gray":
   jump fushigi_gray2_2

label fushigi_common3_hatter:

scene charasel_bg_hatter_night
with dis
$ clockanim()


scene bm_aut_03_1
with dis

play music hatter_garden_p_ali

scene bn_aut_03 with Dissolve(1.2)
play sound se_0544 volume .7
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ねえ、ブラッド」"


show bra_t_03_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice blo_f0322
Blood "「ん？何かな、お嬢さん。\n
改まって」"

hide bra_t_03_16
show bra_t_03_16 at left

show eri_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice eri_f0183
Elliot "「そうだぜ、[firstname]。\n
何だ、にんじんステーキ分けてほしかったのなら、最初から言ってくれれば……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「いらないから、大丈夫よ、エリオット」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（むしろ、話を脱線させないでちょうだい）"

hide bra_t_03_16

hide eri_t_01_3
show eri_t_01_3 at left
show dee_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice dad_f0423
Dee "「うるさいな、ひよこウサギ。\n
お姉さんの話の邪魔をするなよ」"

hide eri_t_01_3
show eri_t_01_3 at left_center
hide dee_t_01_8
show dee_t_01_8 at center
show dam_t_01_9 at right_center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice dad_f0424
Dam "「馬鹿ウサギは放っておいて。\n
お姉さん、話の続きは？」"

play sound se_0161
hide eri_t_01_3
show eri_t_03a_7 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice eri_f0184
Elliot "「おまえらなあ……っ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "空になった皿を掴んだエリオットが立ち上がりかけたが、主が止めに入った。"

hide dee_t_01_8

hide dam_t_01_9

hide eri_t_03a_7
show eri_t_03a_7 at left
show bra_t_02_18 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0323
Blood "「エリオット。\n
お嬢さんの話の途中だ、邪魔をするんじゃない」"

hide eri_t_03a_7
show eri_t_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0185
Elliot "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴたっと。\n
すっかり待ての姿勢で止まっているエリオット。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "強い口調ではなかったが、充分な効果だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（躾が行き届いているわよね）"

hide eri_t_01_10
show eri_t_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
Elliot "「～～～～っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不満げな顔はそのままだが、とりあえずは落ち着いてくれたらしい。"

hide bra_t_02_18
show bra_t_02_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0324
Blood "「それで、お嬢さん。\n
何の話だ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気紛れな主と、屋敷を離れることも多い腹心、そして神出鬼没な双子。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らが全員集まったディナーというこのタイミングで、私は切り出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あのね……」"

if routechara == "Pierce":
    jump  fushigi_common3_hatter2_pierce1
if routechara == "Nightmare":
    jump  fushigi_common3_hatter_nightmare3_gray3
if routechara == "Gray":
   jump fushigi_common3_hatter_nightmare3_gray3

label fushigi_common3_hatter_nightmare3_gray3:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_6")
T "「あなた達だったら……、どんなものをお詫びにあげる？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（この前街までお詫びの品を探しに行ったけど……。\n
男の人って、どんなものがほしいのか、よく分からないんだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この屋敷の人間はみんな個性的だ。\n
少しは参考になる意見が聞けるかもしれない。"

hide bra_t_02_15
show bra_t_03_18 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0334
Blood "「ふむ……。\n
詫び、ねえ……」"

hide bra_t_03_18
show bra_t_03_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0335
Blood "「この私に詫びを入れさせる相手など、そういないからな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（まあ、ブラッドの場合はそうよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むしろこの人があちこちに頭を下げていては、組織が成り立たないし……、何よりも、似合わない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして……、見てはいけないものだとも思う。"

hide eri_t_02_3
show eri_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0247
Elliot "「詫びって言ったら、やっぱり俺は……」"

hide bra_t_03_3
show bra_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0336
Blood "「ああ、おまえはいい。\n
エリオット、皆まで言うな」"

hide eri_t_01_3
show eri_t_02_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0248
Elliot "「へ？」"

hide bra_t_02_3
show bra_t_02_18 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0337
Blood "「おまえの答えなど分かりきっている。\n
その上、ご丁寧にオレンジ色の物体まで手にした状態では……、な」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "溜息をついて、頭を振るブラッドの顔はうんざりしている。"

hide eri_t_02_5
show eri_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0249
Elliot "「だって、詫びを入れるんだろ？\n
だったら、やっぱり自分の好きなものだろうなって」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（エリオットらしいわ）"

hide eri_t_01_5
show eri_t_03a_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice eri_f0250
Elliot "「他に定番といえば……、俺らだったら酒か女か金かってところだけどさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「うーん……。\n
そういうのはちょっとね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らの仕事を考えれば真っ当な（？）詫びの入れ方だろうが、私には向かない詫び方だ。"

hide eri_t_03a_2

hide bra_t_02_18


show dee_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0495
Dee "「僕らだったら何をあげるかな。\n
ただ働きも嫌だし……、どうしようか、兄弟」"

hide dee_t_01_5
show dee_t_01_5 at left
show dam_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0496
Dam "「兄弟、僕達は子供なんだから。\n
大人っていうのは、子供が何かしても笑って許してくれるものだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（この子達らしい回答ね。\n
……ん？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ということは、あまり参考にならなかったっていうことか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕方なく、頭の中に街中で見た品々を思い浮かべるが、どうもぱっとしない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……はあ」"


show bra_t_03_18 at center
hide dee_t_01_5

hide dam_t_02_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Blood "「…………」"

hide bra_t_03_18
show bra_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice blo_f0338
Blood "「詫びなど、要は気持ちの問題だろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「？\n
ブラッド？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "内心肩を落としていると、まるで私の心を読んだタイミングでブラッドが声をかけてくる。"

hide bra_t_03_2
show bra_t_02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0339
Blood "「謝罪の気持ちがあるかないかなど、物だけでは測りきれないさ。\n
なにしろ、渡し方一つで変わってしまうものだからな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「案外、まともなことをいうのね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "正直、常日頃ふざけたところが多いブラッドがまともなアドバイスをするので、驚いてしまった。"

hide bra_t_02_15
show bra_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0340
Blood "「おや、意外かな？\n
まあ、私自身が詫びを入れる機会はなくとも」"

play sound se_0174
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "食後の紅茶を口にしたマフィアのボスはそこで一度言葉を切ると、もったいぶって続けた。"

hide bra_t_03_4
show bra_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0341
Blood "「詫びを入れさせることなら、掃いて捨てるほどあるからな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（それもそうか……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の立場を考えれば、納得する。\n
そう、結局は渡す私と、受け取る相手の問題。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう考えれば、過剰に構えていても仕方ない。"

hide bra_t_01_7
if routechara == "Nightmare":
    jump  fushigi_common3_hatter2_nightmare1
if routechara == "Gray":
   jump  fushigi_common3_hatter2_gray1
label fushigi_common3_hatter2_gray1:
$ fushigi_common3_hatter2_gray2a_seen = False
menu:
    "グレイの役に立てるものなら……。":
        jump fushigi_common3_hatter2_gray2a
    "皆、何だったら喜ぶかしら？":
        jump fushigi_common3_hatter2_gray2b

label fushigi_common3_hatter2_gray2a:
$ fushigi_common3_hatter2_gray2a_seen = True
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「もう一回、街に行ってみようかな」"

$ hi_mes()

scene bn_aut_03
with stripe_l_medium

scene b_aut_03
with stripe_l_medium

scene map_bg_autumn_night with ImageDissolve("gui/stripe_l.png", 1, ramplen=128, reverse=True)

scene map_bg_autumn_day with Dissolve(1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "精一杯の気持ちをこめて、お詫びの品を購入した。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……伝わるといいんだけどな）"

$ hi_mes()

scene map_bg_autumn_eve with Dissolve(1)

scene map_bg_autumn_night with Dissolve(1)
jump fushigi_gray3_1
label fushigi_common3_hatter2_gray2b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「もう一回、街に行ってみようかな」"

$ hi_mes()

scene bn_aut_03
with stripe_l_medium

scene b_aut_03
with stripe_l_medium

scene map_bg_autumn_night with ImageDissolve("gui/stripe_l.png", 1.2, ramplen=128, reverse=True)

scene map_bg_autumn_day with Dissolve(1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの人達が喜ぶかはわからない。\n
それでも、私に出来る精一杯の詫び方を考えて、ようやく決めた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……伝わるといいんだけどな）"

$ hi_mes()

scene map_bg_autumn_eve with Dissolve(1)

scene map_bg_autumn_night with Dissolve(1)
jump fushigi_gray3_1
label fushigi_common3_hatter2_nightmare1:

$ fushigi_common3_hatter2_nightmare2a_seen = False
menu:
    "ナイトメアが受け取りそうなものか……。":
        jump fushigi_common3_hatter2_nightmare2a
    "皆、何だったら喜ぶかしら？":
        jump fushigi_common3_hatter2_nightmare2b

label fushigi_common3_hatter2_nightmare2a:
$ fushigi_common3_hatter2_nightmare2a_seen = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まず最初に考えてしまうのは、ナイトメアのこと。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「もう一回、街に行ってみよう」"

$ hi_mes()

scene bn_aut_03
with stripe_l_medium

scene b_aut_03
with stripe_l_medium

scene map_bg_autumn_night with ImageDissolve("gui/stripe_l.png", 1.2, ramplen=128, reverse=True)

scene map_bg_autumn_day with Dissolve(1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "精一杯の気持ちをこめて、お詫びを決めた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……伝わるといいんだけどな）"

$ hi_mes()
jump fushigi_nightmare3_1
label fushigi_common3_hatter2_nightmare2b:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "皆が喜んでくれそうなものを考える。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「もう一回、街に行ってみよう」"

$ hi_mes()

scene bn_aut_03
with stripe_l_medium

scene b_aut_03
with stripe_l_medium

scene map_bg_autumn_night with ImageDissolve("gui/stripe_l.png", 1.2, ramplen=128, reverse=True)

scene map_bg_autumn_day with Dissolve(1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "精一杯の気持ちをこめて、お詫びを決めた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……伝わるといいんだけどな）"

$ hi_mes()
jump fushigi_nightmare3_1
label fushigi_common3_hatter2_pierce1:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あなた達だったら……、遊園地にあったらいいって思うようなアトラクション、何かあるかしら？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ、この屋敷はマフィアの総本部だ。\n
私の予想外のアイディアが出てくる可能性もあるから、一度聞いてみたいと思っていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（結局、私も仕事から離れられないのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "性分だと自覚しているが、本当に素直じゃない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、彼らは唐突な質問にも、きちんと答えてくれる。"


show eri_t_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0186
Elliot "「アトラクションか……。\n
でも、あの遊園地大抵のものは揃っているからなあ……」"

hide eri_t_01_11
show eri_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0187
Elliot "「アトラクション、アトラクション。\n
……あ、そうだ、いいことを思いついた！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "閃いたというように、エリオットは顔を明るくさせて提案してきた。"

hide eri_t_01_5
show eri_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0188
Elliot "{size=+20}「ブラッドの像を置こうぜ！\n
こう、特大のにんじんを持たせて！！」{/size} "


show bra_t_03_17 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0325
Blood "{size=+20}「ぶはっ！」{/size} "

hide bra_t_03_17
show bra_t_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0326
Blood "「ごほ、げほっ……、何なんだ、それは……。\n
嫌がらせか……っ、げふ、エリオット！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "盛大にむせ返りながらブラッドがぎろりと隣に座った腹心を睨んでいるが、彼にはその意味は通じていない。"

hide eri_t_02_4
show eri_t_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0189
Elliot "「よくあるだろ、偉い奴の銅像って。\n
俺、一度ブラッドのでっっかい像って見てみたかったんだよな」"

play sound se_0198
##special anime"kirakira_left"loop="false"with Dissolve(1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きらきら。\n
陶酔しきった眼でエリオットはブラッドを見ている。"

hide bra_t_01_5
show bra_t_03_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そしてそんな彼は、「助けてくれ」と私を見てきた気がしたが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（あなたで止められない人を私が止められるわけがないでしょうが）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "冷たい私は視線だけで却下した。"

hide eri_t_01_4

hide bra_t_03_6
show bra_t_03_6 at left
show dee_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0425
Dee "「僕、格好よくて、速いのがいいな。\n
この前出来た新しいジェットコースターなんかすごいよかったよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ああ、あれね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「……もう、壊れちゃったけど」"

hide bra_t_03_6

hide dee_t_01_13
show dee_t_01_13 at left
show dam_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice dad_f0426
Dam "「あれは斬新だったよねえ。\n
座席が吹っ飛ぶなんて、画期的だよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（正確には吹っ飛んだんじゃなくて、座席が外れて、落下したんだけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "従業員しか知らない真実である。"

hide dee_t_01_13

hide dam_t_01_13
show dam_t_01_13 at left
show bra_t_01_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0327
Blood "「くだらんな、どうせ悪趣味で、下品な遊園地に出来るものなど、たかが知れている」"

hide bra_t_01_12
show bra_t_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0327_5
Blood "「それぐらいだったら、いっそ紅茶の試飲会でも催したほうが、余程有意義だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（それは、単にあなたの趣味でしょうが）"

hide dam_t_01_13

hide bra_t_03_4
show bra_t_03_4 at left
show eri_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice eri_f0190
Elliot "「俺はブラッドの像がいいと思うんだけどなあ」"

hide bra_t_03_4
show bra_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice blo_f0328
Blood "{size=+20}「却下だ」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（まあ、あれも建てるところまではいいけど、その後の管理が大変だものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "汚れは勝手に落ちるこの世界だが、モニュメントの手入れは意外と大変なのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何よりも……、子供の背丈ほどの高さで作れば落書きはされるし、下手をすれば壊される。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「それ以前に、ゴーランドの遊園地にブラッドの銅像が建つはずがないでしょう。\n
領土争いだけじゃなくて、個人的な恨みだって買っているんだから」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（そんなものを作ったところで、ライフルでぶち壊しかねない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "壊されたら壊されたで、確実にエリオットが怒って、面倒なことになる。"

hide eri_t_01_11
show eri_t_03a_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0191
Elliot "「そういうもんか。\n
難しいぜ、企画とかって俺には畑違いだしなあ」"

hide bra_t_02_10

hide eri_t_03a_2
show eri_t_03a_2 at left
show dee_t_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0427
Dee "「心配しなくても、誰もひよこウサギなんか当てにしていないよ」"

hide eri_t_03a_2

hide dee_t_03_1
show dee_t_03_1 at left
show dam_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0428
Dam "「どうせ、ボスとにんじん以外が浮かぶほど器用じゃないんだから」"

hide dee_t_03_1

hide dam_t_02_2
show dam_t_02_2 at left
show eri_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0192
Elliot "「ブラッドとにんじん料理があれば、どんな奴でも嬉しいに決まってるだろう！\n
なあ、ブラッド！？」"

hide dam_t_02_2

hide eri_t_02_9
show eri_t_02_9 at left
show bra_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

hide bra_t_01_13
show bra_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0329
Blood "「ああ、紅茶だけが私の癒しだ。\n
人の話をまったく聞かないどこかのウサギにこの味を理解しろと言うほうが無謀なこと」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視線を逸らすマフィアのボスは、紅茶で無我の境地に達しようとしているのかもしれない。"

hide eri_t_02_9

hide bra_t_03_2


scene bg_gen_sky_aut_nig
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（参考になったとはいえないけど、仕方ないか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結論としては、あまりアイディアとしてはいいものは得られなかったが、まともな答えが欲しかったわけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分ひとりで考えていてもいい案は浮かばないから、他者の意見を聞こうとしたわけだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（まあ、ここの人間に聞いた段階で、ある程度予想はついていたけどね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「……新しいアトラクションか」"
$ fushigi_common3_hatter2_pierce2b_seen = False
menu:
    "何か考えていってあげようかな。":
        jump fushigi_common3_hatter2_pierce2a
    "ピアス、結局考えたのかしら。":
        jump fushigi_common3_hatter2_pierce2b

label fushigi_common3_hatter2_pierce2a:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何か出来ないか、と。\n
離れていても、つい考えてしまう。"

jump fushigi_common3_hatter2_pierce3
label fushigi_common3_hatter2_pierce2b:
$ fushigi_common3_hatter2_pierce2b_seen = True
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスなら、と。\n
離れていても、つい考えてしまう。"

jump fushigi_common3_hatter2_pierce3
label fushigi_common3_hatter2_pierce3:
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

scene b_aut_01
with stripe_l_medium

scene map_bg_autumn_night
with stripe_l_medium
jump fushigi_pierce3_1
