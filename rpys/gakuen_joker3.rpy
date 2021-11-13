label gakuen_joker3:
scene bg_map_day
with dis
$ clockanim()

jump gakuen_dream_other
label gakuen_joker3_2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「だから……。\n
恋愛なんて嫌なのよ……」"

with dis
$ hi_mes()

scene bg24_rj_day ##instant]

with open_m

play music room2_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鬱々と呻いて、私は目を開けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……暗くなる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "爽やかで明るい朝の光と、暗い気持ち。\n
カーテンの隙間から漏れ零れる陽光も、冷たくなった気持ちを温めてくれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最悪な目覚めだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「……ああ、もう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、ずっと姉に憧れていたらしい。\n
彼自身がそう言ったわけではないが……、きっと私に親切にしてくれたのも、私が姉の妹だったからなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼にとって私は、「[firstname]＝[familyname]」ではなく、「ロリーナ＝[familyname]の妹」だったのだ。"

show m_jo3_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（……姉さん）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完璧に美しく、優しく、聡明な姉を思うと胸が痛んだ。\n
全寮制の学校に行きたかった、本当の理由。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私を通り越して姉を見ていた彼に、自分を見てくれているという幻想を抱いていたなんて、今思い出しただけで羞恥で死にたくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう、私は文字通り、逃げ出したのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（……帰らなくちゃ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唐突に、そんな強いホームシックにも似た感情に襲われた。\n
どうしてだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "急いで家に帰らなければいけないような気がする。"

hide m_jo3_1
show m_jo3_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_12")
T "（皆に会いたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完璧で、美しく、優しい聡明な姉。\n
明るくおませで、ちょっと生意気な、妹のイーディス。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして仕事で忙しくしながらも、私達三姉妹のことを常に想ってくれている父親。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大切な家族に会いたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（大切で……、完璧な）"

hide m_jo3_2
show black onlayer master
with dis
play sound se_0638
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……っ）"

play sound se_0263
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢の中だというのに、眩暈がしたような気がした。\n
違和感がまるでノイズのように、眼裏に浮かぶ家族の姿を切り裂いていく。"

hide black
show m_jo3_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……これは、何？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深層心理か、警告なのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、それほど愚かではないのかもしれない。\n
中途半端に、夢に溺れずにすむ程度には、賢い。"

with dis
$ hi_mes()

scene bg06_sk_h_day ##instantPAY ATTENTION="true"]
hide m_jo3_3


play music room2_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "懐かしくも苦い夢の記憶……。\n
それ以外にも何かあったような気がするが、うまく思い出すことが出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不明瞭なそれらを洗い流すように、顔を洗い、制服に着替える。\n
身だしなみを整えてから、カフェテリアへと移動した。"

play sound se_0774

scene bg25_rr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……ん？）"

play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこに向かう間に気付いた。\n
なんだか、空気がざわざわとしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "音、という意味だけでない。\n
寮内ですれ違う生徒が皆、そわそわしているような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よくよく見れば、そんなふうに浮ついた空気を漂わせているのは生徒だけでもないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓から見た先、何故か庭でバットを素振りする使用人の姿が見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（？？？）"

jump gakuen_cafeteria_notcastle
label gakuen_joker3_3:
with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後になると、周囲の落ち着きのなさはますます増していった。\n
そわそわと視線を交し合ったり、私には分からない暗号のような単語を交し合う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなのを聞いていても気になるだけなので、私はいつものように図書館に行くことにした。"


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの図書館はとても広大で、なんでも本の量にあわせ、今でも館内の拡張を続けているのだそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うまく探しさえすれば、たいていの本は見つかる。\n
本好きの部類である私にとっては、ありがたい場所だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "図書館で適当に本を見繕って、塔のカフェテリアに行くのもいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアには食堂と同じような種類の魔法がかかっていて、軽食の類を呼び出すことが出来るのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "温かい飲み物と、面白い本の組み合わせ。\n
至福のひとときを思いながら、図書館に向かって歩き出す。"

play sound se_0776

play music corridor_day_p_wam
show m_jo3_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0070
Seito "「今日の……どうする……だよな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0057
Seito "「そこは……して……調べておくよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下の片隅で、何人かの男子生徒が集まってこそこそと会話を交わしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "またしばらく歩いていくと、今度は階段のすぐ下で女子生徒が何人か集まっているのが見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0048
Seito "「……だから……で……よね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0111
Seito "「でもそうなると……だから……よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じように、ひそやかに抑えた声で言葉を交し合っている。"


scene bg27_rk_day ##instantPAY ATTENTION="true"]
hide m_jo3_4

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞こえるのはあくまで会話の一部。\n
だが、周囲を気にしたように、楽しそうにこそこそと話し合う様からしても話題が例のイベントであるのは間違いない。"

menu:
    "楽しそうだ。":
        jump gakuen_joker3_4a
    "落ち込む。":
        jump gakuen_joker3_4b
label gakuen_joker3_4a:
$ lovechara_jokbla_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……楽しそう、よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らが楽しそうに見えるからこそ、その中に入れないのが少しばかり寂しい。\n
もちろんそれが、私達新入生を驚かせるためのサプライズなのは分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仲間外れにされているわけでないことも、知っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「でも、クラスが中級だと、仲間外れにならざるを得ないのよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "新入生同士で騒ぐことも出来ない。\n
図書館に向かって歩を進めながら、妙な孤独感に襲われた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアでは新入生にあたる私だが、前の学校で得た知識と経験のおかげで授業自体は中級クラスから始まっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのため、周囲に同じ新入生がいないのだ。\n
結果、上級生の中に新入生が一人というような図になってしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うまく馴染めないように感じてしまうのも、そのせいなのかもしれない。"

jump gakuen_joker3_5
label gakuen_joker3_4b:
$ lovechara_jokwhi_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……なんだかなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスや、クラスメイト達の言う「知らないほうが楽しめる」という言葉に嘘はないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっと、新入生に対するサプライズのイベントなのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲の使用人や、クラスメイト。\n
皆がそわそわとしているのもそのためだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、楽しみにするべき。\n
楽しむべきだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、廊下を歩く私の気分はずいぶんと沈んでいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（馬鹿みたいだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしてこんなにも、落ち込んでしまうのか。\n
馬鹿げてはいるが、その理由はしっかりと自分でも分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あちこちで盛り上がっているのを見かけるのに、その内容を自分が知らないことで、周囲から置いていかれてしまったような錯覚を覚えてしまっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（仲間はずれにされているみたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "錯覚だということは分かっているのに……、一人ぼっちな気分がして。"

jump gakuen_joker3_5
label gakuen_joker3_5:
with dis
$ hi_mes()

scene bg_map_day
with stripe_l_medium

scene bg15_lb_o_day
with stripe_l_long
play sound se_0566
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、放課後は図書館で過ごすことにした。"


scene bg15_lb_i_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "図書館は飲食禁止という残念なところもあるが、その代わり静かだ。\n
今の私には、静寂というのはプラス面。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……やっぱり、どうしても気になっちゃうもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "閉館時間ぎりぎりまで図書館で過ごし、それから食堂に向かうことにした。"

play sound se_0718

scene bg15_lb_i_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本のページをめくるついでに、ちらりと顔をあげて窓の外の景色を見やる。\n
夕日はすでに沈み、空のふもとをほの赤く染めるだけだ。"


scene bg06_sk_h_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろそろ、夕食の時間。\n
夜は近い。"

$ hi_mes()

scene bg_map_eve
with stripe_l_long
##endmemory
jump gakuen_joker4
