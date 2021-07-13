from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
import os
def get_token():
  auth_url = os.environ.get('auth_url', "http://127.0.0.1:/identity/v3")
  username = os.environ.get('username', "admin")
  password = os.environ.get('password', "devstack")
  project_name = os.environ.get('project_name', "admin")
  user_domain_id = os.environ.get('user_domain_id', "default")
  project_domain_id = os.environ.get('project_domain_id', "default")

  auth = v3.Password(auth_url=auth_url, username=username,
                     password=password, project_name=project_name,
                     user_domain_id=user_domain_id, project_domain_id=project_domain_id)
  sess = session.Session(auth=auth)
  keystone = client.Client(session=sess)
  return keystone.session.get_token()

