using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using CsvHelper;
using System.Text;
using CsvReaderWriter;



namespace ConsoleApplication8
{
    class Program
    {
        static void Main(string[] args)
        {
            var _resumeText = "abc$123d$df";


            var title = _resumeText.Substring(0, _resumeText.IndexOf("$"));
            _resumeText = _resumeText.Substring(_resumeText.IndexOf("$") + 1);






            //var reader = new CsvReader(new StreamReader("D:/train_all.csv", System.Text.Encoding.GetEncoding("GB2312")));


            //while (reader.Read())
            //{


            //    Console.WriteLine(reader.GetField(2));



            //}

            var records = new List<string>();
            records.Add("hello");
            records.Add("world");




            using (var writer = new CsvWriter(new StreamWriter("D:/train_all_writer.csv")))
            {
                writer.WriteField("hello");
                writer.WriteField("hello");
            }




            //var text = new CsvWriter<string>();
            //text.Write(new StreamWriter("D:/train_all_writer.csv"), records);






            //writer.WriteRecords(records);

            //writer.Flush();








        }
    }
}
