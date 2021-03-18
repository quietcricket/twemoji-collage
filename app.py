# coding=utf-8
import json

from flask import Flask, render_template, request, redirect
import bs_utils

app = Flask('twemoji-collage')
bs_utils.init_jinja(app.jinja_env)


@app.route('/')
def home():
    return render_template('generator.html')


@app.route('/colors')
def colors():
    return render_template('colors.html', emojis=json.load(open('static/emoji.json')))


if __name__ == '__main__':
    import livereload
    app.debug = True
    app.jinja_env.auto_reload = True
    server = livereload.Server(app.wsgi_app)
    server.watch('static/*.css')
    server.watch('static/*.js')
    server.watch('templates/*.html')
    server.serve(port=8080)
