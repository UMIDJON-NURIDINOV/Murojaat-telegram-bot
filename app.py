
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from keyboard import btn, btn2
from keyboard import btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn11
from keyboatdBtn import btn10, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19
from keyboatdBtn import btn20, btn21

token = '6233181361:AAHK0rbrG-szEOpayek27iMugcX1goWcSDU'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands='start',)
async def Start(message:types.Message):
    await message.answer(f'Hurmatli fuqaro o\'zingiz uchun qulay tilni tanlang.\n'
                         f'\n'
                         f'Уважаемый гражданин, выберите удобный для вас язык.', reply_markup=btn11)
  



@dp.callback_query_handler(text='uzb')
async def Lang(lang:types.CallbackQuery):
    await lang.answer(cache_time=60)
    await lang.message.answer(f'Hurmatli fuqaro o\'zingizni qiziqtirgan savolni tanlash orqali unga qonuniy javob olishingiz mumkin. Savollaringizga javob olish uchun boshlash tugmasini bosing', reply_markup=btn10)

@dp.callback_query_handler(text='boshlash')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

# Texnik ko`rik start


@dp.callback_query_handler(text='texkorik')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Transport vositalarin texnik ko\'rikdan o\'tkazish.\n'
                              f'1. Savol: Jismoniy shaxslarga qarashli bo\'lgan transport vositalarining texnik ko\'rigi qaysi davriylikda o\'tkaziladi? \n'
                              f'2. Savol: Jismoniy shaxslarga tegishli yengil avtomobil necha yilda texnik ko\'rikdan o\'tadi? \n'
                              f'3. Savol: Meni avtomobilimga o\'rnatilgan metan gaz baloni necha yilda sinovdan o\'tkazishim kerak? \n',  reply_markup=btn2)
@dp.callback_query_handler(text='1')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'1-savolga javob: Vazirlar Mahkamasining 2021 yil 9 martdagi 125-son qarori bilan tasdiqlangan Transport vositalarini majburiy texnik ko\'rikdan o\'tkazish tartibi to\'g\'risida nizomning 6-bandiga asosan Jismoniy va yuridik shaxslarga tegishli boshqa transport vositalarining texnik ko\'rigi 1 yanvar — 31 dekabrda o\'tkaziladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='2')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'2-savolga javob: Vazirlar Mahkamasining 2021 yil 9 martdagi 125-son qarori bilan tasdiqlangan Transport vositalarini majburiy texnik ko\'rikdan o\'tkazish tartibi to\'g\'risida nizomning 5-bandining: \n'
                              f'b-kichik bandiga asosan, ishlab chiqarilganiga o\'n bir yildan o\'n to\'rt yilgacha (o\'n to\'rtinchi yili ham) bo\'lgan jismoniy shaxslarga tegishli M1 toifadagi transport vositalari (mazkur bandning “a” kichik bandida ko\'rsatilgan transport vositalaridan tashqari) — ikki yilda bir marta; \n'
                              f'v-kichik bandiga asosan, ishlab chiqarilgan vaqti aniq bo\'lmagan transport vositalari (mazkur bandning “a” kichik bandida ko\'rsatilgan transport vositalaridan tashqari), shuningdek, ishlab chiqarilganiga o\'n besh yil va undan ortiq bo\'lgan jismoniy shaxslarga tegishli M1 toifadagi transport vositalari (mazkur bandning “a” kichik bandida ko\'rsatilgan transport vositalaridan tashqari) — bir yilda bir marta.\n'
                              f'Ishlab chiqarilganiga o\'n yilgacha (o\'ninchi yili ham) bo\'lgan jismoniy shaxslarga tegishli M1 toifadagi transport vositalari (mazkur bandning “a” kichik bandida ko\'rsatilgan transport vositalaridan tashqari) texnik ko\'rikdan ixtiyoriy ravishda o‘tkaziladi.\n\n'
                               f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='3')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'3-savolga javob: Vazirlar Mahkamasining 2015 yil 15 noyabrdagi 326-son qarori bilan tasdiqlangan Siqilgan tabiiy gazda, suyultirilgan neft gazida yoki dizel va gazsimon yoqilg\'i aralashmasida ishlaydigan transport vositalarining xavfsizligi to\'g\'risida umumiy texnik reglamentning 77-bandiga asosan avtomobillarga o\'rnatilgan siqilgan tabiiy gaz (metan) ballon xar uch yilda bir marta texnik sinovdan o\'tkaziladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


# Texnik ko`rik end


# Haydovchilik guvohnomasi start



@dp.callback_query_handler(text='prava')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.\n'
                              f'Haydovchilik guvohnomasiga oid savollar.\n'
                               f'1. Savol: Eski namunadagi haydovchilik guvohnomalarini almashtirish muddatlari qachongacha qilib belgilangan? \n'
                               f'2. Savol: O\'zbekiston Respublikasi fuqarosining xorijda olgan haydovchilik guvohnomasi respublika hududida avtomobil boshqarish huquqini beradimi? \n'
                               f'3. Savol: Eski namunadagi haydovchilik guvohnomalarini almashtirish tartibi qanaqa? Belgilangan vaqtda almashtirmagan haydovchilik guvohnomalarini almashtirishga murojaat qilinganda jarima to\'lanadimi? \n'
                               f'4. Savol: Haydovchilik huquqidan mahrum etilgan shaxslarning haydovchilik guvohnomalarini olish tartibi qanaqa? \n'
                               f'5. Savol: Yo\'qolgan haydovchilik guvohnomalarini qayta tiklash qanday tartibda amalga oshiriladi? \n', reply_markup=btn3)



@dp.callback_query_handler(text='4')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f' 1-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022 yil 12 apreldagi 178-son Qarorida eski namunadagi haydovchilik guvohnomalarini almashtirish muddatlari belgilangan. Jumladan: \n'
                               f'2010 yilgacha bo‘lgan davrda berilganlari — 2023 yil 31 martga qadar; \n'
                               f'2010 — 2012 yillarda berilganlari — 2023 yil 30 iyunga qadar; \n'
                               f'2013 — 2015 yillarda berilganlari — 2023 yil 30 sentyabrga qadar; \n'
                               f'2015 yildan keyin berilganlari — 2023 yil 31 dekabrga qadar muddatlarda majburiy tartibda amalga oshiriladi; \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='5')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'2-savolga javob O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 31 maydagi 408-sonli qarori talablariga asosan (2-ilova, 74-bandi), xalqaro haydovchilik guvohnomalari O\'zbekiston Respublikasi hududida avtomototransport vositalarini boshqarish uchun haqiqiy hisoblanadi. \n'
                               f'O\'zbekiston Respublikasi fuqarolari uchun O\'zbekiston Respublikasi hududida faqat O\'zbekiston Respublikasining milliy haydovchilik guvohnomasi avtomototransport vositalarini boshqarish uchun haqiqiy hisoblanadi. \n'
                               f'Shuningdek, (2-ilova, 76-bandi) boshqa xorijiy fuqarolar va fuqaroligi bo\'lmagan shaxslarning hamda O\'zbekiston Respublikasi fuqarolarining xorijiy davlatlarda olgan haydovchilik guvohnomalarini O\'zbekiston Respublikasining milliy haydovchilik guvohnomalariga almashtirishdan oldin ular YHXX orqali Tashqi ishlar vazirligida tekshiriladi va tekshirish natijasida haydovchilik guvohnomalari tasdiqlangan shaxslarning haydovchilik guvohnomasi, ular tibbiy ko\'rikdan o\'tib, nazariy va amaliy imtihonlarni topshirganlaridan so\'ng, O\'zbekiston Respublikasining milliy haydovchilik guvohnomalariga almashtiriladi. \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='6')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'3-savolga javob: Eski namunadagi milliy haydovchilik guvohnomalari yangisiga almashtirish “Davlat xizmatlari markazi” yoki hududiy DYXXX orqali fuqarolik pasporti (yoki shaxsini tasdiqlovchi boshqa hujjat) va eski namunadagi haydovchilik guvohnomasi va ogohlantirish talonini taqdim etadi va belgilangan BHMning 70 foizi miqdorida (231 ming so‘m) to\'lovni amalga oshiradi. \n'
                               f'Davlat xizmatlari markazi tomonidan fuqarolarga qulay shart-sharoitlar yaratish maqsadida murojaatni elektron tarzda yo\'llash va tayyor xujjatni fuqarolarning yashash manziliga yetkazib berish axborot dasturi amaliyoti joriy etilib, hozirgi vaqtda to\'liq ishga tushirilgan bo\'lib, ushbu amaliyot xududiy davlat xizmatlari markazi orqali amalga oshiriladi, yaʼni murojaat qilayotgan shaxsga uning yashash manzili bo\'yicha xizmat ko\'rsatuvchi DHM xodimi tomonidan qo\'shimcha to\'lov evaziga yangi namunadagi haydovchilik guvohnomasi olib borib beriladi va shaxsan uning egasiga topshiriladi. \n'
                               f'Haydovchi belgilangan muddatlarda almashtirmagan eski namunadagi haydovchilik guvohnomasi bilan avtomobil boshqarsa O\'zbekiston Respublikasi  MJtKning 135-moddasiga asosan maʼmuriy javobgarlikka tortishga asos bo\'ladi, lekin muddati o\'tgan haydovchilik guvohnomasini almashtirishga jarima solinish ko\'zda tutilmagan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='7')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f' 4-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 31 maydagi 408-son qarorida avtomototransport vositalarini mast holda boshqarganligi uchun boshqarish huquqidan mahrum qilingan shaxslar, milliy haydovchilik guvohnomasini qayta olishlari uchun uchun, mahrum qilish muddatidan qatʼi nazar, maʼmuriy jazo muddati nihoyasiga yetgach, majburiy tibbiy ko\'rikdan o\'tishlari, malaka oshirish kurslarida taʼlim olishlari va nazariy hamda amaliy imtihonlarni topshirishlari shartligi belgilab berilgan. \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='8')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'5-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 31 maydagi 408-sonli qaroriga muvofiq yo\'qolgan haydovchilik guvohnomalarini tiklash haydovchining arizasi, imtihon varaqasi, tegishli toifalardagi avtomototransport vositalarini boshqarishga yaroqliligi to\'g\'risidagi tibbiy maʼlumotnoma, imtihon varaqasi mavjud bo\'lmagan hollarda hududiy YHXBning RO\'vaIOBlarining tasdiqnomasi hamda BHMning 1 baravari miqdorida to\'lov to\'langanligini tasdiqlovchi kvitansiya asosida almashtirib beriladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)






# Haydovchilik guvohnomasi end




# Texpasport start




@dp.callback_query_handler(text='texpasport')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Avtomototransport vositalarini ro\'yxatdan o\'tkazishga oid savollar. \n'
                              f'1. Savol: O\'zimni doimiy yashash joyim boshqa hududda. Lekin o\'zim Toshkent shahrida ishlayman va yashayman, Toshkent shahridan yangi avtomashina sotib oldim, Toshkent shahar IIBB YHXBdan davlat raqami olsam bo\'ladimi?\n'
                              f'2. Savol: DYHXX organlarida qanday turdagi transport vositalari ro\'yxatdan o\'tkaziladi? \n',  reply_markup=btn4)



@dp.callback_query_handler(text='9')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'1-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2021 yil 4 maydagi 271-son qaroriga muvofiq sotib olgan avtomototransport vositangizni xohlagan hududingizdan davlat ro\'yxatidan o\'tkazishingiz mumkin. Bunda Siz avtomashinangizga doimiy ro\'yxatga turgan hududingiz bo\'yicha belgilangan seriyali davlat raqami bilan ro\'yxatdan o\'tkazishingiz mumkin.  \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='10')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'2-savolga javob: DYHXX organlarida dvigateli 50 va undan ortiq kub.sm ish hajmiga ega bo\'lgan yoki konstruksiyaviy tezligi soatiga 50 va undan ortiq kilometr bo\'lgan avtomototransport vositalari, elektrodvigatelining quvvati 4 kVt va undan ortiq yoki soatiga 40 va undan yuqori tezlikka ega bo\'lgan elektromobillar (elektromototsikllar, elektroskuterlar va boshqalar), shuningdek, tirkama va yarim tirkamalar\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)





# Texpasport end




# Qayta jihoz start




@dp.callback_query_handler(text='qaytajihoz')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Avtomototransport vositalarini qayta jihozlashga oid savollar. \n'
                              f'1. Savol: Yengil toifadagi avtotransport vositalarini oynalarini tusini o\'zgartirish (qoraytirish)  uchun bazaviy hisoblash miqdorining necha baravarida to\'lov amalga oshiriladi? \n'
                              f'2. Savol: Ishlab chiqarilganiga necha yil bo\'lgan avtomototransport vositalari qayta jixozlanishiga ruxsat etiladi? \n'
                              f'3. Savol: Avtotransport vositalarini qayta jihozlash tartibini tushuntiring? \n', reply_markup=btn5)



@dp.callback_query_handler(text='11')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'1-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2017 yil 1 sentyabrdagi 547-son qaroriga muvofiq, Yengil toifadagi  avtotransport vositalarini orqa va orqa yon oynalarini yorug\'lik o‘tkazuvchanligi cheklanmagan darajada o\'zgartirish (qoraytirish) ruxsatnomasiz, old yon oynalarining tusini yorug\'lik o\'tkazuvchanligi-30 foizdan kam bo\'lmagan darajada o\'zgartirish (qoraytirish) tasdiqlangan davlat standarti bo\'yicha, bazaviy hisoblash miqdorining sakkiz baravari miqdorida to\'lovni amalga oshirish lozim bo\'ladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='12')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'2-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining  2020 yil 30 noyabrdagi 758-son qarori talablariga asosan ishlab chiqarilganiga 20 yil va undan ko\'p muddat bo\'lmagan avtomototransport vositalariga belgilangan tartibda ruxsat etiladi. \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='13')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'3-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022-yil 22-fevral kunidagi 86-son (26-ilovasi) qaroriga muvofiq jismoniy va yuridik shaxslar tomonidan ruxsat etish xususiyatiga ega hujjatni olish uchun ariza berish “license.gov.uz” axborot tizimi, O\'zbekiston Respublikasi Yagona interaktiv davlat xizmatlari portali yoki Davlat xizmatlari markazlari orqali davlat boji (BHMning 30% foizi miqdorida) undirilgan holda yuborilishi belgilangan.  Qaror talablariga asosan 15 ish kuni mobaynida elektron shakldagi javob xatini (ruxsatnoma yoki rad etilganligi to\'g\'risida) olishingiz mumkin. Shuningdek, mazkur qaror bilan ishlab chiqarilganiga 20 yil va undan ortiq muddat o\'tgan (avtotransport vositasining ishlab chiqarilgan yilidan qatʼiy nazar, uning dvigateli va kuzovini xuddi shu rusumli avtomobilniki bilan almashtirish bundan mustasno)  avtomototransport vositalarini qayta jihozlashga yo\'l qo\'yilmasligi belgilangan. \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


# Qayta jihoz end





# Yo`l infratuzilmasi start

@dp.callback_query_handler(text='yolinfratuzilmasi')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Yo\'l infratuzilmasini nazorat qilishga oid savollarga javoblar. \n'
                              f'1. Savol: Mahallamiz hududidan o\'tuvchi avtomobil yo\'lida svetofor  o\'rnatish uchun kimga murojaat qilishim kerak. Svetofor o\'rnatish tartibi to\'g\'risida maʼlumot bering? \n'
                              f'2. Savol: Avtomobil yo\'lini taʼmirlash va yo\'ldagi nosozliklarni bartaraf qilish uchun kimga va qayerga murojaat qilishim kerak? \n'
                              f'3. Savol: Avtomobil yo\'lida qayrilib olish joyini ochish qaysi meʼyoriy hujjat asosida amalga oshiriladi? \n'
                              f'4. Savol: Mahallamiz hududidan transport vositalari yuqori tezlikda harakatlanishi uchun mo\'ljallangan tranzit avtomobillar harakatlanadigan 6 tasmali serqatnov avtomobil yo\'li o\'tgan. Mazkur avtomobil yo\'lida piyodalar o\'tish joyi tashkil qilsa bo\'ladimi? \n'
                              f'5. Savol: Yuk avtomobillarida “Qamchiq” dovoni orqali harakatlanishim mumkinmi? \n'
                              f'6. Savol: Avtomobil yo\'llari va ko\'chalarda transport vositalari harakat tezligi pasaytirish uchun o\'rnatiladigan “Sunʼiy notekislik”lar qachon o\'rnatiladi. “Sunʼiy notekislik” o\'rnatish uchun kimga murojaat qilsam bo\'ladi? \n'
                              f'7. Savol: Katta avtomobil yo\'lida o\'rnatilgan piyodalar svetoforidan piyodalar yo\'lni kesib o\'tishga ulgurmasdan piyodalar uchun mo\'ljallangan svetofor yashil ishorasi o\'chib qizil ishorasi yonadi. Svetofor rejimlarni o\'zgartish uchun kimga murojaat qilish kerak? \n'
                              f'8. Savol: Xavfli yuklarni avtomobil transportida tashish yo\'nalishlari kimlar bilan kelishiladi? \n'
                              f'9. Savol: Bizni mahallamizdan transport vositalar yuqori tezlikda harakatlanadi. Tezlikni pasaytiruvchi yo\'l belgilarini o\'rnatish tartibi to\'g\'risida tushunchalar bering? \n'
                              f'10. Savol: Katta hajmli va og\'ir vaznli yuklarni tashish uchun qaysi tashkilot ruxsatnoma beradi? \n', reply_markup=btn6)



@dp.callback_query_handler(text='14')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'1-savolga javob: O\'zbekiston Respublikasining “Yo\'l harakati xavfsizligi to\'g\'risida”gi Qonunining 13-moddasi 3-xatboshida yo\'llarini saqlashda ularning holati yo\'l harakati xavfsizligi sohasidagi normativ hujjatlar talablariga muvofiqligini taʼminlash bo\'yicha majburiyat mazkur yo\'llar qaysi yuridik va jismoniy shaxslar tasarrufida bo\'lsa, shu yuridik va jismoniy shaxslar zimmasiga yuklatilishi belgilab qo\'yilgan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='15')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'2-savolga javob: O\'zbekiston Respublikasining “Avtomobil yo\'llari to\'g\'risida”gi Qonunining 15-moddasida avtomobil yo\'llarini taʼmirlash va saqlash (xizmat ko\'rsatish) mazkur yo\'llar qaysi yuridik va jismoniy shaxslar ixtiyorida bo\'lsa, o\'sha yuridik va jismoniy shaxslar tomonidan taʼminlanishi, shuningdek 16-moddasida yo\'l tashkilotlari avtomobil yo\'llarining soz holatda bo\'lishini, ulardan transport vositalari muttasil va xavfsiz o\'tishini taʼminlashi shartligi belgilab qo\'yilgan. \n'
                              f'O\'zbekiston Respublikasining “Yo\'l harakati xavfsizligi to\'g\'risida”gi Qonunining 13-moddasi 3-xatboshida yo\'llarini saqlashda ularning holati yo\'l harakati xavfsizligi sohasidagi normativ hujjatlar talablariga muvofiqligini taʼminlash bo\'yicha majburiyat mazkur yo\'llar qaysi yuridik va jismoniy shaxslar tasarrufida bo\'lsa, shu yuridik va jismoniy shaxslar zimmasiga yuklatilishi belgilab qo\'yilgan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='16')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'3-savolga javob: O\'zbekiston Davlat arxitektura va qurilish qo\'mitasi tomonidan tasdiqlangan Avtomobil yo\'llari SHNQ 2.05.02-07 talablari asosida qayrilib olish joylari loyihalanadi va tashkil etiladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='17')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'4-savolga javob: O\'zbekiston Davlat arxitektura va qurilish qo\'mitasi tomonidan tasdiqlangan Avtomobil yo\'llari SHNQ 2.05.02-07 talablari asosida transport vositalari yuqori tezlikda harakatlanishi uchun mo\'ljallangan tranzit avtomobillar harakatlanadigan I va II toifali avtomobil yo\'llarda piyodalar o\'tish joylarini tashkil etishda avtomobil yo\'llari bilan bir sathda kesib o\'tilishiga yo\'l qo\'yilmadi. Ushbu joylarda piyodalar harakati jadalligiga qarab turli sathlardagi piyodalar yo\'lkalari (yer ostki va ustki) tashkil qilinadi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='18')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'5-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 06 apreldagi “Qamchiq davoni orqali avtomobil transportida yuk tashishni yanada tartibga solish chora-tadbirlari to\'g\'risida” 268-sonli qarori bilan “Qamchiq” dovonida ishlab chiqarilganiga               20 yildan  oshgan yuk avtomobillari va avtomobil tirkamalarida yuk tashish taqiqlanadi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='19')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'6-savolga javob:  “Sunʼiy notekisliklar. Umumiy texnik talablar. Qo\'llash tartibi” deb nomlangan O\'zDst 3403 O\'zbekiston Respublikasi davlat standarti ishlab chiqilgan. Shuningdek, O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022 yil 12 apreldagi “Yo\'l harakati qoidalarini tasdiqlash to\'g\'risidagi” 172-sonli qarorida “Sunʼiy yo\'l notekisligi” yo\'l belgisi amaldagi yo\'l harakati qoidalariga kiritilgan. \n'
                              f'Mazkur Davlat standarti asosida sunʼiy yo\'l notekisliklari bolalar va yoshlar taʼlim-tarbiya muassasalari yonida tartibga solinmagan yer usti piyodalar yo\'lakchalaridan 10-15 metr oldinroq, avariyaviylik sabablari tahliliga ko\'ra yo\'llarning maʼlum qismlarida, ayniqsa bolalar va yoshlar taʼlim-tarbiya muassasalari oldidagi xavfli hududlar boshida, bolalar maydonchasi, jamoat dam olish joylarida, stadionlar, vokzallar, do\'kon va piyodalar jamlanadigan boshqa obyektlar oldida o\'rnatilish belgilangan. \n'
                              f'O\'zbekiston Respublikasi “Avtomobil yo\'llari to\'g\'risida”gi qonunining 10-moddasi 2-xatboshisida “Shaharlar va boshqa aholi punktlarining ko\'chalari davlat mulki bo\'lib, mahalliy davlat hokimiyati organlari ixtiyorida bo\'ladi”, 15-moddasida “Avtomobil yo\'llarini taʼmirlash va saqlash mazkur yo\'llar qaysi yuridik va jismoniy shaxslar ixtiyorida bo\'lsa, o\'sha yuridik va jismoniy shaxslar tomonidan taʼminlanishi”, shuningdek 16-moddasida “Yo\'l tashkilotlari avtomobil yo\'llarining soz holatda bo\'lishini, ulardan transport vositalari muttasil va xavfsiz o\'tishini taʼminlashi shart”-deb belgilab qo\'yilgan.  \n'
                              f'O\'zbekiston Respublikasining “Yo\'l harakati xavfsizligi to\'g\'risidagi”gi Qonunining 13-moddasi 3-xatboshida yo\'llarini saqlashda ularning holati yo\'l harakati xavfsizligi sohasidagi normativ hujjatlar talablariga muvofiqligini taʼminlash bo\'yicha majburiyat mazkur yo\'llar qaysi yuridik va jismoniy shaxslar tasarrufida bo\'lsa, shu yuridik va jismoniy shaxslar zimmasiga yuklatilishi belgilab qo‘yilgan. \n'
                              f'Ushbu qonunlar va davlat standarti talablari asosida yo\'lga egalik qiluvchi tashkilot (mahalliy hokimliklar, avtomobil yo\'llari korxona)lar tomonidan “sunʼiy notekisliklar” o\'rnatiladi hamda hududiy DYHXX bilan kelishiladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='20')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'7-savolga javob: O\'zbekiston Respublikasining “Yo\'l harakati xavfsizligi to\'g\'risidagi”gi Qonunining 13-moddasi 3-xatboshida yo\'llarini saqlashda ularning holati yo\'l harakati xavfsizligi sohasidagi normativ hujjatlar talablariga muvofiqligini taʼminlash bo\'yicha majburiyat mazkur yo\'llar qaysi yuridik va jismoniy shaxslar tasarrufida bo\'lsa, shu yuridik va jismoniy shaxslar zimmasiga yuklatilishi belgilab qo\'yilgan. \n'
                              f'Ushbu qonun talablari asosida yo\'lga egalik qiluvchi tashkilotga hamda hududiy DYHXXga murojaat qilinadi. Murojaatda svetofor o\'rnatish manzili va joyi(lokatsiyasi) ko\'rsatiladi. Masʼul xodimlar tomonidan svetofor rejimlari qo\'shimcha o\'rganilib, davlat standarti talablariga muvofiq yoki muvofiq emasligi bo\'yicha chiqarilgan xulosalar asosida svetofor rejimi o\'zgartiriladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='21')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'8-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 35-sonli qarori 56-bandida Xavfli yuklarni transportda tashish yo\'nalishlarini kelishish uchun yukni tashuvchi tashish boshlanishidan kamida o\'n kun oldin hududi bo\'ylab xavfli yukni tashish mo\'ljallanayotgan hududiy yo\'l harakati xavfsizligi boshqarmasiga quyidagi hujjatlarni taqdim etishi shartligi belgilangan: \n'
                              f'a) belgilangan shakl bo\'yicha tashishning ishlab chiqilgan yo\'nalishi uch nusxada; \n'
                              f'b) avtotransport vositasini xavfli yuklarni tashishga qo\'yish to\'g\'risidagi guvohnoma; \n'
                              f'v) alohida xavfli yuklar uchun qo\'shimcha ravishda yukni jo\'natuvchi (yukni oluvchi) tomonidan taqdim etilgan xavfli yukni tashishga maxsus yo\'riqnoma;\n'
                              f'g) O\'zbekiston Respublikasi Sanoat xavfsizligi davlat qo\'mitasining xavfli yuklarni tashish uchun sig\'im (konteynerlar, sisternalar, konteyner-sisternalar va hokazolar)ning yaroqliligi to\'g\'risidagi xulosasi; \b'
                              f'd) avtotransport haydovchisi xavfli yuklarni tashishga qo\'yilishi to\'g\'risidagi guvohnoma; \n'
                              f'Mazkur hujjatlar asosida xalqaro yo\'nalishlarda xavfli yuklarni tashish O\'zbekiston Respublikasi  IIV JXD YHXX bilan mahalliy yo\'nalishlarda Qoraqalpog\'iston Respublikasi Ichki ishlar vazirligi, Toshkent shahri va Toshkent viloyati ichki ishlar bosh boshqarmalari, viloyatlar ichki ishlar boshqarmalarining Jamoat xavfsizligi xizmati Yo\'l harakati xavfsizligi boshqarmalari bilan yo\'nalish sxemalari kelishiladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='22')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'9-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022 yil 12 apreldagi 172-son qarorining 78-bandida “Aholi punktlarida transport vositalarining tezligini soatiga 70 kilometrdan, tegishli yo\'l belgilari o\'rnatilgan maktab va maktabgacha taʼlim tashkilotlariga yetmasdan va o\'tib ketib 300 metrdan kam masofada soatiga 30 kilometrdan, turar joy dahalari va yondosh hududlarda (uy-joy binolari orasidagi yer uchastkasida) esa soatiga 20 kilometrdan oshirmasdan harakatlanishga ruxsat etiladi. Nukus va Toshkent shaharlarida, viloyatlar va tumanlarning markazlarida, shuningdek shaharlar hududlarida transport vositalarining tezligini soatiga 60 kilometrdan oshirmasdan harakatlanishga ruxsat etiladi.”, 80-bandi 5-xatboshida “Qoraqalpog\'iston Respublikasi Vazirlar Kengashi, Toshkent shahar va viloyatlar hokimliklari DYHXX bilan kelishilgan holda, yo\'l sharoitlari yuqori va kichik tezlikda xavfsiz harakatlanishni taʼminlaydigan hollarda, yo\'llarning ayrim qismlari yoki harakatlanish tasmalarida harakatlanish tezligini oshirishga yoki kamaytirishga (tegishli yo\'l belgilari o\'rnatib) ruxsat beradi.”-deb belgilab berilgan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='23')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'10-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2011 yil 26 dekabrdagi 342-son qaroriga 2-ilova «Katta hajmli va og\'ir vaznli yuklarni avtomobil transportida tashishda harakat xavfsizligini taʼminlash qoidalari»ning 9-bandi asosida “Yuk tashuvchi yoki yuk jo\'natuvchi jismoniy yoki yuridik shaxs (yoki ularning vakillari) maxsus ruxsatnoma va yo\'nalish chizmasini olish uchun yo\'lga egalik qiluvchi yuridik shaxslarga tashuvni amalga oshirishdan oldin transport vositasining rusumi, turi, davlat raqami belgilari va yukning o\'lchamlari, haydovchi va yuk tashishga masʼul bo\'lgan xodimlarning ismi, familiyasi, otasining ismi ko\'rsatilgan maʼlumotlarni my.gov.uz portali orqali murojaat qoldiradi. “Amaldagi meʼyoriy hujjatlardagi talablarga muvofiq yo\'lga egalik qiluvchi yuridik shaxslar tomonidan yuk tashishga maxsus ruxsatnoma va harakatlanish yo\'nalishi aniq belgilangan yo\'nalish chizmasi beriladi. \n'
                              f'Mazkur hujjatlar asosida xalqaro yo\'nalishlarda katta va og\'ir vaznli yuklarni tashish O\'zbekiston Respublikasi  IIV JXD YHXX tomonidan  mahalliy yo\'nalishlarda Qoraqalpog\'iston Respublikasi Ichki ishlar vazirligi, Toshkent shahri va Toshkent viloyati ichki ishlar bosh boshqarmalari, viloyatlar ichki ishlar boshqarmalarining Jamoat xavfsizligi xizmati Yo\'l harakati xavfsizligi boshqarmalari tomonidan yo\'nalish sxemalari kelishiladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



# Yo`l infratuzilmasi end




# Qidruv start



@dp.callback_query_handler(text='qidiruv')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Transport vositalariga nisbatan qidiruv eʼlon qilishga oid savollar. \n'
                              f'Savol: Transport vositalariga qanday hollarda qidiruv eʼlon qilinadi. \n', reply_markup=btn7)




@dp.callback_query_handler(text='24')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'1-savolga javob: Transport vositasini boshqargan haydovchi tomonidan qoidabuzarlik sodir etilgan holati YPX xodimi tomonidan aniqlanganda, maʼmuriy javobgarlik to\'g\'risidagi kodeksning tegishli moddalariga asosan bayonnoma rasmiylashtirilib avtomashina jarima maydoniga joylashtiriladi, boshqa holatlarda O\'zbekiston Respublikasi amaldagi qonunchiligi talablari asosida transport vositalariga nisbatan qidiruv eʼlon qilish, ushlash va jarima maydoniga joylashtirish vakolatli organlarining alohida topshiriqlari hamda sud idoralarining qaror, ajrim, hukmlari asosida amalga oshiriladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


# Qidruv end



# Jarimalar start

@dp.callback_query_handler(text='jarimalar')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Transport vositalariga nisbatan belgilanadigan jarimalarga oid savollarga javoblar. \n'
                              f'1. Savol: Transport vositamda tezlikni meʼyoridan oshirgan holda harakatlanganligim uchun menga 1.650.000 so\'m miqdordagi jarima keldi, biroq jarimani to\'lashga imkonim yo\'q 4 nafar voyaga yetmagan farzandim bor, Sizdan jarima miqdorini kamaytirib berishda amaliy yordam berishingizni so\'rayman. \n'
                              f'2. Savol: Chiqarilgan jarima qarori xususida shikoyat berish muddati qanday? \n'
                              f'3. Savol: Men transport  vositamni notarial idora orqali oldi-sotdi qilayotgan vaqtimda, transport vositamda qarzdorlik borligini bildim, lekin bunga qadar menga pochta orqali yashash manzilimga hech qanday jarima qarori kelmagan, agarda men jarima qarorini olganimda jarima imtiyozli to\'lov davrida to\'lab yuborgan bo\'lar edim, ushbu holatda jarima qarori yuzasidan imtiyozli davr muddati qayta tiklanadimi?   \n'
                              f'4. Savol: Men otamga tegishli transport vositasida tezlikni meʼyoridan oshirgan holda harakatlanganligim uchun maxsus avtomatlashtirilgan foto va video qayd etish moslamalari orqali  otamning nomiga jarima kelgan. Ushbu jarimani qanday qilib meni nomimga qayta rasmiylashtirish mumkin? \n'
                              f'5. Savol: Men chorrahada svetoforning qizil ishorasiga bo\'ysungan holda to\'xtab turgan vaqtimda, ortimdan  maxsus xizmat avtomashinasi (tez tibbiy yordam transport vositasi) yo\'l berishimni talab qildi, men transport vositasiga yo\'l berish maqsadida sidirg\'a chiziqni bosib o\'ng tomonga harakatlanishga majbur bo\'ldim, ushbu holatda menga jarima kelsa men jarimani to\'lashdan ozod etilishim mumkinmi? \n', reply_markup=btn8)

@dp.callback_query_handler(text='25')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'1-savolga javob: O\'zbekiston Respublikasi MJtKning 321-moddasi 1-qismi 4 bandida jazo chorasini kuchaytirmagan holda uni maʼmuriy huquqbuzarlik uchun javobgarlik to\'g\'risidagi normativ hujjatda nazarda tutilgan doirada o\'zgartirish sud organlarining vakolat doirasiga kirishligi sababli jarima miqdorini kamaytirish yuzasidan hududiy Jinoyat ishlari bo\'yicha sudlarga murojaat etishingiz tavsiya etiladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='26')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'2-savolga javob: Chiqarilgan qaror xususida shikoyat berish tartibi O\'zbekiston Respublikasi MJtKning 316-moddasida ko\'rsatilgan bo\'lib, unda “Maʼmuriy huquqbuzarlik to\'g\'risidagi ish yuzasidan chiqarilgan qaror xususida shu qarorning nusxasi olingan kundan eʼtiboran o\'n kun ichida shikoyat berilishi mumkin, bundan sud qarori mustasno. Mazkur muddat uzrli sabablar bilan o\'tkazilib yuborilgan taqdirda, bu muddat shikoyatni ko\'rib chiqishga vakolatli organ (mansabdor shaxs) tomonidan qayta tiklanishi mumkin” deb ko\'rsatib o\'tilgan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='27')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'3-savolga javob: Hurmatli fuqaro sizni bu mavzuda berayotgan savolingiz o\'rinli va dolzarb, sizga agarda jarima qarori o\'z vaqtida pochta orqali yetkazilmagan bo\'lsa, yashash manzilingiz bo\'yicha hududiy pochta tarmog\'iga murojaat qilib, nima sababdan jarimani yetkazib berilmaganligi yuzasidan maʼlumot olish lozim bo\'ladi misol uchun: uyingizda hech kim bo\'lmaganligi, siz ushbu manzildan boshqa hududga ko\'chib o\'tganligingiz yoki shunga o\'xshash boshqa holatlar bo\'yicha maʼlumotnoma taqdim qilingandan so\'ng, ushbu maʼlumotnoma bilan yashash manzilingiz bo\'yicha O\'zbekiston Respublikasi MJtKning 315-moddasida “Maʼmuriy huquqbuzarlik to\'g\'risidagi ish yuzasidan qaror ustidan yuqori turuvchi organga (mansabdor shaxsga) yoki jinoyat ishlari bo\'yicha tuman (shahar) sudiga, jinoyat ishlari bo\'yicha tuman (shahar) sudining qarori ustidan esa apellyatsiya instansiyasi sudiga shikoyat berilishi mumkin. Iqtisodiy sudning qarori ustidan O\'zbekiston Respublikasining Iqtisodiy protsessual kodeksida belgilangan tartibda, fuqarolik ishlari bo\'yicha sudning qarori ustidan esa O\'zbekiston Respublikasining Fuqarolik protsessual kodeksida belgilangan tartibda shikoyat berilishi mumkin.” ko\'rsatib o\'tilgan talablardan kelib chiqib, Jinoyat ishlari bo\'yicha sudlarga murojaat qilishingiz mumkin,shuningdek MJtKning 3091-moddasida “Jarima solish to\'g\'risidagi qarorning ko\'chirma nusxasi maxsus avtomatlashtirilgan foto va video qayd etish texnika vositalari qo\'llanilgan holda olingan materiallar ilova qilinib, elektron hujjatni qog\'ozdagi hujjatga aylantirish yo\'li bilan tayyorlanadi hamda mazkur qaror chiqarilgan kundan eʼtiboran uch kun ichida buyurtma pochta jo\'natmasi tarzida huquqbuzarga yuboriladi” deb ko\'rsatib o\'tilgan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='28')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'4-savolga javob: Agarda siz (o\'zingiz tegishli bo\'lmagan )  transport vositasini boshqarib qoidabuzarlik sodir etgan bo\'lsangiz, O\'zbekiston Respublikasi MJtKning 315-moddasi tartibida hududiy YHXBga murojaat qilishingiz mumkin, agarda shikoyat qilish muddati uzrli sabablarga ko\ra o\'tib ketgan bo\'lsa, yashash manzilingiz bo\'yicha Jinoyat ishlari bo\'yicha sudlarga murojaat qilib, shikoyat qilish muddati tiklanishi yoki murojaat qilgan sud idorasi orqali qarorni qayta qaratish mumkin.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)
@dp.callback_query_handler(text='29')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'5-savolga javob: O\'zbekiston Respublikasi MJtKning 171-moddasining 6-qismida  “Tezkor va maxsus xizmatlarning ko\'k yoki qizil yoxud ko\'k va qizil rangli yaltiroq mayoqchani yoqqan holda hamda maxsus tovushli signallar bilan yaqinlashib kelayotgan transport vositalariga ularning to\'siqsiz o\'tib ketishi uchun yo\'l bergan transport vositalari haydovchilari tomonidan sodir etilgan maʼmuriy huquqbuzarliklar foto va video qayd etishning maxsus avtomatlashtirilgan texnik vositalari orqali qayd etilgan taqdirda, haydovchilarning maʼmuriy huquqbuzarligi oxirgi zarurat holatlarda sodir etilgan deb topiladi va maʼmuriy ish ushbu Kodeksning 271-moddasiga muvofiq tugatiladi” deb ko\'rsatib o\'tilganligi sababli mazkur holatda jarima belgilangan tartibda bekor qilinadi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


# Jarimalar end



# Ypx Hodimi start
@dp.callback_query_handler(text='ypxhodimi')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Yo\' harakati xavfsizligi xizmati inspektori bilan bo\'ladigan xolatlarga oid savollarga javoblar. \n'
                              f'1. Savol: Transport vositamni YPX inspektori o\'zi boshqarib jarima maydoniga olib borishi mumkinmi ? \n'
                              f'2. Savol: Transport vositalarining yorituvchi chiroqlariga, yaʼni faralariga “LED” lampochkalar o\'rnatgan bo\'lsa YPX xodimi maʼmuriy bayonnoma rasmiylashtirishga haqqi bormi ?\n'
                              f'3. Savol: YPX xodimi haydovchiga kuch ishlatib avtomashinasiga mindirishi mumkinmi? \n'
                              f'4. Savol: YPX xodimini bodi-kamerasi bo\'lmasa to\'xtatishga haqqi bormi? \n'
                              f'5. Savol: YPX xodimiga to\'xtamagan haydovchilarni quvishga haqqi bormi? \n'
                              f'6. Saovl: YPX xodimi haydovchilarni qaysi hollarda to\'xtatishi mumkin? \n'
                              f'7. Savol: Haydovchining ID-kartasi yoki biometrik pasportini taqdim etganida, uning hujjatlari YPX inspektorining planshetida ko\'rinmasa bayonnoma tuzishga haqqi bormi?\n'
                              f'8. Savol: Haydovchi mast holda bo\'a turib, tibbiy tekshiruvdan yoki alkotesterdan o\'tishdan bosh tortgan taqdirda YPX xodimi unga bayonnoma tuzishi mumkinmi? \n', reply_markup=btn9)

@dp.callback_query_handler(text='30')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'1-savolga javob: O\'zbekiston Respublikasining 2016-yil 16-sentyabrdagi “Ichki ishlar organlari to\'g\'risida”gi O\'RQ-407-son Qonunning 3-bob (Ichki ishlar organlarining majburiyatlari va huquqlari), 17-moddasi, 25-26-xatboshilari (zarur bo\'lgan hollarda, transport vositalarini to\'xtatish hamda uni boshqarish va undan foydalanish huquqini beruvchi hujjatlarni, transport vositasiga, shuningdek tashilayotgan yuklarga oid hujjatlarni tekshirish, haydovchi yoki yukni kuzatib borayotgan shaxs bilan birgalikda transport vositasini va yuklarni tashqi ko\'zdan kechirish; qonun hujjatlarida nazarda tutilgan hollarda va tartibda transport vositalarini va shaxslarni ushlashni, ko\'rikdan o\'tkazishni amalga oshirish, shaxslarni transport vositasini boshqarishdan chetlashtirish, transport vositasini boshqarish huquqini beruvchi hujjatlarni olib qo\'yish, shuningdek transport vositalarini saqlab turiladigan joyga qo\'yish uchun olib borish;)- huquqiga ega ekanligi ko\'rsatib o\'tilgan. Shuningdek, amaldagi “Yo\'l harakati qoidalari”ning 7-bandi talablari asosida transport vositasini boshqarishi mumkinligini maʼlum qilamiz.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='31')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'2-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022 yil 12 apreldagi 172-son qaroriga 3-ilova, 3.4-bandi (Yoritish asboblarida nur sochuvchisi bo\'lmasa yoxud tegishli yorug\'lik asboblari turiga mos bo\'lmagan nur sochuvchi va ishlab chiqaruvchi korxona tomonidan ko\'zda tutilmagan lampalardan foydalanilgan bo\'lsa)da hamda O\'zbekiston Respublikasi MJtKning 127-moddasi (Transport vositalarining tovush chiqaruvchi, yorituvchi va boshqa qurilmalaridan foydalanish, ularni o\'rnatish qoidalarini buzish)da nazarda tutilgan huquqbuzarlik yuzasidan haydovchilarga nisbatan belgilangan tartibda maʼmuriy choralar ko\'riladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='32')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'3-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining  2018 yil 1 dekabrdagi 975-son qarorining 12-bandi “ YPX xodimi o\'z xizmat vazifalarini bajarishda qonun hujjatlarida nazarda tutilgan asoslar mavjud bo‘lganda, jismoniy kuch ishlatish, maxsus vositalarni va o\'qotar qurolni qo\'llash huquqlarga ega” talablari asosida haydovchi va fuqarolarga kuch ishlatishi va maxsus vositalardan foydalanishi mumkin.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='33')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'4-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 1 dekabrdagi 975-son qarorining 14-bandida “YPX xodimi o\'z xizmat vazifalarini bajarishda mobil videokameradan foydalangan holda oshkora olib borishi” talablariga asosan xizmatini bodi-kamera orqali olib borishi kerak.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='34')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'5-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 1 dekabrdagi 975-son qarorining 2-bandi “Maʼmuriy huquqbuzarlik sodir etgan shaxslar o\'z harakatlari bilan boshqa harakat qatnashchilari hayoti (sog\'lig\'i)ga xavf solayotgan transport vositasi haydovchisi YPX xodimining to\'xtash to\'g\'risidagi qonuniy talabini bajarmaganda to\'xtatish maqsadida orqasidan borish” talablari asosida YPX xodimi transport vositalarini orqasidan kuzatib borishi mumkin.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='35')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'6-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 1 dekabrdagi 975-son qarorining 6-bandi “Haydovchi tomonidan yo\'l harakati qoidalarining buzilishi vizual kuzatuvda aniqlanganda yoki maxsus moslama yordamida qayd qilinganda” talablari asosida to\'xtatishi mumkin.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='36')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'7-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022 yil 12 apreldagi 172-son “Yo\'l harakati qoidalari to\'g\'risida”gi qarorning 7-bandi (O\'zbekiston Respublikasi ichki ishlar organlari yoxud konsullik muassasalari tomonidan berilgan biometrik pasporti yoki identifikatsiyalovchi ID-kartasi yonida bo\'gan haydovchilarning, haydovchilik guvohnomasi, transport vositasini ro\'yxatdan o\'tkazganlik to\'g\'risidagi guvohnomasi,transport vositasiga egalik qilish, egasi yo\'qligida undan foydalanish yoki uni tasarruf etish huquqini tasdiqlovchi hujjatlari, avtotransport vositasi oynalarining tusini o\'zgartirishga (qoraytirishga) ruxsatnomasi, transport vositasining texnik ko\'rikdan o\'tganligi to\'g\'risidagi maʼlumotni, transport vositalari egalarining fuqarolik javobgarligini majburiy sug\'urta qilish bo\'yicha sug‘urta polisi planshet orqali tekshiriladi (planshetda aniqlash imkoni bo\'lmagan hamda favqulodda holatlar bundan mustasno)da DYHXX xodimlari tomonidan planshet orqali tekshiriladi deb belgilangan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='37')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'8-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining  2018 yil 1 dekabrdagi 975-son qarorining 14-bandi “Haydovchini mast holda deb hisoblashga asoslar mavjud bo\'lgan taqdirda, uni transport vositasini boshqarishdan chetlatish, mastlik holatini aniqlash uchun belgilangan tartibda tekshiruvdan o\'tkazish, haydovchi mastligi yoki mast emasligini aniqlash uchun tekshiruv o\'tkazilishidan bo\'yin tovlagan taqdirda MJtKning 136-moddasida nazarda tutilgan huquqbuzarlik uchun maʼmuriy bayonnoma rasmiylashtirish” talablari asosida mast holda transport vositasini boshqargan haydovchi tibbiy tekshiruvdan o\'tishdan bosh tortgan taqdirda MJtKning 136-moddasi tartibida maʼmuriy bayonnoma rasmiylashtiradi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='rus')
async def Rus(rus:types.CallbackQuery):
    await rus.answer(cache_time=60)
    await rus.message.answer('Уважаемый гражданин, выбрав интересующий вас вопрос, вы можете получить на него юридический ответ. Нажмите кнопку «Начинать», чтобы получить ответы на свои вопросы', reply_markup=btn12)

@dp.callback_query_handler(text='нач')
async def Rus1(rus1:types.CallbackQuery):
    await rus1.answer(cache_time=60)
    await rus1.message.answer(f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)


@dp.callback_query_handler(text='тех')
async def Rus2(rus2:types.CallbackQuery):
    await rus2.answer(cache_time=60)
    await rus2.message.answer(f'Ознакомьтесь с вопросами. Вы можете получить ответ, выбрав интересующий вас номер вопроса.')
    await rus2.message.answer(f'Технический осмотр автомобилей.\n'
                              f'1. Вопрос: В какой период проводится технический осмотр транспортных средств, находящихся в собственности физических лиц? \n'
                              f'2. Вопрос: Как часто нужно проводить технический осмотр автомобиля, находящегося в собственности физических лиц? \n'
                              f'3. Вопрос: Как часто мне нужно проверять газовый баллон с метаном, установленный в моем автомобиле? \n',  reply_markup=btn14)

@dp.callback_query_handler(text='38')
async def Rus3(rus3:types.CallbackQuery):
    await rus3.answer(cache_time=60)
    await rus3.message.answer(f'Ответ на вопрос 1: В соответствии с пунктом 6 Положения о порядке проведения обязательного технического осмотра транспортных средств, утвержденного постановлением Кабинета Министров Республики Узбекистан от 9 марта 2021 года № 125, технический осмотр иных транспортных средств, принадлежащих физическим и юридическим лицам, должен проводиться с 1 января по 31 декабря.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='39')
async def Rus4(rus4:types.CallbackQuery):
    await rus4.answer(cache_time=60)
    await rus4.message.answer(f'Ответ на вопрос 2: Частота технического осмотра автомобиля указана в пункте 5 положения о порядке проведения обязательного технического осмотра транспортных средств, утвержденного постановлением Кабинета Министров Республики Узбекистан от 9 марта 2021 г. № 125:\n'
                              f'Согласно подпункту "б" транспортные средства категории М1, находящихся в собственности физических лиц, от одиннадцати до четырнадцати лет выпуска (в том числе четырнадцатый год) транспортных средств (за исключением транспортных средств, указанных в подпункте "а" настоящего пункта) проходят технический осмотр один раз в два года;\n'
                              f'Согласно подпункту “в”, транспортные средства с неопределенной датой выпуска (за исключением транспортных средств, указанных в подпункте «а» настоящего пункта), а также транспортные средства категории М1, принадлежащие физическим лицам, выпуск которых составляет пятнадцать и более лет (за исключением транспортных средств, указанных в подпункте «а» настоящего пункта) проходят технический осмотр один раз в год.\n'
                              f'Транспортные средства категории М1, принадлежащие физическим лицам, до десяти лет выпуска (включая десятый год) (за исключением транспортных средств, указанных в подпункте "а" настоящего пункта), подлежат техническому осмотру в добровольном порядке.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)


@dp.callback_query_handler(text='40')
async def Rus5(rus5:types.CallbackQuery):
    await rus5.answer(cache_time=60)
    await rus5.message.answer(f'Ответ на вопрос 3: Баллоны со сжатым природным газом (метаном), устанавливаемые в автомобилях в соответствии с пунктом 77 общего технического регламента о безопасности транспортных средств, работающих на компримированном природном газе, сжиженном нефтяном газе или смеси дизельного и газообразного топлив, утвержденного Кабинетом Министров решением № 326 от 15 ноября 2015 г. техническое испытание проводится один раз в год.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='права')
async def Rus6(rus6:types.CallbackQuery):
    await rus6.answer(cache_time=60)
    await rus6.message.answer(f'Ознакомьтесь с вопросами. Вы можете получить ответ, выбрав интересующий вас номер вопроса\n'
                              f'Вопросы по водительскому удостоверению.\n'
                               f'1. Вопрос:Какой срок замены водительских удостоверений старого образца? \n'
                               f'2. Вопрос: Даёт ли право на вождение автомобиля водительское удостоверение, полученное гражданином Республики Узбекистан за границей? \n'
                               f'3. Вопрос: Какой порядок замены водительских удостоверений старого образца? Оплачивается ли штраф при подаче заявления о замене водительских прав, не замененных в установленный срок?\n'
                               f'4. Вопрос: Каков порядок получения водительских удостоверений лицами, лишенными права управления транспортным средством?\n'
                               f'5. Вопрос:В каком порядке осуществляется восстановление утраченных водительских удостоверений? \n', reply_markup=btn15)



@dp.callback_query_handler(text='41')
async def Rus7(rus7:types.CallbackQuery):
    await rus7.answer(cache_time=60)
    await rus7.message.answer(f' Ответ на вопрос 1: Согласно Постановлению №178 Кабинета Министров Республики Узбекистан от 12 апреля 2022 года, установлены следующие сроки замены  водительских удостоверений старого образца,В частности: \n'
                               f'Выданные в период до 2010 года — до 31 марта 2023 года; \n'
                               f'Выданные в период с 2010 по 2013 г.г. — до 30 июня 2023 года; \n'
                               f'Выданные в период с 2013 по 2015 г.г. — до 30 сентября 2023 года;\n'
                               f'Выданные после 2015 года — до 31 декабря 2023 года; '
                              f'Будет осуществляться в обязательном порядке; \n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)


@dp.callback_query_handler(text='42')
async def Rus8(rus8:types.CallbackQuery):
    await rus8.answer(cache_time=60)
    await rus8.message.answer( f'Ответ на вопрос 2: Согласно требованиям Постановления Кабинета Министров Республики Узбекистан № 408 от 31 мая 2018 года (Приложение 2, пункт 74), международные водительские удостоверения считаются действительны для управления автотранспортными средствами на территории Республики Узбекистан. \n'
                               f'Для граждан Республики Узбекистан управление автомототранспортными средствами на территории страны разрешается только на основании Национального водительского удостоверения Республики Узбекистан. \n'
                               f'Также (Приложение 2, пункт 76) осуществляется замена водительских удостоверений, полученных другими иностранными гражданами и лицами без гражданства, а также гражданами Республики Узбекистан в зарубежных странах на Национальные водительские удостоверения Республики Узбекистан после предварительной проверки Министерством иностранных дел через СБДД, с результатами о прохождении медицинского осмотра, теоретических и практических экзаменов. \n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='43')
async def Rus9(rus9:types.CallbackQuery):
    await rus9.answer(cache_time=60)
    await rus9.message.answer( f'Ответ на вопрос 3: При замене Национальных водительских удостоверений старого образца на новые необходимо предоставить гражданский паспорт (или другой документ, удостоверяющий личность) и водительское удостоверение старого образца, а также предупредительный талон в "Центр государственных услуг" или территориальную ГСБДД и произвести оплату в размере 70% от установленного БРВ (231 тысяча сумов). \n'
                               f'В целях создания благоприятных условий для граждан центром госуслуг внедрена и в настоящее время полностью запущена практика информационной программы по электронной подаче заявления и доставке готового документа по адресу проживания граждан, данная практика осуществляется через региональные центры госуслуг, то есть за дополнительную плату сотрудник регионального ЦГУ доставит готовые водительские права нового образца прямо к месту жительсва их владельца и вручит только обладателю.  \n'
                               f'Если водитель управляет автомобилем с водительским удостоверением старого образца, которое он не заменил в указанные сроки, то по статье 135 КоАП Республики Узбекистан будут основания для привлечения к административной ответственности, но штраф за замену просроченного водительского удостоверения не предусмотрен.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='44')
async def Rus10(rus10:types.CallbackQuery):
    await rus10.answer(cache_time=60)
    await rus10.message.answer(f' Ответ на вопрос 4: Постановлением № 408  Кабинета Министров Республики Узбекистан от 31 мая 2018 года установлено, что лица, лишенные права управления транспортными средствами за вождение в нетрезвом виде, для повторного получения национального водительского удостоверения, независимо от срока лишения, после окончания срока административного взыскания должны проходить обязательные медицинские осмотры, проходить обучение на квалификационных курсах и сдавать теоретические и практические экзамены. \n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)


@dp.callback_query_handler(text='45')
async def Rus11(rus11:types.CallbackQuery):
    await rus11.answer(cache_time=60)
    await rus11.message.answer(f'Ответ на вопрос 5:В соответствии с Постановлением № 408 Кабинета Министров Республики Узбекистан от 31 мая 2018 года, восстановление утраченных водительских удостоверений будет осуществляться на основании заявления водителя, экзаменационного листа, медицинской справки о пригодности к управлению транспортными средствами соответствующих категорий, а при отсутствии экзаменационного листа, необходимо иметь при себе ходатайство РиЭО регионального УБДД, а также квитанцию об оплате государственной пошлины в размере 1 БРВ.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)








@dp.callback_query_handler(text='техпаспотр')
async def Rus12(rus12:types.CallbackQuery):
    await rus12.answer(cache_time=60)
    await rus12.message.answer(f'Ознакомьтесь с вопросами. Вы можете получить ответ, выбрав интересующий вас номер вопроса\n')
    await rus12.message.answer(f'Вопросы о регистрации автотранспортных средств. \n'
                              f'1. Вопрос: Имею постоянное место жительства в другом регионе. Однако, живу и работаю в городе Ташкенте и приобрёл новый автомобиль. Могу ли я приобрести государственные номерные знаки в УБДД ГУВД г.Ташкента?\n'
                              f'2. Вопрос: Какие виды транспортных средств регистрируются в органах ГСБДД? \n',  reply_markup=btn16)



@dp.callback_query_handler(text='46')
async def Rus13(rus13:types.CallbackQuery):
    await rus13.answer(cache_time=60)
    await rus13.message.answer( f'Ответ на вопрос 1:Согласно Постановлению №271 Кабинета Министров Республики Узбекистан от 4 мая 2021 года можете, зарегистрировать автомототранспортное средство в любом регионе страны, независимо от места постоянной прописки. При этом индекс государственных номерных знаков будет совпадать с тем регионом, где владелец автомототранспортного средства прописан на постоянной основе.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)





@dp.callback_query_handler(text='47')
async def Rus14(rus14:types.CallbackQuery):
    await rus14.answer(cache_time=60)
    await rus14.message.answer(f'Ответ на вопрос 2:Автомототранспортные средства с двигателем, объёмом 50 см3 и более, а также с конструктивной скоростью 50 км/ч и более, Электромобили с электродвигателями, мощностью 4 кВт и более, а также со скоростью 40 км/ч и более (электромотоциклы, электроскутеры и другие), кроме того прицепы и полуприцепы\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)




@dp.callback_query_handler(text='кайта')
async def Rus15(rus15:types.CallbackQuery):
    await rus15.answer(cache_time=60)
    await rus15.message.answer(f'Ознакомьтесь с вопросами. Вы можете получить ответ, выбрав интересующий вас номер вопроса\n')
    await rus15.message.answer(f'Вопросы по дооснащению автомобилей. \n'
                              f'1. Вопрос: В каком количестве базовой расчётной величины нужно будет внести оплату за тонировку стёкол легковых автотранспортных средств? \n'
                              f'2. Вопрос:Через сколько лет после выпуска автотранспортных средств разрешается их переоборудование? \n'
                              f'3. Вопрос: Объясните порядок переоборудования автотранспортного средства?\n', reply_markup=btn17)



@dp.callback_query_handler(text='48')
async def Rus16(rus16:types.CallbackQuery):
    await rus16.answer(cache_time=60)
    await rus16.message.answer( f'Ответ на вопрос 1:Согласно Постановлению №547 Кабинета Министров Республики Узбекистан от 1 сентября 2017 года,Тонировка заднего стекла, а также задних боковых стёкол легковых транспортных средств может осуществляться без соответствующего разрешения с неограниченной степенью светопроницаемости, в соответствии с утвержденным государственным стандартом светопропускания - изменение (затемнение) тона передних боковых стекол не менее чем на 30 процентов.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='49')
async def Rus17(rus17:types.CallbackQuery):
    await rus17.answer(cache_time=60)
    await rus17.message.answer( f'Ответ на вопрос 2: Согласно требованиям Постановления Кабинета Министров Республики Узбекистан № 758 от 30 ноября 2020 года, автомототранспортные средства, имеющие срок эксплуатации не более 20 лет, будут допущены к переоборудованию в установленном порядке. \n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)




@dp.callback_query_handler(text='50')
async def Rus18(rus18:types.CallbackQuery):
    await rus18.answer(cache_time=60)
    await rus18.message.answer( f'Ответ на вопрос 3: В соответствии с Постановлением № 86 Кабинета Министров Республики Узбекистан от 22 февраля 2022 года (приложение 26) заявление на получение документа разрешительного характера физическими и юридическими лицами подаётся через информационную систему "license.gov.uz ", установлено, через единый интерактивный портал государственных услуг Республики Узбекистан или центры госуслуг с взиманием государственной пошлины (в размере 30% от суммы БРВ).  Исходя из требований решения, вы можете получить ответное письмо в электронном виде (о разрешении или отказе) в течение 15 рабочих дней. Также этим решением установлено, что не допускается переоборудование транспортных средств имеющие срок эксплуатации более 20 лет (за исключением случаев замены кузова или двигателя такого автомобиля).\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)





@dp.callback_query_handler(text='дорожная')
async def Rus19(rus19:types.CallbackQuery):
    await rus19.answer(cache_time=60)
    await rus19.message.answer(f'Ознакомьтесь с вопросами. Вы можете получить ответ, выбрав интересующий вас номер вопроса\n')
    await rus19.message.answer(f'Ответы на вопросы по контролю за дорожной инфраструктурой. \n'
                              f'1. Вопрос: К кому я должен обратиться, чтобы установить светофор на проезжей части нашего района. Расскажите о процедуре установки светофора? \n'
                              f'2. Вопрос: К кому и куда следует обращаться по вопросам ремонта и устранения неполадок на автомобильных дорогах? \n'
                              f'3. Вопрос: Когда на дорогах и улицах устанавливают «Искусственные неровности» для замедления транспортных средств. К кому обратиться для установки «искусственной неровности»? \n'
                              f'4. Вопрос: На основании какого нормативного документа производится открытие пункта выдачи на автомагистрали? \n'
                              f'5. Вопрос: По территории нашего района проходит оживленная 6-полосная автомагистраль, по которой движутся транзитные автомобили, предназначенные для высокоскоростного движения транспортных средств. Можно ли организовать пешеходный переход на этой автомобильной дороге? \n'
                              f'6. Вопрос: На регулируемом перекрестке, зелёный сигнал пешеходного светофора переключается на красный, прежде чем пешеходы могут перейти дорогу по переходу. К кому можно обратиться, для измения режима светофоров? \n'
                              f'7. Вопрос: Можно ли проехать через перевал «Камчик» на грузовых машинах? \n'
                              f'8. Вопрос: Транспортные средства движутся на высокой скорости вдоль нашего района. Подскажите порядок установки дорожных знаков ограничивающих скорость движения автотранспорта? \n'
                              f'9. Вопрос: С кем согласовываются маршруты перевозки опасных грузов автомобильным транспортом? \n'
                              f'10. Вопрос: Какая организация выдает разрешение на перевозку крупногабаритных и тяжеловесных грузов? \n', reply_markup=btn18)




@dp.callback_query_handler(text='51')
async def Rus20(rus20:types.CallbackQuery):
    await rus20.answer(cache_time=60)
    await rus20.message.answer(f'Ответ на вопрос 1:Абзацем 3 статьи 13 Закона Республики Узбекистан “О безопасности дорожного движения” установлено, что ответственность за обеспечение соответствия состояния дорог требованиям нормативных документов в области безопасности дорожного движения лежит на тех юридических и физических лицах, в ведении которых находятся указанные участки дороги. \n'
                               f'На основании требований настоящего Закона обращение подаётся в организацию, в ведении которой находится данный учасьок дороги, а также в территориальное органы СБДД. В обращении указывается адрес и место (локация) установки светофора. Светофоры будут установлены на основании заключений ответственного персонала относительно того, соответствует ли место, где предполагается установить светофор, требованиям государственного стандарта или нет.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)




@dp.callback_query_handler(text='52')
async def Rus21(rus21:types.CallbackQuery):
    await rus21.answer(cache_time=60)
    await rus21.message.answer(f'Ответ на вопрос 2: Статья 15 Закона Республики Узбекистан “Об автомобильных дорогах” гласит, что ремонт и содержание (обслуживание) автомобильных дорог должны обеспечиваться теми юридическими и физическими лицами, в распоряжении которых имеются указанные дороги, а также статья 16 обязывает дорожные организации обеспечивать исправность автомобильных дорог, бесперебойное и безопасное прохождение по ним транспортных средств. \n'
                              f'Абзацем 3 статьи 13 Закона Республики Узбекистан “О безопасности дорожного движения” установлено, что ответственность за обеспечение соответствия состояния дорог требованиям нормативных документов в области безопасности дорожного движения лежит на тех юридических и физических лицах, в ведении которых находятся указанные участки дороги.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='53')
async def Rus22(rus22:types.CallbackQuery):
    await rus22.answer(cache_time=60)
    await rus22.message.answer(f'Ответ на вопрос 3: «Искусственные неровности» для замедления транспортных средств на дорогах и улицах устанавливают в соответствии с требованиями государственного стандарта Республики Узбекистан O’zDst 3403 "Искусственные неровности. Общие технические требования. Порядок применения". Также в действующие правила дорожного движения включен дорожный знак “Искусственная неровность дороги” на основании Постановления Кабинета Министров Республики Узбекистан №172 “Об утверждении Правил дорожного движения” от 12 апреля 2022 года.\n'
                               f'В соответствии с настоящим государственным стандартом искусственные неровности дороги устанавливаются за 10-15 метров до нерегулируемых надземных переходов, тротуаров в близи детских и молодежных образовательных учреждений, детских площадок, общественных местах отдыха, стадионах, вокзалах, магазинах и пр. Также искусственные неровности дороги устанавливаются на основании анализа причин аварийности перед объектами большого скопления пешеходов, на определенных участках дорог (в особенности в начале опасных зон). \n'
                               f'Пункт 2 статьи 10 Закона Республики Узбекистан «Об автомобильных дорогах» гласит, что «Улицы городов и других населенных пунктов являются государственной собственностью и находятся в ведении органов государственной власти на местах», статье 15 «Ремонт и содержание автомобильных дорог, юридических и физических лиц, предоставленных этими юридическими и физическими лицами, если они находятся в их распоряжении», а в статье 16 указано, что «Дорожные организации обязаны обеспечивать исправность автомобильных дорог и непрерывное и безопасное движение по ним транспортных средств. ".\n'
                               f'Пунктом 3 статьи 13 Закона Республики Узбекистан «О безопасности дорожного движения» установлено, что обязанность по обеспечению соответствия состояния автомобильных дорог требованиям нормативных документов в области безопасности дорожного движения возлагается на юридические и физические лица, которым принадлежат эти дороги.\n'
                               f'На основании этих законов и требований государственного стандарта «искусственная неровность» устанавливается организацией, владеющей дорогой (органами местного самоуправления, дорожными предприятиями), и согласовывается с территориальными органами СБДД.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='54')
async def Rus23(rus23:types.CallbackQuery):
    await rus23.answer(cache_time=60)
    await rus23.message.answer(f'Ответ на вопрос 4: На основании утвержденных государственным комитетом по архитектуре и строительству Узбекистана требований ШНК автомобильных дорог 2.05.02-07 проектируются и организуются места отвода.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)





@dp.callback_query_handler(text='55')
async def Rus24(rus24:types.CallbackQuery):
    await rus24.answer(cache_time=60)
    await rus24.message.answer(f'Ответ на вопрос 5: При организации пешеходных переходов на автомобильных дорогах I и II категорий, по которым движутся транзитные автомобили, не допускается их пересечение на одном уровне с автомобильными дорогами в соответствии с требованиями ШНК автомобильных дорог 2.05.02-07, утвержденными Государственным комитетом по архитектуре и строительству Узбекистана. В этих местах тротуары (подземные и надземные) устраиваются на разных уровнях в зависимости от интенсивности движения пешеходов.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)




@dp.callback_query_handler(text='56')
async def Rus25(rus25:types.CallbackQuery):
    await rus25.answer(cache_time=60)
    await rus25.message.answer(f'Ответ на вопрос 6:Абзацем 3 статьи 13 Закона Республики Узбекистан “О безопасности дорожного движения”установлено, что обязанность по обеспечению соответствия состояния дорог требованиям нормативных документов в области безопасности дорожного движения лежит на тех юридических и физических лицах, в ведении которых находятся указанные дороги.  \n'
                              f'На основании требований настоящего Закона обращение подаётся в организацию, в ведении которой находится данный учасьок дороги, а также в территориальное органы СБДД. В обращении указывается адрес и место (локация) установки светофора. Режим светофора дополнительно изучается ответственным персоналом и изменяется на основании сделанных выводов о соответствии или несоответствии требованиям государственного стандарта. \n\n'            
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)




@dp.callback_query_handler(text='57')
async def Rus26(rus26:types.CallbackQuery):
    await rus26.answer(cache_time=60)
    await rus26.message.answer(f'Ответ на вопрос 7:Согласно постановлению Кабинета Министров Республики Узбекистан от 6 апреля 2018 года № 268 « О мерах по дальнейшему упорядочению грузовых перевозок автомобильным транспортом через перевал «Камчик»» запрещаются перевозки грузов через перевал «Камчик» грузовыми автомобилями и автомобилями-тягачами, с момента выпуска которых прошло более 20 лет. \n\n'
                               f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)




@dp.callback_query_handler(text='58')
async def Rus27(rus27:types.CallbackQuery):
    await rus27.answer(cache_time=60)
    await rus27.message.answer(f'Ответ на вопрос 8:В населенных пунктах скорость транспортных средств не превышает 70 километров в час, до подъезда к школам и дошкольным образовательным организациям с соответствующими дорожными знаками, а после их прохождения на расстоянии менее 300 метров - от 30 километров в час и в жилых массивах и прилегающих к ним территориях (на земельном участке между жилыми домами) допускается движение со скоростью от 20 километров в час.\n'
                               f'В городах Нукусе и Ташкенте, в центрах областей и районов, а также в городах допускается скорость движения транспортных средств не более 60 километров в час. \n\n'
                               f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)





@dp.callback_query_handler(text='59')
async def Rus28(rus28:types.CallbackQuery):
    await rus28.answer(cache_time=60)
    await rus28.message.answer(f'Ответ на вопрос 9:В пункте 56 постановления Кабинета Министров Республики Узбекистан № 35 .\n'
                               f'Установлено, что для согласования маршрутов перевозки опасных грузов грузоотправитель обязан не менее чем за десять дней до начала перевозки представить в территориальное управление безопасности дорожного движения, по территории которого предполагается перевозка опасного груза, следующие документы:\n'
                               f'а) разработанное направление транспортировки по установленной форме в трех экземплярах;\n'
                               f'б) свидетельство о постановке транспортного средства на перевозку опасных грузов;\n'
                               f'в) специальная инструкция по перевозке опасного груза, дополнительно предоставляемая грузоотправителем (грузополучателем) для особо опасных грузов;\n'
                               f'г)заключение Государственного комитета Республики Узбекистан по промышленной безопасности о пригодности емкостей (контейнеров, цистерн, контейнеровозов и др.) Для перевозки опасных грузов;\n'
                               f'г) свидетельство о допуске водителя автотранспорта к перевозке опасных грузов;\n'
                               f'На основании указанных документов осуществляются перевозки опасных грузов по международным направлениям, схемы маршрутов согласовываются с СБДД ДОБ МВД Республики Узбекистан, на местных направлениях с управлением безопасности дорожного движения Министерства внутренних дел Республики Каракалпакстан, главными управлениями внутренних дел города Ташкента и Ташкентской области, службой общественной безопасности управлений внутренних дел областей. \n\n'
                               f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)





@dp.callback_query_handler(text='60')
async def Rus29(rus29:types.CallbackQuery):
    await rus29.answer(cache_time=60)
    await rus29.message.answer(f'Ответ на вопрос 10:На основании пункта 9 Приложения 2 к Постановлению Кабинета Министров Республики Узбекистан от 26 декабря 2011 года № 342 «Правила обеспечения безопасности движения при перевозках крупногабаритных и тяжеловесных грузов автомобильным транспортом» получить специальное разрешение и карту маршрутов, юридические лица, владеющие дорогой, перед осуществлением перевозки должны предоставить информацию о модели, типе, госномерах и габаритах транспортного средства, имени, фамилии, отчестве водителя а сотрудники ответственные за перевозку груза через портал my.gov.uz оставляют обращение через «Согласно требованиям действующих нормативных документов, юридическим лицам, владеющим дорогой, будет выдаваться специальное разрешение на перевозку грузов и карта маршрутов с четко определенным направлением движения. \n'
                               f'На основании этих документов перевозка крупногабаритных и тяжеловесных грузов в международных направлениях согласовывается СБДД ДОБ МВД РУз, главными управлениями внутренних дел Республики Каракалпакстан, главные управления внутренних дел города Ташкента и Ташкентской области, службы общественной безопасности областных управлений внутренних дел, управления безопасности дорожного движения Республики Узбекистан.\n\n'
                               f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)






@dp.callback_query_handler(text='поиск')
async def Rus30(rus30:types.CallbackQuery):
    await rus30.answer(cache_time=60)
    await rus30.message.answer(f'Ознакомьтесь с вопросами. Вы можете получить ответ, выбрав интересующий вас номер вопроса\n')
    await rus30.message.answer(f'Вопросы по ордерам на обыск транспортных средств. \n'
                              f'Вопрос: Транспортные средства будут подвергаться обыску в следующих случаях. \n', reply_markup=btn19)





@dp.callback_query_handler(text='61')
async def Rus30(rus30:types.CallbackQuery):
    await rus30.answer(cache_time=60)
    await rus30.message.answer(f'Ответ на вопрос 1: При совершении правонарушения водителем, управляющим транспортным средством, сотрудниками ДПС составляется протокол на основании соответствующих статей Кодекса об административной ответственности, и транспортное средство помещается в штрафную зону, в иных случаях выдаётся ордер на обыск транспортных средств на основании требований действующего законодательства Республики Узбекистан,  задержание и помещение в штрафную зону осуществляется на основании отдельных поручений компетентных органов и постановлений, постановлений и приговоров органов юстиции.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)





@dp.callback_query_handler(text='штрафы')
async def Rus31(rus31:types.CallbackQuery):
    await rus31.answer(cache_time=60)
    await rus31.message.answer(f'Ознакомьтесь с вопросами. Вы можете получить ответ, выбрав интересующий вас номер вопроса\n'
                               f'Ответы на вопросы о штрафах для транспортных средств. \n'
                              f'1. Вопрос: Получил штраф 1 650 000 сум за превышение скорости на своем транспортном средстве, но оплатить штраф не могу. У меня 4 несовершеннолетних детей. Прошу Вас помочь мне уменьшить сумму штрафа.\n'
                              f'2. Вопрос: В какой срок можно подать жалобу на вынесенное решение о штрафе? \n'
                              f'3. Вопрос: Когда я продавал свое транспортное средство через нотариальную контору, я узнал, что есть задолженность по моему транспортному средству, но до этого я не получал решения о штрафе по почте на мой адрес проживания, если бы я получил решение о штрафе, я уплатил бы штраф в течение льготного периода, в этом случае будет ли востановлен льготный период для оплаты штрафа?\n'
                              f'4. Вопрос: Могу ли я переоформить штраф на своё имя, если зафиксировано нарушение транспортным средством (под моим управлением, оформленным на отца) правил дорожного движения специальными автоматизированными средствами  фото- и видеофиксации? \n'
                              f'5. Вопрос: Могу ли я быть освобожден от уплаты штрафа за административное нарушение, вынужденно совершенное при освобождении дороги для проезда автотранспортных средств экстренных и специальных служб (машины скорой помощи)?\n', reply_markup=btn20)



@dp.callback_query_handler(text='62')
async def Rus31(rus31:types.CallbackQuery):
    await rus31.answer(cache_time=60)
    await rus31.message.answer(f'Ответ на вопрос 1: 1.	В соответствии со статьёй 321 КоАО Республики Узбекистан, части первой пункта 4 рекомендуется обращаться в областные и районные суды по уголовным делам для уменьшения размера штрафа, так как данное решение является компетенцией органов юстиции. \n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)


@dp.callback_query_handler(text='63')
async def Rus32(rus32:types.CallbackQuery):
    await rus32.answer(cache_time=60)
    await rus32.message.answer(f'Ответ на вопрос 2: Порядок подачи жалобы на вынесенное постановление определен статьей 316 Кодекса об административной ответственности Республики Узбекистан, в которой указано, что «На постановление, вынесенное по делу об административном правонарушении, жалоба может быть подана в течение десяти дней со дня получения копии настоящего решения, за исключением решения суда. В случае продления этого срока по уважительным причинам этот срок может быть восстановлен органом (должностным лицом), уполномоченным рассматривать жалобу.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='64')
async def Rus32(rus32:types.CallbackQuery):
    await rus32.answer(cache_time=60)
    await rus32.message.answer(f'Ответ на вопрос 3: Уважаемый гражданин, Ваш вопрос по данной теме уместен и актуален, если решение о штрафе не было доставлено по почте в срок, необходимо обратиться в региональную почтовую сеть по адресу Вашего проживания и получить информацию о причине, по которой штраф был не доставлено, например: никого не было дома, вы после предъявления справки о том, что вы переехали с этого адреса в другой район или других подобных обстоятельств, с этой справкой, согласно ст. 315 КоАО Республики Узбекистан, имеете право обратиться в вышестоящий орган (должностному лицу) или в районный (городской) суд по уголовным делам, а решение районного (городского) суда по уголовным делам может быть обжаловано в апелляционную инстанцию. На основании вышеперечисленных требований можно обращаться в суды по уголовным делам, а также в статье 3091 КоАО РУ «Копия постановления о наложении штрафа оформляется путем приобщения материалов, полученных с помощью специальной автоматизированной фото- и видеофиксации. оборудования и преобразования электронного документа в документ на бумажном носителе, и в течение трех дней со дня вынесения настоящего решения распоряжение будет направлено правонарушителю в виде почтового отправления.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='65')
async def Rus33(rus33:types.CallbackQuery):
    await rus33.answer(cache_time=60)
    await rus33.message.answer(f'Ответ на вопрос 4:Актуальный вопрос. Если вы совершили правонарушение, управляя транспортным средством (которое вам не принадлежит), вы можете обратиться в областной апелляционный суд в соответствии со статьей 315 КоАО РУ. Если срок обжалования истек по уважительным причинам, сообщаем, что срок обжалования может быть восстановлен или решение может быть пересмотрено путем обращения в уголовные суды по месту вашего жительства.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='66')
async def Rus33(rus33:types.CallbackQuery):
    await rus33.answer(cache_time=60)
    await rus33.message.answer(f'Ответ на вопрос 5:Благодарим Вас за вопрос, в части 6 статьи 171 КоАО РУз "Автотранспортные средства экстренных и специальных служб, включающие синий или красный или сине-красный светящийся маяк и со специальным звуковым сигналом сигналов, уступать дорогу встречным транспортным средствам для беспрепятственного проезда, если совершение административных правонарушений водителями зафиксировано с помощью специальных автоматизированных технических средств фотовидеофиксации, то административное правонарушение водителей признается совершенным в крайнем случае и административное дело будет прекращено в соответствии со статьей 271 настоящего Кодекса».\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='сотрудник')
async def Rus34(rus34:types.CallbackQuery):
    await rus34.answer(cache_time=60)
    await rus34.message.answer(f'Ознакомьтесь с вопросами. Вы можете получить ответ, выбрав интересующий вас номер вопроса')
    await rus34.message.answer(f'Частые вопросы дорожной полиции \n'
                              f'1. Вопрос: Может ли инспектор ДПС довести мой автомобиль до штрафной площадки? \n'
                              f'2. Вопрос: Вправе ли сотрудник ДПС составить административный протокол, если в осветительных приборах транспортных средств, т.е. фарах установлены "LED" лампочки?\n'
                              f'3. Вопрос: Может ли сотрудник ДПС заставить водителя сесть в служебную машину? \n'
                              f'4. Вопрос: Имеет ли право сотрудник ДПС без боди-камеры останавливать транспортные средства? \n'
                              f'5. Вопрос: Имеет ли право сотрудник ДПС преследовать водителей, которые не останавливаются по их требованию? \n'
                              f'6. Вопрос: В каких случаях сотрудник ДПС может остановливать водителей транспортных средств? \n'
                              f'7. Вопрос: Имеет ли право водитель составлять протокол, если документы водителя не видны на планшете инспектора ДПС при предъявлении удостоверения личности или биометрического паспорта?\n'
                              f'8. Вопрос: Если водитель отказывается пройти медкомиссию или алкотестер в состоянии алкогольного опьянения, может ли сотрудник ДПС составить на него протокол? \n', reply_markup=btn21)



@dp.callback_query_handler(text='67')
async def Rus34(rus34:types.CallbackQuery):
    await rus34.answer(cache_time=60)
    await rus34.message.answer(f'Ответ на вопрос 1:Глава 3 (Обязанности и права органов внутренних дел), статья 17, пункты 25-26 Закона Республики Узбекистан «Об органах внутренних дел» № O\'RQ-407 от 16 сентября 2016 года (в необходимых случаях, остановка транспортных средств и проверка документов, дающих право управления и пользования им, документов на транспортное средство, а также перевозимого груза, досмотр транспортного средства и груза совместно с водителем или лицом, сопровождающим груз, задержание транспортных средств и лиц в случаях и в порядке, предусмотренных законодательством, указывается, что он вправе осуществить передачу, отстранить лиц от управления транспортным средством, изъять документы, дающие право на управление транспортным средством, а также забрать транспортное средство к месту хранения)'
                               f'Также сообщаем, что вы можете управлять транспортным средством на основании требований пункта 7 действующих «Правил дорожного движения».\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='68')
async def Rus34(rus34:types.CallbackQuery):
    await rus34.answer(cache_time=60)
    await rus34.message.answer(f'Ответ на вопрос 2:На основании приложения 3, пункта 3.4 к Постановлению Кабинета Министров Республики Узбекистан № 172 от 12 апреля 2022 года (При отсутствии в осветительных приборах источника света или при несоответствии источника света типу освещения оборудование и осветительные приборы, не предусмотренные предприятием-изготовителем) в отношении водителя транспортного средства применяются административные меры в установленном порядке в соответствии со статьей 127 (Применение звукового -излучающих, осветительных и других устройств транспортных средств, с нарушением правил их установки) Кодекса об Административной ответственности Республики Узбекистан. \n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='69')
async def Rus35(rus35:types.CallbackQuery):
    await rus35.answer(cache_time=60)
    await rus35.message.answer(f'Ответ на вопрос 3:На основании пункта 12 Постановления Кабинет Министров Республики Узбекистан № 975 от 01.12.2018 сотрудник ДПС, при исполнении своих должностных обязанностей имеет право  применять физическую силу, применять специальные средства и огнестрельное оружие.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)


@dp.callback_query_handler(text='70')
async def Rus35(rus35:types.CallbackQuery):
    await rus35.answer(cache_time=60)
    await rus35.message.answer(f'Ответ на вопрос 4:На основании пункта 14 Постановления Кабинет Министров Республики Узбекистан № 975 от 01.12.2018 сотрудник ДПС обязан выполнять служебные задачи открыто, с использованием мобильной видеокамеры, сообщить участнику дорожного движения об использовании мобильной видеокамеры и предупредить, что в случае совершения им в дальнейшем неправомерных действий в качестве доказательства его вины может быть использована видеозапись.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='71')
async def Rus36(rus36:types.CallbackQuery):
    await rus36.answer(cache_time=60)
    await rus36.message.answer(f'Ответ на вопрос 5:На основании пункта 12 Постановления Кабинет Министров Республики Узбекистан № 975 от 01.12.2018 сотрудник ДПС имеет право преследовать или наблюдать транспортное средство; задерживать лиц, совершившие административное правонарушение, следовать за водителем транспортного средства, создающим своими действиями опасность для жизни (здоровья) других участников дорожного движения, когда он не выполняет законное требование сотрудника YPX об остановке. \n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='72')
async def Rus36(rus36:types.CallbackQuery):
    await rus36.answer(cache_time=60)
    await rus36.message.answer(f'Ответ на вопрос 6:На основании пункта 6 Постановления Кабинет Министров Республики Узбекистан № 975 от 01.12.2018 сотрудник ДПС имеет право останавливать транспортные средства по следующим основаниям:\n'
                               f'установление нарушения водителем Правил дорожного движения (далее — Правила) путем визуального наблюдения либо фиксации с помощью специальных средств;\n'
                               f'наличие данных, свидетельствующих о нахождении транспортного средства, водителя или пассажира в розыске либо причастности к совершению дорожно-транспортного происшествия или иного правонарушения;\n'
                               f'возникновение необходимости в выяснении обстоятельств совершения дорожно-транспортного происшествия, правонарушения, очевидцами которого являются водитель или пассажир;\n'
                               f'в процессе выполнения указаний уполномоченных государственных органов или должностных лиц об ограничении или запрещении движения;\n'
                               f'возникновение необходимости в использовании транспортного средства в порядке, установленном законодательными актами (за исключение транспортных средств, принадлежащих дипломатическим, консульским представительствам и иным представительствам зарубежных государств, международным организациям, а также специальных транспортных средств); \n'
                               f'в процессе проведения специальных мероприятий;\n'
                               f'для проверки документов на право пользования и управления транспортными средствами, а также документов на транспортное средство и перевозимый груз (за исключением специальных и военных грузов, а также грузов, прошедших таможенное оформление и опломбированных таможенной службой).\n'
                               f'Остановка транспортных средств сотрудником ДПС по другим основаниям запрещена. \n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)




@dp.callback_query_handler(text='73')
async def Rus37(rus37:types.CallbackQuery):
    await rus37.answer(cache_time=60)
    await rus37.message.answer(f'Ответ на вопрос 7:В пукте 7 Постановление Кабинета Министров Республики Узбекистан от 12 апреля 2022 года № 172 «О Правилах дорожного движения» говорится о проверке сотрудниками ДПС через планшетное устройство следующих документов (водительское удостоверение, свидетельство о регистрации ТС, подтверждающее право владения ТС, пользования им или распоряжения им в отсутствие собственника) документы, разрешение на изменение (затемнение) цвета стекол ТС, сведения о техническом состоянии ТС техосмотр, страховые полисы ОСАГО). В случаях, когда невозможно определить по планшету и в экстренных случаях, документы проверяются планшетными работниками СБДД с пометкой «проверено».\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



@dp.callback_query_handler(text='74')
async def Rus37(rus37:types.CallbackQuery):
    await rus37.answer(cache_time=60)
    await rus37.message.answer(f'Ответ на вопрос 8:На основании пункта 14 Постановления Кабинет Министров Республики Узбекистан № 975 от 01.12.2018 сотрудник ДПС имеет право, при наличии оснований считать водителя находящимся в состоянии опьянения, отстранить его от управления транспортным средством и провести в установленном порядке его освидетельствование, с оформлением протокола об административном правонарушении, предусмотренном статьей 136 (Уклонение водителей транспортных средств и других участников дорожного движения от прохождения освидетельствования на состояние опьянения) КоАО РУ - в случае уклонения водителя от освидетельствования для определения его состояния.\n\n'
                              f'Ниже ответы на самые часто задаваемые вопросы 👇 Получить ответы на вопросы можно, выбрав одно из направлений! Если ответ на ваш вопрос не найден, вы можете получить ответ на свой вопрос в короткие сроки, оставив заявку в разделе оставить вопрос.', reply_markup=btn13)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)







