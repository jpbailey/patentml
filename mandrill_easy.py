import mandrill

try:
	mandrill_client = mandrill.Mandrill('9wu4qbG2pO9YHS0tU31vpg')
	template_content = [{'content': 'example content', 'name': 'example name'}]
	message = {
		'auto_html': None,
		'auto_text': None,
		'from_email': "joepbailey@gmail.com",
		'from_name':  "Joe Bailey",
		'to':[{"email":"joepbailey@gmail.com"}],
		'subject': 'Patent Activity',
		'text': "here is the patent activity for you"

	}
	result = mandrill_client.messages.send_template(template_name='merilant', template_content=template_content, message=message, async=False, ip_pool='Main Pool')

except mandrill.Error, e:
	# Mandrill errors are thrown as exceptions
	print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
	# A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
	raise
