#match����ֻ���RE�ǲ�����string�Ŀ�ʼλ��ƥ�䣬 search��ɨ������string����ƥ��
def isMatch(pattern,text):
    if re.compile(pattern).search(text):
        return 1
    else:
        return 0
        

========================================================================================================
#ͨ��������װ���е�����ı��ʽ		
import re

class Reg_Exp(object):
    # ��������ģʽ(�޳�html�����һЩ�ַ�)
    pt1 = re.compile("nbsp|0pt'>")
    # ����
    pt2 = re.compile('\d{2,4}��\d{1,2}��')
    # ��ƥ���ȫ���Ƶ�
    r0 = re.compile(u'�Կ�|Զ��|�ɽ�|�������|��������|����ѧԺ|��ѧ����|���˽���|����|Զ�̽���|���Ӵ�ѧ|���^(ѧ)')
    # ����
    r1 = re.compile(u'ְ��|��ѧ|([һ�����������߰˾�ʮ]+|[0-9])��|����')
    # ��ר��У
    r2 = re.compile(u'ְҵѧУ|ְУ|��У|����ѧУ|��ѵѧУ|[^(�ߵ�ר��|˰��ר��|ʦ��ר��|ҽѧר��)]ѧУ')
    # �����ѧ
    r3 = re.compile('academy|institute|school|college|association|univ.*')
    # ȫ�����ĵĴ�ѧ
    r4 = re.compile(r'��ѧ|ѧԺ|ר��ѧУ|�о���|�о�Ժ|�п�Ժ')
    pattern1 = re.compile('academy|institute|school|college|association|univ.*')
    pattern2 = re.compile('academy|institute|school|college|association|univ.*|of|the|and|for')
    pattern3 = re.compile('[^\u4e00-\u9fa5a-zA-Z ]')
    pattern4 = re.compile('[^a-zA-Z ]')