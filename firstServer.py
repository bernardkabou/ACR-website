from http.server import HTTPServer, SimpleHTTPRequestHandler
#permet d'importer le module HTTPServer pour gérer le server

host = 'localhost' 
port = 8080
#Adresse ip et port de communication du server

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Serveur démarré sur {host}:{port}")
try:
    server.serve_forever()
#configuration et démarrage du server

except KeyboardInterrupt:
    print("Arrêt du serveur.")
    server.server_close()
#arrêt du server si on fait ctl+c
