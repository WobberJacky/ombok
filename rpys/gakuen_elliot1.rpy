
scene bg25_rr_day
with dis
label gakuen_elliot1:
$ clockanim()


play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょうど小腹が空いてきたところだ。\n
調理室へ行くついでに、その道すがら帽子屋寮の男女共同区域を探索してみることにした。"

play sound se_0158
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（へえ、本当にいろいろあるのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あちこちの部屋をのぞいてみながら、のんびりと散策を楽しむ。\n
ようやくそれだけの余裕が出来たのだ、と実感する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここしばらくは学校生活に慣れることに忙しくて、必要に迫られた場所ぐらいにしか訪れたことがなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "調理室までの道のりは今までにも何度か通っているはずなのに、こうして改めて探索という形で歩いていると、新しい発見がある。"

with dis
$ hi_mes()


$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0535
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それが聞こえて来たのは、寮の共同区域の中でも、ひとけのないところに差し掛かったときだった。"

play sound se_0535
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か重いものが床に落ちたような音だ。\n
もしくは、壁に重いものを押し付けたときのような。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……なに？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰かが荷物でも落としてしまったのだろうか。\n
様子を見に行こうとそちらへと歩みを進めかけるが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0008
Furyou "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さな……、それでいて切羽詰った声が聞こえて、私は足を止めた。"


play music notice_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その声が聞こえたことにより、音の発生源の周囲の空気が急に穏やかならぬものへと変わる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（揉めごと？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭の中に危険信号がチカチカと点滅する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま、その場から立ち去るのが一番の良策だというのは分かっていた。\n
危ないことには関わらないほうがいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……しかし、好奇心には敵わない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賢く振る舞いたいと思いつつも、好奇心が強い。\n
シンフォニアに入るまでは優等生ぶっていたが、本質はこんなものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "優秀な生徒ばかりに囲まれて、自分自身の相対的なランクを下げることがかえってよかったのかもしれない。\n
今は自然体でいられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（いや、優秀な生徒ばかり……でもないのかしら。\n
この学校も）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "問題の音と声は、そこの角を曲がった先から聞こえてくる。ぴったりと壁に背をつけると、足音を殺してその音が聞こえた辺りへと近づいていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0009
Furyou "「わ、悪かったよ……！！\n
許して……、ぐ……！」"

play sound se_0373 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0026
Elliot "「……反省するのが、ちょっとばかり遅かったみたいだな。\n
ブラッドの、おとなしくしてろって話を聞いてなかったわけじゃないんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（！！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知った声が聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットだ。\n
エリオット＝マーチ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここ帽子屋寮の副寮長で、そしてブラッド＝デュプレの腹心である……、ウサギさん。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本人は全面的に否定しているようだが、その頭上からにょっきり伸びた長い耳は、誰がどう見てもウサギのものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手は自寮の幹部ということもあり、私も彼のことは一方的に知っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、彼と双子達のじゃれあいにも似た魔法合戦、喧嘩は帽子屋寮の名物ともいえる光景だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段は、双子に対しては気が短いところもあるが、面倒見のいいお兄さんといった感じなのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0027
Elliot "「……ブラッドの言いつけを守らないたあ、馬鹿な奴だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（こんなエリオットの声、初めて聞くわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドに対するときの声音とも、双子や、私達一般の生徒に対する声ともまったく違う。\n
低く、感情の見えない静かな声だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃賑やかなエリオットだからこそ、こんな声を出せたのかと驚き、同時にぞっとするような怖さを感じた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（ああ、やっぱり好奇心に従うとろくなことがないわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あまり聞いていて楽しい声ではないし、知るべき面でもなかったような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0010
Furyou "「で、でも、副寮長達だって……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0028
Elliot "「そうだな、俺や双子共も騒いではいるが……。\n
……他寮の奴らと揉めたりはしてねえよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0011
Furyou "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0029
Elliot "「寮の中で遊ぶ分には構わねえ。\n
だが、話が他寮に及べば、どうなるかは分かってんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0030
Elliot "「ついこの間も面倒が起きたばかりなんだ。\n
……ブラッドに余計に手間かけさせてんじゃねえよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oto_g0012
Furyou "「ぐ……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "淡々と言い含めるエリオットの言葉に混じって、苦しげな呻き声が混じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（だ、大丈夫なの……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何が起こっているのかを確認しようと、そろりと角から覗きこんで、再び息を呑んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……！」"


play music disquieting_a_wam
show m_eri1_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが、一人の男子生徒を壁際に追い詰めていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "長躯を活かし、上から押さえ込むような形だ。魔法を使って抵抗されることを防ぐためなのか、喉元に腕を差込んで固定している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでいて、完全に言葉を奪っているわけではない。\n
微妙な力加減が、そういった荒事にエリオットが慣れていることを示していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……怖い）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが、というだけではない。\n
この帽子屋寮という場所が、だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帽子屋寮に決めたとき、最初にあそこはならず者の集団だと、自治ルールにしか縛られない、というような話は聞かされていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、こういった形でルールからの逸脱を見るのは初めてだ。\n
いつもの双子との喧嘩とは、わけが違う。"

hide m_eri1_1
show m_eri1_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが私の気配に気づいたのか、ちらりと視線をこちらへと投げかけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目が合ってしまった……ような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「ひ……！」"

play sound se_0313
hide m_eri1_2 with grad_r_medium
play sound se_0550 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（き、気のせい……、よね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐに顔をひっこめたので、見られてはいないと思うのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰かいるということはバレたとしても、それが私だというところまでは分からない……はずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（人の心配より、私のほうが大丈夫……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心臓がバクバクとうるさい。\n
この音だけで、見つかってしまいそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さっさと逃げてしまいたくなるが、今物音をたてたら盗み聞きをしていたことが決定的になってしまいそうで、動き出すことが出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（み、見つかったら、私もあんなふうに押さえつけられて、脅されちゃうのかしら……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……うう。\n
もう、私、絶対に好奇心に負けたりしないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ろくなことがない。\n
エリオットだって、この場にいなければ、「危険だというけどいい人」くらいの認識で終わっていたのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらくじっとしていると、何事もなかったかのようにエリオットが再び口を開く。"



with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0031
Elliot "「……詫びは入れてもらうぜ？\n
今回のことについては……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、もうこちらを気にしてはいないようだった。\n
話の続きをしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、捕まることはなさそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（今のうちに……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットの声を背中に聞きながら、そそくさとその場から逃げ出した。"

with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg06_sk_h_day
with stripe_l_medium

scene bg06_sk_h_eve with Dissolve(1)

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_day with Dissolve(1)

play music dining_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それから数日。\n
寮や、学校の中で見かけたエリオットは、いつもと変わらなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "盗み聞きをしてしまった、という負い目があるせいか、最初のうちは彼を見かける度にびくりとしていたのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手から何のリアクションもないことに、私はすっかり安心していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（気付かなかったのかしら……。\n
それとも、気付きはしたけれど、誰かが分からなかったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どちらにしろ、私が追及される心配はなさそうだ。\n
図書館から借りてきた、読みかけの本を片手にカフェテリアへと向かう。"


scene bg_par02_ct_hat_day with stripe_l_medlong
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "各寮には、カフェテリアという小さな喫茶スペースが設けられている。\n
かけられている魔法は、食堂と同じものだが、メニューには違いがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食堂の魔法がしっかりとした食事中心なのと違って、カフェテリアの魔法で用意できるメニューは飲み物や軽食が中心だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お気に入りの窓際の席に座って、手元に本を広げる。\n
イメージして、呼び出すのは紅茶だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「…………」"

with dis
$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0718
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

play sound se_0718
pause .5
play sound se_0718
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱら、ぱら、と本のページをめくっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視界の端を、何かがよぎっていったような気がして顔を上げた。\n
ちらりと見やった窓の外に、中庭に向かって歩いていくエリオットの姿が見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……何をしに行くんだろ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは普段からも、自主的に寮内の見回りをしていたりと、本来寮長であるブラッドの仕事じゃないかと思われるようなことを日課としてこなしている。"

menu:
    "何をしているのかしら？":
        jump gakuen_elliot1_2a
    "気にしない。":
        jump gakuen_elliot1_2b
label gakuen_elliot1_2a:
$ lovechara_elliot_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中庭を歩いている姿にも違和感はないのだが……、今は妙に気になってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（覗き見しちゃった後ろ暗さかしら？\n
それとも、特別な一面を知っている、って……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういう、奇妙な優越感だろうか。\n
しかし、エリオットのああいった面は、直に見ていなくとも、隠されてはいないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼が凶暴なことは周囲にも知られているし、恐れられている。\n
この寮で暮らせば、すぐ分かるようなことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（別に秘密を知ったっていうわけでもないのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気になる。\n
むしろ、避けるべきような場面を目撃したというのに……。"

jump gakuen_elliot1_3
label gakuen_elliot1_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見回りを仕事にしているエリオットが中庭に出て行ったとしても、おかしなことは何もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（また、妙な一面を見ることになっても、反応に困るだけだし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（読書の続き、続き……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手元に広げた本へ、意識を集中しようと試みる。"

jump gakuen_elliot1_3
label gakuen_elliot1_3:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（あ、戻ってきた）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "建物の陰に入って見えなくなったエリオットが、再び私のいる位置から見えるところまで戻ってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……何があったの？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その耳が、しょんぼりとたれている。\n
表情も、いつになく暗いような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは、大きな図体でとぼとぼといったふうに歩き去っていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（何があったのかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怪我はしていない。\n
不穏な雰囲気でもないのに、気になって仕方ない。"

with dis
$ hi_mes()

scene bg_par02_ct_hat_day with Dissolve(.8)

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg06_sk_h_day with stripe_l_medlong

scene bg_par15_rg_hat_day with stripe_l_medlong
scene bg_par02_ct_hat_day
with stripe_l_long

play music dining_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しょんぼりエリオットを見かけたのは、その日だけではなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアにいる間、気をつけて観察していると、一日に何度かエリオットは中庭に顔を出しては、やっぱり耳をしゅんとたらして去っていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（き……、気になる……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いったいあそこに何があるというのだろうか。あんまりにも気になったもので、近くに座っていた顔見知りの子に聞いてみることにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女も読書が好きなのか、よくカフェテリアに本を持ち込んでいるのを見かける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お気に入りの席が近いこともあって、自然、顔をあわせると言葉を交わす仲になった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ねえ。\n
ちょっといいかしら」"


show hat_a1_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice oda_g0082
Seito "「ん？\n
なあに？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の声に、手元の本から顔をあげた彼女が私へと向き直る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「邪魔してごめんね？\n
ちょっと聞きたいことがあったものだから」"

hide hat_a1_8
show hat_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice oda_g0083
Seito "「いいわよ、別に構わないわ。\n
それで、何が聞きたいの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気にしないで、というように片手をぱたりと揺らして、彼女は快く促してくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「ありがと。\n
あのね、最近あの辺り……、中庭のほうでエリオット副寮長を見かけるんだけど、何かあるのかしら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの辺り、と私は実際に彼女に分かりやすいように、指で指し示す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女はその先を視線で追って、それから「ああ」と納得したような声をあげた。\n
どうやら彼女は知っているらしい。"

hide hat_a1_2
show hat_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0084
Seito "「副寮長、あの辺りを開墾しているのよ。\n
でも、なかなかうまくいかないみたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "{size=+20}「開墾？？？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "想像もしていなかった単語が出てきて、私は目を丸くしてしまう。"

hide hat_a1_3
show hat_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0085
Seito "「副寮長って……、ほら、ねえ、うん。\n
その……、アレ、でしょ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「アレ？」"

hide hat_a1_5
show hat_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice oda_g0086
Seito "「そう、アレよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「アレ……？\n
アレって……、なに？」"

hide hat_a1_5
show hat_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice oda_g0087
Seito "「アレはアレよ、ええと、ほら……。\n
ぴょんぴょん跳ねる、可愛らしい小動物」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「ああ、ウサギのこ……」"

hide hat_a1_5
show hat_a1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice oda_g0088
Seito "{size=+20}「わわわわわ……！！！！」{/size} "

hide hat_a1_4
show hat_a1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice oda_g0089
Seito "「駄目よ、そんな大声で言ったりしたら……！\n
万が一、エリオット副寮長に聞かれでもしたら……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「お、落ち着いてよ……」"

hide hat_a1_4
show hat_a1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice oda_g0090
Seito "{size=+20}「落ち着けないほど、まずいことなのよ！？大声で言えるようなことじゃないわ！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「まずいことなら、尚のことよ！\n
もうちょっと小声で！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大声を出しているのは、彼女のほうだ。\n
まばらに周囲にいた人達が、何事かとこちらを振り返る。"

hide hat_a1_7
show hat_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0091
Seito "「はあ。\n
そうね、私も落ち着かなくちゃ……」"

hide hat_a1_5
show hat_a1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0092
Seito "「エリオット副寮長に聞かれたら、どんな罰を受けるか分かったものじゃない……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……罰）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女の口にした言葉に、先日の光景を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不始末をやらかしたという男子生徒を、エリオットは慣れたように壁際に追い詰め、脅しをかけていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ウサギ……って、罰を受けるほど禁句なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ああいった「罰」は、日常的に行われるものなのだろうか。"

hide hat_a1_9
show hat_a1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0093
Seito "「当たり前よ……！\n
あなたってば怖いもの知らずなのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「そうかしら。\n
エリオット副寮長の怖いところも、知っているつもりだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（この前、見たばかりだもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それでも、平気でウサギと口に出来てしまうのは、私が彼を恐れていないからだろう。あの場は恐ろしかったが、彼自身を恐れる気持ちにはなれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大体、罰というのはルールを破ったものに与えられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオット個人はウサギと呼ばれることを好まないし、そう呼ばれると分かりやすく不機嫌になるが……それは彼の個人的な問題だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この場合、ルールとはブラッドの決めたもの。エリオットにウサギと言ってはいけない、というのがルールでない限り、罰せられる心配はないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（その、はず）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットはブラッドの忠実な腹心なのだ。\n
その意に背いたり、勝手なことをしたりはしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "公私混同はしない。\n
それだけは、新参者の私にも分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……まあ、個人的にぶち切れそうではあるけど）"

hide hat_a1_7
show hat_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice oda_g0094
Seito "「知っていて口にするなら、余計に怖いもの知らずよ。\n
……で、まあ、ほら、エリオット副寮長はアレでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「そうね、アレね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（ウサギさん）"

hide hat_a1_5
show hat_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice oda_g0095
Seito "「そう。\n
だから、にんじん料理が大好きなのよ」"

hide hat_a1_5
show hat_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice oda_g0096
Seito "「けど、食堂やカフェのメニューにはにんじん料理だけのレパートリーなんてそんなに多くないでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「そう……、ね。\n
普通に比べたらずいぶんとメニューは豊富なほうだとは思うけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食堂には、生徒の出身地に合わせた様々な料理が各種登録されている。その登録された料理の中から、一番イメージに近いものが現れるようになっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にんじん料理なんていうのも（私はまだ挑戦したことがないが）、ないこともないらしい。\n
……どこかの郷土料理なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ウサギの国……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メルヘンだ。"

hide hat_a1_5
show hat_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oda_g0097
Seito "「それで、個人的に、使用人に頼んで調理してもらったりしているみたいなのよね。で、にんじん好きが高じて自家栽培にまで挑戦しているらしいわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「へえ。\n
それじゃあ、あそこには副寮長のにんじん畑があるわけなのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ウサギさんの、にんじん畑……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ますますメルヘンだ。\n
さすが魔法学校、といいたくなってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（いやいや、そういうのが普通なわけじゃないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくら魔法学校とはいえ、エリオットやペーター、ボリスやピアスという魔法生物モドキは稀少な存在だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうして誰もつっこまないのかが疑問ではあるが、そこにつっこんでしまうと、何か大事なところで諸々の支障が発生する。目を瞑っておくべきことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「教えてくれて、ありがとう」"

hide hat_a1_5
show hat_a1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice oda_g0098
Seito "「どういたしまして」"

hide hat_a1_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女はそう言うと、再び読書へと戻っていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はといえば、本に視線を戻すでもなく、窓の外を見やる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中庭の向こう、ここからは見ることのできない位置に、エリオットのにんじん畑があるのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はどうして、毎度その畑に顔を出すたびに、あんなに分かりやすく落胆しているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ出来ていない、まだ実っていない、と日毎がっかりしているというわけでもないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（それはそれで、可愛いとは思うけれども）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……気になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にんじん畑の謎が気になって、読書の気分ではなくなってしまった。\n
私はぱたりと本を閉じると、席をたった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（ああ、気になる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットのことが、やけに気になって堪らない。……いや、今気になっているのはエリオットのことではなく、にんじん畑のことだけども。"

with dis
$ hi_mes()

scene bg_par02_ct_hat_day with Dissolve(.8)

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
$ routechara == "Elliot"
jump gakuen_friend_check_hatter
