
scene map_bg_spring_day with dis
label fushigi_end_castle1:
$ clockanim()

scene map_bg_spring_day with dis

scene hm_spr_01 with dis

play music castle_audience_p_ali

scene he_01 with Dissolve(1.2)
play sound se_0295
pause .3
play sound se_0295

show t_end_siro1 onlayer master with dis
$ show_mes("frame_gen_chara")
King " 「ええと、それでは、今回の裁判を始める。\n
まずこの度の被告人、[firstname]＝[familyname]、その罪状の確認を」"
$ hi_mes()
$ show_mes("frame_gen_chara")
Peter "「…………」"
$ hi_mes()
$ show_mes("frame_gen_chara")
Vivaldi " 「ホワイト。\n
わらわが仕事をしている横でサボる気か？」"
$ hi_mes()
$ show_mes("frame_gen_chara")
Peter " 「……はあ。\n
それでは、罪状を読み上げます」"
$ hi_mes()
play sound se_0471
$ show_mes("frame_gen_monologue")

$ face("ali_t_01_1")
T " （…………）"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_01_7")
T " （なんで、私がこんな場所に立っているんだろう）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 周囲に無言で立つ兵士の武器の先端は、被告人へと向かっている。\n
そう、つまり、現在裁判にかけられている私へと。"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_1")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_06_11")
T " （城に帰ってきた早々、問答無用で引っ張られたものね）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 門のところで待っていた顔馴染みの兵士に声をかけるや否や、あっというまに謁見室へと連れてこられてしまった。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0472
Peter " 「被告人の罪状は、陛下を始め、この城の人間を苛立たせたことですね。\n
やれやれ、まったく、ここの人間は軒並み気が短いんですから」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0525
Ace " 「ええ？\n
俺はそんなにイライラしてなんかいなかったけどなあ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0473
Peter " 「へえ？そうでしたか？\n
確かに君は、いつものようにふらふらと出歩いてばかりでしたね」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0474
Peter " 「ですが、兵士の訓練中にかなり派手に骨を折ったり、必要以上に斬りつけたり、色々としていたと聞きましたけど？\n
僕の聞き間違いでしょうか、エース君？」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0526
Ace " 「ははは、だってあれは鍛錬だろう。\n
多少痛い思いをしなくちゃ身につかないぜ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0527
Ace " 「まるで俺が八つ当たりしたみたいに言わないでくれよ、ペーターさん」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_2")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_01_1")
T " （嘘ばっかり）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " いつもなら裁判の席に顔を出すことがないエースは、珍しく裁判長であるビバルディの横に立って、私を見下ろしている。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 表情だけは爽やかだが、こちらを見る目には何となくぴりっとした辛いものがあった。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0426
Vivaldi " 「ふん、そういうおまえも人のことは言えまい」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0427
Vivaldi " 「あの子が出て行ってから、毎時間帯毎時間帯、騒いでおったくせに。\n
いい顔を見せようとしたところで無駄じゃぞ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0428
Vivaldi " 「だいたい、ストーカー気質のおまえのこと。留守番をしていると言っていたが……、本当は追いかけて物陰からこそこそ見ていたのではないか？」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0475
Peter " 「失礼なことを言わないでください！\n
僕は彼女との約束を破ったりしませんよ！」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0476
Peter " {size=+20}「それに、ついていくのなら、物陰からじゃなくて、正面から堂々と行きます」{/size} "
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_06_17")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_01_5")
T " （真性のストーカーね）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " そして、本人には改める気持ちはまったくない。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0429
Vivaldi " 「……それはかえって悪質じゃ。\n
はあ、まったくこれでは裁判にならぬ、おい、おまえ達」"
$ hi_mes()
hide t_end_siro1  with dis

$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " ビバルディは宰相と軍部責任者から話を聞くのを諦め、並んでいる兵士達に声を掛ける。"
$ hi_mes()

show heisi_t_02_09 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0079
Soldier " 「は……。\n
私達でございますか、女王陛下」"
$ hi_mes()

show viv_t_03_11 at center
hide heisi_t_02_09
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0430
Vivaldi " 「そうじゃ、たまには役なしの意見も聞いてやろう。\n
おまえはどうだった、この子がいなくて、どう思ったのか聞かせてみよ」"
$ hi_mes()

show heisi_t_02_03 at center
hide viv_t_03_11
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0080
Soldier " 「ど、どうと言われましても……。\n
私はただの役なしのカードですし」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 突然ふられた兵士が困ったように同僚の顔を見る。"
$ hi_mes()
hide heisi_t_02_03
show heisi_t_02_03 at left

show heisi_t_01_02 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0054
Soldier " 「親しくはさせて頂いておりますが……」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 意見を求められた兵もまた困ったように首を傾げた。\n
だが。"
$ hi_mes()

show viv_t_01_8 at center
hide heisi_t_02_03

hide heisi_t_01_02
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0431
Vivaldi " 「ええい、はっきり言わぬか！！\n
意見を言わぬのなら、首を刎ねてしまうぞ！」"
$ hi_mes()
play sound se_0490
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 手のひらを杖で打ち、苛立ちをあらわにするビバルディに、兵士達が竦みあがる。"
$ hi_mes()

show heisi_t_02_09 at center
hide viv_t_01_8
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Soldier " 「！」"
$ hi_mes()
hide heisi_t_02_09
show heisi_t_02_02 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0081
Soldier " 「せ、僭越ながら……。\n
その、私としては、寂しかったです」"
$ hi_mes()
hide heisi_t_02_02
show heisi_t_02_02 at left

show heisi_t_02_03 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0055
Soldier " 「私も……。\n
私達を見分けて下さるのは、この方ぐらいですから」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_06_8")
T " 「あなた達」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 私を見ながら答える彼らは、武器を突きつけながらもどこか照れたように言う。"
$ hi_mes()

show viv_t_03_9 at center
hide heisi_t_02_02

hide heisi_t_02_03
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0432
Vivaldi " 「ふん。\n
ならば最初からそう申せばよいのだ、手間を取らせるな」"
$ hi_mes()

show per_t_01_11 at center
hide viv_t_03_9
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0477
Peter " 「ということは、苛ついていたのは役なしも同じと言うことですね」"
$ hi_mes()
play sound se_0330
play sound se_0333
hide per_t_01_11
show per_t_02_11 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0478
Peter " 「本当に、図々しい話ですが。\n
裁判中でなければ、撃ち殺しています」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 書類に書き込むペーターは、心底気に入らないといった様子だ。"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_11")
T " 「あんたね……」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_02_10")
T " （意見を言わなければ首を刎ねるって脅されたんだから、仕方ないでしょうっ）"
$ hi_mes()
hide per_t_02_11
show per_t_02_11 at left

show ace_t_03_3 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_10")
voice ace_f0528
Ace " 「兵に聞くなら、彼女達にも聞かないと不公平だよね。\n
なんて言っても、同僚なんだし……、というわけで、君達はどう思っていた？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 今度はエースが、壁際に立って裁判の行方を見守っていたメイド達に声をかける。"
$ hi_mes()

show siro_t_02_07 at center
hide per_t_02_11

hide ace_t_03_3
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Maid " 「…………」"
$ hi_mes()
hide siro_t_02_07
show siro_t_02_07 at left

show siro_t_02_07 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Maid " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 案の定、顔を見合わせて黙っているメイド達に、エースが追い討ちを掛けた。"
$ hi_mes()

show ace_t_03_11 at center
hide siro_t_02_07

hide siro_t_02_07
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0529
Ace " 「ほら、ちゃんと言わないと……。\n
気の短い陛下がいつものお約束を言い出しちゃうよ」"
$ hi_mes()
play sound se_0184
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_13")
T " 「エース！」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 彼女達には何の非もないのだ。\n
脅さないでというように机を叩いて訴える。"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_02_9")
T " （あんたまで何を言い出すのよ！）"
$ hi_mes()

show viv_t_01_13 at center
hide ace_t_03_11
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice viv_f0433
Vivaldi " 「被告人に発言権はないぞ。\n
[firstname]、黙っておれ」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_15")
T " 「ビバルディ……」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 裁判席から見下ろすビバルディは先ほどからにこりともしない。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 斬首が口癖の、残酷無慈悲な女王。\n
帽子屋屋敷、遊園地と争いを続ける領主としての顔で、私を見ている。"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_02_16")
T " （……そんなに、怒っていたの？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 城を出たときはそこまで怒っているようには見えなかったのだが。"
$ hi_mes()

show siro_t_02_09 at center
hide viv_t_01_13
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0041
Maid " 「勿論寂しかったですわ。\n
この方は優しいですし、一緒にいるととても楽しいんです」"
$ hi_mes()
hide siro_t_02_09
show siro_t_02_09 at left

show siro_t_02_08 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0017
Maid " 「ええ、やはりお嬢様と仕事が出来ないと、寂しいです。\n
いつもよくして頂いていますし」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_11")
T " 「あなた達……」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_01_12")
T " （私の分も仕事が増えて大変だったはずなのに）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 本職の彼女達には及ばないが、私もこの城での仕事にはだいぶ慣れた。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 文字通りの戦力にはならないけれど、メイドとしてならばそこそこ働ける程度にはなっている。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " それだけに、予定されていた仕事は彼女達にも振り分けられたはずだ。"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_11")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_01_12")
T " （責めてくれたっていいぐらいなのに）"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_7")
T " 「優しいのはあなた達のほうじゃない」"
$ hi_mes()
hide siro_t_02_09
show siro_t_01_02 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice hei_f0042
Maid " 「……そんなことはありません」"
$ hi_mes()
hide siro_t_02_08
show siro_t_02_06 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice sam_f0018
Maid " 「ええ、優しいのはあなたのほうですわ」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " はにかんだように笑う二人は、小さく首を振った。"
$ hi_mes()

show viv_t_01_11 at center
hide siro_t_01_02

hide siro_t_02_06
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0434
Vivaldi " 「ふむ……、そうか。\n
意見をまとめるとすれば、おまえがいなくなって苛ついていたり、寂しい思いをしたものは多いということになるな」"
$ hi_mes()
hide viv_t_01_11
show viv_t_01_13 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0435
Vivaldi " 「……ホワイト」"
$ hi_mes()

show per_t_02_9 at center
hide viv_t_01_13
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0479
Peter " 「なんですか？」"
$ hi_mes()
hide per_t_02_9
show per_t_02_9 at left

show viv_t_03_11 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0436
Vivaldi " 「今までに不敬罪や侮辱罪で首を刎ねたことは何度もあるが……。\n
ふむ、こういう場合の罪状は何と言えばよい？」"
$ hi_mes()
hide per_t_02_9
show per_t_03_9 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0480
Peter " 「知りませんよ、ご自分でお考えになったらいかがですか？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " ハートの城の女王と、宰相。\n
私にはあまり馴染みのないその表情に、何も言えなくなる。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " すると、周囲にいた兵士やメイドから声があがった。"
$ hi_mes()

show heisi_t_02_09 at center
hide viv_t_03_11

hide per_t_03_9
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Soldier " 「！」"
$ hi_mes()
hide heisi_t_02_09
show heisi_t_02_09 at left

show heisi_t_01_06 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0056
Soldier " 「陛下……、まさかとは思うのですが、この方を……」"
$ hi_mes()
hide heisi_t_02_09

hide heisi_t_01_06
show heisi_t_01_06 at left

show siro_t_02_03 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0043
Maid " 「それは、あまりに早計かと」"
$ hi_mes()
hide heisi_t_01_06

hide siro_t_02_03
show siro_t_02_03 at left

show siro_t_02_09 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0019
Maid " 「どうか、お考え直しください」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_15")
T " 「皆……」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 女王の裁決に口を挟めばどうなるかなど、私よりも彼らの方が余程よく知っているはずだ。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " だが、上から私達を見下ろすビバルディに彼らは縋るように目を向けている。"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_02_16")
T " （皆のほうが不敬罪に問われたら……）"
$ hi_mes()

show viv_t_03_12 at center
hide siro_t_02_03

hide siro_t_02_09
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
Vivaldi " 「…………」"
$ hi_mes()
hide viv_t_03_12
show viv_t_03_2 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice viv_f0437
Vivaldi " 「ふ、やれやれ、おまえも好かれたものじゃな、[firstname]。他の領土の愚か者だけでなく、わらわの城の者までおまえに重きを置いておるとはのう」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_15")
T " 「ビバルディ」"
$ hi_mes()
play sound se_0160
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 苦笑いを浮かべた女王は、ようやく立ち上がった。"
$ hi_mes()
play sound se_0676
hide viv_t_03_2


show t_end_siro2 onlayer master with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0438
Vivaldi " 「じゃが、ここまでおまえを好いているものを置いて行ったことは、事実。\n
なんらかの罰が必要じゃ」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_04_17")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_04_12")
T " （罰）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " その言葉を聞いて脳裏に浮かんだものは、仮面を付けた道化の待つ監獄だった。"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_02_16")
T " （お城なんだから、どこかに牢屋ぐらいあると思うけど……。\n
どうして、ジョーカーのことを思い出しちゃったのかしら）"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice viv_f0439
Vivaldi " 「被告人、[firstname]＝[familyname]。\n
ハートの女王、ビバルディがおまえに判決を言い渡す」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
Peter " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
Ace " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_15")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 緊張からか、こくりと喉が鳴った。"
$ hi_mes()
hide t_end_siro2 with dis

$ hi_mes()

scene hm_spr_01 with stripe_l_long

play music castle_t_ali

show t_end_siro3 onlayer master with dis
$ show_mes("frame_gen_chara")
Vivaldi " 「うむ……、紅茶がうまい、このクッキーもなかなかの味じゃ。\n
何よりも、あの騒々しい愚か者どもがいないだけで落ち着く」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_7")
T " 「そ、そう？\n
少しでも楽しんでもらえればいいけど」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice viv_f0441
Vivaldi " 「もちろん、楽しいぞ？\n
おまえと二人きりの茶会じゃ、楽しくないはずがない」"
$ hi_mes()
play sound se_0174
$ show_mes("frame_gen_heroine")

$ face("ali_t_04_14")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_05_6")
T " （静かだなあ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 城に戻ってきた早々、裁判にかけられた被告人と、判決を下した女王様。\n
そんな二人が並ぶお茶会とは思えないほど、穏やかだった。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0442
Vivaldi " 「どうしたのだ、[firstname]。\n
おかしな顔をしておるぞ？」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_7")
T " 「だって……、これじゃあ、罰にならないと思って」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice viv_f0443
Vivaldi " 「わらわが罰だと言えば罰なのじゃ。\n
現に他領土の馬鹿者におまえをとられなくて清々するぞ、いい気味じゃ」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " くくくと肩を震わせるビバルディは上機嫌そのものだ。"
$ hi_mes()
play sound se_0621
hide t_end_siro3 with dis


show per_t_02_5 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0481
Peter " 「ああ、[firstname]！\n
こんなところにいたんですね、探しましたよ！！」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_03_7")
T " 「ペーター？」"
$ hi_mes()
hide per_t_02_5
show per_t_02_5 at left

show viv_t_02_7 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice viv_f0444
Vivaldi " 「ホワイト、この時間帯はわらわが約束をしておる。\n
おまえは次の時間帯であろう、順番くらい守れぬのか」"
$ hi_mes()
hide per_t_02_5
show per_t_01_4 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice pet_f0482
Peter " 「……あなたが仕事をさぼらなければ、僕と過ごす時間帯だったんですけどね、陛下」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_4")
T " 「は、ははは」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " お茶会に乱入してきたペーターは、私の傍に寄って、眉を寄せながら不満を訴える。"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_01_7")
T " （何だか、勝手に自分のスケジュールが隙間なく埋められていくのって、変な気分だわ）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " ビバルディが下した判決は、「有罪」だ。\n
さぞかしすごい罰を言い渡されるのだろうと身構えていたのだが、その内容は予想外のものだった。"
$ hi_mes()
hide viv_t_02_7
show viv_t_01_8 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0445
Vivaldi " 「この子がいない間、女王が我慢したのじゃぞ、部下ならば譲れ。せっかく有罪にして城に留めておけると思ったのに、横取りするとは無礼なウサギじゃ」"
$ hi_mes()
hide per_t_01_4
show per_t_01_8 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0483
Peter " 「陛下とばかり過ごしていたら、彼女が～～～～～～になってしまいます！\n
ああ、そんなことになったら、僕は……、僕は！！」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_1")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_01_6")
T " （ビバルディ達がいいって言うまで城から出たらいけないなんて……。\n
無茶苦茶だけど、罰にはなっていない気がする）"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_7")
T " 「罰だって言うなら、もっと厳罰でもいいのに」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 裁判で私を庇ってくれた兵士やメイドの言葉もあって、心配をかけてしまったと反省している。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 一つの場所に縛られることが得意なわけではないが、気持ちは素直に嬉しい。"
$ hi_mes()
hide viv_t_01_8
show viv_t_03_8 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0446
Vivaldi " 「厳罰？\n
それは、鞭で打ったり、水に沈めたり、～～～～を～～～～～～するような厳罰か？」"
$ hi_mes()
hide viv_t_03_8
show viv_t_03_9 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0447
Vivaldi " 「拷問は面倒で好かぬ。\n
どうせ罰するならば、一思いに首を刎ねてしまったほうが清々する」"
$ hi_mes()
play sound se_0551
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_15")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " カップを置いた手が私に伸びて、綺麗に塗られた爪で首筋を撫でられる。"
$ hi_mes()
hide viv_t_03_9
show viv_t_01_11 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0448
Vivaldi " 「じゃが、おまえの首を刎ねてしまったら遊べない。\n
それでは本末転倒じゃ」"
$ hi_mes()
hide per_t_01_8
show per_t_02_2 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0484
Peter " 「当たり前です、心配しないでくださいね、[firstname]。\n
何があっても、あなたの首を刎ねるなんて酷いことは、絶対にさせません！」"
$ hi_mes()
hide per_t_02_2
show per_t_02_5 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0485
Peter " 「水責めにしたり、～～～～を～～～～～～したとか、～～～～～～～～～～～～とかも、絶対にさせませんから！」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_13")
T " 「リアルに言わなくていい！」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_02_9")
T " （思わず想像しちゃったじゃない）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " そんな地獄絵図のような拷問をされるのも、首を刎ねられるのも遠慮願いたい。"
$ hi_mes()
$ hi_mes()
hide viv_t_01_11

hide per_t_02_5


scene bg_gen_sky_spr_day with dis
play sound se_0629 volume .6
$ show_mes("frame_gen_heroine")

$ face("ali_t_03_7")
T " 「…………？」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_05_5")
T " （水の音？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 誰か近くで兵が薔薇に水をあげているのだろうか。"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_06_5")
T " （先刻、聞いたときにはそんな予定は言われなかったけど）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 何しろ、この前の水撒き事件がある。\n
女王陛下のお茶の邪魔をしないよう、彼らは相当に気を付けているはずだ。"
$ hi_mes()
play sound se_0569 volume .6

scene hn_spr_01 with dis

show per_t_01_4 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter " 「！」"
$ hi_mes()
hide per_t_01_4
show per_t_01_5 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0486
Peter " 「まさか……、[firstname]、危ない！！」"
$ hi_mes()
hide per_t_01_5
show per_t_01_5 at left

show viv_t_01_5 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi " 「！！」"
$ hi_mes()
hide viv_t_01_5

hide per_t_01_5


scene bg_gen_sky_spr_day with dis
play sound se_0569
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_4")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_8")
T " 「ペ、ペーター」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_04_9")
T " （なんで、いきなり水が降ってくるのよ\n
！？）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " この世界で天候が崩れることなど、今までありえなかった。\n
しかも、これだけ晴れていて突然の降水などあろうはずがない。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 人為的な理由がない限り。"
$ hi_mes()

play music gag2_a_ali
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0530
Ace " 「あれー、なんで急にホースが暴走したんだろう？\n
おっかしいなあ、原因も分からないなんて参ったぜ、ははははは」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_06_17")
T " 「……エ、エース」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 顔は見えないが、こんな爽やかに問題発言をしてくるような男、二人といるはずがない。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0531
Ace " 「あれ、[firstname]、君もいたのか？」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0531_5
Ace " 「君みたいにうまく水撒きが出来なくてさあ、よかったらコツを教えてほしいんだけど……」"
$ hi_mes()
play sound se_0028
pause .1
play sound se_0683
pause .1
play sound se_0028
pause .1
play sound se_0682

scene hn_spr_01 with dis

show per_t_01_7 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0487
Peter " 「エース君！！\n
なんだって、君がそんなところで水撒きなんてやっているんですか！」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 生け垣の向こうへペーターが発砲したが、発砲した数だけ金属音が返ってくる。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 見えないところに赤い騎士がいるのは間違いなさそうだ。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0532
Ace " 「ペーターさんまでいるなんて、ひょっとして、陛下も？\n
なんだよ、皆して仲よくして、俺だけ除け者なんて冷たいなあ、はははは」"
$ hi_mes()
hide per_t_01_7
show per_t_01_7 at left

show viv_t_01_8 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0449
Vivaldi " 「エース、貴様という奴は何度わらわをずぶ濡れにすれば気がすむのだ！？\n
今度という今度は……！！」"
$ hi_mes()
hide per_t_01_7
show per_t_01_4 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0488
Peter " 「どうせ撒くなら、塩でも撒いてあげます！\n
二度と迷い出て来ないように、念入りに！」"
$ hi_mes()
play sound se_0028
pause .5
play sound se_0028
pause .5
play sound se_0028
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " ペーターはそんなことを言いながら銃を撃ち続けている。"
$ hi_mes()
$ hi_mes()
hide viv_t_01_8

hide per_t_01_4


scene bg_gen_sky_spr_day with dis
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_5")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_06_17")
T " （なんて言うか、殺伐としているというか）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " これが彼らなりのコミュニケーションだということは分かっているが、それにしても……。"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0489
Peter " 「～～～～～～～～、今度こそ仕留めて差し上げます」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0533
Ace " 「そういうこと言わないでよ、ペーターさん。俺も皆の役に立とうとして、率先して水撒きの手伝いなんて似合わないことをしていたんだからさ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0490
Peter " 「似合わないと分かっているなら、余計なことに手を出さないでください！」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " ハートの城の庭に、銃声と金属音が響く。"
$ hi_mes()
play sound se_0028
pause .5
play sound se_0028
pause .5
play sound se_0683
pause .5
play sound se_0682
$ hi_mes()

play music happy_a_ali

scene hn_spr_01 with dis

show viv_t_02_7 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0450
Vivaldi " 「まったく、本当に男どもは騒々しい」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_2")
T " 「ビバルディ」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_05_15")
T " （またずぶ濡れになっちゃって）"
$ hi_mes()
play sound se_0252
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 私は立ち上がると、近くにあったタオルで彼女の長い髪を拭った。\n
せっかくの巻き毛がしっとりと水を含んで重くなっているのが嘆かわしい。"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_17")
T " 「大丈夫？\n
風邪なんてひかないでね」"
$ hi_mes()
hide viv_t_02_7
show viv_t_03_8 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice viv_f0451
Vivaldi " 「そういうおまえこそ、濡れてはおらぬか、[firstname]？」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_06_15")
T " 「うん、私は平気よ」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_01_7")
T " （代わりにペーターがずぶ濡れになったけど）"
$ hi_mes()
hide viv_t_03_8
show viv_t_03_10 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice viv_f0452
Vivaldi " 「ふむ、ならばよい。\n
あやつも、おまえの傘代わりくらいにはなるのだな」"
$ hi_mes()

show per_t_01_1 at center
hide viv_t_03_10
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
Peter " 「～～～～～～～～！」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0534
Ace " 「ペーターさんってば、そんなに怒らないでよ。\n
よく言うじゃないか、二度あることは三度あるって……、うわわっ」"
$ hi_mes()
hide per_t_01_1

play sound se_0028
pause .5
play sound se_0028
pause .5
play sound se_0683
pause .5
play sound se_0682
pause .5
play sound se_0028
pause .5
play sound se_0683
pause .5
play sound se_0028
pause .5
play sound se_0682
$ show_mes("frame_gen_heroine")

$ face("ali_t_01_1")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_06_17")
T " 「あっちはまだ落ち着かなさそうだけどね」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_02_4")
T " （エースも懲りないというか、ペーターも諦めきれないのか）"
$ hi_mes()

show viv_t_01_4 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice viv_f0453
Vivaldi " 「あんな阿呆どもが部下かと思うと、頭が痛くなるが……、[firstname]。\n
ここがおまえのいる場所じゃ、逃がす気はない」"
$ hi_mes()
hide viv_t_01_4
show viv_t_01_6 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice viv_f0454
Vivaldi " 「あいつらが気に入らなかったら、わらわに言うのだぞ。\n
おまえに不快な思いをさせるなど、極刑にしてやるからね」"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_06_8")
T " 「…………」"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 濡れたまま見上げてくる美しい女王様は、私に甘い。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 彼女だけでなく、生け垣を挟んでいる宰相や騎士も、結局は優しいところがある。"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " そうでなければ、今頃、私の首と胴体は離れてしまっているだろう。"
$ hi_mes()
hide viv_t_01_6


scene bg_gen_sky_spr_day with dis
$ show_mes("frame_gen_monologue")

$ face("ali_t_01_13")
T " （裁判だって……、私を思ってやってくれた）"
$ hi_mes()
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 兵士やメイド達の言葉は、余所者の私でも、この城の一員なんだと教えてくれた。\n
だからこそ、首を左右に振る。"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_02_8")
T " 「その必要はないわ」"
$ hi_mes()
play sound se_0028
pause .5
play sound se_0683
pause .5
play sound se_0028
pause .5
play sound se_0682
$ show_mes("frame_gen_togaki")

$ face("ali_t_06_16")
T " 銃声と金属音が、交互に響く。\n
安心や安全とは縁遠い、赤の城。"
$ hi_mes()
$ show_mes("frame_gen_heroine")

$ face("ali_t_03_1")
T " 「よく言うでしょう。\n
朱に交われば、赤くなるって」"
$ hi_mes()
$ show_mes("frame_gen_monologue")

$ face("ali_t_03_5")
T " （身体の中にあるものは違うけど。\n
彼らと同じ赤に包まれて、この城で暮らしていく）"

hide ali_t_03_5
hide frame_gen_monologue
with Dissolve(5)
scene black with Dissolve(5)

##endroll_b
