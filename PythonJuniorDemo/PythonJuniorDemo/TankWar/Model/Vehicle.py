from Position import Position
class Vehicle(object):
    """the original object for all objects that can move"""
    def __init__(self,type='T20'):
        self.type = type
        self.speed = 0
        self.dir = 'UP'#python 有没有枚举
        self.pos = Position()
        self.isAlive = True
        self.Hp = 0
        self.Mp = 0
    def move(self):
        #python 没有casewhen吗
        if self.isAlive==False:
            return
        else:
            newPos = self.pos
            if self.dir=='UP':
                newPos.posY += self.speed
            elif self.dir=='DOWN' :
                newPos.posY -= self.speed
            elif self.dir == 'LEFT':
                newPos.posX += self.speed
            elif self.dir == 'RIGHT':
                newPos.posX += self.speed
            elif self.dir == 'ASCEND':
                newPos.posZ += 1
            elif self.dir == 'DESCEND':
                newPos.posZ -= 1
            else:
                raise Exception('Direction error')
            #需要一个全局方法，由地图对象提供，返回移动结果

