import yaml
import os


class Config:
  def __init__(self):
    self.dirname = os.path.dirname(__file__)
    self.filename = os.path.join(self.dirname,'config.yaml')
    with open(self.filename, mode="r") as file:
      self.content = yaml.load(file, Loader=yaml.FullLoader)


  def __getitem__(self,key):
    return self.content[key]

  def read(self):
    return self.content

  def save(self):
    with open(self.filename,mode='w') as fileToWrite:
      yaml.safe_dump(self.content,fileToWrite,encoding='utf-8', allow_unicode=True)

  def update(self, entry):
    self.content.update(entry)
    return self