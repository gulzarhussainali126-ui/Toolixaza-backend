from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/transcript')
def transcript():
    vid = request.args.get('videoId')
    try:
        api = YouTubeTranscriptApi()
        t = api.fetch(vid)
        data = [{"text": x.text, "start": x.start, "duration": x.duration} for x in t]
        return jsonify({"transcript": data})
    except Exception as e:
        return jsonify({"error": str(e), "transcript": []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
