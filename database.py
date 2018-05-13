# -*- coding: utf-8 -*-

import tushare as ts
import pymysql as mysql
import numpy
import os
import sys
import datetime
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

__host__ = 'localhost'
__user__ = 'root'
__password__ = 'kl345'
__database__ = 'stock'
__charset__ = 'utf8'

class Database():
    def __init__(self, log = None):
        self.db = mysql.connect(host = __host__, user = __user__, password = __password__, database = __database__, charset = __charset__)
        self.cursor = self.db.cursor()
        if log:
            if os.path.exists(log):
                os.remove(log)
            self.log = open(log,  'a')
        else:
            self.log = sys.stdout

        self.debug_files = {'stock':'stock.dbg', 'trade':'trade.dbg', 'company':'company.dbg'}
        self.debug_en = False

    def update(self):
        logs = [item for item in self.debug_files.values()]
        for log in logs:
            if os.path.exists(log):
                os.remove(log)

        self._check_table_stock()
        self._check_table_trade()
        self._check_table_company()

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def _check_table_stock(self):
        try:
            df = ts.get_stock_basics()
        except Exception as e:
            print('[ERR]:', e, file = self.log) 
            print('[ERR]: get_stock_basics fail.' % e, file = self.log) 
            quit()

        if df.empty:
            print('[ERR]: get_stock_basics is empty', file = self.log)
            quit()

        def dict_fix(idx):
            ret = df.ix[idx].to_dict()
            ret['code'] = idx
            return ret
        dict_list = [dict_fix(idx) for idx in df.index]

        self.cursor.execute('delete from stock;')
        self._insert_into_table('stock', dict_list)

    def _check_table_trade(self):
        code_list = [item[0] for item in self.execute('select code from stock;')]
        idx_offset = self.execute('select max(id) from trade;')[0][0]
        idx_offset = idx_offset + 1 if idx_offset else 0

        for code in code_list:
            last_date = self.execute('select max(date) from trade where code = %s;' % code)[0][0]
            if last_date:
                start_date = str(last_date + datetime.timedelta(days = 1))
            else:
                start_date = ''

            try:
                df = ts.get_k_data(code, start = start_date, ktype = 'W')
            except Exception as e:
                print('[ERR]:', e, file = self.log)
                print('[ERR]: get_k_data for %s fail' % code, file = self.log)
                quit()
            
            if df.empty:
                print('[WARING]: %s k_data is empty' % code, file = self.log)
                continue

            index_base = df.index[0]
            def dict_fix(index, offset):
                ret = df.ix[index].to_dict()
                ret['id'] = index- index_base + offset
                return ret
            dict_list = [dict_fix(index, idx_offset) for index in df.index]
            ret = self._insert_into_table('trade', dict_list)
            idx_offset += ret 

            print('[trade]: insert %d records for code %s from date %s' % (ret, code, start_date))

    def _check_table_company(self):
        last_year = self.execute('select max(year) from company;')[0][0]
        if last_year:
            last_quarter = self.execute('select max(quarter) from company where year = %s;' % last_year)[0][0]
            if last_quarter == 4:
                start_year = last_year + 1
                start_quarter = 1
            else:
                start_year = last_year
                start_quarter = last_quarter + 1
        else:
            start_year = 2002
            start_quarter = 1

        idx_offset = self.execute('select max(id) from company;')[0][0]
        idx_offset = idx_offset + 1 if idx_offset else 0

        for year in range(start_year, 2019):
            for quarter in range(start_quarter,5):
                try:
                    df_report = ts.get_report_data(year, quarter)
                    df_profit = ts.get_profit_data(year, quarter)
                    df_growth = ts.get_growth_data(year, quarter)
                    df_debt = ts.get_debtpaying_data(year, quarter)
                except Exception as e:
                    print('[ERR]:', e, file = self.log)
                    print('[ERR]: get company infor at (%d,%d) fail\n' % (year, quarter), file = self.log)
                    quit()

                dicts = []
                for idx in df_report.index:
                    def df2dict(df, code):
                        row = df[df.code == code]
                        if not row.empty:
                            return row.ix[row.index.tolist()[0]].to_dict()
                        else:
                            return {}.fromkeys(list(row.columns))

                    code = df_report.ix[idx].code
                    dic_report = df2dict(df_report, code)
                    dic_profit = df2dict(df_profit, code)
                    dic_growth = df2dict(df_growth, code)
                    dic_debt = df2dict(df_debt, code)
                    
                    dic = {}
                    dic.update(dic_report)
                    dic.update(dic_profit)
                    dic.update(dic_growth)
                    dic.update(dic_debt)
                    dic['id'] = idx + idx_offset
                    dic['code'] = code
                    dic['year'] = year
                    dic['quarter'] = quarter
                    dic['report_date'] = '%s-%s' % (year, dic['report_date'] if dic['report_date'] != '02-29' else '02-28')
                    dic['eps'] = dic_profit['eps'] if isinstance(dic_profit['eps'], float) and not numpy.isnan(dic_profit['eps']) else dic_report['eps']
                    dic['roe'] = dic_profit['roe'] if isinstance(dic_profit['roe'], float) and not numpy.isnan(dic_profit['roe']) else dic_report['roe']
                    dic['net_profits'] = dic_profit['net_profits'] if isinstance(dic_profit['net_profits'], float) and not numpy.isnan(dic_profit['net_profits']) else dic_report['net_profits']

                    for k, v in dic.items():
                        if isinstance(v, float) and numpy.isnan(v):
                            dic[k] = None

                    dicts.append(dic)
                ret = self._insert_into_table('company', dicts)
                idx_offset += ret
                print('\n[company]: insert %d records for year %d quarter %d' % (ret, year, quarter))

    def _insert_into_table(self, name, dicts):
        '''
        name, table name.
        dicts, dict list to insert. TODO: better to be a generator.
        '''
        columns_group = self.execute('desc %s;' % name)
        fmt_proc = lambda x, y: '\'%%(%s)s\'' % x if y.startswith('varchar') or y == 'date' else '%%(%s)s' % x
        values_fmt = '(%s)' % ', '.join(fmt_proc(item[0], item[1]) for item in columns_group)
        values_list = ', '.join(values_fmt % item for item in dicts).replace('None', 'null')

        if self.debug_en:
            with open(self.debug_files[name], 'w') as fp:
                print('\n\n\n\n##### _insert_into_table(%s): %d records ######\n' % (name, len(dicts)), 
                        '\n##dicts##\n', dicts, 
                        '\n##values_list##\n', values_list, 
                        file = fp)
        try:
            self.cursor.execute('insert into %s values %s;' % (name, values_list))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print('[ERR]:', e)
            print('[ERR]: _insert_into_table %s fail\n' % name)
            quit()
        else:
            return len(dicts)
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('[ERR]:', exc_type, exc_value)

        self.db.close()
        if self.log is not sys.stdout:
            self.log.close()

        return False
