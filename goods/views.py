from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Каталог",
        "goods": [
            {
                "image": "deps/images/goods/krossovki-muzhskie-outventure-discovery.jpg",
                "name": "Кроссовки мужские Outventure Discovery",
                "description": "Легкие и удобные кроссовки Discovery mesh станут отличным выбором для несложных походов и увлекательных летних путешествий.",
                "price": 1999.00,
            },
            {
                "image": "deps/images/goods/krossovki-muzhskie-etonic-ashen.jpg",
                "name": "Кроссовки мужские Etonic Ashen",
                "description": "Кроссовки от Etonic в узнаваемом ретродизайне идеально впишутся в ваш повседневный гардероб.",
                "price": 1999.00,
            },
            {
                "image": "deps/images/goods/kedy-muzhskie-puma-caven-20.jpg",
                "name": "Кеды мужские PUMA Caven 2.0",
                "description": "Кеды Caven 2.0 — это утонченный вариант классического баскетбольного дизайна 80-х. Отличный вариант для спортивного образа в духе ретро.",
                "price": 4899.00,
            },
            {
                "image": "deps/images/goods/kedy-muzhskie-adidas-grand-court-alpha-00-s.jpg",
                "name": "Кеды мужские adidas Grand Court Alpha 00 S",
                "description": "Иногда классика — лучший выбор. Кеды в теннисном стиле от adidas станут идеальной основой для комфортных образов на каждый день.",
                "price": 6999.00,
            },
            {
                "image": "deps/images/goods/krossovki-uteplennye-muzhskie-erke-jogging.jpg",
                "name": "Кроссовки утепленные мужские Erke Jogging",
                "description": "Утепленные кроссовки от Erke — оптимальный вариант для долгих и комфортных прогулок зимой.",
                "price": 6599.00,
            },
            {
                "image": "deps/images/goods/botinki-muzhskie-tecnica-magma-20-s-mid-gtx.jpg",
                "name": "Ботинки мужские Tecnica Magma 2.0 S Mid GTX",
                "description": "Высокотехнологичные ботинки Tecnica предназначены для скоростных спусков и подъемов в условиях пересеченной местности и в горах.",
                "price": 25999.00,
            },
            {
                "image": "deps/images/goods/polubotinki-muzhskie-columbia-crestwood.jpg",
                "name": "Полуботинки мужские Columbia Crestwood",
                "description": "Универсальные полуботинки Crestwood от Columbia разработаны специально для походов и активного отдыха на природе.",
                "price": 8999.00,
            },
            {
                "image": "deps/images/goods/polubotinki-uteplennye-muzhskie-etonic-moba.jpg",
                "name": "Полуботинки утепленные мужские Etonic Moba",
                "description": "Ботинки от Etonic станут отличным дополнением вашей походной экипировки. Смело отправляйтесь навстречу приключениям!",
                "price": 6599.00,
            },
            {
                "image": "deps/images/goods/sandalii-muzhskie-outventure-crete-3.jpg",
                "name": "Сандалии мужские Outventure Crete 3",
                "description": "Практичные сандалии на липучке от Outventure подойдут для летних походов и путешествий. Переиздание легендарной модели Crete в новом дизайне и с улучшенными характеристиками сцепления подошвы.",
                "price": 2799.00,
            },
            {
                "image": "deps/images/goods/sandalii-muzhskie-northland-wandern.jpg",
                "name": "Сандалии мужские Northland Wandern",
                "description": "Сандалии Northland — отличный вариант для прогулок и путешествий в теплое время года.",
                "price": 3919.00,
            },
        ],
    }

    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
