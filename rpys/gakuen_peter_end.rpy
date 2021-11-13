label gakuen_peter_end:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_ros_day
with dis

play music dining_day_p_wam

scene bg_par02_ct_ros_day with Dissolve(1.2)
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの翌朝。\n
ストームのとき同様、昨夜の名残で賑やかなカフェテリアに赴く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（え……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二対のわくわくした視線と、一対のじっとりとした視線でもって迎えられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎょっとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズのことでいろいろ相談にのってもらった二人が詳細報告を待ち構えているというのは、予想済み。\n
しかし……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（なんで、ここに？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「ビ、ビバルディ！？」"


play music vivaldi_t_ali

show viv_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice viv_g0273
Vivaldi "「……ふん。\n
なんじゃ、わらわがいたら困るとでも言いたげだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女の機嫌は、あまりよろしくないようだ。\n
拗ねたように息を吐き出すと、ツンっとそっぽを向いてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（そういう態度も……、はまっているなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、うっとりしている場合ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がここにくる前にいったい何があったのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段は自室に朝食を運ばせるビバルディが、朝のこんな時間からカフェテリアにいるなんて、どう考えても異常事態だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のような新入生は、まだまだ授業に選ぶ余地が少ないため、強制的に朝一の授業が時間割りに組まれていたりもするが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディのような研究者扱いの者は、自分の都合にあわせて授業を組むことが出来る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（いや……、授業に出る必要もないのよね。\n
研究者だから、自分が教える側になってクラスを持ったりも出来るんだし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうするかどうかは別として、講師になることも出来る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自由度が高いので、ビバルディはまだ部屋でゆっくりしているはずの時間。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それがこうして、らしくもなくカフェテリアに顔を出しているということは……、何かよろしくないことが起きてしまったのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「隣、かけていい？」"

hide viv_m_03_9
show viv_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice viv_g0274
Vivaldi "「……許可をとる必要などない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（ってことは、いいのね？）"

play sound se_0161
hide viv_m_03_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少々身構えながらも、ビバルディの隣へと腰掛けた。\n
友人二人は向かいの席だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人はすでに朝食を始めていたのか、テーブルの上には食べかけの皿がいくつか並べてある。\n
私は、今朝は寝坊気味なので出遅れた。"


show rose_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0097
Seito "「おはよう、[firstname]」"

hide rose_a2_2
show rose_a2_2 at left
with dis

show rose_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0077
Seito "「許可をいただけたことだし、早く座って」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（許可をとる必要がないって言われただけで、許可をもらえてはいないと思うけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達は、ビバルディに対しても興味津々といった視線を向けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディは赤薔薇寮の寮長ということで、寮生にとっては身近で遠い存在。\n
自治会の会長なんて大層な役職につき権力を持っている分、尚更だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなビバルディが、珍しくも朝のカフェテリアに同席している。\n
好奇心が掻き立てられたとしても、おかしくはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「……えっと。\n
おはよう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっぽを向いてしまった女王様のことを気にしつつも、とりあえず目の前の二人へと挨拶をする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉尻が持ち上がり疑問形のようになってしまったのは、二人が朝食を共にするために私を待ち受けているわけではないと分かっているからだ。"

hide rose_b1_3
show rose_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0078
Seito "「おはよ。\n
えっと……、とりあえず、会長にお礼を言ったほうがいいと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え？」"

hide rose_a2_2
show rose_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice man_g0098
Seito "「見かけたら、エース先輩にも言っておいたほうがいいわね。\n
……そっちは、見かけたら、だけど」"

hide rose_b1_5
show rose_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice tak_g0079
Seito "「ええ、探すまでには及ばないわよね。\n
エース先輩を探して見つけるのは、相当な試練だもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女らの言葉に、反射的に視線をめぐらせてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（いない、か……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いれば目立つであろう笑顔の青年を、カフェテリア内に見つけることは出来なかった。恐らく、またどこかを放浪しているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……そういえば、寮内でもなかなか見ないものね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「お礼を言うのは構わないんだけれども……。\n
私、事情を把握していないの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディやエースが私のために何かをしてくれたというのならば、お礼を言わなければならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、何をしてもらったのかも分からないままに、ただ言葉だけで礼を告げても感謝の心は伝わらないだろう。"

hide rose_a2_1

hide rose_b1_3


show viv_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0275
Vivaldi "「……昨夜のことじゃ。\n
おまえときたらホワイトと……っ、ああ、腹立たしい！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（詳細報告をするまでもなく、バレバレじゃないの……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "反応や態度が、相手の評価や結論を決める。\n
それは、昨夜自らで立証済み。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "反応したら負けだと分かっていても、ビバルディが苛立たしげに口にした言葉にかっと顔が熱くなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな私の様を見て、正面の二人はにま～っと嫌な感じに笑っている。\n
ビバルディの言葉と、私の反応とですべてを察した、といった感じだ。"

hide viv_m_02_6
show viv_m_02_6 at left
with dis

show rose_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0099
Seito "「あなた、昨日ブリーズの終了時刻、寮に戻ってこなかったでしょう？\n
それ、誤魔化してくれたの、会長なのよ？」"

hide viv_m_02_6
show viv_m_02_6 at left_center
hide rose_a1_3
show rose_a1_3 at center
with dis

show rose_b2_6 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0080
Seito "「ああ、なんてお優しいビバルディ様……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本人を目の前にうっとりしている。"

hide rose_a1_3
show rose_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0100
Seito "「……え～と、本当ならば女子寮の点呼を取るのも、副寮長の仕事なんだけどね？\n
そっちはエース先輩がやったのよ」"

hide rose_b2_6
show rose_b2_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0081
Seito "「そうそう、わざわざ変身魔法で副寮長に化けてくれていたらしいわよ」"

hide rose_b2_1
show rose_b2_9 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0081_5
Seito "「……まあ、エース先輩がいなくても、使用人も生徒も誰も疑問には思わないものね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（日頃から寮にいた試しがないものね……、って）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「そ、そんなに迷惑かけちゃっていた\n
の！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ビバルディごめんなさい！\n
そしてありがとう、助かったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人の説明に、私は慌ててビバルディへと向きなおる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それで、彼女がわざわざこの時間にカフェテリアに顔を出したのだ。\n
私に昨夜のことについての申し開きをさせるためだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（迷惑をかけて……、怒っている？）"

hide viv_m_02_6
show viv_m_03_9 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice viv_g0276
Vivaldi "「……ふん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「あの……、言い訳にしか聞こえないと思うんだけど……。\n
ストームのときと違って、ブリーズの終了の合図が聞こえなかったのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「私、ブリーズって初めてで、合図がしたら帰ればいいとしか聞いていなかったものだから。\n
……ごめんなさい」"

hide viv_m_03_9
show viv_m_01_9 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice viv_g0277
Vivaldi "「……よいのじゃ、わらわはおまえに怒っているわけではない。\n
小細工をして、まんまとおまえを手に入れたあのホワイトめが憎たらしいのじゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「？\n
小細工？」"

hide rose_a1_5
show rose_a1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice man_g0101
Seito "「……イベントの終了合図は、寮のどこにいても聞こえるように魔法効果を上乗せされているの。それが聞こえないなんてこと、普通はないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_4")
T "「でも、私本当に……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嘘などついていない。\n
本当に気付かなかったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気付いたら夜もとっぷりと暮れていて、周囲も静かになっていて……。"

hide rose_a1_1
show rose_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0102
Seito "「普通は、ね。\n
でも、嘘をついているとは言っていないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……？」"

hide viv_m_01_9
show viv_m_02_6 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice viv_g0278
Vivaldi "「おおかたホワイトめに、『帰るタイミングを逃してしまったようですね、朝になってから戻ったほうがいいと思いますよ……』、なんて言われたのじゃろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……う。\n
……どうして見てきたように言うのよ」"

hide viv_m_02_6
show viv_m_01_11 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice viv_g0279
Vivaldi "「……分からいでか。\n
そんな手に引っ掛かるとは、単純すぎる……」"

hide viv_m_01_11
show viv_m_03_11 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice viv_g0280
Vivaldi "「いや、純粋というべきか……。\n
そんなところも愛いとは思うが……」"

play sound se_0442 volume .7
play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディは、サラダに入っているトマトこそが憎き敵でもあるかのように、勢いよくフォークをぶすりと突き刺した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ええっと……？」"

hide rose_b2_9
show rose_b2_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice tak_g0082
Seito "「あのね、[firstname]。\n
鈍すぎるわ」"

hide rose_b2_1
show rose_b1_9 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice tak_g0083
Seito "「それ、間違いなく小細工よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「小細工？」"

hide rose_a1_5
show rose_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice man_g0103
Seito "「ええ。\n
それ、たぶん、防音系の魔法だと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「で、でも、いくら私だって、外の音が一切聞こえなくなったら気付くわよ？\n
外の賑やかな喧騒だとかも聞こえていたもの」"

hide viv_m_03_11
show viv_m_02_11 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice viv_g0281
Vivaldi "「言ったであろう？\n
ブリーズ終了の合図は魔力の乗った音だったのだと」"

hide viv_m_02_11
show viv_m_01_13 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice viv_g0282
Vivaldi "「それだけ特徴のある音であれば、それだけを排除するのも難しくはあるまい。\n
魔力による音波の干渉を遮断すればよいのだからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（そんなこと……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……ありえるわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思えばストームの夜にも、ペーターは私の部屋の窓に防音の魔法をかけ、戦闘音だけを排除するというような器用なことをしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだけ調整が可能なら、応用だって可能なはず。\n
魔法効果の乗った音だけを排除するなんてことも、余裕だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "（ペーターの奴……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後で、シメよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……改めて迷惑をかけてごめんね、ビバルディ。\n
それに、フォローもありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜、何があったのかを、ようやくきちんと把握できた。私の知らないところで、ビバルディやエースがおおいにフォローしてくれていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（助かった……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……けど、恥ずかしい）"

hide viv_m_01_13

hide rose_a2_3

hide rose_b1_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまり、朝帰りしたこともバレバレ。\n
視線を伏せがちにしたまま、自分の分の朝食をテーブルへと呼び出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もそもそ、とトーストを口に運ぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これ以上口を開いていると、言わなくてもいいことまで言って自爆してしまいそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正面の二人はにやにやしているし、隣のビバルディは不機嫌そうにそっぽを向きつつも時折ちらちらとこちらへ視線をくれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本人が言っていたとおり、不機嫌なのはあくまでペーターに対して、なのだろう。\n
そして、彼女も年頃の女性。"


show viv_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0283
Vivaldi "「……それで。\n
うまくいったのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく続いた沈黙を破ったのは、ビバルディだった。\n
気になる、と、主張を隠さない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……手助け、してくれたのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「ええ。\n
……うまくいったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐっと親指をたてて、力強く宣言する。"

hide viv_m_03_12
show viv_m_03_12 at left
with dis

show rose_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0104
Seito "「まあ！\n
本当！？」"

hide viv_m_03_12
show viv_m_03_12 at left_center
hide rose_a1_2
show rose_a1_2 at center
with dis

show rose_b1_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0084
Seito "「よかったじゃない！」"

hide viv_m_03_12
show viv_m_01_7 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0284
Vivaldi "「……はあ。\n
物好きな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（それは……、私も思うところがあるけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言わぬが花、だ。"

hide rose_b1_3

hide rose_a1_2

hide viv_m_01_7

##[clearmessage PAY ATTENTION="false"]

scene bg_par02_ct_ros_day with Dissolve(.8)

scene bg_par15_rg_ros_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg10_sb_day
with stripe_l_long

play music school_front_day_p_wam
play sound se_0046
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業が終わって、寮に戻るべく校舎を出る。\n
そうして少し歩いたところで、いきなり傍らの繁みからにゅっと人が登場した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！？」"


show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice pet_g0257
Peter "「[firstname]！\n
こんなところで会えるなんて奇遇ですね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……ペーター？）"

play sound se_0051
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは、両腕をがばっと広げて抱きついてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逃げることはしなかったものの、違和感が残った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅうと抱き寄せられて、首筋に顔を埋められる。\n
抱きつき方にも違和感が……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（感触は同じだけど……、でも……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「こら、離れなさいって。\n
誰に見られるか分からないでしょうっ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "両思いになったとはいえ、バカップルとして名を売るつもりはない。\n
節度を持ったお付き合いを心掛けたいものだ。"

hide per_m_02_5
show per_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0258
Peter "「そんなこと言わないでくださいよっ！\n
せっかく君……、じゃなかったあなたと恋人同士になれたのに！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "また、違和感。\n
今度は、とても分かりやすく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……今、おかしかったわよね？）"

menu:
    "ペーター……、よね？":
        jump gakuen_peter_end2a
    "……エース？":
        jump gakuen_peter_end2b
label gakuen_peter_end2a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ペーター……、よね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声に出して聞いてみると、余計に違和感が強くなった。\n
むぎゅううう、と抱きしめる腕が強くなる。"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ！」"

jump gakuen_peter_end3
label gakuen_peter_end2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「…………。\n
……エース？」"

hide per_m_01_3
show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
Peter "「…………」"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むぎゅううう、と抱きしめる腕が強くなった。\n
同時に、違和感も強まる。"

jump gakuen_peter_end3
label gakuen_peter_end3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そもそも、ペーターがそんな繁みから出てくるわけがないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの筋金入りの潔癖症が、何か特別な事情でもない限りそんなことをするわけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（いや……、特別な事情があっても、しなさそうね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間近で見てきた分、どれだけ重度の潔癖症なのかは分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、今朝がたエースがペーターに化けて使用人をやり過ごした話を聞いたばかり。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（あのときは感謝したものだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「エースね？\n
そうなんでしょう？」"

hide per_m_02_8
show per_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pet_g0259
Peter "「ひ、酷いですよ、[firstname]っ！！\n
僕とペーターさんを間違えるなんてっっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "{size=+20}（『僕』も『ペーターさん』も同一人物よ）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……名前間違えているわよ」"

hide per_m_01_6
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice pet_g0260
Peter "{size=+20}「あ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこは本来、『僕とエース君』と言わなければいけないところだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "肩口に顔を埋められているせいで、顔を窺うことは出来ないが、身にまとう雰囲気で「しくじった」というのが分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「ほら！\n
バレたんだから離れなさいってば……っ！」"

play sound se_0007
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無理矢理体の間に腕をねじこんで、ペーターの姿をしたエースの体を押しやろうと試みた。"

hide per_m_02_3
show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0261
Ace "「はははっ。\n
それまるでペーターさん本人なら抱きつかれるのもやぶさかじゃない、って言ってるみたいだぜ？」"

hide per_m_02_5
show per_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0262
Ace "「恋人に成り立てだっていうのに、あっついなあ。\n
いや、成り立てだからこそなのかな……、妬けちゃうよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターの姿、ペーターの声で、中身がエース。\n
悪夢だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（色々な意味で……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "濃すぎる組み合わせだ。\n
大人しく離れた相手にほっと息はつくものの、頭痛がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「頭、痛い……」"

hide per_m_03_2
show per_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0263
Ace "「お？具合悪そうだな？\n
はは、昨夜ペーターさんに無茶なことでもされた？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_12")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……まさに、悪夢だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターの顔で、エースの性格。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「いいから元の姿に戻りなさいよっ！\n
悪趣味極まりないわよ！？」"

hide per_m_02_1
show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice pet_g0264
Ace "「あはは、楽しいなあ！\n
これ、クセになっちゃいそうだ！」"

play sound se_0346

show white onlayer master with compress_short
play sound se_0370
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "軽やかで爽やかな笑い声の途中で、ぽんっと軽い破裂音が響いて、もくもくと煙が発生する。"

hide per_m_02_5
show ace_m_02_10 at center
with dis
hide white

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その煙が風に流され、視界がクリアになると、もうそこにいるのはペーター＝ホワイトではなくエース。\n
手品のように、見事な変身だ。"


play music ace_t_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あらかじめ、エースがペーターに化けたと聞いていたからこそ見破ることが出来た。そうでなかったら、判断がつけられなかったかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……優秀なのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかくの才能も、エースに関しては無駄使いな気がしてならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「昨日はありがとう。\n
ペーターのふりで、使用人達を誤魔化してくれたって聞いたわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……でも、なんだって今また、ペーターの格好をしなきゃならないの？」"

hide ace_m_02_10
show ace_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0063
Ace "「そりゃあ、君を驚かせようと思ってさ。\n
もし君が気付かなかったら、愛が足りないな～、なんてからかおうと思っていたんだけど」"

hide ace_m_03_11
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0064
Ace "「合格だ、よく気付いたね。\n
俺、そっくりじゃなかった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「そっくりだったわよ。\n
そっくりすぎたからこそ、ちょっとでも違うのが違和感なの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あまりにも似すぎていて、本人にしか見えない。\n
だからこそ、本人と異なるちょっとした仕草が強い違和感になるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「伊達に幼馴染をやっていないわ」"

hide ace_m_03_3
show ace_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice ace_g0065
Ace "「……ちぇー。\n
君が気付かなければ、そのまま行き着くところまで行っちゃおうと思っていたのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「……{size=+20}どこによ{/size}」"

hide ace_m_02_12
show ace_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice ace_g0066
Ace "「え？だから、行き着くところまで……、どこまでだってさ。\n
俺ってロマンチストだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "{size=+20}「ちっとも」{/size} "

hide ace_m_02_1
show ace_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0067
Ace "「はは、[firstname]、君って手厳しいよね。\n
ペーターさんも大変だなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「私は普通よ。\n
ペーターも、大変じゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……むしろ、私のほうが大変よ）"

hide ace_m_03_10
show ace_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice ace_g0068
Ace "「あ、それとも厳しくされるのがいいのかな。\n
ペーターさんって、あれでなかなか……」"

hide ace_m_01_4
show ace_m_01_3 at left
with dis

show per_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pet_g0265
Peter "「{size=+20}僕がどうかしましたか？{/size}\n
ふふ、エース君がこんなところにいるなんて珍しいですねえ？」"


play music peter_t_ali
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（噂をすれば影……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "セクハラじみたことを口走るエースの背後から、ペーターがぴょこんと顔を出した。\n
いやにタイミングがいい。"

hide per_m_02_2
show per_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0266
Peter "「ここはあなたの得意とする獣道じゃあ、ありませんよ？\n
さ、森におかえりなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "市街地に迷い込んだ野性の獣に対するような台詞をのたまいつつ、しっし、と手を振ってエースを追い払おうとしている。"

hide per_m_03_9
show per_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0267
Peter "「……大丈夫ですか、[firstname]？\n
エース君に、何か変なことをされませんでしたか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「されてないわ。\n
……それにしても、タイミングいいわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースが校舎周辺にいるのも珍しいが、ペーターがこうして外にいるのも珍しい。\n
彼は放課後、赤薔薇寮内で仕事をしていることが多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外を出歩くのは最小限にとどめている節があり、書類を他寮に届けるなんていうときにも部下を使うのが常。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "汚れるのが嫌だという、いかにも彼らしい理由だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ペーターはどうしてここに？\n
もう放課後でしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「どこかで、何か問題でもあったの？」"

hide per_m_02_6
show per_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pet_g0268
Peter "「……問題といえば問題でしょうね。\n
いえ、ちょっとした怪談を耳にしまして」"

play sound se_0056
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳にする、の部分でペーターは器用にその長い耳をぴこぴこと揺らしてみせる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「怪談？\n
シンフォニアの怪談ってどんなの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこの学校にも、生徒の好奇心をくすぐる怪談話というものはつきものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん、その正体のほとんどが魔力残滓によるものや、ゴーストによるものだったりするのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中にはそうではない、理屈では解決できないような怪談も伝わっている。\n
そういったものが、シンフォニアにもあるのだろうか。"

hide ace_m_01_3
show ace_m_03_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0069
Ace "「へえ、それは興味深いなあ。\n
俺にも教えてくれよ、ペーターさん！」"

hide per_m_02_4
show per_m_03_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0269
Peter "「ふふ、そうですね。\n
君には、とっても興味深い話だと思いますよ、エース君」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人はにこやかな笑みを交わしあっている。\n
とてもとても、にこやかだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからこそ、とても怖い。\n
とても、とても、だ。"

hide per_m_03_2
show per_m_02_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0270
Peter "「はは、本当に興味深い、面白い怪談なんですよ？」"

hide per_m_02_8
show per_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0270_5
Peter "「なんていったって、{size=+20}僕のドッペルゲンガーが鼻歌交じりに学園内をうろうろしている{/size}」"

hide per_m_02_2
show per_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0270_8
Peter "「……っていうんですからね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……なるほど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースにとっては、身近な怪談だろう。"

hide ace_m_03_11
show ace_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0070
Ace "「それは大変だね、ペーターさん！\n
ドッペルゲンガーを見た人は死んじゃうらしいから、気をつけなきゃ！」"

hide per_m_01_10
show per_m_03_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0271
Peter "「ふふ、僕を心配してくれるんですか？\n
エース君は優しいですね……、{size=+20}死ね{/size}」"

play sound se_0020
$ flash(.1)

play music battle_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朗らかな狸と狐（ウサギ？）の化かしあいに終止符を打ったのはペーターだった。\n
会話の途中で右手を滑らせ、肩からかけている時計を銃に変えて発砲する。"

play sound se_0683
$ flash(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一方のエースも、すぐさま腰の大剣を抜いて応戦しているあたり、さすがだ。\n
先刻も思ったことだが、まさしく才能の無駄使い。"

play sound se_0020
$ flash(.1)
play sound se_0020
$ flash(.1)
play sound se_0020
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……そうね、ドッペルゲンガーを見た人が死んじゃうって、本当かも）"

play sound se_0686
$ flash(.2)
$ flash(.1)
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際、死人が出そうだ。\n
そんな突込みを入れられるあたり、私はこういった日常に慣れてきてしまっている。"

play sound se_0020
pause .1
play sound se_0020

show magic_r onlayer master with Dissolve(1.5) ##PAY ATTENTION="true"]
pause 1
play sound se_0726
hide magic_r with Dissolve(1.5)  ##PAY ATTENTION="true"
play sound se_0728
$ flash_color("orange_3", .2)
$ flash_color("orange_red", .2)
$ flash_color("light_orange", .2)
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間近で銃声、金属音、そして魔法が炸裂していても、あまり気にならなくなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは子供みたいな理由で喧嘩をし、子供並みの堪え性でもって魔法を発動させあっているが、魔力などは一級品。\n
シンフォニア生の中でも、とびきり優秀。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "考えなしの喧嘩に見えても、無関係の生徒を巻き込むようなことはない。\n
いつも、お互い上手に喧嘩をしている。"

play sound se_0020
show magic_b onlayer master with Dissolve(1) ##PAY ATTENTION="true"]
pause .4
play sound se_0458
pause 1
play sound se_0665
hide magic_b with dis
##[cg PAY ATTENTION="true"]
$ flash_color("pastel_blue", .2)
$ flash_color("periwinkle_blue", .3)
$ flash_color("jean_blue", .2)
pause 1
hide per_m_03_1
show per_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0272
Peter "「僕の姿をして、彼女に何をしたんです……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「そこまで深刻になるようなこと、されていないわよ」"

play sound se_0441
##special anime"kiseki03"loop="false"time="1000"]
pause .5
play sound se_0193
play sound se_0581
##[rcg PAY ATTENTION="true"]
show white onlayer master with spread
hide white onlayer master with spread_extrashort
hide ace_m_01_3
show ace_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice ace_g0071
Ace "「はは、そうだよな！\n
ただちょっと抱きしめただけで……」"

hide per_m_02_7
show per_m_01_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pet_g0273
Peter "「充分です！\n
僕の愛する人に抱きつくなんて死罪に値します！！」"

play sound se_0020
$ flash(.1)
pause .1
play sound se_0020
$ flash(.1)
pause .1
play sound se_0020
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースの挑発（？）に、ペーターの攻撃の速度があがる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（愛する人、かあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き慣れた言葉。\n
恋人になれば感慨も出るかと思ったが、あまり変わらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「やめなさいよ、ペーター。\n
エースは、あなたをからかって遊んでいるのよ」"

play sound se_0686
pause .15
play sound se_0496
show magic_g onlayer master with Dissolve(1.5) ##PAY ATTENTION="true"]
with dis
play sound se_0441
##special anime"kiseki04"loop="false"time="1000"]
pause .5
play sound se_0743
hide magic_g with dis
##[cg PAY ATTENTION="true"]
$ flash_color("light_green", .2)
$ flash_color("teal", .1)
$ flash_color("turquoise_green", .1)

pause 1
hide ace_m_03_3
show ace_m_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice ace_g0072
Ace "「遊んでなんかいないって。\n
俺は、ペーターさんと友情を確かめあっているだけだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「魔法を撃ち合ったり、弾きあったりするのが友情の確かめ方？\n
……からかって楽しんでいるくせに」"

hide ace_m_01_3
show ace_m_01_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice ace_g0073
Ace "「男は拳で友情を確かめ合うものなんだよ。\n
けして、ペーターさんの反応を面白がっているわけじゃ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……拳じゃなくて、魔法でしょ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どう見ても、楽しんでいる。"

hide per_m_01_7
show per_m_01_14 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0274
Peter "「僕と君の間に友情なんてものは存在しません」"

play sound se_0020
pause .4
play sound se_0191
$ flash(.2)
hide ace_m_01_1
show ace_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0074
Ace "「え～？恋人が喧嘩をやめてほしがっているんだから、お願いを聞いてあげれば？\n
穏便にいこうよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……エースと仲良くお友達になってほしいとも願っていないけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大体、からかっているのはエースで、真面目に応じてしまっているペーターが不憫なくらい。"

hide per_m_01_14
show per_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0275
Peter "「ああ、[firstname]、あなたが心優しい人だということは、僕だってよく分かっています！」"

hide per_m_02_6
show per_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0275_5
Peter "「ですが、この男はここでやっておかないと……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……いいの？」"

hide per_m_02_7
show per_m_03_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice pet_g0276
Peter "「何がです？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「そうやってあなた達が喧嘩していると……、また私を取り合っているなんて噂が流れるわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「すでに赤薔薇寮の女子の間では、わりとメジャーな噂なんだから」"

hide per_m_03_7
show per_m_03_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_3")
voice pet_g0277
Peter "「取り合いって……。\n
その言い方だと対等なようで、気に食わないんですが……」"

hide ace_m_03_7
show ace_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_3")
voice ace_g0075
Ace "「え、本当に？それ、面白いな！\n
君達の仲間に入れてくれるのなら、俺、当て馬でも間男でもいいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（仲間って……）"

hide per_m_03_5
show per_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice pet_g0278
Peter "{size=+20}「どんな意味であろうと、間に入ってほしくありませんね」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「……それは、同感」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「構うと喜ぶんだから。\n
エサをあげちゃ駄目よ」"

hide ace_m_02_4
show ace_m_03_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice ace_g0076
Ace "「猛獣か何かのように言わないでよ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「もっとタチの悪いものでしょう。\n
構うとろくなことがなさそう」"

hide per_m_02_7
show per_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice pet_g0279
Peter "「そうですねっ、エース君なんかにかまけていた僕が愚かでした！\n
さ、行きましょう！」"

play sound se_0580
play sound se_0584
hide ace_m_03_1

hide per_m_01_12

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは、ひょいと私の手をとるとそのまま歩き出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手を引かれるままに何歩か進んだところで、気紛れのように足を止めて、エースを振り返った。"




show per_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0280
Peter "「しかし、たとえ相手が君であろうと、恩を受けたからには礼を言っておくべきでしょう」"

hide per_m_02_11
show per_m_02_11 at left
with dis

show ace_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0077
Ace "「？\n
なんだなんだ？」"

hide per_m_02_11
show per_m_03_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0281
Peter "「昨夜は、僕の代わりに仕事をしてくれてありがとうございました。\n
……まあ、普段何もしていないんですから、あれぐらい当然なんですけどね」"

hide ace_m_03_9
show ace_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0078
Ace "「どういたしまして。\n
はは、友達なんだから当然だよね」"

hide per_m_03_9
show per_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
##voice pet_g0282
Peter "「そっちは、当然ながら否定させてもらいます」"

hide per_m_02_4

hide ace_m_02_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐいと手を引かれて、再び歩き始める。\n
その背に向かって呼び止めたのは、今度はエースのほうだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0079
Ace "「ちょっと待ってよ、二人とも」"

play sound se_0415
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たったったっと小走りに私達へと追いついて、エースはちょうど私達二人の間に頭をねじ込むようにして囁いた。"



show ace_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0080
Ace "「校舎裏に森があるの知っているだろ？\n
あそこの奥に、いい感じの花畑があるんだ」"

hide ace_m_01_10
show ace_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0081
Ace "「俺、前に冒険の途中で見つけたんだよなー。\n
とても綺麗な場所だから、二人で見に行くといいよ」"

hide ace_m_01_1
show ace_m_01_1 at left
with dis

show per_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0283
Peter "「は？\n
……なんです、唐突に」"

hide ace_m_01_1
show ace_m_03_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0082
Ace "「……あそこなら誰も来ないから、二人きりになれるよ、ペーターさん」"

hide per_m_01_4
show per_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0284
Peter "「……何を企んでいるんです」"

hide ace_m_03_10
show ace_m_02_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0083
Ace "「え？親切心だよ、親切心。\n
恋のキューピッドだしね、俺」"

hide per_m_02_7
show per_m_01_14 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「…………」"

hide per_m_01_14
show per_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0285
Peter "「……助けてもらったのは事実かもしれませんが、あなたがキューピッドとか、鳥肌がたつんですけど」"

hide ace_m_02_1
show ace_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0084
Ace "「ウサギなのに、鳥肌かあ……、はは。\n
さて、俺もそろそろ寮を目指して、壮大な冒険に出かけるぜ！」"

play sound se_0748
hide per_m_01_11
show per_m_01_11 at center
with dis
hide ace_m_03_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言いたいことだけ言うと、エースは手を大きくぶんぶん振って、再び繁みの中へと去っていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "壮大な冒険、というあたり、最初からまともに寮を目指すつもりはないらしい。"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……行ってみる？」"

hide per_m_01_11
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pet_g0286
Peter "「え？その、花畑に？\n
あなたが行きたいのなら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_1")
T "「……せっかくエースが教えてくれたんだもの。\n
行ってみましょうか」"

hide per_m_02_3
show per_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_1")
voice pet_g0287
Peter "「その、エース君が教えてくれたというところが引っ掛かるんですけどね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（でも……、二人きりに、なれる場所）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮生などやっていると、そういう場所は珍しい。\n
イベント時はともかく、落ち着いて二人で過ごせるというのは貴重だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……ペーターと一緒で、落ち着けることなんか、そうそうないけど）"

hide per_m_03_5
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg10_sb_day with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg13_fr_day
with stripe_l_medium

play music forest_thick_day_p_wam
play sound se_0625
play sound se_0623
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校舎裏の森に向かったのはよかったのだが……、エースの紹介など信じるべきではなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（迷子の道案内……。\n
信じるほうが馬鹿よね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とペーターが森の中へと足を踏み入れてから、もうすでに２０分近くが経過しようとしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "森の土は柔らかく、空気はひんやりと湿っぽい。\n
外との空気の質の差が新鮮だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "森歩き自体はいいのだが、さすがに目的地に不安を持ったまま歩き続けるというのは辛い。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「森の奥って、どれくらい奥なのかしら……。\n
エースみたいに方向音痴じゃないけど、帰れるかどうか心配になるわ」"


show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pet_g0288
Peter "「大丈夫ですよ。\n
帰るときには箒に乗ってしまえばあっという間です」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「そうね、上空からなら一発だわ。\n
……花畑もその手で見つけられないかしら」"

hide per_m_02_8
show per_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice pet_g0289
Peter "「さて、どうでしょうね……。\n
試してみますか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターの視線が宙を彷徨って、私もそれにあわせて視線を上空へとやる。\n
うっそうと茂った枝葉が、まるで天井のようになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かきわけて上空に出るのは無理ではないだろうが、校舎を目指すならばまだしも森の中の花畑を探すという意味では無理がありそうだ。"

hide per_m_03_7
show per_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0290
Peter "「その花畑とやらが、開けた場所にあるのでしたら簡単にすむんですが……。\n
……もう少し、歩いてみましょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そうね、まだ平気よ。\n
疲れたわけじゃないもの」"

hide per_m_02_10
show per_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0291
Peter "「疲れたならばすぐに言ってくださいね？\n
抱きかかえて運びますから！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……遠慮しておくわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを言いつつも、ペーターはすでに充分私を気遣って森の中を散策してくれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "歩きやすい場所を選び、危険がないかを常に先に確かめてから私の手を引く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（こうしていると、紳士的に見えるなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋人として付き合い始めたからといって、ペーターが別人になったわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幼馴染で、ストーカーみたいなところもある、彼のまま。\n
中身は変わらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（変わらないのに……、なんだか緊張する）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "甘酸っぱいような、これが恋人同士の感覚なのかと思うと嬉しいような。\n
だが、寂しいような気もする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

hide per_m_02_1
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どれくらい二人で森の中を歩いただろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうなったら花畑ではなく、森の散策が目的でも構わないと思い始めた頃、急に視界が開けた。"


play music night_garden_p_ali

scene bg08_fl_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……わあ！」"

##[rchara1 PAY ATTENTION="false"]
show per_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice pet_g0292
Peter "「これは……、見事ですね……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "森の中の開けた空間、そこだけ日差しが差し込んでいる。\n
その日の光をきらきらと反射するように、一面に白い花が咲き誇っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースが勧めるだけあって、見事な光景だ。\n
迷っていたことなど、吹き飛んでしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_2")
T "「綺麗……！\n
行きましょうっ」"

hide per_m_01_3

play sound se_0619
play sound se_0621
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深く暗い森の中に囲まれた、幻想的な花畑。\n
彼の手を引いて、小走りに森を抜ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……やっと到着ね」"


show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice pet_g0293
Peter "「ええ。\n
本当にあるのかと思いましたが……」"

##[rcg PAY ATTENTION="true"]
show m_per_end1 onlayer master
with dis
hide per_m_02_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "花を踏まないように気をつけながら足を踏み入れ、適当な位置にふわりとスカートを翻して腰掛けた。\n
隣にペーターも座る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「ふふ、いいところを教えてもらったわ。\n
……迷子になるっていうのも、たまにはいいことに結びつくのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice pet_g0294
Peter "「そうですね、今回ばかりは……。\n
……常習はごめんですけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人視線を交わして、微笑みあう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "穏やかな場所だ。\n
森の中を歩いてきて汗ばんだ体に、花畑を抜ける風が涼しくて気持ちいい。"

play sound se_0785
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふわりっとその風にあおられて、懐かしい草の匂いがした。\n
甘いような、青臭いような、そんな独特の匂いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ねえ、ペーター。\n
秘密基地のこと、覚えている？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pet_g0295
Peter "「もちろん覚えていますよ。\n
僕とあなたの愛の巣です」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……実際、巣穴っぽかったけども」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背の高い草の中。\n
天井を結んだり床に敷きこんだりと一生懸命作ったつもりの秘密基地だったが、実際は動物の巣程度のものだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0296
Peter "「懐かしいですね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと隣を見上げると、ペーターは共に遊んだ思い出を懐かしむように、その双眸を細めていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやって目を細くすることで、見えにくい遠くにあるものを見ようとしているかのようだ。\n
遠くを見るときの目つきに似ている。"


play music recollection_wam
hide m_per_end1
show m_per_end2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「…………。\n
……ごめんね、ペーター」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice pet_g0297
Peter "「何がです？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽつりと溢した言葉に、彼は訝しげに眉を寄せる。\n
思い当たる節がないといった顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「秘密基地。\n
私、守れなかったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターがシンフォニアに進学して、私は秘密基地のことを忘れた。\n
苦い初恋の記憶と一緒に、秘密基地のこともうやむやにしてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……だから、あまり帰ってこなくなっちゃったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼がそれで怒って帰ってこなくなった、というわけではないのを知っている。\n
ただ、足は遠のいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帰ってきたときには変わらずに、私に構いたがったし、構われたがった。\n
ストーカーなんて呼びつつ、変わらないことに安堵したのも事実。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（私……、変わってほしくなかったのかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "関係を変えたいと動いて、私達は恋人になった。\n
だが、緊張感を、気恥ずかしくも煩わしく思ってもいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（距離っていうのは、きっかけがあれば簡単に出来てしまうから）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターが、あまり実家に戻らなくなったのも突然だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校の方針として、寮滞在が定められているものの、長期休暇の帰省は禁じられていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帰ろうと思えば、帰れる。\n
たまに帰るので、詰問するほどでもなく、距離はあいていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（ちょっとした、きっかけで）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「秘密基地のことがきっかけになって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0298
Peter "「あれは、仕方がなかった。\n
もちろん、あなたのせいではありません」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0299
Peter "「僕の土地でも、あなたの土地でもなかったわけですからね。\n
壊されるのを止めようがない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「でも、きっかけにはなったでしょう？\n
あれをきっかけに、ますます戻ってこなくなったんだし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
voice pet_g0300
Peter "「……そうですね。\n
なくなってしまった秘密基地を見て……、僕は怖くなったんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「怖い？\n
あなたが？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice pet_g0301
Peter "「ええ。\n
自分から離れたくせに……、離れきるのも嫌で」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅっと繋いでいた手はそのまま握ったまま、ペーターがぽつぽつと語る。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0302
Peter "「あなたの周囲から、僕がいた証が消えていくのが怖かったんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0302_5
Peter "「思い出がなくなっていくことを確認するのが怖くて……、僕はシンフォニアに残るようになりました」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0303
Peter "「……いえ、まあ、実際会長の溜め込んだ仕事を処理する、という名目もあったんですけどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0303_5
Peter "「それでも無理をすれば、帰れないっていうほどの強制力はなかったんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（知っているわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こう見えて、ペーターは頑固だ。\n
そうと決めたら、それを何がなんでも譲らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは私にもいえること。\n
私達は意外と似ているところのある幼馴染だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0304
Peter "「次に帰って、あなたに特別な誰かが出来ていたらどうしよう、と考えたら怖かったんですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0304_5
Peter "「あなたのことを好きだと囁く誰かがいたらと思うと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、頑固な割に、えらく弱気。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0305
Peter "「……[firstname]。\n
僕がシンフォニアに入学したのは、あなたに好きな相手が出来ることが怖かったからです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0306
Peter "「あのとき……、二人だけの秘密基地で、あなたは他の誰かを想って傷ついていた」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0306_5
Peter "「僕は、どんなに傍にいても、けして僕ではその対象になりえないと思ったんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0307
Peter "「傷ついたあなたを慰めたくて……、でも、それすらも満足に出来なかった。\n
こんな僕では、いずれ、あなたに想い合う相手が出来るのを耐え切れない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0308
Peter "「シンフォニアは、僕にとって体裁のいい逃げ場になったんです。\n
幸い僕には魔法に関する才能がありましたから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「……秘密基地を、別に作ったってこと？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice pet_g0309
Peter "「ええ、秘密基地……、そういうことですね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice pet_g0310
Peter "「でも、二人の秘密基地も大事でした。\n
あそこが壊されて……、僕はもっと怖くなりました」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「怖いのに……、離れてどうするのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice pet_g0311
Peter "「ですから……、あなたに特別な誰かができるのが怖くて」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「でも、二人の場所が壊されるのも怖かったんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice pet_g0312
Peter "「そう……、怖いんです。\n
離れるのも、壊れるのも、どちらも怖かった」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice pet_g0313
Peter "「僕は……、あなたのことが、何より怖い。\n
あなたのことが……、好きだから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おずおずと、ペーターが繋いだままだった私の手を引く。\n
その動作に導かれて、彼へと向き直った。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0314
Peter "「あなたが好きで……、会いたくて。\n
でも、会うことを避けるほど怖くもあるんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……分かるわ、その気持ち）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠い昔の、駄目になってしまった初恋を思い出す。\n
告げる前に玉砕した想いですら、遠まわしの否定にあんなにも傷ついた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（好きな人が、一番怖い）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（……なんだ。\n
私と同じ、「好き」じゃない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の思う恋とは違う。\n
そう思っていたが、細かく見てみるとそうでもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、私達は似ているところもある幼馴染だった。\n
いや、幼馴染だからこそ、共通点も多くなるのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「でも、どうして今になって、私をシンフォニアに誘ってくれたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は先生が姉のことを好きだと知って傷つき、彼を諦め、姉から距離をとろうとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは私が彼の手の届かぬ範囲で悲しむことがもどかしく、また立ち直って他に好きな相手を見るのも恐ろしく、距離を置いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0315
Peter "「離れるのも壊れるのも……、怖い。\n
ですけど、それらを見ずにすんだとしても、忘れられるのが一番怖い」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice pet_g0316
Peter "「……まあ、こう思えるようになったのも、時間をあけたからかもしれませんけどね。\n
ウサギって、怖がりな生き物なんですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（……ペーター）"

hide m_per_end2
show m_per_end3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「あなた……、{size=+20}ストーカー行為の裏で、色々考えていたのね{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pet_g0317
Peter "「……え。\n
まあ、それはもう、色々と」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_11")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0318
Peter "「……すみません、あなたを追い掛け回すときは興奮しちゃって、あまり何も考えていませんでした」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……だよね。\n
正直でよろしい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのノリで、深い考えなどあったら、それこそ怖すぎるという話だ。"

hide m_per_end3
show m_per_end4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ねえ……。\n
今でも、私のことが怖い？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pet_g0319
Peter "「もちろんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「私は、あなたの恋人なのに？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周りに人がいないせいだろうか。\n
恋人という言葉も、するりと口にすることができた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0320
Peter "「それでも、ですよ。\n
あなたの気持ちを疑うわけじゃないんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0321
Peter "「でも、あなたはとても魅力的な人ですから……。エース君だって、会長だって、あなたのことが好きで狙っているに違いありません」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……あの二人の愛情は、おもちゃやぬいぐるみに対する執着のようなものよ。\n
もちろん、大事にしてもらっているとは思っているけれど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋情ではない……、と思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "可愛がって気にかけてくれてはいるけれども、それはきっとペーターが私に対して抱いている想いや、私がペーターに対して抱いているものとは違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0322
Peter "「そうかもしれませんけど……、まだ見ぬ敵だとしても怖いんです。\n
あなたが盗られてしまうかもしれない……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0323
Peter "「恋人なのに、いいえ、恋人だから余計に怖いです。\n
……欲張りになるから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅ、とペーターが私の手を握る。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0324
Peter "「ふふ、なんだかおかしな気分です。\n
今まで僕は、手袋をしているのが当然でした」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0325
Peter "「それなのに、今はあなたに直接触れられないのが歯がゆいんです。\n
こんな薄い布が、邪魔に感じてしまいます」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "穏やかな、薄い布越しの体温だ。\n
今は、私も物足りない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「いいの？\n
雑菌が移っちゃうわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0326
Peter "「……あなたの雑菌なら、喜んで」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「そういうことを言うから、怖いのよ、あんたは」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice pet_g0327
Peter "「え？\n
あなたも僕が怖いんですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……違う意味でね」"

play sound se_0551

play music starlit_sky_a_wam
hide m_per_end4
show m_per_end5and8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "繋いだのとは逆の手をついて、ペーターが身を乗り出した。\n
綺麗な整った顔立ちが、ゆっくりと近づいてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当なら、外でこんなことをするつもりはなかった。\n
ペーターに化けたエースと違い、私は節度というものを理解している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲からひんしゅくをかうような愚かなカップルにはなりたくない。\n
と、思っていたのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（誰もいないから、いいわよね）"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "節度も何もありはしない。\n
自分からもペーターのほうへと身を乗り出して顔を寄せる。"

hide m_per_end5and8
show m_per_end6and9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちゅ、と小さな音とともに唇が触れ合った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この一度の接触で、どれだけの雑菌が互いの間を移動したのか、なんて。\n
頭の隅で考えてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私まで、ペーターの潔癖症に毒されている。\n
口に出せばロマンの欠片もなくなる言葉も、なんだか秘密の共有のようで楽しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……ん」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_9")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一度浮いた唇が、再び押し付けられて二回目のキスをした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……ね、ペーター」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pet_g0328
Peter "「……ん。\n
なんです？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "吐息の触れ合う距離で、囁くように言葉を交わす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別に誰に聞かれているわけでもないのに声を潜めるのは、これが秘密の悪巧みだからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「二人だけの、秘密基地を作らない？\n
今度は昔作ったのよりも、もっとちゃんとした秘密基地を」"

hide m_per_end6and9
show m_per_end7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
Peter "「……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の提案に、彼は小さく目を瞠る。\n
それから、笑みに双眸を細くして頷いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……これも、昔とは違う）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前のペーターは、秘密基地を作ることに乗り気ではなかった。\n
潔癖症で、外で遊ぶこと自体が好きではなかったのだから当然だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「ふふ。\n
昔は、私が提案したら、嫌がったくせに」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice pet_g0329
Peter "「今は僕も、秘密基地の必要性を重々に感じていますから。\n
……あなたと、二人きりになれる場所がほしいんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの寮は、基本的に男女間の寮の移動が禁止されている。\n
ストームやブリーズというイベントは、特別なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男女が共同で使える空間は大抵が公用の場所で、開かれすぎている。\n
二人で過ごすには向いていない。"

hide m_per_end7
show m_per_end5and8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「……エースみたいに、キャンプ用品をどこかに隠しちゃいましょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_6")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……何？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0330
Peter "「いえ、いい案だとは思うんですが……。\n
……エース君が潜り込んできそうじゃありません？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……ああ。\n
あの人、迷子とかいうけど、絶妙のタイミングで絶妙の場所から出てくるものね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いいところ、あるいは悪いところで狙いすましたように現れる。空気を読まないのだか、読みすぎているのだか分からないが、そういう性質の男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……一番の目標は、エースに見つからない秘密基地にすることね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0331
Peter "「エース君を殺したほうが早い気が……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「無理無理、あの人って絶対に生き汚いもの。\n
ペーターは、ずっとエースと遊ぶことになっちゃうわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなことをぽんぽん言えてしまうのも、彼らの日常を知っているから。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らときたら、死ぬか生きるかの喧嘩を平気でやらかす。\n
見ている者がひやりとするような魔法を、日常的に放つのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースを殺そうと追いかけまわすペーター、笑いながら応じるエース、そして置いていかれる私……。\n
そうなってしまえば、私は蚊帳の外。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0332
Peter "「エース君とずっと遊ぶなんていうのは勘弁願いたいですね。\n
でも、それじゃあ、どうしましょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0333
Peter "「……秘密基地って、難しいですね。\n
誰にも知られない場所というのは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「そうね……。\n
そういう魔法をかけないと駄目かも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "特定の人間でなければ入れない魔法。\n
鍵の魔法の応用だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0334
Peter "「しかし、ここはシンフォニアですから……。優秀な魔法の使い手が多いので、生半可なものだと破られてしまう可能性も高いです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0335
Peter "「……研究してみます。\n
難しそうですが、取り組み甲斐があるので」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「それも、時間がかかりそうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、焦らなくても、時間は穏やかに流れている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "木々の合間の、雲の流れ。\n
同じように、ゆったりと。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（時間が……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "止まればいい。\n
だが、止まるように動くものが愛しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここでは、流れていく。\n
変わらず、変わっていく。"

hide m_per_end5and8
show m_per_end6and9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0336
Peter "「では。\n
とりあえず、今は、ここを仮の基地ということにしておいて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふ、と吐息が笑って、キスを仕掛ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（今、この時間が秘密基地みたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "隠れるような、時の隙間。"

hide frame_par_togaki
hide ali_m_06_16
with Dissolve(2)
hide m_per_end6and9
show white onlayer master
with compress_extralong
scene black with compress_extraextralong
pause 1
stop music

##endmemory
jump gakuen_a
