from flask import Flask, render_template, redirect
import calendar
from datetime import datetime

app = Flask(__name__)

def month_prev(year, month):
    return (year - 1, 12) if month == 1 else (year, month - 1)

def month_next(year, month):
    return (year + 1, 1) if month == 12 else (year, month + 1)

@app.route('/')
def index():
    now = datetime.now()
    return redirect(f"/{now.year}/{now.month}")

@app.route('/<int:year>/<int:month>')
def show_month(year, month):
    cal = calendar.Calendar(firstweekday=0)
    month_matrix = cal.monthdayscalendar(year, month)
    weekday_names = ['E', 'T', 'K', 'N', 'R', 'L', 'P']
    prev_y, prev_m = month_prev(year, month)
    next_y, next_m = month_next(year, month)
    today = datetime.now()
    return render_template(
        "calendar.html",
        year=year,
        month=month,
        month_name=calendar.month_name[month],
        month_matrix=month_matrix,
        weekday_names=weekday_names,
        prev_year=prev_y,
        prev_month=prev_m,
        next_year=next_y,
        next_month=next_m,
        today_day=today.day,
        today_month=today.month,
        today_year=today.year
    )

