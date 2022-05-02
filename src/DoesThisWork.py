class GameObject:
    def __init__(self, xLoc, yLoc):
        self.xLoc = xLoc
        self.yLoc = yLoc
    def move(self,dx,dy):
        self.xLoc+=dx
        self.yLoc+=dy
    def __str__(self):
        out="xLoc: "+str(self.xLoc)+" yLoc: "+str(self.yLoc)
        return out
'''
class HealthPotion (xLoc:Double,yLoc:Double,var increase:Int)
      extends GameItem (xLoc,yLoc){

  override def use(player: Player): Unit = {
    player.health+=this.increase
  }
  def multiplyEffect(factor:Int):Unit={
    this.increase*=factor
  }
  override def equals(obj: Any): Boolean = {
    obj match{
      case hp:HealthPotion => this.increase==hp.increase
      case _=>false
    }
  }
}
'''
class HealthPotion(GameObject):
    def __init__(self,xLoc,yLoc,increase):
        GameObject.__init__(self,xLoc,yLoc)
        self.increase=increase
    def __str__(self):
        out=super().__str__()
        out+=" increase: "+str(self.increase)
        return out



if __name__ == '__main__':
    print("in main")
    print(type(7))
    go=GameObject(1,2)
    print(go)
    go2=go
    go2.move(2,2)
    print(go)
    hp=HealthPotion(5,6,10)
    print(hp)
    hp.move(10,10)
    print(hp)