print("کد برنامه ها:")
print("روز و ماه=1")
print("اعداد شگفت انگیز=2")
print("ستاره های شگفت انگیز=3")
print("زوج یا فرد!=4")
print("نمره سنج=5")
print("فیبوناچی=6")
print("خروج=7")
i=1
while i:
    app = int(input('کد برنامه ای که میخوای استفاده کنی رو وارد کن :', ))
    if app == 1:
        m = int(input("ماه رو وارد کن:", ))
        d = int(input("روز رو وارد کن:", ))
        if m > 12 or d > 31:
            print('هر سال 12 ماه داره و هر ماه نهایتا 31 روز داره پس نمیتونی ماه رو از 12 و روز رو از 31(برای نیمه اول سال) بیشتر وارد کنی')
        elif m == 12 and d > 19:
            print('امسال اسفند 29 روزس پس روز نباید از 29 بالاتر باشه')
        elif m >= 7 and d > 30:
            print('تعداد روز های نیمه دوم نمیتونه از 30 بیشتر باشه')
        elif m <= 7:
            s = (m - 1) * 31 + d
        else:
            s = (m - 1) * 30 + 6 + d
            days = ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهار شنبه", "پنجشنبه", "جمعه"]
            print(days[s % 7])
    elif app == 2:
        n = int(input("مقدار سطر هاتو وارد کن:", ))
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=' ')
            print()
    elif app == 3:
        n = int(input("مقدار سطر هاتو وارد کن:", ))
        for i in range(n):
            for j in range(i + 1):
                print('*', end=' ')
            print()
    elif app == 4:
        n = int(input('عددی که میخوای امتحان کنی رو وارد کن:', ))
        if n % 2 == 0:
            print("عدد مورد نظر شما زوج است")
        else:
            print('عدد موزد نظر شما فرد است')
    elif app == 5:
        n = float(input("معدلی که میخوای بسنجی رو وارد کن:", ))
        if 17 <= n <= 20:
            print('خیلی خوب!')
        elif 14 <= n <= 16:
            print('خوب')
        elif 9 <= n <= 13:
            print('قابل قیول')
        elif 0 <= n <= 8:
            print('نیاز به تلاش بیشتر')
    elif app == 6:
        def Fibonachi(n):
            if n < 0:
                print("Incorrect input")
            elif n == 1:
                return 0
            elif n == 2:
                return 1
            else:
                return Fibonachi(n - 1) + Fibonachi(n - 2)


        x = int(input("چندمین جمله دنباله فیبوناچی رو میخوای بدونی:", ))
        print(f'دنباله {x}ام فیبوناچی{Fibonachi(x)}هستش')
    elif app == 7:
        print("مرسی که از برنامه استفاده کردی ^^")
        print()
        print("ورژن فعلی:1.1")
        print()
        print("روز یا شب خوبی داشته باشی!!!!")
        print()
        print(':D           *ــــ*')
        break
    else:
        print("ببخشید برنامه مورد نظر موجود نیست یا کد اشتباه هست ):")
        print("اگه میتونید به ما بگید ما اگه به تونیم اضافش میکنیم یا ایراداتمون رو برطرف میکنیم   @ــــ@")