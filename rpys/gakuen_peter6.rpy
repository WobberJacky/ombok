label gakuen_peter6:
scene bg06_sk_h_nig
with dis
$ clockanim()

jump gakuen_common_breeze
label gakuen_peter6_2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ペーターの部屋は三階だから、まずは階段を探さなくちゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とんとんと額を指先で叩いて、記憶を辿る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子寮と女子寮では造りも違う。\n
迷わないよう、注意しなくては。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズへの参加を決めてから、私もちゃんと情報収集してきたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアで会う知人などに教えてもらい、男子寮の間取りについてもしっかり把握してある。"

play sound se_0774
with dis
$ hi_mes()
pause 1


$ time_effect()##PLEASE MANUALLY ADJUST ME
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "途中何度か迷いそうになりつつも、どうにか無事にペーターの部屋へ辿り着くことが出来た。"

play sound se_0217
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0190
Peter "「！！！！！！」"

play sound se_0293 volume .7
play sound se_0394 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がノックをすると同時に、中から激しい物音がした。\n
それから、すぐにドアが開けられる。"

play sound se_0285

show per_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0191
Peter "「お、お待ちしてました、[firstname]！！\n
どうぞ、入ってください！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ありがとう。\n
……どうしたの、涙目よ？」"

hide per_m_03_11
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pet_g0192
Peter "「ちょ、ちょっとベッドに躓きまして……。\n
だ、大丈夫ですよ、僕は大丈夫です」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……そう？\n
ならいいんだけど」"

hide per_m_02_13
show per_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice pet_g0193
Peter "「……来てくれて、嬉しいです。\n
ちょっと……、感動したのもあります」"

hide per_m_02_12
##[chara1 PAY ATTENTION="false"]

play music moon_night2_a_ali

scene bg23_rd_nig with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は招かれるまま、ペーターの自室へと足を踏み入れる。\n
室内は、なんとも彼らしく、綺麗で清潔だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あるべきものが、あるべき場所にきちんとすべて収まっている。\n
本棚も綺麗で、その縁を指先でなぞったところで、埃一つ付かなさそう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、物も少ない。\n
雑多なものがないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "必要最低限なもの、必要なものだけが整頓されて並べてある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……生活感がないわね。\n
モデルルームみたいだわ」"

##[rchara1 PAY ATTENTION="false"]
show per_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice pet_g0194
Peter "「そんな誰が入ったかも分からないような部屋と一緒にしないでくださいよっ。\n
この部屋に入ったことがあるのは、僕とあなただけです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……褒めたつもりだったんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "潔癖症の気のあるペーターにとっては、モデルルームというのも褒め言葉ではなかったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「それにしても、よく片付いた部屋だこと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうしてきょろきょろと見回した視線は、最終的に場違いなリボンに落ち着いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "必要なものしか置かれていないペーターの部屋の中で、違和感を放っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のリボンだ。\n
机の上、丁寧に畳まれて置かれている。"

play sound se_0774
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "机の傍らまで歩み寄る。\n
違和感はかなりのものなのに、そのリボンは部屋の主のように堂々と鎮座していた。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "持って帰るのが悪いような気分になりつつも、手に取った。"

hide per_m_01_4
show per_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやっている間も、ペーターは落ち着かなげにそわそわとしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ペーター？」"

hide per_m_01_13
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0195
Peter "「はい、なんでしょう！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……緊張しているの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼んだ私に対する返事は、裏返り気味だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「……座っていい？」"

hide per_m_02_3
show per_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice pet_g0196
Peter "「は、はい！\n
どうぞ！」"

play sound se_0251 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "椅子を勧められる前に、ぽすりとベッドに腰掛けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……あなたも座ってよ」"

play sound se_0155 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "隣を軽く叩いて、ペーターを呼ぶ。"

hide per_m_03_3
show per_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おずおずと近づいてくるペーターは、叱られて職員室に呼ばれた子供みたいだ。\n
その長い耳も、へにゃりと萎れている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何をそうも、怯む必要があるのだろうか。\n
私は、ペーターが隣に座るのを待ってから口を開いた。"
if lovechara_peter_points == 8:
    jump gakuen_peter6_4a
label gakuen_peter6_3:
menu:
    "大事な話があるの。":
        jump gakuen_peter6_4a
    "軽く聞いてほしいんだけど……。":
        jump gakuen_peter6_4b
label gakuen_peter6_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……あのね、ペーター。\n
話さないといけないことがあるの」"

hide per_m_02_6
show per_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Peter "{size=+20}「！！！！！」{/size} "

play sound se_0052

play music peter_t_ali
show m_per_goodend1 onlayer master
with dis
hide per_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう切り出した途端に、ペーターはまるでバネ仕掛けのおもちゃのように跳ね上がった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま床に膝をつき、私にすがりついてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "{size=+20}「！！！！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（……ええ！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターの奇行には慣れているつもりだったが、さすがに面食らう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0197
Peter "「[firstname]、お願いですから僕を捨てるなんて言わないでください……！\n
悪いところがあるなら直しますから！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「は？\n
何言って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice pet_g0198
Peter "「あなたが僕のことを嫌いでもいいんです！！\n
いえ、よくはないんですけど！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice pet_g0199
Peter "「でも、それは我慢しますから！！\n
だから僕と縁を切りたいなんて言わないでください……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……{size=+20}はあ？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間の抜けた声が出た。\n
ぽかんとする私とは対照的に、ペーターは必死だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その赤い双眸を涙で潤ませて、私の膝にひしっとしがみついている。\n
何がどうして、彼の中で私に捨てられるなんて結論が出ているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際のところ、私はその逆を今夜告げるつもりだったのだ。\n
そして、この前と同様に。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「ちょっと、ペーター落ち着いて……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice pet_g0200
Peter "「嫌ですっっ！\n
あなたに縁を切られてしまうなんて、僕には耐えられません！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice pet_g0201
Peter "「嫌いでもいいんです！！！\n
傍にいさせてください、あなたにとって路傍の石のような存在でも構いません！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「いや、あのね？\n
ペーター……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice pet_g0202
Peter "{size=+20}「好きですっ、好きなんです！\n
愛しているんです！！！！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーター、大絶叫。\n
これは間違いなく、周囲にも聞こえただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……頭痛がしてきた。\n
これではもはや、私の告白どころではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とりあえず早急にこの暴走男をなだめ、誤解を解かなくてはいけない。"

hide m_per_goodend1
show m_per_goodend2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌です嫌ですと繰り返しながら、私の膝に顔をうずめてぐりぐりと頭を振って駄々をこねているペーターの、その銀髪の間からのぞく白い耳をむぎゅっと握った。"

play sound se_0492
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0203
Peter "「い……っ！！？」"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「この長いお耳は何のためについているのかしら。\n
……少しは私の話を聞いてくれる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice pet_g0204
Peter "「い、嫌ですっ！\n
聞きたくありません！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……{size=+20}聞きなさい{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice pet_g0205
Peter "「嫌です～～～っ！！\n
あなたの縁切り宣言なんて聞くぐらいなら、この耳を切り落としたほうが……\n
っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「いいから聞きなさいよっ！\n
{size=+20}私、好きって言ったわよね？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌い、とは真逆の言葉だ。"

hide m_per_goodend2
show m_per_goodend3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0206
Peter "「……え？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターの動きが止まった。\n
きょとんと顔をあげた彼は、その言葉の内容が理解できなかったとでも言うように、訝しげな顔をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……言ったでしょう？\n
聞こえていなかったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前に、確かに言った。\n
ペーターだって驚いていたではないか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0207
Peter "「え、聞き間違いかと……。\n
いつものように夢か幻聴かと思ったんです、けど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……いつも？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつも、夢だか幻聴だかを聞いているというのか。\n
というか、{size=+20}その自覚があったのか。{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……やっぱり、ペーターの気持ちが何であれ、変質者の一歩手前なことに違いはないわね）"

hide m_per_goodend3
show m_per_goodend4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pet_g0208
Peter "「だ、だって、ストームの夜に、抱きしめさせてくれたじゃないですか！\n
それにリボンだって預けてくれました！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……それがどうして絶交宣言に繋がるのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（普通、好意だと思わない？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ペーターはちっとも普通ではない男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0209
Peter "「次の日に呼び出されて……。\n
あなたは様子がおかしかったし、それから僕を避けていたでしょう……っっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0210
Peter "「だから、ストームの夜のことはあなたの最後の優しさで……っ。\n
あなたは、僕のことを切り捨てようとしているんじゃないかって……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「それは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "避けていたのは、気持ちの整理と、ブリーズに備えてのことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズについての打ち合わせを友人らとしていたから。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は新入生で、初めてのブリーズということで、いろいろ前もって準備したり勉強しなくてはいけないこともあったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（成功させて、ペーターとの関係も見直したかったから……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（……急ぎすぎたのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの夜から、ペーターへの意識が変わった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "付き合いは長く、いきなり盛り上がるようなものではなかったが、気持ちを自覚する面もあった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それから一週間程度で、関係を切り替えようだなんていうのは無謀だったのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結果として、ペーターにも中途半端な形で伝わってしまっている。\n
大体、「好き」と言っても幻聴扱いされては話が進むはずがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ごめんね、ペーター。\n
私、あなたがあんまり賢くないってこと忘れていたわ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice pet_g0211
Peter "「……っ、何を言うんですか。\n
僕は賢いウサ……っ」"

play sound se_0424
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後まで言う前に、その頭上に軽くチョップを落とす。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「いいえ、あなたは賢くなんかないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（それが私の幼馴染、ペーター＝ホワイトだもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "勉強に関しては優秀で、シンフォニアに進学してしまうような天才でも、ペーターは人の心には疎い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私への執着だって、それがどういう種類のものなのか、自分でも分かっていないに違いないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなペーターに、私の気持ちが分かるわけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一週間で気付かせようなんていうのが無茶だったのだ。"


play music flower_eve_p_wam
hide m_per_goodend4
show m_per_goodend5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……でも、私も賢くないから、お似合いよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっとチョップを落としたその手を、銀髪に差し込んでやさしく撫でてやる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「……[firstname]？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "泣き出しそうに潤んでいた赤い瞳が、気持ちよさそうに細くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0212
Peter "「あなたは……、賢いですよ、[firstname]？\n
とっても……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうしているときのペーターは、ウサギそのもの。\n
おとなしく、いい子だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0213
Peter "「僕を捨てないでください……、[firstname]、僕はあなたが好きなんです。\n
あなただけが好きで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「ええ、知っているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "繰り返し繰り返し。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は自分の好意を私に押し付けるばかり。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私にも好きになってほしいと言うが、おまけのようだ。\n
むしろ嫌いでもいいなんて、言ってしまえるほど。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「でも、先は長いんだし、変わる可能性もあるわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0214
Peter "「……僕の気持ちが？\n
子供の頃からずっとなんですよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「まあね。\n
でも、これから関係が変われば、気持ちも変わるかも」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「悪い意味じゃなくて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice pet_g0215
Peter "「悪いですよ！\n
そんなことを言わないでください！心変わりするだなんて！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……片思いより、両思いのほうがいいと思うんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ずっと続かない可能性を秘めている。\n
ペーターは、終わる可能性を巧みに避けているようにも思えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……そうね。\n
変わらないほうがいいかもしれない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、変わるものは変わる。\n
少なくとも、シンフォニアで過ごすうち、私のペーターへの気持ちは変わった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、焦る必要はない。\n
私達がシンフォニアを卒業するまでには、まだまだ時間はある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、別にシンフォニアにいる間に限定しなくてもいい。\n
私達は幼馴染で……、これからも、先は長い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その形を、整えたいだけ。\n
だからいくらだって、時間をかけられる。"


scene black with dis
hide m_per_goodend5
show m_per_goodend6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0216
Peter "「好きです、[firstname]、あなたが大好きなんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「ええ、私も好きよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（変わっても……、変わらなくても）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは、私の『好き』という言葉に、幼馴染以上の好意を見出さないだろう。\n
もしくは、またもや幻聴と決め付けているかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これから先、繰り返されるであろう、やりとり。\n
いつか変わるのか、それとも、いつまでも変わらないのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今はまだ知れず。"

hide m_per_goodend6 with Dissolve(5)
hide frame_par_togaki
hide ali_m_06_16
with Dissolve(5)
scene black with Dissolve(5)
stop music
##endmemory
jump gakuen_b
label gakuen_peter6_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「今更なんで、軽く聞いてほしいんだけど……。\n
ペーター、私、あなたに言っておきたいことがあるの」"


show per_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0217
Peter "「は……っ、はい！どうぞ！\n
覚悟は決めています……！！」"

hide per_m_01_6
show per_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0218
Peter "「……何を言われても、離れない覚悟ですけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……{size=+20}結局は、ストーカーなのね{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、隣に座ったペーターは体をガチガチに強張らせ、神妙な顔をしている。\n
死刑宣告前、といった感じだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴるぴると頭上のウサギ耳が小刻みに震えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……ウサギ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "軽く聞いてほしいと言って、この有様。\n
大事な話があるなどとプレッシャーをかけていたら、パニックになっていただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「あのね……。\n
本当に、今更すぎて言いにくいんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "軽く、とは言ったものの。\n
改めて口に出そうとすると、さらりとはいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もとより幼馴染、気心の知れた仲。\n
更にペーターは私のことが大好きという前提がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どう考えても、こっぴどくは振られない。\n
緊張せずにいられる条件が揃っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、実際に自分の気持ちを口にしようとすると、緊張もすれば躊躇いもしてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……言わなきゃ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私から切り出さなければ、私達の関係はずっとそのままだ。\n
それはそれでと思う、逃げ腰を叱咤して……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「ペーター、私……。\n
この前も言ったんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「……あなたのことが、好きよ」"

hide per_m_01_13
show per_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_19")
voice pet_g0219
Peter "「はいっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「…………」"

hide per_m_02_6
show per_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「…………」"

hide per_m_01_8
show per_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_16")
Peter "「…………」"


play music gag1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……え？」"

hide per_m_01_13
show per_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
Peter "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……今の、「はいっ！」が「好きよ」に対する反応？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さらっと流されてしまった。"

hide per_m_02_10
show per_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0220
Peter "「え？\n
お話ってそれだけですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！！\n
それだけって、何よ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……あんたこそ、反応はそれだけなの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "受け入れるにしろ拒むにしろ、「はいっ！」で終わるとは想定外だ。"

hide per_m_03_3
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0221
Peter "「だって僕、金輪際顔を見せるなとか、ストーカーをやめろとか……。\n
改まって言うから、そういった無理難題をふっかけられるとばかり……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

##[rcg time="5000"PAY ATTENTION="true"]
show m_per6_1 onlayer master
with dis
hide per_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「……{size=+20}ストーカーをやめろっていうのは、無理難題じゃないわよね？{/size}」"

play sound se_0492
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手をのばして、ウサギ耳を二本まとめて引っ掴む。"

play sound se_0054
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0222
Peter "「い、いた……っ！！？\n
ちょ、痛いですよ、耳は敏感なんですからやめてください……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悲鳴をあげるペーターは無視して、ぎゅうぎゅうと引っ張ってやった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……うん？\n
なんだか、告白っぽくないな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前の、ラブレターさえ渡せなかったときとは、大分違う。\n
相手が違えば、ここまで違うものなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「この耳は飾りでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声さえ掛けにくかった昔と、相手の耳を引っ張り悲鳴をあげさせている今。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……告白っぽくない）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice pet_g0223
Peter "「本物ですよ！？\n
いたた……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……それじゃ、どうなのよ」"


play music quiet_a_wam
hide m_per6_1
show m_per6_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice pet_g0224
Peter "「何がですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "告白を、ここまで華麗にスルーされるのも、私ぐらいだと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「耳が飾りじゃないのなら、聞こえていたんでしょう？\n
あなたのことを、好きだって言ったんだけれど、私は」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice pet_g0225
Peter "「ええ、聞いていましたよ？\n
でも、それがどうかしましたか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「ど、どうかしたって……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんでもないことのように聞かれてしまって、戸惑う。\n
確かにどうかしたかといわれれば、どうかした……、のか？ "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは前々から私に対して好きだの愛しているだの言いまくっていた。\n
それに対して、私は好きと返したのだから、すなわち両思いになるわけで……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは彼にとって、驚いたり、喜んだりするところではないのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……最初から、見抜かれていた？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昔から天才児と名高いペーターだ。\n
私よりもずっと幼い頃に、シンフォニアへの入学を許可されていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかして最初から私の気持ちなんて分かっていて、それでああして振る舞っていたというのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（人の気持ちが分かっていなかったのは、ペーターでなく私のほうなの……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（だとすれば……。\n
からかわれていた……っていうのはないにしても……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice pet_g0226
Peter "「そりゃあ離れていた期間も長いですが……、僕はあなたの幼馴染ですよ？\n
あなたのことぐらい、分かります」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴんっとペーターは自慢げにその両耳を立てる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（分かっていたっていうの？\n
私の変化を？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（ああ、恥ずかしくなってきた……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「……いつから分かっていたの？\n
私が、あなたのこと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
voice pet_g0227
Peter "「そうですね、確信を持ったのは、ストームの夜……。\n
あなた、この前のストームの夜から優しかったじゃないですか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
voice pet_g0228
Peter "「抱きしめていいか、って聞いたら抱きしめさせてくれましたし……。\n
僕のことを受け入れてくれたふうでしたから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……お見通しだったってわけ）"

hide m_per6_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耐え切れず、ペーターの耳を引っ張っていた手をぱっと離した。\n
解放されるやいなや、器用にその二つの耳がぴこぴこと揺れる。"


show per_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0229
Peter "「だから、僕はちゃあんと分かっていましたよ！\n
なんたって、僕は賢いウサギですから！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「そ、そう……。\n
分かって……いたんだ」"

hide per_m_02_1
show per_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice pet_g0230
Peter "「ええ、はっきり分かりますとも！\n
{size=+20}あなたは、正気を失っているんですよ、[firstname]！{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（そうよね、ペーターでも分かるわよね。\n
私がペーターのことを……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……ん？）"


play music peter_t_ali
hide per_m_02_9
show per_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice pet_g0231
Peter "「僕にははっきり分かります！」"

hide per_m_03_8
show per_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice pet_g0231_5
Peter "{size=+20}「あなたは、どうかしちゃっているんです、[firstname]！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自慢げに耳をぴんっとさせ、胸を張り、ペーターは言い切る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……何？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（どうか……、しちゃっている？）"

hide per_m_03_7
show per_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice pet_g0232
Peter "「分かります！慣れない場所に疲れているのでしょう！\n
繊細なあなたは、パニックに陥っているのです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「パニック……」"

hide per_m_02_11
show per_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice pet_g0233
Peter "「ええ！パニックでおかしくなっているんですよ！\n
あなたは今、どうかしています！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……間違ってはいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごもっともだ、私はどうかしている。\n
パニックに陥っているのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「そうね。\n
そうかも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

play sound se_0373

show m_per6_3 onlayer master
with dis
hide per_m_01_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どん、と。\n
ペーターを突き倒す。"

play sound se_0063
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0234
Peter "「っ！？\n
わっ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完全に油断していたペーターは私の力にも抵抗できず、ばたんっとベッドに背中から沈む。"

play sound se_0327 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その膝の上に乗り上げて押さえ込んだ。\n
小さい頃にやったプロレスごっこを思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "綺麗好きなペーターはあまりやりたがらなかったが、私は嫌いじゃなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……あなたは、私が普通じゃない状態だって言うのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pet_g0235
Peter "「え……っ。\n
ええ、そう思いますが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは、その赤色の双眸をいっぱいに瞠って私を見上げている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「そうね……。\n
その通りだと、私も思う」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（告白すれば「はいっ！」としか反応しないし……、頭がどうかしていると決め付けるようなウサギ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ペーターだ。\n
それこそ、私のよく知る、ペーター＝ホワイト。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずれていて、自分のほうこそ余程おかしいくせに、堂々とこんなことをのたまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（そんなウサギが、好きだなんて）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……私は、おかしくなっているんだわ」"


play music flower_eve_p_wam
hide m_per6_3
show m_per6_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おかしくなっている私は屈みこんで……、ペーターの唇へと触れるだけのキスを落とした。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「{size=+20}！！！！！！{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「好き、よ。\n
おかしくなっちゃうような意味で、私はあなたが好きなの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幼馴染としての好意ではない。\n
触れたいし、愛しいとも思う。"

hide m_per6_4
show m_per6_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「……～～～～っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0236
Peter "「……っざ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ざ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく目を大きく瞠り、口をパクパクとさせていたペーターが、小さく呻くように口を開いた。\n
ざ、と聞き取れたが、なんだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（ろくなことじゃない気がする……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その音を、復唱して聞き返す。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0237
Peter "「ざ、雑菌が……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "{size=+20}黙れ、潔癖症{/size}。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "罵声が口を突いて出そうになった。\n
すんでで留まる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……告白っぽくなさすぎる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳を引っ張り、悲鳴をあげさせ。\n
その上、怒鳴りつけたら、もう告白シーンとはいえなくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（いや……、今でも充分手遅れっぽい……けど）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice pet_g0238
Peter "「雑菌が、移るのに……。\n
どうして、どうして嫌じゃないんでしょう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しんみりと言われ、急に雰囲気がそれらしくなってきた。"

menu:
    "あなたが私を好きだから。":
        jump gakuen_peter6_5a
    "潔癖症が治りつつあるから。":
        jump gakuen_peter6_5b
label gakuen_peter6_5a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……そりゃあ、あんたが私のこと好きだからじゃないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉だけとると、私が非常に自信家であるように響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、あれだけまとわりつかれていて、好かれていないと思うほうがおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何にしろ好意を持たれているのは確かだが、ペーター自身、気持ちを掴みかねているようだ。"

jump gakuen_peter6_6
label gakuen_peter6_5b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「潔癖症が、治りつつあるんじゃないの？\n
ほら、この前も抱き合ったじゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0239
Peter "「それは、あなただからですっ！！\n
あなた以外に触られるのは嫌です！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……ここまで言われて、どうして両思いじゃないのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれだけまとわりつかれていて、好かれていないと思うほうがおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何にしろ好意を持たれているは確かだが、ペーター自身、気持ちを掴みかねているようだ。"

jump gakuen_peter6_6
label gakuen_peter6_6:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（好きは好き、なんだから……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "畳みかけるようにして誘導してしまう……というのは、ずるいだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「私に触られるのは、嫌じゃないのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pet_g0240
Peter "「嫌じゃありませんっ！\n
他の人間だったら、どんな接触も御免ですけど！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……今みたいなのも？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pet_g0241
Peter "「ええ、あなたなら……。\n
しかし、他の輩と考えれば……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pet_g0242
Peter "「マウストゥマウスの接触なんて……、ああおぞましい！！\n
考えるだけで相手を射殺したくなりま\n
す！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pet_g0243
Peter "「でも、あなたとするマウストゥマウスの接触は嫌じゃありませんよ、[firstname]。\n
吐きそうになったりもしません」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キスの感想が、「吐きそうにならなかった」？\n
なんと、ロマンチックなことだろう……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「ペーター、キスっていいなさいよ。\n
マウストゥマウスの接触……、なんてムードがなさすぎるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice pet_g0244
Peter "「……キス。\n
なるほど、そちらのほうがあなた好みなんですね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「わ、私の好みとか、そういう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice pet_g0245
Peter "「僕は、あなたが喜んでくれるなら、なんでもいいです。\n
[firstname]、今度は僕からしてみてもいいですか？」"

play sound se_0327
hide m_per6_5
show m_per6_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりとペーターの右腕が腰裏に回って、私の背中を支えながら身を起こした。\n
ベッドに座ったペーターの膝の上に乗せられるような形になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が馬乗りになるよりも、顔と顔の距離が近い。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0246
Peter "「……ねえ、いいですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "白い手袋に包まれた手のひらが、ねだる言葉を後押しするように私の頬に触れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薄い布越しに感じる体温。\n
慣れ親しんだそれは、私とペーターの今までの関係の象徴のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「…………」"

hide m_per6_6
show m_per6_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、問いかけに答えぬままその手をとった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0247
Peter "「[firstname]？嫌ですか？\n
僕から触れられるのは、好きじゃありませんか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……いいえ？\n
好きよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "拒まれないからか、緊張も抜けて、簡単に言えるようになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ただ、これは邪魔かな、と思って」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pet_g0248
Peter "「これ、ですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_16")
T "「私の『好き』に、これはいらないわ。\n
……ペーターはどう思う？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（あなたは？\n
嫌？）"

hide m_per6_7
show m_per6_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手袋の手首の部分に指を引っ掛けて、くいと下ろしながら問う。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0249
Peter "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今まで体の一部のように、当然としてあった手袋。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを剥ぎ落とされるというのは、ペーターにとってはさぞかし心許ない思いがすることだろう。"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、彼は不安そうに一度吐息をつめたものの、抵抗するようなことはなかった。\n
くるくるとめくって、白い手袋を取り除く。"

hide m_per6_8
show m_per6_9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その下から現れた彼の素手は、手袋をしているときとそう変わらないほどに、白かった。\n
生身の手が、改めて私の頬へと触れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0250
Peter "「……あ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "指先が触れた瞬間、まるで何か熱いものにでも触れたように、はっと一度手を引いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の反応に、ペーター自身驚いているようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（火傷したみたいな反応ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先刻の、薄い反応とは雲泥の差。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……実際、すごく熱いのかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のほうも、頬に熱が昇っている自覚はある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「……ねえ、嫌？\n
苦手？」"

hide m_per6_9
show m_per6_10 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_8")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返事の代わりに、おずおずと触れてくる手。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0251
Peter "「……あなたの雑菌ならば、移されても平気です。\n
触れるのも、触れられるのも、あなたなら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うっとりとした調子で囁いて、ペーターの指先が頬から滑って顎先へと降りる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（わ）"

hide m_per6_10
show m_per6_11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くっと角度をつけて持ち上げられて、唇が触れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（ペーターが……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分から、直に。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「[firstname]……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……ん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "触れ合うことで、何かが変わる。\n
いや、変わらないものが出来上がっていくと、前向きに考えるべきだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「…………」"

hide m_per6_11
show m_per6_12 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "利き手を彼の首裏に回して体を支えながら、もう片手はペーターの空いている手と絡めあう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "指の一本一本を絡める。\n
いわゆる恋人繋ぎというやつだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手を繋いだことぐらいこれまでだっていくらでもあるが、こんなふうに直に触れ合ったことはない。\n
キス以上に、胸が高鳴る。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っん」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pet_g0252
Peter "「は……っ。\n
ああ、[firstname]……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_3")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キスが深くなる。\n
吐息が混じりあって、なんだか涙が滲んでくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0253
Peter "「……苦しいですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_3")
T "「……いいえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだろう。\n
好意の形も未だはっきりとしないのに、この人でなくてはと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0254
Peter "「僕は……、苦しいです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「え……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pet_g0255
Peter "「大好きです。\n
あなたのことが……、大好きで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pet_g0256
Peter "「……好きすぎて、苦しい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「……私も。\n
好きよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（でも、苦しくはないの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "形の違うもの。\n
それでも、重なることは出来るから。"

with dis
$ hi_mes()
hide m_per6_12


scene bg23_rd_nig with Dissolve(.8)

scene bg_par15_rg_ros_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_peter_end
