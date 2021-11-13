jump fushigi_common2_amuse
label fushigi_ace2_2:

scene map_bg_summer_day
with stripe_l_medium

scene charasel_bg_amuse_day
with stripe_l_medium

scene yun_sum_01
with stripe_l_long

play music amuse_inside_p_ali
play sound se_0755

show go_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0072
Gowland "「ほら、[firstname]。\n
これがな、今、うちの遊園地一押しの商品！」"

hide go_t_03_4
show go_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0073
Gowland "「その名も、パスタサンドだ！」"

play sound se_0778
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どーん。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな効果音を伴いながら目の前に差し出されたものを見て、しばらく私は絶句した。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（パスタサンド）"

hide go_t_03_5
show go_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice gor_f0074
Gowland "「上質な食パンの間に、マカロニとスパゲッティを挟み込んだんだ。\n
味付けはトマト風味と、クリームがあってな、今回はトマトにしてみた」"

hide go_t_01_2
show go_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice gor_f0075
Gowland "「結構うまいんだぜ？\n
ボリュームも満点だし、客の評判だって悪くねえ」"

hide go_t_03_9
show go_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice gor_f0076
Gowland "「女性客に特に人気があってな。\n
あんたも、こういう味付け、好きだろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに組み合わせとしては、それほどおかしくはない。\n
味だって、決して悪くない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（主食がダブっている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "パンとパスタ……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも、マカロニとスパゲッティのコラボレーション。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに普通の食べ物同士の組み合わせなので、食べられなくはないのだが、どうしてそれを一纏めにしてしまったのか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「何も、わざわざパンで挟まなくてもよかったんじゃないの？」"

hide go_t_02_8
show go_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice gor_f0077
Gowland "「あのなあ、ここは遊園地だぜ？\n
食べ歩き出来るものじゃないと、遊ぶのに不便だろ」"

hide go_t_03_11
show go_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice gor_f0078
Gowland "「機能性を重視してあるんだ。\n
なあ、おまえら」"

hide go_t_01_10
show go_t_01_10 at left
show yuuen_man_02_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice tan_f0010
Employee "「アトラクションの順番待ちが食事時ですからね！」"

hide go_t_01_10

hide yuuen_man_02_02
show yuuen_man_02_02 at left
show yuuen_woman_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice may_f0010
Employee "「たくさん遊ぶにはボリュームも大事なんです！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相変わらず賑やかな従業員とゴーランドに押し付けられたサンドイッチのようなものを手に取りながら、とりあえず一口味見をする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この遊園地の食べ物は、どれも個性的だ。\n
時々食べ物とは思えない組み合わせが出てくるから、注意が必要なのである。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（うん、これは確かに……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「まあ、おいしくないとは言わない……、けど」"

hide yuuen_man_02_02

hide yuuen_woman_01_02


show go_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0079
Gowland "「そうだろ？\n
トマトだってちゃんと下処理からうちでやって、結構手が込んでいるんだぜ？」"

hide go_t_02_12
show go_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0080
Gowland "「そこらの洋食店にだって負けない味になっているって評判なんだ」"

hide go_t_02_8
show go_t_02_8 at left
show yuuen_man_01_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice tan_f0011
Employee "「うちの軽食は画期的で人気がありますよ！\n
ね、オーナー！」"

hide go_t_02_8

hide yuuen_man_01_04
show yuuen_man_01_04 at left
show yuuen_woman_01_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice may_f0011
Employee "「パスタサンドは、新作の中では人気ナンバーワンですね！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこにこと上機嫌に話してくれるゴーランドや従業員達の言葉通り。\n
確かに女性が好みそうな味付けになっているというのは間違いではない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「まあ……、確かにおいしいんだけど、今ひとつパンチが効いていないのと」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「やっぱり、{size=+20}パスタはパスタで食べたい{/size}」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（いくら食べやすくても、これじゃあ食べている気がしないわ）"

hide yuuen_man_01_04

hide yuuen_woman_01_03


show go_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gor_f0081
Gowland "「あんたの好みは難しいなあ……。\n
じゃあ、とりあえず次に行くか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「次？」"

hide go_t_03_2
show go_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice gor_f0082
Gowland "「ああ、次のうちの目玉商品、あんたに食わせてやる」"

hide go_t_02_12
show go_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice gor_f0083
Gowland "「今度は絶対に素直にうまいって言わせてみせるからな。\n
楽しみにしていろよっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうやら私のリアクションは、ゴーランドのオーナー魂に火を付けてしまったらしい。"

hide go_t_03_5


scene bg_gen_sky_sum_day
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0084
Gowland "「せっかく遊園地にいるんだ、普段のあんたは遠慮してあまり食って行かないからな。\n
今回は腹いっっぱいご馳走してやる」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを言ったゴーランドに園内の名物ツアーへと引きずられて、早三時間帯。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その間にご馳走になった食べ物の数は、自分でも正しく数え切れていない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "というより……、途中から、数えるのを放棄した。\n
明らかにキャパシティオーバーだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（さすがに……、おなかが苦しいんだけどなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地の食べ物は、幅広い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどのサンドイッチのように、手で持って食べられるファーストフードから、レストランまで……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "客のニーズと状況に合わせて選べるようになっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうも彼は今回その中でも、食べ歩きが出来るものを選んでいるようだ。"


scene yun_sum_01
with dis
play sound se_0384
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「ねえ、ゴーランド。\n
もう、おなかが限界なんだけど……」"


show go_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice gor_f0085
Gowland "「何言っているんだよ、[firstname]。\n
あれか、あんたもダイエットが気になるとかそういう口か？」"

hide go_t_02_3
show go_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice gor_f0086
Gowland "「遊園地に来て、そんなこと気にするなって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（この世界の男は、本当にデリカシーがないんだから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "体重も気にならないわけではないが、それ以前の問題だということがどうして分からないのか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「あなたと歩き始めて、もうかなりの量をご馳走になったから。\n
本当に、純粋に、おなかが苦しくて動けないって言いたいのよっ」"

hide go_t_03_7
show go_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice gor_f0087
Gowland "「え？もうなのか？\n
うちの従業員なら、まだまだいけると思うんだが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「…………。\n
{size=+20}あんなに新陳代謝の激しそうな人達と一緒にしないで{/size}」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここの従業員は、男女を問わず、いつでも元気いっぱいだ。\n
彼らなら確かに大丈夫だろうが、一緒にはされたくない。"

hide go_t_03_3
show go_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0088
Gowland "「うーん、そうだな。じゃあ、こいつで最後にしておくか。\n
はいよ、[firstname]」"


show t_ace2_1 onlayer master
with dis
hide go_t_03_9

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……クレープ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice kaz_f0007
Employee "「どうぞ！\n
うちの自慢のクレープを召し上がれ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "移動式の屋台から受け取ったものをそのまま手渡されて、首を傾げる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0089
Gowland "「ああ、新作クレープだ。\n
まずは食ってみろって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……う、うん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（見た目はクリームと果物っぽいけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "アトラクションを例にとっても、発想力という点でこのオーナーに勝る人を私は知らない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（これで実は中身が、～～～～だったり、～～～だったりするんじゃ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（いや……、～～～～～～だってことも）"

hide t_ace2_1

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「じゃあ、いただきます」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっと見つめてくる期待の眼差しに背中を押されるように、まずは一口食べてみる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「おいしい！」"


show go_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gor_f0090
Gowland "「そうだろう、そうだろう。\n
味にはうるさいあんたでも、これは絶対に受けると思ったんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にかっと歯を見せて笑うゴーランドは、子供のように嬉しそうな顔を見せている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「これ……、サワークリーム？」"

hide go_t_01_2
show go_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice gor_f0091
Gowland "「そういうこと。\n
甘いデザートに見せかけてあるけどな、中身は別物にしてある」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "白いクリームの中に溶け込んでいるオレンジは、果物ではなく、サーモンだ。\n
メロンにも見えたものは、キュウリのスライス。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他にも色々と具材が混ざっているようだが、そのどれもがサワークリームの酸味でまとまっている。"

hide go_t_01_12
show go_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0092
Gowland "「うまいか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「うん、おいしいわ。\n
ありがとう、ゴーランド」"

hide go_t_03_9
show go_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice gor_f0093
Gowland "「そうか、よかった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "笑った彼はそのまま近くのベンチへと案内してくれる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今まで同様、食べながら移動するものと思っていたが、どうやらここで休憩を入れるらしい。"

hide go_t_03_5
show go_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0094
Gowland "「あちこち歩いて疲れただろ、少し座っていけよ。\n
遊園地は、どこにも逃げたりしないから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「ありがとう」"

play sound se_0210 volume .6

play music honobono2_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人で掛けても充分に広いベンチに腰を下ろすと、彼は彼で買ってきたらしい珈琲を飲み始めた。眼鏡の奥の目が、座った私を見下ろしてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「何か、変？」"

hide go_t_02_8
show go_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0095
Gowland "「いや……、少しほっとしたところだ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_16")
T "（…………？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベンチにはまだスペースがあるというのに、彼は私の隣に腰掛けることもなく、そのまま肘置きに腰を下ろしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "わざと空けてあるスペース。\n
そこに、優しさと気遣いを感じたのは、自惚れだろうか。"

hide go_t_02_12
show go_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0096
Gowland "「うちに来てから、今ひとつ元気がなかったからな、あんた。\n
荒療治かと思ったが、連れ回してよかったよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（元気がなかった？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_13")
T "「私、いつも通りだったと思うんだけど？」"

hide go_t_03_10
show go_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_13")
voice gor_f0097
Gowland "「そうだな、目に見えてどうこうっていう感じじゃなかったが……。\n
多少なりともホームシックらしく見えた」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（そんな、子供じゃあるまいし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう否定することは簡単だったはずなのに、私はその声をじっと聞いている。"

hide go_t_03_12
show go_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0098
Gowland "「あんたのうちは、もうあそこなんだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ええ、そうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最初は迷い込んだと言ってもよかった、仮の居場所。\n
でも、今になっては……、あの場所に帰りたいという気持ちがある。"

hide go_t_01_10
show go_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0099
Gowland "「はははは、趣味が悪いな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「……自分でもそう思うわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（あなたのところにいるっていう選択肢だってあったはずなのにね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここは、誰でも受け入れてくれるとても居心地のいい場所。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、私の居場所はここではなく、私の帰りを待つ人もゴーランドではない。"

hide go_t_01_8
show go_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0100
Gowland "「まあ、いいさ」"

hide go_t_03_9
show go_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0101
Gowland "「今みたいに、落ち込んだり、イライラしたり……。\n
どうしようもなくなったときにこそ、遊園地だ」"

hide go_t_03_4
show go_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0102
Gowland "「遊んでいけばいい。\n
あんたの来園なら、この俺がいつでも歓迎してやるから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭に添えられる手。\n
珈琲のカップを持っていたせいか、その手は少し熱かった。"

hide go_t_02_8
show go_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0103
Gowland "「ここは遊ぶ場所だぜ、[firstname]。\n
元気が欲しいときは、いつでも来いよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「……ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気負わせない声に、力が抜ける。\n
残ったクレープを、何とか口の中に押し込んで……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「落ち着けるところはないかしら」"

hide go_t_02_12
show go_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice gor_f0104
Gowland "「は？\n
このベンチは落ち着けないか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「そういうわけじゃないけど。\n
おなかがいっぱいだから、少しゆっくりしたいのよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この場所も悪くないが、人通りが激しい。\n
繰り返した私に、ゴーランドはうーんと唸り、やがて顔を上げた。"

play sound se_0467
hide go_t_03_3
show go_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0105
Gowland "「なら、いいところがあるぜ。\n
あそこならばっちりだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思いついたというように指を鳴らし、そう言って彼は立ち上がった。\n
私も続くようにベンチを離れて、ついていく。"

hide go_t_01_2

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music looking_for_a_ali

scene bg_gen_sky_sum_day
with dis
play sound se_0464
$ hi_mes()
$ show_mes("frame_gen_chara")
voice mat_f0002
Captain "「そうよ、私は２５日間の間にお金を貯めて、普通になりたいの」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice oto_f0013
Defender "「普通？\n
まあ、姫様がなりたいっていうのなら、俺達はそのお手伝いをさせて頂きますけど」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice tak_f0000
Defender "「そんな覇気のないことを言うんじゃないわよ。\n
ええ、姫様、私達は全力であなたをサポートします」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice tak_f0001
Defender "「表向きはお手伝い出来ませんが、どこかで倒れたときには必ずお助けに参りますから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice hei_f0013
Child "「……うわあ、すごい。\n
プリンセス、お金稼げるのかなあ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice oda_f0013
Mother "「ふふふ、さあ、どうかしら」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice tad_f0001
Child "「あ、お姫様がオアシスに行ったわ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_17")
T "「…………」"


scene yun_sum_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ゴーランド、これ、何？」"


show go_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice gor_f0106
Gowland "「何って……、見ての通りだぜ。\n
遊園地の定番、キャラクターショーだ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「……こういうときのキャラクターショーって、子供に人気のヒーローとか、着ぐるみショーとか。\n
そういうのが定番だと思うんだけど？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突っ込みどころは山ほどあるが、私達が座っているのは、舞台から一番近い最前列だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舞台にいる役者に気を遣って声もつい控えめになってしまうが、ゴーランドは気にした様子もなく、ポップコーンを摘んでいる。"

hide go_t_02_12
show go_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0107
Gowland "「定番のショーのときもあるぜ？\n
戦うメイドさんが王子様に従う話とか、魔法学校に通う魔法の使えないお姫様の話とか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（それのどこが定番なの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供向けのキャラクターショーなど、大抵は悪者が出てきて観客を巻き込んで暴れたあと、ヒーローによって返り討ちにされるのがセオリーだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（悪役も大抵あっさりと負けるんじゃなくて、一回は優位に立って、でも結局勝てないっていうのが定番よね）"

show t_ace2_2 onlayer master
with dis
hide go_t_03_10

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice tak_f0002
Defender "「ですから、姫様、一人でオアシスに行くにはまだレベルが足りないといったでしょう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice mat_f0003
Captain "「仕方ないじゃない。\n
普通に戦っていたら、全然稼げないんだもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達の前で披露されているショーのタイトルは『砂漠の姫』。\n
タイトルだけならばショーとしてそれほどおかしくない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（親の決めた婚約相手と結婚したくないっていうところは、お姫様が主人公の話では珍しくないけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問題は設定である。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0014
Defender "「そうですよ、回復アイテムも少ないし、まずは砂漠で手頃なモンスターを倒して、堅実にですね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（……親が指名した婚約候補者が暗殺者やギャンブラーで、その人達を巻き込んで大金を稼ぐ話）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（今回は単独行動編みたいね……。\n
この世界らしいといえばらしいのかもしれないけど、突っ込みどころが多すぎない？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ある意味では現実的だが、少なくともショーの対象者は子供ではないだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0014
Child "「お金を稼ぐのって大変なんだね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0002
Child "「そうよね、目的のためには手段を選んでいちゃいけないわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice gor_f0108
Gowland "「今回は二人の守り役しか出て来ないが、他にも姫の幼馴染みや家庭教師が出る話もあるんだぜ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice gor_f0109
Gowland "「全部見るまでにどれだけ時間帯がかかるかは、分かんねえけどよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

hide t_ace2_2
show bg_gen_sky_sum_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（なんで、私こんなところで座ってキャラクターショーなんか見ているんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ち着ける場所に行きたいと言った私を、ゴーランドはこの場所に案内した。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "来たときは板を渡した簡易ベンチが並んでいるだけだったので、ここがキャラクターショーの会場だとは気付かなかったのだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0015
Child "「プリンセス、頑張って！\n
ダークエルフを倒せば、お金がたくさんもらえるよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0016
Child "「一攫千金のチャンスだっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0003
Child "「それに宝が手に入れば、商人が高く買ってくれるもの。\n
負けないでーっ」"

hide bg_gen_sky_sum_day

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（こんなに人気のあるショーだとは思わなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供とその保護者だろう。\n
大人と子供が入り交じって、私達の周囲に同じように腰を下ろしていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "このショーはいつでも開演されているものではないらしく、ときには順番取りで長蛇の列が出来ることもあるらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（人気なのは分かるけど……、人気の理由は謎だわ）"


scene bg_gen_sky_sum_day
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice mat_f0004
Captain "「この……、二回攻撃！」"

play sound se_0029
pause .5
play sound se_0436
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "姫の声と共に、モンスターを倒す音が鳴った。"

play sound se_0654
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0017
Child "「やった、勝ったよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0004
Child "「おめでとうっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "熱狂的な声を上げて、子供達はショーを楽しんでいるようだ。"


$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0015
Defender "「……ん？\n
あなた、誰ですか？」"


scene yun_sum_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舞台には、倒されたモンスター役と、男女の役者が三人だけだったはずだ。\n
そこに……、もう一人、影が増えていた。"


play music secret_a_ali

show t_ace2_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（あの仮面は……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0088
Unknown "「探しましたよ、プリンセス。\n
こんなところにいるなんて、思いませんでした」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice ace_f0089
Unknown "「困りますねえ。\n
勝手に出歩かれたら、皆心配しますよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
Captain "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice mat_f0005
Captain "「あなたは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "男の登場に驚きつつも、姫役の役者はそのまま演技を続けることを選んだらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供達から見えないように、仲間に目配せを送って状況を確認するが、彼らも心境は同じなのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "互いに「誰だ？」と問いかけ合うだけだった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（なんで、ここにいるの？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（それに、何、その格好は！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔を隠していようと、服の色が違おうと、口調を変えようと、見間違えるはずがない。\n
ハートの城の騎士、エースだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「まさか、あの人がアルバイトをしているなんて言わないわよね、ゴーランド？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_10")
voice gor_f0110
Gowland "「いや……、特にそういう話は聞いてねえなあ。\n
まあ、あの迷子騎士のことだから、また迷っているんじゃねえか？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（迷子になったっていうような状況じゃないでしょう、これはっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想外の出来事、それも他の領土の役持ちが現れたというのに、ゴーランドは気楽なものだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0111
Gowland "「飛び入り参加か、これは面白いものが見られそうだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「な、何を悠長なことをっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "周りの子供達はこれもショーの一部だと思っているのだろう。\n
初めての展開に驚きながらも真剣に見ている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0112
Gowland "「しーっ、静かにしろよ、[firstname]。\n
子供の夢は壊すものじゃねえだろ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「そうだけど……。\n
このままやらせたら……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（逆に夢を壊しかねない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の不安を察したのか、ゴーランドは顎を撫でながら視線を舞台に戻す。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0113
Gowland "「俺はここのオーナーだからな、ぶち壊すような真似をするなら止めもするが」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0114
Gowland "「飛び入りでも、客を満足させてくれるのなら歓迎するぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"


play music tension_a_ali
hide t_ace2_3
show bg_gen_sky_sum_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "白い影がふわりと揺らめく。\n
その手に持っている刃の煌めきに、思わずぞっとした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（あれって……、真剣じゃないの！？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
Defender "「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
Defender "「！？」"

play sound se_0604
pause .4
play sound se_0685
pause .15
play sound se_0553
pause .2
play sound se_0579
hide bg_gen_sky_sum_day
show t_ace2_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が息を飲んだ瞬間に、すべては終わっていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "姫役の女一人を残して、舞台に上がっていた守り役を演じていた二人の役者が伏せている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tak_f0003
Defender "「くぅ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0016
Defender "「つ、強い……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（い、いつのまに倒したのか、全然見えなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、守り役を演じていた役なし達の息があることにほっとする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "真剣を持ち込んでいるので油断は出来ないが、一先ず唐突に役者を殺し始めることはなさそうだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0090
Unknown "「プリンセス、そろそろ諦めたらいかがです？\n
あの場所には、あなたを満たすものがある」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0091
Unknown "「それらすべてを捨て去ってでも。\n
変わることが、それほど大事なことですか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0006
Captain "「……っ。\n
嫌よ、私は普通になりたいの！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0007
Captain "「こんな犯罪大国の女王じゃなくて……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0092
Unknown "「……俺に、斬られることになっても？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "低い声。\n
問いかける声のはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首筋に刃を押し当てられているような、冷たい気配を感じた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Captain "「……っ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0008
Captain "「わ、私は……、プリンセスだけど。\n
でも結婚ぐらい、自分の好きな人としたいのよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0009
Captain "「邪魔しないでっ」"

play sound se_0680
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_6")
T "（だめ……！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "姫役を演じている彼女も多少は剣を使えるらしいが、あくまでショーの一環としての腕前だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見せるためではなく、斬るために鍛えたエースの腕に、敵うはずがない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Unknown "「…………」"

play sound se_0674
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "がむしゃらに剣を振るう姫役の女に彼は剣を向け、そして。"

play sound se_0439
pause .5
hide t_ace2_4
show white onlayer master ##instant
play sound se_0191
hide white ##instant
show bg_gen_sky_sum_day onlayer master with spread_short
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T "（え？）"

play sound se_0125
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "風を切りながら、姫役の女の持っていた剣が虚空を裂く。\n
逃げようとも思えないほど必殺のタイミングで……、刃が迫ってきた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！！」"

hide bg_gen_sky_sum_day

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_9")
T "（危ないっ）"

play sound se_0428
pause .6
play sound se_0352
pause .4
play sound se_0043
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぎゅっと目を閉じ、衝撃を待つ。\n
しかし銃声と金属音が響くくらいで、痛みはない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0115
Gowland "「[firstname]、目、開けていいぜ」"

hide black with open_long

play music amuse_inside_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「あ……。\n
ゴ、ゴーランド」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "促されて、目を開く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで暢気にポップコーンを持っていた手には、大型のライフルが握られている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、私に向かってきていた刃は、弾かれ、地面に突き刺さっていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（ゴーランドが庇ってくれなかったら危なかった。\n
ううん、庇ってくれたとしても、間に合わなかったら……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "地面の代わりに刺されていたのは、この私だったはずだ。\n
そう考えると、背筋に冷たいものが一気に溢れた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"


show go_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Gowland "「…………」"

play sound se_0468
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドが、突然指をパチンと鳴らした。"

play sound se_0312
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが閉幕の合図だったのだろう。\n
舞台袖から従業員が出てくると、呆然としている姫役の女と、伏せている守り役の男達を急かして、去っていく。"


show yuuen_woman_02_03 at center
hide go_t_02_13
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0007
Employee "「ああ、プリンセスの賭けの行方は如何に！？\n
続きをどうぞお楽しみに～」"

play sound se_0560
play sound se_0156
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "従業員の声と共に、幕が下りる。\n
驚きと、そして疎らな拍手が起こった。"

hide yuuen_woman_02_03

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0018
Child "「えー、ここで終わりなんてつまらないよっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0005
Child "「もっと、続きが見たかったのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供達は口々に文句を言っているが、役者がいなければショーは始まらない。\n
私も、不満げな声にいつまでも構っていられなかった。"


scene bg_gen_sky_sum_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「……舞台、お邪魔するわよ。\n
ゴーランド」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "形だけ断りを入れると、そのまま彼を振り返ることなく舞台の上に乗った。\n
閉ざされた幕を持ち上げると、舞台の上にあの白い影は既に消えていた。"

play sound se_0064
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（どこにいるの？\n
もう、どこかに行っちゃったの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はどこにでも迷い込み、どこにでも迷い出る。\n
薄暗い舞台の上を移動しながら、舞台袖へと向かった。"


$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0010
Captain "「な、何だったのよ。\n
あの男」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0011
Captain "「オーナーがシナリオを変えたのかしら？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0017
Defender "「シナリオの変更なんて珍しくもないけどさ。\n
あれ、同業者って感じじゃなかったよな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（……当たり前よ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "袖で話し合う役者達の横を通り抜け、更に奥へと進む。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（エースの剣は、完全に実用向きだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見せるための演舞として剣を嗜むものもいるだろうが、あの男の剣は叩き斬るための技術だ。\n
重さも、鋭さも、まったく異なる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元々屋外に設けられた舞台だ。\n
それほど広い袖ではない。\n
その中を抜け、辿り着いた先は……。"


scene bg_gen12_yuk
with dis

play music forest1_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（そういえば、ここ、遊園地の端だったっけ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "広大な遊園地の片隅。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "アトラクションによっては音が出るものもあるから、舞台が邪魔されないようにと端のほうに設置してあるのだとゴーランドは話していた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0093
Unknown "「あれ、[firstname]？\n
そんなに血相を変えて追いかけてくるなんて、どうしたの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「エース」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "木立の中に、白い影が浮き上がっている。"


show ace_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0094
Ace "「残念だけど、サインはお断りしているんだ。\n
ほら、俺、騎士だし……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つけていた仮面を外しながら、エースがそう答える。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「心配しなくても、あなたのサインを強請ろうなんて思っていないわよ」"

hide ace_w_01_10
show ace_w_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice ace_f0095
Ace "「あれ、そうだったの？\n
君がほしがってくれるのなら、ちょっと考えてもよかったのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仮面の下にあった顔は、やはり私のよく知る男のものだった。\n
爽やかに笑う、日差しの下が似合う男。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、その笑顔に何か違和感を覚えてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（……何だか、変）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "違和感の正体は分からないものの、何かがずれていることだけは分かる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「エース……」"

menu:
    "その服なんだけど……。":
        jump fushigi_ace2_3a
    "機嫌、悪い？":
        jump fushigi_ace2_3b

label fushigi_ace2_3a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「その服なんだけど……、一体どういうつもり？」"

hide ace_w_01_1
show ace_w_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice ace_f0096
Ace "「どういうつもりって、そんなに変？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「……変というか、違和感があるというか」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（白いせいかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "会合の際のスーツでさえ、彼の服から赤は消えなかった。\n
例外は舞踏会ぐらいだが、礼装と騎士服では全然印象が違う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも真っ赤なエースが、白い騎士になっているだけなのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（すごく、変な感じ）"

hide ace_w_01_3
show ace_w_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice ace_f0097
Ace "「違和感って……、酷いな。\n
たまたま衣装部屋に迷い込んじゃって、少し拝借しただけだったんだけど」"

hide ace_w_01_2
show ace_w_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice ace_f0098
Ace "「そんなにみっともなく見える？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「みっともないんじゃなくて、エースじゃないみたいというか。\n
落ち着かないというか」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（そもそも、衣装部屋にあったものを勝手に着る理由が分からない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうして衣装部屋に迷い込むのだろう等という疑問は、彼にとっては無意味だろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の迷子癖は私もよく知っている、理屈ではないのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（迷い込んだ先がどこでもいいけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「なんで、そんな服にわざわざ着替える必要があったのよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城と遊園地は敵対勢力だが、決して他領土に来られないわけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ましてや、エースは自分の役割を嫌がっている。\n
変装する必要など、どこにもないはずだ。"

hide ace_w_01_8
show ace_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0099
Ace "「君の傍に侯爵さんがべったりついていたからね。\n
違う形で接近しようと思ったら、たまたま目に入ったんだ」"

hide ace_w_01_10
show ace_w_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0100
Ace "「ははは、本当は白なんて赤よりも好みじゃないんだけどね」"

hide ace_w_01_4
show ace_w_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0101
Ace "「……わざとらしくて」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「？」"

hide ace_w_01_13
show ace_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
Ace "「[firstname]」"

jump fushigi_ace2_4
label fushigi_ace2_3b:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（何だか、ぴりぴりしているというか。\n
爽やかに……、威圧されている気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースは分かりやすいようで、とても分かりにくい。\n
表情の変化だけでは彼の機嫌は判断出来ない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこで役に立つのは、付き合いや経験などの、重ねてきたもの。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……あなた、機嫌が悪くない？」"

hide ace_w_01_11
show ace_w_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice ace_f0102
Ace "「ははは、何言っているんだよ、[firstname]。\n
俺はいつも通りだぜ」"

hide ace_w_01_4
show ace_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice ace_f0103
Ace "「機嫌が悪いはずがないだろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "からからと笑ってくるが、やはりおかしい。\n
声のトーンにも変化はないのだが、言葉の裏に棘が見え隠れしている気がする。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「でも、なんだか……、ちょっと変な気がするんだけど」"

hide ace_w_01_10
show ace_w_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0104
Ace "「変ねえ。\n
ペーターさんや陛下に比べれば、俺なんて面白味のない普通の騎士じゃないか」"

hide ace_w_01_6
show ace_w_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0105
Ace "「機嫌だって、悪くないぜ。\n
久しぶりに君に会ったんだから」"

hide ace_w_01_3
show ace_w_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0106
Ace "「よくなることはあっても、悪くなるなんて……。\n
あるはずがないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（やっぱり、機嫌悪いわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "爽やかな言葉の中に混じる重圧感は、錯覚などではないだろう。"

hide ace_w_01_13
show ace_w_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「[firstname]」"

jump fushigi_ace2_4
label fushigi_ace2_4:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……何？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "近付いてくるエースに、意図が読めず聞き返す。"

hide ace_w_01_11
show ace_w_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0107
Ace "「侯爵さんと、ずいぶん仲がいいんだね。\n
二人で遊園地を食べ歩きなんて、デートみたいだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「あれはデートっていうほどのものじゃないわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（いつから見ていたんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰よりも遊園地に詳しい人物にナビゲートしてもらっていただけだ。\n
楽しかったことを否定する気はないが、デートというのとは違う。"

hide ace_w_01_10
show ace_w_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0108
Ace "「あれで？\n
まるで恋人みたいだったじゃないか」"

hide ace_w_01_3
show ace_w_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0109
Ace "「……俺、君がうじうじと悩みに行きたいっていうから見送ったのにな。\n
浮気されているなんて、思わなかったぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……浮気？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想していなかった言葉に思わず繰り返してしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（浮気）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（私が、ゴーランドと浮気）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "{size=+20}「ありえないわよ、それ」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はあくまで友人の一人だ。\n
大切だとは思うが、そういう対象にはならない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドも、私の帰る場所は遊園地ではないと告げていた。"

hide ace_w_01_8
show ace_w_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0110
Ace "「違った？\n
俺としても、否定してくれるのは嬉しいけど」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は目を伏せながら、私の顎に手をかけてくる。"

hide ace_w_01_6
show ace_w_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0111
Ace "「俺に愛想を尽かせちゃったのか、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「だから、ゴーランドには別にそういう意図はなかったと……」"

play sound se_0749
pause .4
hide ace_w_01_12
show ace_w_01_12 at left
show go_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice gor_f0116
Gowland "「何だよ、あんたには全然通じてなかったのかよ、[firstname]。\n
冷てえな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ゴーランド？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を追いかけてきたのだろうか、いつの間にか背後に立ったゴーランドは、呆れたように肩を竦めて見せた。"

hide go_t_03_2
show go_t_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0117
Gowland "「あんまりいじめるなよ。\n
それも、嫉妬なんかで傷物にされちゃあたまらねえや」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「傷物……？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_14")
T "（あの役者さん達のことかな）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（でも、何に嫉妬するっていうの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースが彼らに妬く理由なんて、どこにもない。"

hide ace_w_01_12
show ace_w_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0112
Ace "「ははは、妬くだなんて、心外だな」"

hide ace_w_01_10
show ace_w_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0113
Ace "「俺はただの通りすがりの、三流役者だけどさ。\n
苛立って誰かに八つ当たりするようなシナリオじゃ、動いてあげられないな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（八つ当たり……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "かつて、クローバーの塔でグレイがエースに言った言葉を思い出す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引っ越しで、ユリウスがいなかったときのエースの荒れ具合は、思い出すだけで肝が冷える。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（あれ？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（だったら、今、エースは誰に対して苛立っているの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドに対して苛立っているのなら、もっと直接的に彼に突っかかっているだろう。"

hide go_t_01_6
show go_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0118
Gowland "「こええな。\n
俺にはおまえとやり合う気はないんだが……」"

play sound se_0428

play music tension_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すっと。\n
先ほどまで穏やかな顔で話していたゴーランドの顔が冷える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に来てから感じることのなかった、晴れていた空に雲が差し込んだような、そんな感覚。"

hide go_t_01_13
show go_t_03_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0119
Gowland "「今のおまえには、この子は返せねえな。\n
今回は、一人で自分のところに帰れよ、騎士」"

hide go_t_03_6
show go_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0120
Gowland "「嫉妬で剣をぶん投げるなら、相手が違うだろ」"

hide ace_w_01_11
show ace_w_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0114
Ace "「……嫉妬ね。\n
なんだかそれって、すごく気持ち悪いなあ」"

hide ace_w_01_6
show ace_w_01_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0115
Ace "「どろどろ、べたべたしていそう」"

hide go_t_02_9
show go_t_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0121
Gowland "「おまえがどろどろしようがどうでもいいがな、当たる相手を間違えているぜ。\n
おまえのところの同僚とか上司とか、多少暴れても問題ない奴にしておけ」"

hide ace_w_01_8
show ace_w_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0116
Ace "「確かに簡単に壊れる相手じゃ鍛錬にもならないんだけどさ。\n
……侯爵さんなら、いい相手になりそうだけどなあ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "短い言葉の中に込められたその響きに、私は息を飲んだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぶら下げたままの抜き身の刃が、森の中で不気味に光る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ゴーランド……」"

hide go_t_02_1
show go_t_03_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice gor_f0122
Gowland "「言っただろう、俺はおまえとやり合う気はねえよ。\n
ほら、客じゃねえならとっとと帰れ」"

play sound se_0512

play music amuse_inside_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ライフルの引き金にかけていた指を外して、ゴーランドが手を振る。\n
言葉通り、彼に戦う気はないらしい。"

hide ace_w_01_4
show ace_w_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0117
Ace "「…………。\n
ちぇ、それじゃあ仕方ないか」"

hide ace_w_01_6
show ace_w_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0118
Ace "「今回は大人しく帰ることにするよ。\n
帰れれば……、ね」"

play sound se_0348
hide ace_w_01_10
show ace_w_01_11 at center
hide go_t_03_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Ace "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "マントを翻した相手は、手に持っていた仮面を差し出してくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！？」"

show t_ace2_5 onlayer master
with dis
hide ace_w_01_11



$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice ace_f0119
Ace "「予約を入れておかないと取られそうだからね、確保しておきたいんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「よ、予約！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口元に触れたひんやりとした感触に、何故か顔が熱くなった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0120
Ace "「そうとも、ここは俺が先に予約しているんだから……。\n
誰にも、触れさせたりしちゃ駄目だぜ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0121
Ace "「約束を破る悪い子には、お仕置きが待っているものなんだから。\n
な、お姫様？」"

hide t_ace2_5

play sound se_0624
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "甘いような。\n
毒のような。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな言葉を最後に残して、エースは去っていった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（顔、まだ赤いのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "全身がぽかぽかと熱い。\n
まるで風邪でもひいたような、おかしな熱が駆け巡っている。"


show go_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0123
Gowland "「……やれやれ。\n
最近の若い奴は、面倒が多くていけねえ」"

hide go_t_02_10
show go_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0124
Gowland "「それに、あいつ、うちの衣装勝手に持って行きやがって……。\n
次は、ちゃんと取り返さねえとな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「次って言うけど……。\n
相手はエースよ、いつ来るかなんて分からないじゃない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（そして、再び来た頃にはずたぼろになっていそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "衣装が無事に帰ってくる保証などないだろう。\n
しかし、私の予想に反してゴーランドは手をぱたぱたと振って見せた。"

hide go_t_03_11
show go_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0125
Gowland "「いや、すぐ来ると思うぜ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「は？」"

hide go_t_01_7
show go_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice gor_f0126
Gowland "「あいつは迷いやすい奴だけどよ、イラついている原因が今回ははっきりしているからなあ。\n
意外と迷わねえんじゃねえか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_13")
T "「原因？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（そういえば嫉妬がどうのとか言っていたけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の言いたい意味がよく分からないまま首を傾げていると、遊園地のオーナーは気を取り直したように手を打った。"

play sound se_0491
hide go_t_01_11
show go_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0127
Gowland "「何はともあれ、食い倒れツアーも一段落したし。\n
今回はこれでお開きとしようぜ」"

hide go_t_03_9


scene bg_gen_sky_sum_day
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結局、はぐらかされてしまったようだ。"

$ hi_mes()

scene charasel_bg_amuse_day
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_long
##endmemory
jump fushigi_common3_amuse ##I think
