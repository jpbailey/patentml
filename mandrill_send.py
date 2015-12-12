import mandrill

# from datetime import datetime
# current_time=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
# print type(current_time)
# print current_time

try:
    mandrill_client = mandrill.Mandrill('9wu4qbG2pO9YHS0tU31vpg')
    template_content = [{'content': 'example content', 'name': 'example name'}]
    message = {'attachments': [{'content': 'ZXhhbXBsZSBmaWxl',
                      'name': 'myfile.txt',
                      'type': 'text/plain'}],
     'auto_html': None,
     'auto_text': None,
     'from_email': 'joepbailey@gmail.com',
     'from_name': 'Joe Bailey',
     'global_merge_vars': [{'content': 'merge1 content', 'name': 'merge1'}],
     'headers': {'Reply-To': 'joepbailey@gmail.com'},
     'html': '<p>Example HTML content</p>',
     'images': [{'content': 'ZXhhbXBsZSBmaWxl',
                 'name': 'IMAGECID',
                 'type': 'image/png'}],
     'important': False,
     'inline_css': None,
     'merge': True,
     'merge_language': 'mailchimp',
     'merge_vars': [{'rcpt': 'joepbailey@gmail.com',
                     'vars': [{'content': 'merge2 content', 'name': 'merge2'}]}],
     'metadata': {'website': 'www.example.com'},
     'preserve_recipients': None,
     'recipient_metadata': [{'rcpt': 'joepbailey@gmail.com',
                             'values': {'user_id': 123456}}],
     'return_path_domain': None,
     'signing_domain': None,
     'subaccount': 'customer-123',
     'subject': 'example subject',
     'tags': ['password-resets'],
     'text': 'Example text content',
     'to': [{'email': 'joepbailey@gmail.com',
             'name': 'Joe Bailey',
             'type': 'to'}],
     'track_clicks': None,
     'track_opens': None,
     'tracking_domain': None,
     'url_strip_qs': None,
     'view_content_link': None}
    # result = mandrill_client.messages.send_template(template_name='example name', template_content=template_content, message=message, async=False, ip_pool='Main Pool', send_at='')
    result = mandrill_client.messages.send_template(template_name='merilant', template_content=template_content, message=message, async=False, ip_pool='Main Pool')
    '''
    [{'_id': 'abc123abc123abc123abc123abc123',
      'email': 'jbailey@rhsmith.umd.edu',
      'reject_reason': 'hard-bounce',
      'status': 'sent'}]
    '''

except mandrill.Error, e:
    # Mandrill errors are thrown as exceptions
    print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
    # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
    raise

