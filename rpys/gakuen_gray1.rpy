
scene bg25_rr_day
with dis
label gakuen_gray1:
$ clockanim()


play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（共同区域……、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまでは学校生活に馴染むのに必死で、塔の探索などあまり考えたことがなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自室とカフェテリアと、その他最低限の施設しかまだ利用したことがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後、せっかく時間があるので、探索してみるとしよう。\n
共同区域まで出てみる。"

with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろいろとプレートが出ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……いろいろあるのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まずはどんな場所があるのか一通り見てまわってみるとしようか。\n
それから、どこか一つの場所に入ってみればいい。"

play sound se_0158
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう方針を決めて、のんびりとした足取りで歩き出す。\n
と、少し離れたところで声が聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0067
Gray "「ナイトメア先生ーー！！\n
ナイトメア先生、どこですかー！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（この声は……、グレイだわ）"

menu:
    "声のするところに行ってみる。":
        jump gakuen_gray1_2a
    "放っておく。":
        jump gakuen_gray1_2b
label gakuen_gray1_2a:
$ lovechara_gray_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ナイトメアを探しているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が行って何が出来るというわけでもないが、どうせ暇をしていたのだ。\n
ナイトメア探しを手伝ってもいいかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声のするほうへと歩き出す。"

jump gakuen_gray1_3
label gakuen_gray1_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ナイトメアを探しているのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "残念ながら、今日一日、ナイトメアを見かけてはいない。\n
声をかけても、助けにはなれないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう考えている間にも、ナイトメアを探すグレイの声はどんどんと近付いてきた。"

jump gakuen_gray1_3
label gakuen_gray1_3:

with dis
$ hi_mes()

scene bg_par15_rg_tow_day with Dissolve(.8)

scene bg25_rr_day
with stripe_l_long

play music gray_t_ali

show gre_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0068
Gray "「ナイトメア先生ー！！\n
……と、君か」"

hide gre_m_02_10
show gre_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0069
Gray "「こんなところで、どうしたんだ？\n
慣れない場所だろうから……、迷子にでもなったか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「違うわ。\n
共同区域にいろいろな施設があると聞いたものだから、探索に来てみたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「あなたは……、ナイトメア探し？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "交流が増えても、初対面の印象から変わらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分もナイトメア探しで忙しいだろうに、ひとけのない廊下でうろうろしていた私を見過ごさないなんて、彼はやはり親切だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして会うたびに声をかけてくれる。\n
塔の執務長なんていう仕事についているだけあって面倒見がいい。"

hide gre_m_03_10
show gre_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0070
Gray "「ああ、そうなんだ。\n
医務室で仕事をしていたはずなんだが、少し目を離した隙に逃げられてしまった」"

hide gre_m_03_11
show gre_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0071
Gray "「君はこの辺りで、ナイトメア先生を見なかったか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ごめんなさい。\n
見ていないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「でも、何かあったときに、学校医に連絡がつかないなんて困るわね。\n
ナイトメアってば、いい加減なんだから」"

hide gre_m_01_11
show gre_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gra_g0072
Gray "「いや、そうじゃない。\n
その辺りはあの人もちゃんとしているよ」"

hide gre_m_01_12
show gre_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gra_g0073
Gray "「怪我人や病人が出たりなど、緊急時にはそれ用に連絡方法が決めてある。\n
だから、安心してほしい」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……変なの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは困っているのだとナイトメアの愚痴を漏らしていたはずなのに、私が彼を批判するようなことを口にすると、やっぱり困った顔でフォローしようとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（この人って……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「その緊急用の手段で、ナイトメアを呼び出すとまずいの？\n
それを使うと、ナイトメアが来るんでしょう？」"

hide gre_m_01_6
show gre_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_g0074
Gray "「いや、それはそうだが……。\n
上司相手に嘘をつくのは、やはり躊躇ってしまうな……」"

hide gre_m_01_11
show gre_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_g0075
Gray "「それに病人や怪我人が出たというのは、喜ばしくない嘘だろう？\n
我々は魔法使いだ、無闇に言葉を乱用するのは避けなければ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……間違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（この人ってば、いい人なんだわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誠実な態度に、感動してしまった。\n
ここシンフォニアにきて、会う人会う人、皆が一筋縄ではいかない癖のある人物ばかりだったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさか自寮に、こんな常識人がいてくれたとは。"

hide gre_m_01_13
show gre_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gray "「……？」"

hide gre_m_01_12
show gre_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0076
Gray "「……どうした？\n
俺の顔に何かついているか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「い、いえ……っ。\n
なんでもないわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "驚きもあって、不躾なまでにまじまじと眺めてしまっていた。\n
訝しげな視線を返されて、失礼にならない程度に慌てて目をそらした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「それであなたは、こうして地道にナイトメアを探しているのね？」"

hide gre_m_03_1
show gre_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice gra_g0077
Gray "「ああ、俺の進められる範囲の仕事はもうすんでいるからな。\n
そうなるとただ待っているだけよりも、探したほうがいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……上司に苦労させられているわね」"

hide gre_m_03_6
show gre_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice gra_g0078
Gray "「……いや、悪い人ではないんだが。\n
なにぶん、書類仕事を蛇蝎のように嫌ってらっしゃるんだ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉尻に疲れが滲んでいる。\n
それじゃあと、グレイは私に背を向けて再びナイトメア探しに行こうとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何が出来るというわけではないのに、その背に声をかけていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（どうせ何か目的があったわけでもないし……）"

hide gre_m_02_12
show gre_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice gra_g0079
Gray "「ん？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「私も手伝うわ。\n
一人より二人のほうが広範囲を探せるでしょう？」"

hide gre_m_02_9
show gre_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice gra_g0080
Gray "「俺は助かるが……、君は構わないのか？\n
探索の途中だったんだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「探索のついでよ。\n
寮内を見てまわるついでに、ナイトメアも探すってだけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私にとっては、何の負担にもならない。\n
だが、グレイにとってはかえって負担になってしまうかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……駄目、かしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "職員の仕事は職員の仕事だ。\n
生徒がそれにちょっかいを出すような真似はやはり敬遠されてしまうだろうか。"

hide gre_m_03_9
show gre_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0081
Gray "「……君は優しい子だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よく言えば真面目、悪く言うならば硬い表情を浮かべていた彼の雰囲気がふわりと緩んだ。\n
人見知りをするタイプなのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（こういう、硬そうな人が笑うと破壊力あるわね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "特別に気を許してくれているのではないかと思ってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し近くなっただけの距離に、妙な期待を寄せてしまうのはありがちな話だ。\n
特別扱いや好意に弱いのは、誰でも同じ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（物腰がスマートっていうか……。\n
真面目そうだけど、女性の扱いがうまそう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いかにもな遊び人よりも、こういうタイプのほうが危険と聞く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（実は、女遊びが派手とか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "職務と上司に忠実で、尚かついい人なんていうのはどうも出来すぎている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（まあ、そこまでプライベートを気にすることもないか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の執務長としての彼は優秀だし、私に対して親切であることに変わりはない。"

hide gre_m_01_4
show gre_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0082
Gray "「それなら、手伝ってもらっても構わないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「ええ、任せて」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメア探索をするのに、グレイの人格など気にする必要はない。"

with dis
$ hi_mes()
hide gre_m_03_4


scene bg25_rr_day with Dissolve(.8)
scene bg_par15_rg_tow_day
with stripe_l_long

$ time_effect()##PLEASE MANUALLY ADJUST ME
play music entrance_p_wam

scene bg_par20_re
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「考えてみれば……。\n
シンフォニアの広大な敷地内で、一人を探すなんて結構な無茶よね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔のエントランス。\n
私達は、力なく柱に背を預け、立ち尽くしていた。"


show gre_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0083
Gray "「……そうだな、これでも普段は、わりと見つかりやすいところにいてくださるんだが……。\n
今日は、本格的に逃亡しているらしい」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（逃亡に、見つかりやすいところにいてくれるも何もあるのかしら……）"

hide gre_m_02_11
show gre_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gra_g0084
Gray "「何がご不満なんですか、ナイトメア先生……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここにはいないナイトメアに対し、呪詛のように、グレイが呻く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の共同区域はしらみつぶしに探した。\n
これだけ探して見つからないということは、グレイの言う通りナイトメアも本気で逃げているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたらすでに塔の外へと出ている可能性もある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ねえ、魔法で探してみたらどうかしら。\n
ナイトメアの魔力波形とか、あなた知らないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達はこれまで、魔法に頼らず体力と直感だけを頼りにナイトメアを探してきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは私よりも優れた魔法使いであり、この捜索の主体となるべきグレイがその手段を使おうとしていなかったからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かしらの考えがあってのことだと思った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、体力勝負にもそろそろ限界がある。\n
本当にナイトメアを見つけたいならば、魔法を使うべきではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（その方が、簡単だわ）"

hide gre_m_02_6
show gre_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の提案に、グレイは困ったように眉尻を下げた。"

hide gre_m_03_3
show gre_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0085
Gray "「君を巻き込んでしまって悪いんだが、俺はナイトメア先生を探すのに魔法は使わないようにしているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「どうして？」"

hide gre_m_03_6
show gre_m_01_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice gra_g0086
Gray "「魔法を使うと……、簡単に捕まえてしまえるだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「……え～と？？？\n
見つけたい……のよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（探しているのに、簡単に捕まえたらいけないなんて……）"

hide gre_m_01_14
show gre_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice gra_g0087
Gray "「ああ、見つけたいとも。\n
しかし、簡単に探して、簡単に捕まえてしまうのはナイトメア先生のためにならない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ナイトメアのためにならない……、ってどうして？\n
仕事をサボって逃げ出しているのを捕まえるんだから、ためになるんじゃない？」"

hide gre_m_01_12
show gre_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_g0088
Gray "「簡単に捕まえられてしまえば、罪悪感も軽くなってしまうだろう？」"

hide gre_m_03_7
show gre_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_g0088_5
Gray "「どうせ簡単に捕まるんだし、と気軽に逃げ出されるようになってしまっては、あの方が困ることになる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「今だって、困っているんじゃないの？\n
……グレイが」"

hide gre_m_03_3
show gre_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice gra_g0089
Gray "「だからこそ、自主性を求めたいんだ。\n
徐々にでも意識を変えていかないことには、精神的な成長を阻害するから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（お、お母さんみたいだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょっと怯んでしまった。\n
彼とナイトメアの関係がよく分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "上司と部下でありながら、ここまで部下に慕われる……、というか面倒をみられている上司なんて、普通はいないのではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（上下関係はあるのに、家族みたい）"

hide gre_m_01_13
show gre_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gra_g0090
Gray "「こうして苦労して探している姿を見ると、あの方も反省して、その後しばらくは真面目に仕事に取り組んでくださる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「まあ、つまり、罪悪感を覚えさせて、徐々に逃げにくくしようと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……でも、逃避癖のある人って、そうそう直らないんじゃないかしら）"

hide gre_m_01_12
show gre_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice gra_g0091
Gray "「……巻き込まれてしまった君にとっては、迷惑な話だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「そんなことないわ。\n
立派だと思う」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（そう……。\n
立派な教育方針……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠回りでも、相手にとっていい方法かもしれない。\n
だが、普通はそこまでしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "子育てのテーマを追求する母親のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（こんなに頑張っているのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "俯きがちに足元を見ているグレイは、見つからないナイトメアに対して、さすがに疲れている様子。\n
どうにかして元気づけられないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私ではナイトメアの仕事の代理にはなれないし、代わりにやってはそれこそ精神的な成長とやらを阻害する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法を使ってナイトメアを見つけ出すのも駄目だとなると、出来ることはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ねえ、グレイ、カフェテリアでお茶にしない？\n
一息入れたらどうかしら」"

hide gre_m_03_3
show gre_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gra_g0092
Gray "「……休憩、か。\n
そうだな、このまま探していても仕方ない」"

hide gre_m_02_12
show gre_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Gray "「…………」"

hide gre_m_02_3
show gre_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gra_g0093
Gray "「そうだ、テイクアウトにしても構わないか？\n
君を案内したい場所がある」"

menu:
    "喜んで。":
        jump gakuen_gray1_4a
    "迷う。":
        jump gakuen_gray1_4b
label gakuen_gray1_4a:
$ lovechara_gray_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……？\n
ええ、喜んで」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（どこに連れて行ってくれるのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の内部、共同区域に関しては、たった今、念入りな探索を終わらせてきたばかりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今更、改めて案内したい場所というのに心当たりがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、相手は塔を熟知している。\n
どこか、通常では足を踏みいれないような場所に案内してもらえるのかもしれない。"

hide gre_m_02_4
show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0094
Gray "「それじゃあ、行こうか。\n
そう迷いなく頷かれてしまうと、エスコートの責任重大だな」"

jump gakuen_gray1_5
label gakuen_gray1_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……？\n
案内したい場所？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は訝しげに彼の言葉を繰り返す。\n
塔の内部、共同区域に関してはたった今、念入りな探索を終わらせてきたばかりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今更、改めて案内したい場所というのに心当たりがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……まだ、どこかあるの？」"

hide gre_m_02_2
show gre_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_g0095
Gray "「ふ、君が不審に思うのも仕方ない。\n
だが、これでも塔に関しては詳しいんだ」"

jump gakuen_gray1_5
label gakuen_gray1_5:
play sound se_0774
hide gre_m_01_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "冗談めかして言ってから、グレイは柱に預けていた背を立て直し、歩き出す。\n
私も、その後を追った。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（そんなふうに言われちゃうと、特別な場所に連れて行ってくれるのかなって期待しちゃうな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一人の探索では、行き着けないような場所へ。"

with dis
$ hi_mes()

scene bg_par20_re with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_par15_rg_tow_eve with Dissolve(1)

scene bg_par11_kt_eve
with stripe_l_long

play music tower_stairs_down_p_ali
play sound se_0384
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_3")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……うん。\n
これは一人では行き着かなかった……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（……絶対に、途中で脱落していたわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイに連れて行かれたのは、延々と続く階段登りの旅だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し先を登っていたグレイがようやく立ち止まるのを見て、こっそりとバレないように息を整える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ階段を登るだけとはいえ、いったい何階分だったのだろう。\n
最初は数えていたものの、途中からはそれすら諦めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ついでに白状するならば、最初は弾んでいた会話は、五階を過ぎたあたりから途切れがちになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……体力、ないなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通、魔法使いは体力に欠けるが、グレイはぴんぴんしている。\n
途中、何度も私を気遣ってくれる余裕すらあった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大人の男性の体力と、小娘に過ぎない私の体力を比べるのも馬鹿らしい。\n
だが、一緒にいると見栄を張ってしまう。"


scene bg_par10_ku_eve with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞かれる度に大丈夫だと意地を張ってきたが、そろそろ体力的にも限界が近かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここがゴールだというのなら、ありがたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……？）"

play sound se_0451
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が顔を上げると、グレイが懐から鍵の束を取り出しているところだった。\n
その中から慣れたように一つを選ぶと、彼は階段の果てにある扉を開ける。"

play sound se_0277
pause .5
play sound se_0276
pause 1
play sound se_0693 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さあっと、風が吹き込んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "火照った身体に、涼しい風が心地いい。"


show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0096
Gray "「さあ、こっちだ。\n
……後少しだから、頑張れるだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（う……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるで子供にするような問いかけに、すでに赤いであろう頬がますます赤くなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（……バレバレ、よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "みっともなく、ぜいぜいはあはあと息を乱すことはしていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意地を張っていたが、途中から明らかに口数が減ったし、後半はずっと無言だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばれていないほうがおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キツくなっているのをグレイは分かっていて、そこで「やめようか」などと言えば私が反発することも分かっていたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（大人だなあ。\n
……私が子供なだけ、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "導かれるままにその扉の向こうへと足を踏み出した。"

play sound se_0383
hide gre_m_01_3

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"


scene bg06_sk_h_eve
with dis


play music evening_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「……わあ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自然と歓声が口をついて出た。\n
日暮れが近いこともあり、鮮やかな朱色に染まる世界が目の前に広がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "空が驚くほどに近い。"

play sound se_0693
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "高台だからか、風が普段感じるよりも強いようだった。\n
ずいぶんと遠くまで見渡すことができる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_2")
T "「ここ、塔の頂上なのね。\n
風が気持ちいいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "強い風に髪がぐしゃぐしゃと乱されるが、それが気にならないほどに気持ちがいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "爽快感と、開放感に、ここまで階段を登ってきた疲れが一気に吹っ飛んでしまった。"


scene bg_par14_ts_eve
with dis

show gre_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0097
Gray "「喜んでもらえてよかった。\n
ほら、君のココアだ」"

play sound se_0471
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイが茶色い紙袋から取り出したのは、紙コップに入ったココアとコーヒーだ。\n
コーヒーは彼ので、ココアが私のものになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法ではない。\n
途中で寄ったカフェテリアで呼び出して、持ってきたものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の管理を行うくらいだから、彼はひとかどの魔法使いのはず。\n
それでも、グレイにはあえて面倒を好むようなところがあるようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんでも魔法ですませてしまわない。\n
魔法学校にあって、そういうところは新鮮に映った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「テイクアウトなんて、出来たのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "茶色い紙袋の中に、紙のカップが並んで二つ。\n
丁寧に、お手拭用のナプキンまでセットになっている。"

hide gre_m_03_4
show gre_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0098
Gray "「カフェテリアや食堂にかかっているのは思い浮かべたものが形になる魔法……、だからな」"

hide gre_m_02_10
show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0098_5
Gray "「だが、テイクアウト仕様にするのは結構難しいんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「そうよね……。\n
皆がテイクアウトして、あちこちで食べ始めたら、掃除も大変そうだし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紙コップの蓋を外して、まだ温かいココアへと口をつける。\n
程よい甘さが身体に染み込んでくるようだ。"

hide gre_m_02_2
show gre_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと隣を見ていると、グレイは無意識なのか、コーヒーのカップを持つのとは逆の手がポケットを探っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かを取り出そうとして、私の視線に気付いてはっとしたようだった。\n
結局何も取り出すことなく、ポケットを探っていた手を戻す。"

hide gre_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に遠慮しているのだろうか。\n
今の一連の動作はまさしくそんな感じだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かをしかけて、躊躇って止めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（何だろう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風に吹かれ、夕焼けを眺めながら考える。\n
細い煙のように細くなった雲が夕日にかかるのを眺めているうちに、ふと閃いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（煙草？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の周囲には煙草を嗜む人がいなかったため、ピンとくるまでに時間がかかってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう一度ちらりと見やった先、グレイはコーヒーをちびちびと啜りながら、時折その紙コップの端を齧っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……口寂しいのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よく、煙草を辞めようとする人が口寂しさから飴やガムに走るという話を聞く。\n
それと似たような代理行為に見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらくは無意識の仕草だ。\n
かし、と紙コップの端を噛む姿は、大人なのに可愛らしくも感じられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同時に、非喫煙者を気にするその姿勢にも好感を抱いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（ますます……、真面目な人）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「もしかして、なんだけど……。\n
煙草、我慢していない？」"


show gre_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0099
Gray "「え？\n
いや、そんなことは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり無意識だったらしい。\n
無言で、紙コップの端へと視線をやる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の視線に誘導されて、己の手に持つ紙コップを見た彼がぎょっとしたような顔をした。"

hide gre_m_03_1
show gre_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0100
Gray "「あ、すまない、気を遣わせてしまったな。\n
だが大丈夫だ」"

hide gre_m_03_2
show gre_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0101
Gray "「いつもここで吸っているものだから、癖になっているんだ。\n
ここに来ると吸いたくなる、条件反射のようなもので……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言い訳のように、普段から我慢がきかないわけではなく、この場所が特別なんだとグレイが主張する。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……つまり、吸いたいんじゃない）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ええ、だから遠慮しないでほしいなと思って。\n
あなたは、いつもここで煙草を吸うんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「いつもどおりにしてもらったほうが、私も楽よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Gray "「…………」"


play music flower_eve_p_wam
show m_gre1_1 onlayer master
hide gre_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイはそれでも迷うようにした後、私の気が変わらないのを見てとると、胸ポケットから煙草の箱を取り出した。"

play sound se_0270 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "トンとその指先が箱の底を叩くと、ぴょこんと煙草が口より飛び出してくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……器用ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice gra_g0102
Gray "「普通だよ。\n
……ああ、もしかして君の周りには喫煙者がいなかったのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ええ、父も吸わないものだから」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_g0103
Gray "「そんな君の前で煙草を吸うだなんて、余計に気が引けるな。\n
……少しでも不快に感じたなら、言ってくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すいと彼は一度視線を空に向け、風向きを確認する。\n
吐き出した煙が私のところへと流れないように、との心遣いだろう。"

play sound se_0350
hide m_gre1_1
show m_gre1_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これだけ気配りをされると、喫煙されても、不快ではない。\n
煙草を咥え、ライターを使って火を灯す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔を傾け、目を伏せがちに細める顔。\n
煙草というアイテムもあって、ますます大人に見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際、彼は大人の男だ。\n
ものすごい年齢差でもないのかもしれないが、学生である私から見ると、別世界の人のようにも感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "煙草を吸う彼は、屋上の風景とあいまって、とても絵になっていた。"

hide m_gre1_2
show m_gre1_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0104
Gray "「ふう……。\n
……はは、そんなに珍しいのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……あ。\n
じろじろ見すぎちゃった？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ええ、珍しいわ。\n
とても新鮮」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "吐き出された紫煙は、風に吹かれてすぐに見えなくなる。\n
それでも、微かに煙の匂いが空気に混じった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0105
Gray "「ないと思うが……。\n
好奇心から、煙草に手を出そうなどとは思わないように」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「あなた、自分は吸うのに私は止めるの？\n
今のところ喫煙を始めるつもりはないけれど……、それはずるくない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gra_g0106
Gray "「自分が吸うからこそ、言うんだ。\n
体にいいものではないし、吸い始めるとやめるのは難しい」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gra_g0107
Gray "「間違いは少ないに越したことはない。\n
若い君が、同じような過ちを繰り返してしまわないようにと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「…………。\n
……それ、すごく年上のセリフみたいだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（年上どころか、むしろ年寄り……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの年齢が幾つかは知らないが、そんなにいうほど年上というわけではないと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法使いの中には外見年齢が当てにならないといわれる者もいるらしいが……、彼は不老の魔法などかけていないはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0108
Gray "「すごくかどうかは置いておくとして、年長者の忠告だ。\n
煙草を吸うなんて、やめたほうがいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「吸う気はないわ。\n
でも……、人が吸う姿を見るのは好きかもしれない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "煙草を口に咥え、火をつけて最初の一息を吐くまでの姿に目を奪われた。\n
今だって、手にした携帯灰皿に灰を落とす仕草が綺麗だと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "吸い口の部分を親指で弾き、器用に灰を落とすのだ。\n
これまで周囲に喫煙者がいなかったからこそ、こんなにも目を奪われるのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それとも……、相手が彼だからだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ありがちだが、年上の人への憧れや、未知のもののように思う新鮮さ。\n
そういったものが芽生えたのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0109
Gray "「いいものじゃないぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……うん、自分が吸うのはね。\n
でも、人のだと……、いいものに見えるときがあるみたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その後、夕日が落ちるまでの時間を彼と共に過ごした。"

with dis
$ hi_mes()
hide m_gre1_3


scene bg_par15_rg_tow_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_medium

scene bg06_sk_h_eve
with stripe_l_medium

scene bg06_sk_h_nig
with dis
##endmemory
$ routechara = "Gray"
jump gakuen_friend_check_tower
