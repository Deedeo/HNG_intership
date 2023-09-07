import json
from flask import Flask, request, jsonify
from datetime import datetime
import pytz


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    current_day = datetime.now(pytz.utc).strftime('%A')

    current_time_utc = datetime.now(pytz.utc)
    utc_offset_hours = current_time_utc.utcoffset().total_seconds() / 3600
    
    if utc_offset_hours < -2 or utc_offset_hours > 2:
        return jsonfiy({"error": "Invalid UTC offset"}), 400

    
    github_file_path = "https://github.com/Deedeo/HNG_intership/blob/main/Stage_one/main.py"
    github_repo_url = "https://github.com/Deedeo/HNG_intership/tree/main"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time_utc.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": github_file_path,
        "github_repo_url": github_repo_url,
        "status_code": 200

    }

    json_response = json.dumps(response_data, indent=2)

    return json_response


if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)