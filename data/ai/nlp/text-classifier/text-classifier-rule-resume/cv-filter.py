#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

cv_basic_patterns = {"name": ["姓名"], "phone": ["手机", "电话"], "email": ["邮箱", "e-mail"],"age": ["年龄"], "address": ["通讯地址"],"location": ["居住地"], "hukou": ["户口"], "gender": ["性别", "男", "女"]}
cv_edu_patterns = {"university": ["毕业院校", "教育背景"], "major": ["专业"], "degree": ["学历", "大专", "专科", "硕士", "博士", "研究生"]}
cv_job_patterns = {"evaluation": ["个人描述", "自我评价", "个人情况", "兴趣"], "career": ["求职意向", "应聘职位", "求职类型", "职位"], "work": ["工作经历", "工作经验", "工作职责", "工作地点", "工作地区"], "project": ["项目经历", "项目"]}

cv_include_keys = {"cv": ["岗位职责", "任职要求", "任职资格", "能力要求", "基本要求", "职责描述", "岗位要求", "岗位描述", "岗位名称", "职位描述"]}
jd_include_keys = {"jd": ["求职意向", "求职状态", "教育背景", "教育经历"]}



def cvMatchFlow(content):
    cv_basic_matches = {}
    cv_edu_matches = {}
    cv_job_matches = {}
    cv_key_matches = {}
    jd_key_matches = {}
    for k,v in cv_basic_patterns.items():
        cv_basic_matches[k]= [content.find(eachv) for eachv in v]

    for k,v in cv_edu_patterns.items():
        cv_edu_matches[k]= [content.find(eachv) for eachv in v]

    for k,v in cv_job_patterns.items():
        cv_job_matches[k]= [content.find(eachv) for eachv in v]

    for k,v in cv_include_keys.items():
        cv_key_matches[k]= [content.find(eachv) for eachv in v]

    for k,v in cv_include_keys.items():
        jd_key_matches[k]= [content.find(eachv) for eachv in v]

        return  cv_basic_matches,cv_edu_matches,cv_job_matches,cv_key_matches,jd_key_matches



def cvRecognition(content):
    cv_basic_matches,cv_edu_matches,cv_job_matches,cv_key_matches,jd_key_matches=cvMatchFlow(content)

    cv_basic_matches.items().










def isNotCV(content):
    for key in jd_keys:
        if key in content:
            return True
    return False

def isCV(content):
    base_info_match = []
    education_info_match = []
    job_info_match = []

    base_info_list = []
    education_info_list = []
    job_info_list = []
    other_info_list = []
    for k, v in cv_patterns.items():
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
        for key in cv_include_keys:
            if key in content:
                return True
        return False
    if len(job_info_match) > 0 and len(education_info_match) > 0:
        for key in cv_include_keys:
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
