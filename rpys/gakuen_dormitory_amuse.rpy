label gakuen_dormitory_amuse_not1:
$ clockanim()

with dis
$ hi_mes()

scene bg_par15_rg_amu_day with Dissolve(1.2)

play music gallery_front_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮は、なんというか……、「ああ、遊園地ね」と思わず納得してしまいそうな建物だった。\n
つまり、それそのもので……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "建物自体は大きいし、所有している土地面積もそれなりに広い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、所狭しといろんなものが並んでいるせいで、どうにも雑多なイメージを受けてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一言で言うと、ごちゃごちゃしているのだ。\n
同時に遊びの空気に満ちてもいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさに遊園地のような、楽しそうな雰囲気。\n
中を覗き込もうとしてみる。"

jump gakuen_dormitory_amuse2
label gakuen_dormitory_amuse_amuse1:
$ clockanim()

with dis
$ hi_mes()

scene bg_map_day
with dis

play music gallery_front_day_p_wam

scene bg_par15_rg_amu_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮は、なんというか、ああ、遊園地ね、と思わず納得してしまいそうな建物だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "建物自体は大きいし、所有している土地面積もそれなりに広い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、所狭しといろんなものが並んでいるせいで、どうにも雑多なイメージを受けてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一言で言うと、ガチャガチャしているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ポジティブに表現したならば、賑やか、なんて言葉が一番相応しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな遊園地寮の敷地内へと入ろうとしたところで、矢印がぴたりと動きを止めた。"


show guide_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0100
Guide "「さあ、ここが終点だよ！\n
ここが遊園地寮だ！」"

play sound se_0058
hide guide_2
show guide_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Guide "「これで俺の任務は終了！\n
後は部屋を貰うだけだよ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ガイドである矢印が案内してくれるのは、ここまでのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "四つの寮を巡る間のことだけだというのに、ずいぶん長い時間を一緒に過ごしたような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しばかり、寂しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ここで、お別れ？\n
少し、寂しいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
Guide "「寂しく思うことなんかないさ！\n
俺は君が迷子になったら、すぐにでも飛んでいくからね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
Guide "「だって俺は……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「迷子を安心できるところまで案内してあげる、一流のガイド？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
Guide "「その通り！\n
俺は一流だからね、迷子を見つけるのも上手なんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
Guide "「だから安心して迷子になるといいよ！\n
俺に会いたければね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「安心して迷子って……」"

play sound se_0082
hide guide_6

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来、迷子を案内するためのガイドであるはずの矢印が、迷子を推奨しながらしゅわしゅわと消えていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "元々半透明で見えにくかった矢印が、首に繋がれた紐ごとしゅわしゅわとぼやけて見えなくなっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちり、と瞬きした次の瞬間には、もうそこに矢印の名残はなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……無茶を言うわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（行っちゃった……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今まで紐を持っていた手の中が、空っぽになってしまっているのが寂しい。\n
よく知らない場所で一人きり……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（また、会えるわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………。\n
……いや、会っちゃ駄目か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのガイドに会うということは、迷子になるのと同義だ。\n
積極的に会いたいような相手ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが……、半透明で見つけにくいとはいえ、あんなに騒々しいガイドなのだ。\n
これから始まる学園生活の中で、また見かけることもあるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……よし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は気合を入れて、遊園地寮の中へ一歩を踏み出す。"

jump gakuen_dormitory_amuse2
label gakuen_dormitory_amuse2:
play sound se_0591

scene bg06_sk_h_day
with dis

play music gag1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ！！？」"


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
Hatena "「！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょうど中から飛び出してきた人物と、危うく正面衝突しかけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すんでのところで身を引いたので助かったが、もう少し遅れていたらぶつかっていただろう。"


scene bg_par15_rg_amu_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「ごめんなさい……っ」"


show pia_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice pie_r0035
Pierce "「ごめんね、ごめんね！\n
大丈夫？ぶつかっていないよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「あら？\n
ピアス？」"

hide pia_m_01_3
show pia_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice pie_r0036
Pierce "「ん？俺の名前を知っているの？\n
あ！分かった！[firstname]、君だね？俺ちゃんと覚えているよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮の前。\n
私とぶつかりそうになったのはピアスだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嬉しそうに、私の名前を覚えている、と繰り返す。\n
……繰り返すまでもないようなことなのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……ファミリーネームまで覚えているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらっと、そんな意地の悪いことを考えてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「どうしたの？\n
そんなに急いで」"

hide pia_m_03_11
show pia_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Pierce "「！」"

hide pia_m_03_3
show pia_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pie_r0037
Pierce "「ああ、そうだ！危ないんだよ！\n
俺もボリスも止めたんだけど、ゴーランド先生がバイオリンを持ち出したんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ゴーランドが、バイオリン？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それのどこが危ないというのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（……ん？\n
いや、なんだか悪い予感がするな）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……なぜかしら。\n
とってもマズイもののように思えるわ）"

hide pia_m_01_3
show pia_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice pie_r0038
Pierce "「俺とかね、すでに知っている人は皆逃げているんだ。\n
残っているのは新入生だけだよ」"

hide pia_m_01_8
show pia_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice pie_r0039
Pierce "「あれ？君も新入生だよね？\n
そうなると、君は残るべきなのかな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「え……、いや、危ないものなら、新入生だろうとなんだろうと逃げるべきじゃないのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスの話は要領を得ない。\n
本人は一生懸命伝えようとしてくれているらしいが、あまりにも断片的だ。"

play sound se_0498
pause .1
play sound se_0312
hide pia_m_03_12

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、その言葉の中にあった皆逃げている、という言葉の意味はなんとなく分かったような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスだけでなく、幾人もの生徒達が強張った表情で足早に遊園地寮から出てきている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0116
Seito "「すいません。\n
俺ちょっと用事を思い出して……」"

play sound se_0591
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0073
Seito "「おおっと、しまった！\n
事務室に提出しないといけない書類があったんだー！」"

play sound se_0417
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0097
Seito "「あ、花壇のアマリリスに水をやる時間だわ！」"

play sound se_0591
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0050
Seito "「すいません、ちょっと星の声に導かれたので旅に出ます！」"

play sound se_0591
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0082
Seito "「頭が盲腸なんで……！！」"

play sound se_0417
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0111
Seito "「宗教上の理由で音楽が禁じられているので、残念ですが失礼します……！！」"

play sound se_0591
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒達が、次々と外へ出てくる。\n
寮の中にいる人間に対して口々に外出する理由を述べるが、それらしいものから、荒唐無稽なものまで様々だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とりあえず、皆の、なんとしてでも理由をつけてこの場から離れたい、という切実な思いは伝わってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一体、遊園地寮の中で何が起こっているのだろう。"


show pia_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0040
Pierce "「う～ん、どっちなんだろう。\n
君は残ったほうがいいのかな」"

hide pia_m_03_13
show pia_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0041
Pierce "「でも、危ないよね。\n
うん、危ないよ、新入生だろうと危ないことはかわいそう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスはぶつぶつと、自問自答している。\n
何がどう危ないのかといったところの因果関係は、まったく分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「え～っと……、危ないのなら逃げるべきじゃないのかしら？\n
何がどうなっているのか分からないけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "理由より先に行動。\n
実際に目の前で逃げていく生徒を見ていると悠長なことは言っていられない。"

hide pia_m_01_13
show pia_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0042
Pierce "「そうなのかな？\n
う～ん、でも遊園地寮に入る新入生にとっては洗礼だとか通過儀礼だとかで……」"

play sound se_0321
hide pia_m_02_9
show pia_m_02_9 at left
with dis

show bor_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0028
Boris "「ピアス！？\n
おまえ、何こんなところでもたもたしているんだよ！」"

hide bor_m_01_3
show bor_m_01_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0029
Boris "「おっさんもう準備万端だぜ！？\n
早く逃げないと……、って、[firstname]、あんたまでどうしてこんなところに……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「ボリス！？\n
ボリスまで逃げるところなの？」"

hide bor_m_01_1
show bor_m_03_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice bor_r0030
Boris "「え？\n
う～ん、逃げるなんて言われるとちょっと格好悪いけど……」"

hide bor_m_03_13
show bor_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice bor_r0031
Boris "「戦略的撤退というか、なんというか……。\n
あ、とりあえずここから移動したほうがいいぜ、あんたも！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……つまり、逃げろってことね）"

play sound se_0591
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「何から逃げているの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "走り出しながらも尋ねる。"

hide bor_m_03_11
show bor_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0032
Boris "「もちろん、おっさんの……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "答えは、ボリスに聞くより先に実感として届いた。"

play sound se_0221
play sound se_0106
$ flash(.1)
hide pia_m_02_9

hide bor_m_01_3


show m_ryou1_yuu1 onlayer master
with dis

play music test_sp_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0043
Pierce "「ぴ！！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0033
Boris "「～～～っっ！\n
ぐあ！？」"

play sound se_0317
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「……っ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前が真っ白になる。\n
チカチカと星が瞬く。"

play sound se_0316
$ flash(.2)
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "がつんと、殴られたかのようだ。"

play sound se_0317
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初、それが音だとは分からなかった。\n
それほどの衝撃……、いや衝撃波といっていい。"

$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世にも恐ろしい、音響兵器。\n
なんとか防御しなきゃ、と思いはするのに、体が思うように動かない。"

play sound se_0316
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私ですらこうなのだから、ちょっと人より個性的な耳を持つ二人にとってはもっと辛いのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0044
Pierce "「～～～っ！\n
お、俺、死んじゃう……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0034
Boris "「し、死んでたまるか……っ！！\n
……あ、駄目、なんかもう、むしろ死にたい気分」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0035
Boris "「……ううう、くそっ」"

play sound se_0509
hide m_ryou1_yuu1
show m_ryou1_yuu2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何をどうしたのか、ボリスがひらりと揺らしたその手の中に、ピンク色の銃が現れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（……っ、銃！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法学校であるシンフォニアで見るのには、違和感のありすぎる武器だ。\n
ボリスはそれをぴたりと寮の一室へと向けて……。"

play sound se_0022
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷いもなく銃弾をその部屋に向けて撃ち込んだ。"

play sound se_0022
camera at hpunch
camera at vpunch

scene bg06_sk_h_day ##instantPAY ATTENTION="true"]
hide m_ryou1_yuu2

pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0036
Boris "「今のうちだ……！\n
早く逃げるぞ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言うや否や、ボリスが私の手をとって走り出す。\n
もう片方の手には、へろへろになっているピアスの襟首を引っ掴んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（なんだかんだで、面倒見いいのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな姿が微笑ましくて、こんな状況にも関わらず笑ってしまいそうになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0043
Gowland "「こら！ボリスだな！？\n
窓ガラスを割るとは、この悪戯猫！悪ガキめ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠くから、ゴーランドの怒声が聞こえる。\n
それに背中を押されるようにして、私達は遊園地寮から逃げ出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓ガラスは銃で撃つ前にゴーランドの演奏で割れていた。\n
それほどに、悪質な音だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（銃よりも悪質な音って、どんな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どんなもこんなも体感したばかりだが、口で説明するのは難しい。"

with dis
$ hi_mes()

scene bg_par15_rg_amu_day
with stripe_l_medium

scene bg20_gd_day
with stripe_l_long

play music garden_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「はあ、はあはあ……」"


show bor_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice bor_r0037
Boris "「～～っ、ふう～」"

hide bor_m_01_9
show bor_m_01_9 at left
with dis

show pia_m_02_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice pie_r0045
Pierce "「ぜいぜい……。\n
ぴい……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どれくらい走っただろうか。\n
背後から感じられていた恐ろしい気配がなくなったのを確認し、私達はようやく立ち止まった。"

if place_of_stay == "Castle":
    jump gakuen_dormitory_amuse_not2
if place_of_stay == "Hatter":
    jump gakuen_dormitory_amuse_not2
if place_of_stay == "Amuse":
    jump gakuen_dormitory_amuse3
if place_of_stay == "Tower":
    jump gakuen_dormitory_amuse_not2
label gakuen_dormitory_amuse_not2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと見た先、引きずりまわしてしまった矢印もぐったりとしている。"

jump gakuen_dormitory_amuse3
label gakuen_dormitory_amuse3:
hide bor_m_01_9

hide pia_m_02_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "力尽きたように道の両サイドに広がる芝生へと腰を下ろす。"

play sound se_0046 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「な、なにあれ。\n
ど、どうなっているの……っ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……あれも、魔法？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、そうとしか思えない。\n
{size=+20}人智を超えた破壊力だ{/size}。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "{size=+20}（な、なんて邪悪な暗黒魔術なの……）{/size} "


show bor_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice bor_r0038
Boris "「いや……、そう思っても無理はないけどさ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "苦しい息の下で問えば、同じように息を弾ませているボリスが答えてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？\n
魔法じゃないの？」"

hide bor_m_03_11
show bor_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_r0039
Boris "「おっさん……、ゴーランド先生のことなんだけどさ。\n
あのおっさん、破壊的なまでの音痴なんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……オンチ」"

hide bor_m_03_6
show bor_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice bor_r0040
Boris "「そ。\n
音痴」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……音痴、ですむレベル？」"

hide bor_m_03_13
show bor_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice bor_r0041
Boris "「う、うう～ん……、すまないレベルだけど。\n
音痴なことなんだよ、あれの要因は」"

hide bor_m_03_11
show bor_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice bor_r0042
Boris "「最悪に音痴だってだけで充分なのに、無意識なのか意識的なのか、その音に魔力を上乗せしているせいでもう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……聴くに耐えないわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聴いた、というよりも感じた、といったほうがいいのだろうか。\n
音の持つ悪い方向への可能性というものを、ひしひしと思い知らされた。"

hide bor_m_03_1
show bor_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0043
Boris "「更に悪いことに本人は自覚がないから、何かあるとすぐに演奏したがるんだ。\n
今回は、新入生歓迎」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……げげげ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "{size=+20}（全っ然、歓迎してない）{/size} "

hide bor_m_01_3
show bor_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice bor_r0044
Boris "「本当、げげげ……、だよな。\n
新入生、今頃死にかけているぜ」"

hide bor_m_01_9
show bor_m_01_9 at left
with dis

show pia_m_03_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice pie_r0046
Pierce "「お、俺も死んじゃいそうだよ……。\n
ゴーランド先生のバイオリン、怖いよ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐったりと芝生にのびていたピアスが、もごもごと呻く。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「歓迎っていうか、嫌がらせよね……。\n
この学校に入って早々、頭痛がしてきたわ」"

hide bor_m_01_9
show bor_m_02_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice bor_r0045
Boris "「そんなこと言うなって……」"

hide pia_m_03_13
show pia_m_03_2 at center
with dis
hide bor_m_02_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice pie_r0047
Pierce "「ねえ、[firstname]、君はどの寮に決めたの？\n
俺、君が遊園地寮に来てくれたら嬉しいな」"

hide pia_m_03_2
show pia_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice pie_r0048
Pierce "「気に入られているみたいだし、君なら、ゴーランド先生を止められる気がするんだ。そしたら俺、もっと安全に遊園地寮で暮らせるよ！」"

if place_of_stay == "Castle":
    jump gakuen_dormitory_amuse_not3
if place_of_stay == "Hatter":
    jump gakuen_dormitory_amuse_not3
if place_of_stay == "Tower":
    jump gakuen_dormitory_amuse_not3
if place_of_stay == "Amuse":
    jump gakuen_dormitory_amuse_amuse2
label gakuen_dormitory_amuse_not3:
hide pia_m_01_2
show pia_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice pie_r0023
Pierce "「ね、遊園地寮のこと嫌い？」"
$ gakuen_dormitory_amuse_not4a_seen = False
menu:
    "嫌いじゃない。":
        jump gakuen_dormitory_amuse_not4a
    "うーん……、どうかな。微妙。":
        jump gakuen_dormitory_amuse_not4b
label gakuen_dormitory_amuse_not4a:
$ gakuen_dormitory_amuse_not4a_seen = True
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「嫌いじゃないわ。\n
楽しそうだしね」"

hide pia_m_03_13
show pia_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_r0024
Pierce "「うんうん！\n
そうだよ、遊園地寮は楽しいんだ！だって遊園地だからね！」"

hide pia_m_03_11
show pia_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_r0025
Pierce "「だから、君も遊園地寮にするといいよ！\n
そうしたら俺と毎日一緒にご飯食べられるし、一緒に寝ることもできるよ！」"

hide pia_m_03_5
show pia_m_03_5 at left
with dis

show bor_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_r0013
Boris "「できねーよ。\n
何のために男子寮、女子寮に分かれていると思っているんだ、おまえは」"

hide bor_m_03_11
show bor_m_03_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_r0014
Boris "「大体、おまえと食事したり眠ったりなんか、ＰＲになってないだろ。\n
むしろ、マイナスポイントだ、マイナスポイント」"

play sound se_0016
hide pia_m_03_5
show pia_m_01_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_r0026
Pierce "「ぴ！？頭を掴まないでよ、痛いよ！？\n
馬鹿になっちゃう！」"

hide bor_m_03_13
show bor_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_r0015
Boris "「どうせ使ってない頭なんだから、どうなっても構わないだろ。\n
元が馬鹿なのに、これ以上馬鹿になりようがない」"

hide bor_m_01_12
show bor_m_02_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_r0016
Boris "「あ～あ……。\n
おまえがマイナスＰＲしたせいで、元が来るつもりだったとしても来てくれなくなっちまう」"

hide pia_m_01_8
show pia_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_r0027
Pierce "「ええ！？[firstname]、来てくれるよね？\n
この寮を選んでくれたんでしょう？」"

jump gakuen_dormitory_amuse_not5
label gakuen_dormitory_amuse_not4b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「うーん……。\n
好きとか嫌いとかいう前に、身の危険を感じるわ」"

hide pia_m_03_3
show pia_m_03_13 at left
with dis
hide bor_m_02_8
show bor_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice bor_r0017
Boris "「そんなことないぜ？\n
慣れれば平気……、って言いたいところだけど、あんたの気持ちはよく分かる」"

hide bor_m_03_11
show bor_m_03_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice bor_r0018
Boris "「慣れてもキツイ。\n
いや、むしろ慣れるはずがない」"

hide bor_m_03_13
show bor_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice bor_r0019
Boris "「実際に体験しちまうと、二度とは味わいたくなくなるよな。\n
俺も同感だ……」"

hide pia_m_03_13
show pia_m_03_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice pie_r0028
Pierce "「それじゃあ、[firstname]。\n
君、遊園地寮には来てくれないの？」"

jump gakuen_dormitory_amuse_not5
label gakuen_dormitory_amuse_not5:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……ごめんなさい、ピアス。\n
悪いけど私、遊園地寮じゃないの」"

hide bor_m_01_3
show bor_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice bor_r0020
Boris "「え、そうなの？\n
俺、あんたは遊園地寮に決めたから、来たんだとばかり思っていたよ」"

if place_of_stay == "castle":
    jump gakuen_dormitory_amuse_castle
if place_of_stay == "hatter":
    jump gakuen_dormitory_amuse_hatter
if place_of_stay == "tower":
    jump gakuen_dormitory_amuse_tower
label gakuen_dormitory_amuse_castle:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ううん、違うのよ。\n
赤薔薇寮に行く前に、他の寮も見てみたくて、回っていただけだったの」"

hide bor_m_01_2
show bor_m_03_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_r0021
Boris "「じゃあ、赤薔薇寮に決めたのか。\n
う～～～ん……、あそこにねえ……」"

hide pia_m_03_13
show pia_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_r0029
Pierce "「ぴ！\n
女王様がいるところだよね！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「そう、女王様。\n
……学校なのに、女王様なんておかしいわよね？」"

hide bor_m_03_13
show bor_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice bor_r0022
Boris "「……会えば、違和感ないと思うよ。\n
まさに女王様だから」"

hide pia_m_01_3
show pia_m_01_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice pie_r0030
Pierce "「女王様、ネズミが嫌いなんだ……。\n
だから、俺のことも嫌いなんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（まあ……、ネズミが嫌いなら、仕方ないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じ、と視線をピアスの頭上に注いでしまう。丸っこいネズミ耳が、酷い酷い、と繰り返す声音にあわせてぴこぴこと揺れている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この学校には、耳が頭の上にある人が多い。\n
耳が頭の上にある人……、人なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この学校にはいろいろ、追求してはいけない部分が多くある。\n
触れてしまっては立ちゆかなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "主に、{size=+20}ペーターとエリオットとボリスとピアスの耳についてだとか。{/size} "

hide bor_m_01_10
show bor_m_02_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0023
Boris "「さて、と。\n
俺は寮に戻って、新入生の介抱をしてやろうかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よっこらせ、っとボリスが立ち上がって伸びをした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「ふふ、面倒見がいいのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、立ち上がる。"

hide bor_m_02_11
show bor_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0024
Boris "「なんていったって、俺、一応寮長だからね。\n
新入りの面倒は見るんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「ああ、なるほど。\n
それで私にも親切にしてくれたのね」"

hide bor_m_02_6
show bor_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice bor_r0025
Boris "「え？あんたなら、新入りじゃなくても……。\n
……ほら、ピアス行くぜ」"

hide pia_m_01_8
show pia_m_03_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice pie_r0031
Pierce "「うう、俺、[firstname]、君ともっと一緒にいたいけど……。\n
君、赤薔薇寮に行くんでしょう？」"

hide pia_m_03_8
show pia_m_03_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice pie_r0032
Pierce "「女王様は俺のこと嫌いだから、我慢するよ。\n
また教室でね！」"

hide bor_m_01_12
show bor_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice bor_r0026
Boris "「このすぐ先が、女王様のいる赤薔薇寮だよ。\n
……また、教室でね」"

jump gakuen_dormitory_amuse_not6
label gakuen_dormitory_amuse_hatter:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ううん、違うのよ。\n
帽子屋寮に行く前に、他の寮も見てみたくて、回っていただけだったの」"

hide pia_m_03_11
show pia_m_01_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_r0033
Pierce "「俺、[firstname]、君ともっと一緒にいたいけど……。\n
君は、帽子屋寮に行っちゃうんだね……」"

hide pia_m_01_8
show pia_m_03_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_r0034
Pierce "「双子が怖いからついていけないし……、我慢するよ！\n
授業で会おうね！」"

hide bor_m_03_4
show bor_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_r0027
Boris "「双子に会ったらよろしく伝えておいてよ。\n
……また、教室でね」"

jump gakuen_dormitory_amuse_not6
label gakuen_dormitory_amuse_tower:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ううん、違うのよ。\n
塔に行く前に、他の寮も見てみたくて、回っていただけだったの」"

hide pia_m_03_11
show pia_m_01_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_r0055
Pierce "「うう、俺、[firstname]、君ともっと一緒にいたいけど……。\n
君、塔に行くんだね？」"

hide pia_m_01_8
show pia_m_03_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_r0056
Pierce "「補佐さんは俺のこと嫌いだから、我慢するよ。\n
また教室でね！」"

hide bor_m_03_4
show bor_m_03_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_r0063
Boris "「お堅い連中に影響されすぎないようにな。\n
……じゃあ、また、教室で」"

jump gakuen_dormitory_amuse_not6
label gakuen_dormitory_amuse_not6:
hide pia_m_03_11

hide bor_m_03_2

play sound se_0142
play sound se_0562
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは悪戯っぽくウィンクを一つくれると、両手をぶんぶん振って挨拶してくれているピアスを、ずるずる引きずるようにしながら行ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（私も、赤薔薇寮に行こう）"


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスやピアスを見送って、歩き始めたところで他の新入生の集団とすれ違った。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0043
Seito "「遊園地寮なんて、名前だけでわくわくしてくるよな。\n
いろいろ面白い仕掛けがあるって聞いたぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0076
Seito "「でもさっき、遊園地寮から逃げてきた、ってヤツいたよな？\n
何か、怖いことでもあるのかなー」"

menu:
    "遊園地寮は面白い。":
        jump gakuen_dormitory_amuse_not7a
    "遊園地寮は危険。":
        jump gakuen_dormitory_amuse_not7b
label gakuen_dormitory_amuse_not7a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（面白いと思うわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……危険でもあるけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスやボリスがいる寮だ。\n
きっと楽しい日々が彼らを待っているだろう。"

with dis
$ hi_mes()

scene bg_map_day
with stripe_l_long
if place_of_stay == "Castle":
    jump gakuen_dormitory_castle_castle1
if place_of_stay == "Hatter":
    jump gakuen_dormitory_castle_hatter1
if place_of_stay == "Tower":
    jump gakuen_dormitory_castle_tower1
label gakuen_dormitory_amuse_not7b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（遊園地寮……、というかゴーランドが危険よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すでに恐怖のリサイタルが終了している今なら、安全だろうか。"

with dis
$ hi_mes()

scene bg_map_day
with stripe_l_long
if place_of_stay == "Castle":
    jump gakuen_dormitory_castle_castle1
if place_of_stay == "Hatter":
    jump gakuen_dormitory_castle_hatter1
if place_of_stay == "Tower":
    jump gakuen_dormitory_castle_tower1

label gakuen_dormitory_amuse_amuse2:

play music view_day_p_wam

show m_ryou1_yuu3 onlayer master
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「いや、あれは私がどうにかできる問題じゃないと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……まあ、私も、住むからには安全に過ごしたいけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice bor_r0046
Boris "「へえ？ってことは、あんた遊園地寮に決めたんだ？\n
物好きだね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは意地悪そうに笑うものの、それを言うならばボリスだって同じ物好きだ。\n
何せ、彼は遊園地寮の寮長なのだから。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「人のことを言えるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice bor_r0047
Boris "「俺は気まぐれなんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「じゃあ、私もよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice bor_r0048
Boris "「……ふうん？\n
じゃあ、俺達、気が合うってわけだね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice pie_r0049
Pierce "「俺ともだよ！一緒の寮なんて最高！\n
ねえ、[firstname]、君、俺の隣の部屋においでよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「そ……、それは無理だと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスは、私の性別を分かっているのだろうか。"

hide m_ryou1_yuu3
show m_ryou1_yuu4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0049
Boris "「無理に決まっているだろ、馬鹿。\n
おまえって、本当に頭悪いよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0050
Pierce "「お、俺、馬鹿じゃないよ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……でも、賢くもない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮、と名前だけ聞くと一つの寮のように思えるが、実際にはエントランスが一緒なだけで、男女共同区域を除き女子寮と男子寮では完全に分離している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、ここシンフォニアには、学生や職員の他に使用人が常駐しており、それぞれの学生寮にも専任の使用人達が住み込んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エントランスには常にそのうちの誰かしらがおり、それぞれの寮を自在に行き交うようなことはできないようになっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少なくとも私より先に入学していて、それなりにシンフォニアで学生生活を送っているはずなのに、どうしてピアスはそこに思い至らないのか。"


play music garden_day_p_wam

scene bg20_gd_day
with dis

show bor_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0050
Boris "「さて、と。\n
そろそろおっさんも気がすんだかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よっ、と、ボリスは立ち上がって伸びをした。"

hide bor_m_02_11
show bor_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0051
Boris "「ほら、立てよ、ピアス。\n
寮に戻って後始末だ」"

hide bor_m_02_1
show bor_m_02_1 at left
with dis

show pia_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0051
Pierce "「俺、片付けは得意だよ！\n
全部埋めちゃえばいいからね！」"

hide bor_m_02_1
show bor_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0052
Boris "「……おい、こら、ピアス。\n
おまえ、倒れた新入生を埋める気か……？」"

hide pia_m_01_6
show pia_m_03_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0052
Pierce "「埋めると早いよ！\n
俺、穴掘るの、うまいんだから！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスは立ち上がって、えへんと胸を張っているが、自慢の方向性が著しく間違えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そもそも片付けイコール埋める、というのもどうなのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「そ、そう……。\n
すごいわね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"

hide bor_m_02_8
show bor_m_01_9 at center
with dis
hide pia_m_03_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice bor_r0053
Boris "「……はあ。\n
ねえ、あんたはまともに手伝ってくれるだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そうね。\n
私も、できる範囲で手伝うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、立ち上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは、自分を気まぐれだとかいうし、裏付けるように外見も軽そうに見える。\n
正直、寮長というと意外な気がしたのだが、ちゃんとしていて見直した。"

hide bor_m_01_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人並んで、遊園地寮へ戻るべく歩き出す。"


scene bg20_gd_day
with dis

scene bg_par15_rg_amu_day
with dis

play music gallery_front_day_p_wam
hide m_ryou1_yuu4
show m_ryou1_yuu5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮の門の前では、ゴーランドが立っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0044
Gowland "「お！[firstname]。\n
あんた、遊園地寮に決めたのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0045
Gowland "「あ～、でも、惜しかったな。\n
もうちょっと早く来ていたら、俺の歓迎演奏会を聴けたのによ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「そ、そうね。\n
……残念だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "付き合いというものがある。\n
表面的に残念がってみせる私に、ボリスが渋面を浮べた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0054
Boris "「ああ、こらあんた、そんな心にもないこと言っていると、おっさんが勘違いするだろ？\n
やめてくれよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「でも、先生だし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_r0055
Boris "「……聴かされたいんだ？\n
あんたが望んでいるのなら、助けないよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "{size=+20}「ごめんなさい」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私にしては珍しいぐらい、心から素直に謝った。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0046
Gowland "「まてまて、なんだおまえら。\n
勘違いって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0056
Boris "「おっさんの演奏は凶器なんだよ。\n
いいかげんに自覚して、控えろよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0047
Gowland "「何を言うか。\n
新入生なんて、リラックスできて喜んでるだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0057
Boris "「……{size=+20}逃げまどってんだよ{/size}。\n
おっさん、いいかげんに自分の音楽センスがテロの域に達していることに気づけって」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0048
Gowland "「ああん？\n
んだとお？人の才能を妬んでケチつけるとは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0058
Boris "「……前向きに、こじつけてくるよな、あんたは」"

hide m_ryou1_yuu5
show m_ryou1_yuu6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0053
Pierce "「ねえ、俺、お片付けしてきていいの？\n
庭に穴掘ってもいいかな。いいよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0059
Boris "「～～～っ。\n
だからピアスっ、おまえは新入生を埋めようとするな！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0049
Gowland "「おっと、カリカリするなよ、ボリス。\n
片付けはいいことじゃねえか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0060
Boris "「あのな、おっさん、ピアスの言う片付けってのは……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_r0050
Gowland "「落ち着けって。\n
なんだ、俺が心が落ち着く曲でも一曲弾いてやろうか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_r0054
Pierce "「穴がだめなら、どうやって片付けるの？\n
ネズミに……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……ピアス、ストップ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とても心臓に悪い。\n
グロテスクというか、聞くだけで後味の悪くなるようなことを言われそうな気がして、遮る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスには、たしかに手伝いが必要だ。\n
ぐいっと袖をまくる。"

hide m_ryou1_yuu6


show bor_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0061
Boris "「……お？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「三人は、倒れている新入生を介抱してあげてちょうだい。\n
私は割れた窓のほうから直していくわ」"


show go_m_01_12 at center
with dis
hide bor_m_01_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_r0051
Gowland "「それじゃあ、今度は目覚めの曲を……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "{size=+20}「永眠しそうだからやめて」{/size} "

hide go_m_01_12
show go_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice gor_r0052
Gowland "「……ひでえな。\n
あんたは俺の演奏を聴いてないから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「聴いていないからこそ、今こうして動けるのよ。\n
ほら、あなたも動いて動いて！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋決めや、手続きはこの片付けが終わってからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "惨状が広がっているであろう寮の中へと向かう。\n
そんな中、ボリスがこそりと私の傍らへとやってきた。"


show bor_m_03_11 at center
with dis
hide go_m_03_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_r0062
Boris "「[firstname]……。\n
俺、あんたが遊園地寮に来てくれて、本当によかったと思う」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「……っぷ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心底、というようなボリスの言葉に、口元に笑みがこみ上げた。"

hide bor_m_03_11


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮。\n
いろいろと手はかかるが、名前に相応しく楽しい学園生活が待っているはずだ。"

with dis
$ hi_mes()

jump gakuen_routechoice
