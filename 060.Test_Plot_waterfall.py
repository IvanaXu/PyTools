#
import matplotlib.pyplot as plt

lr0, lr1, lr2 = 76234, 53654, 46857
print(lr0, lr1, lr2)

plt.figure(figsize=(16, 8))
plt.bar(
    [0, 1, 2, 3],
    [lr0, lr0 - lr1, lr1 - lr2, lr2],
    color="#87CEFA",
    width=0.4,
    bottom=[0, lr1, lr2, 0],
)
plt.savefig("060.Test_Plot_waterfall.jpg")
plt.show()
