label gakuen_boris4:
scene bg_map_day
with dis
$ clockanim()

jump gakuen_storm_bor_pie
label gakuen_boris4_2:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……お風呂あがりって、一割増しくらい見栄えがよくなるわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "髪の毛は濡れているせいで艶々。\n
しっとりした肌は柔らかそうに上気してほんのり桃色だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段からこうだったら、もうちょっと女の子らしくなれるんじゃないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「ある意味風呂上がりマジックよね。\n
……これ、魔法として開発できないものかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "常に風呂上がりの状態をキープする魔法。\n
女性陣からは熱烈な支持を受けることが出来るような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「……そうよ。\n
あの姉さんの妹なんだから、そんなに悪くはないはずよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鏡の中の自分に向かって話しかけてみる。\n
私も、学園内の雰囲気につられてテンションが上がっているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントに加わるつもりでいた分、行き所がなくなった。\n
いつもならしないような馬鹿なことをしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（今の私なら、彼はなんていうかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの頃よりもずっと、私は大人になった。\n
背も伸びたし、手足だって長くなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すましていれば、淑女に見えないこともない……、はずだ。\n
今ならば、あのとき渡しそびれたラブレターを渡すことが出来るだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（彼は、受け取ってくれる？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後の職員室の光景を夢想する。"


scene bg24_rj_nig_s
with dis

play music memory1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0292
Boris "「ねえ、[firstname]、俺さ……。\n
あんたが危なくなったら、何をしてでも助けるし……、怪我をしたら責任をとるつもりだったよ？」"

play sound se_0069 volume .7

scene bg06_sk_h_eve with expand_long
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……え？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その声をきっかけに、夢想の世界が朱色に染まる。\n
遊園地寮の屋根の上、特等席でともに見た夕日の色だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その逆光の中、いつのまにか私が手紙を渡そうとしていた相手は彼ではなく、よく見知ったクラスメイトになっていた。"


scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……{size=+20}っ！！！{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かあああっと頬に熱がのぼる感覚で我に返った。\n
風呂上がりなのに、更に熱くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（い……っ、い、今の何……！！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「な、なんで……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（どうして、ボリスなの？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_11")
T "（私、ひょっとして……）"

menu:
    "ボリスのことが好きなの？":
        jump gakuen_boris4_3a
    "気の迷いだ。":
        jump gakuen_boris4_3b
label gakuen_boris4_3a:
$ lovechara_boris_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（ボリスのことが好きなの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは気のいいクラスメイトで、頼りになる同寮生でもある。\n
一緒に馬鹿をやるのが楽しくて、それでいて頼りになって……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「あああ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭を掻きむしりたくなる。\n
どんどんと、体温が上がっていく。"

jump gakuen_boris4_4
label gakuen_boris4_3b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（いえいえ！\n
気の迷いよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "危ういところを助けてもらったから。\n
もしくは、今のところ一番仲のいい友達だから。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうしてイベントごとにテンションが上がっている今、勘違いしてしまっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう思うのに、言い聞かせる言葉とは裏腹にどんどんと体温が上昇していく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（危ういところを助けてもらったっていっても、そもそもの原因はボリスだし……！\n
どきどきするのはお門違いよ！）"

jump gakuen_boris4_4
label gakuen_boris4_4:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いよいよテンションがおかしな方向へ向かっている。じっとしていられなくなって、私は部屋の中でうろうろと歩きまわり出してしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、そこで。"

play sound se_0648 volume .3 ##loop="true"

play music magic_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこからか、猫の鳴き声が響いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本物の猫の鳴き声というよりは、玩具のアラームのような響きだ。\n
けたたましく、響き渡る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（え、何……っ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな音のするアイテムに覚えはない。\n
だが、確実にその音は私の部屋の中から聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「どこ……っ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その音源を捜して、私は耳をすましてみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（クローゼット？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、その音はクローゼットの中から響いているようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "クローゼットの中には、小物も少々しまっているものの、基本的には洋服類。\n
そんな音が鳴るようなものをしまったことなどない。"

play sound se_0275 volume .7
play sound se_0648 volume .6 ##loop="true"
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "猫の鳴き声が、少し大きくなった。\n
音源はクローゼットで間違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「な……、なんなのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "再び耳をすましてみる。\n
扉を開けたせいか、音はよりはっきりと聞こえ、音源はすぐに分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ハンガーにかけてつるしてあった、私の制服だ。\n
制服のポケットの中から、その音は響いている。"

play sound se_0186
pause .15
play sound se_0648 ## loop="true"
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……うるさっ！\n
って、これ……」"


show m_bor4_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ポケットの中から出てきたのは、ピンク色も鮮やかな猫を象った少し厚めのカードのようなものだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人相（猫相？）悪めにデフォルメされた猫の顔の形をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にゃあにゃあという鳴き声は、そこから響いていた。\n
更によく見ると、つりあがった三白眼がぴかぴかと光っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……ボリス、よね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピンクの猫なんていう奇抜なものから連想するのは彼しかいない。\n
それに彼ならば、私のポケットにこのカードを滑り込ませるのも簡単だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「な、なんの嫌がらせ……。\n
これ、どうやったら鳴きやむのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脱力感に襲われつつも、笑ってしまった。\n
ボリスらしい悪戯だ。"

hide m_bor4_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ついっと指先で猫の鼻面を撫でてみる。"


play sound se_0014 ##loop="false"
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "猫が鳴き止んだ。\n
その代わり、ざざざと受信状態のよくないラジオのような音が響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ノイズに混じって、音がする。\n
何か聞こえないかとそのカードを耳にあててみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0315
Boris "「おーい！\n
聞こえてるか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "{size=+20}「！！！！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスの声がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「き、聞こえているわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "考えるより先に、返事をする。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0316
Boris "「お！\n
繋がった繋がった！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、この猫カードは声の転送魔法が仕込まれたマジックアイテムだったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるで人相の悪い猫が喋っているかのように、ボリスの声が聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（もう、驚かせて……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_5")
T "「……また面白いことしているのね。\n
これも、ボリスの実験？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……実験というか、悪戯）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice bor_g0317
Boris "「まあね！\n
うお……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「ボリス！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……ボリス？\n
ねえ、ちょっと、ボリス？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何やら切羽詰った声と同時に、ノイズが入る。\n
しばらく猫カードに向かってボリスの名前を呼びかけてみるものの、応答はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0318
Boris "「ざざ……っ……くっそ……！\n
速度でいけると思った……ざざっ……」"

play sound se_0014
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「ざざざっ……。\n
[firstname]っ……ざざっ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声は聞こえるが、私の声は届いていないようだ。\n
一体、ボリスはどこで何をしているのだろう。"

play sound se_0299
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しでも状況を聞き取れないかと、猫カードへと耳を押し付ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……風？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ノイズに混ざって、風のような音。\n
もしかしなくとも、ボリスは今外にいるのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（門限、過ぎているわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "通常なら、もう寮の外には出られない時間だ。\n
だが、室内ではあんな音はしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前に、ボリスと一緒に暴走タイルに乗ったときの音を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……高速移動中？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それならばやたらと音声が途切れがちになるのも分かる気がする。\n
私は猫カードに耳に当てたまま、窓へと向かった。"

play sound se_0165
pause 1
play sound se_0585
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しゃっとカーテンを開けて窓の外をうかがう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！！？」"


play music opposition2_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、その外で繰り広げられていた光景に絶句した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ボ、ボリス何やって……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは私の予想通り外にいた。\n
ついでに言うならば、高速移動というのも当たっている。"

play sound se_0729

show m_bor4_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夜でもピンクは目立つ。\n
ボリスは、澄み渡った夜空を背景に使用人達と箒チェイスを繰り広げていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろんあのボリスの箒だから、改造済みなのだろう。\n
普通のように跨るのではなく、まるでボードのように箒の上に立っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風にのって滑空するように飛ぶ。\n
その姿は競技のようにも見えた。"

play sound se_0739
hide m_bor4_2
show m_bor4_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0319
Boris "「あ……っ！\n
見つけた！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "猫カードから、そんな声が聞こえるのと同時に、私の視線の先でボリスがくるりと宙返りで方向を変えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう……、こちらに向かって。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え？？？\n
えええええっ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice bor_g0320
Boris "「ちょーっと危ないから、窓から離れていたほうがいいぜ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓を開けたことにより通信状態がよくなったのか、ボリスの声がクリアに聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、言われた内容のほうはといえば、即座には理解できないようなものだったのだが。"

play sound se_0736
pause .3
play sound se_0400
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐんっとボリスが加速する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれだけのスピードを出していて、更に加速するとは。\n
彼の改造技術は、口だけではないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0035
Servant "「待ちなさい……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0058
Servant "「は、早い！\n
追いつけない！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人達も、手を抜いているわけではないだろうに、なかなか追いつけていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……何をやっているんだろう。\n
真夜中の箒競争？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（でも……、さすがスピードマニア。\n
すごいなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、のんきに観戦してしまうものの、彼らはこちらへ向かってきている。\n
急な状況に危機を察知するのが遅れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（って……！\n
あのスピードでここにつっこんできたら危なすぎない……！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしなくとも、危険すぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人達に捕まらず私の部屋に飛び込むことが出来たとして、あの速度で止まれるとは思えない。\n
ものには惰性というものがあるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも、門限をとっくに過ぎた時間に使用人達を振り切って私の部屋に突撃してくることに何の意味があるのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たとえ外で使用人達を振り切っても、すぐさま部屋に踏み込まれて捕まるに決まっている。\n
なんのために、どうして……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（また、何かの悪戯？\n
それとも、悪戯をして逃げているの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓の脇に避難しつつも、はらはらしながら外を覗く。\n
ふと気づくと、周囲から歓声が聞こえていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0026
Seito "「逃げてー！！\n
逃げ切ってボリスー！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0016
Seito "「こう、こなくっちゃ！\n
これこそストームの醍醐味よね！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0052
Seito "「ボリスは今回もスピード勝負なのね。\n
頑張ってー！！」"

play sound se_0793 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いわゆる黄色い歓声、というやつだ。\n
女子側はわきたっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……ストーム？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞きなれない単語が混じっていたが、今はそれについてを考えている余裕はない。\n
ボリスの姿がぐんぐんっと私の窓へと近づいてきて……。"

play sound se_0743 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0321
Boris "「どいてろよ……！！\n
にゃははは、いっくぜ～！！」"

play sound se_0373
hide m_bor4_3
show bg06_sk_h_nig onlayer master with Dissolve(.2)
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスが、だんっと踏み切って、高速移動を続けていた箒の上から飛び降りた。\n
まだまだ窓枠からは距離がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「……っ！！」"

play sound se_0348
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "惰性で動き続ける箒を片手で掴み、その箒にぶら下がり、ぐいっと体を持ち上げるようにして跳ね飛ぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴんっとしなった体が風を切って一直線に私の部屋へと飛び込んできた。"

play sound se_0091
play sound se_0553
camera at hpunch
camera at vpunch

scene bg24_rj_nig_lon with Dissolve(.2)
hide bg06_sk_h_nig


show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……{size=+20}！！！{/size}」"

hide bor_m_01_11
show bor_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice bor_g0322
Boris "「……よっしっ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓の外が、一拍置いて、わあわあと騒がしくなった。"

play sound se_0386
hide bor_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0027
Seito "「今の見た！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0017
Seito "「決まったわよね！\n
格好いい！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0053
Seito "「純粋なスピード勝負で、使用人から逃げ切ったわ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "スポーツ観戦のノリ。\n
盛り上がりっぷりは最高潮だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、私には何がどうなっているのかが分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスがこんな時間に、派手なパフォーマンスで私の部屋へと突撃してきた理由も分からなければ……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その彼を追いかけ、私の窓近くまでやってきた使用人達が、諦めたような表情を浮べて去っていくのも謎だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（怒られて、連れ戻されるところじゃないの？\n
ここ、女子寮なのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……？？？」"


play music room2_p_wam

show bor_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice bor_g0323
Boris "「はは。\n
訳が分からないって顔してるね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……ええ、実際に訳が分からないもの。\n
何がどうなっているの？」"

hide bor_m_02_6
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice bor_g0324
Boris "「これ、ストームっていうイベントなんだ。\n
今日一日、朝から騒がしかったのはこれが原因ってわけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ストーム……？\n
さっきも誰かがそんなことを言っているのを聞いたんだけど……、ストームって何なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人きり。\n
妙に緊張する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは女子寮で、男子禁制。\n
だが、緊張するのは不慣れな状況にだけではない。"

hide bor_m_01_10
show bor_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0325
Boris "「ストームっていうのはね。\n
男子生徒が女子寮に忍び込んで親睦を深める、っていうイベントなんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「それ……、まずいんじゃないの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夜に女子寮に忍び込んで、親睦を深める……なんて。"

hide bor_m_03_4
show bor_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0326
Boris "「はは、いかがわしい内容じゃないぜ？\n
健全な、お祭り騒ぎだ」"

hide bor_m_03_10
show bor_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0327
Boris "「肝試しみたいなもの、って言ったら分かりやすい？\n
使用人達の目をいかにくぐりぬけるかってのが、醍醐味なんだよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……だから、誰もあなたを捕まえにこないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳をすましても、私の部屋に使用人達が駆けつけてくる気配はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目的地、ゴールに辿り着いてしまえば、それ以上の邪魔はしないということなのだろうか。"

hide bor_m_02_7
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0328
Boris "「そういうこと。\n
本当は、姿隠しの魔法なんかを使って侵入するのが普通なんだけどね」"

hide bor_m_01_10
show bor_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0329
Boris "「魔法の技を試す機会でもあるから、他の連中も手段は色々……。\n
俺は、シンプルに正面突破で振り切ったけどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……それ、力技すぎるわよ」"

hide bor_m_03_2
show bor_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice bor_g0330
Boris "「にゃはは。\n
だって使用人達と本気のレースなんて、こんなときじゃないと出来ないだろ？」"

play sound se_0738
play sound se_0744
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くるりっとボリスが箒を手の中で回してみせる。\n
その動きにあわせて、しゅるしゅると箒が小さくなっていった。"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「どうりで、新入生の男子は緊張していると思った」"

hide bor_m_01_6
show bor_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice bor_g0331
Boris "「ああ、うん、だろうね。\n
２回目以降の生徒なら楽しめるだろうけど、入りたてで、魔法の腕試しなんて緊張するだろうな」"

hide bor_m_01_12
show bor_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice bor_g0332
Boris "「でも、一応メインは新入生でさ。\n
本当は男女の仲をよくするっていうより、新入生との親睦を深めるのが目的なんだよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「新入生との？」"

hide bor_m_03_10
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice bor_g0333
Boris "「そうそう。だから、あんたも何も知らされてなかっただろ？\n
上級生と新入生じゃ、年齢の上下に関わらず、意外と交流が少ないからさ……」"

hide bor_m_01_11
show bor_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice bor_g0334
Boris "「そういう何も知らない女子相手に、説得して、部屋に入れてもらうっていうな。\n
結構な無茶振りだよね」"

hide bor_m_03_11
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice bor_g0335
Boris "「どういうふうに進めるか、侵入方法とかも、経験者が新入生に教えたりするし……、男子生徒同士でも仲良くなる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「こういったイベントで、一気に交流を図ろうってことね。\n
たしかに、こういったハプニングみたいなのを乗り切れば仲良くなれるかも」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……でも、新入生の女子側はもっとパニックになるわよ。\n
知らない男子生徒なんか来たら、部屋に入れたりなんか出来ないでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私だって、ボリスだからこそ、こうしてまともに話せているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来入ってこられないはずの女子寮に男子が侵入。さらには自分の部屋に訪ねてくるなんて事態になったら、今以上に取り乱していただろう。"

hide bor_m_01_10
show bor_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0336
Boris "「そういう場合は、同性の上級生が間に入ってとりなしたりする」"

hide bor_m_02_1
show bor_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0336_5
Boris "「うまくいかなくて追い出されたとしても、後々で顔見知りになって仲良くなれたりするし、きっかけとしてはいいみたいだよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「なるほど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、目的やイベントの主旨を聞いても、不思議だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……ね、ボリス。\n
なんで、あなたが私の部屋に来たの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人とレースがしたいという目的があったとしても、彼ならば他にも部屋に入れてくれる女友達がいくらでもいるはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人懐こくて、気安いボリスには男女関係なく友人が多い。\n
新入生の知り合いだって、私だけではないはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（ああ、でも、クラスメイトで新入生っていうのは私だけか）"

hide bor_m_02_4
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice bor_g0337
Boris "「んん？\n
なに、あんた、俺じゃ不満だったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すいっとボリスが私へとの距離を詰める。\n
その頭上で、猫耳が揺れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いや、不満なんかじゃないけど……。\n
……クラスメイトだものね」"

hide bor_m_01_11
show bor_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice bor_g0338
Boris "「まあ、そうだね。俺達はクラスメイトで、あんたは新入生。\n
当てはまるから訪ねてきたっていうのもあるけど……」"


play music gloomy_a_wam
hide bor_m_03_13
show bor_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice bor_g0339
Boris "「……ねえ、[firstname]。\n
なぞなぞしようよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……なぞなぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりするりと足音もなく近づくボリスが、いつの間にか近くにいる。\n
本物の猫のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "距離感を見誤ってしまいそうになる。"

hide bor_m_03_9
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0340
Boris "「そ、なぞなぞ。\n
あんたに答えてほしいんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……答えられるような内容なら」"

hide bor_m_01_10
show bor_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0341
Boris "「あんた以外には答えられないなぞなぞだよ。\n
だから、当ててね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……プレッシャーだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これも、イベントの一環なのだろうか。\n
断れない雰囲気がある。"

hide bor_m_02_2
show bor_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0342
Boris "「それじゃあ、いくよ？\n
なぞなぞ……」"

hide bor_m_01_12
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0343
Boris "「俺が、他の男をあんたの部屋に行かせたくないと思うのはどうしてだと思う？\n
スピード重視で、一番先に駆けつけたかった理由は、なんでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……ええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間の抜けた声が出た。\n
ボリスの出したなぞなぞの内容が、理解できない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（というか、これって、なぞなぞなの？）"

hide bor_m_01_10
show bor_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0344
Boris "「だから、俺があんたを独り占めしたい理由。\n
これ、な～んだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……っ。\n
さっきと問題文自体が違うわよっ！！」"

hide bor_m_03_8
show bor_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice bor_g0345
Boris "「答えは一緒だから問題ないよ。\n
……ね、当てて？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "甘えた声音で囁かれて、心臓が跳ねる。\n
ドキドキと脈打って、熱を吐き出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その熱が頬まで上がってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（そんなの……）"

menu:
    "からかわないで。":
        jump gakuen_boris4_5a
    "私のことが好きだから？":
        jump gakuen_boris4_5b
label gakuen_boris4_5a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……からかわないでよ」"

hide bor_m_01_13
show bor_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice bor_g0346
Boris "「……ハズレ。からかってなんかいないよ。\n
ハズレたからには、罰がないとね」"

play sound se_0052 volume .6

show m_bor4_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……っ！！」"


play music residence_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "答えたつもりはない、と言うより先に、くりっと首を傾げたボリスに唇を押し当てられていた。"

jump gakuen_boris4_6
label gakuen_boris4_5b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「…………。\n
……私のことが好きだから？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "冗談だといって、引き下がれる程度に軽いノリでそう口にする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは冗談を言っているようには見えない。\n
かといって、自惚れるわけにはいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はそんなにもてるタイプではないし、ボリスは遊園地寮の寮長で、場を盛り上げたり引っ張ったりする立場。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（つまり、結構もてるタイプ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼からの好意は感じつつも、確信が持てるような相手ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大体、私はもう同じような失敗を繰り返すのは御免なのだ。\n
失恋がどれほど厄介で尾を引くのかは、すでに経験済み。"

hide bor_m_02_4
show bor_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0347
Boris "「……正解。\n
当たったんだから、ご褒美あげないとね」"

play sound se_0052 volume .6

play music residence_p_wam
hide m_bor4_4
show m_bor4_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言って、ボリスはくりっと首を傾げて私へと唇を押し当てた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……っ！！」"

jump gakuen_boris4_6
label gakuen_boris4_6:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "猫のような仕草。\n
触れるだけのキスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じんわりと熱が伝わってくる。\n
ちゅ、と唇が浮いてボリスが囁く。"

hide m_bor4_4
show m_bor4_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0348
Boris "「そんな目を見開いたら、おっこちちゃうよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「そ……。\n
そんなに目、大きくないわよ、私」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice bor_g0349
Boris "「え～？\n
……可愛いよ、あんた」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「か、可愛いって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_10")
voice bor_g0350
Boris "「大好き」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「え、ええええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（ボリスが、私のことを好き？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さらっと言われて、頭の中が真白になる。\n
そんな私に、彼は上機嫌で、楽しげだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0351
Boris "「あんたと一緒にいると楽しいんだよね。\n
だから、もっと一緒にいたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0352
Boris "「あんたは？\n
俺と一緒にいて、楽しい？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "至近距離から顔を覗きこまれて、聞かれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……楽しい、と思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0353
Boris "「じゃあ、俺と付き合ってよ。\n
もっともっと楽しませてあげるからさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（ノリが軽い……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな簡単に、付き合うだとか付き合わないだとか決めてしまっていいのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋人関係。\n
私にとっては、重いことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ボリスに対していると、なんだかそんなに構えなくてもいいことのように思えてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0354
Boris "「ね？\n
あんたも、俺のこと、好き？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちゅっと、また軽くキスをされる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼうっとしてしまう。\n
頭がうまく、働かない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「わ、私は……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice bor_g0355
Boris "「……嫌いじゃないだろ？\n
それなら、いいよね？付き合って」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなに簡単にはいかない。\n
ボリスは私が返事をする前に遮ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「え……、ええと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0356
Boris "「ね、頷いてよ。\n
頷いてくれるだけでいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうねだりながら、ボリスは何度も繰り返し口付ける。\n
小さなリップノイズが、何度も何度も静かな部屋に響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「っ……。\n
か、考えさせて……っ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ようやくそれだけを言った。\n
断るにも、受けるにも、簡単にすませていいことではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少なくとも、私にとっては重大事だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（ちゃんと、考えなきゃ）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……でも、何を？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私だって、ボリスのことをよく思っていた。\n
好意を持っていることを、意識し始めていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、私を好きだと言う。\n
そして、付き合いたい、と。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前の私や、私の想い人だった人と違って、彼は躊躇わない。\n
仲介を求めるなんて、考えもしないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "軽いといえば、そうかもしれない。\n
だが、潔い。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0357
Boris "「だめ。\n
考えるんじゃなくて、今思っていることをそのまま答えてよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつのまにか腰に回った腕が私を抱き捕らえ、逃がしてくれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0358
Boris "「俺のこと、好き？嫌いじゃない？\n
付き合っていいと思う？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「う……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "猫に捕まり、その手の中で転がされるネズミか小鳥にでもなった気分だ。\n
ぱたんぱたんと揺れる尻尾が、私を急かすように腰を緩やかに叩く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（う……、ううう）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice bor_g0359
Boris "「ねえ、頷いて。\n
付き合うって言ってよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0360
Boris "「いいかなって、ちょっとでも思ってくれているならさ。\n
……思って、くれるだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……うん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "プレッシャーに負けて、こくんと頷いてしまった。"

play sound se_0063 volume .6
hide m_bor4_5
show m_bor4_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0361
Boris "「……ん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスが満足げに頷いて、ぎゅっと私を引き寄せる。\n
抱きしめられると、体温が直で伝わってしまうような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなにも赤くなって、熱くなって、心音が早くなっているのが、全部バレてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……これで、好きじゃないって言っても、それこそ説得力がないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_9")
voice bor_g0362
Boris "「あんたのこと、好きだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ」"

hide m_bor4_6
show m_bor4_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くいっと顎先を持ち上げられて、キスを落とされる\n "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……っん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "吐息すら絡め取るかのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0363
Boris "「……やっぱり、目が落ちちゃいそう。\n
あんた、本当に可愛いよな」"

hide m_bor4_7
show m_bor4_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後、ご機嫌に呟いたボリスが、ぺろりと私の瞼を舐めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……猫が、ご馳走を食べた後みたいだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゆらゆらと揺れる尻尾と、ぴこぴこと揺れる耳。\n
分かりやすい感情表現。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……全然、違う）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後のとき。\n
手紙さえ渡せない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あんなふうな恋ではない。"

play sound se_0627 volume .6
hide m_bor4_8


play music night_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「！」"

hide bor_m_02_4
show bor_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice bor_g0364
Boris "「……ちぇ。\n
あんたともっと遊んでいたいのにな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「何なの、あの音」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞きながらも、大体の見当はついていた。"

hide bor_m_03_9
show bor_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0365
Boris "「ストーム終了の合図だよ。\n
あーあ、寮に戻って点呼とらねえと」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……そっか。\n
あなた、寮長だものね」"

hide bor_m_01_3
show bor_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_g0366
Boris "「まあね。\n
おっさんに丸投げしたいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……頑張りなさいよ」"

hide bor_m_03_13
show bor_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice bor_g0367
Boris "「え～。頑張りたくなんかないよ。\n
すぐにお別れなんて……、元気が足りない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（……嫌がられないかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと手を伸ばして、ボリスの頭に触れる。\n
柔らかな猫っ毛だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……ぐずらずに、戻らないと駄目よ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くしゃくしゃと撫でてみる。"

hide bor_m_01_9
show bor_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0368
Boris "「……っ！\n
俺、撫でられるの好きだよ」"

hide bor_m_03_4
show bor_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0369
Boris "「あんたに撫でられるのは、特別に好きだ。\n
ね、もっと」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……帰りなさいって。\n
点呼とらないといけないんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わしゃわしゃ。\n
指先に時折触れる、柔らかな猫耳の感触がくすぐったい。"

hide bor_m_01_13
show bor_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0370
Boris "「じゃあ、また撫でてくれる？\n
今度はもっと、誰にも邪魔されないときに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「ええ、撫でてあげるから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話がやたら甘ったるい。"

play sound se_0627 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "また、笛が響く。\n
二回目だ。"

hide bor_m_02_5
show bor_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0371
Boris "「っち。\n
しつこいなあ……、いいとこなのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは忌々しそうに舌打ちしながらも、ようやく私を抱いていた腕を解いてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（いいところ、って……）"

hide bor_m_02_13
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
voice bor_g0372
Boris "「あ、そだそだ。\n
お土産に何かちょうだい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（お土産？？？）"

hide bor_m_01_10
show bor_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice bor_g0373
Boris "「ストームって、肝試しみたいなものだって言っただろ？\n
だから、ちゃんと女子の部屋に入れてもらえたっていう証拠が必要なんだよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまり、戦利品のようなものか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「証拠、ねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線を周囲にめぐらせる。\n
何か、女子寮侵入の証拠になりそうなもの……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教科書や、マジックアイテムの類はあんまりそんな感じがしない。\n
やはり、女性らしいアイテムがいいだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……あ。\n
リボンでどう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "入浴の際に外し、机の上に置いてあったリボンを手に取った。\n
これならば、充分に侵入を果たしたという証拠になるだろう。"

hide bor_m_03_10
show bor_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0374
Boris "「ん、ばっちりだ。\n
これ、貰っていくよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……返してはくれないの？」"

hide bor_m_01_5
show bor_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0375
Boris "「それはブリーズの夜にね。\n
一週間後に、今度はブリーズってイベントがあるんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「まだあるの！？」"

hide bor_m_02_1
show bor_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0376
Boris "「そう嫌がらないでよ、セットになるようなイベントだから。\n
ストームとブリーズって」"

hide bor_m_01_9
show bor_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0377
Boris "「ブリーズは、女子が男子寮に攻めてくるんだよ。\n
盗られたものを取り返しに、ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……この学校って、意外とイベント好きよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どの学校も、学生寮のお祭り騒ぎは珍しくない。\n
ただ、学校公認のものとしては、多いのではないだろうか。"

hide bor_m_03_7
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0378
Boris "「はは、いいことだろ？\n
んじゃ、また明日教室で」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ええ、また明日」"

hide bor_m_01_10

play sound se_0117
pause 1
play sound se_0216
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは私からリボンを受け取ると、窓をひょいと身軽に乗り越えていった。途中何か魔法を使ったのか、着地は軽やかだ。"

play sound se_0619 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "足音とともに、その背中が闇の中に見えなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……うわあ」"

play sound se_0328
play sound se_0327 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怒涛の展開に、そんな声が漏れた。\n
ふらふらっと窓から離れて、ベッドへと倒れこむ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（ボリスが、私のことを好き？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キスをして、付き合ってくれとせがまれ、それに頷いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（ということは……、恋人なの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋人なんていう甘ったるい響きに、転げまわりたいような衝動にかられる。\n
私に恋人が出来るなんて、自分でも信じられない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも相手は、ボリスだ。\n
気になる相手で、猫みたいな男の子。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "胸の中がくすぐったくて、ふわふわとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……今、私、絶対馬鹿みたいな顔をしているわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスの言うように、目が零れ落ちそうになっているというのも有り得る。\n
今ならどんなことでも起こり得そうな気がして、怖くて鏡が見られない。"

with dis
$ hi_mes()

scene bg24_rj_nig with Dissolve(.8)

scene bg_par15_rg_amu_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_boris5
