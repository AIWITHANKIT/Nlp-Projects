from flask import Flask, render_template, request,jsonify
import os
app = Flask(__name__)

@app.route("/new",methods=['GET','POST'])
def data_page():
    
    if request.method == 'POST':
        filesDict = request.files.to_dict()
        uploadData=request.files['media']
        data_file_name = uploadData.filename
        global path
        path = os.path.join(app.root_path,'uploads\\'+data_file_name)
        uploadData.save(path)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=POST enctype=multipart/form-data action="/new">
            <input type=file id="media" name=media>
            <input onclick="update()" type="submit">
        </form>
    ''' 




#uploading code
@app.route("/delete")
def remove():
    
    return jsonify(os.listdir(r"C:\Users\Dell\Desktop\python project\python\uploads"))
        
if __name__=='__main__':
    app.run(debug=True)
