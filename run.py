from flask import render_template, jsonify, request
import requests
from random import *
import init
from backup.database import Article, session
import json

app = init.create_app()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    username = request.values.get('username')
    password = request.values.get('password')
    if username == 'heying' and password == '1030':
        res = {
            'isLogin': '0',
            'msg': 'success'
        }
        return jsonify(res)
    else:
        res = {
            'isLogin': '-1',
            'msg': 'fail'
        }
        return jsonify(res)


@app.route('/api/writeessay', methods=['GET', 'POST'])
def write_essay():
    title = request.values.get('title')
    content = request.values.get('content')
    status = request.values.get('status')

    value = Article(title, content, status)

    session.add(value)
    session.flush()
    lastInsertId = value.id
    session.commit()
    session.close()

    res = {
        'msg': 'success',
        'article_id': lastInsertId
    }

    return jsonify(res)


@app.route('/api/list', methods=['GET', 'POST'])
def show_all():
    result = session.query(Article.id, Article.title, Article.create_time).filter_by(status='1').all()
    l = []
    for row in result:
        i = {'id': row.id, 'title': row.title, 'time': row.create_time}
        l.append(i)

    return jsonify(l)


@app.route('/api/details', methods=['GET', 'POST'])
def details():
    article_id = request.values.get('article_id')
    result = session.query(Article).filter(Article.id == article_id).all()
    l = []
    for row in result:
        i = {'id': row.id, 'title': row.title, 'time': row.create_time, 'content': row.content}
        l.append(i)

    res = {
        'data': l,
        'msg': 'success'
    }
    return jsonify(res)


@app.route('/api/delete', methods=['GET', 'POST'])
def delete_article():
    article_id = request.values.get('article_id')
    result = session.query(Article).filter_by(id=article_id).delete()
    session.commit()
    session.close()
    if result == 1:
        msg = 'success'
    else:
        msg = 'fail'

    res = {
        'id': result,
        'msg': msg
    }

    return jsonify(res)


@app.route('/api/update', methods=['GET', 'POST'])
def update_article():
    article_id = request.values.get('article_id')
    new_content = request.values.get('content')
    new_title = request.values.get('title')
    new_status = request.values.get('status')
    result = session.query(Article).filter_by(id=article_id).first()
    result.title = new_title
    result.content = new_content
    result.status = new_status
    session.flush()
    id = result.id
    session.commit()
    session.close()

    # print(article_id)
    # print(new_content)
    # print(new_title)
    # print(result)

    res = {
        'article_id': id,
        'msg': 'success'
    }

    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
