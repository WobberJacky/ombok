label gakuen_julius4:
scene bg_map_eve
with dis
$ clockanim()

jump gakuen_storm_tower1
label gakuen_julius4_2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は私に向けてぺこりと一礼すると、そのままどこかへと移動を開始しようとする。"

menu:
    "気になることがある。":
        jump gakuen_julius4_3a
    "そのまま見送る。":
        jump gakuen_julius4_3b
label gakuen_julius4_3a:
$ lovechara_julius_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと気になることがあって、彼を呼び止めた。"


show boy_b1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0063
Seito "「？\n
どうかしました？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「えっとその……。\n
ユリウス寮長は、参加しているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうなのだろう。\n
あまりこういったイベントごとには参加しそうにない人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（くだらない、の一言で切り捨てそうよね……）"

hide boy_b1_9
show boy_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice chi_g0064
Seito "「在校生は自由参加なんですけど……。\n
たぶん参加しているんじゃないですか？」"

hide boy_b1_3
show boy_b1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice chi_g0065
Seito "「ユリウス寮長が出掛けていくのを見たっていう奴がいましたから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_6")
T "（！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ユリウスも、参加しているんだ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰の元に向かっているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（…………）"

jump gakuen_julius4_4
label gakuen_julius4_3b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（頑張って）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中でそう呟いて、彼の背を見送っていたところ、ふと何か思い出したというように彼が振り返った。"

hide boy_b1_2
show boy_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0066
Seito "「そういえば、ユリウス寮長も参加しているみたいですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、有名人の挙動を噂するような気楽さから出た言葉のようだった。\n
けれど私の心臓を跳ねさせるには充分だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（ユリウスも、参加しているんだ……）"

jump gakuen_julius4_4
label gakuen_julius4_4:
hide boy_b1_3
show boy_b1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
voice chi_g0067
Seito "「どのあたりを取り締まっているのかな……。\n
あなたも、取り締まれないよう、気を付けて」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「は……？\n
あ、ああ、そうね、ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……あ、うん。\n
そうよね、そっちよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "参加するとしても、プライベートで参加していそうなイメージはない。\n
出ているということは、風紀委員の仕事だろう。"

jump gakuen_storm_tower2
label gakuen_julius4_5:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……ユリウスが参加している）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからといって、何があるわけでもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、微妙に心拍数が早くなっているのが自分でも分かる。\n
浮かれている自分が少し恥ずかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は認めるのも恥ずかしいが……。\n
ユリウスが自分のところに来てくれるのではないかと、思っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……馬鹿だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（肩透かしを食らうに決まっているのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなふうに馬鹿げた期待をしてしまうから、あんな夢をみたのだ。\n
恋なんてしないと決めたはずなのに、今こうしてこの胸は弾んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……本当に、馬鹿）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（本当に……、これって恋なの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "馬鹿だ愚かだと思いながらも、それでも何かを期待しているような自分がいる。"

with dis
$ hi_mes()

scene bg24_rj_nig_lon with Dissolve(.8)

scene bg_par15_rg_tow_nig with Dissolve(1)

scene bg25_rr_nig with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ごめんなさい。\n
人が来る予定があるの」"

hide boy_b1_5
show boy_c1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice kaz_g0063
Seito "「あ、それならいいんです！\n
他を当たるんで！」"

hide boy_c1_4
show boy_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice kaz_g0064
Seito "「よいストームを過ごしてくださいね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「あなたのほうもね」"

hide boy_c1_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他人ゆえに行儀もいい。\n
何度か無難な訪問を受け、そのたびに断りを入れる。"

play sound se_0664
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今回も、部屋の扉をぱたりと閉めた。"


scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……ああ、我ながら救いようがない）"

play sound se_0327 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はばたんっと倒れこむようにしてベッドに突っ伏した。"


play music flower_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームらしい賑やかさでもって、あれから何人かの男子が私の部屋を訪れてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、私はその誰もに、人が来る予定があるからと言って断ってしまっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（イベントだっていうのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかくのイベントなのに、わざわざ寂しく過ごそうとしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別に相手がユリウスではなくても……、むしろユリウスではないほうが楽しく過ごせそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほど訪れた男の子を部屋に入れていたならば、イベントらしい賑やかな会話や、楽しげな空気に混じることが出来た。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、私はそれを断って、部屋に一人でこもっている\n "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "来るかどうかも分からない相手……いや、すべてが勝手な期待で、来ないほうが自然な相手だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、イベントにかこつけて、一緒に過ごしたいと思ってしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（図々しいっていうか……。\n
……頭悪いな、私）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐしゃぐしゃと髪をかきむしりながら身を起こした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今からでもまだ遅くない。\n
部屋で待つのではなく、どこかへ出掛けてみようか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賑やかなイベントに身を任せてしまえばいい。\n
悶々と部屋に引きこもるためのイベントではないはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを思いながら、窓辺へと移動した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外に出て楽しもうと考えながらも、未練がましくこちらに向かう誰かの姿を探すように窓を開けて外を見た。"

play sound se_0586

scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……？」"


play music magic_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ざわりと、空気が騒いだような気がした。\n
窓の外にはなんの変哲もない庭の光景が広がっているだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別に、何かおかしいところなど見当たらない。\n
それなのに、肌にピリリとくる緊張感を感じた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（ストームっていうだけじゃないの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの持つ騒々しいお祭り騒ぎのような空気とは、種類が違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（なんだろう……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲の部屋の窓を見てみるが、皆ストームに夢中になっているのか、窓を開けているのは私だけのようだ。"


scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆は気付いていないのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（それとも、私が気にしすぎているの？）"

menu:
    "気にしすぎ。":
        jump gakuen_julius4_6a
    "何かある。" :
        jump gakuen_julius4_6b
label gakuen_julius4_6a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……気にしすぎているわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスが来やしないかと、神経が過敏になってしまっているのだ。\n
おとなしく、部屋でじっとしておこう。"

jump gakuen_julius4_7
label gakuen_julius4_6b:
$ lovechara_julius_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……何かある）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな気がしてならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（何か……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……何かしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうせストームに参加していないのだ。\n
このまま窓の外を眺めていたところで、問題ないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（様子をみよう）"

jump gakuen_julius4_7
label gakuen_julius4_7:
play sound se_0611

scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "突風と呼んでもいいほどの強い風が、窓の外を吹き荒れた。\n
「何か」の前触れのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばたばたと、カーテンが千切れそうにはためく。\n
そして、影が動いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視界に飛び込んできたのは、箒に跨って高速移動をしているのだと思われる影三つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "猛スピードでありながらも、どこか危なっかしく感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（あれもストーム？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子寮に侵入することがストームの第一段階だというのなら、あの箒に跨った三人の影もストーム参加者なのだろうか。"

play sound se_0173
$ flash(.2)
pause 1
play sound se_0173
$ flash(.2)
pause .4
play sound se_0173

scene white with expand_extrashort
play music battle_a_wam

scene bg20_gd_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……！？\n
まぶしっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唐突に暗かった庭に灯りがともる。\n
幾つもの光球が宙に浮かび、周囲を煌々と照らし出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おかげで、よりはっきりと庭で何が起こっているのかが見てとれるようになる。"


show m_yuri4_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「っ！\n
あれって、もしかして」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "箒に跨り、うろうろと蛇行運転を繰り返す男子生徒は、三人とも揃って覆面を身につけていた。\n
間違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らだ。\n
ボリスが苦い顔をしていた、校舎内で暴走鬼ごっこをくりかえしていた犯人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……本当に覆面をしているのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "危うく接触されかけたときには、ほんの一瞬のことだったので分からなかったが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今こうして遠目に観察すると、それぞれが目元と口元だけが露出するような覆面をしているのが見てとれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかすると、どことなく危うげな印象をうける飛行はそのせいなのかもしれない。\n
これは何かの演出なのだろうか。"

hide m_yuri4_1
show m_yuri4_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0185
Julius "「エリオット、ディー、ダム。\n
追い込め」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐ近く、耳元で囁くようにして声が聞こえた。\n
ユリウスの声だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、周囲を見渡してもその姿を見つけることは出来ない。\n
おそらく、風の拡散魔法をつかって声を広範囲に飛ばしているのだ。"

hide m_yuri4_2
show bg06_sk_h_nig onlayer master
with dis
play sound se_0127
pause .4
play sound se_0736
pause .4
play sound se_0736
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの声に応じるようにして、風が唸る。先に飛び込んできた三人を追うようにして、新しい影が三つ視界へと飛び込んできた。"

hide bg06_sk_h_nig
show m_yuri4_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こちらは顔を隠したりなどはしていない。\n
ブラッドを除く帽子屋寮の三人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（どうしてユリウスが、あの三人に命令を？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それもおかしいが、三人がその命令に従っているのはもっとおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0484
Dee "「ふふふ。\n
その程度の速度で僕達から逃げ切れるとでも？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0485
Dam "「楽しいね、兄弟。\n
合法的に人を追い詰められるっていいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0333
Elliot "「楽しんでる場合か。\n
さっさと片付けるぞ！！」"

play sound se_0736
play sound se_0736
play sound se_0736
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人はぐんと加速すると、それぞれ覆面三人組の後方へとぴったりとつける。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0186
Julius "「あまり追い詰めすぎるな。\n
空中で事故を起こされると、このスピードでは大惨事だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0486
Dee "「僕達、そんなドジしないよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0487
Dam "「そうだよ！\n
あいつらが空中分解したって、僕達は華麗に避けてみせるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0334
Elliot "「こら、ガキ共！今は委員長の言うことをきけって！\n
……忌々しいが、今回だけだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ますます珍しい。\n
エリオットは日頃、ブラッドの敵として帽子屋寮を取り締まろうとする塔と敵対するスタンスを取り続けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その彼が、双子相手にユリウスのいうことをきくように命令するなんて、一体何が起こっているのだろう。"

play sound se_0585 volume .5
pause .4
play sound se_0585 volume .5
pause .6
play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の中でストームに夢中になっていた生徒達の中にも、そろそろ窓の外の騒ぎに気付いた者がいるようだ。\n
時折、窓を開ける音が聞こえてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初は、無秩序に飛び交う三人の覆面生徒を、エリオットやディーとダムもただひたすらに追いかけまわしているだけに見えていたが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（追い込んでいる？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今は、追う三人が、それぞれ微妙な力加減で覆面三人を誘導しているように見えてきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "牧羊犬を彷彿とさせる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "覆面の三人が意図せぬ場所へ曲がろうとすればその方向を防ぐように加速し……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その逆にわざとそこに行かせたかったのでは、というところでは追跡を甘くしているように見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初は私の気のせいかとも思っていたのだが、逃げる覆面三人が示し合わせたわけでもないだろうに、次第追い詰められて並ぶ様にやはりと感じた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、並んで飛ぶ覆面三人も同じだったらしい。"

play sound se_0692 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0075
Mask "「離れろよ……！！\n
散らないと撒けないだろ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0086
Mask "「知らねえよ……！！\n
俺だって、別におまえの隣に来たくて来たわけじゃ……！！」"

play sound se_0698 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0066
Mask "「おまえら散らばって飛べよ……！！\n
固まってたら、すぐ捕まるって分かってるだろ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "焦燥を含んだ声が、風に乗ってここまで届く。\n
私の想像どおり、覆面三人は帽子屋寮幹部三人により追い込まれているのだ。"

play sound se_0400
pause 1
play sound se_0737
play sound se_0737
hide m_yuri4_3
show bg06_sk_h_nig onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もつれ合うように飛ぶ六人の影が庭の端にかかったところで、急に追うほうの三人が急ブレーキをかけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "高速で飛行していたはずなのに、さすがといわざるを得ない見事な停止だ。\n
慣性に流されることなく、その場で静止する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、止まりきれなかった……、というより最初から止まるつもりもなかった覆面の男達はそのまままっすぐに突き進む。"

play sound se_0604
play sound se_0694
pause 1
play sound se_0268
hide bg06_sk_h_nig
show bg_par_sky_web_nig onlayer master
with dis
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "巨大なゴムが伸び縮みするような間の抜けた音が、庭に木霊した。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Mask "「！！！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0087
Mask "「なっ……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Mask "「！！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "罠が仕掛けられていたのだ。\n
何もないように見えていた空間に、接触の瞬間光り輝く巨大な蜘蛛の巣のようなものが浮かび上がる。"


play music looking_for_a_ali
hide bg_par_sky_web_nig


show ace_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0470
Ace "「ははは、まるで蜘蛛に捕まった可哀想な蝶々みたいだね！\n
自ら危険に首をつっこんでいるあたり、炎に飛び込む蛾かな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょこりとその蜘蛛の巣状の罠の下、爽やかな笑い声を響かせるのはエースだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は赤薔薇寮の人間とはいえ風紀委員なので、この場にいても他の三人よりは違和感がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0187
Julius "「エース、油断するな！\n
一人逃げたぞ！」"

hide ace_m_01_4
show ace_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0471
Ace "「ん？\n
え～？」"

hide ace_m_03_2


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！！！」"

play sound se_0401
pause 1
play sound se_0739
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の二人よりも遅れがちだった一人が、仲間の運命を悟った瞬間、無理矢理に方向転換しようとしたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐいっと無理に箒の舳先を持ち上げたせいか、彼の身体は勢いよく上空に回転しながら舞い上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（これって、制御不能状態なんじゃ……\n
！！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "操縦者である覆面の青年は、錐揉み回転で暴走する箒にしがみつくだけで精一杯だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0188
Julius "「止めるぞ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0335
Elliot "「え～？\n
もう落としちまってもよくねえか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0488
Dee "「うんうん、落ちたら学ぶよ。\n
人は失敗から学ぶものなんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0489
Dam "「いいこと言うね、兄弟。\n
痛いめをみるのも大事だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帽子屋幹部三人は、もはや自分の仕事は終わったとばかりに投げやりだ。\n
そうしているうちにも、風に煽られた暴走箒はこちらへと近付いてくる。"


play music battle_ali
play sound se_0743

scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……げ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっかり観客に徹していた私だが、暴走箒がこちらに向かってくるのに我に返った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慌てて杖を手に取り、迎え撃とうとするが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（か、壁なんて作ったら彼が怪我するわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風を固定して壁を作るのは簡単だ。\n
だが、それではあの勢いでぶつかる彼が、怪我をしてしまうことになるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ベストな方法としては、エースが仕掛けていた罠のように、彼の勢いや衝撃を吸収しつつ捕獲する魔法ということになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、そんな複雑な条件のものを突発で作れるわけもない。\n
私はそこまで優秀ではないし、捕縛系の魔法に慣れているわけでもないのだ。"

play sound se_0052
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それほど長い時間ではなかったと思うのだが、考えた結果私は何もしないことにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ窓辺にしゃがみこみ、自らの被害だけを避ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋に飛び込んできた彼は、壁やらドアやらにぶつかって停止するだろう。\n
そこをユリウスに引き渡してしまえば万事解決だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……部屋は相当荒れるだろうけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "散らかったり、壊れたものを片付ける作業を思うと憂鬱になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかくのストームだというのに、何をしているのだか、といった気分になることは間違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（いや、部屋の心配よりも、彼が怪我しないことを願うべきか……。\n
……無理だろうけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの勢いで無傷だったら、おかしいくらいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "追いかけられるからには悪さをしたのだろうし、多少の怪我なら自業自得だろうが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……大怪我なんかはしませんように）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "祈ってあげるくらいしか出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「…………」"

play sound se_0319 volume .5
play sound se_0571
pause .4
play sound se_0075
$ flash_color("indigo", .5)
scene bg06_sk_h_nig
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "水面を思いっきり平手で叩いたときのような音が響いた。"

play sound se_0576 volume .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "涼しい水の細かい粒子が降り注ぐ感触に、私は顔を上げる。"


play music garden_nig_p_wam

show m_yuri4_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……あ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0189
Julius "「……おまえは馬鹿か。\n
対処する時間は、充分にあっただろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むっつりと眉間に皺を寄せたユリウスが、箒に跨り、窓のすぐ近くに浮いていた。\n
片手に、暴走していた箒の主を無造作にぶら下げている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その顔面は、ちょっと同情してしまうほどに赤い。\n
無傷のようだが、被害がないとはいえない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「私の魔法だと、大怪我させちゃいそうだったのよ。\n
……だ、大丈夫なの、その人」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「顔、真っ赤だわ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice jul_g0190
Julius "「プールへの飛び込みに失敗した程度の衝撃だ。\n
すぐに目を覚ます」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice jul_g0191
Julius "「空気中の水分を集めて、水の壁を作ってこいつを受け止めたんだ。\n
おまえは……」"

hide m_yuri4_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言いながら、ユリウスがぱっと手を放した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぶら下げられていた青年の身体がひゅっと重力にひかれて見えなくなることに度肝を抜かれるが、地上にはすでにユリウスの部下が集まっていたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0065
Fuuki "「無事、回収しましたー！\n
他二名とともに、会議室に連行しまーす！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……なんて声が下から響いて、安堵した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………。\n
……ユリウスは、会議室に行かなくてもいいの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぞろぞろと他のメンバーが引き上げていく気配を背後に、ユリウスは動こうとしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その視線が、一度私の部屋の様子を窺うように揺れた。"


show m_yuri4_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0192
Julius "「ストームには参加しなかったのか？」"

menu:
    "ユリウスを待っていた。":
        jump gakuen_julius4_8a
    "その気になれなかった。" :
        jump gakuen_julius4_8b
label gakuen_julius4_8a:
$ lovechara_julius_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……あなたが来るかな、って思って」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0193
Julius "「え……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「知り合いのところを訪問するんでしょう？\n
新入生は知らない人のところに行ったり、訪問を受けたりするみたいだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知り合いがいて、ある程度部屋を把握しているのなら、そちらを訪問するのだろう。\n
そう考えていたのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「あなたも参加しているって聞いたから、もしかしたら来るかなって思ったんだけど……。\n
でも、仕事だったみたいね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、個人的に参加というのはなかったようだ。\n
今の捕り物のために寮を出るところを、目撃されていたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「結局来たのは、別の何かだったけれど。\n
まさか、暴走箒が飛び込んでくるとは思わなかったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "冗談めかした口調の中に、真実を混ぜ込んで私はひょいと肩を竦める。"

jump gakuen_julius4_9
label gakuen_julius4_8b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「参加する気になれなかったのよ。\n
……何人かの男の子が来たけど、皆断ったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「あなたも参加しているって聞いたから、もしかしたら来るかなって思ったんだけど……。\n
でも、仕事だったみたいね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、個人的に参加というのはなかったようだ。\n
今の捕り物のために寮を出るところを、目撃されていたのだろう。"

jump gakuen_julius4_9
label gakuen_julius4_9:
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0194
Julius "「……私を、待っていたのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確認するように問われると、恥ずかしくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「そ、それは……、まあ……。\n
最近、親しいし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……変じゃないわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、この学校の男性でユリウスが一番親しい相手だと思っている。\n
彼だって、他に親しそうな女性はいなかったはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな深刻な話でなくとも、イベントごとだ。\n
相手に選ばれるかと期待してしまう。"


play music residence_p_wam
hide m_yuri4_5
show m_yuri4_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「……[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼ばれて、羞恥に伏せがちになっていた視線を持ち上げた。\n
顎に指先がかかり、くいと引き寄せられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前のめりになるように、窓に寄る。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0195
Julius "「ストームなど、くだらん肝試しだ。\n
そんなものに喜んで参加するのは、浮かれた間抜け共だけだぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……胸に染みる言葉をありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くだらない肝試しの間、そう言いきる彼を待っていたなんてそれこそ正真正銘の間抜けだろう。\n
我ながら情けなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0196
Julius "「だが、おまえの部屋に他の男が侵入するぐらいならば……。\n
私自身が間抜けになったほうがマシだと、思い直した」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice jul_g0197
Julius "「……嫌なら、拒絶しろ。\n
私はこういうことに疎い」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "吐息が触れるほどの近くで囁かれた言葉の意味を、正しく理解するより先に、顔が近付いてきた。"

hide m_yuri4_6
show m_yuri4_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゆっくりと……、私に逃げる余地を残すためにか、嫌になるほどゆっくりと近付いてきた唇がそっと私のそれと重なりあう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……え）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "触れるだけの、柔らかな、それでいてどこかぎこちないキスだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

hide m_yuri4_7
show m_yuri4_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスが私の顎から指を解く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……え？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（ええ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jul_g0198
Julius "「……それから。\n
いくら自室であろうといつ誰が来るのかもわからないんだ、もっとちゃんとした服を着ろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「そんな格好」と言われて、ネグリジェ姿だったことを思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "淡々としたいつもと変わらないユリウスの声に、キスに動揺しているのは自分だけなのかと腹立たしくなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、よくよくみると彼の耳が真っ赤に染まっているのが分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（ユリウスも……、照れている？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに気付いたら、もっと素直になることが出来た。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……あなたがいつまでも来ないから。\n
待ちくたびれていたのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私だって、部屋に戻った当初は誰が来ても……、ユリウスがいつ来ても大丈夫なようにちゃんとガウンだって羽織っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だがいつまで経っても来ないので、もうストームを諦めたつもりでガウンも脱いでしまっていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……っていうか、こんなつもりじゃなかった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントに来てくれたらなあ、くらいのつもりで……、キスとか、そんな。\n
……愛の告白のようにとられてしまったのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（だ、だって、健全なイベントだって聞いたし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントで「自分のところへ来てほしい」というのが、告白のように響くイベントとは……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（……いや、それもそうか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントのある特別な夜に、自分の部屋を訪れてほしいというのだ。\n
特別な意味があって当然だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無作為の訪問というわけでもない。\n
好意はあって当然のもの。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（私も……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好意があるから、ユリウスを待っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_9")
Julius "「…………」"

play sound se_0627
hide m_yuri4_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこか遠くで、笛の音がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0199
Julius "「ストームの終了の合図だ。\n
男子寮に戻って点呼……、ああ、それと先刻の奴らの始末をつけなければ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「始末って何よ、始末って。\n
響きが怖いわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスがいつも通りなので、私もなるべくいつも通りのように振る舞う。\n
心臓がばくばく騒いでいることなど、気付かれたくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "足元から崩れてしまいそうだ。\n
ふっと箒を操って窓辺から去りかけたユリウスが、気紛れのようにこちらに向かって手を出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……何？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice jul_g0200
Julius "「……私も参加するのは初めてだが、ルールは心得ている」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice jul_g0201
Julius "「ストームには戦利品が必要なんだ。\n
聞いていないのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「ああ、そういえば……。\n
戦利品、ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ちょっと待って」"


scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は一度部屋に引っ込み、何か渡せそうなものがないかを探す。\n
ちらりと見やった机の上、風呂に行く前に外したリボンが目に止まった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これならば予備があるので、渡してしまっても大丈夫だ。"


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「これ、持っていって」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "リボンを渡すと、ユリウスはどこかほっとしたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（表面に出さないようにしているけど……、緊張している？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ねえ、この戦利品って私の手元には戻ってこないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0202
Julius "「一週間後に、ブリーズというイベントがある。\n
そのときに……、取り返しにこい」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……まだあるんだ、イベント）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……この学校、わりとイベント好きよね」"

play sound se_0587
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふっとユリウスは私のそんなぼやきに応えるように笑って、それから箒を繰ると窓辺から離れていく。\n
それを最後まで見送って、窓を閉じた。"

play sound se_0165

play music starlit_sky_a_wam

scene bg24_rj_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しゃっと、カーテンまで閉じる。\n
隠れたいような気分だったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……キス、したわよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確認するように呟く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（した。\n
あれは間違いなくキスだった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスからの、キス。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「でも、どうして？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（ストームだから？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントだからといって、ユリウスが流されたりするだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（咄嗟に？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（思いつきで？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（それとも……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭の中がぐるぐるとする。\n
触れた唇がいつまでも熱をもっているような気がした。"

with dis
$ hi_mes()

scene bg_par15_rg_tow_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_julius5
