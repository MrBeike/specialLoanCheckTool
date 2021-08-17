#coding:utf-8

import os
import pandas as pd


def getData(filename:str,getAll:bool=False,columns:list=[],names:list=[])->pd.DataFrame:
    df_origin = pd.read_csv(filename,sep="|",header=None,encoding="utf-8")
    if not getAll:
        df_acquire = df_origin[columns]
        df_acquire.columns=names
    else:
        df_acquire = df_origin
    df = df_acquire.fillna(0)
    return df

def getFile():
    current_path = os.getcwd()
    file_type = {}
    all_files = [f for f in os.listdir(current_path) if f.endswith('dat')]
    for file in all_files:
        type = file.split("_")[1]
        file_type.update({type:file})
    danwei = file_type.get('CLDWDK')
    geren  = file_type.get('CLGRDK')
    zhuanxiang = file_type.get('CLZXDK')
    msg = f'单位贷款文件：{danwei}\n个人贷款文件：{geren}\n专项贷款文件：{zhuanxiang}'
    msg = msg.replace("None",'未找到文件')
    print(msg)
    if not(danwei and geren and zhuanxiang):
        print("缺失报文,请查看上面的文件检查信息")
        _ = input("——————————————————————————")
        return False
    return (danwei,geren,zhuanxiang)

if __name__ == '__main__':
    # danwei = input("请输入单位贷款余额报文路径：")
    # geren = input("请输入个人贷款余额报文路径：")
    # zhuanxiang = input("请输入专项贷款余额报文路径：")
    print("##本程序仅用于专项贷款金数报文与大集中数据核查##")
    print("##本程序不会检查报文的时间及内容的正确性，请自行检查##")
    try:
        danwei,geren,zhuanxiang = getFile()
        df_danwei = getData(filename=danwei,columns =[10,18],names=["贷款借据编码","贷款金额"])
        df_geren = getData(filename=geren,columns=[6,13],names=["贷款借据编码","贷款金额"])
        df_zhuanxiang = getData(filename=zhuanxiang,getAll=True)
        df_sum = df_danwei.append(df_geren,ignore_index=True)
        df_zhuanxiang.columns = ["金融机构代码","内部机构号","贷款合同编码","贷款借据编码","是否个体工商户贷款","是否小微企业主贷款","是否涉农贷款","涉农贷款类型","是否精准扶贫贷款","是否建档立卡贫困人口贷款","是否地方政府融资平台贷款","地方融资平台按法律性质分类类型","地方融资平台按隶属关系分类类型","地方融资平台偿债资金来源分类","是否保障性安居工程贷款","保障性安居工程贷款类型","是否绿色贷款","是否创业担保贷款","创业担保贷款类型"]
        df_combine = df_zhuanxiang.merge(df_sum,how='left',on='贷款借据编码')
        df_result = df_combine.drop(["金融机构代码","内部机构号","贷款合同编码","贷款借据编码"],axis=1)
        df = df_result.groupby(["是否个体工商户贷款","是否小微企业主贷款","是否涉农贷款","涉农贷款类型","是否精准扶贫贷款","是否建档立卡贫困人口贷款","是否地方政府融资平台贷款","地方融资平台按法律性质分类类型","地方融资平台按隶属关系分类类型","地方融资平台偿债资金来源分类","是否保障性安居工程贷款","保障性安居工程贷款类型","是否绿色贷款","是否创业担保贷款","创业担保贷款类型"
    ]).sum()
        df.to_excel('result.xlsx')
    except Exception as e:
        print("出错了。GG:",e)