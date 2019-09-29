import random
import unittest

class CommonFun(unittest.TestCase):
    def getChar(self,times=1):
        tchar=""
        for i in range(times):
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
            val = f'{head:x}{body:x}'
            str = bytes.fromhex(val).decode('gb2312')
            tchar=tchar+str
        return tchar
        # print(tchar)

    def getName(self):
        a1 = ['张', '金', '李', '王', '赵']
        a2 = ['玉', '明', '龙', '芳', '军', '玲']
        a3 = ['', '立', '玲', '', '国', '']
        name = random.choice(a1) + random.choice(a2) + random.choice(a3)
        return name

    # 随机生成手机号码
    def getPhone(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        tele=random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
        return tele

if __name__ == "__main__":
    unittest.main()


