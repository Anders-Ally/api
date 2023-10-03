import requests

def get_public_ip_address():
    api_url = "https://ip-api.com"

    try: 
        ipv4_address = requests.get(api_url)
        ipv4_info = ipv4_address.json()

        ipv6_address = requests.get(f"{api_url}?fields=query, v6")
        ipv6_info = ipv6_address.json()

        
        print("---------------------------------------------------")
        print("IPv4 Informaiton Below: ")
        print("IPv4 Address: ", ipv4_info["query"])
        print("IPv4 Country: ", ipv4_info["country"])
        print("IPv4 Region: ", ipv4_info["region"])
        print("IPv4 City: ", ipv4_info["city"])
        print("IPv4 ISP: ", ipv4_info["isp"])
        print("IPv4 ORG: ", ipv4_info["org"])
        print("IPv4 ASN: ", ipv4_info["as"])

        print("---------------------------------------------------")
        print("IPv6 Informaiton Below: ")
        print("IPv6 Address: ", ipv6_info["query"])
        print("IPv6 Country: ", ipv6_info["country"])
        print("IPv6 Region: ", ipv6_info["region"])
        print("IPv6 City: ", ipv6_info["city"])
        print("IPv6 ISP: ", ipv6_info["isp"])
        print("IPv6 ORG: ", ipv6_info["org"])
        print("IPv6 ASN: ", ipv6_info["as"])
        print("---------------------------------------------------")

  
