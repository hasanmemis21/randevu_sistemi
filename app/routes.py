from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import load_users, load_appointments, save_appointments

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        user = next((u for u in users if u['username'] == username and u['password'] == password), None)
        if user:
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for('routes.dashboard'))
        else:
            return render_template('login.html', error='Hatalı giriş.')
    return render_template('login.html')

@routes.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    appointments = load_appointments()
    return render_template('dashboard.html', appointments=appointments, role=session['role'])

@routes.route('/create', methods=['GET', 'POST'])
def create_appointment():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        message = request.form['message']
        appointments = load_appointments()
        appointments.append({
            "date": date,
            "time": time,
            "message": message,
            "status": "pending"
        })
        save_appointments(appointments)
        return redirect(url_for('routes.dashboard'))
    return render_template('create_appointment.html')

@routes.route('/approve/<int:index>')
def approve_appointment(index):
    appointments = load_appointments()
    appointments[index]['status'] = 'approved'
    save_appointments(appointments)
    return redirect(url_for('routes.dashboard'))

@routes.route('/reject/<int:index>')
def reject_appointment(index):
    appointments = load_appointments()
    appointments[index]['status'] = 'rejected'
    save_appointments(appointments)
    return redirect(url_for('routes.dashboard'))

@routes.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('routes.login'))
