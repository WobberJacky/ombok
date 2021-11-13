label gakuen_routechoice:
stop music
show black with fade
$ renpy.movie_cutscene("Opening_video.mpg")
play music classroom_day_p_wam

scene bg_map_day
with stripe_l_medium

scene bg10_sb_day
with stripe_l_medium

scene bg01_cr_day
with stripe_l_long
play sound se_0497
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がシンフォニア高位魔法学校に来てから、そろそろ一週間が過ぎようとしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮での生活にも慣れてきたし、学校の授業にも慣れてきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初にゴーランドが言っていたとおりに、シンフォニアでは自分の習熟度に合わせて授業を選ぶことができる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その結果、私はシンフォニアに不慣れな新入生でありながら、授業のレベルは中級程度からスタートというややこしいことになってしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おかげでどのクラスでも、周囲にいるのは先輩にあたる在校生ばかりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……といっても、同年代に見える子から、年下っぽい子、年上に見える人まで、年齢はばらばらみたいね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校というよりも、研究施設の教習所のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（ただし、ものすごく難関の教習所。\n
……その一員になれたんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業の難易度としては、問題はない。\n
だが、こうして授業を受けていくと、シンフォニアと私の常識との違いに気付かされることも多くある。"


show kyoushi_b_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0063
Kyousi "「はい、それでは、各自実験を始めなさい。\n
材料に関しては、準備室に揃えてあるから、好きなものを使っていいぞ」"

play sound se_0497

play music test_wam
hide kyoushi_b_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "担当教師の実験開始の号令に、席から立ちあがり、準備室へと向かう。\n
これは魔法薬学の授業だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ新学期の授業が始まったばかりだからなのか、これまでの復習めいた、それほど難易度の高くない実験を課題にされることが多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0117
Seito "「ラズル石とカナル溶液の混合実験なんて、楽勝だよな～」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0083
Seito "「まあ、まだ新学期も始まったばっかりだしなあ。これから先、いやおうなしに難易度もあがるんだろうし、今のうち楽しておこうぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0118
Seito "「……とかいって、失敗したりしてな。\n
これで失敗したら、格好つかないぜ～？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0084
Seito "「う……。\n
そういう、嫌なプレッシャーをかけるなよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "準備室で材料を選ぶ傍ら、交わされる男子生徒達の会話を聞く。\n
愚痴のような軽口を叩きながらも、楽しげだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（でも、油断すると、本当に失敗するわよ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ラズル石とカナル溶液の混合実験は、難易度は低い。\n
だがそれも、丁寧にやれば、という条件つきだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きちんとした手順で、正確に行えば確実に成功するというようなものなのだ。\n
それだけに、集中しないと失敗することも多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……意外だなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が通っていた学校でも、ラズル石とカナル溶液の混合実験は、魔法薬学の基礎としてよく行われていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアのような優秀な学校でも、それが変わらないということが驚きだ。\n
もっと、高度なことばかりしているのかと思っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（逆、なのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "優秀な学校だからこそ、基礎を大事にしているのだろうか。\n
必要な材料を幾つか選んで教室へと戻る。"

play sound se_0039
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まずはラズル石の重さを量って、ちょうどいい比率でカナル溶液をビーカーに注ぐ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「濃度の指定はなかったから……。\n
一般的な溶液濃度だと６０パーセントね」"

play sound se_0174
play sound se_0177
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここで面倒くさがって目分量などにすると、いろいろと後で不都合が生じるのだ。\n
三脚の上に金網を乗せ、その上にビーカーを設置する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後は、マジックランプに点火し、熱していくだけ。\n
手順としても、使用する道具にしても、難易度は高くない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いかに丁寧にするかが、成功に関わってくる。\n
点火する前に、ビーカーの中へとアセリアの花びらを数枚落とした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実験には直接関係ないが、アセリアの花びらには急激な反応を防ぐ緩和剤の効果がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "マジックランプへと手をかざし、魔力を流し込みながら、呪文を唱えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の魔力を燃料に、マジックランプへと火が灯る。"

play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「…………」"

play sound se_0608
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「……よし、っと」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これで間違えていないはずだ。\n
幾度となく、前の学校でも繰り返し習ってきた手順だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、なんとなく不安になってしまうのは、自分がシンフォニア高位魔法学校なんていう特別な場所に来てしまったからなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……場違いなこと、してないといいんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分ひとり、頓珍漢なことをしていたらと考えて、不安になる。そんな不安を誤魔化すように、私はビーカーの中をぐるぐるとガラス棒でかき混ぜた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "反応は順調に進んでくれているのか、ガラス棒に当たる固体の感触は、もうだいぶ小さくなり始めている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カナル溶液は、色が濃いせいで中に落としたラズル石を視認することができない。\n
混ぜるガラス棒に返ってくる感触が、実験の経過を教えてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この調子でうまく溶けてくれれば、実験は成功だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（……いい調子）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここまで反応が進めば、後は連鎖的に反応が進んでいく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_20")
T "「…………」"

play sound se_0739
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひらり、と手をかざして、マジックランプの火を止めた。"


show girl_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0051
Seito "「あら、[firstname]。\n
あなたもう火を止めちゃうの？」"

hide girl_a2_3
show girl_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0052
Seito "「全然反応していないのに、大丈夫？\n
それとも、何か問題でも？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "向かい側から声をかけられて、そちらへと視線をやった。\n
火も止めてしまったので、もうビーカーから目を離しても大丈夫だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（全然反応していない？\n
きちんと反応しているように見えるんだけど……）"

play sound se_0176
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手応えを確かめるように視線をビーカーへと戻して、ガラス棒でもう一度かき混ぜてみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ガラス棒に当たるカナル石の感触は、先ほどよりもさらに小さくなっているようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……順調、よね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ちゃんと反応していると思うんだけど……。\n
私、何か間違えている？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やりなれた実験だったこともあり、特に周囲に確認することなく進めてしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかして、何か勘違いしてしまっているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（間違えているんだったら、やり直さなくちゃ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "斜め向かいの席で同じ実験をしているはずの、彼女の手元を見やる。"


play music gag1_a_wam

show m_kyoutuu1_1 onlayer master
with dis
hide girl_a2_2

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「！？」"

play sound se_0643
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女の手元にあるビーカーは、恐ろしいほどにボコボコと音をたてて煮立っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ラズル石とカナル溶液は熱を加えることで薬学変化を起こすが、反応の際に自らも熱を発生させる。だからこそ、連鎖反応で次々と反応が起こっていくのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、急激に反応が進むことにより高熱が発生してしまう現象のことを、過反応と言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女のビーカーの中身は、明らかにその過反応を起こしてしまっているように見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「そ、それ大丈夫なの！？\n
過反応になっちゃっていない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "過反応が危険なのは、その熱に耐え切れなくなったビーカーが割れてしまう可能性が高いからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくら危険な物質ではないとはいえ、高温の薬液が飛び散るのは危ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、慌てているのは私だけで、そのビーカーの主である彼女は訝しそうに首を傾げていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0053
Seito "「え？\n
この実験ってこういうものでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0054
Seito "「過反応を起こさなきゃ……。\n
あなたのビーカーの方こそ、ちっとも反応していないけど大丈夫なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女の言いようでは、過反応を起こすのが当然とでもいうようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きょろきょろと、改めて周囲の他の生徒のビーカーの様子を見てみると、ほぼ全員が過反応、もしくはそれに限りなく近い状態になっていることに気づいた。"

play sound se_0377
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（こ、こわ……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつ、誰のビーカーが割れてもおかしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Seito "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0055
Seito "「[firstname]、顔色よくないけど大丈夫？\n
具合でも悪いの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「大丈夫よ、具合は悪くないわ。\n
ただ……、いつどこでビーカーが割れるかとハラハラしているの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "具合が悪い、というよりも心臓に悪い。\n
そんな私に彼女はやはり訝しげだ。"

hide m_kyoutuu1_1
show m_kyoutuu1_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0056
Seito "「滅多にビーカーが割れるようなことはないわよ？\n
だって、ビーカーに強化の魔法をかけてあるもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0057
Seito "「過反応の熱に負けるような強化魔法だと、駄目だけれどね。\n
そんなドジをする生徒、あんまりいないから平気よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ビーカーに、強化魔法？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice may_g0058
Seito "「ええ。\n
あなたも、当然、かけているんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（当然？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「かけていないけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice may_g0059
Seito "「！？\n
危険じゃない！すぐにかけないと！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どう見ても、危険なのは煮立っているほうのビーカーだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「私は、そもそも過反応を起こさないように、アセリアの花びらを入れてあるから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「だから、ビーカーに強化魔法をかけていないの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice may_g0060
Seito "「アセリアの花びら？\n
ああ、そっか、アセリアの花びらには、中和作用があったわよね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice may_g0061
Seito "「ってことは、それ、反応進んでいるの？\n
へえええ、アセリアの花をいれると、そんなに静かに反応が進むのね……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女は感心したように言いながら、私の手元にあるビーカーを覗き込む。\n
一方、彼女のビーカーは、相変わらずぼこぼことすごい音を立てている。"

play sound se_0139
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（うわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "強化魔法がかけてあるおかげで、ビーカーが割れて大惨事……、なんて心配はない。しかし、分かっていても、怖くなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0062
Seito "「それ、あなたのアイディアなの？\n
アセリアの花を使って、過反応を起こさないで実験を進めるっていうの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「まさか。\n
これは私が前の学校で習ったやり方よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「たぶん……、シンフォニア以外の学校ではだいたいどこも、この方法で教えるんじゃないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「だって、万が一にでも事故が起こったら危ないもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice may_g0063
Seito "「へえ、そうなの？\n
私たちは、ビーカーを強化するほうで習ったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice may_g0064
Seito "「中和作用があるとはいえ……。\n
アセリアの花を入れることで、結果に何か影響が出たりはしないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「誤差はほとんどない、って私は習ったわね。……あなたが言ったみたいに、ビーカーを強化する方法だと失敗のデメリットが大きすぎるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアと違い、生徒の魔法の腕にばらつきのある一般の学校では、過反応の熱からビーカーを守りきるだけの強化魔法を使える生徒は、そう多くない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "アセリアの花を使った中和は、より安全な上に確実だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただし、過反応を使った実験の場合、急激に反応が進む分結果を早く得ることができるというメリットもある。"


play music test_wam
hide m_kyoutuu1_2
show m_kyoutuu1_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0065
Seito "「あなた……、他所の学校から、シンフォニアに進学してきたのよね？\n
他の学校の話って、新鮮だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0066
Seito "「私も他の多くの生徒と同じで、最初からシンフォニアに来たものだから他の学校を知らないの。同じ実験なのに、基本の操作が違うなんて面白いわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……ええ、本当に」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し……いや、かなり驚いてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「私も、シンフォニアに来て毎日が新鮮よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返事がワンテンポ遅れる。\n
彼女が、当たり前のように違いを認め、それを楽しんだことが意外だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの生徒というのは、もっと……、言い方は悪いが、シンフォニアこそが世界一の魔法学校だという自負に凝り固まっているものだと思っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "経験の違いを、レベルの差、なんて解釈で終わらせられなかったことが嬉しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「私、今度はビーカーを強化する方法でやってみようかしら。\n
ねえ、割れそうになったら助けてくれる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice may_g0067
Seito "「当然よ。\n
それなら私も、次はアセリアの花を使ってみようかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice may_g0068
Seito "「私には、どれくらいの比率でアセリアの花を使うのか教えてくれない？\n
是非、そちらの方法も試してみたいの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「ええ、もちろん構わないわ」"

play sound se_0132
pause .2
play sound se_0132
hide m_kyoutuu1_3
show m_kyoutuu1_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、手元ですっかり反応を終えたらしいビーカーを軽く揺らしてみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "熱した時間が少なかったこともあるのか、ビーカーの上部は熱を持ってはいるものの、触っていられないほどではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とろりと粘度を増した濃い色の液体が揺れた。\n
固体が当たる感触はないので、ほぼ完全に溶け切ったと考えてもいいだろう。"

play sound se_0176
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "念のためガラス棒でかき混ぜてみるが、やはり何か固いものが入っている感触はなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「よし、私のほうは出来たみたい。\n
そっちはどう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "過反応を使って一気に反応を得るのがシンフォニアスタイルだというのなら、彼女の実験ももう終わっていておかしくない。"

hide m_kyoutuu1_4
show m_kyoutuu1_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0069
Seito "「え、と……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、彼女のビーカーの中身は、相変わらず激しく踊るように煮立っていた。"

play sound se_0570

play music gag1_a_wam
hide m_kyoutuu1_5
show m_kyoutuu1_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice may_g0070
Seito "「え～～……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その上、煙までがもくもくと吹き上がり始める。"

play sound se_0731
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ね、ねえ、それ、煙も出るものなの……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までに、実験に失敗して過反応を起こしてしまった例も見てきたが、こんなふうに煙が発生するのは初めて見た。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「こんな反応、初めて見るんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice may_g0071
Seito "「……私も初めて見たわ。\n
やっぱり目分量はよくなかったのかしら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……間違いなく、それが原因だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "断言できる。\n
薬学実験は繊細な計量こそが、成功の秘訣なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「なんだって、薬学で目分量なんて無茶をするのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアだから、なのだろうか。\n
自信があるのか、アグレッシブというか……、アバウトすぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0072
Seito "「それは……。\n
……はあ、やっぱり、ウァーロック先生みたいにはいかないわよね～」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「ウァーロック先生？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice may_g0073
Seito "「これとは別の薬学系の授業を教えてくれている先生なんだけどね。\n
なんと、実験すべてを、目分量で成功させちゃうのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「それは……、すごいわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すごい技術だ。\n
だが、生徒の参考にはならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……むしろ、真似しちゃいけないんじゃないかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice may_g0074
Seito "「ええ、すごいでしょう？\n
私も真似できないかと思ったんだけど、やっぱり駄目だったみたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……そうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私と彼女は、じっともくもくと煙を吐くビーカーへと視線を落とす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "計量における正確性が肝というような実験で、目分量など教えるほうも教えるほうだが、やるほうもやるほうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……あ」"

with dis
$ hi_mes()
hide m_kyoutuu1_6


scene bg06_sk_h_day
with dis
play sound se_0659

scene bg_sky_wa_day with Dissolve(1.5)
camera at hpunch
camera at vpunch
pause .15
play sound se_0318

scene bg06_sk_h_day with Dissolve(1.5)
play sound se_0543

scene bg01_cr_day with Dissolve(3)

scene bg_map_day
with stripe_l_medium

scene bg10_sb_day
with stripe_l_medium

play music classroom_day_p_wam

scene bg01_cr_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法薬学の授業が終わった後、実験器具の片付けをしているところで、同じく片付けの途中らしき何人かのクラスメイトに声をかけられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "クラスメイト、といっても、基礎クラスで一緒の子達ではない。\n
この授業を一緒に取っている子達だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中には、先ほど実験を一緒にやっていた子もいる。"


show girl_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0075
Seito "「ねえねえ、お昼一緒に食べない？」"

hide girl_a2_2
show girl_a2_2 at left
with dis

show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0151
Seito "「私達食堂に行こうと思っているんだけど～……」"

menu:
    "一緒に食べにいく。":
        jump gakuen_routechoice2a
    "断る。":
        jump gakuen_routechoice2b
label gakuen_routechoice2a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ありがとう、誘ってくれて嬉しいわ。\n
ちょうど、今日のお昼何にしようかな、なんて考えていたところだったの」"

hide girl_a2_2
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice may_g0076
Seito "「ほんと？\n
タイミングよかったわね」"

hide girl_b1_3
show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice tak_g0152
Seito "「女神・ローレイのお導きね。\n
ああ、おなか減った～……」"

hide girl_a2_3
show girl_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice may_g0077
Seito "「それじゃあ、さっさと片付けちゃいましょうよ」"

hide girl_b1_2
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice tak_g0153
Seito "「今日のランチメニューが気になるわね～」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ほんとほんと。\n
出し方さえ間違えなければ、美味しいもの」"

hide girl_a2_2
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice may_g0078
Seito "「……間違えなければ、ね」"

hide girl_b1_3
show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice tak_g0154
Seito "「……間違えないといいわね～。\n
ああ、ローレイ、私達に正しい道を示したまえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「自力でなんとかしろって、天啓がくだるわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この国における宗教は、軽口が叩けるほど親しみやすいもの。\n
私も、実家では日曜に家族で礼拝に行くのが習慣だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「まあ、神頼みもしたくなるけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここシンフォニアの食堂では、食べたいものをイメージすると、それに一番近い規定のメニューが出されるというシステムになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのため、イメージが甘かったりすると、全然違うものが出てきてしまうことも少なくないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他国出身の生徒が多いこともあり、規定のメニューは尋常じゃなく幅広い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（正直……、口に合わないものもあるのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食文化の違いというのは、なかなか馬鹿にできない。\n
そんなことを話しながら、私達は和気藹々と片付けをして食堂へと向かった。"

with dis
$ hi_mes()
hide girl_a2_3

hide girl_b1_2


play music dining_day_p_wam

scene bg12_dn_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本日の食事は、当たりだったのか無難なものを食べることが出来た。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（クラスメイトの子達とも仲良くなれたし……。\n
いい時間を過ごせたわ）"

with dis
$ hi_mes()

scene bg10_sb_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
if place_of_stay == "Castle":
    jump gakuen_routechoice_castle1
if place_of_stay == "Hatter":
    jump gakuen_routechoice_hatter1
if place_of_stay == "Amuse":
    jump gakuen_routechoice_amuse1
if place_of_stay == "Tower":
    jump gakuen_routechoice_tower1

label gakuen_routechoice2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ごめんなさい、せっかく誘ってくれたんだけど……。\n
私、今日お弁当なのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は声をかけてくれた子達へと、眉尻を下げて向き直った。\n
お誘いはありがたいが、弁当を持ってきている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここシンフォニアの食堂では、食べたいものをイメージすると、それに一番近い規定のメニューが出されるというシステムになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのため、イメージが甘かったりすると、全然違うものが出てきてしまうことも少なくないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他国出身の生徒が多いこともあり、規定のメニューは尋常じゃなく幅広い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（正直……、口に合わないものもあるのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食文化の違いというのは、なかなか馬鹿にできない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなこともあって、たまに余裕がある朝などは、あらかじめ食べたいものを寮のキッチンで作ってしまうのだ。"


show girl_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0079
Seito "「[firstname]、あなた自分でお弁当作っているの！？\n
うわ～、すごいわね～！」"


show girl_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0155
Seito "「本当、偉いわ。\n
私、お弁当を作る時間があったら二度寝しちゃう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「私だって、毎日作っているわけじゃないのよ？\n
たまに気が向いたときに、ぱぱっと簡単なものを作る程度なの」"

hide girl_a2_4
show girl_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice may_g0080
Seito "「それが出来るのがすごいのよ。\n
私なんて魔法でも使わなきゃ、ぱぱっとお弁当なんて無理よ」"

hide girl_b1_5
show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice tak_g0156
Seito "「同感～。\n
それじゃあ、また今度あなたが学食のときに誘うわ～」"

hide girl_a2_5
show girl_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice may_g0081
Seito "「も、もしくは私達がお弁当を作れたら、一緒にご飯にしましょう」"

hide girl_b1_2
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice tak_g0157
Seito "「そっちのほうだと、いつのことになるやら……だけどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「ふふ。\n
でも、手料理のほうも期待しているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「皆で、中庭で食べても美味しいと思うわよ？」"

hide girl_a2_2
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice may_g0082
Seito "「う～ん。\n
シチュエーションとしては惹かれるんだけどねえ……」"

hide girl_b1_3
show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tak_g0158
Seito "「……善処します～」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな会話を交わしながら、授業の片付けを終わらせると、彼女達と別れて中庭へと向かった。"

with dis
$ hi_mes()
hide girl_a2_3

hide girl_b1_2


scene bg10_sb_day
with stripe_l_medium

play music garden_day_p_wam

scene bg20_gd_day
with stripe_l_long
play sound se_0088
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この時間帯の中庭は、とてものどかだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私と同じようにお弁当を持ち寄り、木陰で思い思いに食事をしている人も多い。\n
すでに食事を終えて、のんびりと横になっている人もいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……空いているかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までにも何回かお弁当を食べたことのある、木陰を目指す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら他に人がいるかもしれない……、とも思ったのだが、どうやら大丈夫だったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（ここでなきゃいけないってわけじゃないんだけど、定位置って落ち着く）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "木漏れ日の温かな木陰へと腰を下ろす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽかぽかとした陽気が気持ちいい。\n
ぼんやりとしながら、今朝方キッチンで作ってきたサンドイッチを口に運ぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誘ってくれた彼女達にはお弁当だなんて言ってしまったが、実際にはパンに具材を挟んだだけのサンドイッチ。\n
お弁当と言えるのかどうかは怪しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（見得を張っちゃったかな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、あの分でいくと、彼女達と弁当作りを競うということもなさそうだ。\n
この程度のものでも、多めに作って誘ってあげれば喜んでもらえるかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……ん？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふっと日差しが翳った。\n
視線を持ち上げる。"


play music view_day_p_wam

show m_kyoutuu1_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……人影だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逆光のせいで顔は判別できないが、男性だということは分かる。\n
女性にしては体格が違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（誰……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして、木陰でぼんやりとサンドイッチを食べている私のところまでわざわざやってくるぐらいなのだから、きっと相手は知り合いだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうに断定してしまったせいで、警戒心は働かない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0000
Hatena "「ふふ。\n
そんな夢見るような瞳で見つめられるとドキッとしちゃうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……{size=+20}誰？{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予想に反して、その声に聞き覚えはなかった。\n
口の中にあったサンドイッチをもぐもぐと咀嚼し、飲み込んでから口を開いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……え～と、あなたは？」"

hide m_kyoutuu1_7
show m_kyoutuu1_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "眩しい木漏れ日から角度を変えるべく、少し身じろぐ。\n
位置を変えたことにより、見下ろす男の顔を判別できるようになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やっぱり知らない顔だ。\n
制服を着ていないから、生徒でも使用人でもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0001
Hatena "「そんな身構えなくともいいじゃないか、[firstname]。\n
俺は無害な男だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名乗った覚えもない名前を、呼ばれる。\n
ますます得体がしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（まさか、ストーカー……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幼馴染のことが頭をよぎる。\n
私のことを追い掛け回す、物好きな白ウサギ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……いやいや、あんなのがぞろぞろいるわけがない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前の男は、耳も尻尾も生えていない。\n
正常に見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あなた……。\n
どうして、私の名前を知っているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jok_r0002
Hatena "「君だけじゃないよ。\n
俺はこの学校の生徒のことなら、よ～く知っているとも」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男の声音は柔らかだが、それでいて意味ありげに響いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（この学校の生徒のこと……、って。\n
いったいどれくらいいると思っているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア高位魔法学校は、世界一の魔法学校と自他ともに認められるだけあって広大な敷地面積を誇る。生徒の数だって、それに比例して当然多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "多国籍で、年齢だってばらばら、研究生も多い。\n
私のような編入生や、事情があっての受け入れを行うこともあると聞く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学年だけでクラス分けされるわけではないから、組織は非常に複雑化している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここの教職員だとしても、在籍する生徒の名前をすべて覚えているなんていうのは無茶だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……私は、あなたを知らないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice jok_r0003
Joker "「ああ、自己紹介が遅れてごめんね？\n
俺はジョーカーだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「ジョーカー？」"

hide m_kyoutuu1_8
show m_kyoutuu1_9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice jok_r0004
Joker "「そう、ジョーカーだ。\n
……ねえ、サンドイッチ、美味しそうだね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカーと名乗った彼が、さっさと断る隙もなく私の隣へと腰を下ろす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "物腰は柔らかだが、押しは強い。\n
そんな印象だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にこにこ、と見守れていると、どうにも食べ辛い。\n
直接ねだられたわけではないが、それに近い空気を感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……食べ辛い）"

hide m_kyoutuu1_9
show m_kyoutuu1_10 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "諦めて、サンドイッチの包みをすっと彼のほうへと差し出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……食べる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夕食の時間までにおなかが空いたらつまもうと思って、少し多めに作ってきてある。\n
ちょっとぐらいならば、分けても平気だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0005
Joker "「え、いいの？\n
君、優しいね」"

hide m_kyoutuu1_10
show m_kyoutuu1_11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いいの？と聞きつつも、行動は早い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょいと手を伸ばして、サンドイッチを手にとって口に運ぶ。\n
まったく遠慮がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0006
Joker "「……もぐもぐ。美味しい。\n
やあ、君、いい奥さんになりそうだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ただのサンドイッチよ？\n
料理、というよりも挟むだけだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice jok_r0007
Joker "「作り方が簡単だろうと、美味しいことに変わりはないよ。\n
必ずしも、難しいもののほうが美味しいってこともないだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「まあ、ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice jok_r0008
Joker "「……サンドイッチのお礼に、いいものをあげよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もぐり、と口の中にサンドイッチを押し込んで、完食したジョーカーがひらりと手を揺らした。"

hide m_kyoutuu1_11
show m_kyoutuu1_12 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か呪文や、印を刻んだというようには見えなかったのに、何もなかったその手のひらの上にオレンジが現れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「わ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "みずみずしく、美味しそうだ。\n
鼻先を爽やかな香りが漂っていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0009
Joker "「タネも仕掛けもありません……、ってね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「へえ、すご……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……ん？）"

hide m_kyoutuu1_12
show m_kyoutuu1_13 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……くないわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "タネも仕掛けもないならば、それは{size=+20}ただの魔法{/size}だ。果物に姿隠しの魔法をかけておき、解除しただけのようにも思える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "高度な魔法になるが、物体を移動させる魔法だってないことはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Joker "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice jok_r0010
Joker "「タネも仕掛けもある……、んじゃないかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「それなら素直にすごい技術、と思えるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "タネのある手品なら、器用だと誉められる。\n
魔法だとすれば、ちっともすごくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0011
Joker "「なんだか……、なんとなく納得がいかない……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……そう？\n
魔法学校なんだから、当たり前でしょ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは、魔法が当たり前の世界。\n
魔法を使って見せたところで感動はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0012
Joker "「そ、そうだよね……。\n
ここ、魔法学校だし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0013
Joker "「……サーカス的な何かは駄目か、やっぱり」"

hide m_kyoutuu1_13
show m_kyoutuu1_14 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカー憮然とした顔をしつつも、ナイフを取りだし（これまた、どこから出したのか分からなかった）、器用にくるくるとその皮をむいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0014
Joker "「はい、半分こ。\n
美味しいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「ありがとう。\n
ちょうど、喉が渇いていたの」"

hide m_kyoutuu1_14
show m_kyoutuu1_15 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "房にわけて、早速口に入れたオレンジは、甘く、美味しかった。\n
もぐもぐとオレンジを堪能する。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「……う～ん。\n
爽やかでいいわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "暖かな庭に、オレンジの香り。\n
さわさわと木々が揺れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "柔らかな時間。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なぜだか、曜日も違うのに日曜日を思い出す。\n
おそらく、ここにいつも一緒にいた人がいないからだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（嫌だわ。\n
ホームシックなんて、子供っぽい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "離れてから、そんなに経っていないのに、家族が懐かしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0015
Joker "「……なあ、[firstname]。\n
君は、ここでの生活を楽しんでいる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔を上げる。\n
ジョーカーは今までと変わらず、にこにこと笑っているものの、その問いに逃げ道はないようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何気ないようで、答えを強制しているような。\n
そんな響きの問い掛けだ。"
$ gakuen_routechoice3b_seen = False
menu:
    "楽しんでいるわ。":
        jump gakuen_routechoice3a
    "……あんまり。":
        jump gakuen_routechoice3b
label gakuen_routechoice3a:
hide m_kyoutuu1_15
show m_kyoutuu1_16a onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「もちろん、楽しんでいるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、はっきりと答えた。\n
最初のうちは、慣れない環境に戸惑いもしたが、最近ではここに馴染めていると自分でも思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "クラスメイト達は親切だし、同寮の友人ともうまくやっている。\n
問題は何もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0016
Joker "「……ふ、そうか、君が楽しんでいるならいいんだ。\n
うんうん、楽しむのはいいことだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカーは満足気だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がここでの学校生活を楽しむことと、彼と。\n
何の関係があるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0017
Joker "「もうしばらくすると、いろいろとイベントもあるから。\n
そっちも楽しみにしていてね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「イベント？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice jok_r0018
Joker "「ああ、学校行事があるんだよ。\n
詳しくは、君の寮の連中にでも聞くといい」"

hide m_kyoutuu1_16a

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカーはそれだけ言うと、ひらひらと手を振って去って行ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（何をしにきたの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それ以前に、何者だったのか。\n
名前しか知ることができなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が学校生活を楽しんでいるかを気に掛けるあたり、学校関係者なのは間違いないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……そろそろ、教室に戻らなくちゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心地いい時間は、長く続かないものだ。"

with dis
$ hi_mes()

scene bg10_sb_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium
if place_of_stay == "Castle":
    jump gakuen_routechoice_castle1
if place_of_stay == "Hatter":
    jump gakuen_routechoice_hatter1
if place_of_stay == "Amuse":
    jump gakuen_routechoice_amuse1
if place_of_stay == "Tower":
    jump gakuen_routechoice_tower1
label gakuen_routechoice3b:
$ gakuen_routechoice3b_seen = True
show m_kyoutuu1_16b onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……あんまり、っていう感じね。\n
悪くはないけど、まだそこまでは」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉を濁す。\n
毎日は充実しているし、少しずつクラスメイトや同寮の友人達とも親しくなれているという実感はある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが……、疲れてもいる。\n
こうして一人になりたいと思ってしまうのは、無意識のうちに人から逃げてしまっている部分があるからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0019
Joker "「……そうか。\n
君を楽しませるのは、骨が折れそうだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽつり、とジョーカーはまるで独り言のように呟いた。\n
言葉の内容とは裏腹に、彼はとても楽しそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やり甲斐がある、というような笑みを含んだ視線を、ちらりと私へと向ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ああ、ごめんなさい。\n
あなたも、学校の関係者でしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカーが何者かは分からないが、こうして学校内にいる、ということは学校の関係者だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が学校生活を楽しんでいるかを気に掛けるあたり、意外と真面目なのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（正直に、本当のことなんて言わなくてもよかったのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口が滑ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "初対面で、正体も知れない相手。\n
しかし、どうも、この男には人の口を割らせるのがうまい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「気を悪くさせたわね。\n
せっかく気にしてくれたのに……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice jok_r0020
Joker "「いいや？\n
構わないよ、正直な感想を聞けなきゃ意味がない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「意味？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice jok_r0021
Joker "「ああ、そう意味だ。\n
ものごとに意味があるっていうのはいいことさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice jok_r0022
Joker "「君がここに馴染めないことにだって、探れば何かの意味がある。\n
まあ、でも、意味なんか、なければないでいいんだけどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（なんだか、こう……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "馬鹿にされているような気になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "腰の仮面が、今にも笑い出しそうだ。\n
何に使うのかは知らないが、ケタケタと笑い声が聞こえるような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jok_r0023
Joker "「もうしばらくすると、いろいろイベントもある。\n
それなら君も、きっと楽しめるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「イベント？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice jok_r0018
Joker "「ああ、学校行事があるんだよ。\n
詳しくは、君の寮の連中にでも聞くといい」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice jok_r0024
Joker "「それをきっかけに、馴染めるといいね。\n
意味があるかどうかはともかく、楽しくないよりは楽しいほうがいい」"

hide m_kyoutuu1_16b

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ジョーカーはそれだけ言うと、ひらひらと手を振って去って行ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（何をしにきたの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それ以前に、何者だったのか。\n
名前しか知ることができなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が学校生活を楽しんでいるかを気に掛けるあたり、学校関係者なのは間違いないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……そろそろ、教室に戻らなくちゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心地いい時間は、長く続かないものだ。"

with dis
$ hi_mes()

scene bg10_sb_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium
if place_of_stay == "Castle":
    jump gakuen_routechoice_castle1
if place_of_stay == "Hatter":
    jump gakuen_routechoice_hatter1
if place_of_stay == "Amuse":
    jump gakuen_routechoice_amuse1
if place_of_stay == "Tower":
    jump gakuen_routechoice_tower1
label gakuen_routechoice_castle1:

play music gallery_front_day_p_wam

scene bg_par15_rg_ros_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業が終わって、赤薔薇寮に戻った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夕食の時間まで、もう少しある。\n
それまで何をして時間を潰そうか。"


play music corridor_day_p_wam

scene bg25_rr_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（そういえば……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校舎のほうは、時間を見つけては探索していたのである程度地理にも詳しくなっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、寮に関してはまだ必要最低限の場所しか知らないような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の部屋と、カフェテリアと、談話室と。\n
それぐらいしか知らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……身近なのに、意外と知らないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "話によると、男女共同区域のほうにはもっといろいろな施設があるとも聞いたような……。"

with dis
$ hi_mes()

scene bg25_rr_day_s
with stripe_l_medium

scene bg01_cr_day_s
with stripe_l_medium

play music classroom_day_p_wam

scene bg01_cr_day
with stripe_l_long

show boy_a2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice suz_g0119
Seito "「探していた本が図書館で貸し出し中でさ～。\n
課題明日までなんだけど、どうしたもんか……」"

hide boy_a2_5
show boy_a2_5 at left
with dis

show girl_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice may_g0083
Seito "「駄目元で、書庫に行ってみたら？\n
卒業した上級生達が、寄贈していった本が残っているみたいよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え？\n
寮に書庫なんてあるの？」"

jump gakuen_routechoice4
label gakuen_routechoice_hatter1:

play music gallery_front_day_p_wam

scene bg_par15_rg_hat_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業が終わって、帽子屋寮に戻った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夕食の時間まで、もう少しある。\n
それまで何をして時間を潰そうか。"


play music corridor_day_p_wam

scene bg25_rr_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（そういえば……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校舎のほうは、時間を見つけては探索していたのである程度地理にも詳しくなっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、寮に関してはまだ必要最低限の場所しか知らないような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の部屋と、カフェテリアと、談話室と。\n
それぐらいしか知らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……身近なのに、意外と知らないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "話によると、男女共同区域のほうにはもっといろいろな施設があるとも聞いたような……。"

with dis
$ hi_mes()

scene bg25_rr_day_s
with stripe_l_medium

scene bg01_cr_day_s
with stripe_l_medium

play music classroom_day_p_wam

scene bg01_cr_day
with stripe_l_long
hide boy_a2_5
show boy_a2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice suz_g0119
Seito "「探していた本が図書館で貸し出し中でさ～。\n
課題明日までなんだけど、どうしたもんか……」"

hide boy_a2_5
show boy_a2_5 at left
with dis
hide girl_a1_3
show girl_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice may_g0083
Seito "「駄目元で、書庫に行ってみたら？\n
卒業した上級生達が、寄贈していった本が残っているみたいよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え？\n
寮に書庫なんてあるの？」"

jump gakuen_routechoice4
label gakuen_routechoice_amuse1:

play music gallery_front_day_p_wam

scene bg_par15_rg_amu_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業が終わって、遊園地寮に戻った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夕食の時間まで、後少しある。\n
それまで何をして時間を潰そうか。"


play music corridor_day_p_wam

scene bg25_rr_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（そういえば……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校舎のほうは、時間を見つけては探索していたのである程度地理にも詳しくなっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、寮に関してはまだ必要最低限の場所しか知らないような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の部屋と、カフェテリアと、談話室と。\n
それぐらいしか知らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……身近なのに、意外と知らないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "話によると、男女共同区域のほうにはもっといろいろな施設があるとも聞いたような……。"

with dis
$ hi_mes()

scene bg25_rr_day_s
with stripe_l_medium

scene bg01_cr_day_s
with stripe_l_medium

play music classroom_day_p_wam

scene bg01_cr_day
with stripe_l_long
hide boy_a2_5
show boy_a2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice suz_g0119
Seito "「探していた本が図書館で貸し出し中でさ～。\n
課題明日までなんだけど、どうしたもんか……」"

hide boy_a2_5
show boy_a2_5 at left
with dis
hide girl_a1_3
show girl_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice may_g0083
Seito "「駄目元で、書庫に行ってみたら？\n
卒業した上級生達が、寄贈していった本が残っているみたいよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え？\n
寮に書庫なんてあるの？」"

jump gakuen_routechoice4
label gakuen_routechoice_tower1:

play music gallery_front_day_p_wam

scene bg_par15_rg_tow_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業が終わって、塔に戻った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夕食の時間まで、後少しある。\n
それまで何をして時間を潰そうか。"


play music corridor_day_p_wam

scene bg25_rr_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（そういえば……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校舎のほうは、時間を見つけては探索していたのである程度地理にも詳しくなっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、寮として住んでいるはずの塔はまだ必要最低限の場所しか知らないような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の部屋と、カフェテリアと、談話室と。\n
それぐらいしか知らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……身近なのに、意外と知らないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "話によると、男女共同区域のほうにはもっといろいろな施設があるとも聞いたような……。"

with dis
$ hi_mes()

scene bg25_rr_day_s
with stripe_l_medium

scene bg01_cr_day_s
with stripe_l_medium

play music classroom_day_p_wam

scene bg01_cr_day
with stripe_l_long
hide boy_a2_5
show boy_a2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice suz_g0119
Seito "「探していた本が図書館で貸し出し中でさ～。\n
課題明日までなんだけど、どうしたもんか……」"

hide boy_a2_5
show boy_a2_5 at left
with dis
hide girl_a1_3
show girl_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice may_g0083
Seito "「駄目元で、書庫に行ってみたら？\n
卒業した上級生達が、寄贈していった本が残っているみたいよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え？\n
塔の中に書庫なんてあるの？」"

jump gakuen_routechoice4
label gakuen_routechoice4:
hide girl_a1_3
show girl_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice may_g0084
Seito "「あら、あなた知らなかったの？\n
でも、まあ、図書館みたいな立派な施設ではないわよ」"

hide girl_a1_2
show girl_a1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice may_g0085
Seito "「知らなくて支障もないほどの……」"

hide boy_a2_5
show boy_a1_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice suz_g0120
Seito "「……物置みたいな感じだよな？」"

hide girl_a1_8
show girl_a1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice may_g0086
Seito "「そうねえ……。\n
本の類にしても、寄贈、といえば響きはいいんだけど……」"

hide girl_a1_1
show girl_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice may_g0087
Seito "「要らなくなったものを置いて行っちゃった、という感じね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「なんだ。\n
不用品の山なのね」"

hide girl_a1_3
show girl_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice may_g0088
Seito "「そういうわけでもないのよ。\n
卒業生が学業で使ったり、生活で必要だったものが大体揃っているから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「！\n
じゃあ、不用品どころか、すごく便利……」"

hide girl_a1_2
show girl_a1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice may_g0089
Seito "「そう……なんだけど、そううまくもいかないの」"

hide boy_a1_8

hide girl_a1_1
show girl_a1_1 at left
with dis

show boy_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice oni_g0085
Seito "「あそこなら、シンフォニアの学園生活で必要になるものの大体はあるような気がするけど……。\n
まず、発掘するまでに力尽きてしまう」"

hide girl_a1_1

hide boy_b1_1
show boy_b1_1 at left
with dis

show boy_a1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice suz_g0121
Seito "「よっぽど切羽詰ってでもいないと、探してみようって気にはならないよ。\n
……今の俺みたいに、危機的な状況でもない限り」"

hide boy_b1_1

hide boy_a1_8
show boy_a1_8 at left
with dis

show girl_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice tak_g0159
Seito "「ねえ、[firstname]、あなたもしかして……。\n
書庫の他にも、共用施設のこと知らないんじゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「え？\n
カフェテリアは知っているわよ？」"

hide girl_b1_8
show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice tak_g0160
Seito "「だめだめ、カフェテリアなんて基本中の基本よ？\n
書庫もそうだけれども、軽い運動のできる運動室だってあるんだから」"

hide boy_a1_8

hide girl_b1_2
show girl_b1_2 at left
with dis

show boy_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice oni_g0086
Seito "「そうだなあ。\n
運動室とは別に、レクリエーション室もあるし……」"


show boy_a2_5 at center
with dis
hide girl_b1_2

hide boy_b1_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice suz_g0122
Seito "「……調理室もある。\n
夜食にぴったりで、よく使うんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「ああ、調理室なら私もたまに使わせてもらっているわ。\n
使い勝手いいわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「夜食には使っていないけど。\n
……太るわよ？」"

hide boy_a2_5
show boy_a2_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice suz_g0123
Seito "「はあ。\n
早く、カロリーダウンの魔法を会得したいよ……」"

hide boy_a2_4
show boy_a2_4 at left
with dis

show girl_a1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice may_g0090
Seito "「ふふ。\n
どこまで本当か分からないけど、噂によると秘密の部屋もあるらしいわよね？」"

hide boy_a2_4
show boy_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice suz_g0124
Seito "「ああ、その噂なら俺も聞いたことある！\n
選ばれし者しか入ることが出来ないんだろ？」"

hide boy_a2_5

hide girl_a1_3
show boy_a2_5 at left
with dis

show boy_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice oni_g0087
Seito "「なんだか、伝説ものみたいだなあ……。\n
勇者しか入れない……みたいな」"

hide boy_a2_5

hide boy_b1_5
show boy_b1_5 at left
with dis

show girl_a2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice may_g0091
Seito "「でも、私もそう聞いたわ」"



hide boy_b1_5
show girl_a2_5 at left
with dis
hide girl_a2_5
show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice tak_g0161
Seito "「あら？そうなの？\n
私は、そこに迷い込むと出られなくなるって聞いたわよ」"

hide girl_a2_5

hide girl_b1_2
show girl_b1_2 at left
with dis

show boy_a2_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice suz_g0125
Seito "「えええ？\n
一気にホラー！？」"

hide girl_b1_2

hide boy_a2_4
show boy_a2_4 at left
with dis

show boy_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_14")
voice oni_g0088
Seito "「でも、俺はそこにシンフォニアの秘宝がある、って聞いたぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「色んな噂があるのねえ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（どこまでが本当で、どこからがデマなのかしら）"

with dis
$ hi_mes()
hide boy_a2_4

hide boy_b1_3


scene bg01_cr_day_s
with stripe_l_medium

scene bg25_rr_day_s
with stripe_l_medium

play music corridor_day_p_wam

scene bg25_rr_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "秘密の部屋はともかくとして、寮の共用区域にはいろいろと面白そうな施設があるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（散策してみようかな）"

label gakuen_routechoice_skip:
with dis
$ hi_mes()
if place_of_stay == "Castle":
    jump gakuen_routechoice_castle2
if place_of_stay == "Hatter":
    jump gakuen_routechoice_hatter2
if place_of_stay == "Amuse":
    jump gakuen_routechoice_amuse2
if place_of_stay == "Tower":
    jump gakuen_routechoice_tower2
label gakuen_routechoice_castle2:
show screen castle_man_choice
$ ui.interact
label gakuen_routechoice_hatter2:
show screen hatter_man_choice
$ ui.interact
label gakuen_routechoice_amuse2:
show screen amuse_man_choice
$ ui.interact
label gakuen_routechoice_tower2:
if renpy.seen_label("gakuen_a") == True:
    jump gakuen_routechoice_tower3
jump gakuen_routechoice_tower4
label gakuen_routechoice_tower3:
if gakuen_routechoice3b_seen == True:
    jump gakuen_routechoice_tower5
jump gakuen_routechoice_tower4
label gakuen_routechoice_tower4:
show screen tower_man_choice
$ ui.interact
label gakuen_routechoice_tower5:
$ extra_joker = True
show screen tower_man_choice
$ ui.interact
