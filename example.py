from rcon import rcon

host = "localhost" # change for your hostname
port = "25566" # change for your port
password = "strongpassword" # change for your server's rcon password

server = rcon(host,port,password) # connect to the server

print(server.users()) # print the currently logged in users in JSON
print(server.status()) # print the server's current status - True = up, False = down
