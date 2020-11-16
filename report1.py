import pymysql
import sys, datetime
from PyQt5.QtWidgets import *
import csv
import json
import xml.etree.ElementTree as ET

class DB_Utils:

    def queryExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db=db, charset='utf8')

        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:  # dictionary based cursor
                cursor.execute(sql, params)
                tuples = cursor.fetchall()
                return tuples
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

class DB_Queries:
    def selectAllPlayer(self):
        sql = "SELECT * FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerTeamid(self):
        sql = "SELECT DISTINCT team_id FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerNation(self):
        sql = "SELECT DISTINCT nation FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerHeight(self):
        sql = "SELECT DISTINCT height FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerWeight(self):
        sql = "SELECT DISTINCT weight FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayer(self, teamid, position, nation, height, heightcheck, weight, weightcheck):
        if teamid == '사용안함' and position == '사용안함' and nation == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player"
            params = ()
        elif teamid == '사용안함' and position == '사용안함' and nation == '대한민국' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE nation IS NULL"
            params = ()
        elif teamid == '사용안함' and position == '미정' and nation == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE position IS NULL"
            params = ()
        elif teamid == '사용안함' and position == '미정' and nation == '대한민국' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE nation IS NULL AND position IS NULL"
            params = ()
        elif teamid == '사용안함' and position == '사용안함' and nation == '사용안함' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE weight >= %s"
                params = (weight)
            else:
                sql = "SELECT * FROM player WHERE weight <= %s"
                params = (weight)
        elif teamid == '사용안함' and position == '사용안함' and nation == '대한민국' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE nation IS NULL AND weight >= %s"
                params = (weight)
            else:
                sql = "SELECT * FROM player WHERE nation IS NULL AND weight <= %s"
                params = (weight)
        elif teamid == '사용안함' and position == '미정' and nation == '사용안함' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position IS NULL AND weight >= %s"
                params = (weight)
            else:
                sql = "SELECT * FROM player WHERE position IS NULL AND weight <= %s"
                params = (weight)
        elif teamid == '사용안함' and position == '미정' and nation == '대한민국' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND weight >= %s"
                params = (weight)
            else:
                sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND weight <= %s"
                params = (weight)
        elif teamid == '사용안함' and position == '사용안함' and nation == '사용안함' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE height >= %s"
                params = (height)
            else:
                sql = "SELECT * FROM player WHERE height <= %s"
                params = (height)
        elif teamid == '사용안함' and position == '사용안함' and nation == '대한민국' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE nation IS NULL AND height >= %s"
                params = (height)
            else:
                sql = "SELECT * FROM player WHERE nation IS NULL AND height <= %s"
                params = (height)
        elif teamid == '사용안함' and position == '미정' and nation == '사용안함' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE position IS NULL AND height >= %s"
                params = (height)
            else:
                sql = "SELECT * FROM player WHERE position IS NULL AND height <= %s"
                params = (height)
        elif teamid == '사용안함' and position == '미정' and nation == '대한민국' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height >= %s"
                params = (height)
            else:
                sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height <= %s"
                params = (height)
        elif teamid == '사용안함' and position == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE nation = %s"
            params = (nation)
        elif teamid == '사용안함' and position == '미정' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s"
            params = (nation)
        elif teamid == '사용안함' and nation == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE position = %s"
            params = (position)
        elif teamid == '사용안함' and nation == '대한민국' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL"
            params = (position)
        elif position == '사용안함' and nation == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s"
            params = (teamid)
        elif position == '사용안함' and nation == '대한민국' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL"
            params = (teamid)
        elif position == '미정' and nation == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL"
            params = (teamid)
        elif position == '미정' and nation == '대한민국' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL"
            params = (teamid)
        elif teamid == '사용안함' and position == '사용안함' and nation == '사용안함':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE height >= %s AND weight >= %s"
                params = (height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE height >= %s AND weight <= %s"
                params = (height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE height <= %s AND weight >= %s"
                params = (height, weight)
            else:
                sql = "SELECT * FROM player WHERE height <= %s AND weight <= %s"
                params = (height, weight)
        elif teamid == '사용안함' and position == '미정' and nation == '사용안함':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position IS NULL AND height >= %s AND weight >= %s"
                params = (height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE position IS NULL AND height >= %s AND weight <= %s"
                params = (height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position IS NULL AND height <= %s AND weight >= %s"
                params = (height, weight)
            else:
                sql = "SELECT * FROM player WHERE position IS NULL AND height <= %s AND weight <= %s"
                params = (height, weight)
        elif teamid == '사용안함' and position == '사용안함' and nation == '대한민국':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE nation IS NULL AND height >= %s AND weight >= %s"
                params = (height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE nation IS NULL AND height >= %d AND weight <= %d"
                params = (height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE nation IS NULL AND height <= %s AND weight >= %s"
                params = (height, weight)
            else:
                sql = "SELECT * FROM player WHERE nation IS NULL AND height <= %s AND weight <= %s"
                params = (height, weight)
        elif teamid == '사용안함' and position == '미정' and nation == '대한민국':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height >= %s AND weight >= %s"
                params = (height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height >= %s AND weight <= %s"
                params = (height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height <= %s AND weight >= %s"
                params = (height, weight)
            else:
                sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height <= %s AND weight <= %s"
                params = (height, weight)
        elif teamid == '사용안함' and position == '사용안함' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE nation = %s AND weight >= %s"
                params = (nation, weight)
            else:
                sql = "SELECT * FROM player WHERE nation = %s AND weight <= %s"
                params = (nation, weight)
        elif teamid == '사용안함' and position == '미정' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND weight >= %s"
                params = (nation, weight)
            else:
                sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND weight <= %s"
                params = (nation, weight)
        elif teamid == '사용안함' and position == '사용안함' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE nation = %s AND height >= %s"
                params = (nation, height)
            else:
                sql = "SELECT * FROM player WHERE nation = %s AND height <= %s"
                params = (nation, height)
        elif teamid == '사용안함' and position == '미정' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height >= %s"
                params = (nation, height)
            else:
                sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height <= %s"
                params = (nation, height)
        elif teamid == '사용안함' and nation == '사용안함' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND weight >= %s"
                params = (position, weight)
            else:
                sql = "SELECT * FROM player WHERE position = %s AND weight <= %s"
                params = (position, weight)
        elif teamid == '사용안함' and nation == '대한민국' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL AND weight >= %s"
                params = (position, weight)
            else:
                sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL AND weight <= %s"
                params = (position, weight)
        elif teamid == '사용안함' and nation == '사용안함' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND height >= %s"
                params = (position, height)
            else:
                sql = "SELECT * FROM player WHERE position = %s AND height <= %s"
                params = (position, height)
        elif teamid == '사용안함' and nation == '대한민국' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL AND height >= %s"
                params = (position, height)
            else:
                sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL AND height <= %s"
                params = (position, height)
        elif position == '사용안함' and nation == '사용안함' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND weight >= %s"
                params = (teamid, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND weight <= %s"
                params = (teamid, weight)
        elif position == '미정' and nation == '사용안함' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND weight >= %s"
                params = (teamid, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND weight <= %s"
                params = (teamid, weight)
        elif position == '사용안함' and nation == '대한민국' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL AND weight >= %s"
                params = (teamid, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL AND weight <= %s"
                params = (teamid, weight)
        elif position == '미정' and nation == '대한민국' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND weight >= %s"
                params = (teamid, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND weight <= %s"
                params = (teamid, weight)
        elif position == '사용안함' and nation == '사용안함' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND height >= %s"
                params = (teamid, height)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND height <= %s"
                params = (teamid, height)
        elif position == '미정' and nation == '사용안함' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND height >= %s"
                params = (teamid, height)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND height <= %s"
                params = (teamid, height)
        elif position == '사용안함' and nation == '대한민국' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL AND height >= %s"
                params = (teamid, height)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL AND height <= %s"
                params = (teamid, height)
        elif position == '미정' and nation == '대한민국' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height >= %s"
                params = (teamid, height)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height <= %s"
                params = (teamid, height)
        elif position == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s"
            params = (teamid, nation)
        elif position == '미정' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s"
            params = (teamid, nation)
        elif nation == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s"
            params = (teamid, position)
        elif nation == '대한민국' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation IS NULL"
            params = (teamid, position)
        elif teamid == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE position = %s AND nation = %s"
            params = (position, nation)
        elif teamid == '사용안함' and position == '사용안함':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE nation = %s AND height >= %s AND weight >= %s"
                params = (nation, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE nation = %s AND height >= %s AND weight <= %s"
                params = (nation, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE nation = %s AND height <= %s AND weight >= %s"
                params = (nation, height, weight)
            else:
                sql = "SELECT * FROM player WHERE nation = %s AND height <= %s AND weight <= %s"
                params = (nation, height, weight)
        elif teamid == '사용안함' and position == '미정':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE nation = %s AND position IS NULL AND height >= %s AND weight >= %s"
                params = (nation, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE nation = %s AND position IS NULL AND height >= %s AND weight <= %s"
                params = (nation, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE nation = %s AND position IS NULL AND height <= %s AND weight >= %s"
                params = (nation, height, weight)
            else:
                sql = "SELECT * FROM player WHERE nation = %s AND position IS NULL AND height <= %s AND weight <= %s"
                params = (nation, height, weight)
        elif teamid == '사용안함' and nation == '사용안함':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND height >= %s AND weight >= %s"
                params = (position, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE position = %s AND height >= %s AND weight <= %s"
                params = (position, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND height <= %s AND weight >= %s"
                params = (position, height, weight)
            else:
                sql = "SELECT * FROM player WHERE position = %s AND height <= %s AND weight <= %s"
                params = (position, height, weight)
        elif teamid == '사용안함' and nation == '대한민국':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL AND height >= %s AND weight >= %s"
                params = (position, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL AND height >= %s AND weight <= %s"
                params = (position, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL AND height <= %s AND weight >= %s"
                params = (position, height, weight)
            else:
                sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL AND height <= %s AND weight <= %s"
                params = (position, height, weight)
        elif teamid == '사용안함' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND weight >= %s"
                params = (position, nation, weight)
            else:
                sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND weight <= %s"
                params = (position, nation, weight)
        elif teamid == '사용안함' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height >= %s"
                params = (position, nation, height)
            else:
                sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height <= %s"
                params = (position, nation, height)
        elif position == '사용안함' and nation == '사용안함':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND height >= %s AND weight >= %s"
                params = (teamid, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE team_id = %s AND height >= %s AND weight <= %s"
                params = (teamid, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND height <= %s AND weight >= %s"
                params = (teamid, height, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND height <= %s AND weight <= %s"
                params = (teamid, height, weight)
        elif position == '미정' and nation == '사용안함':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND height >= %s AND weight >= %s"
                params = (teamid, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND height >= %s AND weight <= %s"
                params = (teamid, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND height <= %s AND weight >= %s"
                params = (teamid, height, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND height <= %s AND weight <= %s"
                params = (teamid, height, weight)
        elif position == '사용안함' and nation == '대한민국':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL AND height >= %s AND weight >= %s"
                params = (teamid, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL AND height >= %s AND weight <= %s"
                params = (teamid, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL AND height <= %s AND weight >= %s"
                params = (teamid, height, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL AND height <= %s AND weight <= %s"
                params = (teamid, height, weight)
        elif position == '미정' and nation == '대한민국':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height >= %s AND weight >= %s"
                params = (teamid, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height >= %s AND weight <= %s"
                params = (teamid, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height <= %s AND weight >= %s"
                params = (teamid, height, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height <= %s AND weight <= %s"
                params = (teamid, height, weight)
        elif position == '사용안함' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND weight >= %s"
                params = (teamid, nation, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND weight <= %s"
                params = (teamid, nation, weight)
        elif position == '미정' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND weight >= %s"
                params = (teamid, nation, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nnation = %s AND weight <= %s"
                params = (teamid, nation, weight)
        elif position == '사용안함' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height >= %s"
                params = (teamid, nation, height)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height <= %s"
                params = (teamid, nation, height)
        elif position == '미정' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height >= %s"
                params = (teamid, nation, height)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height <= %s"
                params = (teamid, nation, height)
        elif nation == '사용안함' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND weight >= %s"
                params = (teamid, position, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND weight <= %s"
                params = (teamid, position, weight)
        elif nation == '대한민국' and height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation IS NULL AND weight >= %s"
                params = (teamid, position, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation IS NULL AND weight <= %s"
                params = (teamid, position, weight)
        elif nation == '사용안함' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND height <= %s"
                params = (teamid, position, height)
        elif nation == '대한민국' and weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation IS NULL AND height >= %s"
                params = (teamid, position, height)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation IS NULL AND height <= %s"
                params = (teamid, position, height)
        elif height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s"
            params = (teamid, position, nation)
        elif teamid == '사용안함':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height >= %s AND weight >= %s"
                params = (position, nation, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height >= %s AND weight <= %s"
                params = (position, nation, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height <= %s AND weight >= %s"
                params = (position, nation, height, weight)
            else:
                sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height <= %s AND weight <= %s"
                params = (position, nation, height, weight)
        elif position == '사용안함':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height >= %s AND weight >= %s"
                params = (teamid, nation, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height >= %s AND weight <= %s"
                params = (teamid, nation, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height <= %s AND weight >= %s"
                params = (teamid, nation, height, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height <= %s AND weight <= %s"
                params = (teamid, nation, height, weight)
        elif position == '미정':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height >= %s AND weight >= %s"
                params = (teamid, nation, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height >= %s AND weight <= %s"
                params = (teamid, nation, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height <= %s AND weight >= %s"
                params = (teamid, nation, height, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height <= %s AND weight <= %s"
                params = (teamid, nation, height, weight)
        elif nation == '사용안함':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND height >= %s AND weight >= %s"
                params = (teamid, position, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND height >= %s AND weight <= %s"
                params = (teamid, position, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND height <= %s AND weight >= %s"
                params = (teamid, position, height, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND height <= %s AND weight <= %s"
                params = (teamid, position, height, weight)
        elif nation == '대한민국':
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation IS NULL AND height >= %s AND weight >= %s"
                params = (teamid, position, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation IS NULL AND height >= %s AND weight <= %s"
                params = (teamid, position, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation IS NULL AND height <= %s AND weight >= %s"
                params = (teamid, position, height, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation IS NULL AND height <= %s AND weight <= %s"
                params = (teamid, position, height, weight)
        elif height == '사용안함':
            if weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s AND weight >= %s"
                params = (teamid, position, nation, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s AND weight <= %s"
                params = (teamid, position, nation, weight)
        elif weight == '사용안함':
            if heightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s AND height >= %s"
                params = (teamid, position, nation, height)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s AND height <= %s"
                params = (teamid, position, nation, height)
        else:
            if heightcheck == '이상' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s AND height >= %s AND weight >= %s"
                params = (teamid, position, nation, height, weight)
            elif heightcheck == '이상' and weightcheck == '이하':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s AND height >= %s AND weight <= %s"
                params = (teamid, position, nation, height, weight)
            elif heightcheck == '이하' and weightcheck == '이상':
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s AND height <= %s AND weight >= %s"
                params = (teamid, position, nation, height, weight)
            else:
                sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s AND height <= %s AND weight <= %s"
                params = (teamid, position, nation, height, weight)

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

#########################################

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("선수 테이블 검색")
        self.setGeometry(0, 0, 1100, 830)
        self.label1 = QLabel("선수 검색", self)
        self.label1.move(50, 20)
        self.label2 = QLabel("팀명:", self)
        self.label2.move(80, 80)
        self.comboBox1 = QComboBox(self)
        self.comboBox1.addItem('사용안함')
        query = DB_Queries()
        rows = query.selectPlayerTeamid()  # rows은 dictionary의 리스트
        columnName = list(rows[0].keys())[0]
        items = ['없음' if row[columnName] == None else row[columnName] for row in rows]
        self.comboBox1.addItems(items)
        self.comboBox1.move(140, 76)
        self.label3 = QLabel("포지션:", self)
        self.label3.move(300, 80)
        self.comboBox2 = QComboBox(self)
        self.comboBox2.addItem('사용안함')
        query = DB_Queries()
        rows = query.selectPlayerPosition()  # rows은 dictionary의 리스트
        columnName = list(rows[0].keys())[0]
        items = ['미정' if row[columnName] == None else row[columnName] for row in rows]
        self.comboBox2.addItems(items)
        self.comboBox2.move(380, 76)
        self.label4 = QLabel("출신국:", self)
        self.label4.move(540, 80)
        self.comboBox3 = QComboBox(self)
        self.comboBox3.addItem('사용안함')
        query = DB_Queries()
        rows = query.selectPlayerNation()  # rows은 dictionary의 리스트
        columnName = list(rows[0].keys())[0]
        items = ['대한민국' if row[columnName] == None else row[columnName] for row in rows]
        self.comboBox3.addItems(items)
        self.comboBox3.move(620, 76)
        self.pushButton1 = QPushButton("초기화", self)
        self.pushButton1.move(900, 72)
        self.pushButton1.clicked.connect(self.pushButton1_Clicked)
        self.label5 = QLabel("키:", self)
        self.label5.move(80, 130)
        self.comboBox4 = QComboBox(self)
        self.comboBox4.addItem('사용안함')
        query = DB_Queries()
        rows = query.selectPlayerHeight()  # rows은 dictionary의 리스트
        columnName = list(rows[0].keys())[0]
        items = ['없음' if row[columnName] == None else row[columnName] for row in rows]
        items.remove('없음')
        items.sort()
        items = [str(item) for item in items]
        self.comboBox4.addItems(items)
        self.comboBox4.move(120, 126)
        self.comboBox4.resize(110, 28)
        self.groupbox1 = QGroupBox(self)
        self.radio1 = QRadioButton("이상")
        self.radio1.setChecked(True)
        self.radio2 = QRadioButton("이하")
        hBox = QHBoxLayout()
        hBox.addWidget(self.radio1)
        hBox.addWidget(self.radio2)
        self.groupbox1.setLayout(hBox)
        self.groupbox1.move(250, 116)
        self.label6 = QLabel("몸무게:", self)
        self.label6.move(460, 130)
        self.comboBox5 = QComboBox(self)
        self.comboBox5.addItem('사용안함')
        query = DB_Queries()
        rows = query.selectPlayerWeight()  # rows은 dictionary의 리스트
        columnName = list(rows[0].keys())[0]
        items = ['없음' if row[columnName] == None else row[columnName] for row in rows]
        items.remove('없음')
        items.sort()
        items = [str(item) for item in items]
        self.comboBox5.addItems(items)
        self.comboBox5.move(530, 126)
        self.comboBox5.resize(110, 28)
        self.groupbox2 = QGroupBox(self)
        self.radio3 = QRadioButton("이상")
        self.radio3.setChecked(True)
        self.radio4 = QRadioButton("이하")
        hBox = QHBoxLayout()
        hBox.addWidget(self.radio3)
        hBox.addWidget(self.radio4)
        self.groupbox2.setLayout(hBox)
        self.groupbox2.move(660, 116)
        self.pushButton2 = QPushButton("검색", self)
        self.pushButton2.move(900,122)
        self.pushButton2.clicked.connect(self.pushButton2_Clicked)
        self.tableWidget = QTableWidget(self)  # QTableWidget 객체 생성
        self.tableWidget.move(50, 180)
        self.tableWidget.resize(1000, 500)
        self.pushButton1_Clicked()
        self.label7 = QLabel("파일 출력", self)
        self.label7.move(50, 720)
        self.groupbox3 = QGroupBox(self)
        self.radio5 = QRadioButton("CSV")
        self.radio5.setChecked(True)
        self.radio6 = QRadioButton("JSON")
        self.radio7 = QRadioButton("XML")
        hBox = QHBoxLayout()
        hBox.addWidget(self.radio5)
        hBox.addWidget(self.radio6)
        hBox.addWidget(self.radio7)
        self.groupbox3.setLayout(hBox)
        self.groupbox3.move(100, 760)
        self.pushButton3 = QPushButton("저장", self)
        self.pushButton3.move(900, 760)
        self.pushButton3.clicked.connect(self.pushButton3_Clicked)

    def comboBox1_Activated(self):
        self.teamidValue = self.comboBox1.currentText()  # positionValue를 통해 선택한 포지션 값을 전달

    def comboBox2_Activated(self):
        self.positionValue = self.comboBox2.currentText()

    def comboBox3_Activated(self):
        self.nationValue = self.comboBox3.currentText()

    def comboBox4_Activated(self):
        self.heightValue = self.comboBox4.currentText()
        if self.radio1.isChecked():
            self.heightCheck = "이상"
        else:
            self.heightCheck = "이하"

    def comboBox5_Activated(self):
        self.weightValue = self.comboBox5.currentText()
        if self.radio3.isChecked():
            self.weightCheck = "이상"
        else:
            self.weightCheck = "이하"

    # 초기화 버튼
    def pushButton1_Clicked(self):
        self.comboBox1.setCurrentIndex(0)
        self.comboBox2.setCurrentIndex(0)
        self.comboBox3.setCurrentIndex(0)
        self.comboBox4.setCurrentIndex(0)
        self.comboBox5.setCurrentIndex(0)
        self.radio1.setChecked(True)
        self.radio3.setChecked(True)

        query = DB_Queries()
        players = query.selectAllPlayer()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(players))
        self.tableWidget.setColumnCount(len(players[0]))
        columnNames = list(players[0].keys())
        self.tableWidget.setHorizontalHeaderLabels(columnNames)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for rowIDX in range(len(players)):
            player = players[rowIDX]

            for k, v in player.items():
                columnIDX = columnNames.index(k)

                if v == None:  # 파이썬이 DB의 널값을 None으로 변환함.
                    if k == 'POSITION':
                        item = QTableWidgetItem('미정')
                    elif k == 'NATION':
                        item = QTableWidgetItem('대한민국')
                    else:
                        continue  # QTableWidgetItem 객체를 생성하지 않음
                elif isinstance(v, datetime.date):  # QTableWidgetItem 객체 생성
                    item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                else:
                    item = QTableWidgetItem(str(v))

                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    # 검색 버튼
    def pushButton2_Clicked(self):
        self.comboBox1_Activated()
        self.comboBox2_Activated()
        self.comboBox3_Activated()
        self.comboBox4_Activated()
        self.comboBox5_Activated()

        # DB 검색문 실행
        query = DB_Queries()
        players = query.selectPlayer(self.teamidValue, self.positionValue, self.nationValue, self.heightValue, self.heightCheck, self.weightValue, self.weightCheck)

        if players == ():
            self.tableWidget.clearContents()
        else:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(len(players))
            self.tableWidget.setColumnCount(len(players[0]))
            columnNames = list(players[0].keys())
            self.tableWidget.setHorizontalHeaderLabels(columnNames)
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

            for rowIDX in range(len(players)):
                player = players[rowIDX]

                for k, v in player.items():
                    columnIDX = columnNames.index(k)

                    if v == None:  # 파이썬이 DB의 널값을 None으로 변환함.
                        if k == 'POSITION':
                            item = QTableWidgetItem('미정')
                        elif k == 'NATION':
                            item = QTableWidgetItem('대한민국')
                        else:
                            continue  # QTableWidgetItem 객체를 생성하지 않음
                    elif isinstance(v, datetime.date):  # QTableWidgetItem 객체 생성
                        item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                    else:
                        item = QTableWidgetItem(str(v))

                    self.tableWidget.setItem(rowIDX, columnIDX, item)

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()

    def pushButton3_Clicked(self):
        self.comboBox1_Activated()
        self.comboBox2_Activated()
        self.comboBox3_Activated()
        self.comboBox4_Activated()
        self.comboBox5_Activated()

        # DB 검색문 실행
        query = DB_Queries()
        players = query.selectPlayer(self.teamidValue, self.positionValue, self.nationValue, self.heightValue, self.heightCheck, self.weightValue, self.weightCheck)

        if self.radio5.isChecked():
            # CSV 화일을 쓰기 모드로 생성
            with open('player.csv', 'w', encoding='utf-8', newline='') as f:
                wr = csv.writer(f)
                # 테이블 헤더를 출력
                columnNames = list(players[0].keys())
                wr.writerow(columnNames)
                # 테이블 내용을 출력
                for rowIDX in range(len(players)):
                    row = list(players[rowIDX].values())
                    wr.writerow(row)

        elif self.radio6.isChecked():
            # 애트리뷰트 BIRTH_DATE의 값을 MySQL datetime 타입에서 스트링으로 변환함. (CSV에서는 패키지가 변환함.)
            for player in players:
                for k, v in player.items():
                    if isinstance(v, datetime.date):
                        player[k] = v.strftime('%Y-%m-%d')  # 키가 k인 item의 값 v를 수정
            newDict = dict(player=players)
            # JSON 화일에 쓰기
            # dump()에 의해 모든 작은 따옴표('')는 큰 따옴표("")로 변환됨
            with open('player.json', 'w', encoding='utf-8') as f:
                json.dump(newDict, f, ensure_ascii=False)

            with open('player_indent.json', 'w', encoding='utf-8') as f:
                json.dump(newDict, f, indent=4, ensure_ascii=False)

        else:
            # 애트리뷰트 BIRTH_DATE의 값을 MySQL datetime 타입에서 스트링으로 변환함. (CSV에서는 패키지가 변환함.)
            for player in players:
                for k, v in player.items():
                    if isinstance(v, datetime.date):
                        player[k] = v.strftime('%Y-%m-%d')  # 키가 k인 item의 값 v를 수정
            newDict = dict(player=players)
            # XDM 트리 생성
            tableName = list(newDict.keys())[0]
            tableRows = list(newDict.values())[0]
            rootElement = ET.Element('Table')
            rootElement.attrib['name'] = tableName
            for row in tableRows:
                rowElement = ET.Element('Row')
                rootElement.append(rowElement)
                for columnName in list(row.keys()):
                    if row[columnName] == None:  # NICKNAME, JOIN_YYYY, NATION 처리
                        rowElement.attrib[columnName] = ''
                    else:
                        rowElement.attrib[columnName] = row[columnName]
                    if type(row[columnName]) == int:  # BACK_NO, HEIGHT, WEIGHT 처리
                        rowElement.attrib[columnName] = str(row[columnName])
            # XDM 트리를 화일에 출력
            ET.ElementTree(rootElement).write('player.xml', encoding='utf-8', xml_declaration=True)

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

main()