
scene bg25_rr_day
with dis
label gakuen_blood1:
$ clockanim()


play music corridor_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帽子屋寮の男女共同区域を探索してみることにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（気になっている場所があるのよね）"


scene bg_par15_rg_hat_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、いつも寮を出るとき、もしくは戻ってくる際にちらりと見えるテラスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "蔓薔薇らしき植物がフェンスを彩り、その奥には白いティーテーブルが見え隠れしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "休日の昼下がりなど、あのテラスでお茶をしたらきっと気持ちがいい。\n
帽子屋寮の庭を見下ろすことのできるあの位置は、特等席だ。"


scene bg25_rr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（行ってみよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "テラスに繋がっているであろう階を目指し、歩きだした。"

with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.5)

scene bg06_sk_h_day
with stripe_l_medium

scene bg06_sk_h_eve with Dissolve(1)

scene bg25_rr_eve
with stripe_l_long

play music corridor_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく寮内を歩きまわると、テラスへと続くドアを見つけることが出来た。\n
共有部分の二階から、出ることが出来るようになっている。"

play sound se_0199

play music hatter_garden_p_ali

scene bg_par12_hct_eve
with stripe_l_medium
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアを押し開けて外に出る。"

play sound se_0141 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さあっ、と吹き抜けた風が思うよりも強くて、乱れる髪を片手で押さえた。\n
そして、そんな風の向こう側に……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あれ……？」"


show bra_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0087
Blood "「おや……、悪党の巣窟に、勇敢なお嬢さんが単身で乗り込んできたようだな。\n
……誰も忠告してはくれなかったのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「あなたは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッド＝デュプレだ。\n
同じ寮とはいえ、普段はほとんど見かけることのない、寮の責任者。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮長という表現も当てはまらない気がする。\n
そういう、親近感を感じない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見回りや、使用人達との連携といったこともほとんどエリオットがしているようだし、雑務をしている様子は無い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校内で率先して騒ぎを起こしているのはもっぱら双子（よくそこにエリオットもいたりする）。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なので、ならず者のボスといわれる割に、ずいぶんと存在感のないトップだと思っていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（こんなところで、のんびりとお茶を啜っていたなんて……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "洒落た造りのティーテーブルの上には、ティーコジーのかかったポットと、湯気を立てるティーカップが一つ、そして幾つかの茶菓子が並べてある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、本人は茶菓子に口をつける気はないのか、彼の前には紅茶だけが置かれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ごめんなさい、知らなかったわ。\n
散策していて迷いこんでしまっただけなの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の口ぶりは回りくどく、からかうようなものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それはつまり、在学している寮生の間には、ここには立ち入ってはいけないという不文律があるということなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おとなしく謝罪して、立ち去ろうとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッド＝デュプレは、この寮のトップで、いわゆる権力者。\n
不用意なことをして刺激したくないし、あまり近付きたいとも思わない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、シンフォニアにおける、ならず者。\n
どこの学校にもいる、素行不良の生徒を束ねる男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世界が違う。\n
近くても遠い、違った世界に住んでいてもらいたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はこの寮を選びはしたが、不良の仲間入りがしたいわけではない。\n
だが、室内に戻りかけた私を引きとめたのはその彼だった。"

hide bra_m_01_2
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0088
Blood "「待ちなさい。\n
せっかく来たのだから、茶の一杯でも飲んでいくといい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「で、でも……。\n
ここ、一般の生徒は立ち入り禁止なんでしょう？」"

hide bra_m_03_15
show bra_m_03_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice blo_g0089
Blood "「いいや？\n
私は別に、禁止した覚えはないぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え、だって……」"

hide bra_m_03_16
show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0090
Blood "「本当に私が禁止していたならば、お嬢さん、そもそも君がここに入れることはなかった」"

hide bra_m_02_2
show bra_m_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0090_5
Blood "「ここに君が入れたこと自体が、私が禁止していない証だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唇をくっと吊り上げる笑みと共に、さらりと言われた。\n
その中に、聞き流してはいけない内容が含まれていたような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（しようと思えば出来る、ってこと？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "命令も、それに従わせることも。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "穏やかにティーカップを傾け、彼の手下ほど派手に問題を起こしているわけではない彼。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、その中でも危険な男なのだと改めて思い知らされる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（下手に逆らってもマズイ……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（……どうしよう）"

menu:
    "ご馳走になる。":
        jump gakuen_blood1_2a
    "断る。":
        jump gakuen_blood1_2b
label gakuen_blood1_2a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……それじゃあ、せっかくだし、一杯いただくわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（一杯だけよ、一杯だけ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それ以上の時間をここで過ごすつもりはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "断れないから、一杯だけ付き合う。\n
ただそれだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうやって自分に言い聞かせていないと、彼のペースに飲み込まれてしまいそうな気がして怖い。"

jump gakuen_blood1_3
label gakuen_blood1_2b:
$ lovechara_blood_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「せっかくだけど……」"

hide bra_m_02_15
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice blo_g0091
Blood "「さあ、お嬢さん、席へどうぞ。\n
それとも私が立つまで、座らない気か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女性が立っている間は、同席している男性も立たなければならないというのは古いマナーだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "マナーに乗っ取れば招かれてくれるのかと尋ねるようでありながら……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "（立ち上がったら力づくででも席につかせるが構わないか）と脅しを含んでいるようにも聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……考え過ぎだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "断る言葉を口にするより先に、言い切られた内容に口を噤んでしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……逃げられそうにない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからといって素直に席につく気にもなれない。"

jump gakuen_blood1_3
label gakuen_blood1_3:
hide bra_m_03_4
show bra_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0092
Blood "「……ふ。\n
君は、聞き分けが悪い」"

hide bra_m_03_3
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0093
Blood "「……さあ、お嬢さん。\n
遠慮なく座ってくれ」"

play sound se_0161
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が躊躇っている間にも、彼の促す声で椅子が一人でに動く。\n
それは、まるで見えない誰かが椅子を引いたかのようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "応じるようにして、渋々と茶会の席についた。"

hide bra_m_03_10
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0094
Blood "「茶会は夜に限る、と思っていたが……。\n
君のようなお客さんが飛び込んでくるのなら、夕方の茶会も悪くはない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……普通、お茶会は昼でしょうに）"

hide bra_m_03_4
show bra_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice blo_g0095
Blood "「さて……」"

play sound se_0468
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は上機嫌に口元を緩めながら、ぱちんと指を鳴らした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ」"

play sound se_0176
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の目の前に、ティーカップが現れた。\n
最初からそこにあったかのように、自然に。"

play sound se_0544
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "続いて、指揮でもするように指先を彼が揺らせば、すでにサーブされていたティーポットがふわりと宙に浮く。"

play sound se_0175
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま、目の前にあったカップへと紅茶を注いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当たり前のように魔法を使ってみせるのが、いかにもシンフォニア流といった感じだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……？）"

play sound se_0785 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふわり、と紅茶のいい匂いが鼻先を掠める。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_11")
T "（花の匂い……？）"

play sound se_0546
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "フレーバーティーなのだろうか。\n
甘く、濃厚な花の香りのようなものが紅茶の香りの中に混じっている。"

hide bra_m_01_2
show bra_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0096
Blood "「私の手下は残念ながら、紅茶の味も分からん朴念仁ばかりでな。\n
せっかくうまい茶葉を手に入れても、馳走のし甲斐がないときた」"

hide bra_m_01_8
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0097
Blood "「お嬢さん、君なら分かってくれるだろう？\n
さあ、どうぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "白いティーカップの中に揺れる液体は、透き通った赤味の強いブラウンだ。\n
ちょうど、夕日の色にとてもよく似ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "テーブルの上には、砂糖やミルクは置かれていなかった。\n
ブラッド＝デュプレはストレートで飲むのがお好みらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（さっさと飲んでしまって、帰ろう）"

play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……いただきます」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ティーカップをそっと持ち上げ、口元に運んだ。\n
近くなると、よりその香りも強くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いい匂いだ。\n
今までにあまり嗅いだことのない香り。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "特別なブレンドの紅茶なのだろうか。\n
ひとしきり匂いを堪能してから、カップの縁へと口付けた。"

play sound se_0379
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「美味しい……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "濃厚な花の香りとは裏腹に、味わいはあっさりとしている。\n
口の中に、味、というよりも華やかな香りが広がっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も実家ではよく紅茶を飲んでいたが、こんな紅茶は初めてだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薔薇のような香りがするのに、安物のフレーバーティーにありがちな付け足した感がない。"

hide bra_m_03_15
show bra_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0098
Blood "「ふふ、味の分かる客人を招けて、私も嬉しいよ。\n
……気に入ってくれたか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「ええ、とっても美味しいわ。\n
これ、なんていう種類の茶葉なの？」"

hide bra_m_02_4
show bra_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice blo_g0099
Blood "「なんだと思う？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……何かしら。\n
花の匂いがするから、何かのフレーバーティーだとは思うんだけど……」"

hide bra_m_02_5
show bra_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice blo_g0100
Blood "「ふふ。\n
それはキーマンのストレートだよ、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え、うそ……！？」"

hide bra_m_03_1
show bra_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice blo_g0101
Blood "「嘘なものか。\n
その紅茶は正真正銘のキーマンだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「キーマンって……、もっと煙っぽい味がしたと思っていたんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「スモーキーフレーバーが売りじゃなかったかしら？」"

hide bra_m_03_5
show bra_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0102
Blood "「……それは嘆かわしい誤解だな、お嬢さん。本来のキーマンとは、独特の強い花の香りを持つ味わいのあっさりとした茶葉なんだ」"

hide bra_m_03_13
show bra_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0103
Blood "「だが、残念なことに本来必要な工程を省いた粗悪なキーマンが出回っているのも事実でな。\n
煙臭いのはそういう紛い物だ」"

hide bra_m_02_13
show bra_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0104
Blood "「まったく……、そんな輩こそ燻製にされてしまえばいいものを……。\n
茶葉を冒涜する者は、皆死んでしまえばいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後半物騒な言葉をしみじみと、だが本気の声で呟かれる。\n
今なら、紅茶のうんちくと共に飲み込んでしまえそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「へえ……、そうなのね。\n
ああ、でも、これ本当に美味しいわ」"

hide bra_m_02_3
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice blo_g0105
Blood "「だろう？ミルクティーにしても、また美味いとは聞くが……。\n
私自身は紅茶に混ぜ物をするのは、邪道だと思っている」"

hide bra_m_03_15
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice blo_g0106
Blood "「うまい茶葉はストレートで、その真価を問われる……」"

hide bra_m_03_2
show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice blo_g0106_5
Blood "「隠し事が通じないからこそ、この素晴らしい香りを純粋に楽しめると思わないか、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「ええ、本当に……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、ふわりと湯気をともなって立ち上る花の香りに、うっとりと目を細める。"

hide bra_m_02_2
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0107
Blood "「君は話と紅茶の味が分かる、素敵なお嬢さんだな。\n
……もう一杯どうだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「いただくわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "差し出したカップの中に、ブラッド＝デュプレが注ぐ鮮やかな夕日色が満ちていく……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……んん？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこで、はたと我に返った。\n
何をのほほんと、ブラッド＝デュプレと紅茶について語り合っているのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さっさと出された一杯を飲み干して、帰ろうと思っていたはずなのに。\n
お代わりまでしてしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "新しく満たされた紅茶に口をつけながら、向かいに座る男の様子を伺った。\n
切れ長の双眸を伏せがちにして、紅茶の芳香を堪能しているようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶のことに関する饒舌さからして、本当に紅茶のことが好きなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その物腰は優雅で、ちっとも本人が言うような……、そして周囲が認めるような「ならず者」というふうには見えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "優雅で、穏やかにも見える。\n
誰か知っている人に似ているような気がしてちくりと胸が痛んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（……誰、だっけ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "苦味が喉までこみ上げているというのに、その正体が思い出せない。"

hide bra_m_02_8
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0108
Blood "「どうした、お嬢さん。\n
そんなに熱い眼差しを向けられていると、気になってしまうんだが」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……誤解だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、見つめてしまっていたのは事実だ。\n
誤魔化すように、言葉を続けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ねえ。\n
あなた帽子屋寮の寮長で……、言葉は悪いけど、シンフォニアのならず者を束ねているのよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、この人自身が「ならず者」らしい。"

hide bra_m_03_4
show bra_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0109
Blood "「ああ、そうだが。\n
それがどうかしたか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「この状況って、どうなの？\n
私、新入生よ？」"

hide bra_m_03_5
show bra_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice blo_g0110
Blood "「それは知っているが……。\n
何か問題が？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「新入生の女子生徒に、寮長自ら紅茶を振る舞って、更にはこんな口の利き方まで許して。\n
それでも問題ないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（私が言うことでもない気がするけど……）"

hide bra_m_01_4
show bra_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice blo_g0111
Blood "「さて……、特に問題があるようには感じないが。\n
紅茶の味の分かるお嬢さんに、茶会に付き合ってもらっているだけだ」"

hide bra_m_01_2
show bra_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice blo_g0112
Blood "「それに、先ほども言ったが……。\n
私は、私が望まないことを許すほど寛容な男ではないよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……それじゃあ、この状況をあなたは望んでいるということ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう聞いてやろうと思うのに、さすがにそこまで厚顔にはなりきれなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮長を務め、厄介者のトップに立つという彼にむかって、私と仲良くなりたいのかなんて聞けない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この気紛れそうな男は、一体何のつもりがあって、私にこんなことを許しているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もの言いたげな視線を感じてはいるだろうに、彼はそしらぬ顔で紅茶を楽しんでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手にされていない以上、どうしようもないので、私も再びティーカップを口に運ぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "甘い花の香りが、本当に鮮やかだ。"

play sound se_0785 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（……美味しい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前の厄介ごとを帳消しにするほどの満足感だ。"

hide bra_m_01_1
show bra_m_03_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

hide bra_m_03_18
show bra_m_03_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0113
Blood "「ところで、お嬢さん。\n
君は、私の名前を知っているか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく互いに紅茶を楽しむ沈黙が続いた中で、ふとブラッド＝デュプレが口を開いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……知っているわよ。\n
ブラッド＝デュプレ、でしょう？」"

hide bra_m_03_16
show bra_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0114
Blood "「ああ、よかった、知っていたのか。\n
……先ほどから君は、私のことをちっとも名前で呼ぼうとしないからな」"

hide bra_m_03_13
show bra_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0115
Blood "「忘れられてしまったかと思ったんだ。\n
そうじゃなかったようで何よりだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……知っているのなら、呼べとでも？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……あなただって、私のことを名前で呼ばないわ。\n
忘れているんでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たくさんいる新入生のうちの一人だ。\n
私にとって、彼は一人しかいない寮長だが、彼にとっての私はその他大勢にすぎない。"

hide bra_m_02_5
show bra_m_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「……[firstname]。\n
[firstname]＝[familyname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の口から名前を呼ばれて、驚いた。\n
しかも、フルネームだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさか、覚えているとは思わなかった。"

hide bra_m_02_15
show bra_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0116
Blood "「ちゃんと覚えているとも。\n
私は記憶力には自信があってね、[firstname]」"

hide bra_m_02_4
show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0117
Blood "「君は、新入生の中でも変り種だからな。\n
君が思う以上に、知られている」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（何よ、それ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「人を希少動物みたいに言わないでちょうだい」"

hide bra_m_02_2
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice blo_g0118
Blood "「ふふ、事実、外部の学校からこちらに進学してくる生徒は珍しい。\n
君は外の世界を知る稀有な生徒だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「……大袈裟だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアは寮制で、ペーターも言っていた通りなかなか外出許可というのがおりないものらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "出ても、近くの街までの日帰り、数時間程度の外出許可なのだそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはもしかすると……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "若くして強大な力を知識として授けられる生徒達が、メンタル面でもきちんと成長するまでは外に出せない、出さない、ということなのではないか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを考えていたところで、彼の声に意識を引き戻された。"

hide bra_m_03_4
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0119
Blood "「私がこうして、君の名を呼んだんだ。\n
君も私を呼んでくれるべきだとは思わないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……私のこと、からかっているのね」"

hide bra_m_03_15
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice blo_g0120
Blood "「ふふ。\n
お嬢さんをからかうなんてこと、私がするわけないだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（その割には、とてもとても楽しそうよ、あなた）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にやにやと笑いながら、ティーカップを傾ける男は意地悪そうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に名前を呼ばれたい、というよりも、新入生に寮長である自分の名を呼んでみろ、と無茶をふっかけて楽しんでいるだけにしか見えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が躊躇えば躊躇うほどに、最終的に言わせる楽しみが増す。"

menu:
    "呼ぶ。":
        jump gakuen_blood1_4a
    "呼ばない。":
        jump gakuen_blood1_4b
label gakuen_blood1_4a:
$ lovechara_blood_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（楽しませてやる気なんか、ないわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、なんでもないように紅茶のカップを持ち上げてその中身を飲み干した。\n
口の中に広がる甘い花の香りに勇気づけられる気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それから、真っ直ぐに彼へと視線を向けて、口を開いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「ご馳走さま、ブラッド。\n
私、そろそろ食堂に向かうことにするわ」"

hide bra_m_02_8
show bra_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッド、と。\n
何気なく聞こえるように、それだけに心を配って発音した名前。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、意外に思ってしまうほど唇に馴染んだ。\n
まるで呼び慣れた名前のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かちゃり、と小さな音をたててティーカップをソーサーへと戻す。"

hide bra_m_02_1
show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0121
Blood "「お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "立ち上がって背を向けかけたところで、呼びかけられて振り返った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「……何？」"

hide bra_m_02_2
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice blo_g0122
Blood "「明日も、茶会につきあってくれ。\n
また別の種類のうまい茶を用意しよう」"

jump gakuen_blood1_5
label gakuen_blood1_4b:
$ lovechara_blood_points =+ 2
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……癪だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼んでも、呼ばなくても、この男はどっちにしろ面白がるに決まっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、なんでもないように紅茶のカップを持ち上げてその中身を飲み干した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、口の中に広がる甘い花の香りを存分に楽しんでから、カップをソーサーへと戻した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「ご馳走さま。\n
私、そろそろ食堂に向かうことにするわ」"

hide bra_m_02_8
show bra_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice blo_g0123
Blood "「…………。\n
……意地っぱりだな、名前を呼んではくれないのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_1")
T "「そのうち、気が向いたらね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざと、そっけなく響くように言う。\n
この男の名前を呼ぶことに躊躇っているなどと、見透かされたくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "立ち上がって、背を向けかけたところで呼びかけられて振り返った。"

hide bra_m_02_13
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0124
Blood "「では、明日もまた君を茶会に誘うとしよう。\n
君が私を名前で呼ぶまで、何度でも」"

hide bra_m_02_8
show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0125
Blood "「私の茶会に招かれてくれるだろう？\n
断りはしないだろうな、お嬢さん」"

jump gakuen_blood1_5
label gakuen_blood1_5:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "関わらないほうがいい、危険な男、だと。\n
そう思っていたはずなのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、だからこそ、断れないのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……ええ。\n
楽しみにしているわ」"

hide bra_m_02_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はそう言って、テラスを後にした。\n
言葉通り、次回に期待しつつ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（紅茶が美味しかったから……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とても、美味しかったから。"

with dis
$ hi_mes()

scene bg_par15_rg_hat_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_medium

scene bg_map_nig with Dissolve(1.2)
##endmemory
$ routechara = "Blood"
jump gakuen_friend_check_hatter
