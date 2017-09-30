using Baza.ComponentModel;
using System.ServiceModel;
using System.ServiceModel.Web;

namespace Baza.DocumentExtractService.Contract
{
    /// <summary>
    /// v3.0文档抽取接口,支持头像的抽取
    /// </summary>
    [ServiceContract]
    public interface IDocumentExtractService
    {
        /// <summary>
        /// 从文本数据中抽取内容
        /// </summary>
        /// <param name="extensionName"></param>
        /// <param name="data"></param>
        /// <param name="options"></param>
        /// <returns></returns>
        [OperationContract]
        [WebInvoke(Method = "POST", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json, UriTemplate = "ExtractDocument", BodyStyle = WebMessageBodyStyle.Wrapped)]
        InvokedResult<ExtractedResult> Extract([MessageParameter(Name = "Path")] string path, [MessageParameter(Name = "Options")] ExtractOption[] options);
    }
}
