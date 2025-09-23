from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time

# Настройки сервера
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обработка GET-запросов"""
        try:
            # Отправляем успешный статус
            self.send_response(200)

            # Устанавливаем правильный Content-Type для HTML
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            # Определяем путь к HTML-файлу
            html_file_path = "../form.html"

            # Проверяем существование файла
            if not os.path.exists(html_file_path):
                # Если файл не найден, отправляем ошибку 404
                self.send_error(404, "File not found")
                return

            # Читаем и отправляем HTML-файл
            with open(html_file_path, "r", encoding="utf-8") as file:
                html_content = file.read()
                # Преобразуем в байты и отправляем
                self.wfile.write(html_content.encode('utf-8'))

        except Exception as e:
            # Обработка ошибок
            self.send_error(500, f"Server error: {str(e)}")


    def do_POST(self):
        """Обработка POST-запросов"""
        try:


if __name__ == "__main__":
    # Создаем и запускаем сервер
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        webServer.server_close()
        print("Server stopped.")