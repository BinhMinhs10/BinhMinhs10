# Tips usefull with Ngrok :tada: :tada:

## Author
   **BinhMinhs10** :sparkles:
### 1. Install Ngrok in `ubuntu` 
```bash
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```
### 2. [Watch Dashboard](https://dashboard.ngrok.com/get-started/your-authtoken)


### 3. Add auth token
```bash
ngrok config add-authtoken your_token
```
### 4. Start Ngrok tunnel
```bash
ngrok http 8000
```