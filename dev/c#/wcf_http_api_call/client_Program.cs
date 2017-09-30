using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Http;
using System.IO;
using RestSharp;


namespace ConsoleApplication5
{
    class Program
    {
        static void Main(string[] args)
        {

            string filePath = @"D:\rcbox.txt";
            string wcfApiUrl = "http://localhost:18018/api/extractdocument";

          
            HttpClient hc = new HttpClient();
            var parameterJson = Newtonsoft.Json.JsonConvert.SerializeObject(new { Path = filePath, Options = new[] { 1 } });



            var response = hc.PostAsync(wcfApiUrl, new StringContent(parameterJson, System.Text.Encoding.UTF8, "application/json")).Result;
            var content = response.Content.ReadAsStringAsync().Result;

            var obj=Newtonsoft.Json.JsonConvert.DeserializeObject<dynamic>(content);
            Console.WriteLine(obj.ExtractResult.Value.Text);

           

            Console.Read();
        }
    }

   
}
