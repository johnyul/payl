'''
Useage: to init permanent csv file
Warning: be carful about the path, if there is an file exists, it might cover
the file
'''
import sys
import os
import csv
project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_root)

import address_book_manage.online_wechat_process as owp
from config import configer

data_dir = os.path.join(project_root,configer['permanent']['data_dir'])
friends_path = os.path.join(data_dir, configer['permanent']['friends_list_csv'])
group_path = os.path.join(data_dir,configer['permanent']['group_list_csv'])
#print(data_dir,friends_path,group_path)


def init_friend_file(friends_path):
    # 基于已有的online模块获取数据，删除临时文件
    wp = owp.WechatProcesser()
    wp.WriteDictToCSV()
    contacts = wp.get_csv_data()
    #wp.del_csv_file()
    columns = list(zip(*contacts[2:]))
    header,index_list = get_header()
    print(header,index_list)
    # TODO 搞明白原因
    res_list = list(map(columns.__getitem__, index_list))
    print(res_list)
    r = list(map(list,zip(*res_list)))
    r.insert(0,header)

    with open(friends_path,'w+') as f:
        writer = csv.writer(f)
        for c in r:
                writer.writerow(c)
        

def get_header():
    '''get csv init header from config file
    '''
    header = []
    index_list = []
    for k,v in configer.items('wechat_friends_info'):
        #print(k,v)
        header.append('_'.join(['wc',k]))
        index_list.append(int(v))
    return header,index_list


def main():
    try:
        with open(friends_path) as f:
            # do whatever
            print("It exists, you'd better check the file first before process any data.")
            print("File path is {}.".format(friends_path))
    except IOError:
        print('no file')
        init_friend_file(friends_path)

if __name__ == "__main__":
    main()
