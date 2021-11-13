jump fushigi_common3_castle
label fushigi_dad3_1:

scene map_bg_spring_day
with stripe_l_medium

scene charasel_bg_castle_day
with stripe_l_medium

scene hg_01
with stripe_l_long
play sound se_0275

play music castle_guestroom_p_ali

show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0351
Peter "「[firstname]、お迎えに来ました！\n
さあ、行きましょうっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ペーター？\n
……あ、ひょっとして、クロケーの道具が届いたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターと一緒に街へ買い物に行き、大きさの違う双子にあったのは、大分前の時間帯だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（二回時間帯が変わる前にはとか言っていたわりには、ちょっと遅かったわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターのことだ、荷物が届いたその瞬間に呼びに来ると思っていたのだが、いつもより行動が遅い気がする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（まあ、この世界で早いも遅いもないんだけど……。\n
なんとなく、ペーターにしては遅かったというか）"

hide per_t_02_5
show per_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice pet_f0352
Peter "「いえ、道具そのものは早々に届いていたんですが、前回余計な邪魔が入ったので、今回はあなたに迷惑をかけないようにしようと思いまして」"

hide per_t_01_4
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice pet_f0353
Peter "「ルールブックを完全暗記して、実践して準備をしていたら、こんなに間が開いてしまいました」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_11")
T "（ゲームのルールを覚えるよりも、仕事をしなさいよ、あんたは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城の宰相という大層な役がついているのに、仕事よりも私のほうが、彼にとっては優先順位が高い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（まあ、この人に文句を言えるような人なんて、ビバルディぐらいだものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、その肝心の上司も仕事をエスケープする人だから、結局のところ苦労するのは下の人間ということになる。"

hide per_t_02_8
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0354
Peter "「ええ、本当に遅くなってしまってすみません、[firstname]。\n
でも、今度は大丈夫です！」"

hide per_t_03_1
show per_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0355
Peter "「どんな事態にも対応できるよう、すべてのＱ＆Ａも確認して、覚えてきました！\n
僕は賢いウサギでしょう、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「そうね。\n
賢いのは否定しないけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうしてその能力を、こういう方向にしか発揮しないのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ペーターは優秀なんだから、私に構うよりももっと色々なことが出来そうなのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もったいないとも思う。\n
潔癖症、ストーカー、電波気質なウサギ。\n
だが、その辺りを修正すれば、頭もよくて地位もあり、見た目だって悪くない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（まあ、それが治ったら、ペーターじゃないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だけを見る白いウサギ。\n
私をこの世界に連れ込んだ案内人にして、元凶だ。"

hide per_t_02_1
show per_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0356
Peter "「[firstname]、どうしました？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「……ううん、何でもないわ。\n
行きましょう」"

play sound se_0361
pause .5
play sound se_0776
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首を傾げるウサギを促して、私は赤い背中の後ろに続いた。"

hide per_t_01_11

$ hi_mes()

scene hn_spr_01
with stripe_l_long

scene bg_gen_sky_spr_day
with dis

play music castle_garden_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "前回中断してしまったゲームの説明を聞き、槌を持った私は練習としてボールに狙いを定めた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_13")
T "「ええと……、この槌でボールを打てばいいのよね？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_13")
voice pet_f0357
Peter "「ええ、そうです。\n
すべてのフープを潜らせて、最後にあの中央の杭に当てれば終了です」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「ルールはよく分かったんだけど……。\n
どうして、あなたがそこにいるの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice pet_f0358
Peter "「だって、あなたは初心者でしょう、[firstname]？\n
じっと見つめていてあげないと、僕は心配で心配で」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「だからって、{size=+20}地面に寝そべった相手に下から見られていたら、私だってやりにくいわよ！{/size}」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（綺麗好きなくせに、何をしているのよっ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice pet_f0359
Peter "「えー、そうですか？\n
でも、ここが一番の特等席じゃないですか」"


show t_twi3_1and3_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段は他人に触るのも嫌がる潔癖症のペーター。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが何を思ったのか、にこにこと笑いながら、頬杖をついた姿勢のまま地面に寝そべっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふさふさの芝が茂っているので、直接土に触れるようなことはないだろうが、それにしても奇妙な光景だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（…………）"


play music honobono1_a_ali
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（そういえば、私もよくこうやって寝っ転がっていたわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "姉さんは行儀が悪いと言っていたが、笑うばかりで止めたりはしなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "下から見上げると、また違った世界が見える。\n
同じ人でも、角度によって色々なものが見えることがある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（自分の憧れを見る気持ち）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "届かないもの。\n
手で触れられないもの。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの人は、私にとって非の打ち所のない、完璧な人だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見上げることで遠くに感じて……、自分との違いに苦笑いと、安堵を覚えていたことを思い出す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "姉さんのようにはなれないと知っていて、見上げる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが私の居場所なのだと受け入れていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（ペーターから見て、どう見えているのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が姉さんを見ていたときのように、彼も見ているのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……憧れて？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（あるいは、羨ましがって？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あり得ない。\n
私に焦がれるような奇特な人が、いるはずがないのだから。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0360
Peter "「[firstname]？\n
どうかしましたか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「特等席ってあんたは言うけど、そこから見る私はどう見える？」"

hide t_twi3_1and3_3
show t_twi3_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pet_f0361
Peter "「どうと言われましても……、困ってしまいますね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までじっと見つめていたはずのペーターは、そっと視線を外してもじもじとしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "白い肌が少し上気しているように見えたのは、私の気のせいだろうか。"

hide t_twi3_2
show t_twi3_1and3_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0362
Peter "「あなたは……、僕の光ですよ、[firstname]。\n
いつでも眩しくて、あなたを見ずにいられない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_7")
T "「ペ、ペーター」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然真面目な声で言われて、私のほうが反応に困ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "愛しい人だとか、花だ蝶だと色々な言葉でたとえられたことはあったが、ここまでストレートなものは珍しい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「そ、そういうときは、太陽とかそういう表現が来るんじゃないの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "照れ隠しもあってか、早口で聞き返すと、ペーターは今も空に浮かぶ太陽を見上げて、首を振った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0363
Peter "「あなたは、あんなに強烈で、一方的な存在じゃありません。\n
もっと……、気を付けていないと消えてしまいそうな存在です」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_10")
voice pet_f0364
Peter "「ですから、僕が守ってあげたいんです！\n
ずっとずっと、僕だけが見守って、僕が幸せにしてあげたいんです、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_10")
voice pet_f0365
Peter "「だから、このままずっとハートの城にいてくださいね！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（…………）"

play sound se_0424
$ flash(.2)
hide t_twi3_1and3_3
show t_twi3_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice pet_f0366
Peter "「だっ！？\n
な、何をするんですか、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こつんと軽く白い頭を小突く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「すぐにそっちに話を持っていくんじゃないわよ、このストーカーウサギ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（一瞬でもときめいた自分が急に馬鹿馬鹿しくなってくる）"

play sound se_0126
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「ほら、そこをどいてよ。\n
今度こそ本気で当てるわよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターは地面で私に叩かれた場所を押さえているが、いまだに動く気配がない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本気だというように手にした棒を何度も振るが、彼のいうところの特等席からは離れない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0367
Peter "「いいえ、動きません。\n
あなたとのゲームなんですから、僕は一番近くであなたを応援してあげたいんです！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「……応援って」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（二人でゲームをするなら、私はあんたの対戦相手ってことになるんだけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっと地面から起き上がる気配のないペーターの説得を諦めて、私は構えに入る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_4")
T "「……まあ、背中から抱きかかえられて、手取り足取りなんてべたな展開よりはマシだけど」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice pet_f0368
Peter "「あ、そういう方向がお好みですか？\n
それでしたら、遠慮なく言ってください、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice pet_f0369
Peter "「僕は全身全霊をかけて、あなたの身体に直接教えてあげますから！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「それ以上変なことを言ったら、本気で、これで、殴るわよ？」"

play sound se_0441
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_9")
voice pet_f0370
Peter "「う、あなたに殴られるのなら本望ですけど……。\n
それは、さすがに痛そうですね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "槌を振って見せると、ペーターは眉を寄せて迷っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「痛そうじゃなくて、痛いわよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「……試してみる？」"

play sound se_0441
play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_13")
voice pet_f0371
Peter "「遠慮します」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_4")
T "（よろしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "両手を挙げて降参を示した相手に、わざと大仰に頷いた私を見て、ペーターはますます柔らかな表情を浮かべて、私を見上げてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "安堵したような顔だった。"

hide t_twi3_4
show t_twi3_5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0372
Peter "「……ふふ、よかった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pet_f0373
Peter "「あなたが笑ってくれたでしょう。\n
少しは元気が出たようで、安心しました」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pet_f0374
Peter "「あなたは怒っている顔も勿論魅力的ですが、僕としてはやはり笑っていてくれるほうが嬉しいです」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「誰にでもっていうわけじゃないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターは、私が帽子屋屋敷を出てこの城に来てから、ずっと私のことを気に掛けてくれている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「あんたと一緒にいるからよ。\n
あんたが特等席で見ていてくれるから、元気でいられる」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T "（このウサギは、本当に不思議）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ずっと前から私のことを知っていたと、ペーターは言う。\n
私がペーターを好きだから、ペーターも好きになったのだと。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（順番が逆だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何度聞かされてもそう思ってきたが、今となっては順番なんてどうでもいい。\n
唯一無二の愛情のような、強いものではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、断ち切ることが出来ない感情が胸の内に宿っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（理由も正体も分からないけど。\n
この気持ちは、悪いものじゃない）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「……好きな人が近くにいるんだもの、元気になれるわ」"



hide t_twi3_5


play music castle_garden_p_ali

show per_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
Peter "「！！！」"

play sound se_0052
hide per_t_01_2
show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice pet_f0375
Peter "「[firstname]……。\n
僕も、あなたが大好きです、愛しています！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "感極まったペーターが身を起こし、私に向かって両手を伸ばしてくる。"

play sound se_0055
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ちょ、ちょっとペーター！？」"

hide per_t_02_13
show per_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice pet_f0376
Peter "「僕の愛しい人、僕もあなたがいれば元気ですよっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_13")
T "（……人の話を聞け！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の声を無視して抱きついてきたペーターは、そのまますりすりと身体を寄せてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、それ以上のことはしない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "以前ならキスを迫ってくることも珍しくなかったが、今の彼はその辺りの分別が出来ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、私もつい許してしまう。"

hide per_t_03_11


scene bg_gen_sky_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「……はあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振りほどこうかと思ったが、諦めてしたいようにさせることにする。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0377
Peter "「[firstname]、[firstname]。\n
ああ、あなたはやはり僕の光、希望そのもの！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0378
Peter "「あなたがいれば、僕の世界はこんなにも眩しいんですね！」"

play sound se_0125
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（……何、この音？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターに抱きつかれているせいで、視界が極端に狭まっているが、嫌な音が聞こえる。\n
まるで硬いものを投げたかのような、音。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！」"

play sound se_0501
$ flash(.2)
play sound se_0506
$ flash(.1)
$ flash(.1)

scene hn_spr_01
with dis

show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_6")
Peter "「…………」"

hide per_t_02_7
show per_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_6")
voice pet_f0379
Peter "「まったく、ここには誰も近付けるなと厳命をしておいたはずなんですがね」"

hide per_t_02_11
show per_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_6")
voice pet_f0380
Peter "「所詮顔なしにはすぎた命令でしたか。\n
僕と彼女の愛を邪魔したんですから、覚悟は出来ていますよね」"


play music deedam_t_ali

show dee_p_02_10 at center
hide per_t_03_7
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_6")
voice dad_f0152
Dee "「ああ、どうりでいつにも増してお城の兵士さんがしつこいと思ったんだよね。\n
全部、斬っちゃったけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……ディー、ダム？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "生け垣の合間から姿を見せているのは、帽子屋屋敷の双子の門番……、のはずなのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_6")
T "（何で、今回もまた大人と子供の姿なのよ？）"

hide dee_p_02_10
show dee_p_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice dad_f0154
Dee "「まったく、通りすがりのお城の見学者に失礼な話だよね。\n
問答無用で斬りかかってくるんだもん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今回は子供姿のディーがそんなことを言う隣で、大人になったダムがこくこくと頷いている。"

hide dee_p_02_13
show dee_p_02_13 at left
show dam_p2_02_8 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0156
Dam "「その上、僕らの大事なお姉さんはこんなところでウサギに襲われている」"

hide dam_p2_02_8
show dam_p2_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0157
Dam "「由々しき事態だよ。\n
お城に入るために、ハートの城の見学ツアーなんて悪趣味なものに大金を払った意味はなかったね」"

hide dam_p2_02_9
show dam_p2_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0158
Dam "「無駄金を使うなんて、二重の意味でショックだ」"


show per_t_01_14 at center
hide dee_p_02_13
hide dam_p2_02_12
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0381
Peter "「先刻からうるさいですね。\n
僕と彼女は愛のゲーム中なんです、邪魔をするなら容赦はしませんよ」"


show dee_p_02_2 at center
hide per_t_01_14
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0159
Dee "「へえ、どう容赦しないの？」"

hide dee_p_02_2
show dee_p_02_2 at left
show dam_p2_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0161
Dam "「だったら、遠慮なんてしていられないよね。\n
お金がかかることは嫌だけど、今回だけは大盤振る舞いしてあげる」"

play sound se_0084
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人とも、言うが早いか、その手に大斧を持って私達へと向かってくる。"


show per_t_02_2 at center
hide dee_p_02_2

hide dam_p2_02_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0382
Peter "「ふっ……、いいでしょう。\n
いつも目障りだと思っていたんです、ここで決着を」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「待ちなさい、ペーター。\n
二人も、動かないで」"


show dee_p_02_11 at center
hide per_t_02_2
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice dad_f0162
Dee "「お姉さん？」"

hide dee_p_02_11
show dee_p_02_11 at left
show dam_p2_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice dad_f0163
Dam "「どうしたの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「……この前にも言ったわよね、あんた達。\n
私、まだ怒っているんだけど？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本当は口で言うほど怒ってはいない。\n
ペーターとのやりとりで、大分気持ちは落ち着いていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（でも、ここで甘い顔を見せれば軽く思われそうなんだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悪いことは悪いと教えなければ、この子達の場合、そのまま勘違いして進めてしまいそうだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の行動も子供っぽいが、教えてくれるまで帰らないと決めたからには、後には引けない。"

hide dee_p_02_11
show dee_p_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dee "「…………」"

hide dam_p2_02_10
show dam_p2_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "棘のある言葉に、二人は困ったように視線を合わせて目線だけで相談をしている。"

hide dee_p_02_8
show dee_p_02_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0164
Dee "「……うん。\n
だから、僕達、今回はお姉さんに許してもらおうと思って来たんだ」"

hide dam_p2_02_13
show dam_p2_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0166
Dam "「わざわざ悪趣味なハートの城の見学ツアーに高いお金を払ったのも、穏便にお姉さんを迎えに来たかったからなんだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「……ふうん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（それ以前に、この城の見学ツアーなんてものがあったことに驚いたわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "需要がまったく見込めそうにないのだが……、ツアーとして存在している以上はある程度ニーズがあるのだろう、多分。"

hide dee_p_02_9
show dee_p_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0167
Dee "「仕事をさぼるとお姉さんが気にするから、ちゃんと有休を使ってここに来たし。\n
僕達、精いっぱい誠意を見せたんだよ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"


show per_t_01_14 at center
hide dee_p_02_6
hide dam_p2_02_8
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice pet_f0383
Peter "「ふん、所詮子供の戯言です。\n
さあ、[firstname]、僕とゲームを続けましょう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_4")
T "（ゲーム）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらりと地面に転がっているボールを見て、私の顔に笑みが浮かぶ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「そうね、一度仕切り直して遊び直しましょう」"


show dee_p_02_3 at center
hide per_t_01_14
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
Dee "「！！」"

hide dee_p_02_3
show dee_p_02_3 at right
show dam_p2_02_3 at left
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
Dam "「！？」"

play sound se_0672
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サイズは違うのに、まったく同じ表情を浮かべた二人が斧を振り上げた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_4")
T "「そうそう……、そこの通りすがりさん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、二人が斬りかかってくるよりも私のほうが早い。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「このゲームには、プレイヤーが四人必要なの。\n
よかったら、一緒に遊んでくれない？」"


show per_t_01_5 at center
hide dee_p_02_3

hide dam_p2_02_3
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pet_f0384
Peter "「え……、ええ！？\n
どうしてですか、[firstname]！」"

hide per_t_01_5
show per_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pet_f0385
Peter "「僕と二人っきりで愛のゲームをしましょうとあれほど固く誓い合っていたじゃないですか！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（誓い合っていない、誓い合っていない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想通り今度は不満の声を上げたペーターの対応は、私も慣れている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「いいじゃない、ちゃんとした形でやったほうが楽しいでしょう？」"

hide per_t_01_6
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice pet_f0386
Peter "「ですが……。\n
いいえ、やはりこれは僕とあなたのゲームで……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_2")
T "「誰がいても、ペーターは楽しいゲームにしてくれるでしょう？\n
私のために」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にっこり。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（……わざとらしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鏡を見たら、さぞかし嘘くさい笑みを浮かべているだろう自分を想像しつつ、最後の一押しをすると白い耳がぴんと立ち上がった。"

hide per_t_02_6
show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0387
Peter "「勿論、あなたのためなら、誰がいようと楽しいゲームにしてみせます！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「……ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_4")
T "（乗せやすいな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よくも悪くも、この宰相様は純粋らしい。"

hide per_t_02_5

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music castle_garden_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……というゲームなんだけど、ちゃんとルールを守って出来るんでしょうね、あなた達？」"


show dee_p_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice dad_f0168
Dee "「勿論だよ。\n
僕達、子供だもん、初めてのゲームでもうまいに決まっているよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（僕達……って、ダムが大人姿なのを忘れているわよね。\n
適当な設定だ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうは思いつつも、目をつぶっておくべきなのは分かっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「くれぐれも、ルール違反はしないでね？」"

hide dee_p_02_4
show dee_p_02_4 at left
show dam_p2_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0169
Dam "「うん、分かっているよ。\n
僕達は賢いから、ちゃんとやるよ、お嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「だから、その呼び方はやめなさいって」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "溜息をつきながら二人にボールを渡す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本来ならば、このゲームは青と黒、赤と黄色でペアなのだが、今回は特別ルールで青と赤のボールを双子に手渡す。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（イメージカラーのどちらかだけって言うのも、落ち着かないものね）"

hide dee_p_02_4

hide dam_p2_02_10
show dam_p2_02_10 at left
show per_t_03_1 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice pet_f0388
Peter "「はい、[firstname]。\n
どうぞ」"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「ありがとう……、あ。\n
二人の槌もあったかしら？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本来四人で遊ぶものだが、ペーターのことだ。\n
もしやと思って問いかければ、彼は予想通り首を横に振った。"

hide per_t_03_1
show per_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0389
Peter "「ああ、そういえばありませんね。\n
ボールだけは四つでセットでしたが、槌までは確認しませんでした」"

hide per_t_03_7
show per_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0390
Peter "「お邪魔虫なんて入れるつもりもなかったですし」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（やっぱり）"

hide dam_p2_02_10

hide per_t_02_7
show per_t_02_7 at left
show dee_p_02_5 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice dad_f0170
Dee "「ようは、このボールが打てればいいんだよね。\n
だったら、これでいいよ」"

play sound se_0672
##special anime kiseki02
hide per_t_02_7

hide dee_p_02_5
show dee_p_02_5 at left
show dam_p2_02_4 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice dad_f0172
Dam "「うん、そうだね。\n
大丈夫だよ、これぐらい動物相手にはいいハンデだもん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "斧を取り出した二人はそう言って、得意げに構えて見せた。"

hide dee_p_02_5

hide dam_p2_02_4
show dam_p2_02_4 at left
show per_t_01_15 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0391
Peter "「ほう、言いますね。\n
だったら、圧倒的な大差で負けさせてあげましょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（ただの球技にそこまで熱意を燃やさないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピリピリとした空気を感じて、頭を抱える。\n
しかも、ここの住人と来たら熱意が一瞬にして殺意に変わることも珍しくない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「斧を使うのはいいけど、振り回して私達に当てたりしないでよ」"

hide dam_p2_02_4

hide per_t_01_15
show per_t_01_15 at left
show dee_p_02_10 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice dad_f0173
Dee "「うん、分かっているよ。\n
斧の使い方には充分気を付けるから、安心してよ、お姉さん」"

hide per_t_01_15

hide dee_p_02_10
show dee_p_02_10 at left
show dam_p2_02_5 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice dad_f0174
Dam "「じゃあ、お先にどうぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「え？\n
いいの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先攻と後攻を決めようとしていた私に、双子は先を譲ってくれる気らしい。"

hide dee_p_02_10
show dee_p_02_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0175
Dee "「ふふふ、レディ・ファーストだよ」"

hide dam_p2_02_5
show dam_p2_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0176
Dam "「ウサギに先を譲るなんてごめんだけど。\n
お姉さんになら喜んで譲ってあげる」"

hide dee_p_02_1

hide dam_p2_02_10
show dam_p2_02_10 at left
show per_t_03_9 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0392
Peter "「……偉そうなことを」"

hide per_t_03_9
show per_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0393
Peter "「まあ、いいでしょう。\n
さあ、[firstname]、あなたの腕前をぜひ見せてください！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "意気揚々と言ったペーターは、さすがに双子がいる前で地面に横たわる気にはなれなかったのか、私の後ろに立ってくれた。"

hide dam_p2_02_10

hide per_t_02_8

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_8")
T "「……それじゃあ、よっと」"

play sound se_0220
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "スタートラインに置いた黄色いボールはころころと転がって、まっすぐに進んでいく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_1")
T "（……あ、結構いい位置までいったわ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「うん、まずまずね」"


show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice pet_f0394
Peter "「さすがです、[firstname]！\n
ああ、あなたは何をしていても完璧です！」"


show dee_p_02_4 at center
hide per_t_02_13
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice dad_f0177
Dee "「じゃあ、次は僕だね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私に続いてスタートラインに立ったディーが青いボールを手にして、構え始める。"

hide dee_p_02_4

$ hi_mes()

scene bg_gen_sky_spr_day
with dis

play music castle_garden_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボールを潜らせねばならないフープは、全部で１２カ所。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "途中までは、銃も刃物も飛び出さずに進んだゲームの流れがおかしくなったのは、ペーターが打ったボールがダムのボールを弾いたときだ。"

play sound se_0220

scene hn_spr_01
with dis

show per_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0395
Peter "「おや、では僕がもう二打追加ですね。\n
ついでに……、{size=+20}ふんっ{/size}」"

play sound se_0220
hide per_t_02_2
show per_t_02_2 at left
show dam_p2_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam "「！！」"

hide dam_p2_02_10
show dam_p2_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0180
Dam "「な、何をするんだ！\n
僕のボールが……」"

hide per_t_02_2

hide dam_p2_02_6
show dam_p2_02_6 at left
show dee_p_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0181
Dee "「あと少しで九つ目のフープだったのにっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もうすぐフープを抜けるという位置にあった赤いボールは、遠く弾き飛ばされてしまっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターのボールもまた最初の位置よりも大分遠くに飛んでいるが、それでも自分からぶつかっているだけまだマシだ。"

hide dam_p2_02_6

hide dee_p_02_3
show dee_p_02_3 at left
show per_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0396
Peter "「ふ、これもゲームのルールです。\n
そして、僕はもう一回打てるんです」"

play sound se_0220
hide dee_p_02_3

hide per_t_03_2
show per_t_03_2 at left
show dam_p2_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0182
Dam "「ずるいよ、大人ってこれだから……」"

hide per_t_03_2
show per_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0397
Peter "「これもルールです。\n
ね、[firstname]、僕達はルールに沿って正しくゲームをしていますよね？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「まあ、進行はルールに従っているけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（いくらなんでもあれは飛ばしすぎじゃないの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤いボールは庭の隅のほうへと転がってしまっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（この槌にしてもかなり重いのに、どうやったらあれだけ遠くに飛ばせるんだか……）"

hide per_t_02_8
show per_t_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice pet_f0398
Peter "「さあ、[firstname]。\n
あなたの番ですよ」"

hide per_t_01_2
show per_t_02_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice pet_f0399
Peter "「打たれたボールのプレイヤーは順番もスキップされますからね」"

hide dam_p2_02_9
show dam_p2_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
Dam "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ダ、ダム？」"

hide dam_p2_02_13
show dam_p2_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice dad_f0183
Dam "「大丈夫だよ、お姉さん。\n
僕、今は子供……じゃなくて、大人だもん」"

hide dam_p2_02_1
show dam_p2_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice dad_f0184
Dam "「ウサギの大人げない仕打ちだって、笑って流せるよ。\n
はははは」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T "（笑い方が引きつっているわよ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「そ、それじゃあ……」"

play sound se_0220
hide per_t_02_1

hide dam_p2_02_4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私のボールは順調に転がり、１０番目のフープの傍にまでつける。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（今のところ、私が一番進んでいるのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飛ばされたダムのボールは別として、ディーとペーターのボールはほぼ同じような位置にある。"


show dam_p2_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0185
Dam "「……兄弟」"

hide dam_p2_02_9
show dam_p2_02_9 at left
show dee_p_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0186
Dee "「分かっているよ、兄弟。\n
僕達はいい子だからね、ちゃんとルールは守るよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "短い会話。\n
だが、その中に何かが含まれていることに私は気付く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（嫌な予感がする）"

hide dee_p_02_1
show dee_p_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
Dee "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ディーは静かにボールとフープの位置を確認すると、斧を振り上げ。"

play sound se_0672
play sound se_0220
$ flash(.1)
play sound se_0703
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "地面を転がるはずのボールは一気に打ち上げられ、ペーターに向かう。"


show per_t_01_15 at center
hide dam_p2_02_9
hide dee_p_02_12
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0400
Peter "「見え透いた手ですね」"

play sound se_0309
pause .5
play sound se_0225
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分に向かってきたボールを手にしていた槌で叩き落としたペーターは、冷ややかに笑っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、ボールを打ったディーも彼がむざむざ当たるとは思っていなかったのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "残念そうな顔を見せずに、平然と言い返した。"

hide per_t_01_15
show per_t_01_15 at left
show dee_p_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0187
Dee "「ああ、つい手が滑っちゃった。\n
うちのひよこと違って、白っぽいから埃かと思って気になったんだ」"

hide per_t_01_15
show per_t_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0401
Peter "「……ええ、そうですね。\n
子供のささやかな悪戯ですからね」"

hide per_t_02_2

hide dee_p_02_2
show dee_p_02_2 at left
show dam_p2_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0189
Dam "「違うよ、悪戯じゃなくて、事故だよ、事故。\n
当たらなかったんだから、不幸な事故とはいえないけどね」"

hide dam_p2_02_4
show dam_p2_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam "「…………」"

hide dam_p2_02_12
show dam_p2_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0190
Dam "「当たれば、面白かったけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見え透いた挑発だ。\n
だが最初に大人げないことをしたのは、ペーターのほう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（状況を悪化させないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そういう意味を込めて彼を見たのだが、白いウサギはなんでもないように返してくる。"

hide dee_p_02_2

hide dam_p2_02_8
show dam_p2_02_8 at left
show per_t_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0402
Peter "「心配はいりませんよ、[firstname]。\n
僕は頭のいいウサギですからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「ペーター」"

hide dam_p2_02_8

hide per_t_03_1

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「そうよね、あなたは賢いウサ」"

play sound se_0220
pause .5
play sound se_0703
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「…………」"

play sound se_0309
pause .5
play sound se_0225
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言葉じりに重なるように、ペーターが打ったボールが二人のほうへ向かっていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らも当たる気はないので、簡単に打ち落とされた。"


show dee_p_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0191
Dee "「危ないなあ、僕達だったからいいけど、鈍くさい動物だったら当たっていたかもしれないよ」"

hide dee_p_02_13
show dee_p_02_13 at left
show per_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0403
Peter "「ああ、すみません。\n
つい集中しすぎたせいで、勢いが余ってしまって」"

play sound se_0126
hide per_t_02_3
show per_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0404
Peter "「僕もまだまだですね。\n
狙った場所になかなか当たらない、もとい、ボールを置けないなんて」"

hide per_t_02_11
show per_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0405
Peter "「次は、今よりももっと狙いを絞らないと」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターが手にしているものが銃ではないだけで、今にも一悶着ありそうな空気が漂っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「……あんた達、これはゲームなのよ。\n
ゲーム」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「分かっている？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を置いて殺伐とした空気に包まれる三人に、無駄と知りつつ忠告してみる。"

hide per_t_03_2
show per_t_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0406
Peter "「ええ、勿論！\n
僕はあなたに従順なウサギですから」"

hide dee_p_02_13
show dee_p_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0192
Dee "「僕達だって、お姉さんを困らせたりしないよ」"

hide per_t_02_5

hide dee_p_02_4
show dee_p_02_4 at left
show dam_p2_02_10 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0193
Dam "「うん。\n
ただ、ちょっと頑張りすぎて……」"

hide dam_p2_02_10
show dam_p2_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0194
Dam "「手が滑ることはあるかもしれないけどね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_9")
T "「…………」"

hide dee_p_02_4

hide dam_p2_02_5

$ hi_mes()

scene bg_gen_sky_spr_day
with dis

play music castle_garden_p_ali
play sound se_0220
pause .2
play sound se_0703
pause .3
play sound se_0309
$ flash(.1)
play sound se_0225
pause .2
play sound se_0220
$ flash(.1)
play sound se_0703
pause .2
play sound se_0309
pause .5
play sound se_0225
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ああ、ぼこぼこ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボールに、あるいは斧や槌によって抉られた地面は、あちこちが見るも無惨に穴だらけだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「～～～～～～～～！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0195
Dee "「この、～～～～～～ウサギ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam "「～～～～～！！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "既に順番に構わず、打ちたいようにボールという名の凶器を撃ち合う彼らを無視して、私は狙いをつける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「……よっと」"

play sound se_0220
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ころころ。"

play sound se_0178
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「よし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボールが杭に当たったことを確認する。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「……三人とも、いい加減にしなさい！」"


scene hn_spr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一度深呼吸して声を上げると、三人はようやく私のほうを向く。"


show dam_p2_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0196
Dam "「あれ……？どうしたの、お姉さん？\n
先刻まで、ゴールよりも大分遠かったよね？」"

hide dam_p2_02_10
show dam_p2_02_10 at left
show dee_p_02_7 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0197
Dee "「うん、まだ着きそうもなかったのに」"


show per_t_02_13 at center
hide dam_p2_02_10
hide dee_p_02_7
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0407
Peter "「さすがです、[firstname]！\n
あなたの華麗な勝利を僕は信じていましたとも！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……嘘をつくな、嘘を）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先刻まで殺気混じりにボールを打ち合っていたウサギに言われても、信憑性は限りなくゼロだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「あんた達が途中で放棄したから、ゲームは私の勝ちよ。\n
文句はないでしょう！」"

hide per_t_02_13
show per_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice pet_f0408
Peter "「ええ、勿論です。\n
あなたは絶対の勝者です！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「だったら、私の言うことを聞くわよね？」"

hide per_t_03_11
show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice pet_f0409
Peter "「はい！」"


show dee_p_02_8 at center
hide per_t_02_5
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
Dee "「？」"

hide dee_p_02_8
show dee_p_02_8 at left
show dam_p2_02_12 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
Dam "「？？？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターは二つ返事で頷いたが、双子は顔を見合わせて不思議そうな顔をしている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（それもそうか。\n
大体ペーターは、ゲームなんてなくても、こんな調子だしね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今回のゲームに対して、特に報酬を決めていたわけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、この世界の住人達に言うことを聞かせるのなら、多少強引でも、言い切るが勝ちだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「ペーターは、今すぐ仕事に戻ること！\n
ここで遊んでいた間に溜まった仕事が終わる前に、私に会いに来たら怒るからねっ」"


show per_t_03_3 at center
hide dee_p_02_8

hide dam_p2_02_12
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice pet_f0410
Peter "「え……、えええ！？\n
そんな、い、今すぐですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「当たり前でしょう。\n
ほら、さっさと帰る！」"

hide per_t_03_3
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice pet_f0411
Peter "「いや、でも……。\n
あなたがいるのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子のことも気にかかるらしく、ペーターはちらちらと視線を動かす。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「私の言うことが聞けないなら、もう二度とハートの城に遊びに来ないわよ」"

hide per_t_02_6
show per_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
Peter "「！！」"

hide per_t_01_3
show per_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice pet_f0412
Peter "「行きます、今すぐ行ってきますから！」"

play sound se_0703
hide per_t_01_5

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "槌を放り出して、名残惜しそうにしながらも、ペーターが去っていった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（これであっちはよし）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（残りは……、こっちね。\n
ディーはともかく、今のダムだと手が届かないから）"


show dee_p_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice dad_f0198
Dee "「お姉さん？」"

hide dee_p_02_11
show dee_p_02_11 at left
show dam_p2_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice dad_f0199
Dam "「どうしたの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「二人とも、そこに座りなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "地面を指差して厳命すると、二人は不思議そうな顔をしながら大人しく座り、私を見上げてくる。"

play sound se_0016
hide dam_p2_02_11

hide dee_p_02_11


scene bg_gen_sky_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その頬を、片方ずつぎゅっと抓った。"

$ flash(.1)
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0200
Dee "「～～～～っ！！\n
いひゃ、いひゃいよ、おへえさんっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0201
Dam "「！！？\n
いひなり、はにするの！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「他所様の庭をこんなに荒らして！\n
限度っていうものがあるでしょう、限度がっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice dad_f0202
Dee "「ぼ、ぼくひゃちだけじゃないよっ。\n
お城のウサギだって……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice dad_f0203
Dam "「ほ、ほうだよっ。\n
あー、痛かった」"

play sound se_0267

scene hn_spr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お得意の嘘泣きではなく、本当に涙ぐんでいる双子を見下ろしながら、私は静かに指を立てた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「……反省が足りないようね？」"

play sound se_0142
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手で抓ろうとする仕草を見せる。"


show dee_p_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dee "「！！」"

hide dee_p_02_6
show dee_p_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0204
Dee "「した、したからっ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「それじゃあ、仲よく片付けてもらいましょうか」"

hide dee_p_02_7
show dee_p_02_7 at left
show dam_p2_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice dad_f0205
Dam "「……片付けるって、ここを？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「他にどこがあるっていうのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "芝はめくれて茶色い土がはみ出ている。\n
いずれ綺麗になる世界とはいえ、このまま放置しておくのは忍びない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「負けた以上はあなた達にもちゃんと罰がないとね。\n
というわけで、ここを片付けるまでは一緒に帰ってあげないから」"

hide dee_p_02_7
show dee_p_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_8")
voice dad_f0206
Dee "「……え？\n
お姉さん？」"

hide dam_p2_02_13
show dam_p2_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_8")
voice dad_f0207
Dam "「僕達と、帰ってくれるの！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（気付かないと思ったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "耳聡いというべきか、それだけ私の言葉に集中していてくれたおかげというべきか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人は一気に目を輝かせると、立ち上がった。"

hide dee_p_02_11
show dee_p_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0208
Dee "「まずは芝を直して、あと、あのフープももういらないから、さっさと抜いちゃおう、兄弟。\n
帰れば、いよいよ本番だよ」"

hide dam_p2_02_9
show dam_p2_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0209
Dam "「うん、綺麗に片付けて、さっさと屋敷に帰らなくちゃ。\n
もう準備はほとんど終わっているんだからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……本番？\n
準備？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "耳慣れぬ単語に首を傾げていると、二人は慌てて首を振った。"

play sound se_0632
hide dee_p_02_4
show dee_p_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0210
Dee "「屋敷に帰ったら教えてあげる」"

hide dam_p2_02_4
show dam_p2_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0211
Dam "「とってもいいことだから、楽しみにしていてね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "早口に言い切って、二人は早速芝の手直しに入る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらちらと私を見る様子は、帽子屋屋敷を出たときにはなかった期待の色が浮かんでいるように見えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（一体何のことかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "訝しく思いながらも、教えてくれる気でいるのならここで追及しなくてもいいだろう。"

hide dee_p_02_7
show dee_p_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0213
Dee "「あ、そうだ、兄弟。\n
後でちゃんとツアーの記念品を回収しにいくのを忘れないようにしないと」"

hide dam_p2_02_1
show dam_p2_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0214
Dam "「勿論だよ、兄弟。\n
あれだけ高いお金を払ったんだから、もらえるものはしっかりもらわないと」"

play sound se_0632
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「……さてと」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（二人が芝を直している間に、私は道具でも片付けていようかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結果はさておき、このゲームのおかげで三人が大人しくなってくれたことは事実だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "片付けるぐらいしても罰は当たらないだろう。"

hide dee_p_02_7

hide dam_p2_02_2

$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0490

play music castle_garden_p_ali

show dee_p_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0215
Dee "「片付け終わったよ、お姉さん！」"

hide dee_p_02_4
show dee_p_02_4 at left
show dam_p2_02_10 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0216
Dam "「これで元通りでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「そうね……。\n
よく出来ました」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "労うように声をかけると、二人は同時ににっこりと笑った。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（……大きさは違うけど、こうして笑うとやっぱり同じ顔よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段は同じサイズの二人。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "（成功しているかどうかは別として）通りすがりを装うためとはいえ、こうして別々の姿でいるところを見るのは、何だか不思議な気分だ。"

menu:
    "ディー、大人にならない？":
        jump fushigi_dad3_6a
    "ダム、子供に戻ってくれる？":
        jump fushigi_dad3_6b

label fushigi_dad3_6a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ねえ、ディー。\n
あなたも大人の姿にならない？」"

hide dee_p_02_4
show dee_p_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice dad_f0217
Dee "「うん、別にいいよ。\n
お姉さん、大人のほうが好き？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「好きとか嫌いじゃなくて……。\n
落ち着かないんだもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "未だに色や髪型や服といった違いがなければ、彼らを見分けることは出来ない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それを情けないと思っていたのに、はっきりと違いが分かる今は今で、違和感がある。"

play sound se_0600
hide dee_p_02_10
show dee_p2_02_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0219
Dee "「どう……？これでいい？\n
このほうが、お姉さんは好きになってくれる？」"

hide dam_p2_02_10
show dam_p2_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0220
Dam "「ずるいよ、兄弟。\n
自分だけアピールするなんて」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ディーが大人に変わって、今度こそ、完全に同じ顔が並ぶ。\n
浮かべる表情や喋り方、服が違うから見分けられる二人。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「うん。\n
やっぱり、あなた達は同じ格好でいてくれるほうが私も安心できるわ」"

hide dee_p2_02_5
show dee_p2_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice dad_f0221
Dee "「じゃあ、この姿で一緒に帰ろう」"

hide dam_p2_02_11
show dam_p2_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice dad_f0222
Dam "「そうだね。\n
お姉さんが安心できるほうが、僕らも嬉しい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぎゅっと今にも手を繋いで帰ろうとする二人に挟まれて、歩き始めたときだ。"


show per_t_01_5 at center
hide dee_p2_02_4
hide dam_p2_02_5
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0413
Peter "「[firstname]！\n
え、もう帰ってしまうんですか！？」"

play sound se_0484
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後から全力疾走で走ってくるペーターの姿が見えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（もう仕事が終わったの？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（それとも、たまたま仕事の量が少なかったとか？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "色々想像が膨らむが、それよりも彼の背後にいる兵士のほうが気になった。"

hide per_t_01_5
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0414
Peter "「もう少しここにいてください。\n
今度は、その子供達がいなくても、ゲームが出来るように兵士を連れてきましたからっ」"

hide per_t_02_6
show per_t_02_6 at left
show heisi_t_02_08 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0032
Soldier "「ホワイト卿の至急の命令ということでしたが……」"

hide per_t_02_6

hide heisi_t_02_08
show heisi_t_02_08 at left
show heisi_t_01_05 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0025
Soldier "「こういうことでしたか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "合点がいったというような兵士と、彼らを先導するペーターが近付いてくる。\n
しかし、双子のほうが今度は早い。"


show dee_p2_02_2 at center
hide heisi_t_02_08

hide heisi_t_01_05
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0223
Dee "「もう貸してやらないよ、お姉さんは僕達のなんだからっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ディー？\n
！！？」"

play sound se_0051
camera at hpunch
camera at vpunch

play music cheerful_a_ali
show t_twi3_6a onlayer master
with dis
hide dee_p2_02_2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言うが早いか、私はディーに抱き上げられてしまった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0224
Dam "「ずるいよ、兄弟！\n
自分だけお姉さんをお姫様抱っこなんて……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0225
Dee "「兄弟、今は喧嘩をしている場合じゃないよ。\n
交互に抱っこしていこう、城を出たら今度は兄弟の番だ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0226
Dam "「ちえ……、仕方ないか」"

play sound se_0620
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "走り出す。\n
抱きかかえられて、振動が私の身体も揺らしていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice pet_f0415
Peter "「逃がしませんよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice dad_f0227
Dee "「お生憎様、僕達、追いかけっこは得意なんだ。\n
お城のウサギになんか捕まらないよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice dad_f0228
Dam "「ばいばい、お城のウサギさん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人にとって、ハートの城での追いかけっこなどいつもの遊びにすぎない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（でも……。\n
何だか、変な感じ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お姫様抱っこなんて私の柄ではないのに。\n
全身を揺らす振動に一緒に巻き込まれていることが、何だか嬉しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（……仲間外れにされていない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（連れていってくれる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飛び出したときに感じていた疎外感が揺れながら、落ちていくようだった。"

hide t_twi3_6a

$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_long
##endmemory
jump fushigi_end_check_hatter1_d
label fushigi_dad3_6b:

show dam_p2_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0229
Dam "「子供の姿？\n
うん、いいよ」"

play sound se_0466
hide dam_p2_02_4
show dam_p_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0232
Dam "「ふふ、お姉さん、子供のほうが好きなんだね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「子供好きっていうわけじゃないけど……。\n
あなた達って、やっぱり同じ姿でいてくれたほうがいいわ」"


show dee_p_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0233
Dee "「そうだね、区別なんて出来ないほうがお姉さんは僕らを同じに扱ってくれるし。\n
僕らとしても、そのほうが嬉しいよね、兄弟」"

hide dam_p_02_10
show dam_p_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0234
Dam "「うん。\n
兄弟のほうがいいなんて言われたら、僕哀しくて斧振り回して本気で喧嘩しなくちゃいけないから」"

hide dam_p_02_8
show dam_p_02_10 at center
hide dee_p_02_10
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0235
Dam "「お姉さんが優しいから、僕らはいい子でいられる」"

hide dam_p_02_10
show dam_p_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice dad_f0236
Dam "「ありがとう」"

hide dam_p_02_4


show t_twi3_6b onlayer master
with dis

play music dream_tsuduki_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「ダ、ダム……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "急に頬にキスをされて、驚く。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0237
Dee "「あー、ずるいよ、兄弟。\n
僕もお姉さんにキスしたいっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0238
Dam "「今は僕がキスをする番なんだから、兄弟はもう少し待っていてよ。\n
譲り合いって大事なんだから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま何度かダムは私の頬に顔を寄せて、唇で触れてくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（な、なんだか……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（こういう触られ方って久しぶりすぎて、緊張する）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むずがゆい気さえするのに、抵抗できなくなってしまう。"

hide t_twi3_6b


play music castle_garden_p_ali

show per_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0413
Peter "「[firstname]！\n
え、もう帰ってしまうんですか！？」"

play sound se_0484
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後から全力疾走で走ってくるペーターの姿が見えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（もう仕事が終わったの？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（それとも、たまたま仕事の量が少なかったとか？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "色々想像が膨らむが、それよりも彼の背後にいる兵士のほうが気になった。"

hide per_t_01_5
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0414
Peter "「もう少しいてください。\n
今度は、その子供達がいなくても、ゲームが出来るように兵士を連れてきましたからっ」"

hide per_t_02_6


show heisi_t_02_08 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0032
Soldier "「ホワイト卿の至急の命令ということでしたが……」"

hide heisi_t_02_08
show heisi_t_02_08 at left
show heisi_t_01_05 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0025
Soldier "「こういうことでしたか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "納得した様子なのがまた、いたたまれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（周りに迷惑をかけるなってあれほど言っておいたのに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（これだから、ストーカーウサギは）"

hide heisi_t_02_08

hide heisi_t_01_05


show dam_p_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice dad_f0239
Dam "「嫌だよ、お城のウサギとやり合ったってボーナスも出ないし、疲れるだけだもん」"

show dam_p_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice dad_f0240
Dam "「くたびれもうけなんて、ただ働きよりも嫌いだ。\n
行こう、お姉さん！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「あ……！」"

play sound se_0620
hide dam_p_02_9


show t_twi3_7b onlayer master
with dis

play music cheerful_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ダムが手を引いて走り出す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その様子を見ていたディーが横から手を出そうとするが、ダムがその間に割り込んできて邪魔をしている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0241
Dee "「兄弟、自分ばっかりずるいじゃないか。\n
お姉さんの手は二本あるんだから、半分ずつって決めただろう！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0242
Dam "「うん、だから今は僕が独り占めして、あとで兄弟と交替しよう。\n
今回は距離で半分こだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0243
Dee "「うーん……。\n
仕方ないな、今回だけだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0415
Peter "「逃がしませんよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "響く銃声に思わず身を竦めていると、ディーが少し後ろに下がる。"

hide t_twi3_7b
show t_twi3_8b onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0244
Dee "「邪魔しないでよっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0245
Dam "「さすが兄弟。\n
助かるよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私よりも少し小さい身体に引っ張られるように走っていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（でも、加減してくれている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子が本気で走れば、私にはとても追いつけない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "置いて行かれるのが目に見えている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが私が走っていられる速度で二人が併走しているということは、合わせてくれているということ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人にとって、ハートの城での追いかけっこなどいつもの遊びにすぎない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_12")
T "（だけど……。\n
何だか、変な感じ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を繋がれて、嬉しくなってしまうなんて私の柄ではないのに。\n
息を乱しながら一緒に巻き込まれていることが、何だか落ち着く。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（……仲間外れにされていない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_1")
T "（連れていってくれる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飛び出したときに感じていた疎外感が高まる鼓動に解けて、消えていく。"

hide t_twi3_8b

$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_long
##endmemory
label fushigi_end_check_hatter1_d:
if renpy.seen_label("fushigi_end_blood_rose1") == True:
    jump fushigi_end_check_hatter2_d
if renpy.seen_label("fushigi_end_elliot1") == True:
    jump fushigi_end_check_hatter2_d
if renpy.seen_label("fushigi_end_dad1") == True:
    jump fushigi_end_check_hatter2_d
else:
    jump fushigi_end_dad1
label fushigi_end_check_hatter2_d:
if fushigi_common3_castle2_deedam2a_seen == True:
    jump fushigi_end_dad1
else:
    jump fushigi_end_hatter1
