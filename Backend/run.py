from flask import Flask, render_template, request, redirect, url_for, jsonify
from app import app


app.run(host='192.168.43.227', port=9999, debug=True)
