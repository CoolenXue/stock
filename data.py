# -*- coding: utf-8 -*-

import tushare as ts
import pymysql as mysql

# DateFrame:
#       index 	The index (row labels) of the DataFrame.
#       columns	The column labels of the DataFrame.
#       size 	Return an int representing the number of elements in this object.
#       dtypes 	Return the dtypes in the DataFrame.
#       shape 	Return a tuple representing the dimensionality of the DataFrame.
#       empty 	Indicator whether DataFrame is empty.
#
#       ix 	    A primarily label-location based indexer, with integer position fallback.
#       loc 	Access a group of rows and columns by label(s) or a boolean array.
#       iloc 	Purely integer-location based indexing for selection by position.
#
#       at 	    Access a single value for a row/column label pair.
#       iat 	Access a single value for a row/column pair by integer position.
#       values 	Return a Numpy representation of the DataFrame.
#
#       axes 	Return a list representing the axes of the DataFrame.
#       blocks 	Internal property, property synonym for as_blocks()
#       ftypes 	Return the ftypes (indication of sparse/dense and dtype) in DataFrame.
#       ndim 	Return an int representing the number of axes / array dimensions.
#       style 	Property returning a Styler object containing methods for building a styled HTML representation fo the DataFrame.
#
# df[0:2]; df['300152':'300698']    # slice by row
# df['pe']; df.pe; df[['pe']];  df[['pe', 'pb']]    # slice by column
# df.ix['300152':'300698', ['pe', 'totals', 'eps', 'pb']]   #slice by row/column
# df.ix[0:3, ['pe', 'totals', 'eps', 'pb']]
# df.at['300152', 'pe']     #uniq value
# df[df.date < '2018-04-13']; df[df.date < '2018-04-13', 'close']   # select

# get_k_data(
#       code = None,               # string
#       start ='' ,                # 'YYYY-MM-DD', 默认为上市日期
#       end = '',                  # 'YYYY-MM-DD', 默认为上一交易日
#       ktype = 'D',               # D(day), W(week) , M(month), 5, 15, 30, 60
#       autype = 'qfq',            # qfq, hfq, None
#       index = False, 
#       retry_count = 3, 
#       pause = 0.001,
# )
# return:   <date>  <open>  <close> <high>  <low>   <volumn>  <amount(成交额)> <turnoverratio(换手率)>

# get_stock_basics(
#       date = None,               # 'YYYY-MM-DD' only after 2016-8-9
# )
# return:   <name>  <industry>  <area>  <pe(市盈率)>    <outstanding(流通股本)>     <totals(总股本(万)>     <totalAssets(总资产)>   <liquidAssets(流动资产)> 
#           <fixedAssets(固定资产)>     <reserved(公积金)> <reservedPerShare> <eps(每股收益)> <bvps(每股净资产)> <pb(市净率)> <timeToMarket(上市日期)>

# get_report_data(
#       year,                      # int (2018)
#       quarter,                   # int (1,2,3,4)
# )
# return:   <code>  <name>  <eps(每股收益)>   <eps_yoy(每股收益同比%)>  <bvps(每股净资产)>  <roe(净资产收益率%)>    <epcf(每股现金流量)>    <net_profits(净利润)>
#           <profits_yoy(净利润同比)>   <distrib(分配方案)>     <report_date（发布日期)>

# get_profit_data(
#       year,                      # int (2018)
#       quarter,                   # int (1,2,3,4)
# )
# return:   <code>  <name>  <roe(净资产收益率%)>  <net_profits_ratio(净利率%)>  <gross_profit_ratio(毛利率%)>
#           <net_profits(净利润)>  <eps(每股收益)>  <business_income(营业收入(百万元))>  <bips（每股主营业务收入(元))>

# get_operation_data(
#       year,                      # int (2018)
#       quarter,                   # int (1,2,3,4)
# )
# return:   <code>  <name> <arturnover(应收账款周转率(次))> <arturndays(应收账款周转天数(天))>  <inventory_turnover(存货周转率(次))>    <inventory_days(存货周转天数(天))>  <currentasset_turnover(流动资产周转率(次))> <currentasset_days（流动资产周转天数(天))>

# get_growth_data(
#       year,                      # int (2018)
#       quarter,                   # int (1,2,3,4)
# )
# return:   <code>  <name> <mbrg(主营业务收入增长率%)>  <nprg(净利润增长率%)>   <nav（净资产增长率)>   <targ(总资产增长率)>
#           <epsg(每股收益增长率)>  <seg股东权益增长率>

# get_debtpaying_data(
#       year,                      # int (2018)
#       quarter,                   # int (1,2,3,4)
# )
# return:   <code>  <name> <currentratio(流动比率)> <quickratio(速动比率)>  <cashratio（现金比率)>  <icratio(利息支付倍数)>
#            <sheqratio(股东权益比率)>   <adratio(股东权益增长率)>

# get_cashflow_data(
#       year,                      # int (2018)
#       quarter,                   # int (1,2,3,4)
# )
# return:   <code>  <name> <cf_sales(经营现金净流量对销售收入比率)> <rateofreturn(资产的经营现金流量回报率)>   
#           <cf_nm(经营现金净流量与净利润的比率)>   <cf_liabilities(经营现金净流量对负债比率)>  <cashflowratio（现金流量比率)>

#df = ts.get_k_data(code = '603337', start = '2013-1-1', ktype = 'M')
#df = ts.get_stock_basics(2018-04-12)
#df = ts.get_report_data(2017, 4)
#df = ts.get_profit_data(2017, 4)
#df = ts.get_operation_data(2017, 4)
#df = ts.get_growth_data(2017, 4)
#df = ts.get_debtpaying_data(2017, 4)
#df = ts.get_cashflow_data(2017, 4)

def type_convert(obj, len = 0):
    type_dict = {'object':'VARCHAR(%d)', 'float64':'FLOAT', 'int64':'INT'}
    if obj not in type_dict:
        return 'NULL'
    if obj == 'object':
        return type_dict[obj] % len
    else:
        return type_dict[obj]

def sql_create_table(db, name, data_frame):
    database = db.cursor()

    # create table
    key = data_frame.index.name
    key_type = type_convert(data_frame.index.dtype.name, 16)
    column_list = '\t\n'.join('%s %s,' % (col, type_convert(data_frame.dtypes.to_dict()[col].name, 16)) for col in data_frame.columns)

    sql = '''
CREATE TABLE IF NOT EXISTS %s(
    %s %s NOT NULL,
    %s 
    PRIMARY KEY (%s)
);'''   % (name, key, key_type, column_list, key)

    database.execute(sql)

    # insert data_frame
    value_str = lambda x, dtype: str(x) if dtype != 'object' else "'" + str(x) + "'"
    value_list = []
    count = 0
    for idx in data_frame.index:
        #if count > 2:
        #    break
        count += 1
        value = '(' + value_str(idx, data_frame.index.dtype.name)
        for col in data_frame.columns:
            value += ', ' + value_str(data_frame.ix[idx].to_dict()[col], data_frame.dtypes.to_dict()[col].name)
        value += ') '
        value_list.append(value)
        print('%d\n' % count)
    values = ','.join(value_list)

    sql = '''
INSERT INTO %s
VALUES %s;
''' % (name, values)

    #with open('D:\\log.txt', 'w') as log:
    #    log.write(sql)

    database.execute(sql)
    db.commit()

df = ts.get_stock_basics()

db = mysql.connect(host = 'localhost', user = 'root', password = 'kl345', database = 'stock', charset = 'utf8')
sql_create_table(db, 'basic', df)
db.close()

#print(cursor.fetchall())
__host__ = 'localhost'
__user__ = 'root'
__password__ = 'kl345'
__database__ = 'stock'
__charset__ = 'utf8'

class Database():
    def __init__(self):
        self.db = mysql.connect(host = __host__, user = __user__, password = __password__, database = __database__, charset = __charset__)
        self.cursor = self.db.cursor()

    key = data_frame.index.name
    key_type = type_convert(data_frame.index.dtype.name, 16)
    column_list = '\t\n'.join('%s %s,' % (col, type_convert(data_frame.dtypes.to_dict()[col].name, 16)) for col in data_frame.columns)

    sql = '''
CREATE TABLE IF NOT EXISTS %s(
    %s %s NOT NULL,
    %s 
    PRIMARY KEY (%s)
);'''   % (name, key, key_type, column_list, key)
    def update(self):
        pass

    def select(self, sql):
        pass
    
    def _check_table_stock(self):
        columns = []
        df = ts.get_stock_basics())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('[ERR]:', exc_type, exc_value, traceback)
        self.db.close()
        return False