
-------配置部分--------
#www.iplaypy.com

host="127.0.0.1"  # the http server's bind ip
switcher_port=80 # http switcher server's port
buflen=8192 # http switcher server's buffer length

# http switcher server's switch table
# each rule contain 2 parts:
#    urlpath's prefix
#    forwarding domain
#
# notice:
#   sequence hit
#   forwarding will remove the perfix
#   no rule hit will raise 404
mapper=[
  ['/other/',"192.168.1.123:80"],
  ["/","127.0.0.1:8080"]
]

web_port=8080  # static file server's port
webdir="/var/www/"  # static file server's document root