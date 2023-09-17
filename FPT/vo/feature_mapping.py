from FPT.vo.pd_mapping_vo import PDMappingVO
from FPT.vo.models_vo import ModelsVO

# feature_map = [
#     { PDMappingVO.TRAIN_MODEL: ModelsVO.LINEAR_RGRESSION
#       },
#     { PDMappingVO.INCREASE_FACTOR: 1
#       },
#     { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
#         PDMappingVO.GET_RATIO: [1],
#         PDMappingVO.GET_SHIFT: [0],
#         PDMappingVO.AS_TARGET : True,
#       },

#     { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
#         PDMappingVO.GET_RATIO: [1],
#         PDMappingVO.GET_SHIFT: [1,2,3],
#       },
#     { PDMappingVO.COLUMN_NAME: PDMappingVO.DOLLAR_VALUE,
#         PDMappingVO.GET_RATIO: [1],
#         PDMappingVO.GET_SHIFT: [1],
#       },
#     { PDMappingVO.COLUMN_NAME: PDMappingVO.INDEX_INDEX_VALUE,
#         PDMappingVO.GET_RATIO: [1],
#         PDMappingVO.GET_SHIFT: [1],
#       },
#     { PDMappingVO.COLUMN_NAME: PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME,
#         PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
#         PDMappingVO.GET_SHIFT: [1],
#       },
#     { PDMappingVO.COLUMN_NAME: PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME,
#     PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
#         PDMappingVO.GET_SHIFT: [1],
#         },

#     { PDMappingVO.COLUMN_NAME: PDMappingVO.IPO_TICKET,
#     PDMappingVO.KEEP_COLUMN : True
#         },
# ]



feature_map = [
    { PDMappingVO.TRAIN_MODEL: ModelsVO.LINEAR_RGRESSION
      },
    { PDMappingVO.INCREASE_FACTOR: 1
      },
    { PDMappingVO.PLOT_FEATURE: True
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
        PDMappingVO.GET_STANDARD: True,
        PDMappingVO.AS_TARGET : True,
        PDMappingVO.GET_SHIFT: [0],
      },

    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
     PDMappingVO.GET_STANDARD: True,
        PDMappingVO.GET_SHIFT: [1,2,3],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.DOLLAR_VALUE,
        PDMappingVO.GET_STANDARD: True,
        PDMappingVO.GET_SHIFT: [1,2,3],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.INDEX_INDEX_VALUE,
       PDMappingVO.GET_STANDARD: True,
       PDMappingVO.GET_SHIFT: [1,2,3],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME,
        PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
        PDMappingVO.GET_SHIFT: [1,2,3],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME,
        PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME],
        PDMappingVO.GET_SHIFT: [1,2,3],
        },

    { PDMappingVO.COLUMN_NAME: PDMappingVO.IPO_TICKET,
    PDMappingVO.KEEP_COLUMN : True
        },
]