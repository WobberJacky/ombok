label gakuen_blood4:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_hat_day
with dis

play music dining_day_p_wam

scene bg_par02_ct_hat_day with Dissolve(1.2)
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "翌朝のカフェテリアは、昨夜の熱が未だ覚めやらずといった様子で、いつもよりもざわついているようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、別にメニューが変わるわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "空いている席へ適当に腰を掛け、いつもと同じ、スクランブルエッグとサラダ、そしてトーストといった朝食を呼び出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0010
Seito "「へっへー、すごいだろ？\n
俺、昨日ちゃんと、戦利品もらってこられたんだぜ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0019
Seito "「いいなー、俺も戦利品はもらってこられたんだけどな～。\n
辿り着くまでに時間がかかっちゃって、ほとんど話せなかったんだよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0020
Seito "「昨日は賑やかだったわよね～。\n
やっぱりストームはああでなきゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0136
Seito "「ふふ、新入生の子達驚いていたわね～。\n
私も去年はもう本当にびっくりしたんだけど……」"

play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あちこちから、ストームについての話題が聞こえてくる。\n
そんな中、私は黙々と朝食を口に運ぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（うう……。\n
食事に集中しなくちゃ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームといえば、ブラッドとのあれこれを思い出してしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "例の……、手紙のことも。\n
思い出さざるを得ない。"


show hat_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0003
Seito "「ねえねえ、[firstname]。\n
あなたのところには、誰が来たの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……んぐ、む」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "突如隣から話題を振られて、私は驚いて動きを止める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "片手でちょっと待って、のポーズを取りつつ、慌てて口の中にあったトーストをオレンジジュースで喉の奥へと流し込んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それから隣を見やる。\n
授業などは重なってはいないものの、カフェテリアで何度か一緒に食事をしたことのある顔見知りの子達だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人連れで、にこにこと笑いながら私を見ている。\n
おそらくは、ストームの感想についてを聞き出したいのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（こういう話題って、女子陣には格好の話のネタだものね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「誰、って……」"

hide hat_a2_3
show hat_a2_3 at left
with dis

show hat_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice sam_g0011
Seito "「あなたのところにも誰か来たでしょう？\n
ストームって、基本的には新入生の行事だもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「そうだったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドやエリオット、双子達が参加していたことから、全体行事だとばかり思っていた。"

hide hat_a2_3
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0004
Seito "「男子寮の新入生が、度胸試しと技試しに、女子寮に侵入して戦利品を取ってくる……、というのがその起源らしいわよ」"

hide hat_b1_2
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0012
Seito "「戦利品を持ってこられなかった子は、臆病者として笑われちゃうらしいわ」"

hide hat_b1_3
show hat_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0012_5
Seito "「だから、昔は新入生の中には顔を真っ赤にして、涙ぐみながら来た男の子もいたらしくね」"

hide hat_a2_2
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0005
Seito "「ふふ、可愛い……。\n
新入生じゃ、たいした魔法を使えない子も多いものね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「そうね……。\n
泣きそうになりながらも一生懸命参加するなんて、可愛いわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（そんな可愛げのある子だったら、どんなにもよかったか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜のブラッドと同じような説明をしてくれる彼女達へと、うんうん、と同意する。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（私のところにやってきたのは、全然違ったけど。\n
新入生でもなかったし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "可愛げなど皆無の傲慢で不遜な男で……。"

hide hat_a2_3
show hat_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0006
Seito "「そういえば！\n
昨夜は、ブラッド寮長も参加していたって話よね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "{size=+20}「！！！！！」{/size} "

hide hat_b1_8
show hat_b1_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice sam_g0013
Seito "「そうそう、エリオット副寮長や双子達だけじゃなくって、寮長も参加していたって噂よね……。\n
すごい面子……」"

hide hat_b1_6
show hat_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
Seito "「……？」"

hide hat_b1_5
show hat_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice sam_g0014
Seito "「って。\n
[firstname]、あなたどうしたの？」"

hide hat_a2_4
show hat_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice oda_g0007
Seito "「トーストを喉に詰まらせたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「げふげふげふっ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽんぽん、と彼女達が咳き込んで苦しむ私の背中を撫でてくれる。\n
が、その手が突如ぴたり、と止まった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……？」"

hide hat_a2_1
show hat_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
Seito "「…………」"

hide hat_b1_1
show hat_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
Seito "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人が、じっと私を見つめている。\n
何かに気付いてしまった、というような顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（ここの寮ときたら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドに限らず、誰も彼もが察しがよすぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気まずい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うっかり彼女らの口にしたブラッドの名前に反応してしまったばっかりに、何かしらあるのではと勘繰られてしまいそうな気がする。"

hide hat_a2_9
show hat_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0008
Seito "「ま、まさか……」"

hide hat_b1_9
show hat_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0015
Seito "「あなたのところに……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "来た。\n
押し込み強盗のごとき勢いで、侵入された。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あげく、昔出しそびれたラブレターなんてものを戦利品として強奪された。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（……なんて、正直に言えないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思い出すだけで顔が火照る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドも、閉じられたままの手紙を開けるなんて真似はしないだろうが……。\n
それでもあんなものが、自分以外の誰かの手元にあるなんていうのは耐え難い。"

hide hat_a2_4
show hat_a2_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0009
Seito "「そ、そんな……っっ！！？\n
と、取られたのね！？」"

hide hat_b1_4
show hat_b1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0016
Seito "「寮長に！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_11")
T "「……え、ええ。\n
本当にもう、どうしたらいいのか……」"

hide hat_a2_7
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_11")
voice oda_g0010
Seito "「ちょ、ちょっと！？\n
なに赤くなっちゃっているの……！」"

hide hat_a2_2
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_11")
voice oda_g0011
Seito "「寮長ってば、何したの～～っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「な、何って……」"

hide hat_b1_7
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_10")
voice sam_g0017
Seito "「何をされたの！？\n
白状しなさい！」"

hide hat_a2_2
show hat_a2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_10")
voice oda_g0012
Seito "「赤くなるってことは、まんざらでもないってことでいいのよね……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達はきゃっきゃっと騒ぎ立て、いきなり止まる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……？」"

hide hat_a2_6
show hat_a2_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice oda_g0013
Seito "「……いえ、ごほん、なんでもないわ。\n
とりあえずあなた、取られたものは取り返すしかないわよ！」"

hide hat_b1_3
show hat_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice sam_g0018
Seito "「そうよ！\n
取られたものは取り返さなきゃ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「う、うん。\n
まあ、そのつもりだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もとより奪われたままにしておくつもりもない。\n
当然、奪い返すつもりではあった。"

hide hat_a2_7
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0014
Seito "「私、あなたの応援をすることにしたわ！」"

hide hat_b1_2
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0019
Seito "「ええ、私もあなたのこと応援する！\n
ブリーズの夜には援護するわ！」"

menu:
    "ありがたい。":
        jump gakuen_blood4_3a
    "どうしようかな。":
        jump gakuen_blood4_3b
label gakuen_blood4_3a:
$ lovechara_blood_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（助かるわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口々に応援してくれる声が心強い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学園にも慣れてきたとはいえ、こうしたイベントを迎えるのはこれが初めて。\n
いくら情報収集したって、経験者の知識にはかなわない。"

jump gakuen_blood4_4
label gakuen_blood4_3b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……うう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "援護してくれるのも、応援してくるというのもとてもありがたい。\n
だが、事情が知れてしまうのはなるべく避けたいと思ってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（昔の失恋アイテムを取られただなんて言えない……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なるべく、そのあたりは伏せたまま手伝ってもらうことは出来るだろうか。"

jump gakuen_blood4_4
label gakuen_blood4_4:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ブリーズって、今回のストームの逆、なのよね？」"

hide hat_a2_2
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice oda_g0015
Seito "「そうよ。ブリーズはストームの逆。\n
今度は女生徒が男子寮に押しかけて、取られたものを奪い返すの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ブリーズのほうは、いつあるの？\n
ストームは前知識なしだから驚いて、参加したっていうより巻き込まれた感じだったわ」"

hide hat_b1_3
show hat_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sam_g0020
Seito "「ブリーズは、ストームの一週間後よ。\n
だから、後六日後になるわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……六日もあるのね」"

hide hat_b1_9
show hat_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice sam_g0021
Seito "「心構えには充分な期間でしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（充分すぎる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おおよそ一週間。\n
そんなに長い期間、あの手紙が自分の手元にないというのは辛い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "万が一中を見られたら……、なんて思うと、居ても立ってもいられなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……遠いわ」"

hide hat_a2_3
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice oda_g0016
Seito "「大丈夫よ、六日なんてすぐだわ！\n
それに……、ほら、同じ寮に住んでいるんだし、寮長に会う機会だってきっとあるわよ！」"

hide hat_b1_2
show hat_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice sam_g0022
Seito "「そうよそうよ、寮長に会う機会なんていくらでもあるわ！\n
……ちょっと出不精だけど、寮長」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達がどうして、ブラッドに会う機会があると言って私を慰めるのかがいまいち分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、確かにブラッドの素行チェックは必要だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしあの手紙の中を見たのならば、それなりに態度は変わるはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういった意味でも、手紙の無事を確認するという意味で、ブラッドの様子を適宜チェックするというのは大事なこと。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「そうね……、しっかりと見張ることにするわ」"

hide hat_a2_2
show hat_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice oda_g0017
Seito "「ええ、そうよね、見張りも必要かも」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「ええ。\n
信用ならないもの」"

hide hat_a2_1
show hat_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice oda_g0018
Seito "「寮長を狙っている人は多いものね……。\n
でも大丈夫よ、だって寮長のほうからあなたに……、その、手を出してきたわけなんでしょう？」"

hide hat_b1_5
show hat_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice sam_g0023
Seito "「ちょ、ちょっと……！\n
手を出したなんて、あからさまな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "{size=+20}「その通りよ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気を遣ったように顔を見合わせる二人へと、私ははっきりと言う。\n
ちょっかいを出してきたのは、ブラッドのほうからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恥ずかしい品を奪われ、それに復讐することに、何の躊躇いがあるだろう。\n
どうやらブラッドは、他にもいろいろ恨みを買っているようだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_2")
T "（私だって、被害者よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昔書いたラブレターを取られているのだ。\n
あんな恥ずかしいめにあわされた者はめったにいまい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "物自体も恥ずかしいが、色々と勘違いもされていそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が、昔書いたラブレターを後生大事にとっておくようなロマンチックな人間だと思われている……、なんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とてもとても恥ずかしい。\n
悶えたくなる。"

hide hat_a2_5
show hat_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0019
Seito "「寮長から手を出したんですって……！\n
寮長ってば寮長ってば……！！」"

hide hat_b1_4
show hat_b1_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0024
Seito "「寮長ったら寮長ったら……！！\n
奪われたのは物ではなくハートってわけね……！」"

hide hat_a2_4
show hat_a2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0020
Seito "「ハートを奪われたら……、帰れない？」"

hide hat_b1_6
show hat_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0025
Seito "「この場合は戻れない、よね。\n
もう引き返せないわ～～っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か、かなりのズレを感じるものの……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私以上に盛り上がっている二人が、きゃっきゃと楽しげに会話を弾ませているが、声は私の右から左へと抜けていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（どうやって取り返そうかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そもそも、取り返しにいって素直に返す男とも思えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……はあ」"

hide hat_a2_6
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice oda_g0021
Seito "「大丈夫よ、私達がついているわ！」"

hide hat_b1_2
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice sam_g0026
Seito "「ええ、その通り！\n
ブリーズまで、一緒に頑張りましょうね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手は寮長で、魔法使いとしても格上。\n
私一人では勝ち目のない相手。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、こうして一緒に挑んでくれる協力者がいるのなら、なんとかなるかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これから六日間。\n
頑張って作戦を立てるとしよう。"

hide hat_a2_3

hide hat_b1_3

with dis
$ hi_mes()

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg06_sk_h_day
with dis

play music school_front_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達とはカフェテリアではよく話すものの、学校の校舎内ではほとんど会うことがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "年齢的には近いが、私より在校暦が長いのだ。\n
習熟度が違うために、私と同じレベルの授業はすでに終えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのため、学校内ではほとんど会うことが出来ない。\n
だから自然と、作戦会議は放課後になるわけで……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく、ブラッドのお茶会には顔を出せそうにない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん、見張りの重要性は理解しているので、作戦がある程度まとまったら参加しようとは思っているのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（紅茶は美味しかったし、残念だけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "主催者に、問題がありすぎる。"

with dis
$ hi_mes()

scene bg06_sk_h_day
with stripe_l_medium

scene bg06_sk_h_eve with Dissolve(1)

scene bg_par15_rg_hat_eve with stripe_l_long

play music corridor_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業を終えて、寮へと戻る。\n
これまでなら、一度部屋に戻って荷物を置いて、テラスに向かっていたところだ。"

play sound se_0774

scene bg25_rr_eve with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、今は違う。\n
荷物を一度部屋に置いてから、カフェテリアへと向かう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こういった作戦会議や、雑談をするのにカフェテリアはうってつけだ。\n
飲み物と軽食ぐらいならば用意できるし……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それぞれがそれぞれの話に花を咲かせているため、少々物騒なことを話していたって、誰かの注意をひいたりするようなことはない。"


play music flower_eve_p_wam

scene bg_par02_ct_hat_eve
with dis


play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアは、すでに放課後らしく賑やかなことになっていた。\n
その中で、いつもの定位置となった席に二人の姿を見つける。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「遅れてごめんなさい」"


show hat_a2_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice oda_g0022
Seito "「お疲れ、[firstname]」"

hide hat_a2_8
show hat_a2_8 at left
with dis

show hat_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice sam_g0027
Seito "「お疲れ様。\n
まずは何か飲み物でも注文したら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そうね、ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は並んで座った二人の向かい側へと、腰を下ろす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここも食堂と同じシステムが採用されており、思い描いた飲み物を手元に呼び出すことができるようになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "飲み物、嗜好品の類ということもあり、食堂よりも失敗する確率が低めなのが嬉しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（でも、紅茶はやめておこう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしたって、ブラッドのお茶会で提供されるお茶と比べてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが用意する茶葉は、すべて一級品。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それもあるが、曖昧なイメージで呼び出した紅茶と、きちんと手順に乗っ取って淹れられた紅茶では明らかに差が出るのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（……舌が肥えたなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無難にココアを呼び出して、手元に引き寄せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……ふう」"

hide hat_a2_8
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice oda_g0023
Seito "「ふふ、疲れているみたいね。\n
……あんまり思い詰めちゃ駄目よ？」"

hide hat_b1_8
show hat_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice sam_g0028
Seito "「そうよ？\n
ブリーズの前に参っちゃったら大変だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「大丈夫よ。\n
そんなことになったら、取り戻せないもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「なんとしても、奪還しないと。\n
出来ないなら、いっそ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "奪還できないのなら、いっそ火炎魔法でも放ってやりたい。\n
部屋ごと、手紙まで燃やしてしまいたいとまで思い詰めている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「……放火魔になりそう」"

hide hat_a2_3
show hat_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice oda_g0024
Seito "「え……」"

hide hat_b1_2
show hat_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice sam_g0029
Seito "「ちょっと？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の言葉に、二人がぎょっとしたように動きを止める。\n
まさか本当にやりかねないとでも、思われてしまっているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、ぱたぱた、と片手を揺らした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「ない、ないわよ。\n
そんなこと実際にするわけがないでしょう」"

hide hat_a2_4
show hat_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_8")
voice oda_g0025
Seito "「いやいや、実際にいたのよ。\n
過去の生徒には」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「え……」"

hide hat_b1_4
show hat_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice sam_g0030
Seito "「……物を奪い返せないのにキレちゃって、黒魔法を使った人とか。\n
遊びにムキになっちゃ駄目よねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「ムキに……、っていうか、それはちょっと……」"

hide hat_a2_9
show hat_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice oda_g0026
Seito "「でしょう？\n
駄目よ？」"

hide hat_b1_9
show hat_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice sam_g0031
Seito "「下手に優秀な魔法使いが揃っている分、洒落にならないんだから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「う、うん……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大真面目に説得されてしまったので、おとなしく頷いておく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ええっと……、まあ、放火の線はないとして、やっぱり一番の難関は使用人達の包囲網の突破かしら」"

hide hat_a2_8
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice oda_g0027
Seito "「ああ、そこは心配しなくてもいいと思うわよ。\n
ブリーズは、ストームほど大掛かりな衝突はないの」"

hide hat_a2_2
show hat_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice oda_g0028
Seito "「もっと形だけの邪魔、といった感じになるわ。\n
ストームは、あれ、一部男子が使用人との戦闘に燃えちゃっているから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「へえ、そうなの？\n
結構、本気で衝突していたわよね？」"

hide hat_b1_8
show hat_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sam_g0032
Seito "「そっちが目的な子達は、ね。\n
一応ストームもブリーズも公認されている行事ではあるのよ？」"

hide hat_b1_1
show hat_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice sam_g0033
Seito "「本気で妨害されてしまっては、なかなか成立させられないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはそうだろう。\n
ストームの夜に垣間見た使用人達の実力は、生徒に負けず劣らず、といった感じがした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからこそ、生徒の中には普段相手をしてもらうことのない職員と戦えることに、ストームの意義を見出す者もいるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……喧嘩好きで、お祭り好き。\n
やんちゃな連中ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく、その筆頭が双子達だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「職員や使用人達があんなにも強いなんて、思ってもみなかったから驚いたわ」"

hide hat_a2_5
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice oda_g0029
Seito "「ふふ、私も最初の頃は驚いたわ」"

hide hat_a2_3
show hat_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice oda_g0030
Seito "「でも、世界一の魔法学校の使用人だもの。\n
職員にしたって、さすがにただものじゃないって感じよね」"

hide hat_b1_9
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice sam_g0034
Seito "「まさか使用人達まで、あれだけの使い手だとは思わないわよね」"

hide hat_b1_3
show hat_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice sam_g0035
Seito "「でも……、ほら、この学校って王族や貴族といった身分の高い方もお忍びでいらっしゃることがあるみたいだし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「ああ、そうか。\n
高貴な方もいるわけだから、警備の意味でも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（身辺警護も兼ねるというわけね）"

hide hat_a2_4
show hat_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice oda_g0031
Seito "「ええ。\n
赤薔薇寮の、ビバルディ様もそうだというお話よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「……いかにも、って感じだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意外性はまったくない。\n
むしろ、一般庶民であるほうが驚いてしまう。"

hide hat_b1_1
show hat_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0036
Seito "「ふふ。\n
隠してないわよね、ビバルディ様は」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「うん。\n
隠し切れないっていうか……」"

hide hat_a2_2
show hat_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice oda_g0032
Seito "「本当に、いかにも、だもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初の頃、寮を決めた後の手続きで会った美しい人を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女が権力者、尊い身分の人なのだといわれるのには、違和感がまったくなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……そっか。\n
そういう可能性も高いのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段クラスメイトとして話している相手が、実は……、なんてこともないとは言えないのだ。"


show m_bra3_6s onlayer master
with dis
hide hat_a2_3

hide hat_b1_3

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの夜に、至近距離で視線を交わした顔を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不良の、ならず者のボスというような粗野な印象のない、整った顔だった。\n
貴族的とすら言える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（まさか、ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（でも……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "飄々と、好きなことを好きなようにしているようなポーズ。\n
それでいて守るべきルールをしっかりと弁えているあたり……。"

hide m_bra3_6s


play music secret_front_p_wam

show hat_a2_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「……っ！」"

hide hat_a2_4
show hat_a2_4 at left
with dis

show hat_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（ブラッドも、そうなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "高貴な人、だったりするのだろうか。\n
有り得るような、有り得ないような。"

play sound se_0270
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "机の下で、軽く足をつま先でつつかれて顔をあげた。\n
目の前の二人は、何故か慌てたように視線を揺らしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おろおろ、と。\n
そんな表現が相応しい。"

play sound se_0425
play sound se_0138
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……なに？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "考え事に気をとられていた私も、やっと周囲の気配に気付いた。\n
変に静かだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ざわざわと空気が乱れてはいるものの、その乱れを押し殺そうとしたような、不自然な静けさ。"

play sound se_0161
hide hat_a2_4
show hat_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0033
Seito "「ま……っ、また後でね！」"

play sound se_0161
hide hat_b1_4
show hat_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0037
Seito "「ごめんなさい。\n
ちょっと失礼するわね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「えっ？」"

hide hat_a2_4
show hat_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice oda_g0034
Seito "「……お邪魔だと思うから」"

hide hat_b1_4
show hat_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice sam_g0038
Seito "「……後で聞かせて」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「ええっ？\n
何を？？？」"

play sound se_0312
hide hat_a2_9

hide hat_b1_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は、がたがたっと椅子を揺らして、まるで逃げるように立ち去っていってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その視線は私に、というよりも私の背後に向けられていたような……。"


show bra_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0214
Blood "「やあ、お嬢さん。\n
楽しい歓談の時間を邪魔してしまって、悪かったな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……ブラッド」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪かったな、とは言っているものの、その表情に悪びれた様子はちっとも見られない。"

play sound se_0161
hide bra_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつの間に背後にやってきていたのか、ブラッドはそのまま悠々と私の隣の椅子を引くと、腰を下ろした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、私の手元にあるココアのカップに顔をしかめる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "熱心な……、というよりも熱烈な……、というか偏執的かもしれない紅茶派からしてみたら、許されざる裏切りに見えたのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「……どうして、あなたがここに？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段はカフェテリアになど、出没しない男だ。\n
出来合いの茶を飲むよりは、自分の手で淹れることを好む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここに通っていると思われたら、それだけで不機嫌になりそうだ。\n
周囲がざわつくのも、分かる気がする。"


show bra_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0215
Blood "「お嬢さんが、私の茶会に来てくれなくなったからな。\n
……どうして顔を出してくれないんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_1")
T "「他にやることがあるの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初のうちこそ招かれてはいたが、最近では来るのが当たり前というような空気になっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただそれだけで、毎日放課後に顔を出すという約束を交わしたわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_2")
T "（そうよ、約束なんかしていないんだから。\n
……腹立たしい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これだけツンケンと対応してやっているというのに、ブラッドは悠々としている。\n
余裕があるのが悔しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が動揺しているのが、楽しいのだろうか。\n
弱みを手元に持っている強みかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（なんて嫌な男）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "被害妄想かもしれないが、目の前にいるだけで脅されているような気分になる。"

hide bra_m_01_13
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0216
Blood "「ふふ。それで私を袖にしてまで、お嬢さんは何をしていたんだ？\n
さぞや、大事な用なんだろうな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ねちねちと、どうせ白状するまで絡み続けるに違いない。\n
誤魔化しもききそうにないので、観念した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「あなたに奪われた手紙の奪還についてをね、相談をしていたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（これで満足？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、動揺している。\n
ブラッドの手元に、あの手紙があるという事実に、平常心ではいられなくなっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを認めてやったのだから、さぞかし満足するだろう、と。\n
見やったブラッドは……。"

play sound se_0771
hide bra_m_03_10
show bra_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "急転直下で、その身にまとう雰囲気を変えていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "酷く、冷たい。\n
殺気のような……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "余裕をなくしてやれば気も晴れると思ったが、それどころではない。\n
晴れるどころか、暗雲が立ち込めている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまで、ブラッド＝デュプレという男が危険なのだという話は周囲からも聞かされていた。\n
本人も認めていたし、誰も否定しない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、私はブラッドを怖いと感じたことはない。\n
それなのに、今初めて、目の前にいるブラッドのことを怖いと感じた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中がぞくぞくとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……どうして、そんな不機嫌なのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私をいじめて楽しんでいるのではないのか。\n
もう充分だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_5")
T "（参っているのよ、私は）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうにすごまれなくたって、充分すぎるほどに。"

hide bra_m_02_9
show bra_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0217
Blood "「不機嫌？\n
そう見えるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「それ以外には見えないわよ」"

hide bra_m_02_3
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice blo_g0218
Blood "「……ふむ、それなら理由は明白だ。\n
お嬢さんがそんなくだらないことで、みっともなく取り乱しているからだろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……っ！\n
喧嘩、売っているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（くだらない？\n
取り乱すのがみっともない？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（それで、不機嫌になっている、ですって？）"

hide bra_m_03_10
show bra_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice blo_g0219
Blood "「だとしたら……？\n
君は買うのか？」"

play sound se_0161 volume .4
pause 1
play sound se_0161 volume .4
pause .4
play sound se_0161 volume .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "緊迫感に耐えかねたように、周囲から小さく席を立つ音が聞こえた。\n
興味より、厄介ごとの臭いに耐えかねたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドを中心に広がるブリザードから、こそこそと逃げ出していく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（私だって、逃げたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋に押し入られて、大事なものをとられて、怒るのは私のほうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……ん？\n
あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと、何かが引っ掛かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "些細なこと。\n
言い回しや、違和感……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（なんだか……、お互いに食い違っているような……）"

hide bra_m_03_11
show bra_m_03_19 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目を逸らしたら、その場で負けが決まってしまいそうで逸らせない。"

hide bra_m_03_19
show bra_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっとのびてきた手が、顎先にかかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_6")
T "「……っ！」"


play music stream_eve_p_wam

show m_bra4_1 onlayer master
with dis
hide bra_m_02_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "反射的に顔を振って、払いのけようとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを強引に力ずくで押さえ込まれ……、そのまま覆いかぶさるようにして口付けられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「な……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……っ{size=+20}！！？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_9")
T "{size=+20}（ここをどこだと思っているのよ！？）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、どこならいいというわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、ここはカフェテリア。\n
衆人環視のど真ん中だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこでも悪いが、こここそ最悪の場所だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆あえて見ないふりをしてくれている。\n
だが、もちろんそれはあくまで「見ないふり」であり、実際に見ていないわけではない。"

hide m_bra4_1
show m_bra4_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
Blood "「……つ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抗議の意味もこめて、噛みついてやる。\n
強引に合わせられた唇の向こうから、小さく呻く声が聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それをいい気味と思うより先に、仕返しのようにキスをされて息があがる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_9")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……っん」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice blo_g0220
Blood "「……は」"

hide m_bra4_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唇をとかれても、すぐには息が整わず、言ってやりたい罵詈雑言の類が頭の中でぐるぐると回る。\n
それが悔しくて、ただただ睨みつけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもは涼しげな色をしたブラッドの目も、剣呑な熱を孕んでいるように見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_5")
T "（……こんなの、違うわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアでは、仲のいい学生カップルを見掛けることもあった。\n
若い恋人達、キスをかわす場面も、そう珍しくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ブラッドとのそれは、そんな場面とはまったく違った。"


show bra_m_02_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「……[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼ぶ。\n
その声にも、親愛の情など聞き取れない。"

hide bra_m_02_16
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0221
Blood "「……おいで。\n
乱暴者のお嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "濡れた唇が、笑みに歪んで忌々しそうに、それでいて不思議と甘ったるく毒づく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "明らかに、私に対する挑発、もしくは侮辱だ。\n
そう捉えた。"

play sound se_0160
hide bra_m_03_10

play sound se_0774
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが席を立つ。\n
当然、私は従わない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はそんな私に飽き飽きし、無言でかつかつと早足に歩き去ろうとする……。\n
しかし、その背中はぴたりと止まった。"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……？」"

play sound se_0584
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "訝しげに見る中、くるりと踵を返してブラッドが戻ってきた。"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……何よ」"


show bra_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice blo_g0222
Blood "「君が見世物になりたいというのならば、置いていくが。\n
……来なさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ」"

play sound se_0492
pause .5
play sound se_0051
play sound se_0161
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "腕をつかまれ、ぐいと引き上げて立ち上がらされる。\n
周囲に視線をやれば、ぽかんとした顔の何人かの生徒と目が合った。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「……！！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆、慌てて目を伏せる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（う……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪目立ちもいいところだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キスをするカップルも、揉めごとを起こす生徒も、珍しくない。\n
だが、出不精の寮長が女生徒と揉めているというのは珍しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（うう……。\n
回避しなくては）"

menu:
    "そのままブラッドと一緒に出る。":
        jump gakuen_blood4_5a
    "ブラッドの手を振りほどく。":
        jump gakuen_blood4_5b
label gakuen_blood4_5a:
$ lovechara_blood_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（ここは、おとなしくブラッドと一緒に動いておいたほうがよさそうね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒達は、ブラッドがいる間はまだおとなしくしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、彼が立ち去ってしまえば、一気にハチの巣を突いたような騒ぎになりそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私など、まだまだ新入生の一人に過ぎない。\n
容赦なく質問攻めにされる姿が、簡単に想像できてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（一応、気を遣ってくれてはいるのかしら）"

hide bra_m_01_5
show bra_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_16")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……いやいや。\n
そもそも、この男のせいだし）"

hide bra_m_01_13

with dis
$ hi_mes()

scene bg25_rr_eve with stripe_l_long

play music starlit_sky_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の腕を引き、ブラッドはそのままカフェテリアを出ると、女子寮と共同空間の境界まで送り届けてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからといって、感謝もないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "移動中、彼も私も口を開こうとはしない。\n
終始無言だ。"


show bra_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0223
Blood "「……いい夜を、お嬢さん」"

play sound se_0774
hide bra_m_01_12

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……お別れ？\n
なんだ、本当に送ってくれただけなのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後、去り際に一言そんな挨拶だけを、そっけなく残していった。\n
その去り行く背中を見送りながら、ぼんやりと思う。"

jump gakuen_blood4_6
label gakuen_blood4_5b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……っ！」"

play sound se_0251
play sound se_0373
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの手を振り払って、距離をとった。\n
こうして私が悪目立ちしてしまっている原因はブラッドだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "諸悪の根源。\n
その彼と一緒にこの場から去ってしまえば、結局、私も同類とみなされてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_2")
T "（……私はただの一般生徒。\n
悪目立ちなんてごめんよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すでに、手遅れの感もあるが。"


show bra_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0224
Blood "「……はあ。強情な。\n
もういい、勝手にしなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「そうさせてもらうわ」"

hide bra_m_03_13

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呆れたような嘆息交じりのブラッドの声にそう言って、背を向ける。"

play sound se_0584


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一人この場に残されれば、周囲から質問攻めにされてしまうだろうが……、私が先にこの場から立ち去ってしまえば問題ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不機嫌なブラッド相手にぎゃあぎゃあ姦しく騒ぐ根性のある生徒も、なかなかいないだろう。"


scene bg25_rr_eve with stripe_l_long

play music starlit_sky_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして歩きながら、思う。"

jump gakuen_blood4_6
label gakuen_blood4_6:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_11")
T "（……私、キスされたことを忘れていた）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、忘れていたのとは違う。\n
キスのことを、問題だと捉えていなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今の話ではなく。\n
ストームの夜のこと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "奪われた手紙のことだけに気をとられて、ブラッドにキスされたことについては、うやむやのうちになんとなく流してしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（許して、いたの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キスされたことを、触れられたことを。\n
それらを問題視しないぐらいに、私はブラッドのことを受け入れてしまっているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……いやいや）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の気持ちが、分からない。\n
下手に分かっては、ドツボにはまりそうでもある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「恋愛沙汰なんて、御免だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽつり、誰も聞くものがいないと分かっていて呟く。\n
酷く、言い訳じみている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと持ち上げた指先で触れた唇は、じんわりと未だ熱を残しているかのようだった。"


with dis
$ hi_mes()

scene bg25_rr_eve
with stripe_l_medium

scene bg_par15_rg_hat_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_long
##endmemory
jump gakuen_blood5
