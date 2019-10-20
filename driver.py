import argparse
import address_book_manage.online_wechat_process as wcp

def main():

    example_text = '''example:

    python driver.py -abm -untag
    # output untaged wechat account id

    python driver.py -abm -ocsv
    # output wechat friend list in csv file

    python driver.py -abm -tag
    # give wechat new friend number tag
    # Warning: they must have wechat remark name first
    '''

    parser = argparse.ArgumentParser(epilog=example_text,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-abm", action="store_true",  help="Address book management")
    parser.add_argument("-untag", action="store_true",  help="output untaged wechat account id")
    parser.add_argument("-ocsv", action="store_true",  help="output csv file list")
    parser.add_argument("-tag", action="store_true",  help="output csv file list")


    # 写条件
    args = parser.parse_args()

    # 处理条件选择
    if args.abm and args.untag:
        wp = wcp.WechatProcesser()
        wp.WriteDictToCSV()
        contacts = wp.get_csv_data()
        unregister_data_list = wp.get_unregister_data(contacts)
        print(unregister_data_list)
        wp.del_csv_file()

    if args.abm and args.ocsv:
        wp = wcp.WechatProcesser()
        wp.WriteDictToCSV()

    if args.abm and args.tag:
        wp = wcp.WechatProcesser()
        wp.WriteDictToCSV()
        contacts = wp.get_csv_data()
        unregister_data_list = wp.get_unregister_data(contacts)
        print(unregister_data_list)
        s = input('Tag all print "Y"')
        if s == 'Y':
            _num = wp.get_numbers(contacts)
            _available_num = wp.get_available_numbers(_num,4002,100)
            wp.registe_data(contacts,unregister_data_list,_available_num)
        wp.del_csv_file()
        
        

if __name__ == "__main__":
    main()

