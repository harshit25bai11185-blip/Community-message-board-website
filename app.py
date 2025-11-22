from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for the SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- DATABASE MODEL ---
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create the database file automatically if it doesn't exist
with app.app_context():
    db.create_all()

# --- ROUTES ---

# 1. READ: Home Page (Display all chats)
@app.route('/')
def index():
    # Get all chats from database
    all_chats = Chat.query.all()
    return render_template('index.html', chats=all_chats)

# 2. CREATE: Add a new chat
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_sender = request.form['sender']
        new_receiver = request.form['receiver']
        new_message = request.form['message']

        new_chat = Chat(sender=new_sender, receiver=new_receiver, message=new_message)
        db.session.add(new_chat)
        db.session.commit()
        return redirect(url_for('index'))
    
    # If GET, show the form (passing None for chat implies creation mode)
    return render_template('create_edit.html', chat=None)

# 3. UPDATE: Edit an existing chat
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    chat_to_edit = Chat.query.get_or_404(id)

    if request.method == 'POST':
        chat_to_edit.sender = request.form['sender']
        chat_to_edit.receiver = request.form['receiver']
        chat_to_edit.message = request.form['message']

        db.session.commit()
        return redirect(url_for('index'))

    # If GET, show the form pre-filled with existing chat data
    return render_template('create_edit.html', chat=chat_to_edit)

# 4. DELETE: Remove a chat
@app.route('/delete/<int:id>')
def delete(id):
    chat_to_delete = Chat.query.get_or_404(id)
    
    db.session.delete(chat_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)