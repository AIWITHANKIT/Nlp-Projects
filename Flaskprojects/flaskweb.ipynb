from flask import Flask, request, render_template, redirect, url_for
import re


myapp = Flask(__name__)

@myapp.route('/updated',methods = ['GET','POST'])
def slugenter():
    if request.method == 'POST':
        global slug
        slug = request.form.get('text')
        new_slug = re.sub(r'[^\w\s]',"",slug)
        new_slug = re.sub("\s","-",new_slug) 
        return redirect(url_for("slugify",slug_url = new_slug,what ="fab"))
        
    return render_template('home.html')   

@myapp.route('/slugify/<string:slug_url>/<string:what>',methods = ['GET','POST'])
def slugify(slug_url,what):
        return slug_url,what

@myapp.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return redirect(url_for("slugenter"))    
myapp.run() 
