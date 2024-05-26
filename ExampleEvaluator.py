# This script is used for offline evaluation of decisions and trajectories 

from simInfo.Evaluation import Decision_Evaluation
from simModel.Replay import ReplayModel

if __name__ == "__main__":
    database = './results/2024-05-26_21-45-17.db'
    model = ReplayModel(database)
    evaluator = Decision_Evaluation(database, model.timeStep)
    while not model.tpEnd:
        model.runStep()
        evaluator.Evaluate(model)