label gakuen_elliot6:
scene bg_map_nig
with dis
$ clockanim()


scene bg_par15_rg_hat_nig
with dis

play music forest_thick_nig_p_wam

scene bg24_rj_nig with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そしてあっという間に、ブリーズの夜が来た。\n
私は部屋の中でじっとそのときを待つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの開始は、それを伝える役目の生徒が各部屋の扉をノックして回ることで知らされるのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "参加する生徒はそれぞれが闇に乗じて中庭を渡ろうと試み、参加する気のない生徒はただその合図を聞き流すだけでいいらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は参加組なので、その合図を待つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……エリオット）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、あの日以来私はエリオットにまともに顔を合わせることが出来ていない。\n
それでも同じ寮に暮らしているのだし、見かけることぐらいはある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、見かけるだけだ。\n
エリオットは私を見ると、とても罪悪感に苛まれたような顔をして目をそらす。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（勝手だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "犯人探しに忙しいことは想像がつく。\n
しかし、勝手だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "勝手に守ろうとして、勝手に離れようとしている。\n
だから私も、勝手に行動することにしたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今からしようとしていることを思うと、胸がドキドキと高鳴る。\n
未だかつて、体験したことがないような高揚だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……これで私も、不良の仲間入りね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もともと淑女なんかではなかった私だが、ライン引きは出来ていた。\n
この一歩を踏み出してしまったら、姉さんのような淑女の振りすら……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……それでも、構わない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうせ、振りでは何も手に入らない。"

play sound se_0300

play music magic_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアが鳴った。\n
時間だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0008
Seito "「開始の合図だわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0009
Seito "「ブリーズよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いよいよ、ブリーズが始まる。"

play sound se_0496

show magic_b onlayer master with Dissolve(1.5)
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「…………」"

hide magic_b with Dissolve(1.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は姿隠しの呪文を唱えると、窓を開けてするりと外へと飛び出した。"

play sound se_0216
pause .5
play sound se_0348

scene bg20_gd_nig
with dis
play sound se_0141
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

play sound se_0738
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "続いて、落下速度を軽減させる。\n
ふわりと芝生の上へと降り立った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスとの会話を思い出す。"


scene bg20_gd_nig_s
with dis

show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0061
Julius "「ブリーズはストームよりは幾分かおとなしい傾向にあるな。まあ、ストームはいつのまにか、使用人との衝突を楽しむ趣が出てきているからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「つまり、ブリーズはあくまでこっそり忍び込むことがメインってことなの？」"

hide yuri_m_02_9
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0062
Julius "「ああ、その通りだ。\n
使用人達の目をくぐって男子寮に入ることが出来れば、それまでだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「でも……、その使用人の目をくぐるのって大変なんじゃない？\n
私はまだ試したことないけれど、夜遊びへの監視は厳しいと聞いたことがあるわ」"

hide yuri_m_03_9
show yuri_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice jul_g0063
Julius "「……{size=+20}試さなくていい。{/size}\n
もちろんブリーズの夜は、使用人達も本来の監視よりも手加減している」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……本当に、公認イベントなのね」"

hide yuri_m_03_11
show yuri_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice jul_g0064
Julius "「だから、先刻から公認イベントだと言っているだろうが。そうじゃなければ、女子寮から物品の強奪なんていうストームの時点で、立派な犯罪だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……確かに」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……よく、学校側が認める気になったわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだけ、問題に発展させない自信があるからか。\n
それとも、問題が起こっても何とかなると解決させるほうの自信か……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いずれにしても、入学時に誓約書まで書かされているのだから（読み飛ばすほど小さく、多岐に渡って制約の文言が連なっていた）、したたかだ。"

hide yuri_m_03_4


scene bg20_gd_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲を見渡すと、使用人がカンテラ片手に見回りをしているのが分かる。\n
だが、彼らだって分かっているはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姿隠しの魔法を使われてしまえば、肉眼で確認することは出来ない。\n
魔力的監視システムを構築しなければ、本当の意味で見張ることなど出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それをしていないのが、使用人側の設けたハンデなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "スリルをなくしてしまわない程度に、それでいて完全に潰してしまわないように、との微妙な力加減が見える。"

play sound se_0748
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0014
Servant "「っここか！！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0083
Seito "「きゃ……！！？\n
っ、なんで見つかったのお！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0015
Servant "「そりゃあ、いくら姿隠しをしていてもなあ……。あれだけ足音たてて、茂みを掻き分けて歩いていたら、そこに人がいるのは分かるだろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも時折、こんなやりとりが遠くから聞こえてきたりもする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "捕まった女子生徒は、何でも一度部屋まで強制送還されるのだそうだ。\n
「振り出しに戻る」というわけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はそういった小さな騒ぎを尻目に、ひたすら目的地に向かって進んでいく。\n
ゆっくり、こっそりと、しかし確実に。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目的地については、ブラッドに確認しておいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの面倒くさがりのブラッドが協力してくれたあたり、彼はこの事態をとても楽しんでいるらしい。"


scene bg20_gd_nig_s
with dis

show bra_m_02_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0511
Blood "「お嬢さんが目的とする部屋は、二階の右から四番目だよ。\n
……だが、いいのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「何が？」"

hide bra_m_02_16
show bra_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice blo_g0512
Blood "「……私でなくて」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「あなたじゃ駄目なのよ、ブラッド。\n
……気持ちは嬉しいけれど」"

hide bra_m_03_3
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_8")
voice blo_g0513
Blood "「……ふう。\n
そういう意味ではなくて……、まあ、いい」"

hide bra_m_03_2
show bra_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_8")
voice blo_g0514
Blood "「……楽しんでおいで。\n
仕返しに妬かせるより、直球のほうが君達らしい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「エリオットにも、聞かせてやりたいわ」"

hide bra_m_03_1
show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice blo_g0515
Blood "「いや……、そうだな、むしろ、君よりエリオットに向いているか。\n
スタンスを崩すほどというのも、楽しそうだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「ちっとも」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当事者とは、必死なものだ。"

hide bra_m_02_2
show bra_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0516
Blood "「……楽しんでおいで」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "楽しむ余裕など、あるものか。"

hide bra_m_02_1


scene bg20_gd_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（二階の、右から四番目）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "忘れないように、何度も復唱しては覚えこんだ部屋の位置。\n
それを更に、脳裏で繰り返す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子寮の近くまでやってきたところで、ストームの夜にエリオットがしてみせたように呪文を唱える。"

play sound se_0725
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、踏み切った。"

play sound se_0734
show magic_g onlayer master with Dissolve(1.5)
pause 1
play sound se_0216

scene bg06_sk_h_nig with spread_short
play sound se_0133
play sound se_0698
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "浮遊というよりも、一時的に重力に干渉するタイプの魔法だ。"

play sound se_0134
hide magic_g with grad_t_long
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目測たがわず、私は目的の窓辺へと降り立つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "万が一にでも間違えてしまっていたらば、洒落にならない。\n
念には念をいれてもう一度確認する。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（……ここだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帽子屋男子寮の二階、右から四番目の部屋で間違っていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここが、私の目的の場所だ。\n
この部屋の中に、彼がいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（いる……のよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（覚悟は出来ている？）"

menu:
    "出来ている。":
        jump gakuen_elliot6_2a
    "迷いがある。" :
        jump gakuen_elliot6_2b
label gakuen_elliot6_2a:
$ lovechara_elliot_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "行動に移す前に、もう一度だけ自問自答する。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……出来ているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際に声に出して答えて、私は自らの魔法媒体である杖を懐から取り出した。"

jump gakuen_elliot6_3
label gakuen_elliot6_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "出来ている、と即答できるほどには、私の決意は固まっていない。\n
ここまで来ても、まだ躊躇いがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（それでも、エリオットを取り戻したい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "取り戻すなんて妙な言い方だが、このままではせっかく縮まった距離が離れてしまうと分かっていた。"

jump gakuen_elliot6_3
label gakuen_elliot6_3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "杖には簡単な呪文が刻まれており、私の魔力に反応してそのサイズを変えるようになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段はヘアピンサイズで懐に収まっているのだ。\n
取り落とさないよう、しっかりと握り締める。"

play sound se_0126
pause .4
play sound se_0526 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "感触を確かめるように、軽く一振りして、姿隠しの魔法を解除した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はもう男子寮の敷地に入ってしまっているので、見つかったとしても問題ないはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……ふう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（そういうイベントなんだもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、私がこれからやろうとしているのはイベント外のこと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深く、息を吸って、吐いて。\n
窓の傍に人がいないのを確かめた後……。"

play sound se_0676
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は杖を思いっきり振りかぶって、目の前にある部屋の窓ガラスを力いっぱい、粉砕した。"

play sound se_0318
play sound se_0316

scene white ##instant]

play music opposition2_a_ali

scene bg23_rd_nig with spread_short

show huryou_d1_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0013
Furyou "「っ！！！！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の奥にいた見覚えのある男子生徒が、何が起こったのか分からない、といった顔でこちらを振り返るのに、私はにっこりと笑みを浮べて見せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「こんばんは」"

hide huryou_d1_6
show huryou_d1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_2")
voice oto_g0014
Furyou "「な……っ！？\n
なんだ、おまえ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_3")
T "「何だとはご挨拶ね。\n
前回はお世話になったのに」"

hide huryou_d1_9
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_3")
voice oto_g0015
Furyou "「！？\n
……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう、見覚えのある彼。\n
エリオット、ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の目的地は、最初からエリオットの部屋ではない。\n
彼だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ルール違反を犯し、エリオットに押さえ込まれ、反発し、私の部屋に石を投げ込み窓ガラスを割ってくれた青年。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「あなたのおかげで、私まで散々なの」"

hide huryou_d1_2


scene bg_par19_fi
with dis

show yuri_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice jul_g0065
Julius "「……犯人が分かったら、処罰せずに連絡がほしいだと？\n
おまえまで、帽子屋寮の流儀に染まって私刑でもするつもりなのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「違うわよ。\n
……いや、ある意味違わないかもしれないけれど」"

hide yuri_m_03_2
show yuri_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jul_g0066
Julius "「今なら、聞かなかったことにしてやる。\n
私は、そういった勝手な行動を取り締まる側の人間だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「ねえ、ユリウス。\n
ストームとブリーズは学校公認のイベントなんでしょう？」"

hide yuri_m_02_4
show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice jul_g0067
Julius "「ああ。\n
それは前に話した通りだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「だからこそ、一部の校則違反も認められるのよね？\n
夜間の外出や、異性の寮への侵入、そして物品の強奪なんてのが」"

hide yuri_m_02_9
show yuri_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice jul_g0068
Julius "「その通りだ。\n
ただし、物品の強奪については強奪とは名ばかり、実際には合意があるが」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_1")
T "「ええ、そうでしょうね。\n
ってことは、合意さえあれば何を奪ってもいいのよね？」"

hide yuri_m_03_8
show yuri_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_1")
voice jul_g0069
Julius "「おまえ……」"

hide yuri_m_03_11


scene bg23_rd_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、私のリボンを結局奪わなかった。\n
私はエリオットに何も奪われることはなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、ブリーズで取り返せるものなんて、本当なら何もないのだ。\n
だけれど。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼には、奪われた。"


show huryou_d1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0016
Furyou "「なっ、ななななな、なんだよおまえ！！？\n
何しにきたんだ！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「だから……。\n
何だとはご挨拶ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「……覚えていないの？\n
とぼけているのか、本当にボケているのか……」"

hide huryou_d1_5
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice oto_g0017
Furyou "「ボケていない、俺は正常だ！\n
おまえは、副寮長エリオット＝マーチご執心の……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな言葉に嬉しくなっている場面ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_8")
T "（でも、嬉しい）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……あら。\n
光栄だわ、知っていてくれたのね」"

hide huryou_d1_2
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice oto_g0018
Furyou "「……知っちゃいるが、何しに来たんだ。\n
エリオット＝マーチの女が……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……ああ、嬉しくなっている場合じゃないのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオット本人よりも、周囲からのほうが高評価とはいかがなものか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_1")
T "「分からないの？\n
今日はブリーズよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "動揺しきった彼の声に返しながら、私は割れた窓から腕を差し入れ、窓を開錠する。"

play sound se_0450
pause .6
play sound se_0585
pause 1
play sound se_0774
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓を押し開けて、部屋の中へと足を踏み入れる。"

hide huryou_d1_2
show huryou_d1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0019
Furyou "「わっ！？\n
勝手に入ってくるなよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は怯えたように、私が距離を詰めた分だけじりっと後ずさった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_10")
T "「あなただって、勝手に人の部屋の窓を割ったくせに。\n
……自分はよくて、人は駄目なの？」"

hide huryou_d1_5
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_10")
voice oto_g0020
Furyou "「ブ、ブリーズに乗じて俺に復讐しにきたのか！！？\n
俺がやったって証拠はあるのかよ！！？」"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……あなた、やっぱり正常じゃないわよ。\n
ボケてるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「復讐なんて言葉が出る時点で、自分がやったって認めているようなものじゃない」"

hide huryou_d1_2
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
Furyou "「！！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_3")
T "「……不安だったのね？\n
窓ガラスがもしも強化されていたら、って」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「私の部屋に投げ込んだ石に、あなたの魔力残滓が残っていたわ。\n
無意識のうちに魔力を込めていたみたいね？」"

hide huryou_d1_2
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice oto_g0021
Furyou "「……！！！！\n
そ、それで俺をどうする気だよ！？」"

hide huryou_d1_2
show huryou_d1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice oto_g0022
Furyou "「風紀委員会に連絡するつもりか！？\n
そうしたら、おまえだって同罪なんだ\n
ぞ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「連絡するまでもないんじゃないかしら」"

play sound se_0113
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は顔をあげて、彼へと近づいてくる足音を示唆する。\n
彼もすぐに、その足音の意味を察したらしい。"

hide huryou_d1_9
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0023
Furyou "「く……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一瞬逃げ道を探すように視線を揺らし、その次には開き直った。"

hide huryou_d1_2
show huryou_d1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0024
Furyou "「罰を受けるなら、おまえもだ！！\n
おまえも、罰を受けることになるんだぞ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうだろう。\n
寮の中で騒動を起こしたという点においては同罪になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……通常ならば。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「この場合、一番に駆けつけてくるのは、風紀委員や使用人じゃないでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは、帽子屋寮だ。"

hide huryou_d1_9
show huryou_d1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0025
Furyou "「あ……」"

play sound se_0590 volume .8
pause .15
play sound se_0273
hide huryou_d1_7
show huryou_d1_7 at left
show eri_m_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0213
Elliot "「おいこら！\n
何の騒ぎだ……！！？」"

hide eri_m_02_9
show eri_m_01_5 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0214
Elliot "「ん？\n
って……、え、[firstname]、あんた……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "噂をすれば影だ。\n
エリオットが、ドアを開けて飛び込んできた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "偶然近くを見回っていた、というわけではない。\n
ちゃんと、計算づくだ。"

play sound se_0158
pause 1

show bra_m_01_2 at center
with dis
hide eri_m_01_5

hide huryou_d1_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0517
Blood "「いやはや、ブリーズの夜とはいえ騒々しいな？\n
……おや、お嬢さんおかしなところで会ったな」"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットの後から悠々と現れたブラッドが白々しく言う。\n
彼が、エリオットをこの近くまで誘導してくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからエリオットは、窓ガラスの割れる音を……、その長い耳でちゃんと聞き取った。"


show huryou_d1_2 at center
with dis
hide bra_m_01_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0026
Furyou "「……っ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "月明かりにも分かりやすく、彼の顔が青ざめる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮長、副寮長と現れたところで彼が最初に何をしたのかを明らかにされてしまえば、厳罰は免れない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "特に彼には問題を起こした前科がある。\n
連想も容易だ。"

hide huryou_d1_2
show huryou_d1_2 at left
with dis

show eri_m_02_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、割れた窓ガラスと、そこに立つ私と、彼との間で視線を往復させ……。"

hide eri_m_02_13
show eri_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0215
Elliot "「……そうか。\n
てめえか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "低い、地を這うような低音を吐き出した。"

hide huryou_d1_2
show huryou_d1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0027
Furyou "「……っひ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットはそのままずかずかと彼へと接近すると、その胸倉を掴みあげようとする。"


show bra_m_02_3 at center
with dis
hide huryou_d1_5

hide eri_m_02_10

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0518
Blood "「……よせ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意外にも、というべきか。\n
それを制止したのはブラッドだった。"

hide bra_m_02_3
show bra_m_02_3 at left
with dis

show eri_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0216
Elliot "「ブラッド！？なんで邪魔するんだよ！？\n
こいつ……、証拠はねえけど、多分……」"

hide eri_m_02_10
show eri_m_02_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0217
Elliot "「……罰を受けなきゃなんねえ。\n
こういう輩はぶちかましていいっつう、ルールだろ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……{size=+20}どんなルールよ{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、ブラッドはその点においては止めない。"

hide eri_m_02_9
show eri_m_02_9 at right
with dis
hide bra_m_02_3
show bra_m_03_14 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0519
Blood "「……ああ、そうだな。\n
だがエリオット、おまえ、分かっているのか？」"

hide eri_m_02_9
show eri_m_03a_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0218
Elliot "「……何がだ？簡単なことだろ？\n
二発、三発ぶっとばして……」"

hide bra_m_03_14
show bra_m_02_16 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0520
Blood "「別に止めはしないが……。\n
おまえ、そこのお嬢さんにも同じ罰を与える気か？」"


play music forest_thick_nig_p_wam
hide eri_m_03a_3
show eri_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0219
Elliot "「……っ！！！」"

hide bra_m_02_16
show bra_m_02_15 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0521
Blood "「ルールなら平等に……。\n
女といえども容赦は出来ないぞ？」"

hide eri_m_01_10
show eri_m_03a_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0220
Elliot "「んな……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの声に、双眸を瞠ってうろたえたようにエリオットが私を見る。\n
私は、ブラッドが言ったように彼と同罪だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓ガラスを粉砕した。\n
彼に罪があるというのならば、私も同じだけの罰を受けなくてはいけない。"

hide eri_m_03a_3
show eri_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0221
Elliot "「……こいつは被害者だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「いいえ、同罪よ。\n
……私を、殴る？」"

hide eri_m_01_6
show eri_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが迷ったのは、ほんの少しの間だった。すぐにその瞳に強い決意の色を浮かべ、エリオットはどっかとその場に膝をついて座り込んだ。"


play music looking_for_a_ali
show m_eri6_1 onlayer master
with dis
hide eri_m_01_11

hide bra_m_02_15

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（エリオット？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、予想外の反応だった。\n
ブラッドと視線を交わしてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0222
Elliot "「ブラッド……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0522
Blood "「な、なんだ……。\n
エリオット？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "応じるブラッドの声も、ちょっと腰が引けている。\n
エリオットはそんなことにも構わず、すうっと深く息を吸うと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "覚悟の滲む声で、とんでもないことを言い出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0223
Elliot "{size=+20}「俺をぶちのめしてくれ！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0523
Blood "「は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とブラッドの、互いにこっそり交し合っていた目が丸くなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0524
Blood "「エリオット……。\n
残念ながら、私にそういう趣味は……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0224
Elliot "「ブラッド、俺はあんたの犬だ！\n
だけど、俺にこいつは殴れねえ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0225
Elliot "「だが、この男はぶちのめしてえんだ！\n
だから俺をぶちのめして、その後、この男をぶちのめさせてくれねえか！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言って、エリオットは殉教者のような面持ちで目を閉じた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しゃん、と伸びた背筋に、腿の上できつく握られた両の拳……。\n
いつか図書館で読んだ文献の内容が、頭を過ぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "{size=+20}「切腹？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠い東の国には、そうして腹を切って詫びることで責任を取るという風習があるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……そういう本、読んだことがあるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice blo_g0525
Blood "「いや……、この場合、タチの悪い青春ものではないかな。\n
私も、昔、誤ってそういう本を読んだことがある」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice blo_g0526
Blood "「あのときと同じ吐き気と……、眩暈が」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice blo_g0527
Blood "「おまえは本当に救いようのない馬鹿だな、エリオット。\n
潔すぎるというかなんというか、ああもう本当に殺したい……」"

play sound se_0103 volume .7
hide m_eri6_1
show m_eri6_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドがあながち演技ともいえない態で、顔の上半分を手のひらで覆って壁に寄りかかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもわざとらしい男だが、今回は本気に見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブツブツと小声で呪詛めいたことを呟きつつも……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（何よ、その助けを求めるような目は。\n
あなただって、面白がって乗ったくせに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……仕方ない。"

hide m_eri6_2

play sound se_0051

show huryou_d1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0028
Furyou "「……っひい！？\n
わわ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、傍らで呆然と立ち尽くしていた諸悪の根源たる青年の腕を掴んで、ずいずいと引っ張るようにしてエリオットの前へと出た。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、すっかり萎縮している。\n
エリオットの「後でぶちのめす」が効いているようだ。"

hide huryou_d1_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのエリオットは、間近に迫っても目を開けようとはしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……ばか」"

play sound se_0424
$ flash(.1)

show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice eri_g0226
Elliot "「……っ！\n
え、あ？あんた……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "覚悟を決めたように緩く皺を寄せ、目を閉じてしまっていたエリオットの額にデコピンを食らわせる。\n
それでようやく、彼は目を開けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「あなたが自決する必要はないわよ。\n
……これは、ストームとブリーズなんだから」"


show huryou_d1_7 at center
with dis
hide eri_m_01_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice oto_g0029
Furyou "「え？\n
は？え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「ね？\n
そうよね？」"

hide huryou_d1_7
show huryou_d1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice oto_g0030
Furyou "「ええ？\n
でも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "{size=+20}「ストームと、ブリーズなのよね？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "念を押すように言いながら、こっそり体の後ろで彼の腕をつねる。"

play sound se_0361
hide huryou_d1_7
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0031
Furyou "「いっで！？\n
いいいっ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "{size=+20}「ね？」{/size} "

hide huryou_d1_2
show huryou_d1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice oto_g0032
Furyou "「は、はい、そうです……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ストームの晩に彼が私の部屋のガラスを割ったから、私も彼のガラスを割り返してやったの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「取られたものを取り返す、っていうのを拡大解釈してみたんだけど……、両成敗ってことで帳消し」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……もちろん、学園側としては器物破損だし、簡単にはいかないだろうけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちら、とそこで視線を持ち上げてブラッドを見る。\n
彼とは、前もって打ち合わせずみだ。"


show m_eri6_3 onlayer master
with dis
hide huryou_d1_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0528
Blood "「……ああ、ストームとブリーズならば仕方がないな。\n
学校公認のイベントで、奪われたものを奪い返すのは認められているはずだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0529
Blood "「……なに。\n
怪我もなかったことだし、窓くらい、魔法でどうとでもなる」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0033
Furyou "「え……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0530
Blood "「ガラスを割られる、というのはある意味ガラスを取られるのと同義だろう。\n
やり返したとして問題はない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0034
Furyou "「そ、そんな無茶な……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0531
Blood "「……問題があるのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0035
Furyou "「！！\n
あ、ありません！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0036
Furyou "「何も！\n
なんの問題もありません！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0532
Blood "「そうだろうとも。\n
なあ、エリオット、おまえにとってもそうだな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0227
Elliot "「え、え～……。\n
……っと、こいつ、殴っちゃ駄目なのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0533
Blood "「ストームとブリーズで、殴るのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0228
Elliot "「だ……、駄目か」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0534
Blood "「……いいとは言わないが、駄目とも言っていない。\n
ストームとブリーズで殴らなくとも、またの機会もあるだろう」"

hide m_eri6_3

play sound se_0052
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひらひら、と面倒くさそうに手をふって、ブラッドが壁によりかかっていた身を起こした。それからちらりと、私の隣にいる青年へと視線をやった。"


show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0535
Blood "「……機会はある。\n
いくらでも」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぞくりと、背中が冷たくなるような流し目だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……こわ）"

hide bra_m_03_4
show bra_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice blo_g0536
Blood "「お嬢さんのおかげで、命拾いしたな。\n
今回は……、な。意味が理解できるか？」"

hide bra_m_03_3
show bra_m_03_3 at left
with dis

show huryou_d1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice oto_g0037
Furyou "「は、ははははは、はい……っっ！！」"

hide bra_m_03_3
show bra_m_02_15 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice blo_g0537
Blood "「ふむ、聞き分けがいい奴は嫌いじゃない。\n
さすが、腐っても我が寮の生徒だ」"

hide bra_m_02_15
show bra_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice blo_g0538
Blood "「……割れた窓ガラスは自分で何とかしなさい。\n
使用人達への説明はこちらでしておく」"

hide huryou_d1_2
show huryou_d1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice oto_g0038
Furyou "「わ、分かりました……！！」"


show eri_m_01_4 at right
with dis
hide huryou_d1_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
Elliot "「…………」"

hide eri_m_01_4
show eri_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice eri_g0229
Elliot "「ブラッド、なんて英断……」"

##special anime"kirakira_right"loop="false"time="1000"]
play sound se_0198
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、きらきらしている。"

hide bra_m_02_2
show bra_m_02_7 at left
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
T "きらきらされているほうのブラッドは、うんざりしている。"

hide bra_m_02_7
show bra_m_03_17 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

hide bra_m_03_17
show bra_m_03_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0539
Blood "「……はあ。\n
主に精神的に疲れた」"

hide bra_m_03_13
show bra_m_02_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0540
Blood "「私はもっと面白くなると思っていたのに……。\n
どうしてお嬢さんへの愛ではなく、私への忠誠を確かめる羽目になるんだ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "己の部下の盲信具合を改めて見せつけられて、ブラッドは喜ぶどころか逆にその暑苦しさに疲労を覚えたらしい。\n
溜息に憂いが滲んでいる。"

hide bra_m_02_3
show bra_m_03_15 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0541
Blood "「私は茶会の続きをしてこよう。\n
……ああ、エリオット、おまえはついてこなくてもいいぞ」"

hide bra_m_03_15
show bra_m_03_15 at left
with dis
hide eri_m_01_3
show eri_m_02_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0230
Elliot "「え、いや、俺、ちゃんと供を……」"

hide bra_m_03_15
show bra_m_01_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0542
Blood "「いらん。\n
……断る」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しっし、と追い払うようにブラッドが手を揺らす。"

hide bra_m_01_13
show bra_m_03_16 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0543
Blood "「そこの暑苦しいウサギは君に任せたよ、お嬢さん。\n
ああ、それからエリオット」"

hide eri_m_02_12
show eri_m_01_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0231
Elliot "「え？\n
なんだ？」"

hide bra_m_03_16
show bra_m_03_17 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0544
Blood "「そこのお嬢さんは、おまえより、よっぽど逞しい。\n
守ってやろうなんて、あつかましいぞ？むしろ、守ってもらえ」"

play sound se_0158
hide bra_m_03_17

hide eri_m_01_7
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだけを言うと、ブラッドはふらふらとテラスに向かって歩みさっていってしまった。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "残されたエリオットはしょぼくれていいのか、それとも、といったような顔をしている。\n
つまり、困った顔だ。"


play music study_taught_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……行きましょうか」"

hide eri_m_01_8
show eri_m_03a_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice eri_g0232
Elliot "「へ？え？\n
い、行くってどこに？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「あなたの部屋に決まっているでしょう。\n
今は、ブリーズなのよ？」"

hide eri_m_03a_2
show eri_m_03a_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice eri_g0233
Elliot "「け、けど俺、あんたに返すもの何も……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「いいから行くわよ！」"

hide eri_m_03a_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はエリオットの腕をぐいぐいと引いて彼の部屋を出る。\n
最後、呆然としている部屋の主を振り返った。"


show huryou_d1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0039
Furyou "「え、えっと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「風紀委員会にもそういうことで話通してあるから、心配しなくて大丈夫よ」"

hide huryou_d1_7
show huryou_d1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
Furyou "「！」"

hide huryou_d1_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは物言いたげに頭を抱えていたが、ブラッドが後ろ盾になってくれたおかげで、なんとか協力してもらえることになったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を貸してもらった効果は大きいが、借りが出来た。\n
いずれ、返さなければならないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……だけど、悪くない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これから付き合っていく人達と、この寮。\n
この居場所が、気に入っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼へだって、仕返しがしたかったというよりも、ケリをつけたかっただけ。\n
この場にもう用はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「でも、二回目はないからね？」"

play sound se_0774
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はエリオットの手を引いてその場を後にした。"


show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0040
Furyou "「……怖え女」"

hide huryou_d1_2
show huryou_d1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Furyou "「…………」"

hide huryou_d1_7
show huryou_d1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0041
Furyou "「……さすが、副寮長の女」"

hide huryou_d1_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なぜか、私に逆らうと怖いという噂が広まるのは、後日談。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_2")
T "（……失敬な。\n
怖いことなんか何もしていないのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とはいえ、それはすべて後の話だ。"

with dis
$ hi_mes()

scene bg23_rd_nig with Dissolve(.8)

scene bg25_rr_nig
with stripe_l_medium

scene bg23_rd_nig
with stripe_l_long

play music quiet_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットの部屋は、意外にも一階だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの部屋が三階にあると聞いていたので、エリオットも同じように上階に部屋を持っているのだとばかり思っていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは私を先に部屋へと通してくれる。\n
部屋の造りは、女子寮とそんなに変らないように見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（少し……、広い？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "副寮長の権限ゆえなのだろうか。\n
私の部屋よりも広いように見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大雑把なところがあるように見えるエリオットだが、その部屋の中は驚くほどきちんと整えられていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（階数よりも……、色々と意外）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "壁を向いて備え付けられた机の上には、授業で使うのだと思われる教科書が綺麗にそろえて並べられているし、ベッドも綺麗にメイキングされている。"

play sound se_0399
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後で、ばたんとドアが閉まる音が聞こえたと思った次の瞬間には、ぎゅうと痛いほどの力でエリオットの懐に閉じ込められていた。"


show m_eri6_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の肩口に顔をうずめて、エリオットはひたすらに私を抱きしめている。\n
無心なようにも思えたし、必死になっているようにも思えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0234
Elliot "「ずっと……。\n
あんたに会いたかった……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_2")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「それは、こっちのセリフよ！」"

play sound se_0007
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳元で囁かれた声に、私はエリオットに抱きしめられた腕のうちから、自分の腕を引き抜こうともがく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何はともあれ、この男の耳を引っ張り倒さないことには気がすまない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、どれだけもがもがと身じろいでもエリオットの腕は緩まない。\n
しっかりと抱きすくめられてしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0235
Elliot "「こっちの台詞、って……。\n
……あんたも、俺に会いたいと思ってくれていたのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「そりゃあ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、正直に告げるのも癪だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_8")
T "「……エリオット。\n
まずは、腕を放してくれないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_8")
voice eri_g0236
Elliot "「……やだ。\n
あんた、そしたら耳引っ張るつもりだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（やだ、とか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしてか、こんな大男が可愛く見えてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「当たり前よ！\n
いきなり忘れろとかいって勝手に離れて……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「それでいて、会いたかったですって！？\n
どの口がそれを言うのよ！」"

play sound se_0062
pause .3
play sound se_0062
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悔しいので、足をげしげしと踏みつけてやる。\n
が、それでもちっともその腕は緩まない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひたすらに、ただただ、私を抱きしめている。\n
そのうち、私のほうがすっかりくたびれてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの気持ちも分かる。\n
エリオットには、逆らっても無駄だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "敵意ならともかく、押し付けであっても、人は好意に勝てない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふてくされた気分でおとなしくしていれば、包み込むように抱くエリオットの体温が制服越しにじわじわと伝わってきて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだかそのぬくもりに急に涙腺が緩みそうになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（どれだけ好きなのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分で自分につっこみをいれる。\n
どれだけの深みにはまってしまったというのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさしく、私は穴に落ちたらしい。\n
制御がきかず、止まらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好意に、負ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0237
Elliot "「……俺さ。\n
馬鹿だから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……知っているわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice eri_g0238
Elliot "「あんたみたいなお嬢さん、俺みたいな不良に付き合わせちゃいけねえって思ったんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice eri_g0238_5
Elliot "「ストームの夜みたいに、危ねえめにあわせちまうかもしれねえから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……知っている」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、私のために身を退こうとしたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のために。\n
私のことなんて、考えずに。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0239
Elliot "「俺は帽子屋寮のＮｏ．２で、恨みを買うことも多い。\n
そんな俺の傍らに、あんたみたいなお嬢さんは置いとけねえって」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……それも、知っているわよ」"

hide m_eri6_4
show m_eri6_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の腰裏を抱いていたエリオットの片腕が持ち上がって、私の後頭部にくしゃりと差し込まれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無骨な手のひらは、私の頭をそのまま包みこめてしまいそうなぐらいに大きい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（ウサギのくせに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_3")
voice eri_g0240
Elliot "「だから、我慢しようと思ったんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……知っているんだってば」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_9")
voice eri_g0241
Elliot "「だけど……、少しの間だぜ？\n
解決したら……、いや、解決させるつもりで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（……嘘も下手）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "絶対に、距離をあけたら、あけたまま。\n
引いてしまっていただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは本当に馬鹿だ。\n
私のことを考えつつ、私の気持ちを考えていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0242
Elliot "「……窓ガラスを割った奴を捕まえたら、あんたに会いに行こうと思ってた」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……うん」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice eri_g0243
Elliot "「でも、俺のことを恨んでいる奴、って考えたら。\n
もう誰が誰だか分からないぐらい数が多くて、自分でびびった」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……そんなに恨まれているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice eri_g0244
Elliot "「ルール違反者に、罰を与えるのも俺の仕事だからな。\n
たまに違反してない奴にも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice eri_g0245
Elliot "「……恨まれもする。\n
あんま、いい奴じゃねえからさ、俺」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、主にはブラッドの代理として働き、ブラッドの決めたルールに逆らう人間を処罰する。\n
そしてブラッドの代わりに恨まれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「泥を被っているとは思わないの？」"

hide m_eri6_5
show m_eri6_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自由にならない腕の、肘から下をそろりと持ち上げて、エリオットの背中へと腕を回した。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0246
Elliot "「ブラッドのためなら喜んで被る。\n
俺はそのためにいるんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0247
Elliot "「でも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朗々とはっきりと、誇らしげに迷いなく泥を被ると言い切ったエリオットの口調が揺れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0248
Elliot "「あんたにまで、その泥が跳ねるのは嫌だと思ったんだ。\n
怪我をさせちまうのだって、絶対に嫌だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知っている。\n
身内には甘い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（こういう人だって……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……ねえ。\n
私の気持ちを知っているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のほうは、守られることを望んだ覚えはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0249
Elliot "「あんたは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……私は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice eri_g0250
Elliot "「俺を……、好き……。\n
……なのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……なんで、疑問形なのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice eri_g0251
Elliot "「や……。\n
だってさ……、なんか自信ねえし……、時間があくと余計に……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_14")
T "「時間なんて無意味よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか、違和感を感じて、言葉を止める。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「いえ、完全に無意味とは言わないけど。\n
でも、確固たるものがあるなら、時間なんて関係ないでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（あのとき、確認しあった……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "絆が、出来たと思った。\n
あれは、確固たるもののはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0252
Elliot "「……はあ。\n
あんた、自分から泥に突っ込んでくるんだもんな～……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「そうよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は勝ち誇ったように笑ってやった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくらエリオットがお馬鹿なウサギさんでも、男子寮の窓ガラスをぶち割って特攻してくる女を「お嬢さん」とは思えないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_4")
T "「私、お嬢さんなんかじゃないの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「あなたを困らせてやろうと画策したり。\n
仕返しだって、自分でやるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（姉さんのような淑女になんかなれない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうならなくてもいい。\n
私は私で、そんな私を好きになってくれる相手だっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「だって、私、あなたが好きなんだもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（もがくわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "みっともなくても、相手に直接、ラブレターを押し付ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0253
Elliot "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_1")
T "「あなたを困らせても」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_1")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_1")
voice eri_g0254
Elliot "「あんたにだったら……、いくらでも困らさられてもいい。\n
……ブラッドにぶちのめされても、かまわねえよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……ふふ。\n
あれ、ブラッド引いていたわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮の規律と恋情との狭間で苦しむエリオットが見てみたい、とのブラッドの（趣味の悪い）リクエストだったわけだが、エリオットの忠誠心に歪みはなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さく笑うと、エリオットも笑ったようだった。\n
吐息が首筋にくすぐったい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0255
Elliot "「あんたも、悪い女だな\n
俺と同じで……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ようやく、抱きしめる腕が緩む。\n
少し距離を作って、エリオットが私の顔を覗き込んでくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪戯っぽい色を浮べた双眸に、私も笑う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ええ、そう。\n
私も、素行不良で……っ」"


play music starlit_sky_a_wam
hide m_eri6_6
show m_eri6_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後まで言うより先に、唇を塞がれた。\n
熱っぽいキスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "離れていた時間を、一息に埋めてしまおうとするかのような、そんな口付けだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（離れたのはあなたのほうなのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "近付くのも、エリオットだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_10")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_10")
voice eri_g0256
Elliot "「ん……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_8")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、欲しいのは、私も。\n
恋が落ちるものならば、一人でなんて落ちてやらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "引きずり込んで、一緒にどこまでも落ちていきたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のほうから積極的にキスを仕掛ければ、微かに怯んだようにエリオットが吐息を逃すのが分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「……ふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……渡せた）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの日、渡せなかった手紙。\n
何度も思い出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、これからはラブレターを押し付ける感覚がそれを上書きしていくのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（これから……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たくさん、渡す。\n
一通ではなく、何通でも。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "山のように。\n
いろんな種類を。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……んっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな気持ちは私の吐息にも滲んだのか、倍返しされて息があっけなく上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "息が苦しくて、体に力が入らない。\n
それなのに、頭はふわふわと浮かれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_8")
T "「……っは」"

play sound se_0327 volume .6
hide m_eri6_7
show m_eri6_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くたくたと力の抜けかけた膝を、エリオットの腕がひょいと掬って抱き上げられた。当たり前のようにベッドへと運搬されて、再びキスが落とされる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どれだけ交わしても足りないし、飽きない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……好きよ、エリオット。\n
あなたは？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（ウサギさん。\n
一緒に、穴に落ちてくれる？）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice eri_g0257
Elliot "「なんでも知っていて賢いのに……、そんなことも知らないのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はもう、弱気な顔をしていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「……いいえ。\n
知っているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、強気に受けて立つ。"

with dis
$ hi_mes()
hide m_eri6_8


scene bg23_rd_nig with Dissolve(.8)

scene bg_par15_rg_ros_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_elliot_end
