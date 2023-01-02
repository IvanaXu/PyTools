day = 6
match day:
    case 1:
        print("星期一")
    case 6 | 7:
        print("周末")
    case _ : 
        print("其他情况")
