from score import get_user_score
from const.global_const  import SCORES_FILE_NAME,BAD_RETURN_CODE
from flask import jsonify
import os
import json


    
def generate_error_response(err):
    html =  '<html> ' \
                '<head>  <title>Scores Game</title> </head> ' \
                    '<body> <body> ' \
                    '<h1><div id="score" style="color:red">{error}</div></h1> </body> ' \
            '</html> '.format(error=err) 
    return html

def show_json_points_in_html_table(data) : 
    html_table = "<table><tr><th>user name</th><th>score</th></tr>"
    
    for key, value in data.items():
      html_table += f"<tr><td>{key}</td><td>{value}</td></tr>"
    
    html_table += "</table>"
    return html_table 

def generate_score_html(user_name,score) :
      style =   '    <style>  table { ' \
                                        'border-collapse: collapse; ' \
                                    '} ' \
                              'td {     border: 1px solid black; ' \
                                       'padding: 5px; ' \
                                       'text-align: left; ' \
                                  '}  ' \
                              'div {  display: inline; } ' \
                    ' }  </style>        '    
      if user_name:
          points_data_html =  '<h1>The score for user {user_name} is  </h1> ' \
                                    '<div id="score">{score}</div>'.format(user_name=user_name,score=score) 
      else :
          points_data_html =   '<h1>The scores for all users are : </h1>' \
                                  '<div id="score"> ' +  show_json_points_in_html_table(score) + ' </div>'
    
      html = '      <html> <head> {style} ' \
                                '<title>Scores Game</title>' \
                           '</head>' \
                           '<body>  {points_data}   </body>  ' \
                   '</html>'.format(points_data=points_data_html,style=style)
      
      
      return html



def score_server(user_name):
    try:
        data = get_user_score(user_name)
        if data != -1:  # we have data --> 0 for no score or no user , json for all list
            return generate_score_html(user_name,data)
        else :
            path =   os.path.join(os.getcwd() , SCORES_FILE_NAME.lstrip("./"))
            err_msg = 'scores data store is not available , or not valid. <br> please verify file and data in path : {path}'.format(path = path)
            err_code = BAD_RETURN_CODE
            raise Exception(f"code: {err_code} , Message: {err_msg}")
    except BaseException as e:
        return generate_error_response(str(e))
        
        
    
    
        
    
        