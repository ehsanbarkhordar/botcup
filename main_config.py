import os


class Config:
    request_timeout = int(os.environ.get('REQUEST_TIMEOUT', 5))
    # 0:print to output        1:use graylog       2:both 0 and 1
    max_retries = int(os.environ.get('MAX_RETRIES', 1))
    check_interval = float(os.environ.get('CHECK_INTERVAL', 0.5))
    time_sleep = float(os.environ.get('TIME_SLEEP', 0.5))
    bot_token = os.environ.get('TOKEN', "699030590:AAFiDaS5AA2qlF1G07p_IFHjg6qwnTWfZVA")
    bot_user_id = os.environ.get('BOT_USER_ID', "41")
    admin_user_id_list = ["1497526823", "1341381900"]
    excel_mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    excel_format = "xlsx"
    excel_template_name = "template.xlsx"
    excel_sheet_name = "Sheet1"
    # Help image config
    help_file_id = os.environ.get('IMAGE_FILE_ID', "2173092373325285889")
    help_access_hash = os.environ.get('IMAGE_ACCESS_HASH', "201707397")
    help_file_size = os.environ.get('IMAGE_FILE_SIZE', "437026")
    help_name = os.environ.get('IMAGE_NAME', "kart_final.jpg")
    help_mime_type = os.environ.get('IMAGE_FILE_ID', "image/jpeg")
    help_thumb = os.environ.get('IMAGE_THUMB',
                                "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAA4KCw0LCQ4NDA0QDw4RFiQXFhQUFiwgIRokNC43NjMuMjI6QVNGOj1OPjIySGJJTlZYXV5dOEVmbWVabFNbXVn/2wBDAQ8QEBYTFioXFypZOzI7WVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVn/wAARCAAhAFoDASIAAhEBAxEB/8QAGwAAAQUBAQAAAAAAAAAAAAAAAAEDBAUHAgb/xAA7EAACAQMCAwILAw0AAAAAAAABAhEAAwQSIQUxQSJREzVCYXF0gZGxsvAGFMEWJTIzNERSY3KCkqHh/8QAGAEAAwEBAAAAAAAAAAAAAAAAAQIDBAD/xAAgEQACAgICAgMAAAAAAAAAAAAAAQIRAyESMSIyE0HB/9oADAMBAAIRAxEAPwDQLYtkdNQEnfl9RXehI5efnUHiD5dvHsnCBLlwHgA9mG7/ADxTnD3ybmOTlAi4GMSI2ikeTz47Bx8bJBS33UBELHYR7aNS6ghYBiCQs7wIn4j310mxJMRzHoprYhGOVi2823hu2nJuAsqQxkb9YjoacthT+kA3QSKq3y+Ipx7Ds6XbCayWuutk6Sw176t45LtPUVa29xM8jQk3xKJbO/BJt2F91J4O3qjQsjpApvFIFpLapcVbY0AuAJglfwn2ijGe0bYZSw0k2pY8yrFfjNRGHFW0wkKhBEgiKRRZbki8yOXdsaEU27SqAWCgKIAB7p50iqAQxMkTHtM0rlWg0d6Lf8C+6sw4txDNt8XzUTLyFRb7hVW4wAGo7DetOmFkmKyvjA/POdt+8XPmNUxu2BmqWSSxG2nSCN9+Z6U6YqJdyWsY7vCt4NS0d8VVD7SFmAFhZJjd4rV8cpbRBzjHTLi8iBXYFkaO0yJLGJ8xnnRZ27XhLrAAghkid+fIGqwcdMkMllSI53gZkx0FM/lL/IH+f/KWOOUvUV5IrtkrOu5aZKacizbQodVqAzHc7gmD3dOlWNkbHeoVzKfKstZtWrikgb3EKjn3mptk7Gs3LlbXWv009JJ9nRtIXLFQWMAmO4yP9mi5aS6oW4oIDBgPODIPvApblxLSarjBF23YwKaXMstupaNWmdB5yRHLvB+iKAaY/wBDTe3WmMjiFmwO2t4iY7Npj+FV+Bm8SzAt5ce391dZRiCCefSfRvyqUoOclX0GmlbLggxBiKyzi/jjO9YufMa99gXuM3swLlYtm3jBnBcCDtAGxPUzvFeB4x45zvWLnzGtME09iM0xOZpfJ/uNFFaiInkn20eSPrpRRXHAnX009a/VL6aKKlm9R49jgoNFFZSgeUKLn7O/9J+FFFVgBjlZLxnx1n+sXPmNFFUAf//Z")
    help_width = os.environ.get('IMAGE_WIDTH', "1187")
    help_height = os.environ.get('IMAGE_HEIGHT', "448")
    help_caption = os.environ.get('IMAGE_CAPTION', "راهنمای ارسال شماره هشت رقمی")
