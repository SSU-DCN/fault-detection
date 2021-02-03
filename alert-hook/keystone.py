from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

def get_token():
  auth = v3.Password(auth_url="http://127.0.0.1:/identity/v3", username="admin",
                     password="devstack", project_name="admin",
                     user_domain_id="default", project_domain_id="default")
  sess = session.Session(auth=auth)
  keystone = client.Client(session=sess)
  return keystone.session.get_token()

