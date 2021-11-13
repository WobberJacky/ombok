label fushigi_joker_5:
scene map_bg_joker_day
with dis
$ clockanim()


scene circus
with dis

scene bg_gen17_cst_a
with dis

scene bg_gen17_cst_k with Dissolve(1.2)

play music forest_circus_p_ali

show jo_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_f0256
White_Joker "「うん、大分片付いたね。\n
これなら撤収まで、そうかからない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_f0257
Mask "「おまえがサボらなけりゃ、もっと早くに片付いただろうけどな、ジョーカー」"

hide jo_t_03_9
show jo_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_f0258
White_Joker "「俺は、サボってなんかいないよ。\n
それに、俺がサボっていたとしたら、\n
ジョーカーだってサボっていたことに\n
なるだろう？」"

hide jo_t_03_2
show jo_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_f0259
White_Joker "「同罪だよ、同罪」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（端から見ていると、ただの腹話術にしか見えないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "荷物の山の近くにいるジョーカーを見ながら、そんなことを思う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスの荷物は、ほとんどが天幕から出されている。\n
中に残っているのは、人だけだ。"

hide jo_t_01_13
show j-boy_a_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0037
Danin "「ジョーカー、他に持っていく物はない？」"

hide j-boy_a_5
show j-boy_a_5 at left
show j-girl_a_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0033
W "「忘れ物をしたら大変だもの。\n
よく確認しないと」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（いよいよ、行くのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "嘘つきの季節と共に現れた、謎の多いサーカスの一団と、その団長。\n
季節が終わったのと同じように、彼らはここではないどこかに旅立っていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ねえ、ジョーカー。\n
あなた達、次はどこに行くの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "深く知らないほうがいい……、そう思っていたはずなのに尋ねてしまう。\n
そのくらい、私は彼らと近づいてしまっていた。"

hide j-boy_a_5
show jo_t_03_19 at center
hide j-girl_a_5
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0260
White_Joker "「次か……。\n
そうだね、どこだと思う、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「誤魔化さないでよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（サーカスについて、ほとんど知らない私に分かるはずがないじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らは一様に口を揃えて「撤収が終わったら、ここからいなくなる」と繰り返していたが、その行き先を私は知らない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（知ったところで、どうにも出来ないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界は、余所者の私には理解できないルールによって縛られている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "土地が回る、引っ越しもその一つ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスもまた土地と同じように巡るものらしいが、彼らの場合には土地そのものと一緒に回るわけではないらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（……安心している？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（それとも、寂しく思っている？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の答えは、そのどちらとも言い切れない。"

hide jo_t_03_19
show jo_t_02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0261
White_Joker "「サーカスは別に消えるわけじゃないよ、[firstname]。\n
近くて遠いところ、遠くて近いところ」"

hide jo_t_02_15
show jo_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0262
White_Joker "「いつでも辿り着けて、同時に行きたいと思うときにはなかなか辿り着けない。\n
俺達がいるのは、そういうところだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "荷物から視線を外して、私を振り返ったジョーカーが指を動かす。"

play sound se_0346

show t_jo5_1 onlayer master
with dis
hide jo_t_02_5

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（トランプ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私のほうに向いているカードには、数字も絵も描かれていなかった。\n
トランプなら、数字や絵が描かれているはずだが。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0263
White_Joker "「このカードと同じだよ。\n
何も描かれていないように見えるけど、ひっくり返せば……」"

play sound se_0079
hide t_jo5_1
show t_jo5_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0264
White_Joker "「……ね？\n
ちゃんと、あるだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「裏の絵柄だけどね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "トランプに入っているスペアのカードなのだろうか。\n
白紙のカードの裏には、何ということもない柄が描かれていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0265
White_Joker "「ふふふ、それは早とちりだよ。\n
[firstname]、どうしてこれが裏だって言えるの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「どうしてって……。\n
普通、トランプだったら絵が描いてあるほうが表でしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゲームで伏せられる柄は、今、彼が提示している柄模様のほう。\n
普通に考えれば、こちらが裏ということになる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0266
White_Joker "「そうだね。\n
このカードの裏に何もなければ、これが表かもしれない」"

play sound se_0079
hide t_jo5_2
show t_jo5_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "くるりと男の手の中でカードがひっくり返る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどは真っ白だったカードの表面には、今まさに見ていた裏面と同じ柄模様が生まれていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（……手品？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（マジックショーに付き合う気はないんだけどな）"

hide t_jo5_3


show jo_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice jok_f0267
White_Joker "「どっちが表か裏かなんて、些細なことなんだよ。\n
そこに存在しているというのは間違いない」"

hide jo_t_02_10
show jo_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice jok_f0268
White_Joker "「このトランプの表と裏が同時に見られないのと同じ、見えないだけだよ。\n
消えたりしない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（消えない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（本当に？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこかに行ってしまうことはあっても、この人は消えないのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引っ越しとは違った理由で、私のいる場所から遠く離れてしまっても、見えないだけで。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（近くに、いるの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それは果たしていいことなのか、それとも忌むべきことなのか、まだ分からない。"

hide jo_t_03_13
show jo_t_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0269
White_Joker "「どう？\n
安心したかな？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「そうね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（この人がどんな存在であれ、いなくなってしまうことに比べれば……。\n
ずっといい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分でも不思議だが、そう私は強く感じている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「突然押しかけて悪かったわね、ジョーカー。\n
あなた達が行くなら、私も帰るわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供っぽい家出はお仕舞い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私のいるべき場所に戻らなくてはいけない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（自分で決めた場所だもの）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（戻らなくちゃ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ここに置いてくれて、ありがとう。\n
あなたのサーカスは楽しかったわ」"

hide jo_t_03_14
show jo_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice jok_f0270
White_Joker "「おや、ずいぶんつれないじゃないか、[firstname]。\n
行くなら、今までの宿泊費代わりに俺に付き合ってよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬、心に残った寂寥感を読まれたのかと思ったが、そうではないらしい。\n
ジョーカーは悪戯を思いついた子供のような顔をして笑っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「付き合うって、まさか……。\n
この荷物の運び出しを手伝えとか？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（大分、量があるわね。\n
少しずつなら手伝えなくはないけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくらなんでも、猛獣が入れられた檻を動かせとか、そんな無茶な指示でなければ、他の団員とも協力して何とかやれるだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たいして役に立つとは思えないが、世話になったのだからそれくらいはするべきだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、彼は首を横に振った。"

hide jo_t_01_2
show jo_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0271
White_Joker "「違うよ、[firstname]。\n
そんなことに君の手をわざわざ借りるつもりはない」"

hide jo_t_01_11
show jo_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0272
White_Joker "「忘れていないかい、ここはサーカスだよ？\n
付き合ってもらうなら、答えは一つしかないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？」"

hide jo_t_01_5

play sound se_0468

show white onlayer master with expand_extrashort
hide white with Dissolve(.1)
show white onlayer master with expand_extrashort
hide white with Dissolve(.1)
play sound se_0708
show white onlayer master with expand

play music circus_a_ali
hide white
show t_jo5_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「な……、何よ、これっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーが指を打ち鳴らすと、一瞬にして私の服が替わっていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "服の早替えなら滞在地でも経験したことがあるが、問題は着せ替えられた服にある。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0273
White_Joker "「うん、思った通りだ。\n
君にはよく似合っているよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0274
Mask "「そうだな……。\n
いかにも、～～～～っぽいところなんか、ぴったりだよな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（あんただって、同じような服を着ているでしょうが）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（しかも、私よりもよっぽど似合うくせにっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "花弁のように大きく開いた襟、頭に載せられた帽子。\n
底の薄い靴は、色合いこそ違えどジョーカーが履いているものによく似ている。"

hide t_jo5_4

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「何を考えているのよ、ジョーカーっ」"


show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice jok_f0275
White_Joker "「何って、もちろん、決まっているだろう。\n
ここはサーカスで、君はそこで技の練習までした、貴重な見学者なんだよ」"

hide jo_t_03_1
show jo_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice jok_f0276
White_Joker "「このまま帰したら、団長の名折れだ。\n
だから、腕試しを、させてあげる」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（腕試し？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「腕試しとかいう以前に、そんな技術がないことぐらい、あなただって知っているでしょう！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何とかの一つ覚えのように、直進しかできない玉乗りで一体何を試せというのか。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0277
Mask "「ぎゃーぎゃーうるせえな。\n
ここまで来たら、さっさと腹を決めろよ」"

hide jo_t_03_7
show jo_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0278
White_Joker "「ああ、そうだ。\n
忘れちゃいけないよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚く私の目の前で、彼は手を持ち上げる。"

play sound se_0468
hide jo_t_02_12

pause .5
play sound se_0173

scene bg_gen17_cst_a
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "再び指を打ち鳴らしたジョーカーに、思わず身構えた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、今度の変化は私の服ではなく、サーカスの天幕全体に影響を与えるものだったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "片付けたはずの荷物が舞台から消え、中には明かりが灯る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（先刻まで、明かりなんてついていなかったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それ以前に、私がこのサーカスに来てから観客席に明かりが付いたことなどない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "後片付けだけ、残骸だけしか残っていないサーカスには、撤収に必要な灯りだけがあればいい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「ジョーカー？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（何を考えているの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の呼びかけに彼は応じることなく、もう一度指を滑らせた。"


show jo_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0279
White_Joker "「[firstname]、君の晴れ舞台だ。\n
俺達だけが見るんじゃつまらない」"

hide jo_t_01_11
show jo_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0280
White_Joker "「君のやる気が出るように……観客も呼んであげる」"

play sound se_0468
hide jo_t_01_5

play sound se_0559
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0041
Father "「ああ、この公演が見られるなんて思わなかったな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0036
Mother "「本当に来られてよかったわ。\n
あら、可愛いピエロさんね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0051
Boy "「パパ、これから何が始まるの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「い、いつのまにこんなに人が……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "客席は満員とは言わないが、そこそこの人が席について、舞台を見ている。\n
撤収間際のサーカスとは思えない人の入りだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで整理整頓されて片付けられていた荷物の一部が、舞台を飾っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（な、何のために片付けたのよ、あんた達はっ！？）"


show jo_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice jok_f0281
White_Joker "「ははは、今更、何を言うんだい、[firstname]。\n
ここでは時間の概念なんて、意味がないのは君も知っているだろう」"

hide jo_t_03_8
show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice jok_f0282
White_Joker "「さあ、おいで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーは軽やかなステップで私の手を引くと、舞台の中央に躍り出た。"


play music title_jok

show t_jo5_5 onlayer master
with dis
hide jo_t_03_1

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0283
White_Joker "「レディス・アンド・ジェントルメン！\n ・・・・
ウエルカム・トウ・ザ・ワンダフル・ワンダーワールド」"

play sound se_0227
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何度も聞いた口上。\n
サーカスの開幕を宣言する、道化師の声が広い天幕に響き渡る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（でも、今までとは違う）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "以前にこの台詞を聞いたとき、私は観客の一人だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼を遠くから見ていた。\n
しかし、今は自分がジョーカーと一緒に舞台にいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんな大勢の前で堂々と動けるほど、私はうまくもない、ド素人でしかない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思うのに、胸の中に込み上げるのは拒否以外の高揚するような感覚。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（どうして？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice jok_f0284
White_Joker "「大丈夫だよ、[firstname]。\n
言っただろう、ここはサーカスなんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice jok_f0285
White_Joker "「一人でやる必要なんてない。\n
皆、君を手伝いたがっているんだから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice jok_f0286
White_Joker "「皆で、楽しませてあげよう。\n
ね？」"

hide t_jo5_5


scene bg_gen19_cbu
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ね、ねえ……。\n
やっぱりやめておくわ」"


show j-girl_a_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice nos_f0034
W "「えー、そんなこと言わないでよ」"

hide j-girl_a_11
show j-girl_a_11 at left
show j-boy_a_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice mat_f0038
Danin "「大丈夫だよ。\n
僕達もよく失敗しているんだから」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（そういう問題じゃないわ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舞台の横に設けられた、狭い空間。\n
そこで大きな玉に乗せられかけている私は、じたばたと悪あがきのように台に戻ろうとしていた。"

hide j-boy_a_11
show j-boy_a_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0039
Danin "「いいんだよ、失敗しても、サーカスなんだもの。\n
楽しんでもらうのが目的なんだよ」"

hide j-girl_a_11
show j-girl_a_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0035
W "「そうよ、そうよ。\n
失敗しても、怒られたりしないわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「そう言われても……、こんな素人が舞台に上がるなんて、やっぱりまずいわよ」"

hide j-girl_a_5

hide j-boy_a_5

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "辛うじて大きな玉に乗って進めるようにはなったが、それだけだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "玉に乗ったままでは方向転換も出来ないし、まっすぐ進むことだって完璧に出来るわけじゃない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（未だに三回に一回は滑り落ちているものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その上、私が登場する予定の舞台の上には、大きな動物の影がある。"

play sound se_0420
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「あれの近くに行って、私に何をして来いって言うのよ……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（いや、それ以前に近付けるの？\n
明らかに肉食動物でしょう、あれはっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "万が一バランスを崩して倒れ込んだら、頭からぱっくりと食べられてしまいそうだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（いくらなんでもそんな楽しませ方は嫌すぎる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "倒れ込む自分の姿と、その末路を思わず想像してしまった。"

play sound se_0226

show j-boy_b_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tak_f0004
Danin "「ほら、出番だよ！\n
早く早く！」"

hide j-boy_b_2
show j-boy_b_2 at left
show j-girl_b_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice man_f0001
W "「あなたの出番よ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「あ、ち、ちょっと！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然現れた子供達は、私の返事を聞くよりも先に巨大な玉を転がし始めてしまった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも……、まるで後戻りはさせないとでも言うように、舞台に向かって。"

play sound se_0173

play music opposition1_a_ali

show white onlayer master with spread_medium
hide j-boy_b_2

hide j-girl_b_3

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（眩しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飛び込んでくる光は、観客席で見ていたときとはまったく違っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遠くの席に座る人にも見えるようにと計算されているのだろうが、浴びる人間にとって眩しすぎる。"

play sound se_0226
hide white
show t_jo5_6 onlayer master with Dissolve(2)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice kat_f0042
Father "「おお、今度は玉乗りだな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_5")
voice chi_f0052
Boy "「可愛い。\n
僕もああやって乗ってみたいなあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "客席にいるときには、ただ歓声が固まっているようにしか聞こえなかったのに、舞台にいると声の聞こえ方もまるで違う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同時に自分に向けられる好奇の視線もまた、まったく違う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（今まで余所者だっていう目で見られることはあったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舞台に立つ者として、誰かの視線を浴びるなんてことはこれが初めての経験。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "好奇心だけではなく、期待と関心のこもった眼差しを受けながら、足下の玉は少しずつ舞台の中央に、そして、そこに置かれた檻へと近付いていく。"

play sound se_0420
hide t_jo5_6 with Dissolve(2)
show t_jo5_7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（どうしよう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "このまま行けば、檻との正面衝突は避けられない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "冷や汗が手の平に滲む。\n
顔が引きつりそうになるのを、必死に堪えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ここに立っている以上は、強ばった顔なんて見せられない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "客席から見ていた風景を思い出す。\n
どんなに高いところで演目をしていたとしても、団員は決して表情を曇らせたりしなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（私はここの人間じゃないけど……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（失敗はしても、お客さんを不安がらせるなんてよくないわ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

play sound se_0420
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（あと、数歩動かしたら、いよいよぶつかる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までになく集中しているせいだろうか、ボールはまっすぐに一定のスピードで進んでいく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その代わり、視線は真っ正面に待つ檻以外を見るゆとりなど、ない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（どうしよう）"

menu:
    "玉から下りる。":
        jump fushigi_joker5_2a
    "このまま進む。":
        jump fushigi_joker5_2b

label fushigi_joker5_2a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（無理よ、無理。\n
下りたほうが絶対にいいわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくら大きい玉とはいえ、所詮、中に詰まっているのは空気だけだ。\n
これがぶつかったぐらいでは、檻はびくともしないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（問題は、バランスを崩した私がどこに落ちるかよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "演目前の猛獣には、餌は与えられない。\n
腹が満ちていれば、演技をしなくなるからだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "当然、先刻から飢えた咆哮をあげているこの虎も、相当に空腹のはず。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（私なんか食べてもおいしくないって言ったところで、通じないだろうし……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……うん、下りよう。\n
下りるしかない……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスは不思議とスリルの調和によって成り立っている。\n
スプラッタな光景など、ここには相応しくないのだ。"



hide t_jo5_7

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうと決まれば、行動は早い。\n
飛び降りようと足に力を込めたところで、突然手を掴まれた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「え……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！！？」"

play sound se_0697
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jok_f0287
White_Joker "「ふふふ、よく声を出さなかったね。\n
悲鳴なんてつまらないからね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jok_f0288
White_Joker "「君は本当にいい団員になれるかもしれないよ。\n
[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ジョ、ジョーカー！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "空中ブランコに足を引っかけてぶら下がっていたジョーカーは、私の腕を掴んだまま大きく身体を反らす。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬、身体に重力を感じるが、そのまま引き上げられた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"


play music circus_a_ali

show t_jo5_8a onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どれだけの力がこの細身にあるのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あろうことか、ジョーカーは私の手を掴んだままブランコの上に腰を下ろすと、その膝の上に私を乗せてしまう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0289
White_Joker "「うん、悪くない。\n
これも役得ってやつかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「ちょ、ちょっと……っ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice sat_f0008
Father "「すごいな、ブランコに全然気付かなかったよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice oda_f0017
Mother "「あっというまだったわね。\n
瞬きも出来ないわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice hei_f0037
Boy "「すごい、すごい！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（こ、これも演出だと思われている？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舞台にいるときには分からなかったが、客とは思ったよりも楽観的なものなのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この流れを知らされていなかった私自身、かなり驚いているが。"

play sound se_0697
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「う、うわわっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jok_f0290
White_Joker "「ぼうっとしている暇はないよ、[firstname]。\n
これが最後のサーカスなんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jok_f0291
White_Joker "「たっぷり、楽しまなくちゃ……。\n
客だけじゃないよ、君も、楽しんでくれ」"

play sound se_0697
hide t_jo5_8a
show t_jo5_9a onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大きく揺られるブランコの上。\n
そこから見下ろす観客席には、たくさんの人がいた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（顔は見えにくいのに……。\n
きらきらしているのが分かる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "客席から見ているときには、華やかな舞台こそ輝いているように見えたが……。\n
スポットライトが当たっていない客席もまた、不思議な熱がある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（この人も、これが好きなのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "内側からしか見えないもの。\n
眼下に広がる輝く舞台は、まるで宝石箱のようだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつだったか、サーカスの裏側を案内してくれたとき、ジョーカーが言っていたことを思い出す。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0291_5
White_Joker "「そうだね、君は客席からの風景はよく知っているだろうけど……。\n
逆の風景は見たことがないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（逆からしか見えないもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最初はほとんど興味がなかったはずなのに、いつのまにかこんなに近くに引き込まれてしまっていた。"

jump fushigi_joker5_3
label fushigi_joker5_2b:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（ぶつかったら、ぶつかったで、さっさと引っ込まないと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元々素人を舞台に上げるという考え方が間違っているのだ。\n
だったら失敗を理由にさっさと退場してしまったほうが、いいだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（ジョーカーには、演目を台無しにして悪いとは思うけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は無理だと訴えた。\n
あそこまで進もうというだけでも、褒めてもらいたいほどだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのままボールはまっすぐに進み、間もなく檻の縁に触れる。"



hide t_jo5_9a

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "案の定、ボールがぶつかると同時に私の身体は衝撃を殺すことが出来なくて、ぐらりと揺れた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "反射的にバランスを取るように腕を動かしたが、一度崩れた体勢は簡単には戻らない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……あ、っと」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（落ちる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "虚空を掴むように手を伸ばすが、支えになるようなものなんてあるはずがない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、伸ばした手は別の人間によって確かに掴まれていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0292
Black_Joker "「……へたくそが。\n
どうせこけるなら、もっと派手にやれよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0293
Black_Joker "「出来ないんだったら、舞台を終わらせるんじゃねえ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ジョーカー！？」"


play music circus_a_ali

show t_jo5_8b onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice jok_f0294
Black_Joker "「下手すぎて見ていらんねえな。\n
もう少し根性出せよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "客席には聞こえないような小さな声で、彼は馬鹿にしたように私を見て言う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（まあ、実際に馬鹿にしているんだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まっすぐにしか進めない玉乗り素人なんて、彼からすれば芸というのもおこがましいのだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「根性でどうにかなるものなの、これ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice jok_f0295
Black_Joker "「少なくとも落ち方っていうものがあるだろうが。\n
例えば、こんな……、方法とかよ」"

play sound se_0468
hide t_jo5_8b
show t_jo5_9b onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足下にあった不安定な感覚が消える。\n
乗っていた球が消えたのだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舞台の上に落下したが、痛みはまったくなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーと手を繋いだまま私の身体も落ちた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（と、虎の檻まで消えている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで獰猛な獣がいた檻は、カラーボールの海に変わっていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0296
Black_Joker "「同じ落ちるでも、こうすればまた別の見せ方になるんだよ。\n
素人でも、その辺りはよく覚えておくことだな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（覚えておけって）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まるで私がここに残るような言い方をしないでほしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（ずっとここにいるはずがないでしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスはもう消える。\n
そうなれば、彼らと過ごすことはない。"

hide t_jo5_9b

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（でも、少し残念だな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を引かれた感触は、いつもの彼と違って乱暴ではなかったから。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（もう少しだけ、留まっていてくれたらよかったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "サーカスにいる彼らといると、監獄のことを思い出さずにすむ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あそこもまたジョーカーの空間だというのに、こうして一緒に舞台に立つことを楽しんでいるのも事実。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（朱に交わればってやつなのかしら、これ）"


show jo_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice jok_f0297
Black_Joker "「おい、何をぼうっとしていやがるんだ。\n
拍手に、ちゃんと応えろよ」"


show t_jo5_10b onlayer master
with dis
hide jo_t_03_5

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「あっ」"

play sound se_0226
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice sat_f0009
Father "「いや、見事だった」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice oda_f0018
Mother "「ええ、本当に見応えがあること。\n
次はどんなことをしてくれるのかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "期待のこもった歓声と、拍手。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（大したことは出来なかったけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「…………」"

hide t_jo5_10b
show t_jo5_11b onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_14")
Black_Joker "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "伏せた顔が一瞬こちらを振り返る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "客から見えないせいだろう、相変わらず意地の悪そうな表情を浮かべていたが、その目は今までのような無愛想さが陰をひそめていた。"

jump fushigi_joker5_3
label fushigi_joker5_3:
play sound se_0226
show circus1_a onlayer master with Dissolve(1.6)
hide t_jo5_11b
show circus2_a onlayer master with Dissolve(1.6)
hide circus1_a
show circus4_a onlayer master with Dissolve(1.6)
hide circus2_a
show circus3_a onlayer master with Dissolve(1.6)
hide circus4_a

play music dream_tsuduki_a_ali


hide circus3_a with Dissolve(2)
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（……終わった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの後も、投げナイフの的にされたり、ジャグリング中の団員にボールを投げ入れたりする役などもやらされたが、無事予定していた内容は終わったらしい。"




show jo_t_03_14 at center with Dissolve(1.6)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "舞台の上に立っているのは、閉幕を告げるために、一人スポットライトを浴びる道化師だけ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここは彼の舞台、彼の空間。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だというのに。\n
彼は舞台袖に引っ込んでいる私を振り返ると、手で招いてくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（え？）"

hide jo_t_03_14
show jo_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice jok_f0298
White_Joker "「おいで、[firstname]」"

hide jo_t_01_3
show jo_t_01_3 at left
show jo_t_02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice jok_f0299
Black_Joker "「とっとと出て来いよ、焦れってえな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ブラックさんまで……？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつの間にか、二人のジョーカーが舞台の上に立っている。\n
それぞれ別の表情を浮かべながら、その片手を私のほうへと差し出して。"

hide jo_t_01_3

hide jo_t_02_10




show j-boy_a_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0040
Danin "「ほら、行かなくちゃ」"

hide j-boy_a_2
show j-boy_a_2 at left
show j-girl_a_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0036
W "「ジョーカーが待っているわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚き戸惑っている私を後押しするように、子供達が声をかけてくる。\n
そして言葉だけではなく、実際に背中を押して舞台へと押し出してしまう。"

hide j-boy_a_2

hide j-girl_a_3
with dis

scene bg_gen17_cst_a
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「う、わわっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たたらを踏む私がふらふらと舞台に躍り出ると、左右から伸びてきた腕が身体を引き上げた。"


show jo_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0300
White_Joker "「待ちくたびれたよ。\n
いっただろう、これは君のための舞台なんだ」"

hide jo_t_01_5
show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0301
White_Joker "「主役が舞台裏に引っ込んだままじゃ、終われないだろう？」"

hide jo_t_03_1
show jo_t_03_1 at left
show jo_t_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0302
Black_Joker "「いつまでも客を待たせるんじゃねえ。\n
幕引きぐらい付き合え」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

play sound se_0227
hide jo_t_03_1
hide jo_t_02_11
with Dissolve(2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いいのだろうかと不安がる私の上にも、惜しみない拍手が降ってくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice kat_f0043
Father "「いい舞台だった」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice hei_f0038
Mother "「ええ、最後まで楽しめたわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice chi_f0053
Boy "「また来るねっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の拙い出演で本当に楽しませられたとは思わない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（だけど……）"


show t_jo5_12 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice jok_f0303
White_Joker "「これにて、サーカスはおしまい。\n
幕引きとなります」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "両の手を二人のジョーカーがそれぞれ握っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "閉幕を宣言する、大事な場面。\n
団員ですらない私は分不相応だと思うのに、何故か袖に戻ることが出来ない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0304
White_Joker "「またの機会、またのご来場を心待ちにしております」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この場に立つことは、これが最初で最後。\n
その気持ちが私を動かした。"

hide t_jo5_12
show t_jo5_13 onlayer master
with dis
play sound se_0227
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（ここでしか見られないものが、確かにあったもの）"

play sound se_0226
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "スポットライトの光と、薄暗い闇色のサーカス。\n
それらを浴びる側に立ってみなければ分からなかったこと。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おかしな二人の団長、そして一緒に舞台を支えてくれた団員。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何よりもこの場を共有しているすべての人に、ありがとうと言う代わりに、頭を下げた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0305
White_Joker "「[firstname]、どうだった？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小声で問いかけてくる声は、果たしてどちらのジョーカーか。\n
だが、白であろうと黒であろうと、返す言葉は変わらない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（ええ、楽しかった）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「……楽しかったわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今まで知らなかったもの、このまま知らなかったかもしれないものに感謝を込める。"

$ hi_mes()
hide t_jo5_13
pause 2

scene circus with ImageDissolve("gui/stripe_l.png", 1.6, ramplen=128, reverse=True)
scene map_bg_joker_day with ImageDissolve("gui/stripe_l.png", 2.4,  ramplen=128, reverse=True)
##endmemory
jump fushigi_end_joker ##I think
