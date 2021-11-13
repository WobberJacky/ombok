jump fushigi_common2_hatter
label fushigi_pierce2_2:
$ hi_mes()

scene charasel_bg_hatter_day
with stripe_l_medium

scene bm_aut_01_1
with stripe_l_medium

scene br_01
with stripe_l_long

play music hatter_gate_p_ali

scene bg_gen_sky_aut_day
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0364
Dee "「お姉さん、お姉さん！\n
面白い玩具を手に入れたんだ、一緒に遊ぼうよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0365
Dam "「今回のはちょっとすごいよ……、お姉さんも気に入ると思うんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「面白い玩具？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの私室で本を物色していたら、双子が扉からぴょこっと顔を見せる。\n
呼ばれるままに廊下に出ると、がしっと腕を掴まれた。"


scene br_01
with dis

show dee_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0367
Dee "「準備も出来ているから、一緒に行くだけでいいんだ。\n
さあ、行こう、行こう！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちょうど私を挟む形で左右に立った彼らは、今にも手を引いて出掛けようとしている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え、い、今からなの？」"

hide dee_t_01_2
show dee_t_01_2 at left

show dam_t_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice dad_f0368
Dam "「そうだよ。\n
うかうかしていたら、あっという間に時間帯が変わっちゃうでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かにこの世界の時間帯は不規則なのだが……。\n
それにしたって、心の準備というものがある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（それにこの子達のすることだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "びっくり箱のような恐ろしいものが待ち受けている可能性だって、ゼロではない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「そうはいっても……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "渋っていると、通りかかった屋敷の主に声をかけられる。"


show bra_t_01_12 at center
hide dee_t_01_2
hide dam_t_01_7
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0316
Blood "「おまえ達、あまりお嬢さんを困らせるものじゃないぞ」"

hide bra_t_01_12
show bra_t_01_12 at left
show eri_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0175
Elliot "「そうだぜ。\n
[firstname]、嫌なら嫌だってびしっと言っていいんだからな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ブラッド、エリオット。\n
どうしたの、仕事に出ているのかと思っていたわ」"

hide bra_t_01_12
show bra_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice blo_f0317
Blood "「ああ、思ったより簡単に相手が折れてくれてね。\n
私達にとって、有意義な交渉になったよ」"

hide eri_t_01_11
show eri_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice eri_f0176
Elliot "「根性ねえ奴らだったけど、早く片付いたのはよかったよな！\n
次の予定が詰まってるから助かったぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「……そ、そう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（どういう交渉をしたんだか……、聞かないようにしよう）"

hide bra_t_03_10

hide eri_t_02_2
show eri_t_02_2 at left
show dam_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice dad_f0370
Dam "「お姉さんは嫌だなんて言っていないよ！」"

hide eri_t_02_2

hide dam_t_01_8
show dam_t_01_8 at left
show dee_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice dad_f0371
Dee "「そうだよ。\n
僕達と遊んでくれるよね、お姉さん？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「え？\n
ええ……、そうね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "両方からじっと見つめられると、さすがに断り辛い。"

hide dam_t_01_8

hide dee_t_01_1
show dee_t_01_1 at left
show eri_t_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0177
Elliot "「だから、無理することねえって。\n
言って駄目なら、俺がキャンプファイヤーして、マイムマイムしてやるからさ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（それも勘弁してほしいわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子と遊ぶのが嫌だというわけでもないので、口ごもった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "掴まれた両腕は開放されそうにないし、長い斧を振り回す彼らのほうが、私より断然に力がある。"

hide dee_t_01_1

hide eri_t_01_10
show eri_t_01_10 at left
show dam_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0372
Dam "「それにね、今回の玩具は大丈夫だよ。\n
お姉さんの言うところの、安全で、危険のない遊びだもん」"

hide dam_t_02_10
show dam_t_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0373
Dam "「僕達、奮発して新しい玩具を買ってきたんだ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………。\n
本当に、安全なの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ、刃物を始めとする危険な玩具が大好きな彼らのことだ。\n
彼らの基準で「安全」と言われても、非常に怪しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（好かれているのは分かるんだけど……、不安が取り除けないというのも変な話よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ディーやダムが私に危害を加えるとは思っていない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、感覚の違いというものは、長い時間帯をこの世界で過ごした今も完全には取り除けない。"

hide eri_t_01_10
show eri_t_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0178
Elliot "「新しい玩具って……、ああ、あれか。\n
あんまりでかい荷物だから何かと思ったら」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「エリオットも知っているの？」"

hide eri_t_02_7
show eri_t_01_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice eri_f0179
Elliot "「ああ。\n
ガキ共が大荷物抱えていたから、すげえ目立ってたんだよ」"

hide eri_t_01_9

hide dam_t_01_6
show dam_t_01_6 at left
show dee_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice dad_f0374
Dee "「ひよこウサギ、横から口を出してきて、ネタバレしないでよ！」"

hide dam_t_01_6
show dam_t_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice dad_f0375
Dam "「そうだよ、お姉さんの楽しみが半減しちゃうだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「……？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（正体がばれたら、楽しみが半減するようなもの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、大抵の玩具はそういうものだろう。\n
マジックがそうであるように、ネタを知ってしまって楽しめるものは少ない。"

hide dam_t_02_3

hide dee_t_02_3
show dee_t_02_3 at left
show bra_t_03_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0318
Blood "「ふふふ。そうだな……、何ごとも初見のほうが楽しめる。\n
その点だけは、門番の言うとおりだが」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顎に手を当てたブラッドが、上から下へとじっと視線を滑らせて、曖昧に頷く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「何か言いたいようだけど？」"

hide dee_t_02_3
show dee_t_02_3 at left
hide bra_t_03_15
show bra_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice blo_f0319
Blood "「いや。\n
せっかくだから、私も混ざろうかと思ったんだが……」"

hide dee_t_02_3
show dee_t_02_6 at left
hide bra_t_02_2
show bra_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice dad_f0376
Dee "「だめだよ、ボス！」"

hide dee_t_02_6

hide bra_t_02_2
show bra_t_02_2 at left
show dam_t_02_7 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice dad_f0377
Dam "「今は僕達がお姉さんと遊ぶんだから！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「う……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ますます……重い）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（ブラッドは、仕事があるでしょうが）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "わざとからかって煽ってみせる相手を睨む。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子とくっつかれている私の様子に笑みを零しながら、ブラッドは肩を竦めて見せた。"

hide bra_t_02_2
show bra_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0320
Blood "「まあ、あれなら、確かにお嬢さんに危険はない。\n
おまえ達にしては名案だな」"

hide bra_t_03_2

hide dam_t_02_7
show dam_t_02_7 at left
show eri_t_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0180
Elliot "「そうだけどよ……。\n
いいか、おまえら、間違ってもふざけて怪我なんかさせるんじゃねえぞ」"

hide eri_t_01_6
show eri_t_03a_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0181
Elliot "「そんなことしやがったら、あれは没収するからな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "マフィアのＮｏ.２だというのに、エリオットの口調はどう聞いても、悪戯好きな弟に釘を刺すお兄さんといった感じだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここの人達のこういった家族を思わせるやりとりが羨ましくなる。"

hide dam_t_02_7

hide eri_t_03a_7
show eri_t_03a_7 at left
show dee_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0378
Dee "「いちいち、うるさいなあ。\n
エスコートぐらい出来るよね、ねえ、兄弟」"

hide eri_t_03a_7
hide dee_t_03_12
show dee_t_03_12 at left
show dam_t_03_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0379
Dam "「勿論だよ、兄弟。\n
どこかの単細胞ウサギとは違うよね」"

hide dee_t_03_12

hide dam_t_03_13
show dam_t_03_13 at left
show eri_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0182
Elliot "「……おい、何でそこで俺を見ながら言ってるんだ？\n
俺はウサギじゃねえって何度……！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（それに関しては、ディーやダムのほうが正しいと思うけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭ににょっきりと生えた長い耳を見れば、どちらに説得力があるかは一目瞭然だ。"

hide dam_t_03_13

hide eri_t_02_9
show eri_t_02_9 at left
show bra_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0321
Blood "「ふむ、まあいい、好きにしなさい。\n
[firstname]、君も気を付けてな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「？\n
え、ええ……」"

play sound se_0773
hide eri_t_02_9

hide bra_t_01_1

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って廊下を進んでいくブラッド達とは反対に、私は屋敷から連れ出された。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（一体、どんな玩具なのかしら）"

$ hi_mes()

scene b_aut_01
with stripe_l_medium

scene s2_01
with stripe_l_long

play music deedam_t_ali

scene bg_gen_sky_aut_day
with dis
pause .5
play sound se_0133
pause 1
play sound se_0063
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0380
Dee "「よっ、ほい、ははは。\n
どう、兄弟、僕、あの木の天辺まで見てきたよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0381
Dam "「僕だって、うちの屋敷の門まで見えたよ。\n
結構弾むよね、これ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

play sound se_0268
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子は空中でそんな会話を続けているが、私は地面に立ったまま呆然と見上げている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "空中とはいっても、別に滞空しているわけではない。\n
時間帯が滅茶苦茶なこの世界でも、空を飛べるのはどこかの夢魔ぐらいだ。"

play sound se_0268
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らは宙に舞い上がっては、ふわりふわりと下りてきて、また空へと舞い上がっていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋の領土内にある、森の平地。\n
その広い場所に置かれているものには、見覚えがある。"


show t_pia2_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「まさかトランポリンを買ってきていたなんて……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "演目としてならばジョーカーのサーカスでも見ていたが、まさか遊び道具としてこんな大きなトランポリンを買うとは思わなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0382
Dee "「お姉さん、見ているだけなんてつまらないでしょう？\n
一緒に飛ぼうよ！」"

play sound se_0268
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0384
Dam "「高いお金を出した甲斐はあったよね。\n
中古品だったけど、よく弾むや」"

play sound se_0133
pause 1
play sound se_0063
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "再び空中高く飛び上がった彼らはそんなことを言って誘ってくるが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（ブラッド、この状況を察していたわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ついていこうなどと提案してくるはずだ。\n
私の服をじっと見ていたのも、納得する。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「遠慮するわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice dad_f0385
Dee "「えーっ、どうして？\n
これなら危険もないし、怖くもないよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice dad_f0386
Dam "「そうだよ、ほら、僕達がいくら飛んでも大丈夫だよ。\n
大きいし、お姉さんが一緒だって何にも問題なんかないのに」"

play sound se_0133
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らの言うように、トランポリンはちょっとした大きさがある。\n
このサイズなら、私が一緒に混ざっても問題ないのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（別の問題があるでしょうが）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勘のいい彼らが気付いていないはずがない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0387
Dee "「お姉さん、早く、早く！\n
浮く感じって面白いよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0388
Dam "「僕達がうまく飛ばせてあげるから、心配いらないし」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「そういうわけにはいかないわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "トランポリンは、弾みをつけて高く飛ぶ遊具だ。\n
そう、高く飛ぶということは、足下がおろそかになるということで。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0389
Dee "「えー、何で、どうして！？\n
これだけ安全な遊びだったら、お姉さんと一緒に遊べると思って、一生懸命選んだんだよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人の気持ちはありがたいと思う。\n
彼らの遊びとしては、規格外なほど安全だということは、私にも分かっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし……。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0390
Dam "「最初はちょっと高さに慣れないかもしれないけど、怖いことなんてなんにもないよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0390_5
Dam "「危なくなったら、僕達が助けてあげるから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "{size=+20}「飛んだら、見えるでしょうがっ！\n
別の意味で危ないわよっ」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくらなんでも、それはまずい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は姉のような完璧な淑女というわけではないが、それでも最低限の慎みは保ちたい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "特に、見た目は子供でも、ときには大人になったりするような彼らが一緒にいるのでは尚更である。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0391
Dee "「大丈夫だよ、こんなところ、僕達以外誰もいないじゃない。\n
気にしすぎだよ、お姉さん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0392
Dam "「うんうん。\n
一緒にいる僕達はお姉さんと同時に飛ぶから、覗き見したりしないよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "素直に信じられないあたり、私も大分この世界に染まったのかも知れない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（単に疑り深くなっただけだったら、嫌だなあ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice dad_f0393
Dee "「覗くようなこそこそした真似、僕達はしないよね、兄弟」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice dad_f0394
Dam "「そうだよ、僕達は汚い大人と違って、ちゃんと見たいときにはお願いするから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「……あのねえ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（問題点がそもそも違う！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "覗く、覗かない云々ではなく、見えるか否かが問題であって、形はこの際関係ない。"


scene s2_01 with dis
hide t_pia2_1


show dee_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0395
Dee "「ほら、一緒に飛ぼうよ、お姉さん。\n
一度飛ぶと癖になって、止まらなくなって楽しいから」"

hide dee_t_01_2
show dee_t_01_2 at left
show dam_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0396
Dam "「うんうん。\n
飛ぶのも落ちるのも、慣れると楽しいよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「だから、いいってばっ。\n
手を離してよ」"

play sound se_0056
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らは右手と左手をそれぞれ握ってぐいぐいと持ち上げようとする。\n
どうしたらいいのだろうか、頭を抱え込みたくなったときだった。"

play sound se_0046

play music battle_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0161
Pierce "「だ、だめだよ。\n
[firstname]、双子とトランポリンなんて、絶対にだめっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（今の声は……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後の森から聞こえてきた声には、聞き覚えがある。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ピアス？」"

hide dee_t_01_2
show dee_t_02_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice dad_f0397
Dee "「なんだよ、ピアス。\n
僕達がお姉さんと遊ぶのを邪魔する気？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで私を引っ張ろうとしていた手を離して、トランポリンの上でディーが凄む。"

hide dam_t_01_9
show dam_t_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0398
Dam "「そうだよ、ネズミのくせに僕達の邪魔をしようなんて……、生意気」"

play sound se_0084
pause .5
play sound se_0672
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ダムもまた斧を取り出して、軽く素振りまでしている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0162
Pierce "「ぴっ！\n
だ、だって、俺もこの子と遊びたいもん！」"

play sound se_0046
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逃げ腰になっている声を追いかければ、森の中に見慣れた小さな影が見えた。"

hide dam_t_02_13
show dam_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0399
Dam "「よく言うよ、お姉さんを追い出したのはおまえじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0163
Pierce "「追い出してなんかいないよ！」"

hide dee_t_02_13
show dee_t_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0400
Dee "「お姉さんが作ったものをびりびりに破いたのはおまえだろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0164
Pierce "「怒っているなんて思わなかったんだよっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0165
Pierce "「それにそれに、駄目にしちゃったのは、俺だけじゃなくて、オーナーさんもそうだし、ボリスだって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（それはそうなんだけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少なくとも、ボリスは謝る態度を見せていただけましだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ピアスは私が怒っていることさえ気付いていなかったみたいだし）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（それに……）"

play sound se_0046
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「ピアス、何であなたそんな物陰に隠れているの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は先ほどから木々に隠れるように顔だけちょこちょこと出している。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞こえてくる声がピアスなので、間違いはないのだが、森の影が邪魔で姿が見えにくい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0166
Pierce "「だって、森から出たら保護色じゃなくなるし……。\n
二人とも、俺のこと嫌いだから、姿を見せたらやられちゃうと思って」"

hide dee_t_02_3
show dee_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0401
Dee "「そうだね。\n
うざいネズミだし、そろそろこのあたりで斬っちゃったほうがあとくされなくていいかも」"

play sound se_0674
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0167
Pierce "「ぴっ！！\n
やめてよ、俺、喧嘩する気はないんだからっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぎらりと斧を構えるディーに、ピアスが慌てる。"

hide dam_t_03_12
show dam_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0402
Dam "「だったら、どうして出てきたんだよ。\n
せっかく僕達が楽しくお姉さんと遊んでいたのに……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0168
Pierce "「だって……。\n
その子は俺が拾ったんだよ、俺の落とし物なんだよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "物陰にこそこそと隠れたまま、ピアスはじっと私を見ている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0169
Pierce "「ディーやダムと遊ぶよりも、俺と遊ぶはずなのに……。\n
ずるいよっ」"

hide dam_t_02_12
show dam_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0403
Dee "「うるさいネズミだなあ。\n
お姉さんがおまえのものなわけないだろう」"

hide dee_t_01_3
show dee_t_02_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0404
Dee "「だいたい、お姉さんを怒らせたくせに図々しいんだよ」"

play sound se_0672
##special anime kiseki03
pause .5
play sound se_0240
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0170
Pierce "「ぴぎゃっ。\n
危ない、危ないよっ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0171
Pierce "「斧なんか投げないでよっ。\n
俺、掃除は嫌いじゃないけど、危険物の処理はしてないんだからっ」"

hide dam_t_02_12
show dam_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0405
Dam "「当たり前だろ。\n
おまえみたいな、頭の軽いネズミに危険物の処理なんか任せられるはずないじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "斧を投げたディーも大きく頷きながら、続けてくる。"

hide dee_t_02_13
show dee_t_03_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0406
Dee "「お姉さんはおまえのことがもう嫌いなんだって。\n
いつまでもちょろちょろしていないで、さっさと帰れよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0172
Pierce "「え……、ええっ！？\n
[firstname]、君まで俺のこと、嫌いになっちゃったの？」"

menu:
    "嫌ってはいない。":
        jump fushigi_pierce2_3a
    "……好きだと思うけど？":
        jump fushigi_pierce2_3b

label fushigi_pierce2_3a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「別に嫌っているわけじゃないけど……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（一緒にいて疲れることも多いけど、嫌だと思ったことはないもの）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（……怖いと思うことはあるけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "刃物やスコップを持って仕事をしているときのピアスには、近寄りがたいものを感じるが、それは彼に限ったことではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（マフィアなんだもの……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らがマフィアであることも、仕事内容も知っていて、容認している。"


show pia_t_01_12 at center
hide dee_t_03_12

hide dam_t_01_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0173
Pierce "「[firstname]……。\n
そうだよね、君は俺のこと、嫌ったりしないよね！」"

play sound se_0198
##special anime kirakira_center
hide pia_t_01_12
show pia_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0174
Pierce "「俺も君のこと大好き！」"

play sound se_0623
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぱあっと顔を輝かせたピアスはようやく木の陰から姿を見せると、手をあげて近付いてきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし。"

play sound se_0502
$ flash(.1)
hide pia_t_01_2
show pia_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0175
Pierce "「ぴっ！！？\n
な、何でいきなり銃で威嚇してくるのっ」"

hide pia_t_02_6
show pia_t_02_6 at left
show dam_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0407
Dam "「こっち来るなよ、ネズミのくせに。\n
このトランポリン、結構高かったんだから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "珍しく斧ではなく銃を撃ったダムがむっとした顔で言うと、ピアスは大きな目に涙を溜めた。"

hide pia_t_02_6
show pia_t_01_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0176
Pierce "「だって……、俺だって、触りたいよ。\n
その子は俺が拾ったんだよ、なのにどうして双子は俺から取ろうとするの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「いや、別に取られちゃったわけでも何でもないと思うんだけど……」"

jump fushigi_pierce2_4
label fushigi_pierce2_3b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「嫌いと言うよりは、好きだと思うけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（まあ、鈍すぎて、頭に来ることはあるけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつだったか、ピアスは自分には罪悪感がないと話していたことがある。\n
悪いことが分からないのだと。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（……いつもうじうじしている私にとっては、羨ましいとさえ思えるぐらいだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうはなりたいと思わないが、自分にはないものに惹かれるのは私も変わらない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ピアスのこと、私は好きよ」"



hide dam_t_01_4
show dam_t_01_8 at left
hide pia_t_01_8
show pia_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice pie_f0177
Pierce "「[firstname]……。\n
嬉しい、俺、すごい嬉しいよ！」"

play sound se_0198
##special anime kirakira_right
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスはそう言って、泣きそうだった顔に笑顔を浮かべた。\n
罪の意識を持たないネズミの微笑みは、女の子のように可愛らしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（私よりも綺麗に笑うなんて、ずるいと思うけど）"

hide dam_t_01_8

hide pia_t_03_11
show pia_t_03_11 at left

show dee_t_02_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice dad_f0409
Dee "「えー、お姉さん、それはないよっ。\n
僕達、こんなにお姉さんのことが好きなのにっ」"

hide pia_t_03_11

hide dee_t_02_7
show dee_t_02_7 at left
show dam_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice dad_f0410
Dam "「そうだよ、そうだよ。\n
あんなネズミのことなんて放っておいて、ここにいてくれればいいのに」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "縋るようにぴたっと双子が両脇からくっついてくる。\n
ぎゅっと抱き締めてくる腕の力は、遠慮がないせいか、息苦しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り払うことなど最初から考えられない、強い力。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ちょ、ちょっと、二人ともっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（何でそんな力いっぱい抱きついてくるのよっ！？）"

hide dee_t_02_7

hide dam_t_02_9
show dam_t_02_9 at left

show pia_t_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice pie_f0178
Pierce "「あー、駄目！！\n
二人とも、その子は俺のなんだから、ぎゅってしちゃ駄目だってば」"

hide dam_t_02_9

hide pia_t_02_8
show pia_t_02_8 at left
show dee_t_03_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice dad_f0411
Dee "「うるさいな、ネズミのくせに」"

hide pia_t_02_8

hide dee_t_03_8
show dee_t_03_8 at left
show dam_t_03_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice dad_f0412
Dam "「お姉さんを哀しませるようなネズミに、お姉さんはやらないよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスの言葉に二人は冷たく答える。"

jump fushigi_pierce2_4
label fushigi_pierce2_4:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子がピアスをいじめるのはよくあることだ。\n
今回もその延長だと思うのだが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（それにしては、いつもよりも二人の口調がきつい気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "トランポリンで跳ねていたときには、こんなに物騒な気配は感じなかった。\n
何か面白くないことでもあったのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（少なくとも、ここに出てくることについてはブラッドもエリオットも止めなかったから、問題はないはずだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "珍しく、二人がぴりぴりしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、理由は分からなくとも、その気配を感じられるピアスは、一定の距離以上にこちらに近付くことが出来ずに、もじもじしているらしい。"


show pia_t_01_4 at center
hide dee_t_03_8

hide dam_t_03_12
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0179
Pierce "「ううう。\n
怖いよ、怖いよ……」"

hide pia_t_01_4
show pia_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0180
Pierce "「でも、[firstname]……。\n
君がそこにいるのに……」"

hide pia_t_03_8
show pia_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0181
Pierce "「どうして、一緒にいちゃいけないの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "うろうろ、うろうろ。\n
近付こうとしては、後退を繰り返すピアスに、二人は冷たい。"

play sound se_0609 volume .6
camera at hpunch
camera at vpunch
pause .5
play sound se_0609 volume .6
camera at hpunch
camera at vpunch
hide pia_t_01_13


show dee_t_01_8 at left
show dam_t_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0413
Dee "「うざいネズミ。\n
これ以上、この近くをうろうろするなら……、始末しちゃうよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "トランポリンから飛び降りて、二人はきつい視線でピアスを睨んでいる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（怖い……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（けど、何で？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人がピアスをいじめるのは珍しくないが、ここまで敵意を見せているのは、これが初めてだと思う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（何でそこまで怒っているの？）"

hide dee_t_01_8

hide dam_t_01_8


show pia_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice pie_f0182
Pierce "「ぴ……。\n
ぴぎゃああっ！！」"

hide pia_t_02_5
show pia_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Pierce "「[firstname]、[firstname]」"

hide pia_t_01_8
show pia_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice pie_f0183
Pierce "「俺、ま、また来るから！\n
今度は一緒に帰ろうね、[firstname]！！」"

play sound se_0621
hide pia_t_02_8


play music forest1_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_13")
T "「……行っちゃった」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（何がしたかったんだろう、ピアス）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "多分様子を見に来たことは間違いないと思うのだが……、双子に押されて、何も出来ずに終わってしまった。"


show dee_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0415
Dee "「あーあ、せっかくお姉さんと楽しく遊んでいたのに。\n
馬鹿ネズミのせいで、気が削がれちゃったよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「あれはあなた達にも原因があるんじゃないの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（かなり、苛立っていたみたいだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "斧を下ろして不満を訴える双子は、いつもと変わらないように見える。\n
あれほど不機嫌になっていた理由が分からなかった。"

hide dee_t_02_8
show dee_t_02_8 at left

show dam_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0416
Dam "「いいんだよ、ネズミだもの。\n
あれ以上うろうろしていたら、ちょん切っちゃったかもしれないけどね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「ちょん切るって……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これが普通の子供の言葉なら、ただの冗談ですむが、彼らの場合は紛れもなく本気だから怖い。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「家出しているとはいえ、ピアスだって、仲間でしょう。\n
そこまでいじめなくてもいいじゃない」"

hide dee_t_02_8
show dee_t_02_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
Dee "「…………」"

hide dam_t_02_2
show dam_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
Dam "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "取りなすようにそう言ったが、二人は同時に不満そうな顔で私を見た。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……何だか、責められているような気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "無言の圧力には、どうしてそんなことを言うのかと、私に投げかけてくるものがある。"

hide dee_t_02_12
show dee_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0417
Dee "「あんな馬鹿ネズミ、知らないよ。\n
いらないなら、始末しちゃったほうがいいよね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「……ディー？」"

hide dam_t_02_12
show dam_t_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice dad_f0419
Dam "「お姉さんを哀しませるようなネズミだもん。\n
遠慮はいらないよね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ダム？」"

hide dee_t_02_11
show dee_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice dad_f0420
Dee "「ま、いいや。\n
トランポリンはまた次の機会にしよう」"

hide dee_t_01_5
show dee_t_02_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice dad_f0421
Dee "「僕、おなか空いちゃった。\n
屋敷に戻ってご飯にしようよ、お姉さん」"

hide dam_t_01_7
show dam_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice dad_f0422
Dam "「うん。\n
帰ろう、お姉さん」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぎゅっと握った手を引いて、二人は私を連れて屋敷へと戻っていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（二人とも、何をそんなに怒っていたんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の中の疑問は解決されないまま。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "肌を震えさせた二人の空気と、ピアスの後ろ姿が気になって仕方なかった。"

hide dam_t_02_4

hide dee_t_02_5

$ hi_mes()

scene charasel_bg_hatter_day
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_long
##endmemory
jump  fushigi_common3_hatter ##I think
