label gakuen_nightmare_end:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_tow_day
with dis

play music corridor_day_p_wam

scene bg25_rr_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの夜の翌日、私は寝不足の目をこすりつつカフェテリアに向かっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜結局、ブリーズ終了の合図をも無視して、ナイトメアの部屋で時間を過ごしてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帰りは朝方ナイトメアが夢を渡って送ってくれたため、誰かに見つかることなく部屋に戻ることが出来た。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目撃証言というあたりでどうにかなる心配はないのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（部屋に私がいなかったのがバレていたら、アウトよね。\n
……ああ、落ち着かない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "数時間の仮眠を経て、いつもの時間には身嗜みを整えて部屋を出る。\n
今日のリボンは、ナイトメアの部屋から取り返してきたものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（バレていませんように）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "階下に下りるべく、階段へと廊下を曲がる。"


show gre_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0020
Gray "「……おはよう、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「！！！！？」{/size} "


play music gray_t_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かけられた声に、口から心臓が飛び出そうになった。\n
グレイが角を曲がってすぐのところで待ち構えていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（こ、これは……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり昨夜の外泊がバレていると考えるべきだろうか。\n
口から出かけた心臓が、今度はばくばくとうるさいほどに騒ぎ出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（他の職員や先生ならともかく……、近しい人にこのての注意を受けることになるなんて……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……胃が痛い）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ナイトメアのように逃走をはかるわけにもいかない。\n
覚悟を決めて身構えたところで、グレイが口元に柔らかな苦笑を浮かべた。"

hide gre_m_01_12
show gre_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0021
Gray "「いや、そんなに身構えないでくれ。\n
俺は君を叱るために待っていたわけじゃないんだ」"

hide gre_m_03_2
show gre_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0022
Gray "「そもそも君を叱るぐらいだったら、ナイトメア様を止めている。\n
……ああ、違った、ナイトメア先生だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ナイトメア様？）"

hide gre_m_02_12
show gre_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice gra_g0023
Gray "「俺はもともと、ナイトメア先生個人の使用人なんだ。\n
あの人がシンフォニアに入ったから、俺もこうしてついてきた」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ついてきただけで塔の管理職にまで登りつめるあたり、グレイは間違いなく優秀な人材なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（まあ、それは以前から分かっていたけど……。\n
ナイトメアに仕えているんだ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「そ、そうなの？」"

hide gre_m_02_9
show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gra_g0024
Gray "「ああ。\n
だから俺にとって、学校の規則よりも……、優先されるのはナイトメア様の幸福だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっぱりと言われて、納得した。\n
二人には主従のような雰囲気と、家族のようなそれが混在している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアはグレイを信頼しているし、グレイはナイトメアの世話を焼くことに生き甲斐を見出しているようにも見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "納得する一方で、ちらりと嫌な予感がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

hide gre_m_02_2
show gre_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gra_g0025
Gray "「昨夜、点呼の折に君の不在を誤魔化したのも俺だ。\n
……まあ、つまり君とナイトメア先生のことは知っている」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（……や、やっぱり）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……いたたまれない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "身近な人に関係を知られるというのは、なんともいえない気分だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「あ……、ああ、その、誤魔化してくれたのは助かったわ。\n
ありがとう」"

hide gre_m_02_8
show gre_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice gra_g0026
Gray "「いや、俺が勝手にしたことだからな。\n
君が気にすることではないさ」"

hide gre_m_02_4
show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice gra_g0027
Gray "「それで君と口裏を合わせておこうと思ってな。\n
……歩きながらで構わないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ええ。\n
こちらからも、お願いするわ」"

play sound se_0384
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやらそのために、グレイはこの場で私を待ち構えていたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がカフェテリアで昨夜のことについて、うっかり適当なことを口にしてしまっていてからでは、口裏の合わせようもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざわざ私の部屋の近くで、私が誰かに会う前に接触するべく待ち伏せてくれていたのだ。\n
恥ずかしがってなどいられない。"

hide gre_m_02_2
show gre_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0028
Gray "「君は、昨夜のブリーズには参加していないことになっている」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ふんふん……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人、カフェテリアに向かって歩きながら打ち合わせのようなやりとりを交わす。"

hide gre_m_03_10
show gre_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0029
Gray "「昨夜、君が出掛けてすぐに、悪いとは思ったが君の部屋に入らせてもらった」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……え」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（み、見られてまずいものは、外に出してなかったわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "即座に脳内で確認する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "所持していると問題があるものだとかを、隠し持っているわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、女の部屋には、知人といえど（あるいは知人であれば尚更）男性に見られたら困るアイテムなんていうのがごろごろとあるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな類を、万が一にも出しっぱなしにしていなかったかと焦る。"

hide gre_m_01_11
show gre_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0030
Gray "「ああ、もちろん君のプライベートなものには一切触れていないし、見るようなこともなるべく避けた」"

hide gre_m_01_4
show gre_m_01_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0030_5
Gray "「ただ君のダミーを用意して、ベッドの中に押し込ませてもらった」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「それを使って、昨夜はずっと部屋にいたことに？」"

hide gre_m_01_14
show gre_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice gra_g0031
Gray "「ああ。\n
君は昨夜、具合が悪くて部屋で眠っていたことになっている」"

hide gre_m_03_9
show gre_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice gra_g0032
Gray "「メイドからも、君の体調があまりよくないらしいという形でしか報告を受けていない。\n
……そういうことにしてくれると助かる」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（助かるのは、こっちよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっかり、助けられてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「分かったわ。\n
私は昨夜ずっと体調が悪くて眠っていたことにすればいいのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今朝方、ナイトメアに送ってもらって部屋に着いたときにも、そんなことがあったとはちっとも気付かなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ベッドも綺麗なものだったし、まさかそこに私の身代わりが押し込まれていたとは。回収まで、全部グレイがやってくれたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「私を助けるつもりはなかったかもしれないけれど……、私からもお礼を言わせてちょうだい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はあくまでナイトメアのために動いたつもりでしかないかもしれない。\n
だが、それでも感謝している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私だって、昨夜は素敵な時間を過ごすことが出来たと思っているのだ。"

hide gre_m_03_6
show gre_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0033
Gray "「俺は、ナイトメア先生のために動いただけだが……。\n
君がそう言ってくれるのならば、その言葉もありがたく受け取っておくよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ありがとう、グレイ」"

hide gre_m_02_8
show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0034
Gray "「俺の方こそ、ありがとう。\n
君には感謝しているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「ええ？\n
私は何も……」"

hide gre_m_02_2
show gre_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_8")
voice gra_g0035
Gray "「いやいや、{size=+20}奥方{/size}が出来たともなれば、あの方ももっと身辺のことにも気を遣ってくれるだろうし……、仕事もしてくれるに違いない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_1")
T "「…………」"


play music gag1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（……んん？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「グレイ？」"

hide gre_m_03_4
show gre_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gra_g0036
Gray "「なんだ？\n
何か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「何か、じゃないわよっ！\n
今、あなたこそ何か、さらっとすごいこと言ったわよ！？」"

hide gre_m_03_1
show gre_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice gra_g0037
Gray "「……何か、言っただろうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「言ったわよ！\n
奥方とかなんとか！！」"

hide gre_m_02_3
show gre_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice gra_g0038
Gray "「ああ。\n
確かにちょっと気が急いていたな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「そうよ、まだ付き合い始めたばかり……」"

hide gre_m_03_2
show gre_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice gra_g0039
Gray "「まだ君のご家族にもご挨拶がすんでいないからな。\n
未婚の君を奥方と呼ぶのは失礼だ」"

hide gre_m_01_13
show gre_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice gra_g0040
Gray "「早急に手はずを整え、婚姻の話を進めるべきだろう。\n
早く、その呼称を適正なものにするためにも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……いやいや、急いでどうするのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ますます、気が急いている。\n
グレイは真顔のようでいて、どこかしら嬉しげな、緩んだ空気が滲んでいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……もしかして、浮かれているの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうなのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの中では、ナイトメアが「結婚して腰を落ち着けたらまともになる」という期待がどうしようもないほどに高まっているようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（どうかなー……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私などはそんなふうに思ってしまうのだが、ナイトメアとの付き合いが私よりも長いグレイがそう思うのならば、そうなるのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、まだ私はナイトメアとの結婚など考えてもいない。\n
どうにかこうにか付き合い始めたばかり、というところだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアがそのつもりなのかどうかすら分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（そうよ、ナイトメアの気持ちだってあるのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……って、私も気が早い）"

hide gre_m_01_1
show gre_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice gra_g0041
Gray "「ああ、少しのつもりが長く引き止めてしまったな。\n
朝食をとる時間が足りなくなってしまうぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……そ、そうね」"

hide gre_m_03_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話の間にも、カフェテリアの前についていた。\n
グレイに促されて、私はカフェテリアへ向けて歩を進めていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の口にした奥方なんて言葉が頭の中をぐるぐると回っているせいで、妙にふわふわとした足取りになってしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜からずっとそう。\n
ふわふわ、浮かれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲からはふらふらしているようにも見えただろう。\n
それが、私が体調悪いという弁に信憑性を増してくれたのは言うまでもない。"

with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

scene bg_par02_ct_tow_day
with stripe_l_long

play music dining_day_p_wam
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの翌日の朝というだけあって、カフェテリアはストームの翌日と同じぐらいに賑やかだった。あちこちから昨夜の話題が漏れ聞こえてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0010
Seito "「おまえ、昨日、部屋に女子来た？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0016
Seito "「来た来た。\n
おまえのとこにも来た？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0011
Seito "「当たり前だろ！\n
ストームのときに、ちゃんと戦利品とってきてあったからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0017
Seito "「だよな。\n
ああでも、隣のクラスのあいつが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0010
Seito "「昨夜、私、三回も使用人に見つかったんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0084
Seito "「ええ？\n
それ、見つかりすぎよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0011
Seito "「最後のあたり、使用人に、見ないふりされてた……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0012
Seito "「有難いんだけど、切ないっていうか……、哀れっていうか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0085
Seito "「そこで見て見ぬふりを選択した使用人のほうも哀れよね……」"

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

play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……楽しそうだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして彼らの感想を直に聞いてみると、やはり私が昨夜体験したのは、ブリーズとは何か違うような気がして仕方ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正しい意味でのブリーズというのにも、興味がわく。"


show tower_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0037
Seito "「[firstname]、こっちこっち！\n
席、とってあるわよ！」"

hide tower_a2_3
show tower_a2_3 at left
with dis

show tower_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0055
Seito "「こっちに来るといいわ！\n
ほらほら、こっちよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呼ばれた声に、そちらへと視線を向ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの翌日にも会った二人組だ。\n
にこやかに笑みを浮かべて、私を手招いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜について追及されるだろうが、グレイとはもうすでに打ち合わせ済みだ。\n
心配ないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……私は病欠、私は病欠）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな設定を心の中で繰り返しながら、彼女達の元へと歩み寄った。\n
彼女達の向かいの席へと、腰を下ろす。"

play sound se_0161
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「おはよう、二人とも。\n
席、いつもありがとうね」"

hide tower_a2_3
show tower_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice hei_g0038
Seito "「いいのよ、たまたま私達が早かっただけだから。\n
それに、あなたの話を聞きたかったの」"

hide tower_b1_2
show tower_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice chi_g0056
Seito "「そうそう。\n
もしかしたらあなたに会えるんじゃないかって、席をとっていただけだから気にしないで？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……ものすごく、待ち構えられていたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここまで期待されていると、病欠しただなんて偽の情報を差し出すのには罪悪感を覚える。だからといって、正直に本当のことを話せるかというと無理。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これから話すことになる病欠設定に説得力が増すよう、控えめな朝食を用意する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段ならサラダにトースト、オレンジジュースといった献立なのだが、今朝はトーストの代わりにヨーグルトにしておく。"

hide tower_a2_2
show tower_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0039
Seito "「あら？\n
あなた、今朝はこれだけ？」"

hide tower_b1_8
show tower_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0057
Seito "「少なすぎない？\n
授業始まってから、お腹鳴っちゃうわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_14")
T "（なんて完璧な前振り）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よしきた、とばかりに私は憂鬱そうな顔を作って見せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「それがね……、私、昨日の夜から体調がよくなくって。\n
寝込んじゃっていたのよ」"

hide tower_a2_9
show tower_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice hei_g0040
Seito "「え！？」"

hide tower_b1_5
show tower_b2_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice chi_g0058
Seito "「えええ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人が素っ頓狂な声をあげる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……ごめんね。\n
期待を裏切っちゃって）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中だけで謝罪する。\n
ナイトメアではないから、彼女達には心は読めない。"

hide tower_a1_5
show tower_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0041
Seito "「それじゃあ、あなた……。\n
ブリーズには参加できなかったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_3")
T "「……ええ。\n
残念だったわ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズらしいブリーズに参加できなかったことに関しては、実際本当に残念に思う気持ちもあるので、我ながらいい具合に感情を込められたと思う。"

hide tower_b2_4
show tower_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0059
Seito "「そんな……、タイミングが悪かったわね。\n
それで、今はもう大丈夫なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「ええ、今はもう。\n
せめて、皆が体験したブリーズの話を聞こうと思って来たのよ」"

hide tower_a1_1
show tower_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice hei_g0042
Seito "「無理はしないほうがいいわよ？\n
あなた、今も少し頬が赤いもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「……そう？\n
もしかしたら、熱が下がっていないのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "表面上はなんでもないように返したものの、内心どきりとした。\n
今現在私の顔が赤いとしたら、その原因はグレイだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの、「奥方発言」のせい。\n
実は、結構動揺は続いていた。"

hide tower_b2_5
show tower_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0060
Seito "「ブリーズの話ぐらい、いつでも聞かせてあげるわよ。\n
だから、もしも具合が悪いなら、無理せず部屋で休んだほうがいいわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「二人とも、心配してくれてありがとう。\n
そうね、自分でまずいと思ったら部屋に戻るとするわ」"

hide tower_a2_9
show tower_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice hei_g0043
Seito "「そうね、そうするといいわ。\n
季節も変わり目だし、無理は禁物」"

hide tower_b2_3
show tower_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice chi_g0061
Seito "「なんだったら、医務室に行って、ナイトメア先生に診てもらったほうがいいわよ。よく効く薬を出してもらえるかもしれないし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここでまた、どきり。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの名前が出てきただけで駄目だ。\n
演技の心配もないくらい、頬が赤くなり、熱っぽく見えるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「分かったわ、具合が悪くなるようだったらそうする。\n
でも、それまではあなた達の話を聞かせてくれない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「参加できなかったせいで、余計に興味津々なのよ。\n
昨夜のブリーズについて、詳しく教えてほしい」"

hide tower_a2_1
show tower_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice hei_g0044
Seito "「そう、たいしたものじゃないけど……」"

hide tower_b1_5
show tower_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice chi_g0062
Seito "「ええ、私達のブリーズなんて普通で……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は、顔を見合わせる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「その、普通のブリーズが知りたいの」"

hide tower_a2_9

hide tower_b1_1
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par02_ct_tow_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg06_sk_h_day
with stripe_l_medium

scene bg06_sk_h_eve with Dissolve(1)

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_day with Dissolve(1)

play music room2_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嘘をついてしまったから、天罰なのだろうか。\n
ブリーズから数日後、私は本当に体調を崩してしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "春から夏にかけて、季節の変わり目の気温の変化にやられてしまったのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最近は暑かったり寒かったりと、天気によって気温の上下が激しかった。"


scene bg24_rj_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝目覚めた段階から、頭が重くて起きられない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……職員か使用人に、連絡しなくちゃ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業を休む際には、各授業への連絡は不要だが、基礎クラスの担任には連絡しないといけないことになっている。\n
私の場合はゴーランドだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "連絡をいれなければと、思考はする。\n
だが、起きられない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "試しに声を出そうとしてみたところ、ひりつく痛みに喉が引きつった。\n
完璧に風邪だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「…………」"
menu:
    "どうにかして使用人を呼ぶ。":
        jump gakuen_nightmare_end2b
    "諦める。":
        jump gakuen_nightmare_end2a
label gakuen_nightmare_end2b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうにかして、身体を起こそうとする。\n
しかし、頭の位置を変えようとするだけで、すさまじい痛みが頭に響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく足掻いた後、ぐたりと脱力した。\n
余計に、要らない体力を使ってしまったような気がする。"

jump gakuen_nightmare_end3
label gakuen_nightmare_end2a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと息を吐き出して、目を閉じた。"

jump gakuen_nightmare_end3
label gakuen_nightmare_end3:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……おとなしくしていよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "動けないのだから仕方がない。\n
無断欠席ともなれば、逆にゴーランドのほうから使用人へと連絡がいくだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのうち、誰かに発見してもらえるはずだ。\n
熱が高いとなれば、看護に来てもらえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……そうなることを祈ろう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "というわけで、私は開き直って二度寝に突入した。"

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
show black onlayer master with close_m

play music view_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……ん）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひやりとした感触が、額に触れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……気持ちいい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "冷たい刺激に、意識が浮上した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、目を開けるのは億劫。\n
目を閉じたままとろとろと夢と現の狭間でまどろみ続ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと、額から冷たい感触が離れていく。\n
惜しくて、もっとと言いたいのに声が出ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "代わりに、遠くで言い争う声が聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0042
Gray "「ナイトメア先生……！\n
彼女の面倒は俺がみますから……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0043
Gray "「あなた自分の病弱っぷりを舐めているんですか！？\n
１００パーセント、感染りますよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0189
Nightmare "「それでも嫌なものは嫌だ！私以外が看病するのはおまえでも許せん！\n
彼女の面倒を見るのは私だ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0190
Nightmare "「私は学校医だぞ！？\n
病気の診られない医者などどうしようもないだろう！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0044
Gray "「それはそうですが……！\n
あなたは元々どうしようもないですし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0191
Nightmare "「なんだと、学校医に向かって……！\n
病人にこそ、私は必要とされているんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0045
Gray "「しかし、あなた自身も、常時病人に近いでしょう！？\n
あなたの部屋に運び込んでしまっては、完全に感染りますって……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0192
Nightmare "「うるさいな、おまえは！\n
いいんだ、感染っても！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0046
Gray "「……っ！？\n
全然よくありませんよ、ナイトメア先生！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0047
Gray "「仕事が溜まっているんですから！\n
ここであなたに病欠などされたらますます溜まります！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0193
Nightmare "「それでもいい！感染ってもいいし、仕事が溜まってもいい！\n
私が看病する！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0048
Gray "「………分かりました。\n
でしたら、たとえ風邪で倒れても仕事はしていただきますからね！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0194
Nightmare "「う、受けて立つぞ！\n
それなら、いいだろう！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（なんだ……、ナイトメアがまた駄々をこねているのね……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふにゃりと、口元が緩んでしまった。\n
ナイトメアが傍にいるというだけで、すっかり気が抜ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭がぼんやりしているせいで、彼らのやりとりの内容は理解できないが……。\n
どうせナイトメアが無茶を言っているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、どうせグレイは折れる。\n
私にも、それくらいは分かってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らの関係性。\n
そして、その中に加わる私。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふ、と吐息だけで小さく笑って、私はまた眠る。"


play music night_room_p_ali

scene bg_par24_rht_nig ##instant]
hide black with open_m
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次に目覚めたときには、だいぶ楽になっていた。\n
どれくらい眠っていたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目を開けると、見覚えのない天井が目に入る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……ここ、どこ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "医務室だろうか。\n
ともかく、自分の部屋でないことだけは確かだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドからの連絡で、どうやら無事に発見してもらえたということだろうか。\n
そういえば、夢か現実か、ナイトメアとグレイの話し声を聞いた気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（今は……、何日の何時？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すでに部屋の中は暗い。\n
最低でも、丸一日は眠っていたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むくりと身体を起こす。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！」"

show m_nai_end1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間近にいる人の気配に驚くが、隣で寝ていたのはナイトメアだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0195
Nightmare "「……んん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "平和そうな寝顔。\n
これは夢ではなく、現実だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……っ、痛）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメア、と呼ぼうとして喉に痛みが走る。\n
どうやら、酷く喉を痛めてしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろりと身を起こし、周囲を見渡して、ここがナイトメアの私室であることを知った。"

hide m_nai_end1
show m_nai_end2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0196
Nightmare "「……ん、ああ、[firstname]、目が覚めたのか。\n
具合はどうだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（だいぶ、よくなったわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice nig_g0197
Nightmare "「そうか、それはよかった。\n
君が登校していないとゴーランドから連絡を受けたメイドが様子を見に行って、君を見つけたんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice nig_g0198
Nightmare "「最初は熱も高かったが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉の途中で、伸びてきたナイトメアの手が私の額へと触れる。\n
ひやりと体温の低い手のひらに、私の体温が流れ込んでいく。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0199
Nightmare "「充分な休息をとったこともあり、熱もだいぶ下がったみたいだな。\n
ああ、喉が渇いただろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_18")
T "（……ええ。\n
何かもらえる？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われて初めて、とても喉が渇いていることに気付いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0200
Nightmare "「君、ココナッツジュースは平気か？\n
あれが一番、吸収が早いんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（あまり……、馴染みがあるとはいえないわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0201
Nightmare "「それなら試してみるといい。\n
たくさん汗をかいているはずだからね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当たり前のように、声に出さなくてもナイトメアとの会話が成立する。\n
今ばかりは、心を読むなと文句を言う気にもなれない。"

hide m_nai_end2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアはベッドを抜け出すと、さっそく飲み物の準備をしてくれた。\n
グラスに入ったココナッツジュースを差し出される。"

play sound se_0211
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きんと冷えたグラスが、熱を持った手にも気持ちいい。\n
少し白色がかった液体は口をつけると、すうっと身体に染み込むようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しょっぱいような、甘いような、よく分からない味だ。\n
まずくはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごくごくと喉を鳴らしてグラスを空ける。"


show nai_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0202
Nightmare "「お代わりは？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（いいわ、ありがとう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この一杯で、生き返ったような心地がする。\n
また熱が下がった気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（気のせいかしら）"

hide nai_m_02_1
show nai_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice nig_g0203
Nightmare "「そうともいえない。\n
体内に冷たいものが入ったのだから、その分だけ体温は下がるさ」"

hide nai_m_02_11
show nai_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice nig_g0204
Nightmare "「あまり冷やしてもよくないが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お代わりは、いらないといったはずだ。\n
それなのに、先ほどとは違うグラスを渡された。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くんと匂いをかいでみる。\n
こちらは、普通の水のようだ。"

hide nai_m_01_2
show nai_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0205
Nightmare "「薬を飲まないといけないだろう？\n
錠剤二つと、粉薬が一つだ」"

hide nai_m_01_11
show nai_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0206
Nightmare "「君が目覚めたら飲んでもらおうと思って、用意しておいたんだよ。\n
ほら、飲みなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（……げ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアほどではないが、私だって薬は好きじゃない。"

menu:
    "おとなしく頷く。":
        jump gakuen_nightmare_end4a
    "無言の抵抗を試みる。":
        jump gakuen_nightmare_end4b
label gakuen_nightmare_end4a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、病気なら飲むべきだ。\n
渋々ながら、おとなしく頷いた。"

hide nai_m_02_1
show nai_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0207
Nightmare "「いい子だ。\n
私を含め、すべての患者が君ほど聞き分けがよければいいんだがな」"

hide nai_m_02_12
show nai_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0208
Nightmare "「おとなしく頷いてくれてよかったよ。\n
ぐったりと寝ている君を相手に、最後の手段に出るべきか否か悩んだ……」"

jump gakuen_nightmare_end5
label gakuen_nightmare_end4b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薬を飲まず、ただこうして寝ているだけでここまで熱が下がっているのだ。\n
このまま休んでいたら、治ったりしないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（ああ、こんな発想が出てくること自体が病気の印かもしれないけど……）"

hide nai_m_03_9
show nai_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice nig_g0209
Nightmare "「飲まないと治らないからな。\n
言っておくが……、拒否するようなら最後の手段に出るぞ？」"

jump gakuen_nightmare_end5
label gakuen_nightmare_end5:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……最後の手段？）"

hide nai_m_03_12
show nai_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice nig_g0210
Nightmare "「アレだよ、アレ。\n
……{size=+20}座薬{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "{size=+20}（殺）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_13")
T "（実行したら、{size=+20}殺す{/size}。\n
本気だから）"

hide nai_m_02_9
show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice nig_g0211
Nightmare "「……っ！！\n
分かりやすい殺気だな！」"

hide nai_m_02_10
show nai_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice nig_g0212
Nightmare "「私だって、君の嫌がることは嫌だとも！\n
だから、おとなしく薬を飲んでくれ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まずは錠剤を渡された。\n
口の中に放り込み、水で流し込む。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごっくん。\n
上手く飲むことが出来た。"

hide nai_m_03_3
show nai_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0213
Nightmare "「……君は薬を飲むのが上手だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（こんなのに、上手いも下手も……）"

hide nai_m_03_10
show nai_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice nig_g0214
Nightmare "「私はいつも三回ぐらい飲み込むのに失敗し、途中で薬が溶け出し、吐き気を催すような不味さに悶絶する羽目になるぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（それは、あなたが下手すぎるのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "病弱で、私などよりもよっぽど医者やら薬の世話になっているはずの男なのに（というか、本人が医者）。"

hide nai_m_03_5
show nai_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0215
Nightmare "「自分で医者になれば、自分の病気を薬や痛い治療以外の方法でなんとか出来るかもしれないと思ったんだが……」"

hide nai_m_03_9
show nai_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0216
Nightmare "「……分かったのは、どうしようもないということだけだったな。\n
薬や痛い処置は避けられない……、医者であろうとも」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……なんだか、影をしょいこんでいるわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、おかげで医者に対する不信感からは解放されたのではないだろうか。"

hide nai_m_03_6
show nai_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0217
Nightmare "「そうだな。\n
他に方法がないと分かった分、諦めもついたよ」"

hide nai_m_02_1
show nai_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0218
Nightmare "「さ、次は粉薬だ。\n
私は粉薬というのが、蛆虫のように嫌いだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（嫌っていても、虫になんか例えないでよ。\n
これから飲む人に向かって……）"

hide nai_m_03_8
show nai_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice nig_g0219
Nightmare "「ああ、すまない。\n
だが、飲んでもらうぞ、辛いかもしれないが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薬包紙に包まれた粉薬を差し出される。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっと錠剤ですら苦しむナイトメアのことだ。\n
粉薬など、自殺行為に等しいに違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むせて、気管に入れては悶えるのだ。"

hide nai_m_02_7
show nai_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0220
Nightmare "「……よく分かったな」"

hide nai_m_02_11
show nai_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0220_5
Nightmare "「あまりにも拒否するものだから、最終的には部下に取り押さえられ、グレイに喉の奥に手をつっこむ勢いで流し込まれるパターンが多いぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（それで、余計に嫌いになるわけね？）"

hide nai_m_03_9
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice nig_g0221
Nightmare "「……その通り」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（分かりやすいなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は薬包紙を受け取ると、それを開いて三角形を作った。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……苦い？）"

hide nai_m_02_4
show nai_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nig_g0222
Nightmare "「味わおうなどと思わないほうがいい。\n
……そんな味だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……了解）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "経験者は語る、だ。\n
クソまずいのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はこれまた覚悟を決めて、味覚がない（と思われる）喉奥めがけてさらさらと粉薬を流し込んだ。\n
そして、すぐさま水を飲む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逆流すると、かえって味わってしまうことになるため、少量で一気に押し流す。"

hide nai_m_01_10
show nai_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0223
Nightmare "「……すごいな、君。\n
本当に、薬を飲むのがうまい」"

hide nai_m_01_2
show nai_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0224
Nightmare "「味に苦しむ思考もほとんどなかったぞ？\n
いやはや、羨ましいな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（コツがあるのよ。\n
……滅多に風邪をひかない私でも、コツを知っているのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、普段あまり病気をしない。\n
その代わり、今回のように一度かかってしまうと長引くのだ。"

hide nai_m_01_1
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0225
Nightmare "「着替えを用意してある。\n
どうだ、着替えられそうか？手伝おうか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……遠慮するわ。\n
自分で着替えられる）"

hide nai_m_02_4
show nai_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice nig_g0226
Nightmare "「……少し、楽しみにしていたのに。\n
まあいい、これだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（楽しみに、って……。\n
よしてよね、こういうのは見られたくないものなの）"

hide nai_m_02_7
show nai_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice nig_g0227
Nightmare "「……はいはい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "差し出された着替えを受け取る。\n
寝ている間にずいぶんと汗をかいたのか、着ているネグリジェがしっとりと蒸れて気持ち悪い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はナイトメアがこちらに背を向けてくれているのを確認してから、ネグリジェを脱いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "着替えと一緒に渡されていたタオルで身体を拭き清める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当ならば、シャワーを浴びたいところだ。\n
もちろん、医者がいるこの場では反対されるに決まっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"

play sound se_0117
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばさりと着替えを広げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（ナイトメア！？）"

hide nai_m_03_10
show nai_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice nig_g0228
Nightmare "「なんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声が、明らかにわくわくとしている。\n
一方、私は広げた着替え片手にわなわな……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（なんで、シャツ一枚なのよ……っ！）"

hide nai_m_03_11
show nai_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice nig_g0229
Nightmare "「恋人の部屋に泊まるときの正装といったら、シャツ一枚と決まっているだろう！\n
それがロマンだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "（そんなロマン捨てなさい、今すぐ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの夜のこともあるし、ナイトメアがロマンチシズムに大いに憧れているというのは知っていたが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不満はいっぱい。\n
だが、罵詈雑言をぶつけようにも、声は出ず。"


play music night_a_wam
play sound se_0551

show m_nai_end3 onlayer master
with dis
hide nai_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何も着ないわけにもいかないので、シャツを着る。\n
ナイトメアのシャツ、だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（……意外と、大きいのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは、あまりがっしりしているようには見えない。\n
病弱だし、顔が中性的なせいもあって、細身に映る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（もっと、細いかと……。\n
筋肉もなさそうだし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice nig_g0230
Nightmare "「……君、私のことをそんなふうに思っていたのか。\n
ショックだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "黙秘。\n
だが心を読まれているので、無意味極まりない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中を無に出来るほど、私は悟りを開いていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（でも、本当に意外だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは細い。\n
実は私より細いんじゃないのか、と疑ったこともある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、こうしてシャツを借りてみると、私にはぶかぶかで大きいことが分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ちゃんと、男の人なのね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice nig_g0231
Nightmare "「いや、だから、君、それは失礼だぞ。\n
私のどこが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぶつぶつとぼやくナイトメアは、放置しておく。\n
と、ぐっと腰に腕が絡みついて、ずりずりと引き寄せられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（ナイトメア？）"

play sound se_0327 volume .6
hide m_nai_end3
show m_nai_end4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice nig_g0232
Nightmare "「こうして、君を懐に抱えこめる程度には、私だって男だよ。\n
手だって君よりも大きい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大きさを比べるように、手を重ねられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの手は、ピアニストのようだ。\n
骨ばっていて、指が長い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その長い指が、するすると私の指に絡む。\n
そのまま懐に抱き込まれ、押し倒されてしまいそうになって、慌てる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（ナイトメア！？\n
感染るわよっ！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただでさえ体の弱いナイトメアなのだ。\n
こうして私といるだけで、心配なくらい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（そういえば……、いつからいたの？\n
もう、手遅れ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "病を引き寄せるような印象さえ持つ、色白な彼。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな密着までしたら、私にいる菌がすべてナイトメアのほうに移住してしまうのではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0233
Nightmare "「ふ、私の体の弱さを舐めてもらっては困るな。\n
君をこの部屋に運びこんだ時点で、もうとっく感染っている！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "{size=+20}（駄目じゃない）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すでに感染っていると主張されてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0234
Nightmare "「そう、駄目なんだよ。\n
手遅れだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0235
Nightmare "「これ以上、君と一緒にいようがいまいが、私の発病は確実だ。\n
だから、どうせなら一緒にいてくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（なんで……、一緒にいたのよ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今からでは遅いだろうが、最初から近付かない手もあった。\n
自室などに連れ込んだらどうなるか、想像はついたはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0236
Nightmare "「私が発病したら……、看病してくれるだろう？\n
君が、優しく」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_10")
T "（そうね……。\n
優しく、{size=+20}グレイに引き渡すわ{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice nig_g0237
Nightmare "「……{size=+20}愛が足りないぞ{/size}」"

play sound se_0327
hide m_nai_end4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごろん、と。\n
ナイトメアに抱えこまれたままベッドに転がった。"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抱きしめる腕が一度緩んで、足元に固まっていたかけ布団を肩口まで引き上げてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（ああ、優しく{size=+20}最終手段でもいいわね{/size}）"


show nai_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_6")
voice nig_g0238
Nightmare "「……やめてくれ。\n
君にそんなことをされたら、立ち直れなくなる」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな、馬鹿な話をしながら。\n
自然と顔の位置が近くなって、ちゅ、と口付けを交わしていた。"


show m_nai_end5 onlayer master
with dis
hide nai_m_02_8

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの体温がいつもより冷たく感じるのは、私自身の体温がいつもより高いからなのだろう。\n
触れる唇まで、ひやりとしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……完全に、感染しちゃったわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_9")
voice nig_g0239
Nightmare "「人に感染すと、治りが早いというからな。\n
……私に感染してくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（遠慮なく、そうするわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "互いに、開き直る。\n
掛け布団の中、引っ付きあって、何度もキスを交わした。"

hide m_nai_end5

with dis
$ hi_mes()

scene bg_par24_rht_nig with Dissolve(.8)

scene bg_par15_rg_tow_nig
with stripe_l_medium

scene bg06_sk_h_nig
with stripe_l_medium

scene bg06_sk_h_day with Dissolve(1.2)

play music daytime_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく喉のほうはよくならなかったものの、熱のほうだけなら次の日には下がってくれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、私がすっかり治った頃……。\n
お約束のように、ナイトメアが発熱した。"


scene bg_par15_rg_tow_nig with Dissolve(1)

scene bg_par24_rht_day with stripe_l_medlong

play music high_day_p_wam
##[rchara2 PAY ATTENTION="false"]
show gre_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0049
Gray "「だから、言ったでしょう！\n
ほら、自業自得なんですから！薬を飲んでくださいよ！」"


show m_nai_end6 onlayer master
with dis
hide gre_m_01_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「意地張ってないで、薬ぐらい飲みなさいよ。\n
顔に死相が出ているわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「なになに？\n
グレイが、優しく喉の奥まで手を突っ込んでくれたら飲める？」"

hide m_nai_end6
show m_nai_end7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gra_g0050
Gray "{size=+20}「よし」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイが傍らでぐいっと袖をまくり、それを見たナイトメアがますます青ざめた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当然だが、私にはナイトメアのように心を読むようなことは出来ない。\n
今のは、ただの脅しだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、グレイは真面目。\n
自分で飲まなければ、現実になる。"

play sound se_0232
hide m_nai_end7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むくっとゾンビのような動きで身を起こしたナイトメアが、ベッドサイドに置かれていたノートとペンを手に取った。"

play sound se_0333

show gre_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0051
Gray "「なんです……？\n
遺言ですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さりげなく不吉なことを呟きながら、グレイはノートを覗き込んだ。"

hide gre_m_03_11
show gre_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0052
Gray "「なになに……？\n
ああ、[firstname]、君の口移しならば飲める気がする、とのことだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「は？」"

hide gre_m_02_10
show gre_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice gra_g0053
Gray "「なるほど、定番ですね……。\n
……[firstname]、どうする？」"


show m_nai_end8 onlayer master
with dis
hide gre_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "{size=+20}「最終手段で」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（馬鹿じゃないの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口移しなんかしている間に錠剤はどんどん溶けて恐ろしい味になるし、粉薬なら最初から酷い味だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私まで巻き込んで、どうしてより酷いことにしたがるのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0240
Nightmare "{size=+20}「！！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0054
Gray "「……最終手段？\n
なんだ、それは？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「ああ、それはね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice nig_g0241
Nightmare "{size=+20}「！！！！！！」{/size} "

play sound se_0007
hide m_nai_end8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアが、力を振り絞って抵抗を開始した。\n
逃げ出そうとしているようだが、こちらは二人、難なく押さえ込む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、もともと体力がない上に、現状は風邪で弱りきっている。\n
すぐに、がくりと力尽きた。"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「今よ、グレイ。\n
今のうちに……」"


show gre_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice gra_g0055
Gray "「最終手段か？\n
なんだか、よく分からないが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「違うわよ！\n
薬のほう！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抵抗できなくなっているうちに、錠剤および粉薬を流し込むのである。\n
今ならば、飲んだ振りも出来ないだろうし、吐き出す気力もないはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（本当、手がかかるんだから）"

hide gre_m_02_4
show gre_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gra_g0056
Gray "「ああ、分かった。\n
今のうちに……」"


show nai_m_01_7 at center
with dis
hide gre_m_02_10

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逃げられないと悟ったのか、ナイトメアもおとなしくなった。\n
体はがっちりと押さえ込まれた状態で、右手だけがふらふらと彷徨っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ん？\n
何？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かを探しているらしい。\n
先刻の、ペンだ。"

play sound se_0333
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは、急いで何かを書いている。\n
今度こそ、遺言だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（たかが薬に大袈裟な……）"


play music flower_eve_p_wam

show m_nai_end9 onlayer master
with dis
hide nai_m_01_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、ノートを覗いて、笑ってしまった。\n
そこにはがたがたに歪んだ字で、こう書かれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "『薬が飲めたら、ご褒美にキスをしてくれ』 "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……子供なのか大人なのか）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いいわよ、いくらでも」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "汚い文字で書かれた、ノートの走り書き。\n
これは、貰ってしまおう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_10")
T "（なんて、素敵なラブレター）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "締まらなくても、ロマンチック。"

hide frame_par_togaki
hide ali_m_06_16
with Dissolve(2)
hide m_nai_end9
show white onlayer master
with compress_extralong
scene black with compress_extraextralong
pause 1
stop music
##endmemory
jump gakuen_a
