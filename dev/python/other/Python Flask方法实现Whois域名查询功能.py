
#导入命令
import commands

game = Module(__name__)

@game.route('/whois/', methods=["POST", "GET"])
def whois():
   if request.method == "POST":
      whois_key = request.form['whois']
   else :
      whois_key = request.args.get('whois')
   com_d = "whois %s" % (whois_key)
   data = commands.getoutput(com_d).replace('\n', '<br />')

   return jsonify(ok=True, data = data)
#www.iplaypy.com