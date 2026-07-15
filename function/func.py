from parliament import Context


def main(context: Context):
    body = context.request.json if context.request.content_type == "application/json" else {}
    return {"message": "Hello from test-func-python!", "input": body}, 200
// save test// save test// save test// save test// save test