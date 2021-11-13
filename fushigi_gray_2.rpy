jump fushigi_common2_hatter
label fushigi_gray2_2:

play music minigame_bj_ali

scene map_bg_autumn_night
with stripe_l_medium

scene bg_gen25_ym
with stripe_l_medium

scene bg_gen10_bc
with stripe_l_long
play sound se_0168

show dealer_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hos_f0060
Dealer "「赤の１５。\n
お客様の勝利です、おめでとうございます」"

hide dealer_3


show man_a1_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice oni_f0001
Customer "「ほう……、君はなかなか強運の持ち主だ。\n
連勝続きじゃないか」"

hide man_a1_1
show man_a1_1 at left
show man_d2_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kat_f0032
Customer "「いやいや、偶然でしょう。\n
あなたのように美しい勝利の女神など、私にはいませんから」"

hide man_a1_1
show man_a1_1 at left_center
hide man_d2_2
show man_d2_2 at center

show woman_c1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice nos_f0003
Customer "「ふふふ……。\n
ご謙遜ばかり」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_7")
T "（うわ……。\n
すごい人と、コインの数）"

hide man_a1_1

hide man_d2_2

hide woman_c1_5
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "さすが帽子屋ファミリーのボス所有のカジノだ。\n
街の小さなブロックが収まってしまいそうな程の広さがある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "当の本人に言わせれば、これでも小さいものらしいが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "本で知識は得ていても、実際に立ち入るのは初めての私には、その違いはよく分からない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ちらちらと見た限り、トランプに興じるテーブルだけでも片手の数では足りないくらいある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_2")
T "（これで小規模……？\n
感覚が違いすぎるわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "一体この一夜でどれだけの大金が動くのか。\n
つくづく一般人とは感覚が違う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ここは、私とは別の世界の人がいる場所だ。"


show bra_s_03_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0353
Blood "「ん？どうした、お嬢さん。\n
せっかく来たんだから、何かで遊んでいけばいい」"

hide bra_s_03_16
show bra_s_02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0354
Blood "「君のエスコートなら、喜んで引き受けてあげるよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "親切ぶって言うブラッドは、どう見ても私をからかっているとしか思えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "元々、こんな場違いな場所に私が来る羽目になったのも、この男の気紛れのせいなのだ。"

hide bra_s_02_15

$ hi_mes()

scene bg_gen10_bc_s
with dis

scene br_03_s
with dis

play music hatter_corridor_p_ali

scene br_03
with dis

show bra_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0355
Blood "「そうだ、[firstname]。\n
君もずっと屋敷にいるばかりでは退屈だろう？」"

hide bra_t_01_2
show bra_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0356
Blood "「資金集めと娯楽用に作ったカジノの改装が、ちょうど終わったところでね。\n
一緒に行ってくれる相手を探していたんだ」"

hide bra_t_02_2
show bra_t_02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0357
Blood "「……ぜひ付き合ってほしい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「カジノ？\n
いや……、ちょっとそれはさすがに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「悪いけど、他を当たってよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見た目も、性格的にも、どう考えても私向きの場所じゃない。\n
そう言って断ろうとしたが、彼は首を縦に振らなかった。"

hide bra_t_02_15
show bra_t_03_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0358
Blood "「心配はいらない。\n
私が持っている遊び場の中でも、小規模で、比較的マナーのいいところさ」"

hide bra_t_03_16
show bra_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0359
Blood "「一宿一飯の恩……、とまでは言わないが、付き合ってくれると嬉しい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……いや、だから私は行かないって」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "断りの言葉を重ねるが、それで引いてくれるような生易しい男ではない。"

hide bra_t_03_13
show bra_t_02_18 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0360
Blood "「義理堅い君のことだ。\n
友人にして家主のお願いを断ったりなんて……」"

hide bra_t_02_18
show bra_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0361
Blood "「そんな冷たいことはしないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にやり。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逃げ道を塞ぐように言ったマフィアのボスを相手に、ただの小娘にすぎない私に反論など出来るはずもなかった。"

hide bra_t_02_2

$ hi_mes()

scene bg_gen10_bc_s
with dis

scene bg_gen10_bc_s
with dis

play music minigame_bj_ali

scene bg_gen10_bc
with dis
play sound se_0168
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_3")
T "（私がこんな場所が似合わない中途半端で初心者な女であることは、分かりきっていたことでしょう？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_10")
T "「…………」"


show bra_s_02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_10")
voice blo_f0362
Blood "「……お嬢さん、そんなに睨まないでくれないか。\n
何も私も君にそんな顔をしてほしくて、ここに連れてきたんじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "きつく睨むと、彼は困ったように微笑む。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_03_17")
T "「マフィアのボスなんてお偉い様と違って、私は何しろ世間知らずなもので……。\n
こういう場所って、合わないわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_16")
T "「遊び方も分からないし……。\n
まあ、折角誘ってくれたのに悪いな、とは思うけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ブラッドにとってはちょっとした遊び場程度の感覚なのかもしれないが、生憎私はマフィアではなく一般人だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "お金を賭けて遊ぶなんて、私の性には合わない。"

hide bra_s_02_15
show bra_s_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0363
Blood "「ふむ、そうか。\n
なら、遊び方を教えてあげよう、おいで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "会合時の黒いスーツを着た男はそう言って、私の手を引く。\n
そのまま無理矢理近くのテーブルに座らせた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_5")
T "「ちょ、ちょっと、ブラッド！」"

hide bra_s_01_2
show bra_s_01_2 at left
show dealer_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_5")
voice hos_f0061
Dealer "「おや、ボス！\n
顔をお見せになるとは、珍しい」"

hide dealer_2
show dealer_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_5")
voice hos_f0062
Dealer "「それも、こんな可愛らしいお嬢さんとご一緒とは……」"

hide bra_s_01_2
show bra_s_02_15 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_5")
voice blo_f0364
Blood "「ああ、改装の具合を見るついでに、お嬢さんとデートでね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_4")
T "「デ、デート！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_10")
T "（いつからデートなんてものになったのよ！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ブラッドが横に立っていれば、足を踏みつけてやるところだが、残念ながら彼は私の背後に立っているせいで、届かない。"

hide bra_s_02_15
show bra_s_03_15 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0365
Blood "「ふふふ、このお嬢さんは照れ屋なんだ。\n
分かっているだろうが……、余計なちょっかいは出すなよ？」"

hide dealer_3
show dealer_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice hos_f0063
Dealer "「はい、心得ております」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_10")
T "（勝手に心得るな！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "私の心の声が聞こえない二人は互いに納得した様子で話を終えると、私に向き直った。"

hide bra_s_03_15
show bra_s_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0366
Blood "「ならいい。\n
さて、とりあえず手始めにルーレットを題材に教えてあげよう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_11")
T "（いやいや、それ以前に私はまだ遊びたいとも何とも言っていないから！！）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_6")
T "「題材って、別に私はカジノに詳しくなりたいわけじゃなくて……。\n
遊ぶ気もないんだけど」"

hide bra_s_01_2
show bra_s_02_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_6")
voice blo_f0367
Blood "「そんなことを言うものじゃない。\n
何事も経験だ」"

hide bra_s_02_1
show bra_s_02_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_6")
Blood "「[firstname]」"

play sound se_0262
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_5")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "突然名前を呼ばれて、手の中に冷たい何かを握らされる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_2")
T "「……コイン？」"

hide bra_s_02_5
show bra_s_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_2")
voice blo_f0368
Blood "「君がこの前私に贈ってくれた本のお返しだ。\n
とりあえず、それを賭けてごらん」"

hide bra_s_02_2
show bra_s_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_2")
voice blo_f0369
Blood "「君にあげたものだ、勝ち負けは気にしなくていいから気が楽だろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_10")
T "「……そういう問題じゃないと思うんだけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "勝ち負けではなく、そもそも私がルーレットをすることが前提となっていることに疑問が残るのだが。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "どうやらブラッドは気付いていて無視しているようだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_13")
T "（分かっていたことだけど、あなたって、性格が悪いわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "お人好しのマフィアというのも商売柄いないだろうが、せめて人で遊ぶのはやめてほしい。"

hide bra_s_02_6
show bra_s_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0370
Blood "「ルーレットのルールは簡単だ。\n
ディーラーが投げたボールがどこに入るかを当てるだけ」"

hide bra_s_03_3
show bra_s_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0371
Blood "「色だけでもいいし、ある一定の範囲に賭けてもいい……、意外と、単純だろう？\n
試してみなさい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "やんわりとした口調だが、帽子の下の目は少しも逃がしてくれる気配はない。"

hide dealer_7
show dealer_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
Dealer "「…………」"

play sound se_0358
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ブラッドの視線を受けて、ディーラーは早々にルーレットを回しボールを入れてしまった。"

hide bra_s_03_10
show bra_s_03_15 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0372
Blood "「さあ、何に賭けるんだ、お嬢さん？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_6")
T "（この人が一勝負もせずにテーブルから離してくれるはずもないか）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_12")
T "（とりあえず、何でもいいからさっさと終わらせよう）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_05_15")
T "「分かったわ。\n
じゃあ……、黒の２４に」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "私の手元からコインが離れるや否や、ディーラーの手によって卓上に置かれた。"

hide dealer_9
show dealer_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice hos_f0064
Dealer "「かしこまりました。\n
他のお客様方は……、いかがですか？」"

hide bra_s_03_15

hide dealer_3
show dealer_3 at left
show man_a1_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice oni_f0002
Customer "「では、私は勇敢なお嬢さんに敬意を表して、黒に」"

hide dealer_3
hide man_a1_2
show man_a1_2 at left
show man_d2_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice kat_f0033
Customer "「なら、私は赤に」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_13")
T "（当たるはずがないでしょう。\n
一目賭けなんて……、ビギナーズラックでもあり得ないわ）"

play sound se_0358
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_7")
T "「！」"


show dealer_4 at center
hide man_a1_2
hide man_d2_8
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_7")
voice hos_f0065
Dealer "「おめでとうございます、可愛いお嬢さん。\n
あなたの勝ちですよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "そして、予想以上の大量のコインが目の前に積まれて、私は呆然としたのだった。"

hide dealer_4

$ hi_mes()

$ time_effect()

show dealer_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hos_f0066
Dealer "「今回は、赤の３０。\n
素晴らしい、おめでとうございます。お嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_12")
T "「…………」"

hide dealer_3


show man_a1_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_12")
voice oni_f0003
Customer "「まただ。\n
ここぞというところの勝負強さだな……、負けが続かない」"

hide man_a1_3
show man_a1_3 at left
show woman_c2_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_12")
voice nos_f0004
Customer "「ふふ……、勝利の女神様も、ずいぶん可愛い姿をしていること」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "じゃらじゃらと積まれていくチップを見つめて、私はこの状況に追い込んだ張本人の姿を探していた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_10")
T "（人をこんな場所に放置して……。\n
どこに行ったのよ、あの紅茶マニアはっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "最初にテーブルについてからというのも、私以外の客は次々と入れ替わり立ち替わり、ゲームは続いている。\n
変わらないプレイヤーは私だけ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "こんな状況に追い込んだマフィアのボスは、何やら誰かと話があるということで、さっさと姿を消している。"


show black onlayer master
with dis
hide man_a1_3

hide woman_c2_1

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0373
Blood "「君を一人で置いていくのは忍びないが、少しだけ待っていてくれ。\n
仕事の話が終ったら、すぐ戻ってくる」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0374
Blood "「ああ、手持ちがなくなったら呼んでくれ。\n
君の負け分は、取り戻してやるから」"

hide black

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_1")
T "（ブラッドは手持ちがなくなったらすぐ呼べって言っていたけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "そんな言葉も何処吹く風。\n
私の前に積まれたチップの山はなかなか減らずにいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "とはいえ、全勝しているわけではない。\n
何度か負けてもいるのだが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "どんなに贔屓目に見ても、チップは増えている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "物言いたげにディーラーを睨むと、彼は穏やかに微笑み返してきた。"


show dealer_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice hos_f0067
Dealer "「どうかされましたか、お嬢さん？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_17")
T "「いいえ、別に」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_4")
T "（……イカサマしているわね、あのディーラー）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "それも、時々はわざと負けさせて、周囲の客に不審がらせないようにするだけの余裕付きで。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "それがどれだけの技術なのか、私には想像することも出来ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_4")
T "（さすが、ブラッド所有のカジノ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "働いているディーラーもまともではない。\n
客を一方的に勝たせて問題にならないのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_6")
T "（まあ、主が率先してそう仕向けたんだから、当然と言えば当然だけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_11")
T "（うーん……、でも、いい加減ここから離れたいんだけどなあ）"

hide dealer_7


show man_c2_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_11")
voice oto_f0042
Customer "「彼女は一体誰の連れなんだ？」"

hide man_c2_2
show man_c2_2 at left
show woman_c2_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_11")
voice nos_f0005
Customer "「あら、知らないの？\n
ブラッド様よ」"

hide man_c2_2
show man_c2_2 at left_center
hide woman_c2_8
show woman_c2_8 at center
show man_d1_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_11")
voice kat_f0034
Customer "「ボス自らがここに現れるのも珍しいが、こんなに可愛いお嬢さんを連れてくるのも珍しい」"

hide man_d1_8
show man_d1_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_11")
voice kat_f0035
Customer "「これは、ぜひ、お相手頂かないとな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "一人勝ちしている（ようにしか見えない）私の相手をしようと、テーブルの周りには人だかりが出来ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "順番待ちということらしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_12")
T "「はあ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "何度目ともしれない溜息をついたときだ。"

hide man_c2_2

hide woman_c2_8

hide man_d1_1

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0192
Unknown "「……こんなところで、何をしているんだ、君は」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "聞き慣れた声に思わず振り返ったが、そこにあの黒いコートは見えなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_05_7")
T "「え……、あれ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_2")
T "（今の声は、確かに……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "本来私が生活をしている場所に住む、彼の声だと思ったのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_5")
T "（幻聴？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_05_15")
T "（まさか、ホームシック？\n
いやいや、そういうキャラじゃないでしょう、私）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "気のせいかと思って、再び正面を向こうと身体の向きを直そうとしたが、その前に腕を掴まれた。"

play sound se_0051
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "強い力、私の身体なんて軽々と持ち上げてしまいかねない、男の腕の力。\n
これだけの強さで痛みを覚えないのが不思議なほど。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_8")
T "「きゃっ……！\n
な、何するのっ！」"

play sound se_0424
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "反射的に腕を振り上げて、相手の顔も確かめずに叩いていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0193
Unknown "「つう……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
Unknown "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_7")
T "「！」"


play music gray_t_ali

show t_gre2_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "聞き慣れた声の低さに驚いて、その顔を見上げた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_7")
T "「あ……、グ、グレイなの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_7")
voice gra_f0194
Gray "「ああ、突然引っ張って悪かった。\n
驚かせてしまったな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "口調も、浮かべる表情も、身に纏う紫煙の気配も。\n
首筋に入ったトカゲのタトゥーも、確かに私のよく知っているグレイだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "しかし、今の彼は……、色々違っていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_2")
T "「驚いたには驚いたけど、あなた、その格好は……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_2")
voice gra_f0195
Gray "「俺の格好？\n
……いつものスーツでカジノに来ると目立つから、さすがに変えたんだが……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_2")
voice gra_f0196
Gray "「どこかおかしいだろうか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "いや、おかしくはない。\n
服の色合いにしても、いつも通りの黒で統一されているから、大きな印象は変わらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "いや、今までであれば白いシャツを着ていたが、今の彼はアンダーウエアまで黒一色だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_17")
T "（そういえば、グレイの服って、あれ以外見たことなかったけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "艶のない皮の上着。\n
大きく張り出した襟。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "いつもかっちりと締まっていた首元は、今、シャツの第三ボタンまで開けられているせいで、はだけている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_03_16")
T "（全然、違う）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_18")
T "「髪型まで違ったから、びっくりして……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "そう、服だけでも、いつものグレイとはイメージがまったく違う。\n
今の彼は髪型まで違っていることも原因の一つなのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "大人の姿になったディーのように直接的に髪の長さが変わったわけではないが、その前髪をすべて後ろに流している。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ただそれだけだというのに、酷く……、色っぽい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_7")
T "（……何だか、目のやり場に困るような）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "胸元こそ緩められているが、それにしても下品なほどではない。\n
真っ正面から見るのは何故か気恥ずかしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "それでも、ついちらちらと見上げてしまう。"

hide t_gre2_1
show t_gre2_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
Gray "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "私の反応を訝しく思ったのだろう、グレイが覗き込んでくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "だが、間近でいつもと違う顔が迫ってくると、それだけでまた心臓が騒がしくなってしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_4")
T "「…………っ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_04_7")
T "（グレイはいつもどおりなのに、私だけどうしてこんなに照れるのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "距離を縮めてくる彼のどこを見たらいいのかわからなくて、思わず顔を手で覆った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "衣装と髪型が違うだけ。\n
頭ではそう分かっているのに、過剰な反応が止まらない。"

hide t_gre2_2


show man_a1_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice oni_f0004
Customer "「君は……。\n
まさか、クローバーの塔の」"

hide man_a1_4
show man_a1_4 at left
show gre_d_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0197
Gray "「そうだが。\n
俺に何か用でも？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "さすがクローバーの塔の主を補佐するグレイだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ただでさえ役持ちということで目立つことも手伝ってか、多少の変装ぐらいでは正体は隠し切れないらしい。"

hide man_a1_4

hide gre_d_01_5
show gre_d_01_5 at left
show man_d2_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice kat_f0036
Customer "「我々も彼女とのゲームを待っていたのでね。\n
ここで攫われるのは、割に合わないな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_7")
T "（あ、忘れていた）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "私達がいるのは、ルーレットのすぐ傍だ。\n
そして、私の周りにはイカサマだと知らないギャラリーがたくさん待っていたはず。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_12")
T "（グレイの姿にばかり目が行っていて、忘れていたなんて）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ただ服が変わっただけだというのに、どこまで踊らされているのか。"

hide gre_d_01_5
show gre_d_01_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0198
Gray "「ゲームか。\n
悪いが、彼女には俺との先約がある」"

hide gre_d_01_12
show gre_d_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0199
Gray "「譲ってやる気はない」"

hide man_d2_6


show man_a1_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice oni_f0005
Customer "「いや、そういうわけにはいかないな。\n
仮にも、オーナーが連れてきたお嬢さんだ」"

hide man_a1_3
show man_a1_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice oni_f0006
Customer "「もてなさずに帰すなど、そんな失礼な真似は出来な……」"

hide man_a1_10
show man_a1_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
Customer "「！！？」"

play sound se_0216

play music tension_a_ali
hide gre_d_01_13
show gre_d_01_15 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0200
Gray "「彼女を、おまえ達が、もてなす？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_12")
T "「グレイ……？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_2")
T "（何だか、空気が重くなったような）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "突然空気の密度が変わったかのような、そんな息苦しさ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "その変化を感じているのは私だけではないらしく、私達を取り囲む男達もまた顔色を変えている。"

hide gre_d_01_15
show gre_d_01_15 at left_center
hide man_a1_4
show man_a1_4 at center
show man_c2_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice oto_f0043
Customer "「おまえ……」"

hide gre_d_01_15
show gre_d_01_5 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0201
Gray "「彼女をもてなすには、役者不足のようだ。\n
いいから、とっとと消えろ」"

hide gre_d_01_5
show gre_d_01_2 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0202
Gray "「これ以上くだらねえことを言うのなら、二度とコインが握れねえ身体にしてやるがどうする？」"

hide gre_d_01_2
show gre_d_01_1 at left_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0203
Gray "「ああ、そのほうが余計な役目を感じずにすむから、いいのか」"

play sound se_0125
pause .8
play sound se_0563
$ flash(.3)
hide gre_d_01_1

hide man_a1_4
show man_a1_4 at left_center
hide man_c2_3
show man_c2_3 at center
show man_e2_3 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice kat_f0037
Customer "「ひゃ！」"

hide man_c2_3
show man_c2_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice oto_f0044
Customer "「くっ」"


show gre_d_01_11 at center
hide man_a1_4

hide man_c2_6

hide man_e2_3
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0204
Gray "「……カジノは怪我をする場所じゃねえだろう？\n
さっさと散れ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "抜き手も見せずにナイフを投げたグレイは淡々とそう言った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "この場を制しているのが誰かなのか分からないほど鈍いものはいなかったらしい。"

hide gre_d_01_11


show man_a2_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
Customer "「…………」"

play sound se_0577
hide man_a2_4
show man_a2_4 at left
show man_c1_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice oto_f0045
Customer "「ちっ」"

hide man_a2_4

hide man_c1_6
with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "何か言いたげに、しかし分が悪いことは分かっているのだろう。\n
私を取り巻いていた人影はクモの子を散らすように離れていった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_05_4")
T "「あの、グレイ？」"


show gre_d_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_05_4")
voice gra_f0205
Gray "「ああ、うぜえ。\n
てめえの金勘定にだけ目を光らせていりゃあいいものを……、面倒くせえったらねえ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_16")
T "（グレイ？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_5")
T "（ひょっとして、昔のグレイって……。\n
こういう性格だったのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "彼は昔のことを語りたがらない。\n
たまに聞いてみるのだが思い出すだけでも恥ずかしいと、お茶を濁してばかりだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_15")
T "（グレイは昔の自分を恥ずかしいって言うけど）"


show t_gre2_2 onlayer master
with dis
hide gre_d_01_13

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_15")
voice gra_f0206
Gray "「あ……。\n
すまない、出てしまった」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_15")
voice gra_f0207
Gray "「まいったな。\n
こんな格好をしているせいか、つい……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_17")
T "「気にしないで」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_2")
T "（いつものグレイとは大分違うし、何だか怖いけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_8")
T "「不謹慎かもしれないけど……。\n
格好よかったわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_9")
T "（別の意味で、どきどきする）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_9")
Gray "「？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_9")
voice gra_f0208
Gray "「それはそうと……。\n
君も、色々あって疲れただろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_9")
voice gra_f0209
Gray "「少し、休憩しよう」"

hide t_gre2_2

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music minigame_bj_ali

show bunny_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice oda_f0014
Banny "「お飲み物はいかがですか？」"

hide bunny_1
show bunny_1 at left
show gre_d_01_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0210
Gray "「ああ、もらおう。\n
それと、彼女にもアルコールの入ってないものを」"

hide bunny_1
show bunny_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice oda_f0015
Banny "「では、こちらをどうぞ」"

play sound se_0211
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_18")
T "「あ、ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ウサギの格好をした女の人から差し出されたグラスを手に取る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_2")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_13")
T "（あれは多分作り物かな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "本物の耳を付けたウサギを見慣れているせいか、本物とそうでないものの違いに思わず目が行ってしまう。"

hide bunny_2
show bunny_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice oda_f0016
Banny "「ふふ、それでは、ごゆっくり」"

hide gre_d_01_13
show gre_d_01_13 at center
hide bunny_1
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "優雅な動きで去っていく彼女。\n
だが、その視線が一瞬振り返ってグレイを見たことに気付いてしまった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "グレイは彼女の視線に気付かないのか、無視しているのか。\n
手にしたグラスを傾けて、喉を潤している。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_17")
T "（慣れているわよねえ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "いつものグレイだったら、この空気に浮いてしまっていただろう。\n
よくも悪くも、スーツ姿というのは固いイメージを与えるものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "思わずじっとその横顔を見ていると、突然、金色の目がこちらに向かってきた。"

hide gre_d_01_13
show gre_d_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
Gray "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_16")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_3")
T "（どうして）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ただ名前を呼ばれただけなのに。\n
周囲の人が、どうしてあんな子供にと笑う声さえ聞こえてくるのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_12")
T "（心臓が跳ねて、止まらない）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_7")
T "「あ、あの……。\n
グレイ」"
menu:
    "カジノにはよく来るの？":
        jump fushigi_gray2_3a
    "別人かと思った。":
        jump fushigi_gray2_3b
label fushigi_gray2_3a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_14")
T "「グレイはこういう場所によく来るの？」"

hide gre_d_01_12
show gre_d_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_14")
voice gra_f0211
Gray "「こういう場所？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_15")
T "「そう、こういう……。\n
大人の社交場というか、そういう場所」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ここはブラッドの私有するカジノの一つ。\n
その彼が言ったように、不必要なトラブルが持ち込まれないようにだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ブラッドについてくる形で中に入った私は、大したチェックもなかったが、きちんとした身分証がないと玄関先で追い返されるらしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_18")
T "「グレイがカジノに来るなんて、ちょっと意外だったわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "クローバーの塔での仕事の様子を見ていると、とてもカジノに悠長に遊びに来るような余裕があるとも思えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "だが、少なくとも私よりは慣れている、そう感じた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_5")
T "（来ているんだとしたら、いつ来ているのかしら）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_15")
T "（ナイトメアのお世話だとか、薬の手配だとか、食事の準備だとか、倒れたときの代理業務とかで、休憩が潰れるのも珍しくないのに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_6")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_15")
T "（あ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "その貴重な休憩を、私もこの前一緒に潰してしまったのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_12")
T "（ナイトメアのことばかりを悪くは言えないわね）"

hide gre_d_01_11
show gre_d_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_12")
voice gra_f0212
Gray "「それを言えば、俺だって君がまさかこんな場所に来るとは思わなかったよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_5")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_2")
T "「どういうこと？」"

hide gre_d_01_6
show gre_d_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_2")
voice gra_f0213
Gray "「分かっていないのか？\n
ここは見た目こそ華やかかもしれないが、紛れもない賭博場の一つだぞ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "溜息混じりにグレイが私の名前を呼ぶ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_3")
T "（呆れちゃった？）"

hide gre_d_01_10
show gre_d_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_3")
voice gra_f0214
Gray "「まあ、君に何も問題がなくてよかったが。\n
とりわけマフィアのカジノなんて、ろくなものじゃないんだ」"

hide gre_d_01_13
show gre_d_01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_3")
voice gra_f0215
Gray "「君ぐらいの子に、興味を持つなと言うほうが無理かもしれないが」"

hide gre_d_01_15
show gre_d_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_3")
voice gra_f0215_5
Gray "「カジノに来るのなら、もう少しまともな奴が運営しているところか、もしくは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "一度言葉を切ったグレイは、声を潜めるように屈み込んでくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_5")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_2")
T "（もしくは、何？）"

hide gre_d_01_11
show gre_d_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_2")
voice gra_f0216
Gray "「俺を、近くに置いておいてくれ。\n
湧いて群がる虫は刻んで……、いや弾いてやるから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_03_10")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "耳元で低く囁かれて、ぞくりと背筋が震える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "危険な声。\n
いつもと違う、ラフな空気。\n
それがカジノの騒がしさと混じり合って、私の中に染み込んでくる。"

jump fushigi_gray2_4
label fushigi_gray2_3b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_13")
T "「最初見たときは、別人かと思ったわ」"

hide gre_d_01_3
show gre_d_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_13")
Gray "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_14")
T "「あなたのそういう格好なんて、初めて見たから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "恋人と言ってもいい関係になった今も、なかなかグレイはプライベートを覗かせてくれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "というより、私生活のほとんどを仕事が占めているような状況なので、見る暇がないというべきか。"

hide gre_d_01_14
show gre_d_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0217
Gray "「そういう格好……。\n
俺の服装でどこかおかしいのなら、指摘してもらったほうが……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_4")
T "「う、ううんっ、そうじゃないのっ。\n
ちょっと、今までのグレイとはイメージが違ったから……、驚いちゃっただけで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_10")
T "「それにグレイがカジノに来るなんて意外だったわ。\n
何か用事があったの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "無理矢理話の方向性を変えると、彼は表情を変えて私を見下ろしてくる。"

hide gre_d_01_6
show gre_d_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0218
Gray "「それは俺の台詞だ。\n
こんなところに一人で来るなんて……、危険すぎる」"

hide gre_d_01_5
show gre_d_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0219
Gray "「君は知らないかもしれないが、ここは帽子屋のカジノなんだぞ。\n
あの男のところで、一人で夜遊びなんて……、何かあったらどうするんだ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_7")
T "（……何だ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_1")
T "（見た目が違って驚いたけど、やっぱり……、グレイはグレイだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "説教を始めたグレイは、真剣に私のことを案じてくれているのだろう。\n
面倒見のいい彼らしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_20")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_03_17")
T "（一瞬でもヤキモチ焼いてくれているのかと思ったけど、そんなこと、あるはずがないわよね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_18")
T "「大丈夫よ、だってここに案内したのは他でもないブラッドだもの。\n
今更、あの人が私に何かするとも思えないでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "あっさりと言った私の言葉に、グレイは一瞬で顔を引き締めた。"

hide gre_d_01_13
show gre_d_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
Gray "「…………」"

hide gre_d_01_12
show gre_d_01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0220
Gray "「悪いが、それだけは頷けないな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_5")
T "「？」"

hide gre_d_01_15
show gre_d_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_5")
voice gra_f0221
Gray "「先刻のテーブルについていた君を、一体何人の男が見ていたと思う？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "何人と問われても、私は見られている側だったのだ。\n
数など知るはずもない。"

hide gre_d_01_5
show gre_d_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0222
Gray "「帽子屋の姿は見えなかったが……。\n
君が男共の眼差しの的になるのは、見ていて面白くなかった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_5")
T "（あれ？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_05_7")
T "（まさか……）"

hide gre_d_01_2
show gre_d_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_05_7")
voice gra_f0223
Gray "「君をじっと見つめていいのは、俺だけの特権だろう？\n
それとも、他の奴らの眼差しは心地よかったのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_04_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "脅されているような声音。\n
だが、私の中にあるものは、場違いな高揚感。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_8")
T "「グレイだけよ」"

hide gre_d_01_9
show gre_d_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_8")
Gray "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_1")
T "「こんなにぞくぞくさせてくれるのは、あなただけだもの」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_03_14")
T "（あなたにとって、周りの女の人の視線が意味のないもののように）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "この金の目だけが、私を震わせる。"

jump fushigi_gray2_4
label fushigi_gray2_4:
hide gre_d_01_12 with dis

$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "飲み物を飲み終えて、場内を歩いているとスロットマシーンのあるコーナーに辿り着いた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "物珍しそうに見る私を見て「やってみるか?」と提案してきたのはグレイ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "コインを入れる場所を探すだけで四苦八苦している私とは違い、慣れた様子でコインを入れると機械の明かりが一気に付く。"

play sound se_0249

scene t_cut_gre2_1u
with dis
pause .15

scene t_cut_gre2_1
with dis

show gre_d_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0224
Gray "「あとは、君の好きなタイミングでバーを動かせばいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_18")
T "「分かったわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_14")
T "「えい！」"

play sound se_0305
pause .5
play sound se_0305
pause .5
play sound se_0305
pause .5
play sound se_0248

scene bg_gen10_bc
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_14")
T "「……あ。\n
やっぱり駄目だわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "出た目は、見事な外れ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_12")
T "「うーん。\n
うまくいかないわね」"

hide gre_d_01_4
show gre_d_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_12")
voice gra_f0225
Gray "「こんなものうまくなる必要はないんだが……。\n
そうだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_11")
T "「グレイ？」"

hide gre_d_01_6
show gre_d_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_11")
voice gra_f0226
Gray "「コインを一枚くれるか、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_13")
T "「あ、うん。\n
どうぞ」"

hide gre_d_01_11
show gre_d_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_13")
voice gra_f0227
Gray "「ありがとう」"

hide gre_d_01_3
show gre_d_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_13")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "私の使った台の隣にある機械の前に行くと、グレイは静かにコインを投入した。"

play sound se_0249
hide gre_d_01_12


scene t_cut_gre2_1u
with dis
pause .15

scene t_cut_gre2_1
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "リールが回り始めても、彼は微動だにしない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_5")
T "（……何をするのかしら？）"


show gre_d_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_5")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "バーに伸びていた手が、一瞬の間に何度も上下する。"

play sound se_0305
pause .5
play sound se_0305
pause .5
play sound se_0305
pause .5
play sound se_0248
pause .15
play sound se_0214
hide gre_d_01_12


scene t_cut_gre2_2u
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_2")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_18")
T "「すごい！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_17")
T "（一回で揃えるなんて）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "溢れかえるコインは私の両手では溢れてしまいそうな程だ。"


scene t_cut_gre2_2
with dis

show gre_d_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0228
Gray "「この手の道具は癖があるからな。\n
ある程度見ていれば、勘で何とかなる」"

hide gre_d_01_13
show gre_d_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0229
Gray "「とはいえ、君にはあまりこういうものに慣れてほしくないが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_18")
T "「グレイは慣れているわよね。\n
仕事の息抜きに来たりするの？」"

hide gre_d_01_14
show gre_d_01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_18")
voice gra_f0230
Gray "「いや、ナイトメア様の部下になってからは、あまり来たことはないな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_5")
T "（部下になってからは、と言うことは）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_13")
T "「……昔は、よく来ていた？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ナイトメアの部下になる前。\n
かつて暗殺者の顔をしていたグレイを、私は知らない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "過去は過去。\n
踏みしめてきたそれがあるからこそ、今の彼がいるのだと分かっているから、知りたいと思う。"

hide gre_d_01_15
show gre_d_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0231
Gray "「そうだな、人並み程度には……、な。\n
正直、こういう雑多な雰囲気だけを言えば、嫌いじゃない」"

hide gre_d_01_3
show gre_d_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0232
Gray "「多分、落ち着くんだろうな。\n
いい加減ガキっぽいものは卒業しなければとは思うんだが」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "いつもなら過去の自分に対して言葉を濁すグレイが、今は少しだけ教えてくれる。\n
それは多分、服装や雰囲気だけが原因ではないのだろう。"


scene bg_gen10_bc
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_15")
T "（……こういう場所が、元々似合う人なんだろうな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "壁際に立つグレイに、誰も彼もが視線を送っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ナイトメアがこの場にいたら、大人の女性の秋波が飛び交っているのが見えたことだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_20")
T "（だって、こんなに格好いいんだもの）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_3")
T "（グレイは、こういう大人の場所が似合う）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_5")
T "「そういえば……、煙草、吸わないの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "煙草が、こういう場面には似合うだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "あちこちに煙草を燻らせる男女の姿が見えた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "先ほど引き寄せられたときにも煙の気配を感じたから、持っていないということはないはずだ。"

hide gre_d_01_14
show gre_d_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0233
Gray "「……いや、やめておこう。\n
少し控えているんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_2")
T "「え？」"

hide gre_d_01_13
show gre_d_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_2")
voice gra_f0234
Gray "「気休め程度にもならないだろうが。\n
この前の小火騒ぎ以降、少しだけ……、な」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_5")
T "{size=+20}「具合でも悪いの、グレイ？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "煙草の有害性は彼だって知っていることだろう。\n
だが、そのリスクを知りながらも、彼は自分の意志で吸っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "長い間に培われた習慣だ、健康だけを理由に他人の私が止められるものでもない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "そう思って、ずっと禁煙については言及したことはなかったのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_11")
T "（そのグレイが煙草を控えるなんて）"

hide gre_d_01_11
show gre_d_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_11")
Gray "「…………」"

hide gre_d_01_6
show gre_d_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_11")
voice gra_f0235
Gray "「いや、身体は何ともないんだが。\n
たわいもない願掛けのようなものだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_01_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "疑問を浮かべている私の視線を振り切るように、グレイは話を変えた。"

hide gre_d_01_4
show gre_d_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0236
Gray "「それはそうと、[firstname]。\n
いい加減、塔に戻ってこないか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_7")
T "「あ」"

hide gre_d_01_12
show gre_d_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_7")
voice gra_f0237
Gray "「君一人が責任を感じる必要はない。\n
何よりも俺は……、こんな場所に連れ出すような男のところに、君を預けておきたくないんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "じっと見つめてくる眼差しに、私は答える言葉を持たない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_6")
T "（だって、まだ……、帰れない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "反省すると言い残して出てきた。\n
自分の我が侭で飛び出した私を、彼はこうして追いかけてきてくれたのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_16")
T "（でも……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "帰れない理由は、口に出せるほど確かなものではなくて。\n
その手を拒む資格など、私にはないと分かっていながら動けない。"

hide gre_d_01_9
show gre_t_01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
Gray "「[firstname]？」"

hide gre_t_01_15
show gre_d_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
Gray "「！」"

hide gre_d_01_2
show gre_d_01_2 at left
show bra_s_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0375
Blood "「まだお嬢さんは、帰る気分ではないらしいぞ。\n
残念だったな、トカゲ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "いつから近くにいたのか。\n
スロットマシーンの影から現れたブラッドは、妙に楽しそうな表情を浮かべて私達を見ていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "あの様子から察して、少し前から私達の様子を見ていたことは間違いない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_02_10")
T "（……相変わらず、悪趣味な男）"

hide bra_s_02_2
show bra_s_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_10")
voice blo_f0376
Blood "「ここはカジノだからな、プライベートで現れる分には構わないが……。\n
今、そのお嬢さんを預かっているのは、私だ」"

hide bra_s_02_11
show bra_s_03_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_10")
voice blo_f0377
Blood "「余計なちょっかいをするのなら、それ相応の覚悟があるんだろうな？」"

hide gre_d_01_2

hide bra_s_03_14
show bra_s_03_14 at left
show dealer_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_10")
Dealer "「…………」"

play sound se_0468
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "彼の背後に控えたあのディーラーが無言のまま、近くのスタッフに合図を送る。\n
ぴりっとした一瞬の緊迫感が、周囲の空気を痺れさせた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "だが、それ以上に、続いた声に私の背筋が凍りつく。"

hide bra_s_03_14

hide dealer_9


show gre_d_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0238
Gray "「……帽子屋」"

hide gre_d_01_13
show gre_d_01_5 at left
show bra_s_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0378
Blood "「何だ？トカゲ」"

hide gre_d_01_5
show gre_d_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0239
Gray "「俺の大事な女を預けるんだ。\n
次に一人で放り出すなんてふざけた真似しやがったら、その首切り落とすぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_6")
T "（……怖い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "声まで冷たい。\n
ここまでグレイが敵意を剥き出しにするのを見たのは、ハートの城の騎士以外では初めてだ。"

hide gre_d_01_2

hide bra_s_02_5
show bra_s_02_5 at left
show dealer_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice hos_f0068
Dealer "「……ボス」"

hide bra_s_02_5
show bra_s_03_16 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0379
Blood "「構うな、やめておけ。\n
いくら単身とはいえ、クローバーの塔の優秀な補佐殿だからな」"

hide bra_s_03_16
show bra_s_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0380
Blood "「下手に手を出せば、噛み付かれるぞ？\n
トカゲの中には、毒持ちもいる……」"

hide bra_s_01_3
show bra_s_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0381
Blood "「私は退屈も、面倒も、嫌いだからな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "銃を取り出した男を制止して、それでもブラッドは笑っていた。\n
緊張感がないと取るべきか、それとも余裕と取るべきか。"


show gre_d_01_11 at center
hide bra_s_01_11
hide dealer_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
Gray "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_7")
T "「あ……。\n
は、はいっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "思わず固い声で返事をすると、グレイはいつもの穏やかな口調で告げた。"

hide gre_d_01_11
show gre_d_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0240
Gray "「たまには羽目を外すのも悪くないが、夜遊びはほどほどにしなさい」"

hide gre_d_01_12
show gre_d_01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice gra_f0240_5
Gray "「特に……、{size=+20}手癖の悪いマフィアには、不用意に近付かないように{/size}」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_02_4")
T "「…………」"

hide gre_d_01_15
show gre_d_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_02_4")
voice gra_f0241
Gray "「返事は？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_11")
T "「は、はい……。\n
分かりました」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "思わず背筋をぴんと伸ばして答えてしまった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_6")
T "（声はいつも通りだけど……。\n
目が、少しも笑っていない）"

hide gre_d_01_13
show gre_d_01_13 at left
show bra_s_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_01_6")
voice blo_f0382
Blood "「酷い言われようだ」"

play sound se_0774
hide bra_s_03_13

hide gre_d_01_13
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "心外そうに呟いたブラッドの声を頭から無視して、ようやくグレイは去っていった。"


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "銃を構えたままだったディーラーがそっと主に視線で確認したが、ブラッドは首を横に振っただけだ。"


show bra_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0383
Blood "「ふふふ、君にはずいぶんと保護者がいるな……。\n
塔の芋虫に、城のウサギ」"

hide bra_s_03_10
show bra_s_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0384
Blood "「そして、とりわけ、あのトカゲは群を抜いて君が心配らしい。\n
もっともあの爬虫類は、保護者というには無理があるようだが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_12")
T "「？\n
どういうこと？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "ブラッドが差しているのは、どうやらグレイの話だけではないようだ。\n
先を促したが、彼は曖昧に笑うばかりで応えてくれなかった。"

hide bra_s_02_2
show bra_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_s_06_16")
voice blo_f0385
Blood "「さて、すっかり興が冷めてしまったな。\n
君とのデートの続きは、また次の機会にしよう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_s_06_14")
T "「……次なんて、期待していないんだけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_6")
T "（あ、でも……、ここならまたあのグレイが見られるのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "賭博場は一種の独特の雰囲気だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "その中に、いつもの姿で現れれば……、当然違和感を覚えることだろう。\n
周りの人間だけでなく、本人も。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_s_06_15")
T "（来るかどうかは分からないけど、あのグレイにはもう一回ぐらい会ってみたいかもしれない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "そう思うのは、不謹慎なのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_s_06_16")
T "それでも、今まで知らなかった、手を伸ばせなかった側面を少しでも知ることが出来るのは悪い気分ではなかった。"

hide bra_s_01_11

$ hi_mes()

scene bg_gen25_ym
with stripe_l_medium

scene map_bg_autumn_night
with stripe_l_long

jump fushigi_common3_hatter
