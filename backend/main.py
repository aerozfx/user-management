from flask import Flask, flash, redirect, url_for, render_template, request
from flask_mysqldb import MySQL
from controller.user_routes import app

app.run(debug=True)   