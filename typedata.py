""" 
    Typedata merupakan materi dasar dalam mempelajari bahasa pemrograman.
    dengan mengenali type data, kita dapat mengetahui karakteristiknya.
    karakteristik seperti kelebihan, kekurangan, dan sifat data trsbt
"""

a = 10       # typedata integer (angka)
b = "oskhar" # typedata string (kata/text/karakter
c = 10.5     # typedata float (angka pecahan)
d = True     # typedata boolean (kondisi benar dan salah)

"""
    semua type data ga perlu terlalu dibuat pusing, cukup tau aja, karena nanti
    saat masuk implementasi (praktik) akan paham sendiri kegunaan dari setiap
    type data yang ada dalam bahasa pemrograman python dan bahasa lainnya

    pemahaman lebih lanjut (opsional):
        Di atas merupakan typedata dasar yang perlu dipahami, selebihnya masih ada
        typedata yang berhubungan dengan ukuran jumlah byte, tapi umumnya itu
        berlaku untuk bahasa selain python seperti bahasa c/c++ dan java

        angka:
            long    -> 8 byte
            int     -> 4 byte
            short   -> 2 byte

        angka pecahan:
            float   -> 4 byte
            double  -> 8 byte
        
        karakter/text:
            char    -> 1 byte
            string  -> (opsional, char tapi berbentuk array, ukuran data tergantung jumlah karakter)
        
        kondisi:
            boolean -> 1 byte
"""

print(a, b, c, d) # menampilkan data ke konsol