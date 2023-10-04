from FPT.vo.pd_mapping_vo import PDMappingVO
from FPT.vo.models_vo import ModelsVO


train_feature_map_ratio = [
    { PDMappingVO.TRAIN_MODEL: [ModelsVO.SVR,
                                ModelsVO.GRADIEN_BOOSTING_REGRESSION, 
                                ModelsVO.DECISON_TREE_REGRESSION, 
                                ModelsVO.LINEAR_RGRESSION, 
                                ModelsVO.RANDOM_FOREST_REGRESSION]
      },

    { PDMappingVO.PLOT_FEATURE: False
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_HARMONEY_CHECK,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [0],
        PDMappingVO.AS_TARGET : True,
      },

    { PDMappingVO.COLUMN_NAME: PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME,
    PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
    PDMappingVO.GET_SHIFT: [1],
     },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME,
    PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
        PDMappingVO.GET_SHIFT: [1],
        },

    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_HARMONEY_CHECK,
        PDMappingVO.GET_RATIO: [1,2,3,],
        PDMappingVO.GET_SHIFT: [1],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.DOLLAR_VALUE,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [1],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.INDEX_INDEX_VALUE,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [1],
      },


    { PDMappingVO.COLUMN_NAME: PDMappingVO.IPO_TICKET,
    PDMappingVO.KEEP_COLUMN : True
        },
]

test_feature_map_ratio= [
  {PDMappingVO.TYPE : PDMappingVO.REGRESSION},
    { PDMappingVO.INCREASE_FACTOR: 1.7
      },
        { PDMappingVO.PLOT_FEATURE: False
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME,
    PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
    PDMappingVO.GET_SHIFT: [1],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME,
    PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
        PDMappingVO.GET_SHIFT: [1],
        },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [0],
        PDMappingVO.AS_TARGET : True,
      },

    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
        PDMappingVO.GET_RATIO: [1,2,3],
        PDMappingVO.GET_SHIFT: [1],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.DOLLAR_VALUE,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [1],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.INDEX_INDEX_VALUE,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [1],
      },


    { PDMappingVO.COLUMN_NAME: PDMappingVO.IPO_TICKET,
    PDMappingVO.KEEP_COLUMN : True
        },
]

# ModelsVO.GRADIEN_BOOSTING_REGRESSION, 
# ModelsVO.DECISON_TREE_REGRESSION, 
# ModelsVO.LINEAR_RGRESSION, 
# ModelsVO.RANDOM_FOREST_REGRESSION,
# ModelsVO.RIDGE,
# ModelsVO.LASSO,
# ModelsVO.ELASTIC_NET,
# ModelsVO.SGD_REGRESSION,
# ModelsVO.K_NEIGHBORS_REGRESSION,
# ModelsVO.EXTRACT_TREES_REGRESSOR,
# ModelsVO.KERNEL_RIDGE,
# ModelsVO.MLP_REGRESSOR,
# ModelsVO.ADA_BOOST_REGRESSOR,
# ModelsVO.BIGGINING_REGRESSOR,
# ModelsVO.GAUSSIAN_PROCESS_REGRESSOR,
# ModelsVO.RANSAC_REGRESSOR,
# ModelsVO.COSTUM_LSTM_MODEL,
                                
train_feature_map_custom = [
    { PDMappingVO.TRAIN_MODEL: [ModelsVO.XGB_CLASSIFIER]
      },
    {PDMappingVO.PLOT_FEATURE : True},
    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_HARMONEY_CHECK,
        PDMappingVO.GET_CLASSIFY: [-100,100],
        PDMappingVO.GET_SHIFT: [0],
        PDMappingVO.AS_TARGET : True,
      },

    { PDMappingVO.COLUMN_NAME: PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME,
    PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
    PDMappingVO.GET_SHIFT: [1,2,3,4],
     },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME,
    PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
        PDMappingVO.GET_SHIFT: [1,2,3,4],
        },

    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_HARMONEY_CHECK,
        PDMappingVO.GET_RATIO: [1,2,3,],
        PDMappingVO.GET_SHIFT: [1],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.DOLLAR_VALUE,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [1],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.INDEX_INDEX_VALUE,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [1],
      },


    { PDMappingVO.COLUMN_NAME: PDMappingVO.IPO_TICKET,
    PDMappingVO.KEEP_COLUMN : True
        },
]

test_feature_map_custom= [
    {PDMappingVO.TYPE : PDMappingVO.CLASSIFICATION},

    { PDMappingVO.COLUMN_NAME: PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME,
    PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
    PDMappingVO.GET_SHIFT: [1,2,3,4],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME,
    PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
        PDMappingVO.GET_SHIFT: [1,2,3,4],
        },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [0],
        PDMappingVO.AS_TARGET : True,
      },

    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
        PDMappingVO.GET_RATIO: [1,2,3],
        PDMappingVO.GET_SHIFT: [1],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.DOLLAR_VALUE,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [1],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.INDEX_INDEX_VALUE,
        PDMappingVO.GET_RATIO: [1],
        PDMappingVO.GET_SHIFT: [1],
      },


    { PDMappingVO.COLUMN_NAME: PDMappingVO.IPO_TICKET,
    PDMappingVO.KEEP_COLUMN : True
        },
]