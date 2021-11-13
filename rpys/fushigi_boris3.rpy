jump fushigi_common3_tower
label fushigi_boris3_1:

scene charasel_bg_tower_day
with stripe_l_medium

scene n_01
with stripe_l_long

play music tower_inside_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔の執務室、書類の山と戦っているナイトメア。\n
そして、それを監視しているグレイに、小声で話しかける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「グレイ、次のお休みっていつかしら？」"


show gre_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0093
Gray "「[firstname]？\n
どうしたんだ唐突に……、まさか、何か問題ごとでも」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あ、違うのよ。\n
何かで困っているとか、そういうことじゃないの」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（この前の件でますます過保護にさせちゃったわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "役なし達に攫われそうになったことは、私にとっては自業自得なのだが、グレイにとっても苦い記憶を残してしまったらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は私を一人で行かせたことに責任を感じている。\n
出掛けようとすると、仕事を放ってでも付き合おうと提案してくるくらいだ。"

hide gre_t_02_4
show gre_t_02_4 at left
show nai_s_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0214
Nightmare "「いいぞ、[firstname]。\n
グレイでよければ、いつでも貸し出してあげよう」"

hide nai_s_01_11
show nai_s_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0215
Nightmare "「ボディガードにはもってこいの男だからな。\n
ただ……、どうせなら私を誘ってほしかったんだが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（そういうことは目の前の仕事の山を片付けてから、言いなさい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "話に入ってくる相手に、心の中で返す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの机は、いつでも書類の山で覆われている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "片付くのがいつになるのか分からないほどの……、大量の仕事だ。\n
仕事が出来ない領主ではないのだが、とにかく彼は気分にむらがありすぎる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（グレイの休みだって、あんたの仕事の進行状況で変わるんでしょうが）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_14")
T "（集中してやりなさいよ、集中して！）"

hide nai_s_02_4
show nai_s_03_6 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice nig_f0216
Nightmare "「うっ……、酷い。\n
私だってたまには君と出かけたっていいじゃな……」"

hide gre_t_02_4
show gre_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice gra_f0094
Gray "「俺としては、この書類をすべて片付けて下さるのなら、いくらでも休憩を取って頂いて構いません」"

hide gre_t_03_9
show gre_t_01_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice gra_f0095
Gray "「ただし、これ以上仕事が滞るようだと……、俺も、大変、困るんです」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアが言葉を言い切る前に、グレイが口を挟む。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉そのものに棘はないのだが。\n
グレイの言葉には、逆らえない雰囲気があった。"

hide nai_s_03_6
show nai_s_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Nightmare "「…………」"

hide nai_s_02_9
show nai_s_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nig_f0217
Nightmare "「大人しく、仕事をしています」"

hide gre_t_01_13
show gre_t_03_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0096
Gray "「ええ、よろしくお願いします」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（よろしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たじろいだナイトメアは、意識を仕事に戻したようだった。"

hide gre_t_03_4
show gre_t_02_2 at center
hide nai_s_01_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0097
Gray "「そうだな……、ナイトメア様の進行次第だが、次の次の時間帯には一度休憩に入れる予定だ。\n
君の都合に合うだろうか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「大丈夫よ。\n
居候をしているだけだもの、グレイに合わせるから」"

hide gre_t_02_2
show gre_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Gray "「……[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あのね、一緒に出かけてほしいところがあるから、付き合ってちょうだい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不思議そうに私を見るグレイの視線には応えず、私はポケットの中に入れておいたものを確かめるように指で触れたのだった。"

hide gre_t_02_10

$ hi_mes()

scene n_01 with Dissolve(.8)

scene charasel_bg_tower_day
with stripe_l_medium

scene bg_gen_sky_win_day
with stripe_l_medium

scene bg_gen_sky_win_nig with Dissolve(1)

play music forest_town_square_p_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice suz_f0003
Customer "「この前あんたが売ってくれた軟膏だが、あれはよく効くな。\n
また頼むよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice sat_f0003
Customer "「それはよかった。\n
これからもご贔屓に……」"


play music forest_town_pub_p_ali

scene bg_gen01_gb
with dis
play sound se_0495 volume .8
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "街中を通り抜け、大通りから少し外れた黒い扉の店に足を踏み入れる。\n
そして私達は、互いに持ったグラスを触れさせた。"

play sound se_0359
pause .6

show gre_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

hide gre_t_01_12
show gre_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0098
Gray "「……外出したいと言うからどこかに行きたいのかと思ったんだが。\n
ここに来たかったのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ええ。\n
だって、この前はゆっくり出来なかったでしょう」"

hide gre_t_03_3
show gre_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gra_f0099
Gray "「いや、俺としてはそんなこともなかったんだが……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達が腰をかけているのは、この前グレイが連れてきてくれたバーのカウンター。\n
まばらな客の話し声も囁き程度で、ＢＧＭのように流れている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（砂時計を、持ってきてよかったわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすがに酒場に入るのに、昼の時間帯では味気ない。\n
入るときにこっそりと、ポケットに入れていた砂時計で、夜の時間帯に変えた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_6")
T "「この前、助けてもらったのにろくにお礼も出来なかったから……。\n
あ、でも、私と一緒じゃ休憩にならない？」"

hide gre_t_02_3
show gre_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_6")
voice gra_f0100
Gray "「いや、そんなことは。\n
むしろ、こんな場所に君のような子を連れてきていると……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「いると？」"

hide gre_t_03_9
show gre_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gra_f0101
Gray "「まるで俺が口説いているように見えるんじゃないかと、そんな気になってくる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_7")
T "（あ、相変わらず心臓に悪いことをさらっと言うわよね、この人）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイは含ませて言っているわけではないと分かっているのに、どきどきしてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一人で赤くなったり、青くなったりすると、かえって誤解を生みかねない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（落ち着かなくちゃ……）"

hide gre_t_02_1
show gre_t_02_1 at left
show master_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice tan_f0028
Master "「ああ、あんたか。\n
可愛い子を連れているね」"

hide gre_t_02_1
show gre_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gra_f0102
Gray "「ああ、この前は突然押しかけて悪かったな。\n
今回は、静かに飲みに来たんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "常連らしいグレイが、マスターに答えている。"

hide gre_t_03_9
show gre_t_01_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0103
Gray "「[firstname]、君は何かリクエストがあるか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今私が持っているグラスにしても、最初の乾杯用に出してもらったジュースだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "場所を考えれば、私もアルコールを頼むのが筋かも知れない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（でも、お酒を飲むのはちょっと……、ね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "家出してお邪魔している身の上には、分不相応というものだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「アルコールが入っていないものなら何でも」"

hide gre_t_01_4
show gre_t_03_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0104
Gray "「そうか、分かった。\n
マスター、少し借りるぞ」"

hide master_1
show master_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice tan_f0029
Master "「ああ、どうぞ。\n
珍しいな、あんたが立つなんて」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（グレイが立つ？）"

play sound se_0160 volume .6
hide gre_t_03_10

hide master_4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かにマスターの言うように、グレイは立ち上がると上着を脱いで、近くの椅子にかけた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのままカウンターの中に入ると、慣れた様子でカップなどを取り出していく。"


play music moon_night1_a_ali
play sound se_0170
play sound se_0545 volume .7
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？\n
グレイ、何をするの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（あれって、確かカクテルを作るときに使うシェーカーよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "金属の容器を持ったグレイは、私の質問に答えずにボトルをいくつか見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "やがて、その中から二つ三つ選ぶと、先ほど取り出したカップで計量し、蓋を閉め……。"


show gre_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

hide gre_t_01_13

play sound se_0233 volume .6
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それを上下に振り始めた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隣のマスターもやっている、カクテルのシェイク。\n
ただそれだけの動作だというのに、酷く似合っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_8")
T "（格好いいなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手慣れた動きにこれが初めてではないことはすぐに分かった。\n
だが、マスターの雰囲気では珍しい事態でもあるようだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（……料理はアレだけど、ココアはおいしく淹れられるんだし。\n
飲み物なら、大丈夫よね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "日頃の奇想天外（ナイトメア曰く人外魔境）な料理を知っているだけに、疑問が浮かんでしまう。"

play sound se_0233 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「慣れているのね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "シャイカーを振るグレイに声をかける。\n
すると、彼は微笑を浮かべて答えてくれた。"


show gre_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0105
Gray "「それほどのものじゃない。\n
ただナイトメア様の部下になるまでは、別に珍しくないことだったから」"

hide gre_t_03_6
show gre_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0106
Gray "「昔取った杵柄というやつだ」"

hide gre_t_02_8
show gre_t_02_8 at left
show master_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0030
Master "「いや、それでもいい手付きだ。\n
それに……」"

hide gre_t_02_8
show gre_t_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイの視線に、マスターは面白そうに続けた。"

hide master_1
show master_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0031
Master "「昔のあんたなら、間違っても作らない組み合わせの飲み物だな」"

hide gre_t_02_10
show gre_t_03_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0107
Gray "「……いつまでも昔と同じ扱いはやめてくれ。\n
[firstname]、君の分だ」"

play sound se_0213 volume .7
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？\n
わ、私の分だったの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "マスターとの会話を照れたように終わらせ、私の前にスッとグラスが置かれる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そういえば、グレイのグラスは既に準備されているのだ。\n
彼が自ら作ってくれたものは、私の飲み物だったらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（私のほうがお礼をするつもりだったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ご馳走になってしまう形になるが、断るのはもっと失礼だろう。\n
ありがたく頂くことにした。"

hide gre_t_03_3
show gre_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0108
Gray "「どうぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T "「……ありがとう」"

play sound se_0573 volume .6
hide gre_t_01_3

hide master_2


scene t_cut_bor3_1u
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グラスに飲み物が注がれると、その色に感嘆を漏らす。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「綺麗な色ね……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（カシスがベースなのかしら。\n
濃い赤だわ）"


scene t_cut_bor3_1
with dis

show gre_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0109
Gray "「アルコールは入っていないが、好みもあるだろうから、味見してくれるか？」"

hide gre_t_03_9
show gre_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0110
Gray "「気に入らなかったら……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「そ、そんなことないわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（若干の不安はあるけど……、色も綺麗だし、匂いも美味しそう）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「頂きます」"

hide gre_t_02_3
show gre_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「おいしい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジュースはジュースでも、甘すぎず、飲みやすい。\n
いかにも女性好みの飲み物だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（……慣れているんだろうな、女の人の扱い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "バーテンダーになるには、相当の修行が必要だと聞く。"

hide gre_t_02_9
show gre_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0111
Gray "「そうか、安心したよ」"

play sound se_0160
hide gre_t_03_4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "カウンターから戻ると、再び私の隣にグレイは腰を下ろした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分のグラスを手にとって、私のほうを見つめてくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（グレイがこういう場所に連れて来る女の人って、きっと誰も彼も綺麗な人よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "住民の暴走を本気で怒って家出してくるような私では、そもそも釣り合わない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だからこそ、こうして付き合ってくれるのだろう。\n
私も女性として扱われていると知っていれば、こんなところに誘ったりもしない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（そこまでしたら、さすがにボリスに悪いもの）"


show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_3")
Gray "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

hide gre_t_03_10
show gre_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gra_f0112
Gray "「君さえよければ……、このまましばらくクローバーの塔に住まないか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然の言葉に、首を傾げる。"

hide gre_t_01_14
show gre_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0113
Gray "「勿論、選ぶのは君だ、強制じゃない。\n
ただ……、君とこうやって静かにグラスを傾ける機会がこれっきりというのは寂しいと思ったんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T "「……グレイ」"

menu:
    "ありがとう。":
        jump fushigi_boris3_5a
    "気持ちは嬉しいけど……。":
        jump fushigi_boris3_5b

label fushigi_boris3_5a:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（突然押しかけたのに、この人はどこまでも面倒見がいいんだから）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ありがとう、グレイ。\n
私もあなたとこうやって過ごすのは楽しいわ」"

hide gre_t_01_11
show gre_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ふふふ。\n
前から思っていたけど、あなたって私に甘いと思うの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、甘えてしまう。\n
本当だったら、手放していいはずの子供に、ずっと構ってくれる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（格好よすぎて、私には不釣り合いよ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「駄目よ、こんな子、甘やかしちゃ。\n
調子に乗るから」"

hide gre_t_03_3
show gre_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice gra_f0114
Gray "「そんなことはないよ。\n
君が今飲んでいる、その飲み物」"

play sound se_0176
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「これ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが、指先でグラスを弾く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飲みやすさも手伝って、ジュースはもう半分ほどしか残っていない。\n
最初に懸念していた心配など何も感じさせない、ノンアルコールのカクテルだ。"

hide gre_t_03_8
show gre_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0115
Gray "「ああ。\n
君を元の場所に帰さないために、何か混ぜたかもしれない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（うそ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、今までにも彼はナイトメアの食事に何度も薬を混ぜたことがある。\n
大抵は悪化した味付けや匂いのせいで、食べる前に気付かれてしまうのだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（変な味なんて、何もなかったのに）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「……じょ、冗談でしょう？」"

hide gre_t_02_1
show gre_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice gra_f0116
Gray "「ああ、冗談だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（笑えないわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "すぐに答えてくれた相手に、ほっと息をついたのも短い間。\n
私のグラスを手にしたグレイは左右に揺らしながら、困ったように笑う。"

play sound se_0211 volume .6
hide gre_t_02_2
show gre_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0117
Gray "「だがな、[firstname]。\n
俺のようなろくでなしなんて、この世界にはごまんといる」"

hide gre_t_03_6
show gre_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0118
Gray "「君の滞在地を知りながらも、不埒な真似をしようと考える奴は少なくない。\n
あんまり簡単に男を信用しすぎないほうがいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……はい、分かりました」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（やっぱり、この人、根本的に面倒見がよすぎるのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬感じたときめきさえも、保護意識からだと分かれば淡く消えてしまうもの。\n
それはまるでグラスの中に浮かぶ、氷のように。"

hide gre_t_02_13


scene bg_gen01_gb
with dis
jump fushigi_boris3_6
label fushigi_boris3_5b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「気持ちは嬉しいけど……、いつまでもいたら、私、ますます甘えちゃうわ」"


show gre_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ナイトメアはああだけど、意外としっかりしているし。\n
長くいればいるだけ、グレイにも、ユリウスにも寄りかかっちゃいそうだもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帰る場所がある。\n
いつかは戻らなくちゃ行けない場所がある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思っているからこそ生まれる、気楽さと開放感。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（居心地のよさにただ甘えるだけなんて、だらしないわ）"

hide gre_t_03_3
show gre_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice gra_f0119
Gray "「君が甘えている……、か？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「甘えているわよ。\n
だって、現に休憩中のグレイと夜遊びをしているぐらいだもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼がいなければ、この近くに来ようなんて、思わなかったかもしれない。\n
この前の失敗は、私にとっても苦いものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（寄りかかっちゃいけないのに、甘えを許してくれる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この人は私の恋人でもなんでもない。\n
気の合う貴重な、そして大切な友人だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（こういう大人の雰囲気のあるお付き合いに、私なんかじゃ不釣り合いだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「ねえ、グレイが嫌じゃなかったら、また……。\n
一緒にこうして座ってくれる？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「お酒が似合うような大人の女じゃないけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "静かな空間で、ゆっくりとグラスを傾ける。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも賑やかな遊園地で過ごしているからこそ感じる、空白の間が、妙に愛おしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（この世界に来るまでの私だったら、考えられもしなかったけど）"

hide gre_t_02_4
show gre_t_02_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice gra_f0120
Gray "「……ああ、喜んで。\n
いや、そうしてくれるのなら、俺も嬉しい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分のグラスを手に取ったグレイは、私のグラスにそれを合わせた。"

play sound se_0359
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼に習って、私も同じようにグラスを触れ合わせる。\n
心地よい音が、耳の奧にじんと残った気がした。"

hide gre_t_02_14


scene bg_gen01_gb
with dis
jump fushigi_boris3_6
label fushigi_boris3_6:
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music forest_town_pub_p_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice chi_f0042
Cat "「みゃあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あなた、また来たの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しばらくノンアルコールカクテルを楽しんでいると、足元に擦り付く感触がある。\n
下を覗けば、またあのピンクの猫がいた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「ふふふ、おいで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "招くように手を伸ばすと、猫は軽々と私の膝へと飛び乗ってきた。"

play sound se_0134 volume .6

scene t_cut_bor3_2u
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0043
Cat "「みゃあ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（……飼い猫なのかな）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（お腹が空いているようにも見えないし。\n
今回も、カウンターの上の食べ物には見向きもしないものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だからといって、普通の飼い猫のようにも見えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首輪も見てみたが、ネームタグのようなものは付いていなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（やっぱり……、似ている気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "縞模様のあるピンクの毛並みが、どうしても気になってしまう。"


scene t_cut_bor3_2
with dis

show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0121
Gray "「君の膝の上が本当に好きなんだな。\n
居心地よさそうにしている」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「だったらいいんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（……気のせいかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の膝の上で大人しくしている猫が、グレイの手を警戒するようにじっと見ている気がする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（よっぽどグレイが苦手なのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "動物は自分を気に入ってくれているのかいないのかを、本能的に察する。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "猫は気紛れな性格もあってか、犬のように顕著ではないはずだが……、どうにもグレイに対して一線を引いている。"

hide gre_t_01_4

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0044
Cat "「みゃあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「うん？\n
また撫でてほしい？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_1")
voice chi_f0045
Cat "「みゃあ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T "（喋れなくても、だいたい何をしてほしいのか分かるっていうのも、変な感じ）"

show t_bor3_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "要望に応えるようにその背中を撫でてやると、猫は気持ちよさそうにのどを鳴らした。\n
長い尻尾もゆったりと動いている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "機嫌のいい証拠だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（ボリス、どうしているかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この猫に触っていると、つい彼のことを考えてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（また、危ない遊びをしていなければいいけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界では、銃や刃物など珍しくもない。\n
役持ちと呼ばれる彼も、怪我をして帰ってくることがよくあった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（……最近は大分減ったけど、ゼロにはならない）"

$ hi_mes()
hide t_bor3_1
show bg_gen01_gb_s onlayer master
with dis
hide bg_gen01_gb_s
show yug_01_s onlayer master
with dis

scene yug_01 with dis
hide yug_01_s


play music amuse_guestroom_p_ali

show bor_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_f0230
Boris "「いてっ……、ちょ、ちょっと、[firstname]。\n
いいって、どうせ放っておけば治るから」"

hide bor_t_01_8
show bor_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_f0231
Boris "「みぎゃっ！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「放っておけば治る傷なんでしょう。\n
だったら、これぐらいで泣き言を言わないのっ」"

play sound se_0424
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスの言葉を確かめるように手当てした場所を軽くはたくと、彼は涙目になった。"

hide bor_t_03_1
show bor_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「～～～～っっ！！」"

hide bor_t_01_3
show bor_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0232
Boris "「ひ、酷いなあ。\n
それに今回のは俺だけじゃなくて、ディーやダム達だって悪いんだぜ」"

hide bor_t_01_9
show bor_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0233
Boris "「あいつら、仕事サボってＮｏ.２さん用にまた罠を仕掛けていたんだけど、ちょっと火薬が暴発してさ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（ちょっと暴発？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞き捨てならない台詞に、思わず顔が引きつる。\n
ボリスの身体には、小さいものとはいえ、あちこちに火傷が出来てしまっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見ているだけでもひりひりと痛そうな姿だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（ちょっとですむようなレベルじゃないわ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「……あの子達も危ないことばかりするんだから。\n
ボリスも気を付けて」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（遊びに行ったと思ったら、怪我して帰ってくるんじゃ、心配だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋に訪ねて来てくれるのは嬉しいが、傷だらけで戻って来られるのは不安だ。\n
ベッドに座った相手に包帯を巻きつけながら思う。"

hide bor_t_02_8
show bor_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0234
Boris "「でもさ、結構どきどきするんだよなあ。\n
こう……、ちょっと火花が出ただけで、どん！といくあの感覚」"

hide bor_t_02_3
show bor_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0235
Boris "「銃の改造中にも思うんだけどさ、どっちに転ぶか分からないあのスリリングさ。\n
ぞくぞくするだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T "（それで怪我を作って帰ってこられたら、私のほうが堪らないわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界は、皆して誰でも代えがきくのだと告げる。\n
それが当たり前で、絶対の真理だというように。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_3")
T "（でも、そんなことない）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「じゃあ、私が同じことしてもいいわよね？」"

hide bor_t_01_10
show bor_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice bor_f0236
Boris "「え？同じことって……。\n
あんたがあいつらと一緒に落とし穴掘ったり、爆薬仕掛けたり、お礼参りしたりするの？」"

hide bor_t_02_10
show bor_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice bor_f0237
Boris "「いやいや、やめておけって。\n
絶対に怪我だけじゃすまないからっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（……あんた達、一体どんな遊びをしているのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "聞くだけで痛くなるような物騒な遊びは控えてほしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「そこまで具体的じゃないけど……。\n
もし、私が怪我して帰ってきたら、ボリスはどう思うの？」"

hide bor_t_01_2
show bor_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
voice bor_f0238
Boris "「どう……って、決まってるだろ。\n
すごいムカムカする」"

hide bor_t_01_11
show bor_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
voice bor_f0239
Boris "「あんたは俺のなのに、怪我させるなんて……、許せるはずがない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「私だって同じよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこまではっきり分かってくれていて、どうして自分は同じ行動を取るのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "好きな人が傷ついた姿で帰ってきて、何とも思わないはずがない。\n
私と同じ答えが得られたことに、嬉しいとも思う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（でも、互いに嫌な気分になるなんて、不毛すぎるじゃない）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「私だって、ボリスが怪我をして帰ってきたら、面白くない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（……遊びに行って傷付いてくるくらいなら、ここにいていいのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉には出来なかったが、手当てを終えて、相手をぎゅっと抱きしめる。"

hide bor_t_03_9
show bor_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「！！！？」"

hide bor_t_01_1
show bor_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0240
Boris "「[firstname]？\n
なに、俺のこと、飼ってくれる気になった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "{size=+20}「ならないわよ」{/size} "

hide bor_t_01_5
show bor_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice bor_f0241
Boris "「ちぇ。\n
ようやくその気になってくれたのかと思ったのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「そういう趣味はないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスを飼う気なんてない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（だいたい、好きな人……、猫だけど、その相手を飼うって何よ。\n
飼うって）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それに、飼い猫というくくりは、ボリスに似合わない。\n
彼はいつでもふらふらと出歩いているほうが彼らしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_13")
T "（じっとしているボリスはボリスらしくないわ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「前に本で読んだんだけど……。\n
猫って、飼い主じゃなくて、家につくものなんですって」"

hide bor_t_03_13
show bor_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
Boris "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「ボリスだったら、どんな家がいい？\n
どんな家だったら……、住んでくれる？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（どんな家だったら、あなたは……。\n
私の家に戻ってきてくれる？）"

hide bor_t_01_11

$ hi_mes()

scene yug_01 with Dissolve(.8)

scene yug_01_s
with dis

scene bg_gen01_gb_s
with dis

play music night_room_p_ali

scene bg_gen01_gb
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（あのとき、ボリスはなんて言ってくれたんだっけ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "覚えていようと思っていたはずなのに、振り返るとすぐには思い出せない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0046
Cat "「にゃあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……あなたにも、いたいと思う家がある？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私のいたいと思う場所。\n
戻りたいと思う場所は、彼のいるあの空間だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「……グレイ」"


show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
Gray "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼とここに来ようと思った理由。\n
それをようやく口に出来るだけの整理が付いた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「私、そろそろ遊園地に帰ろうと思うの」"

hide gre_t_03_10
show gre_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0122
Gray "「……そうか。\n
君がいると、周りが華やぐから……、寂しくなるな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "眼を細めて私を見ているグレイの言葉は、とても残念そうだ。\n
改めて滞在させてもらった場所の居心地のよさを実感してしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（そう言ってくれるのは、とっても嬉しい。\n
でも……、私の帰る場所は、塔じゃない）"

hide gre_t_02_7
show gre_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice gra_f0123
Gray "「君の帰宅が近いと知ったら、ナイトメア様も寂しがりそうだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「次の時間帯には、ナイトメアやユリウスにもちゃんと話をして……。\n
それから戻ろうと思っているわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが何気なく口にした言葉に、思わず口元がほころんでしまう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Cat "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あなたも、帰る家があるんでしょう？\n
そろそろ帰ったほうがいいわ、皆、心配するから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "膝の上で丸くなったままの猫にそう声をかけると、ピンクの猫は身体を伸ばした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま私の顔に口を寄せて、ぺろりと舐めていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ざらざらした感覚に思わず顔がほころんでしまうのは、遠い彼の反応を思い浮かべてしまったから。"


show t_bor3_2 onlayer master
with dis
hide gre_t_02_12

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（ボリスにばれたら、ヤキモチ焼かれるのかしら、これも）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頬にキスをするように舐められて、そんなことを考える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "元の世界では猫のダイナを飼っていたという話をしてから、ボリスは他の猫と私が仲よくすることにいい顔をしない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（……まあ、いいか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピンクでふわふわもこもこの毛並み。\n
ボリスによく似ている、不思議な猫。"

hide t_bor3_2

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Cat "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いきなり飛び降りてしまった猫を追いかけるように手を伸ばしたが、小さな生き物はそのまま早足に離れていってしまった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帰ったほうがいいと言っておきながら、自分の手の届かないところに行ってしまうことが、妙に寂しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（私の飼い猫でもなんでもないのに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（いや、別にボリスだって私が飼っているわけじゃないけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「あの子、柔らかくて、気持ちよかったけど、仕方ないわよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの猫が膝の上にいるときには、まるでボリスが一緒にいるように、とても落ち着けた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "急に体温がなくなった膝の上は、すうすうしている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（でも、ちゃんと帰る場所があるなら、そのほうがいい）"


show gre_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0124
Gray "「結局、触らせてもらえなかったな。\n
残念だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「ふふふ、そうね」"

hide gre_t_01_14

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぬくもりの残りに眼を細めながら。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（今頃、ボリスは何をしているんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことを思った。"

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music forest_town_road_p_ali
play sound se_0180

scene bg_gen_sky_win_eve
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ご馳走様」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice tan_f0032
Master "「どうも、よかったらまたおいで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "会計をすませて、店の外に出ると、ちょうど時間帯が変わった。\n
濃い紺色の空は、今、橙色の鮮やかな色に染まっている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「グレイ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔へ歩き出したところで、後ろに立っていたグレイが静かに私の名前を呼ぶ。\n
無言のまま、彼は一点を見つめていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T "（誰かいるの？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！」"

show t_bor3_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ボリス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私達から少し離れた場所にある、小さな公園。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこにピンク色の猫がいた。\n
店に背を向けるようにして、ベンチの背もたれに腰を下ろしているので、背中がよく見える。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさか、私達に気付いていないということはないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（いつから、近くにいたんだろう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "疑問を覚えながらそっと歩き出すと、グレイが付け加えるように口を開いた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0125
Gray "「今の時間帯なら、ひとけのない場所に行かなければ大丈夫だろう。\n
話があるなら行っておいで、俺は先に塔に戻っているから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「……グレイ。\n
ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "短く礼を告げて、私は彼の元へと足を向けた。"

$ hi_mes()
hide t_bor3_3


$ time_effect()##PLEASE MANUALLY ADJUST ME

scene bg_gen06_ck_win_eve
with dis

play music quiet_night_a_ali
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（何をしているのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "猫はいつだって気紛れ、好きなときに好きな場所に行く。\n
それは彼の口癖のはずだが、今のボリスは落ち込んでいるように見えた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「ボリス……。\n
その、久しぶり」"


show bor_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
Boris "「[firstname]」"

hide bor_t_02_10
show bor_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice bor_f0242
Boris "「うん、久しぶり。\n
元気だった？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り返った相手の顔を見ると、先ほどの猫と被る。\n
しかし、数時間帯ぶりに見るボリスの顔を、懐かしいとも思った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「そうね、私はいつも通りだったかしら」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（嘘ばっかり）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "離れていても、彼のことばかり考えていたのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "戻ったらボリスとこんなことをしよう、ボリスとあんなことをしよう。\n
そう思っていた時間帯は、決して少なくなかった。"

hide bor_t_01_10
show bor_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0243
Boris "「俺は、最悪だったな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「どうしたの、また怪我をしたとか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "素直になれない私とは対照的に、相手は呟く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ生傷が絶えないボリスだ。\n
見えないだけで、どこか怪我をしているのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（そんなときにいなかったなんて）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ち込む私の顔を見て、彼は慌てて首を横に振った。"

hide bor_t_03_5
show bor_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0244
Boris "「あ、違う、違う。俺になんかあったからじゃなくて……。\n
あんたのことで、色々落ち込んでさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「……？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（私のこと？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒らせたことをそんなに気に病んでいたのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何度か瞬きを繰り返すと、ベンチから下りてボリスが、傍に寄ってくる。\n
見上げると、頬に指で触れられた。"

hide bor_t_01_2
show bor_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0245
Boris "「[firstname]。\n
あんた……、殴られたって、本当？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（ど、どうして知っているの！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぞっとするほど低い声に、私の背筋まで凍りつく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの一件について知っているのは、私とグレイ、そして心が読めるナイトメアだけのはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "笑って誤魔化そうかとも思ったが、ボリスの眼は確信に満ちている。\n
とても誤魔化せる雰囲気ではなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「……どこでそんな話を聞いたの？」"

hide bor_t_01_11
show bor_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
voice bor_f0246
Boris "「そんなのどうでもいいよ。\n
大事なのは、俺のものに手を出した奴がいるってこと」"


play music heartrending_a_ali
show t_bor3_4 onlayer master
with dis
hide bor_t_02_12

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ボリス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "労わるように、頬を舐められる。\n
ふと、先ほどの猫を思い出した。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0247
Boris "「すげえ頭に来たし、絶対に撃ち殺してやるって思ったけど……。\n
あんたが大変なときに一緒にいなかったなんて、最大の不覚だよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0248
Boris "「……格好悪い」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ち込んでいるといった言葉は本当なのだろう。\n
その表情は、どこか本音を掴ませないボリスらしくない顔だった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「ボリス」"

hide t_bor3_4
show t_bor3_5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "落ち込んでいる彼を治したいと思ったら、同じような行動に出ていた。\n
淋しそうな目をしているから、目蓋を舐めてみる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……何？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice bor_f0249
Boris "「何って……。\n
だって、あんたがこういうことするのって……、何だかすごい気がして」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（それもそうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人っきりの部屋でなら、もっと密着することも珍しくないが、ここは屋外の公園。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰の目があるかも分からないような場所だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「驚いた？」"

hide t_bor3_5


show bor_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice bor_f0250
Boris "「驚いたっつーか……、うん、驚いた。\n
何か、キスするのもいいけど、こういうのもいい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "喉を鳴らすようにして、ボリスが顔を寄せてくる。"

hide bor_t_01_7
show bor_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0251
Boris "「なあ、[firstname]。\n
遊園地に戻って来いよ」"

hide bor_t_03_9
show bor_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0252
Boris "「あんたがいないのは、もう限界。\n
これ以上離れていたら……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「寂しくて死んじゃう？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_13")
T "（それじゃあ、ウサギじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず浮かんだ自分の考えに、笑いが込み上げる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あれだけ派手に喧嘩をして飛び出してきたはずなのに。\n
久しぶりに会ったら、怒るどころじゃなくなっているなんておかしな話だ。"

hide bor_t_03_13
show bor_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0253
Boris "「猫は寂しくて死んだりはしないけどさ。\n
あんたがいないと、今以上に格好悪くなりそう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「……何よ、それ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスは今だって十分すぎるほど格好いい。\n
格好悪いなんて思わない。"

hide bor_t_01_9
show bor_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0254
Boris "「格好悪いよ。\n
土下座してでも何でも、あんたに帰ってきてほしいって思っているし……」"

hide bor_t_01_3
show bor_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0255
Boris "「あんたの姿が見えないときにまた酷い目に遭っていたら……、堪らない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「心配した？」"

hide bor_t_01_9
show bor_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice bor_f0256
Boris "「……すげえ心配した。\n
クローバーの塔に押しかけてでも、あんたを連れて帰ろうと思ってたんだから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（ボリスがここまで寂しがるなんて、思わなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一時、遊園地がなくなったときでさえ、ボリスは飄々とした態度を崩さなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（それは……、私がいたからだと思っても、いいのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勝手に期待をして、裏切られるのは怖い。\n
そう思うからこそ、ボリスが素直に言葉で表現してくれると嬉しいと思う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「反省もした？」"

hide bor_t_03_13
show bor_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice bor_f0257
Boris "「……山ほど。\n
おっさんの音楽が頂けないのは変わらないけど……」"

hide bor_t_03_6
show bor_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice bor_f0258
Boris "「あんたがいないことに比べたら、あの地獄の雑音を聞かされるほうが、千倍マシだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「ボリス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小指を出した私に、ボリスはきょとんとした顔を見せる。"

hide bor_t_01_8
show bor_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「約束するわ。\n
次の次の時間帯には、遊園地に帰る」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_19")
T "（だから……。\n
これ以上、寂しがらないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の提案に一瞬目を輝かせたボリスだったが、ふと気付いた様子で口を開いた。"

hide bor_t_02_7
show bor_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0259
Boris "「え……、次の次って。\n
いいだろう、今すぐ帰ろうぜっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「駄目よ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然転がり込んできた私を受け入れてくれたグレイ達に、それはあまりに失礼というものだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きちんと礼を告げてからでないと、帰ろうとは思えない。"

hide bor_t_01_4
show bor_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0260
Boris "「えー……、俺、今回こそはあんたと帰るつもりで来たのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……あんまり言うなら、帰る予定をもっと遅くするわよ」"

hide bor_t_02_13
show bor_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
Boris "「！！」"

hide bor_t_01_1
show bor_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice bor_f0261
Boris "「分かった、分かったから！\n
そんなに睨まないでよ……」"


play music transparent1_a_ali

show t_bor3_6 onlayer master
with dis
hide bor_t_03_11

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "指を絡めてきたボリスは、そのままもう一度私に顔を寄せてくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0262
Boris "「その代わり、戻ってきたらずっと俺の傍から離さないから。\n
覚悟、しておきなよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声と一緒に、首に巻いていたファーが私の頬に触れた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T "「……ええ」"


scene bg_gen_sky_win_eve with dis
hide t_bor3_6

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（やっぱり、似ている気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あのバーに行ったときに出てきた猫の毛並みと、ボリスのこれはとてもよく似ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "温かさも、優しさも。\n
ずっと触れていたいと思わせる。"

$ hi_mes()



scene bg_gen_sky_win_eve with Dissolve (.8)

scene map_bg_winter_eve with Dissolve(1.2)
##endmemory
label fushigi_end_check_amuse1_b:
if renpy.seen_label("fushigi_end_gowland1") == True:
    jump fushigi_end_check_amuse2_b
if renpy.seen_label("fushigi_end_boris1") == True:
    jump fushigi_end_check_amuse2_b
if renpy.seen_label("fushigi_end_pierce2") == True:
    jump fushigi_end_check_amuse2_b
else:
    jump fushigi_end_boris1

label fushigi_end_check_amuse2_b:
if fushigi_common3_tower2_boris2b_seen == True:
    jump fushigi_end_boris1
else:
    jump fushigi_end_amuse1
