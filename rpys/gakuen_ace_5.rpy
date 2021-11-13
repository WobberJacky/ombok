label gakuen_ace5:
scene bg_map_day
with dis
$ clockanim()


scene bg25_rr_day
with dis

play music dining_day_p_wam

scene bg_par02_ct_ros_day with Dissolve(1.2)
play sound se_0498
play sound se_0547
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの次の日の朝、カフェテリアはいつも以上に賑やかだった。\n
あちらこちらで、ストームの話で盛り上がっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな中、私はいつものように適当に空いた席に座って朝食を取っていた。\n
メニューも定番の、ジャムとトースト、そしてサラダとオレンジジュースだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さくさくと香ばしく焼けたトーストを齧っていると……。"


show rose_a1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0114
Seito "「そういえば、昨夜、仮面姿の男子生徒がメイドさんに剣を突きつけて寮の中を案内させているのを見たんだけど……」"

hide rose_a1_9
show rose_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0115
Seito "「……あれ、何だったのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……{size=+20}っぐ！？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "隣から聞こえてきた話題に、危うくトーストを喉に詰まらせそうになった。"

hide rose_a1_5
show rose_a1_5 at left
with dis

show rose_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0094
Seito "「さあ？\n
昨夜はストームだったもの、何かイベント絡みじゃないの？」"

hide rose_a1_5
show rose_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0116
Seito "「そうね。\n
でも、さすがに仮面姿で剣を突きつけているのには、驚いちゃって……」"

hide rose_a2_1
show rose_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0117
Seito "「……どう、イベント絡みなのかしら」"

hide rose_b1_8
show rose_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0095
Seito "「なんだか分からないけど、ストームだもの。\n
何だってあるでしょう」"

hide rose_a2_5
show rose_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0118
Seito "「でも、仮面に剣よ……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（そ、それって……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしなくとも、心当たりがある。\n
むしろ周囲が気付かないほうが不思議でならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくらシンフォニアの生徒数が膨大だからといって、赤薔薇寮の生徒で、しかも帯剣しているようなのは、そう多くないと思うのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（しかも、仮面だのを被りそうな、一歩間違えれば変質者の方面にいきそうな具合に無茶苦茶なのときたら……）"

hide rose_a2_4
show rose_a1_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
Seito "「……？」"

hide rose_a1_9
show rose_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice man_g0119
Seito "「あら、[firstname]、あなたどうしたの？\n
むせるなんて、そんなに急いで食べなくても料理は逃げないわよ？」"

hide rose_b1_2
show rose_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice tak_g0096
Seito "「……悪戯好きの子が料理に魔法をかけない限りね」"

hide rose_a1_2
show rose_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice man_g0120
Seito "「……ああ、前にあったか、そういうのも。\n
料理脱走事件ね」"

hide rose_b1_1
show rose_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice tak_g0097
Seito "「ま、めったにないことだけどね」"

hide rose_b1_3
show rose_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice tak_g0098
Seito "「……大丈夫？\n
ほら、これ、オレンジジュース」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "話しこんでいた女子生徒二人が、むせた私を振り返ってそれぞれ心配してくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのうちの一人が差し出してくれたオレンジジュースのコップを受け取って、ぐびぐびと喉に詰まりかけていたトーストを流し込んだ。"

play sound se_0065
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……ふう」"

play sound se_0212
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やっと人心地を取り戻したものの……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ありがとう、もう大丈夫よ。\n
それで……、その仮面男の話、もうちょっと詳しく聞かせてもらってもいい？」"

hide rose_a2_5
show rose_a1_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice man_g0121
Seito "「え？\n
ああ、そんな話していたっけ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽんぽん話題の変わる彼女達。\n
関心はすでに仮面男から最近の魔法による悪戯へと移っていたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（でも、私は移っていないのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前の話題が知りたい。"

hide rose_a1_8
show rose_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0122
Seito "「もっと詳しくって言われても、ねえ。\n
私もね、部屋から出たときに見掛けただけなの」"

hide rose_b1_2
show rose_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0099
Seito "「私は見ていないから、なんとも言えないわ。\n
でも、メイドを人質にとるなんて、すごいわよね」"

menu:
    "すごい、と言われれば確かにすごい。":
        jump gakuen_ace5_2a
    "すごくない。":
        jump gakuen_ace5_2b
label gakuen_ace5_2a:
$ lovechara_ace_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「そりゃあ……、すごい馬鹿よね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すごいかすごくないか、といわれたら、それはすごい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくらイベントだからといって、学校関係者に刃物を突きつけて、脅した上に案内をさせるなんて、正気の沙汰ではない。"

hide rose_a1_5
show rose_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0123
Seito "「いやいや、馬鹿ってだけじゃなくてね？\n
ここの使用人達は皆それなりに強いのよ？」"

jump gakuen_ace5_3
label gakuen_ace5_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……そう？\n
メイドや使用人だって、まさか生徒にいきなり人質にされるなんて事態、備えていないでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "油断しきっている隙をつくなら、充分に可能であるような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "敵がいると身構えているのならば対処できたとしても、身内だと思っている人間から唐突に攻撃を受けた場合、なかなか防げないだろう。"

hide rose_a1_2
show rose_a1_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0124
Seito "「あら、昨夜はストームだったのよ？\n
備えているだろうし、警戒は相当だったと思うわ」"

hide rose_a1_9
show rose_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0125
Seito "「それに、ここの使用人達は、皆それなりに訓練されているの。\n
強いし、普段から、気を張っているはず」"

jump gakuen_ace5_3
label gakuen_ace5_3:
hide rose_b1_4
show rose_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0100
Seito "「ええ。\n
ここの使用人や職員は皆、それなり以上の魔法の使い手なの」"

hide rose_b1_2
show rose_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0101
Seito "「それこそ、普段私達が校則違反をした際に取り締まることが出来る程度には、ね。その使用人を脅していうことを聞かせるなんて、たいしたものだわ」"

hide rose_a2_5
show rose_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0126
Seito "「それだけ使用人達が手ごわいからこそ、ストームをいいことに、使用人と戦うことをイベントのメインに置いている寮だってあるぐらいなんだから」"

hide rose_b1_4
show rose_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0102
Seito "「赤薔薇寮ではそうでもないけど、帽子屋寮なんかその典型よね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帽子屋寮。\n
想像はつく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（双子達ね……。\n
いかにもって感じだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……それは賑やかそうだわ。\n
前に一度、使用人達が警備も手がけている……、というような話も聞いたことがあるし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かの話のついでのように、シンフォニアにはお忍びで高貴な人が生徒として通っている、というようなことを聞いた。"

hide rose_b1_8
show rose_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0103
Seito "「そうね、噂だけど……。\n
ルーンビナスのプリンセスが滞在していたこともあるらしいわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「プリンセスが？\n
そう考えると……、今だって、私達が気付いていないだけで、いらっしゃるのかもしれないわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「プリンセスとまではいかなくても、高貴な方が」"

hide rose_a2_1
show rose_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice man_g0127
Seito "「ふふふ。\n
ビバルディ様も、そんな一人だという話があるのよ？」"

hide rose_b2_3
show rose_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice tak_g0104
Seito "「そうそう、ビバルディ様が本当に女王様だっていう話でしょう？\n
あの方を見ていると、真実味あるわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_12")
T "「そうね、彼女っていかにも……」"

hide rose_a2_2
show rose_a2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_12")
voice man_g0128
Seito "「そう、いかにも……」"

hide rose_b1_2
show rose_b1_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_12")
voice tak_g0105
Seito "「……オーラがあるものね。\n
なんていうのかしら、一般庶民じゃない感じのオーラ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「別世界……みたいな、ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ほうっと、溜息をつく。\n
届かないものを想うような……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディが本当に女王様、なんていうのはハマりすぎだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうなりたいというよりも、遠くでうっとり見ていたいタイプの、憧れの対象だから。"

hide rose_a2_6
show rose_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0129
Seito "「……まあ、そんなわけで、高貴な人を迎えるには警備も必要でしょう？\n
だから、使用人達もそれなりの実力派揃いという話よ？」"

hide rose_b1_6
show rose_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0106
Seito "「使用人達にまつわる不思議な噂も色々あるみたいだし……。\n
だからね、そんな使用人を人質に取るなんて、なかなか出来ないことなのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……それをやってのけたから、仮面の男はすごい、ってわけね」"

hide rose_a1_3
show rose_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice man_g0130
Seito "「……仮面の男って時点で、色々とすごいけどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……それが一番すごいポイントよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（ああ……、なんで、そんな格好でうろつきまわっていたの……。\n
露出がなくても変質者じゃない……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、変質者は言いすぎ。\n
だが、変質者でなくとも、不審者だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（最初から部屋番号を聞いておくとか……。\n
言ってくれたら私から迎えに行ってもよかったのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迎えに行く、なんて。\n
それではまるで、私がエースに会いたがっていたみたいではないか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_9")
T "（また、負け……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……たくない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースには、負けっぱなしだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……ブリーズは頑張るわ、私」"

hide rose_a1_1
show rose_a1_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice man_g0131
Seito "「え、なに、いきなり……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「いや……、やる気になってきたの」"

hide rose_b1_5
show rose_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice tak_g0107
Seito "「ええ？\n
仮面の男に対抗しようとか？」"

hide rose_a1_4
show rose_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice man_g0132
Seito "「ブリーズを頑張ろうっていうのは、悪いことじゃないけど……。\n
それ……、対抗意識を持つ相手、間違えていない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……いいえ。\n
間違えていないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの次の日の朝は、どうにも賑やかで、混乱する。\n
だが、相手を誤るほどではなかった。"

hide rose_a1_5

hide rose_b1_1

with dis
$ hi_mes()

scene bg14_fm_day
with stripe_l_medium

scene bg13_fr_day
with stripe_l_long

play music forest_thick_day_p_wam
play sound se_0624

show bg06_sk_h_day onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早くもブリーズのことを考え始めたせいか、どうにも落ち着かない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもならば板書は当然として、授業に真面目に参加するというのに、気もそぞろだ。"

hide bg06_sk_h_day


show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0000
Gowland "「よ～し、それじゃあ皆、好きに散って儀式のアイテムになりそうなもんを探してこい！」"

hide go_m_02_12
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0000_5
Gowland "「この森はシンフォニアの敷地ではあるが、モンスターも住んでいるからな！」"

hide go_m_03_9
show go_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0001
Gowland "「危険だと判断した場合には、すぐに俺に助けを求めるように！\n
助けるべきかどうかじっくり考えた後、助けてやるからな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……それ、助けてもらう頃には手遅れなんじゃないの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆がそう思ったらしい。\n
周囲からはさざめくように笑い声が響きあう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_10")
T "（……この雰囲気、好きだな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ一年もこの学園にいない。\n
新入生という立場なのに、ずいぶんと長い間ここにいるような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（魔法も、色々と新しいものを教わったし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日の現代魔法史の授業では、現代に伝わる古典魔法……、つまりはおまじないの復習をすることになっていた。"

hide go_m_03_4
show go_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0002
Gowland "「現代魔法についての歴史を紐解くには、古い魔法を知る必要がある！\n
温故知新というのは、どの科目でも大事なことなんだぜ？」"

hide go_m_01_2
show go_m_03_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0003
Gowland "「音楽においても古典派の存在というものは大きくてな？\n
ああ……、実際に弾いたほうが分かりやすいか」"

play sound se_0582
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今まで穏やかだった雰囲気が一変する。\n
ゴーランドが楽器を出そうとしているのだ。"

hide go_m_03_14
show go_m_03_14 at left
with dis

show bor_m_01_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0016
Boris "「やめろよ、おっさん！\n
せっかくの課外授業がぶち壊しになるだろ！！」"

hide go_m_03_14

hide bor_m_01_8
show bor_m_01_8 at left
with dis

show pia_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0001
Pierce "「ば、バイオリン怖いよっ！！\n
この世界からバイオリンなんてなくなっちゃえばいいのにっ！！」"

hide bor_m_01_8

hide pia_m_02_6
show pia_m_02_6 at left
with dis

show boy_a1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0003
Seito "「はは、ピアス、おまえの気持ちも分かるが……。\n
……悪いのはバイオリンじゃなくて、ゴーランド先生の腕だ」"

hide pia_m_02_6
show pia_m_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0002
Pierce "「ぴ！\n
そっか、じゃあ、バイオリンがなくなっても……」"

hide pia_m_01_4

hide boy_a1_5
show boy_a1_5 at left
with dis

show girl_a2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0006
Seito "「……そうね。\n
きっと、また何か別の楽器が出てくるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "軽口を叩きあいながらも、皆が逃げ腰。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線は足元や森の梢へと向けられ、おまじないの材料になりそうなものを探している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドが本気で楽器を出そうとしたら、すぐにでも逃げ出せるように構えていた。"

hide boy_a1_5

hide girl_a2_1

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（私も、何か探さなくちゃ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……何を？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば、授業が始まる前に、ゴーランドが教室でいろいろ説明しながら黒板に例を書いていたような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……はあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっかり聞き逃してしまっていた。\n
体調が悪いわけでもないのに、こんな不真面目なことをしてしまうのは初めてかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（こんなに、授業に身が入らなくなってしまうぐらいに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すでに、負けているのだろうか。\n
さすがに、こんなにぐるぐる思い出してしまうと否定できない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好きになってしまっているのかもしれない。\n
……仮面をつけ、剣を振り回すような男を。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（どうするのよ……）"


scene bg13_fr_day_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice ace_g0256
Ace "「君が俺のことを好きになっちゃったら？\n
はは、もちろん、ちゃんと責任取るに決まっているだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐるぐるしたままの状態でも、脳天気な声は鮮明に思い出される。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同時に、重い声も、鮮明になってしまう。"


scene m_kyoutuu_yume3
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0130
Seinen "「これ……、君のお姉さんに渡してくれないかな。\n
頼む……、ずっと憧れていたんだ」"


scene bg13_fr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……重症だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、どうやら本当にエースのことが好きらしい。\n
少なくとも、意識している。"


show go_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0004
Gowland "「おいおい、どうしたんだ、あんた。\n
立ち尽くしているが……、何を探したらいいのか分からないのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え……？\n
ああ……、ごめんなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに声をかけられて、自分が授業そっちのけで考え込んでしまっていることに気付く。"

hide go_m_02_3
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0005
Gowland "「ま、若いんだから悩むこともあるだろうさ。\n
時期的に……、ストーム絡みか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "沈黙は、肯定。\n
時期を考えれば、そう思われて当然だろう。"

hide go_m_03_9
show go_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0006
Gowland "「そういう悩みごとにこそ、おまじないは効果があるんだぜ？\n
たとえば……、そうだな、恋まじないとかな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……真面目に授業を受けます」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ニヤニヤとした笑みを浮べられ、居たたまれなくなる。\n
教師のくせにからかいすぎだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな私達の会話を聞きつけたのか、他のクラスメイトまで混ざってくる。"

hide go_m_01_3
show go_m_01_3 at left
with dis

show girl_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0007
Seito "「[firstname]、あなた、誰かおまじないをかけたい相手でもいるの？」"

hide go_m_01_3

hide girl_a1_3
show girl_a1_3 at left
with dis

show girl_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0006
Seito "「うふふ、私が知っているヤツ教えてあげましょうか？\n
ちょうどほら、私、イモリを捕まえたの」"

hide girl_b2_2
show girl_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0007
Seito "「これを黒焼きにしてすり潰して……」"

hide girl_a1_3

hide girl_b2_3
show girl_b2_3 at left
with dis

show boy_a1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0004
Seito "「待て待て待て待てっっ！\n
恋まじないの材料ってそんな不気味なものだったか！？」"

hide girl_b2_3
show girl_b1_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0008
Seito "「そりゃあ、ねえ？\n
より効果が強くなりそうなものを選ばないと、うふふ」"

hide boy_a1_4
show boy_a1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0005
Seito "「おまじないっていうか、黒魔術だろ、それは……」"

hide girl_b1_6

hide boy_a1_5
show boy_a1_5 at left
with dis

show boy_b2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0017
Seito "「女子からの差し入れが怖くなる瞬間、だな」"

hide boy_a1_5

hide boy_b2_1
show boy_b2_1 at left
with dis

show bor_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0017
Boris "「……同じ黒焼きでも、魚がいいな。\n
[firstname]、差し入れするなら魚にしてね」"

hide boy_b2_1

hide bor_m_03_11
show bor_m_03_11 at left
with dis

show pia_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0003
Pierce "「差し入れ？黒焼き？\n
[firstname]、君、俺にイモリの黒焼きくれるのっ？」"

hide pia_m_03_11
show pia_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0004
Pierce "「あれ、美味しいよね！\n
チーズのほうがもっとおいしいけど！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が誘導するまでもなく、話題はどんどんと逸れていってくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……このクラスの、こういうところが好き）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わあわあきゃいきゃい、と森の中が一気に恋まじないやら差し入れの話題で賑やかになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり年頃の学生ともなれば、恋愛ネタへの食いつきはいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも時期が時期。\n
ストームからブリーズにかけての期間ともなれば尚更だ。"

hide bor_m_03_11

hide pia_m_01_6


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……恋まじない、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おまじないというのは、一般的には魔法とはいえない儀式の類だ。\n
魔法のように、確実に効果が保証されているわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法であれば、この呪文を正しく唱えればこういう効果が起きるというのが確定している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、おまじないの場合、効果は必ずではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うまく働くこともあれば、そうでないこともある。\n
確実ならば、それは呪いになってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不確定なもの。\n
そして、どこか気恥ずかしさが伴う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（でも、せっかく、このタイミングでおまじないの授業なんだもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと見やった先、ゴーランドは楽しげにしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_1")
T "（開き直っちゃおうかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先に、恋の魔法なんて馬鹿なことを仕掛けてきたのはエースだ。\n
その仕返しに、私が恋のおまじないに頼ったとしたって、何が悪いだろう。"


scene bg13_fr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きゃあきゃあと尚も盛り上がっているクラスメイト達へ、改めて向き直った。"

play sound se_0454
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ねえ、私もイモリを捕まえたいんだけど、どこで捕まえたか教えてくれない？」"


show girl_b1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice nos_g0009
Seito "「……え？」"

hide girl_b1_9
show girl_b1_9 at left
with dis

show girl_a2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice mat_g0008
Seito "「ふふ、あなた、本気？\n
呪いになっちゃうかもよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "冗談を言っているのだと思ったのか、隣にいた女の子が笑い混じりに私を見やる。\n
それに対して、私はきっぱりと返事を言い切る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「いいじゃない、呪いでも。\n
何か、問題あるかしら？」"

hide girl_a2_2
show girl_a1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_2")
Seito "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女が息を飲む。"

hide girl_b1_9
show girl_b1_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0010
Seito "「ないわよっ！\n
ないに決まっているわ！」"

hide girl_b1_7
show girl_b1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0011
Seito "「恋愛成就のためなら黒魔術にだって手を出す！\n
これが女の心意気よ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一方ぐっと握りこぶしを作って力説したのは、私にイモリの黒焼きを使ったおまじないを教えてくれようとしていた彼女だ。俄然張り切っている。"

hide girl_b1_2
show girl_b1_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0012
Seito "「これこそ正しい恋愛道よ！\n
ふふふ、あっちにね、イモリのいる池があるのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こっちよ、と手招きしながら歩き出す彼女の後を追って歩き出す。"

play sound se_0624

show go_m_03_12 at center
with dis
hide girl_b1_6

hide girl_a1_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0007
Gowland "「ふむ。\n
恋まじないも……、授業の中できっちりやったら効果があるかもしれないよなあ？」"

hide go_m_03_12
show go_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0008
Gowland "「さぁてと、俺も教師としてあいつらに指導してくるかな。\n
あのままだと本当に恋の黒魔術になりかねない……」"

hide go_m_01_8
show go_m_01_8 at left
with dis

show girl_c2_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0000
Seito "「効果がある！？」"

hide go_m_01_8

hide girl_c2_4
show girl_c2_4 at left
with dis

show boy_c1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0015
Seito "「恋の黒魔術！？」"

hide girl_c2_4
show girl_c2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0001
Seito "「効き目ありそう……」"

hide boy_c1_4
show boy_c1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0016
Seito "「強力そうだ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後で、クラスメイト達が息を飲む気配が伝わってきた。"

play sound se_0620
play sound se_0484


hide girl_c2_6

hide boy_c1_1


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0009
Seito "「わ、私もやるわっ！\n
溺れる者は藁でも掴むのよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0006
Seito "「俺もやるぞ！\n
それで、彼女が出来るなら……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0018
Boris "「……皆、物好きだねえ。\n
それじゃあ、俺は後学のためにってことにしておこうかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0005
Pierce "「皆でイモリの黒焼きを作るんだねっ？\n
うんうん、俺も頑張るよ！美味しい黒焼き作ろうね！」"

play sound se_0624
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一人が続けば、また一人。\n
ぞろぞろと皆が私達の後を追いかけてきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一人でやる分にはちょっと恥ずかしかったり、効果に期待がもてないそれでも、授業の中で皆とやるなら試してみたいという者は多かったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも、教師の指導のもとで恋まじないを実践するチャンスなんてそうそうない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "期待と、好奇心とが交じり合ったわくわくとした空気が、クラスメイトの間を次々に伝染していく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その結果、最終的にはクラス全員で恋まじないに取り組むことになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気になる相手がいる場合は、相手に自分を好きになってもらうための恋まじないを。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気になる相手がいない場合には、よい出会いが望めるように恋まじないを、といった具合だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆でしばらく、材料収拾に精を出す。"


scene bg17_rv_day
with dis
play sound se_0110

show girl_a1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0010
Seito "「ああっ、イモリに逃げられた……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「結構、すばしっこいわよね。\n
……憎たらしいぐらいだわ」"

hide girl_a1_4
show girl_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice mat_g0011
Seito "「氷系の魔法で一回固めちゃうのはどう？\n
凍らせると、成分が変わっちゃって、やっぱりまずいかしら」"

hide girl_a1_5
show girl_a1_5 at left
with dis

show girl_b2_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice nos_g0013
Seito "「どっちみち黒焼きにしちゃうんだから、いいような気もするけど……。\n
どうなのかしら」"

hide girl_a1_5

hide girl_b2_9

play sound se_0583
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "森の中に湧いた清水の中、足首のあたりまでを浸す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せせらぎの中を、赤と黒のまだら模様のイモリが優雅に身をくねらせて逃げていくのが見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し離れたところからは、恋愛成就ではなく、出会いのためのおまじないの材料を探す生徒たちの会話も聞こえてくる。"

play sound se_0748
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0007
Seito "「出会いを求めるならば……、朝露に濡れたムラサキスミレの花弁と、グリズの実が必要なのか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0007_5
Seito "「……この時間に朝露ってまだ残っているっけ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0002
Seito "「……もう昼過ぎよね？\n
さすがに、この時間には朝露なんて残っていないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0008
Seito "「後から別に採取した朝露を、調合の際に追加する形でもいいのかな……。\n
くそう、こうして考えるとおまじないって根性がいるな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0003
Seito "「……だから、相当に暇な人か、暗い人しかはまれないのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0004
Seito "「もしくは、藁にすがりたいくらい、真剣か」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……私は、最後のではないわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "否定しつつも、真面目にイモリを捕まえるべく、川の流れに挑む。"

play sound se_0583
with dis
$ hi_mes()

scene bg14_fm_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_map_nig
with dis

scene bg_map_day
with dis

scene bg24_rj_nig
with stripe_l_long

show bg06_sk_h_day onlayer master
with dis

play music daytime_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドによる、おまじない講座から数日。ストームの仕返し版でもあるブリーズは、もう次の日というところにまで迫っている。"

hide bg06_sk_h_day

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は自室のベッドの上、ぼんやりと天井を眺めていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……完成、しちゃった）"

play sound se_0533
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "懐から取り出して、天井にかざしてみるのは小さな瓶に入った惚れ薬だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのおまじないの授業の結果、完成したもの。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "捕まえたイモリを黒焼きにして、ゴリゴリとすりつぶし、あんなものやこんなものといろんなものを混ぜ合わせた結果できたものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（いろんな意味で口に入れて大丈夫なのか、不安は残るけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何を材料にしているのかが分かっている分、視線が泳いでしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一緒に授業を受けたクラスメイト達も、皆それぞれ特別な惚れ薬や、出会い薬を作ることに成功していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "材料だけを見るならば、出会い薬のほうが飲みやすい気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ、材料は朝露とムラサキスミレの花弁とグリズの実だ。\n
妙な動物由来の材料が含まれていない分、安心できる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（自分で飲む分には飲みやすい材料というのが、なんとも言えないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こっそりと好きな相手に飲ませるブツはイモリの黒焼きをメインにした惚れ薬で、自分で飲む出会いのための薬は花びらや木の実というあたりが、実に。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（そういえば……）"


scene bg24_rj_nig_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice gor_g0009
Gowland "「月光には人の想いを増幅する作用がある……、って言われているからな。\n
より強力な効果が欲しいやつは、毎晩月明かりに当てておくといいぜ」"


scene bg24_rj_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの言葉を思い出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……パワーアップさせておくべきかしら）"

menu:
    "パワーアップさせる。":
        jump gakuen_ace5_4a
    "そのままでいい。":
        jump gakuen_ace5_4b
label gakuen_ace5_4a:
$ lovechara_ace_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（せっかくだから、パワーアップさせよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むくりとベッドから起き上がると、小瓶を片手に窓際へと向かった。"

play sound se_0165

scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓の外から、月明かりがさあっと部屋へと差し込んできた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "臨む相手は、あのエースだ。\n
いくらパワーアップさせたとしても、させすぎということはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「やるだけやってみよう……」"

play sound se_0218
pause .5
play sound se_0165

scene bg24_rj_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ことりとそれを月明かりの差し込む窓際へと置いて、私はカーテンを閉じてベッドに戻った。\n
再び、ごろりと横になる。"

play sound se_0328
jump gakuen_ace5_5
label gakuen_ace5_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……これ以上、ナニをどうするっていうのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もうすでに、いろんな意味で劇物のような材料だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを、これ以上パワーアップさせる必要はないだろう。\n
私は、ごろんとベッドに横になったまま目を閉じる。"

play sound se_0328
jump gakuen_ace5_5
label gakuen_ace5_5:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの教師指導の下に作成した惚れ薬。\n
それがはたして、あのエースにどれほどの効果があるのか分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そもそも、どうやってエースに飲ませるのかも、まだ考えてはいない。\n
……おとなしく、飲んでくれるだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……せっかく作ったものが無駄になるのは悔しいな）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_13")
T "（いざとなったら、口の中にねじ込んででも……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの夜は近い。\n
私に恋の魔法なんてものをかけたのだから、エースにはその責任をしっかりとってもらうとしよう。"

with dis
$ hi_mes()

scene bg25_rr_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_ace6
