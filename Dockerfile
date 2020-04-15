# Use the LTS release.
FROM python:3.6-stretch

RUN useradd --user-group --create-home --shell /bin/false app 
  
ENV HOME=/home/app

WORKDIR $HOME/api_sample

ADD requirements.txt $HOME/api_sample/

ADD app.py $HOME/api_sample/

#ADD chinook.db $HOME/api_sample/

RUN pip install -r requirements.txt

USER app

