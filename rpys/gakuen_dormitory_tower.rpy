label gakuen_dormitory_tower:
$ clockanim()

with dis
$ hi_mes()

scene bg_map_day
with dis

scene bg_par15_rg_tow_day with Dissolve(1.2)

play music gallery_front_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔、という名前や、元々は天文台だったという話。それらの事前情報から、勝手に古びた石造りの、文字通り「塔」といったような建物を想像していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、矢印に引きずられたようにして連れて行かれた「塔」は、私が想像したよりもはるかに近代的で、綺麗な建物だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（職員寮としても使われているわけだし、そりゃあそうよね。\n
機能的になっているわけだ……）"


show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice sat_g0057
Guide "「ささ、ここが塔だよ」"


scene bg25_rr_day with stripe_l_extralong

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ガイドに案内されて、内部へと足を踏み入れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "内装も綺麗なもの。\n
広さもある。"

play sound se_0058
hide guide_5
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0058
Guide "「さあさあ。\n
進もう」"

play sound se_0773
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ガイドはくねくねと身を泳がせて、私を引っ張っていく。\n
私の腕ほどのサイズしかないくせに、なかなかの力だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく塔の中を進むと、一際立派な扉が目に付いた。\n
ここが目的地……、だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……ここ？」"

hide guide_1
show guide_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice sat_g0059
Guide "「そう、ここ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……いや、ここってどこよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（『医務室』って書いてあるんだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このガイドを信じていいのだろうか。"

play sound se_0217
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0008
Hatena "「入れ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアをノックすると、中から短い返答が聞こえた。"

hide guide_6

play sound se_0285

play music drawingroom_day_p_wam

show m_ryou1_tou1and5and13 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……失礼します」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアを開けて、部屋の中へと足を踏み入れる。\n
そこは、いわゆる執務室、といった造りの部屋になっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "執務机に座るのは銀髪の男。\n
そしてその両脇を、二人の長身の男性が固めている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "短髪と長髪と、対照的な二人だ。\n
短髪の彼は、机に座る銀髪の男の傍らに控えるようにぴしりと立ち、長髪の男は緩く机の上に直接腰かけている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "配置からして、おそらく立場として一番偉いのは机についている銀髪の男だろう。\n
だが、彼は長髪の男の無作法を責めるようなことはなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0012
Nightmare "「やあ、ようこそ、新入生。\n
私はこの塔の主、ナイトメア＝ゴットシャルクだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0013
Nightmare "「学校では学校医を勤めている。\n
具合が悪くなったり怪我をしたりしたら、すぐにここへ来るといい」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0014
Nightmare "「私が……、すぐに楽にしてあげよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……なんて、悪役っぽいの、この人）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "青白い顔。\n
魔法使いの衣装に、わざとらしいほど威厳のある口調。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自己紹介の後半に至っては、完全に……。"

hide m_ryou1_tou1and5and13
show m_ryou1_tou2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0008
Hatena "「……ナイトメア先生。\n
それは響き的に、息の根を止めると言っているように聞こえるんですが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0009
Hatena "「おまえは誰かの息の根を止めるより、自分のを止めるほうが得意だろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0015
Nightmare "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "両脇それぞれから突っ込みをいれられて、ナイトメアと名乗った顔色の悪い学校医は、ぐっと言葉に詰まった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0016
Nightmare "「そんなことは……、げほっ！\n
な、げほげほ、うげほ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0009
Hatena "「……はあ。\n
落ち着いてください、あなたは興奮すると咳き込むんですから……」"

hide m_ryou1_tou2
show m_ryou1_tou3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0010
Gray "「……っと。\n
俺は塔の管理を任されている、グレイ＝リングマークだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0011
Gray "「ナイトメア先生の補佐をしている。\n
校内で見かけたら、よろしく頼む」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなナイトメアの姿に溜息をついた短髪の彼の名はグレイ、というらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "管理を任されている、ということは塔にいる使用人達を統括する立場にあるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（しかし……、補佐の必要な学校医ってどうなのよ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（……補佐っていうより、補助か。\n
学校医っていうより、この人自身に医者が必要そう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今にも倒れそうな顔色。\n
そして、咳き込み続けて止まらない様子。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0017
Nightmare "「げほ、げほげほ！\n
ぐぐぐ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0012
Gray "「……ナイトメア先生、落ち着いてください。\n
さあ、深呼吸を……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……病人と、介護者みたい）"

hide m_ryou1_tou3
show m_ryou1_tou4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次いで、長髪の彼が面倒くさそうに名乗る。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0010
Julius "「私は、風紀委員長のユリウス＝モンレー。\n
この塔の寮長だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先にナイトメアは、この塔の主だと名乗り、そしてユリウスはこの塔の寮長なのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは管理責任者で、ナイトメアの補佐と名乗っているのでいいとして……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（結局、総括の責任者はどっち？）"

hide m_ryou1_tou4
show m_ryou1_tou1and5and13 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice nig_r0018
Nightmare "「……この寮は職員と、生徒が、それぞれ住んでいる。\n
職員側の代表がこの私で、学生一同の代表がそこの委員長だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の疑問を見透かしたようにして、ナイトメアが答えてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえばそんなことを、クラスメイトも言っていた。\n
この寮は元は天文台で、その後職員寮を経て、生徒にも開放されたのだと。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（だから責任者が両方いるのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（ああ、でも、ユリウスは正確には生徒ではなくて研究者だっけ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice nig_r0019
Nightmare "「そう……、それはいいとして……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアが、また私の思考を先回りするように言葉をつぐ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人からじっと視線を注がれて、私も見返す。\n
そんなふうに見つめられる理由が分からない……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しまった。\n
自己紹介を忘れていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼんやりと彼らの観察をしている場合ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだって、名乗るのを忘れていたのだろう。\n
どうしてだか、名乗る必要のない、知り合いのように感じてしまったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（初対面だっていうのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「失礼しました。\n
私の名前は、[firstname]＝[familyname]です」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「先生や先輩方には、ご迷惑をかけることもあると思いますが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手は教職員であり、塔の管理責任者であり、そして上級生（卒業はしていないので、この言い方で正しいのだろうか？）だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "失礼にならないよう、丁寧に自己紹介をしようとしたものの……。"

hide m_ryou1_tou1and5and13
show m_ryou1_tou6and8and11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0020
Nightmare "{size=+20}「気持ち悪い」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いきなり、ナイトメアのそんな言葉で妨げられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……む）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice gra_r0013
Gray "「ナ、ナイトメア先生？\n
気持ち悪いって……、吐きそうなんですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice gra_r0014
Gray "「今、エチケット袋をお持ちしますから……！\n
もう少し我慢してください！」"

play sound se_0470
with dis
$ hi_mes()
hide m_ryou1_tou6and8and11
show m_ryou1_tou7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは慣れたように、懐からしゅばっと茶色の袋を取り出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "{size=+20}（この人、懐にエチケット袋を常備しているの？）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも、それはナイトメアのためらしい。\n
……補佐どころか介護の必要な学校医というのは、どうなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0015
Gray "「さあ……、これを……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずずいっと、エチケット袋を差し出すグレイ。\n
が、ナイトメアはそれに対して首を左右に揺らして、拒絶した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういうリアクションが出来るあたり、そこまで気分が悪いわけではないようだ。"

hide m_ryou1_tou7
show m_ryou1_tou6and8and11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0021
Nightmare "「いや、違う。\n
そうじゃなくて……、[firstname]、君の敬語が気持ち悪い」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_9")
T "（……{size=+20}なんだと？{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「失礼ね。\n
私が気持ち悪いって言うの……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "上流家庭、とまではいかなくとも、私だってちゃんとした家の出身だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最低限のマナーは心得ている。\n
挨拶ぐらい問題なく出来ている……はずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、すでに立場を忘れて、言い返してしまっているあたり……。\n
私は私で、どうなんだというか……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0016
Gray "「……ナイトメア先生、失礼ですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0011
Julius "「おい。\n
いくらなんでも、それは自己紹介をした生徒に対し……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0022
Nightmare "「いいや、気持ち悪い、気持ち悪い、気持ち悪いね！\n
こう……っ、もやもやっとしてしまう……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "傍らからグレイとユリウスがナイトメアを諌めるが、ナイトメアは依然として頭を左右に揺らして、気持ち悪いと主張する。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0023
Nightmare "「気持ち悪いものは気持ち悪い！\n
おまえらは平気なのか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0017
Gray "「……はあ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0012
Julius "「ふん……、何を訳の分からんことを……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0024
Nightmare "「なら、[firstname]！\n
君、ちょっと私達を呼んでみろ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0018
Gray "「ナイトメア先生……。\n
彼女に失礼ですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0013
Julius "「手続きに来た、新入生の一人だぞ？\n
こんなことに何の意味が……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0025
Nightmare "「いいから！呼んでみろ！\n
私達のそれぞれを、だ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……ナイトメア先生」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
Nightmare "「…………」"

hide m_ryou1_tou6and8and11
show m_ryou1_tou9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「グレイさん」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice gra_r0019
Gray "「……うっ！？」"

hide m_ryou1_tou9
show m_ryou1_tou10 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「ユリウスさん」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice jul_r0014
Julius "「……っう！！\n
き、気色悪い……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

hide m_ryou1_tou10
show m_ryou1_tou6and8and11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……どいつもこいつも」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（……っと、本音が漏れた）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目上の人間に対して、失礼なこと。\n
しかし、相手側も相当に失礼だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怒っていい場面なのかもしれないが、私自身も、彼ら同様にとんでもなく気持ち悪い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランド相手に敬語を使おうと試みたときと、同じ反応だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一体、どうしたというのだろう。\n
何かの呪いだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice nig_r0026
Nightmare "「……だろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice gra_r0020
Gray "「で……、ですね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice jul_r0015
Julius "「……だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が考え込む間、彼らは何事か話し合った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その後、奇妙な沈黙がすぎていく。\n
どれくらい、その沈黙が続いただろうか。"

hide m_ryou1_tou6and8and11
show m_ryou1_tou12 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0027
Nightmare "「……よし！[firstname]！\n
君の私達への敬語を禁止する！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice nig_r0028
Nightmare "「なんだか気持ち悪いし、しっくりこない！\n
気持ちの悪いことはやめておくに限る！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice gra_r0021
Gray "「……違和感がありますよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jul_r0016
Julius "「……ああ。\n
今回に限っては、同意する」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ええ？\n
そりゃあ、私だって違和感はあるけれど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice jul_r0017
Julius "「……非常に、な」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「う、うん、まあ……、確かに」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gra_r0022
Gray "「……なら、無理をすることはない。\n
敬語はやめてくれて構わないぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「で、でも、あなた達、この学校の偉い人なんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手続きで必ず来なければならないくらいだ。\n
新入生が敬語も使わずに話していい相手ではないはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0029
Nightmare "「ああ、私は偉いとも！\n
えっへん！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（そう言われると、ちっともさっぱり偉そうに思えないんだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「なら、やっぱり……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice jul_r0018
Julius "「……ただの学校医だろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice gra_r0023
Gray "「……この塔の責任者でもあられる」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（ど、どっちだ……？\n
偉くないの？偉いの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_16")
voice nig_r0030
Nightmare "「私は偉い！\n
塔の、偉大なる主！敬うべき相手だ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（口を開くほどに、目上とは思えなくなってくるんだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（偉い……、のよね？\n
一応、本人もそう言っていることだし）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……じゃあ、やっぱり、敬語なしで話したり出来ません」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice nig_r0031
Nightmare "「いいや、駄目だ！\n
君の、私達への敬語を一切禁止する！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「どうしてよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「偉いなら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice nig_r0032
Nightmare "「私は偉いんだから、絶対なんだ！\n
私が禁止すると言ったら、そうするんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "偉いのなら、敬語を使って当然だと思う。\n
が、彼は「自分は偉いのだから、敬語を使うなと言ったら使うな」と無茶を言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無茶だが……、本人がそう言うのならいいのだろうか。\n
捨て鉢になってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不自然な状況を受け入れてしまいそうになるくらい、彼らに対して敬語を使うという行為の違和感は凄まじかったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、そんなに人懐っこい性格ではない。\n
そのはずなのに、彼らに対しての垣根が、異様なほどに低い。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「あなた達も、それでいいの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイとユリウスへと向き直る。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0024
Gray "「ああ、そうしてくれ。\n
なんというか……、そのほうがしっくりきそうな気がする」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0019
Julius "「ああ、うまく言い表せないが……。\n
そのほうがいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは元々あまり呼称に拘るようなことはなさそうだが、グレイやユリウスは上下関係にもきっちりしていそうなのに……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（いえ、私だって……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまで会ったこともない相手のはずなのに、奇妙な感覚だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0033
Nightmare "「というわけで、[firstname]、君は敬語禁止だ！\n
分かったな！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……ええ、分かりました。\n
いえ、分かったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確認をとるナイトメアに、同級生に返すような気安い口調で返事を返した。"

hide m_ryou1_tou12
show m_ryou1_tou1and5and13 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0034
Nightmare "「うむ。\n
そうだな、それでいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無礼そのものの態度に、ナイトメアは満足したようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その会話を聞いていたグレイやユリウスまでが、どこかしら安心したような顔をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……なんで、あなた達まで安心したような顔をしているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_r0025
Gray "「いや……、理由は分からないんだが……。\n
こう、あるべきものがあるべき場所に落ち着いたかのような……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_r0020
Julius "「私も同感だ。\n
……秩序が取り戻されたかのような、そんな感覚だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人のしみじみとした言葉に、大袈裟なと言いたいところだが、私自身その気持ちが分かってしまうのだから困ってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "敬語を使わなくていいとも言われたことだし、入り口で感じた疑問を聞いてみることにする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「入り口に『医務室』と書かれていたけど、この部屋は結局何なの？\n
医務室というか執務室のように見えるんだけど…」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_r0026
Gray "「ご覧の通り、ナイトメア先生は病弱だからな。\n
あちこち行かずにすむように執務室と医務室を兼用しているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（きっと、ナイトメアへの特別措置なんだろうな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice nig_r0035
Nightmare "「……さて。\n
問題や疑問が落ち着いたところで、委員長、彼女の学生証を作ってやったらどうだ？」"

hide m_ryou1_tou1and5and13
show m_ryou1_tou14 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice jul_r0021
Julius "「分かっている。\n
……手を」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスが机から立ち上がり、私へと一歩を踏み出した。\n
促されるままに、私は矢印を繋いだ紐を左手に持ち替え、右手を差し出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（そういえば無色矢印、部屋に入ってから静かにしているわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちら、と見やれば、無色矢印は目障りにならない程度にくねくねとしながらも、静かにしているようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0022
Julius "「ここに親指の腹を押し付けろ。\n
それが一種の契約になる」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0023
Julius "「おまえはシンフォニアの生徒になることを望んだ。\n
その責任、与えられるであろう知識の対価として、規律に従うことを誓えるか？」"

with dis
$ hi_mes()
hide m_ryou1_tou14
show m_ryou1_tou15 onlayer master
with dis

play music magic_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "差し出されたのは、カードだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今は何も書かれていない。\n
裏も表も、真っ白なカードだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（……契約）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法使いにとって契約というのは、ときに命をかけてでも守らなければならないものだ。だから、簡単には契約や約束を交わさない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの校則、規律についてはすでに目を通してある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その規律に従えると判断したからこそ、私はこうしてここ、シンフォニアにやってきたのだ。"

hide m_ryou1_tou15
show m_ryou1_tou16 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "迷うことはない。\n
私は、ユリウスの差し出した何も書かれていないカードへと、躊躇わず親指の腹を押し付けた。"

play sound se_0138
hide m_ryou1_tou16
show white onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "眩しさに目を閉じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "光が収束したのを瞼裏にも感じて、ゆっくりと目を開けた。"

with dis
$ hi_mes()
hide white
show m_ryou1_tou17 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……あ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどまで、真っ白だったはずのカードには、私の情報が浮かび上がっていた。\n
[firstname]＝[familyname]の名前が刻み込まれている。"

play sound se_0738
with dis
$ hi_mes()
hide m_ryou1_tou17
show m_ryou1_tou18 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確認するようにユリウスがそのカードの表面に指を滑らせると、その動きに反応してカードの上に、私のホログラムが浮き上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このカードの持ち主である私の姿。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（こうして改めて見ると、ちょっと恥ずかしいな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の姿を第三者目線で見る、というのは、なかなか気恥ずかしいものがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0024
Julius "「……契約はうまくいったようだな。\n
これでおまえは、シンフォニア高位魔法学校の正式な生徒だと認められた」"

with dis
$ hi_mes()
hide m_ryou1_tou18
show m_ryou1_tou19 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスがカードの表面から指を離せば、浮かんでいた私のホログラムはふっと消えた。ただのカードへと戻った学生証を、改めてユリウスから渡される。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（これで……、私もシンフォニアの生徒）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たかがカード一枚。\n
しかし、ずいぶんと重く感じた。"


scene bg_par16_rs_tow_day with dis
hide m_ryou1_tou19


show yuri_m_03_9 at center
with dis

play music drawingroom_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0025
Julius "「これで、ここでの手続きは終了した。\n
……おまえ、寮はどこに決めたんだ？」"
if place_of_stay == "Castle":
    jump gakuen_dormitory_tower_not1
if place_of_stay == "Hatter":
    jump gakuen_dormitory_tower_not1
if place_of_stay == "Amuse":
    jump gakuen_dormitory_tower_not1
if place_of_stay == "Tower":
    jump gakuen_dormitory_tower_not1
label gakuen_dormitory_tower_not1:
hide yuri_m_03_9
show yuri_m_03_9 at left
with dis

show nai_m_02_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0000
Nightmare "「まだ決めてないなら、ここはどうだ？\n
悪くないだろう、何せ私の塔だからな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（塔、か……）"
$ gakuen_dormitory_tower_not2a_seen = False
menu:
    "そうね、ここもいいと思う。":
        jump gakuen_dormitory_tower_not2a
    "いいえ、残念ながら……。":
        jump gakuen_dormitory_tower_not2b
label gakuen_dormitory_tower_not2a:
$ gakuen_dormitory_tower_not2a_seen = True
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そうね、ここも悪くないわ。\n
話から想像していたほど、堅苦しいわけでもなさそうだし」"

hide nai_m_02_3
show nai_m_01_6 at center
with dis
hide yuri_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice nig_r0001
Nightmare "「……どうしてそこで、私を見るんだ。\n
ふっ、私が気さくでフレンドリーなよい統治者ということだな？」"


show yuri_m_02_11 at center
with dis
hide nai_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice jul_r0000
Julius "「気さくでフレンドリーであるところは百歩譲って認めてやるとしても……。\n
はたして、おまえ、統治というようなことが出来ているのか？」"

hide yuri_m_02_11
show yuri_m_02_11 at left
with dis

show gre_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice gra_r0000
Gray "「委員長、たとえ形だけとはいえナイトメア先生は塔の管理者なんだ。\n
もっと敬意をだな……」"

hide yuri_m_02_11

hide gre_m_01_6
show gre_m_01_6 at left
with dis

show nai_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice nig_r0002
Nightmare "「か、形だけ……っ！？\n
ひどっ、う……、げほげほぐふっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……フォローするふりしてトドメを刺すなんて、グレイってなかなか高等技術を使うわね」"

hide gre_m_01_6
show gre_m_03_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice gra_r0001
Gray "「トドメを刺すつもりなど……。\n
ナ、ナイトメア先生しっかりしてください……！！」"


show yuri_m_01_1 at center
with dis
hide nai_m_03_3

hide gre_m_03_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice jul_r0001
Julius "「こんなどうしようもない男に、敬意を払うなんて器用な真似が出来るのはおまえぐらいだ。……たまに張り倒したくならないのか、トカゲ」"

hide yuri_m_01_1
show yuri_m_01_1 at left
with dis

show gre_m_01_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice gra_r0002
Gray "「ナイトメア先生に対して、失礼なことを言うな。\n
……その域は通り越した」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……トカゲ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話の流れからすると、それはグレイを指しているのだろう。ちらりと見た先、グレイの首筋に小さな黒いトカゲのタトゥーがあるのが分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あだ名の由来はそこから来ているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（タトゥーか……。\n
真面目そうな人なのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人は見た目によらないと言うし、外見どおりでないのか、はたまた生まれた地域の風習なのかもしれない。"

hide yuri_m_01_1
show yuri_m_03_9 at center
with dis
hide gre_m_01_13

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0003
Julius "「それで……、おまえはどこの寮に決めたんだ？」"
if place_of_stay == "Castle":
    jump gakuen_dormitory_tower_castle1
if place_of_stay == "Hatter":
    jump gakuen_dormitory_tower_hatter1
if place_of_stay == "Amuse":
    jump gakuen_dormitory_tower_amuse1

label gakuen_dormitory_tower_not2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「それが……。\n
もう事務室でどこの寮にするのかは決めてきちゃっているのよね」"


show nai_m_03_4 at center
with dis
hide yuri_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice nig_r0003
Nightmare "「なんと、もう決めてしまっているのか。\n
実際見て回ってから決めても遅くはなかっただろうに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……そうね。\n
でも、残念ながら、選択はもう終わっているの」"

hide nai_m_03_4
show nai_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice nig_r0004
Nightmare "「しかし……、そんなに急がなくとも……」"

hide nai_m_02_9
show nai_m_02_9 at left
with dis

show gre_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gra_r0003
Gray "「そうすることで、手続きが一度ですみますからね。\n
俺は、要領がいいと思いますよ」"


show yuri_m_02_10 at center
with dis
hide nai_m_02_9

hide gre_m_02_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice jul_r0002
Julius "「トカゲの言うとおり、先に決めておくほうが時間を無駄にせず効率的だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……トカゲ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話の流れからすると、それはグレイを指しているのだろう。ちらりと見た先、グレイの首筋に小さな黒いトカゲのタトゥーがあるのが分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あだ名の由来はそこから来ているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（タトゥーか……。\n
真面目そうな人なのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人は見た目によらないと言うし、外見どおりでないのか、はたまた生まれた地域の風習なのかもしれない。"

hide yuri_m_02_10
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0003
Julius "「それで……、おまえはどこの寮に決めたんだ？」"

if place_of_stay == "Castle":
    jump gakuen_dormitory_tower_castle1
if place_of_stay == "Hatter":
    jump gakuen_dormitory_tower_hatter1
if place_of_stay == "Amuse":
    jump gakuen_dormitory_tower_amuse1
label gakuen_dormitory_tower_castle1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「赤薔薇寮よ」"


show nai_m_03_7 at center
with dis
hide yuri_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice nig_r0005
Nightmare "「……{size=+20}げ{/size}」"

hide nai_m_03_7
show nai_m_03_7 at left
with dis

show gre_m_01_15 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Gray "「…………」"


show yuri_m_02_9 at center
with dis
hide nai_m_03_7

hide gre_m_01_15

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは分かりやすく、グレイとユリウスは眉を寄せる形で反応した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……赤薔薇寮、って何か問題あるの？」"

hide yuri_m_02_9
show yuri_m_02_9 at left
with dis

show nai_m_02_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice nig_r0006
Nightmare "「ああ、問題大ありだ。\n
……といいたいところだが、君には問題ないだろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアはひょいと肩を竦めて笑った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「どういうこと？」"

hide yuri_m_02_9

hide nai_m_02_12
show nai_m_02_12 at left
with dis

show gre_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gra_r0004
Gray "「赤薔薇寮は、自治会の治める寮だ。\n
塔はどちらかというと学校側なので……、折り合いはあまりよくない」"

hide nai_m_02_12
show nai_m_03_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice nig_r0007
Nightmare "「風紀委員会は、生徒が規律に反しないかと取り締まる。自治会はその風紀委員会が権力を笠に着て、横暴な振る舞いをしないかどうかを見張る」"


show yuri_m_02_11 at center
with dis
hide nai_m_03_10

hide gre_m_03_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice jul_r0004
Julius "「互いがまともに機能している限り、問題のない対立構造だ。\n
ただそれゆえに、互いに苦手意識はある」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お互いが悪いことをしないように、見張りあうのが風紀と自治会の関係であるらしい。よく出来たシステムだが、学校というより、まるで小さな国のよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（これだけ大きな学校なら、そうもなるわよね）"

hide yuri_m_02_11
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice jul_r0005
Julius "「とにかく、問題だけは起こしてくれるなよ。\n
私の手を煩わせるな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後に会話を終わらせるようにユリウスがそう言って、行け、と顎で示す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう少し話していたい気もするが……。\n
次の新入生も、学生証を作るために待っているに違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「それじゃあ三人とも、またどこかで」"

hide yuri_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは塔の代表者で、それぞれが役職についている。\n
また学校内で見かけることもあるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おとなしくこの場を後にする。"

jump gakuen_dormitory_common4
label gakuen_dormitory_tower_hatter1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「帽子屋寮よ」"


show nai_m_03_7 at center
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice nig_r0005
Nightmare "「……{size=+20}げ{/size}」"

hide nai_m_03_7
show nai_m_03_7 at left
with dis

show gre_m_01_15 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Gray "「…………」"


show yuri_m_02_9 at center
with dis
hide nai_m_03_7

hide gre_m_01_15

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは分かりやすく、グレイとユリウスは眉を寄せる形で反応した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……帽子屋寮、ってやっぱり問題あるの？」"

hide yuri_m_02_9
show yuri_m_02_9 at left
with dis

show nai_m_02_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice nig_r0008
Nightmare "「そうだな……、塔とは相性がよくない。\n
君がまさか帽子屋寮を選ぶとは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは難しい顔をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「不良が多い、とは聞いているんだけど」"

hide yuri_m_02_9

hide nai_m_02_11
show nai_m_02_12 at left
with dis

show gre_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gra_r0005
Gray "「そうだな、不良ではすまされないような連中だが……。\n
帽子屋寮は、規則に従えない者が多く集まっている」"

hide gre_m_02_10
show gre_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gra_r0006
Gray "「君のような子が……、帽子屋寮で本当に大丈夫なのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイのほうは心配そうだ。\n
ユリウスもむっつりとしているし、なんだか責められているような気になってくる。"

hide nai_m_02_12
show nai_m_03_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0009
Nightmare "「私やグレイは、学校医や管理責任者ということで、どちらかというと中立寄りだが……。そこの委員長と帽子屋寮は完全なる対立関係なんだ」"


show yuri_m_02_11 at center
with dis
hide nai_m_03_6

hide gre_m_02_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0006
Julius "「私は風紀委員長として、奴らを取り締まる。\n
……恨みを買うことも多い」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中立、と言ってはみても、ナイトメアもグレイも学校側の人間なのでどちらかというと風紀側だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校内の風紀を取り締まる風紀委員会と、不良の集団（？）が仲のいいわけもない。\n
三人が顔を顰めるのは当然だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……そりゃそうよね）"

hide yuri_m_02_11
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice jul_r0007
Julius "「とにかく、おまえまで問題を起こすようなことはするな。\n
私の手を煩わせるんじゃない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後に会話を終わらせるようにユリウスがそう言って、行け、と顎で示す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう少し話していたい気もするが……。\n
次の新入生も、学生証を作るために待っているに違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「それじゃあ三人とも、またどこかで」"

hide yuri_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは塔の代表者で、それぞれが役職についている。\n
また学校内で見かけることもあるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はおとなしくこの場を後にする。"

jump gakuen_dormitory_common4
label gakuen_dormitory_tower_amuse1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「遊園地寮よ」"


show nai_m_03_7 at center
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice nig_r0005
Nightmare "「……{size=+20}げ{/size}」"

hide nai_m_03_7
show nai_m_03_7 at left
with dis

show gre_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Gray "「…………」"


show yuri_m_02_9 at center
with dis
hide nai_m_03_7

hide gre_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは分かりやすく、グレイとユリウスは眉を寄せる形で反応した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……遊園地寮、って何か問題あるの？」"

hide yuri_m_02_9
show yuri_m_02_9 at left
with dis

show nai_m_02_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice nig_r0010
Nightmare "「ああ、問題あるとも。\n
といっても、それほど深刻なものじゃあないんだが」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアはひょいと肩を竦めて笑った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「どういうこと？」"

hide yuri_m_02_9

hide nai_m_02_12
show nai_m_02_12 at left
with dis

show gre_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gra_r0007
Gray "「遊園地寮は、明るく楽しく、をモットーにした寮なんだが……。\n
たまに楽しさを追求しすぎて、暴走することがあるんだ」"

hide nai_m_02_12
show nai_m_01_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice nig_r0011
Nightmare "「それに何より……。\n
ゴーランドの……、音楽センスは壊滅的なんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの音楽センスが壊滅的であることが、私の寮生活に一体どのような影響を与えるというのだろうか。"


show yuri_m_03_9 at center
with dis
hide nai_m_01_10

hide gre_m_02_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0005
Julius "「とにかく、問題だけは起こしてくれるなよ。\n
私の手を煩わせるな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後に会話を終わらせるようにユリウスがそう言って、行け、と顎で示す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう少し話していたい気もするが……。\n
次の新入生も、学生証を作るために待っているに違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「それじゃあ三人とも、またどこかで」"

hide yuri_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは塔の代表者で、それぞれが役職についている。\n
また学校内で見かけることもあるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はおとなしくこの場を後にする。"

with dis
$ hi_mes()
jump gakuen_dormitory_common4
label gakuen_dormitory_tower_tower1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ここよ。\n
塔に滞在することに決めたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice jul_r0026
Julius "「……っ！\n
そ……、そうか。物好きだな、おまえは」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice jul_r0027
Julius "「……ごほん、だが賢い選択だ。\n
ここは、他の寮のような馬鹿げた騒動は……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらり、とそこでユリウスは一度言葉を切ってナイトメアを見た。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0028
Julius "「……そう、多くはない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（ないとは言わないのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、その原因はナイトメアであるらしい。思い返せば、クラスメイトもナイトメアが問題児（先生なのに）なのだと言っていた。"


show nai_m_01_3 at center
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0036
Nightmare "「どうしてそこで私を見るんだ、委員長。\n
とにかく、[firstname]、君は正しい選択をした！」"

hide nai_m_01_3
show nai_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0037
Nightmare "「この私が、君をしっかりと指導してやろうじゃないか！\n
任せておけ！！」"

hide nai_m_02_1
show nai_m_02_1 at left
with dis

show gre_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_r0027
Gray "「俺も、君が塔を選んでくれたことを嬉しく思う。\n
歓迎するよ、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだかんだと言いつつも、三人は私の入寮を歓迎してくれている。\n
規律には厳しいのかとも思ったが、その空気はどこか暖かい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（外から見るほど、硬い場所でもなさそう）"

hide gre_m_01_4
show gre_m_01_4 at left
with dis

show yuri_m_02_4 at right
with dis
hide nai_m_02_1

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice jul_r0029
Julius "「では、入寮を……と言いたいが……。\n
おまえ、手続きがまだ途中だろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ええ。\n
まだ赤薔薇寮に行っていないわ」"

hide yuri_m_02_4
show yuri_m_02_4 at left
with dis

show nai_m_02_11 at right
with dis
hide gre_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice nig_r0038
Nightmare "「ああ、自治会員の登録か」"

hide nai_m_02_11
show nai_m_02_11 at left
with dis

show gre_m_03_3 at right
with dis
hide yuri_m_02_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice gra_r0028
Gray "「部屋の案内をしようと思ったが……。\n
先に、手続きをすませてきたほうがよさそうだな」"

hide gre_m_03_3
show gre_m_03_3 at left
with dis

show yuri_m_03_4 at right
with dis
hide nai_m_02_11

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice jul_r0030
Julius "「ああ、トカゲの言うとおりだな。\n
ほら、さっさと手続きをすませてこい」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……トカゲ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話の流れからすると、それはグレイを指しているのだろう。ちらりと見た先、グレイの首筋に小さな黒いトカゲのタトゥーがあるのが分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あだ名の由来はそこから来ているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（タトゥーか……。\n
真面目そうな人なのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人は見た目によらないと言うし、外見どおりでないのか、はたまた生まれた地域の風習なのかもしれない。"

hide gre_m_03_3

hide yuri_m_03_4
show yuri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_r0031
Julius "「ぼさっとするな。さっさと動け。\n
その間に、おまえの部屋を見繕っておいてやる」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人に促され、私はその他の手続きから先にすませることにした。"

jump gakuen_dormitory_common4
label gakuen_dormitory_tower_tower2:

scene bg_par15_rg_tow_day
with stripe_l_long

play music gallery_front_day_p_wam
hide yuri_m_01_8
show guide_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0103
Guide "「さあ、ここが終点だよ！\n
ぐるっと回って塔に戻ってきた！」"

play sound se_0058
hide guide_2
show guide_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0094
Guide "「これで俺の任務は終了！\n
後は部屋を貰うだけだよ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ガイドである矢印が案内してくれるのは、ここまでのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "四つの寮を巡る間のことだけだというのに、ずいぶん長い時間を一緒に過ごしたような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しばかり、寂しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ここで、お別れ？\n
少し、寂しいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice sat_g0085
Guide "「寂しく思うことなんかないさ！\n
俺は君が迷子になったら、すぐにでも飛んでいくからね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice sat_g0086
Guide "「だって俺は……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「迷子を安心できるところまで案内してあげる、一流のガイド？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice sat_g0087
Guide "「その通り！\n
俺は超一流のガイドだからね、迷子を見つけるのも上手なんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice sat_g0088
Guide "「だから安心して迷子になるといいよ！\n
俺に会いたければね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「安心して迷子って……」"

play sound se_0082
hide guide_6

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来、迷子を案内するためのガイドであるはずの矢印が、迷子を推奨しながらしゅわしゅわと消えていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "元々半透明で見えにくかった矢印が、首に繋がれた紐ごとしゅわしゅわとぼやけて見えなくなっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちり、と瞬きした次の瞬間には、もうそこに矢印の名残はなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……無茶を言うわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（行っちゃった……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今まで紐を持っていた手の中が、空っぽになってしまっているのが寂しい。\n
よく知らない場所で一人きり……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（また、会えるわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………。\n
……いや、会っちゃ駄目か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのガイドに会うということは、迷子になるのと同義だ。\n
積極的に会いたいような相手ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが……、半透明で見つけにくいとはいえ、あんなに騒々しいガイドなのだ。\n
これから始まる学園生活の中で、また見かけることもあるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……よし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は気合を入れて、再び塔の中へと足を踏み入れた。"


play music drawingroom_day_p_wam

show m_ryou1_tou20 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0039
Nightmare "「おかえり。\n
無事に手続きは終わったみたいだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ。\n
……ただいま」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……って、答えていいのかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice gra_r0029
Gray "「あちこち回って疲れただろう。\n
今日はもう休むといい」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice jul_r0032
Julius "「空いている部屋をいくつか確認させておいた。\n
使用人を呼ぶから、待っていろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の執務室へと戻ると、三人が口々に迎えてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……家、みたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "堅苦しい、といえば堅苦しいのだが、それはなんだか父親に監督される家庭のような雰囲気だ。誰が父親かというと詰まってしまうが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わいわいと学生同士で騒ぐ気安さはないものの、それでも居心地は悪くない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「そんなに気遣ってくれなくても……。\n
そこまで疲れていないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「あちこち回るのは楽しかったし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice nig_r0040
Nightmare "「……私自ら、案内してやってもよかったのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「それは無理でしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔、と名前だけ聞くと一つの寮のように思えるが、実際にはエントランスが一緒なだけで、男女共同区域を除き女子寮と男子寮では完全に分離している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、ここシンフォニアには、学生や職員の他にグレイのような使用人が常駐しており、それぞれの学生寮にも専任の使用人達が住み込んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エントランスには常にそのうちの誰かしらがおり、それぞれの寮を自在に行き交うようなことはできないようになっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "職員とはいえ、ナイトメアだってそう簡単には女子寮に入ることは出来ないはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……いや、学校医だし、割と自由になるのかしら）"

hide m_ryou1_tou20
show m_ryou1_tou21 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice gra_r0030
Gray "「そんなに働きたければ、こちらから……。\n
処理していただかないといけない書類が溜まっています」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice nig_r0041
Nightmare "「……っう。\n
気分が悪い。今日はもう無理だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice jul_r0033
Julius "「今日は、でなく今日も、だろう。\n
私はここしばらく、おまえがまともに仕事をしているのを見たことがないぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice nig_r0042
Nightmare "「そ、そんなことはないぞ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice gra_r0031
Gray "「……そのわりには、机の上から書類が減りませんが」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice nig_r0043
Nightmare "「そ、それは、片付けた先から溜まっていくから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice gra_r0032
Gray "「仕事とはそういうものです。\n
まとめてやろうとすると大変になるんですから、もっとこまめに処理していってください」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「そうよ。\n
真面目に働きなさいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice nig_r0044
Nightmare "「……っ！\n
なんでおまえらそんなにも意気投合しているんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice nig_r0045
Nightmare "「おかしいだろう！私はこの塔の責任者だぞ！？\n
敬え！尊敬しろ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「敬語禁止なんでしょう？」"

hide m_ryou1_tou21
show m_ryou1_tou22 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice nig_r0046
Nightmare "「うっっ！！\n
……げほげほ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがのナイトメアも、自分が口にした言葉の矛盾には気づいたらしく、言葉に詰まって悔しそうにしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際のところ敬語を使うかどうかと、その相手を敬っているかどうか、というのは同義ではないのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_r0047
Nightmare "「……げほげほげほっ！\n
がはっ！」"

play sound se_0631
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉は詰まっても、咳は出る。\n
ついでとばかりに、血まで出る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「し、死なないでよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice jul_r0034
Julius "「いつものことだ。\n
吐血しても、死にはしない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「そ、そう……なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gra_r0033
Gray "「ああ、死んだりはしないが……。\n
ナイトメア先生が倒れたら、学校医がいなくなってしまう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……倒れるような学校医、いらないんじゃないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前で吐血なんてものを見つつ、やけに落ち着いていられる。"


scene bg06_sk_h_day with dis
hide m_ryou1_tou22

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……どうしてかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やけに、馴染んでしまう。\n
塔での学園生活は、きっと落ち着いたものになるだろう。"

with dis
$ hi_mes()



jump gakuen_routechoice
