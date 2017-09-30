using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text;
using System.Text.RegularExpressions;
using System.IO;

namespace ConsoleApplication4
{
    class Program
    {
        static Regex _RegForNumbers = new Regex(@"\d+", RegexOptions.Compiled);
        static Regex _RegForDigit = new Regex(@"\d", RegexOptions.Compiled);
        static Regex _RegForNoise = new Regex(@"[\u4e00-\u9fa5a-zA-Z]", RegexOptions.Compiled);
        //add regex for phone for filter phone
        static Regex _RegForPhone = new Regex(@"((\d{11})|^((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})))", RegexOptions.Compiled);
        static Regex _RegForChineseMobile = new Regex(@"(13\d|14[57]|15[^4,\D]|17[13678]|18\d)\d{8}|170[0589]\d{7}", RegexOptions.Compiled);
        static Regex _RegInternationalMobile = new Regex(@"^5997|^5994|^5993|^1876|^1869|^1868|^1809|^1784|^1767|^1758|^1721|^1684|^1671|^1670|^1664|^1649|^1473|^1441|^1345|^1340|^1284|^1268|^1264|^1246|^1242|^999|^998|^996|^995|^994|^993|^992|^977|^976|^975|^974|^973|^972|^971|^970|^968|^967|^966|^965|^964|^963|^962|^961|^960|^888|^886|^883|^882|^881|^880|^879|^878|^877|^876|^875|^870|^856|^855|^853|^852|^851|^850|^692|^691|^690|^689|^688|^687|^686|^685|^684|^683|^682|^681|^680|^679|^678|^677|^676|^675|^674|^673|^672|^671|^670|^598|^597|^596|^595|^594|^593|^592|^591|^590|^509|^508|^507|^506|^505|^504|^503|^502|^501|^500|^423|^421|^420|^389|^387|^386|^385|^383|^382|^381|^380|^379|^378|^377|^376|^375|^374|^373|^372|^371|^370|^359|^358|^357|^356|^355|^354|^353|^352|^351|^350|^299|^298|^297|^291|^290|^269|^268|^267|^266|^265|^264|^263|^262|^261|^260|^258|^257|^256|^255|^254|^253|^252|^251|^250|^249|^248|^247|^246|^245|^244|^243|^242|^241|^240|^239|^238|^237|^236|^235|^234|^233|^232|^231|^230|^229|^228|^227|^226|^225|^224|^223|^222|^221|^220|^218|^216|^213|^212|^211|^210|^98|^95|^94|^93|^92|^91|^90|^84|^82|^81|^66|^65|^64|^63|^62|^61|^60|^58|^57|^56|^55|^54|^53|^52|^51|^49|^48|^47|^46|^45|^44|^43|^41|^40|^39|^36|^34|^33|^32|^31|^30|^27|^20|^1", RegexOptions.Compiled);


        static void Main(string[] args)
        {
            var lines = File.ReadAllLines(@"d:/phone.txt");
            foreach (var item in lines)
            {


                string code = string.Empty;
                string num = string.Empty;
                var phone = StandardPhone(item);

                if (phone != null)
                {
                    code = phone.CountryCode == null ? string.Empty : phone.CountryCode;
                    num = phone.Number == null ? string.Empty : phone.Number;

                }


                string txt = string.Format("orginal:{0};country_code:{1},phone_number{2}{3}", item, code, num, System.Environment.NewLine);

                File.AppendAllLines(@"d:/process.txt", new List<string>() { txt });
            }
        }

        public static MobileInfo StandardPhone(string phone)
        {

            MobileInfo standardMobile = new MobileInfo();
            if (string.IsNullOrWhiteSpace(phone))
                return null;


            string noiseChar = @"[^\d-+()—_\s]";
            var items = Regex.Replace(phone, noiseChar, ";").Split(';');

            foreach (var item in items)
            {
                StringBuilder num = new StringBuilder();
                MatchCollection mc = _RegForDigit.Matches(item);

                //提取数字
                foreach (Match m in mc)
                {
                    if (m.Success)
                    {
                        num.Append(m.Value);
                    }
                }


                if (item.Trim() == string.Empty || num == null || num.Length <= 7 || num.Length > 15)
                    continue;


                //匹配中国手机
                var chineseMobile = _RegForChineseMobile.Matches(num.ToString());
                if (chineseMobile.Count > 0)
                {
                    standardMobile.Number = chineseMobile[0].Value.ToString();
                    standardMobile.CountryCode = "86";
                }

                //匹配已00或+开始的标准国际手机号码
                else if ((item.Contains("+") && item.IndexOf("+") <= item.IndexOf(num[0].ToString())) ||
                    (num[0].ToString() == "0" && num[1].ToString() == "0"))
                {

                    if (num[0].ToString() == "0" && num[1].ToString() == "0")
                    {
                        num.Remove(0, 2);
                    }
                    var stdPhone = _RegInternationalMobile.Match(num.ToString());

                    if (stdPhone.Success && stdPhone.Value != null && (num.Length - stdPhone.Value.Length) >= 7)
                    {
                        standardMobile.Number = num.Remove(0, stdPhone.Value.Length).ToString();
                        standardMobile.CountryCode = stdPhone.Value;
                    }

                }

            }


            return standardMobile;

        }

        public class MobileInfo
        {


            public string CountryCode { get; set; }

            public string Number { get; set; }

        }
    }
}
