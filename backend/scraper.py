import httpx
import json
import base64

ctgs = [
    "despensa",
    "lacteos-y-huevos",
    "frutas-y-verduras",
    "bebidas-y-jugos",
    "carnes-pescados-y-mariscos",
    "salchichoneria",
    "cocina-pronto",
    "gourmet",
    "cerveza-vinos-y-licores",
    "alimentos-congelados",
    "limpieza-y-hogar",
    "bebes-y-maternidad",
    "farmacia",
    "cuidado-personal-y-belleza",
    "mascotas",
    "ferreteria-y-automotriz",
]


def get_ctg_products(category):
    payload = {
        "hideUnavailableItems": True,
        "skusFilter": "FIRST_AVAILABLE",
        "installmentCriteria": "MAX_WITHOUT_INTEREST",
        "category": category,
        "specificationFilters": [],
        "orderBy": "",
        "from": 0,
        "to": 99,
        "shippingOptions": [],
        "variant": "",
    }
    productCount = 0
    with httpx.Client() as client:
        while True:
            base64data = base64.b64encode(json.dumps(payload).encode("utf-8"))
            print(f"Base64: {base64data}")
            url = f'https://tienda.calimax.com.mx/_v/segment/graphql/v1?workspace=master&maxAge=short&appsEtag=remove&domain=store&locale=es-MX&operationName=Products&variables={{}}&extensions={{"persistedQuery":{{"version":1,"sha256Hash":"4877b29940906d57e924950723efc7ec8c81c57eb7a4c21648153fb257066ce3","sender":"vtex.store-resources@0.x","provider":"vtex.search-graphql@0.x"}},"variables":"{base64data}"}}'
            response = client.get(
                url,
                headers={
                    "accept": "*/*",
                    "content-type": "application/json",
                    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"macOS"',
                },
            )
            j = response.json()
            print(f"response {j}")
            products = j["data"]["products"]
            payload["from"] += 100
            payload["to"] += 100

            if len(products) == 0:
                break
            productCount += len(products)

    print(productCount)
    return productCount


for category in ctgs:
    count = get_ctg_products(category)
    print(category, count)
