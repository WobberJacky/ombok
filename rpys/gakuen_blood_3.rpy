label gakuen_blood3:
scene bg_map_nig
with dis
$ clockanim()

jump gakuen_storm_hatter
label gakuen_blood3_2:


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの三人は一体何をしているのか。\n
本来監督していなければいけないはずのブラッドは、どこにいるというのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんにしても、騒ぎは騒ぎ。\n
知り合いが危険なめにあっている。"


scene bg25_rr_nig
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（止めなきゃ……！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、止めるかどうかを見極めるためにも、とりあえず呼びかけなくては。\n
私は窓を開いて、声を張り上げようとする。"

play sound se_0051
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っむぐ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、そこをいきなり背後から口を塞がれた。\n
窓へとかけようとしていた腕の手首を取られる。"

play sound se_0103
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま背後へと引き寄せられて、どん、と背後に立つ人物の懐へとぶつかった。\n
……はずなのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手を確かめようと身をよじっても、そこに人の姿はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_10")
T "（姿隠しの魔法……！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外から聞こえる喧騒とあわせて、何が起こっているのかと全身から血の気が引く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法を使おうにも、こうして利き手と口を塞がれてしまっていては抵抗のしようがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はパニックになりかけていた。"

menu:
    "それでも暴れる。":
        jump gakuen_blood3_3a
    "様子を窺う。":
        jump gakuen_blood3_3b
label gakuen_blood3_3a:
pause .3
play sound se_0007
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おとなしくされるがままになるわけもなく、私は必死で体をよじる。\n
どうにかして、せめて口を塞ぐ手から逃れなければ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（魔法さえ使えたら……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "腕力では勝てない相手にも、魔法でならば抵抗することが出来る。\n
懸命に頭を振り、その手から逃れようとするものの、相手もそれを許しはしない。"

play sound se_0397

scene bg24_rj_nig
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま半ば抱えられるようにして、自室へと引きずり込まれてしまった。\n
先ほど開錠してしまっていたのがまずかった。"

play sound se_0399
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風呂に向かったときのままに、自室は暗い。\n
姿は見えずとも、背中に感じる他人の体温。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳元に吐息を感じて、ぞわりとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0166
Hatena "「……ふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（え）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice blo_g0167
Hatena "「……気付いてくれないとはつれないな、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……ブラッド？）"


play music blood_t_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き慣れた低い声音が、すぐ耳元でする。\n
私を背後から抱きこむようにして捕らえているのは、どうやらブラッド＝デュプレであるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が叫び出したりするのを警戒してか、ブラッドはしばらく私の口を塞いだままだったが、やがてもう大丈夫と判断したのかその手を離してくれた。"

jump gakuen_blood3_4
label gakuen_blood3_3b:
$ lovechara_blood_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（……冷静に、冷静に）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "がむしゃらに暴れるよりも、まずは状況を把握しようと呼吸を整える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここで暴れて、いざチャンスが訪れたときに充分な声を出せなくては元も子もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、そこで気付いた。"

play sound se_0785 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……紅茶の匂い？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "覚えのある匂いだ。"

play sound se_0397

scene bg24_rj_nig
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の抵抗が一瞬弱まった隙に、半ば抱えられるようにして自室へと引きずり込まれてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほど開錠してしまっていたのがまずかった。"

play sound se_0399
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風呂に向かったときのままに、自室は暗い。\n
姿は見えずとも、背中に感じる他人の体温。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳元に吐息を感じて、ぞわりとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0168
Hatena "「……襲われて抵抗しないとは。\n
君は奇特な女性だな、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……やっぱり）"


play music blood_t_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き慣れた低い声音が、すぐ耳元でする。\n
私を背後から抱きこむようにして捕らえているのは、ブラッドだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が叫び出したりするのを警戒してか、ブラッドはしばらく私の口を塞いだままだったが、やがてもう大丈夫と判断したのかその手を離してくれた。"

jump gakuen_blood3_4
label gakuen_blood3_4:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "「{size=+20}変質しゃ{/size}……むぐっ！！」"

play sound se_0051
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
Blood "「！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不意打ちで叫んでやろうとしたら、慌てたように再び口を塞がれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0169
Blood "「……お嬢さん、今のはもしかしなくとも嫌がらせか？\n
正体は分かっているだろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_9")
T "（分かっているからこそ、よ）"

play sound se_0116
$ flash(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返事の代わりに、がぶっと今度こそその手に噛みついてやった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「～～～っっ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後から声にならない呻き声が聞こえたような気がした。"

play sound se_0741

show m_bra3_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふ、っと魔法が解けて、ブラッドが姿を現す。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0170
Blood "「……お嬢さん、私だ。\n
噛み付くのはやめてくれないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_11")
T "「わひゃっへひへやっへひふほほ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_9")
T "（分かっていて、やっているのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_9")
voice blo_g0171
Blood "「何を言っているのか、分からない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（そりゃそうね）"

hide m_bra3_1
show m_bra3_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、噛みついていた口を開いてやる。\n
とたんブラッドは再び噛み付かれるのを警戒するように、さっとその手を引いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0172
Blood "「……声で分かってくれると思っていたんだが。\n
分かっていなかったのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブツブツと背後でぼやく声が聞こえるものの、聞こえないふりをしてやる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（って、それよりも……！）"

hide m_bra3_2
show m_bra3_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「ブラッド、これは一体なんの騒ぎな\n
の！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "右手首を捕らえていた手が緩んだのをいいことに、くるりと向きをかえてブラッドへと詰め寄る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドア一枚隔てた廊下側からは、未だに喧騒が響いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0173
Blood "「これはストームだよ、お嬢さん。\n
ストームと呼ばれる、シンフォニアの行事の一つだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「行事……！？\n
生徒と使用人達が戦うのが、行事なの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice blo_g0174
Blood "「そう。\n
伝統行事だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……男子生徒と使用人が夜の庭で乱闘もどきを繰り広げるのが？\n
それ、どんな伝統なのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice blo_g0175
Blood "「厳密に言うと、使用人との戦闘は付属物にすぎないはずなんだが……。\n
双子達や、一部の学生にとってはそちらがメインだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（それで、今回は勝つ、なんて言っていたのね……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「じゃあ、何のためのイベントなのよ！？」"

play sound se_0551
hide m_bra3_3
show m_bra3_4 onlayer master
with dis

play music high_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice blo_g0176
Blood "「ふむ……。\n
一番端的に表す言葉は……、肝試し、だろうな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを言いながら、ブラッドはひょいと私の腰へと腕を回した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドに詰め寄るような態勢だったせいか、そうして腰に腕をまわされてしまうと、まるで抱き合うような姿勢になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "改めてその距離の近さに気付かされ、動揺した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！！」"

play sound se_0373
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どん、とブラッドの胸に腕をついて、突っ張ろうとするもののびくともしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手が見知らぬ人ではなかった、というだけ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "未だ部屋に連れ込まれてしまったという状態に変わりはないことに、今更考えが至る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（これって……、まずくない？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深く考えなくともまずい。\n
年頃の男女が、夜中に二人きり……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「ブラッド……っ！\n
悪ふざけはよしてちょうだい！」"

hide m_bra3_4
show m_bra3_5and3_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_9")
voice blo_g0177
Blood "「悪ふざけとは酷いな、[firstname]。\n
君に逢いたくて、こうして忍んできたというのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前で呼ばれて、ぞくりとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先刻、息が当たったのとは違う感覚。\n
今は相手が分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段気だるげに、お嬢さん、としか呼ばれないせいか、ブラッドの声で名前を呼ばれるのが新鮮だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その声まで、似ている、と思ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（そんなわけがないのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は私の「先生」で、明るい日差しのよく似合う優しい人だった。\n
尊敬できる、大人の男性。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もっと安定感があって……、こんなに無意味に色気過剰ではなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（そう、違う人よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（まったくの別人）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は……、まったくの別人である彼に、どきどきとしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0178
Blood "「君に熱心に見つめられるのは悪くないが……。\n
心ここにあらずといったふうに見えるのはどうしてだろうな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことはないと軽く否定してしまえばよかったのに、その言葉に反応して顔を上げてしまった。\n
視線が至近距離で重なる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "動揺を、見抜かれてしまう距離だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0179
Blood "「君は……、私を挑発しているのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "{size=+20}「してないわよ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「…………。\n
でも……、ごめんなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線の圧に負けるようにして、白状した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「あなたって、知っている人に、似ている気がするの。\n
雰囲気っていうか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice blo_g0180
Blood "「ああ、それでだったのか。\n
ようやく納得がいった」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0181
Blood "「君は以前にもお茶会の折に、私を見つめてぼんやりとしていたことがあっただろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0181_5
Blood "「私に気があるのかと、期待して損をしたな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（勘違いさせた？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰かに重ねて見られることの、苦しさや疎ましさを私は知っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知っていて、それをブラッドにしてしまうなんてよくない。\n
意味合いは違えど、失礼なことだ。"

hide m_bra3_5and3_8
show m_bra3_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0182
Blood "「まあ、いいさ。\n
謝ることはないよ、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0183
Blood "「君が……、私しか見えないようにしてしまえばいいのだから、な。\n
幸いにして、その方法には事欠かない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その言葉が何を意味しているのか気付くより先に、彼の顔が近くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさしく有言実行で、彼しか見えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_10")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "綺麗な顔立ちだ。\n
ならず者というよりも貴族的な……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_11")
T "（……綺麗な顔）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その顔が視界いっぱいに近付いてきた、と思ったら、唇に柔らかなぬくもりが触れた。"

hide m_bra3_6
show m_bra3_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「～～～っ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キスされているのだと気付いたのが、遅すぎた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なにしろ、私は経験が浅い。\n
というか、ないに等しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いきなり異性にキスされるだなんて……。\n
気付いたときには既に深くを奪われて、息があがる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "挨拶や、親愛の情などではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるで、違う。\n
今までの経験にない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このキスは、男女のするものだ。\n
特別な関係の……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（私達、そんな関係じゃないのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_3")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_4")
T "「……っは」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達は特別な関係ではない。\n
ブラッドは、特別でなくとも出来るのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（こんな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「ん……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice blo_g0184
Blood "「……ふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ、つ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "息が苦しくて、閉じた視界の眼裏が赤く染まる。"

hide m_bra3_7
show m_bra3_5and3_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ようやく唇を解放されたときには、情けないことに、こんなことをした張本人であるブラッドの腕に支えられるという有様だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0185
Blood "「……慣れていないのか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "「～～～っっ！！！！\n
馬鹿！大馬鹿者！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_7")
T "（いきなり人の唇を奪っておいて、何を言いやがる……、いや、おっしゃるのか）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_7")
voice blo_g0186
Blood "「……大馬鹿者？\n
ふむ？試してみるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「誰がっ、何をよ！この……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（あ……、駄目。\n
口が悪くなる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早くも、寮風に染まっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下品なことを言ってはいけない。\n
姉も悲しむだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（……淑女は黙って、行動あるのみ、よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice blo_g0187
Blood "「……お嬢さん？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_9")
T "「…………」"

play sound se_0446
camera at hpunch
camera at vpunch
hide m_bra3_5and3_8
show m_bra3_9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "力いっぱい、全体重をかけて、ブラッドの足を踏みつけてやった。\n
風呂帰りということもあって、すでに室内履きに履き替えていたのが悔やまれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "１０センチピンヒールは無理でも、せめて硬い土足で踏んでやりたかった。"

play sound se_0596
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0188
Blood "「～～～っい！！」"

hide m_bra3_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでもそれなりの威力はあったのか、私を抱き捕らえていたブラッドの腕が緩んだ。\n
ささっと、速やかに距離を取る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "動揺を見抜かれるのが悔しくて、肩で息をしながらも、あくまで平然としているふうを装う。\n
息を整え、なるべく冷静な声を心掛けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が慌てるのを見て、楽しんでいるに違いないのだ、この男は。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（落ち着け……、落ち着くのよ、私……\n
！！）"


play music room2_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「で？\n
何しにきたのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……変質的行為に及ぶために、こんな騒動起こしたわけじゃないんでしょう？」"


show bra_m_03_19 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひくり、と少しだけブラッドは眉根を寄せた。\n
私が取り乱していないことが、面白くないからか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……充分、取り乱しているわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "内心では、とてもとても。"

hide bra_m_03_19
show bra_m_02_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0189
Blood "「人を変質者みたいに言うのはやめてくれないか。\n
これは、れっきとした伝統行事なんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「{size=+20}こんな変質者みたいなのが？{/size}\n
そんな伝統さっさとやめるべきよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアは名門校ではなかったのか。\n
こんなふうな行事が横行しているとは、とても名門とは言い難い。"

hide bra_m_02_18
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0190
Blood "「はは、そう言うな。\n
皆、楽しんでいる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「どこの世界に、夜這いを楽しむ伝統行事があるっていうのよ！」"

hide bra_m_02_8
show bra_m_03_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
Blood "「…………」"

hide bra_m_03_16
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice blo_g0191
Blood "「いや、夜這いは違う。\n
そちらは{size=+20}私の個人的な趣味{/size}だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "{size=+20}「なお悪いわ」{/size} "

hide bra_m_03_10
show bra_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_13")
voice blo_g0192
Blood "「……こほん。\n
それはまあともかくとしてだな、これはストームという伝統行事なんだ」"

play sound se_0422
play sound se_0312 volume .7
pause .6
play sound se_0311
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これ、といってブラッドがドアの外を示すように、視線をちらりと投げかける。\n
外は相変わらず賑やかだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それどころか、庭での騒ぎが廊下に移っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「ストームっていうのは何なの？」"

hide bra_m_01_11
show bra_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice blo_g0193
Blood "「男子寮の人間が女子寮へと襲撃する。\n
迎撃する使用人たちの防衛を潜り抜け、女子寮に潜入し……、親睦を深めるというわけだ」"

hide bra_m_01_2
show bra_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice blo_g0194
Blood "「そして、侵入できた証拠に戦利品を失敬して帰るという、くだらないほど健全なイベントで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "{size=+20}「強盗イベント？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の奥底から、つっこんでしまった。\n
ついでに、何が起こっているのかと緊張していた身体からも力が抜けて、くたくたとへたり込んでしまいそうになった。"

hide bra_m_03_13
show bra_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0195
Blood "「強盗とは酷いな。\n
学生らしい、寮のお遊びだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……なるほど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうりで朝から皆、そわそわとしていたわけだ。"

hide bra_m_03_12
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0196
Blood "「使用人のガードさえ抜けてしまえば、堂々と女子寮に忍び込めるチャンスだからな。\n
熱も入るというものだ」"

hide bra_m_03_4
show bra_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0197
Blood "「双子などは、忍び込むより使用人を打ち負かすほうに熱中しているが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……あなたは？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子寮に侵入できるぜ、ひゃっほーい、と、はしゃぐようなタイプには見えない。\n
むしろ、そんなブラッドは怖くて想像できない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……したくもない）"

hide bra_m_03_5
show bra_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice blo_g0198
Blood "「私は……、別に困ってはいないからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「何によ」"

hide bra_m_01_4
show bra_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_16")
voice blo_g0199
Blood "「さあ。何に、だろうな。\n
だが……、臆病風に吹かれていると馬鹿にされるのは面白くない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふふっと意味ありげに笑って、ブラッドが誤魔化す。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「臆病風？」"

play sound se_0776
hide bra_m_01_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は楽しそうに口元を笑みに歪めながら、部屋に備え付けの小さな書架の前へと移動した。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見繕うように、並んだ本の背表紙をつうっと指先でなぞる。"


show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0200
Blood "「言っただろう？肝試しだ、と。\n
ストームの最大の目的は……、戦利品だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょい、と書架から本を一冊引き抜いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（そんな本、持っていたっけ……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の部屋には不似合いな、可愛らしい装丁の本だ。\n
詩集か何かだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分で自宅から持ち込んだものであるはずなのに、いまいち記憶に残っていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自宅の本棚にあった本を、魔法を使ってそっくりそのまま移動させただけなので、そのせいかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「戦利品って……」"

hide bra_m_03_10
show bra_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice blo_g0201
Blood "「使用人達の妨害を潜り抜け、無事に麗しの姫君達と密会できた証として……。\n
訪れた先より私物を失敬してくるのが、これまた伝統だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "{size=+20}「とことんタチが悪いわね」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（やっぱり、強盗イベントで間違っていないじゃない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "押しかけて、乗り込んで、私物をくすねて去っていくなんて、強盗そのものだ。\n
そして、ブラッドは、その本を戦利品と定めたらしい。"

hide bra_m_02_4
show bra_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0202
Blood "「まあ、安心してくれ。\n
そのうち、ブリーズという別の伝統行事がある」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（何が、安心しろって？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……聞く前から、嫌な予感がするんだけれど」"

hide bra_m_02_5
show bra_m_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice blo_g0203
Blood "「ストームの逆で、今度は君達が奪われた戦利品を奪い返すために男子寮に侵入するという……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「謹んで、その本をあなたに献上することにするわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何が悲しくて、私までもがそんな強盗めいた真似をしなくてはいけないというのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子寮を襲撃するつもりなんて、欠片もない。"

play sound se_0717
pause .4
play sound se_0717
hide bra_m_02_15
show bra_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0204
Blood "「まったく、君はつれないな。\n
……ん？」"

play sound se_0717
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱらぱらと本のページを繰ったブラッドが訝しげな顔をした。\n
それから、にんまりとその口角を持ち上げて、意地の悪い笑みを浮べる。"

hide bra_m_03_13
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0205
Blood "「君は……、きっと来ることになる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「何よ、予知のつもり？」"

hide bra_m_03_10
show bra_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice blo_g0206
Blood "「魔法など使わなくとも分かるさ。\n
これは、君の大事なものだろう？」"

play sound se_0719
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_15")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（大事なもの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "所有していることすら忘れていたような本が？ "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのままブラッドにあげてしまっても構わない、と思っている。\n
本は読んでこそ価値があり、その対象でないのなら所有者を変えたほうがいい。"

hide bra_m_01_2
show bra_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0207
Blood "「本当に、構わないのか？」"

play sound se_0776
hide bra_m_01_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確かめるように言いながら、ブラッドはゆっくりと歩みを再開して窓へと向かう。"

play sound se_0586
pause 1
play sound se_0627 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが開けた窓の外からは、何かの合図のように笛が鳴るのが聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「？\n
何？」"


show bra_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice blo_g0208
Blood "「ああ、ストーム終了の合図だ。\n
男子生徒はこの合図で、自寮に戻らなければならない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あなたでも？」"

hide bra_m_01_13
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0209
Blood "「ああ、私でも。\n
……シンフォニアから追い出されたいわけではないからな」"

hide bra_m_03_15
show bra_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0210
Blood "「守らなくてはならないルールと、破っても構わないルールの見極めぐらいつくさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "破っても構わないルール、とは言い得て妙だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その辺のぎりぎりを綱渡りしながら、踏み越えそうで踏み越えない一線を楽しんでいるのがこの男なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、窓辺へと足をかける。"

play sound se_0693

show m_bra3_10 onlayer master
with dis
hide bra_m_03_1

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0211
Blood "「取り戻しに来なさい、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にやりと笑う口元、ちらりと手にした本の合間。\n
見えたのは、悪夢の中で見たのとよく似た封筒だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "{size=+20}（！！）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "{size=+20}（あ・れ・は）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "{size=+20}（！！！！！！！）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「ちょっと……っ！\n
待って！待ちなさい……！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_6")
voice blo_g0212
Blood "「女性に引き止められるとは、男冥利に尽きるね。\n
だが……」"

play sound se_0216
hide m_bra3_10
show bg06_sk_h_nig onlayer master
with dis
play sound se_0348
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "捕まえようと私が手を伸ばすのと同時に、とんっとブラッドが窓のヘリを蹴る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "指先に微かに布地の感触はあったものの、ぎりぎり捕まえることは出来なかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0213
Blood "「紳士的に、今夜はお暇しよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中庭の闇に溶けるように、ブラッドの姿が見えなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三階にある私の部屋の窓から飛び降りたとはいえ、心配するような気持ちは一切ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうせ魔法で着地したか……、箒なしでは難易度が上がるが、そのまま飛んで帰ったかのどちらかだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、ブラッドへの心配は１ミクロンだってしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が心配しているのは……。"

hide bg06_sk_h_nig

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ。\n
あ、アレって、アレよね……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰も答えようがないと分かっているのに、声に出して呟いてしまう。\n
どこにしまったのかも、どう処分したのかも忘れていた昔の恋形見。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（あああ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_9")
T "（{size=+20}昔の自分を絞め殺してやりたい{/size}……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうして、あんなところに挟んでおいたのか。\n
どうして、あんな可愛らしい本をいつまでも残していたのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれは、可愛らしく振る舞おうとしていた、過去の残骸だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手紙を処分するなり、本ごと処分するなりしていたならば、こんなことにはならなかったのに。"

menu:
    "なんとしてでも取り返す。":
        jump gakuen_blood3_5a
    "ポジティブに考えてみる。":
        jump gakuen_blood3_5b
label gakuen_blood3_5a:
$ lovechara_blood_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「……っ！\n
なんとしてでも取り返さなきゃ……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今すぐにでも、取り返しに行きたい。"

jump gakuen_blood3_6
label gakuen_blood3_5b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（発想の転換が大事、よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は今まで、あの手紙が現存していることを知らなかった。\n
つまり手元にあっても、ないのと同じ状態だったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今更それがブラッドの手に渡ろうと、今までと何が違うだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「おおいに違うわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分で自分につっこみを入れてしまった。\n
なるべく早く、出来れば今すぐにでも取り戻しに行きたい。"

jump gakuen_blood3_6
label gakuen_blood3_6:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それは出来ない相談だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男女の寮間は厳しく監視されており、行き来することなど出来ない。\n
それこそ……、こんなイベントでぐらいしか。"

play sound se_0696 volume .7

scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……ブリーズ、か」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やるしかない。\n
両手で拳を作り、男子寮がある方向を睨みつける。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「奪い返さないと」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "伝統行事だというが、これほどまでに切実に、目的に沿った女子生徒は今までいたのだろうか。"

with dis
$ hi_mes()

scene bg06_sk_h_nig
with stripe_l_medium

scene bg_par15_rg_hat_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_blood4
