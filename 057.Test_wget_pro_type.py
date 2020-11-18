import os
import wget
import json

with open("train_annotations.json") as f:
    ltrai = [_ for _ in json.loads(f.readlines()[0]).keys()]
with open("val_video_ids.txt") as f:
    lvals = [k.strip("\n") for k in f]
# to change the N.
N, title = 1, "http://tianchi-competition.oss-cn-hangzhou.aliyuncs.com/531798"

def getit(lid, subset, subtyp, subout, ftype):
    """
        @lid:ID;
        @subset:train,val;
        @subtyp:video,i3d_feature,vggish_feature;
        @subout:OUTPUT;
        @ftype:.npy,.mp4;
    """
    n = 0
    for kid in lid:
        url = f"{title}/{subset}/{subtyp}/{kid}{ftype}"
        if n < N and not os.path.exists(f"{subout}/{subtyp}_{kid}{ftype}"):
            try:
                wget.download(url, out=f"{subout}/{subtyp}_{kid}{ftype}")
            except Exception as e:
                print(n, kid, e)
        n += 1
getit(ltrai, "train", "video", "outs/trai", ".mp4")
getit(lvals, "val", "video", "outs/vals", ".mp4")

getit(ltrai, "train", "i3d_feature", "outs/trai", ".npy")
getit(lvals, "val", "i3d_feature", "outs/vals", ".npy")

getit(ltrai, "train", "vggish_feature", "outs/trai", ".npy")
getit(lvals, "val", "vggish_feature", "outs/vals", ".npy")



