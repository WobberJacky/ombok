label gakuen_ace2:
scene bg_map_eve
with dis
$ clockanim()


scene bg14_fm_eve
with dis

play music forest_thick_eve_p_wam

scene bg13_fr_eve with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業を終え、赤薔薇寮へと戻る道を歩いているところ。\n
不穏な物音を聞いた。"

play sound se_0430
play sound se_0204
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……？）"


scene bg13_fr_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこかに怪我をした鳥でもいるのだろうか。\n
激しく翼を羽ばたかせる音と、切実そうな鳥の鳴き声とが聞こえてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "懸命な様子が声からも伝わってくる。\n
こんな悲痛な声で鳴いている鳥を見殺しにするのも、寝覚めが悪い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "茂みを掻き分けて、その怪我をした鳥の姿を探してみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……どこにいるの？\n
怪我をしているの？」"

play sound se_0010
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脅かしてしまわないように、柔らかな声を心掛け、そっと茂みを掻き分けて……。"


show ace_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0124
Ace "「……{size=+20}あ{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

play sound se_0747
hide ace_m_01_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "茂みを掻き分けた先に現れた光景に、私はそっと茂みから手を離した。\n
とんでもないものを見てしまった、と。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（気のせいよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すうはあ。\n
深呼吸をする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……改めて）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう一度気を取り直して、茂みへと手をかけた。"

play sound se_0747
with dis
$ hi_mes()

show m_ace2_1 onlayer master
with dis
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice ace_g0125
Ace "「何やってるんだ？\n
茂みを開いたり閉じたりして」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「…………。\n
……幻覚じゃなかったのね」"

play sound se_0614
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幻覚であってほしかったのだが、現実だ。\n
茂みをかきわけた先、エースは爽やかな笑顔で私へと声を掛けてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばっさばっさと抵抗する鳥の首を掴んでぶら下げながら。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……ええと。\n
私は、普通に授業の帰りなんだけれど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は普通。\n
エースは普通じゃない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……あなたの言葉、そっくりそのまま返すわ。\n
何をやっているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice ace_g0126
Ace "「何って……、あはは、君、おかしなことを聞くなあ。\n
見て分からない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「見て分からないから、聞いているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_9")
T "（……あまり、分かりたくもないけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_9")
voice ace_g0127
Ace "「ふうん？分からないんだ？\n
君の目には、どう見える？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「私の目には……、今にもその鳥をシメようとしているように見えるわ」"

play sound se_0430
play sound se_0205
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースに首をぎゅむっと握られている鳥が、断末魔のような鳴き声でばっさばっさぎゃあぎゃあと騒いでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鳥の翼が、四枚ある。\n
暴れているせいでの錯覚かと思ったが、間違いなく四枚。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（普通の鳥……、じゃない？）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice ace_g0128
Ace "「その通り。\n
なんだ、分かっているんじゃないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice ace_g0129
Ace "「俺はね、今からこの鳥をシメようとしているんだ。\n
今日の夕飯だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice ace_g0130
Ace "「前に仕掛けておいた罠に、引っかかっていたんだ。\n
有難いことだぜ、今夜はリッチなディナーにありつける」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「ちょ、ちょっと待ってね。\n
今、つっこみどころを整理しているから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "得意げに片手に握った鳥を掲げてみせるエース。\n
言いたいことは山ほどある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校内に罠を仕掛けているとはどういうことなのか、とか。\n
他にも罠があるのか、だとか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その鳥が夕飯とはどういうことなのか、とか。\n
食堂に行けば、今夜でなくてもリッチなディナーにありつける、とか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言いたいことが色々ありすぎて、パンク状態だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……どうして、寮と校舎の狭間で、野営なんかしているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すべての疑問はそこに集約する。\n
ここが山の中であるのなら、私のエースに対する対応ももっと違ったものになっていただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "サバイバル生活も可能な、頼もしい人。\n
好感を持ったかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、ここは山の中ではない。\n
シンフォニア高位魔法学校の敷地内だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か魔法による制約があるわけでもなく……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通に（彼といると意味もなく、比較対象に「普通」を連呼してしまう）、校舎と赤薔薇寮とを結ぶ道から少し外れただけの茂み。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしてそんなところで、この男は鳥を捕まえてシメようとしているのか。\n
どうして、そんなところでテントを張って野営準備が万端な状態なのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0131
Ace "「そりゃあ、もう日が暮れかけているからだよ。\n
暗くなってから無理に動いても、いいことなんかないぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「ええ、そうね、遭難したときの大事なセオリーだわ。\n
でも、もっと大事なことが抜けている」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Ace "「？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………。\n
……普通はね、ここからだったら五分もかからずに寮に着くのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その移動で、日は暮れたりしない。\n
授業は終わったばかりで、エースの言うとおり日は傾きかけてはいるが、まだそんな暗くなるような時間ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0132
Ace "「はは、君ってすごいね。\n
俺は多分、三日ぐらいかかるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「み……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（三日？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私だって、進む速さが人によって違うことぐらい理解している。\n
足の速い人間もいれば、遅い人間もいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、エースのそれは一般的な問題をはるかに超えている。\n
常人が五分程度で到達できる距離に、三日かけるというのはあきらかに異常だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……いや、普通か異常かというなら、それこそ今更な話よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_g0133
Ace "「あ、そうだ。\n
いいことを考えたぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_g0134
Ace "「君を、今日の俺の夕食に招待するよ。\n
せっかく美味しそうな鳥が獲れたことだしな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは好意的に接してくれる。\n
恐ろしくなるほど、爽やかな笑顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、ぐいと片手で掴んだ鳥を、私のほうへと掲げてみせた。"

play sound se_0205
hide m_ace2_1
show m_ace2_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0135
Ace "「美味しそうだろ？\n
鳥、好き？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどから会話の間にもシメ続けていたのか、鳥はだいぶぐったりとしてきていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（ど、どうしよう？）"

menu:
    "止める。":
        jump gakuen_ace2_2a
    "放っておく。":
        jump gakuen_ace2_2b
label gakuen_ace2_2a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「ちょっと！エース……！\n
可哀想じゃない、やめてあげなさいよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice ace_g0136
Ace "「ええ～？\n
俺が捕まえて、食べる鳥だぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice ace_g0137
Ace "「無駄に殺すわけじゃないんだから、いいじゃないか。\n
腹をすかせた俺は可哀想じゃないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「そ……っ、それはそうだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "弱肉強食。\n
食物連鎖。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "理屈として分かってはいても、いざ目の前で鳥を殺そうとしているところを見てしまうと、やはり可哀想に思えてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……っていうか、食堂に行けば、この鳥を食べる必要はないと思うけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、食べる分には無駄にならない。\n
狩猟の範囲だし、この世界の冒険者達は、皆そうやって生活している。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Ace "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは、鳥に同情した私に、面白がるような視線を向けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……なんでもないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0138
Ace "「はは、それならよかったよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0139
Ace "「見ろよ、この鳥。\n
羽が四枚もあるから、手羽先が倍食べられるぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0140
Ace "「二人で食べるにはもってこいだよな。\n
あ、そうだ、悪いけど手伝ってくれないか？」"

jump gakuen_ace2_3
label gakuen_ace2_2b:
$ lovechara_ace_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……面白半分に苛めているのなら止めるんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この男は、食べる気満々だ。\n
そうなると、狩猟の範囲になるわけで、私としても止める理由がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0139
Ace "「見ろよ、この鳥。\n
羽が四枚もあるから、手羽先が倍食べられるぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0140
Ace "「二人で食べるにはもってこいだよな。\n
あ、そうだ、悪いけど手伝ってくれないか？」"

jump gakuen_ace2_3
label gakuen_ace2_3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "羽が四枚あるのに、エースはたいして驚いていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（珍しくもないのかしら？\n
さすがシンフォニア……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自生する動植物も、一筋縄ではいかない。\n
以前の、庭園の薔薇がいい例だ。"

hide m_ace2_2

play sound se_0066
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースはごそごそとテントの中をあさると、その中から小刀と、何束かに束ねた野菜のようなものを取り出した。"


show ace_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0141
Ace "「俺は引き続き、鳥を捌いちゃうからさ。\n
君には、野菜の下拵えをお願いしてもいいかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「ちょっと、まだ私、ご馳走になるなんて言っていないわよ？」"

hide ace_m_02_10
show ace_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice ace_g0142
Ace "「え？\n
じゃあ帰るのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きょとん、とした顔で見つめられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……お受けします」"

hide ace_m_03_2
show ace_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice ace_g0143
Ace "「そうこなくっちゃ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……負けた気がする）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろいろエースの行動につっこみをいれてはみたけれど、私だって好奇心がないほうではないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "状況的に気になるし、エースという魔法使いに対する興味もあった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（変わった人だけど、優秀なのよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手早く簡易コンロを組み立てる彼を眺めながらそんなことを思う。\n
料理の準備を整えていくエースはひどく手際がいい。"

hide ace_m_01_1
show ace_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0144
Ace "「野菜は一口サイズに切って、この鍋に放り込んでくれよな。\n
とりあえず煮込めばなんとかなるから」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "組み立てた簡易コンロの上に鍋を設置して、火をつける。\n
野菜を切り終わる頃には湯も沸くだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……煮込めばなんとかなるなんて、大雑把ね。\n
香辛料の類もあるの？」"

hide ace_m_03_11
show ace_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0145
Ace "「はは、キャンプ食なんてそんなものだろ？\n
香辛料も大雑把なものなら、そこのテントの中に入っているよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「それじゃあ、味付けで誤魔化しちゃえるわね。\n
あ、何か、まな板に使えそうなものはある？」"

play sound se_0066
hide ace_m_02_4
show ace_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice ace_g0146
Ace "「はい、これを使ってくれ。\n
作業は……、このあたりにでも座るといいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは再びテントの中をごそごそとして、小さなボードを差し出してくれた。"

play sound se_0251 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを受け取って、示されたとおり、エースが椅子代わりに使っていたのであろう倒木に腰を下ろした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "膝の上にボードを乗せ、束にされてある野菜類を適当に切っていく。"

hide ace_m_03_10
show ace_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0147
Ace "「それじゃあ、俺はちょっとこの鳥さんを美味しい鳥肉にしてくるぜ！\n
待っていてくれよな！」"

play sound se_0010
hide ace_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぷらーんとぐったりとした鳥をぶら下げて、エースが茂みを掻き分けていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小刀は私に渡しているので、あの腰に下げた大剣で捌くつもりなのか。\n
さすがに女（私のことだ）の目の前で、鳥を捌くのは遠慮してくれたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……いや、違うわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースが、この場を離れた理由はもっと単純にして明快だ。\n
私への気遣いなどではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これから今夜一晩を明かす場所を、血生臭くしたくなかっただけに違いない。\n
まだ彼のことをよく知らないはずなのに、そんな確信があった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「そもそも、そんな気遣いができる人なら……。会話の片手間に鳥をシメたり、薔薇の生垣を切りつけたりなんかしないわよね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐったりと力を失っていく鳥の様子だとか、無残に切り開かれた薔薇の生垣だとかを思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今、私は彼の招待客という立場。\n
招待客までは破壊しないことを願う。"



scene bg13_fr_nig
with dis

play music forest_thick_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「…………」"

play sound se_0322

show ace_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice ace_g0148
Ace "「そろそろ、よさそうかな。\n
いい匂いだ」"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちぱちと爆ぜる焚き火を見ているうちに、きゅるるる、とおなか鳴ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲には鳥肉の焼けるいい匂いと、美味しそうなスープの匂いが漂っている。"

hide ace_m_03_10
show ace_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0149
Ace "「はは、君もお腹がすいているみたいだな。\n
もう少しだから、待っていてくれよ」"

play sound se_0643
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手羽先は串にさして焚き火に直接かざして焼いてあり、その他の胸肉やらささみ部分は野菜類と一緒に鍋の中で煮込まれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……{size=+20}負けた気がする{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……く、悔しいわ」"

hide ace_m_02_4
show ace_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0150
Ace "「え？\n
何が？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……すごく、美味しそう」"

hide ace_m_03_2
show ace_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice ace_g0151
Ace "「いいことじゃないか。\n
まずそうに見えるより、いいだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「ええ、いいことなんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学食に向かえば、ある程度手の込んだ料理が食べられると分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、煮込んだだけのスープと、焼いただけの鳥肉にこんなにも心惹かれてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とても、とてもとても、美味しそうだ。\n
ぽた、と串焼きにされた手羽先肉から、溶けた油が炎の中に落ちてめらりと揺れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっかり日が暮れてきたこともあり、炎が闇に映えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "道のあたりならば、まだ明るいのだろうが、こうして道をそれて茂みに入ってしまうと一気に夜の気配が濃厚になる。"

hide ace_m_01_10
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0152
Ace "「先刻捌いたばかりだから、肉も新鮮だしな。\n
きっと美味いぜ～」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「そうよね。\n
切り分けているときにも感じたけど、身がぷりぷりしていて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "凝った料理ではない。\n
鳥肉と野菜を一緒に煮込んで、調味料で味をつけただけだし、手羽先に至っては塩を振っただけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでもこんなに美味しそうなのは、素材がいいからだろう。\n
まさしく、キャンプの醍醐味だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（……{size=+20}私は、一体、何の学校に入ったんだ？{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "場所を忘れかけ、疑問がわいてきてしまう。"

hide ace_m_03_3
show ace_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0153
Ace "「そろそろ火も通ったかな。\n
あち、あちちちっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「ああ、ほら、火傷に気をつけて……っ！\n
大丈夫？」"

hide ace_m_02_2
show ace_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice ace_g0154
Ace "「大丈夫、大丈夫。\n
これくらい、舐めれば治る」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「何を言っているの。\n
流水が一番いいんだけど、痛むなら回復魔法を……」"

hide ace_m_02_12
show ace_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice ace_g0155
Ace "「平気だって。舐めれば治る程度だよ。\n
……ああ、治してくれるっていうなら、君が舐めてくれる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと、エースが私へと視線を流す。\n
何の間違いか、うっかりどきりとしてしまいそうになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "焚き火と同じ色をした、赤い双眸だ。\n
めらめらと踊る炎の色を映して、昼よりも鮮やかに見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それ自体が、光を放っているような。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……っ！\n
馬鹿、さっさと取ってよ！」"

play sound se_0118
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな錯覚を追い払うように、べし、と焚き火の前で屈んでいる彼の後頭部を軽くはたいた。"

hide ace_m_03_12
show ace_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0156
Ace "「あいたっ！\n
ケチだなあ、舐めるぐらい減らないだろうに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……突き飛ばしてほしい？\n
軽い火傷じゃすまないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは、現在焚き火の前で屈んでいる。\n
その背を突き飛ばすと、間違いなく大惨事だ。"

hide ace_m_02_8
show ace_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0157
Ace "「はは。\n
怖いなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは笑いながらも、ひょいひょい、と手羽先の串焼きを私の分まで焚き火脇から取り上げてくれた。"

hide ace_m_03_1
show ace_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0158
Ace "「熱々だから、君こそ火傷しないよう気をつけてくれよ？\n
……うんっ、うまいな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言う彼は火傷などには無頓着なようで、ぱくぱくと頬張っていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ、あつ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真似をして食べると、痛いめにあう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「……ん。\n
はふ、はふ……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「……美味しい！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふうふう、と美味しそうに焼きあがった手羽先に息を吹きかけて冷まし、齧りつく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まず口の中に広がるのが、こんがりと焼けた香ばしい匂い。\n
実際に咀嚼すると、じゅわっとジューシーな肉汁が口の中に溢れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースが言ったとおり熱々だが、文句なしに美味しい。\n
喋るどころではなく、はふはふと鳥肉を堪能する。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……ああ、鳥さん、ごめんなさい。\n
美味しいです……）"

hide ace_m_01_1
show ace_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice ace_g0159
Ace "「あ、味付けが物足りなかったら、その辺のを適当に使ってくれよな。\n
塩と胡椒と、あとメジャーなのだけだけどハーブもあって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ありがと。\n
でもこれ、下手に味付けしなくても美味しいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下味で塩胡椒を擦り込んだだけなのに、そんなシンプルな味わいがたまらなく美味しい。\n
素材の力とは偉大だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「スープのほうも、よそっちゃうわね」"

hide ace_m_01_3
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice ace_g0160
Ace "「うんうん。\n
お願いするよ」"

play sound se_0642
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は一度食べかけの手羽先の串を、焚き火から少し離れたところに刺しなおすと、鍋をぐるぐるとお玉でかき混ぜる。"

play sound se_0096
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふわりと、より強くまたいい匂いがした。\n
水筒の蓋と、内蓋とに、そのスープを注いでいく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「はい、こっちも熱いから気をつけてね」"

hide ace_m_03_3
show ace_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice ace_g0161
Ace "「なんかこうしていると、俺達夫婦みたいだよな！\n
君もそう思わないか？」"

play sound se_0132
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「……あら。\n
{size=+20}ごめんなさい、手が滑ったわ{/size}」"

hide ace_m_02_3
show ace_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_2")
voice ace_g0162
Ace "「あち……！！\n
酷いな、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざとお玉を乱暴に揺らして、エースのほうへと熱いスープの雫を飛ばす。\n
大袈裟な悲鳴をあげる彼は、本気で熱がっているわけでもないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……あなたの冗談は笑えないわ」"

hide ace_m_03_8
show ace_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0163
Ace "「そう？\n
全然？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……ええ。\n
全然」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "また椅子代わりにしている倒木へと身を戻す。\n
椅子になるようなものが他にないため、すぐ隣にエースがいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し道からずれただけで、ここは大自然の真ん中でも何でもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、周囲を茂みに囲まれた中でこうして二人きりで焚き火に当たっていると、妙な錯覚を起こしそうになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアなどではなく、森の奥。\n
誰もいない場所で二人、キャンプをしているかのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……あ、こっちも美味しい！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "スープにも、鳥の出汁と野菜の旨みとが充分に溶け出している。"

play sound se_0065
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の声につられたように、エースもスープへと口をつけて、同じように感嘆の息を吐いた。"

hide ace_m_02_13
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0164
Ace "「はは、やっぱり誰かと一緒の食事っていいよな！\n
いつもより、美味しく感じるぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……いつも一人なの？」"

hide ace_m_03_3
show ace_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0165
Ace "「いや、辿り着いた先でご相伴に与かることも多いよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「毎回、ちゃんと食堂に来たらいいのに。\n
一人での食事って、味気ないでしょう」"

hide ace_m_01_10
show ace_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice ace_g0166
Ace "「そんなこともないけど……、ああ、でも、行こうとは思っていても辿り着けないんだ」"

hide ace_m_01_2
show ace_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice ace_g0166_5
Ace "「よかったら、君、これからも俺に付き合ってよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「どこにいるか分からないあなたを探して？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日はたまたま鳥の鳴き声で気付いたものの、以後もそうやって見つけるというわけにはいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「それこそ、あてどもない旅になりそう」"

hide ace_m_01_4
show ace_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice ace_g0167
Ace "「はは、旅っていいものだけど、巡り合わないのは困るな。\n
そうだ、それなら俺が君を迎えにいくよ」"

menu:
    "楽しみにしているわ。":
        jump gakuen_ace2_4a
    "期待はしない。":
        jump gakuen_ace2_4b
label gakuen_ace2_4a:
$ lovechara_ace_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そう？\n
楽しみにしているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろいろと問題はある人だが、エースと一緒に過ごすのは新鮮だ。\n
やや新鮮すぎるきらいはあるが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人姉妹の真ん中として育ったせいか、こういったアウトドアの経験は乏しい。\n
新しい経験を得ることが出来るというのは、シンフォニアに来る目的でもあった。"

jump gakuen_ace2_5
label gakuen_ace2_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……期待しないで待っているわ。\n
たまになら、こういうのも悪くないもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷子常習犯に「迎えにいく」なんて言われても、信用できない。\n
嘘のつもりがなくとも、きっとエースは辿り着くことが出来ないだろう。"

jump gakuen_ace2_5
label gakuen_ace2_5:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから私は、その誘いを断らずに受けておく。\n
エースはその返事に満足そうだった。"

play sound se_0624
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……誰か、来る？）"

hide ace_m_03_10
show ace_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice ace_g0168
Ace "「あれ？また、お客さんかな？\n
今日はお客さんの多い日だな～」"

play sound se_0010
hide ace_m_02_11
show ace_m_02_11 at left
with dis

show yuri_m_03_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "茂みを掻き分けて顔を出したのは、塔の寮長。\n
そして風紀委員長でもあるユリウス＝モンレーだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、エースと並んでキャンプを堪能している私に目を丸くする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……まともな反応だ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースに感化され始めると、まともな反応が意外に思えてしまう。"

hide yuri_m_03_2
show yuri_m_02_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼のペースにのまれてキャンプを楽しんでいた私も、常識人代表のようなユリウスの登場に我に返り、奇妙な沈黙が続いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この状況を作り出したのは、エース。\n
それをぶち壊すのも、もちろんエース。"

hide ace_m_02_11
show ace_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0169
Ace "「ああ、ユリウス！いいところに来たな！\n
見ろよ、すごく美味しく出来たんだ！」"

hide ace_m_02_4
show ace_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0170
Ace "「ユリウスも、一緒に食べようぜ？\n
人は、多いほうが楽しいっていうしな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呆気に取られているユリウスの様子など気にせず、手招きして呼ぼうとする。\n
その声に、風紀委員長ははっとした様子で瞬いた。"

hide yuri_m_02_3
show yuri_m_03_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0002
Julius "「……こいつだけならともかく、[firstname]、おまえまでこんなところで何をやっているんだ。\n
そろそろ寮の門限だろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ご、ごめんなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返す言葉がない。\n
途中からは、私も充分にキャンプを楽しんでいたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと空に視線をやると、すでに真っ暗。\n
茂みの中は元々暗かったこともあり、あまり時間経過を感じずにいたが、結構な時間が経ってしまっていたらしい。"

hide ace_m_03_3
show ace_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0171
Ace "「ユリウスは、こんなところまでどうしたんだ？\n
あ、俺のこと、探してくれていたとか？」"

hide yuri_m_03_10
show yuri_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0003
Julius "「そんな非生産的なことに使う時間はない。……ちょっと探しものをしていたら、炎の気配と食事の匂いがしたので、顔を出してみただけだ」"

hide ace_m_01_3
show ace_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0172
Ace "「ちぇっ、ユリウスは素直じゃないよな。\n
[firstname]、ユリウス、本当は結構俺のこと好きなんだぜ？」"

hide ace_m_03_7
show ace_m_02_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0173
Ace "「なんたって、俺達は親友！\n
しかも、志を同じくする仲間でもあるんだ！友情って美しいよな！」"

hide yuri_m_01_3
show yuri_m_03_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0004
Julius "「好きじゃないし、思想も同じくしていない。\n
勝手に捏造するなっ！」"

hide ace_m_02_1
show ace_m_03_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0174
Ace "「はは、またまた照れちゃって。\n
あ、ユリウス、ユリウスもこれ食べる？美味いんだぜ」"

hide yuri_m_03_7
show yuri_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0005
Julius "「……エース。\n
おまえはたまにでいいから人の話を聞け」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と言いながらも、ユリウスは焚き火の近くまで歩みよってきた。\n
私はエースのほうへと詰めて、ユリウスの座るスペースを作る。"

with dis
$ hi_mes()
hide ace_m_03_11

hide yuri_m_01_10


show m_ace2_3 onlayer master
with dis
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "門限を促しはしたものの、何も今すぐに追い払おうというわけではないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（ユリウスって、口ほどは厳しくないというか、寛大よね……。\n
なんていっても、エースと付き合っていけるあたり……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さっさと食事を済ませてしまうべく、手羽先の串焼きを手にとり、もぐもぐと頬張る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……美味しい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジューシーだ。\n
また機会があれば、ゆっくりと食べたいと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（何て鳥なのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "四枚翼があったりと、私の知らない鳥だった。\n
シンフォニアにしか生息しない鳥なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だとしたら、もったいない。ただ焼いただけでもこんなにも美味しいのだから、料理の素材としてちゃんとした料理人が扱えばもっと美味しくなるはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ねえ、志を同じくするって、何のこと？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0175
Ace "「ん？\n
ああ、それは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0006
Julius "「同じくしていない。\n
……が、風紀委員のことを言っているのだろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0176
Ace "「そうそう、寮こそ違うものの、学園の風紀を取り締まる者同士」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0176_5
Ace "「俺は自治会のメンバーでもあるけど、風紀委員として、ユリウスの下についているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_g0177
Ace "「やりがいあるんだぜ？\n
学園の風紀を乱す者は容赦せず、ばっさばっさと薙ぎ倒し……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0007
Julius "「……そうやって、おまえが風紀を乱していくのを、私が正していかねばならんのだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……苦労していそうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、エースは役職を股掛けしているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "片方の役職ですら満足にこなしていなさそうなのに、よくもまあ、二つも兼任しようと思うものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0178
Ace "「はは、ユリウスってば、お固いよなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0008
Julius "「……風紀委員が緩くてどうする。取り締まる側だぞ？\n
おまえはその意識が……」"

hide m_ace2_3
show m_ace2_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0179
Ace "「はいはい、ユリウスも食べろよ。\n
これ、美味しくできたんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0009
Julius "「おまえはまた、校内でこんな……。\n
学園広しといえども、狩猟やキャンプをして生活しているようなのはおまえくらいのものだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0010
Julius "「風紀委員のくせに率先して風紀を乱しているようなもので……。\n
聞いているのか、エース！？ちゃんと食堂を利用しろと言っているだろう！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0180
Ace "「だってさあ、辿り着けないんだから、仕方がないだろう？\n
そんなに言うなら、迎えに来てよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0011
Julius "「だから、こうして……。\n
……だが、おまえを毎回探し出すなど、私でも無理だ」"

play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0181
Ace "「うんうん。\n
だから、たまにでいいよ……、はい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースとユリウスが、どこかで聞いたような会話を繰り広げている。\n
つい先刻、私とも同じような会話をした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう考えると、私はエースに気に入られたのだろうか。\n
付き合いの長いユリウスと、同じような扱いで受け入れられている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは、エースから串焼きを受け取ると、さっそくそれを口に運んだ。\n
私と同じように、食欲には敵わなかったのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それほど、この焼き鳥はおいしそうな匂いがする。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0012
Julius "「……美味い」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0182
Ace "「だろう？いい獲物が手に入ったんだ！\n
やあ、今日は俺ついてるぜ！」"

hide m_ace2_4
show m_ace2_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「あ、ユリウス、スープもあるのよ。\n
私はもう終わったから、あなたも食べるといいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の食べ終わった後の水筒の内蓋に、今度はユリウスの分をよそう。\n
洗ってから使わせてあげたいところだが、キャンプライフではそうもいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0013
Julius "「ああ、ありがとう。\n
だが、おまえはもういいのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「私は、もう食べ終わったの。\n
それに門限が近いんでしょう？」"

hide m_ace2_5

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「帰らなくちゃ。\n
係の人に心配をかけちゃうわ」"


show ace_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice ace_g0183
Ace "「俺と一緒だから、門限は平気だよ……、と言いたいところだけど。\n
送っていくよ、夜道は危ないからね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……平気よ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夜道、とはいっても、寮はすぐそこだ。\n
何かあるとはとても思えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……むしろ、一緒に行くほうが時間的な意味で危なさそう）"

hide ace_m_03_9
show ace_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice ace_g0184
Ace "「旅には、いつだって危険がつきものなんだぜ？\n
ましてや、今は夜間」"

hide ace_m_02_6
show ace_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice ace_g0185
Ace "「俺は清く正しい風紀委員だからね。\n
女の子一人で夜道を歩かせるなんて、風紀委員としてあるまじき行いだと思わないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……{size=+20}思わないけど？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつから、歩いて五分の距離が、そんな大層なものになったのか。\n
しかし、エースはまったく聞き入れてくれない。"

hide ace_m_02_10
show ace_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0186
Ace "「というわけで、ユリウス。\n
俺ちょっと行ってくるな」"

hide ace_m_03_10
show ace_m_03_10 at left
with dis

show yuri_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0014
Julius "「ああ、行って来い。\n
私も、食べ終わったら適当に捜索に戻る」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひらりと、ユリウスは気のない様子で答えながらも見送るように手を振ってくれた。"

play sound se_0007 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は立ち上がって、制服のスカートの裾をはたはたと叩く。"

play sound se_0624
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "茂みの向こうの道へと向かいながら、ふと疑問に思い、振り返った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ところで、ユリウス。\n
ユリウスの探し物って何なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、帰り道で見掛けるかもしれない。\n
そうでなくとも、明日からの学校生活の中で見掛けることもあるかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（せっかくだし、聞いておいたら役に立てるかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを思ったからこその、質問だった。\n
善意からの。"

hide yuri_m_02_10
show yuri_m_03_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0015
Julius "「ん……、ああ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスはスープを美味しそうに味わいながら、顔を上げた。"

hide yuri_m_03_8
show yuri_m_01_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0016
Julius "「シュトレーゼ教授からいただいた珍しい魔法生物を、担当の生徒が誤って逃がしてしまったんだ。\n
それを探している」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「へえ。\n
危険な魔法生物なの？」"

hide yuri_m_01_9
show yuri_m_01_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice jul_g0017
Julius "「いや、危険はないな。\n
四枚羽の鳥のような姿をしている、珍しい魔法生物なんだが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（…………）"


play music gag1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……{size=+20}よんまいばね？{/size}」"

hide yuri_m_01_13
show yuri_m_03_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice jul_g0018
Julius "「なんだ、見かけたのか？\n
場所を教えてくれ、捕獲の参考にさせてもらう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……その必要は、もうないと思うわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう、ない。\n
すでに、取り戻しようがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もうすでに、取り戻しようのない場所……、私達の胃袋の中に収まってしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「えっと……。\n
ごめん、気のせいだったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、そっとユリウスから視線をそらした。\n
その珍しい魔法生物を、捌いて焼いて食したなんて、どの口で言えるだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、今現在も、ユリウスが食しているものが……。\n
例の、それ、だろう。"

hide ace_m_03_10
show ace_m_01_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0187
Ace "「はは。今日はついてると思ったのに……。\n
俺って結局、いつもついていないんだよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……あなた、少しはおかしいと思わなかったの？\n
四枚羽の鳥なんて……」"

hide ace_m_01_2
show ace_m_03_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice ace_g0188
Ace "「あー、駄目だぜ？\n
そうやって人のせいにばっかりしていると……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「半分以上あなたのせいよ。\n
私に会った段階でほとんどシメかけていたでしょう……！？」"

hide ace_m_03_4
show ace_m_03_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0189
Ace "「食べた時点で、同罪。\n
だろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「う……！？\n
まさか、あなた、まずいかもしれないと思って、私を巻き込んだんじゃ……」"

hide ace_m_03_12
show ace_m_02_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice ace_g0190
Ace "「はは、そんな小賢しいこと、健全な風紀委員たる俺には無理無理。\n
だけど、君もユリウスも同罪に出来たって点ではついてるのか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「やっぱり、確信犯じゃないの、それ……！？」"

hide ace_m_02_10
show ace_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice ace_g0191
Ace "「いやいや、まさか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースと私は肘でつつきあって、互いに責任を押し付けあう。\n
醜い争いだ。"

hide yuri_m_03_2
show yuri_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「？？？」"

hide yuri_m_02_4
show yuri_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0019
Julius "「なんだ？\n
おまえ達、何か知っているのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「し、知らないわ」"

hide ace_m_02_4
show ace_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_6")
voice ace_g0192
Ace "「う～ん。\n
実はさ～……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は何か口走りかけたエースの頭をどついて、黙らせておく。"

play sound se_0118
camera at hpunch
camera at vpunch
hide ace_m_03_7
show ace_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0193
Ace "「いった……！\n
乱暴だなあ、なんだよ、ユリウスが怖いのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「怖いに決まっているわよ……っ！\n
あんたこそ、罪悪感ってものはないの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小声でぽそぽそと言い合いながら揉めている私達を他所に、ユリウスはスープを完食して満足そうに息をついた。"

hide yuri_m_03_9
show yuri_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0020
Julius "「おまえ達……。\n
寮へ帰るんじゃなかったのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「え……っ！\n
えへへ……、あはは……」"

hide yuri_m_01_5
show yuri_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
Julius "「……？」"

hide yuri_m_03_11
show yuri_m_02_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice jul_g0021
Julius "「……なんだ、不気味だぞ？\n
エースの真似か？」"

hide ace_m_02_8
show ace_m_03_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice ace_g0194
Ace "「え～？\n
なんだよ、それ、俺が不気味ってこと？」"

hide yuri_m_02_3
show yuri_m_03_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice jul_g0022
Julius "「ふん、いちいち確認をとらないと分からないのか？\n
その通りだ」"

hide yuri_m_03_1
show yuri_m_01_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice jul_g0023
Julius "「……ところで、話は変わるが、この鳥はなんだ？\n
今まで食べたことがない味だ」"

hide ace_m_03_9
show ace_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice ace_g0195
Ace "「はは、残念なんだけどユリウス。\n
{size=+20}話、変わってないんだ{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さらっと白状したエースに、私はさあっと青ざめる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスはエースの言葉の意味を取りかねたのか、眉を寄せている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、彼は賢い。\n
エースと違って、いちいち確認をとらなくても自力で分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、思い当たったのか……。"

hide yuri_m_01_9
show yuri_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「……っ{size=+20}！！！！！{/size}」"

play sound se_0052
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、がばっと立ち上がった。"

hide yuri_m_03_3
show yuri_m_03_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0024
Julius "「おまえ達、まさか、これ……っ！？\n
エース！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おまえ達と言いつつ、エースと限定する。\n
さすが、付き合いが長いだけあって、分かっているようだ。"

hide ace_m_03_3
show ace_m_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0196
Ace "「ユリウスも食べたから、共犯だよな！\n
というわけで、俺はちょっと彼女送ってくるから、お説教はその後にな！」"

hide yuri_m_03_12
show yuri_m_03_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0025
Julius "「説教ですむか！」"

hide ace_m_01_4
show ace_m_03_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0197
Ace "「はははは。\n
落ち着けよ、美味しかっただろ？」"

hide yuri_m_03_12
show yuri_m_01_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0026
Julius "「誰が、味の話をしているか……！」"

hide ace_m_03_11
show ace_m_01_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0198
Ace "「え～？してただろ？\n
美味しい、ってさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの怒号を背後に、エースは私の背を押すとその場を逃げ出した。"

play sound se_0621
hide ace_m_01_1

hide yuri_m_01_8

with dis
$ hi_mes()

scene bg20_gd_nig
with stripe_l_medium

scene bg_par15_rg_ros_nig
with stripe_l_long

play music school_front_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま、ばたばたと走って赤薔薇寮の入り口まで辿り着く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "送ってくれるという話だったが、エースに任せるとどこに連れて行かれるのか分からない。\n
私が先に立ち、その手を引く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キャンプ地点から、赤薔薇寮までの所要時間は大体五分程度。\n
本当に、近いのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、その間に、エースが近道と称してあらぬ方向へ突撃しかけた回数、数知らず。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……どうりで、迷子になるわけだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これだけ壊滅的な方向感覚を持っていながらも、本人だけは根拠のない確信を胸に突き進もうとするのだから始末に悪い。"


show ace_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0199
Ace "「今日は、楽しかったよ。\n
ありがとうな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……楽しかった？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "礼を言われる覚えはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ユリウスに殺されないといいわね」"

hide ace_m_03_10
show ace_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice ace_g0200
Ace "「大丈夫だよ、ユリウスは優しいからな。\n
怒っても、怒るだけ怒ったら許してくれるんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……やっぱり、確信犯じゃないの、この人）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ふうん……？」"

hide ace_m_02_10
show ace_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice ace_g0201
Ace "「だから、安心して怒られてくるよ。\n
……でも美味かったよな、アレ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「……ええ、びっくりするぐらい美味しかったわ。\n
ユリウスには悪いけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "珍しい魔法生物を、思いがけず口にしてしまったわけだが、あの味は忘れられそうにない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔を合わせ、なんとなく、笑ってしまう。\n
馬鹿げているが、希少な体験だ。"

hide ace_m_02_1
show ace_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0202
Ace "「ははっ、また遊んでくれよな。\n
一緒に冒険しよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ、またね。\n
……帰ってこられる範囲での冒険なら、付き合ってあげてもいいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日帰りできる程度の範囲で、との私の言葉に、エースは爽やかに笑って見せた。\n
彼は、私が寮のエントランスに入るのを見届けると、来た道を戻っていく。"

play sound se_0624
hide ace_m_03_3


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "来た道、といってもどこまで辿れるのかは分からない。\n
月に照らされた夜道を、ゆらゆら遠ざかる背中を見送る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（次は、いつ会えるのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスのところへ戻れるのかどうかも、怪しいもの。\n
説教を避けられるという点では、確信犯でなくともタチの悪い男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放浪癖のある彼の背中に、そんなことを思った。"

with dis
$ hi_mes()

scene bg_par15_rg_ros_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_ace3
