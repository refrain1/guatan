class guatan(object):
    dao = 1
    gua = 9999
    tan = 1
    cheng = 1
    xitieshi = 1


class laoban():
    def __init__(self, guatan):
        self.guatan = guatan
        self.gua = 0

    def xing(self):
        print('行')

    def jiage(self):
        print('2块一斤')

    def chengcheng(self):
        self.guatan.gua = self.guatan.gua - 1
        self.gua = 1
        print('15斤30块')

    def naeryougua(self):
        print('你瞧瞧现在哪儿有瓜呀，这都是大棚的瓜，你嫌贵我还嫌贵呢')

    def shengguadanzi(self):
        print('我开水果摊的，能卖你生瓜蛋子')

    def zhaocha(self):
        print('你是故意找茬儿，是不是，你要不要吧')

    def flag(self):
        print('要是不熟，我自己吃了它，这下你满意了吧')

    def yaobuyao(self):
        print('你是故意找茬儿，是不是，你要不要吧,你要不要')

    def pigua(self):
        print('你劈我瓜是吧')

    def kill(self):
        print('啊~')


laoban = laoban(guatan)


class xiaodi():
    def sarilang(self):
        print('萨日朗')


xiaodi = xiaodi()

jincheng = False


class huaqiang(object):
    def jiazai(self):
        global jincheng
        jincheng = True

    def zui(hua):
        print(str(hua))

    def nadao(self):
        laoban.guatan.dao = laoban.guatan.dao - 1
        laoban.gua = laoban.gua - 1

    def xitieshi(self):
        print('发现称下吸铁石{xitieshi}个'.format(xitieshi=laoban.guatan.xitieshi))

    def kill(self):
        laoban.kill()
        global jincheng
        jincheng = False


huaqiang = huaqiang()

if __name__ == '__main__':
    huaqiang.jiazai()
    while jincheng:
        duihua = input('请输入华强对话')
        if duihua == '哥们，这瓜多少钱一斤啊？':
            laoban.jiage()
        elif duihua == 'woc,你这瓜皮是金子做的还是瓜粒子是金子做的':
            laoban.naeryougua()
        elif duihua == '给我挑一个':
            laoban.xing()
        elif duihua == '你这瓜保熟吗':
            laoban.shengguadanzi()
        elif duihua == '我问你这瓜保熟吗':
            laoban.zhaocha()
        elif duihua == '你这瓜要是熟的我肯定要啊，那它是生的怎么办啊':
            laoban.flag()
            laoban.chengcheng()
        elif duihua == '你这哪有15斤呀,你这称有问题呀':
            laoban.yaobuyao()
        elif duihua == '看吸铁石':
            huaqiang.xitieshi()
        elif duihua == '另外你说的啊,这瓜要是生的,你自己吃了它':
            huaqiang.nadao()
            laoban.pigua()
            huaqiang.kill()
            xiaodi.sarilang()
