
scene map_bg_autumn_day
with dis
label fushigi_end_blood_rose1:
$ clockanim()


scene map_bg_autumn_day
with dis

play music forest_town_road_p_ali

scene s2_01 with Dissolve(1.2)
play sound se_0460
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城から、帽子屋屋敷へ戻る道。\n
そこを歩きながら、私は隣にいる男の非常識さに呆れ果てていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「あんた、何を考えているのよ！\n
城の周りに一体いくつ爆薬を仕掛けておいたわけ！？」"


show bra_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_13")
voice blo_f0152
Blood "「さて、いくつだったかな……。\n
脱出用にいくつかルートを考えておいたから、それに見合うだけは用意しておいたが」"

hide bra_t_01_3
show bra_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_13")
voice blo_f0153
Blood "「まあ、爆薬は限られた場所でしか使えないからな。\n
それほど多くはないはずだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ハートの城の爆破計画でも立てていたのかしら、この人）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逃げ出すにしても、まさかああいう形で爆薬を使うなどと誰が思うだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……まさか、自分で仕掛けたわけじゃないわよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あんなちゃちな変装で女王の前にやってくるような男だ。\n
気まぐれ次第では有り得ると思っていたが、ブラッドは首を横に振った。"

hide bra_t_03_10
show bra_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0154
Blood "「そんなだるいことを私がすると思うか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「いっそそうだったらいいのにと思ったから聞いてみたのよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ハートの城に爆薬を仕掛けるなんて……、危険すぎるわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "領土争いは続いているのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "当然、帽子屋屋敷の人間が爆薬を仕掛けているのを見れば、ハートの城の人間だって黙っていなかっただろう。"

hide bra_t_02_5
show bra_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0155
Blood "「おや、心配してくれないのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「私に心配されなくちゃいけないほど、繊細な神経の持ち主じゃないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「どうせ心配するなら、あなたの下で働く皆のほうを心配するわ」"

hide bra_t_03_9
show bra_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_1")
voice blo_f0156
Blood "「だが、おかげで退屈はしなかっただろう？」"

hide bra_t_03_1
show bra_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_1")
voice blo_f0156_5
Blood "「兵士を皆殺しにして脱出する方法もあったが、あまりスマートなやり方とは言えない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（スマートかそうじゃないかの問題じゃないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "建物の上から飛び降りるにしても、他に方法はなかったのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（地面が爆発したときには、一体何事かと思った）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋ブラッド＝デュプレともあろうものが、本気で自決を考えたのかと思った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「あなたにとってはあれぐらい当たり前のことなのかもしれないけど、死ぬかと思ったわ」"

hide bra_t_03_2
show bra_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice blo_f0157
Blood "「ふっ、マフィアのボスと一緒にいるんだ。\n
平穏ばかりではつまらないだろう？」"

hide bra_t_02_2
show bra_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice blo_f0158
Blood "「スリルによる高揚感は、クセになると思わないか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "{size=+20}「思わない」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "余裕たっぷりに囁かれた言葉を一蹴する。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は退屈嫌いのマフィアのボスとは違う、一般人だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（ゴーランドじゃあるまいし、スリリングな体験なんてごめんよ）"

if renpy.seen_label("fushigi_tag_rose1") == True:
    jump fushigi_end_blood_rose1_3
else:
    jump fushigi_end_blood2
label fushigi_end_blood2:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言葉にブラッドは肩を竦めてみせる。"

hide bra_t_02_8
show bra_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0159
Blood "「やれやれ。\n
まともに話すのは、久しぶりなのに、君は相変わらずつれないな」"

hide bra_t_02_13
show bra_t_02_18 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0160
Blood "「敵地に乗り込んでまで君を奪いにいった恋人を、もう少し労ってくれてもいいだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「……乗り込んできたのはあなたの勝手でしょう。\n
私が頼んだわけじゃないわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「それに……、私、まだあなた達が何を隠していたのか聞いていないんだけど？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "追及すると、彼は意外そうに言った。"

hide bra_t_02_18
show bra_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0161
Blood "「なんだ、まだ覚えていたのか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「忘れるわけがないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（帽子屋屋敷を出たのがそんなに軽い理由なはずがないじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "簡単に忘れられるようなことだったら、屋敷の中で発散してそれで片付けられる。\n
怒りを持続させるのは意外と体力と気力を使うのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "冷めた私の性格からも、長続きしないことは分かっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（それに怒った相手が相手だし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのまま一緒にいても話してくれないのは仕方ないと流してしまったら、何だか悔しいし、寂しい話だ。"

hide bra_t_02_6
show bra_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0162
Blood "「種明かしは最初にするものじゃない。\n
秘めごとは、胸の内に温めておくからこそ、甘さが増すものだとは思わないか？」"

hide bra_t_03_3
show bra_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0163
Blood "「簡単に手の内を見せてしまったら、つまらない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（つまりはまだ話す気はないということ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遠回しな言い方に苛つくだけの気力がないこともあって、冷静に判断してしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が手の内というだけの秘密めいた隠しごと。\n
一体何を彼らは考えているのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（いつまで、そうやって隠し続けられてしまうんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それとも、私にばれたらそんなにまずいことなんだろうか。"

hide bra_t_03_10
show bra_t_02_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

hide bra_t_02_17
show bra_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0164
Blood "「やれやれ……、君は心配性だな。\n
私が、君を哀しませるようなことをするとでも思ったのか？」"

hide bra_t_03_6
show bra_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0165
Blood "「難儀な性分だということは知っていたが、ここまでとは思わなかった」"

label fushigi_end_blood_rose1_3:
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふと何かに気付いた様子で、ブラッドは私の身体に視線を送ってくる。"

hide bra_t_03_13
show bra_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

hide bra_t_03_12
show bra_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「何よ」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手袋を嵌めた指先がそっと首筋を辿ったのを感じた。"

hide bra_t_03_5
show bra_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0166
Blood "「これは、なんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「これ？？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの視線と指先が向いている先は、私の首筋だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが首元にはドレスに着替えた際に渡されたネックレスを下げている以外には、何もつけた覚えはない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（何かあったっけ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首を傾げる私とは対照的に、ブラッドの視線は鋭いままだ。\n
余程気に入らないものがあるらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（とは言っても、自分の首筋なんて鏡でもない限り見えないし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何度か首を捻ってみるが、やはり見えるものではない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「何か付いている？」"

hide bra_t_03_11
show bra_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice blo_f0167
Blood "「ああ、付いている。\n
悪い虫にでも刺されたのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「刺された？\n
ここ……？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（そういえば、ビバルディの部屋で彼女が……）"


show t_bra3_1s onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「！！！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「あ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思い当たることがある。\n
ちくんと小さな痛みを走らせたビバルディの顔が思い浮かんだ。"

hide t_bra3_1s

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（先刻までのばたばたで忘れていた）"

play sound se_0052
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今更遅いとは思いつつ、彼の視線を遮るように手で首筋を隠すが、ブラッドの追及は止まらなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「ええと、その……」"

hide bra_t_03_9
show bra_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice blo_f0168
Blood "「身に覚えはあるようだな。\n
それは何よりだ」"

hide bra_t_01_10
show bra_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice blo_f0169
Blood "「このまま城に逆戻りして、犯人探しをせずにすむ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「犯人って……。\n
単にキスされただけじゃ……」"

hide bra_t_01_3
show bra_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice blo_f0170
Blood "「ほう。\n
キスされただけ、か」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口調は穏やかに。\n
ただその中にこもる温度を確実に下げながら、ブラッドは私をじっと見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "機嫌が悪い証拠だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事や役付きとして振る舞うときには、あまり本心を見せないブラッドだが、ときにはこんな子供っぽい部分を見せる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "全部を覆い隠されているよりは、感情を見せてくれるだけ気を許されているのかもしれないが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（……でも、こんな殺気混じりの不機嫌さは、いらない）"

hide bra_t_01_12
show bra_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice blo_f0171
Blood "「……姉貴か？それとも、騎士か？\n
ああ、あるいは宰相閣下か」"

hide bra_t_03_9
show bra_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice blo_f0172
Blood "「君にキスをしたがる連中ならそれこそあの城の中には、掃いて捨てるほどいるだろうな」"

play sound se_0751
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逃げ道を塞がれるように、近くの木に身体を押し付けられる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……そんなふうに言わないで。\n
それに、ペーターは、今回逃げるのを手伝ってくれたのよ」"

hide bra_t_03_10
show bra_t_02_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice blo_f0173
Blood "「なるほど、その唇の持ち主は宰相閣下か。\n
色仕掛けとは、君も厄介な口説き方を覚えたものだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「だから、そうじゃないって……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

play sound se_0551

play music secret_a_ali

show t_bra_end1 onlayer master
with dis
hide bra_t_02_14

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「あ、いた……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "覆っていた手を外されたと感じたときには、ブラッドの唇が触れている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最初はただ吸い付いているだけだったブラッドだが、何を思ったのか、突然歯を立てられた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "歯形が残るほど、強い圧力を感じる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「～～～～っ。\n
い、痛いんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_10")
voice blo_f0174
Blood "「消毒だ、しばらく我慢しなさい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_9")
T "「消毒って……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それはむしろあの潔癖症の彼が言う台詞だろう。"


play music forest_town_road_p_ali
hide t_bra_end1


show bra_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0175
Blood "「君が、動物に助力を乞わなければならないほど、私を軽んじていたとは思わなかった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「な……。\n
違うわよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドを弱いとは思っていない。\n
だが、同じようにエースが強くないはずがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "得物の違い、立場、戦闘方法は違えど、二人は間違いなく強者だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "現にブラッドはかすり傷とはいえ怪我を負っていたし、エースもまた髪を焦がしている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（でも、あのまま続いていたら、もっと酷い怪我をしていたかもしれない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それは嫌だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それぞれ領地、陣営が異なるもの同士。\n
いずれ決着をつけなければならないのだとしても、どうしても受け入れられないものはある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人とも私の大事な人だ。\n
怪我をしてほしくはなかった。"

hide bra_t_01_9
show bra_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0176
Blood "「では、なんで宰相閣下にキスなんかさせているんだ！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「ペーターじゃないわよ！\n
これは、ビバルディ……、あ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（しまった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つい反射的に答えてしまったが、既に遅い。\n
ブラッドはよりいっそう険悪な顔で私を睨んでくる。"

hide bra_t_02_11
show bra_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0177
Blood "「あの～～～～～～～～女王。\n
私のものに何をする気だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「そういう言い方はやめてよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_11")
T "（自分のお姉さんに対して、何てことを言うのよ）"

hide bra_t_02_3
show bra_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_11")
voice blo_f0178
Blood "「～～～～～～～～を～～～～～～～～と言って何が悪い」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「そこじゃなくて、私があなたのものっていうあたりが……」"

hide bra_t_02_10
show bra_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
voice blo_f0179
Blood "「ほう、まだ私のものではないというのか？」"

play sound se_0551
hide bra_t_02_6
show bra_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
voice blo_f0180
Blood "「こんなに、私の手に馴染んでいるのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "際どい部分に触れようとする男の手を感じて、慌てて身を離そうとするが逆に抑え込まれてしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ちょ、ちょっと！\n
ここをどこだと思っているのよ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "既にブラッドの支配する領土に入っているとはいえ、屋敷に戻ったわけではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（野外で何をする気よ、この～～～～！！）"

hide bra_t_02_2
show bra_t_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice blo_f0181
Blood "「君の肌に残った薔薇の匂いすら気に入らない。\n
これは女王の残り香だろう？」"

hide bra_t_03_14
show bra_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice blo_f0182
Blood "「どうせ身に付けるなら、私の香りにしておきなさい。\n
こんな毒々しい香りは、君には似合わない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「っ！」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "巧みな指先がドレスの裾に触れてきていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「～～～～！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「い、いい加減に、しなさい！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "{size=+20}「この～～～～～～～～！！」{/size} "

play sound se_0062
hide bra_t_03_10


scene t_cut_bra_end1u
with dis
pause .4

scene t_cut_bra_end1
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "密着した姿勢で出来る反撃など、せいぜい足の甲を踵で踏みつけるぐらいだ。\n
遠慮せずに足を動かすと、確かな手応えがあった。"


show bra_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「！！！？」"

play sound se_0596
hide bra_t_03_5
show bra_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「～～～～っ！」"

play sound se_0779
hide bra_t_03_6
show bra_t_02_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「[firstname]……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピンヒールの一撃はさすがに無視出来るものではなかったらしい。\n
苦痛に歪む顔を見て、少し胸がすっとした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "（当然の報いよ）"


scene s2_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_4")
T "「足が大分痛そうね、ブラッド」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_8")
T "「それじゃあ、私、一足先に屋敷に帰ることにするわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もう一度捕まえられてしまったら、今度は逃げられる保証はない。\n
颯爽と彼の横を抜けて私は歩き出した。"

hide bra_t_02_17
show bra_t_03_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0183
Blood "「こ、こら……、待ちなさい、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_15")
T "（……頑張るわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足下のヒールは文字通りのピンヒールだ。\n
痛みを堪えながらブラッドがこちらに手を伸ばしてくるが、私のほうが早い。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「じゃあ、お先に」"

play sound se_0623
hide bra_t_03_17

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "伸ばしてきた手を振り払うように早足で歩き始める。\n
とはいえ、私自身慣れない靴なので、走ったりは出来ない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0184
Blood "「君の足癖の悪さは知っていたが……。\n
つぅ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呻く声に、一瞬やりすぎたかと罪悪感が掠めた。\n
しかし、ここで戻ってまた迫られては元も子もない。"

play sound se_0621
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（さすがに骨折まではしていないだろうし、放っておこう）"


play sound se_0623
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屋敷までの距離は短い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それに、あれだけの高さから飛び降りることを考えるような男だ。\n
まさか私が踏みつけたぐらいでどうこうするほど、柔ではないだろう。"

$ hi_mes()
if renpy.seen_label("fushigi_tag_rose1") == True:
    jump fushigi_end_rose1_1
else:
    jump fushigi_end_blood_2
