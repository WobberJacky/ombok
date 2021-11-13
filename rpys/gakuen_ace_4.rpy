label gakuen_ace4:
scene bg_map_day
with dis
$ clockanim()

jump gakuen_storm_pet_ace
label gakuen_ace4_2a:
$ lovechara_ace_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（そういうことなら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その証拠品を持ち帰ることが出来なければ、イベント失敗としてゲームの敗者になってしまうのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと見やれば、他にも同じような光景が。"

play sound se_0229
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "新入生だと思われる男の子達が、ぎこちなくも懸命に廊下を歩く女生徒達へと声を掛けている。"

jump gakuen_ace4_3
label gakuen_ace4_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……迷惑な）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その証拠品を持ち帰ることが出来なければ、イベント失敗としてゲームの敗者になってしまうのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと見やれば、他にも同じような光景が。"

play sound se_0229
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "新入生だと思われる男の子達が、ぎこちなくも懸命に廊下を歩く女生徒達へと声を掛けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（明日も早いのに……、こんな夜中にイベントだなんて）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷惑きわまりないが、かといって彼らに罪はない。"

jump gakuen_ace4_3
label gakuen_ace4_3:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「いいわよ。\n
あまり、たいしたものは渡せないけど」"


show boy_b1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice chi_g0017
Seito "「いいんですか……！？\n
ありがとうございます！」"

hide boy_b1_2
show boy_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice chi_g0018
Seito "「これで失敗してたら、きっと他の奴に馬鹿にされちゃうと思ってて……。\n
助かりました！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "考える間を挟んだ後、私は彼の願いを聞き入れることにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱあ、と素直に喜ぶ彼は、やはり悪い人には見えない。\n
同じ新入生として、手助けくらいしてやってもいいだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「いかにも女の子、って感じのものがいいのかしら？」"

hide boy_b1_3
show boy_b1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice chi_g0019
Seito "「何でもいいんですけど……。\n
そうですね、誤魔化しがきかないようなやつだと、疑われる心配がないので有難いです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「女の子らしいもの……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本や、マジックアイテムといったものならばすぐにイメージすることが出来る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、女の子らしいもので、彼に渡してしまっても後で困らないものと考えると、なかなかイメージがわかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "戦利品や証拠品として提示出来るような、女の子らしいもの……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ああ、リボンとかならどうかしら」"

hide boy_b1_5
show boy_b1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice chi_g0020
Seito "「いいと思います……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が、普段髪を止めるのに使っているリボン。\n
あれなら女の子らしい上に、予備がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼に渡してしまったとしても、すぐに困るというようなことはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（でも、予備がたくさんあるわけじゃないし、ないとやっぱり困るな）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「それ、あげたら、あげっぱなしになるの？」"

hide boy_b1_2
show boy_b2_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice chi_g0021
Seito "「いえ、来週に今度はブリーズってイベントがあるらしいんです。\n
そっちでは、女子が男子寮にやってきて、奪われたものを奪い返すという……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……シンフォニアって、周囲が思っているよりもお祭り好きよね」"

hide boy_b2_8
show boy_b2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice chi_g0022
Seito "「はは、そうですね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世間一般では、優秀な学校、世界一の魔法学校として認識されているシンフォニア高位魔法学校。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなイベントがあるとは想像もしていなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何事も、実際に臨んでみないとは分からないことばかりだ。\n
私は彼を案内して自室へと向かう。"

hide boy_b2_2

play sound se_0451
pause .5
play sound se_0282

scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "扉を開錠して、少し迷ったものの、彼を招き入れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……う～ん。\n
安全そうな相手でも、緊張するな）"

play sound se_0399
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段は、女子寮自体が男子禁制。\n
自室に、イベントとはいえ見知らぬ青年を招き入れるのにはドキドキと心臓が騒ぐ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "色恋だのとは違う、罪悪感のような感情だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "罪悪感なんて、それこそ鳥を食べたときのエースが抱くべき感情。\n
今、私の頭をよぎったのも、エースだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いけないことをしている、という背徳感といってもいいのかもしれない。\n
なぜか、あの迷子剣士が思い浮かぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……ちょっと待っていてね。\n
今、リボンを出すわ」"

play sound se_0161 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おずおずと部屋に入ってきた後、ドアの辺りでおとなしく立ち尽くしている彼へそう言って、私はアクセサリーを収納してある引き出しを開ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（リボンの予備は、この辺りに……）"

play sound se_0170
play sound se_0290
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "コンコン、とドアの鳴る音。"

play sound se_0262
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "咄嗟にびくっとしてしまい、引き出しの小物を取り落としそうになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……？\n
こ、こんな時間に誰かしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざわざ部屋にまで訪ねてくるような相手に思い当たる節がない。"


show boy_b2_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0023
Seito "「あ、もしかして、誰か来る約束をしている人がいましたか？\n
すいません、もしそうだったら俺、別の人のところに……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「いいえ、そんな約束をした相手はいないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「私は、さっきあなたに会うまでこのイベントについて知らされていなかったぐらいだもの」"

hide boy_b2_4
show boy_b2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice chi_g0024
Seito "「あ、そうなんですよね。\n
何も知らない女子の新入生への説明も、俺たち男子新入生に課せられた課題らしくて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「うまく説明して分かってもらえないと、部屋に入れてもらえないし、戦利品ももらえないってことなのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「そのあたり、弁論技術を鍛えられているのかも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "例外もあるが、魔法使いというのは、己の魔力を魔法へと変換するための論述式のような技術を必要とする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "新しい種類の構築にも欠かせない。\n
今ある論述の丸暗記で魔法を行使しているうちは、一人前の魔法使いではない。"

hide boy_b2_5
show boy_b2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0025
Seito "「そうですよねっ。\n
俺、自信なかったんですけど……」"

hide boy_b2_3
show boy_b2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0026
Seito "「同じ新入生のあなたに、協力してもらえてよかったです……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「ふふ、大袈裟ね。\n
ブリーズのときには、逆によろしく頼むわ」"

hide boy_b2_2
show boy_b1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice chi_g0027
Seito "「もちろんですよ！\n
任せてください！……っていうのも変ですけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「変といえば、敬語やめてよ。\n
あまり知らない者同士とはいえ、新入生同士なんだから」"

play sound se_0419
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……なんて、だんだんと打ち解けてきつつ、扉へと向かう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、彼以外にも誰か新入生の男子が、戦利品を求めてやってきたのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "季節はだいぶ違うが、ハロウィンを思い出して口元に笑みが浮かんだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分が見えるところにいるとよくないと思ったのか、扉へ向かう私とすれ違うようにして、彼が部屋の奥へと移動する。"

hide boy_b1_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はそれをちらりと視線で追いかけた後、特に警戒することもなく、がちゃりとドアへと手をかけて……。"

play sound se_0282

scene bg25_rr_nig
with dis

show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0284
Ace "「やあ、[firstname]！\n
こんばんは！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「！！！？」{/size} "

play sound se_0319
hide ace_m_03_3


scene bg24_rj_nig_lon with Dissolve(.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばたん、と勢いよくドアを閉める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何も考えていなかった。\n
いわゆる脊髄反射だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "叩きつけるようにして閉めたドアに背中を預けて、深呼吸を何度か。\n
最近、深呼吸が癖のようになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「な……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（なんでエースが！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "現在、エースは私に恋の魔法（口に出すと恥ずかしいネーミングだ）をかけようとしている。\n
もしくは、かけられようとしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのあたりのことを考えると、このタイミングでエースが私の部屋を訪れるのは間違っていない……、かもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、エースがイベントに間に合わせて目的地に到達するなんていうのは異常極まりない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、私も彼が訪ねてくるなんて想定していなかったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0285
Ace "「あはは、どうしたんだ？\n
そんな、バケモノでも見たような声あげちゃって」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「な、なんであなたがここにいるのよ！？\n
イベントにリアルタイムで辿り着けるなんて、おかしいわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
voice ace_g0286
Ace "「そこはそれ、俺は誠実な風紀委員だからな。\n
愛のためなら、妥協も辞さないぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「は、はあ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……ペーターが乗り移ったのかしら？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "半ば本気で思うほど彼らしくもなく、白々しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0287
Ace "「ちょーっと、メイドさんに案内してもらっただけさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「メ、メイドさんに？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段は旅を楽しむだとか言って、誰かに案内されることをよしとしないエース。\n
今回のは、大きな妥協といえよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、一つ気になる点がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の場所、他の時間ならばともかく、今このとき、この場所ではたしてメイドがそこまで親切に案内してくれるものだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（でも……、単独でエースが辿り着けるわけがないわよね……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮内ですらキャンプを敢行する男だ。\n
一人で、ここまで辿り着けるわけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メイドに案内させたという言葉の信憑性は増すわけだが……。"


show boy_b1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0028
Seito "「大丈夫ですか？\n
何か大きな音がしましたけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（しまった！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょこ、と部屋の奥から、新入生の男の子が顔を出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心配してくれているのだろう。\n
気遣わしげな声には、何かあったのならば自分がなんとかしなければというような決意の色が滲んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（……こういうのが、本当の意味で誠実っていうのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "比較対象が目の前にいるだけに、しみじみしてしまう。"

play sound se_0771 volume .4
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0288
Ace "「へえ。\n
誰か来ているのかな、俺にも紹介してくれよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "{size=+20}（ひい）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後、扉隔てた向こうから、空気がすごい勢いで冷えていくのが分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ」"

play sound se_0452
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は慌てて背を扉より浮かすと、扉に鍵をかけた後に彼の元まで小走りで移動する。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「に、逃げて……！」"

hide boy_b1_1
show boy_b1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice chi_g0029
Seito "「え？\n
に、逃げるって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「逃げたほうがいいと思う……！\n
具体的に何がどう、とは言えないんだけど……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……でも、危険だわ）"

play sound se_0361
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私自身、うまく説明出来ない。\n
状況が飲み込めず、立ち尽くす彼の手を引いて窓辺へと連れて行く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脳裏に浮かぶのは森での光景だ。\n
規律を乱した生徒を、容赦なく、笑顔で制圧してみせたエース。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの光景が、何故か今、目の前にちらついて仕方がない。"

play sound se_0287
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……っ、早く早く！」"

hide boy_b1_4
show boy_b1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice chi_g0030
Seito "「え、でも、まだ戦利品を貰っていないし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_6")
T "「……命のほうが大事でしょうっ！？」"

hide boy_b1_5
show boy_b1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_6")
voice chi_g0031
Seito "「ええ！？\n
命にかかわるようなこと！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「それくらい、危険かも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうして、こんなにも危機感を覚えなくてはならないのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とエースは恋人というわけでもないし、私も彼も、何か悪いことをしたわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だけどそれでも。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の入り口からごごごご、と流れ込んでくる冷気に名前をつけるならば、「殺気」なんて言葉になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（ち、痴情の縺れで殺傷沙汰なんて、勘弁……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そもそも、そんなものが発生する土壌すらないはずだというのに。"

hide boy_b1_4
show boy_b1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0032
Seito "「あ、あなたは大丈夫なんですか！？\n
俺、残るべきなんじゃ……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_9")
T "「大丈夫だから、早く行って！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のことを心配して残ろうとしてくれるのは、もちろん彼の善意だ。\n
けれども、今はとにかく、さっさと出て行ってほしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しーんと静かになった扉の前から、嫌な予感しかしないのだ。\n
私は半ば無理矢理、力づくで彼を窓から押し出していく。"


scene bg06_sk_h_nig
with dis
hide boy_b1_1
show boy_b2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0033
Seito "「……分かりました」"

hide boy_b2_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "諦めたのか、彼は心配そうにしながらも、呪文を唱えてふわりと宙に舞った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すうっと夜闇に溶け込むようにして見えなくなる彼の後姿を見送って、ほうと息を吐く。"

play sound se_0413
camera at hpunch
camera at vpunch

scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それとほぼ同時に、背後より聞き捨てならない物騒な音が響く。\n
私は、弾かれたようにそちらを振り返った。"


show ace_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0289
Ace "「……[firstname]、君ってば酷い子だよなあ？\n
鍵をかけて仲間はずれなんて、よくないぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え、エース！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鍵をかけてあったはずのドアを難なく開けて（というか、壊して）、エースがひょっこりと顔を出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その手には、抜き身の長剣がぶら下げられている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（こ、こわ……っ！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抜き身の長剣を片手にぶら下げ、彼は微笑む。\n
いくら爽やかな笑みを浮べていたとしても、ホラーさながらの状況だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「ド、ドアを壊したの！？」"

hide ace_m_01_8
show ace_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice ace_g0290
Ace "「ドアは、壊していないぜ？\n
大丈夫、ちゃんと閉まる」"

hide ace_m_01_3
show ace_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice ace_g0291
Ace "「最初はドアごと斬ろうと思ったんだけど、そうすると部屋の中が廊下から丸見えだろ？\n
物騒だから、それはマズイ」"

hide ace_m_03_9
show ace_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice ace_g0292
Ace "「……ほら、見知らぬ男が侵入してきたりしたら大変だろ？\n
だから、鍵だけ斬ることにしたんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……見知っている人でも、侵入してきたら大変だけど」"

hide ace_m_02_1
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_g0293
Ace "「そう？\n
でも、俺なら安心だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（安心……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無理だ。\n
とてもじゃないが、安心など。"

hide ace_m_03_3
show ace_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0294
Ace "「……ほら、俺って、気が利いているよな。\n
ぱっと見、分からないだろ？」"

play sound se_0664
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは、ドアを閉めてみせた。\n
彼が言うように、そうして閉めると何ら普通のドアとは変わらないように見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の言葉どおり、鍵だけが壊されているのだろう。\n
エースは、私に気を遣ってやったと言わんばかりだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し見方を変えると、外からは異常が分からないということ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "扉が派手に破壊されていれば、誰かが様子を見にやってくるかもしれないが、これでは望めない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（つまり、助けが来ないってことじゃないの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちら、とエースを伺う。\n
にこにこと、いつもどおりの爽やかな笑顔を浮べているようだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（～～目が笑ってない……っ）"

play sound se_0593
hide ace_m_03_12
show ace_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice ace_g0295
Ace "「あれ、[firstname]？どうしたんだ？\n
どうして逃げるんだよ」"

hide ace_m_02_11
show ace_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice ace_g0296
Ace "「はは、せっかく会いに来たのに……。\n
本当、君ってつれないよなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「そ、そうね。\n
私みたいな冷たい子、相手にしないほうがいいわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こちらへと近付いてくるエースから、じりじりと後ずさる。\n
が、すでに窓の近くにいたため、すぐに窓枠へとぶつかってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうなったら、いっそ外に逃げるべきだろうか。\n
今はストームというイベントの最中だが、本来、女子寮は男子禁制。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後どれくらいの時間続くのか分からないが、このイベントさえ乗り切ってしまえば、エースだって女子寮から退散せざるを得ないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（どうする？）"

menu:
    "逃げる。":
        jump gakuen_ace4_4a
    "居直る。":
        jump gakuen_ace4_4b
label gakuen_ace4_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（に、逃げよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう思わずにはいられないほど、目の前のエースは怖かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（すぐに逃げよう。\n
そうしよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "身を翻し、閉じたばかりの窓へと手をかけ……。"

play sound se_0492

play music view_nig_p_wam

show m_ace4_1 onlayer master
with dis
hide ace_m_02_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中を見せた隙を逃さなかったエースに、いともあっさりと捕獲された。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（いや、本気で逃げきれるとは、自分でもあまり期待していなかったけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice ace_g0297
Ace "「逃げるなんて、酷いよなあ。\n
つれないを通り越して、酷い子だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐ、っと背中から私を抱き捕らえる腕が強くなる。"

jump gakuen_ace4_5
label gakuen_ace4_4b:
$ lovechara_ace_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（逃げる必要なんてないわ。\n
悪いことはしていないもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逃げ出したくなる気持ちを押さえつけて、ぐっとエースを見返した。\n
そんな私に対して、エースは双眸を細める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一歩、また一歩と距離を詰め、エースが近付いてくる。\n
逃げる必要はないはずなのに、そのオーラに負けて、また逃げたくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せめて視線だけでも逸らしたくて、背を向け、窓を開けようとする。\n
背中を見せるのは、別に怖がってなんかいないとアピールするためだ。"

play sound se_0055


hide m_ace4_1
show m_ace4_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりと腰にエースの腕が回り、引き寄せられた。"

jump gakuen_ace4_5
label gakuen_ace4_5:
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0298
Ace "「髪、少し湿っている。\n
……お風呂上りだった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後から耳元に顔を寄せて、囁かれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くすぐったいような、寒気にも似た感覚。\n
ぴくりと震えてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースの片腕は私の肩を、もう片手はウェストの辺りを抱いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "セクハラというだけで問題だが、もっと大きな問題がある。\n
抱くほうの手に、エースが抜き身の剣を持ったままだということだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ネグリジェ一枚を纏った体の上に、硬い剣の腹を感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……ね、ねえ、その剣しまってくれない？\n
脅されているみたいで、気分が悪いわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice ace_g0299
Ace "「さあ……、事実、脅しているのかもしれないぜ？\n
君が、酷いことをするから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「私が何をしたっていうの。\n
あなたの被害妄想よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざと素っ気無い声を作り、言い切る。\n
そうでもしないと、背後から私を抱きしめるエースの、その雰囲気に呑まれてしまいそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中越しに感じる、人間らしい体温。\n
真逆に、突きつけられる硬い無機質な剣の感触。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この二種類の感覚は、まさしくエースという男を表している。\n
表裏というより、一体だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0300
Ace "「とぼけるんだ？\n
それとも、本当に分からないのかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0301
Ace "「……賢い君が、おかしいよね？\n
分からないはずがない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「おかしいのは、あなたでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつも、おかしなことばかり。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0302
Ace "「……そうだね、おかしいかもしれない。\n
でも、好きな子が夜に他の男を部屋に連れ込んでいたら、男なら誰だっておかしくなると思わない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……つ、連れ込んでなんかいないわっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice ace_g0303
Ace "「……連れ込もうが、連れ込まれようが、ともかく許されざる事態ってことに変わりはないよ。\n
おかしくなるほどの重大事だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（……あなたは、元々おかしいでしょう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とは、さすがに言えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0304
Ace "「しかも、そうやって必死に逃がすぐらい……、彼のこと気にかけているんだ？\n
尚更……、見逃せないよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ、逆でしょう、逆！\n
関係ない子を、私達の問題に巻き込めないでしょう！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice ace_g0305
Ace "「関係ないなら、いいじゃないか。\n
……どうなっても」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「関係ないからこそ……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の言葉が、私達の考え方の違いを浮き上がらせる。\n
関係ないからと切り捨てる彼と、関係ないから巻き込みたくない私との違いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（エースの関係ない、は、本当の意味での無関心だから……。\n
……だから、簡単に踏み込める）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "関係ない人間はどうでもいいから、いくらでも。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のことだって、どうでもいいから、こんなふうに無造作に迫ってくるのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0306
Ace "「あんまり理解してもらえていないみたいだな。\n
……ふう、俺のアプローチ不足のせいか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0307
Ace "「……参ったぜ。\n
反省点は次に活かさないと」"

hide m_ace4_1

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……{size=+20}次？{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呟かれたエースの言葉に、頬に感じていた熱が、かっと燃えるように頭に移るのが分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「次って、どういうことよ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "咄嗟に怒鳴っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……私が駄目だったからって、他の子で試すつもりなの？」"

play sound se_0551
camera at hpunch
camera at vpunch

show ace_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "胸元に押し当てられていた剣の感触も省みず、くるりと体の向きを変えるとエースを正面から睨み付ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "押し付けられていたのは剣の腹なので、動いたところで心配ないというのは分かっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下手な相手であれば、私が動いた拍子に刃の部分を向けてしまうなんてこともあるかもしれないが、相手がエースならば……という嫌な意味での信頼がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、一瞬だけ、私のそんな反応に驚いたようだったが……。\n
すぐに、にんまりと笑った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもの爽やかさとは、少しだけ違う笑い方だ。"

play sound se_0438
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "片腕は私の腰を抱いたまま、握っていた剣を腰の鞘へと戻す。\n
自由になったその手で、彼は私の頬へと触れた。"

play sound se_0551
hide ace_m_03_2


show m_ace4_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0308
Ace "「はは、君、なんで怒るんだ？\n
実験なんて、了承してないんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice ace_g0309
Ace "「……ま、俺も承諾していないけどな。\n
実験だとか、俺からは言っていないし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースの言葉は、頭を素通りする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（私……、怒っている？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怒っている。\n
頭の中でかっと熱くなった感情の正体は、怒りといって間違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0310
Ace "「承諾していなくても、他の子に試されるのは嫌なんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "指摘されて、愕然とする。\n
私は怒って……、嫉妬している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「次」と、別の誰かを示唆するようなことを言われて、腹を立てているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういう意味じゃない、と言い募ろうと視線を持ち上げ、言葉が消えた。\n
ただひたすらに、頬が熱い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頬も熱く、頭も熱い。\n
興奮してもいるし、怒ってもいるのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の思考、反応。\n
それらが信じられなくて、頭の中が真っ白になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「ち、違うのよ！？\n
怒っているとしても、そういう意味じゃなくて……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice ace_g0311
Ace "「風紀委員なのに風紀を乱すようなことが平気で出来るのかってこと、だろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間髪いれずに返された。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（そうなの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、違う。\n
私が怒っていたのは、そんな道徳的な問題ではなく……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もっと、主観的な……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0312
Ace "「安心してくれよ。\n
次、っていうのは次の実験とかいう意味じゃなくて、次の君へのアプローチってことだから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「あ、安心できないわよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
Ace "「……[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「な、何？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice ace_g0313
Ace "「君も、俺が好きなんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（も、って……。\n
まるであなたが私のこと、好きみたいじゃない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当の意味で、間違っていない正しい意味で。\n
彼は、私を好きだとでもいうのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0314
Ace "「俺も、君が好きだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「でも、それ、意味が……」"

hide m_ace4_2
show m_ace4_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "疑問を口にするよりも先に、口付けられていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逃がさない、というように。\n
これ以上ないほどの接近。"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "腰を、強く引き寄せられる。\n
自然仰け反るようになる背を追うように、彼は屈んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「つ、う……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深くまで交わるキスを求められる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Ace "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただでさえまとまりのなかった思考が、完全に散り散りになっていく。\n
何も考えられない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "酸素が足りなくて、喘ぐ胸ごと引き寄せられて、ぴたりと体が重なる。\n
そして、心臓の鼓動が交わった。"

play sound se_0550 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……どうして）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "音が重なる。\n
鼓動が合わさる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしてか、それがとても不思議なことに思えた。\n
奇跡のように、驚くべきことに。"

hide m_ace4_3
show m_ace4_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……心臓の、音）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なぜだろう。\n
泣きたくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ごく、普通のことだ。\n
心臓など、誰しも変わらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不整脈でもない限り、鼓動のペースも変わらない。\n
それなのに、どうしてか……、特別なことに思える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とても、とても。\n
不思議なことに。"

play sound se_0550 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……ああ。\n
生き物の音だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この人は生きている。\n
今、この場にいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーストではないのだから、生きていることなど当然。\n
それなのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（……今、ここで生きている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おかしなことだ。\n
感傷的になる理由など何一つないのに、涙が出る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_3")
T "「…………」"

play sound se_0627
hide m_ace4_4
show bg06_sk_h_nig onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこか、遠くで笛が鳴る音が聞こえた。\n
それが合図だったかのように、エースが唇を離す。"

hide bg06_sk_h_nig

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_4")
T "「……離れないで」"


show ace_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_4")
voice ace_g0315
Ace "「……え？」"

play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「…………」"

play sound se_0267
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、ずるずると腰砕けにへたり込んでしまった。"

hide ace_m_01_3
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0316
Ace "「……あれ？はは、そんなによかった？\n
男冥利に尽きるなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「う、うるさいわよ……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かぶつけてやりたいと思うものの、あいにく私は普段から床の上に物を直接置くような習慣はない。"

hide ace_m_03_3
show ace_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0317
Ace "「俺も離れたくないよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「っ……」"

hide ace_m_01_11
show ace_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0318
Ace "「でも、時間だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……時間）"

hide ace_m_03_10
show ace_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice ace_g0319
Ace "「一旦、退却しないとな。\n
今のはストーム終了の合図なんだ」"

play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは、部屋の中をうろうろと歩きまわる。\n
持ち帰る戦利品を物色しているのだと気付く。"

hide ace_m_02_12
show ace_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0320
Ace "「ああ、そうだ。\n
さっきいた男に、何か盗られちゃったりしてないよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……盗られていないわよ。\n
それがどうしたの？」"

hide ace_m_03_12
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0321
Ace "「え？いやいや。\n
君が何か盗られちゃったなら、盗り返してあげないといけないなって」"

hide ace_m_03_3
show ace_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0322
Ace "「ほら、俺は風紀委員だからな。\n
困っている人を放っておけないんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……嘘つき）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉だけ聞けば親切に聞こえても、その面持ちは得体のしれない迫力を帯びている。\n
笑顔なところが怖いのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどの彼を逃がしたのは英断だった、と我ながら思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは私が引き出しから取り出しかけていたリボンに気付いたのか、それを手に取った。"

hide ace_m_02_1
show ace_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0323
Ace "「リボン、か。\n
君がいつも使っているやつだよな、これ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「正確に言うと、その予備よ。\n
……あなたは戦利品なんて持ち帰らなくても、誰にも馬鹿にされたりしないでしょうに」"

hide ace_m_03_9
show ace_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice ace_g0324
Ace "「俺が、欲しいんだよ。\n
よし、これに決めた」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは私のリボンをくるくるとその手のひらに巻きつける。"

play sound se_0627
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠くで、再び急かすように笛が鳴った。"

hide ace_m_01_10
show ace_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0325
Ace "「それじゃあ、またな！\n
学校のどこかで会おうぜ！」"

play sound se_0695
hide ace_m_01_4


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "爽やかに笑ってエースは私の横を通って、窓をばたりと開け放つ。\n
外から吹き込む風に、カーテンがはたはたとたなびく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースはそのまま、ひょいと窓枠を飛び越えて見えなくなった。"

play sound se_0053
pause .5
play sound se_0484
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はのろのろと立ち上がると、窓枠に身を乗せて外を見やる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "沈むような闇の向こう、ひらりとたなびくマント。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（……{size=+20}そっち、男子寮とは別方向よ{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どのみち男子寮に戻ることの出来ないエースには、戦利品なんて無意味だろうに。"

with dis
$ hi_mes()

scene bg_par15_rg_ros_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_ace5
