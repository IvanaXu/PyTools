import os
import wget
import json

with open("train_annotations.json") as f:
    ltrai = [_ for _ in json.loads(f.readlines()[0]).keys()]
with open("val_video_ids.txt") as f:
    lvals = [k.strip("\n") for k in f]

N = 5
title = "http://tianchi-competition.oss-cn-hangzhou.aliyuncs.com/531798"

def getit(lid, subset, subtyp, subout):
    """
    :param lid: THE ID LIST.
    :param subset: train, val
    :param subtyp: video, i3d_feature, vggish_feature
    :param subout: THE OUTPUT PATH.
    """
    n = 0
    for kid in lid:
        url = f"{title}/{subset}/{subtyp}/{kid}.npy"
        if n <= N and not os.path.exists(f"{subout}/{subtyp}_{kid}.npy"):
            try:
                wget.download(url, out=f"{subout}/{subtyp}_{kid}.npy")
            except Exception as e:
                print(n, k, e)
        n += 1

getit(ltrai, "train", "vggish_feature", "outs/trai")
getit(lvals, "val", "vggish_feature", "outs/vals")