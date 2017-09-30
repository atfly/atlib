package udf;

import com.aliyun.odps.udf.UDF;

public class ETLString extends UDF {
    // TODO define parameters and return type, e.g:  public String evaluate(String a, String b)
    public String evaluate(String s) {
        return etlString(s);
    }


    public static final String expression = "[\\s\\p{Punct}]+";

    public static final  String CNpunct="。？，！、；：‘’“”（）-《》〈〉。？，！＼；：‘’“”（）－《》";
    public static final  String ENpunct=".?,!,;:''\"\"()-<><>-";


    public static String etlString(String input){
        String etl1 = input.replaceAll("[\\r\\n]+",".").replaceAll("[\\f\\t\\v]+",",");
//        System.out.println(etl1);
        String etl2 = etl1.replaceAll("[   ]+","."); //特殊空白
//        System.out.println(etl2);
        String etl3 = etl2.replaceAll("[\\x14\\x15\\x0b\\xc2\\xa0]+","."); //特殊unicode字符
//        System.out.println(etl3);

        StringBuilder etl4 = new StringBuilder(); //中文标点
        char[] toCharArray = etl3.toCharArray();
        for(char c : toCharArray){
            if(isChinesePunctuation(c)){
                etl4.append(",");
            }else{
                etl4.append(c);
            }
        }
        return etl4.toString().replaceAll("[,]+",",").toLowerCase(); //去掉连续逗号 + 英文字符小写
    }





    /**
     *     使用UnicodeScript方法判断汉字字符
     */
    public static boolean isChineseByScript(char c) {
        Character.UnicodeScript sc = Character.UnicodeScript.of(c);
        if (sc == Character.UnicodeScript.HAN) {
            return true;
        }
        return false;
    }

    /**
     *     根据UnicodeBlock方法判断中文标点符号
     * 因为中文的标点符号主要存在于以下5个UnicodeBlock中，
     U2000-General Punctuation (百分号，千分号，单引号，双引号等)
     U3000-CJK Symbols and Punctuation ( 顿号，句号，书名号，〸，〹，〺 等；PS: 后面三个字符你知道什么意思吗？ : )    )
     UFF00-Halfwidth and Fullwidth Forms ( 大于，小于，等于，括号，感叹号，加，减，冒号，分号等等)
     UFE30-CJK Compatibility Forms  (主要是给竖写方式使用的括号，以及间断线﹉，波浪线﹌等)
     UFE10-Vertical Forms (主要是一些竖着写的标点符号，    等等)
     */
    public static boolean isChinesePunctuation(char c) {
        Character.UnicodeBlock ub = Character.UnicodeBlock.of(c);
        if (ub == Character.UnicodeBlock.GENERAL_PUNCTUATION
                || ub == Character.UnicodeBlock.CJK_SYMBOLS_AND_PUNCTUATION
                || ub == Character.UnicodeBlock.HALFWIDTH_AND_FULLWIDTH_FORMS
                || ub == Character.UnicodeBlock.CJK_COMPATIBILITY_FORMS
                || ub == Character.UnicodeBlock.VERTICAL_FORMS) {
            return true;
        } else {
            return false;
        }
    }


    public static void main(String[] args){

        String text = "简历名称：  工作在前线。。。  智联招聘\n" +
                " 期望从事职业：  互联网产品经理/主管、网络运营管理、互联网产品专员/助理、电...\n" +
                "   简历更新时间：  2015.11.26\n" +
                "   ID：JR093710323R90000002000                                                                       \n" +
                "xxx  手机：xxx\n" +
                "   男    29岁(1987年11月)    6年工作经验    本科    未婚\n" +
                "现居住地：深圳 | 户口：宜昌 | 团员\n" +
                " \n" +
                "  \n" +
                " \n" +
                " 身份证：420502198711291356\u000B手机：xxx\u000BE-mail：xxx \u0014xxx\u0015\n" +
                " \n" +
                " 求职意向                                                               \n" +
                "期望工作地区：  深圳\n" +
                " 期望月薪：  8001-10000元/月\n" +
                " 目前状况：  我目前处于离职状态，可立即上岗\n" +
                " 期望工作性质：  《全职》\n" +
                " 期望从事职业：  互联网产品经理/主管、网络运营管理、互联网产品专员/助理、电子商务经理/主管、网站编辑\n" +
                " 期望从事行业：  政府/公共事业/非盈利机构、媒体/出版/影视/文化传播、互联网/电子商务、广告/会展/公关、IT服务(系统/数据/维护)、网络游戏\n" +
                " 自我评价                                                               \n" +
                "1.工作认真负责，性格沉稳、数据分析能力较强\u000B2.注重团队合作和创新，勇于接受挑战，有强烈的责任感\u000B3.有强烈的上进心和求知欲，学习能力强，可以适应快节奏工作\u000B4.具有良好沟通协调能力，以及优秀的合作精神及抗压能力\u000B5.有文案基础和文章撰写能力，具备软文/评测/合辑等类型文章的发表经验与经历，拥有良好的行业（移动互联网）敏锐度 \u000B6.有丰富的网站/论坛/专题策划经历，具备良好的网站/论坛/专题策划能力 \u000B7.具有产品运营经历，对外推广、客户维护经验 \n" +
                "工作经历                                                               \n" +
                "2014.07 - 至今  招商银行旗下招联金融有限公司  （1年6个月） \n" +
                "   互联网产品运营经理 | 10001-15000元/月 \n" +
                "   互联网/电子商务 | 企业性质：合资 | 规模：100-499人 \n" +
                "   工作描述：  1、产品培训：\u000B负责本行移动端产品的知识培训，（产品类似京东白条、腾讯微粒贷），便于上线前内部运营、客服的知识面得到充足的理解\u000B2、产品测试：\u000B测试产品的稳定性、查看数据、与开发头脑风暴优化产品性能，充分测试产品体验度的Bug与操作习惯\u000B3、调研分析：\u000B通过内部访谈测试和数据分析，探索产品优化方向；分析产品操作体验度及交易过程，并撰写报告\u000B4、职责描述：\u000B产品定位：前期市场调研，产品市场切入点分析、收集竞争对手分析；\u000B产品规划：核心用户需求分析、需求规划\u000B产品设计：分析用户应用场景，协调UE/UI设计\u000B研发推进：需求讲解、评审，制定项目计划\u000B组内沟通：推动整个开发过程，跟踪并及时落实需求\u000B运营管理：各大应用市场上传前预热，申请首发准备工作，上线后的上线报告、结项报告\u000B数据报告：周报、月报、季报、半年报、年报 \n" +
                " \n" +
                "2011.05 - 2014.05  腾讯控股有限公司  （3年） \n" +
                "   互联网产品专员 | 6001-8000元/月 \n" +
                "   互联网/电子商务 | 企业性质：股份制企业 | 规模：10000人以上 \n" +
                "   工作描述：  一、流程更新、梳理：\u000B负责所有财付通个人业务梳理：理财通、AA收款、微信红包、信用卡还款、提现、购买公司业务、活动等\u000B1、对于产品bug优化，及时在内网更新流程，便于客服更好的向用户做好解释工作\u000B2、梳理已知故障、流程等问题，第一时间联系产品、开发确认信息并及时解决，通知客服了解最新知识或流程\u000B二、优化产品的需求推动：\u000B1、官网页面或操作流程有问题，尽快与产品、开发同事沟通，并催促优化，如需排期的需求、BUG优化、事件故障等需求单，催促运维尽快处理\u000B2、对日常使用的数据库、账务系统、病例库、处方库、客服系统、req事件表等有更好的优化建议，及时反馈给相关同事协助推动，便于操作快捷、简单 \u000B3、处理投诉工单，解决客服同事无法处理的问题，帮助用户尽快处理疑问，配合产品、开发及其他同事对产品进行优化和测试工作\u000B三、协助工作，解决问题：\u000B1、关注客服同事投诉量大的问题，跟进问题并且在第一时间处理，协助产品、技术同事优化繁琐的业务处理流程，缩短问题处理时间。例如之前购买公司业务所涉及的退款都需人工操作领导审批财务付款，繁琐并且难免会有错误，推动并讨论优化后，每周一次的退款已大大减少了用户的投诉量，也减少了客服、财务同事的负担。\u000B2、定期分享业务盲点，客服同事也是用户，他们接触用户最能懂用户需要什么，通过分享，不仅可以帮助客服同事了解并熟悉盲点业务流程，更好、更快的为用户解决问题，并且可以更直观的了解到客服同事对于产品知识的看法，从而收集问题推动产品优化 \n" +
                " \n" +
                "2010.09 - 2011.02  深圳泡椒思志信息技术有限公司  （5个月） \n" +
                "   网站运营 产品编辑评测 | 4001-6000元/月 \n" +
                "   互联网/电子商务 | 企业性质：民营 | 规模：100-499人 \n" +
                "   工作描述：  1、公司网站的内容运营，发表高质量的行业资讯、评测、专题等\u000B2、手机产品（软件、游戏）专题策划，参与网站的版面策划，并给出可行性方案\u000B3、公司产品上线测试以及版本更新、Bug反馈跟进\u000B4、网站后台数据统计（自己所参与编辑所写文章也为该网站带来可观流量）参与手机游戏论坛版块炒作话题，制定论坛规章制度 \n" +
                " \n" +
                "2007.10 - 2008.01  武汉商报  （3个月） \n" +
                "   编辑部 | 编辑/撰稿 | 1000-2000元/月 \n" +
                "   媒体/出版/影视/文化传播 | 企业性质：事业单位 | 规模：100-499人 \n" +
                "   工作描述：  实习。。策划会员活动，与会员建立良好关系！\u000B深度挖掘客户需求，并与上级共同策划活动与吸引会员量！ \n" +
                " 项目经历                                                              \n" +
                "2007.01 - 2007.12  采购 \n" +
                "    \n" +
                "教育经历                                                              \n" +
                "2006.09 - 2010.06  湖北大学  传播学  本科 \n" +
                " 培训经历                                                              \n" +
                "2011.06 - 2013.09  英语 \n" +
                "   培训机构：  华尔街英语培训机构\n" +
                " 培训地点：  深圳市福天区车公庙华尔街英语培训机构\n" +
                " 在校学习情况                                                           \n" +
                "活动描述：  2008年汶川地震志愿者！！组织各大高校联谊为灾区献力！ \n" +
                " 语言能力                                                               \n" +
                "英语：读写能力一般 | 听说能力一般 \n" +
                " 专业技能                                                               \n" +
                "网络编辑：良好 | 7个月 \n" +
                " \f";

        System.out.println(etlString(text));
    }
}