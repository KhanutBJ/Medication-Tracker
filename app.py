from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

notifications = []  # List to store received notifications

# Endpoint to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to receive medication notifications
@app.route('/notification', methods=['POST'])
def receive_notification():
    notification_data = request.json
    notification_data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notifications.append(notification_data)
    return jsonify({"message": "Notification Received"})

# Endpoint to fetch notifications
@app.route('/get_notifications')
def get_notifications():
    return jsonify(notifications)

if __name__ == '__main__':
    app.run(debug=True)

# cURL post script
""" curl -X POST http://127.0.0.1:5000/notification \
  -H "Content-Type: application/json" \
  -d '{"medication_id": "PRX123", "status": "due", "drug_name": "Paracetamol", "num_capsules": 2, "time_to_take": "every 1 hours"}'
"""
