from scipy.stats import norm

def sample_size(p, d, alpha, beta):
    """
    计算最少需要参与测试的样本数量
    :param p: 目标不良率
    :param d: 允许的误差
    :param alpha: 显著性水平
    :param beta: 可信水平
    :return: 最少需要参与测试的样本数量
    """
    z_alpha = norm.ppf(1 - alpha)
    z_beta = norm.ppf(beta)
    n = ((z_alpha + z_beta) ** 2) * p * (1 - p) / (d ** 2)
    print("")
    print(f"显著性水平的正态分布Zα: {z_alpha}")
    print(f"可信水平的的正态分布Zβ: {z_beta}")
    return int(n)

p = float(input("请输入目标不良率p（例如：0.005）："))
d = float(input("请输入允许的误差d（例如：0.001）："))
alpha = float(input("请输入显著性水平β（例如：0.01，即实际可能超出目标不良率的几率）："))
beta = float(input("请输入可信水平β（例如：0.99，即实际可能超出目标不良率的几率）："))
print("")
print(f"目标不良率p: {p}")
print(f"允许的误差d: {d}")
print(f"显著性水平α: {alpha}")
print(f"可信水平β: {beta}")


n = sample_size(p, d, alpha, beta)
print("")
print("")
print(f"最少需要参与测试的样本数量: {n}")
