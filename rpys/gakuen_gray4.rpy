label gakuen_gray4:
scene bg_map_eve
with dis
$ clockanim()

jump gakuen_storm_tower1
label gakuen_gray4_2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝から気になっていたイベントの詳細について、ようやっと知ることが出来たというのに、私はそれを楽しむ以上に気落ちしてしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その理由は……、明白だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……グレイは仕事なのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、このストームと呼ばれるイベントの妨害役をする使用人達の統括。\n
その指示で忙しくしているだろうと、誰に教えられずとも分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、彼自身も妨害役として塔の内と外と、見回りに出ているのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな彼自身の訪れを期待しているなんて、あまりに馬鹿げている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「来られるわけ、ない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽつりと呟いて、それからその意味に気付いて動揺した。\n
今の言いようでは、まるで彼に仕事さえなければここへ来ていたかのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（いやいや、可能かどうか以前の問題じゃない。\n
可能でも、来るわけがない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなふうに馬鹿げた期待をしてしまうから、過去の夢まで見る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋なんてろくでもないと決めつけたはずなのに、今こんなにもがっかりしてしまっているのは、寄せた期待の裏返しだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを馬鹿だ愚かだと思いながらも、それでも何かを期待しているような自分がいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "椅子の背に引っ掛けていたガウンを羽織り、髪を乾かし始めた。"

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どれくらい時間が経っただろう。"

play sound se_0191 volume .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱたぱたとタオルで髪を乾かす音に混じって、違う音が聞こえた。\n
耳を澄ましてみる。"

play sound se_0683 volume .4
pause .4
play sound se_0679 volume .4
pause .6
play sound se_0686 volume .4
pause .8
play sound se_0604 volume .4
pause .5
play sound se_0192 volume .4
pause .2

play music battle_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "明らかに物騒な……、戦闘でもしているような音だ。\n
慌ててタオルを放り出し、窓へと飛びついた。"

play sound se_0165
pause 1
play sound se_0585

scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カーテンを開け放ち、窓を開ける。"

play sound se_0794
play sound se_0792
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔を中心に広がる庭。\n
日頃は静かなそこが、今は喧騒に包まれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもなら夜の庭は、暗い。\n
エントランス側にならば街灯も設置されているのだが、この辺りまではその光も届かないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、現在私の眼下にはまばゆいほどの光球がいくつも浮かび、真昼ばりに明るくなっている。"

play sound se_0683
pause .4
play sound se_0604
play sound se_0605
pause .4
play sound se_0192
pause .3
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな中で、剣を交える人影が二つ。\n
浮かび上がった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（ス、ストームって、こういうイベントでもあるの！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどの男子生徒の様子を見る限りは、こっそりと忍び込むものと思っていた。\n
だが、これは、こっそりというレベルではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "堂々と、戦闘を繰り広げている。\n
そもそも、戦うようなイベントだったことが驚きだ。"

play sound se_0585 volume .5
pause .4
play sound se_0585 volume .3
pause .6
play sound se_0585 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲の部屋の住人達も、外で繰り広げられる騒ぎに気付いたらしい。\n
あちこちから窓を開ける音が聞こえる。"

play sound se_0792
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0085
Seito "「わ……！？\n
なんで、こんな派手な戦闘に……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0119
Seito "「帽子屋寮のストームじゃあるまいし……。\n
どうして、こんな戦闘になっちゃっているの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、異常事態のようだ。\n
通常はこういったイベントではないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（……でも、帽子屋寮のストームはこれが当たり前なのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞こえた会話に、そんなことを思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が知らないだけでなく、こういった形でのストームというのは邪道らしい。\n
あくまで、本来は、ひっそりと忍び込むもののようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（一体、誰よ。\n
こんな派手なことをやらかしているのは……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よく見ようと目を細めて、様子を伺う。"

play sound se_0676
pause .2
play sound se_0439
pause .4
play sound se_0683
pause .8
play sound se_0073 volume .8
show m_gre4_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0472
Ace "「あははっ！\n
やっぱり、トカゲさんって強いよね！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0136
Gray "「おまえに褒められても嬉しくないな……！\n
さっさとお引取り願おうか……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0473
Ace "「そんな、つれないこと言わないでくれよ！\n
ほら、風紀を守る者として、常に自己研鑽が大事なんだしさ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0137
Gray "「俺に関わらないところでなら、好きに研鑽してくれ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0138
Gray "「だいたい、おまえは赤薔薇寮のくせに、どうしてここにいるんだ！？\n
これは寮ごとのイベントだぞ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（両方が、知り合いだったとは……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「な……、何をやっているのよ……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呆然と呟いてしまった。\n
煌々と光を放つ光球に浮かび上がった人物は、二人とも私の知る人物だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一人は、ここにいてもおかしくない。\n
グレイだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の管理をしており、ここの使用人を統括する立場にある。\n
だからこそ、こうして問題解決に当たっているのも充分に納得がいく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここでトラブルを引き起こしている元凶は、もちろん彼ではないだろう。\n
ははっと軽やかな笑い声をあげながら、長剣を振り回している人物……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「エース……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう、エースだ。\n
本来ならば赤薔薇寮の住人であり、そこの幹部でもある彼。"

hide m_gre4_1

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……ねえ。\n
このイベントって、他寮に攻め込むのってアリなの……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓から身を乗り出し、同じく近くの窓から呆然と外の光景を眺めていた女子生徒へと問う。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0086
Seito "「う～ん……、普通はないわね。\n
だってストームって、寮内の親睦イベントよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0120
Seito "「特別、禁止するルールもなかったような気がするけど……。\n
慣例として、自分のいる寮内でのイベント……、よね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "となると、やはりエースの行動にこそ問題がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（なんだって塔に……？\n
っていうか、なんだって、グレイに喧嘩をふっかけているの？）"

play sound se_0676
pause .3
play sound se_0439
pause .4

show m_gre4_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことに思いを馳せている間にも、鋭い風切音が響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（そうだった……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは自治会の風紀担当というだけでなく、剣の腕前でも名の売れた生徒だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法使いでありながら常に帯剣しており、その得物である大剣が魔法の媒体にもなっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、実際に何度か彼が剣を振るっている姿を見たことがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（風紀を自称している癖に、暴れているところばかりを見かけるのよね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "素人目から見ても、凄い腕前だった。\n
普通の魔法使いが、物理的に勝てる相手ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_6")
T "「グレイ……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法勝負に持ち込めばまだしも、剣の腕だけでエースと張り合うのは危険だ。"

play sound se_0677
pause .4
play sound se_0506
$ flash(.2)
hide m_gre4_1
show m_gre4_2and6 onlayer master with Dissolve(.6)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "焦って呼んでしまった名に重ねるようにして、先ほどから何度も響いていた金属のぶつかりあう激しい音がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの手元で、銀光が煌く。\n
それがナイフなのだと認識するより先に、彼は受け止めたエースの剣を弾く。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「えええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice ace_g0474
Ace "「やっぱトカゲさんは強いよなあ？\n
ははっ、偶然とはいえ、塔に遊びにこられてよかったぜ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice ace_g0475
Ace "「……っ！」"

play sound se_0742
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！！」"

play sound se_0400
hide m_gre4_2and6 with Dissolve(.6)
show m_gre4_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースの意思に反応したように大剣が薄い光を纏ってつむじ風を放つ。\n
魔法媒体としての力を発揮したのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（魔法剣士なんて、ずるいわよ……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがにこれはグレイも……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gray "「……！」"

play sound se_0438 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "危ない、と身を乗り出したものの（それで何かが変わるわけでもないが）、それは杞憂だった。"

play sound se_0674 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは流れるような動作で、右に構えていたナイフを腰へと戻すと、その返す手で右の太腿に固定してあったベルトより小型のナイフを引き抜いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とても滑らかな動作だ。\n
慣れているというような、熟練の技と分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……グレイ？）"

play sound se_0297
pause .5
play sound se_0606
hide m_gre4_3
show white with spread_extraextrashort
show m_gre4_4 onlayer master with spread_medium
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の身に迫っていたつむじ風は、投擲されたナイフに触れた途端、そこでその威力を解放して無力化されてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイはそのまま、反撃に出た。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0139
Gray "「さっさと帰れ……！！」"

play sound se_0297
play sound se_0677
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……わ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鋭い角度で放たれたナイフに、声をあげてしまう。\n
腕や足ではなく、完全に急所である身体の中心線を狙った投擲だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学園関係者が、生徒に向けていい反撃のレベルを超えているような気がする。\n
万が一があったら……、なんて思うと背筋が冷たくなる。"

play sound se_0683
##special anime"kiseki01"loop="false"time="1000"]
play sound se_0665
$ flash_color("light_purple",.2)
$ flash_color("periwinkle_purple", .3)
$ flash_color("dark_indigo", .3)
pause 1
hide m_gre4_4
show m_gre4_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0476
Ace "「はは、今のは、ちょっと本気だった？\n
出し惜しみするのは、トカゲさんの悪いところだよな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恐ろしい攻撃に対し、向けられた本人は怯む様子もない。\n
朗らかな声をあげながら、エースはかざした長剣の腹でナイフを叩き落とした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく、ナイフには予め氷系の魔法が込めてあったのだろう。\n
ぴきぴきっと音がして長剣の表面に霜が走るのが見えた。"

play sound se_0686 volume .7
pause .1
$ flash(.1)
$ flash(.1)
pause .5
play sound se_0726 volume .7
pause 1
$ flash(.1)
play sound se_0369
play sound se_0728 volume .7
$ flash_color("off_red", .2)
$ flash_color("orange",.2)
$ flash_color("red", .3)
pause 1
hide m_gre4_5
show m_gre4_2and6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……うわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話の合間合間には、剣戟やら魔法が炸裂する音が響き、お互い傍から見る分には必殺の一撃とみられる攻撃を繰り出しあっている。"

play sound se_0683
$ flash(.2)
pause .1
play sound se_0679
pause .6
play sound se_0686
$ flash(.1)
$ flash(.1)
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0087
Seito "「っ、グレイ執務長、すごい……っ！\n
風紀のエース先輩に負けてないわ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0121
Seito "「グレイ執務長って……。\n
ナイトメア先生のお守りなだけじゃなかったのね！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、同意だ。\n
普段、ナイトメアを相手に甲斐甲斐しく世話を焼いている姿と、眼下でエース相手に刃を交えている姿が重ならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じグレイなのに、別人のように見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（こんな……、攻撃的な人だったなんて）"

play sound se_0604
play sound se_0605
pause .5
play sound se_0507
hide m_gre4_2and6
show white onlayer master ##instant]
pause .1
hide white ##instant

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一際大きな音をたてて、二人の刃がぶつかりあった。そのままでは、今までと同じく流されて終わるのが分かっているのか、エースはひょいと飛び退る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あくまでエースを追い払いたいだけのグレイに、追撃するつもりはないようだ。\n
疲れた様子で、グレイはエースを睨めつけ、口を開いた。"


scene bg20_gd_nig
with dis



show gre_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0140
Gray "「……分かった、妥協してやる。\n
日を改めておまえの自己研鑽とやらに協力してやるから、今夜は帰れ」"

hide gre_m_03_7
show gre_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0141
Gray "「ただでさえ忙しいストームの夜だ。\n
おまえの相手をしている暇はない」"


play music ace_t_ali
hide gre_m_01_9
show gre_m_01_9 at left
with dis

show ace_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0477
Ace "「何言っているんだよ、トカゲさん。\n
ストームだからこそ、燃えるんだろ？」"

hide ace_m_01_3
show ace_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0478
Ace "「障害を倒してプリンセスを救い出す！\n
障害あってこその達成感！これぞ正義の味方の醍醐味だよな！」"

hide gre_m_01_9
show gre_m_03_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0142
Gray "「なんだ、それは……。\n
プリンセスだと……？」"

hide ace_m_01_4
show ace_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0479
Ace "「そうそう、プリンセス。\n
ほら、せっかくのストームだし、誰か塔の女の子のところに忍び込んでみようと思ってさ」"

hide ace_m_03_3
show ace_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0480
Ace "「……まあ、実際は迷い込んじゃっただけなんだけど。\n
せっかくだし、戦利品は欲しいよね」"

hide gre_m_03_11
show gre_m_02_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0143
Gray "「毎回毎回、しれっとろくでもないことを言うな、おまえは……。\n
……さっさと帰ってくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しっしと犬猫でも追い払うように、グレイがナイフを持ったままの手を揺らす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一方、エースのほうはといえば、片手を目の上に押し当て、こちらを見やった。"

hide gre_m_02_12

hide ace_m_03_11


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「……！！」"

play sound se_0395
pause .3
play sound se_0395
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達が行動に出るのは、びっくりしてしまうほどに速かった。\n
あっというまにぴしゃりと窓を閉め、中へと引っ込んでしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きょろきょろっと視線を周囲にやるが、先ほどまで好奇心旺盛に窓から外を覗いていた女子生徒達の姿が、嘘のように見当たらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（ええ！？\n
に、逃げ遅れた……っ！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく、彼女達はエースがトラブルメーカーで、人を巻き込んでは迷惑をかけるというのを私以上によく分かっていたのだろう。"

menu:
    "今からでも逃げる。":
        jump gakuen_gray4_3a
    "見届ける。":
        jump gakuen_gray4_3b
label gakuen_gray4_3a:
$ lovechara_gray_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（うううっ。\n
今更でも、とりあえず逃げよう……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は一拍以上遅れて、それでも周囲の女子生徒と同じようにぴしゃりと窓を閉めて逃げようとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、それをエースが見逃してくれるわけもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0481
Ace "「あはは、逃げないでくれよ！\n
逃げられると俺、遠投しちゃうぜ？」"

play sound se_0674
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とんでもない脅し文句だ。\n
……いや、正しくない意味での殺し文句かもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん、私は死にたくなんかない。\n
逃亡を諦めるしかなかった。"

jump gakuen_gray4_4
label gakuen_gray4_3b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（今から逃げても……、無駄よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆の行動は、まるであらかじめ打ち合わせでもしていたかのように素早かった。\n
今から隠れても、遅いだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、私は元より好奇心が旺盛なのだ。\n
この後、二人がどうなるのかも気になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうなってしまったら、仕方がない。\n
おとなしく現状を見守ることにした。"

jump gakuen_gray4_4
label gakuen_gray4_4:

scene bg20_gd_nig
with dis

show ace_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0482
Ace "「ああ、[firstname]、そこにいるの君だろ？\n
ちょうど窓から顔を出しているし、君、俺のプリンセスになってくれよ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「はあ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまり、それは、エースが私の部屋に押しかけてくるということなのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰もが逃げ出すほどに、トラブルメーカーの風紀委員。\n
彼と過ごすストームの夜なんて、怖すぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「え、遠慮するわ……！\n
ほら、私、プリンセスって柄じゃないし……！！」"

hide ace_m_03_11
show ace_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_g0483
Ace "「はは、俺は気にしないよ！\n
俺と君の仲じゃないか！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "{size=+20}「どんな仲よ！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とエースの間には、そんな特別な仲は存在しない。\n
校舎で（運悪く）会ったら、会話をする程度だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それぐらいの関係性で、プリンセス（と書いて犠牲者と読む）として目をつけられるなんてたまったものではない。"

hide ace_m_02_4
show ace_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0484
Ace "「それは、ほら……」"

play sound se_0125
$ flash_color("vermillion", .1)
hide ace_m_02_1
show ace_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0485
Ace "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "のんきにないことないこと（あることないことではない。全部ないことだ）並べようとしたエースの頬に、しゅっと赤い線が走った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私との会話に気を取られていたエースの頬を、グレイの放った投げナイフが掠めたのだ。"

hide ace_m_03_2


show gre_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0144
Gray "「……残念だが、その物語では悪が勝つことになっているらしい。\n
正義の味方はお引取り願おうか」"


play music kaigou2_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、ぞっとするほどに冷えた声だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までも、グレイは普段私が聞いたことのないような低い声で毒づいていたが、これはちょっと別格だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声に乗る温度の違い。\n
先刻までの攻撃以上にひやりとしたものを感じた。"

play sound se_0084

show m_gre4_7 onlayer master
with dis
hide gre_m_01_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0486
Ace "「……はは。なんだかよく分からないけど、トカゲさん、本気になってくれたの？\n
珍しく、ついてるぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぺろりと唇を舐めて、エースが再び長剣を構える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……これは、まずい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひしひしと感じる、うすら寒さ。\n
先刻までの比ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何がきっかけなのか分からないが、エースの言う通りに、グレイは本気になったようだ。\n
それに煽られるように、エースもやる気。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（や、やる気っていうか、もはや「殺」る気……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このままでは、血を見るまで止まらない。\n
戦闘のことなんて何も知らない私にまで、二人の殺気が伝わってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（どうにかして止めないと……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（で、でもどうやって……！？\n
魔法で冷水でもかける？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それくらいしても、戦っていそうだ。\n
攻撃魔法をぶつけるわけにもいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（誰か呼びに行くとか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、心当たりがない。\n
管理を担うグレイ自身が当事者だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "暴走するエースとグレイを止められる人間なんて、存在するのだろうか。\n
いっそ、私も窓を閉め、何も見なかったことにしてしまいたい。"

play sound se_0623
hide m_gre4_7

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「ん……？」"


play music tower_room1_p_ali

show yuri_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice jul_g0312
Julius "「……エース！！\n
貴様、そこで何をしている！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "{size=+20}（いた！）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "暴走するエースとグレイを止められる人。\n
この人しかいないという人が。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "タイミングよく姿を現してくれた、ユリウス。\n
庭に立ち込めていた殺伐とした空気を、その一喝が吹き飛ばす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰かが、風紀委員長であるユリウスに通報してくれたのだろうか。\n
私よりも、よほど冷静な人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（よかった……）"


show ace_m_01_4 at right
with dis
hide yuri_m_03_7
show yuri_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice ace_g0487
Ace "「あ、ユリウスだ。\n
やあ、何をしてるって、ストームに決まっているだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱあっと、ユリウスが登場した途端に、エースから物騒な気配が消えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こういうところで、ユリウスの存在は偉大だ。\n
エースというとんでもない男でも、風紀委員の手綱をしっかりと握っている。"

hide yuri_m_03_7
show yuri_m_01_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0313
Julius "「赤薔薇寮のおまえが、どうして塔のストームに参加しているんだ！！\n
ほら、おとなしくこっちに来い！！」"

hide ace_m_01_4
show ace_m_02_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0488
Ace "「ちぇ～。\n
はいはい、分かったよ、ユリウス！」"

hide ace_m_02_12
show ace_m_03_11 at center
with dis
hide yuri_m_01_8

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0489
Ace "「というわけでごめんな、トカゲさん！\n
もっと遊んでほしかったけど、タイムアウトみたいだ！」"

hide ace_m_03_11
show ace_m_03_11 at left
with dis

show gre_m_01_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0145
Gray "「……はあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこで、グレイも深く脱力したように息を吐いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "張り詰めていた殺気のようなもの（ようなものではなく、そのまんま殺気だったのかもしれない）が霧散する。"

play sound se_0674 volume .6
pause .2
play sound se_0674 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして、両腕に構えていたナイフを、それぞれ懐へとしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただそれらをベルトの鞘に戻しただけだと分かっているのに、それだけで剣呑な雰囲気がなくなるのは魔法のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は今までだって、彼がそのマントの下にナイフを携えていることに気付いていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それを武器として、本当の意味では認識していなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（まさか、こんなにも強いだなんて）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "飾りだと思っていたわけではないが、実用される図は想像していなかったのだ。"


show yuri_m_01_13 at center
with dis
hide ace_m_03_11

hide gre_m_01_13

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0314
Julius "「ほら、おまえはこっちにこい……！\n
このトラブルメーカーめ！！」"


show ace_m_02_10 at right
with dis
hide yuri_m_01_13
show yuri_m_01_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0490
Ace "「あはは、仕方ないじゃないか～。\n
赤薔薇寮でストームしようと思って辿り着いたのが塔だったんだからさ～」"

hide ace_m_02_10
show ace_m_02_10 at center
with dis
hide yuri_m_01_13
show yuri_m_01_13 at left_center

show gre_m_03_11 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0146
Gray "「……豪快だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ものすごく大胆な迷子だ。\n
エースはこんなイベントの折にまで、その迷子の才能を如何なく発揮しているらしい。"

hide yuri_m_01_13
show yuri_m_03_12 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0315
Julius "「行くぞ。\n
無駄だろうが……、説教と始末書だ」"

hide ace_m_02_10
show ace_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0491
Ace "「え～……。\n
無駄だって分かっているなら、いらないのに……」"

hide yuri_m_03_12
show yuri_m_03_7 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0316
Julius "「そうはいくか！\n
おまえときたら、何もペナルティがないと、ますます増長して……」"

play sound se_0623
play sound se_0624
hide gre_m_03_11

hide ace_m_03_9

hide yuri_m_03_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やがて、次第にユリウスの小言を漏らす声と、エースが笑いながらのらりくらりとそれを受け流す声が遠くなっていく。"


play music garden_nig_p_wam

scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（これで一段落……、よね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来のストームとはだいぶ違う形ではあるが、充分すぎるほどにドキドキすることは出来た。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（ドキドキというか、心臓に悪い……。\n
私も部屋に戻ろう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一歩、窓から引いて、戸締りをしようと窓へと手をかける。"

play sound se_0348
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！？」"


show gre_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（わ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐ目の前に、グレイが現れた。\n
魔法を使って跳躍したのだろう。"

play sound se_0269 volume .6

scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の部屋の窓枠に着地して、そのままするりと部屋の中へと侵入される。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「グ……、グレイ？」"

hide gre_m_01_12
show gre_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice gra_g0147
Gray "「君は……。\n
赤薔薇寮の風紀委員と仲がいいのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……へ？\n
赤薔薇寮の風紀委員って……、エースのこと？」"

hide gre_m_01_11
show gre_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice gra_g0148
Gray "「他にもいるが、あれ以上の問題児はいない……。\n
……どうなんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「どう……、って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイとは普段から身長差がある分、見下ろされる角度だ。\n
だが今は、彼が窓枠に身を乗り上げていることもあっていつもより更に高い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな位置から、覗き込むようにして問われる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（な……、なんだか、いつもと雰囲気が違う）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつものグレイのイメージは、大人の男性。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの世話焼きをしているせいで、苦労性にも見えるが、親切で優しくて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、今私の目の前にいるグレイには、そんな優しい雰囲気はない。\n
もっと、鋭い。"

play sound se_0774
hide gre_m_01_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゆっくりと窓を乗り越えて、グレイは完全に私の部屋へと侵入する。\n
小さく、後ろに後ずさってしまった。"



show gre_m_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0149
Gray "「……怖がらせたか？」"

menu:
    "怖い。":
        jump gakuen_gray4_5a
    "そんなことない。":
        jump gakuen_gray4_5b
label gakuen_gray4_5a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ええ、なんだか……、怖いわ。\n
まるで、知らない誰かみたいに見える」"

hide gre_m_01_14
show gre_m_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice gra_g0150
Gray "「はは、知らない誰か……、か。\n
俺は、元々こういう男だ」"

hide gre_m_01_13
show gre_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice gra_g0151
Gray "「君は……、もっと警戒心を持つべきだな」"

jump gakuen_gray4_6
label gakuen_gray4_5b:
$ lovechara_gray_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「そんなことないわ。\n
……ただちょっと、驚いているの」"

hide gre_m_03_9
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice gra_g0152
Gray "「そうか、君は強い子だな。\n
でも……、君は怖がるべきだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……どうして、そんなことを言うの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私を遠ざけたいのだろうか。"

hide gre_m_01_3
show gre_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0153
Gray "「警戒心は、身を守るのに必要なものだからだ。\n
あの風紀委員に対しても、俺に対しても……、必要だ」"

jump gakuen_gray4_6
label gakuen_gray4_6:
play sound se_0158
hide gre_m_03_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイが、一歩、また一歩と私への距離を削る。\n
更に後ずさろうとして、膝裏がベッドへと触れた。"

play sound se_0103 volume .7
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……っ」"

play sound se_0051
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "がくんとそのまま後ろに尻餅をついてしまいそうになったところを、グレイの腕が腰を抱えるようにして支えてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "助けられたととるか、追い詰められたととるか。\n
もう、逃げ場はない。"


show gre_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0154
Gray "「教えてくれないか？\n
君は、ストームに訪問されるほどあの風紀と仲がいいのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……迷い込んだだけだって、言っていたでしょう？\n
その通りだと思うわよ？」"

hide gre_m_02_13
show gre_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gra_g0155
Gray "「だが、迷い込んだ先で、君を選んだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「逃げ遅れたからね」"

hide gre_m_03_8
show gre_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gra_g0156
Gray "「……口実だろう。\n
あいつは、あれで好みがうるさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽんぽんと返すが、同じ分だけ言い返される。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「エースと、私をくっつけたいの？」"

hide gre_m_01_5
show gre_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gra_g0157
Gray "「っ、まさか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「じゃあ、どうして、そんなふうに……。\n
先刻から、変よ？」"

hide gre_m_01_2
show gre_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
voice gra_g0158
Gray "「それは……。\n
俺が……、君を気に入っているから、だろうな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「え……」"

hide gre_m_01_6
show gre_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_6")
voice gra_g0159
Gray "「あんな奴に渡したくないほどには……。\n
……俺は君を、気に掛けている」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「気に掛けてくれているのは……、知っているわ。\n
……ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "課題に忙しいときに、毎晩メッセージを添えたココアを差し入れてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "庭と部屋とで距離を隔てていても、ささやかなコミュニケーションをはかってくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（……いつだって、親切にしてくれた）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これで、気に掛けてもらっていないと思うほうがおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼が、私に対して好意を抱いてくれているのは知っていた。\n
だが、それがどんな種類のものなのかは不明だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知るのは、怖かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "期待して、自惚れて、馬鹿をみるのが怖かったのだ。\n
渡せずに終わったラブレターの存在が、脳内でちらつく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「エースは……、校舎で見かけたら挨拶する程度よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初からエースは塔に迷い込んだのだと言っていた。\n
私を目当てに来たわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの言う通り、好みにうるさく、私が当てはまっていたとしても、わざわざ訪ねてくるほどの執着ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷い込んだ先で、たまたま目について、なんとなくグレイに喧嘩を売る理由に使えそうだから採用しただけ。"

hide gre_m_01_8
show gre_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0160
Gray "「……そうか。\n
それを聞いて、安心したよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（どうして、それであなたが安心するの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースのようなトラブルメーカーと親しくしているわけではないと聞いて、友人として安心してくれているのか。\n
それとも、何か別の意味があるのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう聞いてみたくなるのに、その答えを知るのが怖いとも思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞いてしまって、これまでの居心地のいい関係が壊れてしまったらと思うと、その疑問を口にすることが出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（あのときから、ちっとも変わっていない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言い出せず、気持ちを綴った手紙を渡すことも出来ないままに初恋は終わった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのときのことを夢にみては、幼かった自分を馬鹿だの愚かだの思ってきたが、今も私は全然成長できていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（あのときと同じように……。\n
……ううん、もっと明確に、気持ちはあるのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "惑うように視線を揺らしたタイミングで、名前を呼ばれた。"

hide gre_m_03_10
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gray "「[firstname]」"


play music flower_nig_p_wam

show m_gre4_8 onlayer master
with dis
hide gre_m_01_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔を上げた途端に、口付けられた。\n
驚くほど近くに、グレイの顔がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_6")
T "（！？\n
なんで？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_12")
T "（どうして？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ、ん」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……～～～～っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "パニックに陥っている間にも、口付けは続く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "苦い、煙草の味がした。\n
頭がくらくらとしてくるのはキスのせいか、煙草の味のせいなのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「は……、っ」"

hide m_gre4_8
show m_gre4_9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やがて唇が離れる頃には、すっかり脱力してしまっていた。\n
そんな私の体を、グレイはしっかりと抱き支えてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "宥めるように背を撫でる、大きな手のひらが気持ちいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0161
Gray "「……しまった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭上から、苦い声が響いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（何？\n
キスしたことを、後悔している？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分からしておいて、それはちょっとばかり酷い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、納得もした。\n
勢いとか、その場の流れとか……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ともかく、グレイの気持ちを伴うものではない。\n
そう言われたほうが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0162
Gray "「先走ってしまった。\n
……順番が逆だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……順番？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の懐に預けていた頬を浮かせて、彼を見上げる。"


play music quiet_a_wam
hide m_gre4_9
show m_gre4_10 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0163
Gray "「ああ、順番だ。\n
……好きだよ、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0164
Gray "「俺はまず、それを告げるべきだった。\n
……情けないな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼のぼやく言葉に、かあっと瞬間的に頬に熱がのぼる。\n
頭の中まで沸騰しそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キスされただけでも相当だったのに、今や茹でダコ状態だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤くなった私の額に、頬に、グレイは唇を落としていく。\n
ますます熱くなって……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（あああ、今、私、どれだけ赤くなっているんだろ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice gra_g0165
Gray "「君の返事も、聞かせてもらっていいか？\n
その……、野暮なことを言うようだが……、俺も、君の口から聞きたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の口ぶりから、私の気持ちは態度からバレバレだということが分かる。\n
そう思ったら、逆に踏ん切りがついた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……あのときと、全然違う）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "初恋の、あのとき。\n
相手の気持ちがまるで読めず、心が通ったと思うこともないまま、恋をした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれは一方的で……。\n
それこそ、幻想に恋をしたようなものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今は、目の前に相手がいると分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「私も……、あなたのことが好きだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かつて渡せずに終わったラブレターと違い、その言葉はするりと口をついて出た。"

play sound se_0627 volume .1
hide m_gre4_10
show m_gre4_11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0166
Gray "「……嬉しいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "また、その唇が慈しむように降ってくる。\n
くすぐったくてその腕の中で身じろいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（優しいキス）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だけど、攻撃的な人でもある。\n
今夜、彼の違った一面を見られた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（他に、どんな面があるのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知らない面があるのに、怖くない。\n
彼の言うようには、警戒心など持てそうもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（むしろ、知りたいって思う）"

play sound se_0627 volume .6
hide m_gre4_11
show bg06_sk_h_nig onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓の外からは、ストームの終了を知らせるためのものなのか、笛の鳴る音がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "時間は常に足らず、彼と過ごす時間はいつも短い。"

with dis
$ hi_mes()
hide bg06_sk_h_nig with dis
##[cg PAY ATTENTION="true"]

scene bg_par15_rg_tow_nig with stripe_l

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_gray5
