from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# =======================
# 📘 SAMPLE STUDENT DATA
# =======================
students = [
    {"id": 1, "name": "Alice Santos", "age": 16, "grade": 10, "section": "Zechariah"},
    {"id": 2, "name": "Mark Dela Cruz", "age": 17, "grade": 11, "section": "Reuben"},
]

# =======================
# 🏠 HOME PAGE (MODERN UI)
# =======================
@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Information System</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #b3e5fc, #e3f2fd);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background: white;
                width: 500px;
                border-radius: 20px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                text-align: center;
                padding: 40px;
                animation: fadeIn 1s ease-in-out;
            }
            @keyframes fadeIn {
                from {opacity: 0; transform: translateY(20px);}
                to {opacity: 1; transform: translateY(0);}
            }
            h1 {
                color: #007BFF;
                margin-bottom: 20px;
            }
            p {
                color: #555;
                margin-bottom: 30px;
            }
            .nav-btn {
                display: block;
                margin: 10px auto;
                width: 80%;
                padding: 15px;
                background: #007BFF;
                color: white;
                text-decoration: none;
                font-weight: 600;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            .nav-btn:hover {
                background: #0056b3;
                transform: scale(1.05);
            }
            footer {
                margin-top: 30px;
                font-size: 13px;
                color: #777;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎓 Student Info System</h1>
            <p>Manage, view, and search students easily!</p>
            <a href="/students" class="nav-btn">📋 View All Students</a>
            <a href="/add_student_form" class="nav-btn">➕ Add Student</a>
            <a href="/search_student" class="nav-btn">🔍 Search Student</a>
            <footer>© 2025 Student Management UI</footer>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

# =======================
# 👥 VIEW ALL STUDENTS
# =======================
@app.route('/students')
def show_students():
    html = '''
    <html>
    <head>
        <title>All Students</title>
        <style>
            body { font-family: Poppins, sans-serif; background: #f0f9ff; text-align: center; padding: 40px; }
            h1 { color: #007BFF; margin-bottom: 20px; }
            .card {
                background: white;
                width: 300px;
                margin: 15px auto;
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                transition: 0.3s;
            }
            .card:hover { transform: scale(1.05); }
            .card h3 { color: #333; }
            a.btn {
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                background: #007BFF;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
                transition: 0.3s;
            }
            a.btn:hover { background: #0056b3; }
        </style>
    </head>
    <body>
        <h1>📋 Student List</h1>
    '''
    for s in students:
        html += f'''
        <div class="card">
            <h3>{s['name']}</h3>
            <p><b>Age:</b> {s['age']}</p>
            <p><b>Grade:</b> {s['grade']}</p>
            <p><b>Section:</b> {s['section']}</p>
            <a href="/student/{s['id']}" class="btn">View Info</a>
        </div>
        '''
    html += '<a href="/" class="btn">⬅ Back to Home</a></body></html>'
    return html

# =======================
# 🎯 VIEW STUDENT BY ID
# =======================
@app.route('/student/<int:student_id>')
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return render_template_string(f"""
            <html>
            <head>
                <title>Student Info</title>
                <style>
                    body {{ font-family: Poppins; text-align: center; background: #e3f2fd; padding: 60px; }}
                    .card {{
                        background: white;
                        display: inline-block;
                        padding: 40px;
                        border-radius: 15px;
                        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                    }}
                    h2 {{ color: #007BFF; }}
                    a {{ text-decoration: none; color: white; background: #007BFF; padding: 10px 20px; border-radius: 10px; }}
                    a:hover {{ background: #0056b3; }}
                </style>
            </head>
            <body>
                <div class="card">
                    <h2>🎯 Student Information</h2>
                    <p><b>ID:</b> {student['id']}</p>
                    <p><b>Name:</b> {student['name']}</p>
                    <p><b>Age:</b> {student['age']}</p>
                    <p><b>Grade:</b> {student['grade']}</p>
                    <p><b>Section:</b> {student['section']}</p>
                    <a href='/'>⬅ Back to Home</a>
                </div>
            </body>
            </html>
        """)
    else:
        return "<h2>❌ Student Not Found</h2><a href='/'>⬅ Back to Home</a>"

# =======================
# 🔍 SEARCH STUDENT BY ID
# =======================
@app.route('/search_student', methods=['GET', 'POST'])
def search_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        return f"<meta http-equiv='refresh' content='0; url=/student/{student_id}' />"
    html = '''
    <html>
    <head>
        <title>Search Student</title>
        <style>
            body { font-family: Poppins; background: #f0f9ff; text-align: center; padding: 100px; }
            input, button { padding: 10px; margin: 5px; border-radius: 8px; border: 1px solid #007BFF; }
            button { background: #007BFF; color: white; cursor: pointer; }
            button:hover { background: #0056b3; }
        </style>
    </head>
    <body>
        <h1>🔍 Search Student by ID</h1>
        <form method="POST">
            <input type="number" name="student_id" placeholder="Enter Student ID" required>
            <button type="submit">Search</button>
        </form>
        <br><a href="/">⬅ Back to Home</a>
    </body>
    </html>
    '''
    return render_template_string(html)

# =======================
# ➕ ADD NEW STUDENT
# =======================
@app.route('/add_student_form', methods=['GET', 'POST'])
def add_student_form():
    html_form = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Add Student</title>
        <style>
            body { font-family: Poppins; background: #e1f5fe; text-align: center; padding: 40px; }
            form { background: white; display: inline-block; padding: 30px 50px; border-radius: 15px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            input { margin: 10px; padding: 10px; width: 90%; border: 1px solid #007BFF; border-radius: 8px; }
            button { background: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 8px; cursor: pointer; }
            button:hover { background: #45a049; }
        </style>
    </head>
    <body>
        <h1>➕ Add New Student</h1>
        <form method="POST">
            <input type="text" name="name" placeholder="Full Name" required><br>
            <input type="number" name="age" placeholder="Age" required><br>
            <input type="number" name="grade" placeholder="Grade Level" required><br>
            <input type="text" name="section" placeholder="Section" required><br>
            <button type="submit">Add Student</button>
        </form>
        <br><a href="/">⬅ Back to Home</a>
    </body>
    </html>
    '''
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        section = request.form['section']
        new_student = {
            "id": len(students) + 1,
            "name": name,
            "age": int(age),
            "grade": int(grade),
            "section": section
        }
        students.append(new_student)
        return f"<h2>✅ Student '{name}' added successfully!</h2><a href='/'>⬅ Back to Home</a>"
    return render_template_string(html_form)

# =======================
# 🧠 RUN APP
# =======================
if __name__ == '__main__':
    app.run(debug=True)
