//����
Regex.Replace("hello�������", "[^\u4e00-\u9fa5]", " ").Trim().ToUpper() + " " 

//ʱ��
var pattern_time = new Regex("((((19[6789][0-9]|20[01][0-9])\\s*(��|/|[.]|-|��|�C))(\\s*(1[02]|[0]?[123456789])\\s*(��|/|[.]|-|��|�C)?)(\\s*(3[01]|[12][0-9]|[0]?[1-9])(\\s*��)?)?)|(19[6789][0-9]|20[01][0-9])|([0-9]{2}\\s*��)(\\s*(1[02]|[0]?[123456789])\\s*��)?)"
                            + "\\s*((��\\s*��|��\\s*��|\\s*��)|((\\s|-|��|~|�C|��|��|��)+)\\s*"
                            + "((((19[6789][0-9]|20[01][0-9])\\s*(��|/|[.]|-|��|�C))(\\s*(1[02]|[0]?[123456789])\\s*(��|/|[.]|-|��|�C)?)(\\s*(3[01]|[12][0-9]|[0]?[1-9])(\\s*��)?)?)|(19[6789][0-9]|20[01][0-9])|([0-9]{2}\\s*��)(\\s*(1[02]|[0]?[123456789])\\s*��)?|��\\s*��|��\\s*��|\\s*��))");


//ѧУ							
string pattern_school_str = "(?!��|��|.*��ѧУ|.*��ѧУ|.*��ѧУ|.*��ѧУ|ȫ����ѧ|���ڴ�ѧ|���ڸ���|������ѧ|���ڳ���|����ѧУ|.*ѧ��ѧУ|�Ͷ�ѧУ|�Ͷ���ѧ|�Ͷ�����|�Ͷ�����|�Ͷ���ѧ)([\u4e00-\u9fa5]{2,18}?)(ѧԺ|��ѧ|ѧУ|�о���Ժ|��ѧ)\\s*";