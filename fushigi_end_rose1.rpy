label fushigi_end_rose1_1:

scene map_bg_autumn_eve
with stripe_l_medium

scene b_aut_02
with stripe_l_medium

play music rose_garden_p_ali

scene r_aut_02
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディがこの場所を訪れるのは、決まって夕方だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋屋敷に戻ってから最初の夕方、薔薇園に足を向けると、予想通り彼女はそこにいた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただし……、いつもの彼女の姿ではない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「……何をしているの、ビバルディ？」"


show viv_chil01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice viv_f0474
Vivaldi "「いつもの通りじゃ。\n
薔薇を見ておった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……いや、私が聞きたいのはそういうことじゃなくて、どうしてまた子供の姿なのかなって」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城で人形遊びを提案してきたときのように、彼女は子供の姿のまま、薔薇を散らしている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（余程気に入っているのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "理由までは分からないが、少なくともこの場所でまでその姿でいるのだから、嫌ではないのだろう。"

hide viv_chil01_13
show viv_chil01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0475
Vivaldi "「この前は途中で邪魔が入ったからな、まったく、あの～～～～～～め。\n
女同士の楽しいひとときを邪魔する権利など、男共にはない」"

hide viv_chil01_11
show viv_chil01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0476
Vivaldi "「そうだ、[firstname]、そろそろ持ってきた茶が飲み頃じゃ。\n
一緒にお茶にしようではないか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そういって誘う顔は、私のよく知る女友達のものだった。"

hide viv_chil01_3

$ hi_mes()

$ time_effect()

$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "テーブルには、お茶の準備が整っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そうして椅子に座った私の膝に、ビバルディが乗っている。\n
子供の姿で甘えられると、普段以上に断り辛い。"

show t_end_rose_bra1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「ごめんなさい、勝手に出てきてしまって」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（居候させてもらったのに……、恩を仇で返すなんて）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、彼女の声に私を責める様子はない。\n
小さな手にカップを持って、ゆっくりと口をつけている。"

play sound se_0174
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0477
Vivaldi "「おまえが気にすることはないぞ。\n
すべては、あの～～～～で～～～～～～な愚弟が悪い」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0478
Vivaldi "「それはそうと……。\n
おまえに隠していたことを、あの馬鹿は明かしたのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……ううん、まだなの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屋敷に戻ればさすがに教えてくれると思ったが、ブラッドを始め、屋敷の人間は固く口を閉ざしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "また、仲間外れに逆戻りだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（……まだ、受け入れてもらえていないのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らのすることに深入りしようと思っていないのが悪いのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、彼らが私に見せない部分を知ったら、今のままではいられなくなってしまうような気がする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（どんなに酷いことをしていても、嫌いになれない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らがどんな意図で私を避けているのかは知らないが、ずっとこのままだったらさすがに落ち込むというものだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「迎えに来るぐらいだから、そろそろ教えてくれると思ったんだけど。\n
なんだか、聞きにくいままなのよね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice viv_f0479
Vivaldi "「やはり、おまえを不安にさせる馬鹿になど返すのではなかったな。\n
今からでも遅くないぞ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice viv_f0480
Vivaldi "「わらわが一緒にいれば、そんな顔はさせぬ。\n
あんな愚弟のことなど見捨てて、城に移っておいで」"

play sound se_0551
hide t_end_rose_bra1

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "優しい手付きで私の頬を撫でながら、彼女は愛らしく微笑んだ。\n
斬首を命じるのと同じ唇で、こんな甘いことも言える人だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女の弟であるここの主と同じで、華があって、甘い香りを放っているのに、棘も持っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本当に、薔薇のような姉弟だといつも思う。"


show bra_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0565
Blood "「……私の前で堂々と誘惑しないでもらおうか、姉貴。\n
君もだ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「ブラッド……」"

hide bra_t_02_3
show bra_t_02_18 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice blo_f0566
Blood "「簡単に唆されないでくれ、見た目は子供でも、中身はなにも変わっていない。\n
いや、見た目で油断させるだけ、その姿のほうが悪質か」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薔薇園に現れたブラッドはそう言いながら、私とビバルディの向かい側へ腰を下ろす。"

play sound se_0160

show t_end_rose_bra2 onlayer master
with dis
hide bra_t_02_18
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0481
Vivaldi "「ふん、子供の時分から変わりばえのないおまえに言われたくはない。\n
……おまえの分の茶などないぞ、勝手に座るな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0567
Blood "「私の薔薇園で私が何をしようが、とやかく言われる覚えはないな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0567_5
Blood "「それに、茶なら結構、姉貴に恵んでもらわなければならないほど、落ちぶれていない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言うと、彼はどこからともなくティーポットとカップを取り出した。\n
どうやら彼はここでお茶会をするつもりだったらしい。"

play sound se_0573
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0568
Blood "「それはそうと、私のものにいつまでも馴れ馴れしく触るんじゃない。\n
君も、それを下ろしてこっちに来なさい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「椅子は二脚しかないみたいだけど？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ベンチやブランコが備え付けられている薔薇園に、お茶会が出来るようなテーブルはこの一セットしかない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本来、椅子は全部で三脚あるのだが、最後の一脚にはビバルディの杖が置かれていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（杖を退かすっていうわけにもいかないと思うしね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供の姿では持っているのが難しく、かといって地面に置くわけにも、テーブルの上に置くわけにもいかない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0569
Blood "「座る方法はあるだろう？例えば、君がしているように……、な。\n
君になら、いつでも膝を貸してあげよう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「……座り心地が悪そうね。\n
遠慮するわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（何を考えているんだか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の薔薇園に入れるのは、私達三人だけだ。\n
そのせいか、ブラッドはいつにも増して絡んでくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "素っ気なく断ると、彼は更に口を挟んできた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0570
Blood "「だいたい、どうして君と姉貴がここにいるんだ？\n
城を出る前に打ち合わせでもしていたのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「皆が何かの準備で忙しいみたいだったから、遠慮してあげたの。\n
好きなだけ秘密の打ち合わせでもなんでもすればいいじゃない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "{size=+20}「部外者の私になんか気にせずに、ご自由に」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドは不機嫌そうに睨んでくるが、それは私だって同じだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（まだ教えてくれる気もないくせに……、ちょっかいだけ出さないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "無言のまま睨み合っていると、膝の上でビバルディが動いた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0482
Vivaldi "「……ふ、いつもと違う目線というのも悪くないものじゃな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

play sound se_0267
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ビバルディ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の膝から少し身を乗り出したビバルディは、ブラッドを見上げながら楽しげに笑う。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0571
Blood "「何か用かな、若作りの姉貴」"

hide t_end_rose_bra2
show t_end_rose_bra3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0483
Vivaldi "「ふ、ふふふ。\n
まるで、子供に妻をとられて欲求不満になっている夫のようじゃのう、ブラッド」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice blo_f0572
Blood "「ぶっ！！ごほ、げほ……な、なにを……、ごほっ。\n
な……、何を馬鹿なことを言っているんだ、姉貴！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "紅茶をこよなく愛する彼にしては珍しく吹き出したブラッドは、まだむせ込んでいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は私で、赤くなった顔を隠すことも出来ず息を飲むばかりだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0484
Vivaldi "「図星であろう、今のわらわをこの子が乗せている様子は、親子のようではないか。\n
そうは思わぬか、ママ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「マ……、ママって……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（え、わ、私がママ！？\n
ということは……、父親ってやっぱり）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おそらく父親に当たる男を見れば、彼はまだダメージから回復していなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むせ込みながら、何とか平静を取り戻そうとしている男を煽るように、ビバルディは言う。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0485
Vivaldi "「この愚弟……ではなかった、パパは心が狭くて心配じゃなあ。\n
いつか捨てられてしまうのではないか」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0573
Blood "「変なことを言うんじゃないっ。\n
誰がパパだ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0574
Blood "{size=+20}「間違っても、私は自分の子供を姉貴のように育てたりはしない！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（ブラッド、それは論点が違う）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、子供のいない……、それ以前に結婚もしていない私達には、子育てなど夢のまた夢だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0486
Vivaldi "「ほう、ではどんな子供に育てるつもりだ、パパ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "揶揄をたっぷり含んだ声で、ビバルディは聞く。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0575
Blood "「決まっているだろう、強く、賢い子に育てるさ。\n
銃の腕もいいだろうし、私の娘は、私とお嬢さんに似た……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0487
Vivaldi "「おまえに似た？\n
それはまた、これ以上ない不幸な子だこと、この子そっくりならば愛らしいというのに」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（ブラッドと私に似た子供……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず想像してみる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドの性格と私の性格を足して二で割って。\n
外観はどちらに似るか分からないが、混ざったとして。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……間違いなく、扱い辛そうな予感がする。\n
そして、性格も捻くれそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足して二で割れればいいが、相乗効果にでもなったら手がつけられない強者になるのではないだろうか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（……一番の迷惑を被るのは、絶対にエリオットだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いまだ影も形もない子供の将来を考えて、不安になった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0488
Vivaldi "「おまえに似た男など女癖は悪そうだし、何よりも気が利かぬ。\n
最悪だな、哀れんでしまうぞ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0576
Blood "「姉貴には関係ないだろう。\n
私とお嬢さんの問題だ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0489
Vivaldi "「関係なくはないぞ、わらわにとって姪か甥になるのだ。\n
ああ、ならば子供が出来てから、この子共々奪ったほうがよいかもしれぬ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディは名案を思いついたというように、私を振り返る。"

play sound se_0267
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0490
Vivaldi "「ああ、しかし、出来れば娘がよい。\n
男は……、否応なくこやつに似そうで、手がかかりそうじゃ」"

play sound se_0295
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "反論するようにブラッドの手がテーブルを叩く。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0577
Blood "「やらん！\n
娘であろうと、息子だろうと、お嬢さんも含めて、全部私のものだぞ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "堂々と宣言したブラッドだが、難攻不落の姉はびくともしなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0491
Vivaldi "「ほんに……、人の話を聞かぬ男じゃな。\n
誰がくれと言ったのだ、わらわはおまえから奪うと言ったのだぞ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0492
Vivaldi "{size=+20}「おまえの意思など関係ない」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice blo_f0578
Blood "{size=+20}「もっと質が悪いじゃないか」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（何だろう、どこかで同じような会話を聞いたようなデジャヴが……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "{size=+20}（しかも、そのときよりも今回のほうが、圧倒的に分が悪い気がする）{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ええと、その……。\n
そんなまだいない子供の話は別にいいんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice blo_f0579
Blood "「そうだ、これからの家族計画に余計な口を出すな。\n
夢がなくなるだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「か……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_10")
T "（家族計画）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "単語そのものは珍しくないはずなのに、妙に生々しく感じてしまうのは、何故だろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0493
Vivaldi "「夢などと言える立場か、おまえが？\n
子供云々と偉そうに語るぐらいなら、早々に身を固めることじゃな」"

play sound se_0086
hide t_end_rose_bra3

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呆れたように息をついて、彼女は私の膝から下りていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隣の席に置いたままの杖を持っていくことも忘れない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（ビバルディ？）"


show viv_chil01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0494
Vivaldi "「それと、過度な秘密はかえって不安にさせるだけじゃ。\n
女の不安を解消出来ぬ男に価値などないぞ、わらわをあまり失望させるな、パパ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（こ、子供の言う台詞じゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "外観を裏切る発言だけを投げつけると、ビバルディは背を向けた。\n
そのまま数歩進んでから、突然振り返って私を見上げてくる。"

hide viv_chil01_4
show viv_chil01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0495
Vivaldi "「ああ、それと、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「あ、うん、なに？」"

hide viv_chil01_13
show viv_chil01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Vivaldi "「…………」"

hide viv_chil01_14
show viv_chil01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice viv_f0496
Vivaldi "「いや……、不甲斐ない愚弟に見切りをつけたら、いつでもわらわのもとに来ればよい」"

hide viv_chil01_7
show viv_chil01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice viv_f0496_5
Vivaldi "「おまえが望むなら、人形と言わず子供役になってやってもよいぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ビバルディ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまでのブラッドに対しての容赦ない口調とは少し違う、不思議な響きがあった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T "「……ううん、人形遊びも親子ごっこも、もういいわ。\n
別の形でまた遊びましょうね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（私はビバルディがどんな姿をしていても、同じくらいに好きだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "素直に言葉では表せないから、心の中で伝えておく。"

hide viv_chil01_2
show viv_chil01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0497
Vivaldi "「ああ、わらわはよい子だからのう。\n
楽しみに待っておる」"

play sound se_0624
hide viv_chil01_1

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言い残して、ビバルディの姿は薔薇の奥へと消えていった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "残ったのは、私と……、彼女の弟。"


show bra_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

hide bra_t_02_7
show bra_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0580
Blood "「はあ、やっと帰ったか。\n
どうにもあの姿だと、いつもにも増してやりにくい」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（完全に押し負けていたものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薔薇園では姉弟としての顔を見せる二人は、その力関係もはっきりとしている。"

hide bra_t_03_13
show bra_t_03_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0581
Blood "「だが、ふむ、パパとママ……、か」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ブラッド？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（なんで、そんなにじっとこっちを見るの？）"

hide bra_t_03_15
show bra_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice blo_f0582
Blood "「姉貴が言うと悪意の塊にしか聞こえない響きだが……。\n
子供にそう呼んでもらえるのは、なかなか悪くない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「いや、だから、まだ子供なんて作っていないし！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あなたはどうだか知らないけど、少なくとも私には隠し子だって一人もいないわよ！」"

play sound se_0160

show t_end_rose_bra4 onlayer master
with dis
hide bra_t_02_2
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慌てて抗議したが、それはどうやら彼の琴線に触れてしまったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "立ち上がったブラッドが、私の座っている椅子の傍に寄る。\n
顔を近付けられると、逃げ場を失う。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0583
Blood "「私だって同じさ、どこかで不始末をしたつもりはない。\n
君がいるのに、他に女を作るような男だと思われていたとは、残念だ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぞくっと艶めかしい口調で言わないでほしい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0584
Blood "「ふむ……、相性は悪くないはずだが……。\n
あとはタイミングの問題か」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「いや、だから……、なんで、こんなところで……！！」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一人で納得しているブラッドに、今にも連れ去られそうで、必死に体を押し返す。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（びくともしない……！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "力の差は歴然とはいえ、抵抗しないわけにもいかなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0585
Blood "「君だって、門番の相手をしているところを見る限り、子供嫌いには見えないぞ。\n
自分の子なら、もっと可愛いと思わないか」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_11")
T "（だから、どうして話がそっちの方向に行くのよ！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供がどうとか、そういうことを言う以前に、隠しごとはどこに消えたのか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「ちょ、ちょっと！\n
いい加減、何を黙っていたのかぐらい教えてくれても……」"

play sound se_0551
hide t_end_rose_bra4
show t_end_rose_bra5 onlayer master
with dis

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「ん！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_10")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「……っ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_11")
voice blo_f0586
Blood "「……む」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「……んん、っ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
voice blo_f0587
Blood "「……は」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「……、ぁ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
voice blo_f0588
Blood "「しい……、静かに。\n
喧嘩の原因を突き止めたい君の気持ちをおざなりにするわけではないが……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
voice blo_f0589
Blood "「こっちの計画には、仕込みから実現まで長くかかるからな。\n
秘めごとは、その後にゆっくりと」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「ふ……、っ、あ」"

play sound se_0063
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドはもっともらしく告げると、私を抱きかかえる。\n
今度は力が抜けてしまっているから、されるがままだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0590
Blood "「こと、君に関わることならば、私が把握をしていなければな。\n
子供のことは夫婦の問題だ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0591
Blood "「そうとも、めでたいことなら、いくつあってもいい。\n
そして、いい知らせを部下に伝えてやるのも、いい上司の役目というものだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遠ざかっていく薔薇園を、上機嫌なブラッド越しに滲む視界で見つめる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この場所に入ることが出来る人間が増えるのも、そう遠くないかもしれない。"

scene black with dis
hide frame_gen_togaki
hide ali_t_06_16
with Dissolve(5)
pause 1

$ renpy.movie_cutscene("endroll_c.mpg")
#return
