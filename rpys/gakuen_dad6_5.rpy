label gakuen_dad6_5:
scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_map_eve
with stripe_l_medium

scene bg_map_nig
with stripe_l_medium

scene bg_par15_rg_hat_nig
with stripe_l_medium

play music room2_p_wam

scene bg24_rj_nig
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やがて日が落ちて、夜がやってくる。\n
そわそわと、落ち着かない空気の中、夕食を終えた私は、自室でじっとそのときを待つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの開始は、それを伝える役目の生徒が各部屋の扉をノックして回ることで知らされるのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "参加する生徒はそれぞれが闇に乗じて中庭を渡ろうと試み、参加する気のない生徒はただその合図を聞き流すだけでいいらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は参加組なので、その合図を待つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（確かなことは……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「私は、あの子達が好き」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口に出して呟くと、より強くその気持ちを感じられる気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人に好意を持っている。\n
そして、それは特別な好意だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どちらか一人を選ぶのではなく、その両方を平等に想う、なんて。\n
どちらも選べないから、両方を、なんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら一時の迷いなのかもしれない。\n
彼らは子供で、私も彼らよりは大人のつもりで、それでも子供だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（子供なら……。\n
馬鹿なことをやってもいい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "失敗したって、構わない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……毒されているなあ）"

play sound se_0300

play music magic_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！」"


scene bg06_sk_h_nig with Dissolve(1.6)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアが鳴った。\n
時間だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いよいよ、ブリーズが始まる。"


scene bg24_rj_nig
with dis
play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姿隠しの呪文を唱える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームは、使用人達との正面衝突こそがメインのイベントになっていたが、ブリーズは違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズは、いかに使用人の目に止まらずに男子寮に到達できるかが課題の、隠密行動がメインとなるイベントなのだそうだが……。"

play sound se_0658

show white onlayer master with Dissolve(.2)

scene bg06_sk_h_nig with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "{size=+20}「！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子寮のあたりから、爆発音が聞こえた。\n
唱えかけの呪文を止めて、窓から身を乗り出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0018
Servant "「なんだ！？\n
男子寮のほうから爆発音あり！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0029
Maid "「至急、確認を！\n
状況によってはブリーズの中止を……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0035
Servant "「いや、事故じゃないみたいだ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0030
Maid "「いや、タイミング的に事故じゃないんだろうけど、生徒のやったことならそれはそれで問題でしょう……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "混乱した使用人達の声が聞こえる。\n
ざわざわ、と女子寮も騒がしくなってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆、合図を聞いて、外に出る準備をしていたに違いない。そのタイミングで起こった騒動に、何が起こっているのかを把握できず、戸惑っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0035
Seito "「なに……？\n
何があったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0145
Seito "「こんな騒ぎが起きるなんて聞いていないわよ？\n
なんなの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "上下左右の窓から、ひそやかな囁き声が聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初はもっと静かだったものの、途中から中庭を走り回る使用人達がこちらの様子を伺うどころではないのに気付き、次第に声の大きさも大胆になっていく。"

play sound se_0507
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（まさか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き覚えのある音が聞こえた。\n
ストームの夜に、聞いた音だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その音を知っているのに、状況とうまく繋げられない。\n
それは私以外のブリーズ参加者の間でも同じだったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽかん、とあっけにとられた間が暫く続き……。\n
その沈黙は、一際早く我に返った誰かの声によって破られた。"

play sound se_0436
$ flash(.1)
play sound se_0683
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0123
Seito "「な……っ！！\n
なんでツインズが戦闘しているの！！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0036
Seito "「え？\n
今はブリーズよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0146
Seito "「ストームじゃないのに……？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "騒ぎが広がっていく。"

play sound se_0414
$ flash(.5)
$ flash(.5)
$ flash(.5)
$ flash(.5)

scene bg20_gd_nig with Dissolve(1.5)

play music fly_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの夜と違い、隠密行動を主にするブリーズだけあって、中庭にはいつもの街灯ぐらいしか灯されてはいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その薄闇の向こう、大斧を振るう二人の姿を見た。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「な……、なんで……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私としても、それしか言えない。\n
イベント主旨と違うのは確実だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0019
Servant "「な、なんだって、ブリーズがストームになっているんだ！？\n
間違いにしたって酷いぞ……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0036
Servant "「間違うわけないだろ！？\n
まったく逆だぞ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0031
Maid "「いいから、今度こそ食い止めないと……！！\n
使用人の意地にかけて……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0020
Servant "「そうやってすぐ戦闘に入ろうとするなよ！？\n
完全にストームになってしまうだろ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0037
Servant "「なんで大人サイズになっていないんだ！？\n
……陽動か！？」"


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中庭で、混乱しながらも統率を取り戻そうと連絡しあう使用人達の声が響く。\n
そしてその中にあった、陽動、との言葉に女子寮がわっと賑やかになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0037
Seito "「……ふ。\n
こうなったらツインズの思惑なんてどうでもいいわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0147
Seito "「そうね……！\n
今のこの隙を逃す手はないわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0124
Seito "「今がチャンスよ！\n
今回は成功率高そう！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0038
Seito "「……賭けてるのよね～」"

play sound se_0405
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓に鈴なりになっていた女生徒たちが皆、思い思いに窓辺から飛び出していくのがシルエットで見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（さすが、帽子屋寮の生徒……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、感心している場合ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「っ、私も行かなくちゃ……！」"


scene bg20_gd_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一息遅れて、私も中庭へと飛び出す。\n
けれど、男子寮を目指せばいい他の皆と違い、私のターゲットたる双子達は何故か使用人達と交戦中だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（ど、どうしたものなの？）"

play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

play sound se_0141
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とりあえず飛行の術を使って、ディーとダムの元へと向かうことにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来飛行の魔法は箒のような魔法媒体を使って安定させるものだが、箒がなくとも使うことは可能だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ、箒を使ったときほどの安定や、速度はない。"

play sound se_0414
$ flash(.5)
$ flash(.5)
$ flash(.5)
$ flash(.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鋭い金属のぶつかりあう音が近くなる。\n
双子達は、使用人相手に苦戦しているようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それもそうだ。\n
前回のように男子生徒多勢対使用人ならともかく、今は男子生徒は双子だけ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、二人は子供の姿のままだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（魔力アップもしていないわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「ディー！\n
ダム……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼ぶ。\n
途端に、二人が斧を大きく振るって使用人達から距離をとり、私を見る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当然その声は使用人達にも聞こえたらしく、そちらからの視線も私へと届く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……しまった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズは隠密行動がルールだ。\n
使用人に見つかって捕まった場合、一度部屋まで強制送還され、もう一度最初からの挑戦になる。"


show siyounin_a1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0021
Servant "「女子生徒は、俺が……！」"

play sound se_0496
hide siyounin_a1_4
show siyounin_a1_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0022
Servant "「…………」"


scene bg06_sk_h_nig with Dissolve(1.6)
hide siyounin_a1_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口早に呪文を唱えて、使用人の一人が芝生を蹴って宙に舞う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……げっ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私を捕まえにきたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（箒、箒……っ！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慌てて箒を取り出して、レース仕様に切り替えようと思うものの、隠密ゲームだからと箒を部屋に置いてきたことに気付いて青ざめる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段なら杖と一緒に、コンパクトにして懐に持ち歩いているのに。\n
後悔しても遅い。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0023
Servant "「捕まえ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慣れの差なのか、使用人のほうは同じ箒なしの飛行魔法だというのに、明らかに私より移動が素早い。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0024
Servant "「た……、っと！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「……わわっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "捕まるわけにはいかない。\n
駄目元で私も、空中で逃げ始める。"


scene bg20_gd_nig
with dis

show dam_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0343
Dam "「早く、こっち！\n
……ちっ、お姉さんに手出しはさせないよ！」"

play sound se_0496
hide dam_m_02_3
show dam_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dam "「…………」"

play sound se_0698

play music battle_ali
show m_twi6_1 onlayer master
with dis
hide dam_m_03_15

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ダムが呪文を唱えて、空に舞う。\n
なんと斧に跨り飛ぶというとんでもないスタイルだ。"

play sound se_0698
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それでも媒体がある分、私より素早く安定した飛行が可能になっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（ああいう使い方も出来るのね）"

play sound se_0338
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice dad_g0344
Dee "「お姉さんを任せたよ、兄弟！！」"

play sound se_0380
$ flash(.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "援護で放ったディーの光弾が、追っ手を怯ませる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0345
Dam "「お姉さん……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「ダム……！！」"

play sound se_0698
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はその隙にとダムの元へと急ぐ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0032
Maid "「合流させちゃ駄目よ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0025
Servant "「分かってる！\n
ツインズの逃げ足の速さは身に染みているとも！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0026
Servant "「あの悪戯っ子ども……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすが帽子屋寮の使用人達、と言うべきだろうか。\n
ツインズ対策をよく分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下から私の移動を邪魔するように放たれる魔法を弾くのに精一杯で、移動がますます減速してしまった。"

hide m_twi6_1

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一方ディーのほうも……。"


show maid_b_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0033
Maid "「今日は、負けませんよ……！\n
捕まえて、寮掃除をしてもらいますからね……！！」"

play sound se_0403
play sound se_0048
hide maid_b_9
show maid_b_9 at left
with dis

show dee_m_03_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0346
Dee "「子供相手にムキになるなんてよくないよ！」"

play sound se_0436
$ flash(.3)
play sound se_0437
$ flash(.5)
hide maid_b_9

hide dee_m_03_8
show dee_m_03_8 at left
with dis

show siyounin_a1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0038
Servant "「……たまに子供じゃないくせに、よく言うよ」"

play sound se_0581
play sound se_0543
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "激しい打ち合いが続いている。\n
こうなると、ディーも私達の援護に徹するだけの余裕はないだろう。"

hide dee_m_03_8

hide siyounin_a1_7


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0027
Servant "「ほらほら、一回部屋に戻って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の背後に、使用人が迫る。\n
その腕が、せめて上空にと逃れた私の足を掠めた。"

play sound se_0041
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ダムも懸命に私のほうへと辿りつこうとしているのだが、使用人の妨害にあってなかなか思うように近づくことが出来ないでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下手に私に近づくと、二人まとめて捕まる事態にもなりかねない。\n
私が上にと逃げてしまったせいもあり、上下に距離があいてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（こうなったら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「ダム……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はダムを呼ぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0348
Dam "「お姉さん！？\n
後少しだから……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0028
Servant "「そうはさせる……っっか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、そのまま上空で、魔法を解いた。\n
これまでふわふわと浮いていた私の体が、急速に重力に捕縛される。"

play sound se_0765
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、そんな私の真下には今にも私を捕らえかけていた使用人がいて……。"

play sound se_0107
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0029
Servant "{size=+20}「ぐぎゃっ！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は私の変則的なドロップキックをまともに受けることになる。\n
ひゅるるるるっと、体勢を崩して地面へと落ちていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……下は芝生なので、それほどダメージはないだろう、と無責任なことを考える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん私だってそれで無事ですむわけがなく、バランスを崩して空中へと投げ出された。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "地面に落ちるまでに、魔法をもう一度唱えなおして、バランスを取り戻せるかといったら厳しい。\n
だが、不安はなかった。"

play sound se_0765
play sound se_0348

show m_twi6_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0349
Dam "「っ！」"

play sound se_0698
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "落下しきるより先にダムが滑り込んで、私の体を受け止めてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice dad_g0350
Dam "「お、お姉さん心臓に悪いよ……！\n
そういう無茶は、子供に任せておいてよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「知らなかったの？\n
私だって……、まだまだ子供なのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅう、と私の体を抱きしめて慌てた様子のダム。\n
言い返す声が、掠れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（私だって怖かったわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "喉がカラカラだ。\n
あんな曲芸みたいな真似、勢いがなければ出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キャッチしてくれるという確信があったからこそ、無茶も出来た。"


scene bg20_gd_nig
with dis

show dee_m_02_3 at center
with dis
hide m_twi6_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0351
Dee "「そこ！一段落ついたみたいにしてるけど……！\n
ずるいよ兄弟！」"

hide dee_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dam "「……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下から響いたディーの声に、私達は我に返る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つい、もう逃げ切ったと思ってしまったが、まだ全然逃げ切れてはいない。\n
合流できたというだけだ。"


show m_twi6_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0352
Dam "「どうする、お姉さん？\n
僕と二人で逃げちゃう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、不可能ではないだろう。\n
ディーをおとりにすれば、逃げ切れる確率も上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0353
Dee "「！\n
抜け駆けはよくないよ、兄弟！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0354
Dam "「ふふ、それも運命だよ、兄弟！\n
……どうする？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ダムが、にっこりと笑って私へと選択権を渡す。\n
赤い瞳が私を見る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見透かされるように感じるのは、私にも思い当たる節があるからだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_1")
T "「……もちろん、助けにいくわよ。\n
三人一緒じゃなきゃ嫌だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_1")
voice dad_g0355
Dam "「……ふふ、そうだね。\n
抜け駆けもそれはそれでありだけど、兄弟を見捨てちゃ目覚めも悪い」"


scene bg06_sk_h_nig with Dissolve(1.6)
hide m_twi6_3
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_1")
voice dad_g0356
Dam "「しっかり掴まっててね、お姉さん！」"

play sound se_0141
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ダムは、体勢を整え出す。\n
私も彼の腕の中から抜け出して、斧の後部へと移動した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中にしっかりと腕を回して掴まる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段はくっつかれることが多いせいで、あまり意識したことがなかったが、子供だとばかり思っていたダムの背中は想像以上に男性を意識させるものだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "細身だが、しっかりとしている。\n
筋肉だってついていて……、子供だと思うことは難しい。"

play sound se_0698
show m_twi6_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dam "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ダムが体勢を低く構えて、一気に加速する。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「ディー……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鋭い下降は、猛禽のようだ。\n
私はその爪の代わりのように、ディーの体を地上からかっさらうべく腕を伸ばす。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dee "「！！」"

play sound se_0052
hide m_twi6_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が伸ばした腕を、ディーがしっかりと握り返す。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_9")
T "「……っく！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "腕にずしりとディーの重さがかかって、それと同時に目に見えて飛行速度が落ちた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがに三人乗りというのは無茶なようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0357
Dee "「兄弟、追いつかれちゃうよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の腕から、斧へとしがみつき直したディーが叫ぶ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0359
Dam "「こ、これで精一杯だよ、兄弟……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎりぎりまで高度を落とすことで速度を優先させるが、それでも逃げ切れるかどうかはギリギリだ。"

play sound se_0338
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0039
Servant "「逃がすか……っ！！」"

play sound se_0337
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人達も、すぐさま飛行魔法を発動させて追ってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らも相当熱くなっている。\n
手加減なしの（元々、あったかどうか怪しいが）、本気だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_6")
T "（追いつかれる……！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_6")
Dee "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_6")
Dam "「……！！」"

jump gakuen_dad6_5a
label gakuen_dad6_4:
menu:
    "（ここまで来たら、勝っても負けても……）":
        jump gakuen_dad6_5a
    "（いやいや、やっぱり勝ちたい……！）":
        jump gakuen_dad6_5b
label gakuen_dad6_5a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はぎゅっと目を閉じて覚悟を決める。\n
これだけやって、捕まったなら悔いはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0040
Servant "「捕まえたぞ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0035
Maid "「子供のときのツインズには、まだ負けませんよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎりぎりのところで逃げ切れず、使用人達の手が私達へと届いた。\n
同時に空気が抜けるような音がして、私達の魔法が一斉に解除されてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「……！！」"


play music night_garden_p_ali

scene bg20_gd_nig with Dissolve(1.6)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逃走中ということもあり、勢いのついていた体は前方へと投げ出される……。\n
と、身構えたのだが、そんなことにはならなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐさま別の使用人が発動させた魔法により、静かにその場で停止させられる。\n
私にとっては初めての経験だったのだが、ディーとダムは慣れているようだ。"


show dee_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0360
Dee "「あ～あ……。\n
せっかくお姉さんと愛の逃避行だったのに、捕まっちゃうなんてついていないよ」"

hide dee_m_01_5
show dee_m_01_5 at left
with dis

show dam_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0361
Dam "「そうだね、兄弟。\n
やっぱり大人にならないと、いろいろ不便だね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……どうして、大人にならなかったの？」"

hide dee_m_01_5
show dee_m_01_1 at left
with dis
hide dam_m_01_5
show dam_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice dad_g0362
Dee "「お姉さん、大人の僕達のこと、苦手でしょ？」"

hide dee_m_01_1
show dee_m_01_1 at left
with dis
hide dam_m_01_5
show dam_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice dad_g0363
Dam "「だからね、子供のままでも使用人達に勝てるって証明したかったんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「二人とも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誤解だ。\n
私は別に二人の大人の姿を苦手だとは思っていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや……、ある意味苦手なのだろうか。\n
大人の格好で子供のときと同じように無邪気に接せられると、照れたりときめいてしまったりと、いろいろと大変なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは外見だけが大人になっているだけなので、問題ないかもしれないが、私にとっては大問題。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、大人な彼らに対しての態度は、ちょっとぎこちなくなってしまっている部分がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（気にしてくれていたのね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなふうに、気にかけてくれていたとは驚きだ。"

play sound se_0624
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メイドさんに促されて私は女子寮へと、ディーとダムは使用人に促されて男子寮へと向かって歩き出す。"

hide dam_m_01_10
show dam_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0367
Dam "「お姉さん！\n
また明日遊ぼうね！！」"

hide dee_m_01_1
show dee_m_01_6 at left
with dis
hide dam_m_01_6
show dam_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0368
Dee "「また明日ー！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……もう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今からお小言、明日以降には罰掃除が待っているというのに、二人はのんきなものだ。\n
どうせまた、逃げ出す気なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に向かって大きく手をふりふり、男子寮へと見えなくなっていった。"

with dis
$ hi_mes()
hide dee_m_01_6

hide dam_m_01_6


scene bg_par15_rg_hat_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_par15_rg_hat_day
with stripe_l_medium

play music daytime_a_wam

scene bg20_gd_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズやストームというのは、健全だとはいうものの大胆なイベントだ。\n
何せ、一時とはいえ男女が室内で二人っきりになることができる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それをきっかけに仲が進展することも多いはず。\n
後から聞くところによると、カップルが成立する率も低くないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、カップルというにはちょっといろいろ特殊な事情がある私達はといえば、木陰で三人仲良く涼んでいた。"

play sound se_0464

show m_twi_goodend1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "木の幹に背中を預けて座る私の、それぞれの足を枕に双子が芝生に転がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0369
Dam "「次は絶対に負けないから……！\n
僕達が勝ったら、僕達と付き合ってね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（僕達、ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひとくくりになることも、今は違和感がないものの。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「……そうね、考えておくわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、特に何かが変わることもなく、相変わらずの関係を続けている。\n
双子の私に対する想いが、何であるのかは今も明確ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じく、私が、双子に対して抱いている気持ちの正体もよく分からない。\n
よく分からないままに、私達の関係は形を変えないままに続いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……形を変える機会がなかったのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの夜を一緒に過ごしていたのならば、もしかするともっと違った関係になっていたのかもしれないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……なんて、終わってしまったことを考えても仕方がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ディーとダムの二人も、すでに次のストームとブリーズへと目標を絞っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今のところ二人の目標は、大人への変身魔法を使うことなく、使用人達に勝つことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（そして、私と付き合うこと）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くすぐったいような気持ち。\n
これは、期待なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントとしても、方向性としても、間違っている。\n
私は年長者として、止めるべきなのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……ま、いいわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "終わったばかりで、そんなに先のことを考えるほど計画的でも、大人でもない。\n
考える時間ならばたっぷりとある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次のストームとブリーズまで、あと一年。\n
二人と一緒に成長していけばいい。"

hide frame_par_togaki
hide ali_m_06_16
with Dissolve(2)
show white onlayer master
with compress_extralong

show black with compress_extraextralong
stop music
jump gakuen_b
