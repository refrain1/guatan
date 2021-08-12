class 瓜摊(object):
    刀 = 1
    瓜 = 9999
    摊 = 1
    称 = 1
    吸铁石 = 1


class 老板():
    def __init__(self, 瓜摊):
        self.瓜摊 = 瓜摊
        self.瓜 = 0

    def 行(self):
        print('行')

    def 价格(self):
        print('2块一斤')

    def 称称(self):
        self.瓜摊.瓜 = self.瓜摊.瓜 - 1
        self.瓜 = 1
        print('15斤30块')

    def 哪儿有瓜(self):
        print('你瞧瞧现在哪儿有瓜呀，这都是大棚的瓜，你嫌贵我还嫌贵呢')

    def 生瓜蛋子(self):
        print('我开水果摊的，能卖你生瓜蛋子')

    def 找茬儿(self):
        print('你是故意找茬儿，是不是，你要不要吧')

    def 吃了它(self):
        print('要是不熟，我自己吃了它，这下你满意了吧')

    def 要不要(self):
        print('你是故意找茬儿，是不是，你要不要吧,你要不要')

    def 劈瓜(self):
        print('你劈我瓜是吧')

    def 啊(self):
        print('啊~')


老板 = 老板(瓜摊)


class 小弟():
    def 萨日朗(self):
        print('萨日朗~')


小弟 = 小弟()
进程 = False


class 华强(object):
    def 加载(self):
        global 进程
        进程 = True

    def 拿刀(self):
        老板.瓜摊.刀 = 老板.瓜摊.刀 - 1
        老板.瓜 = 老板.瓜 - 1

    def 吸铁石(self):
        print('发现称下吸铁石{吸铁石}个'.format(吸铁石=老板.瓜摊.吸铁石))

    def 啊(self):
        老板.啊()
        global 进程
        进程 = False


华强 = 华强()
if __name__ == '__main__':
    华强.加载()
    while 进程:
        对话 = input('请输入华强对话\n')
        if 对话 == '哥们，这瓜多少钱一斤啊？':
            老板.价格()
        elif 对话 == 'woc,你这瓜皮是金子做的还是瓜粒子是金子做的':
            老板.哪儿有瓜()
        elif 对话 == '给我挑一个':
            老板.行()
        elif 对话 == '你这瓜保熟吗':
            老板.生瓜蛋子()
        elif 对话 == '我问你这瓜保熟吗':
            老板.找茬儿()
        elif 对话 == '你这瓜要是熟的我肯定要啊，那它是生的怎么办啊':
            老板.吃了它()
            老板.称称()
        elif 对话 == '你这哪有15斤呀,你这称有问题呀':
            老板.要不要()
        elif 对话 == '看吸铁石':
            华强.吸铁石()
        elif 对话 == '另外你说的啊,这瓜要是生的,你自己吃了它':
            华强.拿刀()
            老板.劈瓜()
            华强.啊()
            小弟.萨日朗()
