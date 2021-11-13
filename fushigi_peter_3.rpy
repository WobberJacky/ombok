jump fushigi_common3_tower
label fushigi_peter3_1:

scene map_bg_winter_day
with stripe_l_medium

scene charasel_bg_tower_day
with stripe_l_medium

play music tower_inside_p_ali

scene cg_01
with stripe_l_long

show gre_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0044
Gray "「まだ熱が高いな……。\n
薬が効いていないのか？」"

hide gre_t_02_7
show gre_t_02_7 at left
show nai_s_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0108
Nightmare "「あんなにまずそうな薬を飲んで効かないなんて……。\n
うう、可哀想に」"

hide nai_s_02_10
show nai_s_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0109
Nightmare "「いや、やはり自然治癒力に勝るものはないということだな。\n
よって、私も薬は断固断ることにしよう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（あなたの自然治癒力に任せていたら、よくなる前に病院送りになるだけでしょう？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（……というか、よくならずに悪化しそう）"

hide gre_t_02_7

hide nai_s_02_5
show nai_s_02_5 at left
show yuri_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jul_f0022
Julius "「やれやれ。\n
水に濡れた服でうろうろと歩き回ったツケだな」"

hide yuri_t_03_10
show yuri_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice jul_f0023
Julius "「声も出せないぐらいに熱が高いなら、大人しくしていろ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "滞在中、貸し与えてもらった客室。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベッドに横たわった私の周りには、主立った顔ぶれの他に白衣を着た初老の男性がいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアが倒れたときにいつも呼び付けられるというその先生は、今や、一時的に私の主治医となっていた。"

hide nai_s_02_5

hide yuri_t_01_11


show doctor_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0006
Doctor "「恐らく身体を冷やしたのが一番の原因でしょう。\n
肺に炎症も起きかけていて、放っておいたら危ないところでした」"

hide doctor_5
show doctor_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0007
Doctor "「とはいえ、ナイトメア様よりも体力はありそうですから……。\n
これ以上悪くなることはないかと思いますが」"

hide doctor_4
show doctor_4 at left
show nai_s_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0110
Nightmare "「お、おい、何だそれは。\n
まるで私がまったく体力のない病人のようじゃないかっ」"

hide doctor_4

hide nai_s_03_7
show nai_s_03_7 at left
show yuri_t_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0024
Julius "「ようではなく、おまえほど分かりやすい病人はいないだろう。\n
こいつより体力がなくても、いまさら誰も驚かない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（そうね、さすがにナイトメアより体力がないとは思いたくない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あちこちで血を吐く困った病人と一緒にされては、何も出来なくなってしまう。"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "診察道具を鞄にしまった先生は、彼らに何か白い袋を渡した。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おそらく薬だろう、ナイトメアが露骨に嫌そうな顔をしていたので予想がつく。"

hide nai_s_03_7

hide yuri_t_01_13
show yuri_t_01_13 at left
show doctor_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0008
Doctor "「それでは、私はこれで。\n
あと十時間帯ほど経ちましたら、また様子を見に来ますので」"

hide yuri_t_01_13

hide doctor_1
show doctor_1 at left
show gre_t_03_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0045
Gray "「ああ、そうしてくれると助かる。\n
薬はこれだけでいいのか？」"

hide gre_t_03_9
show gre_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0046
Gray "「他に、栄養剤や体力を回復させるものがあれば、与えても構わないだろうか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T "（まずい）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（グレイが本気だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はお母さんモードに入っているようだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心配してくれるのは嬉しいが。\n
彼の場合、その努力が功を奏したことは、こと飲食物について存在しない。"

hide doctor_1
show doctor_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0009
Doctor "「栄養剤ですか……。\n
そうですね、もし本人が欲しがるようなら多少は……」"

hide gre_t_02_3
show gre_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0047
Gray "「そうか。\n
分かった、参考にさせてもらおう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「～～～～！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_6")
T "（いらない、いらないっ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_9")
T "（参考にしなくていいから！！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが今までナイトメアのために作り上げてきた伝説が、頭の中に蘇ってくる。\n
あれを振る舞われるぐらいなら、それこそ入院したほうがいい。"


show nai_s_03_6 at center
hide doctor_5

hide gre_t_03_10
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0111
Nightmare "「君の意見ももっともだが……。\n
私は入院も嫌だぞ、点滴に検査もごめんだ」"

hide nai_s_03_6
show nai_s_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0112
Nightmare "「ああ、思い出しただけで気分が悪くなる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（あんたの気分が悪いのは、いつものことでしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "病人仲間だとでも思っているのか、青白い顔をした夢魔は私の隣で肩を竦めた。"

hide nai_s_03_5
show nai_s_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0113
Nightmare "「あの点滴がずれたときの腫れ上がった腕といい、検査で飲まされる得体のしれない薬といい……」"

hide nai_s_02_9
show nai_s_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0114
Nightmare "「ああ、駄目だ。\n
やっぱりあんな化学物質なんか身体に取り入れるものじゃない」"

hide nai_s_02_10
show nai_s_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0115
Nightmare "「うん、やはり入院をしないことが一番だ。\n
というわけで、私は薬も入院も拒否するぞっ」"

hide nai_s_03_13
show nai_s_03_13 at left
show yuri_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0025
Julius "「……何を一人で先刻からべらべらと喋っているんだ、ナイトメア。\n
病人の傍で騒がしい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呆れたように言うユリウスが、そっとベッドの上から覗き込んでくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここはクローバーの塔であって、彼の領土ではない。\n
だというのに、私が寝込んで以来、ユリウスは部屋によくやってきてくれる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（仕事もあるのに……、ごめんなさい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声が出せればそう言ってあげたい。\n
でも、腫れてしまったのどから漏れるのは呼吸の音ばかりで声にならなかった。"

hide yuri_t_03_10
show yuri_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「？」"

hide yuri_t_02_4
show yuri_t_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0026
Julius "「何か言いたそうだな」"

hide nai_s_03_13
show nai_s_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0116
Nightmare "「ああ、彼女はおまえの仕事の邪魔をして悪いと思っているんだ。\n
だがな、[firstname]、そんな心配はいらんぞ」"

hide nai_s_02_4
show nai_s_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0117
Nightmare "「何しろ、時計屋は先刻から君のことしか考えていないからなあ。\n
先刻だって、この部屋の前でうろうろとしているところを私が声をかけてや……」"

play sound se_0210
hide nai_s_03_1
show nai_s_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0118
Nightmare "「……ぶ！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスが投げたティッシュボックスが勢い良く、ナイトメアの顔に直撃する。"

hide yuri_t_03_4
show yuri_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0027
Julius "「余計なことを言うな、余計なことをっ！\n
……目の前に今にも死にそうな奴がいて、気にならないほど私の神経は太くないだけだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（何だかんだ言っても……、心配してくれているのよね、ユリウス）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "世話をしてくれようと張り切っているグレイとは違った形で、彼は気遣ってくれている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その気持ちが嬉しかった。"

play sound se_0481
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（また、熱が上がってきちゃったかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐらぐらと歪む視界。\n
目を閉じれば、身体がゆっくりと沈み込んでいくような感覚さえ覚えた。"

hide nai_s_03_2
show nai_s_02_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0119
Nightmare "「ああ、眠いなら、眠ったほうがいい。\n
そのほうが早く元気になれるよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（ありがとう）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（おやすみなさい）"

hide nai_s_02_12
show nai_s_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice nig_f0120
Nightmare "「ゆっくり、おやすみ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひんやりとした手が顔に触れて遠ざかっていくのを感じて、私は眠りについた。"

hide nai_s_01_11

hide yuri_t_02_6

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play music dream_tsuduki_a_ali

show t_per3_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ari_f0007
Lorina "「[firstname]、大丈夫？\n
まだ熱が下がらないなんて……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice ari_f0008
Lorina "「もう一度、先生に診てもらいましょうか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「だ、大丈夫よ。\n
それより、姉さんも休んで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「熱は出ているけど、それ以外は何でもないから」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（安っぽい虚勢だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "喉は腫れ上がっていて、声を出すのも辛い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "関節はぎしぎしと錆び付いたように痛むし、起き上がるだけでも体力を使う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鏡で見ればきっと酷い顔をしているに違いないのに、それでも言わずにいられない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（迷惑をかけたくない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然の雨で冷えた身体を放っていたせいで、引いた風邪。\n
自業自得の結果だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（心配をかけて、更に迷惑をかけているなんて、最低）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "姉だって確か約束があったはずだ。\n
心理学の講演会だか何だか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "知り合いに誘ってもらったというそれに行くことを楽しみにしていたはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（もう始まっているわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今からでも間に合うものなら行ってもらいたかったが、もう講演の開始時刻は過ぎてしまっている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0009
Lorina "「そんなに心配しないで。\n
私、これでも体力には自信があるんだから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0010
Lorina "「熱を出した妹の看病ぐらいで、どうこうなるほど弱くはないわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「でも、もし感染ったりしたら……」"

play sound se_0253
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "姉はベッドサイドから私を見ながら、首を横に振る。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0011
Lorina "「もう……。病人なんだから、素直に甘えてくれればいいのに。\n
心配しすぎよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「だって……。\n
もし、姉さんが感染して、こじらせたら……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "脳裏を過ぎったのは、母のこと。\n
床についてあっという間に旅立ってしまった記憶は、簡単には消えない。"

hide t_per3_1
show t_per3_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0012
Lorina "「ふふふ、心配性なんだから。\n
優しい子ね、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（違うわ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（優しいのは、姉さんよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私はただ小さくて、ずるくて、少しもいいところなんてなくて。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0013
Lorina "「心配しないで。\n
私は……」"

hide t_per3_2
show black onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "穏やかに微笑んでいた顔が一瞬にして消えていた。\n
気付けば私が横になっていたベッドも何もかも消えている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「姉さん？」"

hide black


scene yume01
with dis

scene yume02
with dis

play music dream_inside_p_ali

scene yume03
with dis

show nai_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice nig_f0121
Nightmare "「……彼女は、ここにはいないよ、[firstname]。\n
夢だからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「ナイトメア」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "漂うように夢の空間にいる男は、覗き込むように私に顔を近付けてくる。"

hide nai_t_02_1
show nai_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0122
Nightmare "「熱に浮かされていたから心配したよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……ねえ、あれは本当に夢だったの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ただの夢じゃなかったような気がするのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢というよりは、過去の私と……。"

play sound se_0481
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（……つう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭が痛い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "風邪による頭痛がこんなところにも影響しているのかとも思ったが、もっと強い痛みだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（何で、思い出せないの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくら思い出そうとしても思い出せず、苛立ちだけが募っていく。"

hide nai_t_03_10
show nai_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0123
Nightmare "「……[firstname]。\n
無理をしてはいけないよ、君はまだ病人なんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「ナイトメア」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不意にナイトメアに抱きしめられる。\n
ペーターの腕の中とは違うが、安心できる、そう思える場所だ。"

hide nai_t_02_7
show nai_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0124
Nightmare "「もっといいものを見せてあげよう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「もっといいもの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（何よ、それ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それにあの夢だって、決して悪いだけのものではなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "懐かしい。\n
ただ、懐かしさと同じぐらい、胸が痛くなるというだけで。"

hide nai_t_01_11
show nai_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0125
Nightmare "「では……、君がこの前心配していた彼の姿でも見せてあげることにしよう」"

hide nai_t_02_4

play sound se_0337

show white onlayer master
with dis
play sound se_0337
hide white with Dissolve(.1)
play sound se_0337
show white onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "煙管から吸い込んだ煙をナイトメアが吐き出す。
いつもならば儚く散っていくそれが、一つの塊になっていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（え？）"



hide white

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "紫煙はしばらく蠢いていたかと思えば、やがて一つの形になった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「さすが、夢」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（なんてご都合主義）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "煙から鏡が出てくることもそうだが、その面にあちこちの風景が映っている。"


show nai_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0126
Nightmare "「これはハートの城の映像だな。\n
薔薇の庭に、廊下……」"

hide nai_t_03_12
show nai_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0127
Nightmare "「謁見室、資料室……。\n
おや、白ウサギの姿が見つからないな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「自分の部屋かしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "潔癖症のペーターは、外に出ることを好まない。\n
いや、むしろ嫌がる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事で城内を移動していないのであれば、部屋にいる可能性が高い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「いないわね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "映ったギンガムチェックの部屋はがらんどうだった。"

hide nai_t_02_13
show nai_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0128
Nightmare "「うむ、そのようだな。\n
他に白ウサギが行きそうな場所に思い当たりはないか？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ペーターの行きそうな場所）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しばらく首を傾げて……、ふと気が付く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「まさか、私の部屋にいるなんてことはないわよね？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（留守中の人の部屋に入り浸っていたら、ストーカーを超えて、ただの～～～～～～だけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "{size=+20}（ペーターならやりかねない）{/size} "

hide nai_t_01_2
show nai_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice nig_f0129
Nightmare "「どれ、見てみようか」"

hide nai_t_02_12

play sound se_0731

scene hg_01
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice nig_f0130
Nightmare "「……ふ、どうやら外れらしい。\n
君の部屋にもいないようだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「え、ええ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（よかったんだか、悪かったんだか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、ここまで探して見つからないのでは城の中にいないのかもしれない。\n
宰相という地位にあることも手伝って、彼は仕事も多く、その内容も幅広い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本人は嫌がっただろうが、城下の視察にでも出掛けたのだろうか。"

play sound se_0738

scene bg_gen24_dr_m
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（まさか、見送ってくれた場所にいつまでもいないわよね？）"


show nai_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice nig_f0131
Nightmare "「ん？白ウサギの居場所に心当たりがあるのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「心当たりっていうほどじゃないけど、城の入り口のあたりを映せる？」"

hide nai_t_01_2
show nai_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nig_f0132
Nightmare "「ああ、大丈夫だよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアが鏡をもう一度撫でる。\n
すると、巨大な門が映り……。"

hide nai_t_02_1

play sound se_0731

scene hm_spr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あ！」"


show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見間違いようのないギンガムチェックの服が映る。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0133
Nightmare "「ご名答。\n
よくここだと分かったな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……たまたまよ、本当にたまたま」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城を出てくるときに、別れた場所。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（まさか、ずっとここに立っているわけじゃないわよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに待っているように伝えたが、何も一歩も動くなとは言っていない。"

play sound se_0738
hide per_t_02_7


scene yume01
with dis

show nai_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0134
Nightmare "「そうだな……。\n
気になるのなら、聞いてみればいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「無茶を言わないでよ。\n
夢からの声が聞こえるはずがないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（あなたじゃあるまいし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼ならば、あるいは聞こえるかもしれない。心の声を聞く夢魔であれば、多少の不条理さを飛び越えられてもおかしくはないのだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「ペーターに聞こえるはずがないわ」"

hide nai_t_03_10
show nai_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0135
Nightmare "「そうかな。\n
私には彼が君の声に気付かないほうが有り得ないと思うがね」"

hide nai_t_02_11
show nai_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0136
Nightmare "「試しに呼んでみたらどうだ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普通に考えれば有り得ない話だ。\n
いや、そもそも夢の中で誰かと話すという状況そのものがおかしなこと。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（今更まともなことを言っても仕方ないと思うけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

hide nai_t_02_2


scene hm_spr_01
with dis
play sound se_0731
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "平らな鏡面の向こうには、白いウサギがいる。"


show per_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はじっと城の外へと視線を向けているだけだ。\n
背後に兵士の姿も見えるが、彼らに命令を出しに来たという雰囲気ではなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言いつけを守って、待っているように見える。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（聞こえるはずがない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（ペーターがいくらストーカー紛いだって、夢の中でかける声が届くはずがない）"

hide per_t_01_12


scene bg_gen24_dr_m
with dis
play sound se_0738
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鏡面に映る彼の姿から目が離せなかった。"


show nai_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0137
Nightmare "「だが、聞いてほしいと思うんだろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "低く囁く声は、私の胸の内に入り込むことばかり紡ぐ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（だって、私は自分でハートの城を出てきたのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "皆に迷惑をかけてしまった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "反省のために城を出てきたのに、出てきた先でも熱を出して迷惑をかけている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「その上、ペーターに気付いてほしいなんて言ったら、ホームシックみたいじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "身体の不調は気持ちさえも弱くする。\n
折れてはいけない、流されてはいけないと思うのに。"

hide nai_t_02_1
show nai_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0138
Nightmare "「おや、違ったのか？\n
私はてっきりそうだと思っていたんだがね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「な……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「そんなはずがあるわけがないでしょう。\n
そこまで私は子供じゃないわ」"

hide nai_t_01_2
show nai_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_14")
voice nig_f0139
Nightmare "「では、どうして先刻から鏡ばかり見ているんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「そ、それは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悔しいが、ナイトメアの言うとおりだ。\n
私の目は、横に並んだ夢魔ではなく、鏡の中の白ウサギに向いている。"

hide nai_t_02_3
show nai_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0140
Nightmare "「別にからかっているわけじゃないさ。\n
君が彼を恋しく思うのは、当然のこと」"

hide nai_t_01_6
show nai_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0141
Nightmare "「あんな夢を見るぐらいだ。\n
白ウサギを恋しく思うのも、仕方ない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（あんな夢？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが先ほど見ていた姉との夢だと、何となく察してしまう。\n
だが、『あんな夢』とはどういう意味なのだろう。"

hide nai_t_02_2
show nai_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0142
Nightmare "「それはそうと、このまま見ていても仕方ない。\n
騙されたと思って、呼んでみたらどうだ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（呼ぶのはもう前提なのね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_2")
T "「もしそれでペーターが気付いたらどうするの？\n
ここに呼びつけるの？」"

hide nai_t_03_11
show nai_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_2")
voice nig_f0143
Nightmare "「そうだね、それも可能だ。\n
彼は君の呼び出しになら、二つ返事で頷くだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「私、別にそこまで会いたいわけじゃないんだけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、このまま呼ばずに終えるという選択肢は許してもらえそうにない。"

hide nai_t_02_4


scene hm_spr_01
with dis
play sound se_0731
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は意をけっして鏡に顔を寄せ、ペーターに呼びかける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ペーター、聞こえる？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（聞こえるはずがないのに、何をやっているんだろう、私）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "非現実的なこの世界でも出来ることと出来ないことがある。\n
しかし、試してみたくなった。"


show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]？」"

hide per_t_02_3
show per_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0086
Peter "「[firstname]、どこですか、[firstname]！？」"

hide per_t_01_3


scene bg_gen24_dr_m
with dis
play sound se_0738
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え……。\n
ええ！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ほ、本当に聞こえているの？\n
ナイトメアが何かしたとかじゃなくて？」"


show nai_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice nig_f0144
Nightmare "「そんな器用な真似は私にだって出来ないよ。\n
私はただ繋げただけさ。この前のこれと同じだよ」"

play sound se_0603
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは人魚姫の絵本を取り出し私に見せる。"

hide nai_t_01_4
show nai_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0145
Nightmare "「鏡はきっかけにすぎない。\n
私に出来ることなんて、その程度さ」"

hide nai_t_02_7


scene hm_spr_01
with dis
play sound se_0731

show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0087
Peter "「どこですか、[firstname]！？」"

hide per_t_02_3
show per_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0088
Peter "「あなた達、何をぼうっと立っているんです！？\n
彼女の声が聞こえなかったんですか！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまでの静かな姿が嘘のように、鏡の中でペーターは声を上げていた。"

hide per_t_01_7
show per_t_01_7 at left
show heisi_t_02_09 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0008
Soldier "「こ、声ですか？」"

hide per_t_01_7
show per_t_01_7 at left
hide heisi_t_02_09
show heisi_t_02_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0009
Soldier "「いえ、私には特に何も……。\n
おい、おまえは？」"

hide per_t_01_7

hide heisi_t_02_06
show heisi_t_02_06 at left
show heisi_t_01_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0005
Soldier "「いや、私も誰の声も聞こえなかったが……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然の問いかけに兵士が混乱するのも無理はない。\n
声をかけた私自身届くとは思っていなかったのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（……地獄耳？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（それとも、ストーカー魂故かしら）"

hide heisi_t_02_06

hide heisi_t_01_06
show heisi_t_01_06 at left
show per_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice pet_f0089
Peter "「僕の幻聴だと言うんですか？」"

play sound se_0023
hide per_t_02_9
show per_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_8")
voice pet_f0090
Peter "「他のどうでもいい奴の声ならともかく、僕が、愛しい彼女の声を聞き間違えるとでも？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（ちょっと、あんたどうして銃を構えているのよ！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "兵士に銃を突きつけているペーターの目は冷たく光っていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0146
Nightmare "「どうやら、兵士達に疑われたのが気に入らないらしいな。\n
はは、ペーター＝ホワイトらしい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "画面の中の兵士達は、慌てて手を振っている。\n
こんなことでいちいち撃ち殺されては堪ったものではない。"

hide heisi_t_01_06

hide per_t_03_10
show per_t_03_10 at left
show heisi_t_02_09 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0010
Soldier "「ホワイト卿、いえ、けしてそのようなことは……」"

hide per_t_03_10

hide heisi_t_02_09
show heisi_t_02_09 at left
show heisi_t_01_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0006
Soldier "「ただ、そんなにはっきりと聞こえたのでしたら、お姿がもう見えるかと」"


show per_t_01_5 at center
hide heisi_t_02_09
hide heisi_t_01_06
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0091
Peter "「そうです、まだ彼女の姿が見えないなんて……！！\n
どういうことでしょうか」"

hide per_t_01_5
show per_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0092
Peter "「ああ、なるほど。\n
恥ずかしがって、出て来られないんですね、[firstname]」"

hide per_t_01_2
show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0093
Peter "「彼女はとても思慮深くて、遠慮がちで……。\n
きっと近くから僕を見ているはず！」"

hide per_t_02_13
show per_t_02_13 at left
show heisi_t_02_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Soldier "「…………」"

hide per_t_02_13

hide heisi_t_02_02
show heisi_t_02_02 at left
with dis

show heisi_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Soldier "「…………」"

hide heisi_t_02_02

hide heisi_t_01_02


scene bg_gen24_dr_m
with dis
play sound se_0738
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（……一人でなんて痛々しい妄想を膨らませているんだろう、こいつは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もっとも、部下の冷たい視線からいたたまれなさを感じ取れるぐらいなら、ストーカー宣言などしないだろうが。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が城を出てからずっとこの調子だったのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（うわ……。\n
帰ったときに門に立っている皆になんて言えばいいのよ）"


show nai_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
Nightmare "「…………」"

hide nai_t_02_9
show nai_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice nig_f0147
Nightmare "「君が引いていたら、この先私からは何も出来ないんだが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「そういうあなただって引いているでしょうが」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分だけ部外者のようなことは言わないでほしい。\n
元々ナイトメアが繋げなければ、こんなことにはならなかったのだから。"

hide nai_t_01_4
show nai_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0148
Nightmare "「まあ、それは否定しない……。\n
ん？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鏡の中の変化に気付いたナイトメアは、口を閉ざして再び鏡を覗き込んできた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見れば、門の傍に立ったままのペーターが部下に命令をしているところが映っている。"

hide nai_t_01_2


scene hm_spr_01
with dis
play sound se_0731

show per_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0094
Peter "「あなた達、この近くをしらみつぶしに探してきなさい。\n
彼女が見つかるまで戻ることは許しません」"

hide per_t_02_9
show per_t_02_9 at left
show heisi_t_02_09 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0011
Soldier "「え……。\n
見つかるまでですか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターの無茶な命令に兵士は声を上げるが、それが撤回されることはない。"

hide per_t_02_9
show per_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0095
Peter "「捜索に行くんですから当然でしょう。\n
彼女が戻るよりも先に戻ったら、どうなるかは分かっていますよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "真っ赤な瞳。\n
冷徹に輝くそれに睨まれた彼らに拒否権などあるはずがなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "互いに顔を見合わせた兵士にも思うところはあっただろうが、頷くしかない。"

hide per_t_03_10

hide heisi_t_02_09
show heisi_t_02_09 at left
show heisi_t_01_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0007
Soldier "「か、かしこまりました。\n
直ちに捜索に向かいます」"

hide heisi_t_01_06
show heisi_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0008
Soldier "「ただ、ここの警備の引き継ぎをしなければ……」"

hide heisi_t_02_09

hide heisi_t_01_02
show heisi_t_01_02 at left
show per_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0096
Peter "「引き継ぎ？\n
何を悠長なことを言っているんです」"

hide per_t_02_9
show per_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0097
Peter "「さっさと向かいなさい」"

play sound se_0509
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターは時計に手を掛け、銃に変化させる。"

hide heisi_t_01_02

hide per_t_01_1
show per_t_01_1 at left
show heisi_t_02_09 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0012
Soldier "「は、はい。\n
かしこまりました、ホワイト卿」"

play sound se_0312
hide per_t_01_1
show per_t_01_1 at left
hide heisi_t_02_09
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃を向けられそうになって、兵士達は慌てて走り出した。\n
門の前に立っているのは、白いウサギだけだ。"

hide per_t_01_1


scene bg_gen24_dr_m
with dis
play sound se_0738

show nai_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0149
Nightmare "「……呼んであげればいいのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「呼んでもどうにもならないじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここは夢で、私の身体はまだ熱を持っていて、城に戻ることは出来ない。\n
そんな状況で呼び出せば、この前の夢と同じことの繰り返しになるだけだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアとペーターが喧嘩をして、私はもっと寂しくなって……、いいことなし。\n
それならばいっそ会わないほうがいい。"

hide nai_t_03_9
show nai_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0150
Nightmare "「ふむ……。\n
なら、こういうのはどうかな？」"

hide nai_t_03_12
show nai_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0151
Nightmare "「彼を呼ぶことに抵抗があるなら、君が会いに行けばいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「は？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（何を言っているのよ、ナイトメア）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢の中に潜り込めるのは、夢魔である彼だけの能力だ。余所者とは呼ばれているが、特別な力など私にはないことぐらい、彼もよく知っている。"

play sound se_0719
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "疑問の眼差しで見つめると、ナイトメアは人魚姫の表紙を得意げに叩いた。"

hide nai_t_02_4
show nai_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0152
Nightmare "「いや、ちょうど手元のこれを見て思いついた。\n
心のすべてとは言わないが、一部なら届けてあげよう」"

hide nai_t_01_11
show nai_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0153
Nightmare "「君には立派な足もあることだし、彼女よりは楽なはずだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「彼女って……、人魚姫？」"

hide nai_t_01_6
show nai_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nig_f0154
Nightmare "「ああ。\n
君も、彼女が魔女に何を願うのかは知っているだろう？」"

hide nai_t_02_1
show nai_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nig_f0155
Nightmare "「今の君の心情に彼女は近いんじゃないか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "知らないはずがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "海で助けた王子にもう一度会いたいと願った彼女は、その声と引き替えに陸に上がるための足をもらうのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "美しい歌声と引き替えに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（代償に何を言われるか分からないのに、ほいほい乗れるはずがないわよ）"

hide nai_t_03_1
show nai_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice nig_f0156
Nightmare "「おいおい、魔女と私を一緒にしないでくれ。\n
私がそんな酷いことを提案するような夢魔に見えるのか？」"

hide nai_t_03_4
show nai_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice nig_f0157
Nightmare "「本当は身体ごと送ってあげられればいいんだが、まだ治りきっていないのに城に送るわけにも行かないからね」"

hide nai_t_02_7
show nai_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice nig_f0158
Nightmare "「君の一部分を送ってあげよう。\n
君だって、彼をずっとあそこで待ち惚けさせ続けるのは、忍びないだろう？」"

play sound se_0314
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアが私の胸を指先で押すのを黙って見ていた。\n
有無を言わせない雰囲気に飲まれてしまって、動くことが出来ない。"

hide nai_t_02_2
show nai_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0159
Nightmare "「ただし、身体がないからね。\n
白ウサギに声をかけることは出来ても、触ったりは出来ないし、彼からは君の姿も見えない」"

hide nai_t_03_11
show nai_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0160
Nightmare "「そのあたりは、人魚姫と逆だな。\n
声だけは、彼の元に届く形になる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「だったら……、先刻みたいに声をかけるだけでいいじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何も会いに行く必要はない。\n
自分から出ていっておいて、声だけかけるなんて、虫がよすぎる。"

hide nai_t_03_9
show nai_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0161
Nightmare "「ふむ……、なら、理由をあげようか。\n
君がこのまま何もしなければ、戻ってきた兵士達はどうなるかな？」"

hide nai_t_03_1
show nai_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0162
Nightmare "「君の身体はクローバーの塔で眠っている。何も見つけられずに戻ってきたら、ペーター＝ホワイトが彼らに何をするかは、君のほうがよく知っているだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_11")
T "「……あんたね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（まさか、会いに行かせるためにわざとこんなことをしたんじゃないでしょうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "睨みつけてやったがナイトメアは、どこ吹く風と無視を決め込んだ。"

hide nai_t_02_4
show nai_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0163
Nightmare "「この前、言っただろう？\n
望まなければ、何も見えないままだ」"

hide nai_t_02_1
show nai_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0164
Nightmare "「君はもう少し欲を出したほうがいい。\n
会いたい気持ちを、苦いもので上書きする必要はないさ」"

hide nai_t_01_11


show black onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その言葉が終わるや否や。\n
冷たい手が私の瞼を伏せるように覆った。"

play sound se_0051
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ナ、ナイトメア！？」"

play sound se_0670

play music falling1_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "閉ざされた視界が、一気に回転するような感覚が身体に起きる。\n
反射的に身体に込めた力さえ、嘲笑うように強制的に回されていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（き、気持ち悪い……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐるぐる、ぐるぐる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（最初にペーターと落ちた穴みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのときには、直線的に落下していたが、今回は回転が加わっている分、気持ち悪さも増している。\n
悪酔いしそうだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0165
Nightmare "「行ってらっしゃい、[firstname]。\n
白ウサギによろしく」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな夢魔の声だけが楽しそうに聞こえた。"

hide black

$ hi_mes()

scene black
with dis

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music castle_mae_p_ali

scene hm_spr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ん……。\n
こ、ここは……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（本当に、ハートの城にいる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見慣れた城門から少し離れた場所。\n
赤いギンガムチェックの影は、距離がある状態でも見えている。"


show heisi_t_02_06 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0013
Soldier "「おい、誰かいたか？」"

hide heisi_t_02_06
show heisi_t_02_06 at left
show heisi_t_01_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0009
Soldier "「いや、まったく……。\n
どこなんだろうな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（あの人達は、先刻ペーターと一緒にいた……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "木々の向こう側から顔を出した兵士達は互いに顔を合わせて、首を傾げている。"

hide heisi_t_02_06
show heisi_t_02_06 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0014
Soldier "「おかしいな、どこにもいらっしゃらない」"

hide heisi_t_01_04
show heisi_t_01_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0010
Soldier "「だが、このまま帰るわけにもいかない。\n
もう少し続けよう」"

hide heisi_t_01_04
show heisi_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0011
Soldier "「門にはホワイト卿がずっといてくださるから、警備の心配はいらないだろうし」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（！）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（や、やっぱり、ずっと門のところに張り付いていたわけ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が塔に行ってから何時間帯が経過したと思っているのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（確認しないと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "役がなくとも、私にとっては見知った人達だ。\n
声をかけるべく駆け寄った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ねえ、あなた達。\n
ペーターは、ずっとあそこにいたの？」"

hide heisi_t_02_06
show heisi_t_02_06 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice hos_f0015
Soldier "「それにしても、声なんて聞こえなかったけどなあ」"

hide heisi_t_01_02
show heisi_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice oto_f0012
Soldier "「だが、ホワイト卿には聞こえたって言うし」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「……え？」"

play sound se_0623
play sound se_0624
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私に気付いていないのか。\n
無造作に振り向いた兵士と正面衝突しそうになって、思わず顔を手で覆ったのに、私の身体には何の衝撃もない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（確かに身体がぶつかったと思ったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "通り過ぎた彼らの服を掴もうとするが私の手には何も引っかからない。\n
空気を掴むような、そんな空虚感があるだけだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……本当に、見えていないの？」"

hide heisi_t_02_06

hide heisi_t_01_02


scene hm_spr_01_s
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0159
Nightmare "「ただし、身体がないからね。\n
白ウサギに声をかけることは出来ても、触ったりは出来ないし、彼からは君の姿も見えない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0160
Nightmare "「そのあたりは、人魚姫と逆だな。\n
声だけは、彼の元に届く形になる」"


scene hm_spr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（本当に身体がないなんて）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（でも、触れられなくて、声も聞こえないのなら。\n
ペーターだって気付かないんじゃないの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢の中ではナイトメアが出した鏡を通していた。\n
だが、今の私にあの鏡はないのだ。"


show heisi_t_02_06 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0016
Soldier "「だが、見つけないとお怒りになる。\n
何か痕跡だけでも見つけないと」"

play sound se_0183
play sound se_0183
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らは私には見向きもせずに周囲を捜索している。"

hide heisi_t_02_06

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（とりあえず、近くにだけでも行ってみよう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声をかけるか、かけないかはまた別の話。\n
まずは彼の近くまで行ってみないと、何も出来ない。"

$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME

play music castle_mae_p_ali

show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（ペーター）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（やっぱり見えていないのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目の前で手を振ってみても、彼の視線は私に届かないままだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（声、かけてみてもいいのかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほど鏡越しにかけたときと同じように、もしかしたら、ペーターにだけは聞こえるのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それとも、やはり兵士達のように聞こえないままだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（…………）"

menu:
    "声をかける。":
        jump fushigi_peter3_5a
    "声をかけない。":
        jump fushigi_peter3_5b

label fushigi_peter3_5a:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（先刻みたいに聞こえなかったら寂しいけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんな体験は滅多に出来ないだろう。\n
兵士達が未だ捜索を続ける方向を見つめているペーターに小さく声をかけた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ペーター？」"

play sound se_0313
hide per_t_02_7
show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Peter "「！！！？」"

hide per_t_02_3
show per_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice pet_f0098
Peter "「[firstname]……。\n
その声は、あなたですね、[firstname]！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_4")
T "（うそ……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（本当に聞こえた？）"

hide per_t_01_2
show per_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice pet_f0099
Peter "「[firstname]、どこにいるんです？\n
どうして姿を見せてくれないんですか、[firstname]！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「お、落ち着いてよ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "周囲をきょろきょろと見渡すペーターに慌てて声をかけると、彼はまた反応した。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "やはり、彼に私の声が聞こえているのは間違いないらしい。"

hide per_t_01_3
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0100
Peter "「落ち着けるはずがありません！\n
どうして僕の前に姿を見せてくれないんです！？」"

hide per_t_02_6
show per_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0101
Peter "「あなたの声がするのに、あなたに会えないなんて……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（やっぱり、声をかけないほうがよかったのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "哀しげに俯いたペーターの顔を見ていると、失敗してしまったような気持ちになってくる。"

hide per_t_01_13
show per_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0102
Peter "「まさか、あの頭の弱いネズミのおかしな薬で見えないぐらい小さくなってしまったんですか！？それとも、透明人間になるような薬でも……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「だ、だから落ち着いてってば！\n
何か変なものを飲まされたとか、そういう理由じゃないから！」"

hide per_t_01_5
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice pet_f0103
Peter "「では、どうしてあなたの姿が見えないんです！？\n
あなたが帰ってきてくれたと思ったのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「それは……、その……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（ナイトメアが意識だけ飛ばしたなんて言ったら、絶対に理由を聞いてくるわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、熱が出て動けないとなれば、次に彼がとる行動は一つだ。\n
何が何でもクローバーの塔に押しかけて、私を連れ帰ると言うに決まっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（雑菌だらけだから風邪をひくんだとか、そういうわけの分からない言い掛かりをつけるのが目に浮かぶ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただでさえ寝込んで、塔の皆に迷惑を掛けてばかりいる。\n
これ以上トラブルの元を招くわけにはいかない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……ペーターがどうしているか気になっていたから、来ることが出来たんじゃないかしら。\n
た、多分だけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この前の私の夢に現れた彼と同じようなことを言って誤魔化した。"

hide per_t_02_6
show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0104
Peter "「[firstname]……。\n
あなたがそこまで僕を思ってくれたなんて！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じんと感動したように目を閉じているペーターには、私の嘘が分からないようだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここまで喜んでいる様子を見ると、さすがに良心がちくちくと痛むが、本当のことを言うよりはいいだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（これ以上、グレイ達に迷惑をかけるわけにはいかないものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし感極まった声を上げていたはずのペーターの顔が、突然曇った。\n
見えない私の姿を何とか見出そうとするように視線を彷徨わせて言う。"

hide per_t_02_13
show per_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0105
Peter "「でも……、これでは寂しいです」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「寂しい？」"

hide per_t_03_5
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pet_f0106
Peter "「だって、あなたの顔も見えないなんて……。\n
僕は、僕は……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しゅんと耳を垂らして項垂れるペーターの赤い目は、私を捜すように動いてばかりだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（やっぱり、声をかけないほうがよかったんじゃ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ち込んだ様子で肩を落としているペーターを見ていると、後悔ばかりが込み上げる。"

hide per_t_02_6
show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0107
Peter "「[firstname]……、あなたには、僕が見えているんですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「ええ。\n
あなたの右側にいるわ」"

hide per_t_02_3
show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Peter "「…………」"

hide per_t_02_10
show per_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice pet_f0108
Peter "「このあたりですか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターの紅い瞳が動くが、その視線と私のそれが噛み合わない。\n
まるで行き場を求めるように手が動いている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（触れないのは分かっているけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「そこで、手を止めて」"

hide per_t_03_3
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice pet_f0109
Peter "「はい」"


play music truth_a_ali
show t_per3_3a onlayer master
with dis
hide per_t_02_8

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見えないものに触れようとするのは至難の業でも。\n
私から彼の手に触れることは出来る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何も言わずに私はペーターと手を重ねた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（やっぱり、感触は何もないけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（ペーターに分かるかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隣にいる。\n
手を重ねている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "体温も、肌の感触も何も伝わらない。\n
それなのに、視線が合う。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「見えるの？\n
それとも、ペーターには触れるの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の手には何も伝わってこないままだが、彼には何か分かるのだろうか。"

hide t_per3_3a


show per_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0110
Peter "「いいえ。\n
でも……、分かる気がします」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで行き場もなく彷徨っていた目が、私を見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い瞳に私の姿は映っていない。\n
だが、見てくれているような、そんな気がした。"

hide per_t_01_2
show per_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0111
Peter "「あなたがここにいるのが、分かります」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「ペーター……」"


show t_per3_4a onlayer master
with dis
hide per_t_02_12

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice pet_f0112
Peter "「そして、ここがあなたの唇でしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "{size=+20}「！！！？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_7")
T "「な……、何で分かるのよ！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（本当に見えていないの！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターの指はぴったりと私の唇の位置を当てている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0113
Peter "「だって、僕はあなたのことを誰よりも知っていますから。\n
その位置も、甘さも、全部」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0114
Peter "「見えなくても、触れなくても。\n
分からないほうがおかしいでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「…………」"

hide t_per3_4a
show t_per3_5a onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "触れないと分かっているのに、白ウサギはそっと唇を寄せて重ねてきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手と同じ。\n
どれほど近付いても、触れ合わせても、彼の感触はどこにも感じられない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（それなのに、どうして、こんなに気持ちがいいんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "幻のキス。\n
本当に触れ合っているかどうかも分からないのに。\n
重なったと感じられる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice pet_f0115
Peter "「……これが誰の仕業かは、聞きません。\n
ですが、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice pet_f0116
Peter "「僕は早くあなたに会いたいんです。\n
だから、早く戻ってきてくれませんか？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice pet_f0117
Peter "「もっと、あなたを抱き締めたい。\n
ずっと、あなたに、キスがしたいんです」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（負けたわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これだけ真摯に求められて、何が言えるだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きっと今の私に身体があったら、風邪以外の理由で真っ赤になっているに違いない。"

hide t_per3_5a

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……なるべく早めに帰るようにするけど。\n
あんたも、ここじゃなくて、ちゃんと自分の部屋で待っていなさいよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "照れ隠しから素気なく言った私の言葉に、ペーターは耳を立てた。"


show per_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0118
Peter "「ええ！？\n
だってここなら一番にあなたに会えるじゃないですか！」"

hide per_t_01_5
show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0119
Peter "「この城の誰よりも早く僕はあなたに『お帰りなさい』って言いたいんです！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_14")
T "「……順番なんてどうでもいいじゃない。\n
それにここにだって門番役の兵士さんがいるでしょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「どっちにしても、変わらないわよ」"

hide per_t_02_7
show per_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_13")
voice pet_f0120
Peter "「いいえ、それでしたら、あなたが帰るまで、僕が彼らの代わりに門番をすればいい話です」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「あんたは宰相でしょう！？\n
いつから門番になったのよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（まったく、テンションがころころ変わるんだから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまでのしっとりとした雰囲気でずっといてくれれば、私ももう少し対応を変えられたかもしれないのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（まあ、静かなペーターなんて、ペーターじゃないか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "騒々しくて、潔癖症で、ひとの話を聞かなくて。\n
いつだって、私を一番に思ってくれる、白いウサギ。"

hide per_t_02_11
show per_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0121
Peter "「だって、僕とあなたの感動の再会ですよ！？\n
他の余計な輩なんて、いらないじゃないですかっ」"

hide per_t_03_3
show per_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0122
Peter "「いえ、むしろ感動の邪魔になるぐらいだったら……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「あっちで探している人達を含めて無闇に撃ったりしたら、帰るのを遅らせるからね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い瞳に危険な色が宿ったのを感じて、先に釘を刺しておく。"

hide per_t_03_9
show per_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_02_4
show per_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0123
Peter "「何ででしょう。\n
見えないのに、あなたが僕を睨んでいるような気がします」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「気だけじゃなくて、事実よ。\n
睨んでいるの」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（見えないのに、そういうのは雰囲気で伝わるのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "感情の変化が伝わるほど、私は分かりやすいのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見えないことをいいことに、身体を少しだけ動かす。"


show t_per3_6a onlayer master
with dis
hide per_t_03_5

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "真っ正面から、横へ回り込む。\n
そのまま少し背伸びをして、頬に唇を当てた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キスというには余りに淡い。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（これが分かったらすごいけど、分からないわよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声も出していない。\n
ただ、少しだけ触れさせただけだ。"

hide t_per3_6a


show per_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「……[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「なに？」"

hide per_t_01_11
show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pet_f0124
Peter "「今、僕に何かしましたか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「何かって……、たとえばどんな？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（本当に、分かったの！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が動いたせいで目線はずれている。\n
だが、彼は何故かとても嬉しそうな顔で頷いた。"

hide per_t_02_3
show per_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0125
Peter "「ええ。\n
あなたの匂いがすぐ近くでしたような気がして」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！」"

hide per_t_03_11
show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice pet_f0126
Peter "「犬ではないですが、ウサギもけっこう鼻が利くんです。\n
あなたの甘い香りには、特に敏感ですから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「……気のせいよ、気のせい！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見えないのに身体を急に離して、距離をとる。\n
なのに、無意識に彼の視線の前に立つように移動してしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い城の前に立つ、白いウサギ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（見送ってくれたときと同じ位置）"

hide per_t_02_5
show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Peter "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……もうすぐ帰るから。\n
ハートの城で待っていてね、ペーター」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（約束を守るためだけじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が帰る場所には、間違えようのない目印がある。"

hide per_t_02_3
show per_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_01_13
show per_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0127
Peter "「ええ、分かっています」"

hide per_t_01_10
show per_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0128
Peter "「僕は、ずっといつまでも、あなただけを待っています。\n
あなたが望む場所で、ずっと」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見えないはずなのに。\n
その赤い瞳に、私が映ったような気がした。"

hide per_t_02_12

$ hi_mes()
play sound se_0731

play music dream_inside_p_ali

scene yume01
with dis

scene yume02
with dis

scene yume03
with dis

show nai_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0166
Nightmare "「お帰り、[firstname]。\n
どうだった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「どうせ、見ていたんでしょう？\n
確認しなくてもいいじゃない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（嫌味にしか聞こえないわよ）"

hide nai_t_02_1
show nai_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice nig_f0167
Nightmare "「見てはいたが、聞き耳までは立てなかったよ。\n
さすがにそこまでしたら、君に恨まれそうだからね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "色白の手が本を捲る。\n
開いたページには、相変わらず何が書かれているのか分からない文字が並んでいた。"

hide nai_t_03_11
show nai_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0168
Nightmare "「姿と引き替えに出会った王子様はどうだった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「いつもどおりよ。\n
いつもどおりで、変わらなかった」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（待っていてくれた）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自己満足の我が侭を通した私を、彼はあの場所で待っていてくれた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが分かって、安堵する気持ちもあるが、わざわざ言うまでもないだろう。\n
彼には私の感情なんて、文字どおり手に取るように分かるのだから。"

hide nai_t_02_2
show nai_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0169
Nightmare "「それは何よりだ。\n
変わることばかりがいいこととは限らないからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（どこまでばれていたの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞いてみたいが、返ってくる答えを聞くのは何だかむかむかする。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「そうだわ。\n
ナイトメア、起きたらあの先生をもう一回呼んでくれない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思い出したように言った私を、ナイトメアは不思議そうに見た。"

hide nai_t_01_6
show nai_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nig_f0170
Nightmare "「あの医者をか？\n
どうして？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「決まっているじゃない。\n
いつまでも動物を待ち惚けさせるわけにはいかないから、点滴でもしてもらおうかと思って」"

play sound se_0042
hide nai_t_01_2


show nai_t_02_10 at center
with dis

show gaaan1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice nig_f0171
Nightmare "「な、なに！？\n
点滴だと！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言葉に彼は悲鳴にも近い声を上げた。"

hide gaaan1

hide nai_t_02_10
show nai_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0172
Nightmare "「待て、早まるな、[firstname]。\n
それは最後の手段というやつであって……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（何もあなたがやるわけじゃないでしょうに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただでさえ白い顔色が更に真っ青になっていた。"

play sound se_0433
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「そうね、せっかくだもの。\n
一緒に点滴してもらいましょうか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「あなたも私と一緒なら耐えられるでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（グレイやここの人達も、そういうことなら喜んで協力してくれそうだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "我が侭で巻き込んでしまったお詫びになるかは分からないが、ナイトメアの少しは体調が回復すれば、塔にとってもプラスになるだろう。"

hide nai_t_03_7
show nai_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0173
Nightmare "「じょ、冗談じゃない！！\n
誰がそんな恐ろしいことを」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「まあまあ、そう言わずに……。\n
男なら付き合いなさい」"

hide nai_t_03_3
show nai_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice nig_f0174
Nightmare "「[firstname]、そういう台詞はもっと別の状況で使われるべきであってだな！」"

hide nai_t_02_5
show nai_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice nig_f0174_5
Nightmare "「嫌だぞ、私は絶対に点滴なんかしないからな！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぎゃーぎゃーと騒ぐ夢魔の声を聞き流し、治療プランを考えながら、私は目を閉じた。"

hide nai_t_02_6

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（もうすぐ帰るわよ、ペーター）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呼びかけても、声は届かないと知っていても。\n
彼の答えを私はもうもらっている。"

$ hi_mes()

scene yume03
with dis

scene yume02
with dis

scene yume01
with dis
##endmemory
jump fushigi_end_check_castle1_p
label fushigi_peter3_5b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（声をかけて、気付いてもらえなかったらどうするの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの兵士には、私の声はまったく届いていなかった。\n
姿が見えなくなっていることは、彼らの反応からも確かだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"


show per_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターは私の存在に気付いていないのだろう、じっと誰もいない虚空を見ているだけだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（わざわざ声をかける必要なんてないわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見えない、触れられない。\n
そんな中で声をかけたところで、空しいだけだ。"

hide per_t_01_8


show t_per3_3b onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "立ったままのペーターの背中に寄り添うように立つ。\n
それでも、何の感触もない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もたれ掛かるように少し身体を傾けたが、それでも何の手応えもなかった。"

play sound se_0474
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（時計の音が聞こえるぐらい近くにいるのに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（触れないなんて……。\n
変な感じ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この音が聞こえるときには、私はいつも白いウサギに触れていたのに。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0129
Peter "「[firstname]……。\n
どこにいるんですか？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（ここにいるわよ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（あなたには見えないし、聞こえないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "胸の中で小さく声を作っても、届かない。\n
だが口にして聞こえなかったらと思うと、何も出来ない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（帰ろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "このまま近くにいたら、誘惑に負けてしまいそうだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_3")
T "（そのくせ、気付いてもらえなかったら、勝手に傷つくに決まっている）"


hide t_per3_3b

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気持ちを振り切るようにペーターの背中から離れて、位置を変える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私ではなく、城の前に広がる道を見続けているその整った顔を確かめるように、彼の前へと回り込んだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（久しぶりに近くで顔が見られたし、それでいいわ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice nig_f0175
Nightmare "「おや、本当に声をかけなくていいのか？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……いいのよ。\n
早く、帰して）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私はおとぎ話の人魚ではないのだから。\n
戻ってからゆっくり話せばいい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "溜息にも似た気配を感じた直後、また視界が歪んだ。\n
先ほどとは逆に、現実から夢の中に引き戻される感覚だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_4")
T "（じゃあね、ペーター）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声をかけずに小さく手を振ると、白い影が動いた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（え？）"


show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
Peter "「…………？」"

hide per_t_02_3
show per_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pet_f0130
Peter "「[firstname]？\n
[firstname]、そこにいるんですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（声なんか出していないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚く間にも別の場所に私は引き寄せられていて……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「……ペーター？」"

hide per_t_03_3

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（どうして気付けたの？）"

play sound se_0731
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後に呟いた彼の名前。\n
それが聞こえたのかどうかを確かめるよりも前に、私の意識は夢の中に戻っていった。"


play music dream_inside_p_ali

scene yume01
with dis

scene yume02
with dis

scene yume03
with dis

show nai_s_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nig_f0176
Nightmare "「……どうして、話しかけてやらなかったんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「いいじゃない、別に。\n
そういう気持ちにならなかっただけよ」"

hide nai_s_02_8
show nai_s_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本を手にしたナイトメアはどこか哀しそうな顔をしているように見えた。"

hide nai_s_02_7
show nai_s_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0177
Nightmare "「誰よりも君を望んでいる白ウサギに、君の声が聞こえないはずがないだろう」"

hide nai_s_03_9
show nai_s_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

hide nai_s_03_12
show nai_s_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0178
Nightmare "「もっと欲張ればいいのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「……分不相応なことを願えば、自滅するだけよ。\n
童話の中でもよくある話じゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すぎた欲が身を滅ぼすというのは、使い古された展開だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（人魚姫も、幸せな海の世界で満足していればあんな結末にならずにすんだかもしれないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢魔が手にした本の主人公は、どんな思いであの選択をしたのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（私には、分からない）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「私は別に聖人君子っていうわけじゃないわよ。\n
欲しいときには、ちゃんとそう言っているわ」"

hide nai_s_02_7
show nai_s_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0179
Nightmare "「そうだね。\n
そういうところは、彼によく似ているよ」"

hide nai_s_01_4
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0180
Nightmare "「君達は、だからこそ幸せでいてほしいんだがね」"

play sound se_0721
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本が閉じる音を耳にしたとき、不思議な夢は終わった。"

hide nai_s_02_1

$ hi_mes()

scene yume03
with dis

scene yume02
with dis

scene yume01
with dis
##endmemory

jump fushigi_end_mermaid1
label fushigi_end_check_castle1_p:

if renpy.seen_label("fushigi_end_vivaldi1") == True:
    jump fushigi_end_check_castle2_p
if renpy.seen_label("fushigi_end_peter1") == True:
    jump fushigi_end_check_castle2_p
if renpy.seen_label("fushigi_end_ace1") == True:
    jump fushigi_end_check_castle2_p
else:
    jump fushigi_end_peter1
label fushigi_end_check_castle2_p:
if fushigi_common3_tower2_peter2b_seen == True:
    jump fushigi_end_peter1
else:
    jump fushigi_end_castle1
