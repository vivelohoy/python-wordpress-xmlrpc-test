from __future__ import print_function
from pprint import pprint as pretty_print
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.posts import GetPosts
from wordpress_xmlrpc.methods.users import GetUsers, GetUser
from config import WP_USERNAME, WP_PASSWORD

def print_object(obj):
    pretty_print({k:v for k,v in obj.__dict__.iteritems() if k[0]!='_'})

wp = Client('http://wordpress.hoylabs.com/xmlrpc.php', WP_USERNAME, WP_PASSWORD)

sample_post = wp.call(GetPosts({'number': 1, 'post_status': 'publish'}))[0]
print('''
   _____                       __        ____             __ 
  / ___/____ _____ ___  ____  / /__     / __ \____  _____/ /_
  \__ \/ __ `/ __ `__ \/ __ \/ / _ \   / /_/ / __ \/ ___/ __/
 ___/ / /_/ / / / / / / /_/ / /  __/  / ____/ /_/ (__  ) /_  
/____/\__,_/_/ /_/ /_/ .___/_/\___/  /_/    \____/____/\__/  
                    /_/                                      

''')
print_object(sample_post)
post_author = wp.call(GetUser(sample_post.user))
print('''
    ___         __  __              
   /   | __  __/ /_/ /_  ____  _____
  / /| |/ / / / __/ __ \/ __ \/ ___/
 / ___ / /_/ / /_/ / / / /_/ / /    
/_/  |_\__,_/\__/_/ /_/\____/_/     

''')
print_object(sample_post)

