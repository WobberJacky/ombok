
scene map_bg_summer_day
with dis
label fushigi_end_amuse1:
$ clockanim()


scene map_bg_summer_day
with dis

scene bg_gen11_yuy_sum_day
with dis

play music gag3_a_ali

scene go_01 with Dissolve(1.2)
play sound se_0395

show yuuen_man_02_06 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice tan_f0049
Employee "「オーナーは鈍感すぎるんです！」"

hide yuuen_man_02_06
show yuuen_man_02_06 at left
show go_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0409
Gowland "「お、おい……。\n
おまえら、何もそんな集中的に指を差さなくても」"

hide yuuen_man_02_06
show yuuen_man_02_06 at left_center
hide go_t_02_4
show go_t_02_4 at center
show yuuen_woman_02_04 at right_center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
voice may_f0066
Employee "「戻ってきてくれたからいいものの、あのまま怒って帰ってきてくれなかったらどうするつもりだったんですか！？」"

hide go_t_02_4
show go_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0410
Gowland "「す、すまん、そんなに怒るなよ、悪かったって、な？\n
せっかく帰ってきてくれたんだから、た、楽しい話をだなあ」"

hide yuuen_woman_02_04
show yuuen_woman_01_06 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
voice may_f0067
Employee "「オーナーだけじゃありません！\n
ボリスさんも、ピアスさんも、デリカシーが足りなさすぎるんです！」"

hide yuuen_man_02_06

hide go_t_03_7

hide yuuen_woman_01_06


show bor_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_f0341
Boris "「ごめんごめん、ほ、ほら……、おっさんだってああ言っていることだし。\n
あんた達も機嫌直してくれって、な？」"

hide bor_t_03_11
show bor_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_f0342
Boris "「いつもの馬鹿明るいテンションはどこいったんだよ。\n
取り囲んで追い詰めるなんて、珍しいし……、いや本当、謝るからさ！」"

hide bor_t_01_9
show bor_t_01_9 at left
show pia_t_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pie_f0266
Pierce "「ぴい～。\n
お、俺だって別にいじめようと思ったわけじゃないのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "困り果てた様子でゴーランド達は従業員達から逃れようとしているが、何しろ人数が人数だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "文字通りネズミ一匹逃げ出す隙間もないくらいにぴったりと彼らは詰め寄っていた。"

hide pia_t_02_6

hide bor_t_01_9

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（あれじゃあ、ボリスがドアを繋げる暇もないわね。\n
さて、こっちもあとちょっとだわ、さっさと仕上げないと……）"

play sound se_0333
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "横から聞こえる幾つもの声を聞き流しながら、私は私で書類から視線を外さずにいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地に来たばかりの頃には、従業員の元気すぎる声に辟易したものだが、今は自分の仕事に集中出来るようになっていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（単に耐性がついただけかもしけないけどね）"


show go_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice gor_f0411
Gowland "「[firstname]、本当に悪かったって！\n
だから、こいつらをどうにかしてくれっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "壁に追い込まれた彼らから、時折私に助けを求める声と視線が向く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_4")
T "「同僚の皆が、私のことを気遣ってくれているんだもの。\n
それを無視するなんてこと出来ないわよ」"

hide go_t_03_7
show go_t_03_7 at left
show bor_t_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_4")
voice bor_f0343
Boris "「……あ、あんた、まだ怒っているのかよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「ふふふ、どうかしらね。\n
……怒っていないと、思う？」"

hide go_t_03_7
show go_t_03_7 at left_center
hide bor_t_01_3
show bor_t_01_3 at center
show pia_t_01_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice pie_f0267
Pierce "「ボリス、ボリス、駄目だよ、そんなこと言っちゃ！！\n
ますます怒らせるだけだよ～、怖い、怖いよ～」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

hide go_t_03_7

hide bor_t_01_3

hide pia_t_01_8

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_4")
T "（なんてね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らからは見えない角度で舌を出してやる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒りが冷めないぐらいだったら、戻ってきたりしない。\n
だが、せっかく従業員の皆が口を揃えて訴えてくれているのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（こういう機会は大切にしないとね）"


show yuuen_man_02_06 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice kaz_f0026
Employee "「反省が足りません、反省が！！\n
そもそもちゃんと謝ったんですか、三人とも！？」"

hide yuuen_man_02_06
show yuuen_man_02_06 at left
show yuuen_woman_02_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice chi_f0059
Employee "「……最低ですよ！」"


show go_t_03_7 at center
hide yuuen_man_02_06

hide yuuen_woman_02_04
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gor_f0412
Gowland "「いや、そんなことは……、おい、頼むぜ、[firstname]！何を言っても聞いちゃくれねえんだ、あんたから言って、こいつらを止めてくれよ！」"

hide go_t_03_7
show go_t_03_7 at left
show bor_t_01_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice bor_f0344
Boris "「あんた、何をすれば機嫌を直してくれる？\n
なあ、今なら特別サービスでお魚料理奢ってやるから、許してくれって」"

hide go_t_03_7
show go_t_03_7 at left_center
hide bor_t_01_9
show bor_t_01_9 at center
show pia_t_01_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice pie_f0268
Pierce "「君が帰ってきてくれて本当に嬉しかったんだよ、[firstname]！\n
だから、仲直りしようよっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「本当に反省したの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手元の紙から彼らのほうへ視線を向けると、縋るような三人と目が合った。"

hide go_t_03_7
show go_t_02_4 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0413
Gowland "「している、これ以上ないぐらいにしている！\n
すまなかった」"

hide bor_t_01_9
show bor_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0345
Boris "「あんたと喧嘩したままなんて嫌だよ、今回は俺も調子に乗りすぎたしね。\n
……悪かったと思っているんだ、ごめんな、[firstname]」"

hide pia_t_01_8
show pia_t_03_13 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0269
Pierce "「ごめんなさい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（まあ、ちょうどこっちも仕上がったところだし。\n
このあたりが潮時かしらね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らが従業員の皆に責め立てられている間に書いていた新しい企画書。\n
それを手にして、ぺらぺらと揺すってみる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「なら、私のお願いぐらい、聞いてくれるわよね？」"

hide go_t_02_4
show go_t_03_3 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_3")
voice gor_f0414
Gowland "「は？\n
お願いって……、俺らにか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「当然でしょう。\n
三人が好き勝手なことをしたんだから、皆で平等に協力してもらうわよ」"

hide bor_t_03_6
show bor_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_1")
voice bor_f0346
Boris "「おっさんやピアスと協力～？\n
俺、猫だからそういう集団行動は苦手なんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「……文句があるの、ボリス？」"

hide go_t_03_3
show yuuen_man_01_02 at left_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice tan_f0050
Employee "「あるなんて言うはずがないですよね！」"

hide pia_t_03_13
show yuuen_woman_01_06 at right_center
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice may_f0068
Employee "「この状況で言ったらどうなるかぐらい、分かっていますもんね？\n
あなたは、空気が読めない猫じゃないですよね！？」"

hide bor_t_01_3
show bor_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice bor_f0347
Boris "「……ないです、ありません」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "従業員達に再び詰め寄られて、ボリスは降参というように両手をあげる。"

hide yuuen_man_01_02

hide bor_t_03_11

hide yuuen_woman_01_06
show pia_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0270
Pierce "「お願い、いいよ、いいよ、なんでも聞いてあげるよ～！\n
お届け物？それともお片付け？」"

hide pia_t_01_2
show pia_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0271
Pierce "「俺が出来ることなんて、それぐらいしかないけど……。\n
君がしてほしいなら、喜んでやってくるよ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（そういう方向性のものじゃないんだけど……、聞かなかったことにしておこう）"

hide pia_t_01_6


play music amuse_mae_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「じゃあ、皆、賛成っていうことで。\n
さっそく準備にかかりましょうか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言質は取った。\n
従業員に取り囲まれている彼らの元へと近づく。"


show bor_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0348
Boris "「準備って……、なに、そんな、準備が必要な大ごとをするわけ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ううん、内容自体は簡単よ。\n
大した準備が必要なわけじゃないけど」"

play sound se_0470
pause .5
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「皆、よく自分の担当を確認してちょうだい」"

hide bor_t_01_2
show bor_t_01_2 at left
show go_t_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Gowland "「？？」"

hide bor_t_01_2
show bor_t_01_2 at left_center
hide go_t_01_11
show go_t_01_11 at center
show pia_t_03_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pie_f0272
Pierce "「これ、なあに、[firstname]？\n
大事なもの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「そうよ、とっても大事なものだから……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "{size=+20}「今度破ったりしたら、本気で殴るからね、あんた達」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕上げた企画書をゴーランドに押し付け、念を押しておく。"

hide bor_t_01_2
show bor_t_03_1 at left
hide go_t_01_11
show go_t_01_11 at right
hide pia_t_03_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0349
Boris "「こわ……、あんた、目がマジだぜ。\n
そんな殺気だった目で見なくても、同じミスはしな……」"

play sound se_0042


hide bor_t_03_1
show bor_t_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「！！！」"


hide bor_t_01_2
show bor_t_01_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0350
Boris "「え、あ……。\n
[firstname]、なあ、これ……？」"

hide gaaan1 with Dissolve(.3)

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "内容を横から見たボリスが、指をさして聞いてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「そうよ、それ、企画自体は手間がかからなくていいでしょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_4")
T "「いつも同じじゃあ飽きちゃうもの。\n
気分転換よ、気分転換」"

hide bor_t_01_9
show bor_t_03_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice bor_f0351
Boris "「いや、気分転換というか、これは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドに渡した書類から目を離して、私を見てくるボリスの目は「勘弁してくれよ」と物語っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、ここでそれを素直に口に出すほど、彼は迂闊ではないらしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……文句があるの、ボリス？\n
私がこの遊園地のために頑張って考えた企画には、協力してくれない？」"

hide bor_t_03_11
show bor_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice bor_f0352
Boris "「協力はするっ！\n
協力するけど……、これはなんていうか、他のものじゃ駄目かな？」"

hide go_t_01_11
show go_t_02_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice gor_f0415
Gowland "「はあ……、諦めろ、ボリス。\n
こうなったら腹を括るしかない、おまえも男ならびしっと着こなして見せろ！」"

hide bor_t_01_1
show bor_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice bor_f0353
Boris "「着こなしたくねえんだけど……。\n
おっさんだけならまだしも俺まで……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "がっくりと項垂れたボリスの肩を、ゴーランドが叩いた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一方、頭の上にある書類が見えないピアスはきょときょとと私と彼らを見比べている。"


show pia_t_01_8 at center
hide bor_t_01_3
hide go_t_02_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0273
Pierce "「ぴ？ぴ？え、一体何をするの、[firstname]？\n
俺、協力したいとは思っているんだけど、難しいことは苦手だから心配だよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_2")
T "「大丈夫よ、ピアス。\n
あなたの場合、にこにこしていれば問題はないから」"

hide pia_t_01_8
show pia_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_2")
voice pie_f0274
Pierce "「にこにこ？\n
うん、よく分からないけど、笑っていればいいんだね、[firstname]！」"

hide pia_t_01_6
show pia_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_2")
voice pie_f0274_5
Pierce "「俺、頑張るっ！\n
だから、頑張ったご褒美にちゅうさせてね！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「それはまた別問題よ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何も知らないピアスは言われたとおりに既に笑顔を浮かべている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_4")
T "（いつまでにこにこしていられるのか楽しみね）"

hide pia_t_01_10

$ hi_mes()

scene go_01 with Dissolve(.8)

scene bg_gen11_yuy_sum_day
with stripe_l_medium

scene bg_gen_sky_sum_day
with stripe_l_long

play music amuse_inside_p_ali
play sound se_0557
pause 1
$ hi_mes()
$ show_mes("frame_gen_chara")
voice tan_f0051
Employee "「遊園地にようこそ！\n
ただいまの時間帯の目玉は、あちらのアトラクションですよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice chi_f0060
Boy "「うわあ、すごい！\n
お父さん、早く行こう！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice kat_f0047
Father "「こら、走るんじゃ……！！？」"


show t_end_yuu1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0416
Gowland "「ようこそ、遊園地へ！\n
お子さんに、この時間帯は風船のサービスを……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice chi_f0061
Boy "「……う。\n
うわあああああ、変なのがいる！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice chi_f0062
Boy "{size=+20}「お父さん、変質者がいるよ！\n
怖いよ～～っ！！！」{/size} "

play sound se_0119
pause 1
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kat_f0048
Father "「こ、こら、待ちなさい！\n
そっちは出口で……」"

play sound se_0417

play music gag1_a_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
Gowland "「…………」"



$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地にやってきた子供が、ゴーランドを見るなり表情を変えて出口へかけていく。\n
父親は、慌ててその後を追っていった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "差し出して受け取ってもらえなかった風船がむなしく揺れる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0069
Employee "「しっかりしてくださいよ、オーナー！\n
お客さんを怖がらせてどうするんですかっ\n
？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0417
Gowland "「怖がらせてって……。\n
あのな、こんな格好をしていれば子供が逃げ出すのも仕方ないだろうが！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「ゴーランド」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お客さんが少し引いたところで、彼の元に行く。\n
着ぐるみを被ったゴーランドの傍に。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0418
Gowland "「あ、あんたか、[firstname]、なあ頼むから、せめて別の衣装にしてくれよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0418_5
Gowland "「俺の姿を見て逃げ出す客、これで五人目だぜ、あっちも似たようなものみたいだし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って示す方向には、男性用の制服を着たボリスと、女性用の制服を着たピアスがいた。"


play music cheerful_a_ali
hide t_end_yuu1
show t_end_yuu2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oda_f0019
Girl "「あー、にゃんこだ、にゃんこ！\n
尻尾が可愛い～」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0354
Boris "「お、おい、尻尾を引っ張るなって、俺のは付け尻尾じゃなくてだな？\n
ぎゃっ、握るなって言ってるだろ、やめろってば！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ゴーランドと同じく、先ほどまで風船を手渡していたボリスは、数人の子供に追いかけられて尻尾を狙われていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（子供にとって、あの尻尾ってとっても魅力的なのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこかの門番も欲しがっていたが、気持ちはなんとなく分かる。\n
そして、尻尾のあるもう一匹はというと。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0045
Boy "「あれー、このネズミさん、男の子なの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0025
Girl "「違うわ、女の子よ。\n
だって、スカートを履いているもの」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0275
Pierce "「うう、見ないでよ～。\n
なんで俺だけこんな格好なの、恥ずかしい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこにこしていればいいと言った言葉も忘れて、真っ赤になってもじもじしている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_3")
T "（マフィアの掃除屋がスカートを履くことなんて、まずないでしょうしね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "本当はボリスにも同じ制服を着せようとしたのだが、「ネズミとお揃いの服なんて絶対にいやだ」と断固拒否され、ピアスだけが女装する羽目になったのである。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_4")
T "「ほらほら、ボリスもピアスも、ちゃんと接客してちょうだい。\n
給料を出さないわよ」"

play sound se_0590
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice bor_f0355
Boris "「か、金なんかいらないから、こいつらどうにかしてくれよ、[firstname]！」"

play sound se_0465
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice oda_f0020
Girl "「にゃんこ、待って。\n
撫で撫でしたいの」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice pie_f0276
Pierce "「お、俺も給料いらない、なくていいからっ。\n
早く着替えさせてよーっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice hei_f0046
Boy "「ほら、俺って言ってる。\n
男の子だよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice tad_f0026
Girl "「えー、似合っているのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "役もちの二人だというのに、役なしの子供達に追いかけられている姿がおかしい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0277
Pierce "「似合わなくていい、似合わなくていいから！！\n
脱いでいい？ねえねえ、俺、もういいよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもにも増して小さくなったピアスがふるふるとしながら見上げてくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（女性ものの制服がここまで似合うと、ちょっと複雑なものがあるわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "マフィアの掃除屋だと知っているのに、ピアスにあの制服は私よりも似合っていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kaz_f0027
Employee "「駄目です、臨時オーナーの指示なんですから！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0063
Employee "「そういうことです！\n
さあ、にこにこと笑顔でお客さんを迎えますよーっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0356
Boris "「過酷すぎる……、急に元気になりやがって。\n
どうしてこんなことを俺がやってんだろ……、罰ゲームか何かかよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Girl "「！」"

play sound se_0492
camera at hpunch
camera at vpunch
pause .5
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "げっそりと項垂れたボリスの尻尾を、チャンスと見た子供がぎゅっと掴んだ。"

play sound se_0055
pause .5
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "{size=+20}「～～～～！！！？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「はいはい、じゃあ頑張ってね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（子供が逃げ出すゴーランドと、子供が寄りつく動物組）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足して二で割るとちょうどいいのかもしれないが……、そういうわけにもいかないだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0052
Employee "「ほら、背筋ぴんと伸ばしてくださいよ、オーナー！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0419
Gowland "「だあああっ、オーナーオーナーってうるせえぞ！\n
今のオーナーは、俺じゃねえ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0420
Gowland "「今のオーナーはあんただろう、[firstname]。\n
こいつらどうにかしてくれよっ」"

hide t_end_yuu2
show t_end_yuu3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_3")
T "「そうは言われても。\n
私も一時的に預からせてもらっただけだから、従業員教育は本来のオーナーにお任せするわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（臨時オーナーが少し言ったぐらいで聞くような人達とも思えないし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あと、三回時間帯が変わるまで、私はここの臨時オーナーという役目に就いている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勿論、私に出来ることなんて限りがあるから、大がかりなものは彼の手がなければどうにもならない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_1")
T "（まあ、名目はなんでもよかったんだけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "侯爵に、チェシャ猫、眠りネズミ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "協調性のない彼らに平等に罰を受けてもらうのなら、私が一番偉くなってしまうのが手っ取り早い。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0421
Gowland "「はあ……、分かった。俺だってここのオーナーだ、やってやろうじゃねえか！\n
風船１００個ぐらい、配りきれないはずがない！」"

play sound se_0654
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0053
Employee "「おお、それでこそ、オーナー！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0070
Employee "「では、張り切っていきましょう！」"


$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0357
Boris "「な、なあ、[firstname]、俺、風船は配り終わったんだから、終わりでいい？\n
ノルマは達成しただろう！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の尻尾を、子供達から取り戻したボリスが救いを求めて私を見てくる。\n
だが、私は首を縦には振らなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_4")
T "「駄目よ、私がオーナーでいる間はちゃんと働いてもらうから。\n
この後は、ワゴンでも引いて園内を回ってもらおうかな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_4")
voice bor_f0358
Boris "「鬼か、あんた！ちぇ、もう機嫌直してくれたと思ったのに。\n
……って、おまえら、引っ張るなよ、行くから！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_4")
voice kaz_f0028
Employee "「だって、誰かがついていないとどこに行っちゃうか分からないじゃないですか」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_4")
voice chi_f0064
Employee "「ワゴン販売の極意も、ばっちりと教えてあげますから！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_4")
voice bor_f0359
Boris "「……はあ。\n
あの書類、本当に高くついたなあ」"

play sound se_0745 volume .5
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引きずられるように二人に連れて行かれるボリスを見送りながら、思わず笑みが零れた。"


$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（でも、本当に嫌なだけだったら、ボリスだって付き合わないでしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこにでも行ける、そしてどこにも居場所がないと言った彼だ。\n
本当に嫌だったら、ドアを使って逃げたっておかしくない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが、罰ゲームに付き合ってくれるのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "なんだかんだといっても、彼も私には甘い。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0278
Pierce "「はい、風船だよ。\n
可愛い風船あげるから、遊びにいっておいで」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tad_f0027
Girl "「わあ、ありがとう！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0047
Boy "「僕にもちょうだい、ネズミさんっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0279
Pierce "「はい、これでいい？\n
手を離すと飛んじゃうから、ぎゅっと握っておいてね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（ピアスはピアスで馴染んできているみたいだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段がいじめられっ子のせいか、小さな子とは相性が悪くないようだ。"


play music honobono2_a_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0071
Employee "「あ、そうだ。\n
オーナー、あっちのアトラクションに人が並んでいるみたいなんで、見に行ってもらえますか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……あのあたりかしら？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに遠くに人影が集中しているのが、私がいる位置からも見える。\n
ここから見えるということは、既にかなりの人数が待っているはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（やっぱり、人気のものはどうしても混み合いやすいのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "臨時とはいえ、今の私はオーナーだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "解決まで行かなくとも、確認しなければいけないだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「そうね、とりあえず、様子を見に行ってくるわ。\n
ゴーランド、ピアス、一緒に来てくれる？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_14")
voice gor_f0422
Gowland "「ああ、いいぜ、じゃあこれはおまえらに任せるから、しっかり配っておいてくれ。\n
よし、行くぞ、ピアス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "傍にいた従業員に風船を押し付けて、ピアスに声をかける。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0280
Pierce "「ぴ？う、うん、ついていけばいいの？\n
風船もなくなっちゃったんだけど、俺、何か手伝えることある？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「そうよ。\n
手伝ってちょうだい、ピアス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手招きすると、彼はにこっと笑って飛んでくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0281
Pierce "「うん、いいよ。\n
君のお手伝いなら、いくらでもしてあげ……、むぎゅぅっ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0360
Boris "「おまえ、なに、自分だけ売り込んでいるんだよ、ピアス！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ボリス？\n
あなた、ワゴンセールに行ったんじゃ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "従業員に引きずられていったはずなのに、ピンクに黄色いジャケットを着た猫は目の前にいる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0361
Boris "「だって、こっちのほうが面白そうだし。\n
おっさんの手伝いなんて考えるだけでも嫌だけど……、あんたなら別だよ」"

hide t_end_yuu3
show bg_gen_sky_sum_day onlayer master
with dis

scene black
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0423
Gowland "「こらボリス、調子に乗んな！じゃれる暇があれば手伝えっ！\n
行こうぜ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "向けられる大きなグローブのついた手。\n
その向こうには、いつもとは違った服の猫とネズミ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（すごくおかしな風景なのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ごちゃごちゃしていて、統一感なんてどこにもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T "（それが、楽しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "似合っているようで、どこか不揃いだ。\n
誰も彼もが、ここが遊園地でなければ許されない姿。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（ここだから自然に映る）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "魔法が仕掛けられている、賑やかで、騒がしい場所。\n
おかしなところも全部、愛しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ばらばらということは、色々なものが混ざり合っていることでもある。\n
それをこの場所は教えてくれる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（遊園地なんて最初は苦手だったのに）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「ええ、行きましょう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_12")
T "（おかしな風景の中に、いつのまにか私も混ざっている）"

hide bg_gen_sky_sum_day with dis
hide frame_gen_monologue
hide ali_t_03_12
with Dissolve(5)

scene black with Dissolve(5)

stop music
##endmemory
$ renpy.movie_cutscene("endroll_b.mpg")
#return
