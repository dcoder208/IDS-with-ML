from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 100")
    logs = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM logs")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE status='Suspicious'")
    suspicious = cursor.fetchone()[0]

    normal = total - suspicious
    threat_score = int((suspicious / total) * 100) if total > 0 else 0

    cursor.execute("""
        SELECT source_ip, COUNT(*) as count
        FROM logs
        WHERE status='Suspicious'
        GROUP BY source_ip
        ORDER BY count DESC
        LIMIT 5
    """)
    top_ips = cursor.fetchall()

    conn.close()

    return render_template(
    "index.html",
    logs=logs,
    total=total,
    suspicious=suspicious,
    normal=normal,
    top_ips=top_ips,
    threat_score=threat_score
    )

if __name__ == "__main__":
    app.run(debug=True)