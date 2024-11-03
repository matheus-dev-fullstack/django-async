python -m venv env
env\scripts\activate

pip install -r requirements.txt
uvicorn --reload asyncexercise.asgi:application