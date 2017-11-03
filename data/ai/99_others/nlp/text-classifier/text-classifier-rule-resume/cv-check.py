#!/usr/bin/env python  
# _*_ coding:utf-8 _*_

import xlrd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

pattern_dict = {
    "base_info": ["姓名", "手机", "电话", "邮箱", "e-mail", "年龄", "籍贯", "通讯地址", "居住地", "户口", "性别", "男", "女"],
    "education_info" : ["毕业学校", "毕业院校", "教育背景", "专业", "学历", "大专", "专科", "本科", "硕士", "博士", "研究生"],
    "job_info": ["求职意向", "应聘职位", "求职类型", "工作经历", "工作经验", "职位", "项目经历", "项目", "工作职责", "工作地点", "工作地区", "个人描述", "自我评价", "个人情况", "兴趣"]
}

def nonCVCheck(content):
    non_cv_pattern_keys = ["岗位职责", "任职要求", "任职资格", "能力要求", "基本要求", "职责描述", "岗位要求", "岗位描述", "岗位名称", "职位描述"]
    for key in non_cv_pattern_keys:
        if key in content:
            return True
    return False

def isCVCheck(content):
    is_cv_pattern_keys = ["求职意向", "求职状态", "教育背景", "教育经历"]
    base_info_match = []
    education_info_match = [] 
    job_info_match = []

    base_info_list = []
    education_info_list = []
    job_info_list = []
    other_info_list = []
    for k, v in pattern_dict.items():
        if k == "base_info":
            base_info_list = [content.find(eachv) for eachv in v]
        elif k == "education_info":
            education_info_list = [content.find(eachv) for eachv in v]
        elif k == "job_info":
            job_info_list = [content.find(eachv) for eachv in v]
        else:
            pass
    base_info_match = [ v for v in base_info_list if v != -1]
    education_info_match = [v for v in education_info_list if v != -1]
    job_info_match = [v for v in job_info_list if v != -1]
    print base_info_match
    print job_info_match
    print education_info_match
    if len(base_info_match) > 0 and len(job_info_match) > 0:
        if min(base_info_match) <= min(job_info_match) and min(base_info_match) < len(content)/2:
            return True
        if len(education_info_match) > 0 and min(education_info_match) < len(content)/2 and min(base_info_match) < min(education_info_match):
            return True
        for key in is_cv_pattern_keys:
            if key in content:
                return True
        return False
    if len(job_info_match) > 0 and len(education_info_match) > 0:
        for key in is_cv_pattern_keys:
            if key in content:
                return True
    if len(base_info_match) >= 2  and len(job_info_match) == 0 and len(education_info_match) > 0:
        return True
    return False

if __name__ == "__main__":
    path = "Sample_2.xlsx"
    descPos = 2
    data = xlrd.open_workbook(path)
    tableSample = data.sheets()[1]
    nrows = tableSample.nrows
    datav = []
    for row in range(nrows):
        if row != 0:
            datav.append(tableSample.row_values(row)[descPos].lower())
    f = open("sample_2_res.txt", "w")
    for line in datav:
        if nonCVCheck(line):
            f.write("other\n")
            continue
        if isCVCheck(line):
            f.write("cv\n")
        else:
            f.write("other\n")
    f.close()
