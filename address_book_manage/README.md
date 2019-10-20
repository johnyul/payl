通讯录管理

已实现功能
* 基于itchat，导出微信好友信息到本地csv文件
* 为好友增加序列化信息到微信备注
* 为指定的好友增加特殊后缀

数据库设计

#### Table: person

person_id:Primary key:String:Format -> p00001~p99999
name:String
gender:int -> 0:male 1:female 2:unknown 3:others
type: self-define type
tag: self-define tag

#### Table: person_type

type_id:
type_name:

#### Table: person_tag
tag_id
tag_name

#### Table: contact_info

person_id
phone1
phone2
email
address


#### Table: wechat_account

wechat_account_id:Primary key:String:Format -> z0001 ~ z9999
person_id: the same with Table: person
agent_id: the same with Table: agent
Note: 
* One person can have multiple wechat account, they have the same person_id, but different wechat_account_id
* One wechat account maybe belong to a person or an agent

#### Table: wechat_detail

wechat_account_id:Primary key:String:Format -> z0001 ~ z9999
other info get from wechat

#### Table: agent

agent_id:
name:
type: company,community


