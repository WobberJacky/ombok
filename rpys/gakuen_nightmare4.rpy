label gakuen_nightmare4:
scene bg_map_eve
with dis
$ clockanim()

jump gakuen_storm_tower1
label gakuen_nightmare4_2:
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

show bg25_rr_nig onlayer master ##instantPAY ATTENTION="true"]

scene bg24_rj_nig_lon ##instantPAY ATTENTION="true"]
pause .5
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ふう」"

play sound se_0451
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自室に戻って、鍵を開けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ストームかあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子が女子寮に侵入して親睦を深めるなんて、とんでもないイベントだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスやグレイといった風紀側・管理側の人間は、さぞやてんてこ舞いしていることだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初、このイベント概要を聞いて頭に思い浮かべたのは、ボリスやピアスといったクラスメイト達だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃からいろいろと一緒に馬鹿をしているからだろう。\n
だが、彼らは遊園地寮の住人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じ塔の住人で、そんな悪ふざけに誘ってくれそうな人間というと、なかなか難しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の住人は皆、比較的真面目でおとなしい傾向にあるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まあ、そうでもなければ元職員寮で、風紀委員長が寮長をしている塔など選ばないような気もする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（塔のストームって、どんな感じなのしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

play sound se_0285

show nai_m_01_2 at center ##instantPAY
hide bg25_rr_nig with stripe_l

$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことをつらつらと考えながら開けたドア。\n
目の前には……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じっと凝視する。"

hide nai_m_01_2
show nai_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じくこちらを見つめ返すのは、顔色の悪い学校医だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（…………）"

play sound se_0664
show bg25_rr_nig with Dissolve(.1)
hide nai_m_02_11
##[chara1 PAY ATTENTION="true"]

scene bg25_rr_nig ##instant]
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばたんっとドアを閉める。"


play music gag1_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……幻覚？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（幻覚、よね？\n
本物なわけがない……はず）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice nig_g0062
Nightmare "「……っ！？\n
こら、そのリアクションは傷つくぞ！？」"

play sound se_0429
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抗議するように内側からドアを叩かれる。\n
ドアを開こうとしているのが分かったので、反射的に外側からドアノブを引っ張ってそれを阻止する。"

play sound se_0274
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……何をしているんだろう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、自室のドアを外側から閉めようとしている。\n
間の抜けた状況。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも中から開けようとしているのはナイトメアだ。\n
訳が分からない。"

play sound se_0287
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0063
Nightmare "「く……っ、ぬ……！！\n
開かないぞ！？君、馬鹿力だな！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_9")
T "「む。\n
私が馬鹿力なんじゃなくて、あんたが非力すぎるのよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通、女の力では男に対抗できない。\n
私程度でもこうして充分すぎるほどに抵抗できるのは、相手がナイトメアだからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "非力で、病弱。\n
へなちょこな学校医。"

play sound se_0287
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0064
Nightmare "「むむむ、こ、こうなったら……っ！！\n
私の意地にかけて、って、ぬおおお！？」"

play sound se_0326
pause 1
play sound se_0293
play sound se_0701 volume .6
camera at hpunch
camera at vpunch
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

play sound se_0274
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんとなく状況を察して、急に抵抗のなくなったドアノブからぱっと手を離してみた。"

play sound se_0225
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごとりっと音をたててドアノブが落ちた。\n
強引に引っ張りすぎたせいで、壊れて引っこ抜けてしまったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そしてそれを引っ張っていた張本人であるナイトメアは、その勢いのままに尻餅をつき、それでも勢いを殺せず転がっていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアの向こうの光景ながら、容易に想像がつく。\n
ちょっと見たかった。"

play sound se_0496
hide bg25_rr_nig
show magic_g onlayer master with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

hide magic_g with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は呪文を唱えて、反対側の落ちているドアノブをこちら側へと引き寄せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "角度を調整しながら穴へとはめ込み、それを見届けてこちら側からも外れたドアノブを差し込む。"

play sound se_0049
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "強く引き寄せながら、がちゃがちゃと捻っているとどうやら中でうまいように噛み合ってくれたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……明日、使用人に見てもらわなきゃ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひねれば手ごたえは返ってくるが、微妙にドアノブが斜めになっているような気がする。おそるおそる回してみれば、ドアは普通に開いた。"

play sound se_0285

scene bg24_rj_nig_lon with stripe_l
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "再び外れても困るので、一応このまま固定する形で魔法をかけておく。\n
それから、室内にいるであろうナイトメアの姿を探した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は予想通り、床に転がっている。"


play music nightmare_t_ali
##[rchara1 PAY ATTENTION="true"]
show nai_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0065
Nightmare "「こ、腰が抜けたような気がするぞ！？\n
猛烈に痛い！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「…………。\n
……あなた、人の部屋で何やっているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは床に座り込んだまま涙目だ。\n
もしも本当に腰が抜けているようなら、グレイを呼ぶしかない。"

hide nai_m_03_3
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0066
Nightmare "「何って……、ほほう？\n
ふふ、まだ知らないのか？」"

hide nai_m_02_4
show nai_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0067
Nightmare "「ははは、そんな君に教えてあげようじゃないかっ！\n
今日はな、ストームという一大イベントの日なんだ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「知っているわよ。\n
男子生徒が女子生徒の部屋に侵入し、親睦を深めてその証拠品を持って帰るっていうイベントなんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほど教えてもらった情報を、要約して口にしたところ、ナイトメアは分かりやすくもガガーンとショックを受けた顔をしていた。"

hide nai_m_02_3
show nai_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0068
Nightmare "「そ、そう、ストーム……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_16")
T "（……分かりやすい男よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分が教えたかったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "子供のようだ。\n
自分の持っている情報を、他人に一番に教えたがる子供。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「でも、おかしいじゃない。\n
男子生徒が女子生徒の部屋に侵入するのが、ストームなんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「あなた、生徒じゃなくて学校医よ？」"

hide nai_m_02_9
show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
Nightmare "「…………」"

hide nai_m_02_10
show nai_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
Nightmare "「…………」"

hide nai_m_01_10

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは、のろのろと立ち上がろうと試みる。\n
腰のほうは相当強かにぶつけたのか、顔が引きつっている。"

show m_nai4_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも何とか立ち上がると、仁王立ちで私へと指をびしりと付きつけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（そのポージングのためだけに、痛いのを我慢しているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ますます子供じみている。\n
腰が痛いのならば、おとなしく座って安静にしていればいいものを。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0069
Nightmare "「私は、この塔の責任者だからな！\n
一番偉いんだ！偉いからには楽しいことに参加する権利がある！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「…………」"

hide m_nai4_1

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……あ、そう」"


show nai_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice nig_g0070
Nightmare "「ああ！また、そんな反応を！\n
傷つくんだぞ、そういう冷めたような反応！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……呆れているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "楽しそうという理由だけで、教職員が生徒のイベントに混じるなんて聞いたことがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（普通は、監視とか手伝いとか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……いや、うちの担任あたりは混じっていそうだけれど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脳裏を、陽気に音楽を奏でる担任ゴーランドの姿が駆け抜けていった。\n
人柄は陽気だが、音楽は陰気になる。"

hide nai_m_03_3
show nai_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0071
Nightmare "「いいじゃないか！\n
楽しいことを独り占めするのはよくないぞ！？」"

hide nai_m_02_1
show nai_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0072
Nightmare "「楽しいことは皆で分かち合おうじゃないか！\n
同じシンフォニアに住む、いや、この塔に住むもの同士なんだから！！」"

menu:
    "仕方ないわね。":
        jump gakuen_nightmare4_3a
    "……帰れ。" :
        jump gakuen_nightmare4_3b
label gakuen_nightmare4_3a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……仕方ないわね。\n
いいわよ、あなたとストームをしてあげるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……って、偉そうに言っているけど、あんまりよく知らないんだけど）"

hide nai_m_02_3
show nai_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice nig_g0073
Nightmare "「いいのか！？\n
ふふふ、ずっと前から参加したいと思っていたんだ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは心底嬉しそうだ。"

jump gakuen_nightmare4_4
label gakuen_nightmare4_3b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……{size=+20}帰れ{/size}」"

hide nai_m_01_6
show nai_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice nig_g0074
Nightmare "「嫌だ！！絶対に帰らないぞ！！\n
私はずっと前から、ストームに参加するのを夢見ていたんだ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正体不明の意気込みが滲む。\n
気合だけは充分だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（あんまりよく知らないんだけど……、ストームってこんなふうに臨むものな\n
の？？？）"

jump gakuen_nightmare4_4
label gakuen_nightmare4_4:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（この人も……、ストームの概要しか知らないのかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ナイトメア、今までストームに参加したことなかったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの学校医としてそれなりの年数勤めているであろう彼が、こんな賑やかなイベントに参加したことがなかったとは意外だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今のこのはしゃぎようからして、毎年恒例とばかりに参加してもおかしくない。"

hide nai_m_02_5
show nai_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0075
Nightmare "「……体調やら何やら、都合がつかないことが多かったんだよ。\n
楽しみにしすぎて、熱が出るんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「どれだけ子供なのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠足を楽しみにしすぎて熱を出す子供と同レベルだ。きっと、これまた子供と同レベルに参加したいと騒いで、グレイに迷惑をかけてきたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "想像するまでもなく、そんな光景が眼裏に浮かんだ。\n
本当に、分かり易すぎる人だ。"


play music stream_eve_p_wam
hide nai_m_01_4
show nai_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0076
Nightmare "「それに、今回はどうしても君のところに来たかったんだ。\n
……君は昨夜、うなされていただろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いきなりそのテンションを変えたナイトメアの言葉に、私は息を飲んでしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……っ、ずるいわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "子供みたいにストームに参加させろと騒いでいたかと思えば、こうしていきなり大人のような顔をする。"

play sound se_0327 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは、ぎしりとスプリングを軋ませてベッドへと腰掛けた。"

hide nai_m_01_13
show nai_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0077
Nightmare "「私は特別な魔法使いだからね。\n
私が傍にいれば、悪夢をみるようなことはない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……昨夜の悪夢を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かつての記憶。\n
渡せなかったラブレターと、先生と、託されてしまったラブレター。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、姉さん。"

hide nai_m_02_1
show nai_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0078
Nightmare "「ほら、またそんな顔をしている。\n
大丈夫だ、もう怖い夢は見ない」"

play sound se_0232
hide nai_m_02_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは無造作にベッドの上かけをめくると、するりとその中へともぐりこんだ。\n
そして、手招く。"


show m_nai4_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0079
Nightmare "「おいで？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言いたいことやらツッコミたいことが溢れて、どこから口にしていいのか分からなくなるほどだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれやこれや、色々。\n
とりあえず……、どつくことにした。"


play music gag2_a_ali
play sound se_0445
$ flash(.3)
hide m_nai4_2
show m_nai4_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0080
Nightmare "「{size=+20}ぎゃ……！！？{/size}\n
どうして殴るんだ……！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

play sound se_0499
camera at hpunch
camera at vpunch
pause .4
play sound se_0499
camera at hpunch
camera at vpunch
pause .2
play sound se_0499
pause .6
play sound se_0107
camera at hpunch
camera at vpunch
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私もベッドに乗り上げて、蹴りを連続して繰り出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0081
Nightmare "「ま、待てっ！？\n
なんで蹴るんだ……っ、うわ、落ちる……！！！？」"

play sound se_0553
hide m_nai4_3

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「あんたねえ……。\n
普通、女の子のベッドに勝手に入る！？」"


show nai_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
voice nig_g0082
Nightmare "「だから紳士的に私から先に入ったじゃないか！！\n
何が不満なんだ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_9")
T "「そんな紳士的な順番があるなんて、知らなかったわよ！！\n
普通、世間一般では、教師は生徒のベッドに潜り込まないものよ！？」"

hide nai_m_03_9
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_9")
voice nig_g0083
Nightmare "「私は教師ではなく、学校医だ！\n
生徒の健康を守るのが最優先される！！」"

hide nai_m_02_4
show nai_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_9")
voice nig_g0084
Nightmare "「だから、いいんだ！\n
君を悪い夢から守るためだからな！！」"


play music flower_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……それよ」"

hide nai_m_02_3
show nai_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice nig_g0085
Nightmare "「どれだ？\n
……やれやれ、君は手癖やら足癖やら悪すぎるぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぶつぶつと文句を呟きながら、懲りないナイトメアがベッドの上に上がってきた。\n
私ばかり意識するのも、なんだか馬鹿のように思えてきてしまう。"


show m_nai4_4and4_6and4_9 onlayer master
with dis
hide nai_m_02_11

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……あんたは男で、私が女だってこと分かっているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それとも、私が子供にしか見えていないからこそこんなことが平気で出来るのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（ナイトメアのほうこそ、子供みたいな言動ばかりのくせに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……どうして、あなた、私が昨夜うなされたって知っているのよ。\n
目の下に隈なんて、出来ていなかったと思うんだけれど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは、どうして私の夢見が悪かったことを知っているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はその夢のことを誰にも言ったりはしていない。\n
そもそも、言えるような内容の夢ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（そういえば……、夢の最後……。\n
ナイトメアの声が聞こえた、ような……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、あれも夢だ。\n
まさか、ナイトメアが私の部屋に忍び込んで声を発したなんてことはないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（全部、夢……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢は深層心理。\n
悪夢から救う声が、ナイトメアのものだったことの意味を深くは考えたくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれから、嫌が上でも意識してしまう。\n
しかし、彼は拍子抜けしたような声をあげた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0086
Nightmare "「なんだ、君、覚えていないのか？\n
昨夜、夢の中で会っただろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice nig_g0087
Nightmare "「夢の中で。\n
ああ、姿は現さなかったが、声で分かると思ったんだが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice nig_g0088
Nightmare "「覚えているだろう？\n
忘れてはいないはずだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「あれ……、本当にあなただったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（あれは、夢じゃなかった……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……え？\n
どこからが？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（昨日の声も現実……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢ではないということは、やはり、寝ているときにナイトメアが近くにいたということだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは空間移動の魔法を得意としている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "媒体や呪文すら必要とせずに、するりするりと空間移動の魔法を発動させて移動しているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのあたりの事情を鑑みるに、今回のナイトメアの侵入経路はわざわざ特定するまでもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それと同じように、昨夜も枕元にでもいたのだろうか。\n
寝ている私を、ぬうっと見下ろすナイトメアの図……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……こ、怖い光景）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不気味だ。\n
怖すぎる。"

hide m_nai4_4and4_6and4_9
show m_nai4_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_9")
T "「……い、いくらうなされているからって、寝ている女子生徒の部屋に侵入するのはどうなのっ！？\n
訴えるわよ、この変質者！！」"

play sound se_0716
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_9")
voice nig_g0089
Nightmare "「へ、へへへ変質者！！？\n
そ、そんなことは……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_9")
T "「変質者じゃない！\n
夜中に忍び込むだなんて……、医師だとしてもやっていいことじゃないわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_9")
voice nig_g0090
Nightmare "「誤解だ……！！！\n
私は、君の身体には指一本触れていないぞ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「触れていたら、もっと問題よ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice nig_g0091
Nightmare "「誓って言うが、私が君の部屋に侵入を試みたのはこれが初めてだからな！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice nig_g0091_5
Nightmare "「私は紳士だ、女性の部屋に無断で侵入するなんて、イベントでもなければそうしない！！」"

hide m_nai4_5

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（イベントでも控えなさいよ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっかり呆れがちの視線を向けていたものの、どうやらナイトメアは嘘はついていないようだ。顔を真っ赤にして、変質者疑惑を否定している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……現在進行形で女子生徒のベッドに潜り込んでいることについては、綺麗に棚上げしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、これが初侵入だとすると、どういうことなのかが分からなくなってきた。\n
悪夢にうなされていた私を助けてくれたのはナイトメアだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、私も声を聞いているので、否定はしない。\n
だが、彼は私の部屋には訪れていないのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……？？？」"


show m_nai4_4and4_6and4_9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice nig_g0092
Nightmare "「ふふ、君に私のとっておきの秘密を教えてあげよう。\n
私はね、魔法使いというよりも、夢使いなんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ゆめ、つかい？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞いたことのない単語だ。\n
ナイトメアの作った造語だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0093
Nightmare "「私は、特異体質でね。\n
実は、限られた魔法しか使うことが出来ない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……え？\n
限られた、って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nig_g0094
Nightmare "「たとえば、灯りを生み出す魔法があるだろう？\n
難易度としては、せいぜい初級といったところだ」"

play sound se_0496
hide m_nai4_4and4_6and4_9
show m_nai4_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
Nightmare "「…………」"

play sound se_0741
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呪文は間違えていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ルーンビナスに住むものならば、子供でも使えるような簡単な初級魔法だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのにナイトメアの手のひらの上に生まれたのは、極々小さなホタルのような光だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0095
Nightmare "「ご覧の通りだ。\n
私は、皆が使えるような魔法がほとんど使えない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……あ。\n
そういえば……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前に、姿隠しの魔法を頼まれたことがあったはずだ。"

play sound se_0724
play sound se_0322 volume .4
hide m_nai4_7
show m_nai4_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひらりとナイトメアが手を揺らして促せば、小さな光がふわりと浮かんだ。\n
ぱちりぱちり、と時折終わりかけの線香花火のような音をたてている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それだけだ。\n
私や他の生徒達が使うような、光球とは違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「でもあなた……、空間移動なんていう難しい魔法は簡単にやってのけるわよね？\n
それは、使える限られた魔法ってこと？」"

hide m_nai4_8
show m_nai4_4and4_6and4_9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice nig_g0096
Nightmare "「そうだな……。\n
私に出来るのは、空を飛ぶこと、夢の世界に出入りすること、それと人の心を読むことぐらいだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "{size=+20}「！！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは、さらりととんでもないことを言った。彼が口にした魔法のうち、空を飛ぶ以外の二つは「大魔法」といってもいいようなものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何人もの偉大なる魔法使いが、様々な儀式の果てに見出した成果だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0097
Nightmare "「私がしてみせる空間移動も実はインチキなんだよ。\n
一度夢に入り込み、そこから別の場所に出ているだけにすぎない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「す、すぎない……、って！\n
それ、充分すぎるほどすごいことよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice nig_g0098
Nightmare "「まあ、その代わり、私は他の魔法のほとんどが苦手だ。\n
それに身体も弱い」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアはベッドに横になったまま、器用に肩を竦めて見せる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……特殊体質、突然変異ってやつなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の人間とは、明らかに性質が違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0099
Nightmare "「そうだろうな、おそらく。\n
私に子供が出来たとして、この能力が遺伝するかどうか……、そもそも子供を持つことが出来るのかも危うい」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "{size=+20}（！！！！）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今、私は心に浮かんだ疑問を声には出さなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あくまで心の中で思っただけだ。\n
ナイトメアは、それに答えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（本当に、心を読んでいるんだわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice nig_g0100
Nightmare "「ふふ、普段はなるべく読まないようにしているんだがね。\n
今は特別だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざと、能力を教えるために披露して見せたのだろう。\n
目の前にいる綺麗な男が、何か自分とは違う生き物のように見えてくる。"

menu:
    "（……怖い）":
        jump gakuen_nightmare4_5a
    "（迷惑な……）":
        jump gakuen_nightmare4_5b
label gakuen_nightmare4_5a:
hide m_nai4_4and4_6and4_9
show m_nai4_10a onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……怖い）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正直、恐怖を感じた。\n
あまりにもスペックが違いすぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分とは違う、異質の生き物。\n
そういう思いが強くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのとき、ナイトメアの顔に浮かんだ表情をなんと言えばいいのだろう。\n
諦念の滲んだような、それでいて何もかもを許すような、そんな顔だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼にそんな顔をさせてしまったという事実に胸が痛む。\n
きっとこれまでにも、同じような反応をされたことは多かったはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（慣れているんだわ）"

jump gakuen_nightmare4_6
label gakuen_nightmare4_5b:
$ lovechara_nightmare_points =+ 1
hide m_nai4_10a
show m_nai4_10b onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（迷惑な……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は半眼でナイトメアを見やった。\n
これまでにもちょこちょこ心を読んでいたなんて言われたら、大暴れしそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（……プライバシーの侵害よ。\n
やっぱり、変質者の類じゃない）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice nig_g0101
Nightmare "「な、なんだ君、どうしたんだ。\n
目が怖いぞ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「ふふ……。\n
本当に、普段は読んでいないのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice nig_g0102
Nightmare "「よ、読んでいないともっ！\n
もちろん、そんなズルのようなことを私がするわけないだろう！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっぱりと言い切るその態度や言い分は立派だが、何故その目は泳いでいるのだろう。\n
是非、詳しく追及したい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（是非是非に）"

jump gakuen_nightmare4_6
label gakuen_nightmare4_6:
hide m_nai4_10b


show nai_m_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice nig_g0103
Nightmare "「あ、ああ、そうだ！\n
そうそう、夢の話だ、夢の話だよ、[firstname]！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……夢？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアがわざとらしく話題を切り替えた。"

hide nai_m_03_7
show nai_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0104
Nightmare "「そんなわけで、夢を操ることの出来る私がいれば君は怖い夢を見る必要はない！\n
いい話だろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……別に、怖い夢というわけじゃないのよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言い訳のようにぼそりと言う。\n
嫌な夢ではあるし、うなされていたというのも事実だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれどそれは、私自身が原因だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉さんや、「先生」が悪いわけではない。\n
私の、鬱屈した感情がいけないのだ。"

hide nai_m_02_12
show nai_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0105
Nightmare "「だが……、君は苦しんでいた。\n
私にとっては、それだけで充分な悪夢だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっと伸びてきたナイトメアの手のひらが、私の額へと触れた。\n
不健康なイメージそのままに、ナイトメアの手はひやりと冷たかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風呂上りで体温が上昇していた身体には気持ちいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「それで、私を寝かしつけにきてくれたっていうの？\n
……まだ、眠くないわ」"

hide nai_m_02_7
show nai_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice nig_g0106
Nightmare "「ふふ、任せなさい。\n
私は、夢に関してなら無敵なんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……微妙に情けないわよ、それ」"


play music memory2_a_wam

show m_nai4_11 onlayer master
with dis
hide nai_m_02_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりと私の頬をなでおろした手が、瞼の上にのった。\n
導かれるままに、そっと後頭部を枕に沈める。"

play sound se_0138 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……っ、なに……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "瞼の裏で、淡い光が灯ったようなのを感じた。\n
そしてすぐに、強烈な眠気が波のように襲ってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜感じたのと同じ類の眠気だ。\n
あんまりにも強烈で、何もかもが分からなくなってしまいそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この睡魔に身をゆだねることが出来たのなら、どんなに気持ちいいだろうと思わせる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……逆らう理由はない。\n
強烈な睡魔を操るのはナイトメアだ。"

play sound se_0627 volume .2
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこかから、笛の音が聞こえたような気がした。\n
けれどそれを気にする余裕はもうない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "四肢はぐったりと重く、頭の中はとろとろのふわふわだ。\n
それでも、ぴくりと小さく瞼が震えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0107
Nightmare "「心配ない。\n
ストーム終了の合図だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "宥めるようにくしゃりと頭を撫でられる。\n
そのひやりとした感触に眠気が飛ばないかと思ったものの、そんな心配は必要なかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただただ、気持ちいい。"

hide m_nai4_11
show m_nai4_12 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0108
Nightmare "「おやすみ、[firstname]。\n
悪い夢は見ないよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0109
Nightmare "「怖い夢も……。\n
……あの男の夢も」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（……んん？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かひっかかることをナイトメアが言ったような気がする。\n
けれどもう、それを気にするだけの余力がない……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完全に意識が夢に沈んでしまう瞬間、唇に柔らかなぬくもりが触れたように感じた。"

hide m_nai4_12

with dis
$ hi_mes()

scene bg_par15_rg_tow_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_nightmare5
