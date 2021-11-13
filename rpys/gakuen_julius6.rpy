label gakuen_julius6:
scene bg_map_nig
with dis
$ clockanim()

jump gakuen_common_breeze
label gakuen_julius6_2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ユリウスの部屋は三階だから、まずは階段を探さなくちゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とんとんと額を指先で叩いて、記憶を辿る。\n
これで、お目当ての人に会えるはずだ。"

play sound se_0774
pause 1
with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "途中何度か迷いそうになりつつも、どうにか無事にユリウスの部屋に辿り着くことが出来た。"
if lovechara_julius_points == 8:
    jump gakuen_julius6_3
jump gakuen_julius6_4a
label gakuen_julius6_3:
menu:
    "ノックする。":
        jump gakuen_julius6_4a
    "躊躇う。":
        jump gakuen_julius6_4b
label gakuen_julius6_4a:
play sound se_0217
pause .15
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアをノックするが、反応がない。\n
反応どころか、人のいる気配すらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……え。\n
ええええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予想外の展開に、頭の中が真っ白になった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズでユリウスを訪ねることで、何かが変わるだろうと思っていたし、期待もしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、あの苦い思い出を克服することが出来るんじゃないか……、なんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、ユリウスのことだから、一筋縄ではいかないかもしれないとも覚悟はしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、まさか。\n
居留守どころか、部屋にすらいないというのは予想外だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……ええー？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それ以外、言葉が出てこない。\n
扉に耳を押し当てて中の様子を窺ってもみるが、やはり物音一つしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（やっぱり、留守……、よね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこかで騒動でも起こって、風紀委員長として動かざるを得ないようなことになっているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（それとも……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の訪問など考えていなかったのだろうか。\n
むくむくと、後ろ向きな思考が頭を占め始めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「少し……。\n
少しだけ、待ってみようかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あちらこちらから、楽しげな声が漏れ聞こえる中、ユリウスを待つ。"

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0626 volume .7

play music view_nig_p_wam

scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……結局。\n
ブリーズ終了の笛が鳴り響くまで、ユリウスが部屋に戻ることはなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とぼとぼと、自室へと戻る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……ユリウスは私のこと好きじゃなくなったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……というか、最初から好きでも何でもなかったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……有り得る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの夜のキスは、何だったのだろう。\n
なんらかの感情はあると思っていただけに、ダメージが大きい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（ダメージが大きいってことは、期待していたってことで……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……キスをされて期待するのって、図々しいのかしら？\n
どうなの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いずれにせよ、空回りだったわけで、今はただ恥ずかしい。\n
期待していた時点で、すでに私は……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……はあ）"

with dis
$ hi_mes()

scene bg06_sk_h_nig with Dissolve(.8)

scene bg06_sk_h_day with Dissolve(1.2)

scene bg06_sk_h_eve with Dissolve(1.2)

scene bg06_sk_h_nig with Dissolve(1.2)

scene bg06_sk_h_day with Dissolve(1.2)

play music recollection_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "虚しく終わったブリーズの夜が明けて。\n
私はそれ以来、ユリウスの作業室を訪れることをやめていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、私を避けたのだ。\n
ブリーズというイベントごと、拒絶した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋にいなかったのは、そういうことだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……それなら、せめてブリーズの前に言ってほしかったな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "リボンも、結局返してもらっていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（態度だけ、思わせぶりって……。\n
……キャラじゃないわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの夜の様子だと、それなりにブリーズにも乗り気であるように思えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それ以降も、まるで私に気があるような態度で……。\n
ユリウスは演技でそんなことが出来るほど器用な男ではない……はずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ということは、そこまで彼は本気だったのだ。\n
どこかで私が間違えて、ユリウスは気を変えてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（どこで失敗したの……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくら考えても答えは見えない。"

play sound se_0161

play music flower_day_p_wam

scene bg_par02_ct_tow_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "椅子を引く音で我に返った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの作業室に行く代わりに、私はカフェテリアで時間を過ごすことが多くなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、だからといって読書が進むわけでもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今のようにぼんやりとしてしまうことのほうが多い。\n
私はゆるりと頭を振って、手元に広げた本へと焦点を戻す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして片手で傍らに用意した珈琲のカップを探した。"

play sound se_0542 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本を読みながら飲めるようにと、すぐそばに珈琲を準備していたはずだ。\n
それなのに、どれだけ探してもカップが見つけられない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（未練がましいわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "珈琲の匂いと、苦味に、もう訪ねることの出来なくなった作業室と、そこの主を思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0227
Julius "「……まずい。\n
私が淹れたほうが１０倍は美味いな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（ああ、そうね。\n
カフェテリアの、しかも冷えた珈琲を飲んだりしたら、きっとユリウスならそう言うわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、ついに幻聴まで聞こえだしてしまったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだブリーズの夜から数日。\n
ここまで自分がおかしくなるとは驚きだ。"

play sound se_0718
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱらりと本のページをめくる。\n
内容はまったく頭に入ってこない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0228
Julius "「おい。\n
聞いているのか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずいぶんとリアルな幻聴が聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるですぐそこにユリウスがいて、私に声をかけているかのようだ。\n
少しずつその声に苛立ちが混じり始めるあたり、かなりリアルな幻聴だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0229
Julius "「……おまえが怒っているのは分かる。\n
だが、私の話を聞いてくれないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度は珍しく彼が謝る調子だ。\n
珍しい、というかこれまで聞いたことのないような声のトーン……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（私って、想像力豊かね……）"


show yuri_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice jul_g0230
Julius "「おい。\n
……[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼ばれて、ついに顔を上げてしまった。\n
本当なら、ずっと、その幻聴を聞いていたかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこにユリウスがいないと確かめてしまったら、きっとこの幻聴も聞こえなくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "粘りに粘って、幻聴でもいいからその声を聞いていたかったのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……って。\n
ユリウス？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔を上げた先、眉間にきつく皺を刻んだユリウスが向かいに座っていた。\n
片手に、私のものだと思われる珈琲のカップを持っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（ああ、ついに幻覚まで）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「……いいわ、この際。\n
幻覚だろうが幻聴だろうが」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうなったらヤケだ。\n
相手が幻覚だろうが幻聴だろうが構うものか。"

hide yuri_m_01_12
show yuri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0231
Julius "「……おまえに、謝りにきた」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……やっぱり幻覚は駄目ね。\n
ユリウスがそんな殊勝なこと言うわけないじゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「所詮は私の妄想よね……」"

hide yuri_m_01_9
show yuri_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_9")
voice jul_g0232
Julius "「……大丈夫か、おまえ。\n
ナイトメアを呼んだほうがいいか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「ええ、ええ、見えているわよ。\n
目の前にユリウス＝モンレーの幻覚が」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「しかも、都合よく私に謝りに来たですって？\n
おかしいったらないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通なら現実と思ってもいいのかもしれないが、ここはシンフォニア。\n
思ったものが幻影となる仕掛けもいくつか見たことがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（おかしい……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（おかしいのは私の頭……。\n
ナイトメアなら治せるのかしら）"

hide yuri_m_03_11
show yuri_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_3")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幻覚のユリウスは、私の声に痛そうな顔をした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは「うわ、こいつ、どこかおかしいんじゃないか？」というような、そういう意味でのイタそうな顔ではなく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幻覚扱いされたことに傷ついたような、そんな顔だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……ずるいわ。\n
幻覚のくせに）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……何よ、分かったわよ。\n
聞いてあげるわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は諦めて、幻覚との対話を試みることにした。\n
この学園なら、なんでもありだ。"

hide yuri_m_02_10
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0233
Julius "「…………。\n
……ここしばらくずっと、どうしておまえが急に私の部屋を訪ねてこなくなったのかと考えていた」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……ん？）"

hide yuri_m_03_9
show yuri_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice jul_g0234
Julius "「理由が分からなかったんだが……。\n
やっと気付いたんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……おお）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の深層心理は、どうやってユリウスが部屋にいなかった理由を自分に都合のいいようにこじつける気なんだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうに観客気分で、幻覚ユリウスの次の言葉を待つ。"

hide yuri_m_01_13
show yuri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0235
Julius "{size=+20}「私は、ブリーズをすっかり忘れ去っていた」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "{size=+20}「それはないでしょう」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幻覚相手に即座に切り返してしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言うにことかいて、ブリーズを忘れていたとは何事だ。\n
そんな理由では、納得いかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（幻覚なら、もっと私の納得できるような理由を言ってくれればいいのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「……役に立たないわね、私の深層心理。\n
もうちょっとマシな理由を考えてきなさいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっかりやさぐれた気分で吐き捨てる。"

hide yuri_m_01_9
show yuri_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0236
Julius "「考えるも何も、それが真実なんだが……。\n
なあ、[firstname]、私が悪かった」"

hide yuri_m_01_12
show yuri_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0237
Julius "「謝るから……、幻覚扱いはやめてくれないか。\n
私は、ちゃんとおまえの目の前にいる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……騙されないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまでにも何度か、この手の仕掛けには引っ掛かっている。\n
強く思えば思考が形になるような魔法だ。"

hide yuri_m_03_12
show yuri_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "焦れたように、幻覚ユリウスが動いたのが分かった。"


play music quiet_a_wam
show m_yuri_goodend1 onlayer master
with dis
hide yuri_m_02_11

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手をとられる。\n
本のページをめくっていた手を、しっかりと握られた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段は工具を握っている器用な、大きな手だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……温かい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幻覚じゃないのか。\n
幻聴でも、ないのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（本物だとして……、言い分も本当なら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

hide m_yuri_goodend1
show bg06_sk_h_day onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……すうっと深く息を吸った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "{size=+20}「幻覚でも幻聴でもないならもっと悪いわよ！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_6")
T "{size=+20}「ブリーズを忘れていたってどういうこと！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一息に怒鳴る。\n
忘れていたなんて、どれだけ酷い言い訳なのだろう。"

hide bg06_sk_h_day


show yuri_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0238
Julius "「い、いや、ほら、今まで参加したことがなかったからな。\n
ストームの騒ぎで、満足していた」"

hide yuri_m_02_5
show yuri_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0239
Julius "「おまえはストームの日からも私の作業室に来てくれていたし……。\n
それでうっかり……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（うっかりってレベルじゃないでしょう\n
っ！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう怒鳴ってやろうと思ったのに、目の前にいる男が幻覚でもなければ、その言葉が幻聴でもない、という事実に私の心はすっかり打ちのめされてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "責めることも、ヒステリックに拳を振り上げることも、実行できずにいる。\n
大体、そんなことが出来るほどの関係でもなかったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……ブリーズの夜、どこにいたの」"

hide yuri_m_02_3
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jul_g0240
Julius "「作業室だ。\n
私は研究生だからな、夜間でも塔内であれば移動の自由がある程度認められている」"

hide yuri_m_03_9
show yuri_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jul_g0241
Julius "「あの日は朝からいつになく調子がよくてな」"

hide yuri_m_01_4
show yuri_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jul_g0241_5
Julius "「そのまま翌日の夕方ごろまでぶっ通しで作業を続け、そのまま作業室で仮眠をとり、気付いたら二日ほど過ぎていた」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……あなた、いつか過労死するわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もともとユリウスは研究生として、私達生徒に比べても時間の調整が自由になっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それゆえにやろうと思えばどこまでも勉強や研究をすることが出来るため、無茶をしがちなのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（研究に熱中して、忘れていた……、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……はあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脱力する。\n
怒るのも馬鹿らしいほど、ユリウスらしい。"

hide yuri_m_01_13
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0242
Julius "「ああ、それでおかしいと気付いた。\n
ここしばらく、私は作業室で仮眠をとるようなことがなくなっていたんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

hide yuri_m_03_9
show yuri_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice jul_g0243
Julius "「おまえが、いたから。\n
おまえが顔を出して、うるさく口を挟んでいたからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……悪かったわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスが研究熱心なのは、よく分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはまるで遊びに熱中する子供のような情熱で、彼はその情熱に任せて己の身をないがしろにしているところがあるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに気付いて以来、寝ていないように見えたら部屋に帰れと作業室から追い出したりもしたし……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食事をとってないと分かればカフェテリアから軽食を差し入れることもあった。"


show m_yuri_goodend2 onlayer master
with dis
hide yuri_m_03_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0244
Julius "「誰にも邪魔されない、静かな作業室で……、ようやく私はおまえがいないことに気付いたんだ。\n
そして、その理由にも」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0245
Julius "「……[firstname]。\n
私は、おまえとの約束をすっぽかしてしまった」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……改めて言われなくても分かっているわよ。\n
それに、約束なんてしていないし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（私が勝手に期待しちゃっただけで）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや……、はたして、勝手な期待だったのだろうか。\n
キスで舞い上がったのはおかしなことだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（いえ、おかしくないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jul_g0246
Julius "「明確ではなくとも……、約束していたのと同じだ。\n
私は、研究に打ち込むと周りが見えなくなるというか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（そうよ。\n
約束じゃなくても、重要だった）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「……ええ、本当に。\n
まったく見えなくなるようね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice jul_g0247
Julius "「……私は鈍い男だろうが、おまえが怒っていることくらいは分かる。\n
もう戻ってきてはくれないのか」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……何よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くっと唇を噛む。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（戻ってきてくれ、なんて……。\n
奥さんに出て行かれた旦那さんみたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ恋人ともいえない関係なのに、飛躍しすぎた発想だろうか。\n
彼は真面目だが、真面目すぎて間が抜けているところもある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「まるで、戻ってきてほしいみたいなことを言うのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice jul_g0248
Julius "「それは……。\n
……そうだ、戻ってきてほしい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本格的に、出て行った妻を引き止める夫のようだ。\n
もちろんそんなはずがないのに、長く時間を過ごした特別な関係のような……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（研究のために、イベントごとを忘れるような人よ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ユリウスの言葉を嬉しく感じてしまったことも事実。\n
彼の生活の中に、いかに自分が溶け込めていたのかを知らされた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の欠落に、気付いてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……三日近くかかってはいるけれども）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズを忘れ去っていたというのは、なんとも彼らしい理由だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怒るのも馬鹿らしいほど。\n
そして、呆れるほどに、ユリウスらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（ユリウスらしいなら……、どうしようもない。\n
だって、私はユリウスが好きなんだもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、彼に惹かれている。\n
ユリウス＝モンレーという人に。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……分かったわ。\n
でも、条件があるの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際には、何かもっと他の事情があったのかもしれない。\n
だが、今は追及できるほどの関係にない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0249
Julius "「先におまえとの約束を破ってしまったのは私だ。\n
私に出来うる限りで、その条件をかなえよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悲壮な覚悟さえ滲ませて、ユリウスは頷く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（真面目で……、冗談なんか言えない人）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかめ面をキープするのは、思っていたよりも難しい。\n
私は今、笑い出したいほど……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼に嫌われたわけでなかったことが、拒絶されていなかったことが嬉しい。\n
待ちぼうけを食らわされても、思った通りの人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "滑稽だと思うが、それでもいいとも思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「それじゃあ、条件を言うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウス側に引き寄せられていた珈琲カップを、指先に手繰り寄せる。\n
それを持ち上げて、中身が見えるように彼に向かって揺らしてみせた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「これより、１０倍美味しい珈琲を飲ませてくれる？\n
そうしたら……、許してあげる」"


play music flower_eve_p_wam
hide m_yuri_goodend2
show m_yuri_goodend3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
Julius "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice jul_g0250
Julius "「……分かった。\n
もう二度とこんな泥水のような珈琲を飲もうとは思えないような、美味い珈琲を飲ませてやる」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一瞬驚いたように瞬いたユリウスは、すでにいつもの不遜な態度を取り戻した。"


scene black ##instant]
hide m_yuri_goodend3
show bg06_sk_h_day onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……私はそれほど酷いとは思わないんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスいわく泥水だが、普通に飲めば決してまずいものではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ユリウスの淹れる珈琲と比較しなければ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも私はもう、ユリウスの淹れる珈琲の味を知ってしまっている。\n
立ち上がってカツカツと歩みだす彼の背を追って、私も歩き出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "諸々のことがうやむやになってしまった気もするが、きっとなんとかなるだろう。\n
私はまだシンフォニアにやってきたばかりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これから先、時間はいくらでもある。\n
少しずつでも……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（進んでいけるわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夫婦のようなやりとり。\n
もうすでに行き着いてしまった感があるものの、実際にはまだ始まってすらいない。"

hide bg06_sk_h_day with Dissolve(5)
hide frame_par_togaki
hide ali_m_06_16
with Dissolve(5)
scene black with Dissolve(5)
stop music
##endmemory
jump gakuen_b
label gakuen_julius6_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はその部屋をノックしかけて、躊躇った。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（いなかったら、どうしよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校行事や、イベントといったものをあまり好ましく思っていないユリウスのことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、部屋にいないかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズというイベントを拒絶するのに、これほどもってこいな回避方法はないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "追い払うための煩わしい会話をする必要も、押し切られる心配のどちらも必要なくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと思いついてしまったその考えは、とてもユリウスらしいと思えた。\n
ドアに触れかけた手が、躊躇う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……大丈夫よ。\n
嫌だったら、戦利品を持って行ったりはしない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が押し付けたわけでなく、ユリウスのほうから戦利品であるリボンを求めたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは彼がブリーズに参加するという意思表示ではないか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（だから、大丈夫……なはず）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう、渡せないラブレターの夢をみるのは充分だ。\n
同じことは繰り返さない。"

play sound se_0217
pause .15
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心臓がばくんばくんと騒ぎ出す。\n
この間が、耐え難い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "（早く返事しなさいよっ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌な予感をかき消すべく、心の中で毒づく。\n
どれくらいドアの前で立ち尽くしていただろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0251
Julius "「……開いている」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの返事が聞こえたのは、私がそろそろ諦めたほうがいいんじゃないかと本気で思い始めた頃だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……声、変じゃなかった？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し上擦っているように聞こえた。\n
気のせいだろうか。"

play sound se_0284

scene bg23_rd_nig with stripe_l_medlong

play music cliff_eve_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの部屋へと足を踏み入れる。\n
綺麗な部屋だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の部屋より少し広いように感じられるのは、彼が塔の寮長だからなのか、それとも彼が研究生だからなのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "壁一面には本棚が並べられていて、そこにはぎっしりと隙間なくたくさんの本が詰められている。\n
本以外には物の少ない部屋だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "机の上には書きかけのレポートのような紙が数枚と、ペンが転がっていた。\n
その傍らに置いてあるのが、私のリボン。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "全体的にモノトーンの印象のある部屋の中に、少しだけ雰囲気の違う黒が見える。"


show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「……[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……ん？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "初めて入る部屋だ。\n
物珍しくてきょろきょろしているところでかけられたユリウスの声に、意識を彼へと引き戻される。"

hide yuri_m_02_9
show yuri_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0252
Julius "「……どうして、ここに来たんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……え。\n
どうしてって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん、ブリーズというイベントだからだ。\n
そのイベントを彼と過ごすために……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（まさか……、来たことに、文句でも言う気？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キスまでしておいて、まったく気持ちがなかったと言う気なのだろうか。"

hide yuri_m_02_8
show yuri_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0253
Julius "「おまえが私の部屋に来たのは……。\n
私がおまえにとって、楽な相手だったからか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……はい？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "立ち尽くす彼の眉間には深い皺が刻まれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（ユリウスが……、楽な相手？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこをどうしたら、彼が楽な相手ということになるのだろう。\n
気難しく、どちらかというと難解で、けして楽とはいえない人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「どういうこと？」"

hide yuri_m_03_12
show yuri_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice jul_g0254
Julius "「つまり……。\n
ブラッド＝デュプレが帽子屋寮の人間で、おまえの手が届く相手ではないから私で手を打つ気なのかと聞いている」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……なんで、ブラッドが出てくるの？\n
突飛すぎない？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われた内容があまりにもとんでもなかったもので、怒ることすら忘れてしまいそうになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怒りよりも、驚きと呆れでぽかんとしてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこをどうしてそういう結論や懸念が出てきたのか知らないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（私と同じぐらい……、いえ、私以上のマイナス思考……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が昔、姉さんと自分を比べて落ち込んだように、彼もまた彼自身とブラッドとを比較しているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、キスをして、イベントで訪ねられ、その上で……だ。\n
代わりにされているというのも、あんまりな話。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「あなたそれ、失礼すぎるわ」"

hide yuri_m_02_11
show yuri_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice jul_g0255
Julius "「理解している。\n
こうして、私の部屋を訪れたおまえに対して……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「違うわよ。\n
私に対しても相当失礼だけど、ユリウス、自分にとっても失礼な話だと思うわよ」"

hide yuri_m_02_4
show yuri_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
Julius "「……？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「だって、それじゃあ、あなたがブラッドに劣っているような言い方じゃない」"

hide yuri_m_03_8
show yuri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice jul_g0256
Julius "「……実際、そうだろう。\n
私は人と関わることが得意ではない」"

hide yuri_m_01_9
show yuri_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice jul_g0257
Julius "「塔の寮長、風紀委員長などと務めてはいるが、ルールに沿ってしか動くことができない石頭だ」"

hide yuri_m_01_4
show yuri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice jul_g0257_5
Julius "「他の連中のような華やかさも、柔軟性もない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは淡々と語る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自嘲するような内容だが、それを悲しむような響きはなかった。\n
ただ事実を事実として羅列するような声音だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……似ているなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは私が、自分が姉さんに勝てない事実を並べるのによく似ているような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉の長所を並べるとき、私の中に悔しさはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私では姉になれないことを、もうとっくに理解している。\n
似ているからだろうか、私にはユリウスの狡さも分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「知っているわ。\n
あなたが石頭で頑固なのを、知っている」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（嫌になるほど）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「研究熱心で、でも研究している内容は人にはなかなか理解してもらえないような分野であることも知っているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「ああ、それと皮肉屋で無愛想なのも知っている」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つらつらと、ユリウスの短所を並べていく。\n
こうして私にあげつらわれているのに、彼はちっとも辛そうではなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……嫌になるほど、似ている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私もユリウスも、裏切ることが怖いのだ。\n
誰かの期待を裏切ってしまうことが怖い。\n
こんな人だとは思わなかったと、落胆されたくない。"

hide yuri_m_01_9
show yuri_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0258
Julius "「分かっていて、来たのか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「ええ、そう。\n
あなたがそういう人だと分かっていて、来たの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「イベントじゃなくても、分かっているわよ。\n
今までだって、散々来ていたじゃない」"

hide yuri_m_01_3
show yuri_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice jul_g0259
Julius "「……まあな。\n
今更か」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ、私のほうからも聞くけど……。\n
あなたは私のことを知っているの？」"

hide yuri_m_03_4
show yuri_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice jul_g0260
Julius "「知っている。\n
毎回、人の部屋に押しかけては珈琲を淹れろと迫るし、遠慮という言葉を知らない」"

hide yuri_m_02_2
show yuri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice jul_g0261
Julius "「外面はいいくせに、臆病なところがあって、うるさい。\n
……いらん世話を焼きたがる」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこで彼はちらりと私を見て、鼻で笑った。\n
いつもの、人を小馬鹿にするような不遜な態度だ。"

hide yuri_m_02_12
show yuri_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0262
Julius "「ブラッド＝デュプレにしろ、私にしろ……、男の趣味が悪い」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスにだけは言われたくない。\n
そんな私に意地悪く笑って、彼は懐から小さな石を取り出した。"


play music quiet_a_wam
show m_yuri6_1 onlayer master
with dis
hide yuri_m_03_1

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（共鳴石？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "共鳴石というのは、同じ魔法要素を持つ石が互いに共鳴しようとする力を使ったマジックアイテムだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じ要素を持つ石同士を使って、声を伝えることができる。"

play sound se_0742
hide m_yuri6_1
show white onlayer master with compress_medlong
hide white with compress_medlong
pause 1
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0263
Julius "「……ああ、私だ。\n
ブリーズで問題が起きた」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0068
Fuuki "「大丈夫ですか、委員長。\n
必要があれば、そちらに行きますが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0264
Julius "「いや、こちらは私で対処できる。\n
女子生徒が一人、魔力酔いで倒れた」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしなくても、それは私のことだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔力酔いというのは、魔法を使うための魔力を体内で暴走させてしまうために起こる魔法使い特有の症状だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段、私達は使う魔法に合わせた量の魔力を自動的に生成する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんらかの原因によりその調整がうまくいかないと、必要以上の魔力を生成してしまい……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その使われずに体に残った魔力が体に負荷をかけることになってしまうのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気持ち悪さや倦怠感といった症状が出るが、時間が経つにつれて魔力が分解されれば治る。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0265
Julius "「しばらく動けそうにないので、こちらで保護する。\n
女子生徒の名は……、[firstname]＝[familyname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0069
Fuuki "「了解しました。そのように女子寮に伝えておきます。\n
ああ、それでは男子寮の点呼作業はどうしましょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0266
Julius "「それも、そちらに任せる。\n
……大丈夫か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0070
Fuuki "「任せてください。\n
代理で、しっかりやります！」"


show yuri_m_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0267
Julius "「……これでよし」"

play sound se_0216 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話の終了した共鳴石を、ユリウスはベッドサイドのテーブルへと無造作に置いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「よし、って……」"

hide yuri_m_02_10
show yuri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice jul_g0268
Julius "「時間を気にせずいられるだろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（それって……、いいの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「とんでもなく職権濫用ね……。\n
今の子、あなたに仕事任されてすごく嬉しそうだったわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声だけでも、とても張り切っているのが感じとれた。\n
委員長に仕事を任されたのが嬉しくて、やる気に満ちているといった様子だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その委員長が今こうして、女子生徒と会っていると知ったら失望するだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（だとしたら……、可哀想）"

hide yuri_m_02_12
show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice jul_g0269
Julius "「結果として、充足感が高ければいい。\n
双方にとって、平穏無事で……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "万事解決だというふうに言う、彼。\n
淡々と、それでも言い訳を。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真面目な風紀委員長なのに、こういう面だってある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌なところや、ずるいところ。\n
意地悪なところ。"

hide yuri_m_02_9
show yuri_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0270
Julius "「奴は私に仕事を任されて満足。\n
私もおまえと時間を過ごし……、満足させてくれるんだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（こういうところ……。\n
知らないなんて、もったいない）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「あなたの方こそ。\n
私を満足させてくれるんでしょうね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "似たもの同士。\n
意地を張ったやり取りを交わす。"


play music night_a_wam

show m_yuri6_2 onlayer master
with dis
hide yuri_m_03_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次第に見つめあう視線の距離が近くなり、やがては視線だけでなく互いの唇が重なった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームのときの、慌しさはないのに。\n
時間を気にしなくていいという割に、やけに急いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_3")
T "「……っは」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "触れるだけでなく、深くまで混ざるキスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「……[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "長躯のユリウスが相手だと、どうしたって見上げる角度になる。\n
上向きに唇を塞がれ、息が苦しくなるのと同時に頭がくらくらとしてきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのままふわふわと飛んでいってしまいそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「……？」"

hide m_yuri6_2
show m_yuri6_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "力の入らなくなりそうな腕を持ち上げ、ユリウスの背に手を回す。\n
ぎゅうっ、とその背の生地をたぐる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0271
Julius "「ふ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はなんだかそれにいたく満足げだ。\n
少し悔しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0272
Julius "「いつも、それぐらい可愛げがあればいいんだがな。\n
……運ぶぞ」"

hide m_yuri6_3

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「う、うるさいわね……、って。\n
え？何？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "至近距離で囁くユリウスの唇が濡れているのを直視してしまい、かっと頭に血が上る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっと、今の私は、耳まで真っ赤になってしまっていることだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうしている間にも、ひょいとユリウスが私を抱き上げてベッドへと運んだ。\n
その手つきは、とても丁寧だ。"

play sound se_0327 volume .7

show m_yuri6_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもは工具を持ち、歯車やらネジやらに触れている手が、同じ慎重さでもって今は私に触れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの真剣な眼差しが、今は私に注がれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、真剣なだけではない。\n
熱を含む、艶っぽい視線だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……こ、これって、健全なイベントなんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームにしろ、ブリーズにしろ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「訪ねられたり訪ねたりしたからといって、こういう展開になるようなものではないはず……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうして、さも当然というようにこんな展開に……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（……いや、まったく期待していなかったわけじゃないけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気持ちが通じ合えたら、とか。\n
両思いになれたらというような類の期待だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0273
Julius "「……ああ、健全だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ど、どこが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jul_g0274
Julius "「……健全な男としては、期待するような展開だろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "待っていたことを打ち明けられ、キスをして、返礼に訪ねられ。\n
ユリウスも、期待したのだろうか。"

play sound se_0627 volume .3
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこか遠くで、笛の音がする。\n
おそらくこれがブリーズの終了合図なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、関係ない。\n
本来それを取り締まる側の人間が、ここにいる。"

hide m_yuri6_4
show m_yuri6_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0275
Julius "「おまえが、好きだ。\n
……不健全か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_8")
T "「……年頃の男性としては、ここで追い返すほうが不健全かもね。\n
私も、あなたが好きだし……、健全でしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_8")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "再び唇を落とされて、キスを交わす。"

play sound se_0627 volume .1
hide m_yuri6_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠くでは笛が鳴っているが……。\n
だんだんと聞こえにくくなっていく。"


with dis
$ hi_mes()

scene bg06_sk_h_nig with Dissolve(.8)

scene bg25_rr_nig
with stripe_l_medium

scene bg_par15_rg_tow_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_julius_end
