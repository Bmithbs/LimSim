from simModel.Replay import ReplayModel
from simModel.RGUI import GUI

database = './ExampleDB/LLMAgent_withMemory.db'
model = ReplayModel(database)
gui = GUI(model)

gui.run()