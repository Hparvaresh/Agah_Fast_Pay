from FPT.vo.pd_mapping_vo import PDMappingVO

# feature_map = [
#     { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
#         PDMappingVO.GET_RATIO: [1],
#         PDMappingVO.AS_TARGET : True,
#       },

#     { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
#         PDMappingVO.GET_RATIO: [2,3,4],
#       },
#     { PDMappingVO.COLUMN_NAME: PDMappingVO.DOLLAR_VALUE,
#         PDMappingVO.GET_RATIO: [1]
#       },
#     { PDMappingVO.COLUMN_NAME: PDMappingVO.INDEX_INDEX_VALUE,
#         PDMappingVO.GET_RATIO: [1]
#       },
#     { PDMappingVO.COLUMN_NAME: PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME,
#         PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME]
#       },
#     { PDMappingVO.COLUMN_NAME: PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME,
#     PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME]
#         },

#     { PDMappingVO.COLUMN_NAME: PDMappingVO.IPO_TICKET,
#     PDMappingVO.KEEP_COLUMN : True
#         },
# ]



feature_map = [
    { PDMappingVO.TRAIN_MODEL: PDMappingVO.SVR
      },
    { PDMappingVO.INCREASE_FACTOR: 1.7
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
        PDMappingVO.GET_STANDARD: True,
        PDMappingVO.AS_TARGET : True,
      },

    { PDMappingVO.COLUMN_NAME: PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
        PDMappingVO.GET_RATIO: [2,3,4],
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.DOLLAR_VALUE,
        PDMappingVO.GET_STANDARD: True,
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.INDEX_INDEX_VALUE,
       PDMappingVO.GET_STANDARD: True,
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME,
        PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME]
      },
    { PDMappingVO.COLUMN_NAME: PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME,
    PDMappingVO.GET_DIVIDE: [PDMappingVO.BALANCE_MONEY_OUTPUT_NAME]
        },

    { PDMappingVO.COLUMN_NAME: PDMappingVO.IPO_TICKET,
    PDMappingVO.KEEP_COLUMN : True
        },
]