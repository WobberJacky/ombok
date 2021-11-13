label fushigi_joker_2:
scene map_bg_joker_day
with dis
$ clockanim()


scene circus
with dis

play music gag2_a_ali

scene bg_gen17_cst_a with Dissolve(1.2)

show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_f0107
White_Joker "「一歩ずつ進んでごらん。\n
そう、最初は右……、うん、いいね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「い、いいの……？\n
これで本当に？」"

hide jo_t_03_1
show jo_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0108
White_Joker "「うん、ちゃんと動いているだろう、[firstname]。\n
おっと……、気を付けないとバランスが崩れるよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視界がぐらりと傾きかけたところで、元に戻る。\n
とはいえ、自力で戻したわけではない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「あなたの手がなければ、とても動けそうにないんだけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（それどころか、手を離された瞬間に落ちそうだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足下はふわふわと頼りなく、いくら踏みしめようにも沈んでいくような不確かさがある。"


show t_jo2_1and2_3 onlayer master
with dis
hide jo_t_01_11

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0109
White_Joker "「玉乗りならいいって言っただろう、[firstname]？\n
気に入らないなら、別の演目でもいいけど……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「……いいえ、まだこっちのほうがいいわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "空中ブランコも、綱渡りも高さが半端無い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（だからといってナイフ投げやジャグリングみたいな刃物を使うものなんか、有り得ないし）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jok_f0110
White_Joker "「そう？気が変わったならいつでも言っていいよ。\n
せっかく君がその気になったのに、応えられないなんてつまらないからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（別にその気になったっていうわけじゃないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひねた性格がすべての原因だ。\n
別に玉乗りを本気でマスターしようなんて思っていない（当たり前だが）。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段は外側から見ている、舞台という別の空間、それに惹かれてしまったのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0111
Black_Joker "「そんなへっぴり腰で転がせるわけがねえだろうが。\n
背筋を伸ばせよ、背筋」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（誰も、二人がかりで教えてほしいなんて頼んでいないのに……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ホワイトさんは一応手を引いてくれるが、ブラックさんときたら野次を飛ばしたり、「なってねえ」と言うばかりで手は一切出してこない。\n
代わりに、口ばかり出す。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0112
White_Joker "「そう言うなら、ジョーカーが手を引いてあげればいいだろう？\n
せっかく、エスコートが出来る機会だけど、譲ってあげようか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0113
Black_Joker "「冗談いうなよ。\n
そんなガキのお守りなんかしねえって言っただろうが」"

$ hi_mes()
hide t_jo2_1and2_3


$ time_effect()##PLEASE MANUALLY ADJUST ME

play music gag4_a_ali
pause .5
show t_jo2_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（悔しいけど……、さすがに言うだけあって上手いわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラックさんは一人で玉に乗ったまま、舞台の上を優雅に動いている。\n
そう、大きな玉乗りをしているだけなのに、優雅に見えるのだ、これが。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカス以外の場面で見ても、おかしな光景としか映らないだろうが、さすがにこの場では降り注ぐスポットライトの影響もあって、様になっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（……口が悪い上に、欠伸までしているような男なのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "伊達にサーカスの団長ではないということだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーに手を持ってもらってようやく立っている私が憎まれ口を叩いても、負け惜しみにしかならない。"

hide t_jo2_2
show t_jo2_1and2_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0114
White_Joker "「心配いらないよ、[firstname]。\n
こういうものはコツがあるんだから、それさえ分かればすぐだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「コツねえ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よたよた、よろよろ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今にもバランスを崩して倒れそうになるこの状況で、そう簡単にそんなものが悟れるとも思えないのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（……でも、どうしてだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "玉乗りを始めてまだ一時間帯と経っていない。\n
飽きるほどの長さではないが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの私だったら、そろそろ見切りを付けてやめると言っていてもおかしくないはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（なんだか、楽しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "立った姿勢を維持するのはうまくいかないし、適当なタイミングで下りてしまいたいとさえ思う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、それと同じぐらいに、こうして手を取られていることが、楽しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "うまくいかない私を馬鹿にする声を聞いて、一瞬むっとするが、それ以上に楽しくなってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……馬鹿にされて、喜ぶような変な趣味はないはずなんだけど。\n
え、なに、私、そういう性格していたっけ？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
White_Joker "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「なに……？\n
？？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "唯一の支えだったはずの手が、いつの間にか私の手を離していた。"

hide t_jo2_1and2_3
show t_jo2_4and2_7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "{size=+20}「！！？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「きゃあああっ！？？？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慌てて足をばたばたと動かすが、一度崩れた体勢はそう簡単に戻らない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ジョーカー！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仰け反り、前のめりになり……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_9")
T "（倒れる！\n
というか、落ちる！！）"

hide t_jo2_4and2_7
show black onlayer master with close_medium
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぎゅっと目を閉じたときだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0115
White_Joker "「[firstname]？\n
大丈夫だよ、ほら、目を開けてごらん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

hide black with close_m
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……あ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐらんぐらんと揺れていた身体は、いつのまにかジョーカーの腕の中に収まっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（あ、ボール……。\n
転がっていっちゃった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "乗り手を失ったボールは舞台の上を転がっていく。"


show jo_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jok_f0116
Black_Joker "「まったく、素人とはいえ、おまえ下手すぎるぜ。\n
このジョーカー様のサーカスで練習する以上、もう少しまともになれよな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ころころと転がっていったボールを片足で止めると、ジョーカーは呆れたように言った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま軽く蹴り飛ばして、私のほうへと返してくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どういう仕掛けなのか、ボールは私達の乗っている台の手前までやってくると、自動的に止まった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（ジョーカーが何かしたのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思って横にある顔を見上げると、彼はいつもと変わらぬ笑みを浮かべている。\n
私の意図に気付いていないのか、とぼけているのか。"

hide jo_t_02_2
show jo_t_02_2 at left
show jo_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0117
White_Joker "「ん？少し疲れたかな？\n
休憩にしようか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "笑顔の道化師は、そう告げて台の上から私と共に下りたのだった。"

hide jo_t_02_2

hide jo_t_01_3
with dis
$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME

play music hospital_p_ali

scene bg_gen18_cgu
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舞台から下りて案内された場所は、いわゆる楽屋だった。\n
雑多に置かれた物と物の間に、ぬいぐるみや玩具のような道具が見える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "中には一体何に使うのか分からないような、怪しい道具も置いてあるが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（あれも、サーカスのネタに使うものなんだろうけど、放置しすぎじゃないの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "猛獣相手に使うと思われる鎖や鞭、演出用の楽器まで、仕分けもされず乱雑に混ざってしまっている。"


show j-boy_a_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0029
Danin "「ジョーカーは、飲み物、何がいい？」"

hide j-boy_a_14
show j-boy_a_14 at left
show jo_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0118
White_Joker "「何でもいいよ。\n
ジョーカーは？」"

hide j-boy_a_14

hide jo_t_01_11
show jo_t_01_11 at left
show jo_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0119
Black_Joker "「俺も、別に何だって構わねえよ。\n
まったく、余計なのが来たおかげで、片付けが少しも進みやしねえ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「……悪かったわね。\n
迷惑なら、すぐに消えるわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "玉の上から下りたことも手伝ってか、売り言葉に買い言葉。\n
思わず反論した私の傍にいた女の子が、困ったように間に入ってきた。"


show j-girl_a_11 at center
hide jo_t_01_11
hide jo_t_02_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0020
W "「そんなこと言わないでよ。\n
まだいてよ、ね？」"

hide j-girl_a_11
show j-girl_a_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0021
W "「ねえ、あなたは何がいい。\n
欲しいものがあれば、持ってくるわ、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（こんな小さい子にまで気遣われるなんて……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすがに大人げなかったらしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ありがとう、皆と同じでいいわ」"

hide j-girl_a_3
show j-girl_a_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice nos_f0022
W "「うん、分かった」"

hide j-girl_a_2
show j-girl_a_2 at left
show j-boy_a_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice mat_f0030
Danin "「じゃあ、向こうで準備してくるね」"

play sound se_0415
hide j-girl_a_2
hide j-boy_a_3
with dis
play sound se_0417
pause 1
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "走り去っていく子供達を見送っていると、「さて」とジョーカーが切りだした。"


show jo_t_03_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice jok_f0120
White_Joker "「それで、玉乗りは上達出来そうかな、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「別に上達はしなくてもいいんだけど……。\n
ここにこのまま住むわけでもないし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスの団員に加わるのであれば、一つぐらい持ち技がないとまずいだろうが、私にその気はない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "戻るのは、帰ろうと思うのは、物騒でも大事な……、あの場所だから。"

hide jo_t_03_16
show jo_t_03_16 at left
show jo_t_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0121
Black_Joker "「ふうん、その割にはムキになってやっていたように見えたがな。\n
不器用なのに、よくやるぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「確かに器用じゃないけど……、別に運動音痴っていうほどじゃないわよ」"

hide jo_t_03_16
show jo_t_01_14 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice jok_f0122
White_Joker "「そうだね、乗せたばかりのときには手どころか、抱きつく勢いだったのが、最後は手の支えだけで大丈夫になったし」"

hide jo_t_01_14
show jo_t_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice jok_f0123
White_Joker "「もっとも、俺としては、抱きつかれたままでも悪くなかったんだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「し、仕方ないでしょうっ。\n
あんな不安定な物に乗せられたことなんか、今まで一度もなかったんだから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地の乗り物も不安定といえば不安定だが、あれには一応足場がある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まして、中に空気だけが詰め込まれたボールの上に乗せられて、さあ動けと言われても思ったようにはいかない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（昔から軽業をやっているような人だったらいいだろうけど……、そんな経験なんかないわよ）"

hide jo_t_01_6
show jo_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0124
White_Joker "「じゃあ、別のほうがいい？\n
ジョーカーだったら、何をお勧めする？」"

hide jo_t_02_13
show jo_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0125
Black_Joker "「はあ、こいつに出来そうなやつかよ？\n
あるのか、そんなもん？」"

hide jo_t_02_2
show jo_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0126
Black_Joker "「俺のほうが聞きたいくらいだぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（どれだけ何も出来ない奴だと思われているわけ、私）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "玉乗りのセンスがないことだけは否定しないが……、そんなピンポイントなセンスだけ与えられても困ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それこそ、サーカスに就職するぐらいしか活かしようがないだろう。"

hide jo_t_03_2
show jo_t_03_19 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0127
White_Joker "「俺、意外と猛獣使いとか似合いそうだと思うんだけどなあ。\n
やってみる気はない、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「猛獣って……、あれ？」"

play sound se_0420
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "楽屋の片隅には、火の輪くぐりをするクマやライオンが、いくつかの檻に入れられている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それぞれの巨体に見合う檻は、当然頑丈そうに出来ているのだが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（無理無理、あんなのと一緒にいたら、間違いなく食べられるって）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "道具を使って制するどころではない、プレッシャーで負けること請け合いだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「有り得ないわよ、それ」"

hide jo_t_03_19
show jo_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice jok_f0128
White_Joker "「どうして？\n
だって、君が普段していることだって、同じようなことじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"

hide jo_t_03_10
show jo_t_01_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice jok_f0129
White_Joker "「夢を渡る芋虫、マフィアの幹部、刃物を持ったトカゲに騎士、銃をぶっ放すウサギや猫。……こいつら猛獣よりも、よっぽど危険じゃないか」"

hide jo_t_01_7
show jo_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice jok_f0130
White_Joker "「こいつらなら檻にも入れておけるけど、彼らはそうはいかないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（確かに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "否定できない。"

hide jo_t_02_8
show jo_t_03_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0131
Black_Joker "「そういう意味では、確かに猛獣使いでもいける……のか、本当に？」"

hide jo_t_01_3
show jo_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0132
White_Joker "「才能はあると思うんだけどね。\n
ねえ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「…………！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すっと音もなく間近に迫られて、声が出なくなる。\n
僅かに仰け反った身体は背後の壁に押さえ込まれて……、逃げ場がない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「な、なに……？」"

hide jo_t_01_1
show jo_t_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice jok_f0133
White_Joker "「そんな怖い顔をしないでよ、何も取って食べようってわけじゃない。\n
俺が、檻に入っているあいつらみたいに、がっついているように見える？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「……いいえ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "獣のように飢えているとは思わなかった。\n
ジョーカーの顔はいつもと変わらず、穏やかなものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほど彼があげた他の役持ちに比べれば、直接的な危機感は薄い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（だけど、安心なんて出来ない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何故か、今は檻の中に閉じ込められた猛獣の気持ちのほうが分かる気がした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この人の傍にいると、何故か暗い檻の中に閉じ込められるような感覚を覚える。"

hide jo_t_01_13
show jo_t_03_15 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0134
White_Joker "「ねえ、[firstname]。\n
君もサーカスに入ってみない？」"

hide jo_t_03_15
show jo_t_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0135
White_Joker "「ここは君にとっても、悪い場所じゃないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーの言うことは、的を射ている。\n
ここは、確かに悪いだけの場所ではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、悪いことがまったくない場所でもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（監獄だって……、ある）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "囚人が囚われる、あの暗く、空虚に満たされた空間。\n
あの場所もまたサーカスの持つもう一つの顔だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "団長と看守。\n
サーカスと監獄、二つの側面を統べる彼のように、底が知れない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「サーカスに入る気は、ないわ」"

hide jo_t_03_7
show jo_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
White_Joker "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「あなたのことは嫌いじゃないし、サーカスが嫌いなわけでもない。\n
でも、ずっとここにいるつもりはないの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスは、私の家じゃない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帰る場所があるからこそ、楽しめる場所。\n
非日常を常にしてしまったら、大事なものを失ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（私の家は……、別の場所にある）"

hide jo_t_03_11
show jo_t_03_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
White_Joker "「…………」"

hide jo_t_03_5
show jo_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0136
Black_Joker "「また振られてやんの、ジョーカー。\n
ざまあねえな」"

hide jo_t_03_13
show jo_t_01_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0137
White_Joker "「ジョーカーに言われたくないな。\n
俺が振られたってことは、ジョーカーだって振られたのと同じなんだから」"

hide jo_t_02_2
show jo_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0138
Black_Joker "「ふん、俺はこんなガキにどう思われようと気にしねえよ」"

play sound se_0415
play sound se_0417
hide jo_t_01_7
show j-boy_a_3 at center
hide jo_t_02_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice mat_f0031
Danin "「ただいま」"

hide j-boy_a_3
show j-boy_a_3 at left
show j-girl_a_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice nos_f0023
W "「お茶を淹れていたら遅くなっちゃった、ごめんね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "軽い足音と共に子供達が戻ってくる。"

hide j-boy_a_3
show jo_t_03_1 at center
hide j-girl_a_14
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0139
White_Joker "「お帰り。\n
さて、じゃあ、皆で一休みにしよう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って離れたジョーカーの顔は、やはり笑顔のままだった。"

hide jo_t_03_1

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（やっぱり冗談で言ったの？\n
それとも、少しは本気だったの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の笑い方は、いつも一定で温度を感じさせない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、本心が分からない。\n
自分の中で答えは出ている、彼の気持ちが本気にしろ、冗談だったにしろ、私には応える術なんてない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが分かっているのに……、それでも。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（どうしよう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気になってしまう。\n
彼が本気で誘ってくれていても、断ることしか出来ないのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（本当にサーカスに誘われているのだとしても、ここにはいられない。\n
なのに、何でそんなに気になってしまうの？）"

$ hi_mes()

scene circus
with stripe_l_medium

scene bg_gen_sky_all_day
with dis

play music honobono2_a_ali

scene bg_gen_sky_all_nig with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_f0140
White_Joker "「せっかくだから、泊まっていけばいい。\n
狭くて散らかっているけど、君一人ぐらいなら寝られる場所があるよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時間帯が夜に変わると同時に、ジョーカーはそんなことを言い出した。\n
だから、驚いたのだ。"


scene bg_gen18_cgu
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「サーカスは、夜に寝るの？」"


show jo_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice jok_f0141
Black_Joker "「ばあか、んなわけあるかよ。\n
おまえの住んでいたところだって同じだろうが、夜に寝るとは限らねえよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（じゃあ、どうして夜になって眠るなんて話が出るの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時間帯が不規則な世界。\n
夜に眠るとは限らないのなら、どうして夜になった途端に私の泊まる場所の話になるのだろう。"

hide jo_t_03_4
show jo_t_03_4 at left
show jo_t_03_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0142
White_Joker "「君は夜に眠るんだろう、[firstname]？\n
俺達には構わず、眠るといい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……いいの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本来の滞在地や、他の領土の友人達と違い、彼らとはそれほどの付き合いがあるわけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勝手に上がり込んだ挙げ句に、そこまで甘えていいものだろうか。"

hide jo_t_03_14
show jo_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0143
White_Joker "「いいよ、君が泊まっていってくれると俺も嬉しい。俺はすることがあるけど、独り寝が寂しいならジョーカーをつけてあげる……、いる？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "{size=+20}「いらない」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ホワイトさんにしろ、ブラックさんにしろ、いや誰だろうと、同衾する相手にはならない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とりつく島もない私の言葉に、ブラックさんも舌を出した。"

hide jo_t_03_4
show jo_t_03_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice jok_f0144
Black_Joker "「こっちから願い下げだ」"

hide jo_t_03_12
show jo_t_01_5 at center
hide jo_t_01_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice jok_f0145
White_Joker "「ははは。\n
さて、じゃあ、案内してあげて」"

hide jo_t_01_5
show jo_t_01_5 at left
show j-girl_a_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice nos_f0024
W "「はーい。\n
こっちよ、ついてきて」"

hide jo_t_01_5
hide j-girl_a_2
with dis

scene bg_gen19_cbu
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女に手を引かれるまま、薄暗い通路を歩く。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（…………。\n
結構、舞台裏って広いのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "テントの規模から考えても、広い敷地だろうとは思っていた。\n
舞台があるあの場所を表とするのであれば、ここは文字通りの裏。"

show white onlayer master with eddy_short

scene pri with eddy_short
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（…………？）"

show white onlayer master with eddy_short

scene bg_gen19_cbu with eddy_short
show white onlayer master with eddy_short

scene pri with eddy_short
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "瞬きをした一瞬の間。\n
その間に、私の足はサーカスとはまったく別の場所に入り込んでいた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、知らない場所ではない。"


play music jail_p_ali
show white onlayer master with eddy_short

scene bg_gen19_cbu with eddy_short
show white onlayer master with eddy_short

scene pri with eddy_short
show white onlayer master with eddy_short

scene bg_gen19_cbu  with eddy_short

scene pri with eddy_extralong
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（どうして……、またここに？）"

play sound se_0169
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足下には動き回る玩具の数々。\n
まったく動かないものから、ぎこちなくあたりを移動するものまで様々だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を引いて先導していたはずの彼女の姿もない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（……止まり、かけている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "動き始めたばかりというよりは、そんなふうに見えた。\n
それらを判断するだけの材料など、私は持ち合わせていないはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引かれていたはずの手を見ても、そこにはなにもない。\n
この監獄と同じ、空っぽの……、手。"


show jo_k_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0146
White_Joker "「だめだよ、[firstname]。\n
ここは休むには向かない場所だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り返った先には、灰色の看守服に身を包んだジョーカーの姿。"

hide jo_k_02_8
show jo_k_03_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0147
White_Joker "「迷い込まないようにと思って、案内までつけてあげたのに。\n
ほら、早く戻ったほうがいい」"

hide jo_k_03_15
show jo_k_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0148
White_Joker "「もっとも……。\n
君が、ここで休めるというのなら、俺は止めないけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "囁かれる声は優しいのに。\n
それでも、どこか震えるような悪寒を覚えずにはいられなかった。"

hide jo_k_03_14

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逃げるように、振り切るように身を翻す。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（逃げる？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一体、何から？ "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（ジョーカーから？\n
それとも、もっと別の何かから？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "答えの見つからないまま、夢中で足を動かして……。"


play music honobono2_a_ali

scene bg_gen19_cbu with eddy_extralong
show j-girl_a_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0025
W "「？\n
どうしたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚いたように私を見つめる女の子と目が合う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ……」"

hide j-girl_a_15
show j-girl_a_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nos_f0026
W "「手を離しちゃだめじゃない。\n
もうすぐだから、ちゃんとついてきてね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつのまにか離れた手を握り返して、彼女は先導するように私を連れて行った。"

hide j-girl_a_2

$ hi_mes()

scene map_bg_joker_night
with stripe_l_medium

scene map_bg_joker_day with Dissolve(.8)
scene circus
with stripe_l_medium

play music gag2_a_ali

scene bg_gen17_cst_a
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ころころ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「うーん……。\n
何でうまくいかないのかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他に人のいない舞台の上。\n
大きな玉を足下で転がしながら、私は一人首を捻る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーのような本職（？）の人と比べるのもおこがましいが、ここまで失敗が続くとは思わなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（綱渡りの練習用ロープがあってよかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭上に張られたロープに掴まりながら、ボールを足で動かしているが、やはり支えなしではうまくいきそうもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（あと思いつく理由なんて……。\n
この靴がいけないのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "硬い踵が感覚を鈍くしているのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もっとも靴のせいだけとはいえないが、少しでも成功の可能性を高めるとしたら無意味ではないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ジョーカーの履いている靴は、これに比べればずっと動きやすそうだったし）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「よ……っと。\n
これでどうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "前回ジョーカーが足場代わりにしていた台に戻り、靴下姿になって再びボールの上に乗る。"

show t_jo2_5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「あ……、うん、いいかも」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "使っている玉は同じだから、ふわふわとした不安定感は変わらない。\n
それでも足の裏全体で感じる自分の身体のバランスが、少し分かる気がした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（コツってこういうことかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐る恐る足を動かしてみると、玉はゆっくりと回転していく。\n
いい具合だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（どうしよう、うまくいくと、楽しいわ。\n
これ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足から直に伝わってくる柔らかな感触は、慣れてしまうと、まるで雲の上にいるようだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "現実主義な私らしくないことに、このままなら舞台の上も回れるのではないかという気さえしてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ジョーカーも、あの子達もいないわよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらちらと周囲を見渡して、誰もいないことを確認すると、すぐに足を動かした。\n
少しずつ大胆な動きになっていく足に合わせて、ボールはスムーズに回り始める。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうすると命綱のように握り締めていたロープによって生まれる制限が、少しずつ手狭に感じてきてしまった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_14")
T "（…………。\n
少しくらいなら、ロープを離しても平気かも）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舞台の端まで行くほどの自信はまだ持てないが、ほんの少し……。"

hide t_jo2_5
show t_jo2_6and4_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「……うん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ロープからゆっくりと手を離して、バランスを取りながら進む。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まっすぐに進めるほどの技術がないせいだろう、蛇行するボールは揺れながら軌跡を描き……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そろそろ下りようかと思ったところで、私ははたと気付いた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（しまった）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「あ、どうやって戻ろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "方向転換なんて器用な真似ができるほどうまくないのだ。\n
あの台がある場所まで戻ろうとしても、狙ったとおりになど進めるはずもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（舞台の上には、機材も何もないし……。\n
ジャンプすれば下りられるかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを思いながら下を見た瞬間、身体が大きく傾いだ。"

hide t_jo2_6and4_1
show t_jo2_4and2_7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（まずい……っ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慣れない足場で身体の向きを変えたのが失敗だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "柔らかな球面では体勢を立て直すことも出来ず、私はそのまま床に吸い込まれていく。"

play sound se_0091
hide t_jo2_4and2_7
show black onlayer master with spin_r
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「……あれ、痛くない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ちた衝撃は確かに身体に襲いかかっていたが、それも痛みを与えるほどのものではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして木の床についたはずの手は、自分以外の人間の服を掴んでいる。"


play music falling1_a_ali
hide black
show t_jo2_8 onlayer master with open
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え……。\n
ジョ、ジョーカー！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice jok_f0149
Black_Joker "「まったく、本当に手間のかかる女だな。\n
一人でなにしていやがるのかと思えば……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつの間にいたのか。\n
私の下には、呆れたような視線を向けてくるブラックさんの姿がある。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice jok_f0150
Black_Joker "「おい、怪我はねえんだろう？\n
だったら、とっとと下りろ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「あ、うん。\n
ごめん」"

hide t_jo2_8

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の上からどくと、ジョーカーは落ちていた帽子を拾ってかぽっと頭の上に乗せた。"


show jo_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0151
Black_Joker "「やれやれ。\n
練習熱心なのは悪くねえが、ド素人のくせに、一人でやるときにロープから手なんか離すな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「……あなた、いつから見ていたのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "調子に乗っていたところから見られていたとしたら、さすがに恥ずかしすぎる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0152
Black_Joker "「最初からとも言えるし、最後だけとも言える。\n
どうでもいいだろ、んなことは」"

hide jo_t_02_10
show jo_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0153
Black_Joker "「……で、おまえ、なんでそんなに練習してんだよ。\n
ここが、そんなに気に入ったのか？」"

menu:
    "気に入っている。":
        jump fushigi_joker2_2a
    "そういうわけではない。":
        jump fushigi_joker2_2b

label fushigi_joker2_2a:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐らくは、気に入っていないといったら、嘘だろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "監獄には思うところがあるが、サーカスという空間自体は決して嫌なものではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（そうじゃなかったら、こんなこと一人でやったりなんかしない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段は照らし出されて、輝いている舞台。\n
スポットライトを浴びる機会などない私にとって、それは得難い経験だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「まあ、これも……、やってみると結構楽しいし」"

hide jo_t_02_12
show jo_t_03_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice jok_f0154
Black_Joker "「ったく、最初はちっとも乗り気じゃなかったくせによ。\n
ちょっとうまくいくとすぐに調子に乗りやがる」"

hide jo_t_03_17
show jo_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice jok_f0155
Black_Joker "「素人はこれだから……、後が怖え」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「……？\n
勝手に一人で玉乗りしたのは悪かったと思っているけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そういうと、ジョーカーは酷く嘆かわしそうに肩を竦めて見せた。"

hide jo_t_03_4
show jo_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0156
Black_Joker "「おまえ、本物の馬鹿か？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「む……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（確かに頭がいいとはいわないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこまでも彼の口の悪さは変わらないらしい。"

hide jo_t_01_7
show jo_t_01_7 at left
show jo_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0157
White_Joker "「そんなこと言うなよ、ジョーカー」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（こっちのジョーカーも、本当にどこへでも出てくるのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで屋外で荷造りをしていたはずの団長が、舞台袖からひょっこりと顔を覗かせてくる。"

hide jo_t_03_2
show jo_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice jok_f0158
White_Joker "「いいじゃない、楽しんでいるなら。\n
楽しくないなら何かしらの対策を考えなくちゃいけないけど……」"

hide jo_t_03_10
show jo_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice jok_f0159
White_Joker "「どんな演目だっていいよ、君が楽しめるものを探してごらん、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……あれ？\n
前にも誰かに同じような台詞をいわれなかったっけ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おかしなことに、このサーカスに来てから、既視感を覚えてばかりな気がする。"

hide jo_t_01_7
show jo_t_03_1 at center
hide jo_t_03_7
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0160
White_Joker "「さあ、[firstname]。\n
まだ練習するだろう、今度は付き添ってあげるよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「え。\n
でもあなただって忙しいんじゃ……」"

hide jo_t_03_1
show jo_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice jok_f0161
White_Joker "「平気だよ。\n
君が楽しめるほうが大切だ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にっこりと笑って私の手を引くジョーカーは、何故か上機嫌そうに見えた。"

hide jo_t_02_6

$ hi_mes()

scene circus
with stripe_l_medium

scene map_bg_joker_day
with stripe_l_long
##endmemory
jump fushigi_joker_3 ##I think
label fushigi_joker2_2b:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（気に入っているかっていわれると……、ちょっと違う気がする）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「そういうわけじゃないわよ。\n
ただ出来そうで出来ないのって、何だかむっとこない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元々冷めやすい私だが、同時に負けず嫌いでもある。\n
面倒な性分だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言葉にブラックさんは眉を寄せて首を傾げた。"


show jo_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0162
Black_Joker "「分かるような分からねえような理屈だな。\n
いや、理屈でさえねえか」"

hide jo_t_01_14
show jo_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jok_f0163
Black_Joker "「それなら、俺がいちいちどうこういうほどのことじゃねえな。\n
勝手にしろよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーは今にも消えていきそうだった。\n
だからだろうか。"

play sound se_0117

show t_jo2_9b onlayer master
with dis
hide jo_t_01_8

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0164
Black_Joker "「……なんだよ？\n
用があるなら、とっとと……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「大したことじゃないけど……。\n
ありがとう」"

hide t_jo2_9b


show jo_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
White_Joker "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーは私の顔を見て何度も瞬きを繰り返している。\n
いわゆる鳩が豆鉄砲をくらったような顔というやつではないだろうか、これは。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（……私がお礼を言うのが、そんなに意外だってこと？\n
失礼な）"


show t_jo2_10b onlayer master
with dis
hide jo_t_01_4

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice jok_f0165
Black_Joker "「ふうん、礼だっていうなら……。\n
これぐらいのこと、してみせたって罰はあたらねえだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「え……？\n
！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬で顔を近づけた彼の舌が私の顔に触れた。\n
場所は、ちょうど唇の上。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「な、なにするのよっ」"

hide t_jo2_10b


show jo_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0166
Black_Joker "「ははは、そっちのほうがおまえらしい。\n
殊勝な態度なんて、似合わねえよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーは先ほどまでのぼうっとした様子など掻き消して、楽しげに笑いながら姿を消した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「～～～～っ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（なんなの、なんなの、あの男は！！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "代わりに。\n
残された私は、とてつもなく真っ赤な顔をしているに違いない。"

hide jo_t_02_4

$ hi_mes()

scene circus
with stripe_l_medium

scene map_bg_joker_day
with stripe_l_long
##endmemory
jump fushigi_joker_3 ##I think
