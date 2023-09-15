
curl -k -H 'Authorization: Basic your_auth' 'https://chipmunk-gentle-heartily.ngrok-free.app/api/tutorials/dniv4/ThikgBAwp11Dd4OgHwRN3Q=='  

curl -k -H 'Authorization: Basic your_auth' -x http://localhost:8080 'https://chipmunk-gentle-heartily.ngrok-free.app/api/tutorials/dniv4/ThikgBAwp11Dd4OgHwRN3Q=='  

-----------------------------------------

curl -k -H 'Authorization: Basic your_auth' -x http://localhost:8081 'https://chipmunk-gentle-heartily.ngrok-free.app/api/tutorials/dniv4/ThikgBAwp11Dd4OgHwRN3Q=='  

-----------------------------------------

sudo apt install pipx  
pipx install mitmproxy  

pipx inject mitmproxy pycryptodome  
find ~/.local/pipx/venvs/mitmproxy | grep -i pycryptodome  

-----------------------------------------

cd /tmp  
git clone https://github.com/oscarmrdc/workshop_mobile.git  

cd /tmp/workshop_mobile  
~/.local/bin/mitmdump -s mitmproxy_cipher_dni_aburp.py --mode upstream:http://localhost:8080 --ssl-insecure --listen-port 8081  

curl -k -H 'Authorization: Basic your_auth' -x http://localhost:8081 'https://chipmunk-gentle-heartily.ngrok-free.app/api/tutorials/dniv4/ThikgBAwp11Dd4OgHwRN3Q=='  

cd /tmp/workshop_mobile  
~/.local/bin/mitmdump -s mitmproxy_cipher_dni_deburp.py --listen-port 8082  

