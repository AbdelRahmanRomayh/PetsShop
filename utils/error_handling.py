def api_error_handling(error):
    return {
        "code": error[1],
        "Message": error[0]
    }