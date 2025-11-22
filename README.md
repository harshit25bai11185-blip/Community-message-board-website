# community-message-board-website
This project demonstrates full CRUD (Create, Read, Update, Delete) functionality using a serverless SQLite database.

# technical stack used:
language: python
web framework: flask
database: SQLite (serverless)
orm: SQLchemy
feontend: HTML, CSS, BOOTSTRAP

# project structure
 simple_chat/
│
├── app.py               # Main application entry point and backend logic
├── chats.db             # SQLite database (auto-generated on first run)
├── README.md            # Project documentation
└── templates/           # HTML templates for the frontend
    ├── base.html        # Base template containing the HTML skeleton & CSS
    ├── index.html       # Home page displaying the list of chats (Read)
    └── create_edit.html # Form page for adding (Create) and editing (Update) chats

# code documentation
--> Database Model:
id: Integer (Primary Key) - Unique identifier for every message.
sender: String(100) - Stores the name of the message sender.
receiver: String(100) - Stores the name of the intended recipient.
message: Text - Stores the body of the message.

Note: The database file chats.db is automatically created via db.create_all() if it does not exist.

--> backend routes:
1) / : type: GET
       description: shows all the chats using chat.query.all() and renders index.html
       operation: READ
1) /create : type: GET, POST
       description: GET: renders a form to crate the chat.
                    POST: creates a chat object and commits it to Database.
       operation: CREATE
1) / : type: GET, POST
       description: GET: fetches chats by their specific ids.
                    POST: updates the chat object and commits it to database.
       operation: UPDATE
1) / : type: GET
       description: GET: fetches chats by their specific ids and removes it from the database
       operation: DELETE

--> Frontend templates:
base.html: cotains <head> bootstrap data and CDN links and defines the global css styling.
           uses {% block content %} to allow other pages to inject their content.
           
index.html: Inherits from base.html. Uses a Jinja2 {% for chat in chats %} loop to generate a                card for every message found in the database. Includes logic to display a specific              "No messages" view if the database is empty.

create.html: Inherits from base.html. Acts as a dual-purpose page. It checks {% if chat %} to                 decide whether to display "Edit Message" (pre-filling inputs with existing data) or              "Compose Message" (empty inputs).

