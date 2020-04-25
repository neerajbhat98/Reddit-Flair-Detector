from flask import Flask,render_template,url_for,request
from get_submissions import submission
from predict import predict_flair,preprocess_text,predict_flair_post_request
import keras
from flask import jsonify

app = Flask(__name__)

save_name = 'temp.txt'


@app.route('/')
def show_home_page():
    return render_template('Testing.html')

 
@app.route('/automated_testing',methods=['POST'])
def automated_testing():
        file = request.files['upload_file']
        file.save(save_name)  
        response = dict()
        with open(save_name) as f:
            for url in f:
                if url in response.keys():
                    continue
                else:
                    post = submission(url)
                    flair = predict_flair_post_request(post)
                    response[url] = flair
        print(jsonify(response))            
        return jsonify(response)
    
@app.route('/check',methods =['GET']) 
def check():
    url = request.args.get('url')
    post = submission(url)
    post['content'] = preprocess_text(post['content'])
    flair = predict_flair(post)
    return  render_template('sub.html',post=post,flair = flair) 
        
        
if __name__ == "__main__":
    app.run(debug = True)