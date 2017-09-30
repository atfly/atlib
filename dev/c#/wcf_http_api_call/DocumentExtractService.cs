
using Baza.ComponentModel;
using Baza.DocumentExtractService.Contract;
using Baza.Infrastructure.Logging;
using System;
using System.IO;
using System.Net;

namespace Baza.DocumentExtractService
{
    public class DocumentExtractService : IDocumentExtractService
    {
        /// <summary>
        /// 抽取入口
        /// </summary>
        /// <param name="extensionName">文档后缀名</param>
        /// <param name="data">文档二进制数据</param>
        /// <param name="Options">抽取参数</param>
        /// <returns></returns>
        public InvokedResult<ExtractedResult> Extract(string path, ExtractOption[] options)
        {
            InvokedResult<ExtractedResult> result = new InvokedResult<ExtractedResult>();

            ExtractOption ops = CombineOptions(options);

            var extensionName = System.IO.Path.GetExtension(path);

            var extractors = Extractor.ExtractorFactory.GetExtractors(extensionName);
            if (extractors == null || extractors.Count == 0)
            {
                result.Code = (int)HttpStatusCode.BadRequest;
                result.Message = "没有对应的处理程序";
                return result;
            }

            bool success = false;
            if (!File.Exists(path))
            {
                result.Code = (int)HttpStatusCode.BadRequest;
                result.Message = "不存在该文件:" + path;
                return result;
            }

            var data = File.ReadAllBytes(path);
            try
            {
                //对于有多个处理程序的 按次序执行；如果抽取成功，后面的不再执行
                foreach (var extractor in extractors)
                {

                    result.Value = extractor.Extract(extensionName, data, (ExtractOption)ops);
                    if (result.Value == null)
                        continue;

                    success = true;
                    break;//如果能正常抽取规则，后面的不再执行
                }
            }
            catch (Exception ex)
            {
                result.Code = (int)HttpStatusCode.InternalServerError;
                result.Message = "抽取出错(3)：" + ex.Message + Environment.NewLine + ex.StackTrace;
                Logger.WriteError("ExtractText", ex);
            }
            if (!success)
            {
                result.Code = (int)HttpStatusCode.InternalServerError;
                result.Message = "抽取出错";
                //抽取不成功的记录下来，以便后面继续改进
                FileHelper.DataToFileAsync("_err_" + extensionName, data);
            }
            return result;
        }

        private ExtractOption CombineOptions(ExtractOption[] options)
        {
            ExtractOption ops = (ExtractOption)default(int);
            if (options != null && options.Length > 0)
            {
                foreach (ExtractOption item in options)
                {
                    ops = ops | item;
                }
            }
            return ops;
        }
    }
}
