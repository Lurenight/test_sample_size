# test_sample_size
# 这是一个用来利用单侧正态近似法来计算最小测试样本数的python脚本
# 计算题目：某产品生产线进行不良品率测试，目标不良率不超过0.5%，显著性水平为0.1%，可信水平95%，计算最少需要参与测试的样本数量

# 显著性水平
在您的例子中，显著性水平表示了在产品实际不良率不超过目标值（即 0.5%）的情况下，观察到测试结果不良率超过目标值的概率。您设定的显著性水平为 1%，意味着如果产品实际不良率不超过目标值，那么您有 1% 的概率会观察到测试结果不良率超过目标值。

因此，显著性水平越低，您犯这种错误的概率就越小。当然，显著性水平越低，需要参与测试的样本数量也就越多。因此，在实际应用中需要根据具体情况权衡利弊，选择合适的显著性水平。


# 可信水平
在您的例子中，可信水平表示了在产品实际不良率超过目标值（即 0.5%）的情况下，观察到测试结果不良率超过目标值的概率。您设定的可信水平为 99%，意味着如果产品实际不良率超过目标值，那么您有 99% 的概率会观察到测试结果不良率超过目标值。

因此，可信水平越高，您发现问题的概率就越大。当然，可信水平越高，需要参与测试的样本数量也就越多。因此，在实际应用中需要根据具体情况权衡利弊，选择合适的可信水平。

已收到消息. 在您的例子中，可信水平表示了在产品实际不良率超过目标值（即 0.5%）的情况下，观察到测试结果不良率超过目标值的概率。您设定的可信水平为 99%，意味着如果产品实际不良率超过目标值，那么您有 99% 的概率会观察到测试结果不良率超过目标值。 因此，可信水平越高，您发现问题的概率就越大。当然，可信水平越高，需要参与测试的样本数量也就越多。因此，在实际应用中需要根据具体情况权衡利弊，选择合适的可信水平。


# 可接受误差
在您的例子中，可接受误差表示了测试结果不良率与产品实际不良率之间的最大允许误差。您设定的可接受误差为 0.1%，意味着如果产品实际不良率与测试结果不良率之差不超过 0.1%，那么您认为测试结果是可接受的。

因此，可接受误差越小，测试结果就越精确。当然，可接受误差越小，需要参与测试的样本数量也就越多。因此，在实际应用中需要根据具体情况权衡利弊，选择合适的可接受误差。


# 显著性水平、可信水平和允许误差之间的权衡例子如下

假设您是一家制药公司的质量控制经理，您需要检验一批药品的合格率是否达到了标准。如果合格率低于标准，您需要召回这批药品，否则您需要放行这批药品。您的显著性水平、可信水平和允许误差会影响您的决策。
如果您的显著性水平很高，比如 α=0.1，那么您有 10% 的可能性拒绝一个正确的假设，也就是说您有 10% 的可能性错误地召回一批合格的药品，这会给公司造成损失。如果您的显著性水平很低，比如 α=0.001，那么您有 0.1% 的可能性接受一个错误的假设，也就是说您有 0.1% 的可能性错误地放行一批不合格的药品，这会给消费者造成危害。因此，您需要根据实际情况选择一个合适的显著性水平，既要保证公司的利益，又要保证消费者的安全。
如果您的可信水平很高，比如 1−α=0.99，那么您有 99% 的可能性得出正确的区间，也就是说您有 99% 的可能性正确地判断药品的合格率是否达到了标准。但是，这样的区间往往会很宽，也就是说您对药品合格率的估计不够精确。如果您的可信水平很低，比如 1−α=0.9，那么您有 90% 的可能性得出正确的区间，也就是说您有 90% 的可能性正确地判断药品合格率是否达到了标准。但是，这样的区间往往会很窄，也就是说您对药品合格率的估计比较精确。因此，您需要根据实际情况选择一个合适的可信水平，既要保证区间的可靠性，又要保证区间的精确度。
如果您的允许误差很大，比如 d=0.05，那么您可以接受样本合格率与总体合格率之间相差不超过 5% 的情况。但是，这样的误差可能会影响您对药品质量的判断。例如，如果标准合格率是 90%，而样本合格率是 85%，那么总体合格率可能在 [80%,90%] 这个范围内。这意味着总体合格率可能低于标准合格率，但是由于误差太大，您无法确定。如果您的允许误差很小，比如 d=0.01，那么您可以接受样本合格率与总体合格率之间相差不超过 1% 的情况。但是，这样的误差要求往往需要更多的样本数据来支持。例如，如果标准合格率是 90%，而样本合格率是 85%，那么总体合格率可能在 [84%,86%] 这个范围内。这意味着总体合格率肯定低于标准合格率，但是您需要收集更多的数据来得出这个结论。因此，您需要根据实际情况选择一个合适的允许误差，既要保证误差的可接受性，又要保证数据的可获得性。

