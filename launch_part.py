{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "FastAPI: app.py",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": ["app:app", "--host", "127.0.0.1", "--port", "8000", "--reload"],
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}



'''
basically for the debug it has been implemented 
'''