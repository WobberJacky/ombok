
scene map_bg_autumn_day
with dis

scene charasel_bg_hatter_day
with dis
label fushigi_dad1:
hide screen hatter_man_choice
$ clockanim()

$ hi_mes()

scene b_aut_01
with dis

play music hatter_corridor_p_ali

scene br_01 with Dissolve(1.2)
play sound se_0776
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目的地が決まれば、あとは問い詰めるだけ。\n
二人のいる部屋に向かって、移動を始めた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らの仕事場は屋敷の門だが、休憩中にまで詰めているような性格ではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（あの子達のことだから、また刃物でも弄っているんだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "危険な物が好きな双子は、コレクションの刃物を見せてくれることがよくある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "休憩中に手入れをしておくんだと言った言葉が本当なら、今はまさにその最中かもしれない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（正直……、あまり見たくないけど、仕方ない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここで尻込みしていては、何の解決にもならない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドは掴み所がなく、もったいぶった言葉で煙に巻くに決まっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットの性格から考えれば話してくれる可能性は高いが、ブラッドに心酔している彼のこと、箝口令にはあっさりと従うだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供だからという理由ではなく、あの二人はこの屋敷の中でも特に私に甘い。\n
彼らを今回の交渉相手に選んだのは、それが最大の理由だ。"


show bousi_t_02_06 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0031
Maid "「あれ、ひょっとして……、門番さん達のところに行くんですか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屋敷の廊下を歩いていると、通りがかった使用人からそんな声がかかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ええ。\n
二人のところに行くつもりだけど……、今って何かまずいの？」"

hide bousi_t_02_06
show bousi_t_02_06 at left
show bousi_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice chi_f0027
Maid "「いえいえ……、まずいだなんてそんなこと」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_16")
T "（怪しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この屋敷の使用人は全員マフィアの構成員だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "メイド服を着ていようと、いくらだるそうに見せていても、その本質までは変わらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その彼らまで、どこかおかしい。\n
双子ほどではないが、やはり何かを私に隠しているような気がする。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（一体、何をしようとしているのかしら）"

hide bousi_t_02_06
show bousi_t_02_01 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice may_f0032
Maid "「では、私達はこのあたりで……」"

hide bousi_t_02_01
hide bousi_t_01_02
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が訝しんでいることに気付いたのか、彼らはそそくさと離れていった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（皆して、私に何を隠しているのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私もここの使用人の一人、同僚である彼女達から仕事の話を聞くことも珍しくない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこかで誰かを～～～～したとか、～～～～～～したとか……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そういう物騒な話なのでつい矛先を逸らしてしまうが、私が双子のことを気にしているときには、こっそりと情報をくれたりする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人の本来の仕事は門番。\n
だが外での仕事が長引くと、なかなか戻ってこないことがある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなときには、私が門のところまで様子を見に行くことを知っているのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（なのに、休憩中も最近は何だかだるそうなのに、そわそわしているし……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おかしい。\n
私だけが彼らの中に入れないでいる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（とりあえず、二人に聞くことを優先しなくちゃ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今は、彼らよりもディーとダムに話を聞きに行くと決めたのだ。\n
素直に話すかは分からないが……、とりあえず聞いてみなければ始まらない。"

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music deedam_t_ali

show dee_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0082
Dee "「いらっしゃい、お姉さん！\n
遊びに来てくれたの、嬉しいな！」"

hide dee_t_01_6
show dee_t_01_6 at left
show dam_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0083
Dam "「僕達も今ちょうどお姉さんに会いたいねって話していたんだ」"

hide dam_t_01_9
show dam_t_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0084
Dam "「思いが通じたんだね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアをノックしようとした瞬間、中から青と赤の少年が飛び出してきた。\n
まるで、部屋の中から外の様子を見ていたかのようなタイミングのよさだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の気配を察したのか、それともあるいは先ほど擦れ違った同僚から連絡でもあったのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（……あやしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どちらとも言い切れないが、少なくとも彼らが私に隠しごとをしていることに、間違いはなさそうだ。"

hide dee_t_01_6
show dee_t_01_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0086
Dee "「お姉さんは、どこに行きたい？\n
どこでもいいよ、ハートの城に追いかけっこに行く？」"

hide dam_t_01_7
show dam_t_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0087
Dam "「遊園地でボリスと一緒にネズミで遊ぶのもいいよね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人は揃ってドアを後ろ手に閉めたまま、にこにこと私を見上げている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもなら、自慢のコレクションを見せたいと言って問答無用で部屋に引き込む二人が、である。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（部屋の中、見られたくないのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋が散らかっているから、見せたくないという気持ちは私にも分かる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "年頃の男の子なら、女の子を部屋に入れるのに抵抗があるという気持ちもあるだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、それはあくまで一般的な、普通の男の子の場合だ。\n
この子達に限って、そんな態度は想像できない。"

hide dam_t_01_2
show dam_t_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0089
Dam "「お姉さんはどこに行きたい？\n
どこにでもお姉さんの行きたいところに付き合ってあげる」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人は必死にドアを自分達の身体で隠している。\n
この奧には何もありませんというような態度だが、逆に怪しさが増すだけである。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「ディー、ダム」"

hide dee_t_01_9
show dee_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_8")
voice dad_f0090
Dee "「何、お姉さん」"

hide dam_t_02_1
show dam_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_8")
voice dad_f0091
Dam "「行きたい場所、決まった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「ええ、決まったわ。\n
あなた達の部屋に入れてちょうだい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこでもいいという彼らの言葉に従って、今一番気になる場所を告げると、二人は揃って視線を逸らした。"

hide dee_t_02_10
show dee_t_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0093
Dee "「い、今は散らかっているから、入らないほうがいいよ……。\n
お姉さん、驚いちゃう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「気にしないでちょうだい、大丈夫よ。\n
今更刃物の一本や二本、転がっていても驚かないから」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（この屋敷で刃物や銃が転がっているなんて、いつものことだもの）"

hide dam_t_02_10
show dam_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice dad_f0094
Dam "「ああ、でも……。\n
今は入らないでほしいというか、見られたくないというか……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（よっぽど見られたくないのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何を隠しているのかは分からないが、彼らがここまで私を入れるのを渋ったことは今まで一度もない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「……私が部屋に入るのは、嫌なの？」"

hide dee_t_02_7
show dee_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice dad_f0096
Dee "「い、嫌なんかじゃないけど……。\n
今じゃなければ、むしろ歓迎するところだけど」"

hide dam_t_02_8
show dam_t_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice dad_f0097
Dam "「うん……。\n
今は、ちょっと……、ね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「入れてくれるわよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "渋る双子を押し切るようにそう言うと、彼らは困ったように目配せをしたあと、観念した。"

hide dee_t_03_10
show dee_t_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0098
Dee "「あんまり綺麗じゃないからね。\n
だから、そんなに見ちゃだめだよ」"

hide dam_t_03_9
show dam_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0099
Dam "「そうそう。\n
刃物もあるし、勝手に触ったりしたら危ないからさ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言いながら、いつもとは比べものにならないゆっくりとした動きで、ドアを開けてくれた。"

play sound se_0276
hide dee_t_02_8

hide dam_t_02_9


scene f_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いざ……、と入ってみたのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（あれ？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「片付けてあるじゃない。\n
どうして入れてくれなかったの？」"


show dee_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice dad_f0100
Dee "「そんなことないよ、あちこち散らかっているし」"

hide dee_t_02_10
show dee_t_02_10 at left
show dam_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice dad_f0101
Dam "「そうだよ。\n
お姉さん、そこにもナイフが落ちているから、気を付けて」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人の部屋は、私がよく知るいつもの光景とあまり変わらなかった。\n
確かにいつものように物騒な玩具が転がっているが、その程度だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（……その程度って流せてしまう自分も問題だけど、この際目を瞑ろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイフに、斧。\n
刃が反り返った剣に、ぎざぎざとしたノコギリのようなものまであるが、この程度なら、いつもと変わらない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（特に何もおかしなところはなさそうだけど……）"

hide dee_t_02_10
show dee_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
Dee "「…………」"

hide dam_t_02_6
show dam_t_01_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
Dam "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の後ろをついてくる二人は落ち着かないのか、視線をふらふらと彷徨わせている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "やはり何かを隠しているのは間違いないらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（男の子が隠すもの……？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（今更この子達がそんなものを隠すとも思えないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬浮かんだ想像を追い払うように、首を振って……、それに気が付いた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ソファの下、いつもなら物騒なナイフが押し込まれている場所に、紙の束のようなものがあった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「あ」"

hide dee_t_01_5
show dee_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
Dee "「！！」"

hide dam_t_01_12
show dam_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
Dam "「……！」"

play sound se_0001 volume .6
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屈み込んで取ろうとした私よりも二人のほうが早い。"

play sound se_0313
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引ったくるように私の目の前にあったそれを奪い取ると、二人は顔色を変えた。"

hide dee_t_02_6
show dee_t_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0102
Dee "「だ、だめだよ！\n
お姉さんはこれを見ちゃだめっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_3")
T "「……どうして見ちゃいけないの？\n
いつもならあなた達の宝物だって色々と見せてくれるじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、いつもなら見たくなくても、私の意志など無視して自慢してくるのが、彼らだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが今回だけは様子が違うともなれば、気にするなというほうが無理な話だと、どうして分からないのか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「あなた達、何をそんなに隠すわけ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_11")
T "「ブラッド達と何を考えているの？\n
私だけ教えてくれないなんて、酷いわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供っぽいと自分でもわかっているが、無意識に文句を言うような口調になってしまう。"

hide dam_t_02_3
show dam_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice dad_f0103
Dam "「何も隠してなんかいないよ。\n
本当に、なんでもないんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「なんでもないなら、見せてくれたっていいじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口を尖らせて手を伸ばしたが、彼らはさっと後退って私の手から離れていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「あ……」"

hide dee_t_02_7
show dee_t_03_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice dad_f0104
Dee "{size=+20}「と、とにかく、これだけはお姉さんは見ちゃ駄目なんだってば！」{/size} "

hide dam_t_02_7
show dam_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice dad_f0105
Dam "「そうだよっ。\n
他の誰かならまだしも、{size=+20}お姉さんだけは、駄目！{/size}」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を振り払われたことよりも。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（私だけは、駄目……？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言われたその一言に、胸の中に火が灯った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然やってきた私を受け入れてくれた場所。\n
いくつもの滞在地がある中で、この屋敷を訪れたのは本当に偶然だった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_3")
T "（でも、ここに残ろうと決めたのは、あなた達がいてくれたからだったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "刃物を振り回して、血に染まる双子の門番。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怖いとも思うし、正直これ以上はやめてほしいと思うこともある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも他の滞在地に移るなんて、一度も考えたことはなかったのは、彼らがここにいるからだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………。\n
もういい、分かったわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「そこまで言うなら、見せてくれなくていい」"

hide dee_t_03_8
show dee_t_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice dad_f0106
Dee "「ほ、本当に……？\n
分かってくれたんだね、お姉さんっ」"

hide dam_t_03_10
show dam_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice dad_f0107
Dam "「よかったね、兄弟。\n
さすがお姉さんだよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ほっとしたように私に笑いかけてくるディーとダムに、私の胸の内が読めていたら、どんな顔をしていただろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きっと、こんな表情は浮かべられなかったに違いない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（そんなに教えたくないのなら、もういいわよ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_2")
T "「あなた達が教えてくれる気になるまで、私、ここには来ないことにするから」"

hide dee_t_02_4
show dee_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_2")
voice dad_f0109
Dee "「……え？\n
ここには来ないって、どういうこと？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「簡単に言えば、家出をするって言ったの」"

hide dee_t_01_5
show dee_t_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice dad_f0111
Dee "「家出って……、あの家出のこと？\n
橋の下で夜を明かしたりとか、路上で生活したりとかそういう家出！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（なんでそう、局地的な具体例なのよ）"

hide dam_t_02_10
show dam_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice dad_f0112
Dam "「お姉さんの家はここでしょう、どうして出て行っちゃうの！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_9")
T "「帽子屋屋敷を出て行くんだから、家出で間違っていないはずよ。\n
せっかくだもの、心置きなく、外で遊んでくるわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「あんた達とは、遊んであげない！\n
ついてきても、口なんか聞いてあげないからね！」"

play sound se_0286
hide dee_t_02_7

hide dam_t_02_6

camera at hpunch
camera at vpunch

scene br_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言い切って、唖然とする双子をそのままに、私はその足で部屋を出ていく。"


show bousi_t_01_06 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0018
Maid "「お嬢様？\n
どうされましたか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不思議そうに同僚が声をかけてくるが、今は無視してしまう。\n
ささくれだった気持ちは簡単に沈静化してくれそうもない。"

hide bousi_t_01_06

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（ああ、子供っぽい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自覚はしていても、一度火がついたものは発散するものを求めて暴れ狂っていた。"


show bra_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0293
Blood "「おや、ご機嫌斜めだな。\n
門番達と喧嘩でもしたのかな、お嬢さん？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（そして、こっちはこっちで嫌なタイミングで出てくるし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に来てから神出鬼没な人間ばかりだが、この男もその類に漏れない。\n
どこからともなく現れたブラッドの横を通り過ぎながら、素っ気なく答えた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_2")
T "「喧嘩じゃないわよ、絶縁してきたのよ」"

hide bra_t_01_11
show bra_t_03_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_2")
voice blo_f0294
Blood "「絶縁とは……。\n
それはまた穏やかではないな」"

hide bra_t_03_16
show bra_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_2")
voice blo_f0295
Blood "「退屈しなくて結構だが、君があの子達とそこまで喧嘩をするなんて珍しいじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼のほうが身長も高い分、私の歩く速度に合わせやすい。\n
そのまま自然な動きで横に立つと、私の顔を覗き込んできた。"

play sound se_0584
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気にしながらも、廊下を大股で歩いていく。"

hide bra_t_03_10
show bra_t_02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0296
Blood "「お茶でも飲みながら、ゆっくり話を聞かせてもらおうかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「結構です」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（あなただって私に教えてくれないくせに……。\n
他人事みたいに言わないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供っぽいと自分でも思う。\n
しかし、除け者にされたという感覚は、そう簡単に拭えるものではなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が率いる、帽子屋ファミリー。\n
その名の通り、マフィアにはなれなくても、私に家族のような繋がりを与えてくれる場所だったから尚更だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（そこまで隠したいなら、好きにすればいいわ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「……ちょうどいいわ、ボス。\n
私の有給が大分あったので、今回一気に使わせてもらいます」"

hide bra_t_02_15
show bra_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
Blood "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすがにこれはただの喧嘩ではないと悟ったのか、揶揄する雰囲気を改めてブラッドが片方の眉を持ち上げた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま引き留めようと肩に手を伸ばしてきたが、私のほうが早い。"

play sound se_0051
camera at hpunch
camera at vpunch
hide bra_t_03_5
show bra_t_03_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屈み込んでいた頭の上に乗っていた帽子を、力ずくで引っ張った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「無断欠勤だなんて後で言われたくないから、ちゃんと言ったわよ。\n
それじゃあ、ごきげんよう！」"

play sound se_0584
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚いたように帽子を直す男が足を止めている間に、私は早足に廊下を抜けていく。\n
戸惑ったような気配を背後に感じながら、それでも振り返ったりはしなかった。"

hide bra_t_03_17


$ hi_mes()

scene charasel_bg_hatter_day
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_long
##endmemory

scene bg_gen_sky_aut_day
with dis

play music map_autumn_jok
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「さて、どこに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に住む友人は何人もいるが、しばらく滞在させてもらうことを考えると……。"

$ routechara = "Deedam"
scene map_gen_bg with fade
$ show_mes("frame_gen_togaki")
T "Where do I want to visit?"
$ hi_mes()
$ renpy.mark_label_seen("fushigi_a")
show screen fushigi_map1
$ ui.interact()
