import os, requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the weather Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    if req['queryResult']['intent']['displayName'] == 'greeting':
        
        if req['queryResult']['parameters']['animal'][0:3] == '小豬':
            return jsonify({"fulfillmentText":"ㄍㄡˊ 你好"})
        elif req['queryResult']['parameters']['animal'][0:3] == '小狗':
            return jsonify({"fulfillmentText":" 汪汪! 你好"})
        elif req['queryResult']['parameters']['animal'][0:3] == '小貓':
            return jsonify({"fulfillmentText":" 我們一起學貓叫~ 喵喵! 你好"})
        else :
            return jsonify({"fulfillmentText":" 哈囉 請問你想找哪隻動物 目前在線的可愛動物有 小豬 小狗 小貓"})
            
    if req['queryResult']['intent']['displayName'] == 'ask_math':
        
        if req['queryResult']['parameters']['Operator'][0] == "+" :
            number = req['queryResult']['parameters']['number1'][0] + req['queryResult']['parameters']['number11']
            
            if req['queryResult']['parameters']['animal'][0] == '小豬':
                if number <= 20:
                    ans = "ㄍㄡˊ!" * int(number)
                    return jsonify({"fulfillmentText":"{}。ㄍㄡˊ了{}次，有點餓".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"ㄍㄡˊ!ㄍㄡˊ!ㄍㄡˊ! ㄍㄡˊ{}次粉累ㄝ@@".format(int(number))})
                
            elif req['queryResult']['parameters']['animal'][0] == '小狗':
                if number <= 20:
                    ans = "汪!" * int(number)
                    return jsonify({"fulfillmentText":"{}。汪了{}次，幫我摸摸頭~".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"汪!汪!汪! 要汪{}次，口會很渴餒@@".format(int(number))})
                
            elif req['queryResult']['parameters']['animal'][0] == '小貓':
                if number <= 20:
                    ans = "喵!" * int(number)
                    return jsonify({"fulfillmentText":"{}。喵了{}次，我要罐罐~".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"喵!喵!喵! 大膽奴才，竟然要我喵{}次。".format(int(number))})
            else:
                return jsonify({"fulfillmentText":"你請教的動物不對歐"})
            
        
        elif req['queryResult']['parameters']['Operator'][0] == "-" :
            number = req['queryResult']['parameters']['number1'][0] - req['queryResult']['parameters']['number11']
            if req['queryResult']['parameters']['animal'][0] == '小豬':
                if number <= 20:
                    ans = "ㄍㄡˊ!" * int(number)
                    return jsonify({"fulfillmentText":"{}。ㄍㄡˊ了{}次，有點餓".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"ㄍㄡˊ!ㄍㄡˊ!ㄍㄡˊ! ㄍㄡˊ{}次粉累ㄝ@@".format(int(number))})
                
            elif req['queryResult']['parameters']['animal'][0] == '小狗':
                if number <= 20:
                    ans = "汪!" * int(number)
                    return jsonify({"fulfillmentText":"{}。汪了{}次，幫我摸摸頭~".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"汪!汪!汪! 要汪{}次，口會很渴餒@@".format(int(number))})
                
            elif req['queryResult']['parameters']['animal'][0] == '小貓':
                if number <= 20:
                    ans = "喵!" * int(number)
                    return jsonify({"fulfillmentText":"{}。喵了{}次，我要罐罐~".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"喵!喵!喵! 大膽奴才，竟然要我喵{}次。".format(int(number))})
            else:
                return jsonify({"fulfillmentText":"你請教的動物不對歐"})
        
        elif req['queryResult']['parameters']['Operator'][0] == "*" :
            number = req['queryResult']['parameters']['number1'][0] * req['queryResult']['parameters']['number11']
            if req['queryResult']['parameters']['animal'][0] == '小豬':
                if number <= 20:
                    ans = "ㄍㄡˊ!" * int(number)
                    return jsonify({"fulfillmentText":"{}。ㄍㄡˊ了{}次，有點餓".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"ㄍㄡˊ!ㄍㄡˊ!ㄍㄡˊ! ㄍㄡˊ{}次粉累ㄝ@@".format(int(number))})
                
            elif req['queryResult']['parameters']['animal'][0] == '小狗':
                if number <= 20:
                    ans = "汪!" * int(number)
                    return jsonify({"fulfillmentText":"{}。汪了{}次，幫我摸摸頭~".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"汪!汪!汪! 要汪{}次，口會很渴餒@@".format(int(number))})
                
            elif req['queryResult']['parameters']['animal'][0] == '小貓':
                if number <= 20:
                    ans = "喵!" * int(number)
                    return jsonify({"fulfillmentText":"{}。喵了{}次，我要罐罐~".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"喵!喵!喵! 大膽奴才，竟然要我喵{}次。".format(int(number))})
            else:
                return jsonify({"fulfillmentText":"你請教的動物不對歐"})
        
        elif req['queryResult']['parameters']['Operator'][0] == "/" :
            number = req['queryResult']['parameters']['number1'][0] / req['queryResult']['parameters']['number11']
            if req['queryResult']['parameters']['animal'][0] == '小豬':
                if number <= 20:
                    ans = "ㄍㄡˊ!" * int(number)
                    return jsonify({"fulfillmentText":"{}。ㄍㄡˊ了{}次，有點餓".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"ㄍㄡˊ!ㄍㄡˊ!ㄍㄡˊ! ㄍㄡˊ{}次粉累ㄝ@@".format(int(number))})
                
            elif req['queryResult']['parameters']['animal'][0] == '小狗':
                if number <= 20:
                    ans = "汪!" * int(number)
                    return jsonify({"fulfillmentText":"{}。汪了{}次，幫我摸摸頭~".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"汪!汪!汪! 要汪{}次，口會很渴餒@@".format(int(number))})
                
            elif req['queryResult']['parameters']['animal'][0] == '小貓':
                if number <= 20:
                    ans = "喵!" * int(number)
                    return jsonify({"fulfillmentText":"{}。喵了{}次，我要罐罐~".format(ans, int(number))})
                elif number >20:
                    return jsonify({"fulfillmentText":"喵!喵!喵! 大膽奴才，竟然要我喵{}次。".format(int(number))})
            else:
                return jsonify({"fulfillmentText":"你請教的動物不對歐"})
        else:
            return jsonify({"fulfillmentText":"你請教的動物不對歐"})
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, threaded=True)
