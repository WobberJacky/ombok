
scene map_bg_spring_day
with dis

scene charasel_bg_castle_day
with dis
label fushigi_peter1:
hide screen castle_man_choice
$ clockanim()

$ hi_mes()

scene hm_spr_01
with dis

play music castle_corridor_p_ali

scene hr_01 with Dissolve(1.2)
play sound se_0774
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「ペーターは確か部屋に戻ったはずだったけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城の中を移動しながら、彼の部屋へと向かう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "身体に残る水滴はまだ冷たさを残しているが、これくらいならすぐにでも乾くだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "汚れの残らない世界。\n
濡れた服も、知らない間に乾いてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（ペーターが風邪をひくほど弱いとは思わないけど、でも……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まずは、謝らなければ。\n
逸る気持ちが足を速める。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "早足で角を曲がったところで、人の気配に気付いて、慌てて足を止めた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"


show viv_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice viv_f0211
Vivaldi "「ん……？\n
ああ、おまえか、[firstname]」"

hide viv_t_02_12
show viv_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice viv_f0212
Vivaldi "「どうしたのじゃ、そんなに急いで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ビバルディ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女もあの水騒動でずぶ濡れとなったはずだが、すっかりいつもどおりだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とはいえ、機嫌までは回復していないらしく、私を見る目にもまだ苛立ちが残っている。"

hide viv_t_01_13
show viv_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0213
Vivaldi "「おまけに、何だ、その格好は。\n
濡れたままではないか」"

hide viv_t_03_11
show viv_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0214
Vivaldi "「そんな姿で歩き回っていたら、風邪をひいてしまうぞ。\n
早く着替えておいで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女自身ずぶ濡れになって苛ついているはずなのに、女性らしい気遣いに嬉しくなった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ビバルディ、ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの騒動での片付けをしていたせいで、私のメイド服はまだ濡れたままだが、大したことはない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（元の世界にいたときには、予定外の通り雨にずぶ濡れになったことだってあったし……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "髪から滴るほどびしょ濡れになったわけではないのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "全身が少ししっとりと濡れている程度なのだから、着替えよりも他のことを優先させたほうがいい。"

hide viv_t_01_7
show viv_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0215
Vivaldi "「馬鹿なことを申すな。\n
うちの殺しても死ななそうな男どもとは違うのだぞ」"

hide viv_t_03_7
show viv_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0216
Vivaldi "「女が身体を冷やすものではない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「本当に大丈夫よ、このくらいどうってことないわ。\n
心配してくれてありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心配をかけてしまっているのは心が痛むが、どうしても先にペーターに会って話がしたかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディが口を開くよりも先に、先手必勝とばかりに、話題を逸らすことにする。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「それよりもビバルディ。\n
ペーターを見なかった？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "潔癖症の彼のことだから、きっと自室に戻って汚れを落としているはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城の宰相という地位にあるせいか、彼の部屋には専用のバスルームが設置されている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確認の意味で尋ねたのだが、女王は形のよい眉を顰め、私を一瞥する。"

hide viv_t_01_9
show viv_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0217
Vivaldi "「ホワイトだと……？\n
わらわは見ておらぬが、おまえ達、知っておるか？」"

hide viv_t_02_11
show viv_t_02_11 at left
show heisi_t_02_09 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0006
Soldier "「いえ、私は存じておりません。\n
お役に立てず、申し訳ありません」"

hide viv_t_02_11
show viv_t_01_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0218
Vivaldi "「本当に役立たずじゃな。\n
おい、そこのもの、こやつの首を……」"

hide viv_t_01_8

hide heisi_t_02_09
show heisi_t_02_09 at left
show siro_t_02_08 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0008
Maid "「あの……、ホワイト卿でしたら、先ほどお部屋のほうへ戻られているのをお見掛けいたしましたわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「部屋ね、ありがとう！\n
ビバルディ、いいのよ、いいの！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「ペーターの居場所が分かって助かったわ！\n
だから、その人は処刑しないで、ね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（たかが居所を知らなかっただけで、首を刎ねられるなんてとんでもない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慌てて言い募ると、美しく冷酷な女王は、少し不満げだが納得してくれたようだった。\n
振り上げた腕を下げてくれる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（……危ない危ない）"


show viv_t_01_5 at center
hide heisi_t_02_09
hide siro_t_02_08
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice viv_f0219
Vivaldi "「そうか？\n
ふむ、おまえは控えめじゃな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（控えめとかそういう問題じゃないけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何にしても、処刑を思い留まってくれたので、よしとしよう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "処刑されそうになっていた兵士は小さく礼をしてきたが、元はといえば私がペーターの居場所を聞いたせいなのだ。\n
逆にこちらが申し訳なく思ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「それじゃあ、ちょっとペーターのところへ行ってくるわね。\n
それと……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「ビバルディにも話があるの。\n
後から、会いに行こうと思っていたんだけど……」"

hide viv_t_01_5
show viv_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice viv_f0220
Vivaldi "「おや。\n
女同士の楽しい内緒話か？」"

hide viv_t_03_12
show viv_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
voice viv_f0221
Vivaldi "「ふふふ、それはぜひ聞かねばな」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（……楽しい話じゃなくてごめんなさい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "期待に満ちた眼差しで私の顔を覗き込んでくる彼女に申し訳なく思いながら、耳元にそっと唇を寄せた。"

hide viv_t_03_1

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0300
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ペーター、入っても大丈夫？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（返事がないわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "廊下で会ったビバルディと別れてすぐにこの部屋に来たのだが、擦れ違いになってしまったのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（まさか中で倒れているとは思わないけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「ペーター？」"

play sound se_0282
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "回らないと思っていたノブは、簡単に回ってしまった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（鍵をかけていないのかしら、あの人）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "刺客が横行するハートの城の中で、そんな無防備なことをするとは思えないが、現にドアは簡単に開いてしまった。"


play music peter_t_ali

scene p_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "中を覗けば、いつものギンガムチェックの赤い部屋がそこにはある。\n
だが、その中にいるはずの白いウサギはどこにもいなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここは、私にとっても勝手知ったる恋人の部屋。\n
何度も招かれているのをいいことに、そのまま中へと入る。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「……[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0039
Peter "「え、す、少しだけ待っていてくださいっ。\n
今、行きますから！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少しくぐもったように聞こえた声は、部屋の奥から響いてきて、そして……。"

play sound se_0153
show t_per1_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ペ、ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice pet_f0040
Peter "「すみません、[firstname]。\n
いくら水音があったとはいえ、愛しいあなたの声が聞こえなかったなんて……、僕の失態です！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
Peter "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
voice pet_f0041
Peter "「どうしました？\n
何だか顔が赤いようですが……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "シャワーでも浴びていたのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まだ髪から水を滴らせているペーターは、薄手のシャツにタオルを掛けただけの酷くラフな姿で出てきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "白い肌と、残った水滴。\n
思わず、視線のやり場に困ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「あ、う、ううん。\n
何でもない……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（何で、こんな格好にいちいちどきどきしちゃうのよっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元々顔立ちは折り紙付きのペーターだ。\n
それが、文字通り水の滴るいいウサギになっているだけなのに。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0042
Peter "「本当ですか？\n
何だかどんどん顔が赤くなってきていますが……」"

hide t_per1_1
show t_per1_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の額に手を当てたペーターが目を見開いた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0043
Peter "「熱があるじゃないですか！？\n
ああ、こんな濡れたままの姿でいるから……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0044
Peter "「こんな濡れた服なんか今すぐ脱いでくださいっ。\n
今ならまだバスルームも暖かいですから！早く温めないと！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私をバスルームに連れて行こうとするペーターの手の熱さに、また顔の熱が上がる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "「い、いい！\n
大丈夫だから、本当に！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（この上、バスルームなんて借りたら、おかしくなりそう）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice pet_f0045
Peter "「でも……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ちょ、ちょっと話をしに来ただけだから！\n
部屋に戻って、着替えれば大丈夫よ」"

hide t_per1_2
show t_per1_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice pet_f0046
Peter "「僕にお話……、ですか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚いたように私の顔を覗き込むペーターの視線を受けると、何故かどきどきしてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そっと視線を外して、早口に言った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「皆にも迷惑かけちゃったから、ちょっと頭を冷やしてこようかなって。\n
ビバルディにも断ってきたけど、ペーターにもちゃんと言わなくちゃって思って」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pet_f0047
Peter "「頭を冷やすって……。\n
どういうことですか、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「うん。\n
少し……、ハートの城の外へ反省に行こうかなって」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
voice pet_f0048
Peter "「でしたら、僕も一緒に……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_8")
T "（そう言うと思ったのよね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「駄目よ。\n
悪いことをしたのは、私でしょう？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（ここにいたら、許されてしまう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディもペーターも私を責めない。\n
彼らだけではない、城の誰もが許してしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "でも、許されることを当然だと思いたくない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（矛盾しているかもしれないけど、大事だから、甘えたくない……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice pet_f0049
Peter "「[firstname]。\n
いえ、やはりあなたを一人で外に行かせるなんて……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「じゃあ、ペーターがいなかったら、私はどこへ帰ればいいの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_4")
Peter "「！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_4")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉を探すように逸らされた視線と、ぴんと立ち上がってすぐに垂れた長い耳。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界にわたしをひっぱりこんだときのペーターなら、絶対に見せなかった反応だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（分かってくれている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私がどういう性格をしているのか、この白ウサギはもう知っているはずだ。\n
だから、私の意志を尊重することと自分の感情を天秤にかけて困っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「あなたが私の帰る場所なんだから、待っていてよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（私が迷わないように）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（帰り道を定められるように）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_11")
voice pet_f0050
Peter "「あなたは、本当に……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「嫌な子？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦笑いを浮かべて問いかけると、答えるよりも先に、彼は私を抱きしめた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice pet_f0051
Peter "「いえ」"

play sound se_0551
hide t_per1_3
show t_per1_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice pet_f0052
Peter "「僕にとって、もっとも優しくて、そして残酷なことを言う。\n
本当は行かせたくなんかありません……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（そうね。\n
でも、あなたは私を行かせてくれる）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「身体、また汚れちゃうわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "洗い立ての身体は、まだシャワーの余韻か、いつもよりも温かい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "汚れ一つなかったはずなのに、私の服に残った泥が付いてしまうのが、とても惜しい気がした。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0053
Peter "「あなたに触って汚れたりなんかしません。\n
あなたこそ、こんなに冷えている」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「……すぐ、温まるわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "抱き寄せられているだけで、心地よい石鹸の香りが全身に広がってくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T "「だって、ペーター、あなたが……、あったかいもの」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_8")
T "（……胸の中がもうこんなにほっとしている）"

hide t_per1_4

$ hi_mes()

scene hr_01
with stripe_l_medium

play music castle_mae_p_ali

scene hm_spr_01
with stripe_l_long

show per_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0054
Peter "「いいですね、[firstname]。\n
変な相手にはついていかないこと、あと、悪いものは食べないでくださいね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（私は子供か）"

hide per_t_02_11
show per_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice pet_f0055
Peter "「ちょっとでも近付く相手がいたら、問答無用で殴っていいですから！\n
それとも、やっぱり護衛に誰か……」"

hide per_t_01_1
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice pet_f0056
Peter "「顔なしでもあなたが逃げる間の盾ぐらいには」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「……逆に暴行罪で訴えられそうだから、遠慮しておくわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城の出口まで見送りにきてくれたペーターは、それでも不安そうな顔で私を見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "やっぱりついていこうかどうしようかと悩んでいるのが手に取るように分かった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかしここでペーターについてきてもらっては、城を出る意味がない。\n
せめて心配をさせないよう、精一杯の明るい声で別れを切り出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ここまででいいわ。\n
じゃ、行ってくるわね」"

hide per_t_02_8
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Peter "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不安そうに見送っているペーターに手を振って応えると、私はそのまま歩き出した。"

play sound se_0624
hide per_t_02_6

$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium
##endmemory

play music map_spring_jok

scene bg_gen_sky_spr_day
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「さて、どこに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に住む友人は何人もいるが、しばらく滞在させてもらうことを考えると……。"

##endmemory
$ routechara = "Peter"
scene map_gen_bg with fade
$ show_mes("frame_gen_togaki")
T "Where do I want to visit?"
$ hi_mes()
show screen fushigi_map1
$ ui.interact()
