label gakuen_elliot_end:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_hat_day
with dis

play music morning_a_wam

scene bg24_rj_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの次の日の朝を、私は非常に清々しい気持ちで迎えていた。\n
追い掛け回して捕まえたというような、鬱憤を晴らせた感がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……実際には、どっちが捕まったのか分からないような感じだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手は、本物のウサギさんではないのだ。\n
一晩おとなしくしてくれるような、温厚な小動物でもなくて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、朝方、朝靄に乗じるようにして自室へと帰った。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……点呼とか、大丈夫だったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前ストームの夜に、エリオットは点呼をしなくてはいけないと言って寮へと戻ろうとしていたのを覚えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの夜にも点呼があったとしたら、間違いなく私はアウトだ。\n
何か罰則があるかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……うう。\n
疲れているときにはキツイなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつメイドや使用人に呼び止められてもおかしくないと思っているせいか、どことなくびくびくしてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "警戒しつつも、朝食をとるためにカフェテリアへと向かった。"

with dis
$ hi_mes()

scene bg_par15_rg_hat_day
with stripe_l_medium

play music dining_day_p_wam

scene bg_par02_ct_hat_day
with stripe_l_long
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0010
Seito "「おまえ、昨日、部屋に女子来た？」"

play sound se_0757
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0016
Seito "「来た来た。\n
おまえのとこにも来た？」"

play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0011
Seito "「当たり前だろ！\n
ストームのときに、ちゃんと戦利品とってきてあったからな」"

play sound se_0559
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0017
Seito "「だよな。\n
ああでも、隣のクラスのあいつが……」"

play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0010
Seito "「昨夜、私、三回も使用人に見つかったんだけど……」"

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0084
Seito "「ええ？\n
それ、見つかりすぎよ」"

play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0011
Seito "「最後のあたり、使用人に、見ないふりされてた……」"

play sound se_0541
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

play sound se_0688
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0012
Seito "「有難いんだけど、切ないっていうか……、哀れっていうか……」"

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0085
Seito "「そこで見て見ぬふりを選択した使用人のほうも哀れよね……」"

play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0086
Seito "「…………。\n
……姿隠しの術、もっと真面目に練習したら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0013
Seito "「……そうするわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あちこちから、ブリーズの話題が聞こえてくる。\n
なんとなしに聞きながら、適当に空いた席を探す……、と。"


show boy_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0017
Seito "「はは。\n
だから、そいつさ～」"


show boy_b1_3 at center
with dis
hide boy_a2_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0025
Seito "「嘘だろ～？」"

play sound se_0103
hide boy_b1_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "話に夢中になっていた男子生徒と、すれ違いざまに軽く肩がぶつかってしまった。"


play music library_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あ。\n
ごめんなさい」"


show boy_a2_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice kaz_g0018
Seito "「あ。\n
こっちこそ、ごめん」"

hide boy_a2_1
show boy_a2_1 at left
with dis

show boy_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice suz_g0026
Seito "「お、おい……！」"

play sound se_0559

show gaaan1 onlayer master with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……ん？）"

play sound se_0757
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぶつかったといっても、肩が軽く接触した程度のことだ。"

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お互い軽い謝罪を交わして行き過ぎる……、と思ったのに、何故だか彼らは顔色を変えて足を止めてしまった。"

play sound se_0561
hide gaaan1
show gaaan2 onlayer master with Dissolve(1.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その顔色がどんどん青ざめていく。\n
そして、その顔色と比例して周囲のどよめきも大きくなっていく。"

play sound se_0561
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（え？なに？\n
朝帰りが、ばれているの？）"

hide boy_a2_1

hide boy_b1_4

play sound se_0617
hide gaaan2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "でも、それならばこうして生徒が騒ぐ前に、メイドさんあたりに呼び出しをくらいそうな気がする。大体、そういった場合、生徒同士の結束は固い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうも、事情が違うようだ。\n
周囲の視線は校則破りを見る目というよりも……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（何か、恐ろしいものを見る目のような気がする）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰か事情を教えてくれそうな人はいないか、と視線をうろうろとさせる。"


show huryou_d1_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Furyou "「…………」"

hide huryou_d1_11
show huryou_d2_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふいっと露骨に視線をそらす、見覚えのある男子生徒がいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「…………」"

hide huryou_d2_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はつかつかつか、と彼の元へと歩み寄る。\n
まさか、昨日の仕返しにあることないこと言ってまわったりしたのだろうか。"


show boy_c2_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0015
Seito "「あ、ここ、どうぞ……！！」"

hide boy_c2_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の隣には、別の男子生徒が座っていたものの、私が近づくと逃げるように去っていってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲へと視線をやる。\n
ざっとその場にいた全員が私と目が合わないように視線を伏せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "{size=+20}（なにごとなの？）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この反応は異常すぎる。\n
私は隣の彼の制服の裾をくいくいと引いて、こそこそと小声で聞く。"


show huryou_d2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0042
Furyou "「っ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「あんた、何言ったのよ……！\n
何なのよ、この反応は！」"

hide huryou_d2_2
show huryou_d1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_13")
voice oto_g0043
Furyou "「俺じゃねえよ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「え……。\n
あんたじゃないの？」"

hide huryou_d1_9
show huryou_d1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice oto_g0044
Furyou "「俺じゃねえ！\n
……自業自得だろ、あんたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「私の？」"

hide huryou_d1_9
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice oto_g0045
Furyou "「あんた以外の誰がいるんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「身に覚えが……。\n
……ねえ、あんた、事情を把握してるの？」"

hide huryou_d1_2
show huryou_d2_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice oto_g0046
Furyou "「まあ、一応」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「聞かせなさいよ」"

play sound se_0184
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は譲ってもらった彼の隣の椅子へと座る。\n
彼は、分かりやすい反応で、嫌そうに身を退いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「何よ。\n
私は、もう怒っていないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「それとも、あなたが怒っているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仕返しはした。\n
もうそれに関しては根に持っていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "出来れば、互いに……といきたいところだ。"

hide huryou_d2_6
show huryou_d2_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0047
Furyou "「や、そうじゃなくて……。\n
今のあんたといるといろいろマズイっていうか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「だから、それがどういうことかって聞いているのよ」"

hide huryou_d2_7
show huryou_d1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice oto_g0048
Furyou "「あんた……。\n
昨日、自分が何やったか覚えているだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「ええ、当たり前よ。\n
昨日のことだもの、覚えていないほうが問題だわ」"

hide huryou_d1_7
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice oto_g0049
Furyou "「……見られていたんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の言葉に、ぴしっと硬直した。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（いやいや……。\n
覚悟の上だったでしょうに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怯むことはない。\n
その程度は覚悟していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "覚悟していなければ、皆が外をうろうろしていると分かっているブリーズの夜に、窓ガラスをぶち割って襲撃なんてことは考えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……な、何よ。\n
窓ガラス割ったぐらいで、こんなに怖がられなきゃいけないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは不良も多いという、ならず者が集う帽子屋寮ではないのか。\n
双子やエリオットなんて、校舎破壊の常習犯だ。"

hide huryou_d1_2
show huryou_d1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0050
Furyou "「ガラスを割るなんて、たいした問題じゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……それもそれでどうかと」"

hide huryou_d1_7
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice oto_g0051
Furyou "「その後だよ、その後」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……その後？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ガラスの件以外で、特に周囲に怖がられるようなことをした覚えは……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「やっぱり、身に覚えがないんだけど」"

hide huryou_d1_2
show huryou_d2_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice oto_g0052
Furyou "「あんたさ、エリオット副寮長を土下座させたことになっているんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "{size=+20}「ど！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思いっきり噴いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝食をまだ準備していなくてよかった。\n
口の中に何か入っていたら、今頃大惨事だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「土下座！？\n
私が！？エリオットを！！？」"

hide huryou_d2_9
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice oto_g0053
Furyou "「しいいいいい！\n
大声出すなって、余計に目立つだろうが！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「だ、だって……！！」"

hide huryou_d1_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は慌てて口を押さえて、周囲を見やる。"


show boy_c1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0016
Seito "「……っ！」"

hide boy_c1_4
show boy_c1_4 at left
with dis

show girl_d2_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0140
Seito "「そ、それでさー」"

hide boy_c1_4
show boy_c1_4 at left_center
hide girl_d2_4
show girl_d2_4 at center
with dis

show girl_e1_4 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0115
Seito "「あ、あれがああでああなのよね～」"

hide girl_d2_4
show girl_d1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0141
Seito "「うん、あれがあれであれなんでしょ～。\n
そうよね、あれよね～」"

hide boy_c1_4
show boy_c2_4 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0017
Seito "「そうそう、ああなるとこうなって～」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "限りなくわざとらしく、見てませんよ聞いていませんよ～とアピールをされてしまった。"


show huryou_d1_2 at center
with dis
hide girl_d1_4

hide girl_e1_4

hide boy_c2_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0054
Furyou "「……皆、外から興味津々で見てたんだよ。\n
あんたが窓ガラス割ったりするから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「あ、あんたが先にやったんじゃない……！」"

hide huryou_d1_2
show huryou_d1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
voice oto_g0055
Furyou "「俺は窓ガラス割って逃げたけど、あんたは窓ガラス割ってから襲撃しただろうが……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……そ、そう言われたらそんな事実もあったかもしれないわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の場合、窓ガラスを割る音で野次馬が集まる頃にはもうすべてが終わっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の場合、窓ガラスを割る音で周囲の注意を集めたあげくに、あんなことをしてしまっていたのだ。"

hide huryou_d1_5
show huryou_d2_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0056
Furyou "「その上、寮長と副寮長が駆けつけたんだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そりゃあ、見る。\n
私でも見に行くかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……うわあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呻いてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓ガラスを割って男子寮に乗り込み、副寮長に土下座をさせた女。\n
それは確かに恐れられても仕方がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（あの流れって、外から見ていると、そんなふうに見えていたのね……）"

hide huryou_d2_7
show huryou_d2_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice oto_g0057
Furyou "「……それだけじゃないぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「な、何よ。\n
それ以上は、何もなかったでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「誤解だって話せば、なんとか……」"

hide huryou_d2_6
show huryou_d1_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice oto_g0058
Furyou "「あの後、寮長はよろよろしながら立ち去っただろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「ええ、精神的ダメージを負っていたみたいで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……でも、ブラッドがふらふらしてるなんていつものことでしょう。\n
日中のブラッドなんて常にふらふらよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさか私がブラッドまで倒したことになっているのだろうか、と嫌な予感がよぎる。"

hide huryou_d1_6
show huryou_d1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0059
Furyou "「ふらふらで……。\n
それなのに、昨夜は寮長が点呼とったんだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「…………」"

hide huryou_d1_1
show huryou_d1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice oto_g0060
Furyou "「窓ガラスの件を使用人に説明したのも寮長だし……。\n
……あんた、昨日、部屋に戻らなかっただろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔が赤らんでしまいそうになるのを、誤魔化すように深呼吸する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幸いにしてというか、彼はそっちには興味を示さない。\n
あえて、気にしないようにしているのかもしれないが。"

hide huryou_d1_7
show huryou_d1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0061
Furyou "「あんたの不在を誤魔化したのも、寮長なんだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、怒られずにすんだのはブラッドのおかげらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（後でお礼を言わなくちゃ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……つ、つまり？」"

hide huryou_d1_9
show huryou_d2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice oto_g0062
Furyou "「あんたは副寮長に土下座をさせ……、寮長をあごで使っている」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_4")
T "「な、なんという……。\n
誤解……、誤解だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誤解だ。\n
誤解以外の何物でもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろいろな偶然が重なり合った結果として、そんなふうに見えただけ。\n
いや、どうしてそんなふうに見えるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「わ、私、そんな乱暴者に見えるの！？」"

hide huryou_d2_5
show huryou_d2_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice oto_g0063
Furyou "「……俺にはそう見えるけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞いた相手が悪かった。\n
そりゃあ、そうだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ブラッドがいろいろと手を貸してくれたのはブラッドの気紛れで、エリオットが頭を下げたのは私に向けてではなくブラッドに対してだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は無実。\n
何もしていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……ガラス割り以外は）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのときのインパクトが問題なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「あ、あんたは誤解だって分かっているでしょ！？\n
誤解、解いてよ！」"

hide huryou_d2_11
show huryou_d1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice oto_g0064
Furyou "「……誤解、か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「は？\n
あんた、当事者なんだから知っているでしょう」"

hide huryou_d1_1
show huryou_d1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice oto_g0065
Furyou "「や、だからさ。\n
エリオット副寮長はあんたのために頭下げて、ブラッド寮長もあんたのために手を貸したわけだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……それは事実だけど」"

hide huryou_d1_5
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice oto_g0066
Furyou "「事実、だろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなくくりはずるい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「それは、でも……！！」"

hide huryou_d1_2
show huryou_d1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice oto_g0067
Furyou "「だから、静かにしろって……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……っ！」"

hide huryou_d1_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "はし、と口を押さえて周囲を見る。"


show boy_c2_4 at center
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0018
Seito "「……きょ、今日は天気がいいなー」"

hide boy_c2_4
show boy_c2_4 at left
with dis

show girl_d2_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0142
Seito "「今日のお昼ごはんなにかしらっ」"

hide boy_c2_4
show boy_c2_4 at left_center

show girl_d2_4 at center
with dis
hide girl_d2_4
show girl_e2_4 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0116
Seito "「次の授業、エベルハイド博士の論理で～……」"

hide boy_c2_4
show girl_d2_4 at left_center
hide girl_d2_4
show girl_e2_4 at center
with dis
hide girl_e2_4
show boy_c2_4 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0019
Seito "「あれがそれでこれがそれで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話が噛み合っていない。\n
明らかに、周囲も動揺している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、私も動揺している。\n
肯定してしまったことになるのだろうか。"

hide boy_c2_4

hide girl_e2_4

hide girl_d2_4

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（誤解よ！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうして、そんな恐ろしいまでの誤解をされねばならないのか。無駄と知りつつも、これ以上なるべく目立たないようにこそこそと朝食をすませた。"

with dis
$ hi_mes()

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg10_sb_day
with stripe_l_medium

play music gag2_a_ali

scene bg27_rk_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "噂を打ち消すのは、流すのよりはるかに困難。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "半ば味のしなくなった朝食をとった後、ふらふらと教室へと向かう。\n
日中のブラッド以上のふらふら具合だ。"

play sound se_0586

scene bg01_cr_day with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「！？」"

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつものように扉を開けて、教室に入ったとたん、わっと群がってきたクラスメイト達に囲まれてしまった。"

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「え！？\n
何！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「何なの！？」"


show bor_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice bor_g0019
Boris "「ねえねえ、[firstname]、あんた帽子屋寮の暫定トップにのし上がったってマジ！？\n
超格好いいんだけど！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「暫定トップ！？」"


show pia_m_01_6 at center
with dis
hide bor_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice pie_g0006
Pierce "「すごいね！すごいよ！\n
君ってすごい子だったんだね！」"


show girl_a1_2 at center
with dis
hide pia_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice mat_g0026
Seito "「どうやったの！？\n
何それ！何があったの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだそれは、と、聞きたいのは私だ。"


show boy_a2_2 at center
with dis
hide girl_a1_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0020
Seito "「なんだか今、帽子屋寮全体が騒然としてるって聞いたぜ！\n
あんたのせいらしいじゃないか？」"


show girl_b1_2 at center
with dis
hide boy_a2_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0020
Seito "「それ本当よ！\n
もう皆、朝からそわそわして大変だったんだから！」"


show boy_b2_2 at center
with dis
hide girl_b1_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0027
Seito "「彼女にぶつかった男子生徒が涙目になっててさ～」"

hide boy_b2_2

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆が口々に囃したり、さらなる情報を求めたり、話を大きくしたりしている。"

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とんでもない混乱だ。\n
そして、誤解。"

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せめて、クラスメイトの誤解くらいは解かなくては。\n
すーっと深呼吸をする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「違うわよ！\n
誤解だわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大声でわいわいと騒いでいるクラスメイト達を一喝した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「いい！？\n
それは勘違いよ！！」"


show boy_a1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice oni_g0021
Seito "「いや、勘違いも何も事情を知らないから聞いているんであって……」"

hide boy_a1_1

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「私は帽子屋寮に君臨もしてないし！！\n
暫定トップになんかなったつもりもないわ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教室の入り口近くにて、仁王立ちで宣言する。"


show boy_b2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0028
Seito "「……すごい剣幕だな」"


show girl_b1_5 at center
with dis
hide boy_b2_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0021
Seito "「……よほど堪えたのね」"

hide girl_b1_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "クラスメイトだけあって、朝食時の反応とはちょっと違う。\n
悪いと思ったのか、口々にいろいろ言っていたのが、おとなしくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_4")
T "「まったくの誤解なの！\n
あのね……」"


show bor_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_4")
voice bor_g0020
Boris "「なあ、[firstname]……」"

play sound se_0136
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょんちょん、と肩をつつかれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……ちょっと待っていて。\n
今後の私の評価に関わる、重要な誤解を解いているところだから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後から肩をつつかれるものの、今はそれどころではない。\n
ここで説明しなければ、誤解を放置してしまうことになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逆に、ここで誤解を解けば、クラスメイトが広めてくれて訂正できるかもしれない。"

hide bor_m_03_11
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0021
Boris "「Ｎｏ．２さんが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「だからそれも誤解よ！\n
エリオットが私に土下座なんかするわけないでしょう！」"

play sound se_0136
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょんちょん、と、しつこく肩をつつかれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「ちょっと待ってってば！\n
おとなしく待っていてよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう少しで予鈴が鳴ってしまう。\n
ホームルームが始まってしまえば、もう誤解を解くチャンスはない。"


show eri_m_03b_12 at center with Dissolve(2)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ホームルームが終わると、皆自分の授業に間に合わせるために、それぞれの教室へと移動していってしまうのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その前に、絶対に誤解を解いてしまわなければ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「そんなの、想像もつかないでしょう！？\n
私がエリオットを従わせるだなんて！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼が従うのは、寮長のブラッドであって、私ではない。"

hide bor_m_01_11
show bor_m_03_12 at left_center with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「…………」"


show pia_m_01_3 at right_center with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Pierce "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しーん、とクラスメイト達は静まり返っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……よし。\n
納得してもらえたわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「で、ごめんなさい。\n
何の用かし……」"

hide bor_m_03_12
show bor_m_03_13 at left_center
hide pia_m_01_3
show pia_m_01_13 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ら、と振り返った先で、エリオットが耳をしょんぼりと垂れさせて立っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「！！！！」{/size} "

hide bor_m_03_13
show bor_m_01_9 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_g0022
Boris "「だからＮｏ．２さんが来てるよ、って教えてあげたのに……」"

hide bor_m_01_9
show pia_m_01_13 at left_center
hide pia_m_01_13
show girl_a1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice mat_g0027
Seito "「……悪いけど、想像ついちゃったわね」"

hide pia_m_01_13
show girl_a1_5 at left_center
hide girl_a1_5
show boy_a1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice oni_g0022
Seito "「ああ。\n
……想像できたな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "{size=+20}「！！！！？？」{/size} "

hide eri_m_03b_12
show eri_m_03b_13 at center
with dis
hide girl_a1_5

hide boy_a1_5

pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice eri_g0258
Elliot "「えっと……、なんかよく分かんねえけど……。\n
朝の忙しい時間に悪かったよ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「エ、エエエエエリオット！\n
違うの、違うのよ！？」"

hide eri_m_03b_13
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice eri_g0259
Elliot "「あ、いや……、うん。\n
あんた俺の部屋にネクタイ忘れていっただろ？」"

hide eri_m_01_10
show eri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice eri_g0260
Elliot "「それ、届けに来ただけだったんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……あ。\n
そういえば）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝、着替え直しているときに、ネクタイがないのに気づいてはいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（予備があるから、後でエリオットに聞こうと思っていたんだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、私がネクタイ抜きではまずいだろうとわざわざ届けにきてくれたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……わあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "忘れ物の、ネクタイ。\n
翌朝の受け渡し。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "想像を超えて、照れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_8")
T "（いや、想像も出来ないっていうか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさか、こんなやりとりをする日がこようとは。"

hide eri_m_01_9
show eri_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0261
Elliot "「ご、ごめんな、邪魔して！\n
これ、渡したから……！！」"

hide eri_m_02_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは私の手をとり、その手の中にネクタイを握らせると文字通り脱兎の勢いで走り去っていってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しょんぼりと下げたウサギ耳をなびかせて。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "照れていたのを、勘違いされてしまったかもしれない。"


show bor_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0023
Boris "「すげー……。\n
Ｎｏ．２さんパシらせたあげくに、あんなにしょぼくれさせるなんて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……ち、違うの！\n
今のは事故よ！！」"

hide bor_m_03_11
show bor_m_03_11 at left
with dis

show pia_m_03_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pie_g0007
Pierce "「君、本当にすごいんだね！\n
俺、君のことボスって呼んだらいいのかな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「やめてちょうだい！！！\n
第一、ボスはブラッドでしょう！」"

hide pia_m_03_5
show pia_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice pie_g0008
Pierce "「でも、エリーちゃんを使いっぱしりに出来るならボスだよ！\n
エリーちゃんは、ボスのいうことしか聞かないからね！」"


show boy_a2_4 at center
with dis
hide bor_m_03_11

hide pia_m_01_10

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice oni_g0023
Seito "「すげ～……」"

hide boy_a2_4
show boy_a2_4 at left
with dis

show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice nos_g0022
Seito "「あなたって、すごい子だったのね、[firstname]……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「いや、違うんだって！\n
普通よ、普通」"

hide girl_b1_2
show girl_b1_2 at left
with dis

show boy_b2_2 at right
with dis
hide boy_a2_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice suz_g0029
Seito "「普通は、帽子屋寮の副寮長を従わせるなんて出来ないって……」"

hide boy_b2_2
show boy_b2_2 at left
with dis

show girl_a1_3 at right
with dis
hide girl_b1_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice mat_g0028
Seito "「普通と思っているのなら、尚すごいわ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「～～～～～！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はゴーランドがやってくるまで懸命に誤解を解こうと試みてはいたのだが……。\n
結果として、どうやら誤解をより深めるだけに終わってしまったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……ど、どうしたらいいの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪いほうへ収束してしまいそうだ。\n
つまり、誤解されたまま。"

with dis
$ hi_mes()
hide boy_b2_2

hide girl_a1_3
##[chara2 PAY ATTENTION="false"]

scene bg10_sb_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_par15_rg_hat_day
with stripe_l_medium

play music laboratory_day_p_wam

scene bg_par12_hct_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "数日たっても、その噂はなかなか落ち着いてくれなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が生半可に帽子屋寮の幹部達と親しくしている分、余計にその誤解は解けないでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……はあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの淹れてくれた紅茶の水面を見つめて、つい溜息が零れてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつものようにエリオットと二人で中庭の畑の世話を終わらせて、それから流れで参加したブラッドの茶会でのことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオット本人は、見回りを済ませてくる、とのことで今は席を立っている。"


show bra_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0545
Blood "「おや……、疲れた顔をしているな、お嬢さん。\n
別段エリオットに疲れさせられている……、というわけでもないだろうに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「ブラッド……。\n
それ、セクハラよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ニヤニヤとした笑みを含んだ視線を向けられて、私は向かいに座るブラッドを睨みつける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんでそんなことを知っているのか、と言いたいところだが、ここは帽子屋寮だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子寮を誰かが抜け出したり、その逆に女子寮から誰かが抜け出すようなことがあれば、ブラッドの耳にも入るだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、ある意味誰よりもエリオットの傍にいるのがブラッドなのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなことを言うと、ブラッドは私がエリオットの傍にいるのではなく、こいつが私についてくるんだ、と主張しそうだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただでさえ、察しやすいエリオット。\n
様子からだけでも分かってしまいそうだ。"

hide bra_m_01_1
show bra_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0546
Blood "「互いの部屋を行き来することができないともなれば、さぞかし焦れるだろう。\n
……ああ、それとも校舎内で逢引を？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "涼しい顔で紅茶を啜りながら、ブラッドが言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「し・て・な・い・わ・よ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一音一音区切ってはっきりと否定してやれば、ブラッドはおやおや、という風に片眉を跳ね上げて笑った。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……本当に、セクハラだわ、この紅茶男）"

hide bra_m_01_11
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice blo_g0547
Blood "「エリオットも可哀想に」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……あのね。\n
あなたも分かっているでしょう？」"

hide bra_m_03_2
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice blo_g0548
Blood "「何をだ？\n
好きな女に触れさせてもらえないエリオットの辛さならば、推して知るものもあるが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「違うわよ！\n
そうじゃなくって、噂よ、噂」"

hide bra_m_03_15
show bra_m_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice blo_g0549
Blood "「噂？\n
さて、どれのことだろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しらばっくれているのかとも思ったが、私へそう問い返すブラッドは、本当に私が言う噂がどれなのか見当をつけられずにいるといった感じだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（とんでもないセクハラ男だけど……、寮長だものね。\n
情報量は多いか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮長であり、この学園における有力者の一人でもあるブラッドには、私の耳に入るよりももっと多くの噂や情報が入ってくるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「アレよ。アレ。\n
私が、帽子屋寮のトップにのし上がった……、とかいう」"

hide bra_m_02_15
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice blo_g0550
Blood "「ああ、それか。\n
なかなかに八面六臂の大活躍をしているようで、私も楽しませてもらっているよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「楽しまないでよ。\n
……怒っていないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが蹴落とされたというに等しい噂だ。\n
寮を仕切る者として、腹は立たないのだろうか。"

hide bra_m_02_8
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0551
Blood "「現実的なものなら、な。\n
広がって収拾のつかなくなっているような噂は楽しみの対象にしかなりえない」"

hide bra_m_03_10
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0552
Blood "「広がる種類も色々。\n
集め甲斐のある噂だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「それって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるで、私に関する噂のバリエーションが他にも色々あるかのように聞こえる。"

hide bra_m_03_2
show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0553
Blood "「そうだな、派生は色々だが……。\n
私としては……」"

hide bra_m_02_2
show bra_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0554
Blood "「君が、私とエリオットをたらしこみ、誘惑し、裏から操り、シンフォニア征服を企む妖婦という説に一票を投じたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "{size=+20}「げふっ！！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "飲みかけた紅茶が、気管に入った。\n
激しくむせる。"

hide bra_m_02_1
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0555
Blood "「おやおや、図星か？\n
大丈夫か、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私やブラッド、エリオットや双子も含めた五人で悠々とお茶会を開くことのできるティーテーブルはそれなりに大きいもので……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドも向かいに座った私の背中を撫でるなんてことは出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、できるものならばそうしたいとでも言いたげに身を乗り出して、心配そうに聞いてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_13")
T "（……{size=+20}殴り倒してやりたい{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "初期は萎縮していたというのに、こんな発想が出てくるとはたいした進歩だ。\n
実行したら、噂が真実になってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……っ、こほん。\n
私が誰と誰をたらしこんだですって？」"

hide bra_m_03_10
show bra_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice blo_g0556
Blood "「私と、エリオットだ。\n
その噂によると、君は魔性の魅力でもって幹部を骨抜きにし、裏で暗躍しようとしているということらしい」"

menu:
    "誤解だわ。":
        jump gakuen_elliot_end2a
    "納得がいかない。":
        jump gakuen_elliot_end2b
label gakuen_elliot_end2a:
$ lovechara_elliot_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_4")
T "「誤解だわ……」"

hide bra_m_02_5
show bra_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_4")
voice blo_g0557
Blood "「ははは、気にする必要はない。\n
皆、面白がっているだけで、本気で信じているわけでは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_2")
T "「私が骨抜きにしたのは、エリオットだけよ。\n
あなたのことは別にたらしこんだりしていないわ」"

hide bra_m_03_9
show bra_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_2")
Blood "「…………」"

hide bra_m_02_7
show bra_m_02_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_2")
voice blo_g0558
Blood "「否定するのはそこか。\n
傷つくぞ、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_4")
T "「ふふん。\n
もちろん、たらしこまれたりもしていないしね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どちらがどちらに、というのでなく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "色々と口では言っていても、一緒にいて楽しく、居心地がいいからこそ、私はこうして彼らと関わることを選んだのだ。"

jump gakuen_elliot_end3
label gakuen_elliot_end2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「納得がいかないわ」"

hide bra_m_02_18
show bra_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice blo_g0559
Blood "「そうだな。\n
別に君が暗躍したくて、私達に近づいたわけではないことは分かっている……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_3")
T "「そこじゃないわよ。\n
本当にシンフォニア征服がしたかったら、あなた達の力なんて借りていないわよ」"

hide bra_m_03_3
show bra_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_3")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「飽きっぽいんだもの、あなた」"

hide bra_m_03_6
show bra_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice blo_g0560
Blood "「……ふ。逞しいな、お嬢さん。\n
噂もはずれてはいない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「どういう意味よ」"

hide bra_m_03_7
show bra_m_02_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice blo_g0561
Blood "「……ボス向きかもしれないと誉めているんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「誉めていないわ、それ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（……つまり、自分と似ているってことじゃない）"

jump gakuen_elliot_end3
label gakuen_elliot_end3:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「……何にしても、馬鹿馬鹿しい噂だわ」"

hide bra_m_02_16
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice blo_g0562
Blood "「馬鹿馬鹿しいことほど、面白い。\n
退屈しのぎにはいいんだろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……ここの学校の人って、皆、暇なのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうなのかもしれない。\n
目の前に、その代表がいる。"
if lovechara_elliot_points == 10:
    jump gakuen_elliot_end4b
jump gakuen_elliot_end4a
label gakuen_elliot_end4a:
with dis
$ hi_mes()
hide bra_m_02_8


scene bg_par15_rg_hat_day
with stripe_l_medium

play music view_day_p_wam

scene bg_par03_nb_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームやブリーズといった大きなイベントが過ぎて、落ち着いた日常が帰ってきた。例の噂も、最近ではすっかり下火になっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……ようやく、安心できる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人の噂も７５日なんていう言葉があるが、実際にはそれよりももっと短い期間で治まってくれたようだ。"


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふう、と額を拭って空を見上げる。\n
そろそろ初夏を通り過ぎて、本格的に暑くなってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "高く澄んだ青空に、吹き抜ける風が気持ちいい。\n
私は中庭の片隅、にんじん畑にて靴を脱ぎ、裸足になって待機していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脱いでいるのは靴や靴下だけではない。\n
上着と、ネクタイもそうだ。"

play sound se_0417

scene bg_par03_nb_day
with dis

show eri_m_03a_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0262
Elliot "「悪い、待たせたか！\n
ちょっと見回りが長引いちまってよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「大丈夫よ、私も今来て準備していたところだから。\n
見回り、お疲れ様」"

hide eri_m_03a_4
show eri_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice eri_g0263
Elliot "「おう、ありがとな。\n
あんたにそう言ってもらえると、疲れもふっとぶぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "駆け足でやってきたエリオット。\n
労わりの言葉をかければ、彼は嬉しそうにはにかんでみせる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……嬉しくなるなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つられてしまう。\n
ちっとも素直とはいえない、可愛げもない、どちらかというとエリオットよりブラッドに似ているような私なのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一緒にいると、同じになれる。\n
もちろん、外から見れば、エリオットだって可愛げなどないのだろうけど。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_10")
T "（私には、すごく……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが準備をしている間に、私は彼の脱いだジャケットや靴、ネクタイといったものを私の荷物と一緒にひとまとめにしておく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段はエリオットが作業担当なのだが、今日に限っては二人そろって作業姿だ。"


show m_eri_goodend2_1 onlayer master
with dis
hide eri_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0264
Elliot "「ついにこの日が来たと思うと、感動するな～っ！\n
今夜の晩飯が楽しみだぜ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なかなか芽も出ず、手間のかかったエリオットのにんじん畑だが、今日ようやく収獲を迎えるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達の目の前には、青々と茂ったにんじん畑が広がっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "収獲については、園芸部のお墨付きだ。"

jump gakuen_elliot_end5
label gakuen_elliot_end5:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「エリオットは本当ににんじん好きよね。\n
さすが…………、だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごにょごにょ、の部分には触れないでおく。\n
魔法生物疑惑があろうとなかろうと、彼は己がウサギであることは否定するのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0265
Elliot "「何言ってるんだ？\n
俺、にんじんは嫌いだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「またまた。\n
冗談はその耳だけにしておきなさいよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_3")
voice eri_g0266
Elliot "「いやいや、冗談じゃねえって！\n
俺の耳も別に冗談にもならねえし……、あんた、たまに変なこというよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（変なのはエリオットの自己認識よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前に身の丈サイズの鏡を置いて、確認させてやりたい欲求に駆られる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「普通、にんじん嫌いな人は、こんなに頑張ってにんじんを育てたりしないわよ。\n
あなた、今だって楽しみにしていたじゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice eri_g0267
Elliot "「俺が好きなのはにんじんじゃなくて、にんじん料理だ！\n
生のにんじんなんて、ウサギじゃあるまいし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「は……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "{size=+20}（ウサギよね？）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうなったらとことん追及してみたくもなるが……、エリオット本人にもウサギ耳が生えている理由なんて分からないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ウサギに何故ウサギなのかを問うのは、もはや哲学だ。"
if lovechara_elliot_points == 10:
    jump gakuen_elliot_end6b
jump gakuen_elliot_end6a
label gakuen_elliot_end6a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はこれ以上の追及は諦めることにした。\n
それよりも、早く収獲したい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「さ、始めましょうか？\n
あんまり遅くなると、夕食の準備に間に合わなくなっちゃうわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice eri_g0268
Elliot "「だな！\n
せっかく使用人連中に頼んで、にんじんフルコース作ってもらうことにしたんだし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice eri_g0269
Elliot "「きっと、ブラッドやガキどもも喜ぶぜ～。\n
招待状渡したときなんか、もう三人とも呆然としてたんだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……でしょうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私だって、普通ならばにんじんフルコースに招待されたいとは思わない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今回が特別なのは、その材料となるにんじんが、私とエリオットが精魂こめて世話して、収獲したものだからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、巻き込まれるブラッドやディー、ダムにとっては悪夢そのものだろう。\n
エリオットに悪気がないのが致命的だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0270
Elliot "「あんなに感激してもらえると、奮発したくなるよな～……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……{size=+20}でしょうね{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中だけでそっと手を合わせておいた。\n
それから二人、裸足で畑へと入る。"

hide m_eri_goodend2_1
show m_eri_goodend2_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふかふかとやわらかい土が、足裏にくすぐったい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0271
Elliot "「抜いたにんじんは、こっちの籠にいれてくれ。\n
……んじゃ、やるか！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ええ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シャツの裾をまくって、にんじんの収獲を開始する。\n
茂るにんじんの葉の根元をぐっと掴んで、力を入れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「っ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぽんっと抜けるのが気持ちいい。\n
籠の中に、順調ににんじんが重ねられていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_16")
T "「よいしょ、っと……。\n
あら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0272
Elliot "「どうした？\n
何かあったか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「ん……、ちょっと、抜けない……っ。\n
よっぽど大きいのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何本目かにして、特別大きく実ったにんじんに当たってしまったのか、いくら力を込めても抜けそうにない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0273
Elliot "「はは、あんた細腕だもんな。\n
……どれどれ？」"

hide m_eri_goodend2_2
show m_eri_goodend2_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中腰にかがんで、にんじんを引き抜こうとしていた私の体を背後から包み込むようにしてエリオットが手を重ねる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（……やっぱり大きいなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして懐の中にすっぽりと入れられてしまうと、やはりエリオットは大きいと思う。私の手の上からにんじんの葉を握る手も、がっしりと大きい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中から包み込む体温……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（……昔、こういう童話を読んだ気がするなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "動物の協力もあり、野菜を引っこ抜く童話。\n
……にんじんではなく、カブだったが。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メルヘンだが、乙女らしくない発想にいってしまう……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0274
Elliot "「ほら、せぇの、で引っ張るぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「う、うんっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice eri_g0275
Elliot "「せぇのっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「えい！」"

play sound se_0346
hide m_eri_goodend2_3
show m_eri_goodend2_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_2")
T "「わあ……！\n
ずいぶんと大きいのが獲れたわね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「……っていうか、大きすぎない？\n
何これ、にんじん？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice eri_g0276
Elliot "「にんじんだろ？\n
だいだい色だし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……{size=+20}にんじんのような、何かじゃないの？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice eri_g0277
Elliot "「にんじんだって」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……にんじんにしても、まともなにんじんには見えない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice eri_g0278
Elliot "「じゃ……、まともじゃないにんじんか？\n
これ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……{size=+20}正常には見えないわね{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "園芸部の分けてくれた栄養材や肥料がよかったのだろうか。\n
……いや、よすぎたのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（いや……、悪かったのかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とにかく、極端な育ち具合だ。\n
先刻連想した童話ではないが、サイズとしては童話に出てきたカブそっくりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今まで抜いてきたにんじんも、決して小さいものではなかったが、その中でも群を抜いて大きい。"

hide m_eri_goodend2_4
show m_eri_goodend2_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0279
Elliot "「あんたが、手伝ってくれたからだよな……。\n
あのとき、あんたが声かけてくれてよかった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットはうるうると感激している。\n
努力の結晶とでも言いたげだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「いや……、感激してくれているところ悪いんだけど、別に私のおかげってわけじゃないと思う……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice eri_g0280
Elliot "「いや、あんたが熱心に手伝ってくれたから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（いや～～……、熱心だとかも関係ないと思う）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法か何かのなせるわざだろう。\n
魔法学校なだけに正しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0281
Elliot "「本当に感謝しているんだぜ？\n
ありがとな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_10")
T "（……ま、いいか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが嬉しそうだと、私も嬉しくなる。\n
というか、細かいことがどうでもよくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「……私は調べただけよ？\n
実際に作業をしたのはエリオットだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "改めて感謝の言葉を告げられて、照れくさくなった。\n
私だって少しは手伝ったが、力仕事はすべてエリオットがした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼が根気よく耕さなければ、雑草を抜いて世話をしなければ、こんなにも立派なにんじんは実らなかっただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……いや、カブなんだけど。\n
どう見ても、にんじんというよりは）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実りすぎだ。\n
見渡してみると、やけに大きすぎる茎が多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0282
Elliot "「俺一人じゃ、駄目だった。\n
あんたのおかげだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「いや、あのね、エリオット……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice eri_g0283
Elliot "「ん？\n
なんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「いや……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_8")
Elliot "「？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きらきら。\n
にこにこ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴょこぴょこ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当に……、何もかも、どうでもよくなってしまう。\n
魅惑のウサギさんだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「……どういたしまして」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_8")
voice eri_g0284
Elliot "「ああ、ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな言葉とともに、満足げに笑んだ唇が近くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは外で、畑で、誰に見られているとも分からない場所だというのに、それを止めようとは思わなかった。"

hide m_eri_goodend2_5
show m_eri_goodend2_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唇同士が、軽く触れ合うだけのキスだ。\n
それだけで満たされる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゆっくりと離れて……。\n
……我に返る。"

hide m_eri_goodend2_6
show m_eri_goodend2_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が頬を赤らめたのに、つられたようにエリオットの頬にも朱色が滲む。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0285
Elliot "「さ、さあ……、続きやろうぜ！\n
にんじん抜き！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットはそそくさと私から離れると、再びにんじんをひっこ抜き始めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「にんじん抜き、って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice eri_g0286
Elliot "「さあさあ、抜いていこうぜ！\n
急がないと、日が暮れちまう！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「はいはい……」"


scene bg06_sk_h_day
with dis
hide m_eri_goodend2_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、空は高く澄んで、日が暮れるまではまだまだ時間がかかりそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、夕暮れまで続けるのも悪くない。\n
きっと、収穫のにんじん畑が夕陽色に染まるなんて、色合い的にとても綺麗なはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「にんじん畑で、ウサギさんとにんじん抜き……、か」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも、大好きなウサギさんと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんてメルヘン。\n
なんて平和。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（そして、なんて魔法学校らしくない……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう思いつつ、手は休ませず。\n
私は、次なるにんじんを引っこ抜いた。"

hide frame_gen_togaki
hide ali_m_06_16
with Dissolve(5)
scene black with Dissolve(5)
stop music
##endmemory
jump gakuen_b
label gakuen_elliot_end4b:

play music secret_day_p_wam

show bra_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0563
Blood "「ああ、そうだ。\n
私を楽しませてくれている礼に、君にいいものをあげよう」"

play sound se_0198

scene m_cut_bousi_key1 ##PAY ATTENTION="true"]
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「……なあに、これ。\n
どこかの鍵？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「ずいぶん古いものみたいだけれど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice blo_g0564
Blood "「秘密の部屋の鍵だ。\n
詳しくはエリオットに聞きなさい」"

show m_cut_bousi_key1u onlayer master ##PAY ATTENTION="true"]
with dis
hide bra_m_03_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手をだすように、と促され。\n
それに従うと、その手のひらの上にしゃらりと金色の鎖がとぐろを巻くようにして載せられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その鎖に通されて、同じ色をした古びた鍵がかかっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（楽しいか、楽しくないか……、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンプルなそれこそが、ブラッド＝デュプレという男の行動指針だ。\n
楽しそうだからこそ、ブラッドは私に手を貸してくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、今も楽しむために行動する。\n
この鍵も、何かしら彼を楽しませるためのアイテムなのだろう。"


scene bg06_sk_h_day ##instant]
hide m_cut_bousi_key1u ## PAY ATTENTION="true"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……難儀な）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、彼を楽しませることが出来ている限り、彼は私に味方してくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（せいぜい、楽しませてあげるよう努力するとしようかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ彼は、恋人たるエリオットのボスなのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋人の上司に気に入られようと努力する私は、ちっとも魔性の妖婦などでなく、むしろ気立てのよい「お嬢さん」の部類なのではないか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうに、自画自賛しておきたい。"


##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg06_sk_h_day with Dissolve(.5)

scene bg_par15_rg_hat_day
with stripe_l_medium

play music garden_day_p_wam

scene bg_par03_nb_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームやブリーズといった大きなイベントが過ぎて、落ち着いた日常が帰ってきた。例の噂も、最近ではすっかり下火になっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（……ようやく、安心できる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人の噂も７５日なんていう言葉があるが、実際にはそれよりももっと短い期間で治まってくれたようだ。"


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふう、と額を拭って空を見上げる。\n
そろそろ初夏を通り過ぎて、本格的に暑くなってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "高く澄んだ青空に、吹き抜ける風が気持ちいい。"


show m_eri_end1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0287
Elliot "「結構育ったな～。\n
なあなあ、どれくらいで収獲できると思う？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「そうねえ……。\n
一度園芸部の人に見てもらってから、収獲にしましょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice eri_g0288
Elliot "「楽しみだな！\n
どんなにんじん料理を作ろうか、今から迷うぜ～～！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_1")
T "「ふふ。ついに収穫かあ……。\n
おいしいといいわね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_1")
voice eri_g0289
Elliot "「絶対うまいに決まっている！\n
普通のにんじんでもうまいのに、あんたと一緒に作ったにんじんなんだぜ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（それはどういう基準なんだろう……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、エリオットが嬉しそうにしていると、私も同じように嬉しくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の耳がぴょこぴょこ動くと、細かいことなんてどうでもよくなる。\n
……まったく、罪なウサギさんだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、制服の上着を脱ぎ、ズボンの裾をまくったいつもの作業スタイルで、待ち遠しくて仕方がないといった様子だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なかなか芽も出ず、手間のかかったエリオットのにんじん畑だが、今では葉が伸びやかに茂っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はエリオットと違い、別に熱心なにんじんフリークというわけではなかったはずなのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（……楽しみ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットと共に、その収獲を楽しみに思う気持ちは日々強くなる。"

jump gakuen_elliot_end5
label gakuen_elliot_end6b:

play music flower_eve_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……それにしても、暑いわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "畑は日当たりのいい場所に作ってあることもあり、こうして作業をしているとじっとりと汗ばんでくる。\n
そろそろ衣替えの時季だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "上着を脱いで作業しているエリオットに倣って、私も上着を脱いでしまうことにした。"

play sound se_0067
hide m_eri_end1
show m_eri_end2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットがこちらをじっと見ているのに気づいて、私は首を傾げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0290
Elliot "「あんた……、それ。\n
前から首に下げていたっけか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょい、と指をさされたのは、前にブラッドから渡された鍵だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（そういえば……。\n
詳しくはエリオットに聞けって言われていたけど、忘れていたわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかく貰った物だし、きっと何かで役に立つのだろうと制服の下から首に下げていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はそれをシャツの中から、しゃらしゃらと引っ張り出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「これ、前にブラッドに渡されたの。\n
あなたはこれ、どこの鍵だか分かる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice eri_g0291
Elliot "「……ブラッドが、あんたにそれを？\n
ああ、そういうことか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「？」"

hide m_eri_end2
show m_eri_end3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice eri_g0292
Elliot "「きっとそういうこと……、だよな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice eri_g0293
Elliot "「すげえぜ、ブラッド……！\n
やっぱりブラッドはいいボスだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「？？？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは私には分からないことについてをブツブツと呟いては、一人で納得している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの言っていたとおり、エリオットにはその鍵の意味が分かったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分からないのは私だ。\n
何が、「そういうこと」なのやら。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_15")
T "「ねえ、エリオット、私には分からないわ。\n
これ、どこの鍵なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここシンフォニアでは、こういった物理的な鍵のかかった部屋というのはほとんど見かけない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしくは、そういうふうに見せかけてはいても、なんらかの魔法によるロックとの組み合わせになっていることが多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろいろと思い出そうとはしてみるものの、この鍵が使えそうな扉を思い浮かべることは出来なかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0294
Elliot "「そっか、あんたは知らなかったのか。\n
なら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……エリオット？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらっ……、と。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一瞬。\n
ほんの一瞬。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットの双眸が、真昼間の畑には不似合いな色を孕んだような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実りつつあるにんじんにはしゃぐウサギさんなんて可愛いものではなく、もっと危険な獣のような……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、それは私が名を呼ぶ間にもすっかりどこかへ行ってしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0295
Elliot "「……よし。\n
じゃあ、俺が教えてやるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、にこにこと上機嫌に私のもとまで歩み寄ってくると、ひょいと私の体を担ぎ上げた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつかのストームの夜にしたような、腕に座らせて抱きかかえるような形だ。"

hide m_eri_end3
show m_eri_end4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「エ、エリオット！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_6")
voice eri_g0296
Elliot "「ははは。せっかくだから、今から行こうぜ！\n
あんたに、その鍵の使い道、みせてやるから！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「そ、それはありがたいけど……！\n
どうして私を抱き上げる必要があるの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段の視界よりも、はるか高い位置から見る世界は新鮮だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前回は夜だったり、それどころではない状態だったりということもあって、その視界を楽しむ余裕もなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今は抱き上げたエリオット本人よりも高い視線となっているが、彼ぐらいの長身な人からの世界は、こういうふうに見えているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0297
Elliot "「まあまあ、細かいことは気にするなよ。\n
ほら、行こうぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、その辺りの木にひっかけていた自分の上着と私の上着とを、私を抱えるのとは逆の手に回収する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その、軽い仕草。\n
バランスを崩したりもせず、思う以上に彼が力持ちだと分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_8")
T "「……エリオット。\n
ちなみに、聞きたいんだけれど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_8")
voice eri_g0298
Elliot "「ん～？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、そのままひょいひょいと畑を出て、歩き始める。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「その……、鍵を使える場所って、どこにあるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice eri_g0299
Elliot "「そう遠くはないぜ？\n
帽子屋寮の男女共同区域だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「…………。\n
で、そこまでこのまま移動しようって言うの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice eri_g0300
Elliot "「ああ。\n
大丈夫だ、あんた軽いから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にかっと、エリオットが一点の曇りもない笑顔で言い切った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "「持ち運びの心配はしていないわよっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういう問題ではない。\n
このままの状態で、寮に入るなんて考えるだけで恐ろしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ようやく、デタラメな噂が収束してきているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……逆戻り。\n
いや、前よりも酷い噂になるかも）"

play sound se_0625
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「ちょっと……！！\n
エリオットってば！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_9")
voice eri_g0301
Elliot "「暴れたら落ちるぜ？\n
……落とさねえけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「だったら暴れるわよ！？\n
力いっぱい暴れるわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "落とさないとエリオットが言うから、私は安心して暴れることにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唯一の弱点といってもいい耳を引っ掴んでやろうと手を伸ばすものの……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはすでに読まれていたのか、エリオットはぐいっと体をそらして私の手から耳を逃がす。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_6")
T "「ひ、卑怯よ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_6")
voice eri_g0302
Elliot "「卑怯なのは、あんただろ。\n
それは反則」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "「反則なんてないわよ！\n
力じゃかなわないんだもの！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「下ろしなさいってば、エリオット！」"

hide m_eri_end4
show m_eri_end5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
voice eri_g0303
Elliot "「……嫌だね。\n
噂の一つや二つ、いいだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_9")
T "「よくないわよ！\n
私がとんでもない噂に悩まされているのを、知っていてよくも……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_9")
voice eri_g0304
Elliot "「……、だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼそり、とエリオットが何かを小さく呟いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……何？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼそぼそと、子供が言い訳するような調子の声は、うまく聞き取ることができない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「何よ。\n
聞こえなかったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice eri_g0305
Elliot "「……嫌なんだよ。\n
いくら相手がブラッドでも、あんたが他の誰かのものみたいな噂たてられるのは」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……はあ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……どんな噂？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が聞いたものとは違う気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0306
Elliot "「あんたは俺ので、ブラッドのもんじゃねえ。\n
あんたを誰かと共有するなんて、絶対に嫌だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_16")
T "「……あなたはどんな噂を聞いたのか、聞いてもいい？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0307
Elliot "「……ん？\n
ああ、あんたが俺とブラッドを手玉にとり、帽子屋から始まり、四つの寮を支配下に治めているという……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "{size=+20}「明らかに作り話よ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが以前言っていた通り、噂の拡大具合はたいしたものであるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……嬉しくないわ）"

hide m_eri_end5
show m_eri_end6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice eri_g0308
Elliot "「手玉に取るのは、俺だけにしてくれよ。\n
……なあ、[firstname]、あんたは俺のもんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段は見上げる角度にあるエリオットの顔が、今は私を見上げている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ねだるような、甘えるような……、それでいてその言葉自体が甘い熱を帯びているように響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「手玉にとってくれ、って。\n
……恋人に言う言葉じゃないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice eri_g0309
Elliot "「恋人なら、いいだろ。\n
俺も、あんたのものだから、弄ばれようと何だろうと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「エリオット……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……いや、ウサギを弄ぶような気はないんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゆらゆらと揺れる長いウサギ耳が私の視界をちらつく。\n
格好よくて、凛々しくて、怖いところもある男だと分かっているのに……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_11")
T "（可愛すぎるのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抱え上げられたまま、エリオットの額へと唇を寄せようとして……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「……！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアの窓側に、生徒達がこちらを凝視しているのを発見した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「～～～～っ！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今、自分が何をしようとしていたのかを思うだけで、顔から火を噴きそうだ。"

play sound se_0055
hide m_eri_end6
show m_eri_end7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0310
Elliot "「い！？いてええええええっ！！！\n
耳掴むのやめてくれよっ！痛いんだって……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "「い、いいから！エリオット走って！！\n
早く、目的の場所まで案内して……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice eri_g0311
Elliot "「わ、分かったから、耳！\n
引っ張るのはやめろって……！\n
いてえっ、いててててててて！！」"

play sound se_0417

scene bg_par03_nb_day ##instantPAY ATTENTION="true"]
hide m_eri_end7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットに抱き上げられたまま、その場から逃走する。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（ああ……、今度はどんな噂が……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "考えるのも恐ろしい。"

with dis
$ hi_mes()

scene bg_par15_rg_hat_day
with stripe_l_medium

play music gallery_front_nig_p_wam

scene bg25_rr_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私を担いだままのエリオットによって案内されたのは、帽子屋寮の男女共同区域の一角にある小さな部屋だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「……ここ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その扉の前で、ようやくエリオットに下ろしてもらう。"

##[rchara1 PAY ATTENTION="false"]
show eri_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0312
Elliot "「ああ。\n
ここだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「これを使うのよね……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

play sound se_0450
hide eri_m_01_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドから貰った鍵で、その部屋の扉が開く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あまり使われていないのか、ゆっくりとドアノブをまわして引くと軋みをあげる。"

play sound se_0201

scene bg_par05_br_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中に足を踏み入れると、ふわり、甘い古書の香りが鼻先をくすぐった。\n
好きな匂いだ。"


show m_eri_end8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……ここは、書庫？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "秘密の部屋なんて聞いたので、噂で聞いたことのあるシンフォニアの秘密の隠された部屋だとか、そういったものを想像してしまってもいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これでは秘密の部屋というよりも、忘れられた部屋といった感じだ。\n
壁には一面書架が作られており、その向かい側に大きなカウチが設置されている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0313
Elliot "「ああ。ブラッドが個人的に書斎として使ったりしていたな。\n
その鍵を持ってる奴しか、中には入れねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと、以前聞いた秘密の部屋の詳細を思い出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮のどこかに秘密の場所があって、選ばれたものしか入れないだとか、中にはシンフォニアの秘宝があるだとか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな話だったが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……秘宝はなさそうね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "秘密の部屋なんていうと大層だが、ここは、使われなくなった書庫といった感じの場所だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……その書斎の鍵を、どうして私に？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice eri_g0314
Elliot "「分からないか？」"

play sound se_0103
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "また、抱き上げられるのかと思った。\n
エリオットは、タックルの要領で緩く私の腰の辺りにぶつかってくる。"

play sound se_0374
hide m_eri_end8
show m_eri_end9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん充分に力加減はされているが、勢いは殺せず、カウチへとしりもちをついてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットはそのまま私の膝にうつぶせに頭を乗せるような形で、カウチの上へと乗り上げた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「ちょっと！？\n
エリオット……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice eri_g0315
Elliot "「……秘密の部屋」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「？\n
……ええ、残念だけどデマだったみたいね、その話」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の噂しかり。\n
噂なんてあてにはならないものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0316
Elliot "「……デマとは言い切れないだろ？\n
誰も知らない、誰も来ない……、二人っきりになれる密室なんだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちろりと私を見上げるエリオットの双眸。\n
ウサギには見えない……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その表情に、ブラッドが私にこの鍵を渡してくれた意図を理解した。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_11")
T "（……気がききすぎよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここまで味方してくれなくていい。\n
わざわざ、場所提供まで。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……あの人、キューピッドって柄じゃないでしょうに」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
voice eri_g0317
Elliot "「ブラッドは万能だからな！\n
部下にもすっげえ優しいんだぜ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……そう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……絶対、後でからかって、時間つぶしの材料にする気よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、エリオットにはきかない。\n
つまり、ターゲットは私だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0318
Elliot "「ブラッドに感謝して、ってわけでもないが……。\n
[firstname]、さっきの続き……、してくれねえのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「え……。\n
あ……」"

menu:
    "する。":
        jump gakuen_elliot_end7a
    "しない。":
        jump gakuen_elliot_end7b
label gakuen_elliot_end7a:
hide m_eri_end9
show m_eri_end10 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_8")
T "「……もう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ねだる声に引き寄せられるようにして、身を屈めてエリオットの額へとキスを落とした。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……満足？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_9")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_9")
voice eri_g0319
Elliot "「……いや。\n
足んねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐい、とエリオットが身を起こして、顔を寄せてくる。"

jump gakuen_elliot_end8
label gakuen_elliot_end7b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやって改めてねだられると、羞恥が先にたって行動に移すことができない。\n
焦れたように、エリオットの顔が近くなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0320
Elliot "「あんたがしてくれねえなら、俺がする」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐい、とエリオットが身を起こして、顔を寄せてくる。"

jump gakuen_elliot_end8
label gakuen_elliot_end8:
hide m_eri_end10
show m_eri_end11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私からも距離を縮めて、古書の匂いに包まれた秘密の部屋のカウチの上、甘ったるいキスを交わす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "触れるだけのキスを、戯れのように何度も。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "重ねて、重ねて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_8")
T "「……っ」"

hide m_eri_end11
show m_eri_end12 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま、のしかかられて、ずるずるとカウチの上へと押し倒されていく。\n
埃で曇った窓の向こうには、まだ青空が広がっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな時間に、こんな場所で。\n
こんなことを。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（すっかり、悪い子ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後悔でなく背徳感に背中をぞくりと震わせた私は、きっともう後戻りはできない。\n
帽子屋寮の住人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（……でも、噂ほど酷い悪女じゃないわよ？）"

with dis
$ hi_mes()
hide m_eri_end12

with dis
$ hi_mes()

scene bg25_rr_day
with stripe_l_long

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのしばらく後。\n
寮の廊下で、ブラッドに呼び止められた。"


show bra_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0565
Blood "「なあ、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「なあに？」"

hide bra_m_01_11
show bra_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_16")
voice blo_g0566
Blood "「君が、君に弄ばれたいと宣言したエリオットを尻にひき、馬代わりに走らせて楽しんでいる……、という噂を聞きつけたんだが」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「…………」"

hide bra_m_01_12
show bra_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice blo_g0567
Blood "「もし事実のようなら、私も混ぜてくれ。\n
楽しそうな遊びじゃないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「…………」"

play sound se_0258
camera at hpunch
camera at vpunch
hide bra_m_01_1
show bra_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice blo_g0568
Blood "「……{size=+20}っい！？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ニヤニヤと嫌な笑みを浮かべるブラッドの足を、全体重をかけて勢いよく踏みつけてやった。\n
少しは気が晴れるかと思いきや……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……なかなか、完全には晴れてくれないなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それどころか、噂ときたら、酷くなる一方ではないか。\n
きりがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっともう、後戻りはできない。\n
そう思ったのは確かで、実際に後ろに下がるのは難しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が……、ほんの少しだけ。\n
後ずさりをしたくなってきた、今日この頃。"

pause 1
hide bra_m_02_12
with Dissolve(2)

scene white onlayer master
with compress_extralong

##[bgimage ##instantPAY ATTENTION="true"]
scene black with compress_extraextralong
pause 1
stop music
jump gakuen_a
