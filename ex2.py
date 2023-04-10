# ボックスミューラー法により，の正規分布を有する雑音信号（平均0，分散σ_n^2）を生成する．雑音信号が正規分布を有しているか否かを検証すべく，十分な個数の雑音信号を取得し，その確率密度を取得・図示する．また，その分散を求め，設定した分散に一致しているかを確認する．

import numpy as np
import matplotlib.pyplot as plt

# パラメータ
num_samples = 10000  # 生成する雑音サンプルの数
ave = 0  # 雑音信号の平均
sd = 1  # 雑音信号の標準偏差

# ボックス・ミュラー法を使用して雑音サンプルを生成
u1 = np.random.rand(num_samples // 2)
u2 = np.random.rand(num_samples // 2)
z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
z1 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
noise = np.concatenate((z0, z1))

# 雑音信号に平均値と標準偏差を追加
noise = noise * sd + ave

# 雑音信号が正規分布を持っていることを確認
plt.hist(noise, bins=100, density=True, label='Noise')

# 雑音信号の分散を計算
noise_var = np.var(noise)

# 計算した分散と設定した分散を比較
print("設定値：", sd*sd)
print("計算値：", noise_var)

# 雑音信号の確率密度関数をプロット
x = np.linspace(ave - 3*sd, ave + 3*sd, 100)
plt.plot(x, 1/(sd * np.sqrt(2 * np.pi)) * np.exp( - (x - ave)**2 / (2 * s**2) ))
plt.legend()
plt.show()