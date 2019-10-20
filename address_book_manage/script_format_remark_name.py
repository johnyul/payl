'''
feature: to clean some special sign in remarkName like '\n'
author: John Yul
'''

from wechat_process import WechatProcesser
from random import randint
from time import sleep
import itchat

def get_special_sign(contacts):
    l = [i[8] for i in contacts[2:] if '\n' in i[8]]
    print(l)
    return l

def get_userid_list(contacts,name_list,column):
    ''' get userid list
    column: base on name_list, remarkName is 8,nickName is 13 
    '''
    # TODO 优化该方法,不仅仅是两个for循环
    # 法一：基于二维列表，通过其中一列获取值的index获取另一列的值
    # 法二：优化for循环的写法为可迭代方式
    # 法三: 调整逻辑，在第一次获取对应列表时保留对应的index或者直接算出需要处理的元素位置
    # TODO 把该方法加入wechat_process 中
    userid_list = []
    for i in name_list:
        for el in contacts[2:]:
            if el[column] == i:
                userid_list.append(el[1])
    return userid_list

def clean_spcial_sign(contacts,to_clean_l):
    userid_list = get_userid_list(contacts,to_clean_l,8)
    print('userid_list:',userid_list)
    flag = 0
    for i in userid_list:
        print(to_clean_l[flag])
        print(itchat.set_alias(userName=i,alias=to_clean_l[flag].replace('\n','')))
        flag += 1
        sleep(randint(5,15))

def main():
    wp = WechatProcesser()
    wp.WriteDictToCSV()
    contacts = wp.get_csv_data()

    to_clean_l = get_special_sign(contacts)
    clean_spcial_sign(contacts,to_clean_l)

if __name__ == "__main__":
    main()
