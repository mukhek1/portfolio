from flask import Flask, render_template, request , redirect
import csv
app = Flask(__name__)
print(__name__)
@app.route('/') #This is a declarator
def my_home():
    return render_template('index.html')
    #return 'These are my very 2st blog'
    #return render_template('index.html')  #Flask will look for templates folder.

@app.route('/<string:page_name>') #This is a declarator
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode = 'a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writter = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #return 'From submitted hurrayyyy '
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            #print(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return 'something went wrong. please try again'

#@app.route('/about.html') #This is a declarator
#def about():
#    return render_template('about.html')

#@app.route('/works.html') #This is a declarator
#def work():
#    return render_template('works.html')   

#@app.route('/contact.html') #This is a declarator
#def contact():
#    return render_template('contact.html') 

#@app.route('/about/<username>/<int:post_id>') #This is a declarator
#def about(username = None, post_id=None):
#    return render_template('about.html',name = username, post_id=post_id)  

#Flask will look for "templates" folder. -- All HTML file should be here.
#Flask will look for "static"    folder. -- All CSS & JaveScript files should be here.
 

#@app.route('/blog') #This is a declarator
#def blog():
#    return 'These are my blog'

#@app.route('/blog/2020/dog') #This is a declarator
#def blog2():
#    return 'These are my blog on dog'   

#@app.route('/blog') #This is a declarator
#def blog3():
#    return 'This blog will not work.' 

app.run(debug=True)

