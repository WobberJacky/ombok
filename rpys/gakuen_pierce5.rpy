label gakuen_pierce5:
scene bg_map_day
with dis
$ clockanim()


scene bg25_rr_day
with dis

play music dining_day_p_wam

scene bg_par02_ct_amu_day with Dissolve(1.2)
play sound se_0229
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "翌朝のカフェテリアは、妙な熱気に包まれていた。\n
あちこちから、賑やかな声が聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……昨夜のは、なんだったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正直、夢なのではないかとも疑った。\n
夢なら夢で、あれが私の潜在願望なのかと思うと頭痛がしてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、机の上に置いてあったはずのリボンが姿を消していた。\n
どうやら、あれは夢ではなかったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「現実、か」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予備のリボンがあるので、身支度に困るようなことはなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（やっぱり、夢みたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……ネズミの大群を引き連れたピアスが、女子寮に押しかけて、私にキスをして、リボンを奪って去って行った。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_10")
T "（傍から聞いたら、かなり荒唐無稽よね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一晩が経ったというのに、未だ私には何がなんだかよく分かっていない。\n
ピアスがやってきたことも、イベント自体もだ。"


show amuse_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0074
Seito "「[firstname]！\n
ねえ、こっち空いているわよ！」"

hide amuse_a2_2
show amuse_a2_2 at left
show amuse_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0153
Seito "「こっちにいらっしゃいよ。\n
一緒に、朝食を食べない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼうっと考え込んでいるところで、声を掛けられた。\n
声の主を探す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_18")
T "（あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔見知りの女子生徒達だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じ寮の二人。\n
カフェテリアで会うことが多く、親しくなった友人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ありがとう、空いている席を探しているところだったの。\n
助かったわ」"

play sound se_0160
pause .5
play sound se_0034

show white onlayer master with Dissolve(1.5)
hide white

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "招かれるままに席につき、朝食を呼び出す。何を食べようかと考えるのも面倒なので、トーストに、サラダに、オレンジジュースといった、いつもの定番だ。"

hide amuse_a2_2
show amuse_a2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0075
Seito "「それで、昨夜はどうだった？\n
盛り上がった？」"

hide amuse_b1_3
show amuse_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0154
Seito "「あなたの部屋にも、もちろん誰か来たんでしょう？\n
誰が来たのか、教えてよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（昨夜？盛り上がる？\n
誰か来た……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わくわくとした調子で、隠す様子もない。\n
彼女に言われた内容に眉をひそめる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の部屋には昨夜ピアスが訪れた。\n
相手は明らかではないものの、まるで訪れを見越しているような言葉だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「誰って……。\n
なんで、そんなことをあなた達が知っているの？」"

hide amuse_a2_6
show amuse_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice tad_g0076
Seito "「なんでって、昨日がストームだったからよ。\n
……あなた、説明を聞かされなかったの？」"

hide amuse_b1_2
show amuse_b2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice sam_g0155
Seito "「ストーム直前まで、新入生女子には内緒にするのが伝統だけど……。\n
部屋に来た男子が、ちゃんと説明してくれたでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームという言葉に心当たりがあった。\n
ピアスが昨夜、伝統行事なのだとか言っていたはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（どうせ出鱈目に間違っているんだと思って、まともに聞いていなかったけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子生徒が女子生徒の部屋に訪れて、証拠を奪うイベントだなんて言っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスがまた訳の分からないことを言っていると聞き流してしまっていたわけなのだが……、どうやらかなり正解に近いものだったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「そうね……。\n
男子は来たし、説明もしようとはしていたわ」"

hide amuse_a2_5
show amuse_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice tad_g0077
Seito "「ああ、あなた、もしかして……。\n
男子生徒を追い払っちゃったの？」"

hide amuse_b2_1
show amuse_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice sam_g0156
Seito "「たまに、やっちゃう子いるのよね。\n
やっぱり女子寮に不意打ちで男子が来ると、受け入れられないっていうか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「いえ、私はちゃんと部屋に入れたわよ？\n
彼は、戦利品まで盗って行ったわ」"

hide amuse_a2_9
show amuse_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Seito "「……？」"

hide amuse_b2_5
show amuse_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Seito "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は訝しげに顔を見合わせる。\n
彼女達は友人として、私の性格をそれなりに把握している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからこそ、私が事情を把握もしていないのに男子生徒を部屋に入れるという状況が分からないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……私だって、相手がまともな男子生徒だったら入れたりしていないわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手がピアスだったから、訳の分からないままでも受け入れてしまえたのだ。\n
小さく息をついて、二人へと白状した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……私の部屋に来たの、ピアスだったの」"

hide amuse_a2_1
show amuse_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice tad_g0078
Seito "「それは……、なんというか……。\n
……無理ね」"

hide amuse_b1_9
show amuse_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice sam_g0157
Seito "「……ええ、無理ね。\n
説明なんて、ピアスには無理」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の端的な言葉から、大体どんなことが起こったのかを察してくれたようだ。\n
視線を彷徨わせ、それぞれ呟くように言う。"

hide amuse_a1_5
show amuse_a1_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0079
Seito "「災難だったわね……」"

hide amuse_b1_1
show amuse_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0158
Seito "「混乱したでしょう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そうね、混乱はしたけど。\n
災難ってほどじゃないわ」"

hide amuse_a1_9
show amuse_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tad_g0080
Seito "「ふふ、あなた、ピアスに懐かれているものね。\n
情が移っちゃった？」"

hide amuse_b1_5
show amuse_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice sam_g0159
Seito "「放課後もよく一緒にいるみたいだし……。\n
ふふ、あやしいわ～」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「…………」"

menu:
    "否定する。":
        jump gakuen_pierce5_2a
    "黙秘する。":
        jump gakuen_pierce5_2b
label gakuen_pierce5_2a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「違うわよ。\n
ただゴーランドに頼まれて、補習をしてあげているだけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……よく言うわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜あんなことをしておいて、よくもまあこうつらつらと否定できるものだ。\n
半ば自分に呆れてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら私は、自分で思っていたよりも面の皮が厚いらしい。"

hide amuse_a1_2
show amuse_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0081
Seito "「そうよねえ。\n
相手がピアスじゃあ、ないわよねえ」"

hide amuse_b2_3
show amuse_b2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0160
Seito "「……ないない。\n
さすがに、ピアス相手じゃねえ」"

jump gakuen_pierce5_3
label gakuen_pierce5_2b:
$ lovechara_pierce_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜あんなことがあった私としては、黙秘を通すしかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを、私が呆れ果てたからだと思ったのか。\n
二人はすぐに顔を見合わせると手をぱたぱたと揺らした。"

play sound se_0142
hide amuse_a1_5
show amuse_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0082
Seito "「ごめんごめん、ないわね。\n
あのピアスが相手じゃあね」"

hide amuse_b2_1
show amuse_b2_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0161
Seito "「ふふ、そうね。\n
ピアス相手じゃあ、浮いた話が出るわけもないわね」"

jump gakuen_pierce5_3
label gakuen_pierce5_3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……酷い言われようだ。"

hide amuse_a1_5
show amuse_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0083
Seito "「可愛いけど……、可愛すぎるっていうか……」"

hide amuse_b2_8
show amuse_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0162
Seito "「……あの子、そういうのって想像できないわよね。\n
色恋とか」"

hide amuse_a2_1
show amuse_a2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0084
Seito "「子供みたいだものね、雰囲気っていうか……」"

hide amuse_b1_5
show amuse_b2_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0163
Seito "「う～ん、そう？\n
子供っていうんじゃなくて……」"

hide amuse_b2_9
show amuse_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0164
Seito "「ああ、なんていうか……。\n
想像がつかないのよね、結局」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一般の女子生徒から、ピアスがどういう目で見られているのかがよく分かる。\n
恋愛対象という枠からは外れているのだろう。"

hide amuse_a2_6
show amuse_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0085
Seito "「でも、ピアスだと、いい雰囲気になるとか以前に、意味が分からなかったでしょう？」"

hide amuse_b1_5
show amuse_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0165
Seito "「うん。\n
まともな説明じゃなかったと思うし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「ええ、正直、今も分かっていないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「昨日のあれが、一体なんだったのか、教えてくれると助かる。\n
……どうして、男子が女子寮に侵入してくるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "サラダをつつきながら、話を向ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "概要は合っているかもしれないが、情報不足。\n
昨夜のピアスの説明では、何がなんだかよく分からないままだ。"

hide amuse_a2_3
show amuse_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0086
Seito "「昨日のあれはね、ストームって呼ばれる行事なのよ。\n
シンフォニア学生寮に伝わる伝統行事って感じかしら」"

hide amuse_b1_9
show amuse_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0166
Seito "「元々は公認じゃなくて、男子寮での肝試しみたいなものだったらしいわよ。\n
新入生男子を、女子寮に派遣するの」"

hide amuse_b1_8
show amuse_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0167
Seito "「新入生男子は、無茶を承知で女子寮攻略に挑むってわけね」"

hide amuse_b1_5
show amuse_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0167_5
Seito "「もちろん大多数は使用人によって防がれちゃうわけなんだけれど……、中には成功させる子もいたみたいね」"

hide amuse_a1_2
show amuse_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0087
Seito "「成功した証拠として、女子の持ち物を持ち帰ることの出来た新入生は、その年の英雄。\n
大盛り上がりしたってわけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……いかにも、寮にありそうな馬鹿騒ぎね」"

hide amuse_a1_3
show amuse_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice tad_g0088
Seito "「ええ。\n
それがずっと続いているうちに、いつのまにか伝統になったみたい」"

hide amuse_b1_1
show amuse_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice sam_g0168
Seito "「今はもう公認だから、昔ほど厳しいルールでもないのよ。\n
使用人達も、手加減してくれるから」"

hide amuse_a1_2
show amuse_a1_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice tad_g0089
Seito "「その代わり、新入生女子に事情を説明できるかで難易度を調整しているのよ」"

hide amuse_a1_8
show amuse_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice tad_g0089_5
Seito "「自分の力でストームの説明をして、説得して、部屋に入れてもらわないといけないという形でね」"

hide amuse_a1_3
show amuse_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice tad_g0090
Seito "「相手は新入生じゃなくてもいいんだけど、歓迎会も兼ねているから優先されるの。新入生の男子生徒にとっては、寮生活の洗礼ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……なるほど、納得したわ。\n
それで、私には説明してくれなかったのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨日の浮ついた空気や、そのときが来るまでは……と言っていたボリスやその他のクラスメイト達の反応の意味を理解した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人達が手加減した上に、女子生徒側も予め何が起こるか分かっていたとしたら、肝試しとしての意味合いは完全になくなってしまうだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ありがとう、ようやく合点がいったわ。\n
昨夜から、何がなんだか分からないままだったから」"

hide amuse_a1_2
show amuse_a1_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tad_g0091
Seito "「ふふ、さすがのあなたも、ピアスには甘いのね。普通なら、あなた、事情もよく分からない男子を部屋に入れたりはしないでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「甘いというか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……{size=+20}大量のネズミに、ドアを食い破られそうになったのよ{/size}」"

hide amuse_b2_3
show amuse_b2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice sam_g0169
Seito "{size=+20}「それは、私でも開けるわ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……開けざるをえないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しみじみとした彼女の声に頷く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（そういえば……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ねえ、昨日、それで戦利品を盗られたんだけど……。\n
あれって、戻ってこないのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予備があるとはいえ、毎日使うリボンが一本しかないというのは心細い。\n
出来ることなら、早めに返してもらいたい。"

hide amuse_a1_8
show amuse_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0092
Seito "「ああ、あなたブリーズのことも知らないのね？\n
ストームの約一週間後には、ブリーズというイベントがあるのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ブリーズ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば、ピアスがリボンを見つけた時にそんなことを言っていた気がする。"

hide amuse_b2_1
show amuse_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0170
Seito "「ストームの仕返しをするためのイベントなの。\n
ブリーズのほうは、女子が戦利品を奪い返すために男子寮に忍び込むのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……この学校、意外とイベント好きよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世界一の魔法学校だ。\n
世間一般にあるイメージでいうと、こんなイベントは認めそうにない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "優秀な学校というイメージばかりが先行しがちだが、実際にこうして中に入ってみると、意外性がかなりある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ブリーズ、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの一週間後ということは、あと六日後。\n
なんだか、少しずつわくわくとしてきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その後も、彼女達からストームやブリーズの話を聞きつつ、朝食を進めた。"

hide amuse_a2_4

hide amuse_b2_3
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg20_gd_day
with stripe_l_long

play music garden_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後。\n
いつもならばカフェテリアで勉強するが、今日は遊園地寮の中庭に出ていた。"


show pia_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0151
Pierce "「珍しいね、今日はお外なんだね？\n
今日はお勉強しないの？遊ぶの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「遊ばない遊ばない」"

hide pia_m_03_11
show pia_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice pie_g0152
Pierce "「え～、遊ばないの？\n
遊ぼうよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「遊びじゃなくて、真面目な話」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽかぽかと、夏に向け強くなり始めた日差しの下。\n
私達は、向かい合って立っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日は、ちょっとばかり、実験をしてみようと思っているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「あのね、ピアス。\n
あなた、お友達を呼ぶときって、どうやって呼んでいるの？」"

hide pia_m_01_13
show pia_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
Pierce "「？？？」"

hide pia_m_03_1
show pia_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pie_g0153
Pierce "「来てって思ったら、来てくれるよ！\n
皆、優しくて親切だからね！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「そう、そこよ！」"

hide pia_m_01_6
show pia_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice pie_g0154
Pierce "「そこ？\n
どこ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスの顔の付近ではぐるぐるとクエスチョンマークが飛び交っているように見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（思う、というところ。\n
そこで、ピアスは無意識に第二種召喚魔法を使っているはずなのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐっと、握り拳を作る。\n
ピアスには、召喚の才能がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呪文も魔法陣すらも使わずにあれだけ大量のネズミを一気に召喚し、それを使役するだけの能力があるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今はそれがネズミの形にしか反映されていないため、ピアスはネズミ使いとしか思われていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれどもし、ピアスがもっと自由に、ネズミ以外のものを呼べるようになったのならそれはすごいことだ。\n
能力そのものが、見直される。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "第二種召喚は、実際のモンスターと契約を交わす第一種召喚よりも簡単だと思われがちだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、第二種が自分の魔力に想像力で形を与えて操るという自己完結型の魔法だからなのだが……、規模が大きくなればなるほど、その力関係は逆転する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もともと形と意思ある他者と対話するよりも、ゼロから己の魔力と想像力だけを材料に、巨大な召喚対象を作り上げることのほうが難しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（でも、ピアスなら、かなりいいところまでいけるはずだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれだけ大量のネズミを一気に作り上げられるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同一種とはいえ、細かく分割した魔力の一つ一つに細部まで作りこまれた本物そっくりの形を与え、それを使役している。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「ねえ、別のお友達を呼ぶことは出来ないのかしら。\n
たとえばそうね……、猫とか」"

hide pia_m_02_9
show pia_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice pie_g0155
Pierce "「ぴ！！？\n
にゃんこなんて駄目だよ、にゃんこ怖いよ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ネズミより大きい生き物。\n
対比しやすいからと、猫と口にしてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当然ながら、ピアスは即座に反発した。\n
猫はネズミの天敵だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスとボリスの普段の様子からして、察するべきだった。"

hide pia_m_02_5
show pia_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0156
Pierce "「駄目だよ！\n
にゃんこなんて呼べないよ！呼ばないよ！」"

hide pia_m_01_3
show pia_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0157
Pierce "「君のお願いでも、にゃんこは駄目だよ、食べられちゃう！\n
怖いんだよ！？にゃんこ、怖いんだ！」"

play sound se_0055
hide pia_m_03_3
show pia_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0158
Pierce "「君、ネズミよりにゃんこのほうが好きなの……？\n
やだよ、にゃんこ好きなんて駄目だよ、君はネズミ好きじゃなきゃ駄目だよ！」"

play sound se_0016
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスはぎゅっと私の服の裾を掴むと、ぐいぐいと引っ張りながら懇願する。\n
本当に、猫が苦手なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（いくら猫がネズミを獲るとはいっても……、ピアスのサイズじゃ無理でしょうに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスは（何故か）ネズミ耳や、尻尾が生えているとはいえ、人サイズだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "常にどこかびくびくしたところがあるせいで、実際の身長よりも小柄に見えてしまいがちだが、それでも私より背が高い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなピアスを食べることの出来る猫ともなると、どこぞのピンク猫ぐらいしか思いつかない。\n
別にボリスを召喚しろとは言っていない。"

hide pia_m_01_4
show pia_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0159
Pierce "「俺、にゃんこ怖いけど……っ！\n
でも、君がネズミよりにゃんこのほうが好きだっていうなら、にゃんこにだって負けないよ！」"

hide pia_m_02_8
show pia_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0160
Pierce "「俺には仲間がたくさんいるからね！\n
１００対１くらいでだったら、にゃんこにも勝てるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……卑怯とかいう以前に、グロテスクな図を想像しちゃうから、よして」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こういうピアスの、汚れることを厭わない主義というのは強いと思う。\n
目的のためなら何をしてもいいという、やや外れた感のある思考がたまに怖い。"

hide pia_m_01_7
show pia_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0161
Pierce "「俺はネズミだからね！\n
卑怯なことでもしないと、勝てないんだよ！」"

hide pia_m_02_7
show pia_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0162
Pierce "「俺は君のことが好きだから、にゃんこにも勝つよ！\n
卑怯なことして、俺が怖くなくて、俺が確実に勝てる方法で、勝つよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "（どんな方法よ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下手に触れると、墓穴を掘ってしまいそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……私が好きだから、か）"

menu:
    "頑張って。":
        jump gakuen_pierce5_4a
    "やめて。":
        jump gakuen_pierce5_4b
label gakuen_pierce5_4a:
$ lovechara_pierce_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……そう、頑張ってね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "棒読みで応援する。\n
ストーム以来、ピアスはこうして私に対する好意を隠さない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "子供のようで純粋な好意。\n
だが、私は知っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスは子供ではない。\n
幼くとも、子供とは違う。"

jump gakuen_pierce5_5
label gakuen_pierce5_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「やめなさいよ。\n
……どう考えても、グロのほうにしか考えが向かないから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃ボリスにいじめられ、からかわれているピアスだから、どんな理由にしろそれに対抗しようという心意気は買いたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、卑怯で確実で自分は怖くない方法というのは何をするつもりなのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかもその理由が私ともなれば、実際のところ無関係なボリスとしても浮かばれないだろう。"

jump gakuen_pierce5_5
label gakuen_pierce5_5:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「え～と。\n
猫じゃなくていいから、何か別のものは呼べないの？」"

hide pia_m_01_12
show pia_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice pie_g0163
Pierce "「無理だよ。\n
だって俺、ネズミ以外に友達いないもん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にこっと無邪気な笑みで、とてつもなく物悲しいことを言ってくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人間の友達がいないことだとか、そういうことは彼にとっては些細なことなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……こういうところ、強いわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "強い、というか強かというべきなのか。\n
馬鹿な子と周囲から低く見られ、からかわれ、自分でも分かっているとおり、ネズミ以外の友達がいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな状況でも、彼は自分が不幸だとは思っていない。\n
彼は、彼の置かれている状況に、それなりに満足してしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲が彼を拒絶するのでなく、彼自身が周囲の価値観を拒否しているようにも見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「自己完結の魔法、ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自らの魔力に、自らのイメージで形を与えて使役する第二種召喚魔法は、ピアスに相応しいのかもしれなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（……でも、私は関わるわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その自己完結の世界に。\n
関わりをもったからには、途中で投げ出さない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ネズミ以外の、別の何かを呼んでみてよ。\n
ピアス、あなたはお友達を増やすべきだわ」"

hide pia_m_03_5
show pia_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pie_g0164
Pierce "「そんな必要ないよ。\n
俺にはネズミ達がいるもん、充分だよ！」"

hide pia_m_01_8
show pia_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pie_g0165
Pierce "「どうして、ネズミじゃ駄目なの？\n
君、ネズミ嫌いなの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ネズミ以外、と言う言葉に被害妄想を膨らませたピアスが泣き出しそうな目で私を見る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「違うわよ、ネズミが嫌いなわけじゃないわ。\n
でも……、ネズミ以外のお友達も見てみたいのよ」"

hide pia_m_01_13
show pia_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pie_g0166
Pierce "「ネズミだけで充分だよ。\n
俺には君もいるし、それで充分なんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……手強いわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしたらピアスを説得できるかと考える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "（……よし）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一番簡単な方法をとることにした。\n
子供や動物に一番有効な方法だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すなわち、ご褒美。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「分かったわ。\n
ネズミ以外のお友達を呼べるようになったら……、ちゅうしてあげる」"

hide pia_m_03_13
show pia_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
Pierce "{size=+20}「！！！」{/size} "

hide pia_m_03_3
show pia_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice pie_g0167
Pierce "「ちゅう！？\n
ちゅうって、ちゅう！？ちゅうなの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ、ちゅうよ、ちゅう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなに連呼していると、ネズミになった気分だ。"

hide pia_m_01_3
show pia_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0168
Pierce "「やるよ！俺、頑張るよ！！\n
そしたらちゅうしてくれるんだね！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「ええ、成功したらちゅうしてあげるわ」"

hide pia_m_01_6
show pia_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_2")
voice pie_g0169
Pierce "「やるよやるよ！成功させる！！それで、ちゅうする！\n
俺頑張るから、見ていてね！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「ええ、見ているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やる気に火のついたピアスを眺めながら内心苦笑する。\n
私は明確に、「キスしてあげる」とは言っていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ここまで純粋に喜ばれ、なおかつ期待されてしまうと……。\n
今更、ひっかけでしたなんて言い出せる雰囲気ではなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（私ってば、何を考えているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひっかけるつもりとはいえ、当たり前のようにご褒美がキスなんて言えた自分に驚く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスにとって私の唇にそれだけの価値があると、設定できてしまう。\n
そして、それがひっかけでなくても構わないと思っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、いつのまに絆されてしまっていたのだろう。\n
考えてみても、明確な答えが出てこないあたり、すでに……。"

hide pia_m_02_7
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg20_gd_eve
with stripe_l_long

play music garden_eve_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくら才能の片鱗がみられるとはいっても、ピアスはこれまでネズミしか召喚したことがない。やはり、急なイメージ転換には無理がある。"

play sound se_0346

show m_pia5_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目を瞑り、難しい顔をして念じるピアスの目の前に、黒毛のネズミがぽんっと姿を現す。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0170
Pierce "「ぴ！？\n
ああ、違うよ、違う……、そうじゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0171
Pierce "「ううう～、俺が呼んでいるのは君じゃないんだよ～。\n
ほら、戻って戻って」"

play sound se_0105
hide m_pia5_1
show m_pia5_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声に応じるように鳴く。\n
ネズミはピアスの影へと駆け込んで、そのまま見えなくなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれから毎日、いつもの補習に加えて召喚の練習をしているのだが、なかなかうまくいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イメージがうまく固まらないのか、ピアスが呼び出すのは毎回ネズミだ。\n
もしくは、何も出てきてくれないこともある。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0172
Pierce "「ねえ、[firstname]、やっぱり駄目なんだよ。\n
俺にはネズミしか友達いないし、出来ないんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0173
Pierce "「……駄目っこネズミだもん、俺。\n
ぴい……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そんなことないわ。\n
ほら、ご褒美ほしいんでしょう？」"

hide m_pia5_2
show m_pia5_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_g0174
Pierce "「うん！\n
俺、君にちゅうしてほしいよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_g0175
Pierce "「君にちゅうしたい！\n
ちゅうちゅう！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ご褒美をちらつかせると、疲れていたピアスの顔にぱあっと笑顔が戻る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうしてピアスを宥めすかして練習させているうちに、次第ブリーズの日が近くなっていた。"

hide m_pia5_3

with dis
$ hi_mes()

scene bg_par15_rg_amu_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_long
##endmemory
jump gakuen_pierce6
