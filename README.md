# specialLoanCheck
> 专项贷款数据与大集中系统数据核对。
以借据编号为链接键，按编号从个人贷款与单位贷款余额表中查询该笔贷款余额值,最后按多项标志进行分类汇总，方便统计工作人员进行数据核查。

# 使用指南
(一)使用源码
+ `pip install -r requirements.txt`
+ `python special_loan_check.py`
+  收集同月份该机构的存量专项贷款信息表，个人存量贷款余额表、单位存量贷款余额表，将他们放在项目同一个文件夹下
+ special_loan_check.py,等待程序自动处理。
+ 查看results.xlsx获取汇总报表
  
(二)使用打包exe程序
+ 收集同月份该机构的存量专项贷款信息表，个人存量贷款余额表、单位存量贷款余额表，将他们放在同一个文件夹下。（如：桌面\新建文件夹）
+ 将打包后的exe文件放入“桌面\新建文件夹”中，即四个文件在同一个文件夹内。
+ 双击special_loan_check.exe,等待程序自动处理。
+ 查看results.xlsx获取汇总报表

# 注意事项
1.部分机构存在专项贷款中的借据编号在个人贷款和单位贷款中查找不到的情况，此时程序将此类情况“贷款余额"字段设置为0。请注意余额为0的贷款。
2.该工作仅用作第二辅助作用，不能作为核查唯一参考。作者对稳定性和准确性不作保证，请斟酌使用。