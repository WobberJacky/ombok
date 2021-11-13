
scene bg25_rr_day
with dis
label gakuen_pierce1:
$ clockanim()


play music corridor_day_p_wam

scene bg_par15_rg_amu_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮と他寮との違いの大きなところは、まずはその外観だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "門をくぐってから、寮の建物へと続く中庭にはいろんなオブジェや、マジックアイテムらしきものが置かれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰が作ったのかも分からないし、何のために作られたのかも分からない。\n
ただそのすべてに共通するのは、鮮やかな色合いと楽しげな雰囲気だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……楽しそう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアのどこかにあるという、秘宝の隠された部屋というのも気になるが、室内の探索より先にまずは中庭から始めてみるとしよう。"

with dis
$ hi_mes()

scene bg20_gd_day
with stripe_l_long
play sound se_0624
play sound se_0333 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく探索していると、顔なじみの寮生に声をかけられた。"


show amuse_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0061
Seito "「ねえ、何をしているの？\n
メモ帳なんか広げて、まるで探偵みたいね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（探偵か……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われてみると、そんな気分になってくる。\n
実は、暗号のようなものを見つけたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「このオブジェを見て回っていたら、どれにも小さく数字が描かれているのよ。\n
それで何かの暗号なのかと思って」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（世界一の魔法学校だし、生徒を試すための仕掛けなのかも……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんといっても世界一だ。\n
学校の七不思議にしても、面白そうなものが多いだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これも、その一環なのかも……、と。"

hide amuse_a1_3
show amuse_a1_3 at left
with dis

show amuse_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0145
Seito "「ああ、それ……。\n
……っぷ」"

hide amuse_a1_3
show amuse_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0062
Seito "「はは……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メモ帳片手に暗号説を主張してみた私に、二人は顔を見合わせて噴出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（そ、そんな、笑われるようなこといったかしら）"

hide amuse_a2_2
show amuse_a2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice tad_g0063
Seito "「ごめんなさい。\n
ふふ」"

hide amuse_b1_8
show amuse_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice sam_g0146
Seito "「ふふふ、それ、残念ながら暗号じゃないの。\n
卒業制作の年号よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（探偵気取りで……）"

play sound se_0042
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "{size=+20}（恥）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ががーん。\n
衝撃度を音にして表現したくなってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、言われれば何故気付かなかったのだろうとも思う。\n
彼女達に笑われてしまうのも当然だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メモ帳片手に、卒業制作のオブジェの制作年数を記録して回っていたのかと思うと、今更のように疲労感に襲われる。"

hide amuse_a2_6
show amuse_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0064
Seito "「ふふ。\n
それっぽいものに思わせぶりに書かれているから、引っかかる子も多いのよ」"

hide amuse_b1_2
show amuse_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0147
Seito "「そうそう。\n
何かあるんじゃないか、ってね」"

hide amuse_a2_3
show amuse_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0065
Seito "「実際は、様々な国の言葉で書かれた年号なんだけどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「う……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "泣きたい。\n
そんな疲れが顔にも出ていたのか、二人が気の毒そうに視線を交わす。"

hide amuse_a1_2
show amuse_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0066
Seito "「異国の生徒も多いから、書かれている言葉も様々だもの。\n
思わせぶりだし、引っかかってもおかしくないわよ」"

hide amuse_b1_8
show amuse_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0148
Seito "「引っかかるっていうか……、別に引っかけでもないんだけどね。\n
真面目な子ほど、何かあるんじゃないかって思うみたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……フォローをどうも」"

hide amuse_a1_5
show amuse_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice tad_g0067
Seito "「元気を出してよ……。\n
本当に、『何かある』ものも学園内には多いから……」"

hide amuse_b1_2
show amuse_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice sam_g0149
Seito "「でも、今日は部屋に戻ってゆっくり休んだらいいわ。\n
……疲れたでしょう？」"

hide amuse_a1_1
show amuse_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice tad_g0068
Seito "「カフェテリアで、美味しいものを食べてもいいと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ダメ押しのように二人に言われて、かくりと肩が落ちた。\n
慰められるほど、落ち込む。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……本当に、『何かある』ならよかったのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これが本当に暗号だったりしたのならば、同じ労働をしたとしてもこんなにも切ないくたびれ方はしなかったと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……そうね。\n
カフェテリアで美味しいものでも食べて、それから部屋でゆっくり休むことにするわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……疲れた」"

hide amuse_a1_3
show amuse_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice tad_g0069
Seito "「そ……。\n
……ふふふっ」"

hide amuse_b2_5
show amuse_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice sam_g0150
Seito "「あははっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "馬鹿にするでもなく、彼女達は笑い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「もう……、ふふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達が笑っているのを見ると、自分でも笑うしかないような気になる。\n
自然、笑いがこみあげた。"

hide amuse_a1_2
show amuse_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0070
Seito "「ふふっ、だって～……」"

hide amuse_b2_2
show amuse_b2_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0151
Seito "「ねえ？\n
ははっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「笑わないでよ……、はは」"

hide amuse_a2_3
show amuse_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_8")
voice tad_g0071
Seito "「あなただって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人で視線を交わしながら小さく笑いあう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……あなた達は、どこかに行くところだったの？」"

hide amuse_a2_2
show amuse_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tad_g0072
Seito "「ああ、うん。\n
ちょっとね、ゼミの先生に呼ばれているの」"

hide amuse_a2_8
show amuse_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tad_g0073
Seito "「ふふ。\n
私達は、今から疲れてくるってわけよ」"

hide amuse_b2_8
show amuse_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice sam_g0152
Seito "「多分、今期始まる前に提出したレポートのことだと思うんだけどね……。\n
私達の分も、あなたは寛いでちょうだい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「そうね、気楽な新入生のうちにのんびりしておくわ。\n
二人とも頑張って」"

play sound se_0624
hide amuse_a2_3

hide amuse_b1_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はひらりと手をふって、彼女達と別れる。\n
そろそろ夕方だという時間に呼び出されるだなんて、彼女達も大変そうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（本格的に学生生活に入ったら、私もああなるのかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ともあれ、今はまだ、新入生だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（さて……、私も寮内に戻ろう）"

play sound se_0624
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中庭のオブジェは若干不本意な結果に終わったものの、ほとんど見てまわることができた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達の言っていたようにカフェテリアに寄ってから、部屋に戻ろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう思いながら歩き出そうとして、そこでなんだか、嫌な予感がした。\n
もしかすると、いわゆる虫の知らせというやつだったのかもしれない。"

play sound se_0066
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどメモ帳を出した懐を探す。\n
なんとなく、本当になんとなく……、不安になってしまったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（学生証、持っていたかしら……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段は、ジャケットの内ポケットに手帳や、魔法で小さくした杖などと一緒に収めてある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう使うものでもないので、基本的に気にするのはジャケットを換えるときぐらいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうして今この瞬間、学生証のことが気にかかったのかは、分からない。\n
急にだが、無性に気になってしまったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……嫌な予感がする）"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "内ポケットへと手を入れて探る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（これはメモ帳……、これは杖……、あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもなら当たり前のように感じられる、四角形の硬い感触が探り当てられない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……{size=+20}えええっ？{/size}」"

play sound se_0117
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジャケットを慌てて脱いで、内ポケットを丁寧に確認していく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「杖、でしょう？」"

play sound se_0267
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かがみこんで、取り出した杖を芝生の上に置いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「メモ帳、でしょう？」"

play sound se_0267
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メモ帳を取り出して、杖の隣に並べる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……{size=+20}ない{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジャケットの内ポケットの中身はそれでおしまいだ。\n
学生証は出てこない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「えええええっ？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭の中が真っ白になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たかが学生証などと言ってはいけない。\n
世界一の魔法学校の生徒の証明だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "非常に価値があって、闇市などに流れればかなりの高値になると聞いたことがある。当然、生徒には厳重な保管が求められていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（ど、どうしよ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来なければならないもの、あるのが当たり前のものがなくなると、こんなにも焦るものなのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学生証は、校内のあちこちでパスにもなっている。\n
なくしたとなると、学生生活に支障が出てしまうことは間違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（最後に見たのはいつだっけ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使った記憶があるのは図書館だ。\n
見た覚えというのなら、先ほどポケットからメモ帳を取り出すときに、指先にカードの感触があったような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「と、とりあえず、この辺り一帯を探してみなきゃ……」"

with dis
$ hi_mes()

scene bg20_gd_eve
with stripe_l_long
play sound se_0624

play music garden_eve_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、途方に暮れていた。\n
心当たりのあるところはすべて確認したつもりなのに、それでも私の学生証は見つからない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（そろそろ……、ユリウスの小言を覚悟すべきかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……はあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "憂鬱な溜息が漏れる。\n
慌てて探し回ったこともあって、疲れてもいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうせ塔に自首しにいくなら、時間は関係ない。\n
少し休んでから、心の準備をして塔に向かうことにしよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（怒られるだろうなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_9")
T "（……はあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_9")
voice pie_g0045
Pierce "「あれ？\n
君、どうしたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！」"


show pia_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "突然頭上から声がふってきて、顔をあげた。\n
クラスメイトのピアスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "散歩でもしていたのだろうか。\n
座り込んでいる私の前で、首を傾げている。"

hide pia_m_03_1
show pia_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0046
Pierce "「おなかでも痛いの？\n
暗い顔しているよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……大事なものを落としちゃったの。\n
探しているんだけど、見つけられなくって」"

hide pia_m_03_8
show pia_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pie_g0047
Pierce "「落し物？？？\n
君、落し物をしたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「ええ、そうなの。\n
……学生証を落としちゃったのよ」"

hide pia_m_01_10
show pia_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice pie_g0048
Pierce "「学生証！ああ、それは大変だよ！\n
委員長は怒ると怖いからね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……人を余計に憂鬱にさせないでちょうだいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それが分かっているから、暗い顔をしているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_4")
T "（ああ、ユリウスが怖い……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怒らせたことはないが、絶対に怒ると怖いタイプだ。"

hide pia_m_02_2
show pia_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0049
Pierce "「でも大丈夫だよ！\n
俺が助けてあげる！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……はいはい、ありがとう。\n
でも、あなたがユリウスをなんとか出来るとは思えないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスは心優しいが、ちょっとお馬鹿な子だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ短い付き合いとはいえ、クラスメイト。\n
よく分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆にいじられているし、ボリスにはいじめられている。\n
帽子屋寮の双子に追い掛け回されているのも、よく見る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "苛められっこというほど深刻ではなさそうだが、そういうポジション。\n
本人も楽しんでいる節がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなピアスが、あのユリウスをなんとか出来るとは思えない。"

hide pia_m_01_11
show pia_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0050
Pierce "「なんで？\n
[firstname]、君、委員長に何か恨みでもあるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「ええ？\n
いえ、ユリウスに恨みなんかないわ」"

hide pia_m_02_9
show pia_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice pie_g0051
Pierce "「だって、それじゃあ、どうして委員長をなんとかする必要があるの？\n
俺、馬鹿だからよく分かんないよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「いや、だからね？\n
学生証を落としちゃったんだってば」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを報告しにいかないといけないから、気が重いといっているのに。\n
この子は、何を聞いているのだろうか。"

hide pia_m_01_13
show pia_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0052
Pierce "「うん、それは分かるよ？\n
でもそれって、学生証が見つからなかったからでしょう？」"

hide pia_m_01_11
show pia_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0053
Pierce "「つまり、学生証が見つかれば、問題ないんだよね？\n
委員長をどうにかする必要もないよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "{size=+20}「！！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「も、もしかしてピアス、私の学生証持っているの？\n
どこかで拾ってくれたの？」"

hide pia_m_03_1
show pia_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice pie_g0054
Pierce "「ううん、持ってないよ！\n
俺が君の学生証なんか、持っているわけないじゃないか！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "可愛い、ともいえるかもしれない純粋な笑みで、きっぱりと言われてしまった。\n
がくりと肩を落とす。"

hide pia_m_01_6
show pia_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0055
Pierce "「俺は泥棒じゃないよ？\n
だから、君の学生証も持ってない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "的外れ。\n
おまけに、降り掛かってもいない疑いを自分に掛けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……盗んだなんて言っていないわよ。\n
拾ってくれたのかと期待しちゃったの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな言い方をすると酷いかもしれないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "（ピアスなんかに期待するんじゃなかった……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……いいわ。\n
私、もう一度捜してみてから塔に出頭する……」"

play sound se_0052
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふらりと立ち上がる。\n
先ほどから自首やら出頭やら、犯罪者気分だが、ユリウスが相手では間違っていない気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手は頭の固い風紀委員長だ。\n
……と。"

hide pia_m_02_10
show pia_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0056
Pierce "「君、俺の話聞いていないの？\n
その必要はないんだってば！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……でも、あなた、私の学生証知らないんでしょう？\n
それなら、塔に行かないと」"

hide pia_m_01_3
show pia_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice pie_g0057
Pierce "「うん、俺は盗っていないし、知らないけど……。\n
でも、今からすぐに見つけてあげられるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ええ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスの制止を振り切って歩き出そうとしていた私の足は、現金にもぴたりと止まる。"

menu:
    "（嘘だわ）":
        jump gakuen_pierce1_2a
    "（本当に？）" :
        jump gakuen_pierce1_2b
label gakuen_pierce1_2a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（嘘だわ）"

jump gakuen_pierce1_3
label gakuen_pierce1_2b:
$ lovechara_pierce_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（本当に？）"

jump gakuen_pierce1_3
label gakuen_pierce1_3:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（すぐに見つけられる……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「わ、私だって落としたと思ったところは全部確認して歩いたのよ？\n
そんな簡単には見つからないと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見つかったら嬉しいと思う反面、そんな簡単には見つからないだろうとも思う。\n
しかし、ピアスは自信満々だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（これは……、何か根拠があるのかしら？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんせ、ピアスだ。\n
非常に怪しい。"

hide pia_m_03_11
show pia_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0058
Pierce "「俺、そういうの得意なんだよ！\n
普段はあんまりしないんだけどね、君は俺のこといじめないから！」"

hide pia_m_01_10
show pia_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0059
Pierce "「ネズミのことも、嫌いじゃないんだよね？\n
だから俺、君のために探しものしてあげる！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ピアス、探しものが得意なの？」"

hide pia_m_03_6
show pia_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pie_g0060
Pierce "「得意だよ！\n
皆で探せばあっというまだからね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……皆？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ああ、そうか。\n
ピアスだって在校生だもの、友達ぐらいいるわよね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こう見えて、友達が多いのだろうか。"

hide pia_m_01_2
show pia_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0061
Pierce "「皆～～～……！\n
手伝って～～……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……？」"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice oda_g0153
Mouse "「ちゅう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "{size=+20}「え」{/size} "

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice oda_g0154
Mouse "「ちゅうちゅう」"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice oda_g0155
Mouse "「ちゅうちゅうちゅう」"

##special anime"pierce_friends"loop="false"time="1000"]
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "{size=+20}「ええええ」{/size} "


show m_pia1_1 onlayer master
with dis
hide pia_m_02_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "友達にでも声をかけて、探しものを手伝ってもらうつもりなのかという私の予想は見事に裏切られた。\n
いや、ある意味当たってはいたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "友達に声をかけて、探しものを手伝ってもらうというのは正しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ……。\n
その友達が人間ではなかっただけだ。"

play sound se_0166
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「う……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "害意のないものだとは分かっていても、大量のネズミがうごめく様には、やはり一歩引いてしまいそうになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大量のネズミは、以前教室で見たときと同じように、まるでピアスの影からわくかのようにしてぞろぞろと姿を現した。"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0156
Mouse "「ちゅうちゅう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0062
Pierce "「あのね？\n
彼女が落し物をしちゃったんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0063
Pierce "「それですごく困っているから、助けてあげたいんだよ。\n
探してきてくれる？」"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0157
Mouse "「ちゅうちゅう」"

##special anime"pierce_friends"loop="false"time="1000"]
play sound se_0166
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ネズミが、ざわざわ。\n
うごうご……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0064
Pierce "「そっか！\n
みんな優しいね、ありがとう！」"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0158
Mouse "「ちゅうちゅう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今、どうやって意思の疎通が成立したのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通だったら、ピアスが適当に独り言を言っているだけだと見なしてしまうところだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ネズミ達には伝わったらしい。\n
彼の言葉を理解したかのように、その場から散り散りと周囲に散っていく。"

hide m_pia1_1
show m_pia1_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「ピアス、あなた……。\n
ネズミの言葉が分かるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは、ピアスは動物を使い魔として使うことに才能があるのだと言っていた。それが今のところネズミにしか発揮されていない、とも。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0065
Pierce "「変だよね！\n
俺には皆が言っていることがよく分かるのに、他の人は分からないって言うんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0066
Pierce "「君も分からないの？\n
可哀想だね、皆とお話できないなんて可哀想だよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……そう、ねえ。\n
動物と……、ネズミとでも、会話できるのは悪くないかもしれないわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "動物と会話が出来たなら、というのは子供ならば誰もが思い描く夢だ。\n
ピアスは、それを当たり前のようにしてのけている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ問題なのは、ピアスがそれを魔法だと認識していないということだろうか。\n
実際のところ、彼はネズミ達と会話をする際に魔法を使っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしくは、魔法によってネズミを使役している。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……無意識、なのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、その能力はネズミにしか発揮されていないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを魔法として認識し、なおかつ活かすことが出来たのならば、それは素晴らしい魔法の才能だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（もったいないなあ）"

hide m_pia1_2

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice oda_g0159
Mouse "「ちゅうちゅう」"


show pia_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice pie_g0067
Pierce "「う～ん、これは学生証じゃないよ。\n
でも綺麗だから、俺が貰っておくね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すでに何匹かのネズミが戻ってきたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのネズミが持ってきたのは、ビー玉だ。\n
きらきらと輝く様子は綺麗だが、どう見ても学生証ではない。"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0160
Mouse "「ちゅうちゅう」"

hide pia_m_03_2
show pia_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0068
Pierce "「これも、学生証じゃないよ。\n
何かのマジックアイテムかな、これも俺が貰っちゃおう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういうピアスは、ネズミから何だかよく分からないアイテムを受け取っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ネズミが咥えて運べる程度の大きさのもの。\n
そうたいしたものではなさそうだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（いいのかしら、あれ……。\n
落しものは自分の物って……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……探してもらっている立場じゃ、強く言えないか）"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice oda_g0161
Mouse "「ちゅうちゅう」"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice oda_g0162
Mouse "「ちゅうちゅうちゅう」"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice oda_g0163
Mouse "「ちゅうちゅう、ちゅうちゅう」"

play sound se_0066
##special anime"pierce_friends"loop="false"time="1000"]
hide pia_m_01_6
show m_pia1_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういったことが何度も繰り返されて、ピアスの目の前にはあっというまにガラクタの山が出来た。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「なかなか、見つからないわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "数で攻めればすぐに見つかるのかと思ったが、そうでもないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0069
Pierce "「大丈夫だよ！この子達は、探すのが得意なんだ！\n
ねっ？」"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0164
Mouse "「ちゅうちゅう」"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0165
Mouse "「ちゅうちゅう」"

play sound se_0749 volume .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼に促されて、私の学生証ではないものを運んできていたネズミが再び草むらの中へと消えていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（う～ん……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どれくらいそんなことを繰り返しただろう。"

play sound se_0066
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0070
Pierce "「ああ、学生証だ！やったあ！\n
……ん？あれ？違う？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度はまた別のネズミが戻ってきた。\n
口にくわえているのは確かに学生証ではある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「見せてもらってもいい？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_g0071
Pierce "「いいけど、君のじゃないみたい。\n
君、男の子じゃないもんね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……見ての通りよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無造作に渡された学生証に書かれた名前は、私のものではない。"

play sound se_0138
$ flash(.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと指でなぞって魔力を流し込むと、浮かび上がったのは見知らぬ男子生徒の姿だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「後で届けてあげたほうがよさそうね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pie_g0072
Pierce "「どうして？\n
どうして、そんなことするの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え？\n
だって……、学生証がないと困るでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "困るからこそ、私も今こうしてピアスに手伝ってもらって、学生証を探しているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じように学生証を落としたこの男子生徒も、きっと困っているだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0073
Pierce "「へえ、[firstname]、君、優しいんだね！\n
それじゃあ、この学生証は君にあげるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0074
Pierce "「俺のコレクションに加えようと思ったけど、仕方ないよね！\n
君が返したいって言うなら仕方ない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……？\n
コレクションって？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pie_g0075
Pierce "「落しものは拾った人のものだからね。\n
俺、たくさんいろんなものを持っているんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pie_g0076
Pierce "「皆の学生証もそうだし、あとね、お手紙とか書類とか……。\n
たまに宝石とかお金、綺麗なマジックアイテムも落ちているんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「……どれも、ないと困るものよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
voice pie_g0077
Pierce "「落として、見つけられないってことはそれほど大事ってわけじゃないんだよ！\n
だから俺のものになっちゃうんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「そ、そういうものかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice pie_g0078
Pierce "「そういうものだよ。\n
だからね、落ちているものは大体、俺のものになっちゃうんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふふっとピアスは可愛らしく笑ってみせる。私には、それが無知からくるものなのか、それとも何かの悪意が潜んでいるのかの区別がつかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（それって……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……泥棒と、どう違うの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "泥棒と大差ない気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "落ちているものには、落とした人がいる。\n
けれど、ピアスはそこには目は向けていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来の持ち主にとって、いらないものだから落としたんだという妙な理屈で、彼は拾ったものを自分のものにしてしまう。"

play sound se_0105
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0166
Mouse "「ちゅうちゅう」"

hide m_pia1_3
show m_pia1_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0079
Pierce "「あ、あったよ！\n
これ、君のだ、君の学生証だよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「えっ！\n
本当に！？」"

play sound se_0138
$ flash(.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "受け取った、学生証。\n
表面をなぞって魔力を通せば、私の姿が小さく学生証の上に浮かび上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間違いなく、私のものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「……よかったあ。\n
どこで落としちゃっていたのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_8")
voice pie_g0080
Pierce "「よかったね、[firstname]！\n
これで君、委員長に叱られなくてすむよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「ええ、助かったわ。\n
……ユリウスに怒られるなんて、気が重かったもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰に怒られるのもあまり好ましい状況ではないが、ユリウスはその中でも特別だと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「あなた達も、ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスの足元でちょろちょろとしているネズミ達にも、礼を言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大量に増えていて、どれが私の学生証を見つけてきてくれた子なのかの区別はつかない。"

play sound se_0105
##special anime"pierce_friends"loop="false"time="1000"]
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0167
Mouse "「ちゅうちゅうちゅう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返事のように、鳴き声が返ってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0081
Pierce "「皆、ありがとうね！\n
戻っていいよ！」"

hide m_pia1_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスの号令に従って、前に見たのと同じようにネズミ達はピアスの影へと消えていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（どこに隠れているのかしら）"

play sound se_0105 volume .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちゅうちゅうと聞こえていた鳴き声が、次第に遠くなっていった。"


show pia_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0082
Pierce "「ふふ、また宝物が増えた。\n
嬉しいな、嬉しいよ」"

play sound se_0690 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごそごそ、とピアスはネズミ達が拾い集めてきた落しものを懐へとしまう。\n
やっぱり、それを持ち主に返すつもりはないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ネズミと同じく、どこに隠しているのやら。\n
懐にしまえる量ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これでも、強力な魔法の使い手なのだろう。\n
少なくとも、才能はある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（さて、学生証も見つかったし……）"

menu:
    "部屋に帰る。":
        jump gakuen_pierce1_4a
    "食事に誘う。":
        jump gakuen_pierce1_4b
label gakuen_pierce1_4a:
$ lovechara_pierce_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「部屋に帰って休みたいわ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "暗号の勘違いやら、学生証紛失やらで、すっかりくたびれてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（自業自得だったけど、災難続き……）"

hide pia_m_02_7
show pia_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice pie_g0083
Pierce "「ねえ、ねえ、君もう帰っちゃう？\n
俺とごはん食べない？美味しいよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帰りがけ、ピアスに食事に誘われた。\n
そろそろ夕食の時間も近い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかく誘ってくれたのだから、一緒に夕食に出掛けてもいいかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「そうね、美味しいものが食べたいわ」"

hide pia_m_01_10
show pia_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice pie_g0084
Pierce "「君、俺と一緒にごはん食べてくれるの？\n
わあ、君は本当に優しいね！」"

hide pia_m_03_11
show pia_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice pie_g0085
Pierce "「それとも君、ネズミ好きなのかな！\n
嬉しいな、嬉しいよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱあっと、顔を輝かせるピアス。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（自分から誘ったくせに……）"

jump gakuen_pierce1_5
label gakuen_pierce1_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……ねえ、ピアス？\n
よかったら、一緒に夕食どうかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「お礼……、ってことにはならないかもしれないんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食堂には食べたいものを出す魔法がかかっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "奢るといったような形でのお礼は出来ないが、だからといってここで「はい、さようなら」というのも寂しい気がする。"

hide pia_m_01_6
show pia_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Pierce "{size=+20}「！！！！」{/size} "

hide pia_m_01_3
show pia_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0086
Pierce "「な、な、何をたくらんでいるの！？\n
俺をいじめる？いじめる気なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「は……？\n
いや、食事に誘っただけよ？」"

hide pia_m_02_5
show pia_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pie_g0087
Pierce "「う、嘘だあ……。そんなの、信じないよ。\n
俺をいじめる気なんでしょ？」"

jump gakuen_pierce1_5
label gakuen_pierce1_5:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか、哀れになってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……普段、誰かとごはん食べたりしないのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しないのかもしれない。\n
ピアスは、皆にいじられている一方、恐れられてもいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの大量のネズミを見れば、遠巻きになってしまう周囲の気持ちも分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ほら、一緒に食堂に行きましょう？」"

play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、ピアスへと手を差し出した。\n
お礼という気持ちももちろんある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（でも、それだけじゃないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、このクラスメイトに興味を抱いている。\n
ネズミを友達と呼び、自在に操ってみせるピアスに好奇心を抱いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好奇心なんていうと酷いふうに聞こえるが、悪いことだとは思わない。\n
友達になるにも、まずは関心がなくては。"

hide pia_m_01_1
show pia_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0088
Pierce "「手……、つないでいいの？\n
汚いって思わない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……汚いの？\n
手、洗ってない？」"

hide pia_m_03_1
show pia_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pie_g0089
Pierce "「洗っているよ！！\n
俺、綺麗好きなネズミだもん！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「じゃあ、汚くなんかないでしょう」"

hide pia_m_01_8
show pia_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Pierce "「…………」"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おずおずと……。\n
子供みたい、と思っていたのに、その手が私よりも大きくて、少し驚く。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「行こう？」"

hide pia_m_02_10
show pia_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pie_g0090
Pierce "「……うん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "繋いだ手をゆらゆらと揺らしながら、私達は食堂へと向かった。"

hide pia_m_01_5

with dis
$ hi_mes()

scene bg_par15_rg_amu_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_long
##endmemory

scene bg_map_nig
with dis
$ routechara = "Pierce"
jump gakuen_friend_check_amuse
