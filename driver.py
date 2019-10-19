import argparse
import address_book_manage.wechat_process as wcp

def main():

    example_text = '''example:

    python driver.py -abm -untag
    # output untaged wechat account id
    '''
    #python driver.py -abm -o 
    # output wechat friend list

    parser = argparse.ArgumentParser(epilog=example_text,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-abm", action="store_true",  help="Address book management")
    parser.add_argument("-untag", action="store_true",  help="output untaged wechat account id")




    # 写条件
    args = parser.parse_args()

    # 处理条件选择
    if args.abm and args.untag:
        wp = wcp.WechatProcesser()
        wp.WriteDictToCSV()
        contacts = wp.get_csv_data()
        unregister_data_list = wp.get_unregister_data(contacts)
        print(unregister_data_list)
    else:
        print("WIP")

if __name__ == "__main__":
    main()

