from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Cloud & DevOps Integration Project</h1>
    <h2>Group Members:</h2>
    <ul>
        <li>Huzaifa Waqar (22011556-035)</li>
        <li>Tasmia Riaz (22011556-022)</li>
        <li>Malaika Kashaf (22011556-051)</li>
    </ul>
    <h2>Course Instructor:</h2>
    <p>Mam Hira</p>
    <h2>Project Description:</h2>
    <p>This final year project demonstrates the deployment of a cloud-native web application using CI/CD pipelines, Jenkins, GitHub, Docker, and AWS EC2. It reflects integration of DevOps tools for automated builds and deployments.</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0')

