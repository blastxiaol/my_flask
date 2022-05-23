from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])    #获取表单（模板）并渲染
def index():
    if(request.method=='GET'):
        return render_template('index.html')
    elif(request.method=='POST'):
        name=request.form.get("name")
        password=request.form.get("key")

        print(name,password)
        return "Get the post"




if __name__ == '__main__':
    app.run()
