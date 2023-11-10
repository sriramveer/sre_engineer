from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/diag', methods=['GET'])
def diag():
    try:
        response = requests.get('https://www.travel-advisory.info/api')
        response.raise_for_status()
        return jsonify({"api_status": response.json()}), 200
    except requests.exceptions.HTTPError as errh:
        return jsonify({"api_status": {"status": "error", "code": errh.response.status_code}}), 500
    except requests.exceptions.ConnectionError as errc:
        return jsonify({"api_status": {"status": "error", "code": 503}}), 500
    except requests.exceptions.Timeout as errt:
        return jsonify({"api_status": {"status": "error", "code": 504}}), 500
    except requests.exceptions.RequestException as err:
        return jsonify({"api_status": {"status": "error", "code": 500}}), 500

if __name__ == '__main__':
    app.run(debug=True)
