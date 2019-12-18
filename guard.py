class EnnemyGuard:
  """Class defining the ennemy to knock out with status and position"""

  def __init__(self,location):
    self.is_awake=True
    self.position=location
