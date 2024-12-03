import time 
print(" salam in barname baraye search va etela'ate va ma'ani status code ha ast !!! ")
error = int(input("Enter your number Error ..... for example : 403 or 404 or 267 Enter !!! :"))

print("Loading !!! ")
time.sleep(2)
print("I Finding Error in database ")
time.sleep(3)

if error == 100 :
    print("Continue - ادامه")
    time.sleep(2)
    quit()


elif error == 101 :
    print("Switching Protocols - پروتکل انتقال")
    time.sleep(2)
    quit()


elif error == 102 :
    print("processing - پردازش")
    time.sleep(2)
    quit()


elif error == 200 :
    print("Ok - انجام شد یا بسیار خوب ")
    time.sleep(2)
    quit()


elif error == 201 :
    print("Created - ايجاد شده است ")
    time.sleep(2)
    quit()


elif error == 202 :
    print("Accepted - پذيرفته شده است ")
    time.sleep(2)
    quit()


elif error == 203 :
    print("Non_Authoritative Information ")
    time.sleep(2)
    quit()


elif error == 204 :
    print("No Content - فاقد محتوا")
    time.sleep(2)
    quit()


elif error == 205 :
    print ("Reset Content - تنظيم مجدد محتوا")
    time.sleep(2)
    quit()


elif error == 206 :
    print("Partial Content - محتوای ناقص جزئی")
    time.sleep(2)
    quit()


elif error == 207 :
    print("Multi_status - چند وضعیتی")
    time.sleep(2)
    quit()


elif error == 300 :
    print("Multiple Choices - چند گزینه ای ")
    time.sleep(2)
    quit()


elif error == 301 : 
    print("Moved Permanetly - انتقال دائم (معروف به ریدایرکت 301 )")
    time.sleep(2)
    quit()


elif error == 302 :
    print("Found - تغییر مسیر موقت")
    time.sleep(2)
    quit()


elif error == 303 :
    print("See Other - دیگری را ببینید ")
    time.sleep(2)
    quit()


elif error == 304 :
    print("Not Modified - اصلاح نشده ")
    time.sleep(2)
    quit()


elif error == 305 :
    print("Use Proxy - استفاده از پروکسی ")
    time.sleep(2)
    quit()


elif error == 307 :
    print("Temporary Redirect - تغییر مسیر موقت(ریدایرکت موقت)")
    time.sleep(2)
    quit()


elif error == 308 :
    print("Permanet Redirect - تغییر مسیر دائم")
    time.sleep(2)
    quit()


elif error == 400 :
    print("Bad request - درخواست بد")
    time.sleep(2)
    quit()


elif error == 401 :
    print("Unauthorized - غیرمجاز")
    time.sleep(2)
    quit()


elif error == 402 :
    print("Payment Required - پرداخت الزامی است")
    time.sleep(2)
    quit()


elif error == 403 :
    print("Forbidden - ممنوع")
    time.sleep(2)
    quit()


elif error == 404 :
    print(" error : Not Found - یافت نشد")
    time.sleep(2)
    quit()


elif error == 405 :
    print("Methhod Not Allowed - روش غیر مجاز ")
    time.sleep(2)
    quit()


elif error == 406 :
    print("Not Acceptable - غیر قابل پذیرش ")
    time.sleep(2)
    quit()


elif error == 407 :
    print("Proxy Authentication Required - تایید پروکسی الزامی است")
    time.sleep(2)
    quit()


elif error == 408 :
    print("Request Timeout - مهلت زمانی درخواست ، پایان یافته است")
    time.sleep(2)
    quit()


elif error == 409 :
    print("Conflict - تعارض  و یا تضاد")
    time.sleep(2)
    quit()
    

elif error == 410 :
    print("Gone - رفته(گذشته)")
    time.sleep(2)
    quit()


elif error == 411 :
    print("Length Required - طول مورد نیاز ")
    time.sleep(2)
    quit()


elif error == 412 :
    print("Precondition Failed - پیش نیاز لازم انجام نشد")
    time.sleep(2)
    quit()


elif error == 413 :
    print("Request Entity too large - موجودیت درخواست خیلی طولانی است")
    time.sleep(2)
    quit()


elif error == 414 :
    print(" Request-URL too Large - درخواست نشانی اینترنتی خیلی طولانی است ")
    time.sleep(2)
    quit()


elif error == 415 :
    print("Unsupported Media Type - این نوع رسانه پشتیبانی نمی شود ")
    time.sleep(2)
    quit()


elif error == 416 :
    print("Request Range Not Satisfiable - بعد درخواست ، راضیتبخش نیست ")
    time.sleep(2)
    quit()


elif error == 417 :
    print("Expectation Failed -  انتظار بر آورده نشد ")
    time.sleep(2)
    quit()


elif error == 421 :
    print("Misdirected Request - درخواست گمراه کننده")
    time.sleep(2)
    quit()


elif error == 422 :
    print("Unprocessable Entity - هویت غیر قابل پردازش")
    time.sleep(2)
    quit()


elif error == 423 :
    print("Locked - قفل شده ")
    time.sleep(2)
    quit()


elif error == 424 :
    print("Failed Dependency - وابستگی از بین رفت ")
    time.sleep(2)
    quit()


elif error == 425 :
    print("Unordered Collection - مجموعه نامرتب ")
    time.sleep(2)
    quit()


elif error == 426 :
    print("Upgrade Required - نیازمند به ارتقارسانی")
    time.sleep(2)
    quit()


elif error == 428 :
    print("Precondition Required - پیش نیاز لازم است ")
    time.sleep(2)
    quit()


elif error == 429 :
    print("To Many Requets - درخواست های زیاد")
    time.sleep(2)
    quit()


elif error == 431 :
    print("Request Header Fields Too Large - فیلد های درخواست سر صفحه خیلی بزرگ است")
    time.sleep(2)
    quit()


elif error == 451 :
    print("Unavailable For Legal Reasons - به دلالیل قانونی غیر قابل دسترس است")
    time.sleep(2)
    quit()


elif error == 500 :
    print("Internal Server Error - خطای سرویس دهنده ی داخلی")
    time.sleep(2)
    quit()


elif error == 501 :
    print("Not Implemented - قابل  اجرا نیست")
    time.sleep(2)
    quit()


elif error == 502 :
    print("Bad Gateway -  دروازه بد")
    time.sleep(2)
    quit()


elif error == 503 :
    print("Service Unavailable - خدمات در دسترس نیست ")
    time.sleep(2)
    quit()


elif error == 504 :
    print("Gateway Time-out - وقفه در دروازه")
    time.sleep(2)
    quit()


elif error == 505 :
    print("HTTP Version Not Suppoerted - قابل پشتیبانی نیست HTTP این نسخه از ")
    time.sleep(2)
    quit()


elif error == 506 :
    print("Variant Also Negotiates - متغیر قابل انتقال ")
    time.sleep(2)
    quit()


elif error == 507 :
    print("Insufficient Storage - فضای ذخیره سازی ناکافی است")
    time.sleep(2)
    quit()


elif error == 508 :
    print("Loop Detected - حلقه شناسایی شده است")
    time.sleep(2)
    quit()


elif error == 510 :
    print("Not Extended - تمدید نشده")
    time.sleep(2)
    quit()


elif error == 511 :
    print("Network Authentication - احراز صلاحیت شبکه مورد نیاز است ")
    time.sleep(2)
    quit()

    
elif error == 000 :
    print("0000000000000000")
    time.sleep(2)
    quit()

    
else :
    print("                                                                            ")
    print("____________________________________________________________________________")
    print("This is Not Status Code I Can't Find This In the app ")
    print("                                                                            ")
    print("____________________________________________________________________________")
    print("If you thing/know this is error of status codes  , you can report this to RPI_Network in Discord")
    print("                                                                            ")
    print("____________________________________________________________________________")
    print("DISCORD LINK OF RPI_NETWORK : https://discord.gg/p9T2RYceap ")
    print("                                                                            ")
    print("____________________________________________________________________________")
