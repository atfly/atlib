using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using com.hankcs.hanlp;
using System.IO;
using JiebaNet.Segmenter;
using JiebaNet.Analyser;

using System.Text.RegularExpressions;



namespace ConsoleApplication9
{
    class Program
    {
        static void Main(string[] args)
        {
            System.Text.RegularExpressions.Regex id = new System.Text.RegularExpressions.Regex(@"(QQ\s*：\s*\d{4,})");


            var t = id.Match("在线QQ：  1361125166  个人主页：  http:/");

            Console.WriteLine(t.Value.ToString());









            // java.lang.System.getProperties().setProperty("java.class.path", "D:\\hanlp\\");
            // //Console.WriteLine(HanLP.segment("你好，欢迎在CSharp中调用HanLP的API！"));

            // //Console.WriteLine(HanLP.extractPhrase("你好，欢迎在CSharp中调用HanLP的API！", 5));

            // //Console.WriteLine(HanLP.extractKeyword("你好，欢迎在CSharp中调用HanLP的API！", 5));


            // //Console.WriteLine(HanLP.extractSummary("你好，欢迎在CSharp中调用HanLP的API！", 5));

            // //Console.WriteLine(HanLP.getSummary("你好，欢迎在CSharp中调用HanLP的API！", 5));

            // //Console.WriteLine(HanLP.parseDependency("你好，欢迎在CSharp中调用HanLP的API！"));


            // var seg = HanLP.newSegment();

            // //seg.enableNumberQuantifierRecognize(true);
            // // seg.enableOffset(true);

            // //seg.enableOrganizationRecognize(true);

            // // seg.enablePlaceRecognize(true);
            // //seg.enableMultithreading(true);





            // var txt = File.ReadAllText(@"C:\Users\Alex\Desktop\简历解析优化\TxtResumes\text.txt");
            // var segmenter = new JiebaSegmenter();
            // var segments = segmenter.Cut(txt, cutAll: false);

            //foreach (var str in segments)
            // {
            //     Console.WriteLine(str.ToString());
            // }





            // //Console.WriteLine(HanLP.segment(txt));

            // //Console.WriteLine(HanLP.extractPhrase(txt, 100));

            // //Console.WriteLine(HanLP.extractKeyword(txt, 5));


            // //Console.WriteLine(HanLP.extractSummary(txt, 500));

            // // Console.WriteLine(HanLP.getSummary(txt, 1000));

            // // Console.WriteLine(HanLP.parseDependency(txt));

            // //seg.enableOffset(true);
            // //Console.WriteLine(seg.seg(txt.ToString()));

            // //foreach (var txt1 in seg.seg2sentence(txt).toArray())
            // //{
            // //    Console.WriteLine(seg.seg2sentence(txt1.ToString()));


            // //}

            // // HanLP.CoreSynonymDictionary




            Console.ReadKey();
        }
    }
}