label gakuen_ace3:
scene bg_map_day
with dis

$ clockanim()


scene bg10_sb_day
with dis


scene bg27_rk_day
with dis


play music daytime_a_wam

scene bg06_sk_h_day with Dissolve(1.2)
with dis

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法生物を食べてしまった。\n
字面を見ると、相当に恐ろしい事件だ。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの後、知らずその片棒を担がされてしまったユリウスの協力もあって、事のあらましを闇に葬ることに成功したらしい。"


with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（そりゃあ、そうだろうなあ）"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスとしても、さすがに「食べちゃいました」とは報告できないだろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唯一の救いとしては、エースが綺麗に捌いたおかげで（それはもう綺麗に）、ある意味証拠隠滅は完璧だったことだろう。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなわけで、せっかくの珍しい魔法生物は飼育担当の生徒のミスにより逃亡、その後学園内で消息不明という形で処理されることになった。"


scene bg06_sk_h_day_s
with dis

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0008
Kyouzyu "「まあ、前向きに考えよう。\n
これで、学園内で野生化して増えたら面白い」"


scene bg06_sk_h_day
with dis

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シュトレーゼ教授の、今回の失踪事件についての感想はこんなものであったらしい。\n
諦め半分、ポジティブな発想だ。"


with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……でも、それは期待できそうにないです、先生）"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "四枚羽の珍しい魔法生物は、四本の手羽先に化けてしまった。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは罪悪感からくる胃痛で、しばらくナイトメアの元に通うことになった。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、エースのほうはちっとも懲りていないらしく、それからも度々野営を行っているのを道の傍で見かけるようになった。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前に一度、寮の中でテントが張ってあるのを見たときには眩暈を覚えたほどだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（寮がゴールじゃないのね……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼にとって、寮の中は第二ステージであるらしい。\n
廊下で堂々と焚き火を用いて煮炊きしている姿には、いっそ感動すら覚えた。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（この人って、罪悪感とかないのかしら）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食べたのだから、あの一件に関しては私だって同罪。\n
他人面をするつもりはない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それにしたって、エースのほうが罪が重い。\n
飄々としすぎだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして今、私の目の前。"


scene bg27_rk_day
with dis

play sound se_0229

show ace_m_03_10 at center




with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にこにこと爽やかな笑顔を浮かべたエースが立ちはだかっている。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、頭一つ分以上背が高い。\n
こうして目の前で待ち受けられると、まさしく立ちはだかるといった感じだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……何か御用かしら？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業を終えての帰り道、校舎の廊下でのこと\n "



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼がこうして校舎内にいるのが珍しいのか、通りすがる生徒達が時折ちらちらと振り返っていく。"

hide ace_m_03_10
show ace_m_02_8 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0203
Ace "「酷いなあ～。\n
友達なんだから、俺が君に会いに来たっておかしくないだろ？」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……そうね、友達なら。\n
いつ、私とあなたが友達になったのか不明だけどね」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "友達になるのに、互いの認識だとか許可がいるとは、私だって思わない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、こんなふうにまるで友達であることを免罪符に、何か厄介ごとに巻き込まれそうな気配がひしひしと伝わってくる場合には話が別だ。"

hide ace_m_02_8
show ace_m_03_11 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0204
Ace "「またまたすっとぼけて～。\n
一緒に鳥を捌いて食べた仲じゃないか！」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……どんな仲」"

hide ace_m_03_11
show ace_m_03_3 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice ace_g0205
Ace "「同じ釜の飯を食べたんだ。\n
友達だろ？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にっこり。\n
爽やかに、私と彼が友達であるという事実を主張される。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抵抗しても無駄だろう。\n
彼の押しには敵わない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際、友達というのは間違っていない。\n
あれからも、交流はあったのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……でも、否定したくなるのよね、どうしてか）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはきっと、彼が私を平気でトラブルに巻き込むからなのだろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にこやかに友達だと言われても、どうでもいい扱いをされているように思えてしまう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、人にとって友情の形など千差万別。\n
エースにはエースの、私には私の友情の形がある。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（前向きに捉えれば、だけど）"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_1")
T "「……分かったわ。\n
友達であるのは認めるから、用件を言ってちょうだい」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_16")
T "「方向音痴のあなたがこうして私を迎えにきているなんて、何か用事があるんでしょう？\n
……早く聞かないと、心臓に悪いわ」"

hide ace_m_03_3
show ace_m_01_3 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_16")
voice ace_g0206
Ace "「へえ、よく分かったね。\n
さすが、友達」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「そうね。\n
友達でなくても分かりそうなものだけど」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は両手を腰にあてて、促す。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "徒歩五分の距離で迷う男が、わざわざ私の通るであろう場所まで辿り着き、待ち構えているのだ。\n
何か用件があると見るのが当然だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっと、ろくでもないこと。\n
予感はきっと当たっている。"

hide ace_m_01_3
show ace_m_01_8 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0207
Ace "「せっかちだなあ、もうちょっと段取りというものを楽しもうよ。\n
まあ、いいけどさ」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースはいかにも好青年といった顔で、眉尻を下げてみせる。\n
そうしてひょいと肩を竦めると、にこやかに言い切った。"

hide ace_m_01_8
show ace_m_03_11 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0208
Ace "「俺と、付き合ってくれないか？」"

play sound se_0077 volume .7


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ざわざわっと、周囲がどよめく。\n
聞き耳を立てていた者も少なくなかったのだろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（…………）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なるほど。\n
エースが言うように、確かに段取りというのは大事だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今その重要性をおおいに思い知らされた。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一拍おいて、深呼吸する。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それから、エースを正面から睨み付けた。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「段取りはどこへ行ったのよ？」"

hide ace_m_03_11
show ace_m_02_4 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice ace_g0209
Ace "「君に倣って、急いでみたんだ。\n
段取りなんて、すっ飛ばすに越したことはないよね」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「あなたは、いつも色んなものをすっ飛ばすわよね」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "短い付き合いでも、すでに旧知の仲のようによく分かる。\n
彼はある意味分かりやすく、同時に難解な人でもある。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（誤解を広めるばかりで収束させようとしない人……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲は未だざわめいている。\n
ここで誤解を解いておかなければ、とんでもない噂が広まってしまいかねない。"

menu:
    "慌てて否定する。":
        jump gakuen_ace3_2a
    "もう一度、深呼吸する。":
        jump gakuen_ace3_2b
label gakuen_ace3_2a:
$ lovechara_ace_points =+ 1


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……いきなり、何を考えて、そんなこと言い出すのよ？」"

hide ace_m_02_4
show ace_m_03_2 at center

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0210
Ace "「思い立ったが吉日って言うだろ？\n
あれ？君、顔赤くなってるよ？」"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「そりゃあ、赤くもなるわよっ！\n
こんな場所でそんなことを言われたら！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは授業が終わった後の生徒が出入りに使う、校舎のエントランスに程近い。\n
しかも、今はまさに授業が終わる時間帯で、タイミングも最悪だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "クラブ活動や部活動に赴く生徒や、寮へと帰る生徒で混み合っている。\n
周囲から好奇の視線を向けられているのが、肌で感じられた。"

play sound se_0560
hide ace_m_03_2
show boy_c1_4 at center

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0001
Seito "「赤薔薇寮のエースさんが新入生に告白？」"

hide boy_c1_4
show boy_c1_4 at left


show girl_c2_4 at right

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0001
Seito "「え、本当？\n
決定的瞬間を逃しちゃった！」"

hide girl_c2_4
show girl_c2_4 at left



show girl_f1_7 at right


hide boy_c1_4



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0014
Seito "「誰か、記録のマジックアイテム持っていなかったの！？」"

hide girl_f1_7
show girl_f1_7 at left



show boy_c1_2 at right

hide girl_c2_4


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0002
Seito "「この前の授業で使ったやつなら……」"

hide boy_c1_2
show boy_c1_2 at left


show boy_d1_5 at right

hide girl_f1_7


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0009
Seito "「今から出しても、遅いだろ……」"

hide boy_c1_2

hide boy_d1_5


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここで、エースを連れて、ひとけのないところへと逃げ込むのは簡単だ。\n
だが、そうなると、根も葉もない噂が明日には学園中に蔓延してしまうだろう。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "防ぐためには、この場ではっきりさせる必要がある。"

jump gakuen_ace3_3
label gakuen_ace3_2b:

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（動揺したら負けよ、動揺したら……）"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頬の一つでも赤らめてしまったら、負けが確定する。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これは、会話上での誤解だ。\n
冷静に対処しなければ。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……何のつもり？」"


show ace_m_03_2 at center


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice ace_g0211
Ace "「何って、付き合ってくれって頼んでいるんじゃないか。\n
分かりやすいだろ？」"

jump gakuen_ace3_3
label gakuen_ace3_3:

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_11")
T "「具体的な用件を言いなさいよっ！\n
私に{size=+20}何に{/size}付き合ってほしいの！？」"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「目的語が抜けているわ。\n
そうでしょう？」"

hide ace_m_03_2


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "多少動揺はしたものの、誤解するほど間抜けではない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースはあれだ、「どこか」もしくは「何か」に付き合ってくれという意味で言ったのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けして、「交際しましょう」という意味の付き合いは求めていない。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（それにしても、なんて傍迷惑な……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誤解をしそうな人達のいる場所で、誤解を招くような言動。\n
紛らわしいにも程がある。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（悪意はないんだろうけど……）"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（…………）"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（ない……、のよね？）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのあたり、自信がなくなってきた。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "爽やかに押しが強く、しっちゃかめっちゃかな男ということは理解している。\n
だが、理解しがたい男だと理解しているだけで、本質はまったく分からないのだ。"

play sound se_0560


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、周囲は理解してくれたらしい。"


show boy_c2_5 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0003
Seito "「あー……。\n
そういうことか、驚いた……」"

hide boy_c2_5
show boy_c2_5 at left



show girl_e1_1 at right




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0002
Seito "「なんだ……。\n
告白劇かと思ったのに……」"

hide boy_c2_5

hide girl_e1_1



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲からも納得したような声が聞こえる。\n
どことなく残念そうな響きが伴っているのに、舌打ちしたい気分になった。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_9")
T "（他人事だと思って……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、私だってこれが他人事だったならば、面白がって成り行きを見守っていただろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、当事者としてはそう面白がってもいられない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな場所で告白劇なんてとんでもないが、エースときたら、いかにもとんでもないことをやりそうなのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「で？私に、何をしてほしいの？\n
具体的に言ってもらえる？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ほとんど誤解は解けつつあるといっても、周囲は未だ好奇心いっぱいという様子。\n
ここはきちんと具体的な内容まで明らかにし徹底した誤解の排除をしておきたい。"


show ace_m_02_2 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0212
Ace "「え？\n
ここで言っていいのか？」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……この男。\n
わざとやっているんじゃないでしょうね？）"

hide ace_m_02_2
show ace_m_02_3 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice ace_g0213
Ace "「やあ、困ったな。\n
さすがの俺も照れるぜ？」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「……っ！\n
さっさと言いなさい！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私や周囲をからかって楽しんでいるとしか思えない。\n
ぴしゃりと怒鳴りつける。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは、やれやれというように息を吐いて……。"

hide ace_m_02_3
show ace_m_03_11 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0214
Ace "「俺のこと、好きになってほしいんだ」"

play sound se_0771 volume .4


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "空気が凍った。"

hide ace_m_03_11
show ace_m_03_3 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0215
Ace "「付き合ってほしいんだよ、俺と。\n
それが、具体的な用件」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！！！\n
こっち来て！！！」"

play sound se_0092
hide ace_m_03_3



with dis
$ hi_mes()

scene bg10_sb_day
with dis
with stripe_l_medium

scene bg13_fr_day
with dis
with stripe_l_long

scene bg06_sk_h_day
with dis

play sound se_0620

play music forest_p_wam


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_9")
T "「～～～～～っ！！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_9")
voice ace_g0216
Ace "「あははは、[firstname]、君、結構積極的だね！\n
こんなひとけのないところに俺を連れ込むなんて……」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「寝ぼけたこと言ってないで事情をちゃんと説明しなさい！\n
ちゃんと……！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずるずるとエースを引きずるようにして、校舎を出た。\n
ここも、因縁の場所だ。"


scene bg13_fr_day
with dis



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮に帰ろうと思っていたわけでなく、ひとけのないところひとけのないところと突き進んでいるうちにここまで来てしまった。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正規の道ではまだ人目がある。\n
それから逃げるために、私はずんずんと繁みの中を突き進む。"

play sound se_0086


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲から人の気配が完全に途絶えた辺りで、ようやく足を止めて向き直った。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……で、どういうことなのよ！」"


show ace_m_03_9 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice ace_g0217
Ace "「どういうことも何も……。\n
俺と付き合ってほしい、って言ったじゃないか」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「そうね。\n
好きになってほしい、とも言ったわね」"

hide ace_m_03_9
show ace_m_02_10 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0218
Ace "「うんうん、言ったね。\n
で、どうかな？」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「どうかな……、って」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "絶句してしまう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースの口ぶりは、愛の告白だとかは無縁の、さらりとしたいつもの調子だ。\n
旅に出ない？一緒に鳥を食べない？と、そんな声音。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あまりのことに、言葉の続きがなかなか出てこない。\n
それでもなんとか、より詳細に彼の意図を聞き出そうと私は口を開きかける。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「本気だとしても、私、あなたのことをよく知らないし……」"

hide ace_m_02_10
show ace_m_03_4 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
Ace "「！！」"

hide ace_m_03_4
show ace_m_01_9 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice ace_g0219
Ace "「しっ、静かに」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言い切るより早く、制された。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か気配を感じ取ったのだろうか。\n
私も、息を殺して周囲の気配をうかがってみる。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"

hide ace_m_01_9
show ace_m_01_5 at center

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
Ace "「…………」"

hide ace_m_01_5


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice bor_g0009
Hatena "「～～～♪」"


with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……鼻歌？）"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふんふふ～ん、と上機嫌に誰かが鼻歌を歌っている。\n
知っている声だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……ボリス？）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな繁みの奥で何をしているのかが気になって、葉を掻き分け、こっそりと覗いてみる。"

play sound se_0183

show bor_m_01_5 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0010
Boris "「おっさかっなさ～ん、おっさかなさ～ん♪♪♪」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスはおそらくは自作であろう歌を口ずさみながら、切り株に座って繁みの中で釣竿をふるっていた。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（四枚羽の鳥のときよりも、大分平和的な光景だけど……）"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……こんなところで釣り？）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "水場はない。\n
ボリスはそんな場所で、一体何を釣ろうとしているのだろうか。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（まさか……、エースとは違う意味で危ない人だったんじゃ……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼との付き合いも、まだ短い。\n
だが、ボリスは少なくともエースよりはまともに見えたのに。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……猫耳以外は）"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_11")
T "「…………」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「……ん？」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "釣竿から伸びる釣り糸の行き先を目で確認して、息を呑んだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "釣り糸は地面に向かって伸びてはいるものの、その先は小さな黒い穴に飲み込まれ、ふっつりと途中で切れてしまっているように見える。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（空間が歪んでいるの？）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その穴がどこに繋がっているのかは、こうして見ている限りでは分からない。\n
くん、っと小さくボリスの手にしていた釣竿が揺れた。"

hide bor_m_01_5
show bor_m_02_3 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0011
Boris "「！\n
きたきたきた～～！！」"

play sound se_0052


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あまり釣りのことには詳しくないが、これがいわゆるアタリがきたという状態なのだろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは今まで座っていた切り株から立ち上がると、興奮した様子で釣り糸を引き上げ始める。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そしてただただ真っ黒だった小さな穴の中から、きらりと光る銀色のものが見えた。\n
……魚の鰭だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスに釣りあげられて、その姿を現そうとしているのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（な……、なんて高度な魔法なの！\n
才能の無駄遣いもいいところ！）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな高度な技を使って、わざわざ釣りとは。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、当たりを引いている状態。\n
私まで握りこぶしで身を乗り出してしまっていた。"

hide bor_m_02_3
show bor_m_02_9 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「～～～～！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "銀色の鱗をきらめかせた魚が黒い穴から姿を現そうとした瞬間。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「！？」"

hide bor_m_02_9


scene bg06_sk_h_day
with dis

play sound se_0439


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぶんっと音が聞こえた。"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0012
Boris "「あ！？\n
あああああああああっ！！！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぷつん、と釣り糸が切断されて、銀色の魚が身をくねらせながら黒い穴の中へと戻っていく。\n
犯人は……、エースだ。"


scene bg13_fr_day
with dis


show ace_m_01_4 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0220
Ace "「あはは、惜しかったね～。\n
結構な大物だったよな、あれ！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつのまに抜いたのか、エースがその手にした抜き身の大剣を一閃して釣り糸を切断したのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分でしておきながら、惜しかったねなんて言いようがわざとらしい。"

hide ace_m_01_4
show ace_m_01_4 at left



show bor_m_01_4 at right




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0013
Boris "「そうだよ、大物だよ……っ！！\n
あんたなあ……っ、ああ～……」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "へたへたとボリスは脱力して地面に座り込んでしまう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あとちょっとというところだったので、無理もない。\n
大きな魚を、釣り上げる寸前に逃がされてしまったのだ。"

hide ace_m_01_4
show ace_m_03_10 at left




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0221
Ace "「いくら猫君でも、駄目だぜ？\n
教材用生簀に空間繋いで魚釣り、なんてさ」"

hide bor_m_01_4
show bor_m_03_6 at right




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0014
Boris "「……一匹ぐらいいいじゃないか。\n
あ～あ、風紀さんに見つかるなんてついてないぜ」"

hide ace_m_03_10
show ace_m_03_9 at left




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0222
Ace "「ついてないのは、俺の専売特許」"

hide ace_m_03_9
show ace_m_02_10 at left




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0223
Ace "「俺だって、君の邪魔がしたくて邪魔やっているわけじゃないんだ。\n
あんないいタイミングで釣り糸を切らなきゃいけないなんて、心が痛いよ」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（……嘘つき）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その顔のどこが、心痛を覚えているというのか。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "傷ついている人間が悲しい顔をしなくてはいけないという決まりはないが、エースの言葉は限りなく空々しい。"

menu:
    "（ボリスも可哀想に……）":
        jump gakuen_ace3_4a
    "（エース、絶対タイミング見計らって出ていったわよね）":
        jump gakuen_ace3_4b
label gakuen_ace3_4a:


with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（ボリスも可哀想に……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "規則破りらしいが、釣り上げとの期待が確信に変わった瞬間に釣り糸を切られるなんて、ショックだろう。\n
がっくりと落ちた肩が哀れだ。"

jump gakuen_ace3_5
label gakuen_ace3_4b:
$ lovechara_ace_points =+ 1


with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（エース、絶対にタイミング見計らって出ていったわよね……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうにもそんな気がしてならない。\n
勘繰りすぎだろうか。"

jump gakuen_ace3_5
label gakuen_ace3_5:
hide bor_m_03_6
show bor_m_01_3 at right




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0015
Boris "「はあ～……。\n
また日を改めて、風紀さんに見つからないように挑戦するよ」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースとやりあうつもりはないのだろう。\n
ボリスはくるくると切れた釣り糸を手繰って竿に巻きつけると、撤退の準備をし始めた。"

play sound se_0121
play sound se_0742 volume .5


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちんと手を叩く音に合わせて、空中にあった黒い穴が弾けるようにして消える。"

hide ace_m_02_10
show ace_m_03_3 at left




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0224
Ace "「それじゃあ、俺もまた、教材管理の担当に空間処理について報告しておくよ！\n
君の悪戯を止めるのも、風紀委員の仕事だしな！」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……ボリスのことは報告しないんだ）"

play sound se_0625
hide ace_m_03_3
show ace_m_03_3 at center


hide bor_m_01_3



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうもエースは、ボリスの悪戯自体を止めるというよりも、その目的の邪魔をすることを楽しんでいる節がある。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風紀委員として、これでいいのだろうか。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通ならば、悪戯をしている生徒を見つけたら反省文なり何なりを書かせ、同じことは二度としないと約束させるものだと思うのだが。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（つくづく、風紀委員らしくない風紀委員よね）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呆れた視線をちらりと隣へと向ける。\n
にこにこといつもと変わらぬ表情で、釣竿を背負って逃走するボリスを見送っている。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "捕まえる気は一切ないようだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……変なの）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんないい加減な風紀委員が相手だというのに、ボリスの対応は素直だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たとえばこれがゴーランドに見つかったのだったら、ボリスはもっとぎゃあぎゃあと抵抗しただろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手がユリウスでも、きっとそうだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、エースを相手には抵抗しなかった。\n
そうしてはいけないと、経験から知っているかのようだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（どうしてなのかしら）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真面目で堅物なユリウスや教師であるゴーランドなどよりも、エースのほうが誤魔化すにしろ、ごねるにしろ与しやすい相手のように思える。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ、ふらふら放浪ばかりしている不良風紀委員なのだ。\n
取り締まるにしても、軽い妨害だけで満足してしまうことが多い。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……私が知らないだけ、なのかしら）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう一度、隣の彼へと視線を向けた。"

hide ace_m_03_3


scene bg06_sk_h_day
with dis



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に好きになってほしいと告白してきた彼について、知らないことが多すぎる。\n
その思惑も、真意も、そして人柄すら掴めない。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（それで、答えを出せって言うのが無茶な話）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知れば、理解できるようになるのだろうか。"



scene bg06_sk_h_eve
with dis


scene bg06_sk_h_nig
with dis


scene bg06_sk_h_day
with dis


scene bg14_fm_day
with dis
with stripe_l_medium

scene bg13_fr_day
with dis
with stripe_l_long

scene bg06_sk_h_day
with dis


play music forest_thick_day_p_wam


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice ace_g0225
Ace "「俺のこと、好き？」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「……嫌い」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice ace_g0226
Ace "「ええ？酷いなあ、[firstname]。\n
どうして？」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……あなたが、私を迷子に巻き込むからよ！」"


scene bg13_fr_day
with dis

play sound se_0623


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ざくざくと二人で森の中を歩いていく。\n
森はひたすらうっそうと茂っているし、周囲からは小さく虫や鳥の声がする。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "のどかだ。\n
エースに強制連行されたのでなければ、森林浴気分を味わえる。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……そうそう森林浴よ、森林浴。\n
怒っちゃいけないわ、まともに相手にしちゃ駄目）"


show ace_m_01_11 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice ace_g0227
Ace "「パトロールに付き合ってもらっているんだよ」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「なんで、私が……！」"

hide ace_m_01_11
show ace_m_03_11 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice ace_g0228
Ace "「前も、猫君の取り締まりを手伝ってくれただろ？\n
君のおかげで現場を押さえることが出来た」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「あれは、取り締まるつもりなんかじゃなくて……！」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（あなたが変なことを言うから、連れ出しただけで……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完全に偶然の出来事だ。\n
それを私の手柄のように言われても困る。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、あれ以来、エースにパトロールとか称してよく連れ出される。\n
私は私で、不本意なことに拒めない。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……好き、とか、簡単に言ってくるし）"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（…………）"

play sound se_0086
hide ace_m_03_11
show ace_m_03_9 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_11")
Ace "「…………」"

play sound se_0086


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……エース？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴたり、と突然エースが足を止めた。\n
私も彼に倣って足を止める。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスのときと違い、今度はすぐにその理由が分かった。\n
私達の歩く先、その繁みの向こうから何か賑やかな空気が伝わってくるのだ。"

play sound se_0229 volume .4


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞かれてはまずい内容なのか、声音は低く抑えられている。\n
何を言っているのかその内容までは聞き取れない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、何人かが集まって話し合っているということだけは分かった。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……怪しい）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逢引する男女などというロマンチックなものではなく、男子生徒数人。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな森の中で、声を潜めて集まらなければいけない理由なんて、きっとろくなものではない。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

hide ace_m_03_9
show ace_m_01_10 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0229
Ace "「……しい」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりとエースを見やれば、エースはよくわかりましたとでも言いたげな表情で、人差し指を口に当ててみせた。"

play sound se_0454


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先日と同じく、まずは様子見ということなのだろう。\n
そっと足音を殺して、じりじりとその声が聞き取れそうな範囲まで接近していく。"

hide ace_m_01_10



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0011
Furyou "「へへ。\n
よく見つからずに、ここまで育ったよな」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0002
Furyou "「先生にばれないように、株を盗むのは大変だったんだぜ？\n
植物園からの植物の持ち出しは、禁止されているし……」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0014
Furyou "「おまえの苦労話は聞き飽きたっての。\n
その分、おまえが多めに儲けを取るってことで話がついているんだろ？」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0003
Furyou "「当然。\n
俺がいなけりゃ、株が手に入らなかったんだからな」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……株？\n
何のこと？）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き取れた会話の内容を総合すると、授業で訪れた植物園から何かを盗み出し、ここでひっそりと栽培していた……、ということのようだが。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らはいったい、何を育てているというのだろう。\n
儲けというからには、高値で取引される植物だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たとえば授業でよく使うことになるマンドラゴラは、育てるのが難しい分、高価になる。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを生徒間で育成し、校内の購買よりも少し安いぐらいの値段で販売したとしたら充分な収入になる……、かもしれない。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（育てるのが難しいし危険だから、手間と報酬が釣り合うかどうかがネックだけど……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、その場合、こんなふうにこそこそとする必要はない。\n
隠れて行うということは、それこそ栽培を禁止されているような……。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（何を……？\n
見えないかしら）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背伸びを試みる。"

play sound se_0116


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "足元から響いた音に、息を呑んだ。\n
落ちていた木の枝を、力いっぱい踏みしめてしまったらしい。"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Furyou "「！」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0012
Furyou "「誰だ！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0004
Furyou "「誰かいるのか！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0015
Furyou "「……ち！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "繁みの向こう側で、がさがさと彼らが身構えるのがわかった。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……うわ。\n
これは……、落ち込む）"


show ace_m_02_4 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_g0230
Ace "「はは。\n
なんていうか……、すっごくお約束って感じだよな」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「う……」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ありがちすぎて笑えない。\n
潜入中に好奇心が過ぎて物音をたてた上、それが原因で発見されるなんていうのはかなりの王道だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（お約束的なピンチ……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本の中で見かけたときには、「馬鹿ねー」なんて思っていたのに、それを自分でしてしまうなんて。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "繁みの向こうからは逡巡が伝わってくる。\n
まだ誤魔化しがきく段階なのかどうか、向こうも考えあぐねているのだろう。"

play sound se_0763


with dis
$ hi_mes()
hide ace_m_02_4


show m_ace3_1 onlayer master

pause .5


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0231
Ace "「はいはーい！逃げないで。\n
風紀委員の登場だぜー、動かないでくれよなっ！」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「い……！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは、誤魔化したり、隠れたりするつもりなど毛頭ないらしい。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朗らかに名乗りをあげて繁みを掻き分けていく、風紀委員。\n
私もその後を追う。"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0013
Furyou "「……っ風紀委員！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0005
Furyou "「し、しかもエースだ！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0016
Furyou "「エースか……！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "繁みの向こうにいた三人の男子生徒は、名乗りをあげたのがエースだったことに対して、かなり動揺したようだった。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ますます、マズイことをやっていたのは確定的。\n
しかし、他の風紀委員だったらまだマシだったとでも言いたげな反応だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……？？？）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先日のボリスに対する対応を見る分には、エースはそんなに厳しいほうとも思えなかっただけに意外な反応だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスなら決して見逃さないボリスの悪さを、エースは笑顔で見逃していた。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ルーズなところもあるようなのに、どうして彼は周囲に風紀委員として認められているのか。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（まただわ）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の彼に対する認識と、周囲のそれにズレがある。\n
彼らはどうしたものかと顔を見合わせ……、それぞれ顎を引いて頷きあった。"

play sound se_0621
hide m_ace3_1


show huryou_a1_2 at center




with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "万が一、人に見つかったらどうするかという点について、予め決めてあったのだろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一人が杖を構えて、私達の前に立ちはだかる。\n
その後ろで残りの二人が証拠隠滅のためにか、木の根元へと駆け寄るのが見えた。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らを取り締まる義務があるわけでもない私が焦る。\n
ここしばらく、エースのパトロールとやらに付き合わされていたせいだろうか。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアに在籍する生徒の数は、決して少なくはない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスや双子、エリオットのようによほど有名な生徒でもなければ、名前と顔を一致させて後から追及することは難しいし……。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何をしていたのかの証拠を始末されてしまっては、尚更だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「エース……！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（私も、何かするべき！？）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無理矢理とはいえ、こうして彼の見回りに同行しているのだ。\n
何か手を打つべきだろうか。"

play sound se_0496

show magic_b onlayer master with Dissolve(1.2)
hide huryou_a1_2
show huryou_a1_9 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Furyou "「…………」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "足止め役であろう青年が、呪文を唱える。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（何の魔法……！？）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "足止め程度の魔法なら、まだいい。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、この場から逃走することにのみに気をとられ、手加減を忘れた攻撃魔法でも使われてしまったら、たまったものではない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せめて何の魔法かがわかれば、打ち消すためのカウンター魔法を用意するのだが……。"



with dis
$ hi_mes()
hide magic_b
show m_ace3_2 onlayer master

hide huryou_a1_9

pause .501


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0232
Ace "「はははっ！\n
いいなあ、そういう往生際の悪さ、俺、嫌いじゃないぜ」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "隣で、エースは楽しそうに笑った。\n
そしてそれと同時に、だんっと勢いよく地を蹴って前へと踏み出す。"

play sound se_0605
hide m_ace3_2
show bg06_sk_h_day onlayer master

play sound se_0062


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0014
Furyou "「……ぐうっ！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼がとった行動は、私が準備していたカウンター魔法なんかよりも、とても単純な解決法だった。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呪文が完成する前に、物理的に黙らせたのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手にしていた長剣の柄の部分を、容赦なく男子生徒の喉に叩き込む。\n
彼の杖のもとに集まり、魔法として発動しかけていた魔力が霧散していった。"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Furyou "「……～～っ」"

play sound se_0292


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "物も言えない様子。\n
男子生徒は、ヒューヒューと喉を鳴らしながら崩れる。"

hide bg06_sk_h_day
show m_ace3_2 onlayer master



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一方エースは、彼には見向きもせず、もうすでに次の獲物へと接近していた。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "木の根元に屈み込み、なにやら証拠隠滅をしようとしていた青年の横腹をその背が浮くほどの強さで蹴り上げる。"

play sound se_0538
camera at hpunch
camera at vpunch


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0006
Furyou "「……っがは！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こちらも魔法が発動する前に、強制的に呪文詠唱を中断された形だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……手馴れている）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "物理的な手段による魔法使いの鎮圧、ということだけにではない。\n
それ以前に、彼は暴力を振るい慣れているようだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうでなければ、こんなにも躊躇いなく行動に出られるわけがない。\n
無知ゆえの手加減のなさとは違う。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次々と上がる低い呻き声に、この場から唯一逃げ出そうとしていた青年は、仲間の顛末が気になったのかこちらを振り返った。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（いや、違うわね）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仲間を思って振り返ったのではない。\n
単に、怖かっただけだろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仲間に何が起こったのか、そしてそれが自分にも起こりうるのか。\n
それを確認したくて、彼は振り返ったのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして……。"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0233
Ace "「……はは。\n
そのまま走ったら、逃げられたかもしれないのにね？」"

hide m_ace3_2
show bg06_sk_h_day onlayer master

play sound se_0678
pause .5
play sound se_0100


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースが無造作に投げた大剣が、振り返った彼の頬を微かに掠めて背後の大木へと突き刺さった。"

hide bg06_sk_h_day



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（こ、怖い……！）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見ているだけで、背中が冷たくなった。\n
凶器である剣を大木に刺さるほどの力で、人に向けて投げることの出来るエースという男が怖い。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく……、狙い違えない絶対の自信があったのだろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずるずるっと逃げかけていた青年がへたり込むのを見て、エースはつまらなそうに唇を尖らせた。"


show ace_m_02_11 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0234
Ace "「やあ、もうちょっと逃げてくれてもよかったんだぜ？」"

hide ace_m_02_11
show ace_m_02_12 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0234_5
Ace "「これぐらいでへたり込んじゃうぐらいなら、最初っから風紀に喧嘩売るような真似するなよなあ」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（これくらい、って……。\n
剣をぶん投げられたら誰だって、へたり込んじゃうわよ）"

hide ace_m_02_12
show ace_m_03_9 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice ace_g0235
Ace "「……ああ、ヨッパライ茸を栽培してたのか」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽろぽろと逃げていた青年の腕の中から、赤々とした傘が特徴的なキノコが下生えの草の上へと落ちた。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じく木の根元に向かった二人の内、一人は栽培の証拠を消す担当、もう一人は十分に育った「商品」を持ち出す担当と、それぞれ役割が決まっていたのだろう。"

play sound se_0625


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……ヨッパライ茸の密栽培、ね」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、へたり込んでいる青年の傍らへと歩み寄り、その手の中から零れ落ちたキノコを回収した。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ヨッパライ茸は、見た目は綺麗なのだが、その鮮やかな色で人を酔わせる効果がある。眺めているだけで、大の男でも酩酊してしまうほどだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "マジックアイテムの材料としても重宝されているが、それ以上にお酒の代わりとして、年頃の私達にとっては興味のつきない植物だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その分、管理も厳重で、生徒による勝手な栽培は固く禁じられている。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（お小遣い稼ぎに、育てていたのね……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心地よい酩酊気分を約束してくれるヨッパライ茸の需要は、裏ルートでは高いのだろうと想像はつく。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深刻に危険な植物ではない分、生徒間の商売として成り立ちそうだ。"

hide ace_m_03_9
show ace_m_01_10 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0236
Ace "「はい、それじゃあ学生証を出してくれよな！\n
返却はユリウスから行われるから、きちんと塔に出頭するんだぜ？」"

hide ace_m_01_10
show ace_m_03_11 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0237
Ace "「後で、栽培したことへの詰問と、売りつけた生徒のリストも請求されると思う。\n
証拠隠滅をしたり、そのまま逃げたりなんかしたら……」"

hide ace_m_03_11
show ace_m_02_1 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0238
Ace "「……俺が迎えに行くことになっちゃうからな？\n
自分から大人しく出頭したほうが、身のためだ」"

play sound se_0313


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にこやかにそんな説明をしながら、エースは倒れている二人の前に屈みこみ、その懐から次々と学生証を回収していく。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らにしてみれば、エースに個人情報である学生証を握られている今、それ以上逃げる気なんてないだろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逃げたとしても、彼に追われた上に、より酷い目にあうだけ。\n
実際、三人のうち二人は未だに動けなさそうだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ねえ、医務室に連れて行ってあげたほうがいいんじゃないかしら。\n
怪我をしていると思うわ」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（正確には……、怪我をさせたと思うわ）"

hide ace_m_02_1
show ace_m_02_8 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice ace_g0239
Ace "「え～？大丈夫だよな？\n
そのために、わざと一人見逃したんだぜ？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "証拠品であるヨッパライ茸と、彼らの学生証を回収したことで、いい意味でも悪い意味でも、エースはそれ以上のことをする気はないようだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一人手付かずで残したのは、痛めつけた二人を介抱させるためだったということか。\n
やはり、慣れている。"

hide ace_m_02_8
show ace_m_03_12 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0240
Ace "「な？\n
大丈夫だろ？」"

hide ace_m_03_12
show ace_m_03_12 at left



show huryou_d1_7 at right




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Furyou "「……～～！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見逃された一人が、エースに笑顔で問いかけられて勢いよく頭を縦に振った。"

hide ace_m_03_12
show ace_m_01_10 at center


hide huryou_d1_7



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0241
Ace "「ほらな？\n
さ、そろそろ帰ろうぜ？」"

hide ace_m_01_10
show ace_m_01_4 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0242
Ace "「今日も一日、真面目に働いたらおなかがすいちゃったよ。\n
食堂に辿り着けるといいんだけどな！」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

hide ace_m_01_4


scene bg06_sk_h_eve
with dis



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の言葉に顔を上げると、生い茂り重なり合って空を塞ぐ枝葉の向こうに、赤く燃える夕焼け空がちらちらと見えた。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……そうね」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それ以外に、何を言ったらいいのかが分からない。\n
この男は知れば知るほど、分からなくなる。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（知れば理解できるなんて、とんでもない）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが一方で、分かったこともある。\n
彼が、風紀委員として認められている理由だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、違う。\n
彼は風紀委員として認められているのではなく、恐れられているのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その理由を、今、目の当たりにした。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……怖い男だわ）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは見逃して、密栽培の三人組は容赦なく制圧した。\n
彼なりに、明確な基準があるのだろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、ないかもしれない。\n
基準など何もないことも、彼なら有り得る。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何でもありな気もするし、分からない。\n
分からないからこそ、周囲は彼を恐れるのだろう。"



with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0624

play music forest_thick_eve_p_wam


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帰り道、エースはすっかりいつもの彼だった。\n
何もかわらない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "交わす会話も、いつもと同じだ。\n
とんでもない方向に突き進みかける彼に、私はうるさく修正を加える。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼一人であらぬ方向に突き進んでいくのならば見送るが、彼は当たり前のように私を一緒に連れて行こうとする。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……早く、寮に帰りたい）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "表面上はいつもどおりを取り繕えていても、頭の中は未だに混乱していた。\n
彼に対するイメージを、うまくまとめあげることが出来ない。"


scene bg_par15_rg_ros_eve
with dis



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして歩いているうちにも、赤薔薇寮の中庭へ辿り着いた。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま寮のエントランスに進もうとする私とは逆に、ふと彼が歩みを止める。\n
また、案内されるのは嫌だなんてことを言い出すつもりなのだろうか。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……大丈夫よ、エース。\n
あなたなら、エントランスからでも充分迷えるから」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子寮、男子寮と、エントランスで別れたとしても彼は迷子になれる。\n
寮内キャンプコースは間違いない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "てっきりまた、自称・冒険家の血が騒いでいるのかと思ったのだが、どうやらそうではなかったらしい。"


show ace_m_01_3 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0243
Ace "「違う違う、そうじゃないって。\n
君に、お礼を言おうと思ってさ」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中から聞こえた意外な言葉に、私も立ち止まると彼を振り返った。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「お礼？\n
……お礼を言われるようなことは、何もしていないわよ？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先刻のことだって、私はただ見ていただけだ。\n
彼らを捕まえるために、何かが出来たわけではない。"

hide ace_m_01_3
show ace_m_03_12 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0244
Ace "「いやいや、謙遜するなよ。前も君と一緒のときに猫君を発見したし、今日なんか密栽培だぜ？」"

hide ace_m_03_12
show ace_m_03_3 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0244_5
Ace "「非行のレベルも、どんどん上がっているよな！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実は、ボリスの魚釣りと今回の密栽培の間にも、パトロール中に何度かトラブルには出くわしている。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのたびに、エースは私に感心するのだが……。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「それ、私のおかげじゃないわよ？\n
それじゃあ、私が疫病神みたいじゃない」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "引き寄せるトラブルのレベルが上がっている、と言われているみたいだ。\n
普通、褒め言葉ではない。"

hide ace_m_03_3
show ace_m_02_4 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0245
Ace "「何言っているんだよ。お手柄だぜ？\n
俺達って、相性いいよな」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何がどう相性がいいのかが、張本人である私には分からない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分のよさを人に分かってもらえて、相性がいいなんて言われるのは、有難いことであるはずなのだが……。"

hide ace_m_02_4
show ace_m_02_10 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0246
Ace "「で、さあ。\n
俺と付き合ってくれる？」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "有耶無耶のうちに、なかったことにしてしまえないだろうかとひっそり期待していた告白を、もう一度され直してしまった。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その口調には相変わらず、愛の告白なんて重さはこれっぽっちもない。\n
夕食の誘いでもするかのような、軽やかな口調だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（対応をまともに考えるほうが馬鹿らしいような……）"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「当然、断るわ」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当たり前だ。\n
夕食の誘いではないのだ、受けるほうがどうかしている。"

hide ace_m_02_10
show ace_m_03_9 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0247
Ace "「駄目だよ。\n
俺が、もう、君がいいって決めちゃったから」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……はい？」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（？？？）"

hide ace_m_03_9
show ace_m_01_10 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice ace_g0248
Ace "「断っちゃ、駄目」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまりそれは、私には断る権利がない、ということなのか。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「いやいやいや、なんであんたが駄目だなんていうのよ。\n
私のことは、私が決めるわ」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とてもそうは思えなくても、告白ならば、断れば引くものだ。"

hide ace_m_01_10
show ace_m_03_11 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0249
Ace "「うん、でもさ、君がいいんだ。\n
俺は、君がいい」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話が噛み合っていないような気がする。\n
もう一度深呼吸を挟み、気を落ち着け、改めて目の前にいる男と視線を重ねる。"

hide ace_m_03_11
show ace_m_03_3 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Ace "「…………」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……あなた、楽しんでいるでしょう」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは、噛み合わない会話に私がパニックになる様を楽しんでいるように見えた。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "被害妄想とも言い切れない。\n
この場においても、彼はにこにこしているのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（なんてタチの悪い……）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の性格がいいとは思わないが、エースはそんな私以上に捻くれている。\n
もしくは歪んで見える。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうは見えない分だけ、タチが悪い。"

hide ace_m_03_3
show ace_m_01_10 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0250
Ace "「楽しいか楽しくないかといえば、楽しいさ。\n
好きな子と仲良く出来るんだから」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……別に、そう仲良くしているわけじゃないけど」"

hide ace_m_01_10
show ace_m_03_12 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice ace_g0251
Ace "「はは、つれないなあ。\n
でも、それでこそ魔法のかけがいがある」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「ま、魔法……！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（何か、かける気なの！？）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは、これで優秀な魔法使いだ。\n
魔法勝負になれば、太刀打ちできない。"

hide ace_m_03_12
show ace_m_02_1 at center




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0252
Ace "「そ。\n
恋の魔法」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「…………」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「……{size=+20}殴っていいかしら{/size}」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐ、っと私は利き手で握りこぶしを作った。\n
恋の魔法なんて、うすら寒いにもほどがある。"



with dis
$ hi_mes()
show m_ace3_3and3_5 onlayer master

hide ace_m_02_1

pause .5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0253
Ace "「はは、そういうと思った。\n
でも……、俺は本気だよ」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ！\n
エース！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "半ば威嚇のつもりで拳を握っていた腕をエースにとられ、ぐいと距離を詰められた。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の手首を握っても、まだ余裕のある大きな手にぎくりとする。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（本気……、なの？）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋の魔法だなんてふざけたことを言っているくせに、エースの赤い双眸は怖いぐらいに真剣だった。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口元はいつものように嘘くさい爽やかな笑みを浮べているというのに、その眼が笑っていない。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……魅惑の魔法でもかける気？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋の魔法なんていうと馬鹿馬鹿しく聞こえるが、魅惑や誘惑、そのあたりの強力な魔法を使えば人を意のままに操ることも出来てしまう。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「暗示とか……、そういうことを考えているんじゃないでしょうね？」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0254
Ace "「……はは。\n
似たようなことは考えているかな」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "『俺のこと、好きになってほしいんだ』 "



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先日言われた言葉を思い出して、ぞくぞくと背中に冷たいものが走った。\n
鼓動が早くなる。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはときめき、なんて生ぬるいものじゃない。\n
どちらかというと、恐怖に近い。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（暗示だとしたら）"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「人の心を魔法で動かせると思っているの……っ！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "陳腐な台詞だ。\n
『人の心を操る魔法』が可能か否かといえば、可能に決まっている。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはこれまでにも、様々な魔法使いが挑戦し続けた分野。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、一時的な錯覚で、その行動に影響を与えることには成功しても、恋愛のような長期のスパンで成功したという話は聞かない。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人間の精神には、外部からの暗示や働きかけを、自然と中和・解除するだけの力が備わっている。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、マインドコントロールや洗脳なんてことになると、まずはその健全な精神の持つ免疫機能を破壊するところから始めることになる。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、エースは、それを飛び越えようとしている。\n
なんでもかんでもすっ飛ばしてしまう彼らしく。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（いや、段階を踏まれて、精神を壊されるのも冗談じゃないけど）"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「い、嫌よっ、そんな実験！\n
私は付き合うのは御免よ！！」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice ace_g0255
Ace "「実験って……。\n
別に、実験がしたいわけじゃないんだけどなあ……」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「じゃあ、なんなのよ！？\n
万が一成功したらどうするのよ！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_6")
T "「その……っ、私があなたのことを好きになっちゃったら！」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好きになって、実験は成功しました、はいおしまい、というわけにはいかないだろう。\n
問い詰めずにはいられない。"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0256
Ace "「君が俺のことを好きになっちゃったら？\n
はは、もちろん、ちゃんと責任取るに決まっているだろ？」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0257
Ace "「俺は風紀委員だぜ？\n
風紀委員たるもの、婦女子に対して不道徳な振る舞いはしないよ……、なるべくね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽそりと追加された呟きが不穏だ。\n
爽やかな笑顔で、責任は取ると言い切られ、頭がくらくらとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「と、とらなくていい！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice ace_g0258
Ace "「え？とらなくていいの？\n
でも、風紀委員として……というか、男として……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "{size=+20}「責任をとらないといけないようなことはしないでちょうだい！」{/size} "
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もっと色々言ってやりたいのに、掴まれた腕を引かれ、腰を抱き寄せられて言葉がうまくまとまらない。"
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薔薇の生垣の木陰。\n
悪い魔法使いに捕らわれて、笑いかけられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0259
Ace "「……違うんだよ、[firstname]。\n
そうじゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「女性の心を操ろうなんて、それこそ風紀を正す者として道徳に反する……」"

hide m_ace3_3and3_5
show m_ace3_4 onlayer master



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice ace_g0260
Ace "「……違うんだって。\n
君の心をどうこうするわけじゃない」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0261
Ace "「……俺の心を、どうにかしてほしいんだ」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……{size=+20}へ？{/size}」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice ace_g0262
Ace "「俺に、恋の魔法なりなんなりかけてよ。\n
俺は君が好きだから、君に恋がしてみたいんだ」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice ace_g0263
Ace "「それで、君も俺に恋とかそういうのをしてみてほしい。\n
……せっかく心臓があるんだし、心動かされてみたいんだよ、君に」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「は、はあ……？」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice ace_g0264
Ace "「実験っていうなら、そうかもしれないな。\n
試す価値がある」"

play sound se_0496
hide m_ace3_4
show m_ace3_3and3_5 onlayer master



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
Ace "「…………」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「……な、何をしたの？」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
voice ace_g0265
Ace "「何にも」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「う、嘘！\n
今、呪文みたいなのを……」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice ace_g0266
Ace "「呪文みたいなの？\n
そう聞こえたのなら、呪文かもな」"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「～～～～……！？」"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice ace_g0267
Ace "「な？\n
俺と恋に落ちてみようぜ？」"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（…………）"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（会ったときから、そうだったけど……。\n
この人、無茶苦茶だわ）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋に落ちるというより、真っ暗闇に落ちる気持ち。\n
いっそ、意識を失いたくなった。"

hide m_ace3_3and3_5



with dis
$ hi_mes()

scene bg_par15_rg_ros_eve
with dis


scene bg_par15_rg_ros_nig
with dis


scene bg25_rr_nig
with dis
with stripe_l_medium

scene bg24_rj_nig
with dis
with stripe_l_long

play music dream_inside_wam
##special anime old film

show m_kyoutuu_yume1 onlayer master



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "エースがあんなことを言い出したせいだろうか。\n
懐かしい夢を見た。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "ただ、穏やかな時間に、穏やかな会話を交わすだけの夢だ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "夢の中の舞台は、窓から日が差し込む小さな部屋。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "壁際には古い本棚がいくつか置かれており、そこにはもう誰も必要とはしていないんじゃないかと思わざるを得ないような古びた資料が、整然と並べられている。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "夢の中だというのに、匂いまでが鮮明だ。\n
黴臭いような、それでいてどこか甘い古い紙の匂い……。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "部屋の中ほどでは、なにやら机の上の私物を整理している人物の姿が見える。"

jump gakuen_dream_notblood
label gakuen_ace3_6:


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「エースのせいで……。\n
嫌な夢を見たわ……」"



hide m_kyoutuu_yume1 with open_medium

play music room2_p_wam


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鬱々と呻いて、私は目を開けた。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「…………」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最悪な寝起きだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、この夢を見るのはずいぶんと久しぶりのような気がする。\n
一時期は、毎日のようにうなされていたものなのだが。"



with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……ああ、もう」"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間違いなく、エースのせいだ。\n
エースが恋の魔法なんて、わけの分からないことを言い出すから、悪いのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのせいで、こんな昔のことを思い出す。\n
彼は、ずっと姉に憧れていたらしい。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼自身がそう言ったわけではないが……、きっと私に親切にしてくれたのも、私が姉の妹だったからなのだろう。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼にとって私は、「[firstname]＝[familyname]」ではなく、「ロリーナ＝[familyname]の妹」だったのだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私を通り越して姉を見ていた彼に、自分を見てくれているという幻想を抱いていたなんて、今思い出しただけで羞恥で死にたくなる。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唯一の救いは、誰にも私の想いを知られることなく終わったことだろうか。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（だから恋愛なんて御免なのよ）"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "出来ることならば、恋愛沙汰になど関わりたくない。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（ああ、だから……）"

play sound se_0327


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むくりと身を起こしたベッドの中で、ぼんやりと眼を伏せる。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しだけ、本当に少しだけ。\n
そんな私だからこそ、魔法でも使わない限り恋愛など無理なのではないかと、そう思ってしまった。"

jump gakuen_cafeteria_notjoker
label gakuen_ace3_7:


with dis
$ hi_mes()

scene bg06_sk_h_day
with dis



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日、何かが行われるらしい。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう考えたとき、何故か、エースの姿が思い浮かぶ。\n
最近、彼に振り回されっぱなしだ。"



with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントごとが行われるとして、彼はどういう役割を果たすのだろうか。"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（…………）"



with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（それがどんな役割にしても、まともに果たしそうもない……）"



scene bg_map_day
with dis
with stripe_l_long
##endmemory
jump gakuen_ace4
