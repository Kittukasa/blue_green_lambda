def lambda_handler(event, context):

    html = """
    <html>
    <body style="background-color:blue;color:white;text-align:center;font-size:40px;">
    DEV VERSION - BLUE
    </body>
    </html>
    """

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html
    }