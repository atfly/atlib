using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Baza.MailFetching.Services
{
    public class ResumeDetector
    {
        private static readonly Regex _WhiteBlankRegex = new Regex(@"\s+", RegexOptions.Compiled);
        private static readonly IDictionary<string, string[]> _Patterns = new Dictionary<string, string[]>
        {
            { "main", new []{ "求职意向", "求职状态", "教育背景", "教育经历", "个人资料", "实习经历", "期望薪水", "居住地", "自我评价" } },
            { "base", new []{ "姓名", "手机", "电话", "邮箱", "e-mail", "年龄", "籍贯",
                "通讯地址", "居住地", "户口", "性别", "男", "女", "信箱", "邮件" } },
            { "education", new []{ "毕业学校", "毕业院校", "教育背景", "专业", "学历", "大专", "专科", "本科", "硕士", "博士", "研究生" } },
            { "job", new []{ "求职意向", "应聘职位", "求职类型", "工作经历", "工作经验", "职位",
                "项目经历", "项目", "工作职责", "工作地点", "工作地区", "个人描述", "个人技能",
                "个人经历", "实习经历", "自我评价", "个人情况", "兴趣", "工作业绩", "工作简历" } }
        };

        public static bool Detect(string text)
        {
            if (!string.IsNullOrEmpty(text))
            {
                text = _WhiteBlankRegex.Replace(text, "");
                if (string.IsNullOrEmpty(text))
                    return false;

                text = text.ToLower();
                var baseItems = _Patterns["base"].Select(i => text.IndexOf(i)).Where(i => i >= 0).ToArray();
                var educationItems = _Patterns["education"].Select(i => text.IndexOf(i)).Where(i => i >= 0).ToArray();
                var jobItems = _Patterns["job"].Select(i => text.IndexOf(i)).Where(i => i >= 0).ToArray();
                var half = text.Length / 2;
                if (baseItems.Length > 0 && jobItems.Length > 0)
                {
                    if (baseItems.Min() <= jobItems.Min() && baseItems.Min() < half)
                        return true;

                    if (educationItems.Length > 0 && educationItems.Min() < half && baseItems.Min() < educationItems.Min())
                        return true;

                    return _Patterns["main"].Any(text.Contains);
                }

                if (jobItems.Length > 0 && educationItems.Length > 0 && _Patterns["main"].Any(text.Contains))
                    return true;

                if (baseItems.Length >= 2 && jobItems.Length == 0 && educationItems.Length >= 2)
                    return true;

                if (jobItems.Length >= 2 && educationItems.Length >= 2)
                    return true;
            }
            return false;
        }
    }
}