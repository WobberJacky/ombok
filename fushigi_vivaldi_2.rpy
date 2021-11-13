jump fushigi_common2_amuse
label fushigi_vivaldi2_2:

scene map_bg_summer_day
with stripe_l_medium

scene charasel_bg_amuse_day
with stripe_l_medium

play music amuse_inside_p_ali

scene yun_sum_01
with stripe_l_long
play sound se_0481
pause .50
play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬眩暈がしたような気がして、近くの壁に寄りかかる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あれ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（気のせいかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさか遊園地の賑やかさに身体がついていかなかった、なんてことはないだろう。\n
ここには何度も遊びに来ているし、宿泊させてもらったこともある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（……でも、何だか背筋がぞくぞくするというか。\n
ちょっと寒気がするような）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まるで、風邪をひいたときのような、悪寒。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "「そんなはずないわよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここ遊園地は今、暑い季節だ。\n
身体を冷やすようなことはない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（元々病弱なナイトメアじゃあるまいし。\n
そんな中で風邪なんかひいたら、間抜けすぎる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの水浸し事件で濡れたメイド服のまま、あちこちうろうろとしていたことは事実だが、あれぐらいで風邪をひくほど柔ではないはずだ。"


show pia_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0024
Pierce "「……あれ、[firstname]？\n
どうしたの、こんなところで壁に寄っかかっているなんて」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「ピアス……。\n
ちょっと眩暈がしただけよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "アトラクションの陰から現れたピアスが、心配そうにこちらを見ていることに気付いて、そう答えた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "熱があるわけでもなければ、身体がどこか痛むわけでもない。\n
城を出てきたことで少し気が昂ぶっているのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（ただ、それだけよ）"

hide pia_t_03_3
show pia_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice pie_f0025
Pierce "「ちゅう？\n
大丈夫なの、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「ええ、心配してくれてありがとう」"

play sound se_0158
play sound se_0584
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "礼をいうと、ピアスは頷いてそっと手を出してくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その手の意味が分からずにきょとんとしていると、彼は私の手を取って歩き出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ピアス、どこに行くの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（ピアスと何か約束していた記憶もないんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "丁度休憩の時間帯に入るところだったので、特に制止はしないでおいた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこに連れて行かれるのか分からないまま首を傾げていると、彼は名案を思いついたという表情で答える。"

hide pia_t_01_8
show pia_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0026
Pierce "「君は大丈夫っていうけど、何だか元気がないみたい。\n
だから、俺が君を元気にしてあげる！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……え？」"

hide pia_t_02_11
show pia_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice pie_f0027
Pierce "「君は俺を嫌わないし、いじめない。\n
優しくて、俺の大事な友達だから、元気にしてあげたいんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「私、そんなに落ち込んでいたの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（そんなつもりはなかったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地に来て、ゴーランドは私を客分扱いしてくれた。\n
しかし、何もせずに滞在させてもらうのは忍びない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう伝えると、彼は苦笑いをしながらも、アトラクションの待機列の整理等といった手が必要な場合のみ手伝わせてくれていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（ピアスから見て落ち込んでいるようじゃ、使えないと思われても仕方ないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "家出してきた人間を受け入れてくれるだけでも、ありがたいことなのに、迷惑をかけてしまっている。"

hide pia_t_01_6
show pia_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0028
Pierce "「うーん、俺には難しいことはよく分からないけど。\n
君に元気がないのは分かるよ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

hide pia_t_02_9
show pia_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice pie_f0029
Pierce "「だから、元気にしてあげたいんだ。\n
俺、君のこと大好きだから！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「……ピアス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "体調の不安定さも手伝ってか、いつもだったら穿った見方をしてしまう私が、今は素直に嬉しいと感じている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（仕事はアレだけど……。\n
こういうところは、ピアスって優しいわよね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（でも、どこで何をしてくれるんだろう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を引いて歩く彼の足取りは軽く、どこに行くのかまったく分からないままだった。"

$ hi_mes()
hide pia_t_03_6


scene charasel_bg_amuse_day
with stripe_l_medium

play music pierce_t_ali

scene pi_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ああ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（私って、どうして読みが甘いのかしら）"

$ hi_mes()

scene t_cut_viv2_1u with Dissolve(1.2)
pause 1

scene t_cut_viv2_1 with Dissolve(1.2)

show pia_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice pie_f0030
Pierce "「えへへ、これがね、俺のお気に入りのチーズで。\n
こっちもおいしいんだ」"

hide pia_t_01_2
show pia_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice pie_f0031
Pierce "「あれあれ、こっちだったっけ？\n
それとも、これが一番おいしかった奴だっけ？」"

play sound se_0690
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスは大きな袋を抱えて、中からチーズを取りだしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、目の前のテーブルの上は既に黄色の山が出来ていて、こんもりと盛り上がっている状況だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誘われるままに身体が小さくなる薬を飲み、ピアスの家に入るところまでは、私もまだよく分かっていなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（そうよね、ピアスにとっての元気になれる食べ物って、{size=+20}これだものね{/size}）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どこかの大きなウサギさんも、遊園地にいるピンクの猫も。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "食べ物に強い嗜好性があることを否定する気はないが、それを人に強要するのはどうかと思う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「ね、ねえ、ピアス。\n
いいわよ、もうその辺りで」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（むしろ、これだけ積まれたところで、食べられないって）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気持ちとしては、もう既におなかいっぱいになっている。"

hide pia_t_02_9
show pia_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0032
Pierce "「ちゅう、そんなことないよ。\n
おいしいチーズを食べれば、きっと君だって元気になれるからっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さな親切。\n
そして、大きなお世話。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "好意を持ってくれるのは嬉しいが、それがこういう形に昇華されてしまうと、ありがた迷惑になる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（悪意がないのは分かっているんだけど。\n
……素直に好意を受け取るのは難しい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私は余所者だから、好かれている。\n
そんなことを考えて、卑屈になってしまうのは癖みたいなもの。"


scene pi_01
with dis
hide pia_t_01_11
show pia_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0033
Pierce "「[firstname]、チーズは嫌い？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……嫌いじゃないけど、今、食べたいとは思えないのよ」"

hide pia_t_01_8
show pia_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice pie_f0034
Pierce "「そっかあ。\n
君、チーズが食べられないくらいに落ち込んでいるんだ、可哀想……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「！！？」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぐいっと引き寄せられ、何をされるのかと驚く。\n
するとピアスは、小さい子にするように私の頭を撫でた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ピ、ピアス！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然の行動に、思わず声が跳ね上がった。"

hide pia_t_02_10
show pia_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0035
Pierce "「慰めてあげる。\n
元気になーれ、元気になーれって」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（こ、こんな子供騙しみたいなことをまさか、ピアスにされるとは）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私よりもずっと大人な人にされるのならまだしも、ピアスに頭を撫でられるとは思わなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「も、もういいわっ。\n
元気になった、元気になったから！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "抱え込まれた頭を取り戻して、慌てて言う。\n
するとネズミの少年は、ぱあっと顔を輝かせた。"

hide pia_t_01_10
show pia_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0036
Pierce "「本当？\n
えへへ、俺なんかでも君を元気に出来るんだね、[firstname]！」"

hide pia_t_03_5
show pia_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0037
Pierce "「ちゅうもしてあげようか？」"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "{size=+20}「それはいい！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今にもキスをしようと顔を近付けてきたピアスを、私は全力で払いのけたのだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（……あ、でも確かに少し元気が出たような気もする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "うかうか落ち込んでいられないと言うべきなのかもしれないが。\n
少なくともピアスといると、城で感じていた自己嫌悪は薄れてくれる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（紛れてしまっているだけで、解決にはなっていないんだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも気の持ち方一つで、どうにか回ってくれる。"

hide pia_t_03_10
show pia_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0038
Pierce "「ちゅう。\n
どうして、皆、俺がちゅうしようとすると逃げちゃうんだろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首を傾げるネズミは一人自問を続けている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「……ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その背中に小さく、感謝を告げたが多分聞こえていないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（今度おいしそうなチーズがあったら、買ってきてあげようかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを思う程度には、私も彼の優しさに救われている。"

hide pia_t_01_13

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music pierce_t_ali

show pia_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pie_f0039
Pierce "「あ、いけない！\n
忘れていた！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「どうしたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの後、二人で珈琲を飲んだり、昼寝をしたりして何をするでもなくだらだらと私達は過ごしていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスもお気に入りのチーズを囓って上機嫌だったはずだが、今は慌ただしく家の中をぐるぐると走っている。"

play sound se_0590
play sound se_0690
hide pia_t_03_3
show pia_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0040
Pierce "「俺、この時間帯、仕事に行けって言われていたんだった！\n
大変だ、大変だよっ」"

hide pia_t_01_3
show pia_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0041
Pierce "「エリーちゃんに怒られちゃう！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「仕事なら、早く行かなくちゃ。\n
どこまで行くの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "盛大な音を立てて部屋を走りまわるピアスに問いかける。"

hide pia_t_02_6
show pia_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0042
Pierce "「ええと……、ど、どこだったっけ？\n
ええと、ええと……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ばたばた。\n
室内を走り回るピアスは、どうしようと繰り返してばかりで落ち着かない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（仕方ないわね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「ピアス！」"

play sound se_0055
hide pia_t_01_4
show pia_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
Pierce "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "走り回る相手の尻尾を掴み、強制的に止めた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「少し落ち着いて。\n
ほら、忘れものがあったら大変でしょう、身支度ちゃんと整えて、早く行きなさい」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（私はお母さんか）"

hide pia_t_03_3
show pia_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice pie_f0043
Pierce "「……そ、そうだね。\n
早く準備していかないと、皆に怒られちゃうもんね」"

hide pia_t_01_8
show pia_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice pie_f0044
Pierce "「ありがとう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「どういたしまして」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の仕事がどんな仕事なのか、私も知らないわけではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人を傷つける。\n
あるいは、傷つけるよりももっと酷いこともする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスは帽子屋ファミリーの掃除屋だ。\n
その背後で流れるものを知りながら……、それでも私は彼に怪我がないことを願ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "偽善で構わない。\n
自己中心的と言われても仕方ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（だって、こんなお節介なネズミがどこかで怪我をしたら、可哀想だもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思う気持ちは、顔も存在も知らない誰かの命を心配するよりも、ずっと強い。"

$ hi_mes()
hide pia_t_01_5


play music amuse_inside_p_ali

scene yun_sum_01
with stripe_l_long

show pia_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pie_f0045
Pierce "「じゃあ、行ってきます！\n
……って、あわわわ、危ない、危ない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……ちゃんと前を見て歩きなさいよ」"

hide pia_t_03_3

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（先が思いやられるなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地の入り口近くまでピアスを見送って、私は気付いてしまった。"


scene t_cut_viv2_2
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「この薬、残りが大分少ないけど……。\n
足りるのかしら？」"


scene t_cut_viv2_2u
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスの部屋から出てくるときに渡された、元の大きさに戻る薬を振ってみる。"

play sound se_0132
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頼りなく聞こえてくる水音は予想よりもかなり少ない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice man_f0000
Kusuri "「私を飲んで……。\n
さあ、どうぞ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（相変わらず喋る薬なんて不気味だけど、飲まないことにはどうしようもないし）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（……まあ、身体も小さいんだし、足りるかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピアスが行ってしまった以上、一先ずはこれを飲むしかない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

play sound se_0739
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ごくり、と残っていた薬を飲んでみる。"


scene yun_sum_01
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「やっぱり、少なかったのかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもなら数口飲めば本来の身体の大きさになれるはずなのに、薬はぎりぎり一口程度しかなかったせいだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "多少大きくはなったものの、本来の身長には程遠い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（小型犬よりもちょっと小さいぐらいの大きさかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先刻よりは少し高くなった視点であちこちを見渡してみたが、知り合いが通る気配もない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（どうしよう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少なくとも先ほどのサイズよりは大きいから、簡単に踏みつぶされることはないと信じたいが、ここは遊園地だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "当然、子供も多い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（蹴飛ばされないように気を付けながら、とりあえずゴーランドの家の近くまで戻ってみようかしら）"


scene bg_gen_sky_sum_day with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "運がよければ、途中で馴染みの従業員やボリスとも合流出来るかもしれない。\n
そう思って、歩き始めたが、何しろ小さな歩幅だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想以上に進まない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（ゴーランドのところに着くよりも先にピアスが帰ってきたら、笑うしかないわね）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice oda_f0001
Girl "「あー、可愛いお人形さんだっ」"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"


scene yun_sum_01 with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背後から聞こえた声にまずいと思ったときには、小さな女の子（いや大きさでいえば私のほうが今は小さいが）が私を持ち上げていた。"


show girl_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oda_f0002
Girl "「すごい、どうなっているのかな。\n
自分で動くお人形さんなんて、初めてだわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「いや、あの……。\n
私は人形じゃなくて」"

hide girl_1
show girl_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice oda_f0003
Girl "「すっごーい！\n
お人形さん、喋れるの！？」"

hide girl_5
show girl_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice oda_f0004
Girl "「ママにも見せてあげなくちゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "両手に私を持ったまま、子供は走り出そうとしている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（まずい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この子の親がどこにいるのかは知らないが、このまま人形扱いされるのは非常によろしくない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（握り潰されるとは思わないけど……。\n
万が一、この高さから落とされたら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供の手の高さとはいえ、今の私にとっては充分脅威を感じる高さだ。\n
どうしようかと考えをめぐらせてみても、いい解決方法など浮かんでこない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0040
Vivaldi "「待ちなさい。\n
その人形は、私のものだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（今の声は…………）"


play music vivaldi_t_ali
show t_viv2_1 onlayer master
with dis
hide girl_4

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこに現れた人物を見て、驚きに目を見開く。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0041
Vivaldi "「勝手に持っていくなど、行儀が悪いことはやめなさい」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oda_f0005
Girl "「…………。\n
お姉さん？それとも、お兄さんなの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女がそう問いかけたのも無理はない。\n
今、遊園地に姿を見せている人物が本当にビバルディなのか、私も一瞬自信がなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐らく声を聞かなければ、すぐには気付けなかっただろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_6")
T "（女性もののスーツ姿は見たことあったけど、男装なんて初めて見たわ。\n
口調も、いつもと違うし……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも美しく巻かれていた綺麗な髪が、首筋のところで切りそろえられている。\n
ダークグレーのスーツに身を包み、襟元はきちっと黒いネクタイで絞られていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの女王然とした口調ではなく、どこか落ち着きのある口調。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（服の色が赤じゃないから、余計にそう感じるのかしら）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0042
Vivaldi "「おや、可愛いことを言うな。\n
だが、賢い女なら余計な詮索などせず、早く私にその子を返しなさい」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0043
Vivaldi "「私は内緒でここに来ているのでね、事を荒立てたくない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice oda_f0006
Girl "「……？\n
よく分からないけど、この子はあなたのなのね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0044
Vivaldi "「そういうことだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice oda_f0007
Girl "「うん、分かったわ。\n
はい！」"

play sound se_0267
hide t_viv2_1

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少女は素直にビバルディへ私を渡した。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を受け取った彼女は、柔らかく頷く。"


show viv_da_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0045
Vivaldi "「ありがとう。\n
目を離した途端にどこかに行ってしまったから、心配していたんだ」"

hide viv_da_01_3
show viv_da_01_3 at left
show girl_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oda_f0008
Girl "「見つかってよかったね、それじゃあ」"

play sound se_0465
hide viv_da_01_3
show viv_da_01_3 at center
hide girl_4
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供はビバルディの微笑みに照れたように笑い返して、そのまま走り去っていった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ビバルディよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "改めて私を持っている女性に尋ねると、彼女は呆れたように溜息をついた。"

hide viv_da_01_3
show viv_da_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0046
Vivaldi "「言ったであろう、わらわはお忍びなのだぞ。\n
自分からそう簡単に正体をばらすと思うのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（認めているようなものじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私にだけ聞こえる、小声のせいだろう。\n
その口調はすっかりいつものハートの女王に戻っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（それに……）"

hide viv_da_01_4
show viv_da_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
Vivaldi "「[firstname]？」"
$ fushigi_vivaldi2_3a_seen = False
menu:
    "……格好いい。":
        jump fushigi_vivaldi2_3a
    "いつものほうが落ち着く。":
        jump fushigi_vivaldi2_3b

label fushigi_vivaldi2_3a:
$ fushigi_vivaldi2_3a_seen = True
show t_viv2_2 onlayer master
with dis
hide viv_da_02_11

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「格好いいわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
Vivaldi "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice viv_f0047
Vivaldi "「なんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「前の会合のスーツ姿も綺麗で、格好良かったけど……。\n
その姿もすごく似合っているわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元々ビバルディは目鼻立ちのくっきりとした、凛とした美しさがある。\n
身体つきだって私とは比べものにならないほど、柔らかな線を描いているのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それを男性ものの服に押し込めている姿は、見ているだけで不思議な魅力を感じてしまう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0048
Vivaldi "「ふふ、そうか。\n
おまえがそこまで気に入るとは思わなかったが……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「でも……。\n
その服だと、きつくないの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "下世話な話だが、思わず視線が彼女の胸元に向かってしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "上着のデザインの関係からか、服の下にある膨らみはほとんど気にならないが、なくなったわけではないだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0049
Vivaldi "「おや……、気になるのなら、見るか？\n
それとも、触るか？」"


play music secret_a_ali
hide t_viv2_2
show t_viv2_3a onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「！！！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「い、いいっ！\n
そんなことしないでいいからっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "胸元に寄せられ、慌てて断る。\n
ビバルディに他意はないのだろうが、こちらが意識してしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（……部屋の中にある人形と同じサイズだものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "抱きしめやすいのは分かるが、出来るなら勘弁してもらいたい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0050
Vivaldi "「む……。\n
気にしたのはおまえではないか、なんだその態度は……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「だ、だって……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（何だか触ったり、見たりしたら……、おかしな気分になりそうなんだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、正確には既におかしな気分になっている。\n
服と、雰囲気がいつもと違うだけ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "中身は、私のよく知っているビバルディだと頭ではよく分かっているのに。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_7")
T "（心臓が飛びだしそうなほど、どきどきしているなんて）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_7")
voice viv_f0051
Vivaldi "「おかしな子。\n
格好いいと言ったり、わらわを見て顔を赤く染めたり……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_7")
voice viv_f0052
Vivaldi "「そんなにおかしくはないであろう？\n
さすがのわらわも男装の持ち合わせはなくてな、キングの持ち物を勝手に借りてきたのだが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（ああ、ビバルディらしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どんな姿形をしていても、彼女はやはり女王様だとそんなことを思う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「そういうときには一言断ったほうがいいんじゃ……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice viv_f0053
Vivaldi "「何を言う。\n
わらわの城のものをわらわがどう使おうが、わらわの勝手じゃ」"

jump fushigi_vivaldi2_4
label fushigi_vivaldi2_3b:
hide t_viv2_3a
show t_viv2_2 onlayer master
with dis


$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（格好いいんだけど……、何だか知らない人みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を見る眼の優しさも、冷たくも、甘くもなる雰囲気も、何も変わらないのに。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0054
Vivaldi "「なんじゃ、そんなに熱心にわらわのことを見て。\n
ああ、この格好のわらわに感銘を受けたのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「感銘も受けたけど……。\n
私はいつものビバルディのほうが好きだわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの薔薇の香水の香りもしない。\n
服の下に押し込められたビバルディの気配が、酷く遠く感じる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0055
Vivaldi "「そうか……。\n
それはそれで、何だか残念な気もするが」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0056
Vivaldi "「ふふふ、おまえがいつものわらわをどれほど好いているのかが分かっただけでも、よしとしようではないか」"


play music secret_a_ali
hide t_viv2_2
show t_viv2_3b onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「そ、その格好でキスは……っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "引き寄せられ、頬に口付けられて戸惑う。\n
ほんの軽い戯れに、わたわたと取り乱した。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0057
Vivaldi "「何じゃ、気に入らぬのか？\n
たかだか服が少し違うだけではないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「～～～～っ。\n
そ、それはそうなんだけど！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_7")
T "（何というか、とってもおかしな気持ちになるって言うか……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものビバルディのほうが、彼女らしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの彼女の姿のほうが好き。\n
そう頭の中では分かっているのに、気持ちがついてこない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0058
Vivaldi "「……ああ、そうか、そうか。\n
分かったぞ、[firstname]、おまえ、照れておるのだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にやりと書き込みたくなるような笑みを浮かべて、ビバルディが私の顔を覗き込む。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0059
Vivaldi "「この世界の男どもときたら、どいつもこいつもろくなものではないからな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0059_5
Vivaldi "「そんな中にわらわのような理想的な存在がいたら……、ときめかずにはいられまい？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice viv_f0060
Vivaldi "「ふふふ、可愛い子。\n
サイズだけでなく、おまえは本当に愛らしいのう」"

jump fushigi_vivaldi2_4
label fushigi_vivaldi2_4:

play music amuse_inside_p_ali
hide t_viv2_3b

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を手にしたビバルディはそう言うと、ずっと握ったままだった私を小さな鞄の中に入れて歩き出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「え？\n
あれ、どこに行くの？」"


show viv_da_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice viv_f0061
Vivaldi "「その姿では、移動するのも大変であろう？\n
わらわが運んであげる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

hide viv_da_01_2
show viv_da_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice viv_f0062
Vivaldi "「ふふふ、まさかおまえをこうして運べる日が来るとはのう。\n
他の馬鹿どもに拾われる前に、わらわが拾えてよかった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "満足げに言うビバルディは、機嫌がいいのか、何とも軽い足取りだった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振動で揺れる鞄の中、必死に布にしがみついたが、彼女は気にした様子もなく歩き続けていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「わ……、と」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_12")
T "（そ、それにしても……。\n
わざわざお忍びで、一体何をしに来たんだろう、ビバルディ）"

hide viv_da_02_5

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music amuse_inside_p_ali

show t_viv2_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0063
Vivaldi "「それで、[firstname]。\n
何でおまえ、そんな可愛らしい大きさなのだ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地内にある、飲食店の一つ。\n
そのテラス席に座ったビバルディはテーブルの上に私を乗せると、改めてじっと見つめてきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "長い睫に縁取られた綺麗な眼が、どこか楽しげに私の姿を映している。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ピアスの家に行っていたから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "特に隠す理由もない。\n
素直にそう言うと、彼女は形のいい眉をぴくりと反応させた。"

hide t_viv2_4
show t_viv2_5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで上機嫌だった表情が瞬時に曇る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（ビバルディ、ピアスが苦手だものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくら姿形は凛々しい男の姿になっていても、こういう反応を見るとやはり中身は私のよく知る彼女なのだとほっとする。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0064
Vivaldi "「ネ、ネズミの家だと……？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0065
Vivaldi "「あのネズミ、おまえに一体何をしたのだ！？\n
こんな姿にして……、まさか～～～や～～～～～～など」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「違うわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（どこをどうやったら、そういう発想にいくのよ）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice viv_f0066
Vivaldi "「世の中の男は、大抵愚かなものじゃ。\n
そういった嗜好の持ち主もいるだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「……ビバルディ。\n
今のあなたも、知らない人には多分男の人に見えていると思うわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_4")
T "（それも、多分お人形さん趣味のある、ちょっと危ない方向の人に）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice mat_f0000
Customer "「ねえ、あれ……。\n
やっぱりそういうことよね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_4")
voice chi_f0001
Customer "「格好いいのに……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひそひそとそこかしこから囁かれる声を聞けば、どう見られているかは明らかだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（サイズが悪いわよね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（せめてもう少し大きければ、まだ……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（いや、それはそれで別の方向でまずいのか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "男の人は大変だなあと、こんなときにどうでもいいことを思う。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0067
Vivaldi "「あのネズミめ……。\n
次に会ったら、そのときにはわらわ自ら首を……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0046
Pierce "「大変、大変！\n
大事なことを忘れちゃっていたよーっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「！！！？」"

hide t_viv2_5
show t_viv2_6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ピアス？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いきなり現れたピアスに、ビバルディの顔が青ざめる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "テラス席から身を乗り出すように外を見れば、地面を這うように見ているピアスがいた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ピアス！\n
私はこっちよ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さい身体で精一杯の声を上げると、大きな耳がぴくんと動く。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0047
Pierce "「その声は、君だね、[firstname]！\n
よかったあ、俺、君に渡した薬が空っぽだったことに気が付いて、大急ぎで戻ってきたんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0048
Pierce "「えへへ、ちゃんと仕事も終わらせてきたんだよ。\n
偉いでしょう？」"

hide t_viv2_6

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "テーブルの上にいる私に気付いたのか、ピアスはほっとしたように立ち上がり、私のほうへと歩いてくる。"


show pia_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0049
Pierce "「君がどこかで潰されちゃったんじゃないかって心配したんだ、[firstname]。\n
無事でよかったよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、その歩みに顔色を変えているビバルディは、震えるような声で言った。"

hide pia_t_01_11
show pia_t_01_11 at left
show viv_da_01_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0068
Vivaldi "「ち、近付くな、このネズミがっ。\n
それ以上近付いたら、ただではすまさぬぞっ」"

play sound se_0679
pause .8
play sound se_0680
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉は勇ましいが、腰が完全に引けてしまっている。\n
先ほどまでは装えていた口調も、今はいつも通りだ。"

hide pia_t_01_11
show pia_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0050
Pierce "「ぴ？\n
その声は……、女王様？」"

hide pia_t_03_10
show pia_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0051
Pierce "「あれあれ、どうして、女王様がいるの？\n
それも、そんな格好で……」"

play sound se_0184
hide viv_da_01_8
show viv_da_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「！！！」"

play sound se_0454
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "間近に迫ったピアスに、とうとうビバルディは後退ってしまった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界で彼女を下がらせることが出来るのは、ピアスぐらいなものだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（本人にとっては不名誉なことだろうけど）"

hide viv_da_02_3
show viv_da_02_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice viv_f0069
Vivaldi "「う……、ネズミ、何でネズミなどのところにおるのだ、[firstname]！！\n
つ、次にはいい加減、城に戻るつもりで準備をしておくのだぞっ」"

play sound se_0591
hide viv_da_02_6

pause .5
hide pia_t_01_3
show pia_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後にそんな言葉だけを残して。\n
ピアスの前からビバルディは走り去っていった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（……まさか、ビバルディが逃げるなんて）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あまりの勢いに、引き止める隙もなかった。\n
プライドの高い女王様のあんな姿を見たのは初めてだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よっぽどネズミが苦手なのだろうが。"

hide pia_t_01_3
show pia_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Pierce "「？？」"

hide pia_t_03_12
show pia_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0052
Pierce "「女王様、結局何だったの、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……それを聞く前に帰っちゃったのよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（でも、次にはってことは……、多分また来てくれるんだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのときは、果たしていつもの服なのか。\n
それとも、あの男装の麗人としてなのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（……どちらにしても、ビバルディが自分から遊園地に来るなんて意外だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "チェスがそうであるように、女王は本来、簡単に城から出るような役どころではないはずだ。\n
その彼女がわざわざここまで来るなんて。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（今度来たら、理由を聞かなくちゃ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを思いながら、今はもう見えなくなった背中を私は視線だけで追いかけたのだった。"

$ hi_mes()
hide pia_t_01_13


scene charasel_bg_amuse_day
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_long
##endmemory
jump fushigi_common3_amuse##I think
