# Use the LTS release.
FROM nethacker/ubuntu-18-04-python-3:python-3.7.3

RUN useradd --user-group --create-home --shell /bin/false app 
  
ENV HOME=/home/app

WORKDIR $HOME/api_sample

ADD requirements.txt $HOME/api_sample/

ADD app.py $HOME/api_sample/

#ADD chinook.db $HOME/api_sample/

RUN pip install -r requirements.txt

USER app

