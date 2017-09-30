
class Radio(Input):
    def __init__(self, name, args, *validators, **attrs):
        self.args = args
        super(Radio, self).__init__(name, *validators, **attrs)

    def render(self):
        x = '<span>'

        for arg in self.args:
            #if isinstance(arg, (tuple, list)):

	    if type(arg) == tuple:
                value, desc= arg

            else:
                value, desc = arg, arg 


            attrs = self.attrs.copy()

            attrs['name'] = self.name

            attrs['type'] = 'radio'

            attrs['value'] = arg

            #if self.value == arg:

	    
	    if self.value==value: 
		select_p=' checked="checked"'
	    else:
		select_p=''


                #attrs['checked'] = 'checked'
            #x += '<input %s/> %s' % (attrs, net.websafe(desc))
	    #net.websafe(arg),select_p,self.addatts(),net.websafe(arg)
	    radio_id = net.websafe(self.name)+'_'+net.websafe(value)
	    x += '<input type="radio" name="%s" id="%s" value="%s" %s/><label for="%s"> %s</label>' % (net.websafe(self.name), radio_id, net.websafe(value), select_p, self.addatts(), net.websafe(desc))
        x += '</span>'
        return x