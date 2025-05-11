from flask import Flask, session, render_template, redirect, url_for
import random
import time

app = Flask(__name__)
app.secret_key = 'super-secret-key'

# Хранилища посещений и статистики
visit_log = []  # Пример: [{'time': '10:43:22', 'user_id': 123}]
user_stats = {}  # Пример: {123: 3, 456: 2}

@app.route('/')
def index():
    if 'user_id' not in session:
        user_id = random.randint(100000000, 999999999)
        session['user_id'] = user_id
    else:
        user_id = session['user_id']

    current_time = time.strftime('%H:%M:%S')

    # Добавляем в журнал
    visit_log.append({
        'time': current_time,
        'user_id': user_id
    })

    # Обновляем статистику
    if user_id in user_stats:
        user_stats[user_id] += 1
    else:
        user_stats[user_id] = 1

    return render_template('index.html', visits=visit_log, stats=user_stats)

if __name__ == "__main__":
    app.run(debug=True)