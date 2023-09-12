from FPT.dal.pgdao.fast_pay_train_pg import FastPayTrainPGDao

class Dal():
    def __init__(self) -> None:
        self.fast_pay_train_pg = FastPayTrainPGDao()
        
    def read_sql_by_query(self,query:str):
        return self.fast_pay_train_pg.read_sql_by_query(query)

    