# importing the required libraries
import os
from flask import Flask, render_template, request, send_file

# initialising the flask app
app = Flask(__name__)

# displaying the HTML template at the home url
@app.route('/')
def index():
   return render_template('download.html')

# Sending the file to the user
@app.route('/download')
def download():                                                                                                                            
   return send_file(r'C:\Users\Dell\Desktop\python project\python\uploads\Coldplay - Yellow.mp3', as_attachment=True)

@app.after_request
def delete(response):
   print("downloaded")
   #os.remove(r'C:\Users\Dell\Desktop\python project\python\uploads\Coldplay - Yellow.mp3')
   return response
if __name__ == '__main__':
   app.run() # running the flask app

#whole download project at this url https://www.youtube.com/watch?v=BP8ulGbu1fc  
