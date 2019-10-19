import itchat
import csv
from time import sleep
import os
import arrow

class WechatProcesser():
    def __init__(self):
        itchat.auto_login(hotReload=True, enableCmdQR=False)
        self.csv_file = "wechat_accounts.csv"
        self.tmp_file = arrow.now('local').format('YYYYMMDD_hh_mm_ss') + '_' + self.csv_file
        self.origin_data = itchat.get_friends()
        self.columns = list(self.origin_data[0].keys())
        self.columns.extend(['ContactType','ChatRoomOwner','HeadImgUpdateFlag'])

#    def loginCallback(self):
#        print("***登录成功***")
#    def exitCallback(self):
#        print("***已退出***")
#    itchat.auto_login(hotReload=True, enableCmdQR=False, loginCallback=loginCallback, exitCallback=exitCallback)
    
    #def WriteDictToCSV(csv_file,csv_columns,dict_data):
    def WriteDictToCSV(self):
        try:
            with open(self.tmp_file, 'w',encoding='utf-8-sig') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.columns)
                writer.writeheader()
                for data in self.origin_data:
                    writer.writerow(data)
            print('file_name:{}'.format(self.tmp_file))
        except IOError :
                print("I/O error({0}): {1}".format(errno, strerror))
        return
    
    #def get_csv_data(file_path):
    def get_csv_data(self):
        print("file_path:",self.tmp_file)
        with open(self.tmp_file, 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            #logger.debug(your_list)
            return your_list

    def del_csv_file(self):
        if os.path.exists(self.tmp_file):
            os.remove(self.tmp_file)
            print("delete tmp csv file")
        else:
            print("The file does not exist")

    def get_unregister_data(self,list_data):
        name_list = [_j[8] for _j in list_data][2:]
        no_z_list = []
        for __i in name_list:
            # TODO: 这里的方式太personal，需要替换为通用方案
            if 'z' in __i:
                pass
            else:
                no_z_list.append(__i)
        str_list = list(filter(len, no_z_list))
        return str_list

    def registe_data(self,contacts,unregist_name_list,id_num):
        """
        为有标注但是无序号的微信好友增加序号
        !!Warning: 该方法会修改微信的备注数据，慎用
        contacts: 微信获取的好友信息
        unregist_name_list: 需要处理的有备注但是没有序号的名称列表
        id_num: 可以使用的序号的第一个
        """
        # 生成指定的序号
        # TODO: 这里的序号生成不够通用，另外需要生成的序号也是需要指定的
        from random import randint
        from time import sleep
        # 构造对应的序号
        s_num = []
        for i in range(int(id_num),int(id_num)+100):
             s_num.append('z' + str('{0:04}'.format(i)))
        # 构造对应的userID
        userid_list = []
        for i in unregist_name_list:
            for el in contacts[2:]:
                if el[8] == i:
                    userid_list.append(el[1])
        # 进行处理
        flag = 0
        for i in userid_list:
            print(itchat.set_alias(userName=i,
                alias=unregist_name_list[flag]+'.'+s_num[flag]))
            flag += 1
        sleep(randint(5,15))

    def registe_data(self,contacts,unregist_name_list,sign):
        """
        为有标注但是无序号的微信好友增加序号
        !!Warning: 该方法会修改微信的备注数据，慎用
        contacts: 微信获取的好友信息
        unregist_name_list: 需要处理的有备注但是没有序号的名称列表
        id_num: 可以使用的序号的第一个
        """
        # 生成指定的序号
        # TODO: 这里的序号生成不够通用，另外需要生成的序号也是需要指定的
        from random import randint
        from time import sleep
        # 构造对应的userID
        userid_list = []
        for i in unregist_name_list:
            for el in contacts[2:]:
                if el[8] == i:
                    userid_list.append(el[1])
        # 进行处理
        flag = 0
        for i in userid_list:
            print(itchat.set_alias(userName=i,
                alias=unregist_name_list[flag]+'.'+sign))
            flag += 1
        sleep(randint(5,15))

def main():
    # 获取数据
    wp = WechatProcesser()
    #wp.WriteDictToCSV()
    #contacts = wp.get_csv_data()
    # 获取未标注数据: 是有备注，但是没有指定序号的数据
    #unregister_data_list = wp.get_unregister_data(contacts)
    #print(unregister_data_list)
    #------------------------------
    # 对有备注但未标记序号的数据做处理
    # id_num = 8888 #注意: 请改成你实际需要的数字
    #wp.registe_data(contacts,unregister_data_list,id_num)
    #------------------------------
    # 用于增加特殊后缀
    #name_list = ['']
    #wp.registe_data(contacts,name_list,'@')
    

if __name__ == "__main__":
    main()
