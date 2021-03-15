import numpy as np

# 入手元：気象庁ホームページ（https://www.data.jma.go.jp/gmd/risk/obsdl/index.php）
# 2018年4月の東京の最高気温（日別）
x = np.array([21.9, 24.5, 23.4, 26.2, 15.3, 22.4, 21.8, 16.8,
              19.9, 19.1, 21.9, 25.9, 20.9, 18.8, 22.1, 20.0,
              15.0, 16.0, 22.2, 26.4, 26.0, 28.3, 18.7, 21.3,
              22.5, 25.0, 22.0, 26.1, 25.6, 25.7])
# 2018年4月の札幌の最高気温（日別）
y = np.array([8.3, 13.0, 8.4, 7.9, 7.0, 3.7, 6.1, 8.5, 8.6,
              11.9, 12.1, 14.4, 7.0, 10.5, 6.6, 10.6, 16.6,
              19.1, 20.1, 19.8, 24.5, 12.6, 16.4, 13.0, 13.3,
              14.1, 14.4, 17.0, 21.3, 24.5])


mx = x.sum() / len(x)
my = y.sum() / len(y)
sx = np.sqrt(((x - mx)**2).sum() / len(x))
sy = np.sqrt(((y - my)**2).sum() / len(y))
sxy = ((x - mx) * (y - my)).sum() / len(x)
print("東京の最高気温の標準偏差:{:4f}".format(sx))
print("札幌の最高気温の標準偏差:{:4f}".format(sy))
print("共分散:{:4f}".format(sxy))
print("相関係数:{:4f}".format(sxy / (sx * sy)))
