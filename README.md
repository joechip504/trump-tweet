# trump-tweet

## Developer Setup

### Windows

Run powershell as admin.

```bash
Set-ExecutionPolicy RemoteSigned 
```
Type 'Y' when prompted.


Open a new powershell window (not as admin).
```bash
cd 'path/to/project/root'
.\trump-tweet-env\Scripts\activate.ps1
python .\src\app.py
```
http://localhost:8080/trump-tweet/content/index.html

(to stop, run 'deactivate')
