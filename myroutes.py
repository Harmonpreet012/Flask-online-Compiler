from flask import  request,  send_file, render_template, redirect, jsonify, url_for
import datetime
import os
import time

def home():
    return render_template("home.html")
    
def compile():
    code = request.form['code']

    #writing code to file
    code_filename = "output.cpp"
    f = open("codes/"+code_filename, "w")
    f.write(code)
    f.close()

    #writing output of compilation to tile
    output_filename = code_filename+".txt"
    f = open( "codes/"+output_filename, "w")
    f.close()

    os.system("g++ "+os.getcwd()+"/codes/"+code_filename+" 2>"+ os.getcwd()+"/codes/"+output_filename)
    f = open('codes/'+output_filename, 'r')
    temp = f.read()
    lines = f.readlines()
    f.close()

    #if error exists, return errors
    if len(temp)>0:
        return "<h1>Error</h1><br>"+temp
    
    #writing output of code to file
    os.system('./a.out>'+os.getcwd()+"/codes/"+output_filename)
    f = open('codes/'+output_filename, 'r')
    output = f.read()
    f.close()

    #return output
    return "<h1>Compiled Successfully... </h1><br>"+output
