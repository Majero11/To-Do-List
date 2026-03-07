# entry point to the application 

from app import app 

if __name__ == "__main__":
    # debug = true only for development phase -> you can see error 
    app.run(debug=True)