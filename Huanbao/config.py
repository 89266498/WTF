tables = {'PARA': 'UNITID',
          'PARA1': 'UNITID',
          'PARA2': 'UNITID',
          'PARA3': 'UNITID',
          'T_BASE_ORG': 'T_ORGID',
          'T_BASE_PDI': 'ITEMID',
          'T_BASE_REALTIMEPOINT': 'UNITID',
          'T_BASE_STAT_PARA': 'REMARK',
          'T_BASE_STAT_PARA1': 'REMARK',
          'T_BASE_STAT_PARA2': 'REMARK',
          'T_BASE_STAT_PARA3': 'REMARK',
          'T_BASE_STAT_PARA4': 'REMARK',
          'T_BASE_STAT_PARA5': 'REMARK',
          'T_BASE_UNIT': 'UNITID',
          'T_BASE_WATCHPARA_CX': 'T_ORGID',
          'T_BASE_WATCHPARA_NVNC': 'T_ORGID',
          'T_BASE_WATCHPARA_NVNC_FCEMS': 'T_ORGID',
          'T_BASE_WATCHPARA_NVNC_SO2NOX': 'T_ORGID',
          'T_BASE_WATCHPARA_NVNC_YCO2': 'T_ORGID',
          'T_BASE_WATCHPARA_TY': 'T_ORGID',
          }


def getsqlcmds(sourceunit):
    cmds = {}
    for key, value in tables.items():
        cmds[key] = r"select * from administrator.{0} where {1}='{2}'".format(key, value, sourceunit)
    return cmds
