
scene bg25_rr_day
with dis
label gakuen_nightmare1:
$ clockanim()


play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らに言われて気付いたが、私は本当にまだまだこの塔のことを知らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらくの間、学校に適応することだけを考えて、塔の自室と校舎とを往復するような生活を繰り返していたが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろそろ他の場所に足を伸ばしてみてもいいかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（色々と、面白そうな場所があるみたいだし……）"

with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg25_rr_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の男女共同区域へと行ってみる。\n
この辺りで知っている場所といったら、最初に学生証を作ってもらうために訪ねたナイトメアの医務室ぐらいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（……ナイトメア、元気かしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校生活が始まってからは、あまり見かけていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校医を呼ばなくてはいけないような怪我や病気をしていないと考えれば、それに越したことはないのだけれども。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（ちょっと、覗いてみようかな？）"

menu:
    "顔を見にいこう。":
        jump gakuen_nightmare1_2a
    "仕事の邪魔したら悪いわよね。":
        jump gakuen_nightmare1_2b
label gakuen_nightmare1_2a:
$ lovechara_nightmare_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく見かけていないことだし、顔を見に行ってみよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……生きているといいんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "青白い顔や、病弱そうな様子を思い出すと冗談でなくそんなふうに思った。\n
ナイトメアは放っておくと、いつのまにか倒れていそうな気がしてならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（放っておけないっていうか……、心配になっちゃうのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、医務室を訪ねてみることにした。"

jump gakuen_nightmare1_3
label gakuen_nightmare1_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "便りがないのは元気な証拠。\n
ナイトメアに何かあったなら、塔でも騒ぎになるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一応、あれでも責任者……らしい。\n
それなりにやっているだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（私が心配するようなことでもないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仕事の邪魔をしてしまっては、グレイに悪い。\n
医務室を訪ねるのは、やめておくことにした。"

jump gakuen_nightmare1_3
label gakuen_nightmare1_3:
with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0774
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0019
Nightmare "「おい……っ！\n
君っ！[firstname]……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……？」"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の廊下を歩いているところで、誰かに名前を呼ばれた。\n
立ち止まって、きょろきょろと周囲を見渡してみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……誰もいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（気のせい？\n
でも、それにしては、やけにしっかりと聞こえたけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nig_g0020
Nightmare "「ここだっ、ここだよ……！\n
上だ、上！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "囁きかけるような声は尚も聞こえる。\n
どうやら、気のせいではないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……上？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はついっと視線を持ち上げて……、悲鳴をあげそうになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！？」"


play music nightmare_t_ali
show m_nai1_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔色の悪い銀髪の男が、べたりと天井に張りついていたのだ。\n
手足を突っ張って、身体を固定している。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「な……っ、ナイトメア！！？\n
あなた、何やって……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice nig_g0021
Nightmare "「しぃいいいいい！！\n
大声を出すんじゃない！見つかってしまうだろう！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「み、見つかるって、あなた……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相当に目立っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通は天井に人が貼りついていると思わないから、見上げたりしなければ死角かもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、一度天井を見上げてしまえば悪目立ちしているとしか言いようがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（く、蜘蛛のお化けか何かみたいだわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "冗談みたいな光景だ。\n
魔法学校といえど、そう見ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア高位魔法学校の塔で、彼は学校医のはずだ。\n
何故、どうして、学校医が天井に張りついているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……何やっているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice nig_g0022
Nightmare "「……そ、そこにグレイはいないだろうな！？\n
どうだ、[firstname]、ちょっと見てくれ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「グレイ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われて周囲を確認するが、ちょうどこの時間帯ここはちょっとしたエアポケットになるのか、私達以外の人影はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒はおろか、使用人の姿もなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「いないわよ。\n
どうしたの？グレイを探しているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice nig_g0023
Nightmare "「まさか……！\n
逆だ、グレイから隠れているんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……グレイから？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、訝しげな視線でナイトメアを見上げる。あまり親しいというわけではないが、グレイの私の中における印象はとてもいいものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その彼から、逃げなくてはいけないような理由が想像できない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……あなた、何をしたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0024
Nightmare "「っ……、酷いぞ、[firstname]！！\n
どうして、そこで、私が何かをしたことになるんだ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「だって、グレイが何か悪いことをするだなんて想像できないんだもの。\n
あなたが彼に何かして、それで彼に追われていると考えたほうがしっくりくるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（ナイトメアが何かをやらかす図なら、簡単に想像がつくもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice nig_g0025
Nightmare "「……むう。\n
君、何か今、とっても失礼なことを考えていただろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「まさかまさか、そんなことないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice nig_g0026
Nightmare "「な、なんとなく分かる気がするんだ！\n
君が何を考えているかがな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……へえ。\n
気のせいよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice nig_g0027
Nightmare "「……ふん。\n
まあ、グレイがいないなら降りてやるとするか」"

play sound se_0724
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（偉そうに……）"

play sound se_0216
hide m_nai1_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは、ぱっと天井で突っ張っていた手足から力を抜くと、ふわりっと廊下へと降りてきた。\n
まさに風船のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「それで、どうしてグレイから逃げているの？」"


show nai_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice nig_g0028
Nightmare "「はは、グレイだけじゃないぞ！\n
私は、とてもたくさんの人間に命を狙われている！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……へえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……それ、グレイにも命を狙われているっていうふうに聞こえるわよ？」"

hide nai_m_03_11
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice nig_g0029
Nightmare "「そうだとも！！\n
あいつは私を殺そうとしているんだ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ええ？\n
あなた、熱でもあるの？」"

hide nai_m_02_4
show nai_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice nig_g0030
Nightmare "「むむむ、君はどうしてそうグレイの味方ばかりするんだ！？\n
私より、あいつのことが好きなのか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「話が飛躍しすぎよ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どちらが好きかといえば、どちらも好きでも嫌いでもない。\n
ナイトメアにしてもグレイにしても、好意を語るような間柄ではなかった。"

hide nai_m_03_6
show nai_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0031
Nightmare "「だったら、私の味方をしてくれ。\n
いいだろう、[firstname]？」"

hide nai_m_02_7
show nai_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0032
Nightmare "「君しか私の味方はいないんだ。\n
私を、この恐ろしい牢獄から救ってくれないか……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「何よ、恐ろしい牢獄って」"

hide nai_m_02_8
show nai_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice nig_g0033
Nightmare "「いいから！\n
助けてくれ！」"
$ gakuen_nightmare1_6a_seen = False
menu:
    "救う。":
        jump gakuen_nightmare1_4a
    "放っておく。" :
        jump gakuen_nightmare1_4b
label gakuen_nightmare1_4a:
$ gakuen_nightmare1_6a_seen = True
$ lovechara_nightmare_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（なんだか、よく分からないけれど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "救ってほしいと助けを求めているのならば、手助けくらいなら……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「で？\n
救うって、どうしたらいいの？」"

hide nai_m_03_2
show nai_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
Nightmare "「……！！！」"

hide nai_m_03_3
show nai_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice nig_g0034
Nightmare "「助けてくれるのか！！\n
君は、まるで女神のようだな！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……はいはい。\n
だから、それでどうしたらいいの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こういう子供のような反応は、ペーターで慣れている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、ナイトメアは大人の男のはずなのに、子供のような振る舞いをする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私までつられてしまいそうだ。"

hide nai_m_01_6
show nai_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0035
Nightmare "「そうだな。\n
私に、姿隠しの魔法をかけてくれないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……え？\n
そんなことでいいの？」"

hide nai_m_02_3
show nai_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice nig_g0036
Nightmare "「ああ、それで充分だ。\n
……ふふ、グレイの奴も、私が姿隠しの魔法を使うとは思うまいっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姿隠しの魔法なんて、魔法使いの子にとっては、かくれんぼの基礎だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "子供同士のかくれんぼの場合、姿隠しの魔法がアリかナシかで派閥が分かれるし、そもそもそれ以前に魔法そのものがアリかナシかで揉める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "運動神経は悪くても、魔法の腕のいい子なら魔法アリのルールのほうが嬉しいし、その逆の腕白坊主の場合は魔法ナシのルールで遊びたがる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "互いのルールの折衷案を作るだけで、一日が潰れるなんてことも多々あるほど。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「もしかして、ルールで姿隠しの魔法は駄目なんていうのがあるの？\n
それなら私、ルール違反は嫌よ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たとえば、かくれんぼに参加しているナイトメア自身には姿隠しの魔法を使ってはいけないという模範ルールがあるとしても、外野にはそれは適用されない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（それで、私を共犯者に……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（っていうか、この人、かくれんぼなんかしているの？？？）"

hide nai_m_02_12
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice nig_g0037
Nightmare "「いやいや、私達の間にそんな明確なルールはないとも。\n
遊びじゃあないからな」"

hide nai_m_02_4
show nai_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice nig_g0038
Nightmare "「お互い命がけだ。\n
真剣にならざるを得ない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう語るナイトメアの横顔は、とても真剣だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（命がけのかくれんぼ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……大袈裟よ」"

hide nai_m_02_5
show nai_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0039
Nightmare "「大袈裟じゃないとも。\n
……さ、ほら、早く姿隠しの魔法をかけてくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（なんで、自分でかけないのよ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "疑問は残るものの、彼は職員。\n
一応、目上にあたる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアに急かされて、懐から杖を取り出すと呪文を唱えた。"

play sound se_0496

show magic_b onlayer master
with dis
pause 1.5
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

play sound se_0731
pause 1
hide nai_m_03_10 with grad_b_medlong
pause 1


hide magic_b with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice nig_g0040
Nightmare "「はは、これはいい！\n
ありがとう、[firstname]、君のおかげで助かったよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の声だけが、彼がいるのであろう場所から聞こえてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「今度、ちゃんと事情を説明しなさいよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice nig_g0041
Nightmare "「話せる範囲でなら話すと約束しよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……そんな限定されたのじゃ、納得いかないわ」"

jump gakuen_nightmare1_5
label gakuen_nightmare1_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（どうも、胡散臭い……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "具体的に何をしてほしいというわけでもなく、救ってくれなんて広義でしか話を持ち掛けてこないあたりがかなり怪しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"
show nai_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice nig_g0042
Nightmare "「な、なんだその目は。\n
君、もっと他人を信じる心をもたないとよくないぞ！？」"

hide nai_m_03_7
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice nig_g0043
Nightmare "「勇気を出して、私を助けるんだ！\n
さあ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……本格的に、胡散臭い）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「悪いことは悪いと言う勇気も大事よね。\n
……とにかく、ちゃんと事情を聞かない限り、助けられないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっぱりと、告げる。\n
下手に騙されでもしたら、他の人へも迷惑がかかりそうな気がする。"

hide nai_m_02_4
show nai_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「っ！」"

hide nai_m_03_7
show nai_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0044
Nightmare "「た、頼む、お願いだ、助けてくれ！\n
君しか頼れる人がいないんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは泣き落としに出てきた。"

hide nai_m_03_3
show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0045
Nightmare "「何、難しいことじゃない！\n
姿隠しの魔法をかけてくれるだけでいいんだ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「駄目よ。\n
そんなこと言っても、ちゃんと事情の説明が出来ないんだもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「自分の魔法がどのような効果を及ぼすのか、把握しないままに力を使うのはよくないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（っていうか、なんで、自分でかけないのよ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姿隠しの魔法なんて、そう難易度は高くない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「何か、制限でもかけられているの？\n
悪いことなら、加担できないわよ」"

hide nai_m_02_10
show nai_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice nig_g0046
Nightmare "「……そうか。\n
君は……、君はっ、私に死ねと言うんだな！？」"

hide nai_m_02_8
show nai_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice nig_g0047
Nightmare "「鬼！悪魔！！意地悪！！」"

play sound se_0119
hide nai_m_03_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは、ついには諦めたのか走り去っていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……結構、元気そうな人ね）"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "具合の悪そうな顔をしていたり、死ぬだの口走っているが、天井に張りついたりあれだけ走れるのなら大丈夫だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、走り去ったナイトメアを見送り、探索を続けることにした。"

jump gakuen_nightmare1_5
label gakuen_nightmare1_5:
with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_par02_ct_tow_day
with stripe_l_long

play music dining_day_p_wam
play sound se_0229
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その後、しばらくあちこちを見て回ってから、カフェテリアへと向かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "基本的に設備としては食堂とよく似ており、生徒が頭でイメージした食べ物により近いものを提供するという魔法が備わっている……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……のだが、そのメニューには違いがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食堂のメニューがボリュームのあるしっかりしたものが多いのに対し、カフェテリアのメニューは飲み物や軽食を中心とした、あっさりとしたものが多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後の雑談や、朝食時などには、食堂よりもこちらを使う生徒のほうが多かったりもする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昼食や夕食などしっかり食べたいときには食堂を、朝食やおやつ時にはカフェテリアをというふうに、皆使い分けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私もそんな生徒の一人で、一息いれたいときにはこちらを使うようにしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……ふう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "テーブルの上に温かいココアを呼び出して、文字通り、一息つく。"

play sound se_0177
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……ナイトメアに遭遇しただけなのに、疲れたわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "温かく、甘いココアを飲んでいると、ゆるゆると疲れが取れていくような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0065
Seito "「まだ、ナイトメア先生、見つかってないらしいぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0037
Seito "「使用人達、必死だったよな……。\n
締め切りの近い書類が、大量に溜まっていたって話だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0066
Seito "「グレイ執務長が、すごい形相で駆け回っていたぞ。\n
……相当、まずいみたいだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0038
Seito "「相当っていうか、ナイトメア先生はいつもまずいだろ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0067
Seito "「そんな中でも、相当、だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き捨てならない会話を聞いてしまった。\n
私は立ち上がると、そんな話をしていた彼らへと歩み寄った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ねえ……、ちょっと詳しく聞かせてくれない？\n
ナイトメア先生がどうしたっていうの？」"


show boy_a1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice suz_g0068
Seito "「え？\n
ああ、興味ある？」"

hide boy_a1_2
show boy_a1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice suz_g0069
Seito "「ナイトメア先生が、また医務室から逃亡したんだよ。\n
このままじゃ私は死んでしまうっ、とかって感じで」"

hide boy_a1_5
show boy_a1_5 at left
with dis

show boy_b2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice tan_g0039
Seito "「まあ、実際、ナイトメア先生の体調って危うくてさ～。\n
でも、仕事してもらわないわけにはいかないだろ？」"

hide boy_a1_5
show boy_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice suz_g0070
Seito "「それで、仕事をさせたい使用人側と、逃げたいナイトメア先生の間で鬼ごっこになるってわけ。今回は、まだ見つかってないらしくってさ」"

hide boy_b2_1
show boy_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice tan_g0040
Seito "「いつもみたいに空間魔法を駆使して、逃げ回っているのかねえ。\n
ナイトメア先生、空間魔法だけは得意だよな」"

hide boy_a1_3
show boy_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice suz_g0071
Seito "「むしろ、それ以外の魔法を使っているところを見たことがないな。\n
……逃げてばっかだしな」"

hide boy_a2_8
show boy_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice suz_g0072
Seito "「噂じゃ、空間魔法の腕がずば抜けている分、他の魔法はからっきしっていうぜ？\n
姿隠しの魔法さえ使えないって聞いた」"

hide boy_b2_5
show boy_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice tan_g0041
Seito "「ともかく、双方、必死だよな。\n
俺達寮生としては、グレイ執務長の剣幕がすごいから、早く見つかってほしいけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「…………。\n
……ありがとう」"

hide boy_a2_2

hide boy_b1_9
##[chara2 PAY ATTENTION="false"]
if gakuen_nightmare1_4a_seen == True:
    jump gakuen_nightmare1_6a
jump gakuen_nightmare1_6b
label gakuen_nightmare1_6a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（とんでもないことをしちゃったかも……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの口車に乗せられて、その逃亡に力を貸してしまった。\n
命がけだの何だの……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嘘ではないが真実でもないという詭弁だ。\n
まともにとったわけではないが、片棒を担いだことは事実。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_9")
T "（～～～っ！！\n
ナイトメアの奴、次会ったときは覚えていなさいよっ！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪態をつきたいのを抑え、グレイや使用人達に正しい情報を伝えるべく、カフェテリアを後にした。"

with dis
$ hi_mes()

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
$ routechara = "Nightmare"
jump gakuen_friend_check_tower
label gakuen_nightmare1_6b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（……よかった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの口車に乗せられなくてよかった。\n
やはり説明できないことというのは、ろくでもない事情だったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仕事をしたくなくてサボって逃げ回っているだなんて……、片棒を担がなくて本当によかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（実際、体は悪いみたいだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "（……早く、みつかればいいのに。\n
逃げ回るよりは、治療でも受けたほうがいいわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうに思いながら、温かいココアを口に運ぶ。"

with dis
$ hi_mes()

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
$ routechara = "Nightmare"
jump gakuen_friend_check_tower
