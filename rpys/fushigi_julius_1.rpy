
scene map_bg_winter_day
with dis

scene charasel_bg_tower_day
with dis
label fushigi_julius1:
hide screen tower_man_choice
$ clockanim()
$ hi_mes()

scene cr_01
with dis

play music nightmare_t_ali

scene n_01 with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "休んでいる上司の部屋を訪れるなど、部下としてはあるまじき行為だろうが、今は構っていられない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ノックもそこそこに扉を開けると、私の気配を察していたかのように、ナイトメアはベッドから身を起こしたところだった。"


show nai_s_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0448
Nightmare "「おや、どうしたんだ、[firstname]。\n
そんな暗い顔をして」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「先刻からユリウスを捜しているんだけど見つからなくて」"

hide nai_s_01_11
show nai_s_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice nig_f0449
Nightmare "「時計屋……？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ、ユリウスは、今、どこにいるの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の作業場は復旧作業に入ったばかりだ。\n
いくら仕事第一の彼でも、あれでは手を休めざるをえないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、その予測は目の前で首を横に振った夢魔の反応で、あっさりと否定された。"

hide nai_s_01_2
show nai_s_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0450
Nightmare "「時計屋なら、空き部屋を使って仕事をしている」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

hide nai_s_02_13
show nai_s_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice nig_f0451
Nightmare "「部屋が元通りに戻るまでだが、しばらく間借りするそうだ。\n
部下の話では、部屋から使える道具を持ち出していったようだぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「な……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの職人気質は私もよく知っているつもりだったが、読みが甘かったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすがに今回ばかりは休んでいると思っていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（そ、そこまで仕事尽くしだとは思わなかった）"

hide nai_s_02_11
show nai_s_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice nig_f0452
Nightmare "「いやはや……。\n
時計屋の仕事熱心さには、感服する」"

hide nai_s_02_9
show nai_s_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice nig_f0453
Nightmare "「私だったら、ゆっくりと休むところだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（あなたの場合は、もう少し見習ったほうがいいわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの半分……、とまではいわないが、せめて三分の一でも見習えば、グレイの心労は確実に減るだろうに。"

hide nai_s_02_7
show nai_s_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……ふうん、そう。\n
都合の悪いことは、聞こえないのね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっ、と見つめると、ナイトメアは白々しく首を傾げてみせる。"

hide nai_s_03_7
show nai_s_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0454
Nightmare "「なっ、何のことだ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（読めるくせに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "夢魔であるナイトメアは、心を読むことが出来る。\n
本来であれば思考は聞こえているはずだが、あくまで知らないふりを通すようだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦言を呈しそうになったが、ユリウスのことを思えばこうしてはいられない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事の遅れを取り戻そうとするのなら、ユリウスはいつも以上に仕事に集中するだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（塔を離れる前に、謝っておこうと思ったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この場所にいると、優しさがいたたまれない。\n
反省の意味もこめて、私は塔をしばらく離れようとしていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「教えてくれてありがとう、ナイトメア。\n
行ってみるわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔の客室ならば、私も大体把握している。\n
身を翻して、歩き始めたところに声がかかった。"

hide nai_s_03_3
show nai_s_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0455
Nightmare "「ああ、待ちなさい、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"

hide nai_s_02_11
show nai_s_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice nig_f0456
Nightmare "「私は君の考えに賛成だよ。\n
グレイには私から話しておく」"

hide nai_s_02_4
show nai_s_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_5")
voice nig_f0457
Nightmare "「後のことは気にせず、君が納得出来るようにしておいで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（やっぱり聞こえていたんじゃないの！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず睨み返したが、夢魔の表情は変わらなかった。\n
むしろよりいっそう楽しげに微笑んで、手まで振ってくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（……ありがとうなんて、言わないからね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま早足に彼の部屋を後にした。"

play sound se_0399
hide nai_s_02_3

$ hi_mes()

scene cr_01
with stripe_l_long
play sound se_0776

play music tower_corridor_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔には、いくつもの部屋がある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "会合の際に他領土の役持ちが滞在する客室を始め、空き部屋が全部でいくつあるのか、見当もつかない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、仕事に集中できる環境を望むユリウスならば、人の気配の少ない区画を選ぶはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔の職員も滅多に来ることがないほど静かな場所となれば、当然限られてくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（このあたりなら、ほとんど使われることもない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔の中枢部から離れた区画にある部屋を一つ一つ回っていたときだ。"


$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0176
Julius "「……おまえ、こんなところで何をしているんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！\n
ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り返れば、そこには工具を持ったユリウスが立っていた。"


show yuri_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0177
Julius "「その部屋は私がしばらく借りることになっている。\n
空き部屋を探しているのなら、他の部屋にしろ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ち、違うわ。\n
部屋を探していたわけじゃなくて……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（あなたを探しに来たの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言いかけたところで、言葉がのどの奥に張り付いてしまう。\n
いまだ焦げた上着を見ると、胸の奥がちくちくと痛む。"

hide yuri_t_03_12
show yuri_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0178
Julius "「だったら、こんなひとけのない場所で何をしていたんだ、おまえは」"

hide yuri_t_03_4
show yuri_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0179
Julius "「おまえのほうが私よりもこの中には詳しいだろう。\n
このあたりには、何もないぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（うう……、空気が重い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事第一のユリウスにとっては、あの空間はもっとも大切な場所だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その部屋で（ナイトメアにも責任の一端はあるが）小火を出してしまった私に対して、怒るのも無理はない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_5")
T "「……ごめんなさい、迷惑をかけて」"

hide yuri_t_02_11
show yuri_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_5")
voice jul_f0180
Julius "「は？\n
何のことだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「だって、ユリウスの部屋であんな……」"

hide yuri_t_02_5
show yuri_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_4")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_3")
T "「だから、その……、ごめんなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスの顔を見ていられず、頭を下げた。\n
短い沈黙の後で、相手は溜息をつく。"

hide yuri_t_02_3
show yuri_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0181
Julius "「はあ……、おまえが謝る必要はないだろう。\n
そもそも芋虫が許可もなく私の部屋に入り込んでいたのが原因だ」"

hide yuri_t_03_11
show yuri_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0182
Julius "「まったく、虫なら虫らしく、森にでも隠れていればいいのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦い言葉が響くと同時に、頭の上に手が載せられた。\n
くしゃりと髪を掻き混ぜて、ユリウスは言う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔を上げると、いつも無愛想な目が、少し綻んで私を映していた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……何を言えばいいの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな戸惑いは彼の中にもあったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉を探すようにしばらく沈黙した後に、ユリウスは彼らしいことを口にした。"

hide yuri_t_01_13
show yuri_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0183
Julius "「それに、元々時計の修理は私の仕事だ。\n
多少焦げていても内容は大きく変わらない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、気にするな。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（多分、そういう意味なんだろうけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の性格を考えれば、最大限の優しさで守られているのが分かる。\n
そして、分かるだけに……、申し訳なくなってくるのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（怒ってくれていいのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この手は、優しい。\n
だが、頭を撫でる手に、小さな火傷の痕を見つけて、私は目を見開いた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「ユ、ユリウス、その手！？\n
小火のときに……」"

hide yuri_t_01_2
show yuri_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice jul_f0184
Julius "「これぐらいでいちいち大声を出すんじゃない」"

hide yuri_t_03_13
show yuri_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice jul_f0185
Julius "「水ぶくれにもなっていないし、ただの痕だ。\n
この程度の火傷なら、すぐに消える」"

hide yuri_t_03_4
show yuri_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice jul_f0186
Julius "「指も動くし、仕事にも問題はないからな。\n
治療するまでもない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……でも、痛いでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（どうして、気付かなかったんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最初にユリウスが火を消そうとしたあのとき、水もなければ、火を消せる道具もなかったのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の上着だって、防火対策がほどこされているわけでも何でもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（怪我なんてしないと思い込んでいたの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "無事だと、どうして確かめもせずに判断してしまったのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らは私にはない力もあるが、斬られれば血も出るし、銃で撃たれれば傷つくのは変わらない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……ごめんなさい」"

hide yuri_t_02_10
show yuri_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jul_f0187
Julius "「大袈裟なやつだな。\n
おまえがそう殊勝だと、やりづらい」"

hide yuri_t_03_1
show yuri_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jul_f0188
Julius "「さあ、私はそろそろ仕事に戻る。\n
おまえももう少し休んでこい」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（……優しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段は突き放すようなことを言うのに。\n
私が弱っていることを察しているのか、ユリウスの言葉に刺はなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（あなたに優しくしてもらってばかりだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、頭から手が離れたことを寂しく思う前に口を開く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「あのね、ユリウス。\n
……私、しばらく塔から離れようと思うの」"

hide yuri_t_01_7
show yuri_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
Julius "「……[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「だから、その……。\n
しばらくはあなたの邪魔もしないから、静かに過ごせると思う」"

hide yuri_t_03_2
show yuri_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一人で仕事に詰める性格のユリウスだ。\n
納得こそすれども、驚きはしないと思っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし……。"

hide yuri_t_03_13
show yuri_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0189
Julius "「……芋虫や、トカゲが、おまえに何か言ったのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口を開いた彼の声は、どこかイライラとしているように感じたのは、私の気のせいだったのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（な……、何でそんなに不機嫌になるの？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ち、違うわ。そういうことじゃなくて……。\n
その、少し反省してこようと思って」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「ナイトメアもしばらく禁煙するようにグレイにお説教されていたみたいだし。\n
私だけ無罪放免っていうわけにはいかないでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事を休むのは気が引けるが、何かお詫びをしたいと思った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは思いっきり胡乱げな眼差しで見つめたあと、仕方ないと言いたげに肩を竦めて続ける。"

hide yuri_t_03_12
show yuri_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0190
Julius "「はあ……、おまえは頑固だからな。\n
一度決めたら、簡単に翻しはしないだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

hide yuri_t_01_13
show yuri_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice jul_f0191
Julius "「分かった、好きにしろ。\n
外に行くのに、わざわざ私の許可を取る必要はない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「……うん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま彼は私の横を通り過ぎ、空き部屋に入る直前に声をかけてきた。"

hide yuri_t_01_1
show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ、うん。\n
なに、ユリウス？」"

hide yuri_t_03_9
show yuri_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0192
Julius "「いや……、出かけるのはいいが。\n
気を付けて行ってこい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぶっきらぼうな、一言。\n
多分、彼を知らない人間が聞いたら、社交辞令にしてももう少し言いようがあると思うだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、私にとっては何よりも嬉しい言葉だった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「うん、行ってきます」"

hide yuri_t_02_9
show yuri_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice jul_f0193
Julius "「……ああ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "互いにぎこちない言葉が、出発の挨拶。\n
だが私を見つめる彼の暗い瞳に、背中を押してもらえたような気がした。"

hide yuri_t_02_6

$ hi_mes()

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium
##endmemory

play music map_winter_jok

scene bg_gen_sky_win_day
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「さて、どこに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に住む友人は何人もいるが、しばらく滞在させてもらうことを考えると……。"

$ hi_mes()
$ routechara = "Julius"
$ show_mes("frame_gen_togaki")
scene map_gen_bg with fade
T "Where do I want to visit?"
$ hi_mes()
show screen fushigi_map1
$ ui.interact()
