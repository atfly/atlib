using System;
using System.Collections.Generic;
using System.Linq;

using System.Threading.Tasks;
using System.Threading;
using System.IO;

using System.Text.RegularExpressions;
namespace Hirede.ResumeParse.Batch
{
    class Program
    {
        public static string resumeDir = System.Configuration.ConfigurationManager.AppSettings["ResumeDir"];
        public static int runningThreads = int.Parse(System.Configuration.ConfigurationManager.AppSettings["RunningThreads"]);
        public static int maxThreads = int.Parse(System.Configuration.ConfigurationManager.AppSettings["MaxThreads"]);
        public static int interval = int.Parse(System.Configuration.ConfigurationManager.AppSettings["Interval"]);
        public static int batch= int.Parse(System.Configuration.ConfigurationManager.AppSettings["Batch"]);

        private static readonly Regex cjkCharRegex = new Regex(@"\p{IsCJKUnifiedIdeographs}", RegexOptions.Compiled);
        private static readonly Regex isEnRegex = new Regex("[a-zA-Z]", RegexOptions.Compiled);
        static void Main(string[] args)
        {


            if (Directory.Exists(resumeDir))
            {
                double extractTotalMS = 0;
                double parserTotalMS = 0;
                DateTime dt = DateTime.Now;

                int loop = 0;

                List<string> resumes = Directory.GetFileSystemEntries(resumeDir).ToList<string>();

                //foreach (string item in resumes)
                //{
                //    loop++;

                //    //resume extractor
                //    DateTime extractStart = DateTime.Now;
                //    string txt = ResumeExtract(item.ToString());
                //    double extractCost = (DateTime.Now - extractStart).TotalMilliseconds;
                //    extractTotalMS = extractTotalMS + extractCost;

                //    Console.WriteLine("Resume Extract time : {0} file : {1} language : {2} current_time_cost_ms : {3} total_resumes : {4} total_time_cost_ms : {5} extract_file_per_second : {6}",
                //        DateTime.Now, item.ToString(), GetResumeLanguage(txt), extractCost, loop, extractTotalMS, loop * 1000 / extractTotalMS);


                //    if (loop % 60 == 0)
                //    {
                //        Thread.Sleep(interval);
                //    }
                //}

                Parallel.ForEach(resumes, new ParallelOptions { MaxDegreeOfParallelism = maxThreads }, (item, loopState) =>
                {
                    loop++;

                    //resume extractor
                    DateTime extractStart = DateTime.Now;
                    string txt = ResumeExtract(item.ToString());
                    double extractCost = (DateTime.Now - extractStart).TotalMilliseconds;
                    extractTotalMS = (DateTime.Now - dt).TotalMilliseconds; 

                    Console.WriteLine("Resume Extract time : {0} file : {1} language : {2} current_time_cost_ms : {3} total_resumes : {4} total_time_cost_ms : {5} extract_file_per_second : {6}",
                        DateTime.Now, item.ToString(), GetResumeLanguage(txt), extractCost, loop, extractTotalMS, loop * 1000 / extractTotalMS);

                    //sleep
                    if (loop % batch == 0)
                    {
                        Thread.Sleep(interval);
                    }
                    //resume parser 
                    if (!string.IsNullOrEmpty(txt) && GetResumeLanguage(txt) == "zh")
                    {
                        DateTime parserStart = DateTime.Now;
                        string score = ResumeParse(txt);

                        double parserCost = (DateTime.Now - parserStart).TotalMilliseconds;
                        parserTotalMS = (DateTime.Now - dt).TotalMilliseconds; ;

                        Console.WriteLine("Resume Parser time: {0} file : {1} score : {2} current_time_cost_ms : {3} total_resumes : {4} total_time_cost_ms : {5} parse_file_per_second : {6}",
                        DateTime.Now, item.ToString(), score, parserCost, loop, parserTotalMS, loop * 1000 / parserTotalMS);

                    }


                   

                });

            }
            else
            {
                Console.WriteLine("Resume Dir not existed");
            }

            Console.Read();

        }




        public static bool IsChinese(char c)
        {
            return cjkCharRegex.IsMatch(c + "");
        }

        public static string GetResumeLanguage(string txt)
        {
            if (string.IsNullOrEmpty(txt))
            {
                return string.Empty;
            }
            var numberOfChinese = txt.Count(c => IsChinese(c));
            if (numberOfChinese > 60 || ((double)numberOfChinese) / txt.Length >= 0.15)
            {
                return "zh";
            }

            return "en";
        }

        public static string ResumeExtract(string resumeFile)
        {
            string resultStr = string.Empty;
            try
            {
                using (DocumentExtract.DocumentExtractServiceClient client = new DocumentExtract.DocumentExtractServiceClient("DocumentExtractService3"))
                {
                    var result = client.Extract(Path.GetExtension(resumeFile), GetFileData(resumeFile), new DocumentExtract.ExtractOption[] { DocumentExtract.ExtractOption.Text, DocumentExtract.ExtractOption.Image });
                    if (result.Value != null)
                    {

                        resultStr = result.Value.Text;

                    }

                } 
            
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }



            return resultStr;

        }


        public static string ResumeParse(string txt)
        {
            string resultScore = string.Empty;
            try
            {
                Service.Contract.ResumeText rt = new Service.Contract.ResumeText();
                rt.Text = txt;
                using (ResumeParse.ResumeParseServiceClient client = new ResumeParse.ResumeParseServiceClient())
                {
                    resultScore = client.ParseRawResume(null, rt).CompletionBoost.ToString();

                }
                    

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);

            }
            return resultScore;

        }

        /// <summary>
        /// 将文件转换成byte[] 数组
        /// </summary>
        /// <param name="fileUrl">文件路径文件名称</param>
        /// <returns>byte[]</returns>
        public static byte[] GetFileData(string fileUrl)
        {
            FileStream fs = new FileStream(fileUrl, FileMode.Open, FileAccess.Read);
            try
            {
                byte[] buffur = new byte[fs.Length];
                fs.Read(buffur, 0, (int)fs.Length);

                return buffur;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return null;
            }
            finally
            {
                if (fs != null)
                {

                    fs.Close();
                }
            }
        }






    }

}
