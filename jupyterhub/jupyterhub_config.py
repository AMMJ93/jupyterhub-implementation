import os

c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

c.DockerSpawner.environment = {'MLFLOW_TRACKING_USERNAME': os.environ['MLFLOW_TRACKING_USERNAME'],'MLFLOW_TRACKING_PASSWORD': os.environ['MLFLOW_TRACKING_PASSWORD'], 'MLFLOW_TRACKING_URI': os.environ['MLFLOW_TRACKING_URI'], 'GRANT_SUDO': 'yes' }


## Configure authentication (delagated to GitLab)
c.JupyterHub.authenticator_class = 'oauthenticator.google.GoogleOAuthenticator'

c.GoogleOAuthenticator.client_id = os.environ['OAUTH_CLIENT_ID']
c.GoogleOAuthenticator.client_secret = os.environ['OAUTH_CLIENT_SECRET']
c.GoogleOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

#Data persistence
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir

c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir, 'jupyterhub-shared': notebook_dir + '/'+'shared'}

#Idle remove
c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': 'python3 /srv/jupyterhub/cull_idle_servers.py --timeout=5400'.split(),
    }
]

