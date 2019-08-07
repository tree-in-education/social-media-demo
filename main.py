# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

# A very simple Flask Hello World app for you to get started with...
import twint
import asyncio
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS



def convertTweet(x):
    return {'link':x.link, 'tweet': x.tweet, 'urls': x.urls, 'photos': x.photos, 'video': x.video, 'username': x.username}

app = Flask(__name__)
app.logger.info('This is a log message!')
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/twint-geo')
def hello_twint():
    asyncio.set_event_loop(asyncio.new_event_loop())
    # tweets=[]
    # Configure
    c = twint.Config()
    # c.Store_json = True
    # equivalent to `-s` bitcoin
    # c.Search = "santa"
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    c.Geo =" {}, {},2km".format(lat, lng)
    # c.Username = 'noneprivacy'
    c.Limit = 5
    # Custom output format
    # c.Format = "Tweet id: {id} | Username: {username}"
    c.Store_object = True
    # c.Store_json = True
    # c.Media = True
    c.Images = True
    # c.Output = "./myfile.json"
    twint.run.Search(c)
    tweets = twint.output.tweets_list
    # app.logger.info('TWEET LIST size')
    # app.logger.info(len(tweets))
    tweetsMap = list(map(convertTweet, tweets))
    tweetsClean = tweetsMap # list(map(lambda x: len(x.photos) > 0, tweetsMap))
    #test = {"h":1, "b":2, "data": tweets}
    # return jsonify(tweets)
    # app.logger.info(tweets)
    # content = get_file('./myfile.json')
    return jsonify(tweetsClean)




@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
