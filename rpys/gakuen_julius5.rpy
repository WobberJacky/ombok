label gakuen_julius5:
scene bg_map_day with Dissolve(1)
$ clockanim()


scene bg_par15_rg_tow_day
with dis

scene bg_par02_ct_tow_day
with dis

play music dining_day_p_wam
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームから一夜明けた、朝のカフェテリア。\n
昨夜の熱気が残っているのか、いつもよりも賑やかだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "適当に空いている席を見つけて座った。\n
朝食ともなると毎朝ほとんど定番で、あまり変わり映えはしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の献立は、トースト・サラダ・スクランブルエッグにオレンジジュースだ。\n
たまにサラダの代わりにスープにしてみたりもする。"


show boy_a2_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0088
Seito "「俺、昨夜、ユリウス寮長のこと見直した……。\n
すごいよな、あの帽子屋寮の幹部を使ってたんだぜ？」"

hide boy_a2_6
show boy_a2_6 at left
with dis

show boy_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0052
Seito "「だよなあ。\n
実力がなきゃ、あの三人が言うことを聞いたりするわけがないだろうしな」"

hide boy_a2_6
show boy_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0089
Seito "「実力っていうか、影響力だよな……。\n
それをブラッド寮長が許可したわけだろ？」"

hide boy_a2_3
show boy_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0090
Seito "「ちゃんと他の寮長と対等にやりあえているっていうのが……。\n
自分の寮のことだから、なんだか、嬉しいな」"

hide boy_b1_4
show boy_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0053
Seito "「普段は頭脳派インドア派……、ぱっとしない引きこもり……とか何とか言われてるけど。でも、いざというときに強いってのも充分格好いいよ」"

hide boy_a2_2
show boy_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0091
Seito "「俺、塔でよかった……！\n
実は、ちょっと肩身狭かったんだよなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……おお）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "トーストを齧っているところで、どこからか聞き覚えのある声がと思ったら、彼らだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前、ユリウスが地味だとか塔がつまらないとか嘆いていた二人組だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、彼らも昨日の騒動を聞き及んでいるらしい。"

hide boy_a2_5

hide boy_b1_3

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（ふふん）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "認められているのはユリウスで、別に私が得意になるようなことではないと分かっているのに、顔がにやけてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり親しい友人が褒められているのを聞くと嬉しくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……親しい友人？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「いやいやいやいやいや。\n
朝っぱらから何を……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "果たして親しい友人でキスをするものだろうか、なんて自分につっこみをいれてしまいそうになって我に返った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱっと手を頬に押し当てる。\n
赤くなってないかどうかを、触れた体温から確かめようとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……馬鹿なことを）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "余計に動揺してしまうばかりだ。"


show tower_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0045
Seito "「おはよう、[firstname]。\n
……何、百面相しているの？」"

hide tower_a1_2
show tower_a1_2 at left
with dis

show tower_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0068
Seito "「おはよう、向かいに座っていいかしら。\n
あら、何を赤くなっているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目ざとい顔見知りの友人二人に発見されてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達は上級生で、私よりも学習のレベルは先に進んでいる。\n
そのため、学校の授業で一緒になるようなことはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その代わり、こうしてカフェテリアや、談話室といった寮の共同空間で会うとよくしてくれるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……赤くなっている？」"

hide tower_b2_3
show tower_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice chi_g0069
Seito "「ええ、赤くなっているわね。\n
どうしたの？何か、いいことでもあった？」"

hide tower_a1_2
show tower_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice hei_g0046
Seito "「昨夜のストームで？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（それぐらいなら、話しても平気よね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームというイベントを楽しんだ名残で、ちょっとばかり浮かれているということにすれば問題ないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、彼女達の問いかけにこっくりと頷いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ、そうなの。\n
周囲がストームの話をしているものだから、ちょっと思い出しちゃって」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ、男子が女子の部屋を目指して忍び込んでくるなんていうイベントだ。\n
そして、短時間とはいえ部屋の中で二人きりになれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思い出して頬の一つや二つ、赤らめたとしてもおかしくはないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（相手も分からないことだし……、適当に誤魔化しちゃえば……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこまでの打ち明け話をせずとも盛り上がることは出来るはず。\n
しかし、私の向かいに座った二人は嫌な感じでにんまりと笑った。"

hide tower_a2_8
show tower_a2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0047
Seito "「へえ、そうなの。\n
あのユリウス寮長と、思わず頬を赤らめちゃうような一幕があったのね？」"

hide tower_b2_2
show tower_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0070
Seito "「へええええ、それはそれは。\n
聞き捨てならないわねえ、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しゅるるるるっと蛇が絡みつくような声だ。\n
甘ったるく、懐柔するような響きを持っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言外に、逃がすものかという気迫すら感じる。\n
話のタネを見送るつもりはないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（まず……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "捕まった、と、焦る。\n
何かしら根拠があって、情報を掴んでいるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……なんで、相手をユリウス限定にしているのよ。\n
他の誰かかもしれないでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "往生際が悪いと知りながらも、そう言い返す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達も、確証がなければこんな言い方はしないだろう。\n
一応分かってはいるが、あがく。"

hide tower_a2_6
show tower_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0048
Seito "「あなた、自分が話題になっているのを知らないの？\n
それらの話を統合すると……、ねえ？」"

hide tower_b1_3
show tower_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0071
Seito "「今日の朝の話題はなんといっても、昨夜の騒ぎよ？\n
ストームも、もちろん盛り上がりはしたけれど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「どういうこと……？\n
私が話題って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達は、答えるかわりにひょいと肩を竦めて周囲を示して見せた。\n
つまり、自分で聞いてみろということなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのままでも充分聞こえるかもしれないが、手っ取り早く魔法を使って情報を集めることにした。"

play sound se_0496

show magic_b onlayer master with Dissolve(1.5)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

hide magic_b with grad_t_medlong
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲で話されている話題の中から、設定したキーワードにまつわるものだけを集める魔法だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人ごみの中で誰かと会話したり、騒がしい場所で特定の誰かを探すときなどに便利な魔法なのだが、ちょっと設定をいじるとこうして情報収集にも使える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今回キーワードに設定するのは、ずばり『私』だ。\n
私にまつわる会話を、周囲からピックアップする。"

hide tower_a2_3

hide tower_b1_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0081
Seito "「昨日の覆面退治すごかったわね。\n
ああでも、巻き込まれそうになった女の子は大丈夫だったのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0082
Seito "「ほら、部屋に突っ込まれてたでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0117
Seito "「ああ、あれだったらちゃんと寮長がフォローして、突っ込む直前に捕縛していたわよ。だから、彼女の部屋にも被害は出てないと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0083
Seito "「ああ、そうなの？\n
なら良かった」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0084
Seito "「新入生だったんでしょう？\n
初めてのストームであんな邪魔が入るなんて可哀想だもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0066
Seito "「ああ、でも、彼女はストームに参加してたのかな。\n
俺が行ったときには誰もいなかったし、人を待っているからって言っていたよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0067
Seito "「そのすぐ後にあの騒ぎだから……。\n
ストームに、ちゃんと参加できたのかなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……げげげげげ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他にも何人かの会話を聞いてみたものの、おおよそ中身は一緒だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆私の安否を気遣ってくれていて、そして同時に私のストームが失敗に終わらなかったかを心配してくれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（さすが、真面目な生徒が多いといわれる塔……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆、真面目な発想だ。\n
気遣いもしてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、その親切が今は痛い。\n
真面目な生徒も多いが、それでも年頃、好奇心旺盛な生徒だっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちろりと視線を持ち上げると、目の前の二人は変わらず。\n
にこやかに、私が口を開くのを待ち構えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"


show tower_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice hei_g0049
Seito "「で、どんないいことがあったのかしら？\n
ふふふ、是非とも聞かせてほしいわね」"

hide tower_a2_2
show tower_a2_2 at left
with dis

show tower_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice chi_g0072
Seito "「別に誰と、という部分は教えてくれなくてもいいのよ？\n
具体的かつ詳細に、何があったのかを教えてさえくれれば」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "{size=+20}（妥協してない）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "優しそうに、「言えるところだけ教えてくれればいいの」なんて言っている彼女達だが、すでに、私のストームの相手がユリウスだということは確定している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私から聞き出すまでもなく、状況証拠からそこまで推理してしまっているのだ。\n
更に悪いのは、それが外れていないということ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……うう」"

hide tower_a2_2
show tower_a1_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice hei_g0050
Seito "「ほらほら、唸ってないで白状しなさいよ」"

hide tower_b2_3
show tower_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice chi_g0073
Seito "「どんないいことがあったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は、とてもわくわくとしている。\n
だんまりを通すわけにはいかなさそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……それなら）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「あ、あのね、私、昨日ユリウスとは何の約束もしていなかったのよ。\n
そもそも、ストームがどんなイベントなのかも知らなかったし……」"

hide tower_a1_8
show tower_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice hei_g0051
Seito "「そうね。\n
新入生の女子生徒にとっては、サプライズイベントだもの」"

hide tower_b2_2
show tower_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice chi_g0074
Seito "「私もそうだったわ。\n
去年のストームが最初で、あんまりにも驚いて……」"

hide tower_a1_3
show tower_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice hei_g0052
Seito "「部屋に来た男子を変質者扱いして追い返したのよね……」"

hide tower_b2_5
show tower_b2_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice chi_g0075
Seito "「今思うと、申し訳なさで胸が一杯になるわね……。\n
……で、それがどうしたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どさくさに紛れて、彼女のささやかなトラウマを聞いてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「いや、だからね？\n
ユリウスが、ストームに参加するとも思っていなかったの」"

hide tower_a1_1
show tower_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
Seito "「……？？？」"

hide tower_b2_8
show tower_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
Seito "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は顔を見合わせては、クエスチョンマークを飛ばしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「えっと……、つまりね。\n
私、昨夜、確かにユリウスを待ってはいたんだけど、来るとは思っていなかったのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「だって、あの人ってああいう人でしょう？\n
ストームなんか参加しそうにないじゃない」"

hide tower_a2_5
show tower_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice hei_g0053
Seito "「……そうね、その通りだわ。\n
というか、言われてみれば、去年のストームにも寮長は不参加だったわ」"

hide tower_b1_8
show tower_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice chi_g0076
Seito "「そもそも、これまでのストームに寮長が参加したことがあったのかしら……。\n
そんな話、聞いたことないもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは研究生だ。\n
生徒ではなく、研究員といっていい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼がストームに参加しなくとも、あまり周囲は不審に思ったりはしないはず。\n
そして、彼の学生時代を知るのは、すでに教職員や学校関係者ぐらいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「その……、だからね？\n
笑わないで聞いてほしいんだけど」"

hide tower_a1_1
show tower_a1_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice hei_g0054
Seito "「笑ったりするものですか」"

hide tower_b1_5
show tower_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice chi_g0077
Seito "「ええ、笑ったりしないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人が約束してくれたのをしっかりと聞き届けてから、私は口を開いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……その。\n
ユリウスが来たことが、嬉しかったのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽそりと出来るだけ、限りなく小さな声で呟いた。\n
本題である何があったのかを隠すための方便とはいえ、その気持ちに嘘はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むしろ、口にしているうちに本気でそう思っている自分に気付いてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「だから……、来てくれただけで満足して終わり。\n
何もなかったのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（何も……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（……キスされたこと以外は）"

hide tower_a1_7
show tower_a1_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
Seito "「…………」"

hide tower_b2_2
show tower_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
Seito "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は、奇妙な顔で黙り込んでしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……何よ。\n
やっぱり、嘘っぽかったかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あまりに純すぎる説明だっただろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なまじ、進んでいるような関係よりも恥ずかしいかもしれない。\n
だんだんと、じんわりと頬に熱がのぼってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完全に嘘というわけでもないだけに、いたたまれない。\n
この場から逃走してしまいたい。"

hide tower_a1_8
show tower_a2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0055
Seito "「……いい。\n
すごくいいと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

hide tower_b2_5
show tower_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice chi_g0078
Seito "「あなたって、クールに見えて結構可愛いところがあるのね。\n
分かったわ、応援する」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……へ？」"

hide tower_a2_6
show tower_a2_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice hei_g0056
Seito "「ブリーズのことなら、私達に任せてちょうだい！」"

hide tower_b1_3
show tower_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice chi_g0079
Seito "「絶対にあなたを寮長のところまで送り届けてみせるわ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（心強い味方が出来た……の？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の話は、彼女達の何かを燃えたぎらせてしまったようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……っていうか、応援してくれているところを悪いんだけど、ブリーズ自体をあまりよく分かっていないんだけど）"

with dis
$ hi_mes()
hide tower_a2_7

hide tower_b1_2


scene bg_par02_ct_tow_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

play music corridor_day_p_wam

scene bg06_sk_h_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後、ユリウスの作業室を訪れた。\n
その前に一度カフェテリアに寄って、三人分の紅茶を用意する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう、三人分だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（たぶん、いるわよね……、ブラッド）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく、いるはずだ。"

play sound se_0290

scene bg_par23_jr_k with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0643
Blood "「ああ、君は立たなくてもいい。\n
私が出よう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0644
Blood "「ふふ。\n
可愛いお嬢さんと、紅茶には目がないんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……やっぱり）"

play sound se_0199

scene bg_par06_jr with stripe_l_medlong

play music tower_room1_p_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの作業室の扉を内側から開けて、私を招き入れてくれたのはブラッドだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアを開ける前から、私だと分かっていた口ぶりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が、ブラッドがいると見当をつけて今回は最初から紅茶を持ってきたということも、お見通しだったらしい。"


show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0203
Julius "「……ああ、おまえか。\n
何の用だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「何の用って……、特に用事はないわ。\n
ああ、昨夜の件についてはいろいろ聞きたいけれど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まずはブラッドへと手にしていた盆を差し出す。"

play sound se_0177
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドがすいっとカップを手に取ってから、その盆をユリウスの作業机の隅に下ろし、ユリウスの分を机に置く。"

play sound se_0546
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうに給仕をしている傍で、いきなりユリウスが錯乱した。"

hide yuri_m_02_9
show yuri_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「……～～～～！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（な、何……？）"


play music gag2_a_ali
hide yuri_m_02_3
show yuri_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice jul_g0204
Julius "「さ……っ、昨夜のことなんて、この男の前で話すことじゃないだろう！\n
おまえは何を考えているんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「ば……っ！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "{size=+20}何を考えている、は、おまえのほうだ{/size}。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の言っている昨夜の件というのは、例の覆面三人組のこと。\n
けして、その後の……キスとか、いい雰囲気になったことではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あんまりにも動揺しすぎて、ぽろっとティーカップが手の中から落ちた。"

hide yuri_m_03_7
show yuri_m_03_7 at left
with dis

show bra_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0645
Blood "「……おっと。\n
危ないな、お嬢さん」"

play sound se_0731 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのティーカップが床に落ちて、破片と一緒に中身をぶちまけてしまうより先にブラッドが動いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょい、と指先でさすだけで、空中でカップが静止する。"

play sound se_0095 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "スライムのようにふよふよと琥珀色の紅茶が空中で波打った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが指先を跳ね上げれば、まるで時計の針を逆に回したかのように、紅茶はカップの中へとおさまり、カップは私の手の中へと戻る。"

hide bra_m_02_6
show bra_m_02_15 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0646
Blood "「紅茶ももったいないが、それよりも火傷は危ない。\n
気を付けなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「え……、ええ。\n
ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "スライムっぽくうごめく紅茶を見てしまった分、再び口をつけるのが少々怖くなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、そんなことより、もっと怖いこと。\n
問題は、ユリウスと、それにつられた私の慌てよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、それらを見た、ブラッドの対応。\n
何より恐ろしいのは、そこだ。"

hide bra_m_02_15
show bra_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0647
Blood "「……それはさておき。\n
私も、昨夜の件について、是非とも議論を戦わせたいな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "{size=+20}「忘れてちょうだい」{/size} "

hide bra_m_02_2
show bra_m_02_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice blo_g0648
Blood "「いかにも面白そうなことを忘れろと？\n
そんなもったいないこと、出来るわけがないだろう」"

hide yuri_m_03_7
show yuri_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice jul_g0205
Julius "「{size=+20}忘れろ。{/size}\n
そして{size=+20}帰れ{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "低い声で、呻くようにユリウスが言う。"

hide bra_m_02_5
show bra_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0649
Blood "「……ふふん」"


play music tower_room1_p_ali
play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドはニヤニヤと私達を見ていたものの、何の気紛れかおとなしく帰るつもりになったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くいと紅茶のカップを傾けてその中身を干すと、空になったカップを机へと戻した。"

hide bra_m_03_4
show bra_m_03_15 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0650
Blood "「……ふむ。ずいぶんと嫌われてしまったらしい」"

hide bra_m_03_15
show bra_m_03_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0650_5
Blood "「では、私がいると昨夜の件について存分に話し合えないらしいので、帰るとしようか」"

hide yuri_m_01_3
show yuri_m_01_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0206
Julius "「……さっさと出て行け」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……ええ、そうしてちょうだい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別にブラッドが帰ったからといって、昨夜のキスの件についてを話し合うつもりはないが、からかわれるのも御免だ。"

hide bra_m_03_1
show bra_m_03_16 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0651
Blood "「では、お嬢さん。\n
すぐそこまで、送ってくれるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……はあ？」"

hide bra_m_03_16
show bra_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice blo_g0652
Blood "「すぐそこだよ。\n
この部屋を出たところまでで構わない、見送ってくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐそこだからこそ、見送りなど必要がないように思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（何を企んでいるのかしら）"

play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、おとなしく帰ってもらうためには、それぐらいの妥協は必要だろう。\n
私はブラッドを見送るべく、カップを一度机へと戻して外へ出た。"

play sound se_0199
hide yuri_m_01_13

hide bra_m_01_2


scene bg_par23_jr_k
with dis

play music secret_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その後を追うようにして、ブラッドも廊下へと出てくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（……ものすごく、ニヤニヤしているわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "面白そうなことを忘れたり放置するなど、もったいないという彼。\n
どうして彼は追及をやめてくれたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段のブラッドならば、己の欲に忠実だ。\n
したいと思ったことは必ずやりとげるし、欲しいと思ったものは必ず手に入れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは知りたいと思ったことに対しても、同様であるはず。\n
そういう人だと、短い付き合いでも心得ていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（どうして？）"


show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice blo_g0653
Blood "「……知りたいか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「え……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心を読み当てたかのような問いかけ。"

menu:
    "知りたい。":
        jump gakuen_julius5_2a
    "知りたくない。":
        jump gakuen_julius5_2b
label gakuen_julius5_2a:
$ lovechara_julius_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……知りたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そそのかされるように頷く。"

jump gakuen_julius5_3
label gakuen_julius5_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……遠慮したいわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誘惑から顔を背けるように、首を横に振る。"

jump gakuen_julius5_3
label gakuen_julius5_3:
hide bra_m_03_15
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0654
Blood "「ふ……」"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりと伸びてきたブラッドの腕が、私の腰を抱き寄せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！」"

play sound se_0051
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐっと引き寄せられて、咄嗟に仰け反った上半身。\n
しかし、すっぽりとその腕の中に収められてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逃げようと突っ張った片腕をブラッドの空いた片手にとられ、抵抗のしようがなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_11")
T "「……っ、何がしたいのよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大声を出して人に来られてしまっては、またとんでもない噂になる。\n
音量自体は抑えつつも怒気を滲ませる私に、ブラッドは余裕だ。"


show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0655
Blood "「ふふふ、あの鉄面皮の委員長にあんな顔をさせるとは……。\n
君も罪な女だな、お嬢さん？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「な……っ、何の話よ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（ユリウスの馬鹿……！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中でユリウスを罵倒する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一番油断ならない相手の目の前で、よくも思わせぶりなことを口走ってくれたものだ。\n
本当にろくでもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は懸命に掴まれた腕を引き、ブラッドの腕の中から逃れようとする。"

hide bra_m_02_2
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0656
Blood "「それで……、昨夜はお楽しみだったのか？\n
いいじゃないか、私達は友人だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「あなたみたいなろくでもない友人、持った覚えはないわよ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ニヤニヤとしながら、昨夜の一件について聞き出そうとする彼を睨みつける。\n
そんな私の視線は、彼の分厚い面の皮を射抜けない。"

hide bra_m_02_8
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0657
Blood "「ろくでなしほど味もある。\n
……試してみるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "{size=+20}「試しません！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐぐっと顔が近くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "綺麗な顔だとは思う。\n
素行不良だなんて言われてはいるが、その顔立ちは貴族的なものがあった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おまけに、夢に見たかつて好きだった人に雰囲気が似ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それなのに、今こうして抱きしめられていてもちっともときめきを感じない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッド＝デュプレという男に対して友人としての気安さは覚えるものの……、それは胸が苦しくなるような失恋の痛みとは無縁だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……ブラッドの印象が強烈すぎて、先生のイメージが飛んじゃったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「彼」に似た人なんていたら、きっと胸が潰れそうなほどに痛むと思っていた。\n
それなのに今、こんなにも平気でいられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いかにこのセクハラめいた腕から逃れようかと焦るような気持ちはあっても、悲しく辛い記憶とは無縁だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは今、目の前にいる彼の強烈な個性のおかげなのか。\n
それとも……。"

play sound se_0441
hide bra_m_03_4
show bra_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0658
Blood "「……おっと」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……{size=+20}！！！？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょいとブラッドが顔を引き、今までブラッドの頭があったその位置をすごい勢いで回転しているスパナが通っていった。"

play sound se_0563
$ flash(.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どんな魔力の込め方をしていたのか、スパナは壁に突き立った。\n
……当たったら死んでしまいそうな勢いだ。"

hide bra_m_03_5
show bra_m_03_5 at left
with dis
hide bra_m_03_10
show yuri_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0207
Julius "「見詰め合っているところを、邪魔して悪いな。\n
だが、公共の場で風紀を乱すな」"

play sound se_0492
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ！」"

play sound se_0051
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（わ……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐいっとユリウスが私の手を掴んで、引く。\n
ブラッドは抵抗することなく、おとなしく私の体を解放してくれた。"

play sound se_0210
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのため、勢い余ってぼすんっと私はユリウスの懐に飛び込むような形になってしまう。"

hide bra_m_03_5
show bra_m_01_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0659
Blood "「お嬢さんに見送ってもらうつもりだったが、委員長、君にまで見送ってもらえるとは光栄だ。\n
では、私は失礼しよう」"

play sound se_0774
hide yuri_m_02_7
show yuri_m_02_7 at center
with dis
hide bra_m_01_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひらひらと手を揺らして、ブラッドは去っていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさしく愉快犯の名が似合う、飄々とした男。\n
引っ掻き回すことだけが目的だったのは明白だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（ふ、普通、自ら当て馬を買って出る……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何を考えているのかが読めない。\n
いや、ある意味では明快なのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は単に、面白がっている。\n
退屈を疎み、楽しいことに目がないくせに面倒くさがり。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、退場もあっけない。\n
……残されたほうは面倒なことになるというのに。"


play music corridor_day_p_wam
hide yuri_m_02_7
show yuri_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0208
Julius "「……おまえも、もっとちゃんとしたらどうだ。\n
おまえに隙があるから、あんな男につけこまれるんだ」"

play sound se_0100
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "めきっと片手で壁にめり込んだスパナを引っこ抜きながら、ユリウスは顔を顰めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "眉間の皺の深度が、いつも以上に深い気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（結構、力持ち……、ってっ！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「何よ、私が悪いって言うの！？」"

hide yuri_m_03_7
show yuri_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
voice jul_g0209
Julius "「見詰め合って、抵抗もしていなかったようだしな。\n
ああ……、邪魔して悪かったか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ポイっと放るようにしてユリウスは私を解放した。"

menu:
    "ムカムカする。":
        jump gakuen_julius5_4a
    "悲しい。":
        jump gakuen_julius5_4b
label gakuen_julius5_4a:
$ lovechara_julius_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_9")
T "（ムカムカムカっ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とんでもなく腹立たしい。"

jump gakuen_julius5_5
label gakuen_julius5_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……信じてくれないんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、信じるも何も、私達には根拠となるような関係がない。\n
胸の奥がずきんと痛む。"

jump gakuen_julius5_5
label gakuen_julius5_5:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確かに本気で抵抗していたかと言われればそうではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、ブラッドに対して好意があるからではなく、彼が本気ではないと分かっていたからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本気なら、彼はもっと違う出方をするはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "付き合いの短い私でも分かるのだから、ユリウスだってそれは承知のはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "フンと私は息を吐いて、ぱたぱたと制服の裾を払い、身嗜みを整えた。\n
わざとらしく、これぐらいなんでもないといったふうを装う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ブラッドは、昨日の件で？」"

hide yuri_m_02_7
show yuri_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0210
Julius "「……ああ。\n
あの生徒三人組の処置についてをな」"

play sound se_0774
hide yuri_m_02_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "話題を変えてしまえば、ユリウスは不完全燃焼といったふうに顔をしかめながらも、渋々と応じた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして、すたすたと私に背を向けて作業室へと戻る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ついてこいとすら言ってくれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（いいわよ、勝手についていくから）"

play sound se_0774

scene bg_par06_jr with stripe_l_medlong

play music tower_room1_p_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "開き直って、勝手知ったる作業室へと足を踏みいれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "机に置いてあった紅茶を手に取る……、いや、取ろうとしたところで、それより先にユリウスがそれを回収した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……何よ」"


show yuri_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice jul_g0211
Julius "「そんなもの、飲むな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……あ。\n
もしかして、ブラッドに気を遣っていただけで、実は紅茶嫌いだったりするの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは珈琲のことを「醜悪な香りを放つ劇物だ」とか平気で罵るが、ユリウスはそんな彼とは違って常識人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口では構わないといいつつも、やはり紅茶嫌いだったのかもしれない。"

hide yuri_m_01_3
show yuri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0212
Julius "「あの男の匂いだと思うと忌々しい。\n
……制服をかいでみろ、うつっているのが分かる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

play sound se_0585
pause 1
play sound se_0320
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き返すより先に、もうユリウスは部屋の隅へと移動してしまっていた。\n
途中無造作に窓を開け、外の植え込みへと紅茶を捨てる。"

play sound se_0587
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……紅茶の香りが忌々しいのは、紅茶が嫌いなんじゃなくて？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かっと頬が熱くなる。\n
ドキドキと心臓が騒いだ。"

hide yuri_m_01_8
show yuri_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0213
Julius "「……紅茶に未練があるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「い、いいえ。\n
最近は紅茶よりも珈琲が好きになったの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんとかやりすごして、なんとかいつもの様子を取り繕う。\n
ぎこちないのは、ユリウスも一緒だ。"

hide yuri_m_01_3
show yuri_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0214
Julius "「……いっそ、珈琲の豆でお守りでも作ったらどうだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ブラッド避けに？」"

hide yuri_m_03_13
show yuri_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice jul_g0215
Julius "「おまえから珈琲の匂いがしていれば、あいつも近寄らんだろう。\n
むしろ、出会いがしらに豆を投げつけろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……仕返しが怖いわよ」"

hide yuri_m_02_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスはそんな他愛もないことを大真面目に言いながら、いつもどおりの手順で珈琲を淹れていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつも通りだ。\n
だからこそ逆に違いが浮き出て、彼もまた平静を装おうとしているのが分かる。"

play sound se_0468
play sound se_0779
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちんと彼が指を鳴らすと同時に、供給された魔力に反応して珈琲ミルが一人でに豆を挽きはじめる音が聞こえてきた。"

play sound se_0785
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらくすると、ふわりと珈琲のいい香りが、そう広くない作業室の中に満ちる。"


show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0216
Julius "「出来たぞ。\n
……ほら」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手渡されるカップを受け取る。\n
先ほどまでは紅茶に満たされていたカップに、今は珈琲が注がれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……私みたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶の香りのする「彼」に、昔の失恋を重ねていたはずなのにそれがもう気にならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "胸の痛みはどこかへ姿を消してしまい、代わりに訪れたのは珈琲の香りを伴う「彼」への思慕だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（違う人と、こんなふうに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "珈琲を味わう特別な時間が持てるようになるなんて、これまで考えたこともなかった。"

hide yuri_m_02_9
show yuri_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスも立ったまま、無言で珈琲を味わっている。\n
眉間の皺が、ゆるりと伸びるのが見てとれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ねえ、昨夜の三人はどうなったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "タイミングを見計らって聞いてみる。"

hide yuri_m_02_10
show yuri_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0217
Julius "「厳重注意、だな。\n
ここ数日の間、奴らが校内で飛び回っていたのは、ストームの練習のつもりだったらしい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ストームの？」"

hide yuri_m_02_8
show yuri_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice jul_g0218
Julius "「女子寮に侵入しなければいけないと聞いて、スピードで使用人達を振り切ってしまえばと考えたんだそうだ」"

hide yuri_m_03_10
show yuri_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice jul_g0219
Julius "「……双子やオレンジウサギのレースを見て閃いたというのだから、頭が痛い」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ああ、それで昨日はエリオットやディー、ダムが風紀の仕事を手伝っていたの？」"

hide yuri_m_03_4
show yuri_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0220
Julius "「いや、動機が判明したのはその後だ。\n
あれは帽子屋との取引だ」"

hide yuri_m_01_12
show yuri_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0221
Julius "「エリオット＝マーチ、トゥイードル＝ダム及びディーには処罰が溜まっている。\n
まあ、主に反省文の提出、もしくは清掃活動などの奉仕だな」"

hide yuri_m_01_13
show yuri_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0222
Julius "「それを、あの三人を捕まえるのに協力することで棒引きできないかというのが、帽子屋の申し出だったんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「なるほど、それで利害の一致、ね。\n
三人は罰を受けるかわりに、暴走覆面を捕まえるのに協力したのね」"

hide yuri_m_01_3
show yuri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice jul_g0223
Julius "「こちらにとっても、箒レースに慣れた人材の提供はありがたかったからな。\n
それであちらの提案を呑み、昨夜の捕り物になったわけだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふんふんとユリウスの説明に納得する。\n
風紀委員と帽子屋寮が手を組むのには相応しい理由だ。"

hide yuri_m_01_9
show yuri_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0224
Julius "「……影響を受けた原因と取引などしていたとは癪に障る。\n
ああいうのは、真似をしたがる愚か者も出てくるんだ」"

hide yuri_m_03_13
show yuri_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0225
Julius "「次に覆面共が騒ぎを起こしたら、と準備を進めていたんだが……。\n
まさかストームが目的だったとは思わなかった」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……男子にとっては、大事なイベントみたいだもの。\n
あなたには分からない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは、私の声に微妙そうな顔をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまでストームやブリーズに参加したことがないらしい彼には、分かりかねる思いなのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好きなひとに会いに行くために、馬鹿をするなんていうのは。"

hide yuri_m_02_11
show yuri_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0226
Julius "「……分かりたくもない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "吐き出すように言ったユリウスの声に、今度はむかっとくるよりも笑みが漏れる。\n
きっと、その声の調子が自分自身に言い聞かせるように響いたせいだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「分かりたくない」と願う言葉は、逆の意味になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はもう、分かってしまったのだ。\n
だからこそ、分からなかった頃に戻りたいとぼやく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……戻れないわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がそうであるように、彼もまた、らしくもない自分に戸惑っているようだ。"

hide yuri_m_02_8
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par23_jr_k
with stripe_l_medium

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_map_eve with Dissolve(1.2)
##endmemory
jump gakuen_julius6
