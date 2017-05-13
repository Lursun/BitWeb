
class Circles :
    circleslist=dict()
    def __init__(self,circleid,blocks):
        Circles.circleslist[circleid]=blocks
    @staticmethod
    def getCircle(circleid):
        return Circles.circleslist[circleid]
        