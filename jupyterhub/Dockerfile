# Do not forget to pin down the version
FROM jupyterhub/jupyterhub:0.9.3

# Copy the JupyterHub configuration in the container
COPY jupyterhub_config.py .

RUN apt update

RUN apt install wget

# Download script to automatically stop idle single-user servers
RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.3/examples/cull-idle/cull_idle_servers.py

# Install dependencies (for advanced authentication and spawning)
RUN pip install \
    dockerspawner==0.10.0 \
    oauthenticator==0.8.0

RUN rm -rf /opt/conda/lib/python3.6/site-packages/dockerspawner/volumenamingstrategy.py

COPY volumenamingstrategy.py /opt/conda/lib/python3.6/site-packages/dockerspawner/ 

RUN apt install openssh-server -y
