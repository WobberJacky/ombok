label gakuen_joker_end:
scene bg_map_nig
with dis
$ clockanim()


scene bg_par15_rg_tow_nig
with dis

scene bg24_rj_nig
with dis

play music view_nig_p_wam

scene bg06_sk_h_nig with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いよいよ、ブリーズの夜がやってきた。\n
そわそわと浮き足立つような空気は、ストームの夜を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのときとは違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの夜は何も知らずに戸惑っていたが、こうして迎えたブリーズの夜は、何が起こるのかを把握した上で覚悟を決めている。"


scene bg24_rj_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は部屋の中で静かに待機していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（そろそろ……、かしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの開始は、それを伝える役目の生徒が各部屋の扉をノックして回ることで知らされるのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "参加する気のある人間はその音を合図に行動を開始し、参加する気のない生徒はただその合図を聞き流すだけでいいらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は参加組なので、その合図を待つ。"

play sound se_0290
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアが鳴った。\n
時間だ。"


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0008
Seito "「開始の合図だわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0009
Seito "「ブリーズよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いよいよ、ブリーズが始まる。"

play sound se_0275

scene bg25_rr_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し待ってから、ドアを開けて外を見た。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう、そこにノックの合図をした生徒の姿は見当たらない。\n
姿隠しの魔法を使っているのか、それとももう行ってしまったのか。"

play sound se_0262
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、ポケットの中から小さな鍵を取り出した。\n
ホワイトさんのほうのジョーカーから渡された鍵だ。"


scene bg25_rr_nig_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0121
Joker "「君は、これがどこの鍵だか知っているはずだよ。\n
……使い方もね」"


scene bg25_rr_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は前に一度、彼がこの鍵を使うところを見ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は部屋から出ると、ばたんとそのドアを閉めた。\n
ドアを振り返る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_14")
T "（あれは……、あの部屋に限らないのよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鍵のほうが、部屋を決める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前にあるのは、私の部屋のドアだ。\n
これまで、何度も開け閉めをしてきた。"

play sound se_0262
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手の中の鍵を、そっとドアノブに近づける。"


show m_jo_end1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今まで何もなかった金属のドアノブの表面に、鍵穴が浮かびあがった。\n
鍵穴へと鍵を差し込んで、回す。"

play sound se_0451
hide m_jo_end1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "開錠される音が、廊下へと響き渡った。\n
ドアノブへと手をかけて、押し開く。"

play sound se_0285
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "通常なら、私の部屋へと繋がるドア。\n
けれど、この鍵を使ったならば繋がる場所は別だ。"
if lovechara_jokbla_points == 4:
    jump gakuen_joker_end3
jump gakuen_joker_end1_5
label gakuen_joker_end1_5:

show m_jo_end2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0127
Joker "「いらっしゃい、[firstname]。\n
でも、君が選ぶのはここでいいの？」"
menu:
    "構わない。":
        jump gakuen_joker_end2b
    "どういう意味？":
        jump gakuen_joker_end2a
label gakuen_joker_end2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_15")
T "「……ええ、構わないわ。\n
私は、ここを選ぶわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_15")
voice jok_g0128
Joker "「そう。\n
それが君の選択ならどうぞ」"

jump gakuen_joker_end3
label gakuen_joker_end2a:

scene bg_par13_fr ##instantPAY ATTENTION="true"]
hide m_jo_end2

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「……どういう意味？\n
私、何か間違えた？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "渡された鍵を使い、彼のいるシンフォニアの秘密の部屋へと繋がる扉を開けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（何も、間違えていないわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのはずだ。\n
何も間違えていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう思うのに、次第に不安になる。\n
ふわふわと、覚束ない夢の中に迷い込んでしまったような心地だ。"


show jo_m2_03_19 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0129
Joker "「だって君は、ここを心からは楽しめていないだろう？\n
いつだって、小さな違和感を覚えている」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（……っ！！）"

hide jo_m2_03_19
show jo_m2_03_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jok_g0130
Joker "「だから、積極的に楽しめない。\n
この世界に、背を向けたがっている」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「そんなこと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ない、と言いたい。\n
けれど、言いたいと思ってしまっている時点ですでにもう認めてしまったようなものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（世界だなんて大袈裟だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、私はずっと、この学校生活に違和感を覚えていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世界一の魔法学校なんていう恵まれた環境で、たくさんの友人に囲まれて……、幸せな学校生活のはずなのに。"

hide jo_m2_03_14
show jo_m2_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0131
Joker "「君自身が受け入れられない世界を、君は楽しめるのかな。\n
俺は、どっちでもいいんだ」"

hide jo_m2_01_12
show jo_m2_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0132
Joker "「決めるのは君だよ、[firstname]。\n
君だけが決めることが出来る」"

play sound se_0481
hide jo_m2_01_11


show black onlayer master
with dis

play music disquieting_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカーの声に、頭がぐらぐらとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0133
Joker "「俺は……、君が望むままに」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……どうして？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（どうして私は、ここに馴染めないの？\n
原因は何？）"

hide black
show m_jo_end_w1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視界の端を、見覚えのある色彩がひらりと揺らめいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（姉さん……！）"

hide m_jo_end_w1
show m_jo_end_w2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの夜と同じだ。\n
廊下の向こうに、ぽつんと後姿の影がたたずんでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_12")
T "（追いかけなきゃ……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "胸が潰れるほどの焦燥がこみ上げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここで追いかけないと、もう二度と会うことが出来ないような気がした。\n
そんなふうに焦るなど、おかしなことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉は実家にいる。\n
長期休みに実家に戻れば、いつもと同じように迎えてくれると分かっているはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう私は分かっているのに、目の前で見てしまうともう駄目だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "存在が危うく揺れる、姉の後ろ姿。\n
追わずにいられない。"

play sound se_0051
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "引き寄せられるようにして姉の後ろ姿を追いかけた私の腕を、ジョーカーが捕まえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「っ、放して！\n
姉さんを追いかけなきゃ……っ！」"

play sound se_0551
hide m_jo_end_w2
show m_jo_end_w3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振りほどこうと腕を振るものの、逆にぐいっと引き寄せられて、その腕の中に閉じ込められてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "「ジョーカー……っ！！」"

play sound se_0007
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice jok_g0134
Joker "「大丈夫だよ、[firstname]。\n
彼女がいないのは、君が一番よく分かっているだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice jok_g0135
Joker "「ああ、ここには、と言ってあげたほうが優しいかな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_4")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉さんが、いない。\n
姉さんが「ここには」いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よく似ているようで、その意味合いには大きな違いがある。"

play sound se_0052

scene bg25_rr_nig ##instantPAY ATTENTION="true"]
hide m_jo_end_w3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抱き寄せる腕の中から逃れようともがきながら振り返った先、廊下にはもう姉の後ろ姿はなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（姉さん、どこに行ってしまったの？）"


show m_jo_end_w4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そもそもシンフォニアの塔の中に姉がいるはずがないということは、頭の中から消えていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、違う。\n
消えたのではなく、自分から否定してしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉は、イーディスや父親とともに実家で私を待っている。\n
そんなことはもう、信用できない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がこの世界に馴染めず、違和感を抱き続けた理由がようやく分かった気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（ここは……、満たされすぎているんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょっと別れがたく思ってしまうほど、個性的な人達ばかり。\n
楽しくスリルもある賑やかな毎日。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恵まれた環境で学び、育つ。\n
実家では姉さんや家族が待ち、帰る場所もある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "将来は開け、何も欠けたところがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（欠けたところのないものなんて、不自然だもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この世界はおかしい。\n
私にとって、都合がよすぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完璧すぎることが、世界を壊す。"

hide m_jo_end_w4
show m_jo_end_w5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……ねえ、ジョーカー。\n
これは、夢なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すべてが曖昧な中、私を掴む腕の感触だけが確かだ。\n
この手が私を妨害して、思い通りにいかせない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "暴れるのをやめてもなお、放してもらえない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0136
Joker "「さあ、俺にも分からない。\n
たくさんある可能性の一つに、うっかり紛れ込んでしまったのかもしれない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0137
Joker "「分からないし、そんなことには興味もない。\n
ただ……」"

play sound se_0055
camera at hpunch
camera at vpunch
hide m_jo_end_w5
show m_jo_end_w6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐいと引き寄せられて、その腕の中に完全に捕らえられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0138
Joker "「君は、たくさんの幸せが溢れる楽園よりも、俺を選んだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_7")
T "「……あなたを選んだつもりはないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（ただ、私は受け入れられなかった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これを、現実とは。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_12")
T "（選んだつもりなんてないわ）"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すがるように、抱きしめる彼の背に回した腕に意味なんてない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふわふわ、ひらひらと揺れていたドレスの裾を思い出す。\n
私を幻想の世界から呼び起こす、姉の声。"

hide m_jo_end_w6
show al_01_s onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昔、庭で眠ってしまった私を起こすのは姉の役目だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0059
Lorina "「あらあら、こんなところで寝ちゃって。\n
[firstname]？ほら、起きて？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（ええ。\n
そうね、起きなきゃいけない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幸せな夢だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつだって、家に帰れる。\n
待っていてもらえる。"

hide al_01_s
show m_jo_end_w6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……きっと、私の願望の形をしているのね。\n
ここは、私に優しすぎるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ほどほどに散らかっていて、それでいてついていけないほどの異世界でもない。\n
その中間、手を伸ばせばどちらにでも行ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0139
Joker "「はは。\n
幸せな願望を重ねたのは何も君だけじゃないさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0140
Joker "「美味しいところだけをつまみ食いし、楽しいところだけを詰め込んだ。\n
ここは……、おもちゃ箱の世界だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（……おもちゃ箱の、世界）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おもちゃ箱の中のように、楽しいものが詰まっている。\n
遊びに夢中で、現実を忘れてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0141
Joker "「もう充分に楽しんだ？\n
満足したかい？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭の中を、覚えていないはずのたくさんの記憶がよぎっていった。"

hide m_jo_end_w6
show m_jo_end_w7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「……ええ。\n
楽しかったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "答える声は、思った以上に晴れやかだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0142
Joker "「それじゃあ、そろそろ行こうか。\n
……君が収まるべき箱の中へ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢から覚めた先、私が目覚めるのはどこなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0143
Joker "「大丈夫だよ、安心して。\n
どこにいったって、俺が君を閉じ込めてあげるからね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「……それの、どこが安心できるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういいながらも、強く抱きしめる彼の腕の檻の中、私は確かに安らぎを感じていた。"

hide m_jo_end_w7
show pri onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脳裏に浮かぶのは、牢獄の幻だった。\n
物置で、鍵を使って開けたドアの先に一瞬垣間見えた世界。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あちらこそが、私にとっての真実なのだろうか。\n
それとも、また新しい夢に誘われるだけなのか。"

hide pri
show m_jo_end_w8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（牢獄へ行くくらいなら、幻想の世界のほうを選んでしまいそう。\n
迷いそうだけど……、ジョーカーがいるのなら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこにいっても、私を閉じ込めてくれるのだという彼。\n
ジョーカーがいれば、迷うまでもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこへ紛れても、どんな夢をみても、一人にはならないという確証。\n
彼に安堵を覚えてしまった私は、きっともう戻ることは出来ないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（幸せな夢は、終わる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "終わらせたのは、私だ。"

hide m_jo_end_w8 with Dissolve(5)
##[cg time="5000"PAY ATTENTION="true"]
hide frame_par_togaki
hide ali_m_06_16
with Dissolve(5)
scene black with Fade(5)
stop music
##endmemory
jump gakuen_b
label gakuen_joker_end3:
play sound se_0481

scene bg_par13_fr
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋に足を踏み入れようとした瞬間、くらりと眩暈がした。\n
ほんの少しの間だけ、意識が惑う。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0144
Joker "「[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さく、ジョーカーの声が聞こえた。\n
ぼんやりとそんな眩暈を振り払うように瞬いた先、私を待ち構えていたのはやはり彼だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さく呼ばれたのはホワイトのほうのジョーカーの声。\n
ただ、目の前にいるのはブラックのほうだ。"


show m_jo_end_b1 onlayer master
with dis

play music forest_thick_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前と同じくセピア色の空気が流れる不思議な部屋の中、長椅子にふんぞり返るように座っている。\n
待ち構えるといった様子に、思わず怯む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ホワイトと、ブラック。\n
我ながら、的を射ているネーミングだと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じ顔をしていても、すぐに見分けはつく。\n
浮かべる表情に、違いがありすぎるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「……ホワイトさんはどうしたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice jok_g0145
Joker "「ジョーカーか？\n
さあな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice jok_g0146
Joker "「あいつは、趣味の悪いいじめっこだからな。\n
今のおまえは、いじめ甲斐がないんじゃねえの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_16")
T "「何それ。\n
口の悪さでなら、あなたのほうがよっぽどいじめっ子みたいだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_16")
voice jok_g0147
Joker "「俺はあいつに比べたら優しいぜ？\n
てめえが、舞台を楽しもうとしている間はな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……舞台？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "舞台になど立った覚えはない。\n
このまま学校生活を続けていけば、そのうち何かの行事で舞台に立つようなこともあるかもしれないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少なくとも、今、私の知る限りではそんな予定は入っていない。"

hide m_jo_end_b1

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「なんだか知らないけど、一人で残念だわ。\n
ホワイトさんなジョーカーの驚く顔も見たかったのに」"


show jo_m1_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice jok_g0148
Joker "「ああん？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「私……、たぶん、あなた達の正体が分かったと思うの」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……たぶん、正解だと思う）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確信に近いものを持っている。\n
彼らについて調べているうちに、よく似た存在に気付いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの学生ならば、誰もがその存在を知っているのに、誰も具体的な人物には会ったことがないとされている。"

hide jo_m1_02_15
show jo_m1_03_19 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0149
Joker "「言ってみろよ。\n
当たりだったら、ご褒美をくれてやるぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_3")
T "「言ったわね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカーのくれる「ご褒美」というと以前のキャンディーを彷彿とするが、ブラックさんのくれるご褒美となると想像がつかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は彼へと歩み寄った。\n
長椅子のすぐ前で、胸を張って彼を見下ろす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じ顔をしているはずなのに、下から私を見上げる視線はまさしく睥睨といった感じで、やはり人相が悪い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その凶悪そうな表情が、どことなく笑みを含んでいるように見えるのは、それなりに付き合いを重ねてきたからだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（機嫌、よさそう）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「あなた……。\n
シンフォニアの校長なんでしょう？」"

hide jo_m1_03_19
show jo_m1_03_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Joker "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "素っ頓狂なことを言っているという自覚はあった。\n
だが、それと同じぐらいに当たっているという自信もある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカーのことについて、皆に聞いてまわっていて気付いたのだ。\n
ジョーカーの存在と、シンフォニア学校長の存在は対極にある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆が存在することを知っていて、その役職の名は知っているのに顔を知らない学校長と。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆が見かけたこともあり、言葉を交わしたことはあるのに、何者なのかがよく分からないジョーカー。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（居場所を探っていたはずなのに、いつのまにか、正体探しを始めていた）"

hide jo_m1_03_18
show jo_m1_03_19 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice jok_g0150
Joker "「へえ？\n
俺が聞いた噂じゃあ……、俺とジョーカーは用務員ってことになってたはずだが」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「どこに住んでいるのか、普段どこにいるのか、そのすべてが謎に包まれた用務員なんておかしいでしょう」"

hide jo_m1_03_19
show jo_m1_03_17 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jok_g0151
Joker "「おかしいことなんざ、シンフォニアにゃあ、山ほどあるだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「何より、誰もその謎を追及しようとしていないのが、おかしすぎるのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるで魔法によって、その存在を追及することが禁じられているかのようだ。\n
皆、ジョーカーが用務員であるという事実までで、納得してしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その用務員が、どこの寮に属し、どこで生活しているのかというところにまで考えが及ばない。そうさせない仕組みがあるに違いないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（魔法を、使っているんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰にも気付かれないように、踏み込まれないようにと、煙に巻いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "居場所どころか、正体も不明。\n
そんな相手を、ブリーズのターゲットにしないといけないというのだから一苦労だ。"

hide jo_m1_03_17
show jo_m1_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0152
Joker "「あー……、アレだ、ほら。\n
俺らが嫌われ者すぎて、誰も俺らに興味をもたなかったから……かもしれないぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……往生際が悪いわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完全に、誤魔化す調子になっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_3")
T "（嫌われているだなんて思っていないくせに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろんな人から話を聞いたが、そこから浮かぶジョーカー達の評判は悪いものではなかった。"

hide jo_m1_01_10
show jo_m1_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0153
Joker "「うるせえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳を塞ぎたくなるような暴言が返ってくる。\n
が、それにも慣れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口にしている言葉の酷さほど、彼の言葉に敵意はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_8")
T "「この部屋が、何よりの証拠じゃないの」"

hide jo_m1_01_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、ぐるりと視線を周囲へとめぐらせた。時間を止めてしまったような、緩やかに時間を進め続けているような……、不思議な部屋だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの秘密の部屋として噂されるこの部屋の鍵を持つのに相応しい人物だなんて、校長しかいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0031
Joker "「それは……、俺が『鍵』の持ち主に相応しいからじゃないかな。\n
ほら、選ばれし者だけが入れるんだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア創設者の帰りを待つことを選んだ、意思を持つ部屋がその鍵を託す相手なんて限られている。"


show jo_m1_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Joker "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自信満々に語ってはみたものの、無言のジョーカーを見ているうちに、何かとんでもない勘違いをとうとうと語ってしまっただろうかと不安になった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「ジョーカー？」"

play sound se_0055
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……っ！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼ぶと同時に、腰がぐっと圧迫された。それが無造作にブラックが伸ばした腕が、私の腰を絡め取ったからだと気付くまでに数秒かかる。"

hide jo_m1_03_11

play sound se_0251
camera at hpunch
camera at vpunch

show m_jo_end_b2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気付いたときには、ぼすんっと引き寄せられた先の長椅子に尻餅をついていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_11")
T "「……ええと？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "椅子にふんぞり返ったブラックの足の間。\n
がっちりと腰を抱く腕が、ベルトのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0154
Joker "「正解だったら、ご褒美をやるって言っただろ？\n
だから、褒美に……、抱きしめてやる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「！？\n
い、いらないわよ、そんなのご褒美じゃなくてペナルティーだわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラックのくれるという「ご褒美」に興味はあったが、想像以上にろくでもなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抱きしめてやることが褒美だなんて、どれだけ自信家なのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、ついご褒美のほうに気を取られてしまったが、正解宣言のほうも驚きだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予想をしていたから、口にした。\n
けれど、こうして認められると、やはり衝撃がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（この、口が悪くてどうしようもない男が、シンフォニア学校長の片割れだなんて）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、片割れなのか。\n
それとも、どちらかが校長という職で、片方は補佐なのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「……ねえ、どうして人前に出ないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice jok_g0155
Joker "「面倒だからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「せめて、学校内では、校長としていたらいいのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jok_g0156
Joker "「だから、言ってんだろ。\n
面倒くせえんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「どうして私にだけ、印象操作の魔法をかけなかったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
Joker "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の尋ねる疑問を、片っ端から「面倒」なんて乱暴な理由で片付けていたブラックが初めて言葉に詰まった。"

hide m_jo_end_b2
show m_jo_end_b3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0157
Joker "「……っち。\n
面倒くせえ女だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0158
Joker "「ジョーカーの野郎と、くだらねえゲームをしていたんだよ。\n
……てめえが帰るか、帰らないかで」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「私が……、帰る？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（……どこに？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずきりと、胸が痛んだ。\n
きっと気のせいだろうが、体が重くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（帰ることが……、重い？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悲しくなる理由も、その言葉を辛いと思ってしまう理由もないはずだ。\n
私には、家族の待つ実家がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0159
Joker "「てめえが悪いんだ。\n
人がせっかく入れてやったっていうのに、つまんなさそうな顔しやがって」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（……あ。\n
そうか、そうなんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の入学をごり押ししたのはペーターだが、その許可を最終的に下したのは校長であるジョーカーだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それがホワイトとブラックのどちらの意思によるものだったのかは分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、彼ら二人は私をシンフォニアに迎え入れてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……悪かったわよ。\n
なかなか環境に適応できなかったの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "バツが悪い思いをする。\n
彼は、すべてを知る立場にあったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうしてせっかく入れてくれたというのに、周囲にうまく馴染めず、少し浮いていた私を彼らはどんなふうに見ていたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あなたは、私がシンフォニアに残るほうに賭けたのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意外だ。\n
彼のほうが捻くれた答えを出しそうなのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0160
Joker "「ああ、俺は優しいからな。\n
てめえが楽しもうとする限り、味方でいてやるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼なりに、私が早くシンフォニアに馴染めるように気を遣ってくれていたのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一方、彼の言葉を裏返すと、ホワイトさんのほうは私が帰るほうに賭けていたのだろう。\n
優しい顔をして意地悪なことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……妙な感じ）"

hide m_jo_end_b3
show m_jo4_1and4_3s onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと目を閉じてみた眼裏で、ひらりといつか見たドレスの裾が舞う。\n
ストームの夜に見た幻だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（せっかくだから、ご褒美を満喫しておこう……、かな）"

hide m_jo4_1and4_3s
show m_jo4_2s onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉の残像。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれは、もしかしたら、ホワイトさんが私に見せていたのかもしれない。\n
私の郷愁を、ホームシックをかきためるために。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……そう。\n
あれは幻よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉を失うのではないかという恐怖にかられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早く家に帰らなくてはと焦るなんておかしなこと。\n
実家は常にあるものだし、帰ればいつだって会える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かあったというような連絡は受けていない。\n
虫の知らせともいえないような、馬鹿げた幻覚だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "惑わされてはいけない。\n
あの幻の姉を追いかけてしまうと、私が抱いている違和感が、決定的なものになってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、違和感を追求しない。\n
姉の幻も追わない。"

hide m_jo4_2s
show m_jo_end_b4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（終わらせたくないの）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice jok_g0161
Joker "「不安なら……、手紙を書きゃあいい。\n
てめえの家族に向けて、めそめそと泣き言書きつらねりゃいいんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「そうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手紙が届く距離だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "元気にしていると、伝えられる。\n
元気にしていると、伝えてもらえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0162
Joker "「……返事もくるさ。\n
ここでは、返ってこない手紙はない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう、きっと姉からは丁寧な手紙が届くだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の書いた分量の二倍は固い。\n
綺麗な文字で綴られた長文を想像すると、笑みが漏れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "家の様子から、近所の変化、姉自身の近況から、イーディスや父さんのこと。\n
姉のことだから、ことこまかに愛情のこもった手紙を届けてくれることだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……そうね、手紙を出すのも悪くない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつか渡せなかったラブレターの代わり。\n
家族に手紙を書いてみようか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（あの手紙は……、渡しても返事をもらえそうになかったけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "家への手紙なら、返ってくることが保証されている。\n
安心していられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「そのうち、手紙を書くわ。\n
私がシンフォニアでどう過ごしているのか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（それに、私がどれだけ姉さんのことを好きなのか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice jok_g0163
Joker "「……筋金入りのシスコンだな、てめえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そりゃあ、そうだろう。\n
少し離れているだけで、こんなにまでホームシックになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ホワイトさんのジョーカーが、罠を仕掛けるまでもない。\n
私はすでに、帰りたくなっている。"

hide m_jo_end_b4
show m_jo_end_b5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_3")
T "「悪い？\n
それくらい、私の姉さんは素敵な人なのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抱きしめる腕の中で、ふんと鼻で笑う。\n
それからゆっくりと体から力を抜いて、その腕のうちに体を預けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「手紙を、書くわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice jok_g0164
Joker "「……ああ、好きにしろよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「ええ、好きにする」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく、私は手紙を書かないだろう。\n
たとえ書いたとしても、投函はしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう分かっていて、繰り返す。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「手紙を、書くわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（たとえ、届かなくても）"

hide m_jo_end_b5
with Dissolve(5)
hide frame_par_monologue
hide ali_m_01_1
with Dissolve(5)
scene black with Fade(5)
stop music
##end memory
jump gakuen_b
