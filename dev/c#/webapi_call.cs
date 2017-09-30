using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using System.IO;



namespace ConsoleApplication10
{
    class Program
    {
        static void Main(string[] args)
        {


          
 
            string extractUrl = "http://localhost:50447/Document/Extract";
            var data=File.ReadAllBytes(@"C:\Users\Alex\Desktop\简历解析优化\log谷露后同步51 (1)\gllue_web11_1494211349.html");

            HttpClient hcExtract = new HttpClient();
            var parameterJsonExtracct = Newtonsoft.Json.JsonConvert.SerializeObject(new { ExtensionName = ".html",Data= data });

            var responseExtract = hcExtract.PostAsync(extractUrl, new StringContent(parameterJsonExtracct, System.Text.Encoding.UTF8, "application/json")).Result;
            var contentExtract = responseExtract.Content.ReadAsStringAsync().Result;



            string wcfApiUrl = "http://localhost:50447/Resume/Parse";
            string Text = contentExtract;
           
            var parameterJson = Newtonsoft.Json.JsonConvert.SerializeObject(new { Text = Text });
            HttpClient hcParse = new HttpClient();
            
            var responseParse = hcParse.PostAsync(wcfApiUrl, new StringContent(parameterJson, System.Text.Encoding.UTF8, "application/json")).Result;
            var contentParse = responseParse.Content.ReadAsStringAsync().Result;

            //var obj = Newtonsoft.Json.JsonConvert.DeserializeObject<dynamic>(content);
            //Console.WriteLine(obj.ExtractResult.Value.Text);


        }
    }
}
