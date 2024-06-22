# data.py

restaurants = [
    {
        "id": "1",
        "name": "Warung Sate Pak Samin",
        "description": "Sate kambing yang lezat dengan bumbu kacang khas.",
        "location": "Jl. Wahid Hasyim No.1, Jombang",
        "city": "Jombang",
        "image": "warung_sate_pak_samin.jpg"
    },
    {
        "id": "2",
        "name": "Bakso President",
        "description": "Bakso urat dan bakso telor yang nikmat.",
        "location": "Jl. KH. Ahmad Dahlan No.20, Jombang",
        "city": "Jombang",
        "image": "bakso_president.jpg"
    },
    {
        "id": "3",
        "name": "Soto Dok Lamongan",
        "description": "Soto ayam dengan kuah bening khas Lamongan.",
        "location": "Jl. Basuki Rahmat No.30, Jombang",
        "city": "Jombang",
        "image": "soto_dok_lamongan.jpg"
    },
    {
        "id": "4",
        "name": "Ayam Goreng Bu Tini",
        "description": "Ayam goreng renyah dengan sambal terasi spesial.",
        "location": "Jl. Merdeka No.15, Jombang",
        "city": "Jombang",
        "image": "ayam_goreng_bu_tini.jpg"
    },
    {
        "id": "5",
        "name": "Nasi Pecel Bu Umi",
        "description": "Nasi pecel dengan bumbu kacang yang gurih dan pedas.",
        "location": "Jl. Dr. Soetomo No.10, Jombang",
        "city": "Jombang",
        "image": "nasi_pecel_bu_umi.jpg"
    },
    {
        "id": "6",
        "name": "Rujak Cingur Bu Nur",
        "description": "Rujak cingur dengan bumbu petis yang autentik.",
        "location": "Jl. KH. Wahid Hasyim No.45, Jombang",
        "city": "Jombang",
        "image": "rujak_cingur_bu_nur.jpg"
    },
    {
        "id": "7",
        "name": "Warung Nasi Tumpang",
        "description": "Nasi tumpang dengan sayur lodeh dan tempe bosok.",
        "location": "Jl. KH. Ahmad Dahlan No.12, Jombang",
        "city": "Jombang",
        "image": "warung_nasi_tumpang.jpg"
    },
    {
        "id": "8",
        "name": "Bebek Goreng Pak Slamet",
        "description": "Bebek goreng empuk dengan sambal korek yang pedas.",
        "location": "Jl. Merdeka No.25, Jombang",
        "city": "Jombang",
        "image": "bebek_goreng_pak_slamet.jpg"
    },
    {
        "id": "9",
        "name": "Mie Ayam Pak Edi",
        "description": "Mie ayam lezat dengan pangsit goreng renyah.",
        "location": "Jl. Basuki Rahmat No.40, Jombang",
        "city": "Jombang",
        "image": "mie_ayam_pak_edi.jpg"
    },
    {
        "id": "10",
        "name": "Es Degan Pak Mul",
        "description": "Es degan segar dengan gula jawa asli.",
        "location": "Jl. Wahid Hasyim No.55, Jombang",
        "city": "Jombang",
        "image": "es_degan_pak_mul.jpg"
    },
    {
        "id": "11",
        "name": "Rawon Setan Bu Endang",
        "description": "Rawon setan dengan daging empuk dan kuah kental.",
        "location": "Jl. Merdeka No.18, Jombang",
        "city": "Surabaya",
        "image": "rawon_setan_bu_endang.jpg"
    },
    {
        "id": "12",
        "name": "Lontong Balap Pak Man",
        "description": "Lontong balap dengan lentho dan sambal petis.",
        "location": "Jl. Dr. Soetomo No.25, Jombang",
        "city": "Jombang",
        "image": "lontong_balap_pak_man.jpg"
    },
    {
        "id": "13",
        "name": "Bakmi Jowo Pak Di",
        "description": "Bakmi jowo dengan rasa gurih dan nikmat.",
        "location": "Jl. Basuki Rahmat No.35, Jombang",
        "city": "Jombang",
        "image": "bakmi_jowo_pak_di.jpg"
    },
    {
        "id": "14",
        "name": "Nasi Krawu Bu Tini",
        "description": "Nasi krawu dengan daging empal dan serundeng.",
        "location": "Jl. Merdeka No.10, Jombang",
        "city": "Jombang",
        "image": "nasi_krawu_bu_tini.jpg"
    },
    {
        "id": "15",
        "name": "Sate Ayam Ponorogo",
        "description": "Sate ayam dengan bumbu kacang yang khas.",
        "location": "Jl. KH. Ahmad Dahlan No.50, Jombang",
        "city": "Ponorogo",
        "image": "sate_ayam_ponorogo.jpg"
    }
]

details = {
    "1": {
        "name": "Warung Sate Pak Samin",
        "description": "Sate kambing yang lezat dengan bumbu kacang khas.",
        "location": "Jl. Wahid Hasyim No.1, Jombang",
        "city": "Jombang",
        "image": "warung_sate_pak_samin.jpg",
        "contact": "0812-3456-7890",
        "website": "http://www.satepaksamin.com",
        "opening_hours": {
            "Monday": "10:00 AM - 10:00 PM",
            "Tuesday": "10:00 AM - 10:00 PM",
            "Wednesday": "10:00 AM - 10:00 PM",
            "Thursday": "10:00 AM - 10:00 PM",
            "Friday": "10:00 AM - 11:00 PM",
            "Saturday": "10:00 AM - 11:00 PM",
            "Sunday": "10:00 AM - 10:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r1",
                "name": "Alice",
                "review": "Sate yang sangat lezat dan empuk!",
                "photo": "review1.jpg",
                "date": "01 January 2024"
            }
        ],
        "ratings": [5, 4, 5, 5],
        "reservations": []
    },
    "2": {
        "name": "Bakso President",
        "description": "Bakso urat dan bakso telor yang nikmat.",
        "location": "Jl. KH. Ahmad Dahlan No.20, Jombang",
        "city": "Jombang",
        "image": "bakso_president.jpg",
        "contact": "0813-7654-3210",
        "website": "http://www.baksopresident.com",
        "opening_hours": {
            "Monday": "09:00 AM - 09:00 PM",
            "Tuesday": "09:00 AM - 09:00 PM",
            "Wednesday": "09:00 AM - 09:00 PM",
            "Thursday": "09:00 AM - 09:00 PM",
            "Friday": "09:00 AM - 10:00 PM",
            "Saturday": "09:00 AM - 10:00 PM",
            "Sunday": "09:00 AM - 09:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r2",
                "name": "Bob",
                "review": "Bakso terbaik yang pernah saya makan!",
                "photo": "review2.jpg",
                "date": "15 January 2024"
            }
        ],
        "ratings": [4, 5, 5],
        "reservations": []
    },
    "3": {
        "name": "Soto Dok Lamongan",
        "description": "Soto ayam dengan kuah bening khas Lamongan.",
        "location": "Jl. Basuki Rahmat No.30, Jombang",
        "city": "Jombang",
        "image": "soto_dok_lamongan.jpg",
        "contact": "0812-9876-5432",
        "website": "http://www.sotodoklamongan.com",
        "opening_hours": {
            "Monday": "08:00 AM - 08:00 PM",
            "Tuesday": "08:00 AM - 08:00 PM",
            "Wednesday": "08:00 AM - 08:00 PM",
            "Thursday": "08:00 AM - 08:00 PM",
            "Friday": "08:00 AM - 09:00 PM",
            "Saturday": "08:00 AM - 09:00 PM",
            "Sunday": "08:00 AM - 08:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r3",
                "name": "Charlie",
                "review": "Soto yang sangat segar dan lezat!",
                "photo": "review3.jpg",
                "date": "20 January 2024"
            }
        ],
        "ratings": [5, 4, 4, 5],
        "reservations": []
    },
    "4": {
        "name": "Ayam Goreng Bu Tini",
        "description": "Ayam goreng renyah dengan sambal terasi spesial.",
        "location": "Jl. Merdeka No.15, Jombang",
        "city": "Jombang",
        "image": "ayam_goreng_bu_tini.jpg",
        "contact": "0812-4567-8901",
        "website": "http://www.ayamgorengbutini.com",
        "opening_hours": {
            "Monday": "10:00 AM - 10:00 PM",
            "Tuesday": "10:00 AM - 10:00 PM",
            "Wednesday": "10:00 AM - 10:00 PM",
            "Thursday": "10:00 AM - 10:00 PM",
            "Friday": "10:00 AM - 11:00 PM",
            "Saturday": "10:00 AM - 11:00 PM",
            "Sunday": "10:00 AM - 10:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r4",
                "name": "Diana",
                "review": "Ayam gorengnya sangat renyah dan enak!",
                "photo": "review4.jpg",
                "date": "10 February 2024"
            }
        ],
        "ratings": [5, 5, 5, 4],
        "reservations": []
    },
    "5": {
        "name": "Nasi Pecel Bu Umi",
        "description": "Nasi pecel dengan bumbu kacang yang gurih dan pedas.",
        "location": "Jl. Dr. Soetomo No.10, Jombang",
        "city": "Jombang",
        "image": "nasi_pecel_bu_umi.jpg",
        "contact": "0812-6543-2109",
        "website": "http://www.nasipecelbuumi.com",
        "opening_hours": {
            "Monday": "07:00 AM - 07:00 PM",
            "Tuesday": "07:00 AM - 07:00 PM",
            "Wednesday": "07:00 AM - 07:00 PM",
            "Thursday": "07:00 AM - 07:00 PM",
            "Friday": "07:00 AM - 08:00 PM",
            "Saturday": "07:00 AM - 08:00 PM",
            "Sunday": "07:00 AM - 07:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r5",
                "name": "Edi",
                "review": "Nasi pecelnya enak banget!",
                "photo": "review5.jpg",
                "date": "15 February 2024"
            }
        ],
        "ratings": [4, 4, 5, 5],
        "reservations": []
    },
    "6": {
        "name": "Rujak Cingur Bu Nur",
        "description": "Rujak cingur dengan bumbu petis yang autentik.",
        "location": "Jl. KH. Wahid Hasyim No.45, Jombang",
        "city": "Jombang",
        "image": "rujak_cingur_bu_nur.jpg",
        "contact": "0812-7890-1234",
        "website": "http://www.rujakcingurbunur.com",
        "opening_hours": {
            "Monday": "08:00 AM - 08:00 PM",
            "Tuesday": "08:00 AM - 08:00 PM",
            "Wednesday": "08:00 AM - 08:00 PM",
            "Thursday": "08:00 AM - 08:00 PM",
            "Friday": "08:00 AM - 09:00 PM",
            "Saturday": "08:00 AM - 09:00 PM",
            "Sunday": "08:00 AM - 08:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r6",
                "name": "Fajar",
                "review": "Rujak cingurnya mantap!",
                "photo": "review6.jpg",
                "date": "20 February 2024"
            }
        ],
        "ratings": [5, 5, 4, 4],
        "reservations": []
    },
    "7": {
        "name": "Warung Nasi Tumpang",
        "description": "Nasi tumpang dengan sayur lodeh dan tempe bosok.",
        "location": "Jl. KH. Ahmad Dahlan No.12, Jombang",
        "city": "Jombang",
        "image": "warung_nasi_tumpang.jpg",
        "contact": "0812-3456-7891",
        "website": "http://www.nasitumpang.com",
        "opening_hours": {
            "Monday": "09:00 AM - 09:00 PM",
            "Tuesday": "09:00 AM - 09:00 PM",
            "Wednesday": "09:00 AM - 09:00 PM",
            "Thursday": "09:00 AM - 09:00 PM",
            "Friday": "09:00 AM - 10:00 PM",
            "Saturday": "09:00 AM - 10:00 PM",
            "Sunday": "09:00 AM - 09:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r7",
                "name": "Gilang",
                "review": "Nasi tumpangnya enak banget!",
                "photo": "review7.jpg",
                "date": "25 February 2024"
            }
        ],
        "ratings": [4, 4, 4, 5],
        "reservations": []
    },
    "8": {
        "name": "Bebek Goreng Pak Slamet",
        "description": "Bebek goreng empuk dengan sambal korek yang pedas.",
        "location": "Jl. Merdeka No.25, Jombang",
        "city": "Jombang",
        "image": "bebek_goreng_pak_slamet.jpg",
        "contact": "0812-6789-0123",
        "website": "http://www.bebekgorengpakslamet.com",
        "opening_hours": {
            "Monday": "10:00 AM - 10:00 PM",
            "Tuesday": "10:00 AM - 10:00 PM",
            "Wednesday": "10:00 AM - 10:00 PM",
            "Thursday": "10:00 AM - 10:00 PM",
            "Friday": "10:00 AM - 11:00 PM",
            "Saturday": "10:00 AM - 11:00 PM",
            "Sunday": "10:00 AM - 10:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r8",
                "name": "Hadi",
                "review": "Bebeknya empuk dan sambalnya mantap!",
                "photo": "review8.jpg",
                "date": "01 March 2024"
            }
        ],
        "ratings": [5, 4, 5, 4],
        "reservations": []
    },
    "9": {
        "name": "Mie Ayam Pak Edi",
        "description": "Mie ayam lezat dengan pangsit goreng renyah.",
        "location": "Jl. Basuki Rahmat No.40, Jombang",
        "city": "Jombang",
        "image": "mie_ayam_pak_edi.jpg",
        "contact": "0812-3456-7892",
        "website": "http://www.mieayampakedi.com",
        "opening_hours": {
            "Monday": "09:00 AM - 09:00 PM",
            "Tuesday": "09:00 AM - 09:00 PM",
            "Wednesday": "09:00 AM - 09:00 PM",
            "Thursday": "09:00 AM - 09:00 PM",
            "Friday": "09:00 AM - 10:00 PM",
            "Saturday": "09:00 AM - 10:00 PM",
            "Sunday": "09:00 AM - 09:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r9",
                "name": "Ika",
                "review": "Mie ayamnya enak banget, pangsitnya juga renyah!",
                "photo": "review9.jpg",
                "date": "05 March 2024"
            }
        ],
        "ratings": [5, 5, 4, 4],
        "reservations": []
    },
    "10": {
        "name": "Es Degan Pak Mul",
        "description": "Es degan segar dengan gula jawa asli.",
        "location": "Jl. Wahid Hasyim No.55, Jombang",
        "city": "Jombang",
        "image": "es_degan_pak_mul.jpg",
        "contact": "0812-9876-5433",
        "website": "http://www.esdeganpakmul.com",
        "opening_hours": {
            "Monday": "08:00 AM - 08:00 PM",
            "Tuesday": "08:00 AM - 08:00 PM",
            "Wednesday": "08:00 AM - 08:00 PM",
            "Thursday": "08:00 AM - 08:00 PM",
            "Friday": "08:00 AM - 09:00 PM",
            "Saturday": "08:00 AM - 09:00 PM",
            "Sunday": "08:00 AM - 08:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r10",
                "name": "Joko",
                "review": "Es degannya segar banget, pas buat cuaca panas!",
                "photo": "review10.jpg",
                "date": "10 March 2024"
            }
        ],
        "ratings": [5, 5, 4, 5],
        "reservations": []
    },
    "11": {
        "name": "Rawon Setan Bu Endang",
        "description": "Rawon setan dengan daging empuk dan kuah kental.",
        "location": "Jl. Merdeka No.18, Jombang",
        "city": "Jombang",
        "image": "rawon_setan_bu_endang.jpg",
        "contact": "0812-7654-3211",
        "website": "http://www.rawonsetanbuendang.com",
        "opening_hours": {
            "Monday": "10:00 AM - 10:00 PM",
            "Tuesday": "10:00 AM - 10:00 PM",
            "Wednesday": "10:00 AM - 10:00 PM",
            "Thursday": "10:00 AM - 10:00 PM",
            "Friday": "10:00 AM - 11:00 PM",
            "Saturday": "10:00 AM - 11:00 PM",
            "Sunday": "10:00 AM - 10:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r11",
                "name": "Kiki",
                "review": "Rawonnya enak banget, dagingnya empuk!",
                "photo": "review11.jpg",
                "date": "15 March 2024"
            }
        ],
        "ratings": [5, 4, 5, 5],
        "reservations": []
    },
    "12": {
        "name": "Lontong Balap Pak Man",
        "description": "Lontong balap dengan lentho dan sambal petis.",
        "location": "Jl. Dr. Soetomo No.25, Jombang",
        "city": "Jombang",
        "image": "lontong_balap_pak_man.jpg",
        "contact": "0812-1234-5678",
        "website": "http://www.lontongbalappakman.com",
        "opening_hours": {
            "Monday": "08:00 AM - 08:00 PM",
            "Tuesday": "08:00 AM - 08:00 PM",
            "Wednesday": "08:00 AM - 08:00 PM",
            "Thursday": "08:00 AM - 08:00 PM",
            "Friday": "08:00 AM - 09:00 PM",
            "Saturday": "08:00 AM - 09:00 PM",
            "Sunday": "08:00 AM - 08:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r12",
                "name": "Lina",
                "review": "Lontong balapnya enak, lenthonya garing!",
                "photo": "review12.jpg",
                "date": "20 March 2024"
            }
        ],
        "ratings": [4, 5, 4, 4],
        "reservations": []
    },
    "13": {
        "name": "Bakmi Jowo Pak Di",
        "description": "Bakmi jowo dengan rasa gurih dan nikmat.",
        "location": "Jl. Basuki Rahmat No.35, Jombang",
        "city": "Jombang",
        "image": "bakmi_jowo_pak_di.jpg",
        "contact": "0812-8765-4321",
        "website": "http://www.bakmijowopakdi.com",
        "opening_hours": {
            "Monday": "10:00 AM - 10:00 PM",
            "Tuesday": "10:00 AM - 10:00 PM",
            "Wednesday": "10:00 AM - 10:00 PM",
            "Thursday": "10:00 AM - 10:00 PM",
            "Friday": "10:00 AM - 11:00 PM",
            "Saturday": "10:00 AM - 11:00 PM",
            "Sunday": "10:00 AM - 10:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r13",
                "name": "Mia",
                "review": "Bakminya gurih dan nikmat, cocok buat makan malam!",
                "photo": "review13.jpg",
                "date": "25 March 2024"
            }
        ],
        "ratings": [4, 4, 5, 5],
        "reservations": []
    },
    "14": {
        "name": "Nasi Krawu Bu Tini",
        "description": "Nasi krawu dengan daging empal dan serundeng.",
        "location": "Jl. Merdeka No.10, Jombang",
        "city": "Jombang",
        "image": "nasi_krawu_bu_tini.jpg",
        "contact": "0812-5432-1098",
        "website": "http://www.nasikrawubutini.com",
        "opening_hours": {
            "Monday": "08:00 AM - 08:00 PM",
            "Tuesday": "08:00 AM - 08:00 PM",
            "Wednesday": "08:00 AM - 08:00 PM",
            "Thursday": "08:00 AM - 08:00 PM",
            "Friday": "08:00 AM - 09:00 PM",
            "Saturday": "08:00 AM - 09:00 PM",
            "Sunday": "08:00 AM - 08:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r14",
                "name": "Nina",
                "review": "Nasi krawunya enak banget, daging empalnya empuk!",
                "photo": "review14.jpg",
                "date": "30 March 2024"
            }
        ],
        "ratings": [5, 5, 4, 4],
        "reservations": []
    },
    "15": {
        "name": "Sate Ayam Ponorogo",
        "description": "Sate ayam dengan bumbu kacang yang khas.",
        "location": "Jl. KH. Ahmad Dahlan No.50, Jombang",
        "city": "Ponorogo",
        "image": "sate_ayam_ponorogo.jpg",
        "contact": "0812-6789-4321",
        "website": "http://www.sateayampionorogo.com",
        "opening_hours": {
            "Monday": "10:00 AM - 10:00 PM",
            "Tuesday": "10:00 AM - 10:00 PM",
            "Wednesday": "10:00 AM - 10:00 PM",
            "Thursday": "10:00 AM - 10:00 PM",
            "Friday": "10:00 AM - 11:00 PM",
            "Saturday": "10:00 AM - 11:00 PM",
            "Sunday": "10:00 AM - 10:00 PM"
        },
        "customerReviews": [
            {
                "review_id": "r15",
                "name": "Oka",
                "review": "Sate ayamnya empuk dan bumbu kacangnya enak banget!",
                "photo": "review15.jpg",
                "date": "05 April 2024"
            }
        ],
        "ratings": [5, 5, 5, 4],
        "reservations": []
    }
}

menus = {
    "1": [
        {"item": "Sate Kambing", "description": "Sate kambing yang lezat dengan bumbu kacang.", "price": "20.000"},
        {"item": "Sate Ayam", "description": "Sate ayam dengan bumbu kacang.", "price": "15.000"},
        {"item": "Gule Kambing", "description": "Gule kambing dengan kuah gurih.", "price": "25.000"},
        {"item": "Sop Kambing", "description": "Sop kambing yang segar.", "price": "22.000"},
        {"item": "Teh Manis", "description": "Teh manis hangat.", "price": "5.000"}
    ],
    "2": [
        {"item": "Bakso Urat", "description": "Bakso urat yang nikmat.", "price": "18.000"},
        {"item": "Bakso Telor", "description": "Bakso dengan isian telor.", "price": "20.000"},
        {"item": "Bakso Campur", "description": "Bakso campur dengan berbagai isian.", "price": "22.000"},
        {"item": "Mie Bakso", "description": "Mie dengan bakso.", "price": "15.000"},
        {"item": "Es Teh", "description": "Es teh segar.", "price": "5.000"}
    ],
    "3": [
        {"item": "Soto Ayam", "description": "Soto ayam dengan kuah bening.", "price": "15.000"},
        {"item": "Soto Daging", "description": "Soto daging dengan kuah bening.", "price": "20.000"},
        {"item": "Soto Babat", "description": "Soto babat dengan kuah bening.", "price": "18.000"},
        {"item": "Soto Campur", "description": "Soto campur dengan berbagai isian.", "price": "22.000"},
        {"item": "Teh Poci", "description": "Teh poci hangat.", "price": "7.000"}
    ],
    "4": [
        {"item": "Ayam Goreng", "description": "Ayam goreng renyah.", "price": "18.000"},
        {"item": "Ayam Bakar", "description": "Ayam bakar dengan bumbu kecap.", "price": "20.000"},
        {"item": "Sambal Terasi", "description": "Sambal terasi spesial.", "price": "5.000"},
        {"item": "Lalapan", "description": "Lalapan segar.", "price": "8.000"},
        {"item": "Es Jeruk", "description": "Es jeruk segar.", "price": "7.000"}
    ],
    "5": [
        {"item": "Nasi Pecel", "description": "Nasi pecel dengan bumbu kacang.", "price": "10.000"},
        {"item": "Lontong Pecel", "description": "Lontong pecel dengan bumbu kacang.", "price": "12.000"},
        {"item": "Nasi Campur", "description": "Nasi campur dengan berbagai lauk.", "price": "15.000"},
        {"item": "Tahu Tempe", "description": "Tahu tempe goreng.", "price": "8.000"},
        {"item": "Es Dawet", "description": "Es dawet segar.", "price": "7.000"}
    ],
    "6": [
        {"item": "Rujak Cingur", "description": "Rujak cingur dengan bumbu petis.", "price": "15.000"},
        {"item": "Rujak Manis", "description": "Rujak manis segar.", "price": "12.000"},
        {"item": "Rujak Buah", "description": "Rujak buah segar.", "price": "10.000"},
        {"item": "Es Campur", "description": "Es campur dengan berbagai isian.", "price": "10.000"},
        {"item": "Es Teller", "description": "Es teller segar.", "price": "12.000"}
    ],
    "7": [
        {"item": "Nasi Tumpang", "description": "Nasi tumpang dengan tempe bosok.", "price": "12.000"},
        {"item": "Sayur Lodeh", "description": "Sayur lodeh segar.", "price": "10.000"},
        {"item": "Tempe Goreng", "description": "Tempe goreng renyah.", "price": "5.000"},
        {"item": "Peyek Kacang", "description": "Peyek kacang gurih.", "price": "7.000"},
        {"item": "Es Teh", "description": "Es teh segar.", "price": "5.000"}
    ],
    "8": [
        {"item": "Bebek Goreng", "description": "Bebek goreng empuk.", "price": "22.000"},
        {"item": "Bebek Bakar", "description": "Bebek bakar dengan bumbu kecap.", "price": "25.000"},
        {"item": "Sambal Korek", "description": "Sambal korek pedas.", "price": "5.000"},
        {"item": "Lalapan", "description": "Lalapan segar.", "price": "8.000"},
        {"item": "Es Teh", "description": "Es teh segar.", "price": "5.000"}
    ],
    "9": [
        {"item": "Mie Ayam", "description": "Mie ayam dengan pangsit goreng.", "price": "15.000"},
        {"item": "Mie Ayam Bakso", "description": "Mie ayam dengan bakso.", "price": "18.000"},
        {"item": "Mie Ayam Ceker", "description": "Mie ayam dengan ceker ayam.", "price": "17.000"},
        {"item": "Pangsit Goreng", "description": "Pangsit goreng renyah.", "price": "5.000"},
        {"item": "Es Teh", "description": "Es teh segar.", "price": "5.000"}
    ],
    "10": [
        {"item": "Es Degan", "description": "Es degan segar.", "price": "10.000"},
        {"item": "Es Degan Gula Jawa", "description": "Es degan dengan gula jawa.", "price": "12.000"},
        {"item": "Es Degan Jeruk", "description": "Es degan dengan perasan jeruk.", "price": "15.000"},
        {"item": "Teh Manis", "description": "Teh manis hangat.", "price": "5.000"},
        {"item": "Teh Tawar", "description": "Teh tawar hangat.", "price": "3.000"}
    ],
    "11": [
        {"item": "Rawon", "description": "Rawon dengan daging empuk.", "price": "20.000"},
        {"item": "Rawon Setan", "description": "Rawon setan dengan kuah kental.", "price": "25.000"},
        {"item": "Empal", "description": "Empal daging sapi.", "price": "22.000"},
        {"item": "Kerupuk", "description": "Kerupuk renyah.", "price": "5.000"},
        {"item": "Es Teh", "description": "Es teh segar.", "price": "5.000"}
    ],
    "12": [
        {"item": "Lontong Balap", "description": "Lontong balap dengan lentho.", "price": "12.000"},
        {"item": "Lontong Mie", "description": "Lontong mie dengan sayur.", "price": "15.000"},
        {"item": "Lentho", "description": "Lentho garing dan renyah.", "price": "7.000"},
        {"item": "Sambal Petis", "description": "Sambal petis khas.", "price": "5.000"},
        {"item": "Es Teh", "description": "Es teh segar.", "price": "5.000"}
    ],
    "13": [
        {"item": "Bakmi Jowo", "description": "Bakmi jowo dengan rasa gurih.", "price": "15.000"},
        {"item": "Bakmi Godog", "description": "Bakmi godog dengan kuah kaldu.", "price": "17.000"},
        {"item": "Bakmi Goreng", "description": "Bakmi goreng dengan bumbu spesial.", "price": "18.000"},
        {"item": "Nasi Goreng", "description": "Nasi goreng spesial.", "price": "20.000"},
        {"item": "Es Teh", "description": "Es teh segar.", "price": "5.000"}
    ],
    "14": [
        {"item": "Nasi Krawu", "description": "Nasi krawu dengan daging empal.", "price": "20.000"},
        {"item": "Empal", "description": "Empal daging sapi.", "price": "22.000"},
        {"item": "Serundeng", "description": "Serundeng gurih.", "price": "5.000"},
        {"item": "Lalapan", "description": "Lalapan segar.", "price": "8.000"},
        {"item": "Es Teh", "description": "Es teh segar.", "price": "5.000"}
    ],
    "15": [
        {"item": "Sate Ayam", "description": "Sate ayam dengan bumbu kacang.", "price": "15.000"},
        {"item": "Sate Kambing", "description": "Sate kambing dengan bumbu kecap.", "price": "20.000"},
        {"item": "Lontong", "description": "Lontong empuk.", "price": "5.000"},
        {"item": "Kerupuk", "description": "Kerupuk renyah.", "price": "5.000"},
        {"item": "Es Teh", "description": "Es teh segar.", "price": "5.000"}
    ]
}
