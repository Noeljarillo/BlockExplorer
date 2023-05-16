import requests
import json

block_hashes = ["0xfb2afa8a9c6f2f53b348798884c8628becca1af4151b3e55cb16aedecf322d93", "0x1ad85adf0fe80538014b4b677e884b77edb5fdb73966c40b47aef4cde8e62354"]

tx_hashes = [
    "0x977b0f69a4d1f0209ca9c64e46a256e12142fb3802bacfb559106b7a31ba3c30",
    "0x5654fbd35ac0b419a9a98f934a61b3ce070b82267e0bbf8013fa79d67da31fb7",
    "0x77a53689a793fc194869f9877b06288b62b913fd4e05737da0009acc630e0de1",
]

for block_hash in block_hashes:
    response = requests.get(f"http://localhost:5000/block/{block_hash}")
    print(f"For block hash: {block_hash}")
    print("Response status code:", response.status_code)
    print("Response content:", json.dumps(response.json(), indent=4))

for tx_hash in tx_hashes:
    response = requests.get(f"http://localhost:5000/transaction/{tx_hash}")
    print(f"For transaction hash: {tx_hash}")
    print("Response status code:", response.status_code)
    print("Response content:", json.dumps(response.json(), indent=4))
