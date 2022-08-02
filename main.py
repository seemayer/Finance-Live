########  imports  ##########
from flask import Flask, jsonify, request, render_template
import market_data as md
import screens
import os

app = Flask(__name__)

@app.route('/')
def home_page():
    # load homepage and send data to be displayed on page
    return render_template('index.html', files=os.listdir('./data'), screened=os.listdir('./screen passed'))

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    processed_text.replace('\r\n', ',')
    li = list(processed_text.split(','))
    #remove periods from end
    li = [item[:-1] if item[-1] == '.' else item for item in li]
    #replace internal dots with dashes to get yahoo format
    li = [item.replace('.', '-') for item in li]
    #add suffix
    li = [item + '.L' for item in li]
    
    print(li)
    md.reset_market_data(lst_tickers=li)
    return processed_text

@app.route('/fn_runner', methods=['POST'])
def fn_runner():
    result = request.get_json()
    module_name = result['module']
    function_name = result['function']
    
    module = __import__(module_name)
    func = getattr(module, function_name)    
    
    try:
        parameter_dict = result['parameters']
        print(f"Running {module_name}.{function_name} with parameters {parameter_dict}") 
        myobject = func(**parameter_dict) # if parameters exist then pass them
    except:
        print(f"Running {module_name}.{function_name} with no parameters")
        myobject = func() # if no parameters then don't

    print(f'object returned from function = {myobject} of type {type(myobject)}')
    
    return jsonify(myobject)


#########  run app  #########
if __name__ == "__main__":
    # change for commmit
    app.run("0.0.0.0", 6969)