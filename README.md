# trump-tweet

## Developer Setup

### Windows

#### Install packages
Then run the 'devbuild' command to watch the filesystem for changes and reload quickly.
```bash
cd .\trump-tweet-app\
npm install
npm run devbuild
```

#### Run the development server
Open a new powershell window 
```bash
cd 'path/to/project/root'
.\trump-tweet-env\Scripts\activate.ps1
python .\src\app.py
```
http://localhost:8080/trump-tweet/content/devbuild.html

(to stop the venv, run 'deactivate')

#### Problems?
Run powershell as admin.
```bash
Set-ExecutionPolicy RemoteSigned 
```
Type 'Y' when prompted.


