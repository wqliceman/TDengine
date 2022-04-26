

from util.dnodes import *
from util.log import *
from util.sql import *
from util.cases import *


class TDTestCase:

    def init(self, conn, logSql):
        tdLog.debug(f"start to excute {__file__}")
        tdSql.init(conn.cursor())

    def run(self):  # sourcery skip: extract-duplicate-method
        # for func now() , today(), timezone()
        tdSql.prepare()
        today_date = datetime.datetime.strptime(
            datetime.datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")

        tdLog.printNoPrefix("==========step1:create tables==========")
        tdSql.execute(
            '''create table if not exists ntb
            (ts timestamp, c1 int, c2 float,c3 double,c4 timestamp)
            '''
        )
        tdSql.execute(
            '''create table if not exists stb
            (ts timestamp, c1 int, c2 float,c3 double,c4 timestamp) tags(t0 int)
            '''
        )
        tdSql.execute(
            '''create table if not exists stb_1 using stb tags(100)
            '''
        )
        tdLog.printNoPrefix("==========step2:insert data into ntb==========")
        tdSql.execute(
            'insert into ntb values(now,1,1.55,100.555555,today())("2020-1-1 00:00:00",10,11.11,99.999999,now())(today(),3,3.333,333.333333,now())')
        tdSql.execute(
            'insert into stb_1 values(now,1,1.55,100.555555,today())("2020-1-1 00:00:00",10,11.11,99.999999,now())(today(),3,3.333,333.333333,now())')
        tdLog.printNoPrefix("==========step2:query test of ntb ==========")

        # test function now()
        # ntable
        tdSql.query("select now() from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1w from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1w from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1d from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1d from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1h from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1h from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1m from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1m from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1s from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1s from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1a from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1a from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1u from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1u from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1b from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1b from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1w from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1w from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1d from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1d from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1h from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1h from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1m from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1m from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1s from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1s from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1a from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1a from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1u from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1u from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1b from ntb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1b from db.ntb")
        tdSql.checkRows(3)
        tdSql.query("select * from ntb where ts<now()")
        tdSql.checkRows(3)
        tdSql.checkData(1, 1, 3)
        tdSql.query("select * from ntb where ts<=now()")
        tdSql.checkRows(3)
        tdSql.checkData(2, 1, 1)
        tdSql.query("select c1 from ntb where ts=now()")
        tdSql.checkRows(0)
        tdSql.query("select * from ntb where ts>=now()")
        tdSql.checkRows(0)
        tdSql.query("select * from ntb where ts>now()")
        tdSql.checkRows(0)
        tdSql.query("select now() from ntb where ts=today()")
        tdSql.checkRows(1)

        # stable
        tdSql.query("select now() from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1w from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1w from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1d from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1d from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1h from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1h from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1m from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1m from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1s from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1s from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1a from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1a from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1u from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1u from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1b from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() +1b from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1w from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1w from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1d from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1d from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1h from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1h from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1m from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1m from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1s from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1s from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1a from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1a from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1u from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1u from db.stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1b from stb")
        tdSql.checkRows(3)
        tdSql.query("select now() -1b from db.stb")
        tdSql.checkRows(3)
        # tdSql.query("select * from stb where ts<now()")
        # tdSql.checkRows(3)
        # tdSql.checkData(1,1,3)
        # tdSql.query("select * from stb where ts<=now()")
        # tdSql.checkRows(3)
        # tdSql.checkData(2,1,1)
        tdSql.query("select c1 from stb where ts=now()")
        tdSql.checkRows(0)
        # tdSql.query("select * from stb where ts>=now()")
        # tdSql.checkRows(0)
        # tdSql.query("select * from stb where ts>now()")
        # tdSql.checkRows(0)
        tdSql.query("select now() from stb where ts=today()")
        tdSql.checkRows(1)

        # table
        tdSql.query("select now() from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1w from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1w from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1d from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1d from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1h from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1h from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1m from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1m from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1s from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1s from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1a from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1a from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1u from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1u from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1b from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() +1b from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1w from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1w from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1d from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1d from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1h from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1h from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1m from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1m from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1s from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1s from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1a from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1a from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1u from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1u from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1b from stb_1")
        tdSql.checkRows(3)
        tdSql.query("select now() -1b from db.stb_1")
        tdSql.checkRows(3)
        tdSql.query("select * from stb_1 where ts<now()")
        tdSql.checkRows(3)
        tdSql.checkData(1, 1, 3)
        tdSql.query("select * from stb_1 where ts<=now()")
        tdSql.checkRows(3)
        tdSql.checkData(2, 1, 1)
        tdSql.query("select c1 from stb_1 where ts=now()")
        tdSql.checkRows(0)
        tdSql.query("select * from stb_1 where ts>=now()")
        tdSql.checkRows(0)
        tdSql.query("select * from stb_1 where ts>now()")
        tdSql.checkRows(0)

        # tdSql.query("select * from stb_1 where ts<now")
        # tdSql.checkRows(3)
        # tdSql.checkData(1, 1, 3)
        # tdSql.query("select * from stb_1 where ts<=now")
        # tdSql.checkRows(3)
        # tdSql.checkData(2, 1, 1)
        # tdSql.query("select c1 from stb_1 where ts=now")
        # tdSql.checkRows(0)
        # tdSql.query("select * from stb_1 where ts>=now")
        # tdSql.checkRows(0)
        # tdSql.query("select * from stb_1 where ts>now")
        # tdSql.checkRows(0)
        
        tdSql.query("select now() from stb_1 where ts=today()")
        tdSql.checkRows(1)

    def stop(self):
        tdSql.close()
        tdLog.success(f"{__file__} successfully executed")


tdCases.addLinux(__file__, TDTestCase())
tdCases.addWindows(__file__, TDTestCase())
