label fushigi_blood_start:
hide screen hatter_man_choice
scene map_bg_autumn_day with dis

scene charasel_bg_hatter_day
with dis
label fushigi_blood1:
$ clockanim()

$ hi_mes()

scene b_aut_01
with dis

play music hatter_corridor_p_ali

scene br_01 with Dissolve(1.2)

show bousi_t_02_06 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice may_f0012
Maid "「ボスですか？\n
先ほど書類をお届けしたときには、もう仕事は終わられていましたよ～？」"

hide bousi_t_02_06
show bousi_t_01_05 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice may_f0013
Maid "「門番さん達も、エリオット様も……、お部屋にはいらしていないようでしたし」"

with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの部屋に向かう途中、顔を合わせたメイドはそう教えてくれた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ありがとう。\n
じゃあ、ちょっと捜してみるわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（さすがにブラッドの仕事中に顔を出すのは、気が引けるものね）"

hide bousi_t_01_05

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "若きマフィアのボスにとっての都合がいいタイミングは、なかなか分かりにくい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が暇をアピールするときは大抵多忙なことが多く、そして組織のトップがそうそう暇なはずがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "分かりにくく、そして……。\n
意外なところで、その本心を見せてくるから不思議だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（一言で言っちゃえばひねくれ者なのよね、多分）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッド＝デュプレを一言で表すことなど私には出来ない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の身内である女性に言わせれば「あれはただの馬鹿だ」と一言の元に切り捨てられてしまうだろうが、私はそこまで思い切りよくはない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怖い部分も持っている。\n
慣れた今でさえ、近付くことを躊躇うこともある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（でも、避けるとかえって機嫌が悪くなるし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事で忙しいだろうと思って会いに行くのを控えれば、逆に私の部屋にやってくる始末だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（本当に分かりにくい）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（厄介な人）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼に更に厄介なことを尋ねにいかねばならないのだから、面倒には違いない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「まあいいわ。\n
簡単に口を割るとは思わないけど、たまにはびしっと言わないと調子に乗られるばかりだろうし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドが私のことをよく見ているように、私もまた彼のことを見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "例えば血生臭い仕事が絡むことだったら、彼は絶対に私には見せない。\n
その辺り、徹底した情報管理が出来る男だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオット以下、この屋敷に出入りするもの全員の口を閉ざさせることぐらい、彼には何でもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（でも、今回は絶対に違うわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本気で隠していない。\n
しかし、教えたくないから黙っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（何よ、それ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私への彼らの態度は、おかしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供じみた悪戯でも、もっと凝っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仲間外れのような真似をされなければならないほど、私は彼らにとってお荷物ではないと思っていたのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（ファミリーには入れない）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（でも……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "分かりにくい男の分かりにくい形で、好かれていると思っていたのに。"

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play sound se_0300
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "歩きながらブラッドの部屋の前にやってきて、静かにノックした。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0016
Blood "「ああ、開いている。\n
用があるなら入りなさい」"

play sound se_0285

play music blood_t_ali

scene bl_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「……お邪魔します」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋の中はいつもの光景。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "壁一面を埋め尽くす本棚。\n
中央にある応接セットと、執務机。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薔薇、紅茶、そして本の香りが漂う、帽子屋屋敷の心臓部。\n
そこに男が一人、腰を下ろしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の気分を察してもこの男は悪びれることがない。\n
ほんの少し口元を歪めただけで、いつもと変わらない態度だ。"


show bra_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0017
Blood "「何だ、機嫌が悪そうじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「悪そうに見えるのは、理由が思い当たるからじゃないの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "（白々しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "睨んだまま机の横に立っていると、ブラッドは視線を逸らした。\n
手元の書類に目を走らせているようにも見えるが、素振りだけだ。"

hide bra_t_01_11
show bra_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0018
Blood "「さて……。\n
君がそう言うということは、私に原因があるようだが……、思い当たらないな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなはずはない。\n
ブラッドだけではない。エリオットも双子も、彼らは私に何かを隠している。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「最近、何をこそこそしているの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まどろっこしい駆け引きや言葉遊びを挟む気持ちの余裕もない。\n
単刀直入に聞いた。"

hide bra_t_03_13
show bra_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0019
Blood "「こそこそ？\n
おかしなことを言うな、お嬢さん」"

hide bra_t_02_6
show bra_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0020
Blood "「私達はマフィアだぞ。\n
堂々としているほうがおかしいだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とぼけた彼の顔を見ている限りでは、口を割る気がないのは明らかだ。\n
あくまで知らぬ存ぜぬを貫く気らしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「ふうん、そう。\n
まだ誤魔化すのね？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（この手だけは使いたくなかったけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は意を決して、秘密兵器を取り出した。"

play sound se_0335
hide bra_t_02_2



pause 1



show bra_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0021
Blood "「ん？\n
何だ、お嬢さん、紅茶なら……」"

hide bra_t_03_6
show bra_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「！！」"

hide bra_t_03_5
show bra_t_03_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0022
Blood "「[firstname]、まさか、それは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が手にした缶を見ていたブラッドの顔色が変わった。\n
人に動揺を悟らせない彼がここまで感情を出すなんて、珍しいことだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（ラベルしか貼られていないのに、よく分かるわよね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_14")
T "「これ、この前お城であったお茶会のときに美味しいって言ったら、ビバルディがくれたのよね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「{size=+20}誰かさん{/size}から横取りしたお茶だって言っていたわ」"

play sound se_0759 volume .7
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "掲げ持った紅茶の缶を振ると、茶葉が立てる乾いた音がした。"


hide bra_t_03_17
show bra_t_02_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴくりとブラッドの頬が動く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "紅茶好きの彼が、同じように紅茶好きの女王と茶葉を巡って争っていることは、周知の事実である。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勝敗がどういう内訳になっているかは私も知らないが、この茶葉に関してはビバルディが彼に先んじたのは間違いない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_6")
T "（すごく嬉しそうだったものね、ビバルディ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城に顔を出したとき、自慢げに紅茶の缶を見せてくれた友人の顔を思い出す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が味を誉めると秘密だと言って一缶分けてくれたのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逆に、我らがボスときたら、数時間帯は奪われた紅茶についてくどくどと愚痴を並べていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "負けたのが余程悔しかったらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（その逆もよく見るけど、今回ばかりは負けていてくれて助かったわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おかげでこうやって取引材料に出来る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「……私はあなたほど紅茶好きっていうわけじゃないもの。\n
取引の材料があれば、応じてもいいわよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_2")
T "「あ、別にすごいものなんて期待していないわ。\n
単に、ちょっと口を滑らせてくれればいいだけ」"

play sound se_0759 volume .7
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見せ餌のように、もう一度缶を揺すって音を立ててやる。"


hide bra_t_02_17
show bra_t_03_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私をじっと見ていたブラッドは、しばしの沈黙の末、ようやく口を開いた。"

hide bra_t_03_15
show bra_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0023
Blood "「私相手に交渉を持ちかけるとは、君もずいぶん成長したものじゃないか。\n
お嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「ありがとう。\n
きっと近くにいる人の影響ね、どんどん汚くなっていくわ」"

hide bra_t_03_10
show bra_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_8")
voice blo_f0024
Blood "「お褒めに与り光栄だよ。\n
ふ、ふふふふ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「あはははは」"

hide bra_t_03_9
show bra_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_12")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一緒に乾いた笑いを漏らして、そして同時に睨み合う。"

hide bra_t_02_9
show bra_t_02_18 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0025
Blood "「お嬢さん、私は君のことが嫌いじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（知っているわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドは、一時的にならば嫌いな人間を滞在させる酔狂な人間かもしれないが、私達は酔狂では片付けられないほど長く一緒に過ごしている。"

hide bra_t_02_18
show bra_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0026
Blood "「得難い、貴重な女性だと評価をしている」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「あら、ありがとう。\n
でもね、ブラッド」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "{size=+20}「紅茶の缶を見ながら言っても、説得力はないわよ」{/size} "

hide bra_t_03_11
show bra_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（実は馬鹿にしているでしょう、あんた）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の顔ではなく、彼の視線はさっきから揺れる缶を見ていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呆れたように言う私にようやく視線を向けたかと思えば、ブラッドは小さく息をついてみせる。"


play music quiet_night_a_ali

scene bl_01
with dis
hide bra_t_03_7
show bra_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0027
Blood "「……真正面からいけば、紅茶欲しさに君を口説いているようにみえるだろう。\n
それとも、君はそういう口説き方のほうがお好みか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつのまに手首を掴まれていたのだろう。\n
気付けば間近に迫った顔から逃げられない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぺろりと。\n
まるで味見をするように唇の上を彼の舌が這った。"

hide bra_t_03_1
show bra_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0028
Blood "「紅茶ももちろん欲しい、それは否定しない。\n
だが、今までも、これからも、君と並べる気はないぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（この人は……、本当に質が悪いわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不意打ちのように囁かれる言葉が本心からのものだと分かってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の紅茶好きは度を超している。\n
そんな紅茶以上に求めてくれているのだという感覚に、流されてしまいそうになった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（だけど、まだ頷けない）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「だったら、教えてよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誤魔化されると、不安になる。\n
確かめて、決定的な拒否を向けられることが怖い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（私はあなたほど強くもないし、自信もないのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "親しくなっても、完全に寄りかかることが出来ない。"

hide bra_t_02_2
show bra_t_02_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0029
Blood "「…………」"

hide bra_t_02_17
show bra_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0030
Blood "「だから、何も隠してなどいないと言っただろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「嘘つき」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……そんなに、教えたくないの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "出会ったばかりの頃の私なら、彼に誤魔化されたところで何とも思わなかっただろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だがよくも悪くも、今の私は隠しごとをされていることに、苛立ちと不安がある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（弱くなった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "前だったら、気にしないでいられた。\n
今は勝手に苛々して……、答えてもらえないこの状況に、納得出来ずにいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何だか、とても情けない気持ちだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "泣くつもりなんてなかった。\n
女の涙一つで籠絡できるような相手ではないと分かっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "なのに、じわっと込み上げてくるものが私の意志を裏切っていた。"

hide bra_t_03_13
show bra_t_03_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0031
Blood "「[firstname]？\n
な……、何で……、泣きそうになっているんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「泣いてなんかいないわよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勢い込んできたのに、泣き脅しなんて、みっともないにも程がある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "泣いてなんかいない、泣かされるようなことなんて、何もされていない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思うのに……、ブラッドは目に見えて狼狽している。\n
先刻は私を煙に巻こうとしたくせに、一体どういう変化だろう。"

hide bra_t_03_17
show bra_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0032
Blood "「だが……、その……。\n
泣きそうな顔はしているだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "煙に巻こうとした顔と、たかだか小娘の変化に落ち着かなくなる顔。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どちらも本当で、嘘というわけではないはずなのに。\n
彼のすべてに触れる勇気を私は未だに持てずにいる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（もう少し奧まで手が届くんじゃないの？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（今まで見せてくれなかった顔を見せてくれるの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな欲求が込み上げてしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「なら、教えてよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっと見上げながら口を開けば、ブラッドは視線を逸らした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までのようにすべてを遠ざけられているわけではなくても、誤魔化そうとする態度に変わりはない。"

hide bra_t_03_7
show bra_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0033
Blood "「……だから、その。\n
別に、何も隠してなどいない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

hide bra_t_03_13
show bra_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "互いに、気まずい沈黙。\n
私もブラッドも、素直とは縁遠い性格をしているので、こうなってしまうと意地の張り合いだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこまでこの沈黙が続くかと思っていると、意外にもブラッドが先に口を開いた。"

hide bra_t_02_12
show bra_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0034
Blood "「[firstname]……。\n
その、私は……」"

play sound se_0285
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、彼の言葉はノックなしに扉を開いた誰かのせいで止められてしまった。"


play music elliot_t_ali

show eri_t_02_4 at center
hide bra_t_02_13
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0021
Elliot "「なあ、ブラッド！\n
例のイベントなんだけどさ、やっぱり、ホールじゃなくて庭のほうが……って」"


show bousi_t_01_02 at center
hide eri_t_02_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0009
Maid "「あと、お花の手配の件ですけど～」"



hide bousi_t_01_02
show bousi_t_01_02 at left
show bousi_t_02_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0006
Maid "「あれ……、お嬢様まで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "賑やかな声が、中にいた私達の様子にぴたりと止まる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り返れば、予想通り。\n
メイドと一緒にやってきたオレンジ色のウサギが見えた。"


show eri_t_02_5 at center
hide bousi_t_01_02
hide bousi_t_02_06
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0022
Elliot "「やば。\n
……い、いたのか、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "明らかに、「しまった」という顔をしているエリオットに足を向けながら、声をかける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「ええ、いたわ、エリオット」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「ところで……。\n
その『イベント』って、何のことかしら？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（この屋敷で催し物なんて、予定はないはずだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハウスキーピングが主な私の仕事。\n
マフィアとしての危険な仕事の情報は入ってこないし、望んでもいない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットが口を滑らせた『イベント』は、そういった物騒な響きは含んでいなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城で開かれた舞踏会のように、この屋敷でもルールに基づいてお茶会が開かれたことがある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、大きな催し物であるのならば、メイドの私にもその情報は事前に与えられているはずだ。"

hide eri_t_02_5
show eri_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0023
Elliot "「あ……、いや、その……。\n
気のせいじゃないか、何でもないぜ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の追及に目を泳がせたエリオットに、ブラッドが冷たい視線を向けていた。\n
黙れ、と目線で威嚇しているのが分かる。"


show bra_t_02_14 at center
hide eri_t_01_9
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0035
Blood "「エリオット……。余計なことは言わなくていい、さっさと持ち場に戻れ。\n
指示は後で出す」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……ブラッド」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうしてそこまで隠そうとするのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だって、この屋敷の人間だと思っているのに。\n
完全に隠してもくれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だからといって、覗かせてもくれないなんて。"

hide bra_t_02_14
show bra_t_02_18 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0036
Blood "「…………。\n
君が知る必要はない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴしゃり。\n
余計な口を挟むだけの隙もない、断定の言葉。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「……分かったわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（そう、よく分かった）"

play sound se_0118
$ flash(.1)

play music hatter_corridor_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぱしんと大きな音が響く。\n
手の平に走った痺れに私も驚いていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T "（え？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分でやっておきながら信じられない。\n
ブラッドの頬には、私が叩いたせいで薄い赤が広がっている。"


show eri_t_02_6 at center
hide bra_t_02_18
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0024
Elliot "「あ」"

hide eri_t_02_6
show eri_t_02_6 at left
show bousi_t_01_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0007
Maid "「い、痛そう……」"


show bra_t_03_12 at center
hide eri_t_02_6
hide bousi_t_01_06
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ギャラリーの声にもブラッドは態度を変えない。\n
ただ目の前に立つ私を見て、やがて名前を呼んだ "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「教える必要がないんでしょう、私には。\n
もう、結構よ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットやメイドも目を丸くしているが、驚いているのは彼らだけではない。\n
私も同じだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（……絶対に、避けると思ったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思いっきり叩き付けた手のひらから逃げなかったブラッドは、そんな私をじっと見ている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「あんた達は私がいないほうが好都合みたいだもの。\n
ご希望通り、出ていってあげる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「秘密のお話でも何でもすればいいでしょう！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今は何の感情も見えない瞳から目を逸らし、私はそのまま部屋の入り口に向かう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（こんなつもりじゃなかったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただ話してほしかった。\n
硝煙にまみれるファミリーの一員ではなくとも、この屋敷で共に過ごす人間として認めてくれていると知っていたから。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットの横を抜けると、彼は彼で動揺したまま私とブラッドを交互に見ていた。"


show eri_t_03a_4 at center
hide bra_t_03_12
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0025
Elliot "「な……、ちょ、ちょっと待てよ。\n
[firstname]！ブラッド！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアの横で立っていたエリオットはおたおたとしていたが、背後の男は静かなままだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（ブラッドの、馬鹿！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットとおろおろとするメイドを押しのけ、私はその足で屋敷の外へと飛び出した。"

hide eri_t_03a_4

pause .4
play sound se_0319
$ hi_mes()

scene b_aut_01
with stripe_l_medium

scene map_bg_autumn_day
with stripe_l_medium
##endmemory

play music map_autumn_jok

scene bg_gen_sky_aut_day
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「さて、どこに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に住む友人は何人もいるが、しばらく滞在させてもらうことを考えると……。"

$ routechara = "Blood"
$ hi_mes()
scene map_gen_bg with fade
$ show_mes("frame_gen_togaki")
T "Where do I want to visit?"
$ hi_mes()
show screen fushigi_map1
$ ui.interact()
