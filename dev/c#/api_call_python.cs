using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using System.IO;

namespace ConsoleApplication3
{
    class Program
    {
        static void Main(string[] args)
        {
            string url = "http://120.55.168.18:8839/job_parse";
            string Text = File.ReadAllText(@"D:\a.json");

            //var parameterJson = Newtonsoft.Json.JsonConvert.SerializeObject(new {  Text });
            HttpClient hcParse = new HttpClient();

            var responseParse = hcParse.PostAsync(url, new StringContent(Text, System.Text.Encoding.UTF8, "application/text")).Result;
            var contentParse = responseParse.Content.ReadAsStringAsync().Result; 
            var obj = Newtonsoft.Json.JsonConvert.DeserializeObject<dynamic>(contentParse);
            //Console.WriteLine(obj.ExtractResult.Value.Text);
        }
    }
}
