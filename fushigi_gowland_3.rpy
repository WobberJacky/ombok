jump fushigi_common3_tower
label fushigi_gowland3_1:

scene map_bg_winter_day
with stripe_l_medium

scene charasel_bg_tower_day
with stripe_l_medium

scene ts_01
with stripe_l_long

play music tower_room2_p_ali
play sound se_0479

show yuri_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Julius "「…………」"

play sound se_0691 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものように、ユリウスは時計の修理をしている。"

hide yuri_t_01_9

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、塔に居候してからこの部屋に入り浸り続けている私は私で、渡された知恵の輪と格闘をしていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「……ああ、もう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（こうまでうまくいかないと、かえってストレスが溜まるわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "知恵の輪というゲームは、思考過程と解けたときの達成感を楽しむもの。\n
難題であればあるほど、開放感も高まるものなのだが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ちっとも解けやしない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の手元にあるのは、あの三つの輪っかが絡み合った知恵の輪。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少し歪んでいるその形を利用して外せるのだろうという予測は立っているのに、どう角度を変えても、外れる気配がない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「これをこうして……」"

play sound se_0691 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「で、こっちをこう……？」"

play sound se_0691 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

play sound se_0691 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

play sound se_0691 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（私、そんなに不器用じゃないつもりだったんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "がちゃがちゃと音が生まれるばかりで、輪は絡まったままだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここまでやって解けないとなると、いよいよ本格的に不器用の称号を受け取らなければならないだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（情けなさすぎる……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "偶然外れてくれないかと、ぐるぐる回してみても、解けてくれない。"


show yuri_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0111
Julius "「…………。\n
そんなに苛々と試していたら、解けるものも解けないだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はいつものように手元だけを見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私のほうに一瞥も向けた様子もなかったが、これだけ続く金属音はさすがに無視できなかったのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、うるさい雑音を追い出すという雰囲気ではなかった。\n
彼の性格から考えて、本当に迷惑だったら文字通り追い出すところだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……アドバイス？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つまり、言葉の足りない彼からの、貴重な助言と考えるのが筋だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慣れない人には分かりにくいが、そのあたりは今までの付き合いで何となく察する。"

hide yuri_t_01_9
show yuri_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0112
Julius "「どこかの夢魔じゃないんだ。\n
普段のおまえになら、充分解けるレベルのパズルだぞ」"

hide yuri_t_01_12
show yuri_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0113
Julius "「少し気を落ち着けてみろ。\n
苛立ったままでは、何も進まない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

hide yuri_t_03_10


scene bg_gen_sky_win_day
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（そうは言われてもね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭の中をよぎっているのは、この前の遊園地でのゴーランドの姿。\n
考えないようにしているつもりでも、つい考えてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（あんなの、変だもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、服だけを見れば、いつもの彼の服のほうがずっと変だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "馬の飾りが付いた黄色いジャケット。\n
サイズの合っていないバイオリンに、垂れた三つ編み。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰が見ても、遊園地のオーナーその人だと分かる服。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "アトラクションと同じぐらいに、奇をてらっているとしか思えない、主張の強い衣装を着たゴーランド。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（そうよ、いつもの格好で出てきてくれればよかったのに）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "髪は短く、さっぱりとした顔。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（無精髭は、男の魅力なんでしょう。\n
勝手に剃らないでよ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（三つ編みも落とさないで。\n
服だって、全然……、似合っていない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本当は違う。\n
私の目から見ても、非の打ち所のない、格好いいと言える格好だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの奇妙な装いが嘘のような……、大人の男性の姿。\n
なのに、全然、ゴーランドらしくない。"


scene ts_01
with dis


$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「……あんなの、嫌よ」"


show yuri_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「あんなの、私の知っているゴーランドじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼がこの世界の有力者の一人であることは間違いない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私に見せる顔、見せない顔、その違いを見せないように使い分けていることも、知っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（見せないでくれていてよかったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見せてくれて嬉しいと思うよりも、あんな姿のゴーランドを見たくなかったという気持ちのほうが強い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（我侭だなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隠されている間は、好奇心も手伝って覗きたいと思ったことも何度かあったのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見たくなかったと思った途端に、掌を返すなんて……。\n
聞き分けの出来ない、子供みたいだ。"

hide yuri_t_02_4
show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「あ……。\n
ちょ、ちょっとユリウス、何するのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "前回同様私の持っていたパズルを手にしたユリウスは、くるくると回した後に、ぽいと自分の作業台の上に投げてしまった。"

hide yuri_t_03_9
show yuri_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0114
Julius "「今のおまえには、こっちのほうがよさそうだ」"

hide yuri_t_01_1

play sound se_0212

scene t_cut_go3_1u
with dis

play music cheerful_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「？\n
……！！？」"


scene t_cut_go3_1
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「…………。\n
何、これ？」"


show yuri_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_16")
voice jul_f0115
Julius "「見ての通り、知恵の輪だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "{size=+20}「あれとは明らかにサイズが違うじゃない！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（形だけはオーソドックスな知恵の輪だけど……。\n
何、何なの、このサイズは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "握りの部分ときたら、私の指よりも太い。\n
そして、当然のように……、重い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地での仕事でも重いものを持って運んだことがあるが、これはその中でもトップクラスに近い。"

hide yuri_t_03_2
show yuri_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0116
Julius "「あれよりは簡単だろう。\n
今のおまえにはこれぐらいでちょうどいい」"

hide yuri_t_01_13
show yuri_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0117
Julius "「それが解けなければ、他のどんな簡単なやつも解けはしないだろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言いたいことだけ言い終えると、ユリウスは再び机に戻り、仕事を再開した。"

play sound se_0161
pause .5
play sound se_0479
hide yuri_t_01_4

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（確かに、これって一番定番なのは間違いないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "文字通り、捻って、そして噛み合わせるだけ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは答えてくれそうにないので、私は目の前に置かれた知恵の輪に取り掛かる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「よっ……。\n
ん？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（あれ、上手く抜けない）"

play sound se_0691
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "音を立てながら何度か金具を合わせてみるが、うまくいかない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（なんで？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先刻まで使っていたタイプは初めて手にするものだったが、この手の知恵の輪なら、それこそ家で何個も解いたことがある（大きさは普通のものだったが）。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "出来ないはずがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思うのに、いくら捻っても、角度を変えてみても……、耳障りな音が生まれるばかりだ。"

$ hi_mes()

$ time_effect()

play music tower_room1_p_ali
play sound se_0691
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_11")
T "「……どうして解けないの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（こんな単純なパズルが解けないはずがないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすがにずっと握り締めていると、腕も疲れてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もはやパズルというよりも金属の塊にしか見えなくなっているそれを横に放って、大きく息をついた。"


show yuri_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0118
Julius "「解こうとしているからだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「……は？」"

hide yuri_t_03_4
show yuri_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jul_f0119
Julius "「絡まったものを無理矢理解こうとすれば、無理が生じるのは当たり前だ。\n
意地になれば意地になるほど、絡まって複雑になる」"

hide yuri_t_01_13
show yuri_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jul_f0120
Julius "「おまえの性格からすれば、予想通りだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（つまり、解けないのが分かっていてよこしたわけ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だとすればずいぶん意地悪な話だが、ユリウスが何の意図もなくそんなことをするとは思えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何か考えがあってのことだと思うが……。\n
その理由が私には分からない。"

hide yuri_t_03_10
show yuri_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0121
Julius "「これもそうだが、単に力任せでも外れたりしない。\n
解くには、それなりのコツがいる」"

play sound se_0463
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この前のときと同じように、ユリウスは難なく三つの輪を二つと一つに分かれさせてしまう。\n
そして、また同じように元に戻す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手品師のような動きだ。"

hide yuri_t_02_10
show yuri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0122
Julius "「言っただろう、仕事の息抜きで使っているんだ。\n
余計に頭を悩ましていたら息抜きにならない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「うーん……」"


play music quiet_night_a_ali

show t_go3_1 onlayer master
with dis
hide yuri_t_02_11

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（何も考えずにやってみろってことかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが考えずに解くというのは、私の性格からはとても難しい。\n
根暗で、いつまでも悩む性格だということは、ユリウスも知っているだろうに。"

play sound se_0691
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "再び大きな金具を手にとって、何度か動かしてみる。\n
ガチャガチャという耳障りな音。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞き慣れたくはない音だが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（うるさいなあ）"

play sound se_0691
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "素直にそう思いながら、適当に手を動かした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（やっぱりそう簡単にいかな……、え？）"

play sound se_0463
hide t_go3_1
show t_go3_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「な、なんで？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何気なく指を動かすと、今まで何をしても外れなかったことが嘘のように、呆気なく解ける。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "信じられない思いで二つに分かれた金属を呆然と見ていると、静かな声がかかった。"



hide t_go3_2


play music tower_room1_p_ali

show yuri_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0123
Julius "「おまえも知っているだろう、これほど簡単な知恵の輪はない。\n
外れなかったのは、輪のせいではなくて、おまえに原因がある」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "原因。\n
この場合にユリウスが言う原因なんて、一つしか思い浮かばない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……そりゃあ、ずっともやもやしていたけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（今は……、こっちに気持ちが集中していたせいで、苛つくどころじゃなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目の前にある輪のことしか考えていなかった。\n
今までずっと、気になっていたはずなのに。"

hide yuri_t_02_10
show yuri_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0124
Julius "「絡まった以上、無理矢理解けばこじれるだけだからな。\n
何事にも、頃合いというものがある」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（……そんなこと、私だって知っているわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、言葉で説明されても、素直に頷けただろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（私のことだもの、かえって反発するだけよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "素直になれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言ってしまえば、たった一言。\n
伝えるのに一呼吸ですむ言葉さえ、こじれた気持ちは蓋をされて、表に出ることは出来ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（ユリウスらしいわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "意図が通じないかもしれない、そう思えるほどの遠回しな優しさ。\n
だが、けして突き放すようなことはせず、一定の位置から見ていてくれた。"

hide yuri_t_03_10
show yuri_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0125
Julius "「さて……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "眼鏡の奥から、暗いのに温かい目が私を映す。"

play sound se_0161
hide yuri_t_03_4
show yuri_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0126
Julius "「また仕事だ。\n
今回も、あの騒がしい場所だが……」"

hide yuri_t_01_11
show yuri_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0127
Julius "「おまえはどうする？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "イスから立ち上がったユリウスに、私は解けた知恵の輪を机に置く。\n
そうして、外へ向かう背中に、ついていくことにした。"

hide yuri_t_01_7

$ hi_mes()

scene ts_01 with Dissolve(.8)

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium

scene map_bg_summer_day with Dissolve(1)

scene yum_sum_01_1
with stripe_l_medium

scene bg_gen_sky_sum_day
with stripe_l_medium

play music amuse_inside_p_ali
play sound se_0557
play sound se_0755
$ hi_mes()
$ show_mes("frame_gen_chara")
voice mat_f0014
Child "「すごい、すごーいっ！\n
次はあれに乗ろうよ、あれ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice nos_f0000
Child "「ジェットコースターの次に乗るなら、あっちのほうがいいわっ。\n
早く行きましょうよ！」"

play sound se_0465

scene yun_sum_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元気な声を上げながら、私達の横を子供達が走り去っていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（この時間帯も大繁盛みたいね）"


show yuri_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Julius "「…………」"

hide yuri_t_03_13
show yuri_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice jul_f0128
Julius "「相変わらず、騒々しい。\n
仕事でなければ、来たくない場所だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「そうでもないわよ。\n
住めば都ってどこかの諺でもいうでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（私も最初は苦手だったけど……。\n
今は、ほっとする気もする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの仕事部屋の静寂も心地いいが、この賑やかさだって捨てたものじゃない。"

hide yuri_t_02_8
show yuri_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0129
Julius "「……こうとも言うな。\n
朱に交われば、赤くなる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（仲直りさせたいのか、喧嘩を続行させたいのか、どっちなのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、ユリウスの顔を見ている限りでは、単にからかっているだけなのだろう。\n
彼は性格が悪い悪いと言いながらも、大元の部分は口で言うほどひねていない。"

play sound se_0051

show bor_t_02_6 at center
hide yuri_t_03_1
with dis

play music boris_t_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0174
Boris "「[firstname]！お帰り！！\n
あんまり帰ってこないから、そろそろ痺れをきらせて迎えに行こうかと思ってたんだぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ボリス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひょこっとどこからともなく姿を現したボリスは、すぐさま身体を寄せてくる。"

hide bor_t_02_6
show bor_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0175
Boris "「おっさんが『おまえが行くと、かえって怒らせるから行くな』なんて失礼なこと言うしさ」"

hide bor_t_01_3
show bor_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0176
Boris "「酷くない？\n
俺もあんたがいなくて、つまらなかったのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "拗ねたように口を尖らせ、後ろから抱きついてくるボリスを、緩やかに引き剥がす。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ねえボリス、ゴーランドがどこにいるのか分かるかしら？\n
先刻から探しているんだけど見かけなくて……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「家にもいないみたいだし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスはゴーランドに時計を渡しに来たのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "約束の時間帯は間違っていないはずだが、大きな屋敷をノックして出てきたのは、留守を任されていた従業員が一人だけだった。"

hide bor_t_03_13
show bor_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0177
Boris "「おっさん？\n
今の時間帯なら、園内をうろうろしているはずだけど……」"

hide bor_t_01_10
show bor_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0178
Boris "「あ、そういえば、俺もこの時間帯、見かけていないな。\n
どこをほっつき歩いているんだか……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「またお客さんが来ている、とか……。\n
そんなこと、ないわよね？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（この前にも来ていたんだもの、今回もなんてことそうそうあって）"

hide bor_t_03_12
show bor_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice bor_f0179
Boris "「あのおっさんに、客～？\n
少なくとも、俺は見ていないけど……」"

hide bor_t_01_3
show bor_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice bor_f0180
Boris "「どうせその辺をうろうろ巡回でもしているんじゃないかな。\n
足腰弱くしないためにも、動いたほうがいい年だし」"

hide bor_t_02_2
show bor_t_02_2 at left
show yuri_t_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice jul_f0130
Julius "「この時間帯に来ることは予め伝えていたんだが……、約束していた意味がないな。\n
長引くようなら、一度塔に戻るか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの意見ももっともだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地は広い。\n
この敷地からたった一人を捜し出すのは、大仕事だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "領主であるゴーランドが私を見つけるのとはわけが違う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「……私はもうちょっとだけ、探してみる。\n
ユリウスは仕事があるのなら先に戻っていても」"

hide yuri_t_03_4
show yuri_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_14")
Julius "「…………」"

hide yuri_t_02_10
show yuri_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_14")
voice jul_f0131
Julius "「いや、こんな荷物を持って何度もここに来る気にはなれん。\n
どうせなら、一回で片付けていく」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "てっきり「分かった」と二つ返事で頷くと思っていた彼の言葉に、思わず止まってしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「……一緒に探してくれるの？」"

hide yuri_t_03_13
show yuri_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice jul_f0132
Julius "「…………。\n
仕事なんだ、仕方ないだろう」"

hide yuri_t_01_13
show yuri_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice jul_f0133
Julius "「何をぼうっとしている？\n
ゴーランドを探すんだろう、早くしないと時間帯が変わるぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「あ、うん！\n
今行くわっ……、ボリス、ありがとう」"

play sound se_0417
hide yuri_t_01_11

hide bor_t_02_2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "くるりと背を向けて園内へ歩き出すユリウスの後を追う。\n
塔に戻るなんて言っていたのに、彼は相変わらずお人よしな面があるようだ。"


show bor_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0181
Boris "「ふうん。\n
時計屋さん、本当に……、面倒見がいいよね」"

hide bor_t_01_10

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music amuse_inside_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……どこにいるのかしら」"


show yuri_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0134
Julius "「さあな。\n
ここは無駄に広いから、あの目立つオーナーを捜すだけでもことだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人混みを掻き分けながら進むものの、一向にゴーランドの姿は見えない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（お客さん、多いわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地は大賑わいだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "老若男女を問わず……、それどころか種族さえ関係なく、ここには色々な客が訪れる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "真っ赤なお城でも、綺麗な塔でも、マフィアのお屋敷でも、こんなことはあり得ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（来るものは拒まない、それも遊園地のルールなのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の滞在地では見られない光景。\n
ここだから、私もずっといたいと思ったのに。"

hide yuri_t_01_4
show yuri_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

hide yuri_t_03_8
show yuri_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ユリウス？\n
どうしたの？」"

play sound se_0313
camera at hpunch
camera at vpunch

show black onlayer master with grad_t_short
hide yuri_t_03_3


play music truth_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "急に立ち止まったユリウスを振り返ろうとしたら、背後から目隠しをされた。\n
突然のことに、呆気にとられながら聞いてみる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0135
Julius "「な、なんでもない……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「なんでもないって、そんなはずがないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ボリスやディーやダム達ならまだしも）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これが他の人間がすることなら悪戯だと私も思うだろうが、相手はユリウスだ。\n
彼が何の意味もなく、こんな行動を取るはずがない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「ちょ、ちょっと、これじゃ何も見えないわ。\n
危ないから離してちょうだい」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice jul_f0136
Julius "「……心配するな、転んでもここはただの地面だ。\n
ぶつけたところで、怪我はしない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "{size=+20}「そういう問題じゃないわよ！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「離してっ」"

play sound se_0007
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り払うように手を動かすが、しっかりと抑え込んだ手のひらは簡単には外れてくれない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「ユリウス！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（理由も言わないなんて、どういうつもりなの）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見えない視界。\n
突然、ユリウスの手が外れぬまま、私を引き摺り出した。"

play sound se_0365 volume .1
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jul_f0137
Julius "「[firstname]、いいから、今は大人しく……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「こんなのあなたらしくないわよ、ユリウス！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "靴が擦れる感覚に抵抗するように力を入れると、ユリウスの手の力が一瞬弱くなった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（今だっ）"

play sound se_0051
camera at hpunch
camera at vpunch
hide black with grad_b

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屈み込むようにして、彼の手を振り払い、正面に向き直って。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目の前に映った光景に、思考が停止した。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（あれって、ゴーランド？）"


play music secret_a_ali

show t_go3_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "建物の影、そこに重なり合うゴーランドと相手の姿があった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いかにも親密そうに身体を密着させる姿から、その関係を推し量ることなんて、簡単なことだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで視界を塞いでいた人など、私の目にもう映らない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（誰？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（その人は、誰？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視線を逸らしたいのに、凍りついたように身体が動きを止めている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（誰……、なのよ、その人）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭ががんがんする。\n
目の前の風景がぐるぐる回って、気持ち悪い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（ゴーランド）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアではないのだ。\n
心の声なんて、届くはずもないのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "肉声はのどに張り付いたまま、苦さだけを染み込ませるように、私の身体でぐるぐると回り続ける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「…………！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（……嫌）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドが、私以外に。\n
私以外が、ゴーランドに……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（触らないで）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言ってしまえば、楽になれるのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（勝手に出ていった私に、そんなことを言う資格なんてないのに）"

hide t_go3_3

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足ががたがた震えていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逃げ出したい。\n
今すぐこの場から消えてしまいたい。"


show yuri_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「[firstname]……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスが困惑したように私の名前を呼んでいることに気付いたが、その声さえ聞きたくなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（馬鹿みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は気遣ってくれていたのに。\n
自分で台無しにしてしまった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（自業自得だわ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「ごめん。\n
ちょっと……、頭を冷やしてくる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「ユリウスは、先に、戻っていていいから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうにかその言葉を振り絞るのが、限界だった。"

hide yuri_t_02_3

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「……[firstname]？」"

play sound se_0417
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "早足にその場を去っていく私を、背後から誰かが呼んだような気がしたが、振り返りはしなかった。"

$ hi_mes()


$ time_effect()

play music quiet_night_a_ali
show bg_gen_sky_sum_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベンチに座って、動いていく雲を見つめる。\n
遊園地の雑踏も、まったく耳に入らない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（自惚れていたのよね、結局）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔にいれば、いや、どこだって構わなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界のどこかにいれば、いつかゴーランドが迎えに来てくれると私はどこかで期待していたのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（迎えにこない理由、もう少し考えればよかったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "迎えにこない。\n
迎えに行けないのではなく、行かない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉の違いは小さいが、その差は絶対的で、けして超えられない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（背中しか見えなかったけど、綺麗な人だったわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らがいた場所は人目を忍ぶにはもってこいの、薄暗い路地。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "女性の姿は私の位置からはっきりとは見えなかったが、身に付けたドレスは充分に確認できた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きっとゴーランドに似合うような、大人の女性だろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（そうよね、私一人に絞ることなんて、ないもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドの本来の役は、「侯爵」、貴族の代名詞のようなものだ。\n
付き合いのある女性の一人や二人がいたところで、おかしくない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「……これも、振られたっていうのかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "喧嘩別れして、心変わり。\n
なんて、陳腐なシナリオだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（でも、私にはお似合いよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒って飛び出して、恋人の心変わりに苛立って。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（姉さんみたいには、なれないもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦い記憶が、胸を過ぎった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0138
Julius "「食え」"

hide bg_gen_sky_sum_day
show t_go3_4 onlayer master
with dis

play music heartrending_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視界に入ってきたものに首を傾げると、いつも珈琲のカップを出してくれる手が、クレープを差し出してくれていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事部屋から出ること自体を嫌うユリウスが、まだここにいたことに驚く。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（先に帰ったと思っていたのに）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jul_f0139
Julius "「おまえの好みなど分からんから、適当に買ってきた。\n
文句を言わずにとっとと食べろ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「……ん、ありがとう」"

hide t_go3_4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一口囓ると、ラズベリーの風味が口の中に広がってくる。\n
甘くて、酸っぱい。"


show yuri_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0140
Julius "「おまえ……、顔色が真っ青だぞ。\n
夢魔にも負けない酷い顔色だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「うん、そうかも……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何かを紛らわすように、クレープをぱくつく。\n
それほど大きくないものだから、すぐに食べ終わってしまった。"

play sound se_0471
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "くしゃっと紙を握って、ゴミ箱に放る。\n
無言でいる私に、ユリウスは溜息をついた。"

hide yuri_t_01_10
show yuri_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0141
Julius "「まったく、いつもの私の仕事を邪魔するだけの図々しさはどうした……？\n
あれは……」"

hide yuri_t_03_4

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「[firstname]！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "響いた大きな声に、思わず身体が竦む。\n
誰かなど、確認するまでもないのに……、視線が追い掛けてしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「ゴーランド」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（また、あの格好だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ち着いた印象を与えるスーツ。\n
髭も三つ編みもない、さっぱりとした顔。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（さっぱりしすぎて、全然……、ゴーランドらしくない）"


show go_n_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_5")
voice gor_f0251
Gowland "「おい、大丈夫か、[firstname]。\n
あんたが青い顔して去って行くのが見えたから……」"

hide go_n_03_2
show go_n_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_5")
voice gor_f0252
Gowland "「って、おい、どうして泣いて……。\n
時計屋、おまえ、何したんだよ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "涙腺が緩くなっているのだろうか、彼の姿を見るなり、私は顔を歪ませて俯いてしまった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな私を見て、ゴーランドは近くにいたユリウスに問いただしてくる。"

hide go_n_03_5
show go_n_03_5 at left
show yuri_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0142
Julius "「……こいつが泣いているとしたら、その原因はおまえだ。\n
濡れ衣を着せる気か？」"

hide go_n_03_5
show go_n_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0253
Gowland "「はあ？\n
俺が原因って……、[firstname]、何か気に入らないこと……」"

play sound se_0785 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_3")
T "（また、あの匂い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を伸ばされて感じる、甘ったるい、バニラの香り。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（嫌だ……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（こんなの、ゴーランドじゃないわ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「何でもないわよ。\n
それに……、あの人は、いいの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の性格の悪さも、自虐趣味も大したものだと思う。\n
自分が傷つくと分かっているのに、聞いてしまうのだから。"

hide go_n_03_3
show go_n_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0254
Gowland "「はあ……、あの人って、誰だよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しらを切るつもりなのか、首を傾げるゴーランドを見て、不覚にも涙が出そうになる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（いつのまに、こんなに……、依存していたんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大丈夫だとずっと思っていた。\n
誰でも受け入れてくれる遊園地、そのオーナーであるゴーランド。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（ゴーランドが私じゃない人を見るのがこんなに嫌だなんて。\n
思っていなかった）"

hide yuri_t_02_7
show yuri_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice jul_f0143
Julius "「……物陰でこそこそといちゃついていたくせに、何を言う。\n
その上、何だ、その甘ったるい香りは」"

hide go_n_03_10
show go_n_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice gor_f0255
Gowland "「物陰で……って、え、おい、まさか。\n
あれ、見ていたのかよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "がっくりと頭を抱えたゴーランドは、しばらくそのまま唸っていたが、一息に顔を上げた。\n
そこに。"


show lady_5 at right
hide yuri_t_03_13
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0019
Woman "「ゴーランド侯爵様、どうされました？\n
急に走り出されるから、びっくりしました」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（あの人は、先刻ゴーランドとくっついていた……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後から現れた女は、ゴーランドの横に立つと、自然な仕草でその腕を伸ばした。"

play sound se_0313
hide lady_5
show lady_5 at right
hide go_n_03_3
show go_n_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0256
Gowland "「だから、あんたもしつこいな。\n
俺には、ちゃんと好きな女がいるんだって言っただろう」"

hide lady_5
show lady_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0020
Woman "「そんなこと……。\n
私は、これほどあなたをお慕いしていますのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "絡みつく腕を振り払いながら、渋い顔でゴーランドが言う。\n
鼻を突くのは、濃厚なバニラの香り。"

play sound se_0785
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（この匂い、嫌い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "バニラアイスは遊園地の定番商品。\n
だが、しばらくは食べられそうもない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「私達、邪魔みたいだし……、帰るわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベンチから立ち上がり、ユリウスの腕を掴んで逃げるように歩き出すと、肩を掴まれた。"

play sound se_0492
hide go_n_03_1
show go_n_03_6 at center
hide lady_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0257
Gowland "「待ってくれよ、あんた……、どこに帰るんだ？\n
まだ俺のこと、許せないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（許せないんじゃないわ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_3")
T "（本当は、怖いだけ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突き付けられて、結果を得てしまえばそれまで。\n
終わるのはどんなことも一瞬だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（決定打を与えるなら、早くしてよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも自分から決定的な言葉は告げられない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この気持ちを抱えたままでい続けることも辛いのに。\n
自分では終わりを招くだけの力もない。"

hide go_n_03_6
show go_n_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0258
Gowland "「……答えてもくれないのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（嫌われたわよね）"

hide go_n_03_1
show go_n_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice gor_f0259
Gowland "「分かった。\n
もう二度と、会わない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドがはっきり告げた言葉に、肩が震えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（本当に、嫌われた）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_5")
T "（もう、顔も見たくないほど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦しい。\n
息が止まってしまいそうな程、胸が痛い。"

hide go_n_03_11
show go_n_03_11 at left
show lady_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0021
Woman "「え？\n
ど、どういうことですか、侯爵様？」"

hide go_n_03_11
show go_n_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0260
Gowland "「あんたとは、もう二度と会わないっていうことだ。元々、取引のあるところからの紹介だったから、失礼のないようにしていたつもりだったが」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（……え？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、話は私を無視して進んでいく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不思議に思って、別れの言葉の矛先を確かめるように振り返る。\n
そこには、見慣れないのに、よく知っている緑の眼があった。"

hide go_n_03_1
show go_n_03_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0261
Gowland "「事情が変わった。\n
あんたには悪いが、遊園地には二度と来ないでくれ」"

play sound se_0051
camera at hpunch
camera at vpunch

show t_go3_5 onlayer master
with dis
hide lady_5

hide go_n_03_5


play music transparent1_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ゴ、ゴーランド！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスと繋いでいた手が引き離されて、ゴーランドに抱き寄せられる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いまだに鼻を擽るバニラの香り。\n
だが急接近した顔のほうが、今は目に入る。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0262
Gowland "「最初に言うべきだったな。\n
俺が惚れているのは、この子だけだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0263
Gowland "「どんなに口説かれても、意味がねえんだ。\n
何しろ、ぞっこんなもんでな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_4")
T "（……ぞっこん？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（ゴーランドが……、私に、ぞっこん？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私にも、彼にもまるで似合わない言葉だ。\n
それでも、抱き寄せる腕に力がこもったのを感じて、何も言えなくなる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひねた言葉も、強情を張る気持ちも。\n
そんなたわいない一言に飲まれて、消えてしまった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0022
Woman "「ゴーランド侯爵様……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「…………」"

hide t_go3_5
show bg_gen_sky_sum_day onlayer master
with dis
play sound se_0118
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（うわ、すごい音）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice gor_f0264
Gowland "「いってえ……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice tad_f0023
Woman "「ええ、よく分かりましたわ。\n
あなたが、～～～～趣味の、～～～～～だってことは！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice tad_f0024
Woman "「ごきげんよう。\n
今後の取引は、よくよく考えさせて頂きます」"

play sound se_0098
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "淑女の顔を保ったまま、それでもゴーランドに張り手を閃かせた彼女は、颯爽と背を向けて歩いて行く。"


scene yun_sum_01 with dis
hide bg_gen_sky_sum_day


play music amuse_inside_p_ali


show go_n_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0265
Gowland "「いって。\n
ああ、本気で殴られるなんて久しぶりだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「それ……、結構腫れるわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然の展開にびっくりして、ぽかんとしながらも告げる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手形が残るとまでは言わないが、彼の頬にはくっきりと赤い痕跡が出来てしまっていた。"

hide go_n_03_10
show go_n_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0266
Gowland "「まあ、自分が蒔いた種だからな。\n
てめえで刈るさ」"

hide go_n_03_11
show go_n_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0267
Gowland "「……あんたも、殴るか？\n
だったら、逆のほうにしてくれると、さすがの俺も助かるんだが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（なんでそうなるのよ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここには鏡はないから分からないが、私はそれほど欲求不満な顔をしているのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「殴る理由なんてないでしょう」"

hide go_n_03_6
show go_n_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gor_f0268
Gowland "「殴られるだけの理由はあると思うんだがな。\n
誤解、させただろう？」"

hide go_n_03_1
show go_n_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gor_f0269
Gowland "「取引のあるところのお嬢さんでな、どうしても園内を案内してくれって言われたから、応じただけだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_9")
T "「……だったら、どうしてそんな格好をしていたのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地の案内ならば、いつものオーナーとしてのゴーランドでいいはずだ。\n
だというのに、どうしてそんな別人のような格好をする必要があったのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（まるで、恋人同士でデートしているみたいだった）"

hide go_n_03_5
show go_n_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gor_f0270
Gowland "「……それは、その、向こうの希望があったからなんだが。\n
なんだなんだその目は、別に後ろめたい理由なんてないぜっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「……そうよね、あんな綺麗な人に強請られたら悪い気はしないでしょうし」"

hide go_n_03_3
show go_n_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_16")
voice gor_f0271
Gowland "「拗ねるなって、悪かった、[firstname]。\n
あんたを不安がらせるつもりはなかったんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言うと、ゴーランドは赤くなった頬と逆の頬を差し出してきた。"

hide go_n_03_2
show go_n_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0272
Gowland "「だから、これはけじめだ。\n
あんたを怒らせたことも、頭に来させたことも……」"

hide go_n_03_11
show go_n_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0273
Gowland "「思いっきりぶつけてくれて構わないぜ」"
$ fushigi_gowland3_5a_seen = False
menu:
    "それじゃあ、遠慮なく。":
        jump fushigi_gowland3_5a
    "いいわよ。":
        jump fushigi_gowland3_5b
label fushigi_gowland3_5a:
$ fushigi_gowland3_5a_seen = True
pause .5
play sound se_0424
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（痛い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それほど力を入れていたつもりはなかったが、手のひらがじんと痺れた。"

hide go_n_03_5
show go_n_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0274
Gowland "「……やっぱり、あんたのほうがいてえな。\n
予想はしていたけどよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「そんなに馬鹿力じゃないわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "音だって、先ほどの彼女に比べればずっと小さかったはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（私だって、痛い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "痛いと感じているのは、手のひらではない、胸の中。"

hide go_n_03_10
show go_n_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0275
Gowland "「そうだな。\n
頬だけの話じゃなくて、あんたの顔が哀しそうだったから、俺も苦しかった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼もまた、私と同じ感覚だったのだろうか。"

hide go_n_03_2
show go_n_03_2 at left
show yuri_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0144
Julius "「……まったく、どうでもいい相手にまで愛嬌を振りまかなければいけないなんて、オーナーとは因果な商売だな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ずっと私達のやりとりを見ていたユリウスが、呆れたように口を挟んでくる。\n
手に持った仕事の品を押し付けるようにして、続けた。"

hide yuri_t_03_10
show yuri_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0145
Julius "「おまえ達が喧嘩をしようが、バイオレンスな趣味に目覚めようが、私には関係ない。\n
帰らせてもらうぞ、ゴーランド」"

hide go_n_03_2
show go_n_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0276
Gowland "「ああ、悪かったな、時計屋。\n
世話かけた」"

hide yuri_t_02_11
show yuri_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0146
Julius "「……ふん、そう思うなら、詫びの一つでも持って来い」"
jump fushigi_gowland3_6
label fushigi_gowland3_5b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「いいわよ。\n
それに……、最初に飛び出していったのは私のほうだもの」"

hide go_n_03_4
show go_n_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
Gowland "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ほっとしたように肩を落としたゴーランドの背後に、別の影が現れる。"

hide go_n_03_4


scene bg_gen_sky_sum_day
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0147
Julius "「そうか、なら代わりに私がしてやろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え？\n
！！！？」"

play sound se_0107
camera at hpunch
camera at vpunch
pause 1
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_10")
Gowland "{size=+20}「～～～～っ！！！？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ユ、ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（今、スパナ握り締めて殴らなかった？）"


scene yun_sum_01
with dis


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさか背後からユリウスに殴られるとは思っていなかったのだろう。\n
ゴーランドは蹲って、声も上げられずにいる。"

hide yuri_t_03_12
show yuri_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0148
Julius "「思い切りぶつけていいといったからな。\n
遠慮しないでやらせてもらった」"

hide yuri_t_03_1
show yuri_t_03_1 at left
show go_n_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0277
Gowland "「時計屋……、それはねえだろっ」"

hide yuri_t_03_1
show yuri_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0149
Julius "「黙れ。\n
おまえ達の痴話喧嘩に巻き込まれるのは、もうごめんだ」"

hide yuri_t_01_3
show yuri_t_03_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0150
Julius "「これに懲りたら、同じことの繰り返しにならないようにするんだな」"

jump fushigi_gowland3_6
label fushigi_gowland3_6:
hide yuri_t_03_12

hide go_n_03_10

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう告げて、今にも踵を返して立ち去ろうとする彼のほうへと近付く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ、ユリウス。\n
私も……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（ナイトメア達にまだ何も言ってないもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "居候中はユリウスの部屋に入り浸ってはいたが、間借りしていたのはクローバーの塔の一室だ。\n
彼らにまだ礼も言っていない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（勝手に綺麗になるといっても、そのままなんて失礼すぎる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、私の足を止めさせたのは、追いかけた相手本人だった。"


show yuri_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0151
Julius "「おまえの家は、ここだろう。\n
いつまでも他所でふらふらするんじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「……でも」"

hide yuri_t_02_10
show yuri_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice jul_f0152
Julius "「塔の連中は、放っておけばいい。\n
どうせ夢魔のことだ、だいたいの事情は察しているだろう」"

hide yuri_t_03_10
show yuri_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice jul_f0153
Julius "「やることがあるなら、それを優先しろ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（……知っていたの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの部屋でリングと格闘していた時間帯は確かに多かった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、それ以外の時間帯について、彼は一度も言及したことはなかったはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きっとユリウスは私が部屋にいない間、どこで何をしていたのか、知っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ありがとう、ユリウス。\n
今度は遊びに行くわね」"

hide yuri_t_01_11

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "去る背中に声をかけてからゴーランドを振り返ると、彼はとても渋い顔をしていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……ゴーランド？」"


show go_n_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0278
Gowland "「いや、なんつーか。\n
時計屋があんたに手を出すようなことはないと思っていたが……」"

hide go_n_03_1
show go_n_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0279
Gowland "「正直、面白くねえな。\n
こういうのは」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（先刻までの私みたいなことを言うのね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_4")
T "「あら、妬いてくれるの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "冗談交じりの口調で言えば、返ってきたのは、本心からだとわかる真剣な声。"

hide go_n_03_11
show go_n_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0280
Gowland "「そりゃあ……、妬くぜ。\n
俺はあんたにぞっこんだって言ったばっかりだろう？」"

play sound se_0051

show t_go3_6 onlayer master
with dis
hide go_n_03_12


play music happy_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引き寄せられて、唇が重なる。\n
ここが遊園地だということも忘れて、私はその背中に腕を回した。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「……んっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
Gowland "「…………っ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「………ふ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キスをしていても、無精髭がないから、くすぐったくない。\n
髪も短くそろえられている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（早く、普段のあなたに戻ってね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "無難な格好も似合っているし、格好いいとは思うが、私が好きになったのは、遊園地のオーナー。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも周りを楽しませようとしている相手なのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さく微笑むと、ゴーランドもつられたように表情を緩めた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0281
Gowland "「離さねえよ。\n
あんたは、俺の好きな女だからな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_8")
T "（私だって、同じぐらいにぞっこんだわ）"

$ hi_mes()
hide t_go3_6


scene yun_sum_01 with Dissolve(.8)

scene yum_sum_01_1
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_long

label fushigi_end_choice_gowland:
if fushigi_gowland3_5a_seen == True:
    jump fushigi_end_gowland_julius1
else:
    jump fushigi_end_check_amuse1_g
label fushigi_end_check_amuse1_g:

if renpy.seen_label("fushigi_end_gowland1") == True:
    jump fushigi_end_check_amuse2_g
if renpy.seen_label("fushigi_end_boris1") == True:
    jump fushigi_end_check_amuse2_g
if renpy.seen_label("fushigi_end_pierce2") == True:
    jump fushigi_end_check_amuse2_g
else:
    jump fushigi_end_gowland1
label fushigi_end_check_amuse2_g:
if fushigi_common3_tower2_gowland2a_seen == True:
    jump fushigi_end_amuse1
else:
    jump fushigi_end_gowland1
label fushigi_end_read_gowland_1:
if fushigi_common3_tower2_gowland2a_seen == False:
    jump fushigi_end_gowland1
