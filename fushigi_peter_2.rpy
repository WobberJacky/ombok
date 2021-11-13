jump fushigi_common2_tower
label fushigi_peter2_2:

scene map_bg_winter_day
with stripe_l_medium

scene charasel_bg_tower_day
with stripe_l_medium

play music tower_inside_p_ali

scene cg_01
with stripe_l_long
play sound se_0300
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ、はい。\n
どなた？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gra_f0028
Gray "「ああ、[firstname]。\n
俺だ、少しいいだろうか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「……グレイ？」"

play sound se_0282
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドア越しに聞こえた声に驚きながら扉を開くと、そこには予想通りの長身の男性が待っていた。"

$ hi_mes()

play music tower_corridor_p_ali

scene cr_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「どうしたの、突然。\n
何か、用でも？」"


show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gra_f0029
Gray "「用という程じゃないんだが……。\n
ナイトメア様から君を呼んでくるようにと言われて、迎えに来たんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「ナイトメアが？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（特に何も約束していなかったわよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔の一室を借りて生活をし始め、数時間帯が経っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は客人として滞在し、その間、塔の主であるナイトメアとも何度か顔を合わせていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「この前会ったときは、特に何も言っていなかったけど……。\n
呼んでいるなら、会いに行くわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「特に用事もないし……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "客人として滞在しているので、仕事もない。\n
暇を持て余しているといってもいい状況だ。"

hide gre_t_03_10
show gre_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0030
Gray "「すまないな。ナイトメア様はご自分の部屋にいらっしゃる。\n
そこまでは俺も付いていこう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「ありがとう」"

hide gre_t_02_11

$ hi_mes()

scene charasel_bg_tower_day
with stripe_l_medium

play music tower_stairs_up_p_ali

scene n_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの部屋は、いつでも書類の匂いがする。\n
とは言っても、落ち着いた図書館のような雰囲気があるというわけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むしろ、雑然と書類が積まれ、今にも雪崩を起こしそうなその様子は真逆だろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、今クローバーの塔の領主の部屋は、かつてないほど様変わりしていた。"


scene t_cut_per2_1u
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「グレイ。\n
これ、どういうこと？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gra_f0031
Gray "「いや、俺が君を呼びに行ったときには、こんなことにはなっていなかったんだが」"


scene t_cut_per2_1
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアを抜けて、中に入った途端、私達は足を止めずにはいられなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（この部屋にこんなに本があることも意外だけど……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（それにしても、多すぎない、これは？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の身長ほどに積み上げられた本の山は、一つや二つではない。\n
部屋全体を埋め尽くすように広がりを見せている。"


show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0039
Nightmare "「ああ、待っていたよ、[firstname]。\n
いらっしゃい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "Nightmare."

hide nai_s_01_11
show nai_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nig_f0040
Nightmare "「ふっ……、どうだ。\n
なかなか圧巻だろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「圧巻だけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "{size=+20}「とりあえず、宙に浮きながら煙草を吸うのはやめて」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（灰が落ちて、本が焦げたらどうするのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あろうことか、ナイトメアは煙管を口にくわえながら、浮いている。\n
浮くのは勝手だが、万が一、この本に火でも付いたら大火事になりかねない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（そして、火事になったら間違いなく煙を吸って動けなくなるタイプよね、この人って）"

hide nai_s_02_3
show nai_s_02_3 at left
show gre_t_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice gra_f0032
Gray "「そうですよ、ナイトメア様。\n
それにこの大量の本はどうしたんですか」"

hide nai_s_02_3
show nai_s_03_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice nig_f0041
Nightmare "「ああ、これか。\n
この前頼んでおいたものが一気に届いてな」"

hide nai_s_03_12
show nai_s_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice nig_f0042
Nightmare "「君にあげようと思ったんだ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「私に？」"

hide nai_s_03_11
show nai_s_02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice nig_f0043
Nightmare "「そうだよ。\n
部屋にこもるにしても、読み物があったほうがまだ手慰めにはいいだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（気付いていたの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔に居候してから、私はほとんど出掛けていない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、塔の中で何かの役目に就いているわけでもない私は、やることもなく部屋でぼうっとしていたのだが。"

hide nai_s_02_2
show nai_s_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0044
Nightmare "「君の趣味に合うかどうかは分からないが、好きなものを選んでくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（ごめんね、気を遣わせちゃって）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "胸の中で言葉を作って謝ると、彼は何でもないように頷いて見せた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まるで本の海のような室内を動きながらグレイは首を振っている。"

hide gre_t_03_11
show gre_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0033
Gray "「とはいえ、すごい量ですね。\n
これすべてを、ナイトメア様がお選びになったんですか？」"

hide nai_s_01_1
show nai_s_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0045
Nightmare "「まあな。\n
ふふん、どうだ、最近の流行の本ぐらい、私はきちっと把握しているんだ」"

hide nai_s_02_4
show nai_s_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0046
Nightmare "「素晴らしいだろう！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（そこで調子に乗るから、いつも失敗するのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "黙っていれば静かな感謝と賞賛が向けられるはずなのに、台無しにしてしまうのは彼の性格によるものだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「それじゃあ早速……」"

play sound se_0603
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手近にあった一冊をとって、ぱらぱらと捲って……。"

play sound se_0718
pause .4
play sound se_0718
pause .4
play sound se_0721
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何も言わずに閉じた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "得意げに浮いている主の「どうだっ！」という眼差しに応えずに、また別の本を手にとってみる。"

play sound se_0603
pause .5
play sound se_0718
pause .4
play sound se_0721
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「ナイトメア」"

hide nai_s_03_1
show nai_s_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice nig_f0047
Nightmare "「何だ？\n
礼ならいいぞ、もう充分もらった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「そうじゃなくて……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「まさかとは思うけど、これ……。\n
{size=+20}全部、絵本なの？」{/size} "

hide nai_s_02_3
show nai_s_01_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice nig_f0048
Nightmare "「ああ、そうだよ。\n
童心に返って、美しい物語に心を浸すには、絵本が一番だからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「それは否定しないけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（まさか、この部屋に押し込まれた本すべてが絵本だとは、さすがに思わなかったわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "装丁がしっかりしているから一般書かと思ったのだが、確かに積み上げられた本の中には、ファンシーでカラフルな表紙の本がいくつか見える。"

hide gre_t_02_3
show gre_t_03_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

play sound se_0718
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「グレイ？」"

hide gre_t_03_10
show gre_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
Gray "「…………」"

hide gre_t_02_12
show gre_t_02_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gra_f0034
Gray "「可愛い……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどから沈黙し続けているグレイが気になったので声をかけたのだが、彼は彼で別の世界に行ってしまっているらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大きな手の中にあったのは、まさに絵本らしいファンシーな動物の絵柄だったが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（私よりも、グレイに対しての癒し効果のほうが大きいんじゃないの、これ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも苦言を呈する忠実な部下は、今や絵本の世界にとっぷりと入り込んでしまっている有様だ。"

hide nai_s_01_6
show nai_s_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0049
Nightmare "「ふ……、作戦成功」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「…………」"

hide nai_s_02_4
show nai_s_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice nig_f0050
Nightmare "「冗談だ、冗談！そんな絶対零度の眼差しで私を見るのはやめてくれ、[firstname]！\n
ちゃんと目的の本はあるんだ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（どうだか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見事に術中にはまっているグレイを見ていると、単に仕事をさぼる口実にされたのではないかという気持ちになってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の向けた疑惑の眼差しから逃れるように、ナイトメアは一冊の本を取り出した。"


show t_per2_1and_end3 onlayer master
with dis
hide nai_s_03_3

hide gre_t_02_14

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0051
Nightmare "「本当だよ。\n
ほら、これだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「人魚姫？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人魚の女の子と、飾り立てられた服を着た男性が表紙に立っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_4")
T "（この世界にも人魚姫ってあるのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "表紙の男女の姿には私も見覚えがあった。\n
彼らはヒロインの人魚姫と、人間の王子だろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0052
Nightmare "「ああ、あるよ。\n
現にこうして本になっているだろう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0053
Nightmare "「君の世界とまったく同じとは限らないが……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「ふうん。\n
…………？」"



hide t_per2_1and_end3

play sound se_0718
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先刻中身を確認した本と同じように差し出された本のページを捲った。\n
しかし、先ほどとは違った理由で私の手が止まる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「これ、どこの国の言葉？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に来て、文字や言葉で不自由したことはなかったが、今、本の中に書かれた文字は私には読めない文字だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（というより、これは……。\n
そもそも{size=+20}文字なの？{/size}）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "流れるような書体ね、などとはお世辞にも言えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "挿絵もなければ、文字と思わしき部分もすべて虫が這いずっているような、そんな印象しか与えてこない。"


show nai_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0054
Nightmare "「読めないか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「読めないわよ、これじゃあ。\n
あなたなら読めるの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（読めない本を渡されても困るんだけど）"

hide nai_s_03_10
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice nig_f0055
Nightmare "「ふ、これは読むものじゃないんだ。\n
これは、イメージを繋げるために選んだだけだからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（イメージを繋げる？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢魔の言うことはよく分からない。\n
不思議そうな顔をしている私の前で、ナイトメアは指を打ち鳴らした。"

play sound se_0468
hide nai_s_02_1

$ hi_mes()

play music dream_inside_p_ali

scene yume01
with dis

scene yume02
with dis

scene yume03
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "途端に感覚が変わる。\n
きらきらとオーロラのようなものが輝いている、おかしな空間。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（夢？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "積み上げられていた本も、童話の世界にトリップしていたグレイの姿も今は見えない。"


show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0056
Nightmare "「そうだよ。\n
ここでなら、その物語も先を広げられる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！！！」"

play sound se_0718
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ページは右に左に、あちこちのページを広げていく。"

play sound se_0727
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、ページが動く度に読めない文字もまた夢の空間の中へと飛び立つ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「何なの、これは……」"

hide nai_s_01_11
show nai_s_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice nig_f0057
Nightmare "「おや、忘れてしまったのかな、[firstname]。\n
ここは夢だ」"

hide nai_s_02_4
show nai_s_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice nig_f0058
Nightmare "「どんな非日常的なことが起きたとしても、おかしくはないだろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達が話す合間にも文字はどんどん溢れて、空間に広がり。"

hide nai_s_03_1

$ hi_mes()
play sound se_0730

scene white
with dis

play music transparent1_a_ali

scene bg_gen07_sc1
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「！」"

play sound se_0139
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（う、海？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一面のマリンブルーに目を見開いた。"

play sound se_0139
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚いた拍子に口の中からは大量の泡が溢れてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "息が出来ない。\n
海で泳いだ経験が、反射的に息を詰めさせる。"


show nai_s_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0059
Nightmare "「ふふふ、どうして息を止める必要がある？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（どうしてって……、当たり前でしょう\n
！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "肺に残った空気は僅かだ。\n
全部出してしまったら、息が出来なくなる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "息が出来なくなったら、沈むしかない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_6")
T "（こんなところで溺れさせたら、化けて出てやるわよ！）"

hide nai_s_02_4
show nai_s_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_6")
voice nig_f0060
Nightmare "「息が出来なくなる？\n
そんなことはないさ」"

hide nai_s_01_2
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_6")
voice nig_f0061
Nightmare "「今の君なら、ここで息をすることぐらい簡単だろう？」"

hide nai_s_02_1
show nai_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_6")
voice nig_f0062
Nightmare "「ほら、力を抜いてごらん。\n
そんなに力を入れていたら、かえって苦しいだけだよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（今の私なら？）"

play sound se_0167
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水の中にいるはずなのに、固い音が確かに聞こえた気がした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あ」"


show t_per2_2 onlayer master
with dis
hide nai_s_03_10

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「何、これは？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice nig_f0063
Nightmare "「忘れてしまったのかな。\n
君が持っていた本のことを」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "楽しそうに笑う夢魔の手には、さっきまで私が持っていた本がある。\n
表紙を飾っている人魚は、今の私と同じ姿をしていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「まさか……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声を発しても、もう口から泡は漏れない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうだ、ここは夢。\n
私が人魚になってしまうような場所ならば。\n
本当に、溺れるはずもない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「もっと早く、教えてくれればいいのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "身体の周りを水が漂う感覚は、夢とは思えないほど真に迫っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（動揺する私を見て楽しんでいたんじゃないでしょうね）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice nig_f0064
Nightmare "「それは誤解だよ、[firstname]。\n
元気のなかった君を励ましたくて、私なりに色々と考えたんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言いながらナイトメアは煙管で煙を吸い込んだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0065
Nightmare "「外では見せられないものも、ここならこうやって見せてあげられる」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0065_5
Nightmare "「本当の海に連れて行ってあげたいところだが、ここまで深い海の世界は簡単には見られないからね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "海の中で煙草を吸う、そんな非現実的な光景も夢ならばこそだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "吐き出された煙は輪となって飛んでいく。\n
頭上にある水の縁へと向かうように、紫の輪は浮き上がっていった。"

hide t_per2_2

play sound se_0139

show nai_s_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0066
Nightmare "「せっかくなんだ、泳いでみたらどうだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「この足……、もとい、ヒレで？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "両足を無理矢理くっつけられたような感覚のヒレ。\n
試しに動かそうとするがどうにもならない。"

hide nai_s_01_6
show nai_s_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0067
Nightmare "「ここは理屈じゃない。\n
したいようにしてみれば、うまくいく」"

hide nai_s_02_11
show nai_s_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0068
Nightmare "「ここは夢、私の領域だからね、君が望むようにしてみればいいんだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（また曖昧なことを）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とはいえ、このままでは何も変わらないのは事実だ。"

hide nai_s_02_2

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……こう、かしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "潜水するような感覚で身体をひっくり返す。\n
幼い頃に習ったバタ足を思い出しながら、ゆっくりと水を掻いていく。"

play sound se_0068
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「嘘……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（本当に泳げる）"

play sound se_0139

play music heartrending_a_ali

scene bg_gen07_sc2 with grad_b
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水を蹴るごとにどんどん深い場所へと潜っていく。\n
不思議な感覚だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あ……、魚」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_8")
T "（綺麗）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（そう言えば、ずいぶん前に姉さん達と海に行ったわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まだ母が生きていた頃。\n
私が覚えている、貴重な海の記憶。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（こんなふうに深く潜ることは出来なかったけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（……母さんが亡くなって、姉さんが言っていたわよね）"


scene bg_gen07_sc1_s
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice ari_f0004
Lorina "「また、海に行きましょうね。\n
お母様はいないけど、四人で」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あれはいつ交わした約束だっただろう。\n
とても大切な約束だったはずなのに、ずっと思い出すこともなかった。"


scene bg_gen07_sc2
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「結局行けなかったけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（行けなかった？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうして、そんなことが気になるのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私はこの世界に残ると決めたのだから、行けなかったと判断してもおかしくないはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]……。\n
[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「え」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！？」"

play sound se_0068

play music transparent1_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこから現れたのか。\n
私の潜ろうとしていた方向から、白い光が浮かび上がってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "長い耳と、雪のように白い髪。\n
水を通しているはずなのに、困ったように笑う目まで、はっきりと見えた。"


show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0057
Peter "「……はあ。\n
何をしているんですか、あなたは？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「何って言われると困るけど……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「それを言ったら、何であんたがここにいるのよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はハートの城で私の帰りを待っているはずだ。\n
ペーターは城で待つと約束していたのに。\n
その彼がどうしてここにいるのだろうか。"

play sound se_0068
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "近付いてきたペーターもまた、私の手を取ると首を傾げた。"

hide per_t_02_7
show per_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0058
Peter "「さあ？\n
ここは、ナイトメアの領域ですから理由もなく僕が入り込めるはずがないんですが」"

hide per_t_03_5
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0059
Peter "「でも、ずっとあなたのことを考えていたからかもしれません」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水中で白い髪がまるで海草のように揺れている。\n
海の中で、彼の白い髪と、赤い目に意識が集中してしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（何だか、今にも消えていきそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "簡単に消えてしまうほど弱いひとではないのに。\n
何故かそんなことを思ってしまった。"

menu:
    "嘘じゃないわよね？":
        jump fushigi_peter2_3a
    "ペーター……、よね？":
        jump fushigi_peter2_3b

label fushigi_peter2_3a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「本当に、ペーターよね？」"

hide per_t_02_8
show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
voice pet_f0060
Peter "「ええ、僕ですよ。\n
僕はあなただけの、あなたのための白ウサギ、ペーター＝ホワイトです！」"

hide per_t_02_5
show per_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
voice pet_f0061
Peter "「愛しいあなたのことばかり考えて、考えて。\n
眠れぬ夜を何度過ごしたことか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの勢いで捲し立てるペーターは、握った手に力を込めてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも、加減はしているのか、痛みはない。\n
感情的にもなるのに、私を傷つけるようなことはしない、不思議な接触。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（こんな触れ方をしてくるのは、あなたぐらいだと思うけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（あまりにもタイミングがよくない？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「偽物じゃないわよね？」"

hide per_t_01_13
show per_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
voice pet_f0062
Peter "「ええ、信じられないのならどうぞ触ってください」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "掴んでいた手を誘うように、彼は自分の頬へと当てた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……じゃあ、遠慮なく」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（相変わらず綺麗な肌）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "周囲を満たす水の感触は変わらない。\n
今も、夢とは思えないほどのリアリティがある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、手の下に感じた温かさには及ばない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「……ペーター」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "名前を呼ぶとぴくりと耳が反応した。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（落ち着く）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "出てくる前、ペーターの部屋で感じた気持ちと同じだ。\n
充足感が胸に広がり、ゆっくりと染み渡っていく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「……[firstname]」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "壊れ物を扱うように、でも強い力で抱き寄せられた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここは夢の中の海。\n
匂いなんて感じるわけがないのに、間近でいつもの石鹸の香りを感じたような気がした。"

play sound se_0474
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（ちゃんと、時計の音も聞こえる）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………」"

hide per_t_02_12
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice pet_f0063
Peter "「僕は、嘘じゃありません。\n
ジョーカーもここにはいない、嘘などつく必要はないでしょう？」"

hide per_t_03_1
show per_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice pet_f0064
Peter "「……あなたには、まだ苦いものが残っているとしても」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（苦いもの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "疑問を口にするよりも早く、唇が降ってくる。"



show t_per2_3 onlayer master
with dis
hide per_t_02_11


play music dream_tsuduki_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「んっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice pet_f0065
Peter "「忘れてほしくても、薄れさせるぐらいしか僕には出来ない。\n
それでも、あなたがこの世界にいてくれるのなら、構いません」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「ペーター？」"

jump fushigi_peter2_4
label fushigi_peter2_3b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……本当に、ペーターなのよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞いてしまったのは、あまりにこの夢に感覚がありすぎるせい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達の間にある海水も、周囲を泳ぐ魚の動きも。\n
まるで本当の海に沈んでいるような気になってしまう。"

play sound se_0208
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（ほら、だって聞こえる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの国に引っ越したとき、聞こえていた哀しい鳴き声。\n
帰りたいという、鳴き声が響いてきた。"

play sound se_0206
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Lorina "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！」"

play sound se_0207
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice ari_f0005
Lorina "「帰っていらっしゃい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クジラの声に混じって聞こえる、懐かしい声に身体が強ばる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（姉さんはここにはいない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（声なんて、聞こえるはずがない）"


show per_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_11")
voice pet_f0066
Peter "「[firstname]、ここはあなたの深層意識です」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「…………？」"

hide per_t_01_12
show per_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice pet_f0067
Peter "「恐らく、僕や夢魔でもない限り、ここまで入り込めるものはいないでしょうけど……」"

hide per_t_02_11
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice pet_f0068
Peter "「ここは、あなたにとって深すぎる。\n
上に戻りましょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……でも、ペーター」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視線を向けた先には、まだ海が広がっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（姉さんの声は、もっと奥から聞こえた気がするのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "海の底に何があるのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見てみたい。\n
同時に、見たくない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（怖いもの見たさみたいなものなのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "空っぽでも構わないから、結果が欲しいとどこかで思っている。\n
しかし、私の身体を抱き締める腕にこもる力は変わらない。"

hide per_t_02_6
show per_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0069
Peter "「……お願いです。\n
戻って、ください」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

play sound se_0208
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「分かったわ、上に戻る」"

hide per_t_01_8
show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
Peter "「…………」"

play sound se_0068
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "半ば抱きかかえられるように導かれていった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐんと水が身体の横を流れていくのが分かる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（夢なのに、そうとは思えないぐらい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水に流れる髪まで忠実に動いている。"

hide per_t_02_7
show per_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0070
Peter "「あなたは、もっと深い場所に行きたいのかもしれませんけど……。\n
僕は、それだけはさせたくないんです」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（そんな哀しい声で言わないでよ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice ari_f0006
Lorina "「ほら。\n
早く、帰っていらっしゃい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "案内役を自負する白ウサギに引かれて離れていく。\n
だが、彼の言葉に従うと決めたのは他でもない私自身。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも、下から響く声に引かれている自分が、酷く薄情に思えた。"

jump fushigi_peter2_4
label fushigi_peter2_4:

play music transparent1_a_ali


hide t_per2_3

hide per_t_01_13
show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0071
Peter "「この世界にあなたがいてくれればそれでいいと思っていたんです。\n
でも、僕はどんどん欲張りになる」"

hide per_t_02_10
show per_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0072
Peter "「あなたが今どうしているか知りたくて、あなたが辛くないように出来ればと、そればかり考えて」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

hide per_t_03_5
show per_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice pet_f0073
Peter "「だから、許せないんです」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水の流れが止まる。\n
いや、正しくは浮上していた身体が、止まったのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の身体に手を回したまま、真っ赤な目でペーターははるか遠い水面を睨み付けている。"

hide per_t_03_10
show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0074
Peter "「どういうつもりですか、ナイトメア。\n
ここはあなたの領域でしょう、彼女に危険が及んでいたかもしれないのに」"

hide per_t_02_7
show per_t_02_7 at left
show nai_s_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0069
Nightmare "「それこそ、心外だよ、白ウサギ。\n
もっと深い所にまで彼女が潜り込もうとしていたら、私だって止めていたさ」"

hide nai_s_01_9
show nai_s_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0070
Nightmare "「私だって、彼女には幸せになってもらいたい者の一人だからね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "魚の群れの中に浮かび上がるのは、黒衣の夢魔。\n
ペーターとは対照的な色彩は、彼とは違った意味で海の中で浮き上がっている。"

hide per_t_02_7
show per_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0075
Peter "「信用なりませんね。\n
もう少し奧まで進んでいたら、彼女は……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（何をそんなに脅えているの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアが言っていたように、ここは夢だ。\n
それも、夢魔がいる夢の中。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼がその力を存分に発揮できる場所で、危害を加えられるような事態など私には想像も付かない。"

hide per_t_01_1
show per_t_02_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

hide per_t_02_11
show per_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0076
Peter "「だいたい、この風景は何です？\n
人魚姫？」"

hide per_t_03_10
show per_t_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0077
Peter "「質が悪いにも程があります。\n
彼女を泡にして消すつもりですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（怒っている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を抱き上げたまま睨むペーターは本気で怒っていた。\n
私のほうに視線を向けることもなく、水中に浮かぶナイトメアを見上げている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0071
Nightmare "「まあ、他の映像でもよかったんだがね、他意はない。\n
彼女の性格からすると、人魚姫のほうがいいかと思っただけだよ」"

hide per_t_02_7
show per_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0078
Peter "「白々しい。\n
もし、彼女が思い出したら……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「思い出す？」"

hide per_t_01_1
show per_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice pet_f0079
Peter "「……あ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "明らかに狼狽した様子で、ペーターが私を見た。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「どういうこと、ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（何を隠しているの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は私に嘘をつかない。\n
だが、すべてを見せてくれているわけではないことぐらい、私も知っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見せないほうがいい。\n
知らないほうがいい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターがそう判断したことは、私の周囲から弾かれていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「私が思い出したらいけないことって……、一体、何なの？」"

hide per_t_01_5
show per_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
Peter "「[firstname]……」"

hide per_t_02_6
show per_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
Peter "「…………」"

hide per_t_02_6
show per_t_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice pet_f0080
Peter "「すみません。\n
それは言えません」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "問い詰めた私に、彼は申し訳なさそうに言葉を紡いだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（どうして、教えてくれないの？）"


play music opposition1_a_ali
hide nai_s_02_4
show nai_s_03_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice nig_f0072
Nightmare "「簡単なことだ」"

hide nai_s_03_11
show nai_s_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice nig_f0073
Nightmare "「……怖いからだよ。\n
私には、ペーター＝ホワイトの気持ちのほうがよく分かる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ナイトメア」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（いつの間にこんなに近くにいたの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後に忍び寄っていた夢魔は、そのままするりと手を伸ばしてくる。"

hide per_t_01_13
show per_t_01_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「！」"

play sound se_0023
pause .4
play sound se_0020
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の背後に向けて、ペーターが銃を撃った。"

hide nai_s_02_1
show nai_s_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0074
Nightmare "「無駄だよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、ここは夢の中。\n
夢魔であるナイトメアに危害を加えられるような存在など、いない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あっ……」"


show t_per2_4 onlayer master
with dis
hide per_t_01_7

hide nai_s_01_1

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "反射的に身を捩ったときには、もう既にナイトメアの腕の中だった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0075
Nightmare "「ここは私の領域だ。\n
銃でどうにか出来るはずがないだろう、ペーター＝ホワイト」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0081
Peter "「ナイトメア……、どういうつもりです。\n
まさか、彼女を元の世界に返すとでも言うつもりですか！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声を荒げるペーターに、夢魔は首を横に振った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0076
Nightmare "「それこそまさかだよ。\n
言っただろう、私だって彼女に幸せになってもらいたいんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0077
Nightmare "「だがね、私は君のことも気に入っているからな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「ナイトメア？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を抱きとめている夢魔は不思議な笑みを浮かべている。\n
現実の世界にいるときには、あまり見せない表情だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターに向けた眼差しには、どこか冷ややかなものさえ感じた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（まさか、ペーターに何かするつもりじゃ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "咎めるように睨むと、彼はようやく私に視線を向けて、笑った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0078
Nightmare "「心配しなくていいよ、[firstname]。\n
言っただろう、私は彼のことも嫌いじゃない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0079
Nightmare "「彼が今すぐに私を撃ち殺したいと思っていても、ね。\n
好意は確かなものだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0082
Peter "「あなたに好かれているだなんて、考えただけで反吐が出ます」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0083
Peter "「ここが夢で命拾いをしましたね。\n
現実だったら、今頃は……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0080
Nightmare "「ふふ、怖いウサギだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターと違って、ナイトメアはその腕に私を抱きとめている。\n
手足を動かした様子もないのに、ペーターとの距離が開いていく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0084
Peter "「まだ話は終わっていませんよ、ナイトメア！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0081
Nightmare "「そうかな？\n
だが、夢はいつか覚めるもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "肩を震わせているナイトメアは、薄笑いのまま指を立てた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0082
Nightmare "「今は君の夢へと帰るがいい、白ウサギ」"

play sound se_0468
play sound se_0730
hide t_per2_4
show white onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()


hide white


scene yume02
with dis

scene yume03
with dis

play music dream_inside_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（いつもの夢の中だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "明るいような、暗いような。\n
果てがないようで、実はとても狭い空間。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほど空間に満ちていたはずの海水も、魚も。\n
そして、突然現れたペーターも、すべて消えていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "残されたのは、私と、夢の主だけ。"


show nai_s_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0083
Nightmare "「よほど、彼は君が心配らしい。\n
まさか、私の領域の中に飛び込んでくるとは思わなかったよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「ペーターは無事なのよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思い出すのは、監獄での一幕。\n
無理矢理空間を破って現れた彼は大怪我を負っていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ここが監獄と同じ仕組みだったら、今頃は……）"

hide nai_s_01_4
show nai_s_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice nig_f0084
Nightmare "「心配しなくていい。\n
自分の夢に帰っただけだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「そう、……ならよかった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアがペーターに危害を加えるとは思えなかったが、否定をされて安心する。"

hide nai_s_03_12
show nai_s_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

hide nai_s_03_9
show nai_s_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「？」"

hide nai_s_02_7
show nai_s_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice nig_f0085
Nightmare "「君はまだ、帰りたいと……。\n
いや、帰らなければならないと思っているのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "静かな問いかけに、私は一瞬声に詰まる。\n
目を伏せかけたが、心が読める夢魔には意味がない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「分からない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（ペーターといたいと思うのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほど聞こえたあの声に、気持ちが揺れた。"

hide nai_s_02_8
show nai_s_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

hide nai_s_03_9
show nai_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0086
Nightmare "「そんな顔をしてくれるな。\n
君を泣かせでもしたら、今度こそ白ウサギに撃ち殺されてしまう」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは突然私の頭を撫でだした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「ナイトメア？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "戸惑いながら呼びかけると、彼は困ったように微笑む。"

hide nai_s_03_10
show nai_s_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0087
Nightmare "「物語の終わりがハッピーエンドとは限らない。\n
だが、幸福か否かは当事者にしか判断できない」"

hide nai_s_02_2
show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0088
Nightmare "「誰かの不幸が誰かの幸せを招くかもしれないし、その逆もまた然りだ」"

hide nai_s_01_11
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0089
Nightmare "「現実は童話のように簡単にはいかないが、望むことは悪いことばかりじゃない。\n
望んで初めて見えるものだってある」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_3")
T "「…………」"

hide nai_s_02_1
show nai_s_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_3")
voice nig_f0090
Nightmare "「さあ、そろそろ戻るとしよう。\n
グレイの奴が、また仕事仕事と騒ぎ始めている」"

hide nai_s_01_4
show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_3")
voice nig_f0091
Nightmare "「あいつまでここにやってきたら、騒がしいだけだからな。\n
帰ろう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「……うん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（夢の果ての幸せ……、か）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何気なく呟かれた夢魔の言葉が、酷く気になった。"

hide nai_s_01_11

$ hi_mes()

scene yume03
with dis

scene yume02
with dis

scene yume01
with dis
##endmemory

scene map_bg_winter_day
with dis

jump fushigi_common3_tower ##I think
