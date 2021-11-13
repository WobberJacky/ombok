label gakuen_op3:
if gakuen_op3a_read_seen == True:
    if gakuen_op3b_read_seen == True:
        if gakuen_op3c_read_seen == True:
            if gakuen_op3d_read_seen == True:
                jump all_readed
if renpy.seen_label("gakuen_op3a_read") == True:
    if renpy.seen_label("gakuen_op3b_read") == True:
        if renpy.seen_label("gakuen_op3c_read") == True:
            if renpy.seen_label("gakuen_op3d_read") == True:
                jump all_readed
jump selecting
label selecting:
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "事務室に行って寮を決める前に、ちょっと情報収集しておこう。"
$ hi_mes()
menu:
    "Hear about the Red Rose Dormitory":
        jump gakuen_op3a
    "Hear about the Hatter Dormitory":
        jump gakuen_op3b
    "Hear about the Amusement Park Dormitory":
        jump gakuen_op3c
    "Hear about the Tower":
        jump gakuen_op3d
label all_readed:
jump gakuen_op3h
label gakuen_op3f:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「まだ、全部聞いてないわよね？\n
事務室に行って決める前に、きちんと情報収集しておかなきゃ」"

jump gakuen_op3
label gakuen_op3g:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「この寮についてはもう聞いたわね。\n
他に、まだ聞いていないところはあったかしら……」"

jump gakuen_op3
label gakuen_op3a:
if gakuen_op3a_read_seen == True:
    jump gakuen_op3g
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「赤薔薇寮というのは、どういうところなの？」"
$ gakuen_op3a_read_seen = True


show girl_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice mat_g0102
Seito "「そうね、赤薔薇寮はとても華やかな寮よ。\n
寮長は、自治会会長のビバルディ様よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（ビバルディ……、様？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「自治会……？\n
自治会って、生徒会とは違うの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞きなれない役職に、首を傾げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒会長というのはよく聞くが、自治会会長というのはよく分からない。\n
同じようなものだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（自治会……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "{size=+20}（町内会みたいなもの？）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、たぶん、違うのだろう。"

hide girl_a1_3
show girl_a1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0103
Seito "「ん～、生徒会と似たようなものだけど、組織としてのあり方が少し違うわね。\n
生徒会は、学校の監督の下にある組織でしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「そうね。\n
あくまで生徒代表として学校側の企画に参加する形……、よね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、ごく普通の、生徒のあり方だと思う。"

hide girl_a1_8
show girl_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0104
Seito "「そうそう、主体は学校側にあるわ。\n
自治会は、そこが違うのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（名前から推察するに……。\n
……町内会みたいだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「学校側から独立している、ってこと？」"

hide girl_a1_3
show girl_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice mat_g0105
Seito "「ええ。自治会の運営は、自治会役員によって行われているの。\n
学校側の指導や、指示は受けない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「それって、勝手にやっている生徒会みたいなの？」"

hide girl_a1_2
show girl_a1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice mat_g0106
Seito "「違うわよ。\n
もっと、本格的なの」"

hide girl_a1_8
show girl_a1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice mat_g0107
Seito "「変な集まりでもなければ、暴走しているわけでもないし……。\n
……いえ、たまにするけど」"

hide girl_a1_1
show girl_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice mat_g0108
Seito "「万が一学校側が生徒の意向を無視して勝手なことをやり始めたりなんかした場合には、自治会役員が私達の先頭に立って、学校側と争議することになるの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「へえ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "驚いた。\n
本当に、ずいぶんと本格的だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教師陣に任せっぱなしにするわけでなく、生徒自ら対等な立場で学校の運営に参加している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その方針が生徒達にとって不利益である、ということになれば、生徒代表として話し合いの席につくことになる……といった感じなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（自治会かあ……。\n
……名前は、町内会みたいだけど）"

hide girl_a1_3
show girl_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice mat_g0109
Seito "「赤薔薇寮は、その自治会の役員や、主だった自治会員が集まっている寮よ。\n
皆、とても華やかで、素敵な人たちなの」"

hide girl_a1_2
show girl_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice mat_g0110
Seito "「もし、あなたが自治会に興味があるようなら、赤薔薇寮を選ぶといいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「……ありがとう。\n
参考になったわ」"

hide girl_a1_2

jump gakuen_op3a_read
label gakuen_op3a_read:
jump gakuen_op3
label gakuen_op3b:
if gakuen_op3b_read_seen == True:
    jump gakuen_op3g
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「帽子屋寮というのは、どういうところなの？」"
$ gakuen_op3b_read_seen = True


show boy_a1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice oni_g0067
Seito "「帽子屋寮は、シンフォニアにある四つの寮の中で一番自由な寮だろうな。\n
……ああ、でも、ある意味一番厳しい寮なのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（自由だけど、厳しい？）"

hide boy_a1_8
show boy_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice oni_g0068
Seito "「う～ん。説明が難しいな。\n
簡単に言うと、帽子屋寮は不良が多いんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「不良……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……世界一の魔法学校にも、不良なんているものなのね」"

hide boy_a1_5
show boy_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice oni_g0069
Seito "「ははは、結構多いよ。\n
優秀だからって、人格者とは限らないだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「それはそうだろうけど……」"

hide boy_a1_2
show boy_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice oni_g0070
Seito "「でも、だからといって、落ちこぼればっかりが集まっているわけじゃないんだぜ？そもそも、シンフォニアにそこまで出来の悪いのはいない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（う……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳に痛い言葉だ。\n
私はこの学校に相応しいのだろうかという疑問が、再びわきあがる。"

hide boy_a1_3
show boy_a1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0071
Seito "「寮長のブラッド＝デュプレなんかは、成績が学校全体でも上位に食い込むぐらい優秀な魔法使いだ」"

hide boy_a1_8
show boy_a1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0071_5
Seito "「ただ……、こう他人に決められたルールに従うのが嫌い、という人でさ」"

hide boy_a1_1
show boy_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0072
Seito "「……むらっけがあるんだよな。\n
学業にも、やることにも、すべてにおいてさ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「そういう意味での、不良なわけね。\n
つまり、素行的な意味合いで」"

hide boy_a1_5
show boy_a1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice oni_g0073
Seito "「そういうこと。\n
そして、そういう人が寮長なのが、帽子屋寮」"

hide boy_a1_8
show boy_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice oni_g0074
Seito "「学校側の決めたルールからは、疎遠でいられる。\n
そういう意味じゃ、一番自由でいられる寮だな」"

hide boy_a1_3
show boy_a1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice oni_g0075
Seito "「その代わり、寮長の決めたルールは絶対だ。\n
それに反すると……、口にするのも恐ろしいことになる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「え。\n
ど、どんな……」"

hide boy_a1_9
show boy_a1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice oni_g0076
Seito "「人知れず、闇に葬られるとかなんとか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……冗談か、誇張よね？」"

hide boy_a1_9
show boy_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice oni_g0077
Seito "「いやあ、それが……、誇張とも言いにくくてさ。\n
……怖い下っ端もたくさん抱えているから」"

hide boy_a1_5
show boy_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice oni_g0078
Seito "「……意外と、信憑性高いんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「何よ、それ。\n
まるで{size=+20}マフィア{/size}じゃない……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "社会のルールはいともあっさりと破ってみせるくせに、仲間内のルールは大事にするなんて、まさにそんな感じだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……ん？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（これって……、猫とネズミ並みに、禁句だった？）"

play sound se_0449
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、帽子屋寮の住人だという男子生徒は、ポン、と手を打って納得する。"

hide boy_a1_5
show boy_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0079
Seito "「そうだな、それが一番しっくり来る。\n
帽子屋寮はマフィアの巣窟だな！」"

hide boy_a1_3
show boy_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0080
Seito "「もしも、あんたが自由を好むのなら、帽子屋寮にするといい。\n
退屈だけは絶対しない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「……ありがとう。\n
参考になったわ」"

hide boy_a1_2

jump gakuen_op3b_read
label gakuen_op3b_read:
jump gakuen_op3
label gakuen_op3c:
if gakuen_op3c_read_seen == True:
    jump gakuen_op3g
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「遊園地寮というのは、どういうところなの？」"
$ gakuen_op3c_read_seen = True
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前からして、コミカルなイメージだ。"


show girl_b1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0128
Seito "「そうね、とっても賑やかで楽しい寮よ。\n
ゴーランド先生を見ていると、想像つくでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……なんで、ゴーランドが？\n
学生寮でしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「寮監とか？」"

hide girl_b1_8
show girl_b1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice nos_g0129
Seito "「いいえ、職員や教員は、普通、塔に住んでいるものなんだけどね。\n
ゴーランド先生だけ、遊園地寮に住み着いちゃっているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え、それ、いいの？\n
学生寮なのに……」"

hide girl_b1_8
show girl_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice nos_g0130
Seito "「今のところ平気みたいね。\n
遊園地寮の寮長は、ボリスがやっているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え？\n
ボリスが？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別にボリスを馬鹿にするわけではないのだけれど、それでも驚いてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスと私は、同じクラス。\n
ということは実力は似たようなもの。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "というわけで、そのボリスが寮長なんていう力あるポストにいることが、意外だったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（いや、入学手段自体がすれすれな感じだし、同じ実力とも限らないんだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、そんなに上位のクラスではないはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアはもっと実力主義、である気がしていた。\n
役職付きになるには秀でた何かが必要ではないのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の疑問に、クラスメイトの女の子がくすくすと笑う。"

hide girl_b1_3
show girl_b1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0131
Seito "「名前だけの寮長だからいいのよ。\n
実際に寮の管理をしているのは、ゴーランド先生よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「アバウトね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それでいいのかもしれない。\n
ゴーランドのような教員がいる中で、それとは別に寮長として上に立つ人間がいては揉めそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それよりはいっそのこと、建前上の寮長と実質的な寮長と分けてしまったほうが、力関係が分かりやすい。\n
もちろん、それも気が合えばの話。"

hide girl_b1_8
show girl_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0132
Seito "「ゴーランド先生も、ボリスも、面白いものや楽しいことが大好きなの。\n
そのせいで、遊園地寮は他の寮よりいろいろと仕掛けが多いのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「仕掛け？\n
寮に、どんな仕掛けがあるの？」"

hide girl_b1_3
show girl_b1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nos_g0133
Seito "「踏むと、目的地まで運んでくれるタイルとか。\n
……まぁ、今は故障中だから、変なところに運ばれちゃうけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "{size=+20}「駄目じゃない」{/size} "

hide girl_b1_2
show girl_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice nos_g0134
Seito "「面白いからいいのよ。\n
賑やかなのが好きなら、遊園地寮はおすすめよ？」"

hide girl_b1_3
show girl_b1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice nos_g0135
Seito "「……ただし、安全かどうかは保証できないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……ありがとう。\n
参考になったわ」"

hide girl_b1_5

jump gakuen_op3c_read
label gakuen_op3c_read:
jump gakuen_op3
label gakuen_op3d:
if gakuen_op3d_read_seen == True:
    jump gakuen_op3g
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「塔というのは、どういうところなの？\n
ここだけ名前に寮、ってつかないのね」"
$ gakuen_op3d_read_seen = True

show boy_b1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice suz_g0103
Seito "「塔は、元々は天文台だったところを教職員用の寮に改造した場所なんだ。\n
だから、建築物としても一番趣きがあると思うよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「教職員用の寮なのに、生徒が住めるの？」"

hide boy_b1_8
show boy_b1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice suz_g0104
Seito "「最初のうちは教職員専用だったんだけど、その後、生徒用にも開放されたんだ。\n
……っていっても、先生達が多いから希望する生徒は少ないんだけどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「そう、よね。\n
なんだか、ちょっと堅苦しそうだわ」"

hide boy_b1_8
show boy_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice suz_g0105
Seito "「それに、寮長が風紀委員長のユリウス＝モンレーだからなあ。\n
他の寮に比べたら、窮屈かもしれないな」"

hide boy_b1_3
show boy_b1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice suz_g0106
Seito "「あ、ちなみに、ユリウス＝モンレーも、ただの生徒じゃないよ。\n
研究員として残っている、学者なんだ」"

hide boy_b1_2
show boy_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice suz_g0107
Seito "「半生徒、みたいな感じ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（教師陣に、学者の風紀委員長……。\n
{size=+20}間違いなく窮屈だわ{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思考を、顔に出てしまっていたらしい。\n
彼は少し慌てたように、言葉を続ける。"

hide boy_b1_3
show boy_b1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0108
Seito "「でも、真面目で堅いだけの寮だとは思わないでくれよ？\n
塔にはナイトメア先生という、とんでもない問題児もいるからね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……問題児？\n
先生が？？？」"

hide boy_b1_5
show boy_b1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice suz_g0109
Seito "「ああ、とびきりのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「先生が問題児だなんて……。\n
一体、どんなところなのかしら」"

hide boy_b1_1
show boy_b1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice suz_g0110
Seito "「塔に来れば、嫌でも分かる」"

hide boy_b1_1
show boy_b1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice suz_g0111
Seito "「結構、賑やかで楽しいんだよ。\n
他の寮に比べるとスリルは足りないかもしれないけどさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「……住むところに、スリルなんていらないわ」"

hide boy_b1_8
show boy_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice suz_g0112
Seito "「じゃあ、やっぱり、塔がおすすめだ」"

hide boy_b1_3
show boy_b1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice suz_g0113
Seito "「僕は、塔での生活が気に入っている。\n
穏やかで、落ち着いていて、ほのぼのとして……、はいないけど」"

hide boy_b1_2
show boy_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice suz_g0114
Seito "「もし、君が特にスリルを追い求めていないなら、塔に来るといい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……ありがとう。\n
参考になったわ」"

hide boy_b1_3

jump gakuen_op3d_read
label gakuen_op3d_read:
jump gakuen_op3
label gakuen_op3e:
label gakuen_op3a_check:
if renpy.seen_label("gakuen_op3a_read") == True:
    if renpy.seen_label("gakuen_op3b_read") == True:
        if renpy.seen_label("gakuen_op3c_read") == True:
            if renpy.seen_label("gakuen_op3d_read") == True:
                jump gakuen_op3h
jump gakuen_op3f
label gakuen_op3h:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆の話を聞いていると、シンフォニアの寮は本当に特色豊かだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "華やかな赤薔薇寮。\n
自由な帽子屋寮、賑やかな遊園地寮、少し硬い塔……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「皆、いろいろ聞かせてくれて、ありがとう。\n
よくよく考えてから、決めることにするわ」"


show boy_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_2")
voice oni_g0081
Seito "「うん、よく考えて、自分に合ったところを選びなよ」"

hide boy_a2_3
show boy_a2_3 at left
with dis

show girl_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_2")
voice nos_g0136
Seito "「ええ。\n
寮選びは、学生生活に多大な影響を与えることになるから……」"

hide boy_a2_3
show boy_a2_3 at left_center
hide girl_b1_8
show girl_b1_8 at center
show boy_b1_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_2")
voice suz_g0115
Seito "「後悔のないように。\n
でも、気軽にな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……励ましたいのか、脅したいのか、どっち？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とても、気軽に考えられるようなアドバイスではない。"

with dis
$ hi_mes()
hide boy_a2_3

hide girl_b1_8

hide boy_b1_2


scene bg10_sb_day
with stripe_l_medium

play music entrance_p_wam

scene bg_par29_js
with stripe_l_long
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "事務室についた。\n
私以外の新入生でも賑わっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……すみません、入寮の手続きを行いたいんですが」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "並んだり、長時間待たされるようなことになるのだろうかと覚悟しつつも、事務の女性へと声をかける。"


show jimu1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0086
Jimu_w "「はい、この書類ですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あっけないほど、すぐに、必要な書類を用意してくれた。\n
流れ作業で、慣れているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（入寮届け……、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これに記入して、提出するだけですむようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただの紙切れ。\n
簡単な作業で、この先の生活が変わる。"

hide jimu1_3
show jimu1_2 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0087
Jimu_w "「それでは、記入が終わりましたらこちらの受付まで書類の提出をお願いします」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……どの寮にしよう？）"

hide jimu1_2
with dis
$ hi_mes()
scene map_par_bg_move with fade
show screen gakuen_move
$ ui.interact()
