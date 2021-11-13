label gakuen_blood_end:
scene bg_map_day
with dis
$ clockanim()


play music morning_a_wam

scene bg06_sk_h_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの翌朝。\n
私は非常に気だるい朝を迎えていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜は結局、中庭の騒動が終わった頃合に、撤収する女子生徒の集団の中に紛れ込むようにして自室に帰ったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手伝ってくれた彼女達の姿を探したが、皆が蛍光塗料まみれだったり、ボロボロだったりしたこともあり、見つけることが出来なかった。"

with dis
$ hi_mes()

scene bg25_rr_day
with stripe_l_medium

scene bg_par02_ct_hat_day
with stripe_l_long

play music dining_day_p_wam
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなわけで、朝食の席で会えないかとカフェテリアの入り口近くで待つ。\n
前のストームの翌日と同じで、カフェテリアはいつも以上に賑やかだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆がわいわいと、ブリーズの感想を語り合っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0014
Seito "「昨日のブリーズは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0023
Seito "「うん、何がどうなって、ああなったんだ……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0015
Seito "「さあ……。\n
でも寮長のすることだから、何か色々と……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0024
Seito "「ああ……。\n
とりあえず、後半は普通に進行していたみたいでよかったけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……あれからは、普通だったんだ。\n
よかった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらっと聞こえた男子生徒の会話に、聞き耳をたてる。\n
あの後、どうなったのか気になっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（責任者が混乱を引き起こして、大丈夫なのかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは帽子屋寮の寮長だが、前日の騒動の首謀者でもある。\n
責任問題沙汰になったりはしないのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう心配していたのだが、杞憂で終わりそうだ。\n
なんだかんだと納得させてしまっている。"


show hat_a2_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0053
Seito "「……ん、あら、[firstname]。\n
おはよう、どうしたの？」"

hide hat_a2_8
show hat_a2_8 at left
with dis

show hat_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0060
Seito "「おはよう、[firstname]。\n
もしかして、私達を待っていてくれたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ええ、会えてよかったわ。\n
あれから、大丈夫だった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が何かしたというわけではないが、私がそれが原因でブラッドが気紛れを起こしたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当ならば、ちょっと気になる男の子と男子寮で親睦を深める、なんていう嬉しいイベントだったはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、前半、彼女達は男子寮の中に足を踏み入れることすら出来なかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（突入しちゃってからは、どうなったのか、詳細も分からなかったし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人が応援してくれたからこそ可能だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドならばおそらく私が乗り込んだ後は妨害を止めるよう指示しているはず。\n
そう当たりはつけていたものの、顛末を知らず罪悪感を覚える。"

hide hat_a2_8
show hat_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0054
Seito "「大丈夫どころじゃないわ！」"

hide hat_b1_8
show hat_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0061
Seito "「ええ！\n
大丈夫なんてものじゃ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ええ？\n
駄目だったの？失敗？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先刻漏れ聞いた話では、後半は普通に進行したとのことで安心してしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "全体進行が成功したにしろ、協力してくれた彼女達が失敗では申し訳なさすぎる。\n
一体、どういう顛末だったのだろう。"


play music study_a_wam
hide hat_a2_5
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0055
Seito "「駄目じゃないわ！\n
すごく楽しかった！」"

hide hat_b1_9
show hat_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0062
Seito "「ええ、無茶苦茶で最高だった！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「？？？\n
どういうこと？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（大丈夫じゃないのに、楽しくて最高？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「楽しかった……、ってあの後どうなったの？」"

hide hat_a2_2
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice oda_g0056
Seito "「いつものブリーズよりもよかったってこと。\n
あの後ね……」"

hide hat_b1_2
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice sam_g0063
Seito "「最初は、女子生徒ＶＳ使用人ＶＳ男子生徒、なんていう三つ巴になっていたのよ。\n
その時点で無茶苦茶だったけど……」"

hide hat_a2_2
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice oda_g0057
Seito "「使用人達も、とりあえずよく分かんないけど捕まえとくか～的な適当さでね。\n
いつもより混乱していたの」"

hide hat_b1_3
show hat_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice sam_g0064
Seito "「そう、ストームの夜みたいな感じよね」"

hide hat_b1_8
show hat_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice sam_g0065
Seito "「でも、使用人を蹴散らし、ツインズとエリオット副寮長や、男子生徒までかいくぐって男子寮を目指すなんて、難易度が上がりすぎで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……え～と、それのどこが最高なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……最悪の状況にしか思えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームは、男子生徒と使用人の衝突もイベントのうちだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それと違い、ブリーズは、あくまで隠密行動が基本で、使用人の目をいかに盗んで男子寮に到達するかが醍醐味だったはずだ。"

hide hat_a2_3
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0058
Seito "「途中、あなたが突っ切ったあたりから、全員を妨害するって感じじゃなくなったの」"

hide hat_b1_8
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0066
Seito "「行きたい子は行ってもいいって感じでね。\n
でも、妨害騒ぎもそのまま続行で……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「続行！？\n
ブラッドは、私が侵入したら止めるように指示したって言っていたわ」"

hide hat_a2_3
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice oda_g0059
Seito "「……ふむ。\n
あなたも、成功したみたいね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「あ……。\n
それは……」"

hide hat_b1_3
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice sam_g0067
Seito "「言ったでしょう？\n
行きたい子は行ってもいいって感じだったの」"

hide hat_b1_3
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice sam_g0068
Seito "「行きたい子は行けて、どんちゃん騒ぎを続けたい子は続けられる……。\n
かなり楽しかったわよ？」"

hide hat_a2_3
show hat_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice oda_g0060
Seito "「姿隠しの魔法が下手で、普通なら通り抜けられずに使用人に見つかっちゃうような子でも、行きたいなら通してくれちゃったし……」"

hide hat_b1_3
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice sam_g0069
Seito "「普通なら出来ないような、魔法での対戦も出来たしね！\n
希望者だけっていうのが、かえって盛り上がって……」"

hide hat_a2_8
show hat_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice oda_g0061
Seito "「そうそう、そっちに夢中になっちゃった」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「じゃあ……、あなた達も楽しめたのね？」"

hide hat_a2_8
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice oda_g0062
Seito "「楽しめなきゃ、こんなに盛り上がっていないわ」"

hide hat_b1_3
show hat_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice sam_g0070
Seito "「ああいうのもいいわよね！」"

play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達はそんな話をしながらも、空いている席を探して移動する。\n
それぞれ手元に食べたい朝食を呼び出し、ブリーズの話を続行した。"

hide hat_a2_2
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0063
Seito "「皆、最終的には満足がいったんじゃないかしら」"

hide hat_b1_2
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0071
Seito "「いつもより楽しめたと思うわよ。\n
先刻言ったみたいに、行きたい子は男子寮に簡単に入り込めたし……」"

hide hat_b1_3
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0072
Seito "「大暴れしたい子は使用人や男子生徒とまでやりあえたし……、ね？」"

hide hat_a2_3
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0064
Seito "「使用人相手に挑みたがる男子の気持ちが分かっちゃったわ。\n
大暴れするって楽しいのね～」"

hide hat_a2_3
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0065
Seito "「ええ、楽しかった。\n
またやりたいわ……」"

hide hat_a2_3
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0066
Seito "「男子をぶちのめすのって、快感……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は、本当に楽しげだ。\n
どこか恍惚とした様子で呟く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（いや、その楽しみ方はどうかと……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……まあ、楽しかったのなら何より、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「いいブリーズになったみたいね……？」"

hide hat_a2_3
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice oda_g0067
Seito "「ええ、とっても！」"

hide hat_b1_3
show hat_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice sam_g0073
Seito "「ものすごくね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人、声を揃えて満面の笑顔で言い切られてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜の名残なのか、疲労の色もその顔には見られるものの、基本的には充足感が満ちている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……いいのかしら、これって）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "新たな楽しみ方が出来たようだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ああ、でも目的は達成できなかったんじゃない？\n
男子寮の住人との親睦は深められなかったんでしょう？」"

hide hat_a2_2
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice oda_g0068
Seito "「いやいや、拳で語る友情もあるっていうか……」"

hide hat_b1_2
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice sam_g0074
Seito "「そう、やりあってこそ深まる親交もあるっていうか……」"

hide hat_a2_3
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice oda_g0069
Seito "「うん。\n
今まで以上に、親睦は深まった気がするわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いいの……、だろうか。"

hide hat_a2_3
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0070
Seito "「後半から盛り上がったから、完膚なきまでにとはいかなかったのよね！\n
来年こそは、打倒してみせるわ！」"

hide hat_b1_3
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0075
Seito "「そうね、来年こそは絶対に倒すわ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……え？\n
ちょ、ちょっと待ってよ、来年はもう通常通りのブリーズでいいじゃない」"

hide hat_a2_3
show hat_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice oda_g0071
Seito "「ええ～？\n
せっかく面白かったんだもの」"

hide hat_b1_3
show hat_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice sam_g0076
Seito "「面白いイベントは、後世にしっかり残していかなきゃ駄目よ」"

hide hat_a2_5
show hat_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice oda_g0072
Seito "「ええ、シンフォニアのイベントって、生徒達が発展させていっているんだもの。\n
……きっと、皆も同意見よ、ほら」"

hide hat_a2_8

hide hat_b1_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人の言葉に促されて、私は周囲の声に聞き耳をたててみる。\n
特に選んで聞くまでもなく、周囲は昨夜の話題で盛り上がっている。"

play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0008
Seito "「昨日のブリーズはすごかったなー！\n
女子って、あんなに強かったんだって、ちょっと驚いたよ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0011
Seito "「魔法に物理的な力は関係ないっていっても、イメージとしてな……。\n
強力な魔法だと、肉体的にも負担がかかるから」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0012
Seito "「でも、女子は理論系とか研究系に強いと思っていたけど、実践でも同じくらいで……。\n
正直、見直した」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0022
Seito "「それでね、私がツインズの蛍光ペイントに当たりそうになったとき！\n
彼ったら、私のこと庇って被弾してくれたのよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0138
Seito "「それは気があるって考えていいんじゃない！？\n
いいなあ、私なんて、普通に戦っていたわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0009
Seito "「また、やりたいよなあ。\n
こういうの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0013
Seito "「帽子屋寮の伝統ってことで、ブリーズの中身を変えてもいいんじゃないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0010
Seito "「寮に侵入するのもいいけど、真剣な魔法勝負っていうのもいいイベントだよな。\n
どっちを選ぶかは自由で……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0014
Seito "「そうそう、自由なら気分で決めてもいいわけだし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0011
Seito "「うちの寮の方針にも合致するよな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0023
Seito "「また機会があったら、やりたいわね～！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0139
Seito "「普通に部屋で話すより、一緒に戦うなんて特殊な状況のほうが楽しいものね！\n
またやりたいわ！」"

play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「…………」"


show hat_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice oda_g0073
Seito "「……ね？」"

hide hat_a2_3
show hat_a2_3 at left
with dis

show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice sam_g0077
Seito "「ほら、楽しめているでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、本当のようだ。\n
昨夜の妨害騒ぎは、帽子屋寮の住人達に受け入れられてしまったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（こうやって、ストームやらブリーズなんていう伝統も出来上がってきたのかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初はイベントのつもりでやったことではなかったとしても。\n
こんなふうに受け入れられていく図が想像できる。"

hide hat_a2_3

hide hat_b1_3

with dis
$ hi_mes()

scene bg_par02_ct_hat_day with Dissolve(.8)

scene bg_par15_rg_hat_day
with stripe_l_long

play music corridor_day_p_wam
play sound se_0774
play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝食を食べ終わった後、私達はそのまま一緒に登校することにした。\n
もちろん所属するクラスは違うので、校舎までの道のりが一緒というだけだ。"


show hat_a2_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0074
Seito "「あ、そうだわ。\n
私、気になっていたんだけれど……、あなた、身体は大丈夫？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "{size=+20}「え！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "並んで歩く中、さりげなく、何気なく。\n
言われた言葉に、咄嗟に反応してしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「な、ななな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（な、何かおかしかった……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもどおりを心がけていたつもりだったのだが。"

hide hat_a2_8
show hat_a2_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0075
Seito "「え、いや、ほら、結構無茶な突入の仕方をしちゃったから……」"

hide hat_a2_8
show hat_a2_8 at left
with dis

show hat_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0078
Seito "「冷静になって考えたら、友達に魔法をぶつけるなんて有り得ないわよね……」"

hide hat_a2_8
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0076
Seito "「ええ、イベントが終わって正気に戻ったらぞっとしちゃった。\n
相当危険だったわよね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「{size=+20}あ{/size}。\n
そうね、そうよね……」"


play music gag1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（そっちか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思えば、当然。"

hide hat_a2_3
show hat_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

hide hat_b1_8
show hat_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "立ち止まった二人に、横合いから覗き込まれて凝視された。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「な……、な、なによ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じーーーーーーーーー……、っと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線が痛い。\n
何かを探るようでいて、待っているようでもある。"

hide hat_a2_8
show hat_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「……[firstname]？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「なに……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真顔で名前を呼ばれて、身構える。\n
何を言われるのか……。"

hide hat_a2_8
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0077
Seito "「顔、赤いわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "{size=+20}「！！！！！！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "指摘されて、余計に顔に熱が集中した。\n
ばっと、顔を手で覆ってしまう。"

hide hat_a2_2
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

hide hat_b1_8
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

hide hat_b1_3
show hat_b1_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0079
Seito "「……寮長、手、早すぎ」"

hide hat_a2_3
show hat_a2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0078
Seito "「……さすが、我が寮の主」"

hide hat_a2_6
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0079
Seito "「でもね、[firstname]？\n
ブリーズで押しかけて、さらに奪われてきてどうするのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「そ、そんなこと言われても……！」"

hide hat_b1_6
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice sam_g0080
Seito "「……その様子じゃ、目的の物も、取り戻せていないんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「う……」"

hide hat_a2_2
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice oda_g0080
Seito "「もう……っ！\n
今は授業もあるから勘弁してあげるけど、あとでじっくり話聞かせてよね？」"

hide hat_b1_3
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice sam_g0081
Seito "「詳しくよ！？\n
じっくり、聞き出してあげるんだから……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「い、嫌よ……っ！？\n
なんで、そんな恥ずかしいこと……！」"

hide hat_a2_3
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice oda_g0081
Seito "「あら。\n
恥ずかしがるようなこと、されたのね！？」"

hide hat_b1_3
show hat_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice sam_g0082
Seito "「みっちり聞かせてもらうから……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_4")
T "「！？\n
勘弁してよ……っ！」"

hide hat_a2_2

hide hat_b1_2


scene bg06_sk_h_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして、騒がしかった一週間は終わり。\n
日常が始まる。"

with dis
$ hi_mes()

scene bg06_sk_h_day with Dissolve(.8)

scene bg06_sk_h_eve with Dissolve(1)

scene bg_map_eve with Dissolve(1)

scene bg_par15_rg_hat_eve
with stripe_l_long

play music hatter_garden_p_ali
play sound se_0200

scene bg_par12_hct_eve with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後のお茶会は、もはや私の日課だ。\n
クラスメイトや、寮の友人らと予定がない限りは、こうしてテラスに顔を出してブラッドにお茶をご馳走になっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……この人、一体、いつ授業受けているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "通常の生徒ではなく、研究員だとしても、それに応じたゼミや会議がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、私がいつ来ても、ブラッドはテラスにいた。\n
そこで紅茶の満ちたカップを傾け、悠々と過ごしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（大丈夫なの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日中、学校でその姿を見たことがないというのも、どうかと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昼はだるいだの、日が出ている間は動く気がしないだの、そういう戯言を日頃聞かされていることもあり、余計不安になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……魔法使いとしては、優秀なんだろうけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このシンフォニアで、寮長を任されているぐらいなのだ。\n
私が心配してやるような必要はないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう結論づけて、私も目の前の紅茶のカップを手に取る。"

play sound se_0174

show bra_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0331
Blood "「……ふと思ったんだが。\n
お嬢さん、たまにはこちらに座ってみないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、そのタイミングで口を開いたブラッドに、私は紅茶に口をつけることなく動きを止める。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何を言い出すのかと、視線をやれば、ブラッドがこちらと言って示したのは彼の隣だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「そこは、エリオットの席でしょう？」"

hide bra_m_01_2
show bra_m_03_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice blo_g0332
Blood "「別に、厳密にそう決まっているわけではないよ。\n
それに、今この場所に奴はいない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ええー……？\n
二人並んで座るなんて、おかしくない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おかしい。\n
カウンター席ならばともかく、お茶会の席で二人しかいないのに、わざわざ並んで隣に座るなど不自然だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通は対面の席。\n
そう、今私が座っているような形で落ち着く。"

hide bra_m_03_16
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0333
Blood "「……おかしいことは、ないだろう？\n
お嬢さん、人間のパーソナルスペースというものは横のほうが狭いんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「パーソナルスペース？」"

hide bra_m_03_4
show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice blo_g0334
Blood "「パーソナルスペースというのは、人間の持つ個人的な空間のことを指す。\n
つまり、他人にそこに侵入されて不安や不快を覚える距離のことだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（言葉は知っているけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……博識ね。\n
で、それがどうしたの？」"

hide bra_m_02_2
show bra_m_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0335
Blood "「個人差はあるが、概ね人のパーソナルスペースというのは横に狭い」"

hide bra_m_02_15
show bra_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0335_5
Blood "「つまり……、正面３０センチ以内に他人がいると落ち着かなさを感じても、隣ならば肩が触れ合う程度に近くとも気にならない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「へえ、言われてみたらそうね。\n
その通りだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じ距離でも、その相手が隣なのか、正面なのか、後ろなのか、で耐えられる度合いは変わってくる。それを、パーソナルスペースと呼ぶらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「だから、移動しろ、って？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（もったいつけて……）"

hide bra_m_02_5
show bra_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice blo_g0336
Blood "「ああ、是非とも。\n
……どうかな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

menu:
    "隣に移動する。":
        jump gakuen_blood_end2a
    "不審に思う。":
        jump gakuen_blood_end2b
label gakuen_blood_end2a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこまで解説されて促されると、移動しないのも悪い気がしてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（パーソナルスペース、ね）"

play sound se_0160

play music blood_t_ali

show m_bra_end_1a onlayer master
with dis
hide bra_m_02_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ティーカップをソーサーごと持ち上げて、彼の隣へと移動した。\n
普段ならばエリオットの定位置である、ブラッドの左隣の席だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_14")
T "（……新鮮だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "隣に、ブラッドがいる。\n
目の前には誰もいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段ならば、目の前の人物との会話に気をとられ、見過ごしてしまいがちな赤薔薇がいつもより綺麗に見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「こういうのも、悪くないわね。\n
位置を変えると、いつもと違って新鮮だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice blo_g0337
Blood "「そうだろうとも。\n
私も、楽しめる」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……ん？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今、不穏な言葉を聞いたような気がした。\n
楽しめるとはどういうことだ。"

hide m_bra_end_1a
show m_bra_end_2a onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "身構えるよりも先に、するりと伸びてきたブラッドの左腕が私の腰を抱いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0338
Blood "「対面の席では、手が届かないからな……。\n
常々、つまらないと思っていたんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「手が届くからって、面白くなんかならないわよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice blo_g0339
Blood "「いや、私は面白いぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「面白くなくていいっ！\n
こら、放しなさいよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抱き寄せられて、距離がより近くなる。\n
紅茶と薔薇とが混じる香りがふわりと鼻先を掠めて、そこから連想する記憶に頬が赤らむ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0340
Blood "「ああ、お嬢さんもまんざらでもなさそうじゃないか。\n
……ふふ、任せておきなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「何を！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice blo_g0341
Blood "「身も、心も」"

hide m_bra_end_2a

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つっこみのつもりで言った言葉に、まともに返されて頭がくらくらとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、くらくらとしている場合ではない。\n
ここはテラスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前のカフェテラスのときよりマシだが、公共の場。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一般の生徒が訪れる可能性はほとんどゼロに近いが、エリオットや双子達が顔を出す可能性はかなり高い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな場所で何をしようというのか。\n
いや、何と問うのも恐ろしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "「い・や・よ！！！\n
どっちも断る！」"


show bra_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice blo_g0342
Blood "「おや、つれない。\n
……まあ、いつものことか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "はっきりと拒絶して、べりっと腰に絡みついていたブラッドの手を引っぺがして脱出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやって逃がしてくれるあたり、ブラッドとしてもあまり本気ではなかったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この男が本気だったならば、私が何をしようと、何を言おうと目的を達成している。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「そうよ。\n
何もかもを断るのはあなたの専売特許じゃないの」"

jump gakuen_blood_end3
label gakuen_blood_end2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「パーソナルスペースの話は分かったけれど……。\n
それでどうして、私に隣に来いなんて言うの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とびきり美味しい紅茶。\n
ご馳走してくれる主催の意向にはなるべく沿いたいとは思うのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（ブラッドだもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その意図が読めないままに、動くのは危険だ。\n
そう判断せざるを得ないだけの時間は、この男と共に過ごしている。"

hide bra_m_03_12
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0343
Blood "「この、ティーテーブルもそういった概念を参考にして、作られているわけだ。\n
人が向かいあわせに座っても、圧迫感を覚えない適切な距離が保たれている」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ええ、そうね……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（だから？\n
それが、どうしたっていうのよ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やっぱり意図が分からない。\n
博識を披露したかっただけ、というわけでもないだろうし……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「それで、どうして席移動の話になるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正面での適切な距離と、隣で適切な距離が異なるというは分かった。\n
だが、どちらも適切な距離であるならばそう差はないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "距離に変化はあっても、どちらも適切であるならば感覚的な違いもない。\n
それならば私は、まだ相手の顔を見ることができる対面のほうが落ち着く。"

hide bra_m_03_15
show bra_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは、訝しげな視線を向ける私へと、なかなか通じない意図に焦れたように溜息をつき。\n
口を開くと、きっぱりと言い切った。"

hide bra_m_03_13
show bra_m_02_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0344
Blood "「正面に座られていると、手が届かなくて面白くない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「面白くなくて結構よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "{size=+20}（手が届いたら何をするつもりなのよ）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「席移動は、お断りします」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは帽子屋寮幹部にほぼ占有されているとはいえ、立派な公共施設なのだ。\n
そんな場所で、何をしようというのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じろりと睨んでやれば、ブラッドは面白くなさそうに息を吐く。"


play music blood_t_ali
hide bra_m_02_18
show bra_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0345
Blood "「断る……、か。\n
昨夜の私と同じようなことを言うね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_4")
T "「そうだったわね。\n
でも、何もかもを断るのはあなたの専売特許じゃないのよ」"

jump gakuen_blood_end3
label gakuen_blood_end3:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_3")
T "「真似をしたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドときたら、昨夜は断りっぱなしだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手紙を返すことを断り、私を帰すことも下ろすことも、自分が医務室へ行くことも断った。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_6")
T "（あ……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「そうだわ！\n
怪我！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「平気だったの！？\n
あのときだって、無茶して……」"

hide bra_m_03_6
show bra_m_02_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice blo_g0346
Blood "「……無茶に関しても、君の専売特許ではなかったということだろう。\n
それより、我慢をするほうが堪える」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「我慢って……」"

hide bra_m_02_18
show bra_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice blo_g0347
Blood "「触れ合うことくらい、いいだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「だ、駄目よ……」"

hide bra_m_03_13
show bra_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice blo_g0348
Blood "「どうして？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（どうして……、ってそりゃあ、ここが学校だから）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脳裏に即座に浮かんだ返答は、あえて口にすることはせず、呆れた視線を向けるだけにしておく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくら自由度の高いシンフォニアとはいえ、男女で寮の間の行き来はそう簡単なことではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "万が一、見つかりでもしたら、厳しい処罰を受けることになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう考えると、ストームやブリーズというイベントがいかに特別なものなのかが分かるというものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子が男子寮に忍び込む。\n
男子が女子寮に忍び込む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはブラッドの言う、破ってはいけないルールに抵触する行為にあたる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、あの日以来私もブラッドの部屋を訪れたことはないし、ブラッドも私の部屋に訪れたことはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会うのはもっぱらここ。\n
物足りなくも安全な、公共の場だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……紳士的にね。\n
紅茶好きのあなたなら、お茶会は聖域でしょう？」"

hide bra_m_02_6
show bra_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むっつりと眉間に皺を寄せて紅茶を飲むブラッドをよそ目に、私は美味しい紅茶を堪能することにした。"

hide bra_m_02_3

with dis
$ hi_mes()

scene bg_par12_hct_eve with Dissolve(.8)

scene bg_par15_rg_hat_eve
with stripe_l_medium

scene bg06_sk_h_eve
with stripe_l_medium

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_day with Dissolve(1)

play music secret_nig_p_wam

scene bg06_sk_h_eve with Dissolve(1.2)


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice blo_g0349
Blood "「さあ。\n
どうぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その日。\n
いつものようにテラスにお茶をご馳走になりにいったはずの私は、一つの部屋に連れ込まれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "テラスと同じく男女共用区域の中にある場所。\n
だが、こんな場所があるとは知らなかった。"


scene bg_par05_br_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう広くもない部屋には、大きなカウチが一つと、テーブルが一つきりしかない。\n
そして、壁は全面本棚になっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いかにも誰かの書斎、読書を楽しむだけの部屋といった具合だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「……ここは？」"


show bra_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice blo_g0350
Blood "「私の秘密の部屋だ。\n
お気に召したかな、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「秘密の部屋！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「秘密の部屋って……、選ばれた者しか入れなかったり、一度足を踏み入れたら二度と出れなかったり、シンフォニアの秘宝が隠されてたりする……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……とかいうあれ？」"

hide bra_m_03_9
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice blo_g0351
Blood "「ああ、お嬢さんも噂は知っているのか。\n
だが、残念ながらこの部屋は違う」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「まあ、そうでしょうね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの秘宝がありそうには見えない。"

hide bra_m_03_4
show bra_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0352
Blood "「秘密の部屋ではあるが……。\n
別に、存在は隠されていないからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……秘密の部屋なのに、隠されていないの？」"

hide bra_m_01_12
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice blo_g0353
Blood "「私しか、使わない。\n
私しか、入ることを許していない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……横暴だわ」"

hide bra_m_03_10
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice blo_g0354
Blood "「寮長なんていう面倒くさい仕事を引き受けているんだ、これぐらいは役得だ。\n
他の寮長も、大体がそういうエリアを持っている」"

hide bra_m_02_8
show bra_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice blo_g0355
Blood "「……秘密の部屋の噂というのも、そこから大袈裟に広がったのかもしれないな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「ふうん……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（意味ありげね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの秘宝やら、入ったら出られなくなるようなトラップやら。\n
ここがそうでないにしろ、ブラッドなら真相を知っていそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……ま、聞いても、素直に教えてくれるとは思えないわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの秘宝でも見合わないほどの見返りを要求されそうだ。"

hide bra_m_02_5
show bra_m_02_20 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0356
Blood "「ここならば、人目を気にしなくていいだろう？\n
……おいで、お嬢さん」"


play music flower_eve_p_wam

show m_bra_end3 onlayer master
with dis
hide bra_m_02_20

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドはカウチへと足を上げて座ると、その腰のあたりへ招いた。\n
私が座ると、当たり前のようにブラッドの腕が緩く腰に回る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして触れられるのは、久しぶりだ。\n
ほぼ毎日のように、テラスでの茶会で顔を合わせているというのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（学生だものね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通の学校ならば、校外や、互いの家などを行き来できる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、全寮制で、生徒の出入りが厳しくチェックされるシンフォニアにおいてはそういったことが難しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が特に抵抗することなく、おとなしくカウチに座ったのも、そのせいだ。\n
軽く触れ合うこともままならないというのは、私だって物足りない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かといって、過激な接触を求めているわけではないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（言い訳じみている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "素直になるのは難しい。\n
ブラッドはそれもいいと受け入れているが、つくづく物好きな男だと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……ねえ、ブラッド。\n
いいかげんにあの手紙、返してよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう誤解はとけたはずだ。\n
あれは、恋人に向けたものではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "宛先の人物の行く末すら、私は知らずにいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0357
Blood "「……未練があるのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、私があの手紙の話題を持ち出すたびに、ブラッドは不機嫌になる。\n
今も眉根を寄せて、嫌そうな顔をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

hide m_bra_end3
show m_bra_end4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の腰に回されていた手を、ゆらりと閃かせると、まるで魔法のようにその手の中にあの封筒が現れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（……って、魔法よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやらブラッドは、あの手紙を大事に手元に置いてあるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「未練なんかないわよ。\n
ただ……、あなたが持っていることが嫌なの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……いえ、他の誰でも嫌だけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（あなたが持っているのは、特に）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ、幼かったころの恋心だ。\n
つたないながらの精一杯の気持ちをこめて書いた、初めてのラブレター。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを、現状付き合っている男に所有されているというのは、どうしたらいいのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（付き合って、いるのよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "色々と疑問符のつきまとう付き合い方だ。\n
その上、宛先の違うラブレターを後生大事に保管されてしまっていては身動きがとれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「ねえ……。\n
お願い」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "進展させたい。\n
変化を、あの手紙は阻害する。"


play music memory1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0358
Blood "「……私は、君を泣かせたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……いきなり、何の宣言？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice blo_g0359
Blood "「私だけのために、君を泣かせたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手の中で、封筒を回してみたりと弄びながら、ブラッドはしみじみと言った。\n
私は眉を寄せる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0360
Blood "「君の部屋から拝借した本にも、この封筒にも……、涙の痕がある」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "指摘されて息を呑んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "失恋を封じた過去を思い出す。\n
涙も無縁ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉にもらった可愛らしい恋愛詩集に、渡せなかったラブレターを挟んで、棚にしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今思うと、ずいぶんとロマンチックな感傷にも思えるが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（陶酔型の自虐趣味だわ。\n
冷静に考えると、悪趣味）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……だから嫌だったのよ。\n
そういうの、あなたって気付く人だから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他人のことなんてどうでもいいというふうに見せながら、それでいて観察眼の鋭い男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、私が気付いてほしくないことにも気付く。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0361
Blood "「……[firstname]、私は狭量な男なんだ。\n
君に涙を流させた男を、殺してやりたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは睦言のような言葉だった。\n
彼が似合わないからよしておくと止めた、ベッドで囁く甘い言葉。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうに感じる、あまやかな囁き。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_11")
T "（こんな言葉を、こんなに甘く口にするなんて）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "君を泣かす奴を許さない、なんていうのは恋愛小説の中ではよく見るフレーズだ。\n
だが、彼が言ったのはそんな漠然としたものではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今は流れていない涙を拭うよう、手紙を持ったままのブラッドの手指が、私の目元に触れた。\n
頬を、指腹が撫でる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0362
Blood "「君を泣かせていいのは、私だけだ。\n
だから、そんな男に泣かされたことなんか忘れてしまえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「無理よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（忘れるなんて、無理）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice blo_g0363
Blood "「ならば、月並みだが……。\n
私が忘れさせてやろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……本当。\n
芸のない台詞ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice blo_g0364
Blood "「……ワンパターン、か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「……定番から、広げていくんでしょう？」"


play music happy_a_ali
hide m_bra_end4
show m_bra_end5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頬に触れていた手がするりと後頭部へとまわって、引き寄せられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "上から口付けるようにして、キスを交わす。"

play sound se_0469 volume .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かさついた小さな音が耳に届く。\n
ブラッドが無造作に放った手紙が、床に落ちる音だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0365
Blood "「ああ、しかし……、忌々しいな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キスの合間に、ブラッドが毒づく。\n
あまやかさはどこへやら、呪うような声音だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0366
Blood "「かつての恋心を君に返してやるつもりはない。\n
だからといって、捨ててしまうのも癪だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0367
Blood "「形あるものは奪えるが、形のないものを奪うのは難しい。\n
……面倒な」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……私も、面倒だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice blo_g0368
Blood "「そう、君が一番の面倒ごとだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「忘れていない？\n
私にとっても、あなたは面倒な人なのよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice blo_g0369
Blood "「……ああ、どうして私はこんな面倒ごとに首をつっこんでしまったのか。\n
忌々しい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらり、と。\n
視線だけで燃やしてしまえそうな眼で、ブラッドが床に落ちた手紙を一瞥する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな様に、不思議と癒される。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昔の傷などないと思っていた。\n
安らぎを感じる場もおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、こんな悪態に似た応酬に私は確かに癒されていた。"

hide m_bra_end5
show m_bra_end6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0370
Blood "「忘れてしまえ」"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "また、引き寄せられる。\n
今度は顔だけでなく、身体ごと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私を引き寄せながら、ブラッドは逆に身を起こす。\n
キスを交わしながら、器用に体勢を入れ替えられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0371
Blood "「忘れるんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "繰り返し、ブラッドが囁く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……無理）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "繰り返す口付けに上がる息の下、思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "忘れようにも、忘れるべき記憶はもう遠い。\n
かつて大好きで、あんなに憧れた人の顔を、今はもう思い出すことも出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思い出せないものを、忘れることなんて出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほど眼前にあった懐かしい手紙からは、ここしばらくですっかり匂いが移ったのか、紅茶の匂いがした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶と、薔薇。\n
ブラッド＝デュプレの匂いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの手紙の符号は、すでに彼ではなくなった。\n
これから先、あの手紙を見て思い出すのはきっと、ストームとブリーズの夜だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今、目の前にいる、彼のこと。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（あの手紙）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドから取り返したら、自らの手で処分してしまおうと思っていた。\n
悲しくてみっともない過去を、清算するつもりで燃やしてしまおう、と。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、やっぱり惜しい。\n
もうすでに、新しい思い出が上書きされてしまったから。"

hide m_bra_end6
show m_bra_end7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……っ、それ。\n
あなたが、持っていてくれていいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice blo_g0372
Blood "「君はやはり……、たいした女だな。\n
昔の男への恋心を、こうして私に託すとは」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "未練を捨てないのかと、責めるように問う。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0373
Blood "「……まあ、いい。\n
今、君を泣かせるとしたら、この私だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（今、私がラブレターを送るとしたら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「泣かせないでよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice blo_g0374
Blood "「……ふん。\n
たっぷり、なかせてあげよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なく、の漢字変換やら、意味が違うように聞こえたのは、その言葉の受け取り手である私の問題だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（いえ、嫌な意味で正解な気がする……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大きな手のひらが、器用に制服をまさぐり、ボタンを弾いていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "秘密の部屋。\n
男女共同区域にある一室。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校内に変わりはない。\n
そして、私達は将来を誓い合ったわけでもなく、それどころか恋人同士なのかすら疑わしい関係。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_9")
T "（姉さんが知ったら、卒倒モノね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_9")
voice blo_g0375
Blood "「後で、君にトラップを抜ける方法を教えてやる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「トラップ？\n
トラップって……、あの夜間外出禁止の？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_6")
voice blo_g0376
Blood "「ああ、そうだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここシンフォニアでは、定められた時間以降の外出が校則で禁じられている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子寮であれば、女子寮内で部屋の出入りは自由だが、寮から外に出るようなことは禁じられているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当然、寮のエントランスには使用人が控えているから、普通に出入りすること自体が無理。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ここは世界一の魔法学校。\n
生徒だって、優秀なる魔法使いの卵。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓から浮遊で、姿隠しの魔法で……、と。\n
正規の手段以外で外に抜け出す方法はいくらでもある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういったことに備え、魔力を感知して反応するよう仕掛けられていた。\n
生徒間では、トラップと呼ばれている、それらの仕掛け。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姿隠しを行おうが、その魔力を感知されてしまえば、脱走はすぐに使用人達にばれてしまうことになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「あれ、抜ける方法なんてあるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまでにも、生徒同士の雑談の中で、トラップのことが話題になったことはあった。しかし、それが突破可能なんていうのは初耳だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0377
Blood "「誰にでも思いつく方法、というわけではないがね。\n
出来ないことはない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "器用に指先をひらめかせては、私の服をはだけていきながら、ブラッドはつらつらと語る。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0378
Blood "「男子と女子の寮の壁を越えることは、曲げられないルールだが……。\n
夜遊びは逸脱可能な範囲のルールだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（相変わらず、無茶苦茶で勝手な理屈）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「それで……、それを私に教えてどうするの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice blo_g0379
Blood "「決まっているだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは、唇を吊り上げて笑う。\n
いかにも、悪役らしく。"

hide m_bra_end7
show m_bra_end8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0380
Blood "「私と、夜遊びをするんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉と同時に唇が首筋に押し当てられて、ちくりとした痛みが刻まれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "吐息が跳ねる。\n
唇の触れた場所が、熱を持つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今は見えないが、きっと痕も残っているだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（ごめんなさい、姉さん）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここにいない人に、謝罪する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はそのうち、ブラッドに教えられた方法を使って自ら夜遊びに繰り出すだろう。\n
夜のひそやかな時間を、この男と過ごすために使うようになるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……私、やっぱりあなたの言う通りの女なのかもしれないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たいした女だと、ブラッドはそんなふうに言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0381
Blood "「実際、そうだろう。\n
……私に似合っている」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼には似合わない、あまやかさが戻る。"

with dis
$ hi_mes()
hide m_bra_end8


scene bg_par05_br_eve with Dissolve(.8)

scene bg_par15_rg_hat_eve
with stripe_l_medium

scene bg06_sk_h_eve with Dissolve(1)

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_day with Dissolve(1)

scene bg06_sk_h_eve with Dissolve(1)

play music evening_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "時間は流れていく。\n
穏やかに、波乱に満ちて。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "矛盾しているようだが、言葉のままなのだから仕方がない。\n
学生として保護された安全な場所の中で、ぎりぎりの綱渡り。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初に寮を選ぶ際に聞かされた、帽子屋屋敷は物騒でスリルに満ちているという言葉に嘘はなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつのまにか私もそんな日々に適応して……。\n
気付いたときには、学期末の試験も終了し、長期休暇が目の前に迫っていた。"


play music secret_day_p_wam

scene bg_par12_hct_eve with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「……絶対に、嫌よ」"


show bra_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice blo_g0382
Blood "「……そんなに反対するようなことでもないだろうに。\n
頑固なお嬢さんだな」"

hide bra_m_02_13
show bra_m_02_13 at left
with dis

show eri_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice eri_g0014
Elliot "「そうだぜ、[firstname]。\n
別にいいじゃねえか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「嫌よ！\n
断るわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は拒絶を強調すべく、語気を強めた。\n
いつのまにか、「断る」は私のほうの口癖になってしまっている。"


play music hatter_garden_p_ali

show m_bra_end9and11 onlayer master
with dis
hide bra_m_02_13

hide eri_m_01_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつものテラスでの茶会の席。\n
今回はエリオットと双子も一緒で、ティーテーブルの上には所狭しと茶菓子が並んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットの目の前だけが、オレンジ色に染まっているのもいつもの光景だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0048
Dee "「いいな、いいな、ボス。\n
僕らも連れて行ってよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0049
Dam "「僕らも行きたいよ、ボス。\n
旅行なんて羨ましい」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0015
Elliot "「ば～か。ブラッドとこの子の二人だけで行くんだぜ？\n
特別な旅行に決まってるだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "{size=+20}「決まっていないわよ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice blo_g0383
Blood "「ああ、その通り、特別な旅行なんだ。\n
さすがは私の腹心だな、エリオット」"

hide m_bra_end9and11
show m_bra_end10 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice blo_g0384
Blood "「……それほど出来た腹心なら、そのオレンジ色の物体をもう少し横に寄せるくらい、造作もないだろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice blo_g0385
Blood "「避けてくれないか、先ほどからちらちらと視界に入るんだ。\n
その、目に痛いほど鮮やかなオレンジが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice eri_g0016
Elliot "「ああ、すまねえ。\n
ほら、これで手が届くだろ？」"

play sound se_0545
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice blo_g0386
Blood "「……私は、{size=+20}退けろといっているんだ{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice eri_g0017
Elliot "「ええ！？\n
これ、最高級のにんじんで作ったキャロットケーキなんだぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_9")
voice eri_g0018
Elliot "「ブラッド、食欲ないのか？\n
[firstname]、あんたが冷たいからブラッドが落ち込んじまってるじゃないか！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは上機嫌だろうが落ち込んでいようが、エリオットの愛好するオレンジ色の食物を口に入れるようなことはないと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（いや、むしろ、そのオレンジもどきのせいで落ち込んでいるんじゃないの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちら、と見やったブラッドは、なんとも言いがたい顔をしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も同様。\n
エリオットに悪意がないのが分かっている分、無碍にすることも出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（ウサギだし……。\n
仕方ないわよね……、ウサギだし）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice blo_g0387
Blood "「ああ……、そうだな、私は落ち込んでいる。\n
お嬢さん、君がつれないからだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（嘘おっしゃい）"


scene bg06_sk_h_eve
with dis
hide m_bra_end10

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「泣き落としされても、断るわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "再度言い切って、私は紅茶のカップを口元へと運ぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "長期休暇が近づくにつれ、私とブラッドの間ではこの話題が何度も繰り返されている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初は、長期休暇はどう過ごすのか、なんて他愛もない話題だったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "多くのシンフォニアの生徒達が、長期休暇には実家へと里帰りをしていく。\n
自然な流れとして、私も、実家に帰ろうと思っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが、とんでもないことを言い出すまでは。"


play music blood_t_ali

show m_bra_end9and11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0388
Blood "「いいじゃないか、君のご実家を訪ねることぐらい。\n
やはり、ご挨拶は大事だろうからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「いらないわよ！\n
結構です！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう。\n
ブラッドは長期休暇を利用して、私の実家までついてくるなどと言い出しているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0019
Elliot "「なんで駄目なんだ？\n
別にいいじゃねえか、実家に人を呼ぶぐらいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0050
Dee "「うん！\n
僕もお姉さんの実家に行きたいよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0051
Dam "「そうだよ！\n
僕だって行きたいよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「駄目よ。\n
あなた達も、帰るなら、自分の実家に帰りなさいよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだって、人の実家に押しかけたがるのか。\n
双子は拗ねたように、唇を尖らせている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな姿は普通の子供のようで、別に２・３日ならいいわよと口走りたくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、ここで懐柔されるわけにはいかない。何故なら、彼らのボスが私の言質をとろうと、てぐすねひいて待ち構えているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0389
Blood "「そこまで拒絶されると……。\n
何か、私に見られてはまずいものがあるのかと勘繰りたくなるな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「ないわよ、そんなもの。\n
ただ……、いきなりあなたなんて連れて行ったら、家族がパニックよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice blo_g0390
Blood "「いきなりじゃないだろう。\n
事前に通告している」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いきなりでなくとも、確実に大パニックだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋人ができた、なんて。\n
報告すらしていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、いきなり実家に男性を連れて帰るなんて、いくらなんでも段階を飛ばしすぎている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「私、家族に、あなたのことを話していないのよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice blo_g0391
Blood "「では、話すといい。\n
どうして、話さないんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「話すと揉めるからに決まっているでしょう。\n
第一、実家まで来て、なんて挨拶するつもりなのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は年頃の娘だ。\n
下手に恋人が出来たなどと報告したら、余計な波風をたてるだけ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0392
Blood "「それは、まあ。\n
娘さんをくださいと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "{size=+20}「帰って！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さらに段階を飛ばしている。\n
実家に挨拶でその台詞は、笑えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ実家に来たわけでもない男に、つい帰れなんて口にしてしまう。\n
塩もまきたいくらいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0052
Dee "「でも、お姉さん。\n
外堀を埋めるのって大事なんだよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0053
Dam "「そうそう、家族に認められない恋愛なんて、長続きしないよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……どこで、そんな言葉覚えてきたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子にまでもっともらしい顔で説得されそうになって、頭を抱える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "家族に認められる云々、というのは、もっとちゃんとしたお付き合いを経たカップルのいうことではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とブラッドには当てはまらない……、ような気がする。\n
何せ、まだこういう関係になって、それほど時間は経っていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（いや、それ以前の問題よ。\n
まだ、まともに告白すらしていない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それで、実家に挨拶とは。\n
とても正常とは言い難い手順の踏み方だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「家族に挨拶に行く、っていうのは……。\n
もっと、こう、時間を重ねたカップルのすることでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice eri_g0020
Elliot "「そっか？\n
結婚したいって思ったら、すぐにでも必要だろ？」"

play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "{size=+20}「！！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このウサギさんは、何を言い出すのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "度肝を抜かれすぎて、せっかくの美味しい紅茶が気管に入った。\n
げふげふっと咳き込む。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_6")
T "「げほ！\n
けほけほ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "息が苦しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0021
Elliot "「だ、大丈夫か……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_13")
T "（大丈夫じゃないわよ！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怒鳴りつけてやりたいものの、声が出ない。"

hide m_bra_end9and11
show m_bra_end12 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0393
Blood "「そんなに驚くことではないだろうに……。\n
お付き合いさせていただいているからには、実家への挨拶は果たすべき務め」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0394
Blood "「いずれ男に訪れる試練だ。\n
もちろん、私とて避けて通るつもりはない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0022
Elliot "「さっすが、ブラッド。\n
かっこいいぜ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「あ……、あ……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あんまりにもあんまりすぎて、言葉が続かない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0023
Elliot "「[firstname]、落ち着けよ。\n
あんた、顔真っ赤だぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0054
Dee "「お姉さん、可愛い。\n
嬉しいの？照れているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0055
Dam "「結婚式には呼んでね？\n
でも、僕ら子供だから、ご祝儀は期待しないで」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0395
Blood "「こらこら、お嬢さんは恥ずかしがりやなんだ。\n
あまりからかうな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_12")
T "（誰のせいよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深呼吸。\n
深呼吸。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうにかこうにか、深呼吸を繰り返して呼吸を整える。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0396
Blood "「ああ、もちろん、ご両親だけでなく、お義姉さんにも挨拶をするつもりだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「っ！？\n
人の姉さんを、お義姉さんなんて呼ばないで！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが、軽く眉根を寄せる。\n
困惑したような顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0397
Blood "「そうは言ってもな、お嬢さん。\n
私は、まだ君のお姉さんの名前を知らないから、他に呼べないんだが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "「呼ばなくていいから……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが、姉さんを名前で呼んでいるところを想像したら、眩暈までしてくるようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな私の言葉に、ブラッドは「ああ」と何かに気付いたように声をあげた。"

hide m_bra_end12
show m_bra_end13 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふっと柔らかい笑みを浮べて私を見る。\n
滅多に見ないような、悪役らしくない笑みだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慈しむような、そんな色。\n
{size=+20}不気味だ。{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0398
Blood "「君は心配性だな、[firstname]。\n
大丈夫だ、私には君しか見えていない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本格的に、不気味。\n
自らも似合わないと認める、甘い言葉だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（{size=+20}紅茶の飲みすぎで、どうかしちゃったのかしら{/size}……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、珍しい茶葉が手に入ったりすると、ちょっと見たことないぐらい奇妙なテンションに突入する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今手元にある紅茶は、上質ではあるが飲み慣れたアールグレイだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0399
Blood "「君の姉さんに、君の姉という以上の興味はない。\n
私は傾いたりしないよ。証明しよう」"

hide m_bra_end13
show m_bra_end14 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドはすでに、私の初恋と、それにまつわる諸々を知っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0024
Elliot "「なんだ、あんた、身内に横恋慕されるとかそんな心配してたのか？\n
心配しすぎだって」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「え、いや……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice dad_g0056
Dee "「ボスは、何かを気に入ったら長いから、大丈夫だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice dad_g0057
Dam "「紅茶に対する異常な執念を見ていたら、分かるよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "事情も知らない三人に、口々に応援（？）される。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……とにかく、断るわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice blo_g0400
Blood "「君が断ったとしても、私は、したいと思ったときにしたいことを……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……いいから。\n
今回はやめて」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくらなんでも、まだ早い。"


play music rose_garden_p_ali
hide m_bra_end14
show m_bra_end15 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「そのかわり、手紙を書くから」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice blo_g0401
Blood "「手紙……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「ええ。\n
手紙を……、書くわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice blo_g0402
Blood "「……私にか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そう。\n
あなたに」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice blo_g0403
Blood "「……そ、そうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "珍しく、ブラッドは動揺している。\n
実家に行くよりも、よほど。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（そうよ。\n
実家に行くなんて、まだ現実的じゃないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もっと、現実的に、越えなければいけないことがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dee "「？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dam "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0025
Elliot "「手紙？\n
なんのことだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0404
Blood "「……こっちの話だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の人には、通じない。\n
私とブラッドだけに通じることだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「気持ちを込めて、手紙を書くから」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（今、私がラブレターを送るとしたら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「まずは、そこから始めましょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "内容も、前とは違ったものになる。"


hide m_bra_end15
show white onlayer master
with compress_extralong
scene black with compress_extraextralong
pause 1
stop music
##endmemory
jump gakuen_a
