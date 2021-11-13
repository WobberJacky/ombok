
scene black
with dis
label fushigi_end_mermaid1:

play music dream_inside_p_ali

scene black
with dis

scene bg_gen07_sc2
with dis
$ clockanim()


scene bg_gen07_sc1
with Dissolve(1.2)
play sound se_0570
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "身体を包み込んでいる不思議な感触。\n
薄く目を開いた先には、深い青が広がっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（また、夢？）"


$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……ナイトメア？」"

play sound se_0139
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呼びかけた声は水の中で反響した。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（ああ、やっぱり夢ね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水中で声がこんなに響くはずがない。"


$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「ナイトメア、いるんでしょう。\n
いい加減に姿を見せてよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（今度は一体何をするつもりなの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、いつもなら呼べばすぐに現れる夢魔が出てくる気配は一向になかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「ナイトメア、どこにいるの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（夢はあなたの領域なんだから、聞こえないはずがないって言っていたじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普通の声だけでなく、心の声でも呼んでみたが、それでも周囲に誰かが現れる気配はない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（誰も、いないの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の周囲から生まれる水音を除けば、完璧と言ってもいい静寂が広がっていた。"

play sound se_0139
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（本当に、誰もいない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、夢は本来一人でみるものだ。\n
誰かと一緒にみるほうがおかしい。"


$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（この世界に来てから、おかしなことばかり起きるから……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰かがいる夢にも慣れてしまった。"

play sound se_0139
$ flash_blue(.2)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Lorina "「[firstname]」"

$ flash_blue(.2)

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_4")
T "（姉さん……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（やっぱり、これは夢なんだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水の奥底から響いてくる声は、私の記憶の中にあるもの。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "優しくて、完璧な……。\n
この世界にはいないはずの人。"

play sound se_0708

show white onlayer master
with dis

show lori_3 at center
with dis
hide white with spread_short
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0020
Lorina "「おかしなことを言うのね。\n
私はここにいるじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の目の前に姉さんが現れ、完璧な彼女は優しく微笑んでいる。"

hide lori_3
show lori_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0021
Lorina "「さあ、帰っていらっしゃい、[firstname]。\n
いつまでも、そんな夢ばかりに捕らわれていては駄目なのよ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「…………」"

hide lori_9
show lori_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice ari_f0022
Lorina "「夢は、いつか覚めるものだもの、魔法だって、ずっとは続かないわ。\n
……ほら、よく見てちょうだい」"

play sound se_0671
show t_end_mermaid1 onlayer master
with dis
hide lori_16
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "諭すような穏やかな声のまま、姉の姿が人魚二人に変わった。\n
驚く私の手には、見覚えのないナイフが握らされている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0055
Mermaid "「帰りましょう、今ならまだ間に合うわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0020
Mermaid "「元の姿に戻るの、そのためにはどうすればいいのか、分かっているでしょう？\n
もう、時間がないわ、早く……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「わ、私は……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（これは、どこまでが夢なの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢だとしたら、どうしてここにナイトメアが出てこないのか。\n
これほど切実に彼を呼んだことはなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（悪い夢なら、早く覚めてほしいのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "握られたナイフの柄の冷たさが、身体の芯まで染み込んでくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（私が人魚姫なんだとしたら、王子は……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice may_f0056
Mermaid "「あなたをこの海から引き離した元凶にしか、あなたは救えない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人魚は私の心を読んだかのように、はっきり告げる。\n
その微笑からは、温度が感じられなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0021
Mermaid "「彼をその短剣で貫いて、そして」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「そんなの……、出来るはずがないでしょう！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（ペーターを刺すなんて、夢の中でも嫌よ）"

play sound se_0139
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水の中に彼女達の声以外に何かが響いている。"

hide t_end_mermaid1

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（何の音？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_6")
T "（身体が泡になっている？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足と言わず、手と言わず。\n
先ほどまでは唇から漏れるだけだった泡が、今、私の全身から生まれていく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_13")
T "（溶けているみたい）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_13")
Mermaid "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_13")
voice sam_f0022
Mermaid "「手遅れになる前に早く……、あなたが溶けてしまう前に」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（魔法が解けて、泡になったら、私はどうなるのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "想いを伝えることの出来なかった人魚姫。\n
会いたかったはずなのに、何も言えずに逃げるように帰ってしまった私。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（共通点なんて、何も言えなかったことぐらいじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は声を失ったわけでもない。\n
気付いてもらえなかったらという不安感に勝てなかっただけ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（そんな私に、ペーターを刺してまで魔法を解く資格なんてあるはずがないわ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice may_f0057
Mermaid "「本当にそれでいいの？\n
このままでは、あなたは泡になって消えてしまうのよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_17")
voice sam_f0023
Mermaid "「このまま消えたくはないでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「そんなの……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（当たり前じゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "泡になって消えていけるほど、私は諦めのいい人間じゃない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（夢）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（きっと、そうよ。\n
これは夢に決まっている）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（こんなことが起きるなんて夢に決まっているもの……。\n
必ず、目が覚める）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "早く起きなければ。\n
そう思うのに、水音も人魚達も消えてくれない。"


play music tragedy2_a_ali

show per_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ペーター！？」"

play sound se_0139
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "青い世界に浮かび上がる、赤い服。\n
目が合うと同時に、ペーターは私の身体に手を伸ばしてきた。"

hide per_t_01_13
show per_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0216
Peter "「あちらに……、戻りたいですか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（何を言っているの？）"

play sound se_0570
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水と泡の音が邪魔をする。\n
ペーターの声がよく聞こえない。"

hide per_t_01_8

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0058
Mermaid "「早くしなければ、もう戻れなくなってしまう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0024
Mermaid "「消えてしまうわ、可愛い私の妹」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

play sound se_0139
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "泡は次々と生まれて、私の身体を包み込んでいく。\n
一緒に沈んでいくペーターの身体すらも、同じように覆い隠してしまう。"


show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0217
Peter "「だったら、僕があなたを帰します。\n
他の誰にも手伝わせない」"

hide per_t_02_6
show per_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0218
Peter "「どんな形であれ、あなたを幸せに導くのは、僕だけの役目ですから」"

hide per_t_02_11
show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

play sound se_0674
hide per_t_02_10


show t_end_mermaid2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0491
Peter "「僕はあなたを愛しているから、帰りたいと本当に願うのなら、止められません」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「ペーター！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "叫んでも、ペーターは私の持っているナイフに胸を埋める。\n
傷つけたくはないのに、手がナイフから離れてくれない。"

play sound se_0645
$ flash_red(.1)
hide t_end_mermaid2
show splatter onlayer master with grad_r_extrashort
with dis

scene bg_gen07_sc1_c with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_5")
T "「ペーター、嘘」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_4")
T "（夢なら、今すぐ、覚めて）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手の中に生まれた鈍い感覚と、青の世界を染める赤。\n
泡に包まれていても、その色を見間違えるはずがなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「ペーター！\n
しっかりしてっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（嫌……。\n
こんなの、こんな結果なんて、私は望んでいない！）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「ナイトメア、いるなら出てきてよ！\n
早く私の悪夢を消して、目を覚まさせてちょうだい！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（こんな夢をどうして私に見せるのよっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私はこの人を傷つけたくない。\n
こんな悪夢など望んでいなかった。"


show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]」"

play sound se_0332
show white onlayer master with expand
hide per_t_02_6
show usape_11 at center
with dis
hide white onlayer master with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0492
Peter "「[firstname]、[firstname]。\n
……ごめんなさい、僕では、あなたを幸せに出来なかった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターは酷く悲しそうに表情を歪める。\n
その姿は人間から、私をこの世界に連れ込んだウサギの姿に変わった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「違うわ！\n
そんなこと……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ペーターが悪いわけじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視界に映るすべてが赤い。\n
白いウサギから流れてくる赤が、透明な海を染めていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「悪いのは、あなたじゃなくて……」"


show jo_t_02_4 at center
hide usape_11
with grad_b

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jok_f0409
White_Joker "「……そう、よく分かっているじゃないか。\n
その通り、本当に悪いのは君なんだよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ジョーカー……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_13")
T "（どうして、ここに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこからともなく現れた男に、目を見開く。"

hide jo_t_02_4
show jo_t_03_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0410
White_Joker "「おや、忘れちゃったのかい、[firstname]。\n
自分から牢屋に近付く、貴重な囚人は君のほうだ」"

play sound se_0671

scene bg_gen07_scpr with Dissolve(1.5)
hide jo_t_03_14
show jo_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0411
White_Joker "「監獄への入り口はいつでも開いている。\n
だったら、俺が現れるのも自然な流れじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水中に監獄が浮かびあがり、看守のジョーカーはそう言った。"

hide jo_t_01_2
show jo_t_01_2 at left
show usape_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0493
Peter "「殺されたくなければ消えなさい、ジョーカー。\n
僕はどんな手を使ってでも、あなたに彼女を渡す気なんてありません」"

hide jo_t_01_2
show jo_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0412
White_Joker "「ははは、そんな姿で何を言うんだい、ペーター＝ホワイト。\n
君には俺を止めることも、彼女を救うことも出来ない」"

hide usape_5
show usape_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0494
Peter "「……ええ、そんなことは充分に分かっていますよ。\n
だから、あなたではなく……、彼女を、彼女自身に、返します」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！」"

play sound se_0051
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターはそう言うなり、私を引き寄せた。\n
血煙のような赤が、水の中に不思議な模様を刻む。"


show t_end_mermaid3 onlayer master
with dis
hide usape_9

hide jo_t_01_5
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ペーター……？」"

play sound se_0475 volume .80
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計の針の音が耳に直接流れ込んでくる。"

$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「っ」"

play sound se_0638 volume .70
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（頭が痛い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ずきずきと。\n
秒針の振動と同じタイミングで、私の頭の中で痛みが生まれる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0413
White_Joker "「へえ、君のエゴも大したものだね、ペーター＝ホワイト。\n
あんなに忘れさせたがっていたのに、俺に渡すのは、そんなに嫌なんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "嘲笑するジョーカーの声が水を通して響く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターが何をしようとしているのか、彼にはわかっているのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この場で白ウサギの意図を理解していないのは、私だけだった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ペーター、何を……？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice pet_f0495
Peter "「本当は、この世界であなたを幸せにしたかったけど。\n
僕が止めてしまったことで、あなたを監獄に送り込ませるぐらいなら」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice pet_f0496
Peter "「……忘れてしまってください、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「何を言うのよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（忘れられるはずがないじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私をこの世界に引っ張り込んだ、おかしなウサギ。\n
私の話を聞かなくて、気に入らなければすぐに銃を向けて。"

$ flash(.1)
hide t_end_mermaid3
show t_end_mermaid4 onlayer master
with dis
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「……痛っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭痛はどんどん酷くなるばかり。\n
呻いていると、白い手がそっと顔に触れた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0497
Peter "「[firstname]。\n
……あなたのことを幸せにしてあげられなくて、ごめんなさい」"

play sound se_0167
hide t_end_mermaid4
show black onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「！！」"


scene bg_gen07_sc1
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「ペーター……？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「ペーター！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（ジョーカーもいない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "カチッ、と時計の音が響いたのをきっかけに、すべてが消える。"

scene bg_gen07_sc1 with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しきりに囁いていた人魚の姿もない。\n
周囲を見渡しても、誰もいなかった。"

play sound se_0570 volume .70

show t_end_mermaid5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「どこ……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_3")
T "「ペーター、どこにいるのよ！」"


play music badend_gohome_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつのまにか、私の姿は人魚に変わっていた。\n
ヒレに力を込めて、行くあてもない海の中を泳ぐ。"

play sound se_0570
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "奧へ、更に奧へ。\n
海の底へと泳いでいく。"

hide t_end_mermaid5
show t_end_mermaid6 onlayer master with grad_b_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "暗い海の底。\n
光の見えない場所。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "青を通り越した、漆黒の海。\n
その奧にドアが一枚見える。"

hide t_end_mermaid6
show door1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（どうして、こんなところにドアが？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sat_f0012
Door "「開けて」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0044
Door "「会いたい人がいるんでしょう？\n
会いに行きましょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（そうよ、会いたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "会って、無事を確かめないと。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（こんな夢、早く終わらせなくちゃ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引き寄せられるままに、ドアノブに手をかける。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0023
Lorina "「さあ、開けて」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

play sound se_0277
hide door1
show door2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（今、会いに行くから、待っていて。\n
ペーター）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "出口の見えない、海の世界。\n
早く抜けて、あの白いウサギのいる場所に戻らないと。"

play sound se_0278
hide door2
show door4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "（今なら、絶対に迷わずに行けるはずだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今は、ペーターのことしか考えられない。\n
だったら、扉の向こうは彼のいる場所に繋がっている。"

hide door4
show door6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T "（会えないはずがない。\n
ペーターは、ペーターだけは、きっと、待っていてくれる）"

hide door6
show door7 onlayer master
with dis

scene door7
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の誰も私を待っていなくても。\n
あの白いウサギだけは、きっといると信じて、私はドアを抜けた。"

play sound se_0272
hide door7 with dis

hide frame_gen_togaki
hide ali_t_06_16
with Dissolve(5)

stop music

$ renpy.movie_cutscene("endroll_c.mpg")
#return
