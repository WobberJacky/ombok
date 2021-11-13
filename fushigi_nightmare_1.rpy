
scene map_bg_winter_day
with dis

scene charasel_bg_tower_day
with dis
label fushigi_nightmare1:
hide screen tower_man_choice
$ clockanim()

$ hi_mes()

play music tower_stairs_down_p_ali

scene cki1_01 with Dissolve(1.2)

show toustaff_a1_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kat_f0021
Tower_Employee "「グレイ様、時計屋の仕事場周辺と、上下の階には特に問題はありません」"

hide toustaff_a1_1
show toustaff_a1_1 at left
show gre_t_01_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0126
Gray "「そうか。\n
一部屋だけですんだだけ僥倖と言うべきだろうな」"

hide gre_t_01_12
show gre_t_01_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0127
Gray "「ナイトメア様にも困ったものだ。\n
しばらくは自室で大人しく静養していてもらわなければ」"

hide toustaff_a1_1
show toustaff_a1_1 at left_center
hide gre_t_01_15
show gre_t_01_15 at center
show toustaff_b1_5 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hos_f0043
Tower_Employee "「……また、書類が溜まりますね」"

hide toustaff_a1_1
show toustaff_a1_7 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kat_f0022
Tower_Employee "「元々、大量に溜まっていましたしね」"

hide gre_t_01_15
show gre_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gra_f0128
Gray "「それを言うな。\n
俺だって頭が痛い」"

play sound se_0415
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "階段の踊り場。\n
呆れたように溜息をつくグレイの姿をようやく見つけて駆け寄った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「グレイ」"


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "主に代わって塔の機能を取り仕切る彼に声をかけると、グレイは驚いたようにこちらを見た。"

hide gre_t_01_6
show gre_t_03_3 at center
hide toustaff_a1_7
hide toustaff_b1_5
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0129
Gray "「[firstname]、君も煙を吸ったりして大変だっただろう？\n
もう少し休んでいたほうがいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（本当に、この塔の人達は私に甘すぎる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小火が起きた原因でもある私を責めたっていいはずなのに、むしろ、労ってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "甘くて、優しくて……。\n
卑屈な私は、勝手に落ち込むばかりだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（責められたほうが楽なこともあるのに、絶対にしない）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ううん、私は大丈夫。\n
それよりも……、ナイトメアは、今部屋かしら？」"

hide gre_t_03_3
show gre_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gra_f0130
Gray "「ああ、ナイトメア様なら、部屋で休んでいるが……。\n
どうしたんだ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「さすがにちょっとまずかったかなって……、様子を見に行こうと思うんだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「……もう行っても、大丈夫？\n
具合が悪いなら、また後で行くわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの具合を一番正しく理解しているのは、補佐である彼だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "面会さえ難しい状態なら断ってくるだろうと思ったが、グレイはいつものように静かに微笑むと、首を横に振った。"

hide gre_t_02_10
show gre_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0131
Gray "「もちろん、構わない。\n
君が顔を見せてくれたほうがあの方も喜ぶだろうから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が顔を見せたところで、気分に変化はないと思うが、伝えても寂しくなるだけだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「それじゃあお見舞いに行ってくるわ」"

hide gre_t_02_2
show gre_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
Gray "「…………」"

hide gre_t_02_9

play sound se_0774
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "金色の瞳に見送られて、私は階段を上り始めた。"

$ hi_mes()

scene cki1_01 with Dissolve(.8)

scene cr_01
with stripe_l_long
play sound se_0290
pause .5
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ナイトメア、入るわよ」"

play sound se_0285

scene n_01 with ImageDissolve("gui/stripe_l.png", 1, ramplen=128, reverse=True)

play music nightmare_t_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ノブを回して室内に入ると、そこはひっそりと静まり返っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "室内の奧に備え付けられた寝台には、横たわる人の影がぼんやりと浮かび上がっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（眠っているのかしら）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（それとも、また貧血とか？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ、倒れることも珍しくもないクローバーの塔の領主様だ。\n
少しずつ近付いていって、その顔を覗き込むと、突然その目が開いた。"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「っ！？」"


show nai_s_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice nig_f0218
Nightmare "「そんなに驚くことはないじゃないか、[firstname]。\n
うう……、のどがイガイガする」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「まだ煙が残っているんでしょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目を開けただけで苦い顔をする相手に、呆れるように告げた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの部屋にあったものは、彼の仕事に関わるものばかりだ。\n
時計を扱うあの部屋には、機械油や金属が多々揃っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "金属はともかく、油の中には火がつけば酸化して身体に刺激を与えてしまうものがあったとしても、仕方ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……有毒ガスが出なくて、本当によかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "健康な人ならともかく、身体の弱いナイトメアではどうなっていたか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（吐血どころか、意識不明の重体とか、寝たきりで一歩も動けない体だとか……）"

hide nai_s_02_10
show nai_s_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice nig_f0219
Nightmare "「き、君はなんてことを想像しているんだ、[firstname]！\n
寝たきりで一歩も動けない体だなんて……」"

hide nai_s_01_12
show nai_s_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice nig_f0220
Nightmare "「うう……、大声を出したせいで、また気分が。\n
げほ、ごほ……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……そういうところが、危険な想像をかき立てるのよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（特に、あなたときたらこの世界でも類を見ないほど身体が弱いんだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怪我が数時間帯で元通りに治るこの世界でも、ナイトメアの病気は一向によくならない。"

hide nai_s_01_10
show nai_s_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0221
Nightmare "「う……、わ、私だって、好きで病弱なわけではなくてだな。\n
これはいわゆる一つの才能というか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "{size=+20}「そんな才能、何の役に立つのよ」{/size} "

hide nai_s_01_4
show nai_s_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice nig_f0222
Nightmare "「……うっ、ひ、酷い」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の場合は既に才能云々ではなく、ただの弱点でしかないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（肝心なときには血を吐いて倒れて、その上簡単に意識をなくすし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが部下になる前からずっとこの調子だったとしたら、筋金入りの病弱具合だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それ以前、一体どうやってこの病弱な夢魔は仕事をしていたのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（グレイがいない当時からつきあっている部下を、尊敬するわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逃亡する、血を吐く、倒れる、寝込む。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（何だかとんでもなく駄目な領主にしか聞こえない）"

hide nai_s_02_7
show nai_s_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice nig_f0223
Nightmare "「[firstname]、それはあんまりだろう。\n
私だって、びしっと出来るときは出来ているじゃないか」"

hide nai_s_02_10
show nai_s_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice nig_f0224
Nightmare "「だいたい本来の私は夢の中にこもっているのが筋であって、外に出るのはお門違いというか……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「だったら夢の中に仕事を持ち込んで片付けるなり、何なりすればいいのに」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……あ、でも夢の中でもしっかりしているとは言い切れないか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が現実に出て来なかったハートの国を思い出す。\n
夢の中でまで盛大に吐血していたのは、幻覚ではないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（どこにいても、身体の弱さだけは変わらないわよね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（特に、今は弱っているわけだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "有毒ガスは出なかったにせよ、部屋に立ちこめていた煙は身体にいいものではなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "特に身体が弱いわけでもない私でさえ、のどを痛めたのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "体力も抵抗力もない彼にとっては、散々なことだっただろう。"

hide nai_s_03_7
show nai_s_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0225
Nightmare "「まったくだな。\n
グレイには延々と治療中にも説教を受けたし……」"

hide nai_s_03_6
show nai_s_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0226
Nightmare "「あいつ、絶対に私に対する尊敬が足らない。\n
私は偉いのに……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアは体をベッドに預けたまま、脇に座っている私に愚痴る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（私は？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（私に対しての文句はないの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "綺麗なものだけで出来ているわけではない私は、心を読まれることにいつまで経っても慣れない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも、つい胸の内から問いかけてしまうのは……、口に出して確認するだけの勇気がないからだ。"

hide nai_s_03_8
show nai_s_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0227
Nightmare "「私が君に何を言える？\n
こんなことを起こして、どうするつもりだ……、とでも？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（そうじゃないけど……。\n
あなたがサボったことも原因だけど、煙管の扱いを間違えた私にも責任はあるわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアが喋り、私は心の中で返す。\n
このやりとりにも、最初は戸惑っていたが、はっきり口に出来ないときには、都合がいい。"

hide nai_s_03_12
show nai_s_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0228
Nightmare "「言えるはずがないだろう。\n
そもそも最初に時計屋の部屋に逃げ込んだのは私だ」"

hide nai_s_03_9
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0229
Nightmare "「君を責めるのなら、その前に自分の咎を責めるべき。\n
それが上に立つものの仕事というものだよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「あなたが悪くないとは言わないわよ。\n
むしろ自覚があるのなら、仕事はきちんとすべきだと思う」"

hide nai_s_02_1
show nai_s_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0230
Nightmare "「せ、せっかく私が励まそうとしているのに……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「それでも、あなたを含めて、塔の人達は私に甘いわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒られて、謝る。\n
そのやりとりが出来ることで、幾分罪悪感が薄まる気がしていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（安易な考えなのかもしれないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私に甘い人達相手だからこそ、申し訳なくなる。\n
そう思うと、ナイトメアは柔らかな視線を向けて、頷いた。"

hide nai_s_01_4
show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0231
Nightmare "「君に罰を与えるのは、いつだって他人よりも、君自身だ。\n
私が余計な口を挟むまでもないよ」"

hide nai_s_01_11
show nai_s_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0232
Nightmare "「それに、君をいじめて、これ以上グレイや時計屋の機嫌を損ねるほうが怖い」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後はわざと茶化したように言ったが、それが本心ではないことぐらい、心の読めない私にだって分かる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（意地悪）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（意地悪なのに、優しいなんて、ずるい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "面と向かって責められるべきだったのに、許されてしまう。\n
この世界の人は皆私に甘すぎる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（私が余所者で、この世界の住人じゃないから？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "余所者で、お客さんだから、失敗をしても、誰も責めはしない。\n
仲間として見られてはいないのかと、淋しい気持ちになる。"

hide nai_s_02_8
show nai_s_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0233
Nightmare "「それは違うな、[firstname]。\n
余所者だから甘いわけじゃない」"

hide nai_s_02_11
show nai_s_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0234
Nightmare "「君が責任を感じすぎているだけで、無理矢理許しているわけでもないよ。\n
私達だって、君が危険なことに首を突っ込めば、叱ってでも止めるさ」"

hide nai_s_02_13
show nai_s_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0235
Nightmare "「私達は、君が好きだからね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひんやりとした冷たい手が頬に触れる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の手はいつでも冷たい。\n
例外は高熱を出して倒れているときぐらいだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「小火だって、充分危険なことだわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（ユリウスの部屋だって、あんなことになって……。\n
ううん、彼の仕事場だけじゃすまなかったかもしれない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だって、右も左も分からないような子供ではないのだ。\n
火による災害がどんな事態をもたらすか、簡単に想像出来る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「怒ってくれればいいのに」"

hide nai_s_03_11
show nai_s_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice nig_f0236
Nightmare "「君は、いつまで経っても許されるのが下手な子だな。\n
怒られないほうがきついのは分かるが……」"

hide nai_s_03_4
show nai_s_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice nig_f0237
Nightmare "「私も、普段自分が怒られることのほうが多いから、どう叱ったらいいのか分からないんだよ。\n
すまないな、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「あなたが謝ることじゃないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（私が望むから怒るんじゃ、意味がないし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでは単に、私の我侭に付き合わせてしまうだけだ。"

hide nai_s_03_9
show nai_s_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0238
Nightmare "「ふ……。\n
それもそうだな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "眼帯で覆われていない片眼が、力を抜いたように瞬いて、小さく視線を動かした。"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その視線が一カ所で止まったかと思うと、私の髪に手を伸ばしてくる。"

hide nai_s_03_10
show nai_s_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0239
Nightmare "「ん？どうしたんだ、[firstname]。\n
この髪の毛は……？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ、これ？\n
少し焦げちゃったみたいね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慌てていて気付かなかったのだが、言われてみれば彼の手が触れている部分は少し焦げている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（一部屋があれだけ燃えて、火傷もせずに、髪が少し焦げただけなんだから、大したことないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目の前の病人のように、寝込んでいるわけでもない。"

hide nai_s_02_13
show nai_s_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice nig_f0240
Nightmare "「大したことがないわけあるか、大事件だ！\n
他に火傷とかはないのか、[firstname]！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「お、落ち着いてよ。\n
大丈夫よ、これだって本当に先端が焦げただけだから」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "急に起き上がろうとした相手を、焦ってベッドに押し戻す。"

hide nai_s_02_6
show nai_s_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0241
Nightmare "「焦げただけ……、じゃない！\n
髪は女性にとって大切なものだろう、それを……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「平気よ、ちょっとはさみで切ればすむ話だし」"

hide nai_s_02_10
show nai_s_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice nig_f0242
Nightmare "「そういう問題じゃ……。\n
……う、急に起き上がったから、眩暈が」"

play sound se_0328
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ずるずると。\n
先ほどまで勢い込んで起き上がろうとしていたナイトメアは、とうとう力尽きたらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベッドの中に沈み込んでいく。"

hide nai_s_02_9
show nai_s_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0243
Nightmare "「うう、気持ち悪い。\n
君は無事だと思っていた自分にも腹が立つ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぼそぼそとそんなことを言って、ナイトメアはしょんぼりとした様子でシーツを被った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とはいうものの、白いシーツの下から少しだけ髪の毛がはみ出て、完全に隠れ切れていないのが、いかにも彼らしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いじいじとくるまっている姿は、彼が自称する蓑虫そのもの。\n
思わず笑みが浮かびかけたが、それも一瞬だけだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（それでも、やっぱり……。\n
あなたも、私を怒らないのね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「髪ぐらい、何でもないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "痛くもないし、痕が残るようなものでもない。\n
仕事場が燃えてしまったユリウスのほうが、よっぽど無事ではないと思う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（大事なものばかりだったはずなのに、不在中に部屋が燃えていたりしたらショックに決まっている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、そんなユリウスも、私を責めたりはしなかった。"

hide nai_s_01_7
show nai_s_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0244
Nightmare "「君の責任感には、本当に完敗だよ。\n
……君が自分を責めていることを知っているのに、私達からは何も言えないさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（そうかもしれないけど、私の気がすまないのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "眉を寄せると、ナイトメアがもそもそと微動する。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"


play music honobono2_a_ali
hide nai_s_01_10
show nai_s_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice nig_f0245
Nightmare "「この塔にいると、そうやって自分を責め続けてしまうだろう。\n
それなら少し、外で気分を変えてくるといい」"

hide nai_s_02_13
show nai_s_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice nig_f0246
Nightmare "「だが、[firstname]、君の家はここだ。\n
気持ちの整理がついたら、帰ってきてくれ」"

hide nai_s_02_1
show nai_s_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice nig_f0247
Nightmare "「……待っているから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "シーツ越しのくぐもった声。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔も見えないのに、柔らかく微笑んでいるような気がしたのは、私の都合のいい解釈なのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "優しく、大切に思われていることが伝わってくる。\n
そうなると、単に謝るだけでは納得できそうにない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……この場所を離れてみるのも、手かもしれないわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今回の火事でナイトメアが寝込む状態になっている。\n
人手はいくらあっても足りないだろうし、彼がいなくては進まない用件も多い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな中、こんな気持ちのままで仕事をしても迷惑になってしまうかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「それじゃあ、グレイに話してから、外で反省してくる。\n
私がいないからってみんなに迷惑をかけちゃ駄目よ」"

hide nai_s_02_2
show nai_s_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0248
Nightmare "「何を言うんだ。\n
私は仕事の出来る、立派な上司だぞ」"

hide nai_s_03_8
show nai_s_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0249
Nightmare "「君に無用な心配など……、げふっ、ごふっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然シーツの塊がごほごほとむせはじめる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「はいはい……、そうね、大丈夫よね」"

hide nai_s_03_2
show nai_s_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice nig_f0250
Nightmare "「そ、そうだとも……。\n
何も心配することなんて……がほっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（シーツの中でまで吐血していないでしょうね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアでは、有り得ない話ではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（先刻までは格好よかったのにな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の場合、格好よさまで夢のように儚いものらしい。"

hide nai_s_03_5
show nai_s_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice nig_f0251
Nightmare "「な、何を言うっ。\n
私はいつでも、格好いい……う、ぐっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「分かったから、無理して喋らないでちょうだい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背中をさすり、発作が落ち着くまで待ってから、静かに部屋を出た。\n
その足でグレイに事情を説明し休みをもらう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして既に時間帯が移り変わっている塔の外へ歩き出した。"

hide nai_s_03_6

$ hi_mes()

scene n_01 with Dissolve(.8)

scene cki1_01
with stripe_l_medium

scene charasel_bg_tower_day
with stripe_l_long
##endmemory

play music map_winter_jok
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「さて、どこに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に住む友人は何人もいるが、しばらく滞在させてもらうことを考えると……。"
scene map_gen_bg with fade
$ routechara = "Nightmare"
$ show_mes("frame_gen_togaki")
T "Where do I want to visit?"
$ hi_mes()
show screen fushigi_map1
$ ui.interact()
