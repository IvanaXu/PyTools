# -*- coding:utf-8 -*-
# @auth ivan
# @time 20190131
# @goal Test_F1-micro&F1-macro
"""
https://www.cnblogs.com/techengin/p/8962024.html

F1-score = 2*(P*R)/(P+R)

准确率(P) = TP/(TP+FP)
召回率(R) = TP/(TP+FN)

对于数据测试结果有下面4种情况:
真阳性(TP): 预测为正, 实际为正;
假阳性(FP): 预测为正, 实际为负;
假阴性(FN): 预测为负, 实际为正;
真阴性(TN): 预测为负, 实际为负;
TODO: check.
"""
"""
from sklearn.metrics import f1_score

    average : string, [None, 'binary' (default), 'micro', 'macro', 'samples', \
                       'weighted']
        This parameter is required for multiclass/multilabel targets.
        If ``None``, the scores for each class are returned. Otherwise, this
        determines the type of averaging performed on the data:

        ``'binary'``:
            Only report results for the class specified by ``pos_label``.
            This is applicable only if targets (``y_{true,pred}``) are binary.
        ``'micro'``:
            Calculate metrics globally by counting the total true positives,
            false negatives and false positives.
        ``'macro'``:
            Calculate metrics for each label, and find their unweighted
            mean.  This does not take label imbalance into account.
        ``'weighted'``:
            Calculate metrics for each label, and find their average, weighted
            by support (the number of true instances for each label). This
            alters 'macro' to account for label imbalance; it can result in an
            F-score that is not between precision and recall.
        ``'samples'``:
            Calculate metrics for each instance, and find their average (only
            meaningful for multilabel classification where this differs from
            :func:`accuracy_score`).
"""
from sklearn.metrics import f1_score, precision_recall_fscore_support
y_true = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4]
y_pred = [1, 1, 1, 0, 0, 2, 2, 3, 3, 3, 4, 3, 4, 3]

print(f1_score(y_true, y_pred, labels=[1,2,3,4], average='micro'))
# 0.6153846153846153

p_class, r_class, f_class, support_micro = precision_recall_fscore_support(
    y_true=y_true, y_pred=y_pred, labels=[1, 2, 3, 4], average=None)
print(f_class.mean(), f_class)
# 0.6041666666666666 [0.75       0.66666667 0.5        0.5       ]

print(f1_score(y_true, y_pred, labels=[1,2,3,4], average='macro'))
# 0.6041666666666666



