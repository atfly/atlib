#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/26 10:18
# @Author  : skydm
# @Site    : 
# @File    : new_test.py

import re
import copy
import time
from Main_Scripts.util.data_process import *
from Main_Scripts.util.reg_exp import Reg_Exp

reg = Reg_Exp()

class SchoolNer(object):
    def __init__(self):
        (self.adult_list, self.synonyms_history_list, self.synonyms_now_list, self.independent_list,
        self.sd_list, self.before_list, self.flast_list, self.full_list, self.jx_list, self.big_school_list,
        self.error_contain_school, self.school_985_list, self.school_211_list, self.school_first_list,
        self.school_second_list, self.school_third_list, self.school_special_list, self.jx_error_dict,
        self.en_school_name, self.en_school_jx, self.en_school_zh, self.en_school_jx_zh, self.new_ch_school_en,
        self.new_ch_school_jx, self.new_ch_school_en_zh, self.new_ch_school_jx_zh ,self.zh_school_url, self.en_school_url, self.en_school_rank, self.en_school_zh_jx, self.en_school_zh_jx_zh) = self.return_dict()
        self.history_dict = dict(zip(self.before_list, self.flast_list))
        self.jx_dict = dict(zip(self.jx_list, self.full_list))
        self.synonyms_dict = dict(zip(self.synonyms_history_list, self.synonyms_now_list))
        self.only_en_school_name = copy.deepcopy(self.en_school_name) # 深拷贝
        self.only_en_school_zh = copy.deepcopy(self.en_school_zh)  # 深拷贝
        # 生成字典
        self.school_en_dict, self.school_jx_dict, self.en_school_jx_total, self.en_school_name_total, self.school_en_zh_dict = self.get_dict()
        self.zh_school_url_dict = dict(zip(self.sd_list,self.zh_school_url))
        self.en_school_url_dict = dict(zip(self.only_en_school_name,self.en_school_url))
        self.en_school_rank_dict = dict(zip(self.only_en_school_name,self.en_school_rank))
        self.en_school_zh_jx_dict = dict(zip(self.en_school_zh_jx, self.en_school_zh_jx_zh))

    # 获取英文高校名及其对应的中文名
    # 获取英文高校名简称及其对应的中文名
    def get_dict(self):
        self.en_school_name.extend(self.new_ch_school_en)
        self.en_school_zh.extend(self.new_ch_school_en_zh)
        self.en_school_jx.extend(self.new_ch_school_jx)
        self.en_school_jx_zh.extend(self.new_ch_school_jx_zh)
        school_en_dict = dict(zip(self.en_school_name, self.en_school_zh))  # 英文：中文 字典
        school_jx_dict = dict(zip(self.en_school_jx, self.en_school_jx_zh)) # 英文简写：中文 字典
        school_en_zh_dict = dict(zip(self.en_school_zh, self.en_school_name))  # 中文：英文 字典
        return school_en_dict, school_jx_dict, self.en_school_jx, self.en_school_name, school_en_zh_dict

    # 判断是否是成人高校
    def contain_adult(self, school):
        for element in self.adult_list:
            if element in school:
                return element

    # 判断是否是独立学院
    def contain_independent(self, school):
        for element in self.independent_list:
            if element in school:
                return element

    # 判断名称是否在标准库中
    def contain_sd(self, school):
        s = []
        for element in self.sd_list:
            if element in school:
                s.append(element)
        middle = list(map(len, s))
        if len(middle)>0:
            result = s[middle.index(max(middle))]
        else:
            result = None
        return result

    # 判断简写是否在字符串中
    def contain_jx(self, school):
        for ele in self.jx_list:
            t = ele.split(" ")
            for i in t:
                if i in school and i != '':
                    return self.jx_dict[ele]
        for ele in self.en_school_zh_jx:
            if ele in school and ele != '':
                return self.en_school_zh_jx_dict[ele]


    # 判断名称是否在历史沿用名表中
    def contain_history(self, school):
        for element in self.before_list:
            if element in school:
                return self.history_dict[element]

    # 判断名称是否在同义词库中
    def contain_synonyms(self, school):
        for element in self.synonyms_history_list:
            if element in school:
                return self.synonyms_dict[element]

    # 判断是否在整个高校字典库中
    def contain_big_school(self, school):
        for element in self.big_school_list:
            if element == school:
                return element

    # 判断名称是否在简写错误库中
    def filter_jx_error(self, school):
        for i in self.jx_error_dict:
            school = school.replace(i, '')
        return school



    # 获取确定字段的数据
    def return_dict(self):
        tt = get_data('adult_td_school', 'school')  # 获取成人高校
        t0 = get_data('school_independent', 'school')  # 获取独立院校
        t1 = get_data('all_school_new', 'school', 'url')  # 获取标准院校库
        t2 = get_data('school_history', 'fbefore_school', 'flast_school')  # 历史沿用名字典表
        t3 = get_data('school_jx_dict', 'school', 'zh_jx_name')  # 引入简写字典表
        t5 = get_data('tongyi_dict_new', 'fhistory_name', 'fnow_name')  # 同义词词库
        t6 = get_data('big_school', 'school')  # 大的高校词库
        t7 = get_data('dirty_data', 'school')  # 错误词库
        t8 = get_data('school_985', 'school')  # 985 高校
        t9 = get_data('school_211', 'school')  # 211 高校
        t10 = get_data('school_first_level', 'school')  # 一本高校
        t11 = get_data('school_second_level', 'school')  # 二本高校
        t12 = get_data('school_third_level', 'school')  # 三本高校
        t13 = get_data('school_special', 'school')  # 专科高校
        jx_error_list =  get_data('school_jx_error', 'jx_error')  # 简写错误词库
        school_985_list = [i[0] for i in t8]
        school_211_list = [i[0] for i in t9]
        school_first_list = [i[0] for i in t10]
        school_second_list = [i[0] for i in t11]
        school_third_list = [i[0] for i in t12]
        school_special_list = [i[0] for i in t13]
        adult_list = [i[0] for i in tt]  # 成人高校
        synonyms_history_list = [i[0] for i in t5]  # 同义词的历史曾用名
        synonyms_now_list = [i[1] for i in t5]  # 同义词的当前用名
        independent_list = [i[0] for i in t0]  # 独立院校词库
        sd_list = [i[0] for i in t1]  # 标准词库
        before_list = [i[0] for i in t2]  # 历史沿用名
        flast_list = [i[1] for i in t2]  # 对应历史沿用名的当前名
        full_list = [i[0] for i in t3]  # 全称
        jx_list = [i[1] for i in t3]  # 对应全称的简称列表
        big_school_list = [i[0] for i in t6]  # 解析的简历的高校
        error_contain_school = [i[0] for i in t7]  # 错误词库
        jx_error_dict = [i[0] for i in jx_error_list]  # 简写错误词库
        en_school = get_data('school_foreign_new', 'school_en', 'school_jx', 'school_zh','school_zh_link','rank', 'school_zh_jx')  # 国外大学
        ch_school = get_data('school_jx_en_dict_new', 'en_jx_name', 'school_en', 'school')  # 国内大学
        en_school_name = [i[0].lower() for i in en_school]
        en_school_jx = [i[1].lower() for i in en_school if i[1] != '']
        en_school_zh = [i[2].lower() for i in en_school]
        en_school_jx_zh = [i[2].lower() for i in en_school if i[1] != '']
        ch_school_en = ['' if i[1] is None else i[1].replace('\xa0', '').lower() for i in ch_school]
        new_ch_school_en = [i for i in ch_school_en if i != '']
        ch_school_jx = ['' if i[0] is None else i[0].replace('\xa0', '').lower() for i in ch_school]
        new_ch_school_jx = [i for i in ch_school_jx if i != '']
        new_ch_school_en_zh = [i[2].lower() for i in ch_school if i[1] is not None and i[1] != '']
        new_ch_school_jx_zh = [i[2].lower() for i in ch_school if i[0] is not None and i[0] != '']
        # 链接和世界排名
        zh_school_url = [i[1] for i in t1]
        en_school_url = [i[3] for i in en_school]
        en_school_rank = [i[4] for i in en_school]
        # 国外高校简写
        en_school_zh_jx = [i[5] for i in en_school if i[5] is not None and i[5] != '']
        en_school_zh_jx_zh = [i[2] for i in en_school if i[5] is not None and i[5] != '']
        return adult_list, synonyms_history_list, synonyms_now_list, independent_list, sd_list, before_list, flast_list, full_list, jx_list, big_school_list, error_contain_school, \
               school_985_list, school_211_list, school_first_list, school_second_list, school_third_list, school_special_list, jx_error_dict, \
               en_school_name, en_school_jx, en_school_zh, en_school_jx_zh, new_ch_school_en, new_ch_school_jx, new_ch_school_en_zh, new_ch_school_jx_zh, zh_school_url, en_school_url, en_school_rank, \
               en_school_zh_jx, en_school_zh_jx_zh

    def contain_school_en_jx(self, school):
        for element in self.en_school_jx_total:
            if school == element:
                return self.school_jx_dict.get(element,'')

    def contain_school_name(self, school):
        if len(school) > 0:
            s = []
            l = []
            for element in self.en_school_name_total:
                split_tmp = [reg.pattern2.sub('', i) for i in element.split(" ")]
                tmp = [i.strip() for i in split_tmp if i != '']
                split_set = set(tmp)
                intersect = split_set.intersection(school)
                if intersect != set() and set(tmp).issubset(intersect):
                    s.append(intersect)
                    l.append(element)

            middle = list(map(len, s))
            if len(middle) > 0:
                result = l[middle.index(max(middle))]
                return self.school_en_dict.get(result, '')

    # 判断是否在翻译的外国高校名中
    def contain_foreign_school(self, school):
        for element in self.only_en_school_zh:
            if element in school:
                return element


    def get_analysize_result(self, school):
        # 去掉university以及of the这样的单词
        school = school.lower()
        name = reg.pattern3.sub( '', school)
        split_list = [i for i in name.split(' ') if i != '']
        for element in split_list:
            en_jx_name = self.contain_school_en_jx(element)
            if en_jx_name is not None:
                return en_jx_name, self.school_en_zh_dict.get(en_jx_name, ''), True
        if reg.pattern1.search(school) != None:
            school_new = [reg.pattern2.sub('', i) for i in split_list]
            school_new = set([i for i in school_new if i != ''])
            # 判断是否在英文学校和中文学校中
            if school_new != set():
                zh_name = self.contain_school_name(school_new)
                if zh_name is None:
                    school_spell = get_spell(school_new)
                    new_name = self.contain_school_name(school_spell)
                    if new_name is None:
                        school = reg.pattern4.sub( '', school)
                        return None, school, False
                    else:
                        return new_name, self.school_en_zh_dict.get(new_name, ''), True
                else:
                    return zh_name, self.school_en_zh_dict.get(zh_name, ''), True
        else: # 有可能是翻译的中文
            school = self.contain_foreign_school(school)
            if school is not None:
                return school,self.school_en_zh_dict.get(school,''),True

    def analysis_school(self, school, num):
        label = False
        if num == 4:
            # 判断是否是成人高校
            adult_name = self.contain_adult(school)
            if adult_name is None:
                # 判断是否是独立院校
                independent_name = self.contain_independent(school)
                if independent_name is None:
                    # 判断名称是否在标准库中
                    st_name = self.contain_sd(school)
                    if st_name is None:
                        # 判断是否包含在历史合并表中
                        history_name = self.contain_history(school)
                        if history_name is None:
                            # 判断是否包含在同义词词库中
                            sy_name = self.contain_synonyms(school)
                            if sy_name is None:
                                # 判断简写是否在字符串中
                                school = self.filter_jx_error(school)
                                jx_name = self.contain_jx(school)
                                if jx_name is None:
                                    if self.get_analysize_result(school) is None:
                                        school = re.findall(r'^.*学院|^.*大学|^.*学校|^.*研究所|^.*研究院|^.*中科院|^.*美院|^.*职大|^.*职院|^.*师大|^.*师院', school)
                                        if len(school)>0:
                                            school = school[0]
                                            school = re.sub(u'[^\u4e00-\u9fa5a-zA-Z]', '', school)
                                            last_name = self.contain_big_school(school)
                                        else:
                                            return '', '', label
                                        if last_name is None:
                                            if len(school)<30:
                                                return school, self.school_en_zh_dict.get(school,''), label
                                            # return '未登录高校', label
                                            else:
                                                return '', '', False
                                        else:
                                            return last_name, self.school_en_zh_dict.get(last_name,''), label
                                    else:
                                        zh_name, en_name, label = self.get_analysize_result(school)
                                        return zh_name, en_name, label
                                else:
                                    if ('学院' not in school) and ('大学' not in school):
                                        label = True
                                        return jx_name, self.school_en_zh_dict.get(jx_name,''), label
                                    else:
                                        last_name = self.contain_big_school(school)
                                        if last_name is None:
                                            return school, self.school_en_zh_dict.get(school,''), label
                                        else:
                                            return last_name, self.school_en_zh_dict.get(last_name,''), label
                            else:
                                label = True
                                return sy_name, self.school_en_zh_dict.get(sy_name,''), label
                        else:
                            label = True
                            return history_name, self.school_en_zh_dict.get(history_name,''), label
                    else:
                        label = True
                        return st_name, self.school_en_zh_dict.get(st_name,''), label
                else:
                    label = True
                    return independent_name, self.school_en_zh_dict.get(independent_name), label
            else:
                label = True
                return adult_name,self.school_en_zh_dict.get(adult_name,''),label
        elif num ==3:
            if self.get_analysize_result(school) is None:
                label = False
                return '',school,label
            else:
                label = True
                zh_school, en_school, label = self.get_analysize_result(school)
                return zh_school,en_school,label
        else:
            return school, '', label


    def get_detail(self, school):
        if school in self.school_211_list:
            if school in self.school_985_list:
                group = 2
            else:
                group = 1
        else:
            group = 0
        # 判断学校的级别
        if school in self.school_first_list:
            level = 1
        elif school in self.school_second_list:
            level = 2
        elif school in self.school_third_list:
            level = 3
        elif school in self.school_special_list:
            level = 4
        else:
            level = 0
        return group, level

    def world_school_rank(self,school):
        if school in self.only_en_school_name:
            return self.en_school_rank_dict[school]
        else:
            return 0

    def get_url(self,zh_school,en_school):
        if zh_school in self.sd_list:
            school_url = self.zh_school_url_dict[zh_school]
            return school_url
        elif en_school in self.only_en_school_name:
            school_url = self.en_school_url_dict[en_school]
            return school_url

    def get_result(self, school):
        school_new = preprocess(school)
        num = judge_type(school_new)
        zh_school, en_school, label = self.analysis_school(school_new, num)
        world_rank = self.world_school_rank(en_school)
        learn_type = judge_special(school_new)
        group, level = self.get_detail(zh_school)
        if num == 1:
            school_type = 2
        elif num == 2:
            school_type = 3
        elif num == 3:
            school_type = 4
        elif (num == 4) and (en_school not in self.new_ch_school_en):
            school_type = 4
        elif (num == 4) and (en_school in self.new_ch_school_en):
            school_type = 1
        else:
            school_type = 0

        school_url = self.get_url(zh_school, en_school)

        normalize_result = {}
        now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        data = {}
        normalize_result['time'] = now_time
        data['old_name'] = school
        data['zh_name'] = zh_school
        data['en_name'] = en_school
        data['group'] = group
        data['level'] = level
        data['type'] = school_type
        data['is_full_time'] = learn_type
        data['is_standard'] = label
        data['world_rank'] = world_rank
        data['url'] = school_url
        if school_type != 0:
            normalize_result['success'] = True
            normalize_result['data'] = data
            normalize_result['message'] = ''
            return normalize_result
        else:
            normalize_result['success'] = False
            normalize_result['data'] = {}
            normalize_result['message'] = '标准化失败'
            return normalize_result