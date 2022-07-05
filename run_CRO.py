from models.multiple_solution.evolutionary_based.CRO import BaseCRO
from utils.FunctionUtil import *
import random
import multiprocessing
import pandas as pd
from models.multiple_solution.evolutionary_based.tuner.Preset import Preset

## Setting parameters
root_paras = {
    "problem_size": 100,
    "domain_range": [-100, 100],
    "print_train": True,
    "objective_func": C28   # original C30
}

cro_paras = {
    "epoch": 500,
    "pop_size": 300,
    "G": [0.02, 0.2],
    "GCR": 0.1,
    # tune the following parameter
    "po": 0.4,
    "Fb": 0.9,
    "Fa": 0.1,
    "Fd": 0.1,
    "Pd": 0.1,
    "k": 3
}

cro_para_range = {
    "po": [0.0, 1.0],
    "Fb": [0.0, 1.0],
    "Fa": [0.0, 1.0],
    "Pd": [0.0, 1.0],
    "k": [1, 15]
}
# po: the rate of free/occupied at the beginning (note: pop_size = free + occupied)
# Fb: BroadcastSpawner/ExistingCorals rate
# Fa: fraction of corals duplicates its self and tries to settle in a different part of the reef
# Fd: fraction of the worse health corals in reef will be applied depredation
# Pd: Probabilty of depredation
# k : number of attempts for a larvar to set in the reef.



## Run model
random.seed(666)

## tuning method training
#proc = multiprocess.Process()
#for i in range(10):
#    md = BaseCRO(root_algo_paras=root_paras, cro_paras=cro_paras)
#    md._tuning_train__(cro_para_range, i, 1800)

# fixed-preset training
def preset_train(iters, preset, running_time):
    for i in range(iters):
        md = BaseCRO(root_algo_paras=root_paras, cro_paras=cro_paras)
        md._preset_train__(preset, i, running_time)


#if __name__ == "__main__":
#    file_name = "C:/courses/thesis preparation/new model reference model/collect data/presets.xlsx"
#    pre_list = pd.read_excel(file_name, sheet_name="Presets", index_col=0)  # returns a dataframe

#    predic0 = pre_list.iloc[0].to_dict()
#    predic0['k'] = int(predic0['k'])
#    pre0 = Preset(predic0, name=0)

#    predic1 = pre_list.iloc[1].to_dict()
#    predic1['k'] = int(predic1['k'])
#    pre1 = Preset(predic1, name=0)
    
#    proc0 = multiprocessing.Process(target=preset_train, args=(3, pre0, 40))
#    proc1 = multiprocessing.Process(target=preset_train, args=(3, pre1, 40))
#    proc0.start()
#    proc1.start()
#    proc0.join()
#    proc1.join()


