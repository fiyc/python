from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import json
import sys
sys.path.append('project/controller')
import service
import model
app = Flask(__name__)
 
def convertObj(obj):
	d = {}
	d.update(obj.__dict__)
	return d

@app.route("/")
def blog():
	return render_template("blog.html")

@app.route("/index")
def index():
	userAgent = request.headers.get('User-Agent')
	if userAgent.find('Mobile') != -1 :
		return render_template("index_mobile.html")
	else:
		return render_template("index.html") 

@app.route("/blog")
def list():
	data = service.GetListViewModel()
	userAgent = request.headers.get('User-Agent')
	if userAgent.find('Mobile') != -1 :
		return render_template("list_mobile.html", data=data)
	else:
		return render_template('list.html', data=data)

@app.route("/detail/<articleId>")
def detail(articleId):
	id = int(articleId)
	data = service.GetArticleDetail(id)
	
	userAgent = request.headers.get('User-Agent')
	if userAgent.find('Mobile') != -1 :
		return render_template("detail_mobile.html", data=data)
	else:
		return render_template("detail.html", data=data)

@app.route("/blogansy/<typeId>")
def getListByType(typeId):
	id = int(typeId)
	data = service.GetArticleListByType(id)

	return json.dumps(data, default=convertObj, ensure_ascii=False)
@app.route("/ansysearch")
def searchArticleList():
	typeId = request.args.get('typeId')
	keyword = request.args.get('keyword')
	pageIndex = request.args.get('pageIndex')
	id = int(typeId)
	pageIndex = int(pageIndex)
	data = service.GetPagingArticleList(id, keyword, pageIndex)

	return json.dumps(data, default=convertObj, ensure_ascii=False)

#app.run()

getListByType(1)