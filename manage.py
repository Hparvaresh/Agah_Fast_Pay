
from FPT.logic.fast_pay_train_logic import FastPayTrainLogic
from gcl.utils.config.configuration import Configuration
from test_env import RuntimeConfig
def run():
    FPL =FastPayTrainLogic()
    FPL.run()



if __name__ == '__main__':
    Configuration.apply(RuntimeConfig, alternative_env_search_dir=__file__)
    Configuration.config_logging()
    run()

