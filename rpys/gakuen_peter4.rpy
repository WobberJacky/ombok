label gakuen_peter4:
scene bg_map_nig
with dis
$ clockanim()

jump gakuen_storm_pet_ace
label gakuen_peter4_2:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（そういうことなら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その証拠品を持ち帰ることが出来なければ、イベント失敗としてゲームの敗者になってしまうのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと見やれば、他にも同じような光景が。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "新入生だと思われる男の子達が、ぎこちなくも懸命に廊下を歩く女生徒達へと声を掛けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「いいわよ。\n
それじゃあ、私もあなたに何か渡せばいいのね？」"


show boy_b2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_8")
voice chi_g0010
Seito "「あ、いえ、それは大丈夫なんです。\n
私物を渡してほしいわけじゃなくて……」"

hide boy_b2_5
show boy_b2_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_8")
voice chi_g0011
Seito "「俺、迷子になっちゃってて……、道を教えてほしいんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「あ、なんだ。\n
お目当ての場所があるのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_4")
T "（……っていうか、お目当ての子が）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「好きな子？」"

hide boy_b2_1
show boy_b1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice chi_g0012
Seito "「～～～っ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分かりやすく、その男の子の顔が真っ赤になった。"

hide boy_b1_4
show boy_b1_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0013
Seito "「他の奴が行く前に、早くその子の部屋に行きたいんです。\n
でも、なんだか焦っちゃって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恥ずかしさのせいか、視線は私から逸らしたまま、彼は早口にぽそぽそと事情を教えてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰か好きな子がいて、その子の部屋に行きたいけれども慣れない女子寮の中で迷子になってしまったのだそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋にはそれぞれ番号が振られてはいるものの、次の数字が廊下を跨いでしまうと、慣れないうちはどこに次の部屋がくるのか判断が難しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（これは応援してあげたくなっちゃうなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「いいわ、教えてあげる。\n
彼女の部屋番号を教えてくれるかしら？」"

hide boy_b1_6
show boy_b1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice chi_g0014
Seito "「あ、ありがとうございます……！！！\n
彼女の部屋は……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の口にした部屋番号でだいたいの位置の見当をつける。\n
おそらく当たっているはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「それじゃあ、ついてきてちょうだい」"

hide boy_b1_2
show boy_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice chi_g0015
Seito "「はいっ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かしこまった彼の返事が、なんだか可愛い。\n
同じ新入生ながら、やはり私のほうが年上だからだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（恋をしていると、男の子も可愛くなるんだな……）"

play sound se_0774
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを思いながら、私は彼を案内して歩き始めた。"

hide boy_b1_3
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()


$ time_effect()##PLEASE MANUALLY ADJUST ME

play music corridor_nig_p_wam
##[rchara1 PAY ATTENTION="false"]
show boy_b2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice chi_g0016
Seito "「ありがとうございました！\n
あなたも、よいストームを過ごしてくださいね！」"

hide boy_b2_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言って手を振ってくれた彼に見送られて、私は自室に戻るべく歩き始める。"

play sound se_0774
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（よいストームをっていうのも、なんだかおかしいけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_10")
T "（ふふ、なんだかいい気分）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ささやかながら、いいことをした気がする。恋のキューピットを気取るつもりはないが、それでも彼のストームがうまくいけばいいと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人やメイドに見つからないように潜入するというルールのせいか、表立って派手なことにはなっていないものの……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも寮の中の空気はどこも華やいでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳をすませば聞こえる声。\n
そのどれもが楽しげだ。"

play sound se_0559

show boy_c2_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0012
Seito "「お、おまえ行けよ……っ！」"

hide boy_c2_1
show boy_c2_1 at left
with dis

show boy_d1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0009
Seito "「えええっ！？\n
おまえが行ってこいよ……っ！」"

hide boy_c2_1
show boy_c2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice suz_g0013
Seito "「でも、戦利品を貰わないと……っ！」"

hide boy_d1_5
show boy_d2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hos_g0010
Seito "「だから、俺じゃなくておまえでもいいだろ！？\n
行ってこいよ……っ！」"

hide boy_c2_4

hide boy_d2_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下の陰で、互いに押し合う男子生徒。"


show girl_c1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0007
Seito "「……私のところにも、誰か来るかなあ。\n
誰も来なかったら来なかったで嫌よね……」"

hide girl_c1_1
show girl_c1_1 at left
with dis

show girl_d2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0008
Seito "「それはつまり、高嶺の花だったってことかもよ。\n
ポジティブにいきましょうよ、ポジティブに」"

play sound se_0559
hide girl_c1_1

hide girl_d2_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の前で、こそこそとそんな会話を交わして励ましあう女子生徒。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（私のところにも、誰か来るのかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう考えて、すぐさま頭に浮かんだのはボリスやピアスといったクラスメイトの男の子達だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、そのほとんどが遊園地寮だということに思い当たる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あくまで、これは寮内のイベントらしい。\n
さすがに、寮を跨いで遊びに来るようなことはないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "となると、赤薔薇寮にいる誰かになるわけだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（知り合いの同寮生といえば……）"

menu:
    "ペーターだわ。":
        jump gakuen_peter4_3a
    "エースかしら。" :
        jump gakuen_peter4_3b
label gakuen_peter4_3a:
$ lovechara_peter_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（うん、ペーターに決まっている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなイベントを、ペーターが逃すわけがない。\n
放課後のお茶会でも、僕にすべてを委ねて云々と言っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……ペーターったら。\n
最初から、教えてくれていたらよかったのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "新入生には内緒と言っていたので、サプライズまでを含めてが、イベントの主旨なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分かっていても、つい文句が零れてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは相手がペーターだから、だ。\n
幼馴染の気安さで、少々理不尽な文句だって言える。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ペーターは、基本的に私が本気で嫌がるようなことはしないし……。\n
他の誰かが来るよりは、緊張しないですみそうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "常日頃ストーカー活動に余念のないペーターだが、私が本気で嫌がるようなことはしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり賢いと自称するだけはあるのか、その境界は見誤らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（なんだか、ちっちゃい頃を思い出すな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幼馴染だし、昔はよく互いの家で泊まりっこをしたものだ。\n
懐かしくて、わくわくとする。"

jump gakuen_peter4_4
label gakuen_peter4_3b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……エース、かしら？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディに命じられて、今夜のために赤薔薇寮に引き留められているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、そのビバルディは、どうやらこのイベントにおいて私のために何かをしようとしているというような口ぶりだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのビバルディの意図に沿ってエースが動くとしたならば……。\n
彼が、私の部屋にくる可能性が高い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（あれね……、いわゆる八百長）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がちゃんとこのイベントを楽しめるように、きっとビバルディが気をきかせてくれたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースはトラブルメーカーでインパクトも強いが、実のところ、たいして知らない人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼とまともに二人きりで話すのは、今回が初めてになるかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……ちょっとは、人となりが分かるかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう考えると、これはこれでいい機会なのかもしれない。\n
知人と親しくなるチャンスだと思えば、わくわくと楽しみになってきた。"

jump gakuen_peter4_4
label gakuen_peter4_4:
play sound se_0451
pause 1
play sound se_0285

play music room2_p_wam

scene bg24_rj_nig_lon with stripe_l
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自室につくと、私は鍵を開けて足を踏み入れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら私が外にいる間に誰か来たのでは。\n
そんな可能性についても考えていたが、どうやらそういうことはなかったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が出たときと、まったく同じ状態のまま。\n
部屋は静かだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……覚悟を決めて、待つとしよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントだと分かっているのに、周囲の華やかな空気に乗せられてしまっているのか、心拍数が早くなっているのが自分でも分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "入浴時、他の子達の会話を思い出す。\n
彼女達同様、浮かれている自分が気恥ずかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……なんてことないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（緊張することはないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、何かを期待しているような自分がいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "プレゼントを開ける前のうきうき感。\n
驚くような楽しいことが起こるかもしれない、と。"

with dis
$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME
play music secret_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（誰かも言っていたけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "（これは、これでへこむわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどまでの甘酸っぱい緊張感はすでにない。\n
私はぐったりと弛緩してベッドに横たわっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ、{size=+20}誰も来ない{/size}。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "緊張した分、脱力感も大きい。\n
周囲からは賑やかな声や気配が漏れ聞こえているというのに、私の部屋の中だけは静かだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（私って、実はものすごく寂しい子だったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "理由をつけるとしたら、クラスメイトに遊園地寮の生徒が多いこと、だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋で誰かを待ったりなどせず、カフェテリアや、ビバルディ、もしくは他の誰か、友人の部屋へと遊びに行ってしまえばよかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今から移動してもいいのだろうが、なんだかすっかり乗り遅れてしまった感がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……ふう」"

play sound se_0063
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "溜息をついて体を起こした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかくの公認イベントなのだから、楽しまなければ損というものだ。\n
何かしら、行動は起こすべきだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……待っていても、誰も来ないのだから。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（適当に、どこかに行ってみようかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして部屋にこもっているよりも、よっぽど面白いことに出会えるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、なかなか扉から外に出ようという気になれないのは、もし誰かが来たら……なんて、今でもまだどこか期待してしまっているからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せめて外の様子だけでも伺ってみようと、窓を開けてみた。"

play sound se_0165
pause 1
play sound se_0585

scene bg06_sk_h_nig
with dis
play sound se_0523
$ flash(.1)
$ flash(.1)
play sound se_0412
$ flash(.2)
$ flash(.1)
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……！？」"


play music battle_a_wam
play sound se_0683
$ flash(.1)
$ flash(.2)
play sound se_0125
pause .3
play sound se_0191
$ flash(.1)
pause .2
play sound se_0020
$ flash(.1)
play sound se_0020
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓を開けた先は、戦場だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

play sound se_0587

scene bg24_rj_nig_lon with stripe_l
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前に広がる光景が理解しがたくて、ばたりと窓を閉めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（な……、なんで……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「なんで、中庭でペーターとエースが戦っているの……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲から賑やかな気配が伝わってくるわけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓ガラス一枚隔てたところで、あんな乱闘が行われていたのならば、そりゃあ賑やかにもなるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……？）"

play sound se_0792 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓を閉めただけで、急に外の物音が遠くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓に対して、何か特別な魔法で強化した覚えはない。\n
寮の施設に、予めそういう強化が施されているという話も聞いたことがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、ただの防音にしては手が込みすぎている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ガヤのような人の声は聞こえていたのに、彼らの戦闘音だけが綺麗にシャットアウトされていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「どうなっているの……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう一度、窓を開けてみる。"

play sound se_0585

scene bg06_sk_h_nig
with dis
play sound se_0020
pause .3
play sound se_0020
pause .5
play sound se_0726 volume .7
pause 1
$ flash(.3)
play sound se_0369
play sound se_0728 volume .7
camera at hpunch
camera at vpunch
$ flash_color("light_red",.2)
$ flash_color("dark_orange",2)
$ flash_color("light_orange",.2)
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賑やかな喧騒が飛び込んできた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……防音の魔法がかけられていたの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらくはそうなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも、すこぶる高度な魔法だ。\n
音を選別している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことをするのは、騒音の原因たる二人のうちのどちらか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これだけ騒いでいれば、使用人達も気付いていないわけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ストームとは関係ない騒動とみなしているのか、それともいつものことだと思っているのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠巻きに何人かがちらちらと見ている程度だ。"


scene bg20_gd_nig
with dis

show ace_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0041
Ace "「あ、やっと気付いてくれたんだー？\n
君、結構のんきだねー！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓際の私の姿に気付いたらしい。\n
剣を片手に、エースがこちらに向かって大きく手を振って見せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……聞こえなかったのよ！」"

hide ace_m_02_4
show ace_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice ace_g0042
Ace "「ははあ。\n
ペーターさんってば、そんな小細工までしていたのか、はは、卑怯だなあ」"

hide ace_m_03_11
show ace_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice ace_g0043
Ace "「でも、俺、前にも言ったけど、小賢しい人って嫌いじゃないぜ？\n
ずる賢い子も嫌いじゃないけど……」"

hide ace_m_01_10
show ace_m_01_10 at left
with dis

show per_m_01_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice pet_g0127
Peter "「うるさいですよっ！！\n
さっさと死んでください！！！」"

play sound se_0020
pause .3
play sound se_0020
pause .3
play sound se_0020
hide ace_m_01_10
show ace_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice ace_g0044
Ace "「おっと、危ない危ない。\n
ペーターさん、怒りっぽすぎると早死にするよ？」"

hide ace_m_01_3
show ace_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice ace_g0045
Ace "「カルシウムが足りてないんじゃないかなあ。\n
俺、心配だよ」"

hide per_m_01_1
show per_m_01_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice pet_g0128
Peter "「君に心配されるいわれはありません！！！！」"

hide ace_m_03_7
show ace_m_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice ace_g0046
Ace "「何言っているんだよ、ペーターさん。\n
俺達、友達だろ？」"

play sound se_0198
##special anime"kirakira_left"loop="false"time="1000"]
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きらっと星でも飛びそうな勢いで、エースが爽やかに笑って見せた。\n
……薄ら寒い。"

hide ace_m_01_4
show ace_m_01_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0047
Ace "「友達なら、思いやりを持たなきゃ。\n
友情を長続きさせるには……」"

hide per_m_01_7
show per_m_02_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0129
Peter "「続く以前に、始まっていません！」"

hide ace_m_01_10
show ace_m_03_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0048
Ace "「はは。君と彼女の関係みたいに？\n
それは深刻だなあ」"

hide per_m_02_11
show per_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0130
Peter "「ああ、彼女を引き合いに出すとは！\n
君と彼女が比べられるとでも！？」"

hide per_m_01_5
show per_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0131
Peter "「あなたと友達になるぐらいなら、僕は死んだほうがマシです！でも僕は彼女を残して死ぬわけにはいかないので、エース君、君が死んでください！」"

play sound se_0020
pause .3
play sound se_0020
pause .5
play sound se_0457
pause 1
play sound se_0369
$ flash_color("red", .2)
$ flash_color("orange_3", .2)
$ flash_color("orange", .2)
pause 1
hide ace_m_03_11
show ace_m_02_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0049
Ace "「はははっ、ヒステリーはよくないぜ！\n
[firstname]、君もそう思うだろ？」"

hide ace_m_02_1
show ace_m_03_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0050
Ace "「校内には、怒りっぽい動物ばかりで困るよなあ」"

play sound se_0439
##special anime"kiseki03"loop="false"time="1000"]
pause .5
play sound se_0193
play sound se_0581
show white onlayer master ##instant]
hide white with spread_short
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターの魔法媒体である銃が、パンと乾いた音をたてるたびに、なんらかの魔法攻撃がエースに向かって発動している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを避けたり、斬り捨てたりとエースも負けていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "数々の魔法を引き金を引くだけの動作で発動させるペーターもすごいが、放たれる魔法を片っ端から避けたり、切り捨てているエースもすごい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……優秀なのよね、この二人って）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは、刀身を振り回すと同時に地面を蹴ってふわりと浮かび上がった。"

play sound se_0441
pause .1
play sound se_0496

play music looking_for_a_ali
show m_per4_1 onlayer master
with dis
hide ace_m_03_10

hide per_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼にとっての魔法媒体はその剣なので、空中浮遊の魔法を発動させたのだろう。\n
空中を駆け上がるようにして、私の窓際までやってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「エース！？\n
あなたがこんなところに来たら、私まで巻き込まれるじゃない……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（流れ弾が……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは、エースに向けて見境なく魔法を乱射している状態なのだ。\n
的が、こんな近距離にいると私まで危ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0051
Ace "「なんだよ、君も友達甲斐がないなあ。\n
せっかくだから、一緒に的になろうぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0052
Ace "「ほら、ペーターさん。\n
気をつけないとこの子に流れ弾が当たっちゃうよ！」"

hide m_per4_1
show m_per4_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0132
Peter "「エース君、君って人は……！\n
彼女を人質にするなんて卑怯ですよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……そうよ。\n
今回ばかりは、全面的にペーターに賛成する」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "爽やかな笑顔はそのままだが、私を人質としているのは明らかだ。\n
中庭へと叩き落としてやりたいが、それが難しいのは分かっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どういう事情かは知らないが、二人はやりあっていて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……で、何がどうしてあんたたちはこんなところでやりあっているのよ。\n
今日は、ストームなんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞いた話と、エースやペーターがやっていることはまるで違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームというのは、男子生徒が使用人達に見つからないようにこっそり女子寮に侵入して、その証拠となるものを持ち帰るというイベントのはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それがどうして、中庭での決闘沙汰になってしまっているのか。\n
私の疑問に、エースはその双眸を細めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもと同じ爽やかな笑みなのに、私には意地悪く見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0053
Ace "「俺はさ、会長の指示で、君を守るために参上したナイトなんだよ。\n
君の部屋に侵入しようとするウサギさんを追い払うための、さ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……そういうことだったのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディの言っていたのはこのことだったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（それで、エースとペーターが中庭で戦闘になっていたのね。\n
……って、あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "納得しかけて、途中で気が付いた。\n
それにしては、位置関係がおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ねぇ、今の話が本当なら、あなたの立つべき場所はそこじゃないんじゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓辺に立った私に、最初に気付いたのはエースだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまり、この窓に向かっていたのはエースで、ペーターはこちらに背を向けていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターが侵入しようとしていて、エースが本人の言うとおりナイトの仕事をしていたというのならば、その位置関係は逆になりそうなものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0054
Ace "「そうなんだよね～。\n
ペーターさんったらさ、君の部屋に近付く連中をこてんぱんにしているだけで自分は近付かないんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0055
Ace "「俺の仕事は取られちゃって、やることもない。\n
でも、せっかく来たのに、そのまま帰るなんて寂しいだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0056
Ace "「だから、仕方なく、逆に回ったってわけ。\n
はは、たまには悪役もいいよな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……あなた、日頃もあんまり善玉じゃないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice ace_g0057
Ace "「え～？俺は、清く正しい、風紀担当だぜ？\n
善玉でないわけがないだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースの中では、風紀担当イコール正義の味方であるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、その主張の張本人であるエースが、日頃果たして風紀委員らしい行動をしているかと言われたら首を傾げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今だって、そうだ。\n
私を人質に取られたことにより、攻撃の手を休めて悔しげにしているペーターを見下す様ははまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターのほうは、片手には魔法媒体である銃をぶらさげ、もう片手はぎゅっと悔しそうに拳を作っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こちらを真っ直ぐに見る双眸は、睨みつけているようにも、今にも泣き出しそうにも見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（こんな場面じゃないけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……どこかで）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなことが、前にもあったような気がする。\n
ペーターにこんな顔をさせてしまったことが、あったような気がする。"

hide m_per4_2
show m_per4_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「エース」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice ace_g0058
Ace "「なんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「ビバルディには悪いけど……、ナイトは必要ないわ。\n
……充分、楽しんだでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice ace_g0059
Ace "「え～～？\n
お役目を果たさないで帰ったら、職務放棄で会長に怒られるのは俺なんだぜ～？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……普段から、お役目なんて投げ出すのが役目だと思っているくせに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「私からもビバルディに言ってあげるから。\n
ね、お願い」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice ace_g0060
Ace "「……ふうん？\n
俺のこと、ちょっとは理解してくれているみたいだね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice ace_g0061
Ace "「ちぇ、仕方ないなあ。\n
友達の言うことなら、上司よりも優先して聞かないと俺の騎士道に反する」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice ace_g0062
Ace "「引くのは癪だけど……。\n
ま、ペーターさんにはたっぷり遊んでもらったし、それでよしとするか……」"

play sound se_0216
pause .4
play sound se_0348
hide m_per4_3
show black onlayer master with grad_b_short

scene bg06_sk_h_nig ##instant]
hide black
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースはそう言うと、たんっと女子寮の壁を蹴って身を翻した。\n
翻ったマントに一度視界を奪われる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視界が戻ったとき。\n
ペーターが、怪訝そうな顔をしながらも、追撃するつもりなのか銃を再び構えていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「ペーター！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
Peter "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名を呼べば、ぴくっと跳ねるように顔が上がってこちらを見上げる。\n
ちょいと手を振って、手招きをした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その間にエースはゆっくりと地上へと降り立つと、そのまま悠々と立ち去っていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……うん。\n
正義の味方には見えないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ダークヒーローか、もしくは怪盗がいいところ。\n
一番はまりそうなのは、どちらにしろ悪役だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは、エースを追撃するべきか私の元へくるべきかを迷うように視線を揺らした。"

play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逡巡後、ぴょんと踏み切って宙に舞うと、こちらへとやってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「……[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怒られるとでも思っているのか、その耳はしょんぼりと垂れ下がっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……入ったら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pet_g0133
Peter "「……はい」"


scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりと、ペーターは窓から入ってくる。\n
確認して、私は窓を閉めた。"

play sound se_0587
pause 1
play sound se_0165

play music flower_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ついでにカーテンも閉めてしまえば、外からは見えない。"


show per_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは、落ち着かなさそうに、視線をゆらゆらと揺らしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……私の部屋に来ようとする人を、追い払っていたの？」"

hide per_m_01_13
show per_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pet_g0134
Peter "「……はい。\n
だって、[firstname]、こんなイベントに乗じてあなたの部屋に行くなんて、不埒な輩です……！」"

menu:
    "でもイベントだから楽しみにしていた。":
        jump gakuen_peter4_5a
    "……それもそうね。":
        jump gakuen_peter4_5b
label gakuen_peter4_5a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「でも、せっかくのイベントなのよ？\n
……私だって楽しみにしていたのに」"

jump gakuen_peter4_6
label gakuen_peter4_5b:
$ lovechara_peter_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「そうね、きっと私だって驚いたわ。\n
男の子が突然部屋に来れば……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……案内するのは平気だったけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのあたりを説明すると、また揉めそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「でも、それをあなたが判断してしまうなんてずるいわ。\n ・
私にだって、参加する・しないを決める権利があるはずでしょう」"

jump gakuen_peter4_6
label gakuen_peter4_6:
hide per_m_02_7
show per_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怒られた子供のように、ペーターはしょんぼりとして俯いている。\n
ウサギ耳も、へにゃりと力なく垂れていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどまでエース相手に銃を振り回して戦っていた勇ましさはどこにもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……誠実なんだか、馬鹿なんだか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すべてを任せてとか、委ねて、とか。\n
そうして出た結論が、警護とは。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に近付く男を追い払おうとはするくせに、自分がそうしようとは思わない。\n
普段はあんなに好意を押し付けてくるくせに、いざというときには怯んでしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……というか、的外れに純粋なのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（本物の、ウサギみたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふわふわ、真っ白い。\n
夢の世界の、白ウサギ。"

hide per_m_01_13
show per_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0135
Peter "「あなたの楽しみを奪ってしまったというのならば、罰は受けます。\n
ですが、耐えられなかったんですっ！」"

hide per_m_01_8
show per_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0136
Peter "「他の男があなたの部屋に行って、あなたのものを奪っていくなんて……！\n
それに、ブリーズがきたら、あなたはその男の部屋に行ってしまう！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ブリーズ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "またもや、聞きなれない単語が出てきた。\n
こちらもまた、何かのイベントなのだろうか。"

hide per_m_02_7
show per_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0137
Peter "「このストームと対をなすイベントなんです。\n
今度は女子寮の生徒達が、奪われたものを男子寮に取り返しにいく……、という」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（この学校って、対をなすものが多いなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……シンフォニアって、意外とお祭り好きよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あまり聞いたことのないようなイベントが、公認で行われている。\n
内容的には、いかにも寮でのお遊びというようなものなのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その自由度の高さが、ある意味、さすがシンフォニアといえるのかもしれない。"

hide per_m_03_5
show per_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0138
Peter "「僕、嫌なんです。\n
あなたが、他の誰かのところに行ってしまうなんて、耐えられません……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤い双眸を潤ませて、ペーターは切なそうに言う。\n
だが、彼は自分がその「誰か」に立候補しようという考えには至らないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（いつも、こうなのよね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストーカーみたいなことをしでかすくせに、肝心のところでは誠実で純粋。\n
そして、いつものごとく、空回り。"


play music quiet_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……それなら、ペーター」"

hide per_m_02_6
show per_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice pet_g0139
Peter "「なんでしょう。\n
罰を受ける覚悟なら出来ています……！」"

hide per_m_01_8
show per_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice pet_g0140
Peter "「僕は、あなたになら、八つ裂きにされても構わない……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「はあ……。\n
あんたの中じゃ、私は、モンスターか何かなの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鏡台まで歩み寄ると、その上に置かれていたリボンを手にとって彼の元へと戻った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「私はイベントに参加したい。\n
でも、ペーターは私が他の誰かと過ごすのは嫌」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……それなら、あんたが、私のストームに付き合ってよ。\n
それなら、問題ないでしょう？」"

hide per_m_02_11
show per_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0141
Peter "「え！？ぼ、僕がですか……！？\n
ええっ、で、ででで、でも……っ」"

play sound se_0627 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "焦るペーターの声に重ねるようにして、笛の音が外から響いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく、ストーム終了の合図なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は待つことで、ペーターはエースと戦うことで、すっかり時間を無駄にしてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「……ほら、もう終わっちゃうわ。\n
これ、終わりの合図なんでしょう？」"

hide per_m_01_5
show per_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice pet_g0142
Peter "「……はい。\n
寮に戻って、点呼を取らないと」"

hide per_m_02_4
show per_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice pet_g0143
Peter "「会長やエース君が、そういった雑務をやるとは思えませんからね……」"

hide per_m_03_9
show per_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice pet_g0143_5
Peter "「たまにはまともに仕事をしてほしいんですけど、能無しに期待するだけ無駄でしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に叱られると思ってしょげかえっていたのが、ようやく少し調子を取り戻した。\n
それに口元を緩めて笑えば、彼もどこかほっとしたようだ。"

hide per_m_03_10
show per_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0144
Peter "「……怒らないんですか？\n
僕は、あなたの邪魔をしたのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「そうね、わざわざ防音魔法までかけて、私が気付かないようにして、部屋に近付こうとした人を追い払っていたものね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_9")
T "（……絶対に、無関係の人も巻き込まれているわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「……ちなみに、私が普通にドアから誰かを招き入れていたらどうするつもりだったの？」"

hide per_m_03_5
show per_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice pet_g0145
Peter "「窓のついでに、あなたの部屋全体に感知系の魔法をかけておきました。\n
あなた以外が入ったら、すぐに分かります」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「解いてから、帰ってよ？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "筋金入りのストーカーに死角はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「誰も来ないから、寂しかったのよ？\n
友人が少ないのかと思って」"

hide per_m_02_9
show per_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice pet_g0146
Peter "「そんなことありません！\n
あなたは誰よりも魅力的です！」"

hide per_m_01_3
show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice pet_g0147
Peter "「僕が何もしなければ、ストームであなたを訪れる者だって列を成したに決まっていますよ！！\n
僕が保証します！！！」"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅっと、ペーターが私の手を握って力説する。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（来なければ来ないで寂しいけど……、列をなされるっていうのもそれはそれで……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「いや……、私、一人くらいがいいんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "多すぎず、少なすぎず。\n
一人、訪れてくれたら、それでいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、その相手が気心が知れた相手であれば……。\n
……そう、ペーターが来てくれれば、それでよかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……あんたとか」"

hide per_m_02_8
show per_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
Peter "「……？」"

hide per_m_03_5
show per_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
voice pet_g0148
Peter "「……ああ！そうですね！\n
今は僕一人ですから、一人がいいなら、ちょうどですよね！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、ずれている。\n
だが、それすらも居心地いい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……ちょうどいい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "布越しの体温。\n
一生懸命そう主張する姿が、懐かしいのと同時に……、愛しいと思ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恋情なのかどうかも分からない。\n
ただ、私に対してこんなにも一生懸命で真っ直ぐな彼に、愛着は持っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（真っ直ぐがいきすぎて、ストーカーだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、握られた手を引き抜くと、代わりにペーターの手へリボンを持たせてやった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「戦利品が、必要なんでしょう？」"

hide per_m_03_1
show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice pet_g0149
Peter "「ああ、ええ。\n
でも、僕相手に、戦利品の有無を問えるような相手がいるとは思えませんけどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "{size=+20}「じゃあ返してくれる？」{/size} "

hide per_m_02_8
show per_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_2")
voice pet_g0150
Peter "「{size=+20}嫌です！！{/size}\n
あなたのリボンですから！大事にします！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……や、ブリーズには取り返しにいくわよ？」"

hide per_m_01_5
show per_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
Peter "{size=+20}「！！！！！」{/size} "

hide per_m_01_6
show per_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice pet_g0151
Peter "「あ、あなたのリボンをいつまでも持っていたい……。\n
でも僕の部屋にあなたが来てくれるというのは魅力的です……っっ！」"

hide per_m_02_6
show per_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice pet_g0152
Peter "「ああ、僕はどうしたらいいんですか！？\n
悩ましい！非常に悩ましいです、[firstname]！」"

play sound se_0627 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……そうね。\n
とりあえず寮に戻って、点呼を取ったほうがいいと思うわ」"

hide per_m_03_5
show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice pet_g0153
Peter "「そ、そうですねっ！\n
まだブリーズまで時間はあるわけですし……、徹底抗戦するかどうかはじっくり考えてみようと思います！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「先刻、エースとやっていたような一騎打ちを私に期待しないでよ？\n
……ほら、行きなさい」"

hide per_m_02_8
show per_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pet_g0154
Peter "「ええ……。\n
あの、[firstname]、最後に、我侭をいいですか……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に押し出されるようにして、再び窓辺に向かう途中。\n
ペーターが、そっと切り出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「何よ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "また変なことを言い出したら、今度こそ殴ってやろうと拳を固める。"

hide per_m_01_8
show per_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0155
Peter "「あ、あのっ、そのっ。\n
最後に、あなたのこと……っ、抱きしめてもいいですか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……はあ？」"

hide per_m_02_12
show per_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice pet_g0156
Peter "「いえっ、その、あなたがせっかく楽しみにしていたストームを僕が邪魔してしまったので、せめてのお詫びというか……」"

hide per_m_03_11
show per_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice pet_g0157
Peter "「ああ、でも、僕が抱きしめたらお詫びにはなりませんよね！\n
お別れが寂しくて、僕が抱きしめたいだけなんですけど！」"

hide per_m_01_5
show per_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice pet_g0158
Peter "「ああ、賢いウサギのはずなのに何を言っているんでしょうね、僕はっ！\n
すみません、帰ります……！！」"

play sound se_0585
pause .5
play sound se_0492 volume .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早口にそう言って、投身自殺するかの勢いで窓から飛び出しかけた彼の制服の袖を、はしっと捕まえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……何やっているんだろう、私）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームというイベントの持つ空気に酔っ払ってしまっているのかもしれない。\n
ペーターは自分が何を言っているのだろうと言うが、私もおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の袖を捕まえて引き止めているなんて、普段なら有り得ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもならペーターのほうが無理矢理強引に私を抱きしめて、殴られるのが定番の流れ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざわざ抱きしめてもいいかなんて、改めて断りをいれられ。\n
やはりいいと言われて、引き留め。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもと違う。\n
定番の流れになっていない。"

hide per_m_01_13
show per_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0159
Peter "「あ、あの……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……いいわよ」"

hide per_m_03_3
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice pet_g0160
Peter "「えっ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「いいって言っているの！\n
抱きしめなさいよ！」"

hide per_m_02_3
show per_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
voice pet_g0161
Peter "「は、はい！！\n
そ、それでは……」"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「…………」"


play music night_a_wam

show m_per4_4 onlayer master
with dis
hide per_m_01_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそるおそるといった感じだった。\n
躊躇うように、抱きしめられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠慮がちな抱擁。\n
制服の布越しに、遠回りした体温が少しずつ染みてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その熱が、じんっと頬に集まっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……相手はペーターよ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pet_g0162
Peter "「……大好きです。\n
僕が好きなのは、あなただけです」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呪文のように、耳元で囁かれる。\n
その響きは、まるで私に言い聞かせているみたいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かを思い出しそうになった。\n
しかし、記憶の尻尾は捕まえかけた手をするりと抜け出していってしまう。"

play sound se_0627 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……行かないと」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pet_g0163
Peter "「……はい、そうですね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「あなた、副寮長なんだから」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice pet_g0164
Peter "「分かっています」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分かっていると言いながら、ペーターの腕は緩まない。\n
やんわりとした圧で私を抱き続けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、それを強く拒めない。\n
結局、私達は４度目の笛が鳴るまでそうして抱き合ったままだった。"

with dis
$ hi_mes()
hide m_per4_4


$ time_effect()##PLEASE MANUALLY ADJUST ME

play music room2_p_wam

show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0165
Peter "「……それじゃあ、僕は行きますね。\n
ちゃんと戸締りしてから寝てくださいよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「はいはい、分かっているわよ。\n
あんたのほうこそ、気をつけて戻りなさいよ」"

hide per_m_02_8
show per_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0166
Peter "「はい、気をつけます。\n
……では、いい夢を見てくださいね」"

hide per_m_02_12
show per_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pet_g0167
Peter "「それが僕の夢なら、とても嬉しいです。\n
僕は、いつも、あなたの夢を見ますから」"

play sound se_0693
hide per_m_03_4

play sound se_0695 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言って、ペーターは窓辺から飛び降りていった。\n
さあっと吹き込む風にカーテンが揺れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（また、ストーカー発言を……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ただの甘ったるい台詞にも聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "途中魔法を使ったのか、中庭に着地したペーターの背中が闇に溶けるように見えなくなる。\n
私は、しばらくそのまま見送っていた。"

with dis
$ hi_mes()



scene bg24_rj_nig_lon with Dissolve(.8)

scene bg_par15_rg_ros_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_peter5
