label gakuen_joker2:
scene bg_map_day
with dis
$ clockanim()


scene bg10_sb_day
with dis

play music classroom_day_p_wam

scene bg01_cr_day with Dissolve(1.2)
play sound se_0229

show kyoushi_c1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice sat_g0022
Kyousi "「では、ここで、本日の授業を終了します。\n
次回は、教科書の５８ページから始めます……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教壇の上では占い学の教授が授業を終えるための挨拶をしているが、すでに教室の中はそわそわと落ち着きのない空気に満たされている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "午前中、最後の授業というのはいつもこんな感じだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（こういうところは、シンフォニアも他の学校もあまり変わらないのね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世界一の魔法学校ということで、もっと別世界のような学校生活を想像していたのだ。しかし、どんな名門校であれ、学校は学校だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校を構成する生徒は、魔法に関する優秀な才能を持っていようと、やはり未成熟なのである。\n
その点は、他の学校と何も変わらない。"

hide kyoushi_c1_2

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教師が出て行くと同時に、わっと教室の中が賑やかになった。"

play sound se_0528

show girl_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0034
Seito "「[firstname]、ねえ、あなた……、今日のお昼はどうするの？\n
食堂に行くなら、一緒にどう？」"

play sound se_0528
hide girl_a2_3
show girl_a2_3 at left
with dis

show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0137
Seito "「あ、私も今日は食堂なの。\n
一緒に行ってもいい？」"

hide girl_a2_3
show girl_a1_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0035
Seito "「ええ、いいわよ。\n
[firstname]、あなたはどうする？」"

play sound se_0528
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「私も、食堂に行くつもりよ。\n
混ぜてもらってもいい？」"

hide girl_a1_8
show girl_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice may_g0036
Seito "「そのつもりで声をかけたのよ。\n
ふふ、それじゃあ移動しましょうか」"

hide girl_b1_2
show girl_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice tak_g0138
Seito "「そういえば、食堂のほうに、新しいメニューが増えたらしいわよ。\n
……覚悟を決めて挑んでみましょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……食堂の新作発表は、罰ゲームじみているわよね」"

hide girl_a1_3
show girl_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice may_g0037
Seito "「……実際、罰ゲームのようなものだもの。\n
こんなところでまで、生徒を試さなくてもいいのにと思わない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「生活の中に潜む試練よね……」"

hide girl_b1_8
show girl_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice tak_g0139
Seito "「まさしくね……」"

hide girl_a1_5

hide girl_b1_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな会話を交わしながらも、私は机の上を片付け、食堂に移動する準備を整えた。"


scene bg27_rk_day
with dis
play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの食堂には、イメージした料理を呼び出すという魔法がかけられている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはとても便利で、素晴らしい魔法ではあるのだが……、なにぶんメニューのレパートリーが広すぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ルーンビナスの定番から、私達にとってみればゲテモノ料理に分類されてしまうようなものまで、各種豊富に取り揃えられているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "優秀な魔法使いの卵であれば誰であっても、どこの国民であっても変わらず受け入れるというシンフォニアの方針によるものが大きい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろんな国出身の生徒達が困らないようにと、各国の郷土料理を取り入れていくうちにこれだけ多岐にわたるメニューが完成していったのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、その結果として……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しでも料理のイメージにぶれがあると、近くて遠い別の「何か」が出てきてしまうという困った事態が頻繁に発生するようになってしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そしていつからか、追加された新メニューを使っての力試しは生徒の間での恒例になってしまっていた。"


show girl_a2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0038
Seito "「新作メニューは、攻略が難しいのよね……。\n
何度か食べたことのあるメニューなら、味のイメージもしやすいんだけど」"

hide girl_a2_5
show girl_a2_5 at left
with dis

show girl_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0140
Seito "「新作は、こんなのが出ましたっていう情報から料理の味をイメージしないといけないものね……」"

hide girl_b1_9
show girl_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0140_5
Seito "「しかも、基本同じメニューのバリエーション違いが大量に追加されるというのがきつい……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……そうなのよね。\n
今回は、何が来るのか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "新しく追加されたメニューについて話しているうちに、食堂についた。"

hide girl_a2_5

hide girl_b1_1


scene bg12_dn_day
with stripe_l_long

play music dining_day_p_wam
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食堂の中に足を踏み入れると、すでに追加メニューに挑戦している生徒も多くいるのか、あちらこちらから歓喜の声やら苦悶の声やらが響いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……阿鼻叫喚ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しでもイメージを明確にするべく、情報を集めてみることにする。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0067
Seito "「見た目は普通のミートパイだよな……、ぱく、もぐもぐ……。\n
んぐぐぐぐぐ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0068
Seito "「ぐ……っ、辛っ！！！\n
辛すぎ……！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0056
Seito "「うわ、おまえパイの中から、煮えたぎった真っ赤な何かが出てきてるぞ！？\n
……もしかしてそれ、地獄風ミートパイなんじゃないのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0069
Seito "「み……っ、水……っ！！\n
喉が、喉が焼ける……っ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_10")
T "（……地獄風ミートパイ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名称からして、恐ろしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤いソースや、辛いソースを使った料理に地獄風という名前がつくのはよくあることだが、シンフォニアで聞くともっとリアルに聞こえてしまう。"


show girl_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0039
Seito "「あ、[firstname]、これが今回の追加メニューみたいよ。\n
あなたも見るでしょう？」"

play sound se_0472
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ありがとう、助かるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今回の追加メニューについてのお知らせを渡されて、それに目を落とす。\n
いかにも手作りといった様子のビラだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのビラに、何種類かのミートパイの名が書かれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（なになに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「田舎風ミートパイ、地獄風ミートパイ、創作ミートパイ、斬新なミートパイ、海鮮風ミートパイ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……もはや、名前からは味のイメージが出来ないわね」"

hide girl_a2_2
show girl_a2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice may_g0040
Seito "「また難題がきたわね……。\n
ミートパイをイメージすると、この五つのうちのどれかが来るというわけよね……？」"

hide girl_a2_5
show girl_a2_5 at left
with dis

show girl_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice tak_g0141
Seito "「一番の問題は、普通のミートパイがメニューに含まれていないことよ……っ！\n
ノーマルなミートパイはどこ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……もっともなツッコミだけど、普通のはなさそう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "バリエーションやら発展系に力を入れすぎた結果なのか、ベースとなる基本のミートパイの存在が抜けて落ちている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それともノーマルなミートパイは元々メニューに含まれており、今回新たにこの五種のバリエーションが追加されたということなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達はビラを片手に、空いている席へと腰を落ち着けた。"

hide girl_a2_5
show girl_a2_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0041
Seito "「さあ、挑戦するわよっ！\n
地獄風でも田舎風でも、なんでもくるといいわっ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……本当に？」"

hide girl_a2_7
show girl_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice may_g0042
Seito "「……ごめんなさい、嘘ついたわ。\n
地獄風だけは、絶対に避けたいわね」"

hide girl_b1_4
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice tak_g0142
Seito "「右に同じく。地獄風以外なら、何とかなる！\n
……あなたも挑戦するでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（どうしようかしら……）"
$ gakuen_joker2_2a_seen = False
menu:
    "ミートパイに挑戦する。":
        jump gakuen_joker2_2a
    "別の料理にする。":
        jump gakuen_joker2_2b
label gakuen_joker2_2a:
$ lovechara_jokbla_points =+ 1
$ gakuen_joker2_2a_seen = True
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（ここまで盛り上がっているんだもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私だけ挑戦しないわけにもいかないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これも、付き合いというやつだ。\n
よし、と覚悟を決めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「ええ、もちろん。\n
私も挑戦するわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達はそれぞれ、ミートパイのイメージを思い描く。"

play sound se_0034
pause .2
play sound se_0034
pause .2
play sound se_0034

show white onlayer master with Dissolve(1.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前に、それぞれ白い皿の上に乗ったミートパイが現れた。\n
ほかほかと湯気をたてていて、とても美味しそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この段階では、三つのミートパイに違いはないように見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……そう、問題は具材よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "果たして、中に入っているのは何なのか。\n
当たりなのか外れなのかを確かめるべく、私達はそれぞれ覚悟を決めて、ミートパイを手にとった。"

hide girl_a2_5
show girl_a1_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0043
Seito "「い、行くわよっ」"

hide girl_b1_3
show girl_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0143
Seito "「ええ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_6")
T "「……覚悟は出来ているわ」"

play sound se_0609 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごくり、と鳴ったのは私の喉か、それとも彼女らのうちの誰かのものか。\n
私達は香ばしい匂いを放つミートパイへとゆっくりと齧りつく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さくっとしたパイ生地の歯ごたえに続いて、とろりと熱々の中身が溢れてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（こ、これは……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（……ポテトと、ベーコン？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ホクホクのジャガイモに、コマ切れにされたベーコンが塩味をプラスした素朴な味わいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ミートパイといった感じではないが、これはこれで美味しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「じゃがいも……。\n
いもを使っているから田舎風？」"

hide girl_a1_7
show girl_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice may_g0044
Seito "「私のは……、えびやイカが入っているから海鮮風ね」"

hide girl_b1_5
show girl_b2_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice tak_g0144
Seito "「私のは、トマトソースで野菜と和えられた豆がいっぱい入っているんだけど……。\n
これ、何……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……創作ミートパイ？\n
ほら、大豆は畑の肉っていうし……」"

hide girl_b2_9
show girl_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice tak_g0145
Seito "「そ、それなら本物のお肉がよかったな……。ああ、でもあえて肉を使わないっていうなら、斬新なミートパイかもしれないわよね」"

hide girl_a1_3
show girl_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice may_g0045
Seito "「豆と野菜だけならダイエットにはよさそうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、地獄風だけは避けたいという切実な祈りは聞き届けられたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（……飛び込んでみれば、あっけなくうまくいくこともあるわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なぜか、思い出すのはジョーカーのこと。\n
秘密の部屋より秘密の詰まっていそうな、あの男。"

hide girl_a2_2

hide girl_b2_5
##[chara2 PAY ATTENTION="false"]
jump gakuen_joker2_3
label gakuen_joker2_2b:
$ lovechara_jokwhi_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……やめておこう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今のところ分かっているのは、地獄風ミートパイが激辛危険物ということぐらい。\n
他の４種については、名前しか分かっていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その名前から味の予測はほぼつかないのだから、ミートパイのイメージは地獄風に毒されている可能性がある。\n
はずれを呼び出す確率は高い。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……私、堅実派なの」"


show girl_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice may_g0046
Seito "「えええええっ！？\n
ここまできて、挑戦しないなんてあんまりだわ！」"

##[rchara2 PAY ATTENTION="false"]
show girl_b1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice tak_g0146
Seito "「そうよ！一緒にとんでもないものを出して、涙しましょうよ！\n
皆で食べれば怖くないって言うじゃない！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「{size=+20}言わないわよ。{/size}\n
そもそもどうして、地獄風が出てくるって決定事項なのよ！」"

hide girl_b1_7
show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice tak_g0147
Seito "「……いや、なんとなく……。\n
今のところ、地獄風が一番インパクト強いから……」"

hide girl_b1_2
show girl_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice tak_g0148
Seito "「間違いなく、今ミートパイをイメージすると、地獄風の要素が混ざるわよね……。\n
……危険だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「それでも、挑戦するの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はやめておきたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「まあ、一口ぐらいなら食べてみたい気もするけど……」"

hide girl_a2_4
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice may_g0047
Seito "「そうね……、やめておこうかしら。\n
もうちょっと情報が出揃ってからでもいいわよね」"

hide girl_b1_5
show girl_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice tak_g0149
Seito "「危ないことに首をつっこまなくても……、ね。\n
……ちょっと、面白そうだったんだけど」"

play sound se_0034

show white onlayer master with Dissolve(1.5)

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "残念そうな彼女達。\n
だが、いたって普通の昼食をテーブルへと呼び出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうに、身を賭けてのネタに走る気にはなれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲からミートパイに一喜一憂する声がこだまする中、私達は堅実に昼食をとった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……危ないことには、飛び込んだりしないほうがいいわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なぜか、思い出すのはジョーカーのこと。\n
秘密の部屋より秘密の詰まっていそうな、あの男。"

hide girl_a2_1

hide girl_b1_9
##[chara2 PAY ATTENTION="false"]
jump gakuen_joker2_3
label gakuen_joker2_3:
with dis
$ hi_mes()

scene bg10_sb_day
with stripe_l_medium

scene bg20_gd_day
with stripe_l_long

play music garden_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昼食の後、午後の一番最初の授業は空きだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たまたま取れる授業がなかったので、無理に詰めることはせず、自習時間として空けておくことにしたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "といっても、実際に自習に使うのは次の授業で小テストがあったりするときぐらい。基本的には、読書に当ててしまうことが多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "図書館に訪れてもいいし、借りてきた本をどこか別の場所で読んでもいい。\n
今日は天気がいいので、読みかけの本を片手に中庭に出ることにした。"

play sound se_0624
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもの木陰へと向かう。\n
午後の授業が始まったこともあり、周囲にはひとけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中庭全体がまったくの無人というわけではないが、人影はまばらだ。"

play sound se_0251 volume .8
pause .5
play sound se_0717
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お気に入りの位置。\n
木陰に腰を下ろして、本を開く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_14")
T "（……そういえば、ジョーカーとはここで初めて会ったのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一人で昼食のサンドイッチを食べているところに、彼がやってきたのだ。"

play sound se_0625
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_14")
T "（……ジョーカー？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "芝生を踏む足音が聞こえたときに、すぐさま彼を連想してしまったのは状況がよく似ていたせいだろう。"


show jo_m1_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（ほら、やっぱり）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔を上げると、彼がいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目が合ったのに、ジョーカーはぴくりとも表情を変えない。\n
ふいっと、すぐに視線をそらしてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひたすらに不機嫌そうだ。\n
なんだか……、凶暴といってもいい表情。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むすりと、つまらなさそうな顔で歩いている。\n
私に気付いていないのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……目、合ったわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか様子がおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無視するのもそうだが、こんなふうに不機嫌を表に出しているのは、なんとなく彼らしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の中にある彼のイメージは、いつだって飄々と笑顔を浮かべている。"

menu:
    "声をかけてみる。":
        jump gakuen_joker2_4a
    "見ている。":
        jump gakuen_joker2_4b
label gakuen_joker2_4a:
$ lovechara_jokbla_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ジョーカー」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声をかけてみることにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か、彼が平静ではいられないようなことでもあったのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼がポーカーフェイスを保っていられないほどのこととなると、よっぽどのことのような気がする。"

hide jo_m1_02_15
show jo_m1_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0034
Joker "「ああ？\n
なんだ、俺になんか用かよ」"

jump gakuen_joker2_5
label gakuen_joker2_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（もう少し、様子を見てみよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これだけ様子がおかしいのだ。\n
声をかけるのは、もう少し様子をみてからにしたほうがいいかもしれない。"

hide jo_m1_03_4
show jo_m1_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Joker "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……お？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "また目が合ってしまった。\n
今度は彼のほうから、顔を上げてこちらを見ている。"

play sound se_0625
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（お、おおお？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずんずんずんっと接近してくる。\n
そして私の間近までやってきた彼は、木陰に座る私を睥睨して口を開いた。"

hide jo_m1_03_11
show jo_m1_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0035
Joker "「じろじろ見てんじゃねーよ、クソガキ。\n
殺すぞコラ」"

jump gakuen_joker2_5
label gakuen_joker2_5:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "{size=+20}（誰、この人）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別人だ。\n
私の知っているジョーカーではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカーと同じ顔で、同じ声。\n
だが、その振る舞いはまるでチンピラだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "隻眼を細め、私を睨み付けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（兄弟？\n
親戚？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他人というには似すぎている。\n
まるきり本人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、今の「彼」に問いただそうとは思えない。\n
関わりたくない類の雰囲気がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ご……、ごめんなさい、人違いだわ。\n
知っている人に……、ジョーカーによく似ていたものだから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと視線をそらしながら謝罪の言葉を口にした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（さっさと謝って、お引き取りいただこう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしてジョーカーとそっくりなのかだとか、もちろん気になることはある。\n
聞いてみたいが、安易に聞けるような雰囲気ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼に比べたら、表面上はフレンドリーな帽子屋寮の住人達のほうがまだマシだ。"

hide jo_m1_03_10
show jo_m1_02_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0036
Joker "「ああ、あんた……、[firstname]＝[familyname]。\n
だろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え？\n
ええ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「な、なんで私の名前……」"

hide jo_m1_02_14
show jo_m1_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice jok_g0037
Joker "「はっ、てめえの名前だけじゃねえよ。\n
シンフォニアの関係者の名前なら、片っ端から把握してる」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（……まただ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカーと同じことを言う。\n
この広大な敷地に関わる人間の名前全部を把握しているなんて、無茶もいいところだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼もやはり、ジョーカーと同じくシンフォニアの関係者なのだろうか。\n
そう思うと、少しだけ彼に対する恐れが薄れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「あなたの名前も、教えてくれる？」"

hide jo_m1_02_8
show jo_m1_03_19 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice jok_g0038
Joker "「てめえみたいなガキに名乗る名前なんて、持ち合わせてねえよ。\n
……と、言いたいところだが、気が変わった」"

hide jo_m1_03_19
show jo_m1_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice jok_g0039
Joker "「教えてやるよ。\n
俺の名前は、ジョーカーだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「……は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怖さも忘れて、声をあげしまった。\n
ジョーカーにそっくりな……、ジョーカーではない彼の名前がジョーカー？ "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……訳が分からない）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「ジョーカーっていうのは……。\n
あなたにそっくりな、もう一人の彼の名前でしょう？」"

hide jo_m1_03_9
show jo_m1_03_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice jok_g0040
Joker "「ああ、そうだな。\n
あいつもジョーカーだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……で、あなたもジョーカーなの？\n
ああ、ファミリーネームがジョーカーなのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんとか＝ジョーカーと、なんとか＝ジョーカーの兄弟なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "並べてみていないので、どれほど似ているのか確信は持てないが、印象としてはそっくりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "左目を眼帯で隠しているところまで、完璧に。\n
服装まで同じなのだから、間違えないほうがおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（むしろ同一人物って言われても、信じちゃうわよね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ違うのは、その身に纏う空気と口の悪さだけだ。\n
ここまで言動が異ならなければ、同一人物にしか思えなかっただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（こっちのジョーカーは、とことん口が悪い）"

hide jo_m1_03_16
show jo_m1_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jok_g0041
Joker "「ば～か、ファミリーネームもクソもあるかよ。\n
俺はジョーカーで、あいつもジョーカーだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼がまるで違うものであるかのように名乗った名前が、まったく同一に聞こえたのは私の耳に問題があるのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「えっと……？\n
あっちのジョーカーもジョーカーで、あなたもジョーカーなのね？」"

hide jo_m1_01_7
show jo_m1_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice jok_g0042
Joker "「そうだって言ってんだろーが。\n
てめえはバカか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（なんて暴言……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これだけ言われると、怒りよりも呆れが勝つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の知っている飄々とした彼もジョーカーで、今こうして私の目の前にいる、壊滅的なまでに口が悪い彼もジョーカーなのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_14")
T "（双子みたいに、セットでいてくれたらいいのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのほうが分かりやすい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_6")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと、閃いてしまった。\n
彼らは本当に「ジョーカー」なのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子のように二人一緒にセットで現れていないということは、同じ顔をした人物が二人いるという証拠もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それでもこうして感じる気配は別人のよう……。\n
二重人格かもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「あなた達、もしかして……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二重人格なんじゃないの、と言いかけて躊躇った。\n
当たり前だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子は病気ではないが、二重人格は立派な病気だ。初対面の相手に「あなたは病気なのか」と問い質すなんて、マナー違反どころか失礼極まりない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（大体、二重人格なんて、そうそういないらしいし……）"

hide jo_m1_01_8
show jo_m1_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice jok_g0043
Joker "「なんだよ、言いかけてやめられると気持ち悪いんだよ。\n
俺らが、もしかすると……、何だって？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……なんでもない」"

hide jo_m1_03_4
show jo_m1_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
Joker "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "珍しいが、きっとそうだ。\n
心の病気だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう考えたら、彼の暴言だっていくらでも聞き流してしまえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ごめんなさい、あなたに用があったわけじゃないの。\n
ジョーカーが二人いるなんて思わなくて」"

hide jo_m1_03_11
show jo_m1_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice jok_g0044
Joker "「けっ。俺とアイツを間違えたってのかよ。\n
は、おまえ目ン玉腐ってんじゃねーのか？」"

hide jo_m1_01_7
show jo_m1_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice jok_g0045
Joker "「全然、似てねえだろうが。\n
見る目のねえガキだぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "{size=+20}（そっくりよ）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人並んで、鏡に映してみろといいたい。\n
それとも、実際に並べてみたら、全然似ていなかったりするのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（私の勘違い……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "受ける印象が似ているせいで、片方がこの場にいない今、私は彼らがそっくりだと勘違いしてしまっているという可能性もないことはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まったく同じといっていいほどにそっくりに見える。\n
言動は別人だが……、とても別個のものとは思えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……いえ、ちょっと、食堂でばたばたしていたから。\n
食べ合わせが悪くて、体調が悪いのかも」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無茶苦茶な言い訳だ。\n
だが、もうなんでもいいから誤魔化して、退散してしまいたい。"

hide jo_m1_01_10
show jo_m1_03_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0046
Joker "「食堂？\n
……新作メニューを試したのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ミートパイのこと？」"

hide jo_m1_03_18
show jo_m1_03_19 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jok_g0047
Joker "「ああ、それだ。なんか色々すげえらしいじゃねえか。\n
食堂のあたりから、間抜けな悲鳴が聞こえてたぜ、けけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……確かに、すごかったわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "主に地獄風が。\n
運悪くそれに当たった生徒は、名前どおりの地獄に叩き落されていた。"
if gakuen_joker2_2a_seen == True:
    jump gakuen_joker2_6a
jump gakuen_joker2_6b
label gakuen_joker2_6a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「試したけど、私は無事に美味しいパイを食べることが出来たわ。\n
えっと……、私が食べたのは、田舎風ミートパイだったの」"

hide jo_m1_03_19
show jo_m1_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice jok_g0048
Joker "「なにい？そこはやっぱり地獄風だろ、てめえ分かってねえなあ。\n
でもまあ、挑戦した勇気は認めてやるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（どうしてこう、偉そうなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、そうやって笑う顔からは、毒気を感じない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "からっとしている。\n
そういう意味では、愛想がなくとも、前に会ったジョーカーよりいい人に見えた。"

jump gakuen_joker2_7
label gakuen_joker2_6b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「あんな悲鳴を聞いた後じゃ、挑戦する気にもなれないわ。\n
私は堅実なのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほど、友人らとの会話でも繰り返した単語を主張する。\n
それに、彼は露骨に嫌そうな顔をした。"

hide jo_m1_02_1
show jo_m1_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0049
Joker "「堅実、ねえ。\n
そんなことばっかり言ってっから、てめえはつまんねえ女なんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（……っ！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしてこの男に、そんなことを言われなければいけないのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "（あ、あなたが私の何を知っているっていうのよ……）"

hide jo_m1_03_4
show jo_m1_03_17 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice jok_g0050
Joker "「楽しむってことを知らねえ馬鹿正直なガキはこれだからな。\n
あ～、つまんねえ」"

jump gakuen_joker2_7
label gakuen_joker2_7:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……そんなに言うなら、自分で挑戦してみたら？\n
本当にすごいのよ？色とか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も自分では食べていないので、その味について言及することは出来ないが、とにかく見た目の色彩も強烈だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口に運んだつわもの達が悲鳴をあげるのも納得できる、という色だ。"

hide jo_m1_03_17
show jo_m1_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_g0051
Joker "「ば～か、そういうのは、人が食ってるのを見て楽しむもんだろうが。\n
……よし、ジョーカーの奴にみやげで持っていくか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……やめなさいよ、可哀想でしょ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "運試し気分で、ある程度の覚悟があって口に入れても、あの阿鼻叫喚の地獄絵図なのだ。何も知らずに口に入れてしまっては、もっと酷いことになりそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の制止も聞かず、彼はニヤニヤと、いかにも悪巧みしていますといった顔で、食堂に向かっていく。"

hide jo_m1_02_5

play sound se_0625
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……あれ？\n
でも、二重人格だとしたら、自分で食べるってこと？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなら、覚悟は出来ているのだろうか。\n
しかし、人格が分かれているとすれば……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（……一応は、止めたわよ）"
$ hi_mes()
##[clearmessage PAY ATTENTION="false"]

scene bg_map_day
with stripe_l_long
##endmemory
jump gakuen_joker3
