from flask import Flask
from datetime import datetime

app = Flask(__name__)
start_time = datetime.now()
deployment_time = datetime.now().strftime("%B %d, %Y – %I:%M %p")

@app.route('/')
def dashboard():
    uptime = datetime.now() - start_time
    return '''
    <html>
    <head>
        <title>SkillShift Dashboard</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Inter', sans-serif;
                margin: 0;
                padding: 0;
                background: #0f172a;
                color: #e2e8f0;
                text-align: center;
            }
            header {
                background: #1e293b;
                padding: 40px 20px;
            }
            h1 {
                font-size: 36px;
                color: #38bdf8;
            }
            p.subtitle {
                font-size: 18px;
                color: #94a3b8;
                margin-bottom: 20px;
            }
            ul {
                list-style: none;
                padding: 0;
                color: #f1f5f9;
                font-size: 16px;
            }
            ul li {
                margin: 8px 0;
            }
            .btn {
                margin-top: 20px;
                background: #38bdf8;
                color: #0f172a;
                border: none;
                padding: 12px 24px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 16px;
                cursor: pointer;
                transition: 0.3s ease;
            }
            .btn:hover {
                background: #0ea5e9;
            }
            .chart-container, .student-table {
                margin: 40px auto;
                max-width: 600px;
                background: #1e293b;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(56, 189, 248, 0.3);
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }
            th, td {
                padding: 10px;
                border-bottom: 1px solid #334155;
                color: #f1f5f9;
            }
            th {
                text-align: left;
                color: #38bdf8;
            }
            footer {
                margin-top: 60px;
                font-size: 14px;
                color: #64748b;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to SkillShift</h1>
            <p class="subtitle">Unlock your tech future. Learn tech. Get hired.</p>
            <ul>
                <li>Web Development</li>
                <li>DevOps with AWS</li>
                <li>Data Analysis</li>
                <li>Cybersecurity</li>
                <li>Azure Cloud</li>
            </ul>
            <button class="btn" onclick="alert('Registration form coming soon!')">Register Now</button>
        </header>

        <div class="chart-container">
            <p style="color: #f8fafc; font-size: 16px; margin-bottom: 10px;">
                Insights from our last 4 IG posts:
                <br>
                <strong>12</strong> people are ready to start, and
                <strong>4</strong> are struggling with account creation.
            </p>
            <canvas id="metricsChart"></canvas>
        </div>

        <div class="student-table">
            <h2 style="color: #38bdf8;">Student Progress Monitor</h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Course</th>
                    <th>Status</th>
                </tr>
                <tr>
                    <td>Tolu</td>
                    <td>DevOps with AWS</td>
                    <td style="color: #10b981;">Ready</td>
                </tr>
                <tr>
                    <td>Blessing</td>
                    <td>Web Development</td>
                    <td style="color: #f97316;">Stuck</td>
                </tr>
                <tr>
                    <td>Charles</td>
                    <td>Data Analysis</td>
                    <td style="color: #10b981;">Ready</td>
                </tr>
                <tr>
                    <td>Grace</td>
                    <td>Cybersecurity</td>
                    <td style="color: #10b981;">Ready</td>
                </tr>
            </table>
        </div>

        <p style="margin-top: 30px; color: #94a3b8; font-size: 14px;">
            App Uptime: ''' + str(uptime).split('.')[0] + '''<br>
            Last Deployment: ''' + deployment_time + '''
        </p>

        <script>
            const ctx = document.getElementById('metricsChart').getContext('2d');
            const chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Ready', 'Struggling'],
                    datasets: [{
                        label: 'Enrollment Status',
                        data: [12, 4],
                        backgroundColor: ['#10b981', '#f97316']
                    }]
                },
                options: {
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        y: { beginAtZero: true }
                    }
                }
            });
        </script>

        <footer>
            – Precious 💻 | www.ceeyitsolutions.com
        </footer>
    </body>
    </html>
    '''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

