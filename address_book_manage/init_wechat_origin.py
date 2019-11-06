creat_table_sql = '''
CREATE TABLE "wechat_origin" (
	"MemberList"	TEXT,
	"UserName"	TEXT,
	"City"	TEXT,
	"DisplayName"	TEXT,
	"PYQuanPin"	TEXT,
	"RemarkPYInitial"	TEXT,
	"Province"	TEXT,
	"KeyWord"	TEXT,
	"RemarkName"	TEXT,
	"PYInitial"	TEXT,
	"EncryChatRoomId"	TEXT,
	"Alias"	TEXT,
	"Signature"	TEXT,
	"NickName"	TEXT,
	"RemarkPYQuanPin"	TEXT,
	"HeadImgUrl"	TEXT,
	"UniFriend"	INTEGER,
	"Sex"	INTEGER,
	"AppAccountFlag"	INTEGER,
	"VerifyFlag"	INTEGER,
	"ChatRoomId"	INTEGER,
	"HideInputBarFlag"	INTEGER,
	"AttrStatus"	INTEGER,
	"SnsFlag"	INTEGER,
	"MemberCount"	INTEGER,
	"OwnerUin"	INTEGER,
	"ContactFlag"	INTEGER,
	"Uin"	INTEGER,
	"StarFriend"	INTEGER,
	"Statues"	INTEGER,
	"WebWxPluginSwitch"	TEXT,
	"HeadImgFlag"	TEXT,
	"IsOwner"	INTEGER,
	"ContactType"	TEXT,
	"ChatRoomOwner"	TEXT,
	"HeadImgUpdateFlag"	TEXT
);
'''
import sqlite3

def create():
    try:
        c.execute(creat_table_sql)
    except:
        pass

#def insert():
#    c.execute("""INSERT INTO mytable (start, end, score)
#              values(1, 99, 123)""")
#
#def select(verbose=True):
#    sql = "SELECT * FROM mytable"
#    recs = c.execute(sql)
#    if verbose:
#        for row in recs:
#            print row

db_path = r'/address_book_manage/data/wechat.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()
create()
#insert()
conn.commit() #commit needed
#select()
c.close()
