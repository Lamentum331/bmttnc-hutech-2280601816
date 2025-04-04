# from flask import Flask, render_template, request, jsonify
# from cipher.caesar import CaesarCipher
# from cipher.vigenere import VigenereCipher
# from cipher.railfence import RailFenceCipher
# from cipher.playfair import PlayfairCipher  # Import PlayfairCipher

# app = Flask(__name__)

# # Router routes for home page
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Router routes for caesar cipher
# @app.route('/caesar')
# def caesar():
#     return render_template('caesar.html')

# @app.route('/encrypt', methods=['POST'])
# def caesar_encrypt():
#     text = request.form['inputPlainText']
#     key = int(request.form['inputKeyPlain'])
#     caesar_cipher = CaesarCipher()
#     encrypted_text = caesar_cipher.encrypt_text(text, key)
#     return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# @app.route('/decrypt', methods=['POST'])
# def caesar_decrypt():
#     text = request.form['inputCipherText']
#     key = int(request.form['inputKeyCipher'])
#     caesar_cipher = CaesarCipher()
#     decrypted_text = caesar_cipher.decrypt_text(text, key)
#     return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# # Router routes for vigenere cipher
# @app.route('/vigenere')
# def vigenere():
#     return render_template('vigenere.html')

# @app.route('/vigenere/encrypt', methods=['POST'])
# def vigenere_encrypt():
#     text = request.form['inputPlainText']
#     key = request.form['inputKeyPlain']
#     vigenere_cipher = VigenereCipher()
#     encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)
#     return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# @app.route('/vigenere/decrypt', methods=['POST'])
# def vigenere_decrypt():
#     text = request.form['inputCipherText']
#     key = request.form['inputKeyCipher']
#     vigenere_cipher = VigenereCipher()
#     decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)
#     return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# # Router routes for rail fence cipher
# @app.route('/railfence')
# def railfence():
#     return render_template('railfence.html')

# @app.route('/railfence/encrypt', methods=['POST'])
# def railfence_encrypt():
#     text = request.form['inputPlainText']
#     key = int(request.form['inputKeyPlain'])
#     railfence_cipher = RailFenceCipher()
#     encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
#     return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# @app.route('/railfence/decrypt', methods=['POST'])
# def railfence_decrypt():
#     text = request.form['inputCipherText']
#     key = int(request.form['inputKeyCipher'])
#     railfence_cipher = RailFenceCipher()
#     decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)
#     return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# # Router routes for playfair cipher
# # Router routes for playfair cipher
# @app.route('/playfair')
# def playfair():
#     return render_template('playfair.html')

# @app.route('/playfair/encrypt', methods=['POST'])
# def playfair_encrypt():
#     text = request.form['inputPlainText']
#     key = request.form['inputKeyPlain']
#     playfair_cipher = PlayfairCipher()
#     matrix = playfair_cipher.create_playfair_matrix(key)
#     encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
#     return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# @app.route('/playfair/decrypt', methods=['POST'])
# def playfair_decrypt():
#     text = request.form['inputCipherText']
#     key = request.form['inputKeyCipher']
#     playfair_cipher = PlayfairCipher()
#     matrix = playfair_cipher.create_playfair_matrix(key)
#     decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
#     return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
# # main function
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5050, debug=True)
from flask import Flask
import subprocess
import sys

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return '''
    <h1>Bảo mật thông tin nâng cao</h1>
    <ul>
        <li><a href="/caesar">Caesar Cipher UI</a></li>
        <li><a href="/vigenere">Vigenere Cipher UI</a></li>
        <li><a href="/railfence">Rail Fence Cipher UI</a></li>
        <li><a href="/playfair">Playfair Cipher UI</a></li>
    </ul>
    '''

# Route to open Caesar Cipher UI
@app.route('/caesar')
def open_caesar_ui():
    subprocess.Popen([sys.executable, './lab-03/caesar_cipher.py'])
    return '''
    <h1>Caesar Cipher đang chạy</h1>
    <a href="/">Back to Home</a>
    '''

# Route to open Vigenere Cipher UI
@app.route('/vigenere')
def open_vigenere_ui():
    try:
        subprocess.Popen([sys.executable, './lab-03/vigenere_cipher.py'])
        return '''
        <h1>Vigenere Cipher đang chạy</h1>
        <a href="/">Back to Home</a>
        '''
    except Exception as e:
        return f'''
        <h1>Error: {str(e)}</h1>
        <a href="/">Back to Home</a>
        '''

# Route to open Rail Fence Cipher UI
@app.route('/railfence')
def open_railfence_ui():
    subprocess.Popen([sys.executable, './lab-03/railfence_cipher.py'])
    return '''
    <h1>Rail Fence Cipher đang chạy</h1>
    <a href="/">Back to Home</a>
    '''

# Route to open Playfair Cipher UI
@app.route('/playfair')
def open_playfair_ui():
    subprocess.Popen([sys.executable, './lab-03/playfair_cipher.py'])
    return '''
    <h1>Playfair Cipher đang chạy</h1>
    <a href="/">Back to Home</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)