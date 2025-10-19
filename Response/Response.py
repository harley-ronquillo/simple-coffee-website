class HttpResponse:
    def create_response(self, data, message, status):
        payload = {"status": status}
        if data:
            payload["data"] = data
        if message:
            payload["message"] = message
        response = {
            "status": status,
            "message": message,
            "data": data
        }
        return response

    def success(self, data, message, status=201):
        return self.create_response(data, message, status)

    def error(self, data, message, status=500):
        return self.create_response(data, message, status)
