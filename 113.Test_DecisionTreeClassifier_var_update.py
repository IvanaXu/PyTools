#
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree.export import export_text

N, M, max_depth = 100, 10000, 3
Cols = [
    f"X{icol}"
    for icol in range(N)
]
_x, _y = make_classification(
    n_samples=M, 
    n_features=N, 
    n_informative=N//3,
)
data = pd.DataFrame(_x, columns=Cols)
data["Target"] = _y

X = data[Cols]
y = data["Target"]
print(X.head())
print(pd.value_counts(y))

model = DecisionTreeClassifier(
    max_depth=max_depth,
    min_samples_leaf=M//20,
    random_state=10086,
)
model.fit(X, y)
print(f"Score: {model.score(X, y):f}")

# 
_e = export_text(
    model, feature_names=Cols, show_weights=True, decimals=4)

_rsep0, _rsep1 = "|   ", "|---"
_rule, i_rule, j_rule = [], [np.nan for _depth in range(max_depth)], None
for i_e in _e.split("\n"):
    print(i_e)
    if not i_e:
        continue
    elif "weights" in i_e:
        _rule.append(j_rule)
        continue

    _rule0 = f"""{i_e.split(_rsep1)[0]}{_rsep1}"""
    _rule1 = i_e.split(_rsep1)[1].strip(" ")

    for _depth in range(max_depth):
        _leaf = f"""{_rsep0*_depth}{_rsep1}"""
        if _rule0 == _leaf:
            if _depth == 0:
                i_rule = [np.nan for _depth in range(max_depth)]
            i_rule[_depth] = _rule1
            j_rule = i_rule.copy()

            if _depth + 1 == max_depth:
                i_rule[_depth] = np.nan
            break

_rule_cols = [f"RULE{_depth}" for _depth in range(max_depth)]
_vars = [icol for icol, _0 in zip(X.columns, model.feature_importances_) if _0 > 0]
_rule = pd.DataFrame(_rule, columns=_rule_cols)
# print(_rule)

assert _rule.shape[0] <= 2**max_depth
assert _rule.shape == _rule.drop_duplicates().shape

_result = []
for irule in _rule.to_dict("split")["data"]:
    idata = data.copy()
    for jrule in irule:
        if not pd.isna(jrule):
            _r0 = jrule.split(" ")[0]
            _r1 = jrule.replace(_r0, " ")
            idata = eval(f"""idata[idata["{_r0}"]{_r1}]""")
    _result.append(irule+[idata])
_result = pd.DataFrame(_result, columns=_rule_cols+["idata"])
# print(_result)

_result["cnt0"] = _result["idata"].apply(lambda x: x[x["Target"] == 0].shape[0])
_result["cnt1"] = _result["idata"].apply(lambda x: x[x["Target"] == 1].shape[0])
assert _result["cnt0"].sum() == data[data["Target"] == 0].shape[0]
assert _result["cnt1"].sum() == data[data["Target"] == 1].shape[0]

_result["pcnt0"] = _result["cnt0"]/_result["cnt0"].sum()
_result["pcnt1"] = _result["cnt1"]/_result["cnt1"].sum()

_result["rate0"] = _result["cnt0"]/(_result["cnt0"]+_result["cnt1"])
_result["rate1"] = _result["cnt1"]/(_result["cnt0"]+_result["cnt1"])
_result["Arate1"] = _result["cnt1"].sum()/(_result["cnt0"].sum()+_result["cnt1"].sum())
_result["lift"] = _result["rate1"]/_result["Arate1"]

_result.sort_values("lift", ascending=False, inplace=True)
_result["iKS"] = _result["cnt1"].cumsum()/_result["cnt1"].sum() - _result["cnt0"].cumsum()/_result["cnt0"].sum()
_result["KS"] = KS = _result["iKS"].max()
print(f"KS: {KS:f}")

_result.drop(["idata", "iKS"], axis=1, inplace=True)
_result.sort_values(_rule_cols, ascending=True, inplace=True)
_result.to_csv("113.Test_DecisionTreeClassifier_var_update.csv", index=False)

print(_result)
