#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
import re

reload(sys)
sys.setdefaultencoding("utf-8")

cv_basic_patterns = {"name": "姓名", "phone": "手机|电话", "email": "邮箱|e-mail|mail|email", "age": "年龄|岁",
                     "address": "通讯地址|居住地", "gender": "性别|男|女"}
cv_edu_patterns = {"university": "毕业院校|教育背景", "major": "专业", "degree": "学历|大专|专科|硕士|博士|研究生"}
cv_job_patterns = {"evaluation": "个人描述|自我评价|个人情况|兴趣", "career": "求职意向|应聘职位|求职类型|职位", "work": "工作经历|工作经验|工作职责",
                   "project": "项目经历"}

content = "姓名：周小代  工作年限：10年以上工作经验  城市：广东 深圳市  性别：女  出生日期：1975-07-01  手机：13825267167  邮箱：xiaodaizhou@163.com  职位：经理    教育经历    学校：湖南省怀化师范高等专科学校  所学专业：汉语言文学  学历：本科；毕业年份：1998    工作经历    公司：深圳伟立(宝安)吉泰电子有限公司  职位：文员  开始日期：1996-03；结束日期：1998-08  工作内容：  至 办公室 负责文件存档、派车、制作各种报表供领导决策使用  【工作经历详细介绍】      公司：深圳桑菲消费通信有限公司  职位：组长  开始日期：2000-03；结束日期：2002-07  工作内容：  IQC a.负责IQC所有进料（塑胶料，电子料，包装材料等其它物类）的检验  b.IQC各成员间的工作安排与协调；IQC异常的初步确认与处理；IQC各种报表的制作  (2)     公司：斯曼特显示科技(深圳)有限公司  职位：主管  开始日期：2005-05；结束日期：2007-11  工作内容：  至 物控 a.计划的编排与生产协调：制定月生产计划和周进行近期计划的编排,创建生产订单,安排生产,协  调物料齐套/产能/设备运行状况及跟进计划的有效执行,突发事件异常问题的处理  b.与销售单位沟通，对FORECAST信息反馈和维护进系统  c. 缺料处理:根据生产计划制作合理的到货计划，保障生产用料供应顺畅；生产缺料的交期回复与  跟进问题物料的快速处理；缺料原因分析、总结及责任相关部门改善  d. 协调关系:加强与生产、采购 财务等部门的联系，经常交换信息，及时调节库存水平,共 同努力完成各项工作任务  e.负责外协加工厂的物料结算  f.订单评审      公司：深圳市亚维讯电子科技有限公司  职位：经理  开始日期：2007-12；结束日期：2009-01  工作内容：  至 PMC 1.部门整体工作事务的处理和与供应商及部门间的沟通与协调  2.参与公司宏观管理和策略制定，负责审批和修订部门作业流程和管理制度  3.制订部门内部短、中、长期工作计划，并跟踪实施结果，负责检讨改善  4.组织并考核生产计划、物料控制、物料采购及供应商开发计划和达成进度  5.参与供应商的考核、评估，配合相关部门确定解决方案,分析、处理供应商重大异常  6.部门文件资料及单据的签发与审批  7.负责部门人员的绩效考核与教育训练等"

jd_include_keys = {"cv": "岗位职责|任职要求|任职资格|能力要求|基本要求|职责描述|岗位要求|岗位描述|岗位名称|职位描述"}
cv_include_keys = {"jd": "求职意向|求职状态|教育背景|教育经历"}


def isMatch(pattern, text):
    if re.compile(pattern).search(text):
        return 1
    else:
        return 0


def cvMatchFlow(content):
    cv_basic_matches = {}
    cv_basic_matches["total"] = 0
    cv_edu_matches = {}
    cv_edu_matches["total"] = 0
    cv_job_matches = {}
    cv_job_matches["total"] = 0
    cv_key_matches = {}

    cv_key_matches["total"] = 0
    jd_key_matches = {}
    jd_key_matches["total"] = 0

    for k, v in cv_basic_patterns.items():
        cv_basic_matches[k] = isMatch(v, content)
        cv_basic_matches["total"] = cv_basic_matches[k] + cv_basic_matches["total"]

    for k, v in cv_edu_patterns.items():
        cv_edu_matches[k] = isMatch(v, content)
        cv_edu_matches["total"] = cv_edu_matches[k] + cv_edu_matches["total"]

    for k, v in cv_job_patterns.items():
        cv_job_matches[k] = isMatch(v, content)
        cv_job_matches["total"] = cv_job_matches[k] + cv_job_matches["total"]

    for k, v in cv_include_keys.items():
        cv_key_matches[k] = isMatch(v, content)
        cv_key_matches["total"] = cv_key_matches[k] + cv_key_matches["total"]

    for k, v in jd_include_keys.items():
        jd_key_matches[k] = isMatch(v, content)
        jd_key_matches["total"] = jd_key_matches[k] + jd_key_matches["total"]

        return cv_basic_matches, cv_edu_matches, cv_job_matches, cv_key_matches, jd_key_matches


cv_basic_matches, cv_edu_matches, cv_job_matches, cv_key_matches, jd_key_matches = cvMatchFlow(content)

print(cv_basic_matches)
print(cv_edu_matches)
print(cv_job_matches)
print(cv_key_matches)
print(jd_key_matches)
