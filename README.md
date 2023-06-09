# BPSK_simulator
ディジタル変調方式のビット誤り率特性をシミュレーションしたプログラムです。

## ex1.py
ランダムなデータに基づくBPSK変調のベースバンド時間波形を生成しています．
ベースバンド信号としてシンボルタイミング点においてのみ信号が存在するインパルス信号を想定し, 振幅は平均信号電力が1となるように設定しています.

![simulation result of ex1](simulation_result/B_1.png)

## ex2.py
ボックスミューラー法により，の正規分布を有する雑音信号（平均0，分散σ_n^2）を生成するプログラムです．
雑音信号が正規分布を有しているかを検証するため，雑音信号を生成し，確率密度を取得・図示しています．
また，その分散を求め，設定した分散に一致しているかを確認しています．

![simulation result of ex2](simulation_result/B_2_1.png)
![simulation result of ex2](simulation_result/B_2_2.png)
![simulation result of ex2](simulation_result/B_2_3.png)

## ex3.py
SNRの違いが信号波形に与える影響を確認するためのシミュレーションプログラムです.
SNRが0dBと10dBのときのベースバンド時間波形を図示しています.

![simulation result of ex3](simulation_result/B_3.png)

## ex4.py
ビット誤り率特性(BER)を取得し、計算により求められた理論BERと比較します。
具体的には、SNRを0dB～10dBまで1dB刻みで変化させたときのBPSK信号のビット誤り率特性を取得し，誤差補関数により与えられる理論BER特性との比較を行っています.

## ex5.py
得られたBPSK信号のビット誤り率特性を用いて，BPSK信号の通信路容量を取得するとともに，シャノンの通信路容量（シャノン限界）と比較しています.

![simulation result of ex5](simulation_result/B_6.png)
