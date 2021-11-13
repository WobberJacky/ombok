label fushigi_ace_start:
hide screen castle_man_choice

scene map_bg_spring_day with dis

scene charasel_bg_castle_day
with dis
label fushigi_ace1:
$ clockanim()

$ hi_mes()

scene hm_spr_01
with dis

play music castle_corridor_p_ali

scene hr_01 with Dissolve(1.2)

show siro_t_02_02 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hei_f0009
Maid "「エース様ですか？\n
先ほど、ご自分の部屋に戻るとおっしゃっていましたが……」"

hide siro_t_02_02
show siro_t_02_08 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hei_f0010
Maid "「今となっては、城のどちらにいらっしゃるか……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「……ごめん、答えにくいことを聞いたわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースを捜して城内をうろうろとしていたのだが、質問を受けた彼女もちょっと困ったような雰囲気だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はとにかく迷う。\n
住み慣れた城内だろうと関係ない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼にとっては、自分の部屋に戻るという行為さえ、一つの冒険なのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（部屋に戻ろうとしていたってことは、今も移動中かもしれないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しばらく城をあけるのだから、一言ぐらい断っておこうと思ったのだが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一所に留まっていてくれるのならともかく、動き続ける迷子を捜し出すのは、かなり難儀だ。"

hide siro_t_02_08
show siro_t_02_07 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0011
Maid "「申し訳ありません。\n
お役に立てなくて……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「気にしないで。\n
あなただって……、例の水騒動で大変だったでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの傍に付いていた彼女も、泥まみれだったはずだ。\n
今はもう身支度を調えているが、他の仕事も押しているだろう。"

hide siro_t_02_07
show siro_t_02_01 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0012
Maid "「いいえ、私など……。\n
お探しのエース様に早くお会い出来るといいですね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何でもないように笑って、そっと会釈を返してくれる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女は女王の抱えるメイドの中でも、その私室にまで入ることを許されているメイドだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "癇癪を起こしたビバルディに呼ばれていたのだろう。\n
そのまま早足に女王の部屋のほうへと歩いて行った。"

hide siro_t_02_01

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「……さてと、エースが捕まらないなら仕方ないかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼のことだから、部屋に戻ろうとして城の外に出てしまっている可能性もある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普通ならあり得ないことだろうが、すべては{size=+20}エースだから{/size}という理由で、納得できる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（いいんだか、悪いんだか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慣れてしまった。\n
あの滅茶苦茶な騎士に振り回されることにも、一緒にいることにも……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、せめてしばらく出かけるのであれば、一言断ってからと思ったのだが……、思ったとおりにはいかないものらしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「いつもこんな調子だものね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（それにエースのことだから、出先にひょっこりと顔を出すかもしれない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むしろその可能性のほうが高いのかもしれない。\n
そう思って、私は城の門へと足を向けた。"

play sound se_0774
$ hi_mes()


scene hr_01 with Dissolve(.8)

scene charasel_bg_castle_day
with stripe_l_medium

scene hn_spr_01
with stripe_l_long

play music castle_garden_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城は薔薇の庭によって包まれている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迷路のように道が組まれたそこを歩いていく。\n
最初の頃は迷いかねなかったこの道も、今では慣れたもの。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（もっとも、エースにとっては迷う場所らしいけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼と同列に並べられては堪ったものではない。\n
そんなことを思っていたときだ。"

play sound se_0440
pause .4
play sound se_0644
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "耳障りな音に、思わず足が止まった。"

play sound se_0748

show ace_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0071
Ace "「ふう、やっと抜けられたぜ。\n
あれ、[firstname]！」"

hide ace_t_02_2
show ace_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0072
Ace "「ははは、こんなところで会うなんて奇遇だなあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "真っ赤な服を着た、真っ赤な騎士が、真っ赤な薔薇を斬って笑っている。\n
どうやら私の横に広がっていた薔薇の繁みを斬って現れたようだが……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「……ビバルディにばれたら、怒られるわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薔薇の手入れを怠ったという理由で兵を斬首にする女王様だ。\n
大した理由もなく薔薇を斬ったと言われれば、当然、反応は読める。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（手入れだって楽じゃないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この際、エースが神出鬼没なのは諦める。\n
しかし薔薇を斬られてしまうと、先ほどの騒動の原因にもなった水撒きを思い出して、私の顔も思わず曇った。"

hide ace_t_02_10
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0073
Ace "「えー、だって薔薇に突っ込んだら俺だって痛いんだぜ？\n
立ちはだかる障害を越えてこそ、旅は楽しめるものだしな」"

hide ace_t_03_11
show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0074
Ace "「はははは」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「……はいはい、分かったわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（今更反省するような人でもなかったわよね、あんたは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、このタイミングで彼に会えたのは私にとってもラッキーといえる。\n
何しろ、彼ほど会いたいときに会える保証がない人間はいないのだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ちょうどいいわ、話があるの、エース」"

hide ace_t_02_4
show ace_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Ace "「[firstname]？」"

hide ace_t_03_2
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice ace_f0075
Ace "「なになに、君の秘密の話？\n
それはちょっと興味があるな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い騎士は、何を言われるのかとどこか楽しげに笑っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、私がこれから言うことは内緒話でも何でもない。\n
だから、あっさりと言った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「私、しばらく城を離れようと思うの」"

hide ace_t_01_10
show ace_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0076
Ace "「へえ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「だから、その……。\n
しばらく、いなくなるから」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（いなくなるから……何？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言いながら、自分の声に力が入らない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（何を期待したんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "行くなと引き留めてもらいたかった？\n
それとも、見送ってほしかったのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分でも、何を求めていたのかがよく分からない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉が続かない私を見下ろしていたエースは、何故か納得したような顔で、手を打った。"

hide ace_t_01_3
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0077
Ace "「そうか、[firstname]、出掛けちゃうのか。\n
君も、旅に出るんだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「は？」"

hide ace_t_03_10
show ace_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0078
Ace "「君も、とうとうアウトドアの魅力に目覚めたんだろ？\n
いいことじゃないか、旅は色々なものを教えてくれる最高の環境だ」"

hide ace_t_02_1
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0079
Ace "「さあ、一緒に壮大な旅に出ようぜ」"

play sound se_0051
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "{size=+20}「違うわよ！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "肩を抱かれ宣言されると、落ち込みかけた自分が馬鹿らしくなってきた。"

hide ace_t_03_3
show ace_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0080
Ace "「ははは、照れることなんかないぜ？\n
騎士たる俺が、ばっちりとエスコートして……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「あんたの場合は、旅と言うよりも{size=+20}遭難に近いアウトドアでしょうがっ{/size}」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「私はそういうのじゃなくて……、城の外に反省に行ってくるって言っているのよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慌てて訂正を入れると、エースは不思議そうに首を傾げる。\n
何でそんなことを言い出したのか理解出来ないという顔だった。"

hide ace_t_01_4
show ace_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0081
Ace "「君が……、反省？\n
確かに君はいつもうじうじしていて、後ろ向きだけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（悪かったわね）"

hide ace_t_03_9
show ace_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
voice ace_f0082
Ace "「でも、君がわざわざ外で反省するようなことって……。\n
そんな大きな失敗があったら、俺も知っていそうなものだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……しでかしたでしょう、失敗」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（あなたと一緒に）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後の言葉はのどの奥に押し込んで、代わりに上目遣いで見上げると、エースはやっと気付いたらしい。"

hide ace_t_03_7
show ace_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0083
Ace "「あ、ひょっとして、先刻の陛下とペーターさん達のこと？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「そうよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この口振りでは、彼はまったくその可能性に気付いていなかったのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ますます意外そうに目を瞬きさせている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_16")
T "（まあ、エースにとっては失敗の範疇には入らないのかもしれないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "上司や同僚相手に平気で斬りかかり、銃を向けられる相手に言っても、無駄だったかもしれない。"

hide ace_t_01_3
show ace_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0084
Ace "「君が落ち込む必要なんてないじゃないか、[firstname]。\n
そもそも、あんな水の近くでお茶会をしようとした陛下に問題があると思うぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「……ビバルディがお茶会をしたかったのなら、邪魔するのはメイドとして悪いことよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰にでも愛される余所者。\n
その立場のおかげで、私は彼女に首を刎ねられることもなく、こうして立っていられる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だからこそ、過度に甘えるようなことはしたくない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「ちゃんとけじめは付けないと」"

hide ace_t_03_7
show ace_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
Ace "「…………」"

hide ace_t_02_13
show ace_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice ace_f0085
Ace "「君が出ていくなら、俺も一緒に行くよ。\n
女の子にだけ責任を押し付けるなんて、騎士の風上にも置けないだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「……駄目よ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の手を引いて歩き出そうとしたエースを振り払って、私は言う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「いい、エース。\n
私は悪いことをしたと思うから、反省しに行くの」"

hide ace_t_03_10
show ace_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice ace_f0086
Ace "「ああ、分かっているよ。\n
だから……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「あなたにとって、旅は罰にならないでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きっぱりというと、彼は手を引くのを止めた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り返って私を見た顔は、少し驚いているように見える。"

hide ace_t_01_10
show ace_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（自覚はしているのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースにとっては、城の中に留まることのほうが、罰としては有効だろう。\n
この城にいたいと思う私がここを離れようとするのと同じように。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自らの役を厭っている彼にとって、城に留められる以上の罰はない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「少しの間よ。\n
ビバルディやペーターにも反省してくるって言付けてあるから」"

hide ace_t_01_11
show ace_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0087
Ace "「だけど……、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "珍しく何か言葉を探しているらしい彼に、私は最後に告げた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「私が直接出かけることを伝えたのは、あなただけよ。\n
エース」"

hide ace_t_03_7
show ace_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Ace "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「だから、少し、頭を冷やしに行かせてよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悪いことをした。\n
彼にとっては大したことではないだろうが、私はきちんと責任をとりたいのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（我が侭で、自己満足な話だけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お客さんでいないために。\n
この城の一員として生活を続けていくために、失敗には相応の罰を。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「……行ってきます」"

play sound se_0624
hide ace_t_02_8

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じゃあねという言葉の代わりに手を振って、歩き出す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後からは戸惑うような気配を感じた気がしたが、振り返ったら、決心が鈍りそうだった。"

$ routechara = "Ace"
$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium
##endmemory

play music map_spring_jok

scene bg_gen_sky_spr_day
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「さて、どこに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に住む友人は何人もいるが、しばらく滞在させてもらうことを考えると……。"

scene map_gen_bg with fade
$ show_mes("frame_gen_togaki")
T "Where do I want to visit?"
$ hi_mes()
show screen fushigi_map1
$ ui.interact()
