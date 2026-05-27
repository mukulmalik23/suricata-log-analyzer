from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():


  alerts = []
  http_count = 0
  unique_ips = set()

  try:
    with open("logs/eve.json", "r") as f:

        for line in f:
            try:
                data = json.loads(line)

                alerts.append(data)

                if data.get("event_type") == "http":
                    http_count += 1

                if "src_ip" in data:
                    unique_ips.add(data["src_ip"])

            except:
                pass

  except:
    pass

  return render_template(
    "index.html",
    alerts=alerts[-20:],
    total_alerts=len(alerts),
    http_count=http_count,
    unique_ips=len(unique_ips)
)


if __name__== "__main__":
  app.run(debug=True)
