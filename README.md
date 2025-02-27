
This project connects to the **Ethereum blockchain** using **Infura** and fetches real-time blockchain data like the **latest block number** and **gas price**.

## 📌 Features
- ✅ Connects to an **Ethereum Node** using Infura
- ✅ Retrieves **latest block number**
- ✅ Fetches **current gas price** in Gwei
## Setup Instructions  
1️⃣ Clone the repository:  
```bash  
git clone https://github.com/anas666/fetch-eth-data.git  
cd fetch-eth-data
```
2️⃣ Install dependencies:

`pip install web3`

3️⃣ Set up Infura: Go to Infura, sign up, create an Ethereum project, and copy your Infura `API Key`.
4️⃣ Add your Infura Key: Open fetch_eth_data.py and replace "YOUR_INFURA_PROJECT_ID" with your actual Infura API Key.
5️⃣ Run the script:

`python fetch_eth_data.py`

✅ Expected output:

![image](https://github.com/user-attachments/assets/9cd230a8-1437-446c-aaef-a82f06a408ce)

## Technologies Used
1. Python 🐍
2. Web3.py (Ethereum SDK)
3. Infura (Ethereum Node Provider)
