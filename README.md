# Social Media Demo
## Serve twint-based tweets from twitter to clients based on various inputs.

### To run locally:
 - from the home directory. run `pip3 install -r requirements.txt` from the command line
 - then run `python3 main.py` or `python3.7 main.py` _NOTE: you may need to update python command to match version number. python 3.6 is a minimum requirement)_

### To deploy:
_NOTE: this project is configured to run with google cloud app engine that you have already setup and logged into_
 - run `gcloud app deploy` or `gcloud app deploy --quiet` to default to yes on prompts
